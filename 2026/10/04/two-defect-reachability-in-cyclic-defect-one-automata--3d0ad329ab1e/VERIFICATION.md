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

The proof was checked symbolically against the exact set action of the two letters. The critical identity is that if \(K\) is the two-element kernel class of the duplicated image \(d\), then for \(h\notin K\),
\[
(Q\setminus\{h\})b=Q\setminus\{e,b(h)\},
\]
whereas for \(h\in K\) the image still has size \(n-1\). Since \(b\) restricts to a bijection from \(Q\setminus K\) onto \(Q\setminus\{e,d\}\), the permitted oriented hole differences are exactly all nonzero residues other than \(d-e\).

`artifacts/verify_two_defect.py` was executed from its packaged path. It exhaustively enumerated all rank-\((n-1)\) maps through \(n=7\), and for every map compared the theorem prediction to direct enumeration of all words \(ba^kba^j\) with \(0\le k,j<n\). It also replayed the explicit constructive witness and verified its length bound. Deterministic random checks covered \(8\le n\le13\). The captured output is `artifacts/verification.txt` and ends with `VERIFY_OK`.

The computation does not establish the infinite theorem by itself and does not test reachability of exceptional antipodal targets using three or more occurrences of the defect-one letter.
