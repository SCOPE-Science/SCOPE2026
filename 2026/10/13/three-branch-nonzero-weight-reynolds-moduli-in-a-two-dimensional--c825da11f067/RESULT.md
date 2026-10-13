# Three-branch nonzero-weight Reynolds moduli in a two-dimensional Lie–Yamaguti algebra

## Finding

Let \(K\) be a field and let \(L_K\) be the two-dimensional Lie–Yamaguti algebra with basis
\[
\{e_1,e_2\},
\]
binary bracket
\[
[e_1,e_2]=e_1,
\]
and ternary bracket
\[
\{e_1,e_2,e_2\}=e_1,
\]
with the usual skewness in the first two ternary slots.

Fix a nonzero weight
\[
\mu\in K^\times.
\]
A Reynolds operator of weight \(\mu\) is a linear map \(R:L_K\to L_K\) satisfying
\[
[Rx,Ry]
=
R\!\left([Rx,y]+[x,Ry]+\mu[Rx,Ry]\right)
\]
and
\[
\{Rx,Ry,Rz\}
=
R\!\left(
\{x,Ry,Rz\}
+\{Rx,y,Rz\}
+\{Rx,Ry,z\}
+2\mu\{Rx,Ry,Rz\}
\right).
\]

Write
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}.
\]
Then the complete Reynolds system is equivalent to just
\[
\boxed{
a^2+bc+\mu a(ad-bc)=0,
}
\]
and
\[
\boxed{
c\bigl(a+d+\mu(ad-bc)\bigr)=0.
}
\]

Consequently,
\[
\boxed{
\operatorname{Rey}_\mu(L_K)
=
\mathcal A\cup\mathcal B_\mu\cup\mathcal N,
}
\]
where
\[
\boxed{
\mathcal A=
\left\{
\begin{pmatrix}
0&b\\
0&d
\end{pmatrix}
:b,d\in K
\right\},
}
\]
\[
\boxed{
\mathcal B_\mu=
\left\{
\begin{pmatrix}
a&b\\
0&-\mu^{-1}
\end{pmatrix}
:a,b\in K
\right\},
}
\]
and
\[
\boxed{
\mathcal N=
\{R\in M_2(K):R^2=0\}.
}
\]

The intersections are
\[
\boxed{
\mathcal A\cap\mathcal B_\mu
=
\left\{
\begin{pmatrix}
0&b\\
0&-\mu^{-1}
\end{pmatrix}
:b\in K
\right\},
}
\]
\[
\boxed{
\mathcal A\cap\mathcal N
=
\left\{
\begin{pmatrix}
0&b\\
0&0
\end{pmatrix}
:b\in K
\right\},
}
\]
and
\[
\boxed{
\mathcal B_\mu\cap\mathcal N=\varnothing.
}
\]

Teng and Guo's Example 3.10 displays
\[
\begin{pmatrix}
k_1&k_2\\
0&k
\end{pmatrix}
\]
at weight
\[
-\frac1k.
\]
For \(\mu=-1/k\), this is exactly the whole branch \(\mathcal B_\mu\). The complete moduli space therefore has two additional branches: the plane \(\mathcal A\) and the square-zero cone \(\mathcal N\).

For every finite field \(\mathbf F_q\) and every fixed
\[
\mu\in\mathbf F_q^\times,
\]
the number of Reynolds operators is
\[
\boxed{
|\operatorname{Rey}_\mu(L_{\mathbf F_q})|
=
3q^2-2q.
}
\]

Their rank distribution is
\[
\boxed{
\#\{\operatorname{rank}R=0\}=1,
}
\]
\[
\boxed{
\#\{\operatorname{rank}R=1\}
=
2q^2-q-1,
}
\]
and
\[
\boxed{
\#\{\operatorname{rank}R=2\}
=
q(q-1).
}
\]

Thus nonzero Reynolds weight produces exactly
\[
q(q-1)
\]
invertible operators. They are precisely the matrices in \(\mathcal B_\mu\) with
\[
a\ne0.
\]

The full Lie–Yamaguti automorphism group is
\[
\boxed{
\operatorname{Aut}(L_K)
=
\left\{
\begin{pmatrix}
s&t\\
0&1
\end{pmatrix}
:
s\in K^\times,\ t\in K
\right\}.
}
\]

For every finite field \(\mathbf F_q\), the Reynolds operators of a fixed nonzero weight form exactly
\[
\boxed{2q+2}
\]
automorphism-conjugacy classes.

A structural orbit-size description is:
\[
\boxed{
2\text{ singleton orbits},
}
\]
\[
\boxed{
2\text{ orbits of size }q-1,
}
\]
\[
\boxed{
2q-3\text{ orbits of size }q,
}
\]
and
\[
\boxed{
1\text{ orbit of size }q(q-1).
}
\]
When \(q=2\), some of these numerical sizes coincide; the displayed list records the structural orbit families.

Over every extension field,
\[
|\operatorname{Rey}_\mu(L_{\mathbf F_q})(\mathbf F_{q^m})|
=
3q^{2m}-2q^m,
\]
so the fixed-weight Hasse–Weil zeta function is
\[
\boxed{
Z(T)
=
\frac{(1-qT)^2}{(1-q^2T)^3}.
}
\]

## Assumptions and scope

Teng and Guo introduce Reynolds operators of arbitrary weight on Lie–Yamaguti algebras. Their Definition 3.1 is the definition used above. Their Example 2.5 is exactly the two-dimensional algebra treated here, and Example 3.10 supplies the branch \(\mathcal B_\mu\) for nonzero weight.

The source works over an algebraically closed field of characteristic \(0\). The classification above is proved directly from polynomial identities and is valid over an arbitrary field.

The theorem is restricted to
\[
\mu\ne0.
\]
Weight \(0\) is the Rota–Baxter case and is not part of the accepted claim here.

No quotient is taken until the separate automorphism-conjugacy statement.

## Proof

The ternary bracket is induced from the binary Lie bracket:
\[
\{x,y,z\}=[[x,y],z].
\]
Indeed,
\[
[[e_1,e_2],e_2]=[e_1,e_2]=e_1.
\]

Teng and Guo's Example 3.7 records that a Reynolds operator of weight \(\mu\) on a Lie algebra is automatically a Reynolds operator of the same weight on the associated Lie–Yamaguti algebra obtained from
\[
\{x,y,z\}=[[x,y],z].
\]
Therefore it is enough to solve the binary Reynolds identity.

For
\[
R(e_1)=ae_1+ce_2,
\qquad
R(e_2)=be_1+de_2,
\]
the only nontrivial ordered basis pair is \((e_1,e_2)\). Direct substitution gives
\[
a^2+bc+\mu a(ad-bc)=0
\]
and
\[
c\bigl(a+d+\mu(ad-bc)\bigr)=0.
\]

Suppose first that
\[
c=0.
\]
The first equation becomes
\[
a^2(1+\mu d)=0.
\]
Since \(K\) is a field,
\[
a=0
\]
or
\[
d=-\mu^{-1}.
\]
These are exactly the planes
\[
\mathcal A
\]
and
\[
\mathcal B_\mu.
\]

Now suppose
\[
c\ne0.
\]
Put
\[
\Delta=ad-bc.
\]
The second equation gives
\[
\mu\Delta=-(a+d).
\]
Substituting this into the first equation yields
\[
0
=
a^2+bc-a(a+d)
=
bc-ad
=
-\Delta.
\]
Hence
\[
\Delta=0
\]
and
\[
a+d=0.
\]

By Cayley–Hamilton, a \(2\times2\) matrix with trace and determinant both zero satisfies
\[
R^2=0.
\]
Conversely, every square-zero matrix has trace and determinant zero, and substitution into the two equations shows that it is a Reynolds operator. This gives \(\mathcal N\), including the square-zero matrices with \(c=0\).

The three intersection formulas follow immediately. In particular, a matrix in \(\mathcal B_\mu\) has
\[
d=-\mu^{-1}\ne0.
\]
If it were square-zero, its determinant would force \(a=0\), but then its trace would be nonzero. Hence
\[
\mathcal B_\mu\cap\mathcal N=\varnothing.
\]

Over \(\mathbf F_q\), both affine planes have \(q^2\) points. The square-zero cone in \(M_2(\mathbf F_q)\) has \(q^2\) points: besides zero, its nonzero elements are exactly the rank-one nilpotent matrices, and there are \(q^2-1\) of them.

The two nonempty intersections have \(q\) points each. Therefore
\[
q^2+q^2+q^2-q-q
=
3q^2-2q.
\]

Every nonzero element of \(\mathcal A\) has rank \(1\), and every nonzero element of \(\mathcal N\) has rank \(1\). A matrix in \(\mathcal B_\mu\) has determinant
\[
-\frac{a}{\mu},
\]
so it is invertible exactly when
\[
a\ne0.
\]
There are
\[
q(q-1)
\]
such matrices. Subtracting from the total gives the stated rank-one count.

For automorphisms, write
\[
P=
\begin{pmatrix}
p&u\\
r&s
\end{pmatrix}.
\]
Preservation of
\[
[e_1,e_2]=e_1
\]
gives
\[
r=0,
\qquad
p(s-1)=0.
\]
Invertibility forces
\[
p\ne0,
\]
so
\[
s=1.
\]
These maps also preserve the induced ternary bracket, proving the automorphism formula.

For
\[
P=
\begin{pmatrix}
s&t\\
0&1
\end{pmatrix},
\]
conjugation is
\[
P
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
P^{-1}
=
\begin{pmatrix}
a+\dfrac{ct}{s}
&
-a t+bs-\dfrac{ct^2}{s}+dt
\\
\dfrac cs
&
d-\dfrac{ct}{s}
\end{pmatrix},
\]
with upper-right entry more explicitly
\[
-a t+bs-\frac{ct^2}{s}+dt.
\]

On \(\mathcal A\), the parameter \(d\) is invariant. At \(d=0\), zero is fixed and all nonzero \(b\) form one orbit of size \(q-1\). For each
\[
d\ne0,
\]
all \(b\) form one orbit of size \(q\). Thus \(\mathcal A\) contributes \(q+1\) orbits.

The set
\[
\mathcal N\setminus\mathcal A
\]
is a single orbit: \(c\ne0\), scaling normalizes \(c\), and a shear kills the diagonal entry. Its size is
\[
q(q-1).
\]

On \(\mathcal B_\mu\), write
\[
\delta=-\mu^{-1}.
\]
Then \(a\) is invariant and
\[
b\longmapsto bs+(\delta-a)t.
\]
The case \(a=0\) is exactly the already-counted intersection with \(\mathcal A\). For
\[
a\ne0,\qquad a\ne\delta,
\]
there is one orbit of size \(q\) for each \(a\), giving \(q-2\) new \(q\)-orbits. At
\[
a=\delta,
\]
the scalar matrix
\[
\delta I
\]
is fixed, while the matrices with \(b\ne0\) form one orbit of size \(q-1\).

Adding the structural orbit families gives
\[
(q+1)+1+q
=
2q+2
\]
orbits and the stated size distribution.

Finally, the same point count holds over every extension field with \(q\) replaced by \(q^m\), which gives the zeta function.

## Verification

The included program `artifacts/verify.py` reconstructs both Reynolds identities from the binary and ternary products.

It verifies symbolically that the binary Reynolds defect reduces to
\[
a^2+bc+\mu a(ad-bc)
\]
and
\[
c\bigl(a+d+\mu(ad-bc)\bigr).
\]

It also checks directly that the ternary Reynolds identity is automatic for every operator satisfying the binary Reynolds identity on this induced Lie–Yamaguti algebra.

The program exhaustively enumerates every \(2\times2\) matrix for every nonzero weight over
\[
\mathbf F_2,\quad
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7.
\]

For a fixed nonzero weight, the operator counts are
\[
8,\quad21,\quad65,\quad133,
\]
matching
\[
3q^2-2q.
\]

The corresponding rank profiles are
\[
(1,5,2),\quad
(1,14,6),\quad
(1,44,20),\quad
(1,90,42).
\]

The automorphism-class counts are
\[
6,\quad8,\quad12,\quad16,
\]
matching
\[
2q+2.
\]

The checker verifies the structural orbit-size distribution, including the coincident sizes at
\[
q=2.
\]

It returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field classification is proved symbolically above.

## Relationship to prior work

Teng and Guo introduce arbitrary-weight Reynolds operators on Lie–Yamaguti algebras. Their Example 3.10 uses exactly this two-dimensional algebra and displays the full affine plane
\[
\mathcal B_\mu
\]
for nonzero weight, but it is presented as a family of examples rather than an exhaustive classification.

Das develops the general relationship between twisted Rota–Baxter operators and Reynolds operators on Lie algebras. The inspected full text contains no two-dimensional classification and no finite-field moduli or automorphism quotient for the affine Lie algebra underlying this example.

The weight-zero case is a Rota–Baxter problem and belongs to a different branch of the operator theory. The accepted theorem concerns only
\[
\mu\ne0,
\]
where the new affine plane \(\mathcal B_\mu\) contains all invertible solutions and the total fixed-weight moduli has three branches.

Targeted searches for the exact two-dimensional algebra, nonzero Reynolds weight, the square-zero branch, the polynomial
\[
3q^2-2q,
\]
and the automorphism count
\[
2q+2
\]
did not locate a covering result.

## Limitations

The theorem concerns one canonical two-dimensional Lie–Yamaguti algebra.

Only nonzero Reynolds weights are classified in the accepted claim.

The finite-field automorphism count is for conjugation by automorphisms of the fixed Lie–Yamaguti algebra.

A specialized low-dimensional Reynolds-operator classification may use Lie-algebra terminology and a different basis normalization. Failed searches do not prove novelty.

## References

1. W. Teng and S. Guo, “Cohomologies of Reynolds Lie-Yamaguti algebras of any weight and applications,” arXiv:2406.12859v1, first public 6 March 2024.
2. A. Das, “Twisted Rota-Baxter operators and Reynolds operators on Lie algebras and NS-Lie algebras,” arXiv:2009.09368v1, first public 20 September 2020.
3. J. Zhao and Y. Qiao, “Cohomologies and deformations of relative Rota-Baxter operators on Lie-Yamaguti algebras,” *Mathematics* 12 (2024), 166.
