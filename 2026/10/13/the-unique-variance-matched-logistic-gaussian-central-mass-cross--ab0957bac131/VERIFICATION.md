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

Variance matching gives logistic scale sqrt(3)/pi. With a=pi/(2 sqrt(3)), H(c)=tanh(ac)-(2 Phi(c)-1), H(0)=0. The log ratio R of the positive derivatives of the two central masses has R'=S=c-2a tanh(ac), S(0)=0, S'(0)=1-pi^2/6<0 and S''=4a^3 sech^2(ac)tanh(ac)>0 for c>0. Since S' tends to 1 and S tends to infinity, R has a single strict minimum on the positive half-line. Its endpoint values satisfy R(0)>0 (pi^3>24) and R(c) tends to infinity (quadratic Gaussian exponent versus linear logistic exponent). Independently of numerical signs of R, the logistic two-sided tail is asymptotic to 2 exp(-2ac) and the Gaussian two-sided tail to 2 phi(c)/c by the Mills ratio, giving the quoted prefactor and ensuring H(c)<0 for sufficiently large c. Since H initially increases from zero, H' must be negative somewhere by the mean value theorem, so R's minimum is negative. Thus H is increasing, decreasing, then increasing to zero. The first increasing part is positive and the last is strictly negative, so exactly one positive crossing lies in the middle and the signs follow. Independent exact-rational replay, python3 /workspace/checks/2.py, uses Machin's formula with alternating arctangent bounds, outward rational square-root bounds, a positive exponential Taylor bound with geometric remainder, and integrated Gaussian Taylor remainder bounds. It certifies H(1)>0, H(2)<0, and H(1.74447161774732493)>0>H(1.74447161774732494). The Finding's decimal is supported; the bundled floating-point transcript's longer value ending in 319 is not a reliable rounding to that precision (the correct value at 15 decimal places ends in 325). This does not affect the Finding or the all-radius proof.

## originality

PASS

The closest primary literature studies exactly the same CDF-deviation equation with a tunable logistic slope and gives a numerical relation for non-origin crossings. It anticipates a crossing near the claimed location, but the available primary passages do not give or imply an exact crossing count and everywhere sign comparison at variance matching. The one-sigma theorem for the same variance normalization and the same-day exponential comparison are also non-covering. The distinct supported claim is the all-radius analytic classification at fixed variance, not discovery of logistic-versus-normal CDF deviations, standardization, or the elementary tail asymptotics by themselves.

## value

PASS

Matching variance is a standard, independently motivated way to compare coverage in common standard-deviation units. The prior one-sigma comparison does not indicate when the ordering reverses or whether it reverses repeatedly. The all-radius theorem fixes that boundary and the direction on either side, separating a precise structural result from numerical fits and isolated probability-table values. The standard tail equivalent supports the interpretation but is not the sole value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
