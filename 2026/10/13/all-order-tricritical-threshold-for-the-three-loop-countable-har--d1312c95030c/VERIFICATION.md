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

Checked the normalized equations for the star with loops at 0,1,2 against source §5. For z1>z2, r=(1+z1)/(1+z2)>1 and z1=r^k z2 give z2=(r−1)/[r(r^(k−1)−1)]; r=e^(2s) gives the two recorded hyperbolic formulas reversibly. Substitution gives c_k; the sum of nonloop coordinates is (Λ−2λ)/S^k, proving the total-activity formula and the strict positivity criterion S>m. Conversely for any positive summable activities with this total the reconstructed law solves every coordinate. At s=0, m=(k+1)/(k−1), c=c_*, and an admissible local merger requires λ>λ₀ as used in the orientation statement. For the independent expansion use m=sinh((k+1)s)/sinh((k−1)s) and a=c_k/c_*. Then (Λ−2λ)/(λ/c_*)=S_*a^(−1−1/k)−ma^(−1). The log-sinh Taylor series gives the recorded quadratic term, vanishing at S_*=k(3k+1)/[3(k−1)^2], and the quartic there divided by λ_*/c_* is −k(k+1)(37k²+110k+37)/[1080(k−1)]. The symbolic replay `python3 /workspace/branches/independent-checks.py 1` confirms these identities with symbolic k, not finite extrapolation. This root yields λ_*>λ₀. For λ>λ_* the curve first rises; since S grows like e^(2(k−1)s/k) and m like e^(2s), a first zero of S−m exists and the continuous extension there equals 2λ<Λ_c. The maximum is interior, and every level strictly between Λ_c and that maximum has a crossing on each side. They yield two unequal oriented laws and both reversals. The symmetric self-consistency residual tends to +∞ at z→0 and −∞ at z→∞ since S(z)=λ^(1/k)(1+z)z^(−1/k)=o(z) at infinity. All five laws are in ℓ¹, hence ℓ^((k+1)/k), so the source's normalizability and injectivity for normalized laws give five distinct measures. The checker and frozen record of verification were inspected, not executed. The result is local in the threshold and a lower bound in count, not a global uniqueness, stability, or extremality claim.

## originality

PASS

The same-model paper already has the general equations, the binary value 49/9, and an exact binary five-measure interval; these are not new. The supported extension is the all-order local threshold with signed quartic and a proved coexistence interval for general k. Leading distinct comparators concern different graphs, control variables or classes of laws, not an equivalent all-order theorem for this graph.

## value

PASS

The binary constant is explained by an explicit all-order sign change, including the actual direction at its degenerate setting. The same curve then yields a concrete coexistence conclusion for every tree order, beyond presenting a normal form or a few finite examples. The threshold concerns local branch orientation, not thermodynamic dominance, and the interval does not imply an exact global count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
