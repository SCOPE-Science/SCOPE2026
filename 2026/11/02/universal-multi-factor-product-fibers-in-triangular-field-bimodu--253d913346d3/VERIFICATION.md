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

The entire stated formula follows algebraically from the expansion of a triangular product and the first/last diagonal-zero criterion. No infinitary assertion is inferred solely from finite enumeration.

Exact command 1: `python3 verify_prime_fields.py`. This computes every target probability for \(q=2,3\) and \(1\le k\le5\), and for \(q=5\) and \(1\le k\le3\), by full ring convolution. Its complete captured output is `verification_prime_fields.txt` and terminates in `VERIFY_OK`.

Exact command 2: `python3 verify_bimodule.py`. This independently computes every target probability for the asymmetric \((\mathbb F_2,\mathbb F_4,\mathbb F_4)\) bimodule through word length four, and for the two differently acting \((\mathbb F_4,\mathbb F_4,\mathbb F_4^2)\) bimodules through word length three. Arithmetic in \(\mathbb F_4\) uses the irreducible polynomial \(z^2+z+1\). Its complete captured output is `verification_bimodule.txt` and terminates in `VERIFY_OK`.

Both programs were run directly from the complete provided files, and independent replays were compared byte-for-byte with their recorded outputs. The explicit finite checks test only the enumerated fields and lengths. The proof, including the all-length formula and the separate center computation, is needed for the global claim.
