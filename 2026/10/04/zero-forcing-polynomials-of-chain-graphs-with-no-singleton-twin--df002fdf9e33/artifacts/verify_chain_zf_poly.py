from itertools import product


def build_graph(alphas, betas):
    vertices=[]
    for i,a in enumerate(alphas):
        for k in range(a): vertices.append(('A',i,k))
    for j,b in enumerate(betas):
        for k in range(b): vertices.append(('B',j,k))
    idx={v:i for i,v in enumerate(vertices)}
    adj=[set() for _ in vertices]
    for i,a in enumerate(alphas):
        for k in range(a):
            u=idx[('A',i,k)]
            for j,b in enumerate(betas):
                if j<=i:
                    for l in range(b):
                        v=idx[('B',j,l)]
                        adj[u].add(v); adj[v].add(u)
    return vertices,adj


def is_zero_forcing(adj, mask):
    n=len(adj)
    blue={i for i in range(n) if (mask>>i)&1}
    while True:
        add=[]
        for u in tuple(blue):
            white=[v for v in adj[u] if v not in blue]
            if len(white)==1:
                add.append(white[0])
        old=len(blue)
        blue.update(add)
        if len(blue)==old:
            return len(blue)==n


def predicted(vertices, alphas, betas, mask):
    index={v:i for i,v in enumerate(vertices)}
    for side,sizes in (('A',alphas),('B',betas)):
        for i,c in enumerate(sizes):
            white=sum(1 for k in range(c) if not ((mask>>index[(side,i,k)])&1))
            if white>1:
                return False
    return True


def multiply(poly, factor):
    out=[0]*(len(poly)+1)
    c=factor
    for i,a in enumerate(poly):
        out[i]+=a*c
        out[i+1]+=a
    return out


def formula_counts(alphas,betas):
    p=len(alphas); n=sum(alphas)+sum(betas)
    poly=[1]
    for c in list(alphas)+list(betas):
        poly=multiply(poly,c) # product (x+c), ascending coefficients
    return [0]*(n-2*p)+poly


graphs=0; subsets=0
for p in range(1,4):
    for vals in product(range(2,5), repeat=2*p):
        if sum(vals)>12:
            continue
        alphas=vals[:p]; betas=vals[p:]
        vertices,adj=build_graph(alphas,betas)
        n=len(vertices)
        actual=[0]*(n+1)
        for mask in range(1<<n):
            a=is_zero_forcing(adj,mask)
            b=predicted(vertices,alphas,betas,mask)
            if a!=b:
                raise AssertionError((alphas,betas,mask,a,b))
            if a:
                actual[mask.bit_count()]+=1
        expected=formula_counts(alphas,betas)
        if actual!=expected:
            raise AssertionError((alphas,betas,actual,expected))
        graphs+=1; subsets+=(1<<n)

# Boundary test: singleton twin classes make the hypothesis genuinely necessary.
vertices,adj=build_graph((1,1),(1,1))
if predicted(vertices,(1,1),(1,1),0) is not True or is_zero_forcing(adj,0) is not False:
    raise AssertionError('boundary check failed')

print(f'VERIFY_OK graphs={graphs} subsets={subsets} max_order=12 boundary=P4')
