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

The theorem is proved by the coordinate-support and projection arguments in `RESULT.md`. The standalone `verify.py` requires Python 3 and standard-library modules only. Run `python verify.py` from the directory containing this file and the checker. It enumerates every element of \(G\), and for each element exhaustively tests commutation with every other element, in the following cases: \(C_2\to C_2\), \(C_3\to C_3\), \(C_4\to C_2\), \(C_4\to C_4\), \(C_2^2\to C_2\), \(C_2^2\to C_2^2\), \(S_3\to C_2\), \(D_8\to C_2\), \(A_4\to C_3\).

The exact sizes of these groups are respectively \(4,27,16,256,16,256,36,64,1728\). The exact center sizes are \(4,3,4,4,4,4,1,2,1\), respectively. The first case is the unique exception; all others give diagonal copies of \(Z(R)\). The checker prints `VERIFY_OK` only if all exact center sets agree. The examples do not prove the general statement; no formal/infinite certification or independent audit is claimed.
