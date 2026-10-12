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
# Verification

The proof is symbolic and cutoff-free. It uses the complete-sequence criterion for sorted positive weights and exhausts the multiplicative partitions of \(\Omega(n)\le4\). The only exact candidate that satisfies every prefix inequality is \(60\), with positive weights
\[
1,1,1,3,6,8,9,16,22,42,108.
\]

The bundled `verify.py` is an independent regression implementation. It constructs a smallest-prime-factor sieve, factors every composite integer through \(10^6\) with \(\Omega(n)\le4\), generates every divisor together with its divisor sum from that factorization, computes \(s(d)\), and applies the complete-sequence criterion. It also checks the explicit candidate failures used in the proof. Its successful output is stored in `verify_output.txt`.

Finite verification does not establish the infinite theorem; it checks the symbolic case analysis against a large bounded domain and exact candidate weight lists.
