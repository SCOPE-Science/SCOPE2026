# Exact quadratic \(1\)-type profile of Simon’s monotone two-order Fraïssé limit

## Finding

Let \(M\) be the Fraïssé limit in Simon’s Example 1.1. Its language has two linear orders \(\leq_1,\leq_2\) and an irreflexive binary relation \(R\) satisfying
\[
a'\leq_1 a\,R\,b\leq_2 b'\quad\Longrightarrow\quad a'Rb'.
\]
Simon defines \(f_M(m)\) to be the maximum, over all \(m\)-element parameter sets \(A\subseteq M\), of the number of complete \(1\)-types over \(A\).

For this Fraïssé limit the maximum is unnecessary: every \(m\)-element parameter set has the same number of complete \(1\)-types. Precisely,
\[
f_M(m)=2(m+1)^2-1\qquad(m\geq 0).
\]
More finely, the types satisfying \(x\notin A\) number
\[
(m+1)(2m+1),
\]
and the remaining \(m\) types are the equality types \(x=a\) for \(a\in A\).

## Assumptions and scope

The statement concerns exactly the Fraïssé class in Simon’s Example 1.1, not arbitrary pairs of orders with a monotone relation. The language is relational and finite, and the finite class is Fraïssé as stated in the source. Hence ultrahomogeneity implies that complete \(1\)-types over a finite base are determined by the corresponding one-point quantifier-free extensions, and the Fraïssé extension property realizes every admissible finite one-point extension.

The argument counts labeled extensions over a fixed parameter set. It does not assume that the two induced orders on that set have any particular relative permutation.

## Proof

Fix an \(m\)-element parameter set \(A\). Enumerate it in increasing \(\leq_1\)-order as \(a_0,\ldots,a_{m-1}\), and independently in increasing \(\leq_2\)-order as \(b_0,\ldots,b_{m-1}\). Monotonicity of \(R\) says that each row is a final segment in the second order and that these final segments shrink as the first-order row increases. Thus there are unique thresholds
\[
0\leq t_0\leq t_1\leq\cdots\leq t_{m-1}\leq m
\]
such that
\[
a_iRb_j\quad\Longleftrightarrow\quad j\geq t_i.
\]
Here \(t_i=m\) means an empty final segment. The condition \(\neg aRa\) restricts which threshold sequences can occur relative to the permutation taking the \(a_i\)-ordering to the \(b_j\)-ordering, but the count below is independent of that restriction.

Now add a new point \(x\notin A\). Let \(c\in\{0,\ldots,m\}\) be the cut at which \(x\) is inserted into the second order. Put
\[
b_c^{*}=|\{i:t_i=c\}|,
\qquad
\ell_c=|\{i:t_i<c\}|.
\]
For an old row with \(t_i<c\), monotonicity forces \(a_iRx\); for \(t_i>c\), it forces \(\neg a_iRx\). The rows with \(t_i=c\) form one consecutive block in first-order position. Inside that block, monotonicity allows exactly an initial segment to satisfy \(a_iRx\). Write \(q\in\{0,\ldots,b_c^{*}\}\) for the length of that initial segment.

After inserting the new second-order column, the transformed old row thresholds are
\[
T_i=
\begin{cases}
t_i,&t_i<c,\\
c,&t_i=c\text{ and }a_iRx,\\
c+1,&t_i=c\text{ and }\neg a_iRx,\\
t_i+1,&t_i>c.
\end{cases}
\]
They are nondecreasing. Let \(z\) be the threshold of the new row \(x\). Since the new column occupied by \(x\) has position \(c\) and \(R(x,x)\) is false, one must have
\[
z\in\{c+1,\ldots,m+1\}.
\]
Finally insert the new row at a first-order cut \(r\in\{0,\ldots,m\}\). For fixed \(z\), the augmented threshold list is nondecreasing precisely when \(z\) is inserted among the equal values \(T_i=z\). Therefore the number of valid row cuts is
\[
1+|\{i:T_i=z\}|.
\]
Summing this over all allowable \(z\) gives, for fixed \(c,q\),
\[
N_{c,q}=(m-c+1)+|\{i:T_i\geq c+1\}|.
\]
Exactly \(m-\ell_c-q\) transformed old thresholds are at least \(c+1\), so
\[
N_{c,q}=2m-c-\ell_c+1-q.
\]
Summing over \(q\) yields
\[
N_c=(b_c^{*}+1)(2m-c-\ell_c+1)-\frac{b_c^{*}(b_c^{*}+1)}2.
\]

It remains to sum over \(c\). Set \(b_c=b_c^{*}\). Then \(\sum_c b_c=m\) and \(\ell_c=\sum_{d<c}b_d\). Starting from \((2m+1)\sum_c(b_c+1)=(2m+1)^2\), the terms subtracted in the preceding expression have total
\[
\sum_c c(b_c+1)+\sum_c(b_c+1)\ell_c+\frac12\sum_c b_c(b_c+1)=m(2m+1).
\]
For the middle sum one uses
\[
\sum_c(b_c+1)\ell_c
=
\frac{m^2-\sum_c b_c^2}{2}+m^2-\sum_c cb_c.
\]
Consequently the number of one-point extension types with \(x\notin A\) is
\[
(2m+1)^2-m(2m+1)=(m+1)(2m+1).
\]
This depends only on \(m\), not on the induced finite structure on \(A\). Adding the \(m\) equality types gives
\[
(m+1)(2m+1)+m=2(m+1)^2-1,
\]
as claimed.

## Verification

The bundled `verify.py` carries out two finite replays. First, for every nondecreasing threshold sequence through \(m=8\), it evaluates the cut/block formula above and checks that the result is always \((m+1)(2m+1)\). Second, through \(m=5\), it exhausts every actual finite base: every relative permutation of the two orders and every threshold sequence satisfying diagonal irreflexivity. It enumerates the distinct one-point extension signatures and obtains
\[
1,6,15,28,45,66
\]
for the types with \(x\notin A\), hence
\[
1,7,17,31,49,71
\]
for all complete \(1\)-types. The replay ends with `VERIFY_OK`.

## Relationship to prior work

Simon’s paper introduces \(f_M\) as the finite-parameter type-growth invariant used to formulate the polynomial-growth side of the rank-one classification. The same paper gives the monotone two-order Fraïssé class as a basic example and later formalizes the relevant monotone relation as an intertwining relation. The inspected source states neither the exact \(f_M\) profile above nor the stronger fact that the count is independent of the finite parameter configuration.

Targeted searches were made under the exact polynomial, the first values of the sequence, the phrases “two linear orders”, “monotone relation”, “Fraïssé”, “intertwining”, and “type growth”, and under the source title. No covering statement was located. The contribution claimed here is only this exact object-specific type count and its base-independence; the Fraïssé construction, the definition of \(f_M\), and the general rank-one theory are due to Simon.

## Limitations

The proof is elementary once the finite structures are encoded by Ferrers thresholds, so an equivalent observation may exist in unindexed notes or folklore. The search did not establish exhaustive bibliographic nonexistence. The executable replay checks finite instances and the combinatorial parametrization, but the all-\(m\) result rests on the symbolic summation in the proof. No independent audit has been performed.

## References

Pierre Simon, “NIP \(\omega\)-categorical structures: the rank 1 case”, arXiv:1807.07102; Proceedings of the London Mathematical Society 125 (2022), 1253–1331, DOI:10.1112/plms.12482.
