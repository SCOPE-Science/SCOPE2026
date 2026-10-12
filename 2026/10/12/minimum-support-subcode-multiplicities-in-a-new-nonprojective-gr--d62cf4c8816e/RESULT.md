# Minimum-support subcode multiplicities in a new nonprojective Griesmer family
## Finding

Let \(p\) be an odd prime and let
\[
n\ge3,\qquad 2\le m\le n-1,\qquad 1\le t\le p-1.
\]
Pelen's Theorem 4.4 defines
\[
D=\mathbb F_p^n\setminus I,
\]
where
\[
I=
(\mathbb F_p^m\times0)
\cup
\left\{
(-1,\ldots,-1,j,0,\ldots,0):1\le j\le t
\right\}.
\]
The resulting code \(C_D\) has dimension \(n\), length
\[
N=p^n-p^m-t,
\]
and meets the classical Griesmer bound.

For every \(1\le r\le n\),
\[
d_r(C_D)
=
p^n-p^m-t-p^{n-r}+p^{\max(0,m-r)}.
\]

The exact number \(M_r\) of \(r\)-dimensional subcodes attaining \(d_r(C_D)\) is also explicit.

For \(1\le r\le m\), set
\[
a=m-r,\qquad c=n-m.
\]
Then
\[
M_r
=
p^{r(c-1)}
\left(
\left[{m-1\atop a-1}\right]_p(p^r-1)
+
p^a
\left[{m-1\atop a}\right]_p(p^r-t)
\right).
\]

For \(m<r<n\), set
\[
h=n-r,\qquad c=n-m.
\]
Then
\[
M_r
=
p^{mh}\left[{c\atop h}\right]_p
-
t\,p^{m(h-1)}
\left[{c-1\atop h-1}\right]_p.
\]

Finally,
\[
M_n=1.
\]

Here
\[
\left[{u\atop v}\right]_p
\]
denotes a Gaussian binomial coefficient, interpreted as zero when \(v<0\) or \(v>u\).

The generalized-weight values themselves are not the originality claim: a code meeting the classical Griesmer bound attains the generalized Griesmer bound at every order. The new statement is the exact description and count of all subcodes attaining those weights.

## Assumptions and scope

Let
\[
V=\mathbb F_p^n,
\qquad
A=\mathbb F_p^m\times0\le V,
\]
and write
\[
b_j=(-1,\ldots,-1,j,0,\ldots,0),
\qquad
1\le j\le t.
\]
Thus
\[
I=A\cup\{b_1,\ldots,b_t\}.
\]

The code is
\[
C_D=
\left\{
(u\cdot x)_{x\in D}:u\in V
\right\}.
\]
Pelen proves that this is an
\[
[p^n-p^m-t,n,(p-1)(p^{n-1}-p^{m-1})-t]_p
\]
Griesmer code.

For an \(r\)-dimensional message subspace \(U\le V\), let
\[
W=U^\perp,
\qquad
\dim W=n-r.
\]
The support of the corresponding subcode is the complement, inside \(D\), of the coordinates indexed by
\[
D\cap W.
\]

## Proof

Let
\[
a=\dim(W\cap A)
\]
and let
\[
s=
\left|
\{j: b_j\in W\}
\right|.
\]
Since
\[
D=V\setminus I,
\]
the number of zero coordinates of the subcode is
\[
|D\cap W|
=
|W|-|W\cap I|
=
p^{n-r}-(p^a+s).
\]
Therefore its support size is
\[
N-p^{n-r}+p^a+s.
\]

By the dimension formula,
\[
a\ge\max(0,m-r).
\]
Thus the support is minimized exactly when
\[
a=\max(0,m-r)
\]
and simultaneously
\[
s=0.
\]
Such subspaces exist in every order, as is also made explicit by the counting construction below. Hence
\[
d_r(C_D)
=
N-p^{n-r}+p^{\max(0,m-r)}.
\]

It remains to count the minimizing \(W\).

Assume first that
\[
1\le r\le m.
\]
Then
\[
a=m-r,
\]
and if
\[
C_0=\mathbb F_p^{n-m}
\]
denotes a fixed complement of \(A\), the projection of \(W\) to \(C_0\) must be all of \(C_0\). Fix
\[
A_0=W\cap A,
\qquad
\dim A_0=a.
\]
Every such \(W\) is the graph, modulo \(A_0\), of a linear map
\[
f:C_0\to A/A_0.
\]

Let
\[
\alpha=(-1,\ldots,-1)\in A.
\]
If
\[
\alpha\in A_0,
\]
then all selected vectors \(b_j\) correspond to the single forbidden value
\[
f(e)=0
\]
at the distinguished first basis vector \(e\in C_0\). The number of allowed maps is therefore
\[
(p^r-1)p^{r(c-1)}.
\]

If
\[
\alpha\notin A_0,
\]
the \(t\) selected vectors give \(t\) distinct forbidden values of \(f(e)\), so the number of allowed maps is
\[
(p^r-t)p^{r(c-1)}.
\]

The number of \(a\)-subspaces \(A_0\) containing \(\alpha\) is
\[
\left[{m-1\atop a-1}\right]_p,
\]
while the number not containing \(\alpha\) is
\[
p^a\left[{m-1\atop a}\right]_p.
\]
Multiplying and adding gives the first formula for \(M_r\).

Now assume
\[
m<r<n.
\]
Then a minimizing \(W\) satisfies
\[
W\cap A=0.
\]
Put
\[
h=n-r,\qquad c=n-m.
\]
Choose the projected \(h\)-space
\[
Y\le C_0.
\]
If the distinguished vector \(e\notin Y\), every linear map
\[
f:Y\to A
\]
is allowed. If
\[
e\in Y,
\]
exactly \(t\) possible values of \(f(e)\) are forbidden.

There are
\[
\left[{c-1\atop h-1}\right]_p
\]
such \(Y\) containing \(e\). Starting from all
\[
p^{mh}\left[{c\atop h}\right]_p
\]
graphs and subtracting the forbidden ones gives
\[
M_r
=
p^{mh}\left[{c\atop h}\right]_p
-
t\,p^{m(h-1)}
\left[{c-1\atop h-1}\right]_p.
\]

At
\[
r=n,
\]
the only subcode is the whole code, so
\[
M_n=1.
\]

## Verification

`artifacts/verify.py` uses only the Python standard library.

It reconstructs \(D\) directly and enumerates every subspace of the message space in reduced row-echelon form for the following five instances:
\[
(p,n,m,t)=(3,4,2,1),
\]
\[
(3,4,2,2),
\]
\[
(3,5,3,2),
\]
\[
(5,4,2,1),
\]
and
\[
(5,4,2,4).
\]

For each \(r\), the verifier computes every subcode support directly from the defining set and checks both the minimum support and its multiplicity against the formulas above.

For example, when
\[
(p,n,m,t)=(3,4,2,2),
\]
the hierarchy is
\[
(46,62,68,70)
\]
and the numbers of minimizers are
\[
(15,63,34,1).
\]

When
\[
(p,n,m,t)=(5,4,2,4),
\]
the hierarchy is
\[
(476,572,592,596)
\]
and the corresponding multiplicities are
\[
(45,525,146,1).
\]

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Pelen introduces the generalized-order-ideal construction and proves that the family above is a nonprojective Griesmer family with at most five nonzero ordinary weights. The paper identifies its projective multiplicity geometry as a Belov-type anticode construction, but it does not discuss generalized Hamming weights or the number of higher-dimensional extremal subcodes.

Kurz, Landjev, and Rousseva prove that every code meeting the classical Griesmer bound also meets the generalized Griesmer bound at every generalized-weight order. Their theorem therefore covers the values \(d_r(C_D)\) in stronger generality. It does not count the subcodes attaining each \(d_r\).

Pan--Chen--Liu--Liu determine full subcode-support weight distributions for several modified Solomon--Stiffler families obtained from repeated simplex codes by deleting whole projective subspaces. That framework is highly relevant, but the present family is nonprojective and has an additional partial multiplicity defect concentrated on selected representatives along one projective line. Their formulas therefore do not directly cover the present code.

Earlier subcode-support work on down-set codes is also inapplicable to this exact defining set: Pelen explicitly notes that once the generalized order ideal meets the upper level, these defining sets are neither ordinary down-sets nor unions of coordinate subspaces.

Focused searches using the source title, Theorem 4.4 parameters, Belov-type terminology, the equivalent deleted-subspace-plus-exceptional-line geometry, and minimum-support-subcode multiplicities found no prior formula for \(M_r\).

## Limitations

The theorem applies to the specific one-upper-element saturated family of Pelen's Theorem 4.4. It does not automatically extend to arbitrary generalized order ideals or to the characteristic-function codes later in the paper.

No novelty is claimed for the generalized Hamming-weight values themselves.

The counting argument classifies minimum-support subcodes only; it does not determine the complete support-weight distribution in every subcode dimension.

A finite-geometry source using different terminology could contain an equivalent prescribed-intersection count, although no such same-family specialization was found in the inspected literature.

## References

1. Rumi Melih Pelen, *Optimal and minimal \(p\)-ary linear codes from generalized order ideals of hierarchical posets*, arXiv:2609.33128v1, 27 September 2026.
2. Sascha Kurz, Ivan Landjev, and Assia Rousseva, *Optimal codes and arcs for the generalized Hamming weights*, arXiv:2601.00250v1, 1 January 2026.
3. Xu Pan, Hao Chen, Hongwei Liu, and Shengwei Liu, *Optimal Few-GHW Linear Codes and Their Subcode Support Weight Distributions*, arXiv:2408.10005v1, 19 August 2024.
4. Yu Luo and Zihui Liu, *On the Subcode-Support-Weight Distributions of Some Classes of Optimal Codes*, IEEE Transactions on Information Theory 69 (2023), 1531--1543, DOI 10.1109/TIT.2022.3217078.
