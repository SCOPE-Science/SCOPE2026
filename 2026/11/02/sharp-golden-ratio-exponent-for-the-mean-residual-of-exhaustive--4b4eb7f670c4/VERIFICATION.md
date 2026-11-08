---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The fair-input transform has exact length recurrence a_(2n+rho)=a_n+E[a_B]+rho, B~Bin(n,1/2), with a_0=0,a_1=1 and b_m=a_m/2 for residual-one expectation. The golden exponent alpha=log_2 phi obeys n^alpha+(n/2)^alpha=(2n)^alpha. Taylor concavity and Chernoff bound control the binomial Jensen deficit uniformly by <4, including the B=0 atom. The constants 1/10,9/10 in the positive-length lower induction have spare >=.05; the 3,-2 upper induction includes odd lengths and B=0 correctly. Thus all N>=1 bounds and existential worst-case lower follow. Independent rational recurrence through N=64 and all 2^N strings through N=10 agreed; those finite checks are not the infinite proof.

## originality

PASS

Best-of-knowledge PASS for the quantitative all-N sharp-mean exponent, not for the recursion or conjectured worst-case exponent. The same mean recurrence and heuristic golden exponent are explicitly in Garivier 2026 Section 8; its deterministic upper exponent about .773 is weaker and for a different statistic. No inspected primary theorem supplies matching all-N two-sided mean bounds; older Peres/Pae extraction-rate results are qualitative. Earlier divide-and-conquer recurrence theory may independently imply these bounds.

## value

PASS

The expected leftover size is a natural efficiency invariant of an exhaustive unbiased-bit extractor. Proving the exact exponent conjectured heuristically by its inventor gives sharp decay of mean extraction loss and a nontrivial pointwise existence bound; no maximum-case equality or limit constant is asserted. The all-size bound is not a renamed finite table or routine output-rate calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
