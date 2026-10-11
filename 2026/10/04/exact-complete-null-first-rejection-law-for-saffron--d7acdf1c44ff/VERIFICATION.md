---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Before the first rejection, the published SAFFRON recursion keeps only the initial-wealth term. The index equals one plus the number of prior noncandidates. At stage \(j\), a rejection has probability \(a_j\), a nonrejecting candidate has probability \(\lambda-a_j\) and repeats the stage, and a noncandidate has probability \(1-\lambda\) and advances. Summing the geometric loop gives rejection-before-advance probability \(a_j/(1-\lambda+a_j)\), and multiplying stage survivals gives the exact product. In the uncapped case, elementary product and logarithm inequalities give the two-sided envelope. A fresh exact-rational finite-state replay independently matched the stage factorization on a finite schedule.

## originality

PASS

The SAFFRON source defines the candidate clock, initial-wealth recursion and FDR guarantee but does not state the attained complete-null first-rejection product or the gamma-allocation envelope. A current online-testing review likewise summarizes control and power rather than this exact law. Targeted searches for global-null, any-rejection, first-rejection and renewal formulations did not locate an equivalent source. The residual possibility of an older alpha-investing renewal derivation is retained explicitly.

## value

PASS

The exact law separates the candidate-filtering clock from gamma allocation and quantifies the attained complete-null conservatism of a standard adaptive online FDR procedure. The sharp concentration/diffusion envelope is a motivated calibration boundary and provides exact implementation benchmarks, not merely a restatement of validity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
