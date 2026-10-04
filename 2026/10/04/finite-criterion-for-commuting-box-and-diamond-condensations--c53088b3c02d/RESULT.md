# Finite criterion for commuting box and diamond condensations
## Finding

Sato's 2026 survey introduces, for a fusion frame
\[
(W,\leq,R),
\]
two right-sided relation completions:
\[
\beta(R)=R\circ\leq,
\qquad
\delta(R)=R\circ\leq^{-1}.
\]
They are used separately to obtain \(\Box\)-condensed and \(\Diamond\)-condensed normal forms for the corresponding one-modality fragments.

For a finite preorder \((W,\leq)\), the two completions commute on **every** modal relation
\[
R\subseteq W^2
\]
if and only if
\[
\boxed{
\leq\circ\leq^{-1}
=
\leq^{-1}\circ\leq.
}
\]

There is an exact order-theoretic form of this condition. Let
\[
x\equiv y
\quad\Longleftrightarrow\quad
x\leq y\ \text{and}\ y\leq x,
\]
and let \(P=W/{\equiv}\) be the quotient poset. Then the following are equivalent:

1. \(\beta(\delta(R))=\delta(\beta(R))\) for every relation \(R\subseteq W^2\);
2. \(\leq\circ\leq^{-1}=\leq^{-1}\circ\leq\);
3. every connected component of the comparability graph of \(P\) has both a least and a greatest element.

When these conditions hold, let \(E\) relate two points of \(W\) exactly when their quotient classes lie in the same comparability component of \(P\). Then
\[
\leq\circ\leq^{-1}
=
\leq^{-1}\circ\leq
=
E,
\]
and for every \(R\),
\[
\beta(\delta(R))
=
\delta(\beta(R))
=
R\circ E.
\]

Moreover,
\[
R\circ E
\]
is the least relation containing \(R\) that is fixed by both \(\beta\) and \(\delta\).

Thus a finite intuitionistic preorder admits an order-independent two-step joint condensation exactly when each comparability component is bounded above and below.

There is also a fusion-frame corollary. If the original modal relation \(R\) satisfies both Sato's \(\Box\)-p and \(\Diamond\)-p confluence conditions, then under the equivalent conditions above the common completion
\[
S=R\circ E
\]
again satisfies both p-conditions and is simultaneously:

\[
\Box\text{-brilliant},
\qquad
\Diamond\text{-brilliant},
\qquad
\Box\text{-condensed},
\qquad
\Diamond\text{-condensed}.
\]

So, on precisely the finite preorders described above, the two one-sided condensation procedures can be merged into a canonical joint relational normal form after two steps.

## Assumptions and scope

A fusion frame consists of a nonempty set \(W\), a preorder \(\leq\), and a modal relation \(R\).

Relation composition is written in the source orientation:
\[
x\,(A\circ B)\,z
\]
iff there exists \(y\) with
\[
xAy
\quad\text{and}\quad
yBz.
\]

The operators \(\beta\) and \(\delta\) are considered here as algebraic operations on all binary relations on \(W\). Sato introduces them under the corresponding p-conditions because those hypotheses give the desired truth-preservation theorems for the \(\Box\)-free and \(\Diamond\)-free fragments.

The theorem does **not** claim that applying both condensations preserves truth in the full bimodal language. Its content is structural: it identifies exactly when the two relation completions are compatible and yield the same least simultaneous fixed point.

Finiteness is needed only for the characterization by a least and greatest point in each comparability component. The algebraic equivalence between commutation and
\[
\leq\circ\leq^{-1}
=
\leq^{-1}\circ\leq
\]
does not require finiteness.

## Proof

Because \(\leq\) is reflexive,
\[
R\subseteq R\circ\leq
\quad\text{and}\quad
R\subseteq R\circ\leq^{-1}.
\]
Because \(\leq\) is transitive,
\[
(R\circ\leq)\circ\leq
=
R\circ\leq
\]
and similarly for \(\leq^{-1}\). Hence \(\beta\) and \(\delta\) are extensive, monotone, idempotent operators on the lattice of binary relations.

For every \(R\),
\[
\beta(\delta(R))
=
R\circ\leq^{-1}\circ\leq,
\]
while
\[
\delta(\beta(R))
=
R\circ\leq\circ\leq^{-1}.
\]
Therefore equality
\[
\leq^{-1}\circ\leq
=
\leq\circ\leq^{-1}
\]
immediately implies commutation for every \(R\).

Conversely, if \(\beta\) and \(\delta\) commute for every relation, apply them to the identity relation
\[
I_W.
\]
Then
\[
\beta(\delta(I_W))
=
\leq^{-1}\circ\leq
\]
and
\[
\delta(\beta(I_W))
=
\leq\circ\leq^{-1},
\]
so the two middle relations are equal.

Now interpret these relations order-theoretically. Put
\[
U=\leq\circ\leq^{-1},
\qquad
L=\leq^{-1}\circ\leq.
\]
Then
\[
xUz
\]
means that \(x\) and \(z\) have a common upper bound, while
\[
xLz
\]
means that they have a common lower bound.

Assume
\[
U=L=C.
\]
The relation \(C\) is reflexive and symmetric. It is also transitive.

Indeed, suppose
\[
xCy
\quad\text{and}\quad
yCz.
\]
Because \(C=L\), choose \(a\) with
\[
a\leq x,\qquad a\leq y.
\]
Because \(C=U\), choose \(b\) with
\[
y\leq b,\qquad z\leq b.
\]
Then
\[
a\leq y\leq b,
\]
so \(a\) and \(z\) have the common upper bound \(b\). Hence
\[
aCz.
\]
Using \(C=L\) again, choose \(c\) with
\[
c\leq a,\qquad c\leq z.
\]
Since \(c\leq a\leq x\), the point \(c\) is a common lower bound of \(x\) and \(z\), so
\[
xCz.
\]

Thus \(C\) is an equivalence relation.

Every comparable pair belongs to \(C\). Conversely, if two points have a common upper or lower bound, they are joined by a length-two path in the comparability graph. Therefore the \(C\)-classes are exactly the connected components of the comparability graph of the quotient poset \(P=W/{\equiv}\), lifted back to \(W\).

Because \(P\) is finite, every such component has a greatest element. To see this, enumerate its elements. Since any two have a common upper bound in the component, combine the first two to obtain an upper bound, combine that upper bound with the third, and continue. The resulting point lies above the entire component. The same argument using common lower bounds gives a least element.

This proves that
\[
U=L
\]
implies the bounded-component condition.

Conversely, suppose each comparability component of \(P\) has a least point and a greatest point. Any two elements in the same component therefore have both a common lower and a common upper bound. Elements in different components have neither, because any common bound would create a comparability path between them. Hence
\[
U=L=E,
\]
where \(E\) is the component equivalence relation.

Under these equivalent conditions,
\[
\beta(\delta(R))
=
\delta(\beta(R))
=
R\circ E.
\]

Since
\[
E\circ\leq=E
\quad\text{and}\quad
E\circ\leq^{-1}=E,
\]
the relation \(R\circ E\) is fixed by both \(\beta\) and \(\delta\).

To prove minimality, let \(S\supseteq R\) be fixed by both operators. Right closure under \(\leq\) and \(\leq^{-1}\) propagates every \(S\)-edge along every finite zigzag of comparable target points. Hence an edge from \(x\) to one point of a comparability component forces edges from \(x\) to all points of that component. Therefore
\[
R\circ E\subseteq S.
\]

Finally assume the original relation \(R\) satisfies both p-conditions:
\[
\leq\circ R\subseteq R\circ\leq,
\qquad
\leq^{-1}\circ R\subseteq R\circ\leq^{-1}.
\]
For
\[
S=R\circ E,
\]
we have
\[
S\circ\leq=S,
\qquad
S\circ\leq^{-1}=S.
\]
Also,
\[
\leq\circ S
=
\leq\circ R\circ E
\subseteq
R\circ\leq\circ E
=
R\circ E
=
S
=
S\circ\leq,
\]
and dually
\[
\leq^{-1}\circ S
\subseteq
S
=
S\circ\leq^{-1}.
\]
Thus both p-conditions are preserved.

The equalities
\[
S\circ\leq=S,
\qquad
S\circ\leq^{-1}=S
\]
are exactly the two right-brilliance conditions. Sato's proposition that a p-frame which is brilliant is condensed then gives both condensation conditions.

## Verification

The bundled checker exhaustively enumerates all labelled finite posets on up to four points and verifies:
\[
\leq\circ\leq^{-1}
=
\leq^{-1}\circ\leq
\]
if and only if every comparability component has a least and greatest element.

For every poset on at most three points, it additionally enumerates every binary relation \(R\) and verifies that the two condensation composites commute for every \(R\) exactly in the bounded-component cases.

Whenever the criterion holds, the checker verifies that the common result is fixed by both right-condensation operators and is exactly the relation obtained by saturating targets over comparability components.

It also checks, for every small relation satisfying both p-conditions, that the common completion again satisfies both p-conditions.

The computation is exhaustive for the stated finite test sizes and corroborates the general relational proof.

## Relationship to prior work

Sato defines \(\Box\)-condensation by
\[
R\mapsto R\circ\leq
\]
and \(\Diamond\)-condensation by
\[
R\mapsto R\circ\leq^{-1}.
\]
The paper proves separately that these operations create condensed and brilliant frames and preserve truth in the corresponding one-modality fragments.

The checked source does not analyze the interaction of the two completions, ask when their order matters, or identify a least simultaneous fixed relation.

The theorem above supplies that missing compatibility criterion. It shows that the obstruction is entirely controlled by the intuitionistic preorder: the two procedures commute universally exactly when common-upper and common-lower compatibility coincide, which in the finite quotient poset is equivalent to every comparability component having both endpoints.

Targeted searches for commuting \(\Box\)- and \(\Diamond\)-condensations, common-upper/common-lower criteria, and simultaneous brilliant completions did not locate an equivalent modal-semantic statement. General order theory supplies the terminology of common bounds and comparability graphs, but no checked source connects that criterion to these condensation operators.

## Limitations

The result is structural and does not assert truth preservation for formulas containing both \(\Box\) and \(\Diamond\) after the joint completion.

For infinite preorders, commutation is still equivalent to equality of the common-upper and common-lower relations, but a connected component need not have a global least or greatest element. The finite endpoint characterization therefore does not extend verbatim.

The theorem gives a universal criterion, meaning commutation for every modal relation \(R\). A particular relation can commute under the two operations even when the underlying preorder fails the universal criterion.

The result does not classify the shortest sequence of alternating condensations needed when the two operators fail to commute.

## References

[1] Yuta Sato, “Intuitionistic and Constructive Modal Logics for Classical Modal Logicians,” arXiv:2608.29708, first posted 30 August 2026.

[2] Alex K. Simpson, *The Proof Theory and Semantics of Intuitionistic Modal Logic*, PhD thesis, University of Edinburgh, 1994.

[3] Patrick Blackburn, Maarten de Rijke, and Yde Venema, *Modal Logic*, Cambridge Tracts in Theoretical Computer Science 53, Cambridge University Press, 2001.
