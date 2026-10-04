# Exact quantifier-rank threshold for finite directed cycles
## Finding
Let \(\vec C_n\) be the directed cycle on \(n\ge 3\) vertices in the relational language \({S}\), with \(S(i,j)\) exactly when \(j\equiv i+1\pmod n\). Define
\[
g(1)=1,\qquad g(2)=4,\qquad g(q)=2^{q-1}+3\quad(q\ge 3).
\]
For every \(q\ge 1\) and \(m,n\ge 3\), Duplicator wins the \(q\)-round Ehrenfeucht--Fraisse game on \(\vec C_m\) and \(\vec C_n\) if and only if
\[
m=n\quad\text{or}\quad m,n\ge g(q).
\]
Equivalently, two finite directed cycles satisfy the same first-order sentences of quantifier rank at most \(q\) exactly under the same numerical threshold as undirected cycles.

## Assumptions and scope
The language has one binary relation \(S\) and no constants, functions, or additional order. Loops are absent because \(n\ge 3\). Quantifier rank is the usual maximum nesting depth. The claim concerns isolated directed cycles only; it does not address disjoint unions of cycles, directed paths, cycles with named vertices, or logics with counting.

## Proof
Write \(C_n\) for the ordinary undirected cycle on the same vertex set. Its edge relation is quantifier-free definable inside \(\vec C_n\) by
\[
E(x,y)\;:=\;S(x,y)\lor S(y,x).
\]
Brown and Hoshino prove that for undirected cycles Duplicator wins the \(q\)-round game exactly when \(m=n\) or \(m,n\ge g(q)\), with the above \(g\).

This immediately gives the lower-bound direction for directed cycles. If \(m\ne n\) and \(\min(m,n)<g(q)\), their undirected cycles are separated by a sentence of quantifier rank at most \(q\). Replacing each undirected atomic predicate \(E(x,y)\) by \(S(x,y)\lor S(y,x)\) preserves quantifier rank, so the directed cycles are also separated at rank \(q\).

It remains to prove Duplicator's upper bound. For \(q=1\), every loopless directed cycle has the same one-variable atomic type. For \(q=2\) and \(m,n\ge4\), after the first matched vertices are chosen, any second vertex has exactly one of four atomic positions relative to the first: equal, immediate successor, immediate predecessor, or neither. All four possibilities are available in every \(\vec C_r\) with \(r\ge4\), so Duplicator matches the same position type.

Assume now \(q\ge3\) and \(m,n\ge2^{q-1}+3\). Brown and Hoshino's upper-bound proof cuts each cycle at the first selected vertex and reduces the remaining \(q-1\) moves to a game on two paths whose two endpoints are already matched. The key path strategy is coordinate-based: with the left endpoints identified and the right endpoints identified, responses copy signed coordinate displacements from a matched endpoint when a move is close, and otherwise place the response at the corresponding prescribed offset. Consequently the strategy preserves not only undirected adjacency but also the orientation from the left endpoint to the right endpoint. On a directed path, an arc among selected vertices is exactly the condition that their coordinates differ by \(1\) in the positive direction. Hence the same response rules are a partial isomorphism for the directed successor relation.

After a first move on \(\vec C_m\) and \(\vec C_n\), rotational symmetry lets Duplicator match arbitrary chosen vertices. Cutting each directed cycle at those matched vertices produces consistently oriented directed paths \(\vec P_{m+1}\) and \(\vec P_{n+1}\), with both copies of the cut vertex treated as the two matched endpoints. Brown and Hoshino's endpoint-preserving path bound applies for the remaining \(q-1\) rounds because \(m,n\ge2^{q-1}+3\). By the orientation observation above, the resulting partial maps preserve \(S\). Therefore Duplicator wins the original \(q\)-round directed-cycle game.

Combining the two directions proves the claimed criterion.

## Verification
A direct finite-game solver independently evaluated all pairs \((\vec C_m,\vec C_n)\) with \(3\le m\le n\le12\) for \(1\le q\le4\). It recursively checks every Spoiler move and all possible Duplicator replies, validating equality and the directed arc relation on every selected pair. The program reports `VERIFY_OK cases=220`, agreeing with the closed form in every tested case. This finite computation is corroboration only; the proof above establishes the statement for all admissible \(m,n,q\).

## Relationship to prior work
Brown and Hoshino give the exact threshold \(g(1)=1\), \(g(2)=4\), and \(g(q)=2^{q-1}+3\) for undirected cycles. Pichler's finite-model-theory lecture notes explicitly discuss isolated directed cycles and state the sufficient bound that \(C_n\equiv_q C_{n+1}\) whenever \(n\ge2^q\), while noting that the cycle composition argument works for directed or undirected cycles. The result here sharpens that directed-cycle bound to the exact threshold and shows that orientation does not change the full rank profile.

## Limitations
The originality check found no exact directed-cycle statement with the threshold \(2^{q-1}+3\), but this is a literature-search conclusion rather than a proof of priority. The main residual risk is that the orientation-preserving refinement of the classical cycle strategy may appear in older lecture notes, theses, or textbooks not indexed by the searches performed. The result also relies on careful reading of the coordinate strategy in Brown and Hoshino; no claim is made for arbitrary orientations or for unions of directed cycles.

## References
1. Jason Brown and Richard Hoshino, “The Ehrenfeucht-Fraisse Game for Paths and Cycles,” *Ars Combinatoria* 83 (2007), 193–212. Public PDF: https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf
2. Reinhard Pichler, “Database Theory: Ehrenfeucht-Fraisse Games,” lecture notes, 24 May 2011, especially the directed-cycle discussion on pp. 53–54. Public PDF: https://people.inf.elte.hu/kiss/12abea/dbt07.pdf
