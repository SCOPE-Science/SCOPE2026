import math

def pt(n,j):
    a=2*math.pi*j/n
    return (math.cos(a),math.sin(a))

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(t,a): return (t*a[0],t*a[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def norm(a): return math.hypot(a[0],a[1])

for n in range(3,102,2):
    m=(n-1)//2
    V=[pt(n,j) for j in range(n)]
    C=[mul(.5,add(V[j],V[(j+m+1)%n])) for j in range(n)]
    target=math.sin(math.pi/(2*n))
    assert max(abs(norm(c)-target) for c in C)<2e-12
    for j in range(n):
        endpoint=mul(.5,add(V[(j+1)%n],V[(j+m+1)%n]))
        assert norm(sub(endpoint,C[(j+m+1)%n]))<2e-12
        assert norm(sub(mul(.5,add(V[j],V[(j+m+1)%n])),C[j]))<2e-12

print('VERIFY_OK')
