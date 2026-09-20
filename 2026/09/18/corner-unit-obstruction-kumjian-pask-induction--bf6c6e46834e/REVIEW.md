# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The core obstruction is ring-theoretic and independent of the
combinatorics of a \(k\)-graph. For \(B=eAe\), one has \(AB=Ae\) and
\((1-e)B=0\). If \(e\neq1_A\), then \(Ae\neq A\), so the identity \(e\) of
\(B\) does not act as the identity on \(A\). Hence \(A\) is not a unital
right \(B\)-module and cannot be an ordinary free right \(B\)-module.

For a finite-vertex KP algebra,
\(1_A=\sum_{v\in\Lambda^0}s_v\) and
\(p_H=\sum_{v\in H}s_v\). Nonzero orthogonal vertex idempotents imply
\(p_H\neq1_A\) for proper \(H\), so the obstruction applies directly to the
claimed freeness theorem.

The tensor correction was checked algebraically:
\(a\otimes v=ae\otimes v\) for every unital \(B\)-module \(V\), yielding
\(A\otimes_BV\cong Ae\otimes_BV\). The standard adjunction with \(eM\) follows
by mutually inverse explicit maps. The two-loop rank-one example satisfies
the graph hypotheses and supplies an elementary counterexample. In the
source's own \(H=\{w\}\) example, \(s_v\otimes1=0\) follows immediately from
\(s_vs_w=0\) and \(1=s_w\cdot1\).

The review deliberately does not infer failure of exactness: exactness is a
separate question about the flatness of \(Ae_B\).

## Originality

**PASS, to the best of our knowledge.** The corner adjunction and Morita
theory are standard and are treated as prior art. Clark--an Huef--
Luiten-Apirana (2017) already use vertex subsets to obtain graph-algebra
Morita equivalences. The originality claim is restricted to identifying the
unit obstruction in arXiv:2609.20230v1, giving the all-proper-\(H\)
finite-vertex contradiction, the zero tensor in its worked example, and the
precise unital correction of the induction/restriction pair.

The source preprint was inspected at its current v1, including its
conventions, hereditary-corner construction, Section 3 freeness and
induction statements, worked example, and later Morita-corner formulation.
Targeted literature checks for the paper identifier/title together with
correction, erratum, corner, freeness, and equivalent terminology did not
locate a public correction of this issue. The arXiv submission history
currently lists only v1.

Residual risk is non-negligible because the preprint is recent and the
obstruction is short once the mismatch between \(1_A\) and the corner unit
\(p_H\) is noticed. Older ring-theoretic literature certainly contains the
general corner facts, so no novelty is claimed for those facts themselves.

## Value

**PASS.** The challenged theorem is advertised as the flatness/freeness
mechanism supporting hereditary-subgraph induction over fields. The
obstruction is universal across every proper nonempty finite-vertex
hereditary saturated corner, not a sporadic example. It also supplies a
canonical repair of the functorial formulation and pinpoints a zero vector in
the source's explicit induced basis. The result separates the false
freeness claim from the still-open possibility that \(Ae\) is flat in cases
of interest, preventing an overstatement of downstream damage.

## Limitations

The result is stated for finite vertex sets so that \(p_H\) is a genuine
global idempotent and both \(A\) and \(B\) are unital. Infinite-vertex
local-unit formulations are not analyzed here. No claim is made that
\(Ae_B\) fails to be flat or free, nor that every downstream theorem in the
source paper is false. The principal residual originality risk is a
subsequent author revision or an older equivalent observation expressed only
in general corner-module language.

No independent validation is asserted.
