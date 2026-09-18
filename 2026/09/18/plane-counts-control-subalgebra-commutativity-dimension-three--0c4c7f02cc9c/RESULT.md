# Plane counts control subalgebra commutativity in dimension three

Let \(q\) be a prime power and let \(L\) be a three-dimensional Lie algebra over
\(\mathbb F_q\). Write \(\mathcal L(L)\) for its lattice of Lie subalgebras and
\[
\operatorname{sd}(L)
=
\frac{|\{(A,B)\in\mathcal L(L)^2:[A,B]\subseteq A+B\}|}
     {|\mathcal L(L)|^2}
\]
for the subalgebra commutativity degree introduced by Muhie--Otera--Russo.
Let
\[
N=q^2+q+1
\]
be the number of one-dimensional subspaces of \(L\), and let \(t(L)\) be the
number of two-dimensional Lie subalgebras of \(L\).

## The universal three-dimensional formula

For every three-dimensional \(L/\mathbb F_q\),
\[
\boxed{
\operatorname{sd}(L)
=
1-\frac{q(q+1)(N-t(L))}{(N+t(L)+2)^2}.
}
\]
Equivalently, since
\[
|\mathcal L(L)|=N+t(L)+2,
\]
the subalgebra commutativity degree is determined solely by the total number of
subalgebras:
\[
\boxed{
\operatorname{sd}(L)
=
1-\frac{q(q+1)\bigl(2q^2+2q+4-|\mathcal L(L)|\bigr)}
        {|\mathcal L(L)|^2}.
}
\]

If \(F_2(L)\) denotes the factorization number used in
Muhie--Otera--Russo, namely the number of ordered pairs
\((A,B)\in\mathcal L(L)^2\) with \(A+B=L\), then
\[
\boxed{
F_2(L)
=
t(L)^2+(2q^2+1)t(L)+2q^2+2q+5.
}
\]
Both displayed functions are strictly increasing in \(t\) on \(0\le t\le N\).
Consequently, for three-dimensional Lie algebras \(L_1,L_2\) over the same
\(\mathbb F_q\),
\[
\boxed{
\operatorname{sd}(L_1)=\operatorname{sd}(L_2)
\iff
t(L_1)=t(L_2)
\iff
|\mathcal L(L_1)|=|\mathcal L(L_2)|
\iff
F_2(L_1)=F_2(L_2).
}
\]

### Proof

Every one-dimensional subspace is a Lie subalgebra, so there are \(N\) lines.
Together with the zero algebra, \(L\) itself, and the \(t=t(L)\) Lie-subalgebra
planes, this gives \(|\mathcal L(L)|=N+t+2\).

Any ordered pair involving \(0\) or \(L\) is permutable. Any pair involving a
Lie-subalgebra plane is also permutable: two distinct planes sum to \(L\), and a
line together with a plane either lies inside that plane or sums to \(L\).
Thus the only possible nonpermutable pairs are two distinct lines.

Two distinct lines \(A,B\) are permutable exactly when their vector-space span
\(A+B\) is a two-dimensional Lie subalgebra. There are
\[
N(N-1)=Nq(q+1)
\]
ordered pairs of distinct lines. Every Lie-subalgebra plane contains \(q+1\)
lines and hence contributes \(q(q+1)\) ordered pairs of distinct lines. Two
distinct lines determine a unique vector-space plane, so these contributions do
not overlap. Therefore the number of nonpermutable ordered pairs is
\[
q(q+1)(N-t),
\]
which proves the formula for \(\operatorname{sd}(L)\).

For \(F_2(L)\), the ordered factorizations are: the \(2|\mathcal L(L)|-1\)
pairs with at least one factor equal to \(L\); the \(t(t-1)\) ordered pairs of
distinct Lie-subalgebra planes; and the \(2tq^2\) ordered line--plane pairs in
which the line is not contained in the plane. Hence
\[
F_2(L)
=
2(N+t+2)-1+t(t-1)+2tq^2,
\]
which simplifies to the displayed expression.

Finally,
\[
\frac{d}{dt}
\left(
1-\frac{q(q+1)(N-t)}{(N+t+2)^2}
\right)
=
\frac{q(q+1)(3N-t+2)}{(N+t+2)^3}>0
\]
for \(0\le t\le N\), while \(F_2(L)\) is visibly strictly increasing in \(t\).
This proves all equivalences.

## Complete four-value classification

A three-dimensional Lie algebra is either solvable or perfect: if \(L'\ne L\), then \(\dim L'\le2\), and every Lie algebra of dimension at most two is solvable. Thus the solvable and perfect cases below exhaust all possibilities.

Every three-dimensional Lie algebra over \(\mathbb F_q\) has exactly one of the
following four values of the subalgebra commutativity degree:
\[
\boxed{
D_0(q)=
\frac{8(q^2+q+2)}{(q^2+q+4)^2},
}
\]
\[
\boxed{
D_1(q)=
\frac{3q^3+12q^2+16q+16}{(q^2+2q+4)^2},
}
\]
\[
\boxed{
D_2(q)=
\frac{6q^3+18q^2+24q+16}{(q^2+3q+4)^2},
}
\qquad
\boxed{D_3(q)=1.}
\]
They satisfy
\[
D_0(q)<D_1(q)<D_2(q)<1.
\]
All four values occur for every prime power \(q\): one may take an irreducible quadratic companion matrix for \(D_0\), a nilpotent Jordan block (the Heisenberg algebra) for \(D_1\), \(T=\operatorname{diag}(0,1)\) for \(D_2\), and a scalar action for \(D_3\).

More precisely:

1. \(D_0(q)\) occurs exactly for solvable \(L\) whose two-dimensional abelian
   ideal \(V\) admits a presentation
   \[
   L=\mathbb F_qx\ltimes_TV
   \]
   in which \(T=\operatorname{ad}_x|_V\) has no
   \(\mathbb F_q\)-rational invariant line, equivalently its characteristic
   polynomial is irreducible.

2. \(D_1(q)\) occurs exactly when either \(L\) is perfect, or \(L\) is solvable
   and \(T\) has exactly one invariant line, equivalently \(T\) is nonscalar
   with a repeated eigenvalue. In particular the three-dimensional Heisenberg
   algebra has this value.

3. \(D_2(q)\) occurs exactly for solvable \(L\) for which \(T\) has exactly two
   invariant lines, equivalently \(T\) has two distinct eigenvalues in
   \(\mathbb F_q\).

4. \(D_3(q)=1\) occurs exactly for solvable \(L\) for which \(T\) is scalar.
   This includes the abelian algebra (\(T=0\)) and the nonabelian
   almost-abelian scalar-action algebra (\(T\ne0\)).

Thus
\[
\boxed{
\frac{8(q^2+q+2)}{(q^2+q+4)^2}
\le \operatorname{sd}(L)\le1
}
\]
is sharp for all three-dimensional Lie algebras over \(\mathbb F_q\).
The three nontrivial values have asymptotics
\[
D_0(q)\sim\frac8{q^2},\qquad
D_1(q)\sim\frac3q,\qquad
D_2(q)\sim\frac6q.
\]

### Solvable case: projective eigenlines

A solvable three-dimensional Lie algebra has a two-dimensional abelian ideal
\(V\). Here is a short argument valid in every characteristic. If
\(\dim L'\le1\), then either \(L'=0\), or a plane containing \(L'\) can be
chosen abelian and ideal; when \(L'=\mathbb F_qd\) is noncentral, write
\([x,d]=\lambda(x)d\) and take \(V=\ker\lambda\).

If \(\dim L'=2\), put \(D=L'\). If \(D\) were nonabelian, choose a basis
\(y,z\) of \(D\) with \([y,z]=z\). For \(x\notin D\),
\(\delta=\operatorname{ad}_x|_D\) is a derivation. Writing
\[
\delta(y)=ay+bz,\qquad \delta(z)=cy+dz
\]
and applying \(\delta\) to \([y,z]=z\) gives \(a=c=0\). Hence
\(\delta(D)\subseteq\mathbb F_qz\), and therefore
\[
L'=[x,D]+[D,D]\subseteq\mathbb F_qz,
\]
contradicting \(\dim L'=2\). Thus \(D\) itself is an abelian ideal.

Choose \(x\notin V\) and write \(T=\operatorname{ad}_x|_V\). Let
\[
e(T)=
|\{\ell\in\mathbb P(V):T\ell\subseteq\ell\}|
\]
be the number of projective eigenlines of \(T\). A Lie-subalgebra plane is
either \(V\), or has the form
\[
U=\ell\oplus\mathbb F_q(x+u)
\]
with \(\ell=U\cap V\). Such a plane is closed under brackets exactly when
\(T\ell\subseteq\ell\). For each invariant line \(\ell\), the choice of
\(u\) is modulo \(\ell\), giving exactly \(q\) distinct planes. Therefore
\[
\boxed{t(L)=1+q\,e(T).}
\]
For a \(2\times2\) endomorphism over \(\mathbb F_q\),
\[
e(T)\in\{0,1,2,q+1\},
\]
according as its characteristic polynomial is irreducible; it has one repeated
eigenvalue but is nonscalar; it has two distinct eigenvalues; or it is scalar.
Hence
\[
t(L)\in\{1,q+1,2q+1,N\},
\]
and substitution into the universal formula yields the four values above.

### Perfect case: a finite conic

It remains to show that every perfect three-dimensional Lie algebra has
\(t(L)=q+1\), without classifying perfect forms.

Fix a basis \(e_1,e_2,e_3\), and form the \(3\times3\) matrix \(A\) whose
columns are the coordinate vectors of
\[
[e_2,e_3],\qquad [e_3,e_1],\qquad [e_1,e_2].
\]
Perfectness makes the bracket map
\(\Lambda^2L\to L\) surjective, hence \(A\) is invertible. Moreover
\[
\operatorname{tr}(\operatorname{ad}_{[x,y]})
=
\operatorname{tr}([\operatorname{ad}_x,\operatorname{ad}_y])=0.
\]
Since \(L=[L,L]\), every adjoint map has trace zero. In the chosen basis these
three trace conditions are precisely
\[
a_{23}=a_{32},\qquad
a_{31}=a_{13},\qquad
a_{12}=a_{21},
\]
so \(A\) is symmetric.

A vector \(a=(a_1,a_2,a_3)^T\ne0\) represents the plane
\[
P_a=\ker(a_1e_1^*+a_2e_2^*+a_3e_3^*).
\]
A generator of \(\Lambda^2P_a\) is proportional to
\[
a_1e_2\wedge e_3+a_2e_3\wedge e_1+a_3e_1\wedge e_2,
\]
so \(P_a\) is a Lie subalgebra exactly when
\[
\boxed{a^TAa=0.}
\]

If \(q\) is odd, \(A\) is a nonsingular symmetric matrix, so this equation is a
nonsingular projective conic. A nonsingular conic over a finite field has
exactly \(q+1\) rational points. Hence \(t(L)=q+1\).

If \(q\) is even, write \(a_{ii}=b_i^2\), possible because finite fields are
perfect. Symmetry gives
\[
a^TAa=(b_1a_1+b_2a_2+b_3a_3)^2.
\]
The linear form on the right is nonzero: otherwise \(A\) would have zero
diagonal, and a symmetric \(3\times3\) zero-diagonal matrix in characteristic
two has determinant zero. Thus the Lie-subalgebra planes are exactly the
projective points on one projective line, again \(q+1\) of them.

This completes the classification.

## Two consequences for the recent examples

Muhie--Otera--Russo computed equal subalgebra commutativity degrees for the
three-dimensional Heisenberg algebra and, for odd \(q\),
\(\mathfrak{sl}_2(\mathbb F_q)\), despite their being nonisomorphic. They also
found equal factorization numbers. The formulas above show that both
coincidences are forced by the same elementary invariant:
\[
t(\mathfrak h_3)=t(\mathfrak{sl}_2)=q+1.
\]
Indeed, every perfect three-dimensional Lie algebra over a finite field has the
same value \(D_1(q)\), while every solvable algebra with a unique projective
eigenline has that value as well.

For the comaximal graph \(\Gamma(L)\) of Towers--Zuleta--Gutierrez, let
\(E_{11}\) denote the number of graph edges joining two line subalgebras.
A pair of distinct lines is nonpermutable exactly when it is such an edge, so
\[
\boxed{
E_{11}=\frac{q(q+1)(N-t(L))}2,
\qquad
1-\operatorname{sd}(L)
=
\frac{2E_{11}}{|\mathcal L(L)|^2}.
}
\]
Thus in dimension three the deficit of the subalgebra commutativity degree is
exactly the normalized line--line part of the comaximal graph.

The four possible factorization numbers are correspondingly
\[
\begin{array}{c|c}
t(L)&F_2(L)\\ \hline
1&4q^2+2q+7\\
q+1&2q^3+5q^2+5q+7\\
2q+1&4q^3+8q^2+8q+7\\
q^2+q+1&3q^4+4q^3+8q^2+5q+7.
\end{array}
\]

## Context and limitations

Muhie, Otera and Russo introduced the subalgebra commutativity degree in
arXiv:2609.19086v1 (16 September 2026), obtained general bounds, computed the
three-dimensional Heisenberg case over prime fields and the
\(\mathfrak{sl}_2(\mathbb F_q)\) case for odd \(q\), and observed the equality
of both the degree and the factorization number in those two examples. Their
results, including the fact that abelian and almost-abelian Lie algebras have
degree one, are prior work.

Towers, Zuleta and Gutierrez introduced the comaximal graph in
arXiv:2605.09583 and classified it for Lie algebras of dimension at most three
over finite fields. In the solvable derived-dimension-two case they already
obtained the plane counts
\[
1,\quad 1+q,\quad 1+2q,\quad 1+q+q^2
\]
according to the eigenline type of the adjoint action. Those plane counts and
their graph classification are also prior work.

The novelty claim here is restricted to the universal three-dimensional
formula expressing \(\operatorname{sd}(L)\) and \(F_2(L)\) through the plane
count, the resulting equivalence with lattice cardinality, the complete
four-value classification of the new invariant over every finite field, the
projective-eigenline mechanism in the solvable case, and the
classification-free proof that every perfect three-dimensional algebra has
\(q+1\) Lie-subalgebra planes. The comaximal-graph edge identity is an immediate
bridge between these two recent invariants.

Originality is to the best of our knowledge. The modular-pairs paper is a very
recent v1 and may be revised. The perfect-case classification appearing in the
comaximal-graph paper is not used here; the perfect-case argument above is
self-contained. No claim is made about dimensions greater than three.

## References

1. S. K. Muhie, D. E. Otera and F. G. Russo, *On the number of modular pairs
   in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1
   (2026), https://arxiv.org/abs/2609.19086.
2. D. A. Towers, Y. Zuleta and I. Gutierrez, *The comaximal graph of a
   finite-dimensional Lie algebra*, arXiv:2605.09583 (2026),
   https://arxiv.org/abs/2605.09583.
3. D. A. Towers, Y. Zuleta and I. Gutierrez, *Comaximal Graphs of
   finite-dimensional Lie algebras over finite fields: Triangle counts and
   structural invariants*, arXiv:2608.16575 (2026),
   https://arxiv.org/abs/2608.16575.
