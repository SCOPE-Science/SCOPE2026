---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The official article confirms the adjacent-difference PMF and correct CDF in Eqs. (2)–(3), then labels the explicit S_c(w+1) as inclusive in Eq. (4) and divides the PMF by it. Eq. (4) also prints a spurious 1−F(w+1) equality; correctly the inclusive tail is 1−F(w−1) and the displayed numerical function is 1−F(w). Telescoping gives S_c(w) for the inclusive tail and the hazard odds identity follows by division, with h(0)=37/64 and published odds 37/27 at kappa=3. Summing the adjacent differences with weights t^w gives the inclusive-tail PGF on |t|<1, with G(1)=1 by continuity on [0,1]. The explicit series in Eq. (6) instead uses the strict tail in the inclusive-tail identity; its series corresponds to (W−1)_+, not W. At (3,1), independently summing direct and corrected series at t=.7 gives 0.8163776768708304 versus 0.9184859669583292 for the shifted series (250 terms). From S_c(w)=(2/(w+1)−1/(w+1)^2)^3, the exact mean equals 8*zeta(3)−12*zeta(4)+6*zeta(5)−zeta(6)−1 = 0.8327998896188664…, whereas the verified Eq. (9) omits 27/64. These are checks of the analytic formulas; the paper attributes Figure 2 to Eq. (4), but the plotting implementation was not verified.

## originality

PASS

The original component is the diagnosis of a particular published law's internally inconsistent survival label and consequent hazard, PGF and mean, including a quantifiable mean error and the odds interpretation. The inclusive-tail conventions, summation by parts, and tail-sum identity themselves are standard.

## value

PASS

This is not just a change of survival naming. It changes the probability interpretation and gives a value greater than one if the published odds are used as a probability; it also changes the represented distribution and nearly halves the example mean. The source uses the printed moments in its method-of-moments discussion, so the correction matters even in a regime with finite moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
