# The finite torus-to-circle function space retracts onto a circle and eight points

## Finding
Let \(C\) be the four-point minimal finite circle, with minimal elements \(0,1\), maximal elements \(2,3\), and \(i<j\) for each \(i\in\{0,1\}\), \(j\in\{2,3\}\). Give \(T=C\times C\) the product specialization order and \(\mathcal F=\operatorname{Map}(T,C)\) the compact-open topology. Then \(\mathcal F\) contains exactly \(2836\) maps and admits a strong deformation retraction onto its twelve-map subspace consisting of the four constant maps and the eight maps
\[
\alpha\circ\pi_i,\qquad i\in\{1,2\},\quad\alpha\in\operatorname{Aut}(C).
\]
The constant maps form a copy of \(C\); each of the other eight maps is isolated in the whole finite mapping poset. The displayed twelve-map space is the Stong core of \(\mathcal F\). In particular,
\[
\mathcal F\simeq C\sqcup\coprod_{j=1}^{8}\{\mathrm{pt}_j\},
\qquad
|K(\mathcal F)|\simeq S^1\sqcup\coprod_{j=1}^{8}\{\mathrm{pt}_j\}.
\]
Thus \(H_0(\mathcal F;\mathbb Z)\cong\mathbb Z^9\), \(H_1(\mathcal F;\mathbb Z)\cong\mathbb Z\), and all higher integral homology groups vanish. The first-homology statement is a new mapping-space invariant; the previously known nine connected components alone do not determine it.

## Assumptions and scope
The finite spaces are \(T_0\) Alexandroff spaces, identified with their specialization posets; continuity is order preservation. The product \(T\) has exactly sixteen points, indexed in lexicographic order by \(\{0,1,2,3\}^2\). Its order complex has the weak homotopy type of the usual two-torus. The compact-open function space for finite source and target is itself finite, and its specialization order is the pointwise order \(f\le g\) if \(f(t)\le g(t)\) for all \(t\in T\). The theorem concerns this precise finite function space, not the classical compact-open space of maps between geometric realizations and not the second, non-product, minimal finite torus model.

## Proof
**Exhaustive description of the mapping poset.** For an isotone \(f:T\to C\), the preimage \(D=f^{-1}(\{0,1\})\) is an order ideal. Every comparability-connected component of \(D\) must have a single image in \(\{0,1\}\), since the two minimal target values are incomparable. Similarly every comparability-connected component of \(T\setminus D\) has a single image in \(\{2,3\}\). Conversely, arbitrary choices of the two permitted values independently on these components give a valid isotone map: the only cross-level order relations go from \(D\) to its complement, and every minimal target lies below every maximal target.

If \(c_D\) and \(c_U\) are the numbers of components of the two induced comparability graphs, the number of maps associated with an ideal \(D\) is exactly \(2^{c_D+c_U}\). Exhausting the \(2^{16}\) possible subsets by their down-closure test leaves exactly \(430\) ideals. Their complete component-signature distribution is

| \((c_D,c_U)\) | \((0,1)\) | \((1,0)\) | \((1,1)\) | \((1,2)\) | \((1,3)\) | \((1,4)\) | \((2,1)\) | \((2,2)\) | \((3,1)\) | \((4,1)\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Number of ideals | 1 | 1 | 228 | 82 | 16 | 1 | 82 | 2 | 16 | 1 |

The weighted sum is \(2836\). The standalone verifier also obtains precisely the same full set of maps by an independent recursive linear-extension enumeration, not merely by matching totals.

**A complete beat-point certificate.** Index these \(2836\) maps by increasing binary ideal mask in the lexicographic source-point order, then by the lexicographically ordered binary choices on their comparability components, discovered from the source vertices in increasing index order. The accompanying `collapse_certificate.txt` has exactly \(2824\) lines. Each line contains a deleted map index, a surviving witness index, and `up` or `down`. For an `up` deletion, the witness is the *least* element of the currently surviving strict upper set; for `down`, it is the *greatest* element of the strict lower set. The standalone `verify.py` independently constructs the entire mapping order and checks all \(2824\) witnesses against the updated surviving set, one at a time. Its complete verification gives \(2668\) up-beat and \(156\) down-beat deletions.

Every such deletion is a strong deformation retraction by the beat-point theorem for finite spaces. Therefore their composition is a strong deformation retraction from the original function space to the induced subposet on the twelve survivors. The verifier checks that these survivors are *exactly* the four constants and eight projection-after-automorphism maps. It checks every comparability in the terminal subposet. The constants inherit precisely the order of \(C\), while all eight other maps have no comparabilities except equality. These eight maps are also isolated in the original function poset: an order comparison with any one of them would restrict to a pointwise comparison with a circle automorphism on each appropriate coordinate fiber; the only circle endomorphism comparable with an automorphism is that automorphism itself. The latter elementary assertion is also exhaustively checked for all \(36\) circle endomorphisms.

The terminal space has no beat points: each minimal and each maximal element of its four-point circle component has two incomparable neighboring extrema, and each isolated point has none. It is therefore the Stong core. Its order complex is the disjoint union of one four-edge circle and eight vertices. Strong deformation retractions preserve homotopy type and integral homology, proving all conclusions.

## Verification
From the directory containing `verify.py` and `collapse_certificate.txt`, run `python3 verify.py` using only the Python standard library. It reconstructs the source and target orders, independently enumerates the \(2836\) maps by ideal signatures and by recursive backtracking, checks the full ideal-signature distribution, builds all pointwise comparabilities, and replays all \(2824\) beat-point witnesses with the current active-set inequalities. It then checks the twelve-point core, all its inherited comparabilities, the full automorphism/projection list, and the nonzero induced homology maps.

The successful packaged check prints:

`VERIFY_OK maps=2836 ideals=430 two_enumerations=true beat_deletions=2824 core=4_point_circle_plus_8_isolates nonzero_maps=8`

The proof is an exact, exhaustive finite certificate for the stated sixteen-point source and four-point target. No finite sample is extrapolated to an unproved infinite family.

## Relationship to prior work
Cianci and Ottina identify the product of two four-point circle spaces as one of the two sixteen-point minimal finite torus models. Yoshise develops finite-circle and finite-torus topological complexity, including the rigidity of nonzero-degree maps between equal-size finite circle models. May and Pishevar explain the pointwise specialization order on compact-open function spaces and the comparison of connected components with homotopy classes. These sources provide the objects and machinery, not the strong deformation-retract calculation here.

A previously published computation for exactly the same source and target establishes the \(2836\)-map count and the nine homotopy classes, with eight projection-after-automorphism maps isolated and the other \(2828\) maps connected. Those facts are not claimed as new. The present contribution determines the **entire finite-space homotopy type**, including the nontrivial first homology of the large component, by a complete beat-point certificate. Nine connected components are compatible with many different higher homotopy types and do not imply the asserted circle core. Published strong-collapse computations for mapping spaces with a six-point sphere, a thirteen-point projective-plane model, and certain nine-point finite spaces have different source posets and do not calculate this torus mapping space.

## Limitations
The exact retraction is proved only for \(T=C\times C\) and target \(C\); neither larger circle models nor a higher-dimensional product is classified. The proof is computer-assisted but finite and exhaustive, with the complete checkable witness sequence embedded; the certificate must be replayed to audit the nonstandard collapse step. It does not assert an equivalence of the full finite function space with the classical mapping space, which has infinitely many homotopy components. An unindexed historical computation of this precise finite mapping-poset core cannot be excluded by the searches reported in the review.

## References
1. R. Yoshise, *Topological complexity of Khalimsky circles*, arXiv:2302.06380v1 (first public 2023-02-13), especially the finite-circle and finite-torus discussion and Appendix A; primary MSC 55M30.
2. N. Cianci and M. Ottina, *Poset splitting and minimality of finite models*, arXiv:1512.06088v1 (2015), Section 6 on the two minimal sixteen-point torus models.
3. J. P. May and E. Pishevar, *Finite Spaces and Larger Contexts*, Chapter 3, Section 3.2 (finite compact-open mapping-space order and finite-space homotopies), freely accessible manuscript at https://math.uchicago.edu/~may/PAPERS/FINITE.pdf.
4. Previously published mathematical finding, *Nine homotopy classes of direct maps from the minimal finite torus to the four-point circle* (2026), published-finding corpus record 4776d1df4145, establishing the component census but not the mapping-space strong deformation retract.
5. R. E. Stong, *Finite topological spaces*, Transactions of the American Mathematical Society 123 (1966), 325–340 (beat points and finite-space cores).
