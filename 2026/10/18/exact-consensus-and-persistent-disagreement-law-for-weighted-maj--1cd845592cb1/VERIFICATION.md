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

# Reproducibility and verification

Run `python3 verify_std.py` with Python 3. The file requires only the Python standard library and is self-contained. It constructs independent first-step rational equations for every leaf-pair state in \(\{0,1,\mathrm{mixed}\}^m\). The unresolved configurations have a strictly positive total chance of selecting a mixed pair and therefore a well-defined transient Markov solution. For all \(1\le m\le6\) it checks every one of the \(2^{2m+1}\) binary initial states under both uniform weights and strictly unequal positive rational weights; the solved eventual-consensus probability is compared exactly with the theorem. It also independently averages those Markov probabilities over Bernoulli product initial states at five rational parameters, and checks an exact independent combinatorial expansion.

Execution of the embedded code produced:

`PASS 21906 exact rational finite-state/initial-law comparisons`

The exact mathematical proof for all \(m\) relies on the two-case majority transition, permanent pair freezing, the first selected edge, independent Bernoulli factorization, and geometric coupon-collection waiting times. Finite Markov calculations and any numerical illustrations are not claimed to establish the theorem for unbounded \(m\). There are no externally supplied certificates, unproved conjectures, or independent scientific-validation claims.
