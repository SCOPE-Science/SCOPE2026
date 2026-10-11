---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The primary paper's Theorem 4.2 proof was reconstructed from the displayed generator. At the AM--GM step the three factors are \(aA/S(t)\), \(beta e^{-\lambda	au}S(t-	au)/(1+\kappa I(t-	au))\), and \(1+\kappa I(t)\), whose product contains the omitted factor \(ho(t)=rac{S(t-	au)}{S(t)}rac{1+\kappa I(t)}{1+\kappa I(t-	au)}\). The theorem's initial-history domain supplies no lower bound \(ho(t)\ge1\). For the submitted exact history, \(I(t-	au)=I(t)\), so an earlier dropped infected-state ratio in the paper is neutralized; direct rational reconstruction gives \(a=80/9\), \(b=16/3\), \(\widetilde{\mathcal R}_0^S=80/21>1\), \(\mathcal LU=2486393/90900\), and the printed state-independent post-AM--GM expression \(-8761/900\). Thus the asserted upper bound is false on an admissible positive history. The final claim correctly stops at proof failure and does not infer that the persistence theorem itself is false.

## originality

PASS

The final claim is a source-specific correction to a concrete printed inequality. Full inspection of the primary article confirms the exact AM--GM step and the unrestricted positive-history domain. Fresh DOI/title/erratum and Resultary searches found the article and unrelated delay results but no published correction of the omitted ratio. General delayed-epidemic persistence theorems are inapplicable to originality of this statement-level correction because they cannot make this displayed inequality valid. Best-of-knowledge originality therefore passes, while an unindexed erratum remains a residual risk.

## value

PASS

The omitted factor is structurally tied to the delay and occurs at the step producing the theorem's state-independent negative drift. The exact admissible history reverses the claimed upper-bound ordering while the stated threshold exceeds one, so the correction materially affects the proof of a headline persistence result rather than only notation or a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
