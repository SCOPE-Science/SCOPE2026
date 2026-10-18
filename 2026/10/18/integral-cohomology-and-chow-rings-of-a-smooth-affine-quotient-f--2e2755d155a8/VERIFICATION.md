---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification and reproducibility

Run `python3 verify.py` using a standard Python 3 interpreter. The program has no third-party dependencies. It verifies the defining invariant identities for all small field points satisfying the hypersurface equation over \(\mathbb F_3\) and \(\mathbb F_5\) with one or two auxiliary factors, independently counts the boundary and complement for \(n\in\{1,2,3\}\) and field orders \(q\in\{3,5,7\}\), checks \(\#Y_n(\mathbb F_q)=q^{n+2}+q(q-1)^n\), and checks the binomial Betti-rank and Euler formulas. It reports that all finite checks passed.

The mathematical proof in `RESULT.md` does not infer infinite-range conclusions from these samples. Its decisive steps are explicit quotient gauges, the isomorphism \(D_n\simeq\mathbb A^1\times(\mathbb G_m)^n\), triviality of the normal bundle, the integral Gysin exact sequence, the self-intersection formula, and Chow localization. The cohomological conclusion is integral and restricted to the complex model; the finite-field point-count conclusion is algebraic. No independent audit or external formal certification is claimed.
