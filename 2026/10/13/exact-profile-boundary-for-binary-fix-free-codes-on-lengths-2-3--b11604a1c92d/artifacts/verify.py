from itertools import product
W={l:[format(i,f'0{l}b') for i in range(1<<l)] for l in (2,3,4)}
def cross(a,b):
    if len(a)>len(b): a,b=b,a
    return b.startswith(a) or b.endswith(a)
M={}
E={}
for m2 in range(1<<len(W[2])):
    c2=[W[2][i] for i in range(len(W[2])) if (m2>>i)&1]
    for m3 in range(1<<len(W[3])):
        c3=[W[3][i] for i in range(len(W[3])) if (m3>>i)&1]
        if any(cross(x,y) for x in c2 for y in c3): continue
        avail=[z for z in W[4] if not any(cross(x,z) for x in c2+c3)]
        key=(len(c2),len(c3))
        if len(avail)>M.get(key,-1): M[key]=len(avail); E[key]=(c2,c3,avail)
expected={
(0,0):16,(0,1):13,(0,2):10,(0,3):8,(0,4):6,(0,5):4,(0,6):2,(0,7):1,(0,8):0,
(1,0):9,(1,1):7,(1,2):6,(1,3):5,(1,4):4,(1,5):1,
(2,0):4,(2,1):3,(2,2):2,
(3,0):1,(3,1):0,(4,0):0}
assert M==expected,(M,expected)
# complete feasibility equivalence and first impossible Kraft layer
bad=[]
for a2 in range(5):
  for a3 in range(9):
    for a4 in range(17):
      if 4*a2+2*a3+a4<=16:
        feasible=(a2,a3) in M and a4<=M[(a2,a3)]
        if not feasible: bad.append((a2,a3,a4,4*a2+2*a3+a4))
assert min(x[3] for x in bad)==13
assert [x[:3] for x in bad if x[3]==13]==[(2,0,5)]
assert all(((a2,a3) in M and a4<=M[(a2,a3)]) for a2 in range(5) for a3 in range(9) for a4 in range(17) if 4*a2+2*a3+a4<=12)
print('VERIFY_OK')
print('max_a4_table',sorted((a2,a3,m) for (a2,a3),m in M.items()))
print('first_infeasible_scaled_kraft=13 profile=(2,0,5) Kraft=13/16')
print('all_scaled_kraft_at_most_12_feasible=True')
