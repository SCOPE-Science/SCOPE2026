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

The proof in `RESULT.md` supplies the full infinite-family argument by direct contraction, rank stratification, Gauss-lemma irreducibility, and projective cycle degree. No external or independent audit has been performed.

Run `python3 verify.py` using only the Python 3 standard library. The checker uses a fixed integer seed and exercises the explicit tensor contraction identity and rank-one factorization over several dimensions; it also verifies the Segre degree and degree-eight subtraction. The script is finite evidence only; no finite test establishes irreducibility or the infinite claim.
