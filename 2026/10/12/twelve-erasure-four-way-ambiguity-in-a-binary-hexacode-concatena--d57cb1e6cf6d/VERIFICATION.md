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

# Reproducibility and scope

Execute `python3 verify.py` using only Python 3 standard-library modules. Successful execution prints `VERIFY_OK` after comparing two independent exact methods.

The first method reconstructs \(\mathbb F_4\), checks all \(20\) relevant quaternary rank-three minors and the Hermitian product condition, enumerates the complete \(64\)-word binary code and its \(651\) binary two-dimensional subcodes, and verifies \(240\) distinct twelve-coordinate plane supports, partitioned into the three claimed repair-block profiles. The second method derives a six-row binary generator from the quaternary code, and for each of the \(18564\) twelve-coordinate masks computes the binary parity-restriction rank on the six unerased coordinates. It independently tests the same ambiguity dimension by counting all compatible codewords. The results are \(9576\) dimension-zero masks, \(8748\) dimension-one masks and \(240\) dimension-two masks. The incidence count is independently checked.

The source code itself is included as `verify.py`. Its loops cover the entire finite domain indicated above; no random sampling, inaccessible database, or unstated software dependency is involved. The argument for why these checks imply the enumerated theorem is presented in `RESULT.md`. No independently performed audit or scientific priority certification is claimed.
