---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Writing R_n(w)=w(w+1)···(w+n−1), the two-block coefficient 2^{j−1}−1 converts the unnormalized PGF into (R_n(2z)−2R_n(z))/2, with zero constant and linear coefficients. Evaluation at 1 gives n!(n−1)/2, and factoring the first rising-factorial term yields 2z times the difference of the products over h=1,…,n−1 in the normalized formula. For each h and nonzero z with Re z≥0, the squared-modulus difference of 2z+h and z+h is 3|z|²+2h Re z>0. The second factor z+h is nonzero there, and the index set is nonempty for n≥2, so strict factorwise dominance implies the products cannot be equal, including on the imaginary axis. The z² coefficient is the positive unsigned Stirling number [n,2] divided by L(n,2); n=2 gives P=z². I independently multiplied the n=8 factors and compared to the rising-factorial coefficients and recomputed the cubic discriminant −307921820 and Routh margin 2301540. That confirms the exact nonreal example, not all-degree stability, which follows from the modulus proof. Replay: RESULT.md lines 21–47; the separate finite verifier verify.py and logged output in VERIFICATION.md were inspected, not executed.

## originality

PASS

The full two-block nonzero-root exclusion is a distinct proved case of the earlier conjecture. The PGF identity, the forced zero at the origin (from the established support) and particular negative integer zeros are prior or immediate from prior statements, not novelty in themselves. No compared source proves the full exclusion for k=2.

## value

PASS

Two blocks are the first natural case beyond a single rising factorial; the family contains genuinely nonreal roots. The proof settles a cited conjectural location uniformly in n for that subfamily and explains why the imaginary axis is strictly excluded after factoring out zero. This is materially stronger than the finite sample or the trivial origin check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
