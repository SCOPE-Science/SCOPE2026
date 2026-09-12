# Fiber-symmetry obstruction for Rado realizations, with a shift-invariant existence contrast

## Context

Let R denote the Rado random graph: the unique countable graph satisfying the
extension property that for every pair of finite disjoint vertex sets U, V
there exists a vertex x outside U union V joined to all of U and none of V.
The motivating target was the smoothness dichotomy for simultaneous conjugacy
of commuting pairs in Aut(R): whether the orbit equivalence relation of
G = Aut(R) acting on X = {(g,h) : gh = hg} by simultaneous conjugation is
Borel reducible to equality on 2^N. One natural non-smoothness strategy was to
build a highly symmetric Rado presentation on N x Z whose large symmetric
centralizer could code E_0. The finding below emerged directly from testing
that strategy: the fully fiber-symmetric product presentation is impossible,
while a shift-symmetric one is possible.

## Definitions

- Rado extension property on a countably infinite vertex set V: for all finite
  disjoint U, V subsets of V there is x in V \ (U union V) adjacent to every
  vertex of U and to no vertex of V.
- Product vertex set V = F x Z with |F| >= 4 (F = N allowed) and Z countably
  infinite. Fiber permutations act by sigma . (i,m) = (sigma(i),m) for
  sigma in S_F. A graph E on V is fiber-permutation invariant if
  E(a,b) = E(sigma.a, sigma.b) for all fiber permutations sigma.
- Joint shift acts by (i,m) -> (i,m+1).
- The 2-2 witness: U = {(0,0),(1,0)}, V = {(2,0),(3,0)} using fibers 0,1,2,3
  and a fixed 0 in Z.

## Result

Theorem A (fiber-permutation obstruction). Let V = F x Z with |F| >= 4. There
is no graph on V satisfying the Rado extension property that is invariant
under all fiber permutations. In particular, no graph on N x Z isomorphic to
the Rado graph admits the full fiber-permuting symmetric group S_N as
automorphisms. Only the finite group S_4 on four fibers is used.

Theorem B (shift-invariant Rado graphs exist). By contrast, there does exist a
graph on N x Z satisfying the full Rado extension property and invariant under
the joint shift (i,m) -> (i,m+1), via pair-dependent patterns.

Together the pair isolates fiber-permutation symmetry, not translation
symmetry, as incompatible with the Rado property, and blocks in product form
the symmetric-centralizer coding route toward non-smoothness.

## Proof / evidence

Theorem A. Suppose E is fiber-permutation invariant and satisfies Rado
extension. Apply the 2-2 witness above and let x = (k,w) be any candidate,
x not in U union V. If k is outside {0,1,2,3}, the transposition of fibers 0
and 2 fixes x and sends (0,0) to (2,0); invariance gives E(x,(0,0)) =
E(x,(2,0)), contradicting the demanded true vs false. If k = 0, transpose
fibers 1 and 2, fixing x and identifying (1,0) with (2,0) with the same
contradiction. The cases k = 1, 2, 3 are symmetric: for k = 1 swap fibers 0
and 2; for k = 2 swap fibers 0 and 3 (fixing fiber 2, contrasting U-point
(0,0) true against V-point (3,0) false); for k = 3 swap fibers 0 and 2. Every
candidate fails, so E lacks the Rado property.

Theorem B. Write E((i,m),(j,n)) = M[i,j,n-m] with symmetry
M[i,j,d] = M[j,i,-d], M[i,i,0] = false, M[i,i,d] = M[i,i,-d]. Enumerate all
finite requirements (U_s,V_s). At stage s only finitely many pattern values
(indices <= K_s, |d| <= D_s) are decided. Pick a fresh orbit K = K_s+1
exceeding all indices in play and a large shift t so every difference t - m
for (i,m) in U_s union V_s is fresh, then set M[K,i,t-m] to realize the
required pattern for witness x = (K,t) with symmetric counterparts. No
internal fiber-K constraint is triggered since U_s union V_s has no fiber-K
vertex. The union over all requirements satisfies Rado extension and is
shift-invariant by construction.

Computation corroborates but the theorems do not depend on it:
`output/artifacts/uniform_twins_check.py` exhausts all 2^5 x 2^5 = 1024
uniform invariant window-patterns with result 0/1024 admitting the 2-2
witness; `output/artifacts/perpair_satisfiability.py` confirms per-pair
Z-invariant finite-window satisfiability. Both scripts were re-executed and
pass.

## Limitations

This does not decide the target smoothness dichotomy: it blocks one natural
non-smoothness route (symmetric centralizer coding via S_infinity-symmetric
product presentations) but neither proves smoothness nor constructs an
alternative E_0-hardness witness. It rules out only fiber-permutation-symmetric
product presentations, leaving non-uniform coding strategies and turbulence
approaches open. Sharpness for |F| < 4 and non-product symmetric presentations
is not addressed. The Theorem B existence mechanism is close to textbook
universal-set Cayley constructions; its role here is contrast isolating the
culprit symmetry.

## Reproducibility

Run `python3 output/artifacts/uniform_twins_check.py` (expect 0/1024,
OBSTRUCTION CONFIRMED) and `python3 output/artifacts/perpair_satisfiability.py`
(expect satisfiable True, PER-PAIR SATISFIABILITY CONFIRMED). The proofs above
are self-contained; enlarging K_s to dominate the current requirement indices
is the only implicit bookkeeping detail.

## References

- P. Cameron, The Random Graph (arXiv:1301.7544), Chapter 1: extension
  property, universal-set Cayley/shift constructions, automorphism group
  subgroups and overgroups.
- M. Bodirsky, M. Pinsker, All reducts of the random graph are model-complete
  (arXiv:0903.2553): Thomas classification of five closed supergroups.
- M. Grech, A. Kisielewicz, Wreath product in automorphism groups of graphs
  (arXiv:1910.11811): imprimitive vs product action, Aut(G) = A wr B theory.
