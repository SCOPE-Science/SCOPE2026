---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The integer rows l,lA are independent: dependence would give a rational eigenvalue of t²−qt+1, hence ±1, impossible. The induced surjective torus map preserves normalized Haar, including for nonprimitive l. The pair (u0,u1) is therefore product uniform, and q u1 modulo 1 stays uniform conditional on its q-bin. The recurrence u2=q u1−u0 mod 1 makes u2 uniform even conditional on u0 and the middle bin, proving all triple probabilities and stationarity. As a separate fourth-law check, on 000 let U=q u0 and W=q u2, independent Unif[0,1). The congruence fixes u1=(U+W)/q², since u0+u2<1. Thus u3 is the fractional part of Z=(1−q^−2)W−q^−2 U. Z has density 1/(1−q^−2) on [0,1−2/q²]; its negative portion wraps into the final bin. Since (q−1)/q≤1−2/q², each of the first q−1 output bins has mass q/(q²−1), and the last has the remaining mass 1/(q+1). Multiplying by q^−3 gives the exact cylinder vector and q=3 values, and strict entropy loss at length four follows from nonuniformity. Read the polygon verifier and its wrap bounds; it is finite corroboration, not needed for the all-q proof, and was not executed. No arbitrary nonconsecutive word law is concluded.

## originality

PASS

Credit the three-word uniformity to the already evaluated trace-divisibility result (direct for the companion and in law for every allowed sensor). The supported distinct claim is the exact fourth-cylinder vector and resulting sharp depth-four departure for the trace-matched strips, not novelty of the three-word marginal or the polygon approach. None of the strongest inspected comparators evaluates or directly implies that fourth-word vector for these strips.

## value

PASS

Trace matching is a motivated resolution in the recurring map, not an arbitrary selection of bins. Given the known short-block independence, a natural unresolved diagnostic is exactly when it fails. The explicit fourth cylinder shows the first failure uniformly across all traces and sensors, and quantifies its size rather than inferring it from entropy or asymptotics. This exact threshold and bias are useful for interpreting apparent finite-window independence of natural torus observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
