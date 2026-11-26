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

Write z=e^(−μ) and a=μ/[2(1+μ)]. The defining PMF equals (b+c y)z^y, where b=1−(1+a)z>0 by e^μ>1+μ and c=a(1−z)>0. Hence the difference telescopes to total mass 1 and P(Y>=k)=(1+ak)z^k. Summing the nonnegative increments of k^r gives the raw moment identity; the weights 1 and 2k−1 for r=1,2 with the three elementary geometric sums give the printed corrected moments. The PGF equals b/(1−zs)+c zs/(1−zs)^2, algebraically the frozen form; c>0 leaves an uncancelled pole of order two. Equivalently p_y~c y z^y, so the MGF converges for t<μ and its terms do not tend to zero at or above μ. At μ=1 independent direct summation gives mean 0.8121451054212745, second raw moment 2.0253494665568038 and variance 1.3657697942970708 (rounding). Reading the original PDF and transcribing Eqs. (18), (21), (22) gives 0.4904943422160591, 1.5084302478481624 and 1.2678455481021979 respectively; they cannot be alternate forms of the PMF moments. `python /workspace/audit_checks_1_5.py 2` independently sums PMF weights and verifies the corrected formulas. The five claimed Table 1 rows at μ=0.5,0.8,1,1.5,2.5 agree at printed precision. The μ=0.1 row is not recovered (even the printed mean 14.024 differs from 14.0500005); the frozen claim scopes the check to selected rows, not the whole table. The exponential-moment conclusion uses the stipulated standard probability meaning of light-tailed, not a claim about informal shape comparisons or larger kurtosis.

## originality

PASS

The supported distinct claim is a source-specific correction: the primary paper's analytic moments contradict its own defining PMF and selected numerical results, and its advertised heavy-tail language needs the formal tail qualification. The general tail-sum and geometric-series techniques are not new. No already corrected DZL statement was identified by the bounded checks; the corrigendum lookup was unavailable and does not count as a negative result.

## value

PASS

The correction resolves a large numerical disagreement in the first moment and incompatible second-moment/variance prescriptions for a recently proposed distribution. Those errors matter for users calibrating or interpreting the model; the exponential-moment cutoff also distinguishes formal tail behavior from finite-range skewness or kurtosis. The contribution is the explicit, verified correction of the underlying model paper, not a routine derivation presented as a new general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
