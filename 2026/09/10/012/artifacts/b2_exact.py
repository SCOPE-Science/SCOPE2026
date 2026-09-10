"""Lane-515: exact finite-type B2 transverse-slice certificate (integer arithmetic only).
B12=[[0,2],[-1,0]] (|bc|=2 -> finite type B2). Verify:
 (a) mutation cycle closes with period 6 at (B,C) level exactly;
 (b) complete list of c-vectors (= wall normals up to sign) on the cycle;
 (c) q>0 on every slice normal (real-root side);
 (d) rank-3 imaginary-side vectors all have n3 != 0 (closed-form + box scan).
"""
import json

def mutB(B,k):
    m=len(B); Bp=[[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if i==k or j==k: Bp[i][j]=-B[i][j]
            else: Bp[i][j]=B[i][j]+(abs(B[i][k])*B[k][j]+B[i][k]*abs(B[k][j]))//2
    return Bp
def mutC(C,B,k):
    # COLUMNS = c-vectors (validated against the analytic B2 root system).
    m=len(C); Cp=[row[:] for row in C]
    for i in range(m): Cp[i][k]=-C[i][k]
    for j in range(m):
        if j==k: continue
        for i in range(m):
            Cp[i][j]=C[i][j]+max(0,C[i][k])*max(0,B[k][j])-max(0,-C[i][k])*max(0,-B[k][j])
    return Cp

B=[[0,2],[-1,0]]; C=[[1,0],[0,1]]
seq=[0,1,0,1,0,1]
traj=[(tuple(map(tuple,B)),tuple(map(tuple,C)))]
for t,k in enumerate(seq):
    Cn=mutC(C,B,k); Bn=mutB(B,k); B,C=Bn,Cn
    traj.append((tuple(map(tuple,B)),tuple(map(tuple,C))))
    print("t=%d mut=%d B=%s C=%s" % (t+1,k,B,C))
cvecs=set()
closed = (traj[-1]==traj[0])
print("period-6 closure (B,C back to seed0):",closed)
assert closed, "B2 cycle did not close"
for (Bt,Ct) in traj:
    for j in range(2): cvecs.add(tuple(Ct[r][j] for r in range(2)))
print("distinct c-vectors on cycle:",sorted(cvecs))
# sign coherence audit on every visited seed
for (Bt,Ct) in traj:
    for j in range(2):
        col=[Ct[r][j] for r in range(2)]
        assert not any(v>0 for v in col) or not any(v<0 for v in col)
print("PASS sign coherence on all 7 (6+1) visited seeds")
def q2(v): return (v[0]-v[1])**2+v[1]**2
print("q on c-vectors:",{v:q2(v) for v in sorted(cvecs)})
assert all(q2(v)>0 for v in cvecs)
print("PASS all B2 wall normals real-root side (q>=1)")
# rank-3 form
S=[[2,-2,-1],[-2,4,-2],[-1,-2,2]]
def q3(v): return sum(S[i][j]*v[i]*v[j] for i in range(3) for j in range(3))/2
imag=[(a,b,c) for a in range(-3,4) for b in range(-3,4) for c in range(-3,4)
      if (a,b,c)!=(0,0,0) and q3((a,b,c))<=0]
print("rank-3 q<=0 vectors in box:",imag)
print("of which with n3=0:",[v for v in imag if v[2]==0])
assert not [v for v in imag if v[2]==0]
print("PASS obstruction: every rank-3 vector with n3=0 has q>=1 (closed form (a-b)^2+b^2)")
json.dump({"b2_cvecs":sorted(cvecs),"period6":closed,
           "imag_box":[list(v) for v in imag]},
          open("output/artifacts/b2_slice.json","w"),indent=1)
print("wrote output/artifacts/b2_slice.json")
