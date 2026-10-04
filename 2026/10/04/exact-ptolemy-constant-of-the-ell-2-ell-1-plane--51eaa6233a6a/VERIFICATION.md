---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof was replayed symbolically from the stated norm.

1. On \(uv\ge0\), \(|u-v|\le\sqrt{u^2+v^2}\); on \(uv\le0\), \(|u-v|=|u|+|v|\). Hence \(\|\cdot\|_{2,1}=\max\{E,F\}\) exactly.
2. The sharp global comparison \(F\le\sqrt2\,E\) follows from Cauchy--Schwarz.
3. \(E\) obeys Ptolemy because it is Euclidean. \(F\) obeys the same four-point inequality because it is the pullback of the absolute-value metric on \(\mathbb R\) under \((u,v)\mapsto u-v\).
4. The four active-branch combinations in the two numerator factors reduce to two same-branch cases with factor \(1\) and two mixed cases with factor at most \(\sqrt2\).
5. For \(x=(a,0)\), \(y=(0,a)\), \(z=(a,a)\), \(a>0\), direct substitution gives the ratio \(\sqrt2\).

No numerical experiment, finite enumeration, or inaccessible external lemma is required for correctness. The only stated limitation concerns literature coverage, not the proof.
