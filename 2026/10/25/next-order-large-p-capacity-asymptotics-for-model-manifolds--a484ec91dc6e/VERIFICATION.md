---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Set ε=1/(p−1). The radial p-harmonic equation gives Cap_p(B_R)^ε=1/I_ε with I_ε=∫_R^∞S(t)^(-ε)dt. Replacing S by C t^k e^(h t) gives C^(-ε)(hε)^(kε−1)Γ(1−kε,hεR). For t>=R the log of the multiplicative relative error O(1/t) affects hε I_ε by O(ε² log(1/ε)), genuinely smaller than the requested ε term. Γ(1−kε,hεR)=1+ε(kγ_E−hR)+o(ε), and the explicit factors give the displayed coefficient with correct h^(m−1−k) scaling. Checked both k=0 and k>0 and the fixed-radius lower-end effect. Independently numerically evaluated exact incomplete-gamma model integrals at p=1001 for multiple C,h,k,R,m examples; the limiting formula is established symbolically, not by numerical fitting.

## originality

PASS

Jin–Yin give the logarithmic high-p term and an O(1/p) remainder from coarser sphere-growth comparisons, whereas this result assumes a full relative leading asymptotic and determines the formerly unexpanded constant. The radial capacity formula and incomplete gamma evaluation are classical, not original. The specific coefficient under arbitrary C,h,k and fixed R is not in the inspected stronger general source. PASS is qualified by the possibility of an implicit general Laplace/Watson lemma making the refinement routine.

## value

PASS

The formerly unresolved O(1/p) term in a geometric capacity asymptotic becomes an explicit scale-invariant coefficient when first-order sphere growth is known, recovering the volume amplitude C and fixed radius R instead of merely geometric rank. This is a naturally motivated endpoint refinement of an existing open quantitative remainder, not an arbitrary parameter substitution; it gives a directly usable formula for a nontrivial infinite class of model manifolds. Its technical depth is limited to a careful radial Laplace/incomplete-gamma expansion, and no general nonradial theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
