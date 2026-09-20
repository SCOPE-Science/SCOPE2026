# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The finite-index formula was checked independently at the approximation, Bernstein, Gelfand and Kolmogorov steps.

For the upper bound, a threshold \(t>\eta_n\) leaves fewer than \(n\) high-weight image fibers. On the region \(|u|>t\), each of those fibers can be isolated by disjoint neighborhoods in the compact Hausdorff domain of the source functions. Urysohn cutoffs then produce a rank-\(<n\) operator that agrees with the weighted composition operator wherever \(|u|\) exceeds any prescribed \(s>t\), so the remaining norm is at most \(s\).

For the lower bounds, \(t<\eta_n\) gives \(n\) distinct image points with representatives \(x_i\) satisfying \(|u(x_i)|>t\). Disjoint peak functions at those image points span an isometric \(\ell_\infty^n\) on which evaluation of the image operator is diagonal with all diagonal moduli \(>t\). This yields the Bernstein bound directly, the approximation bound by a kernel-dimension argument, and the Gelfand bound by finite-dimensional intersection. For Kolmogorov numbers, evaluation at the \(x_i\) contracts the target onto \(\ell_\infty^n\); the diagonal image contains \(tB_{\ell_\infty^n}\), and every subspace of dimension \(<n\) has quotient map norm one, giving the same lower bound.

The limiting threshold \(\rho\) is exactly the point at which the high-weight image becomes finite. Above it the same finite-fiber construction gives finite-rank approximants. Below it, an elementary recursive separation lemma produces countably many pairwise disjoint open neighborhoods meeting the infinite threshold image. Peak functions supported there span an isometric \(c_0\) on which the weighted composition operator is bounded below by the chosen threshold.

That \(c_0\) witness gives the lower distance to compact, finitely strictly singular and strictly singular operators. It also gives the weakly compact lower bound: a weakly compact operator cannot be bounded below on a copy of \(c_0\), since otherwise the unit ball of \(c_0\) would become relatively weakly compact under the inverse isomorphism, contradicting nonreflexivity. The matching upper bound comes from finite-rank approximation.

No complementability of the witness subspaces is used.

## Originality

**PASS, to the best of our knowledge.** The principal nearby results were separated from the claimed contribution:

- Kamowitz (1981) is classical prior art for compact weighted endomorphisms of \(C(X)\).
- Singh--Summers (1987), as restated explicitly by Albanese--Mele (2023), gives the classical equivalence of compactness and weak compactness with finiteness of each positive threshold image.
- Takagi--Miura--Takahasi (2003) already determine the essential norm of a weighted composition operator on \(C(X)\) in terms of the same threshold-image sets. The distance-to-compact formula is therefore not claimed as new.
- Lin--Wong (2009) gives a structural decomposition for compact disjointness-preserving operators between spaces of continuous functions.
- Standard \(s\)-number literature supplies the definitions and general inequalities.

The contribution claimed here is narrower: the exact equality of all four finite-index scales
\[
a_n=b_n=c_n=d_n
\]
with the counting rearrangement of the fiber-maximal weights for every \(n\), plus the exact common distance to the weakly compact, finitely strictly singular and strictly singular classes and the quantitative isometric-\(c_0\) witness below that distance.

No matching finite-index four-scale formula or singular-ideal distance statement was identified in the literature consulted. The main residual originality risk is older continuous-function/disjointness-preserver literature. In particular, the full Singh--Singh 1995 survey, the Singh--Manhas 1993 monograph and the full Takagi--Miura--Takahasi 2003 article were not exhaustively inspected, so an equivalent statement under older terminology cannot be excluded.

## Value

**PASS.** The theorem upgrades a classical compactness/essential-norm threshold into a complete finite-dimensional approximation profile. A single transparent invariant—the number of image fibers that survive each weight threshold—simultaneously determines four standard \(s\)-number sequences. Its limit also controls four operator-ideal distances, and the proof identifies a reusable geometric mechanism: infinitely many surviving image fibers force an isometric \(c_0\) witness. This gives a sharp quantitative boundary between finite-fiber approximation and persistent infinite-dimensional behavior.

## Scientific limitations

The result is scalar-valued and uses the exact geometry of \(C(K)\) peak functions. Vector-valued \(C(K,E)\) spaces may have additional operator-ideal phenomena from the fiber space \(E\). The compactness and essential-norm components are prior art. Literature coverage is strongest for the explicitly listed weighted-composition and compact disjointness-preserver sources; older monographs, surveys and Banach-lattice terminology remain the principal source of residual uncertainty.
