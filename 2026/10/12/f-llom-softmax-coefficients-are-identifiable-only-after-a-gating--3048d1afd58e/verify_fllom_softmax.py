import math

def softmax(gates, x):
    vals=[g[0]+sum(b*z for b,z in zip(g[1:],x)) for g in gates]
    c=max(vals)
    ev=[math.exp(v-c) for v in vals]
    s=sum(ev)
    return [v/s for v in ev]

def lomax_pdf(y, lam, gamma, delta, x):
    theta=math.exp(gamma+sum(d*z for d,z in zip(delta,x)))
    return theta*(lam**(lam+1))/((lam+theta*y)**(lam+1))

def mix_pdf(y,x,gates,components):
    w=softmax(gates,x)
    return sum(wi*lomax_pdf(y,*c,x) for wi,c in zip(w,components))

# Three distinct gates with intercept and two slopes.
gates=[(0.3,-0.5,0.8),(-0.7,1.1,-0.2),(1.2,0.4,0.6)]
u=(2.0,-0.9,1.7)
shifted=[tuple(a+b for a,b in zip(g,u)) for g in gates]
xs=[(-1.0,0.5),(0.0,0.0),(0.7,-1.3),(2.0,1.0)]
for x in xs:
    a=softmax(gates,x); b=softmax(shifted,x)
    assert max(abs(v-w) for v,w in zip(a,b)) < 1e-14

components=[(3.0,-0.2,(0.5,-0.1)),(1.7,0.4,(-0.2,0.3)),(5.0,-0.6,(0.1,0.7))]
for x in xs:
    for y in (0.1,1.0,4.0):
        assert abs(mix_pdf(y,x,gates,components)-mix_pdf(y,x,shifted,components)) < 1e-14

# The shifted coefficient set is not a label permutation of the original one.
assert set(gates).isdisjoint(set(shifted))

# Reference-normalized representation recovers exact log-odds coefficients.
base=gates[-1]
normalized=[tuple(a-b for a,b in zip(g,base)) for g in gates]
assert all(abs(v)<1e-15 for v in normalized[-1])
for x in xs:
    w=softmax(normalized,x)
    for m in range(2):
        lhs=math.log(w[m]/w[-1])
        rhs=normalized[m][0]+normalized[m][1]*x[0]+normalized[m][2]*x[1]
        assert abs(lhs-rhs)<1e-13

# Exact likelihood flatness along common shifts for arbitrary observations.
obs=[(0.4,(-1.0,0.5)),(1.2,(0.0,0.0)),(2.0,(0.7,-1.3))]
def ll(gs):
    return sum(math.log(mix_pdf(y,x,gs,components)) for y,x in obs)
assert abs(ll(gates)-ll(shifted))<1e-13

# Reconstruct Table 1 free-parameter counts from the published rounded values.
n=500
rows=[(1,-705.511,1429.665),(2,-649.926,1349.570),(3,-644.355,1369.500),(4,-643.597,1399.058)]
counts=[]
for M,loglik,bic in rows:
    p=(bic+2*loglik)/math.log(n)
    counts.append(p)
    assert abs(p-(3*M+2*(M-1)))<3e-4

print('VERIFY_OK')
print('max_softmax_shift_error',max(max(abs(a-b) for a,b in zip(softmax(gates,x),softmax(shifted,x))) for x in xs))
print('loglik_difference',ll(shifted)-ll(gates))
print('bic_inferred_counts',[round(v,6) for v in counts])
