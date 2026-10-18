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

# Verification and limits

The standalone source `verify.py` evaluates exactly the triple Roman defense inequality at every cell. It builds the theorem's two optimal labeling families for 1,485 choices of \((m,n)\), with \(2\le m\le34\) and \(m\le n\le3m+8\), and asserts their weights equal \(\min\{4m,2m+n\}\). Additionally it traverses all labelings of weight strictly less than the formula on six small boards, using a complete bounded recursive enumeration of labels \(\{0,1,2,3,4\}\). The exhaustive counts by board are \(122\), \(882\), \(6{,}075\), \(49{,}296\), \(22{,}330\), and \(272{,}090\), respectively. No lower-weight labeling passed the defense condition. The recorded stdout is in `verification_output.txt`.

Run from a directory containing the extracted files with `python3 verify.py`. The script needs Python 3 standard library only. The unrestricted theorem relies on the direct surplus case split and the constructive upper bound in `RESULT.md`; the finite checks do not establish the result for all orders on their own. Possible prior coverage in unindexed literature and unavailable full-text sources is not ruled out. No independent audit has been performed.
