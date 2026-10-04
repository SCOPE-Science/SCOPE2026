# Sharp finite instance-arity cutoff for instantial neighbourhood frames
## Finding

Let
\[
(X,N)
\]
be a finite instantial neighbourhood frame with
\[
n=|X|\ge1.
\]

For \(k\ge0\), write
\[
f_k^N(B_1,\ldots,B_k;A)
\]
for the instantial operation on subsets of \(X\):
\[
f_k^N(B_1,\ldots,B_k;A)
=
\left\{
x\in X:
\exists D\in N(x)\;
\left[
D\subseteq A
\ \text{and}\
D\cap B_i\ne\varnothing
\text{ for every }i
\right]
\right\}.
\]
This is the finite-arity operation underlying the BAIO semantics of instantial neighbourhood logic.

Then the finite initial segment
\[
f_0^N,f_1^N,\ldots,f_n^N
\]
determines the full neighbourhood function \(N\) uniquely.

More precisely,
\[
\varnothing\in N(x)
\quad\Longleftrightarrow\quad
x\in f_0^N(;\varnothing).
\]
If
\[
D=\{d_1,\ldots,d_m\}\ne\varnothing,
\qquad
m=|D|\le n,
\]
then
\[
\boxed{
D\in N(x)
\quad\Longleftrightarrow\quad
x\in
f_m^N
\bigl(
\{d_1\},\ldots,\{d_m\};D
\bigr).
}
\]

The cutoff is sharp in the worst case. For every \(n\ge1\), there exist two distinct \(n\)-world instantial neighbourhood frames whose induced operations agree for every instance arity
\[
k\le n-1
\]
but disagree at arity \(n\).

Consequently, \(n\) is the least uniform instance-arity bound from which every labelled \(n\)-world instantial neighbourhood frame can be reconstructed exactly.

## Assumptions and scope

The source paper uses an \(\omega\)-indexed family of BAIO operations
\[
f_k:B^{k+1}\to B
\]
and, on the powerset algebra of a frame, the corresponding infinitary notation
\[
\Box_N(\Gamma;A)
=
\left\{
x\in X:
\exists D\in N(x)
\left[
D\subseteq A
\ \text{and}\
D\cap C\ne\varnothing
\text{ for every }C\in\Gamma
\right]
\right\}.
\]

Here **instance arity** means the number \(k\) of instance arguments \(B_1,\ldots,B_k\); the support argument \(A\) is not counted. Thus \(f_k\) has ordinary function arity \(k+1\).

The reconstruction theorem is about the full set-valued neighbourhood function \(N\), not merely modal validity under a fixed valuation. Since arbitrary subsets of a finite labelled carrier are admitted as algebra elements, singleton instance arguments can name individual worlds.

No monotonicity, supplementation, seriality, or other closure condition is imposed on \(N(x)\).

## Proof

Fix
\[
x\in X.
\]

For the empty neighbourhood, the semantic clause gives
\[
x\in f_0^N(;\varnothing)
\]
if and only if there is some
\[
E\in N(x)
\]
with
\[
E\subseteq\varnothing.
\]
The only such set is \(\varnothing\), so
\[
x\in f_0^N(;\varnothing)
\quad\Longleftrightarrow\quad
\varnothing\in N(x).
\]

Now let
\[
D=\{d_1,\ldots,d_m\}\ne\varnothing.
\]
If
\[
D\in N(x),
\]
then \(D\) itself witnesses
\[
x\in
f_m^N
\bigl(
\{d_1\},\ldots,\{d_m\};D
\bigr).
\]

Conversely, suppose the right-hand side holds. Then there exists
\[
E\in N(x)
\]
such that
\[
E\subseteq D
\]
and
\[
E\cap\{d_i\}\ne\varnothing
\qquad(1\le i\le m).
\]
The latter conditions force
\[
d_i\in E
\qquad(1\le i\le m),
\]
hence
\[
D\subseteq E.
\]
Together with \(E\subseteq D\), this gives
\[
E=D.
\]
Therefore
\[
D\in N(x).
\]

Since every subset \(D\subseteq X\) has size at most \(n\), the operations through instance arity \(n\) recover every membership statement
\[
D\in N(x)
\]
and therefore determine \(N\) completely.

For sharpness, fix an \(n\)-element carrier
\[
X=\{1,\ldots,n\}
\]
and a distinguished world \(x_*\in X\). Define two frames \(N^-\) and \(N^+\) that agree away from \(x_*\), while
\[
N^-(x_*)=\mathcal P(X)\setminus\{X\},
\qquad
N^+(x_*)=\mathcal P(X).
\]

Clearly the frames are distinct.

We show that their operations agree at every
\[
k\le n-1.
\]
Since
\[
N^-(x_*)\subseteq N^+(x_*),
\]
only the implication from \(N^+\) to \(N^-\) needs proof.

Suppose
\[
x_*
\in
f_k^{N^+}(B_1,\ldots,B_k;A).
\]
If there is already a proper witness
\[
E\subsetneq X,
\]
then
\[
E\in N^-(x_*)
\]
and there is nothing to prove.

The only remaining possibility is that the full set \(X\) is needed as a witness. Then necessarily
\[
A=X
\]
and every \(B_i\) is nonempty. Choose
\[
b_i\in B_i
\]
for each \(i\), and put
\[
E=\{b_1,\ldots,b_k\}.
\]
Because
\[
k\le n-1,
\]
we have
\[
|E|\le n-1,
\]
so
\[
E\subsetneq X.
\]
Moreover
\[
E\subseteq A
\]
and
\[
E\cap B_i\ne\varnothing
\]
for every \(i\). Thus \(E\) is a witness in \(N^-(x_*)\). For \(k=0\), take \(E=\varnothing\).

Hence
\[
f_k^{N^-}=f_k^{N^+}
\qquad
(0\le k\le n-1).
\]

At arity \(n\), take
\[
A=X,
\qquad
B_i=\{i\}
\quad(1\le i\le n).
\]
Any witness must contain every element of \(X\), so the unique possible witness is \(X\). Therefore
\[
x_*\in
f_n^{N^+}
(\{1\},\ldots,\{n\};X)
\]
but
\[
x_*\notin
f_n^{N^-}
(\{1\},\ldots,\{n\};X).
\]

Thus no uniform cutoff below \(n\) reconstructs all \(n\)-world frames.

## Verification

The bundled checker independently implements the instantial operations.

For carrier sizes
\[
1\le n\le4,
\]
it enumerates every possible local neighbourhood family
\[
\mathcal N\subseteq\mathcal P(X)
\]
and verifies the reconstruction equations for every subset \(D\subseteq X\).

It separately verifies the sharpness pair
\[
\mathcal P(X)\setminus\{X\}
\quad\text{versus}\quad
\mathcal P(X)
\]
by exhaustively testing every support set and every tuple of instance sets for all
\[
k\le n-1,
\]
and then verifies that the \(n\) singleton arguments distinguish the pair.

The finite replay corroborates the proof. The general theorem is set-theoretic and does not depend on extrapolation from the checked carrier sizes.

## Relationship to prior work

De Groot's 2026 Thomason-duality paper defines complete atomic instantial neighbourhood algebras using a set-indexed operator and identifies the underlying BAIO as an \(\omega\)-indexed family of finite-arity operations. Its duality proof already contains the reconstruction idea
\[
D\in N(x)
\]
via the operator applied to the atoms below \(D\). On a finite powerset algebra, this immediately supplies the upper bound \(|D|\le n\).

The new content here is the **sharp uniform cutoff**. The source does not state that \(n\) is the least possible bound on \(n\)-world frames, nor does it give a pair of distinct \(n\)-world frames invisible to every lower instance arity.

The original INL paper introduces the full family of instantial modalities and studies expressive fragments. De Groot's 2022 Hennessy–Milner paper studies an \(\omega\)-indexed collection of INL fragments. Its publisher-accessible abstract confirms the fragment hierarchy is a central object, but full text was not available in the comparison channel; no accessible statement located there gives the exact \(n\)-world reconstruction cutoff or the lower-bound frame pair above. This remains the principal literature risk.

A 2026 paper of Payette and Brunet treats Henkin completeness for full INL and a unary fragment. That proof-theoretic restriction is different from the finite-frame question addressed here.

## Limitations

The theorem concerns exact reconstruction of a labelled finite neighbourhood frame from its algebraic operations. It is not a statement that every modal formula on an \(n\)-world model can be rewritten with at most \(n\) instance arguments without changing formula size or nesting structure.

The lower-bound pair uses arbitrary instantial neighbourhood frames. Additional frame conditions can lower the necessary cutoff.

The result does not identify the optimal cutoff for restricted subclasses such as singular, atomic, monotone, or topological neighbourhood frames.

The 2022 paper on arity-indexed INL fragments could contain an equivalent finite-frame consequence under different terminology; its full text was not accessible during the comparison.

## References

[1] Jim de Groot, “Thomason Duality for Instantial Neighbourhood Frames,” *Journal of Symbolic Logic*, First View (2026), 1–20. DOI:10.1017/jsl.2026.10202.

[2] Johan van Benthem, Nick Bezhanishvili, Sebastian Enqvist, and Junhua Yu, “Instantial Neighbourhood Logic,” *Review of Symbolic Logic* 10(1) (2017), 116–144. DOI:10.1017/S1755020316000447.

[3] Jim de Groot, “Hennessy-Milner and Van Benthem for Instantial Neighbourhood Logic,” *Studia Logica* 110 (2022), 717–743. DOI:10.1007/s11225-021-09975-w.

[4] Gillman Payette and Tyler Brunet, “Henkin Completeness of Some Instantial Neighbourhood Logics,” *Australasian Journal of Logic* 23(2) (2026), 148–165. DOI:10.26686/ajl.v23i2.10308.
