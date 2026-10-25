# Scientific review

## Correctness — PASS

The claim is an all-complex-parameter statement for zero-free polynomials of degree at most three, with the standard normalized Hardy \(H^2\) coefficient norm. Every polynomial in the domain has a factorization \(p(z)=a_0\prod_{j=1}^3(1+x_jz)\) with \(|x_j|\le1\), allowing zero parameters. The original inequality is algebraically equivalent to \(7(1+|e_2|^2+|e_3|^2)-3|e_1|^2\ge0\). Phase expansion and the triangle bound reduce it to a real cube inequality.

Four exhaustive sign regions of the factors \(7r_j^2-3\) are checked. Three admit strictly positive rational tensor Bernstein coefficients of degree four on rational boxes containing the respective regions. The fourth admits a positive leading quadratic coefficient and a nonnegative discriminant complement with a degree-eight rational Bernstein certificate. Precisely one Bernstein coefficient vanishes, forcing the unique radius triple \((1,1,1/4)\) up to permutation. Restoring phases forces the unit factors to agree and the short factor to oppose them. The extremizing polynomial gives ratio \(7/10\) exactly. The included `verify.py` ran successfully and checked all certificate coefficients using exact fractions. No continuum-wide conclusion is inferred from a sample grid.

## Originality — PASS, subject to historical-priority risk

The most directly relevant source is S. L. Krushkal, *A General Theorem on Sharp Evaluation of Polynomial Coefficients*, **Axioms** 15 (2026), 699 (DOI `10.3390/axioms15090699`), particularly Theorems 1–2 and Section 5. It discusses coefficient extremals for nonvanishing polynomials, but explicitly sets the new general degree range at \(n\ge5\) and leaves smaller degrees for further analysis. Its structural reduction to maximizing the first coefficient does not supply the numerical cubic Hardy constant or classify the maximizing roots. Related July 2026 and earlier Hardy-function papers supply the framework and degree-unrestricted bounds but do not establish this exact finite-degree equality classification on the material inspected.

Targeted searches for the constant \(\sqrt{7/10}\), zero-free cubics, Hardy \(H^2\) coefficients, rotated two-boundary-root extremizers, equivalent root-factor inequalities, and general results dominating degree three identified no equivalent result. The stronger general Hardy coefficient estimate \(\sqrt{2/e}\) is numerically weaker than the cubic value. Some older full texts and the complete July 2026 preprint could not be inspected; negative searches alone are not proof of historical novelty.

## Mathematical value — PASS

A finite-degree sharp constant is a natural invariant of the zero-free polynomial subspace of a Hardy coefficient ball. The cubic case identifies a non-binomial extremizer with two coincident boundary roots and a third strictly external root at a specific distance. Thus it records genuinely new geometric behavior at the first small degree beyond the elementary quadratic benchmark. The exact extremizer can serve as a concrete finite-dimensional comparison for broader polynomial-coefficient conjectures; no downstream theorem is needed to motivate its precise value.

## Scope and risks

The theorem is limited to one coefficient, degree at most three, and normalized \(H^2\). Its extremizer is permitted because the disk is open, not closed. Earlier literature on coefficient extrema is extensive, and complete historical priority cannot be certified from the accessible sources. The algebraic checker tests an exact identity and finitely many exact Bernstein coefficient inequalities, which together prove global positivity; it does not provide external or independent certification.

Self-review: passed. Independent audit: not yet performed.
