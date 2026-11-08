---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For Hardy normalized Berezin transform F_phi(w)=(1-|w|^2)/(1-conj(w)phi(w)), iterated Schwarz gives |phi(w)|<=|w|^m when phi has zero order m>=2, so |F_phi(w)| <= (1-r^2)/(1-r^(m+1)) <1 with fixed gap outside every small origin disk, including at r->1 limit 2/(m+1). Thus all near-Re=1 level points lie at small r. Uniform angular Taylor analysis yields 1-Re F=r^2+O(r^(m+1)), derivative 2r+O(r^m)>0, so each angular ray has exactly one small radius r=sqrt(delta)(1+O(delta^((m-1)/2))). Imaginary part at that level equals delta^((m+1)/2) Im(a_m exp(i(m-1)theta))+O(delta^((m+2)/2)); angular continuity gives the whole compact vertical interval with extrema ±|a_m|delta^((m+1)/2)+O(delta^((m+2)/2)). Its positive width recovers m from the logarithmic slope and |a_m| from the prefactor; no claim to recover phase or higher jets. Independently checked nine nonmonomial finite-delta sections, supplementary only. Correct for every analytic disk selfmap of finite zero order m>=2, not just monomials.

## originality

PASS

Best-of-knowledge originality after same-object source and implication comparisons. This result is not accepted merely because its wording differs from a prior title. Already known reductions, analytic machinery and restricted special cases are credited. Material access risks are explicitly listed.

## value

PASS

The local unparameterized Berezin range is a natural geometric invariant. Quantifying the qualitative superattracting cusp yields a sharp inverse theorem that recovers both the discrete vanishing order and continuous leading coefficient magnitude under arbitrary analytic tails. It has direct motivation from the same-model 2026 cusp/convexity question and is not merely a plot of a single monomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
