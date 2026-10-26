"""Independent numerical checks for a hierarchical ecological-chain theorem.
Requires Python 3.10+ standard library only. This is NOT an infinite proof.
"""
from math import exp, isfinite


def integrate(f, initial, horizon, h):
    x = list(map(float, initial))
    steps = round(horizon / h)
    assert abs(steps*h - horizon) < 1.e-8
    for j in range(steps):
        k1 = f(x)
        k2 = f([a + h*b/2 for a,b in zip(x,k1)])
        k3 = f([a + h*b/2 for a,b in zip(x,k2)])
        k4 = f([a + h*b for a,b in zip(x,k3)])
        x = [a + h*(b+2*c+2*d+e)/6 for a,b,c,d,e in zip(x,k1,k2,k3,k4)]
        if (j % 500 == 0):
            assert all(isfinite(v) for v in x)
    return x


def ecological_final(x0, r, d, pred):
    n=len(x0)
    assert len(pred)==n-1
    def f(x):
        g=r*(1-sum(x))-d
        return [x[i]*(g - (pred[i-1]*x[i-1] if i else 0)) for i in range(n)]
    return integrate(f,x0,1200.,0.06)


def triangular_final(x0,pred):
    a=[x/x0[0] for x in x0]
    q=[p/pred[0] for p in pred]
    def f(y):
        return [0.] + [-q[i-1]*y[i-1]*y[i] for i in range(1,len(y))]
    result=integrate(f,a,160.,0.04)
    return [x/sum(result) for x in result]


def within(x,y,eps,description):
    gap=max(abs(a-b) for a,b in zip(x,y))
    assert gap<eps, (description, gap, x, y)


def run():
    checks=0
    triples=[([.21,.19,.11],[.3,.7]),([.06,.25,.16],[.3,.7]),
             ([.21,.19,.11],[2.,2.]),([.06,.25,.16],[2.,2.])]
    for x0,p in triples:
        a2=x0[1]/x0[0]
        a3=x0[2]/x0[0]
        u=a3*exp(-p[1]/p[0]*a2)
        prediction=[1/(1+u),0.,u/(1+u)]
        within(triangular_final(x0,p),prediction,4.e-7,'three-species reduction')
        checks+=1
        for r,d in [(1.,.25),(1.7,.1)]:
            v=ecological_final(x0,r,d,p)
            within([a/sum(v) for a in v],prediction,4.e-7,'three-species physical flow')
            assert abs(sum(v)-(1-d/r))<4.e-7
            checks+=1
    x0=[.17,.11,.07,.12,.08]
    p=[.7,.4,.9,.6]
    reference=triangular_final(x0,p)
    assert min(reference[::2])>1.e-4
    assert max(abs(x) for x in reference[1::2])<1.e-8
    for scale in [.5,2.,5.]:
        scaled=[scale*x for x in p]
        within(triangular_final(x0,scaled),reference,1.e-9,'predation-scale invariance')
        checks+=1
        for r,d in [(1.,.3),(2.,.9)]:
            v=ecological_final(x0,r,d,scaled)
            within([a/sum(v) for a in v],reference,4.e-7,'five-species physical flow')
            assert abs(sum(v)-(1-d/r))<4.e-7
            checks+=1
    # Without predation, all species retain their initial relative weights.
    pzero=[0.]*4
    no_pred=ecological_final(x0,1.,.3,pzero)
    within([a/sum(no_pred) for a in no_pred], [a/sum(x0) for a in x0],4.e-7,'zero-predation boundary')
    assert no_pred[1] > .01 and no_pred[3] > .01
    checks+=1
    print('PASS:',checks,'separate numerical comparisons; three-species exact formula;')
    print('five-species parameter-scale universality; singular zero-predation test.')
    print('Five-species predicted composition:', [round(z,9) for z in reference])
    print('Warning: finite integration is not a proof for arbitrary n or all parameters.')

if __name__ == '__main__':
    run()
