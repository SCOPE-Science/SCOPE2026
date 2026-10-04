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

The proof was replayed from the printed vector field. For \(H=-z+(k+2)x^2/(2a)\), exact expansion yields \(\dot H=b-(k+1)x^2-(y-x)^2\), and the first equation converts the last term to \(\dot x^2/a^2\). The invariant-measure step uses only \(\int LH\,d\mu=0\) for a compactly supported invariant measure and a polynomial \(H\).

The bundled checker uses exact rational arithmetic for the source parameters. It verifies \(k+1=28/5\), \(b/(k+1)=125/7\), and \(1/(a^2(k+1))=5/4032\), and it checks the polynomial identity coefficient by coefficient. Its successful terminal output is `VERIFY_OK`.

Limits: the checker is an algebra replay, not an independent audit and not a numerical existence proof for the chaotic attractor. The equality-rigidity argument is established in the proof, not inferred from the checker.
