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

The proof was checked in two independent forms.

1. **Game invariant.** After \(j\) moves, every corresponding Venn cell has equal atom count or both counts at least \(2^{q-j}\). A Spoiler split of a large cell is answered by matching any subthreshold piece exactly and keeping the other piece above the next threshold, or by splitting both resulting pieces above that threshold. At the final round, matching cell emptiness makes all Boolean-term equalities agree.
2. **Separating formulas.** The recursive formula \(A_k(x)\) splits \(x\) into disjoint parts supporting \(\lfloor k/2\rfloor\) and \(\lceil k/2\rceil\) atoms. Induction gives the intended semantics and quantifier rank \(\lceil\log_2 k\rceil\).

The standalone `verify.py` directly solves the full Ehrenfeucht--Fraisse game on the powerset representations of \(B_n\). Running it gives:

`VERIFY_OK cases=64 states=186264`

The tested range is \(1\le n,m\le4\) and \(0\le q\le3\). This finite enumeration is not used as proof of the general theorem.

Literature limits: the closest fully inspected source is arXiv:cs/0407045. An older paper, DOI 10.1016/0304-3975(80)90048-1, was available only through metadata and abstract in the checked sources, so exact full-text overlap remains unresolved.
