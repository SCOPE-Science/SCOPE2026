# Scientific assessment

## Correctness — PASS

The stated claim is restricted to the smooth characteristic-five members of the marked reciprocal genus-four hyperelliptic family. Factoring the reciprocal quintic through the coordinate \(z=t+t^{-1}\) yields the explicit squarefree criterion. Coefficient extraction from the square of the degree-ten branch polynomial yields a Cartier matrix splitting into two conjugate \(2\)-by-\(2\) blocks, each with determinant \(D\). The second twisted Cartier iterate, using the appropriate semilinear order, reduces the rank-one case to \(N\); the ranks \(0,2,4\) and \(a\)-numbers \(2,0\) follow without assuming anything about Newton slopes.

Exact polynomial elimination gives the degree-six irreducible factor and the four exceptional rational first-coordinate values. Common-root calculations exclude all but the one smooth rational pair and show that each root of the irreducible factor gives exactly one smooth marked parameter. The included symbolic checker independently reproduces the asserted polynomial identities and enumerates every pair over the base field. All algebraic closures and extension counts are justified by the elimination/irreducibility argument, not by finite sampling.

## Originality — PASS, with residual risk

The family itself is explicitly taken from Ohashi--Kudo, arXiv:2312.16858v1, equation (3.6), and is not new. The inspected original article addresses superspecial curves and their classification principally in characteristics at least seven. It does not assert the complete rank-zero locus in characteristic five. The related superspecial census cannot cover the conclusion by implication, since a curve can have \(5\)-rank zero without being superspecial. The Hasse--Witt conventions of Achter--Howe are known technical background, not a novelty claim. Targeted searches did not identify an existing classification with the same characteristic, marked parameters, and three Cartier-rank regimes. An earlier unindexed computation or isomorphic reformulation remains a genuine residual risk; a negative search is not a proof of uniqueness in the literature.

## Mathematical value — PASS

The arithmetic of a classical low-dimensional automorphism-rich hyperelliptic family is a natural problem. In the exceptional small characteristic five, the explicit determinantal and Frobenius-twisted equations give a complete global rank stratification and a finite geometrically exact nonordinary extremal locus. Determining that this locus consists of one rational pair and a single degree-six Frobenius orbit, together with its field-of-definition census, is a naturally motivated classification not implied by the original superspecial research. It distinguishes an entire characteristic-specific arithmetic phenomenon, rather than an arbitrary small-field table.

## Scope and independent assessment

The parameters are equation-marked, not geometric isomorphism classes. Rank zero is not claimed to imply Newton supersingularity. The full zeta functions are outside scope. The exact verifier requires SymPy. Historical coverage could be broader than the inspected sources.

Self-review: passed. Independent audit: not yet performed.
