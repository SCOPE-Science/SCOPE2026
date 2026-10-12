# Review of algebraic local conicality for banana graph hypersurfaces

## Correctness — PASS

The statement is quantified over integers \(n\ge4\) and closed complex points on \(X_n\) with at least three zero homogeneous coordinates. The central unit-normalized identity is exact on the appropriate projective chart, and the substitution \(y=x_k/(1+cx_k)\) is invertible on a Zariski neighborhood because both denominators evaluate to \(1\) at the point. Algebraic product, formal local ring, Hilbert series, and singular stratification follow by direct computation. Irreducibility and Serre's criterion establish normality. The checker passes 1,002 support tests, 176 identity tests, and 135 Hilbert tests. These tests are corroboration; the symbolic identities establish infinite coverage. The derivation is not sensitive to nonzero-coordinate values.

## Originality — PASS, with residual risk

Aluffi–Marcolli, *Feynman motives of banana graphs* (arXiv:0807.1690, equation (1.28), Lemma 3.8), contains the graph polynomial and boundary incidence. Patterson, *On the Singular Structure of Graph Hypersurfaces* (arXiv:1004.5166, Theorem 4.13, Proposition 4.17 and Example 4.19), already covers multiplicity and tangent-cone information; these are excluded as stand-alone novelty claims. The specifically assessed fact is an invertible Zariski-local algebraic coordinate change that removes all higher-order terms uniformly at all singular closed points, which is stronger than knowing a tangent cone. Direct inspections and published-record searches did not locate the same analytic-equivalence theorem. Residual risk: other literature could contain the explicit specialization, and no search certifies historical uniqueness.

## Value — PASS

Local analytic/contact type, unlike tangent cone alone, controls the entire completed local ring and shows that all higher-degree corrections in the ambient graph equation are geometrically removable. A single formula uniformly describes generic nodes, higher-multiplicity intersections, and all other singular closed points in every degree. It supplies an exact stratum-compatible local model for further invariants or stratified analysis, rather than a small numerical recomputation. It is deliberately restricted to this motivated classical family.

## Limitations

Only the stated banana graph hypersurfaces and closed complex points are covered. The coordinate changes need not glue globally; numerical tests alone are never used as proofs; an unindexed equivalent algebraic trivialization remains possible. Not independently audited.

Self-review: passed. Independent audit: not yet performed.
