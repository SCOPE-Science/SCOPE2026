# Minimal projective-plane blockers: a five-versus-six shattering gap with point-transitive amplification

## Finding

Let \(\Pi=\operatorname{PG}(2,3)\) be the ternary Desarguesian projective plane. Define \(\mathcal B\) to consist of **all inclusion-minimal subsets of points meeting every projective line** (including sets that are themselves lines). Regard each member of \(\mathcal B\) as a Boolean concept with point-membership queries. Then
\[
|\mathcal B|=247,\qquad \operatorname{VCdim}(\mathcal B)=5,\qquad \operatorname{Ldim}(\mathcal B)=6.
\]
The full concept class comprises thirteen four-point lines and 234 six-point projective triangles, each triangle being the union of the three open sides of a nonconcurrent triple of lines.

For a query support \(S\), let \(t(S)=|\{B\cap S:B\in\mathcal B\}|\). The **complete trace spectra for support sizes three through six** are as follows. Each entry is \(t: \text{number of supports with }t(S)=t\):

| \(|S|\) | Complete spectrum |
| --- | --- |
| 3 | \(8:286\) |
| 4 | \(15:13,\ 16:702\) |
| 5 | \(29:117,\ 31:468,\ 32:702\) |
| 6 | \(56:468,\ 57:78,\ 60:936,\ 61:234\) |

A five-point set is shattered **exactly when it is obtained by deleting one point from a six-point projective triangle**. There are 702 such sets, and every one has exactly two distinct projective-triangle completions. No six-point set is shattered.

For \(\operatorname{PG}(2,2)\), the corresponding class has seven minimal blockers and \((\operatorname{VCdim},\operatorname{Ldim})=(2,2)\); hence order three is the first Desarguesian projective-plane order with the strict separation.

For every integer \(m\ge1\), form a hypergraph \(\mathcal H_m\) from the disjoint union of \(m\) copies of the point-line hypergraph of \(\operatorname{PG}(2,3)\). This hypergraph is linear, four-uniform, four-regular and point-transitive. The concept class of its inclusion-minimal transversals satisfies
\[
|\mathcal B(\mathcal H_m)|=247^m,\qquad
\operatorname{VCdim}(\mathcal B(\mathcal H_m))=5m,\qquad
\operatorname{Ldim}(\mathcal B(\mathcal H_m))=6m.
\]
The gap is thus unbounded in this symmetric hypergraph class. The hypergraph is disconnected for \(m>1\).

## Assumptions and scope

Points of \(\operatorname{PG}(2,3)\) are nonzero vectors in \(\mathbf F_3^3\), modulo nonzero scalar multiples. Lines are kernels of nonzero linear functionals modulo scalars. There are thirteen points and thirteen lines; each line contains four points; each point lies on four lines; two distinct lines meet at exactly one point. A hitting set \(B\) is minimal if deleting any element causes some line to become unhit. Equivalently, every \(p\in B\) lies on a line meeting \(B\) only in \(p\). This equivalence is elementary and constitutes the exhaustive finite test.

The VC dimension is the greatest \(d\) for which some \(d\) points realize all \(2^d\) membership traces. The Littlestone dimension is the greatest depth of a complete binary membership-query decision tree for which each root-to-leaf path is consistent with at least one concept; branches have answers zero and one. Queries along a root-to-leaf path may be taken distinct because a repeated point cannot contribute a consistent binary split.

## Proof

**Finite classification and traces.** Normalize each projective point by requiring its first nonzero coordinate to equal one. The supplied `verify.py` independently reconstructs the thirteen projective lines as the solutions to normalized nonzero ternary linear functionals. It enumerates all \(2^{13}=8192\) point masks and retains exactly those meeting every line and having the stated witness line at each selected point. It gets exactly 247 sets, comprising 13 lines and 234 six-point sets. It independently enumerates all nonconcurrent triples of lines and checks that their three open-side unions are exactly the 234 six-point blockers. This enumeration is exhaustive rather than a sampling argument.

For every support of cardinality three, four, five and six, compute its complete collection of membership traces against every enumerated blocker. The program iterates, respectively, over all \(\binom{13}{3}=286\), \(\binom{13}{4}=715\), \(\binom{13}{5}=1287\) and \(\binom{13}{6}=1716\) supports, establishing the table. The five-point spectrum gives a shattered support, while the six-point spectrum gives no shattered support. A larger shattered support would have a shattered six-point subset, proving \(\operatorname{VCdim}=5\). The same exhaustive comparison shows that the 702 shattered supports are precisely all triangle-minus-one-point sets. Counting extensions yields exactly two triangles per such support. The independent affine-coordinate program `independent.py` reconstructs the design differently and reproduces the complete spectra and the online rank.

**Adaptive lower bound.** In `certificate.json`, `adaptive_tree` contains a complete depth-six membership-query tree, with 63 internal nodes and 64 distinct terminal blocker masks. `verify.py` recursively checks every node, both children, every root-to-leaf assignment, and the membership of its terminal blocker in the independently reconstructed 247-element class. Therefore every path is realized and \(\operatorname{Ldim}\ge6\).

**Adaptive upper bound.** Every blocker above has at most six points. If a depth-seven tree were shattered, its all-positive path would demand seven distinct query points included in one blocker; repetition of a query cannot split both descendants consistently. This is impossible, so \(\operatorname{Ldim}\le6\).

**Fano control case.** An independent enumeration on the seven points of \(\operatorname{PG}(2,2)\) gives precisely its seven three-point lines as minimal transversals. Every two-point support has four traces. A three-point support cannot be shattered with only seven concepts, so VC dimension equals two. The hypothesis-count bound \(\operatorname{Ldim}\le\lfloor\log_2 7\rfloor=2\), together with the two-point shattered support, yields Littlestone dimension two.

**Amplification and symmetry.** A transversal of a disjoint union of hypergraphs is inclusion-minimal exactly when its restriction to each component is inclusion-minimal. Hence the concept class is a Cartesian product over disjoint query sets. VC dimensions add by taking unions of shattered supports and restricting any shattered set to its components. Littlestone dimensions add as well: concatenate shattered trees for the lower bound. For the upper bound use induction on nonempty version spaces in the standard splitting recurrence \(\operatorname{Ldim}(C)=\max_q(1+\min\{\operatorname{Ldim}(C_{q,0}),\operatorname{Ldim}(C_{q,1})\})\), ignoring empty splits. A query in one component splits only that component; the inductive sum bound gives the upper bound for the product. Each component has automorphisms acting transitively on points, and permutations of components preserve incidence, making the disjoint union point-transitive. Uniformity four, degree four, and pairwise edge intersection at most one follow componentwise.

## Verification

Run `python3 verify.py certificate.json` and `python3 independent.py` from a directory containing these files. Both use only the Python standard library. The certificate contains all thirteen normalized projective points, all thirteen line masks, the 247 minimal blocker masks and the explicit depth-six tree. The first program reconstructs incidence and every mask, checks complete spectra, triangle extensions and every adaptive witness. The second uses affine coordinates and independent minimality and online-dimension calculations. Expected terminal markers: `ALL_PROJECTIVE_BLOCKER_SHATTERING_CHECKS_PASS` and `ALL_AFFINE_INDEPENDENT_CHECKS_PASS`.

## Relationship to prior work

Coolsaet, Botteldoorn and Fack (2022) already classified minimal blocking sets of small Desarguesian planes up to equivalence. Their geometric enumeration, including the small-plane blocker objects, is prior work and is **not** claimed here as new. The present claims concern exact static/adaptive query-learning dimensions, complete trace spectra, a geometric characterization of shattered supports, an explicit adaptive certificate and unbounded point-transitive hypergraph amplification. Mary's 2024 preprint studies algorithms to enumerate minimal transversals of bounded-VC hypergraphs, not the query-learning dimensions of their transversal concept classes. Neither source's accessible description entails these dimensions. The complete original article of Coolsaet and collaborators was not accessible for line-by-line comparison; historical-priority assessment is accordingly qualified.

## Limitations

The computation proves exact results only for the stated finite planes, not a general formula for all projective orders. The amplified hypergraphs are disconnected when the number of components exceeds one. Classification of minimal blockers in small planes is existing literature; neither the bare number 247 nor the existence of projective triangles is presented as a novel result. The main historical classification source's full text could not be inspected, so an undiscovered equivalent statement remains a residual originality risk. There has been no independent external mathematical audit.

## References

1. K. Coolsaet, A. Botteldoorn, V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, Journal of Combinatorial Designs 30 (2022), 561–580. First published 2022-03-31. DOI: 10.1002/jcd.21842.
2. A. Mary, *Enumeration of minimal transversals of hypergraphs of bounded VC-dimension*, arXiv:2407.00694, initially posted 2024-06-30.
