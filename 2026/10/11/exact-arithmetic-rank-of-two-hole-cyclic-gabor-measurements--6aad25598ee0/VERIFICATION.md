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

# Exact checks and limits

Run `python3 CHECK.py` using standard Python 3. The program generates the integer cyclotomic polynomial \(\Phi_N\) via monic division of \(X^N-1\), builds exact residue vectors of \(X^j\), and computes all Weyl ambiguity sums by integer-vector addition. It checks every \(5\le N\le35\), \(1\le a<N\), exactly \(589\) cases, against the stated totient-free gcd-sum form of the formula. Expected output: `EXACT_CHECK_OK: 589 pairs (5 <= n <= 35, 1 <= a < n)`.

This finite check is not an exhaustive proof for arbitrary \(N\). The proof is the factorization of the two-/three-/four-site deleted-character sums and the complete congruence inclusion-exclusion count in `RESULT.md`. The rank/ambiguity equivalence used there is [1, Theorem 1]. No spectral conditioning or nonlinear phase-retrieval claim is verified. No independent mathematical audit has occurred.
