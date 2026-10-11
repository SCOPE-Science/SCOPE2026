# Independent mathematical audit

## correctness

PASS

The q=2 source/sink/interior response classification is complete above length four. At q=3, the seven pointed cases determined by distance 0,1,2 from either endpoint versus a three-deep interior give a winning two-round continuation for lengths at least eight, while an exact game check gives Spoiler a win on lengths 7 and 8. For q>=4, Brown--Hoshino's protected-gap strategy is orientation-preserving when the same signed displacement and corresponding endpoint side are copied. The undirected lower bound transfers through \(E=S\lor S^{-1}\), except the directed q=3 boundary that is handled separately. A fresh independent exact EF solver reproduced every case for \(1\le q\le3\), \(1\le n\le m\le10\), including \(P_7\not\equiv_3P_8\).

## originality

PASS

Brown--Hoshino's undirected threshold is \(7\) at rank three, whereas the audited directed successor path has threshold \(8\): in particular the undirected \(P_7,P_8\) pair is rank-three equivalent but its directed counterpart is not. That strict boundary change prevents implication-level coverage by the undirected theorem. Weis--Immerman study a different, stronger word signature and a two-variable fragment. Resultary searches found no exact unrestricted successor-only directed-path classification.

## value

PASS

The result identifies the exact effect of orientation on a canonical finite-model family: it changes precisely the rank-three cutoff while leaving the higher dyadic regime intact. Exact quantifier-rank thresholds are natural benchmarks for finite-variable distinguishability, and the P7/P8 boundary is structurally motivated rather than an arbitrary finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
