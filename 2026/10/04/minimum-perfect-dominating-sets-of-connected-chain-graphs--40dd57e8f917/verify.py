from itertools import combinations

def comps(n,p):
    if p==1:
        yield (n,); return
    for cuts in combinations(range(1,n),p-1):
        z=(0,)+cuts+(n,)
        yield tuple(z[i+1]-z[i] for i in range(p))

def graph(alpha,beta):
    A=[];B=[]
    for i,a in enumerate(alpha,1):
        A += [('A',i,k) for k in range(a)]
    for j,b in enumerate(beta,1):
        B += [('B',j,k) for k in range(b)]
    V=A+B
    adj={v:set() for v in V}
    for a in A:
        for b in B:
            if b[1] <= a[1]:
                adj[a].add(b); adj[b].add(a)
    return V,adj,A,B

def perfect(D,V,adj):
    D=set(D)
    return all(sum(u in D for u in adj[v])==1 for v in V if v not in D)

def criterion(D,alpha,beta):
    D=set(D);p=len(alpha)
    x=[0]*p;y=[0]*p
    for t,i,k in D:
        (x if t=='A' else y)[i-1]+=1
    for i in range(p):
        if x[i] < alpha[i] and sum(y[:i+1]) != 1: return False
    for j in range(p):
        if y[j] < beta[j] and sum(x[j:]) != 1: return False
    return True

def prediction(alpha,beta):
    SA=sum(alpha);SB=sum(beta);p=len(alpha)
    if SA==1 and SB==1: return 1,2
    if SA==1: return 1,1
    if SB==1: return 1,1
    exc = int(p==2 and alpha[0]==1 and beta[1]==1)
    return 2, alpha[-1]*beta[0]+exc

profiles=subset_checks=perfect_sets=criterion_checks=minimum_checks=exception_profiles=0
max_order=10
for N in range(2,max_order+1):
  for SA in range(1,N):
    SB=N-SA
    for p in range(1,min(SA,SB)+1):
      for alpha in comps(SA,p):
       for beta in comps(SB,p):
        profiles+=1
        V,adj,A,B=graph(alpha,beta)
        good=[]
        for mask in range(1<<N):
            D=[V[k] for k in range(N) if mask>>k&1]
            p1=perfect(D,V,adj); p2=criterion(D,alpha,beta)
            subset_checks+=1; criterion_checks+=1
            if p1!=p2:
                raise AssertionError(('criterion',alpha,beta,D,p1,p2))
            if p1:
                good.append(D); perfect_sets+=1
        g=min(map(len,good)); c=sum(len(D)==g for D in good)
        gp,cp=prediction(alpha,beta)
        minimum_checks+=1
        if (g,c)!=(gp,cp):
            raise AssertionError(('minimum',alpha,beta,g,c,gp,cp,[D for D in good if len(D)==g]))
        if p==2 and alpha[0]==1 and beta[1]==1 and SA>=2 and SB>=2:
            exception_profiles += 1
print(f'VERIFY_OK profiles={profiles} subset_checks={subset_checks} perfect_sets={perfect_sets} criterion_checks={criterion_checks} minimum_checks={minimum_checks} exception_profiles={exception_profiles} max_order={max_order}')
