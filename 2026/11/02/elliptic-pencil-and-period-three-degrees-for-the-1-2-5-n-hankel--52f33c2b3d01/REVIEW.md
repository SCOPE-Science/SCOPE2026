# Independent mathematical audit

## correctness

PASS

On the generic complex rank-two Hankel recurrence with a0=1,a1=b,a4=c, the intermediate curve is P²-(S²+2bS)P+bS³-c=0 and Y²=S⁴+4b²S²+4c, a smooth genus-one double cover when b,c,c-b⁴ are nonzero. The affine recurrence parameters are birational on the generic rank-two locus. At the two points above infinity, a_{4+k} has pole orders k+4 (or k+3 if 3 divides k) and k; the drop comes from a simple zero in the Lucas recurrence h_k(1). There are no other poles as all moments are polynomials in the recurrence parameters on the affine curve. Degree of the finite rational function is total polar order. Thus for every n>=6 degree is 2n-7 when n=2 mod 3, 2n-6 otherwise. Independent SymPy eliminants at generic specializations n=6..9 recovered the formula; these finite checks only corroborate the valuation proof.

## originality

PASS

Reed and Tsakiris establish uniformity and an upper bound on Hankel coordinate projection degree and tabulate nearby third-index patterns, but their inspected Theorem 5 and Remark 7 do not determine an all-n exact degree for the sampling pattern {1,2,5,n}. General Prony/decimation stability results use primarily arithmetic progressions and do not directly imply the genus-one pole loss. Novelty assessed for this specific nonarithmetic pattern, not generic recurrence geometry.

## value

PASS

Exact generic completions for a natural four-moment sample pattern refine a general bound with an unexpected residue-three phenomenon explained geometrically by missing leading pole terms on a genus-one fiber. This resolves a meaningful enumerative algebraic-matroid question for every n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
