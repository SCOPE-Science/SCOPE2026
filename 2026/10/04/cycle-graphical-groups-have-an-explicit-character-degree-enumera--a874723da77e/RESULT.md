# Cycle graphical groups have an explicit character-degree enumerator

## Finding

Let \(q\) be a prime power and let \(n\ge5\). Label the edges of the cycle \(C_n\) cyclically by
\[
y_1,\ldots,y_n\in\mathbf F_q,
\]
and let \(B_{C_n}(y)\) be the corresponding \(n\times n\) antisymmetric weighted adjacency matrix. Define
\[
\rho_i(C_n;q)
=
\left|
\left\{
y\in\mathbf F_q^n:
\operatorname{rk}B_{C_n}(y)=2i
\right\}
\right|.
\]
Put
\[
Q=q(q-1)
\]
and
\[
A_{n,j}
=
\frac{n}{n-j}\binom{n-j}{j}.
\]

If
\[
n=2m+1,
\]
then
\[
\boxed{
\rho_i(C_n;q)=A_{n,i}Q^i
\quad(0\le i<m),
}
\]
and
\[
\boxed{
\rho_m(C_n;q)
=
A_{n,m}Q^m+(q-1)^n.
}
\]

If
\[
n=2m,
\]
then
\[
\boxed{
\rho_i(C_n;q)=A_{n,i}Q^i
\quad(0\le i<m-1),
}
\]
while the two top ranks satisfy
\[
\boxed{
\rho_{m-1}(C_n;q)
=
A_{n,m-1}Q^{m-1}+(q-1)^{n-1},
}
\]
and
\[
\boxed{
\rho_m(C_n;q)
=
2Q^m-q(q-1)^{n-1}.
}
\]

Equivalently, define
\[
L_n(q;u)
=
\sum_{j=0}^{\lfloor n/2\rfloor}
A_{n,j}Q^j u^j.
\]
Then the complete rank enumerator
\[
R_n(q;u)
=
\sum_i \rho_i(C_n;q)u^i
\]
is
\[
\boxed{
R_{2m+1}(q;u)
=
L_{2m+1}(q;u)
+
(q-1)^{2m+1}u^m,
}
\]
and
\[
\boxed{
R_{2m}(q;u)
=
L_{2m}(q;u)
+
(q-1)^{2m-1}u^{m-1}
-
q(q-1)^{2m-1}u^m.
}
\]

For every odd prime power \(q\), let
\[
\mathbf G_{C_n}(\mathbf F_q)
\]
be the graphical group associated with \(C_n\). Then the number of irreducible characters of degree \(q^i\) is
\[
\boxed{
\operatorname{ch}(C_n,i;q)
=
q^{n-2i}\rho_i(C_n;q).
}
\]
Thus every cycle graph has an explicit polynomial character-degree enumeration.

## Assumptions and scope

The rank formulas hold for every finite field, including characteristic \(2\). The character formula is asserted only for odd \(q\), exactly where the class-two graphical group is covered by the character-rank correspondence used in the primary literature.

The notation
\[
\operatorname{ch}(C_n,i;q)
\]
means the number of ordinary irreducible complex characters of
\[
\mathbf G_{C_n}(\mathbf F_q)
\]
having degree \(q^i\).

The domain \(n\ge5\) is chosen because the literature problem is about new graph families beyond the already treated elementary cases; the rank-enumerator argument itself also specializes to smaller cycles.

## Proof

Write
\[
t=q-1.
\]
First suppose that at least one edge weight vanishes. The support of the nonzero edge weights is then a disjoint union of paths. A run of \(r\ge1\) consecutive nonzero cycle edges contributes a weighted path on \(r+1\) vertices.

Every nonzero weighted path can be diagonally rescaled to the unweighted path without changing rank. Its antisymmetric adjacency matrix has rank
\[
2\left\lceil\frac r2\right\rceil.
\]
Indeed, the determinant of every even-order weighted path is the square of the product of alternating edge weights, and the odd-order case has a full-rank even principal subpath. Therefore the half-rank contributed by a nonzero run of length \(r\) is
\[
\left\lceil\frac r2\right\rceil.
\]

The proper support patterns can be counted by a three-state cyclic transfer matrix. The states record whether the current nonzero run has not started, has odd length, or has even positive length. With \(u\) marking half-rank and \(t\) marking a nonzero edge, take
\[
M=
\begin{pmatrix}
1&tu&0\\
1&0&t\\
1&tu&0
\end{pmatrix}.
\]
For any support containing at least one zero, the cyclic state sequence is unique and has weight
\[
t^{|\operatorname{supp}(y)|}
u^{\operatorname{rk}B_{C_n}(y)/2}.
\]
Consequently the trace
\[
\operatorname{tr}(M^n)
\]
counts all proper support patterns with exactly the required weights.

The matrix \(M\) has one zero eigenvalue, while its two nonzero eigenvalues satisfy
\[
\lambda^2-\lambda-Q u=0,
\qquad
Q=t(t+1)=q(q-1).
\]
Hence
\[
L_n(q;u):=\operatorname{tr}(M^n)
\]
satisfies
\[
L_n=L_{n-1}+QuL_{n-2},
\]
with
\[
L_1=1,
\qquad
L_2=1+2Qu.
\]
The standard Lucas-polynomial expansion gives
\[
L_n(q;u)
=
\sum_{j=0}^{\lfloor n/2\rfloor}
\frac{n}{n-j}\binom{n-j}{j}
Q^j u^j.
\]

The only remaining issue is the all-nonzero support.

If \(n=2m+1\) is odd, every edge weight is nonzero and every principal path obtained by deleting one vertex has even order \(2m\) and nonzero determinant. Therefore
\[
\operatorname{rk}B_{C_n}(y)=2m
\]
for every all-nonzero specialization. There are
\[
t^n
\]
such specializations. The cyclic transfer trace does not count the all-nonzero odd support, which proves
\[
R_{2m+1}
=
L_{2m+1}+t^{2m+1}u^m.
\]

Now let \(n=2m\). For an all-nonzero specialization, the Pfaffian is, up to an irrelevant sign,
\[
y_1y_3\cdots y_{2m-1}
-
y_2y_4\cdots y_{2m}.
\]
Among the
\[
t^{2m}
\]
all-nonzero assignments, exactly
\[
t^{2m-1}
\]
make this Pfaffian zero: after choosing any \(2m-1\) nonzero weights, the final weight is uniquely forced and remains nonzero.

If the Pfaffian is nonzero, the matrix has rank \(2m\). If it vanishes, the rank is exactly \(2m-2\), because deleting two adjacent vertices leaves an even-order weighted path with nonzero determinant. Thus the actual all-nonzero contribution is
\[
t^{2m-1}u^{m-1}
+
\left(t^{2m}-t^{2m-1}\right)u^m.
\]
For even \(n\), the cyclic transfer trace counts the all-nonzero support twice, once for each parity phase, contributing
\[
2t^{2m}u^m.
\]
Replacing that artificial contribution by the true one yields
\[
R_{2m}
=
L_{2m}
+t^{2m-1}u^{m-1}
-q t^{2m-1}u^m.
\]
Taking coefficients gives the displayed rank formulas.

Finally assume \(q\) is odd. The graphical group for \(C_n\) has
\[
n
\]
vertex generators modulo its derived subgroup. The general character-rank theorem for class-two groups gives
\[
\operatorname{ch}(C_n,i;q)
=
\rho_i(C_n;q)
\left|\mathbf G_{C_n}(\mathbf F_q)/
\mathbf G_{C_n}(\mathbf F_q)'\right|
q^{-2i}.
\]
Since the abelianization has order
\[
q^n,
\]
this becomes
\[
\operatorname{ch}(C_n,i;q)
=
q^{n-2i}\rho_i(C_n;q).
\]

As a consistency check,
\[
\sum_i
\operatorname{ch}(C_n,i;q)q^{2i}
=
q^n\sum_i\rho_i(C_n;q)
=
q^{2n},
\]
which equals the order of the graphical group because \(C_n\) has \(n\) vertices and \(n\) edges.

## Verification

The included replay constructs the antisymmetric weighted cycle matrix directly and computes ranks over
\[
\mathbf F_2,\ \mathbf F_3,\ \mathbf F_4,\ \mathbf F_5.
\]
The field
\[
\mathbf F_4
\]
is implemented as
\[
\mathbf F_2[z]/(z^2+z+1).
\]

It exhaustively checks the rank distribution against the closed formulas for
\[
(n,q)=(5,2),(5,3),(6,3),(7,3),(8,2),(6,4),(5,5).
\]
The verified rank-count vectors are respectively
\[
(1,10,21),
\]
\[
(1,30,212),
\]
\[
(1,36,356,336),
\]
\[
(1,42,504,1640),
\]
\[
(1,16,80,129,30),
\]
\[
(1,72,1539,2484),
\]
and
\[
(1,100,3024).
\]

For every checked case the counts sum to \(q^n\). For odd \(q\), the replay also verifies that the resulting character multiplicities satisfy the irreducible-degree sum-of-squares identity
\[
\sum_i
\operatorname{ch}(C_n,i;q)q^{2i}
=
q^{2n}.
\]

The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the formulas.

## Relationship to prior work

Rossmann's 2021 paper formulates the character-enumeration problem for graphical groups as Question 1.10. It records polynomial answers for the edgeless graphs, path graphs, and complete graphs, and then rewrites the general problem as counting specializations of a generic antisymmetric graph matrix by rank. The paper explicitly says that it is unclear whether this rank-count approach can answer the question in general.

The cycle family is the first natural unicyclic family beyond the path case. The present calculation answers the rank-count problem for all cycles by separating proper supports, which are path forests, from the all-nonzero support. The even-cycle case has a genuine additional phenomenon absent from paths: cancellation between the two perfect-matching monomials in the Pfaffian. This is exactly the source of the two correction terms in the even formula.

O'Brien and Voll's general class-two character theorem is used only to convert the new cycle rank counts into character multiplicities for odd \(q\). Their theorem does not enumerate the cycle specializations.

Targeted searches under “graphical groups”, “cycle graph”, “irreducible characters”, “weighted antisymmetric cycle”, “skew adjacency rank”, and “rank distribution over finite fields” did not locate the displayed cycle rank enumerator or its graphical-group character formula.

## Limitations

The character statement is restricted to odd \(q\), matching the available graphical-group character-rank theorem. The matrix rank enumerator itself is proved for every finite field.

The result treats cycles only. More general unicyclic graphs attach trees to a cyclic core, and their rank distributions require additional bookkeeping.

An equivalent weighted-cycle rank distribution may exist in finite-matrix or Pfaffian-enumeration literature under terminology not captured by the searches. Failed searches do not prove novelty.

## References

1. T. Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” arXiv:2107.05564v1, first public version 12 July 2021; *Bulletin of the London Mathematical Society* 54 (2022), 1830–1846. Primary MSC 20D15.
2. E. A. O'Brien and C. Voll, “Enumerating classes and characters of \(p\)-groups,” arXiv:1203.3050, *Transactions of the American Mathematical Society* 367 (2015), 7775–7796.
