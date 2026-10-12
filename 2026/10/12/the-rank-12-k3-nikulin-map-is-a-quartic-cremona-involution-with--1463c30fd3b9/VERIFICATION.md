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

The verification target is the rational map
\[
\Phi[W:X:Y:Z]=[C W Z:C X Z:-C Y Z:D],
\]
with \(C\) and \(D\) generic homogeneous binary forms of degrees \(2\) and \(4\).

Running `python3 verification.py` under SymPy \(1.14.0\) checks exactly that
\[
C(W',X')=C^3Z^2,\qquad D(W',X')=C^4Z^4D,
\]
that the second iterate is a common scalar multiple of \([W:X:Y:Z]\), and that
\[
\det J_\Phi=4Z^2C^3D.
\]
The replay prints `VERIFY_OK` only after these symbolic identities pass.

The script does not prove squarefreeness or coprimality for special parameter values. Those are explicit hypotheses of the finding, satisfied on the very general open locus of the source family. The base-locus decomposition from these hypotheses is proved in `RESULT.md`; no finite point sampling is used.
