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

# Reproducible checks

Run `python3 checks/verify_fo4.py` and `python3 checks/verify_width.py` in an ordinary Python 3 installation (standard library only). Expected standard outputs are stored in `checks/fo4_output.txt` and `checks/width_output.txt`. The programs were executed and both expected-output files captured from their actual runs.

The first checker enumerates \(63^3=250047\) ordered three-tuples of nonzero vectors in the six-dimensional binary symplectic space, identifies \(17\) distinct pairing/linear-dependence signatures, compares their possible extensions in dimensions six and eight, checks all \(15^3=3375\) ordered triples in dimension four, and tests the dimension-two-to-three four-variable separator. The second checks the sharp forbidden-set count and uniform fiber inequality for \(3\le k\le11\), together with an explicit pair of a totally isotropic basis and dual witness at the next width.

**What is proved without computation:** for every \(k\ge3\), a one-move extension either copies a sum of at most \(k-2\) fixed vertices or finds a vector in an affine pairing fiber outside all such small spans, because the fiber is strictly larger. This supplies an arbitrary-length \(k\)-pebble strategy in all dimensions at least \(k-1\). The isotropic independence formulas supply the matching lower bound on variable width. The finite tests merely exercise sample boundaries and independent implementations of the requisite linear-algebraic mechanisms.

**Unverified scope:** no counting-logic version, arbitrary-field version, or independent external proof audit is claimed. The searches cannot exclude all historically equivalent presentations.
