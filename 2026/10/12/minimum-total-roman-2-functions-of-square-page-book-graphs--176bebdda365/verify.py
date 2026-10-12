from itertools import product

def book_graph(m):
    n = 2 + 2*m
    adj = [set() for _ in range(n)]
    def add(u,v):
        adj[u].add(v); adj[v].add(u)
    x,y=0,1
    add(x,y)
    for i in range(m):
        u=2+2*i; v=u+1
        add(x,u); add(u,v); add(v,y)
    return adj

def is_tr2df(adj, lab):
    positive={v for v,a in enumerate(lab) if a>0}
    if any(len(adj[v] & positive)==0 for v in positive):
        return False
    for v,a in enumerate(lab):
        if a==0 and sum(lab[u] for u in adj[v])<2:
            return False
    return True

def vectors_exact(length,total,max_value=2):
    vec=[0]*length
    def rec(i,rem):
        if i==length:
            if rem==0: yield tuple(vec)
            return
        for a in range(min(max_value,rem)+1):
            vec[i]=a
            yield from rec(i+1,rem-a)
    yield from rec(0,total)

def expected(m):
    n=2+2*m
    if m==1:
        out=[]
        for z in range(n):
            lab=[1]*n; lab[z]=0; out.append(tuple(lab))
        return 3,set(out)
    if m==2:
        out=set()
        lab=[0]*n; lab[0]=lab[1]=2; out.add(tuple(lab))
        lab=[0]*n
        for i in range(2): lab[2+2*i]=lab[3+2*i]=1
        out.add(tuple(lab))
        for choices in product([0,1],repeat=2):
            lab=[0]*n; lab[0]=lab[1]=1
            for i,c in enumerate(choices): lab[2+2*i+c]=1
            out.add(tuple(lab))
        return 4,out
    lab=[0]*n; lab[0]=lab[1]=2
    return 4,{tuple(lab)}

print('VERIFY_OK')
checked=0
for m in range(1,13):
    adj=book_graph(m)
    target,exp=expected(m)
    below=[]; mins=[]
    for w in range(target+1):
        for lab in vectors_exact(len(adj),w):
            checked += 1
            if is_tr2df(adj,lab):
                (below if w<target else mins).append(lab)
    assert not below,(m,below[:3])
    assert set(mins)==exp,(m,len(mins),len(exp),set(mins)^exp)
    print(f'm={m}: gamma_tR2={target}, minimum_functions={len(mins)}')
print('bounded_labelings_checked =',checked)
print('all minimum functions matched the classification')
