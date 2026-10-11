# Independent mathematical audit

## correctness

PASS

I independently rebuilt \(\mathbb F_{25}=\mathbb F_5(u)\) with \(u^2=3\), verified that \(1+u\) has the required order, closed the defining set to \(\{0,1,\ldots,17,20,21,22\}\), formed the degree-21 generator polynomial and its three shifts, and checked the Gram matrix is zero. Exhausting all \(5^3\) words reproduced the exact weight distribution. The 24 generator columns are all nonzero and represent 24 distinct projective points, so \(d_2=24-1=23\) and \(d_3=24\); \(d_1=19\). The 96 minimum words collapse to 24 supports modulo four nonzero scalars, and the complements form the claimed cyclic orbit.

## originality

PASS

Li--Cao--Li's complete primary article identifies the exact defining set and records only the ordinary parameters \([24,3,19]\), optimality and BCH lower bound; it does not provide the weight enumerator, projectivity, generalized hierarchy or minimum-support orbit. A separate 2026 article explicitly studies weight distributions and hierarchies for two self-orthogonal code classes, so it was treated as a serious comparison: its accessible primary article page and exact searches contain no \([24,3,19]\) match. A verified full PDF could not be obtained through the authorized fallback, so possible hidden specialization is retained as residual risk rather than assumed absent.

## value

PASS

The source advertises the code because it is optimal, while the audited result determines its entire three-dimensional support geometry: exact weights, projectivity, generalized hierarchy and cyclic structure of every minimum support. These are natural structural invariants of an optimal code rather than arbitrary extra statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
