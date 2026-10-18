---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Square modulus reduces to a concave quadratic q(cos θ)=s²+b²+2bdx−(s²−d²)x². The nearest cosine samples u<0<v give two contacts. A quartic F(R) with F′>0 gives a unique R∈(0,1), and constructed positive coefficients balance those contacts. For every competitor the weighted convex two-sample lower functional has positive definite Hessian; selecting λ∈(0,1) makes the candidate its unique minimizer and certifies global face optimality for all odd N. Taylor expansion yields the stated N⁻² coefficient. Independently used direct nonsmooth sampled-grid optimization for N=5,7,9,11,21,101,501,1001 and found the analytic root ratio to numerical precision. This is not an extrapolation to all N.

## originality

PASS

Neuwirth supplies the continuous-circle √2 value and Newman extremizer; the published unrestricted finite-cyclic theorem is restricted to even N, while a published all-N phase minimax fixes all coefficient magnitudes equal. Neither solves the N odd sign-face optimization over VARIABLE magnitudes, nor supplies this monotone quartic and precise lower-bound expansion. Pass with older interpolation/crest-factor priority risk.

## value

PASS

The fixed sign face is not arbitrary: it contains the translated continuous Newman extremizer. Its sharp all-odd sampled-grid answer quantifies finite-sampling gain and supplies a rigorously motivated lower bound for the still unrestricted odd Sidon problem. The theorem does not claim the global complex-phase optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
