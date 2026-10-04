# Exact commutation law for factual hedged belief contractions
## Finding

Belardinelli and Zhang define contraction directly on unconstrained Kripke models. For a factual propositional formula \(\lambda\), its truth set is unchanged by contraction because the valuation is unchanged.

Fix a world set \(W\) and write
\[
X=\llbracket\lambda\rrbracket\subseteq W.
\]
For one accessibility row \(S\subseteq W\), the contraction update is therefore the set map
\[
C_X(S)=
\begin{cases}
S\cup(W\setminus X),&S\subseteq X,\\
S,&S\not\subseteq X.
\end{cases}
\]
The condition \(S\subseteq X\) is exactly the belief condition for the factual formula on that row.

For two factual formulas with truth sets \(X,Y\subseteq W\):

1. every \(C_X\) is idempotent;
2. the two contractions commute on every row,
\[
C_X(C_Y(S))=C_Y(C_X(S))
\qquad\text{for all }S\subseteq W,
\]
if and only if
\[
X=Y
\qquad\text{or}\qquad
X\cup Y=W.
\]

Because the update is rowwise and applies the same rule to every agent, this gives an exact model-level criterion. Factual contractions by \(\lambda\) and \(\mu\) commute on every unconstrained Kripke model if and only if
\[
\mathsf{CPC}\vdash\lambda\leftrightarrow\mu
\qquad\text{or}\qquad
\mathsf{CPC}\vdash\lambda\vee\mu.
\]

There is also an exact finite census. For \(n\) propositional variables let
\[
N=2^n
\]
be the number of Boolean valuations. Formulas modulo classical propositional equivalence correspond to subsets of this \(N\)-element valuation set. The number of ordered commuting pairs is
\[
2^N+3^N-1
=
2^{2^n}+3^{2^n}-1,
\]
out of
\[
4^N=4^{2^n}
\]
ordered pairs. Hence the number of ordered noncommuting pairs is
\[
4^N-3^N-2^N+1.
\]
For \(n=1,2,3\), the commuting counts are respectively
\[
12,\qquad 96,\qquad 6816,
\]
out of
\[
16,\qquad 256,\qquad 65536.
\]

## Assumptions and scope

The theorem concerns the contraction operation introduced for hedged public announcements on standard Kripke models with no frame constraint on the doxastic accessibility relations.

The contracted formulas \(\lambda,\mu\) are factual: they contain only propositional atoms and Boolean connectives. This restriction is essential to the proof because their truth sets remain fixed when accessibility relations change. For modal contraction inputs, the truth set of the second input may change after the first contraction, so the fixed-set calculation below no longer applies.

The commutation statement is universal over Kripke models. It is stronger than saying that two contractions happen to commute on one particular model.

## Proof

Fix \(X\subseteq W\).

For idempotence, suppose first that \(S\not\subseteq X\). Then
\[
C_X(S)=S,
\]
so a second application also fixes \(S\). Suppose instead that \(S\subseteq X\). Then
\[
C_X(S)=S\cup X^c.
\]
If \(X=W\), this is just \(S\). If \(X\ne W\), the set \(S\cup X^c\) contains a point outside \(X\), so it is not a subset of \(X\) and a second application fixes it. Thus
\[
C_X^2=C_X.
\]

Now assume \(X=Y\). Commutation is immediate.

Assume instead that
\[
X\cup Y=W.
\]
Equivalently,
\[
X^c\subseteq Y
\qquad\text{and}\qquad
Y^c\subseteq X.
\]
Consider any \(S\subseteq W\).

If \(S\subseteq X\cap Y\), applying the two contractions in either order yields
\[
S\cup X^c\cup Y^c.
\]
If \(S\subseteq X\) but \(S\not\subseteq Y\), then \(C_Y\) initially fixes \(S\). Applying \(C_X\) gives \(S\cup X^c\). Since \(X^c\subseteq Y\), the witness showing \(S\not\subseteq Y\) remains present, so a subsequent \(C_Y\) still fixes the set. The reverse order gives the same result. The case \(S\subseteq Y\) but \(S\not\subseteq X\) is symmetric. If \(S\) is contained in neither, both maps fix it. Hence the maps commute.

For necessity, suppose
\[
X\ne Y
\qquad\text{and}\qquad
X\cup Y\ne W.
\]
Use the empty row \(S=\varnothing\). Then
\[
C_X(\varnothing)=X^c.
\]
Because \(X\cup Y\ne W\), there is a point outside both \(X\) and \(Y\), so
\[
X^c\not\subseteq Y.
\]
Therefore
\[
C_Y(C_X(\varnothing))=X^c.
\]
Symmetrically,
\[
C_X(C_Y(\varnothing))=Y^c.
\]
Since \(X\ne Y\), their complements differ. Thus the maps do not commute.

This proves the set-theoretic criterion.

For the propositional criterion, if
\[
\mathsf{CPC}\vdash\lambda\leftrightarrow\mu,
\]
then the truth sets agree in every model. If
\[
\mathsf{CPC}\vdash\lambda\vee\mu,
\]
then their union is the whole world set in every model, so the contractions commute.

Conversely, if neither formula is valid, choose one Boolean valuation on which \(\lambda\) and \(\mu\) differ and another on which both are false. Put copies of these valuations into one Kripke model and choose an empty accessibility row. The source semantics permits unconstrained doxastic relations, so this is a legitimate model. Its two factual truth sets are distinct and do not cover the world set, so the preceding calculation gives noncommutation.

For the census, let the Boolean valuation set have size \(N\). There are \(2^N\) equal ordered pairs \((X,X)\). There are \(3^N\) ordered pairs with
\[
X\cup Y=W,
\]
because at each valuation the allowed membership patterns are \(10\), \(01\), and \(11\). The two families overlap only at
\[
(X,Y)=(W,W).
\]
Inclusion-exclusion gives
\[
2^N+3^N-1.
\]

## Verification

The proof is symbolic and covers arbitrary world sets for the set-map theorem and arbitrary finite propositional vocabularies for the logical census.

The bundled checker exhaustively tests every triple
\[
(X,Y,S)
\]
on carriers of sizes \(1\) through \(7\). It checks idempotence and verifies that commutation on all rows is equivalent to
\[
X=Y
\quad\text{or}\quad
X\cup Y=W.
\]
It separately enumerates all ordered set pairs for carrier sizes through \(8\) and confirms the count
\[
2^N+3^N-1.
\]
For propositional vocabularies with \(n=1,2,3\), it reproduces the commuting counts \(12,96,6816\).

The finite computations corroborate the proof; they are not used to infer the general theorem.

## Relationship to prior work

Belardinelli and Zhang introduce the hedged public-announcement contraction operator, define it by adding all counterexamples to a believed formula to each relevant accessibility row, and axiomatize the resulting dynamic logic. Their treatment also develops generalized event models and a general event-composition operation.

The present theorem isolates the composition behavior of the basic contraction operator when its inputs are factual. The source gives one-step contraction principles, but the checked text does not state the exact pairwise commutation criterion, the universal idempotence of factual contraction as a model transformation, or the finite census of commuting propositional inputs.

Baltag, Fiutek, and Smets study belief contraction in epistemic plausibility models by three different operations—severe withdrawal, conservative contraction, and moderate contraction. Those operators alter plausibility structure rather than using the row-expansion mechanism above, so their iteration laws do not cover this set-map classification.

## Limitations

The theorem is restricted to factual contraction inputs. With modal inputs, the first contraction can change the truth set governing the second update, and the fixed-set argument no longer applies.

The logical converse uses the source's explicit absence of frame constraints. If one restricts the starting models to a narrower class, additional pairs may commute accidentally because the empty-row witness or other separating rows are excluded.

The count is semantic modulo classical propositional equivalence; it does not count syntactic formulas.

## References

[1] Gaia Belardinelli and Snow Zhang, “Belief Contraction in Dynamic Epistemic Logic,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 137–157. DOI:10.4204/EPTCS.447.8.

[2] Alexandru Baltag, Virginie Fiutek, and Sonja Smets, “Suspending Judgement: Belief Contraction in Dynamic Epistemic Logic,” *Proceedings of the 23rd International Conference on Principles of Knowledge Representation and Reasoning* (2026). DOI:10.24963/KR.2026/10.
