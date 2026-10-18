---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The exact phase-damping concurrence condition C_s>0 is equivalent to s|ad-bc|>(1-s^2)sqrt(|ad bc|). With four independent circular complex Gaussian coordinates before Haar normalization, the two squared product magnitudes are independent products of two exponentials. Their ratio has exact CDF F(h)=h log(1/h)/(1-h)^2-h/(1-h). On A<=B, triangle inequalities show t/(1+t^2)<=sqrt(AB)/|P-Q|<=t/(1-t^2), t=sqrt(A/B), implying a sharp phase-independent 2F(v_-^4)<=p(s)<=2F(v_+^4) for 0<s<sqrt(2)-1. Both ends expand to 8s^4 log(1/s)-2s^4+O(s^6 log(1/s)). Exact logarithmic and constant terms follow from the squeeze, not stochastic simulation. An independent partial-transpose eigensolver for 1600 Gaussian-Haar states at each s=0.1,0.35,0.7 found zero disagreements with the concurrence threshold (4800 checks).

## originality

PASS

The original 2012 source gives statewise concurrence and an integral representation for separation-time distributions. The explicit two-term small-visibility tail with logarithmic coefficient 8, constant -2 and rigorous elementary nonasymptotic bracket is a sharper endpoint result not stated in the primary full text examined.

## value

PASS

An exact nonanalytic s^4 log(1/s) survival law and rigorous finite-s enclosures quantify a physically natural long-time entanglement lifetime fraction; the distinction between logarithmic decay and a simple s^4 power law matters for statistics of noisy two-qubit memories.

The dated certificate retains the supplied scientific assessment, sources and limitations.
