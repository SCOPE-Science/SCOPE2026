# Independent mathematical audit

## correctness

PASS

On the zero-sum space the SRG adjacency quadratic gives (kI-A)((h+1)I+A)=D I. If lambda=k-1, adjacent vertices have identical closed neighborhoods and connectedness would make the graph complete, so k-lambda-1>=1 and h>=2. For b=e_x-e_y the potential levels in units 1/D are h,1,0,-1,-h. The cuts at the outer levels contribute 2k(h-1), and each inner-side cut has k(k-lambda)-2(k-lambda-1)-2 times the internal wing edge count with the last term understood as minus twice that count. Summing gives M-2w_e. The diagonal 2h/D is strictly between zero and one, since D-2h=(k-2)h+mu>0. Complementing the diagonal subtracts 4h/D and adds one to each absolute column sum; symmetry gives equality of both endpoint norms for each projector. Orientation changes are signed coordinate conjugations. For (16,6,2,2) the rook wings are triangles and Shrikhande wings are paths, giving w=6 and 4 respectively, and the four asserted norms. Independent rational L+ calculation checked all 120 unordered vertex pairs and all 48 columns per graph, along with symmetry, idempotence and tr(Q)=15. Replay: /workspace/branches/365269cd-1892-4542-a823-9db8b5dff4ed/independent_srg_projection_check.py and independent_pair_check.txt in the same directory. Frozen supporting material was inspected, not run; the finite check is not the general proof.

## originality

PASS

The general SRG wing-edge law and the resulting canonical cospectral separation survive the comparisons. The rook-only canonical constants are exactly covered by a different same-day Hamming record and are credited here only as the known side of the witness. Neither priority between those records nor arbitrary minimum projection constants are asserted.

## value

PASS

The endpoint norms measure worst total absolute current for a unit edge injection (and the complementary cycle load). On a class with a three-eigenvalue adjacency algebra, the law reduces that norm exactly to one local subgraph statistic; a standard matched pair demonstrates that no function of the SRG spectrum alone suffices. This is useful beyond re-evaluating the known rook constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
