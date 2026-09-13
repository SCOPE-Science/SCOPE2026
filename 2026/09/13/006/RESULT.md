# Fully general genus-0 triple Hurwitz census and recursion step (d=7)

## Context

Single Hurwitz numbers (one arbitrary profile plus simple points) and double Hurwitz
numbers (two arbitrary profiles plus simple points) have explicit formulas and
polynomiality theory. Hurwitz numbers with three arbitrary nonsimple profiles
(triple regime) are intrinsically harder and lack general closed formulas.
R. X.-F. Chen (arXiv:2308.08455) developed quasi-triple theory with explicit
formulas only in the one-part case (one profile equal to (d)) and Bai-Chen gave
explicit formulas in the two-part (2,d-2) case. An instance in which all three
profiles have at least three parts lies strictly outside both families and tests
the general theory. This record establishes the first exact census in that fully
general regime for a concrete degree-7 instance, with a verified cut-join step.

## Definitions and conventions

Fix degree d=7, genus g=0, ordered branch locus B={p1,p2,p3,p4} of four fixed
distinct points in P^1(C), with ramification profiles alpha=(4,2,1) at p1,
beta=(3,3,1) at p2, gamma=(2,2,2,1) at p3, tau=(2,1^5) (simple transposition)
at p4. Ramification deficits d-l(mu) are 4,4,3,1, total 12=2d-2, satisfying
Riemann-Hurwitz sum_p(d-l(mu_p))=2d-2+2g with g=0.

Permutations are written on {0,...,6} with compose(p,q)[i]=p[q[i]] (apply q
first). An ordered monodromy tuple (a,b,c,t) of respective cycle types
alpha,beta,gamma,tau satisfies t*c*b*a=id, i.e. t=(c*b*a)^{-1}. Hurwitz moves
and transitivity are computed in this convention; a mirror-convention rerun
gives identical counts, so the content is convention-independent.

The connected ordered B-pointwise Hurwitz number is H=sum_{[f]}1/|Aut(f)| over
isomorphism classes of connected genus-0 degree-7 covers with the ordered
ramification. By the monodromy correspondence (Riemann existence) with ordered
fixed branch locus, H=N_conn/7!, where N_conn is the number of transitive
tuples (a,b,c,t) in S7 of the four prescribed types with t*c*b*a=1. Each cover
with automorphism group Aut(f) contributes 7!/|Aut(f)| labeled tuples, hence
the division by 5040. N_all and N_disc denote all tuples and disconnected
tuples respectively.

## Result

Theorem. For the above data, N_all=153720, N_conn=120960, N_disc=32760, and
therefore H=120960/5040=24. The 192-per-fiber connected tuples form a single
pure-braid orbit (one Hurwitz component). Merging the last two branch points
via w=t*c, the one-step cut-join identity N_all=42840*2+7560*3+15120*3=153720
holds exactly, with fused w-types (4,2,1),(2,2,1,1,1),(3,2,2), class-constant
cut numbers 2,3,3, and connected/disconnected bookkeeping
192=96[(4,2,1),T->T]+24[(2,2,1,1,1),F->T]+72[(3,2,2),T->T] per fixed-a fiber
(40+12=52 disconnected remainder).

Non-containment: none of alpha,beta,gamma equals (7), so Chen one-part
dimension-reduction does not apply; none equals (2,5), so Bai-Chen (2,d-2)
formulas do not apply. All three profiles have >=3 parts: fully general triple
regime.

## Proof and evidence

Character count. For classes C1..C4 in finite group G, the number of tuples
with gi in Ci and g4*g3*g2*g1=1 is
N=(|C1||C2||C3||C4|/|G|)*sum_chi chi(g1)chi(g2)chi(g3)chi(g4)/chi(1)^2.
Class sizes: |C_alpha|=630, |C_beta|=280, |C_gamma|=105, |C_tau|=21.
Murnaghan-Nakayama from scratch (rim-hook enumeration, no character library)
gives dimensions [1,6,14,15,14,35,20,21,21,35,15,14,14,6,1], sum of squares
5040, hook-length agreement, full row and column orthogonality. Only four
irreps contribute nonzero terms chiA*chiB*chiC*chiT/dim^2: (7):+1,
(4,2,1):-1/245, (3,2,1,1):-1/245, (1^7):+1, so S=2-2/245=488/245 and
N_all=(630*280*105*21/5040)*(488/245)=153720.

Transitive backtracking census. Fix a0=(0 1 2 3)(4 5) of type (4,2,1).
Enumerate all 280 permutations of type (3,3,1) and all 105 of type (2,2,2,1)
by full S7 scan; for each of 29400 pairs (b,c) set t=(c*b*a0)^{-1} and test
transposition type. Result: 244 pass, 192 transitive with a0, 52 not (orbit
split 24 of type 3+4, 28 of type 1+6). By simultaneous-conjugation symmetry
each a in class alpha has the same fiber count, so
N_all=244*630=153720, N_conn=192*630=120960, N_disc=52*630=32760,
exactly matching the Burnside value. Hence H=24 (integer, so generically
trivial automorphisms; each connected cover counts with weight 1).

Braid orbit. Hurwitz moves sigma_i:(gi,gi+1)->(gi+1,gi+1*gi*gi+1^{-1})
preserve product, cycle-type multiset, and transitivity. BFS from one
connected tuple under pure-braid squares sigma_i^{+-2} (which preserve the
ordered profile) reaches 120960 distinct tuples, i.e. all of N_conn: single
orbit, one irreducible Hurwitz component.

Cut-join step. Put w=t*c so w*b*a=1. Per fixed-a0 fiber the occurring w-types
are mu=(4,2,1):136=96 conn+40 disc; mu=(2,2,1,1,1):36=24 conn+12 disc;
mu=(3,2,2):72=72 conn+0 disc (conn/disc = transitivity of (a,b,c,t)),
summing to 244. Independently enumerated triple totals N(a,b,w) with w*b*a=1:
N(4,2,1)=42840, N(2,2,1,1,1)=7560, N(3,2,2)=15120, with class-constant cut
numbers #{(t,c):t*c=w} equal to 2,3,3 on the respective classes (verified over
full classes of sizes 630,105,210). Hence
N_all=42840*2+7560*3+15120*3=153720; per fiber 68*2+12*3+24*3=244. Joint
(a,b,w) vs (a,b,c,t) transitivity table shows the 24 connected covers fusing
to (2,2,1,1,1) arise from disconnected (a,b,w) triples: t supplies the missing
transitivity across a 1+6 split.

## Limitations

Single instance (d=7, this profile triple plus one simple point); no general
closed formula is claimed. The braid certificate is computational BFS over
120960 tuples for this instance, not a general transitivity theorem. The
cut-join identity is the one-step instance fusing tau with gamma; the full
recursion tower is not computed.

## Reproducibility

Rerunning the fiber scan (5040-element class listing plus 29400 pair tests)
reproduces 244/192/52 in seconds. Artifacts burnside_terms.json (per-irrep
dim, character values, terms; S=488/245) and census_summary.json (fiber
counts, orbit split, fused-type table, cut numbers, joint transitivity table,
H=24) are included. Mirror convention compose'(p,q)=compose(q,p) with
t'=(a*b*c)^{-1} reproduces the same fiber numbers.

## References

R. X.-F. Chen, Towards studying the structure of triple Hurwitz numbers,
arXiv:2308.08455v2; R. Vakil, Genus 0 and 1 Hurwitz numbers: recursions,
formulas, graph-theoretic interpretations, Trans. AMS 2001; Goulden-Jackson-Vakil
double Hurwitz theory; Bai-Chen triple/double Hurwitz (2,d-2) formulas;
Frobenius-Burnside class-algebra enumeration; cut-and-join theory (Fesler;
Mironov-Morozov-Natanzon; Luo-Zhu).
