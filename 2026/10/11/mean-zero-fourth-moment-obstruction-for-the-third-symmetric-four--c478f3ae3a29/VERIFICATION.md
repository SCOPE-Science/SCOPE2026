---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The explicit boundary function f_t(e^{iθ})=e^{iθ}exp(it cos2θ) is continuous, unimodular, odd and therefore mean zero. Jacobi–Anger gives Fourier coefficients of S3 f_t at n=−3,−1,1,3 equal −J2(t), iJ1(t), J0(t), iJ1(t). The squared modulus has nonzero frequency lags 0, ±2, ±4, ±6 with |g|² hat(0)=A²+2B²+C², hat(2)=−iBC, hat(4)=B²−AC, hat(6)=−iBC; Parseval gives fourth moment (A²+2B²+C²)^2+4B²C²+2(B²−AC)^2. Independent symbolic expansion from Bessel power series gives 1+5t^6/576−11t^8/2304+473t^10/460800+O(t^12); positive sixth-order coefficient proves an interval of nonzero t with norm>1. At t=1 independently checked the exact rational alternating Bessel interval bound using k=0..9 lower and k=0..10 upper and obtained certified rational lower surplus ≈0.004814465479050505; floating evaluation 1.00481446547905 agrees but is not the proof. Normalized Haar Lp monotonicity extends violation to all p≥4. S3 is a sharp symmetric projector, not the Poisson multiplier; the asserted endpoint conjecture is untouched.

## originality

PASS

The full primary 13-page Kovalev manuscript was acquired and read, including Proposition 4.1, Remark 4.3, Proposition 4.4 and Conjecture 5.1. It proves L∞ to L3 contractivity of symmetric Fourier sections; Remark 4.3 gives an S1 >3 obstruction using an input with nonzero mean; Proposition 4.4 constructs odd zero-mean data to obstruct Poisson Lp for p>4, but neither evaluates mean-zero S3 at p=4 nor states the sixth-order Bessel fourth-moment failure. The prior published Poisson endpoint-deficit result, read in full, proves a different unimodular family satisfies the finite-radius Poisson p=4 inequality; that does not entail a sharp-cutoff S3 norm. Related one-sided Riesz projection contractivity likewise has a distinct multiplier. Best-of-knowledge O PASS with residual risk of unindexed Fourier-section norm counterexamples; lack of complete priority index does not imply novelty.

## value

PASS

A rigorously certified endpoint obstruction for a precise sharp symmetric Fourier section is a motivated counterexample to a natural proof strategy arising from a current harmonic-analysis conjecture. The zero-mean and unimodular restrictions sharply distinguish it from the known S1 example and make the sixth-order loss mathematically informative. No exact operator norm, broader theorem or resolution of the Poisson conjecture is required for this correct natural negative result to be valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
