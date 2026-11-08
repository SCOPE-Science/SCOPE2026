---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For simple C_n with n>=5, every vertex outside L has nonempty neighboring-L signature iff cyclic 000 is absent. A repeated nonempty signature for two zeros is necessarily shared singleton central 1 in 00100; similarly reverse complement side uses 111 and 11011. Alternating zero/one runs each have length 1 or 2; permitted run transitions yield two explicit transfer matrices with determinant polynomials P_A=1-tz²-t²z³-t²z⁴-t²z⁵-t³z⁶ and P_B=1-tz²-t²z⁴-(t²+t³)z⁵-t³z⁶-t⁴z⁸. The cyclic trace identity -z d_z log det(I-T) counts vertex-labelled words with correct n/k root factors. At t=1 each supported exponent set has gcd 1, so unique simple minimal positive pole; P_B(alpha)-P_A(alpha)=alpha³(1-alpha²-alpha⁵)>0 for alpha<2/3, implying beta>alpha and b_n/a_n~(alpha/beta)^n. Independent direct neighborhood enumeration over all 2^n masks for n=5..13 agrees with both univariate determinant coefficients; the bivariate formal proof is the transfer-matrix argument, not these finite tests.

## originality

PASS

Chakraborty–Foucaud–Henning–Laihonen 2026 establishes existence of dominating/LD partitions in isolate-free graphs, not their cardinality generating polynomials or asymptotic scarcity on cycles. Other LD-partition graph-class papers address existence. OEIS A001636 already includes the unweighted A_n(1) sequence and is not claimed new. Distinct novelty is two-sided size-resolved B_n(t), joint comparison and exponential ratio.

## value

PASS

The exact size-marked counts for both kinds of identifying partitions and their strictly different growth rates answer a natural enumeration question motivated by 2026 graph-partition existence results. The exponential scarcity constant provides a useful asymptotic distinction that cannot be read from existence alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
