# Nonexistence of compactly branched degree > 1 quasiregular self-maps of the Cartan group

## Context

The Cartan group **C** is the 5-dimensional free step-3 rank-2 simply connected
Carnot group with a fixed left-invariant rank-2 distribution,
Carnot–Carathéodory metric, and homogeneous dimension Q = 10.
Quasiregular maps on Carnot groups were initiated by Heinonen–Holopainen for
2-step Heisenberg-type groups; the step-3 Cartan case lies outside that theory.
In Euclidean quasiregular theory, Zorich/winding-type maps give non-injective
branched covering examples, but in dimension n >= 3 the standard winding map
is branched along an unbounded (n-2)-plane. The target question asks whether a
sub-Riemannian winding/Zorich-type analogue exists on **C**: a nonconstant
non-injective K-quasiregular self-map with compact nonempty branch set and
global Brouwer degree > 1. This connects to Heinonen's ICM problem on allowable
branch sets and to Vuorinen's question on proper branched covers with compact
branch.

## Definitions

- **C**: 5-dimensional free step-3 rank-2 Carnot group; as a manifold C ≅ R^5.
  Layer dimensions (2,1,2); topological dimension 5; homogeneous dimension
  Q = 1·2 + 2·1 + 3·2 = 10.
- **K-quasiregular** (analytic definition, K >= 1 finite): horizontal
  W^{1,Q}_{loc} regularity plus |D_H f|^Q ≤ K J_f a.e.
- **Branched covering**: continuous, open, discrete map. Branch set B_f is the
  set where f is not a local homeomorphism.
- **Proper**: preimage of every compact set is compact (hence closed with
  compact fibers). For R^n → R^n maps, global Brouwer degree via one-point
  compactification S^n → S^n is defined only for proper maps.
- **Degree > 1**: global Brouwer degree strictly greater than 1 (hence
  surjective, nonzero degree).

## Result

**Theorem.** There is no finite K ≥ 1 and no nonconstant non-injective
K-quasiregular self-map f : **C** → **C** with compact (possibly empty) branch
set whose global Brouwer degree is strictly greater than 1. In particular,
there is no sub-Riemannian winding/Zorich-type branched covering self-map of
the Cartan group with compact nonempty branch set and degree > 1.

The obstruction is purely topological and uniform in K: every continuous, open,
discrete, proper self-map of R^5 with compact branch has exterior sheet number
m = 1 and hence |deg| ≤ 1 (= 1 if sense-preserving).

## Proof / Evidence

Identify **C** with R^5, so n = 5 ≥ 3. Any candidate meeting the specification
must be continuous (also from Sobolev regularity), open and discrete (contained
in "branched covering" language), and proper (presupposed by global degree:
a non-proper R^n → R^n map has no well-defined global degree via S^n → S^n).
No Reshetnyak-type theorem is invoked.

**Lemma.** Let n ≥ 3 and f : R^n → R^n be continuous, open, discrete, proper
with compact branch set B_f. Then the exterior covering has sheet number
m = 1; in particular no such map has degree > 1.

*Proof.* f(B) is compact. Choose a closed ball D with f(B) in its interior and
put U = R^n \ D ≃ S^{n-1}, connected and simply connected since n-1 ≥ 2.
Since U contains no branch values, f : f^{-1}(U) → U is an ordinary covering:
fibers are finite (properness + discreteness), each point has a homeomorphic
neighbourhood (unbranched), and closedness (proper maps are closed) yields
evenly covered neighbourhoods. Properness makes it finite-sheeted; U connected
gives constant sheet number m ≥ 1 (m ≥ 1 by surjectivity of nonzero-degree
proper maps). U simply connected implies the covering is trivial:
f^{-1}(U) = ⊔_{j=1}^{m} U_j with each f|_{U_j} : U_j → U a homeomorphism.
For a regular value y ∈ U, deg f = Σ_{x ∈ f^{-1}(y)} i(x,f) with local indices
±1 (local homeomorphism), so |deg f| ≤ m; sense-preserving gives deg f = m.
Thus deg > 1 forces m ≥ 2. But K_0 = R^n \ f^{-1}(U) = f^{-1}(D) is compact by
properness and has exactly one unbounded complementary component W. Each sheet
U_j is unbounded: a bounded sheet would lift y_k → ∞ to a bounded sequence
with accumulation point x* and f(x_k) = y_k → f(x*), impossible. Each U_j is
connected, unbounded, in the complement of K_0, so U_j ⊂ W. Then W ∩ U_j = U_j
partitions connected W into m ≥ 2 disjoint nonempty relatively open sets,
impossible. ∎

Applying the lemma with n = 5 rules out the existence horn for every finite K.
Sobolev/distortion bounds play no further role.

## Limitations

This is a negative resolution of the existence horn only. It does **not** prove
every nonconstant quasiregular self-map of **C** is globally injective. Maps
that are not proper (hence have no global degree) or branched maps with
noncompact branch set are outside the specification and left open, consistently
with Zorich/winding-type maps with noncompact branch (e.g. standard winding
map branched along an axis). The lemma is sharp in dimension: it fails for
n = 2 (z ↦ z² has compact branch {0} and degree 2).

## Reproducibility

`output/artifacts/check_numerology.py` verifies layer dimensions (2,1,2),
topological dimension 5, Q = 10, and n = 5 ≥ 3 (S^4 exterior simply connected).
The proof is deductive, using only standard covering theory,
one-point-compactification degree, and topology of complements of compact sets
in R^n.

## References

- Kauranen–Luisto–Tengvall, On proper branched coverings and a question of
  Vuorinen, Bull. Lond. Math. Soc. 54 (2022), 145–160; arXiv:1904.12645.
  (Vuorinen question: n = 3 or empty branch ⇒ homeomorphism; n ≥ 4
  compact-branch general-domain case left open.)
- Berstein–Edmonds, The degree and branch set of a branched covering,
  Invent. Math. 45 (1978), 213–220. (Closed-manifold setting.)
- Heinonen–Holopainen, Quasiregular maps on Carnot groups, J. Geom. Anal.
  (1997). (Analytic definition; openness/discreteness for 2-step
  Heisenberg-type; step-3 Cartan excluded.)
- Aaltonen–Pankka, Local monodromy of branched covers and dimension of the
  branch set, arXiv:1509.06617. (Berstein–Edmonds normalization context.)
