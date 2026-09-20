# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The main new ingredient is the variable-radius packing criterion for full Assouad dimension. Its two directions were checked directly from the standard equal-radius packing characterization. For exponents below \(\dim_A F\), equal-radius counterexamples already make the normalized power sums arbitrarily large. For exponents above \(\dim_A F\), choosing an intermediate exponent \(s\) and binning arbitrary radii dyadically gives a convergent geometric series
\[
\sum_j O(2^{js})2^{-jt}.
\]
The center-separation needed to replace each dyadic class by an equal-radius packing follows from pairwise disjointness of the original balls.

In the holomorphic-motion argument, the source packings may therefore be chosen equal-radius. After conjugating by \(f_{\lambda_0}^{-1}\), uniform quasisymmetry on a compact parameter disk gives the same ambient diameter control used in Menssen--Younsi Lemma 4.2. The normalized image diameters are divided by an extra fixed factor so that every implicit-function variable lies strictly in \((0,1)\), matching the hypothesis of their quoted inf-harmonic implicit-function theorem. At the base parameter the implicit exponent is exactly the chosen source exponent.

The inf-harmonic compactness step is valid because the reciprocal exponents have a finite prescribed value at the base parameter, excluding local uniform divergence to infinity. For any target parameter and any exponent below the reciprocal limiting majorant, the defining power sum diverges. Uniform quasiconformal inscribed disks preserve a fixed fraction of each image diameter; these disks remain pairwise disjoint and lie in the controlled target ambient disk. Unlike the quasi-Assouad setting, no further power relation between their radii and the ambient radius is required. The variable-radius criterion then gives the desired target Assouad lower bound.

The symmetric version was checked against Menssen--Younsi Lemma 5.3. Intersecting each source disk with \(f_{\lambda_0}(\mathbb R)\) preserves at least half its diameter, so the source power sums still diverge by a uniform factor. Their symmetric diameter-ratio lemma and symmetric implicit-function theorem then apply verbatim, while the same variable-radius target criterion removes the quasi-Assouad scale-transfer step.

The quasicircle consequence follows by substituting the symmetric full-Assouad theorem into the same Smirnov/Menssen--Younsi argument used for quasi-Assouad dimension. Assouad dimension is finitely stable, and the algebra gives \(1+k^2\).

## Originality

**PASS, to the best of our knowledge.**

The closest and decisive source is Menssen--Younsi, arXiv:2609.19522v1, submitted 17 September 2026. The paper proves that the reciprocal quasi-Assouad dimension is inf-harmonic, but its Question 1.11 explicitly asks whether the theorem remains true with full Assouad dimension and states that the authors were unable to prove this. The present theorem answers that question affirmatively.

Searches for combinations of “Assouad dimension”, “inf-harmonic”, “holomorphic motion”, “reciprocal Assouad dimension”, and the source arXiv identifier did not locate an earlier solution. The 2023 theorem of Chrontsios Garitsis--Tyson gives sharp planar quasiconformal distortion inequalities for Assouad dimension; Menssen--Younsi themselves cite it to note that the Harnack-type distortion consequence is already known for full Assouad dimension. That theorem is weaker than inf-harmonic parameter dependence and does not cover the present claim.

The auxiliary variable-radius characterization is an elementary consequence of standard Assouad packing estimates and is not claimed as independently new. Likewise, the inf-harmonic compactness and implicit-function theorems, quasiconformal geometry, and Smirnov's symmetric-motion argument are prior inputs.

Searches for an Assouad-dimension \(1+k^2\) quasicircle bound did not locate a matching prior statement. However, because that numerical corollary may admit independent derivations through other geometric compactness methods, the originality verdict does not depend on separate priority for the corollary.

Residual risk: arXiv:2609.19522v1 is extremely recent, so a contemporaneous solution not yet indexed could overlap. No inaccessible paper was identified as specifically likely to contain the same inf-harmonic Assouad theorem.

## Value

**PASS.**

The result directly resolves an explicit open question in a preprint devoted to holomorphic variation of Assouad-type dimensions. It also explains why the full Assouad problem is, after the correct packing reformulation, structurally simpler than the quasi-Assouad case: the extra radius-versus-ambient-scale constraint disappears. The symmetric strengthening carries the same mechanism into the sharper Smirnov-type setting.

The theorem gives more information than the previously known quasiconformal two-point distortion inequality: inf-harmonicity entails continuity, superharmonicity, Harnack inequalities on arbitrary parameter domains, and a harmonic-envelope structure.

## Literature inspected

- K. Menssen and M. Younsi, arXiv:2609.19522v1, especially Theorems 1.9 and 1.13, Question 1.11, Proposition 2.12, Theorem 2.9, Lemmas 4.1--4.2, Lemmas/Theorems 5.1--5.3, and Section 6.
- A. Fuhrer, T. Ransford and M. Younsi, *Holomorphic motions, dimension, area and quasiconformal mappings* (2023), for the inf-harmonic framework.
- E. K. Chrontsios Garitsis and J. T. Tyson, *Quasiconformal distortion of the Assouad spectrum and classification of polynomial spirals* (2023), especially the full-Assouad distortion theorem.
- J. M. Fraser, *Assouad Dimension and Fractal Geometry* (2021), for standard Assouad packing/weak-tangent background.
- S. Smirnov, *Dimension of quasicircles* (2010), as used through the symmetric-motion lemmas quoted in Menssen--Younsi.

No independent validation, formal verification, or peer review is asserted.
