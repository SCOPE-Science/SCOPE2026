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

Run `python3 verify.py` with a standard Python 3 interpreter. The program uses no third-party packages.

It constructs the regular cyclic tournament \(R_9\) directly from the modular arc rule and exhausts all \(4^9\) four-state assignments for the three coordinates of \(\operatorname{Hom}(\overrightarrow{C}_3,R_9)\). It checks exactly \(720\) valid cells, the cell vector \((90,270,270,90)\), and all \(1917\) Hasse covers.

The program then rebuilds the deterministic staged matching, verifies \(359\) matched pairs, identifies exactly one critical cell in dimension \(0\) and one in dimension \(1\), and topologically sorts the reversed-matching Hasse orientation to certify acyclicity.

As a separate numerical check, it constructs the full cellular chain complex over \(\mathbb F_2\). The boundary ranks are \((89,180,90)\), giving Betti numbers \((1,1,0,0)\) and Euler characteristic \(0\).

The finite computations prove the named finite case only. No extrapolation to larger cyclic tournaments is made. Successful replay ends with `CYCLIC_R9_HOMC3_VERIFY_OK`.
