# Four-arrow Kronecker modules sharpen the brick-chain growth constant

## Finding
Let \(k\) be an algebraically closed field. Write \(b_A(M)\) for the number of brick chain filtrations of a finite-dimensional right module \(M\) over a finite-dimensional \(k\)-algebra \(A\), and let
\[
F(m)=\sup\{\log b_A(M):\operatorname{length}_A(M)=m\}.
\]
Then
\[
\limsup_{m\to\infty}\frac{F(m)}{m^2}\ge
\frac{2+\log(3/8)}{72}
=0.014155149263726024\ldots .
\]
This improves the previously published lower endpoint
\[
\frac{1-\log2}{25}=0.012274112777602188\ldots
\]
by about \(15.3\%\).

The bound is realized inside the four-arrow Kronecker family. If \(Q_4\) has two vertices and four parallel arrows from the first to the second, then for every \(n\ge1\) a nonempty Zariski-open subset of \(\operatorname{Rep}(Q_4,(4n,2n))\) consists of bricks \(M\) of composition length \(6n\) with
\[
\log b_{kQ_4}(M)\ge
\left(1+\frac12\log3-\frac32\log2\right)n^2-O(n).
\]

More generally, in the fixed-arrow square-staircase specialization of the same construction, the normalized coefficient is
\[
c(q)=\frac{1+\frac12\log(q-1)-\frac32\log2}{(q+2)^2},\qquad q\ge3,
\]
and among integer arrow counts \(q\ge3\), this coefficient is maximized at \(q=4\).

## Assumptions and scope
The base field is algebraically closed. The logarithm is natural. The argument concerns the square choice \(a=b=n\) and the staircase partition \(\nu=(n,n-1,\ldots,1)\) inside the general Kronecker construction; it does not assert that this is the globally optimal choice of parameters or partitions. The resulting inequality is a lower bound for the open global asymptotic problem, not an evaluation of the limsup.

## Proof
Enomoto's general \(q\)-Kronecker construction gives, for \(q\ge3\), integers \(a,b\ge1\), and a partition \(\nu\) fitting the \(a\)-by-\(b\) rectangle, a nonempty open set of brick representations of dimension vector
\[
\alpha=(a+(q-1)b,a+b)
\]
whose brick-chain count is at least
\[
K(q,a,b)\ge \frac{(q-1)^d d!}{H(\nu)^2},
\]
where \(d=|\nu|\) and \(H(\nu)\) is the hook-length product.

Take \(a=b=n\) and the staircase \(\delta_n=(n,n-1,\ldots,1)\). Put
\[
d_n=\frac{n(n+1)}2,
\qquad
H_n=H(\delta_n)=\prod_{j=0}^{n-1}(2j+1)^{n-j},
\]
and
\[
L_n^{(q)}=\frac{(q-1)^{d_n}d_n!}{H_n^2}.
\]
Then \(\alpha=(qn,2n)\), so the composition length is \((q+2)n\). Also
\[
\frac{H_n}{H_{n-1}}=(2n-1)!!,
\qquad
d_n-d_{n-1}=n,
\]
which gives the exact ratio
\[
\frac{L_n^{(q)}}{L_{n-1}^{(q)}}
=(q-1)^n
\frac{\prod_{j=1}^n(d_{n-1}+j)}{((2n-1)!!)^2}.
\]
The same Stirling estimates used for the three-arrow case give
\[
\log\!\left(\prod_{j=1}^n(d_{n-1}+j)\right)
=n(2\log n-\log2)+O(1)
\]
and
\[
\log((2n-1)!!)
=n\log n+n\log2-n+\frac12\log2+O(n^{-1}).
\]
Therefore
\[
\log\frac{L_n^{(q)}}{L_{n-1}^{(q)}}
=\bigl(2+\log(q-1)-3\log2\bigr)n+O(1),
\]
and summation yields
\[
\log L_n^{(q)}
=\left(1+\frac12\log(q-1)-\frac32\log2\right)n^2+O(n).
\]
Since generic modules in the construction satisfy \(b_{kQ_q}(M)\ge L_n^{(q)}\), division by their squared length \((q+2)^2n^2\) gives \(c(q)\).

At \(q=4\),
\[
c(4)=\frac{2+\log(3/8)}{72}
=0.014155149263726024\ldots,
\]
whereas Enomoto's \(q=3\) specialization gives
\[
c(3)=\frac{1-\log2}{25}
=0.012274112777602188\ldots .
\]
Thus the four-arrow family strictly improves the known lower endpoint.

It remains to optimize within the fixed-\(q\) square-staircase family. Extend \(c(q)\) to real \(q>1\), write
\[
A(q)=1+\frac12\log(q-1)-\frac32\log2,
\]
and note that the sign of \(c'(q)\) is the sign of
\[
h(q)=\frac{q+2}{2(q-1)}-2A(q).
\]
One has
\[
h'(q)=-\frac3{2(q-1)^2}-\frac1{q-1}<0.
\]
Moreover \(h(3)>0\) because \(\log2>1/2\), while
\[
h(4)=\log(8/3)-1<0
\]
because \(e>8/3\). Hence the continuous maximum lies strictly between \(3\) and \(4\), and \(c(q)\) decreases for every real \(q\ge4\). A direct exact comparison gives \(c(4)>c(3)\): it is equivalent to \(25\log3-3\log2>22\), and the elementary bounds \(\log3>13/12\) and \(\log2<7/10\) make the left side larger than \(1499/60>22\). Consequently \(q=4\) is the integer maximizer.

## Verification
The accompanying verifier reconstructs \(d_n\), \(H_n\), and \(L_n^{(q)}\) with exact integers; checks the displayed ratio identity for \(3\le q\le8\) and \(1\le n\le20\); evaluates \(c(3)\) and \(c(4)\) at high precision; and checks the discrete coefficient profile through \(q=1000\). These computations support the algebra and arithmetic only. The infinite asymptotic statement follows from the proof above, not from finite enumeration.

## Relationship to prior work
Enomoto's 2026 preprint proves the general Kronecker lower bound used here and then specializes the asymptotic argument to the three-arrow Kronecker quiver, obtaining \((1-\log2)/25\) as the lower endpoint for the global limsup and explicitly leaving the exact limsup open. The four-arrow specialization and its normalized coefficient are not stated in the inspected full text. Ringel's earlier 2026 preprint concerns brick-chain complexity measured by filtration length rather than the number of brick-chain filtrations, so it does not imply the count-growth bound here.

Searches for the four-arrow specialization, the exact constant \((2+\log(3/8))/72\), and equivalent normalized Kronecker formulations found no prior statement of this improvement. The main residual originality risk is the recency of the source preprint and the possibility that the same one-parameter optimization has appeared under different terminology or in material not yet indexed.

## Limitations
The result does not determine the global limsup and does not optimize over unequal \(a,b\), other partitions, or constructions outside this Kronecker family. The lower bound inherits the source theorem's algebraically closed-field hypothesis. The independent audit channel has not been performed.

## References
1. Haruhisa Enomoto, *Finiteness and growth of brick chain filtrations*, arXiv:2609.10217, first public version 2026-09-09.
2. Claus Michael Ringel, *The brick chain complexity of an artin algebra*, arXiv:2606.27879, first public version 2026-06-26.
