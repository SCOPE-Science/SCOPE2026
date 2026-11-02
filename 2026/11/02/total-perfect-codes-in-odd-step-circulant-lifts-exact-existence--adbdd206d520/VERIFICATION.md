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

# Verification record

The exact theorem is proved by the sliding-neighborhood identity in `RESULT.md`. A binary candidate \((u_j)\) satisfies the total perfect code property precisely when \(\sum_{h=0}^{2r-1}u_{j-2r+1+2h}=1\) for every cyclic vertex \(j\). Subtracting equations at \(j\) and \(j+2\) forces \(u_j=u_{j+4r}\), which settles every ambient length through the remaining parity and divisibility argument. No finite computation is used to prove this implication for unbounded parameters.

The standalone program `verify.py` implements three genuinely distinct finite checking routes. First, it enumerates all binary subsets and tests the original graph-neighborhood condition for six small parameter choices. Second, it reconstructs arbitrary solutions from initial bits by the original consecutive-equation recurrence, without assuming the claimed periodicity, in 45 cases. Third, it generates and directly tests all \((2r)^2\) claimed residue-class solutions for \(1\le r\le12\) and three consecutive lift factors, totalling 7,800 checked constructions. Its recorded output is

```
LITERAL_SUBSET_ENUMERATION_OK 6
SEED_RECURRENCE_ENUMERATION_OK 45
CANONICAL_CONSTRUCTIONS_OK 7800
VERIFY_OK
```

To replay, run `python3 verify.py` from the directory containing the embedded files. The verifier uses only the Python 3 standard library. The checks do not establish priority or independently certify the proof, and they must not be mistaken for infinite exhaustive enumeration. Scientific comparison covered the relevant arXiv primary materials; one older closed-neighborhood paper was accessible only by its abstract. Independent audit has not been performed.
