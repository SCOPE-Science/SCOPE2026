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
# Reproduction and scientific limits

Run `python3 verify.py` in the containing directory. The checker uses only the Python 3 standard library and enumerates row-reduced representatives of projective points and two-spaces for the three parameter pairs \((q,n)=(2,4),(2,5),(3,4)\). It tests exact incidence counts, common-point counts, intersection adjacency degrees, the critical-distance Euclidean identity over rational numbers, and the two critical distance eigenvalues. All three cases passed.

The arbitrary-prime-power and unbounded-dimension results are proved symbolically in RESULT.md using \(BB^\top=(r-1)I+J\), \(B^\top B=(q+1)I+A\), and scalar convexity. The finite enumeration does not certify the universal statements by itself. Literature searches, even when negative, are not proof of original priority. Independent audit and independent validation have not been performed.
