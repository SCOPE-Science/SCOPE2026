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

The proof is symbolic and does not depend on the regression cutoff. Its critical exact checks are:

- for even \(n\ne2\), \(6\mid\psi(n)\) and \((1152/385)/3<1\);
- for odd \(n\) with \(5\nmid n\), \(2\mid\psi(n)\) and \((4608/2431)/2<1\);
- for odd \(n\) with \(5\mid n\), \(6\mid\psi(n)\) and \((1536/715)/3<1\);
- \(\psi(39270)=124416\) and \(\varphi(124416)=41472>39270\).

`verify.py` recomputes these identities using exact integer and rational arithmetic and performs an independent finite scan through \(200000\). The scan is a regression check only and is not an exhaustive certificate for the infinite theorem. Its captured output is stored in `VERIFY_OUTPUT.txt`.
