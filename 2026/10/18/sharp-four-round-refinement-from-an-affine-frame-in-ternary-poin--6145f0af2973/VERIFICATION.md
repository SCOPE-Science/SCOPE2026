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

The exact theorem is established in `RESULT.md` by an all-dimensional coordinate argument; the following are finite supporting checks, not formal or independent certification.

Run using ordinary Python 3 from this directory:

```
python3 check_refinement.py
python3 check_witnesses.py
```

The first program builds point–hyperplane graphs over \(\mathbb F_3\) by enumerating normalized nonzero normals and right-hand sides, then applies full synchronous multiset refinement. It directly verifies first discreteness at round four in dimensions \(d=2,3,4,5,6\), all claimed intermediate hyperplane class counts, a persistent pre-round-four point collision, and graph vertex totals. For the theorem, dimensions \(d\ge3\) are relevant; \(d=2\) is a consistency control. The exact outputs of this run are stored in `check_refinement.out`.

The second program does not run colour refinement. It independently enumerates the proposed already-recovered point set \(P\) and verifies that the incidence bit-vector of every affine hyperplane on \(P\) is unique in dimensions \(d=2,3,4,5,6,7,8,9\). It also verifies the symbolic two-coordinate count identities used to show the pre-round-four collision. Its recorded run is in `check_witnesses.out`.

Limitations: these programs verify only finite stated instances and identities. The proof in `RESULT.md` supplies the quantifiers for all integers \(d\ge3\); independent mathematical audit has not been carried out.
