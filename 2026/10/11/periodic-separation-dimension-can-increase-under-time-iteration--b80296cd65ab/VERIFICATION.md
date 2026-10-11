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

The exact-rational checker \(\texttt{check.py}\) recomputes Euclidean squared gaps over every unordered pair of points in each finite shell for \(q=2,\dots,6\) and \(m=2,\dots,12\). It independently enumerates the full orbit and the \(q\) shorter orbits of the \(q\)-th iterate, and checks vertical shell separation at indices through \(30\). With the Python standard library it prints \(\texttt{PASS 420 exact rational diagnostics}\).

The universal inequality, compactness of the union, continuity at the sole limit point, exact all-index gap claims, entropy zero, and the asymptotic content limits are separately proved in \(\texttt{RESULT.md}\). Finite tests cannot establish any of those infinite statements by enumeration alone.

The primary literature comparison is limited by incomplete access to later sections of the 19-page source preprint. No independent audit or external certification has been performed.
