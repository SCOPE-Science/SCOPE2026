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

The universal proof has two exact components. First, the continued-fraction matrix product is reduced modulo \(2\); its action on the three nonzero vectors of \(\mathbb F_2^2\) converts the parity of the number of even Euclidean quotients into the parity of the penultimate convergent numerator, and hence into the parity of the least positive coefficient \(a\) in \(ap-bq=1\). Second, the two-prime-power formula uses the exact inclusion-exclusion decomposition from the primary source, with the two cross-intersection sizes selected by the opposite parity of \(b\).

`verify.py` was replayed from the packaged path. It checks the Bézout parity theorem for every coprime odd pair in the finite box \(p\le301\), \(q\le401\), giving 15169 cases. It also computes \(T(n)\) directly from its definition and compares with the branch formula for 304 generated odd two-prime-power cases with \(n\le30000\). The recorded output is stored in `verification_output.txt`.

These finite checks are corroborative only. They do not establish the infinite theorem; the proof in `RESULT.md` does. No statement is made about the many-prime case, and possible unindexed classical overlap remains a literature limitation.
