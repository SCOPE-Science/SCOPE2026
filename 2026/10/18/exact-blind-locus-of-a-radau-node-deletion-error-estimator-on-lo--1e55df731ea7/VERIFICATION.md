---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Using the specified two-stage Radau IIA Q and c, deletion-indicator zero forces an affine collocation polynomial a+bt. Equal logistic derivatives imply U1=U2 (excluded by h>0,a∈(0,1)) or U1+U2=1. Solving yields h=12(1-2a)/((1+2a)(3-2a)), U1=(1+2a)/4, U2=(3-2a)/4 with positive h iff a<1/2. The true logistic hitting time H(s)=2atanh(s)+2atanh(s/2) exceeds h(s)=12s/(4-s²) by strictly positive coefficients from s^5; thus true endpoint below U2 and max absolute error supremum 3/4 as a→0. Independently recomputed resultant 192(3x-1)(81x³-27x²-26x-8) at (a,h)=(1/6,9/4); x<=77/192 rules out cubic for [0,1]^2, and y=2/3 is unique. Fourteen rational parameter values verified with exact substitutions. No solver-convergence statement is inferred.

## originality

PASS

Best-of-knowledge new claim is precisely the exact right-Radau/logistic one-parameter blind locus, strictly positive true error and sharp supremum with bounded-stage uniqueness witness. Saupe et al. introduce the deletion-interior-stage indicator in adaptive SDC, but no evaluated logistic zero-error-signal locus is in the inspected method/source. Related spurious-equilibrium and Fehlberg/Simpson failure precedents concern different equations/estimators; an unindexed special analysis remains a priority risk.

## value

PASS

A physically bounded and even uniquely positive-stage collocation root produces a zero local indicator yet a sharply order-one actual endpoint error. The complete if-and-only-if curve and 3/4 supremum give a mathematically diagnostic counterexample for assessing the reliability of node-deletion step controllers; not a generic caution based only on numerical coincidences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
