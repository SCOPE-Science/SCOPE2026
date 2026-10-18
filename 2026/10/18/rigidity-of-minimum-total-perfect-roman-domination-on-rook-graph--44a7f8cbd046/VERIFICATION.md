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

The proof in `RESULT.md` is a self-contained argument for all integers \(2\le m\le n\). Run `python3 verify_tpr_rook.py` using Python 3, without third-party packages, to reproduce `verify_tpr_rook.out`.

The program directly enumerates all labelings on seven boards, then independently enumerates all assignments of weight at most the theorem's constructive upper bound on six additional boards. It checks both domination clauses, the minimum weight and every optimum's multiplicity. Thirteen board instances pass, including the \(K_2\square K_2\) exception. The general theorem does not depend on finite enumeration; no machine-assisted certification of the infinite proof or independent validation has been performed.
