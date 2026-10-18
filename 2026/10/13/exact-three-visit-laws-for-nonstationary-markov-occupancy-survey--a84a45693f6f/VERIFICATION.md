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

For occupancy probability psi, initial conditional detection pi, transitions a=P(1|0), b=P(1|1), expansion of the seven nonzero histories gives u=psi*pi and r=psi*(1-pi)*a. Thus b=(q110+q111)/u, a=q101/(q100+q101), psi=u+r/a, pi=u/psi. Positivity makes divisions safe. The remaining three independent algebraic equalities q111=ub², q011=rb and q001=r(1-a), with reconstructed parameters in (0,1), are both necessary and sufficient for an interior eight-cell history law, with q000 by normalization. Two-wave observations determine only (u,r,b), leaving a free interior interval and infinitely many quadruples. Independently tested 256 exact rational parameter quadruples and the analytic inversion; this proves an ideal population-law identification theorem, not finite-sample estimation.

## originality

PASS

On inspected evidence this exact final claim is not a mere restatement or implication of a known stronger theorem; all four formal comparisons below and material primary-source inspections distinguish what is already known. Originality is best-of-knowledge, not independence or certification.

## value

PASS

An exactly invertible and sharply minimal replicate design plus necessary-and-sufficient polynomial compatibility tests answers a natural statistical identifiability question for a directly Markov observed detection process. Distinguishing structural identification from practical survey guidance can guide model checking and experimental design, even though the assumptions exclude a second hidden detection layer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
