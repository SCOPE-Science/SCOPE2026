# Scientific review — the moving-branch genus-two Hasse divisor in characteristic three

## Correctness — PASS

The claim is quantified over **every** monic separable quintic over **every** algebraically closed field of characteristic \(3\). The smooth parameter is \(t\in\mathbb P^1\setminus V(h)\), with the member at infinity interpreted via the \(s=1/t\) chart. The classical genus-two Cartier–Manin matrix yields the exact homogeneous quadratic \(\mathcal H(T,S)=AT^2+BTS+CS^2\). Two universal coefficient identities establish \(\operatorname{Disc}(\mathcal H)=\operatorname{Res}(h,D^{(3)}h)\) and the fixed-root collision condition. Separability rules out an identically zero divisor. A resultant-zero Hasse divisor is a double point at exactly one excluded singular collision; resultant-nonzero gives exactly two distinct smooth Hasse zeros. Translation by a smooth parameter forces the relevant matrix to have positive rank, so every smooth nonordinary member has \(a=1\). Second semilinear Frobenius iterates, evaluated for the explicit \(\mathbb F_3\) example, distinguish \(3\)-ranks \(0\) and \(1\). The standalone Python 3 verifier recomputes a Sylvester determinant and all 162 separable monic quintics over \(\mathbb F_3\). Finite checks alone were not used to prove universality.

**Residual correctness risks:** The formula uses a specified genus-two differential convention; a transpose leaves the determinant and rank invariant. The statement concerns the parameter line, not stack-theoretic pullback orders at automorphism points. Full Newton polygons or arithmetic splitting are not asserted.

## Originality — PASS, with priority limitations

Cavalieri–Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891 (submitted August 28, 2023), define the precise family and derive its mass formula; their Section 5 and Remark 5.5 give the general number-of-zeros bound and identify the difficulty of controlling individual vanishing orders. The source neither states the universal third-Hasse-derivative resultant identity nor the all-quintic two-or-zero smooth-fiber dichotomy, including singular collision absorption. Classical Yui 1978 provides the Cartier coefficient method, and no originality is claimed for this method. Relevant public literature searches for genus-two Hasse determinants, branch-point variation, resultants and characteristic-three reducedness did not find a covering implication. Finding no source in a bounded search is not a proof of uniqueness; Yui's full article and other classical work were not exhaustively verified.

**Residual priority risk:** A classical or unindexed calculation might already express the same collision resultant or reducedness phenomenon. The inspected open-access mass-formula paper is sufficiently close to make that risk explicit.

## Mathematical value — PASS

The mass formula and generic-bound statement do not determine whether the expected two zeros persist as smooth nonordinary fibers, merge at singular boundary, or acquire higher local multiplicity. The exact resultant detects and classifies this boundary collision for **all** quintics, without any generic-automorphism hypothesis. Universal reducedness of the nonordinary divisor over the smooth parameter locus and the two distinct \(3\)-ranks at the two exceptional fibers are natural geometric refinements, not table recomputation. This is a motivated complete classification in a natural family of genus-two Jacobians.

## Limits of review

The primary open-access source's relevant full text and the exact standalone verifier were inspected. The Yui result was checked through bibliographic material and its explicit use in the primary article, rather than through an independent reading of the full historical journal paper. This remains a self-review; no independent audit or validation has been performed.

Self-review: passed. Independent audit: not yet performed.
