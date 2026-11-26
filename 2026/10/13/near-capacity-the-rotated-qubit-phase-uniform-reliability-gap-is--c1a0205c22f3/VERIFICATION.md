---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For fixed p in (0,1/2), write u=p−t_R, delta=C−R, A=p(1−p), L=log((1−p)/p). Derivatives give delta=Lu+u²/(2A)+(1−2p)u³/(6A²)+O(u⁴) and D(p−u||p)=u²/(2A)+(1−2p)u³/(6A²)+O(u⁴). Since L>0, u=delta/L−delta²/(2AL³)+O(delta³), giving the stated converse coefficient. As an independent check of the optimization, set q_s=p^(1+s)/[(1−p)^(1+s)+p^(1+s)]. The derivative of the negative log partition function is the cross-entropy C+L(q_s−p), strictly decreasing in s. At s=0 it is C, and at s=1 it is strictly less than C, so for all sufficiently small positive delta the unique optimizer is interior and has q_s=p−delta/L exactly. At that optimizer the objective equals D(q_s||p) by the tilt identity. Its cubic coefficient is (1−2p)/(6A²L³). Subtraction and division by the common leading quadratic term verify both gap formulas and their positive coefficients. Theorem 3 of the cited paper verifies the worst-phase converse interpretation; its Eq. (9) is the aware achievable benchmark.

## originality

PASS

The primary paper already supplies the channel, aware benchmark, phase-uniform converse and strict separation. The distinct content is the quantitative near-capacity expansion of their difference, including the first nonzero coefficient, not the strict inequality or either benchmark itself. The inspected earlier or indexed results do not give a third-order comparison or a stronger result directly containing one.

## value

PASS

The prior strict separation and the known dispersion scale do not quantify how the exhibited penalty disappears near capacity. The calculation shows the leading quadratic scale of the aware benchmark survives in this converse and cannot expose its penalty; the cubic coefficient is the first quantitative separation and gives a corresponding explicit asymptotic lower bound on the actual penalty. This resolves a motivated precision question for the source's concrete counterexample, rather than calculating an arbitrary higher-order term.

The dated certificate retains the supplied scientific assessment, sources and limitations.
