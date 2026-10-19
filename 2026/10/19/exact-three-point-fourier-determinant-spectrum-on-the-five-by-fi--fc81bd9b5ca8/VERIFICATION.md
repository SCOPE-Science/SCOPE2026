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
# Exact verification
The file `checker.py` requires only Python 3 and its standard library. Run `python3 checker.py` from a directory containing this file. It checks the two complete unrooted determinant spectra, an independent six-permutation determinant evaluation, the rooted counts, their translation multiplicity relation, all optimizing frequency triples, and both global incidence totals. It terminates with `CHECK_PASS` on success.

All cyclotomic squared moduli are represented as integer pairs \((X,Y)\) meaning \((X+Y\sqrt5)/2\); no floating point enters any acceptance comparison. The linear-algebra and affine-equivariance reductions are proved in `RESULT.md`. The script is an exact exhaustive finite certificate for the stated group; it does not establish any analogous classification for larger primes. Independent audit has not been performed.
