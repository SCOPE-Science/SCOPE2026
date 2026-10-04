# Review

## Correctness

PASS. The primary source gives the adjoint
\[
\phi_\rho^\dagger(y)=\rho y+y^{16}
\]
and the identity
\[
(\operatorname{im}\phi_\rho)^\perp=\ker\phi_\rho^\dagger.
\]
At a singular parameter, a nonzero adjoint-kernel vector satisfies \(y^{15}=\rho\). The fifteenth-power map has kernel exactly \(\mathbb F_4^\times\), so projective normals are in bijection with the \(21\) singular parameters. This proves that the images are all \(21\) hyperplanes. The hull is nonzero exactly when the normal is trace-zero, giving five projective points, and eliminating the normal yields
\[
\rho^5+\rho^4+1=0.
\]
The standalone verifier independently exhausts all field elements and confirms every stated finite count and incidence identity.

## Originality

PASS. The primary paper already gives the numerical \(60\)-LCD/\(5\)-non-LCD split and lists the five exceptional parameters in one primitive-element representation. It does not identify the singular image family with the complete projective dual plane, and it does not give the invariant polynomial
\[
\rho^5+\rho^4+1.
\]
Focused searches by source identifier, example number, polynomial, trace-zero condition, and hyperplane formulation found no prior same-object statement. The main residual risk is that this compact specialization of the source's isotropy criterion may exist in non-indexed notes.

## Value

PASS. Example 6.15 is explicitly presented as an exhaustive finite verification. The projective-normal bijection explains the entire singular family conceptually, and the trace-zero line explains the exceptional count without case-by-case testing. The degree-five equation makes the five parameters basis-independent and reveals their \(2+3\) Frobenius decomposition. This is a natural structural refinement of the worked example.

Same-model review: passed. Independent audit: not yet performed.
