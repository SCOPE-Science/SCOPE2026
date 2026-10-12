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
The proof uses Kwiatkowski's published two-weight formulas for the equal SR-sum of the one-weight simplex expansion. The all-parameter part is then an exact ceiling calculation for the Griesmer sum.

`verify.py` performs two independent kinds of checks. First, for several prime powers and every tested \(2\le k\le8\), it evaluates the Griesmer sums directly from integer ceilings and confirms the identities \(G_q(2k,d)=N-1\) and \(G_q(2k,d+1)>N\). Second, for six small prime-field cases it constructs the generator matrix whose columns are all ordered pairs of nonzero vectors of \(\mathbb F_q^k\), verifies rank \(2k\), enumerates every message, and checks the two predicted weights and frequencies.

The recorded execution output is `VERIFY_OK`. These finite executions test the implementation and the published specialization but do not replace the symbolic proof for arbitrary prime powers.

Scientific limits: the verification does not classify code equivalence, does not treat nonlinear codes, and does not independently re-prove the full general SR-sum theory outside the specialized construction used in the claim.
