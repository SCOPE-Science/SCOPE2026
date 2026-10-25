---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The positive square-root amplitude imposes D(f)=1 exactly. Fourier differences 1,2,3 permit direct Laurent constant extraction of log J with weighted degrees <=6. Substituting U=at+k t^3+k lambda t^5, V=a k t^2+lambda t^4, W=a lambda t^3 gives a vanishing quadratic, quartic (k-(2m+1)/(2sqrt m))^2/m, and on that locus sextic 2(lambda-(12m^2+15m+4)/(12m))^2/m+1/(24m). Coefficient vanishing is unique in each variable, parity yields O(t^8), and distance in Dirichlet norm to the monomial phase orbit is sqrt(m+1)|t|+O(t^3). Independently evaluating the actual boundary exponential integral using 65-digit circular quadrature for m=1,2,4, both tuned and off-tuned jets (nine tests at t=0.0003), reproduced the normalized fourth/sixth-order predictions with maximum relative discrepancy 0.00118. These finite tests check coefficients but are not infinite-order proofs; the Taylor/Laurent derivation covers every m.

## originality

PASS

Best-of-knowledge originality is assigned to the exact strengthened/specialized claim, not to previously published premises: Fixed-direction f_t=z cos t+h sin t in Andreev–Matheson excludes t² and t³ corrective harmonic terms; hence its local maximality does not supply the displayed quartic/hexic minimum. Frank–Ivanisvili supplies only nonnegativity, not asymptotic sharpness of the four-mode family. Targeted Resultary searches and primary-paper comparisons were performed; unsuccessful searches are not priority proof. The sharp theorem dominates the sign Delta>=0 and equality characterization for every analytic f, but strict inequality alone does not entail that the deficit can be of order t^6 along a specified normalized family, the unique resonant optimizers, or the coefficient 1/(24m).

## value

PASS

The first adjacent Fourier direction is Hessian-degenerate at a sharp Dirichlet exponential inequality extremizer. Its nonlinear companion modes and positive sixth-order obstruction determine the local stability scale, including explicit counterexamples to lower bounds of quadratic and quartic Dirichlet distance. The object is the actual equality geometry of a recently sharp inequality, not an arbitrary finite polynomial moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
