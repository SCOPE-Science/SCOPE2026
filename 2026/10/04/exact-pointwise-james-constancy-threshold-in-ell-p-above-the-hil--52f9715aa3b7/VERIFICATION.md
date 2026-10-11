---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For \(t\ge p\), taking \(y=x\) at any unit base point gives the value \(M_t(0,2)=2^{1-1/t}\), which is already the published global \(\ell_p\) James-type maximum, so every base point has exactly that value. For \(t<p\), the balanced vector \(u=2^{-1/p}(e_1+e_2)\) with the Hanner partner \(v=2^{-1/p}(e_1-e_2)\) attains the global branch \(2^{1-1/p}\). At \(e_1\), writing \(a=|y_1|\) reduces the two chord lengths to \(A(a)^p=(1+a)^p+1-a^p\) and \(B(a)^p=(1-a)^p+1-a^p\). Strict Clarkson inequality gives \(M_p(A(a),B(a))<2^{1-1/p}\) for every \(a<1\); monotonicity of power means gives the same strict inequality for every \(t<p\), while the endpoint \(a=1\) gives \(M_t(2,0)<2^{1-1/p}\). Continuity on the compact interval makes the pointwise supremum at \(e_1\) strictly smaller, proving nonconstancy. The packaged sampler agrees with the reduction but is not used as an infinite proof.

## originality

PASS

The complete 2023 primary paper defines the pointwise James-type profile, proves orbit invariance, continuity and constancy on almost/convex-transitive spaces, and in Example 3.7 records the global \(\ell_p\) profile. It does not classify pointwise constancy on non-Hilbert \(\ell_p\). The audited threshold is not a title-level restatement: below \(p\), \(\ell_p\) is not covered by the transitivity theorems and the strict coordinate-versus-balanced comparison is required. Current Resultary searches returned the assigned statement as the exact pointwise threshold hit and neighboring generalized/global James constants, but no stronger pointwise theorem containing it.

## value

PASS

The pointwise James profile was introduced specifically to distinguish base-point geometry from the usual global constant. Determining exactly when that dependence disappears in the canonical non-Hilbert \(\ell_p\) family is a natural structural classification. The low-side strict separation shows a genuine pointwise phenomenon rather than merely rewriting the global constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
