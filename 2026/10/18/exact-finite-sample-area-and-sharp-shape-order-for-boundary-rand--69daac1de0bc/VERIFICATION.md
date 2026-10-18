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

The complete proof is in `RESULT.md`; the executable `checker.py` uses Python 3 and NumPy. Run `python checker.py`. The checker evaluates the claimed mean area as (i) an exact multinomial occupancy sum, (ii) the exact inclusion–exclusion quotient, and (iii) the moment expansion of the three-uniform integral, using `fractions.Fraction`. It checks 75 triples of identities for sample sizes \(1\) through \(15\) and five rational probability vectors, including the limiting boundary vector. The sharp endpoint expressions are checked exactly for \(N=3,\ldots,24\) (22 integer sizes).

An independent geometric numerical check samples points uniformly on the Euclidean perimeter of a \(3\)-\(4\)-\(5\) triangle, sorts by boundary coordinate and computes normalized hull area by the cyclic shoelace formula. At \(N=3,5,8,15\) there are 60,000 independent draws per sample size; the seeded experiment gives absolute mean deviations below five empirical standard errors. The general identities and strict extremizers are proved analytically. Sampling cannot prove infinite or uniform claims.

The empty-side occupancy cases, normalization by the original triangle area, strict triangle inequalities, and unattained limiting endpoint are explicit in the proof. Independent mathematical audit has not been performed.
