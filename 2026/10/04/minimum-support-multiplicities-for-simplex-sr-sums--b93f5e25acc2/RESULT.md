# Minimum-support multiplicities for simplex SR-sums
## Finding

Let
\[
2\le k_1<k_2
\]
and let \(q\) be a prime power. Consider Kwiatkowski's Griesmer-optimal simplex SR-sum
\[
C=K(S(k_1,q))\oplus_{\mathrm{SR}}K(S(k_2,q)).
\]
Its dimension is
\[
k=k_1+k_2
\]
and its length is
\[
n=(q^{k_1}-1)(q^{k_2}-1).
\]

For \(1\le r\le k\), define
\[
a_r=\max(0,k_1-r),\qquad
b_r=\max(0,k_2-r),
\]
and
\[
c_r=k-r-a_r-b_r.
\]
Write
\[
\left[{u\atop v}\right]_q
\]
for the Gaussian binomial coefficient.

Then the number \(M_r\) of \(r\)-dimensional subcodes attaining the \(r\)-th generalized Hamming weight is
\[
M_r=
\left[{k_1\atop a_r}\right]_q
\left[{k_2\atop b_r}\right]_q
\left[{k_1-a_r\atop c_r}\right]_q
\left[{k_2-b_r\atop c_r}\right]_q
|\mathrm{GL}(c_r,q)|.
\]

For \(k_1<k_2\), this becomes the three-part formula
\[
M_r=
\left[{k_1\atop r}\right]_q
\left[{k_2\atop r}\right]_q
|\mathrm{GL}(r,q)|
\qquad (1\le r\le k_1),
\]
\[
M_r=
\left[{k_2\atop r}\right]_q
\left[{r\atop k_1}\right]_q
|\mathrm{GL}(k_1,q)|
\qquad (k_1<r\le k_2),
\]
and, with \(c=k_1+k_2-r\),
\[
M_r=
\left[{k_1\atop c}\right]_q
\left[{k_2\atop c}\right]_q
|\mathrm{GL}(c,q)|
\qquad (k_2<r\le k_1+k_2).
\]

For context, the generalized weights are
\[
d_r=
q^{k_1+k_2}-q^{k_1+k_2-r}-q^{k_1}-q^{k_2}
+q^{a_r}+q^{b_r}.
\]
These weight values are not claimed as new: generalized Griesmer theory already implies the hierarchy for a code meeting the classical Griesmer bound. The finding here is the exact structure and multiplicity of all subcodes attaining each \(d_r\).

For the binary case
\[
(q,k_1,k_2)=(2,2,3),
\]
the hierarchy is
\[
(10,15,18,20,21)
\]
and the corresponding minimizer counts are
\[
(21,42,42,21,1).
\]
For
\[
(q,k_1,k_2)=(3,2,3),
\]
the hierarchy is
\[
(138,184,200,206,208)
\]
and the minimizer counts are
\[
(104,624,624,104,1).
\]

## Assumptions and scope

Let
\[
V=V_1\oplus V_2,
\qquad
\dim V_i=k_i.
\]
The source's projective description of the simplex SR-sum shows that, after projective normalization, its generator columns are exactly
\[
\operatorname{PG}(V)
\setminus
\bigl(\operatorname{PG}(V_1)\cup\operatorname{PG}(V_2)\bigr),
\]
with every projective point repeated \(q-1\) times.

For an \(r\)-dimensional subcode, let \(U\le V\) be its message subspace and put
\[
W=U^\perp.
\]
Then
\[
\dim W=k-r.
\]
Set
\[
a=\dim(W\cap V_1),\qquad
b=\dim(W\cap V_2).
\]

The statement is made for the two-simplex family in the source with unequal dimensions, ordered as \(k_1<k_2\). It does not claim an analogous formula for an arbitrary SR-sum.

## Proof

A projective generator column is zero on the entire subcode \(U\) precisely when its representing vector lies in \(W=U^\perp\). Therefore the zero projective columns are
\[
\operatorname{PG}(W)
\setminus
\left(
\operatorname{PG}(W\cap V_1)\cup
\operatorname{PG}(W\cap V_2)
\right).
\]
Their number is
\[
\frac{q^{k-r}-q^a-q^b+1}{q-1}.
\]
Because each projective column occurs \(q-1\) times, the subcode support is
\[
q^{k_1+k_2}-q^{k_1+k_2-r}-q^{k_1}-q^{k_2}+q^a+q^b.
\]

Dimension inequalities give
\[
a\ge \max(0,k_1-r)=a_r
\]
and
\[
b\ge \max(0,k_2-r)=b_r.
\]
Hence the support is minimized exactly when
\[
a=a_r,\qquad b=b_r.
\]
These bounds are simultaneously attainable, as the construction below also shows.

Fix
\[
A=W\cap V_1,\qquad B=W\cap V_2
\]
with dimensions \(a_r,b_r\). In the quotient
\[
(V_1/A)\oplus(V_2/B),
\]
the image
\[
\overline W=W/(A\oplus B)
\]
has dimension
\[
c_r
\]
and intersects each coordinate summand trivially. Its two coordinate projections are therefore injective. Thus \(\overline W\) is the graph of an isomorphism
\[
T:X\longrightarrow Y
\]
between a \(c_r\)-dimensional subspace
\[
X\le V_1/A
\]
and a \(c_r\)-dimensional subspace
\[
Y\le V_2/B.
\]

Conversely, every choice of \(A,B,X,Y\) and isomorphism \(T:X\to Y\) yields a unique \(W\) with the required two intersection dimensions. Therefore the number of minimizing \(W\), and hence the number of minimizing \(r\)-subcodes, is
\[
\left[{k_1\atop a_r}\right]_q
\left[{k_2\atop b_r}\right]_q
\left[{k_1-a_r\atop c_r}\right]_q
\left[{k_2-b_r\atop c_r}\right]_q
|\mathrm{GL}(c_r,q)|.
\]

Substituting the three ranges for \(r\) gives the stated piecewise formulas.

At \(r=1\),
\[
(q-1)M_1=(q^{k_1}-1)(q^{k_2}-1),
\]
which agrees with the minimum-weight codeword frequency in the source's ordinary weight distribution.

## Verification

`artifacts/verify.py` uses only the Python standard library and independently constructs the projective generator set for the two small instances
\[
(q,k_1,k_2)=(2,2,3)
\]
and
\[
(q,k_1,k_2)=(3,2,3).
\]

For every \(r\), it enumerates all \(r\)-dimensional message subspaces in reduced row-echelon form, computes each subcode support directly from the projective generator columns with multiplicity \(q-1\), and compares the observed minimum and number of minimizers with the closed formulas.

It verifies
\[
(d_1,\ldots,d_5)=(10,15,18,20,21),
\qquad
(M_1,\ldots,M_5)=(21,42,42,21,1)
\]
over \(\mathbb F_2\), and
\[
(d_1,\ldots,d_5)=(138,184,200,206,208),
\qquad
(M_1,\ldots,M_5)=(104,624,624,104,1)
\]
over \(\mathbb F_3\).

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Kwiatkowski introduces the SR-sum, gives its weight-distribution machinery, explains the projective shortening of SR-sum generator columns, and proves that the unequal-dimension simplex family
\[
K(S(k_1,q))\oplus_{\mathrm{SR}}K(S(k_2,q))
\]
meets the classical Griesmer bound. The source does not classify minimum-support subcodes of higher dimension.

Kurz, Landjev, and Rousseva prove a generalized Griesmer theorem showing that a code meeting the classical Griesmer bound attains the generalized Griesmer bound at every generalized weight. Consequently the values \(d_r\) above are already covered in stronger generality and are used only as context here.

The new statement is finer: it counts and structurally parametrizes every \(r\)-dimensional subcode that attains \(d_r\). Searches using the SR-sum name, the equivalent punctured-projective-space description, Solomon--Stiffler terminology, generalized-weight minimizers, and the Gaussian-binomial multiplicity formula did not locate an earlier same-family count.

## Limitations

No novelty is claimed for the generalized Hamming-weight values themselves.

The counting identity for subspaces with prescribed intersections is standard finite-dimensional linear algebra; the contribution is its exact application to classify all generalized-weight minimizers in this newly introduced SR-sum family.

An older finite-geometry source not indexed by the searched terminology could contain an equivalent prescribed-intersection count specialized to the same punctured projective system.

The theorem concerns two simplex summands. More general SR-sums can have different projective multiplicities and need separate analysis.

## References

1. Mariusz Kwiatkowski, *SR-sum of linear codes*, Advances in Mathematics of Communications 25 (2026), 267--281, DOI 10.3934/amc.2026052.
2. Sascha Kurz, Ivan Landjev, and Assia Rousseva, *Optimal codes and arcs for the generalized Hamming weights*, arXiv:2601.00250v1, 2026.
3. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
