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

Deleting first + and final - bijects primitive length-2n excursions with Catalan(n-1) Dyck words. The finite uniquely parsed positive-excursion code has bounded return times 2..2N. Induced suspension entropy and Gibbs inequality give the unique pressure root for every N≥1 (N=1 has h=0). The critical weights a_n=C_{n-1}/4^n sum to 1/2 and satisfy a_n~(4sqrt(pi))^{-1}n^{-3/2}. Writing t=2N(log2-h_N), the bulk n≤N/2 contributes o(1), while the endpoint Laplace contribution tends to e^c/(2sqrt(pi)) for t=.5logN+loglogN+c. Monotone bracketing at c=.5log pi proves the o(1) law. Independently solved finite renewal roots at N=100,1000,10000 with residual <5e-15, found t=4.601166876,6.162955772,7.615242740; finite slow convergence is not an infinite proof.

## originality

PASS

The Hedges positive-excursion code and its qualitative finite-core exhaustion are expressly antecedents; the proposed new claim is the length-ordered root equation and the explicit logN/loglogN/constant asymptotic. Published mathematical-record searches for this precise cutoff and equivalent renewal formulations found the assigned result but no stronger record implying its three-term law. Hedges original full paper could not be independently retrieved; only its available abstract and quoted source sections were compared, leaving a named priority risk rather than an automatic novelty rejection.

## value

PASS

A natural canonical length cutoff for an infinite code has quantified entropy-convergence speed. The nontrivial logarithm-of-logarithm correction and constant distinguish it from qualitative exhaustion and give an exact quantitative benchmark for finite-core pressure computations; neither plain Catalan enumeration nor the limit h→log2 provides these terms without singular renewal analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
