# Independent audit — 2026-10-01

## Final claim

Exact dimension-three four-request all-symbol code lengths

## Disposition

**Passed.** Correctness, originality, and value all pass for the final claim as stated in `RESULT.md`; no claim repair is required.

## Correctness

Assuming an odd-characteristic length-seven rank-three four-all-symbol PIR realization, the known \(ASP(2,4,q)=6\) and Lemma 16 force pairwise distinct columns. A zero column can be deleted without affecting recovery of the remaining symbols, contradicting the length-seven lower bound; proportional columns can be rescaled to equality without changing subset spans, contradicting Lemma 16. Thus the seven columns are distinct projective points. For each point, three disjoint non-singleton recovery sets partition the other six points into three collinear pairs, forcing every selected secant to contain three points; a five-point secant is impossible. Hence the incidence is the Fano plane, whose coordinate realization forces characteristic two. The source's length-eight construction gives the matching odd-characteristic upper bound. Independent reimplementation verified all 210 four-request multisets of the displayed length-eight matrix over each of \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), and enumerated all 1,716 spanning seven-subsets of \(PG(2,3)\), finding zero with the required local matching property.

## Originality

The primary 2026 paper gives the one-column gap for \(t=4,k=3\), proves value seven in characteristic two, and explicitly lists exact \(t=4\) values and alphabet dependence as future directions. No prior source found in all-symbol, disjoint-repair-group, availability, projective-geometry or Fano terminology states the odd-characteristic lower bound. The classical Fano representability obstruction is prior and is not claimed as new.

### Equivalent formulations

Searches:
- Resultary semantic search for ASP(3,4,q), all-symbol PIR/batch, Fano and odd characteristic
- Web searches for exact all-symbol four-request dimension-three lengths and projective/Fano reformulations

Evidence:
- Resultary's exact hit was this record; the closest later Fano-related SCOPE result concerns rank-three fooling-set matrices, a different invariant.

Reasoning: The contribution is the reduction from an optimal all-symbol PIR recovery structure to Fano incidence, not the classical representability theorem itself.

### Broader coverage

Searches:
- Boruchovsky, Gruica, Niemann and Yaakobi, arXiv:2601.04041 full text
- Li and Wootters, APPROX/RANDOM 2019 disjoint-repair-group framework
- Mendez, Rincón and de la Peña, Linear Algebra Appl. 478 (2015) for Fano representability background

Evidence:
- The primary all-symbol paper gives Theorem 20 bounds, Lemma 16 distinctness, Proposition 24 for characteristic two, and explicitly leaves the \(t=4\) gap/alphabet dependence open. The older works provide broader recovery or matroid background, not this exact parameter value.

Reasoning: No broader theorem inspected mechanically yields \(ASP(3,4,q)=8\) for every odd-characteristic field.

### Exact database or table

The audited value closes a missing table entry by proof; it is not a recomputation of a known table.

Searches:
- Searches for exact ASP/ASB parameter tables at \((k,t)=(3,4)\) and odd q
- Inspection of the primary paper's \(t=4\) section and Discussion/Future Directions

### Claim versus prior implication

The Fano-incidence argument supplies the missing strict exclusion of length seven in odd characteristic; the prior bounds do not imply it.

Evidence:
- Those results imply only \(7\le ASP(3,4,q)\le ASB(3,4,q)\le8\) in odd characteristic and value seven in characteristic two.

### Source inspections

- **Serving Every Symbol: All-Symbol PIR and Batch Codes** — OPEN_GAP_NOT_COVERING. Material read: Full text around Lemma 16, the \(t=4\) section/Theorem 20, Proposition 24, and Discussion/Future Directions. Evidence: The source leaves exact \(t=4\) values and alphabet dependence open and does not prove the odd-characteristic dimension-three lower bound. Source: https://arxiv.org/abs/2601.04041
- **Completion and decomposition of a clutter into representable matroids** — BACKGROUND_COMPONENT_ONLY. Material read: Bibliographic/result-level scope as cited by the record. Evidence: The Fano representability fact is prior; it does not connect all-symbol recovery sets to Fano incidence. Source: https://doi.org/10.1016/j.laa.2015.01.023

### Residual risks

- Older majority-logic/disjoint-repair literature uses overlapping language, but no inspected result implies this exact all-symbol parameter value; the 2026 primary source itself presents the case as unresolved.

## Value

The result closes the smallest unresolved odd-characteristic \(t=4\) case in a newly introduced code family and yields a complete dimension-three classification with a sharp characteristic dichotomy. The Fano obstruction is structural rather than a brute-force small-field census, while the finite checks serve only as reproducibility support.

## Limitations

The exact classification concerns linear all-symbol PIR/batch codes of dimension three with four requests; the Fano representability fact itself is classical, and older disjoint-repair/majority-logic literature remains a residual terminology-coverage risk.
