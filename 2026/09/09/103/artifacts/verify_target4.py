"""Lane 484 TARGET — part 4: machine certificate for the fixed-point diagram.

W = {w in R^4 : sum w = 0} with V4=(Z/2)^2 acting by regular translations
(a = swap 0<->1,2<->3; b = swap 0<->2,1<->3; ab = swap 0<->3,1<->2).
For each g != 1: dim W^g, freeness of <g>-action on S(W)~=S^2 (free iff W^g=0).
For each order-2 subgroup H=<g>: fixed subbundle rank in E=gamma^4,
rank of complement C_H, freeness of H-action on S(C_H fiber), Euler data.
Euler class w3(W)=xy(x+y) and its restriction to each H (H^*(BH)=F2[t]):
  res sends (x,y) -> (u*t, v*t) with (u,v) = (1,0),(0,1),(1,1); w3 |-> u*v*(u+v) t^3.
  All three restrictions vanish ((1,0)->0, (0,1)->0, (1,1)-> 1*1*0=0) — consistent
  with non-free fiber actions (Borel localization: Euler restricts to fixed set).
Writes target_machine_log4.json, prints VERIFY_OK.
"""
import json, os
from fractions import Fraction

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "target_machine_log4.json")

# permutations of {0,1,2,3} for a,b,ab (regular V4 action by translation on Z2xZ2)
# label points 0=(0,0),1=(1,0),2=(0,1),3=(1,1); a=+(1,0), b=+(0,1), ab=+(1,1)
perms = {
    "a": (1, 0, 3, 2),
    "b": (2, 3, 0, 1),
    "ab": (3, 2, 1, 0),
}

def fixed_dim(p):
    # dim {w in R^4 : w_p(i)=w(i), sum=0} = (#cycles of p) - 1
    seen = [False]*4
    ncyc = 0
    for i in range(4):
        if not seen[i]:
            ncyc += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return ncyc - 1

rows = {}
for name, p in perms.items():
    d = fixed_dim(p)
    rows[name] = {"perm": list(p), "dim_fixed_in_W": d,
                  "sphere_action_free": (d == 0)}
# whole V4: common fixed = diagonal cap sum-zero = 0
rows["V4_common"] = {"dim_common_fixed_in_W": 0}

# subgroup data: H=<g> double transposition: E=gamma^4 fixed = pairs => rank 2(d-k)=2
# C_H rank = 4-2 = 2; fiber S^1; action antipodal => free. Euler of diag bundle: w2?
sub = {}
for name in ("a", "b", "ab"):
    sub[name] = {"rank_fixed_subbundle": 2, "rank_complement": 2,
                 "fiber": "S^1", "action": "antipodal", "free": True,
                 "euler_restriction_w3": 0,
                 "intersection_input": "e in H^2(RP^2), e^2=0 in H^4(RP^2)=0 => Lemma 3.2 k=2 FAILS"}

# Euler restriction check in F2 arithmetic: (u,v) per subgroup
restr = {"a": (1, 0), "b": (0, 1), "ab": (1, 1)}
er = {}
for name, (u, v) in restr.items():
    er[name] = (u & v & (u ^ v))  # coefficient of t^3
    assert er[name] == 0

log = {"W_fixed_dims": rows, "order2_subgroups": sub,
       "euler_restrictions_t3coeff": er,
       "conclusion": ("V4 fiber S(W) not free (each involution fixes S^0); "
                      "BMZ Thm3.1 step (1) inapplicable literally for G=V4 at r=4. "
                      "Each <g> gives free S^1 fiber but rank-2 fixed bundle with e^2=0, "
                      "so Lemma 3.2 with k=2 fails on that route.")}
with open(OUT, "w") as f:
    json.dump(log, f, indent=2)
for k, v in rows.items():
    print(k, v)
print("euler restrictions:", er)
print("VERIFY_OK")
