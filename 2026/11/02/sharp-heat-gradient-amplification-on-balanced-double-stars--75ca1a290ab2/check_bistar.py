"""Reproduce finite tests for the exact heat-gradient norm on balanced double stars.

Only Python's standard library is needed. Finite tests support, but do not replace,
the unrestricted ODE and positivity proof given in RESULT.md.
"""
import math
from fractions import Fraction


def coefficients(m, t):
    delta = math.sqrt((m + 3)**2 - 8)
    alpha, beta = ((m + 3) - delta)/2, ((m + 3) + delta)/2
    slow, fast = math.exp(-alpha*t), math.exp(-beta*t)
    b = (slow-fast)/delta
    a = ((beta-2)*slow+(2-alpha)*fast)/delta
    u = ((beta-m-1)*slow+(m+1-alpha)*fast)/delta
    h = math.exp(-(m+1)*t)
    x = math.exp(-t)
    center = a+2*m*b
    leaf = u+b+(m-1)/m*max(0,2*x-h-u)
    peak = 0 if m == 1 else math.log(beta*(alpha+2*m-2)/(alpha*(beta+2*m-2)))/delta
    return center,leaf,peak,b,a,u,h


def graph(m):
    hub_a,hub_b=m,m+1
    al=list(range(m))
    bl=list(range(m+2,2*m+2))
    n=2*m+2
    edges=[(hub_a,hub_b)]+[(hub_a,i) for i in al]+[(hub_b,i) for i in bl]
    neighbors=[[] for _ in range(n)]
    for a,b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    return hub_a,hub_b,al,bl,neighbors


def row_heat_uniformization(neighbors,x,t):
    n=len(neighbors)
    rate=max(len(s) for s in neighbors)
    mu=rate*t
    row=[0.0]*n
    row[x]=1.0
    w=math.exp(-mu)
    output=[w*r for r in row]
    cumulative=w
    k=0
    while k < 2000:
        k+=1
        nextrow=[0.0]*n
        for i,value in enumerate(row):
            if not value: continue
            nextrow[i]+=value*(1-len(neighbors[i])/rate)
            for j in neighbors[i]: nextrow[j]+=value/rate
        row=nextrow
        w=w*mu/k
        for i in range(n): output[i]+=w*row[i]
        cumulative+=w
        if k>mu and (1-cumulative)<3e-15:break
    assert k<2000
    assert abs(sum(output)-1)<2e-12
    return output


def tree_W1(diff,al,bl,hub_b):
    # Tree-cut formula: leaf edges contribute absolute leaf mass,
    # and central edge contributes the signed mass on one hub-side.
    return sum(abs(diff[i]) for i in al+bl)+abs(sum(diff[i] for i in bl)+diff[hub_b])


def series_check(m,order=8):
    # Derivative generator on the 2m+1 independently variable gradients.
    n=2*m+1;c=2*m
    T=[[0]*n for _ in range(n)]
    for i in range(m):
        for j in range(m):T[i][j]-=1
        T[i][i]-=1
        T[i][c]=1
    for i in range(m,2*m):
        for j in range(m,2*m):T[i][j]-=1
        T[i][i]-=1
        T[i][c]=-1
    for j in range(m):T[c][j]=1
    for j in range(m,2*m):T[c][j]=-1
    T[c][c]=-2
    # Reduced generator for (D,c), where D=sum(g)-sum(h).
    Q=[[-(m+1),2*m],[1,-2]]
    rows=[]
    for z in [c,0]:
        p=[0]*n;p[z]=1
        rows.append([])
        for k in range(order+1):
            rows[-1].append(p[:])
            p=[sum(p[i]*T[i][j] for i in range(n)) for j in range(n)]
    q00,q01=[1,0],[0,1]
    reduced=[]
    for k in range(order+1):
        reduced.append((q00[:],q01[:]))
        q00=[sum(q00[i]*Q[i][j] for i in range(2)) for j in range(2)]
        q01=[sum(q01[i]*Q[i][j] for i in range(2)) for j in range(2)]
    # Check center row against b for both side leaf gradients and a for center.
    # Note that Q is used as column evolution, so b=[exp(tQ)]_{1,0}.
    for k in range(order+1):
        A=reduced[k][0][1]  # row zero of Q^k, col one: 2m*b
        B=reduced[k][1][0]  # row one of Q^k, col zero: b
        C=reduced[k][1][1]  # a
        center=rows[0][k]
        assert center[:m]==[B]*m
        assert center[m:2*m]==[-B]*m
        assert center[c]==C
        # Leaf gradient row decomposition (symmetric + antisymmetric modes).
        U=reduced[k][0][0]
        H=(-m-1)**k
        X=(-1)**k
        cG=Fraction(-2*X+H+U,2*m)
        cH=Fraction(H-U,2*m)
        actual=rows[1][k]
        for i in range(m):assert Fraction(actual[i])==Fraction(X if i==0 else 0)+cG
        for i in range(m,2*m):assert Fraction(actual[i])==cH
        assert actual[c]==B


def run():
    tests=0
    for m in [1,2,3,4,5,7,10,15,25]:
        series_check(m)
        hub_a,hub_b,al,bl,neighbors=graph(m)
        for t in [0,.0001,.002,.04,.15,.4,.8,1.5,3.0]:
            row_a=row_heat_uniformization(neighbors,hub_a,t)
            row_b=row_heat_uniformization(neighbors,hub_b,t)
            row_l=row_heat_uniformization(neighbors,0,t)
            wc=tree_W1([a-b for a,b in zip(row_a,row_b)],al,bl,hub_b)
            wl=tree_W1([a-b for a,b in zip(row_a,row_l)],al,bl,hub_b)
            center,leaf,peak,b,a,u,h=coefficients(m,t)
            assert abs(wc-center)<3e-11, (m,t,wc,center)
            assert abs(wl-leaf)<3e-11, (m,t,wl,leaf)
            assert wc+1e-12>=wl,(m,t,wc,wl)
            if t>0:assert center>leaf
            tests+=1
        _,_,peak,_,_,_,_=coefficients(m,0)
        if m>1:
            lo=coefficients(m,peak*.95)[0]
            hi=coefficients(m,peak*1.05)[0]
            top=coefficients(m,peak)[0]
            assert top>lo and top>hi and top>1
    print('CHECK_OK exact_taylor_orders=9 m_values=9 heat_row_transport_cases='+str(tests)+' checked_graph_families=balanced_double_stars')


if __name__=='__main__':run()
