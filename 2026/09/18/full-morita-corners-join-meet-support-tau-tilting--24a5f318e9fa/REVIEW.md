# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The argument reduces the strict Morita-context case to ordinary Morita equivalence through either full diagonal idempotent. Under \(R_e=(-)e\), the \(B\)-corner is transported by \(\Theta=-\otimes_BM\), so the componentwise conditions become simultaneous membership in \(\mathcal U\) and \(\mathcal V\), giving the intersection. Direct induction transports to \(X\oplus\Theta(Y)\); when this is support \(\tau\)-tilting, its factor class is the smallest torsion class containing \(\mathcal U\) and \(\mathcal V\), hence their join. The equivalence of the two cross conditions with the two inclusions \(\mathcal V\subseteq\mathcal U\) and \(\mathcal U\subseteq\mathcal V\) follows from the mutually inverse corner equivalences.

The equality criterion was checked in both directions. If the directly generated class equals the componentwise class, then a class containing both \(\mathcal U\) and \(\mathcal V\) equals their intersection, forcing \(\mathcal U=\mathcal V\). Conversely, equality of the corner torsion classes makes \(X\) and \(\Theta(Y)\) the same basic Ext-projective generator by the Adachi--Iyama--Reiten bijection, so the direct sum basicizes to a support \(\tau\)-tilting module with the prescribed class.

The semisimple family is exact: for \(C=k^n\), support \(\tau\)-tilting modules correspond to subsets of the \(n\) simples, direct sum corresponds to union, and the componentwise strict-context condition corresponds to intersection. Hence all \(4^n\) ordered pairs yield support \(\tau\)-tilting direct induction and exactly the \(2^n\) diagonal pairs have union equal to intersection.

## Originality

**PASS, to the best of our knowledge.** The recent source arXiv:2609.18746v1 was inspected for its main direct-induction theorem, componentwise torsion class, radical-valued converse, and matrix/strict-context examples. The source already shows that the radical hypothesis cannot simply be dropped and already uses a matrix strict context to exhibit an intersection obstruction; those facts are treated as prior art.

Searches for equivalent formulations involving strict/full Morita contexts, support \(\tau\)-tilting modules, functorially finite torsion classes, direct induction, and join/meet lattice operations did not locate the general theorem above, the equivalence of the bilateral cross conditions with equality of transported torsion classes, or the \(4^n\) versus \(2^n\) semisimple family.

Classical Morita/torsion theory is the main residual risk. Green--Psaroudakis (2014) supplies the relevant corner functors, and Kashu (2003) proves order-preserving correspondences for torsion theories in Morita contexts. These establish ingredients, not the support-\(\tau\)-tilting gluing statement claimed here. Older literature on torsion theories and localizations in Morita contexts was not exhaustively inspected theorem-by-theorem, so an equivalent lattice-theoretic observation under different terminology remains possible. This is a residual originality risk, not evidence of known coverage.

## Value

**PASS.** The result identifies the exact mechanism behind the opposite extreme to the radical-valued case of arXiv:2609.18746: full corners collapse both corner module categories to one Morita-equivalent category, where prescribed componentwise gluing is intersection while direct induction is join. This gives an exact functorial-finiteness criterion for the prescribed class, a conceptual form of the bilateral compatibility conditions, and an infinite semisimple family in which direct induction succeeds for every pair while the prescribed-class criterion holds for an exponentially vanishing fraction \(2^{-n}\).

## Review status

No independent validation, formal verification, expert attestation, or journal peer review is asserted.
