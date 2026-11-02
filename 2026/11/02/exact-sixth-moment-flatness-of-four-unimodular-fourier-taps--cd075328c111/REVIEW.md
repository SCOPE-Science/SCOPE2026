# Scientific review

## Correctness — PASS
Four unimodular coefficients are normalized at the endpoints using the legitimate scalar and argument-rotation symmetries. The exact cubic convolution Laurent expansion yields the stated trigonometric polynomial; a two-variable half-sum/half-difference substitution reduces the full feasible phase torus to a real, strictly convex one-variable cubic. Its sole interior critical point is explicit and globally minimizing, including the boundaries. Equality is reconstructed using cube-root argument rotations. The binary comparison is exhaustive for eight normalized sign patterns. Nonattainability by finite root-of-unity alphabets follows from the irreducible nonmonic polynomial of the requisite algebraic number. The actual `artifacts/verify.py` performs independent exact-coefficient and numerical consistency checks; these are corroborations, not the infinite proof.

## Originality — PASS, provisional
The 2019 first-public Balister–Bollobás–Morris–Sahasrabudhe–Tiba work proves uniform flatness for arbitrarily long binary polynomials, not this fixed-length continuous-phase sixth-moment minimum. Schmidt's 2013 paper studies fourth-moment autocorrelation/merit factors in asymptotic unimodular families, not sixth-order exact phase optimization. Sankuru and Babu's 2020 iterative constant-modulus sequence design minimizes the quartic integrated sidelobe level rather than the sixth moment. The published four-frequency sixth-moment *upper* norm inequality optimizes the opposite direction over arbitrary magnitudes, and its affine-phase equality cases are not our complex minimizers. The published four-point fourth-moment phase-only classification identifies fourth-order optimization, but its extremizers have sixth moment at least \(385/4\), strictly above our optimum. Searches also tested exact constant, equivalent phase parameters, Fourier-autocorrelation and polyphase terminology. Historical priority remains provisional owing to possible unindexed small-sequence tables; these are not represented as having been inspected.

## Value — PASS
The one-dimensional four-tap aperture is a canonical first nontrivial phase-design problem in Fourier flatness and correlation norms. The sharp sixth-moment minimum, complete phase-rigid equality classification, strict fourth/sixth tradeoff, and obstruction to every root-of-unity alphabet give a motivated exact phase-only benchmark. It does not simply substitute a parameter into the published fourth-moment or upper sixth-moment results. No generalized code-performance claim is inferred.

## Scope and residual risks
Only four consecutive frequencies on the continuous circle, equal unit magnitudes and the sixth moment are addressed. Some older small-length polyphase tables may contain an equivalent computation. This is an analytical proof with numerical auxiliary checks; no independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
