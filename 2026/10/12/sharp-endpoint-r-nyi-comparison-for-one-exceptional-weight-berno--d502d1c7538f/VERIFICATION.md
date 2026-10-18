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

For S=sum_{i=1}^n B_i+a B_{n+1}, a real, n>=1, we checked the partition: a=0 (n+1 points, modal mass c_n); a noninteger or |a|>n (2(n+1) disjoint points, modal mass c_n/2); integer |a|=k in [1,n] gives contiguous support n+k+1 and masses [binom(n,j)+binom(n,j-k)]/2^(n+1). The binomial estimates (n+1)c_n²<=3/4 and (n+floor(n/2)+1)c_n²<=1 follow via exact consecutive ratios; strictness for n=2,k=1 is direct. For k>floor(n/2) and n>=20, the proved Gaussian ratio bound p_n(j)<=c_n exp(-d(j)^2/n) implies M<3c_n/4, so K M²<27/32. Independently recomputed all 190 integer pairs with 1<=n<=19, inspecting exactly 3990 atom positions, exact worst ratio 3/4 at (n,k)=(1,1); this finite bridge exhausts the only unproved region, not the infinite n argument. Central binomial asymptotics with a=0 give H0/Hinf->2. Symmetry a versus -a and all real collision cases checked.

## originality

PASS

Li (2026) states the endpoint coefficient 2 for all weighted fair Bernoulli sums as Conjecture1.1, proves coefficient 2 at Rényi order α>=1/2 in Theorem1.4 and a weight-dependent LOGARITHMIC endpoint constant in Theorem1.5; neither implies the claimed sharp fixed endpoint coefficient for this infinite one-exceptional-weight family. Jain–Sah–Sawhney obtain weaker general anti-concentration bounds. The result is genuinely a structured family, not a claim to solve the general conjecture.

## value

PASS

Verifies a natural, infinite, continuously parametrized subfamily of a specific current extremal Rényi-entropy conjecture, across all n>=1 and exceptional real weights, with the conjectured strict endpoint factor and asymptotic exponent optimality. Support collisions at integral exceptional weights make the result substantive rather than a generic concentration estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
