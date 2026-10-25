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

## Reproduction

Execute `python3 verify_dodeca.py` using Python 3 and SymPy. The program's final line is `COMPLETE_EXACT_DODECAHEDRON_SECTION_CERTIFICATE_OK`. It exactly enumerates 92 chambers, all 180 geodesic edges, every shared boundary type, and the two algebraic cosine values, without a numerical tolerance for the combinatorial conclusions.

## Analytic check and limits

The local spherical flux coefficient is the one-sided mean of a cosine, \(1/\pi\), multiplied by interface arclength and by the uniform surface density, \(1/(4\pi)\). The finitely many arrangement vertices yield second-order error. The checker is a finite exhaustive proof component and does not by itself certify the continuum \(t\to0\) asymptotic. No independent audit has been conducted.
