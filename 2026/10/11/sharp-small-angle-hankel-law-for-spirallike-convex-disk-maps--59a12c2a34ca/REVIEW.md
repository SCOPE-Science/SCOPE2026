# Review of Sharp small-angle Hankel law for spirallike convex disk maps

## Correctness

PASS. The positive-real-part substitution follows exactly from the normalized half-plane constraint for \( |\beta|<\pi/2 \). Integrating the logarithmic derivative produces a nonvanishing derivative, so every Carathéodory coefficient choice represents an admissible locally biholomorphic map. Direct Taylor expansion gives the stated \(H_{2,2}\) polynomial, while the classical two-step Schur parametrization includes all possible first three Carathéodory coefficients.

At zero angle the full three-parameter compact body has a unique extremum, up to rotational symmetry, at \(r=1/2\), \(x=-1\). The radial derivative there is uniformly at least \(3/32\) for all remaining Schur choices, forcing every sufficiently small-angle optimizer onto \(|x|=1\). The exact negative-definite Hessian on this boundary yields an analytic unique optimizer branch, leading coefficient \(-59/432\), and an even fourth-order error. The explicit degree-two Blaschke witness realizes the same quadratic term and beats the quoted comparison by \(41\beta^2/864+O(\beta^4)\). The accompanying code recomputes all needed exact derivative and coefficient identities.

## Originality

PASS with an explicitly limited source-access risk. The full available author-uploaded text of Ahamed–Sarkar–Das (2026) was read across its definitions, theorems, proof, and references. It states the quoted upper-bound expression and asks for sharp nonzero-angle behavior, but gives neither the small-angle optimal second variation nor the Schur-parameter angular drift; its displayed formula is contradicted by the explicit admissible example under its local hypotheses.

The earlier Krishna–Reddy (2015) article is cited in that manuscript for the same bound, but its complete text was not accessible despite open-access and authorized institutional attempts. Its exact assumptions are therefore not asserted here. Third-Hankel Banach-space estimates and Fekete–Szegö estimates concern different functionals. Targeted search for the exact coefficients, small-angle aliases, extremizer parameterization, and inequivalent wider theorems located no dominating claim. Results on Hankel operators instead concern a different use of the term Hankel.

## Value

PASS. Determining sharp nonzero-angle second Hankel behavior is an explicitly motivated coefficient-extremal problem. The result not only supplies the sharp local invariant and all local extremizer structure, but also rigorously identifies a mismatch between an all-angle bound and the admissible class in the same new paper. The precise \(-10/9\) angular drift is necessary to obtain the true \(-59/432\) quadratic coefficient; freezing the zero-angle extremizer does not determine the optimum. This is an analytically substantive boundary-stability result, not a minor numerical recalculation.

The comparison is restricted to the locally biholomorphic disk class and the displayed 2026 formula. No claim is made about globally univalent restrictions or the inaccessible original 2015 full text.

Same-model review: passed. Independent audit: not yet performed.
