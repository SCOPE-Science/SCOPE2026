# Order-\(p\) Acentralizer fibers in rank-two abelian \(p\)-groups

## Finding

Let
\[
G=C_{p^a}\oplus C_{p^b},
\qquad
1\le a<b,
\]
where \(p\) is any prime. Choose generators \(x,y\) of the two cyclic factors and define
\[
u=p^{a-1}x,
\qquad
v=p^{b-1}y.
\]
Then
\[
G[p]=\langle u,v\rangle\cong C_p^2.
\]
Its \(p+1\) order-\(p\) subgroups are
\[
U_\infty=\langle v\rangle
\]
and
\[
U_t=\langle u+t v\rangle,
\qquad
t\in\mathbf F_p.
\]

For a subgroup \(U\le G\), define the Acentralizer-fiber multiplicity
\[
m_G(U)
=
\left|
\left\{
\varphi\in\operatorname{Aut}(G):
\operatorname{Fix}(\varphi)=U
\right\}
\right|.
\]

Then every finite slope has the same multiplicity:
\[
\boxed{
m_G(U_t)
=
\begin{cases}
p^b(p-2),&a=1,\\[4pt]
p^{3a+b-4}(p-1)(p-2),&a\ge2,
\end{cases}
\qquad
t\in\mathbf F_p.
}
\]
The distinguished long-factor socle line has
\[
\boxed{
m_G(U_\infty)
=
p^{3a+b-3}(p-1)(p-2)
+
\mathbf 1_{b=a+1}\,
p^{4a-3}(p-1)^2.
}
\]

Thus for odd \(p\), every order-\(p\) subgroup is an Acentralizer, as expected from the existence theorem of Mozafar and Taeri, but the automorphism fibers are not uniform:
\[
m_G(U_\infty)>m_G(U_t).
\]
The characteristic subgroup \(U_\infty\), coming from the long cyclic factor, is distinguished quantitatively.

For \(p=2\),
\[
m_G(U_t)=0
\]
for every \(t\), while
\[
\boxed{
m_G(U_\infty)
=
\begin{cases}
2^{4a-3},&b=a+1,\\
0,&b\ge a+2.
\end{cases}
}
\]
Hence among order-\(2\) subgroups, only the long-factor socle line can occur as an exact automorphism fixed subgroup, and only for adjacent exponents.

For the classical case
\[
G=C_p\oplus C_{p^2},
\]
summing the \(p+1\) fibers gives
\[
m_G(U_\infty)+\sum_{t\in\mathbf F_p}m_G(U_t)
=
p(2p^3-4p^2+1),
\]
exactly the published value of
\[
\theta(G,p).
\]

## Assumptions and scope

An Acentralizer is the fixed subgroup
\[
\operatorname{Fix}(\varphi)
=
\{g\in G:\varphi(g)=g\}
\]
of an automorphism \(\varphi\).

The theorem refines existence by counting the entire automorphism fiber over each subgroup of order \(p\). It does not count fibers over arbitrary larger subgroups.

The formulas hold for every prime \(p\). The odd-prime case is the setting in which Mozafar--Taeri prove that every subgroup of a rank-two finite abelian \(p\)-group is an Acentralizer. Their even-prime theorem identifies missing Acentralizers; the formulas above sharpen the order-\(2\) slice by exact multiplicity.

## Proof

Every automorphism of
\[
G=C_{p^a}\oplus C_{p^b},
\qquad
a<b,
\]
has the form
\[
\varphi(x_0,y_0)
=
\left(
\alpha x_0+\beta y_0
\pmod {p^a},
\;
p^{b-a}c\,x_0+\delta y_0
\pmod {p^b}
\right),
\]
where
\[
\alpha\in(\mathbf Z/p^a\mathbf Z)^\times,
\quad
\beta,c\in\mathbf Z/p^a\mathbf Z,
\quad
\delta\in(\mathbf Z/p^b\mathbf Z)^\times.
\]
Write
\[
A=\alpha-1,
\qquad
D=\delta-1,
\qquad
g=b-a.
\]
Fixed points solve
\[
Ax_0+\beta y_0\equiv0\pmod {p^a},
\]
\[
p^g c\,x_0+D y_0\equiv0\pmod {p^b}.
\]

On the socle basis \(u,v\), the induced action is
\[
u\longmapsto \bar\alpha\,u+\bar c\,v,
\qquad
v\longmapsto \bar\delta\,v,
\]
where bars denote reduction modulo \(p\).

Suppose the fixed subgroup has order \(p\). Its socle is itself, so the fixed subspace of this lower-triangular \(2\times2\) action must be one-dimensional. There are three possible residue patterns.

First suppose
\[
\bar\alpha\ne1,
\qquad
\bar\delta=1.
\]
Then \(A\) is a unit modulo \(p^a\), so the first fixed-point equation determines
\[
x_0\equiv-A^{-1}\beta y_0\pmod {p^a}.
\]
The second equation becomes
\[
E y_0\equiv0\pmod {p^b},
\]
where
\[
E
=
D-p^g cA^{-1}\beta.
\]
The fixed subgroup has order \(p\) exactly when
\[
v_p(E)=1.
\]
For each fixed \(\alpha,\beta,c\), writing \(D=ps\), the residue of \(s\) modulo \(p\) must avoid exactly one value. Hence there are
\[
(p-1)p^{b-2}
\]
allowable \(\delta\). Since the numbers of choices for \(\alpha,\beta,c\) are
\[
p^{a-1}(p-2),\qquad p^a,\qquad p^a,
\]
this case contributes
\[
C_1
=
p^{3a+b-3}(p-1)(p-2).
\]
Its fixed socle line is always
\[
U_\infty.
\]

Second suppose
\[
\bar\alpha=1,
\qquad
\bar\delta\ne1.
\]
Now \(D\) is a unit modulo \(p^b\), so the second equation determines
\[
y_0\equiv-D^{-1}p^g c\,x_0\pmod {p^b}.
\]
The first equation becomes
\[
F x_0\equiv0\pmod {p^a},
\]
where
\[
F
=
A-\beta D^{-1}p^g c.
\]

If \(a=1\), then \(F\equiv0\pmod p\) automatically, so the kernel has exactly \(p\) elements. This case has
\[
C_2=p^{b+1}(p-2)
\]
automorphisms.

If \(a\ge2\), the kernel has order \(p\) exactly when
\[
v_p(F)=1.
\]
For fixed \(\beta,c,\delta\), among the
\[
p^{a-1}
\]
choices with \(\alpha\equiv1\pmod p\), exactly
\[
(p-1)p^{a-2}
\]
satisfy this valuation condition. Hence
\[
C_2
=
p^{3a+b-3}(p-1)(p-2)
\]
for \(a\ge2\).

The fixed socle line in this case is
\[
U_t,
\qquad
t=-\frac{\bar c}{\bar\delta-1}.
\]
For every fixed nonunit residue pattern except \(\bar c\), this relation is a bijection between the \(p\) values of \(\bar c\) and the \(p\) finite slopes \(t\). Therefore the \(C_2\) automorphisms are equally distributed among the \(p\) subgroups \(U_t\). This gives
\[
m_G(U_t)=\frac{C_2}{p}.
\]

Third suppose
\[
\bar\alpha=\bar\delta=1.
\]
If \(\bar c=0\), the socle fixed space has dimension \(2\), so the fixed subgroup has at least \(p^2\) elements. Thus exact order \(p\) requires
\[
\bar c\ne0.
\]
If also
\[
\bar\beta=0,
\]
then
\[
(\varphi-I)(G)\subseteq pG,
\]
so
\[
|\operatorname{Fix}(\varphi)|\ge p^2.
\]
Thus exact order \(p\) further requires
\[
\bar\beta\ne0.
\]

Assume now that both \(\beta\) and \(c\) are units modulo \(p\). The first fixed-point equation determines
\[
y_0\equiv-\beta^{-1}Ax_0\pmod {p^a}.
\]
Write
\[
y_0=-\beta^{-1}Ax_0+p^a t,
\qquad
t\in\mathbf Z/p^g\mathbf Z.
\]
Substitution in the second equation gives
\[
\left(
p^g c-D\beta^{-1}A
\right)x_0
+
Dp^a t
\equiv0
\pmod {p^{a+g}}.
\]

If \(g\ge2\), every coefficient in this last congruence is divisible by \(p^2\). The parameter space
\[
\mathbf Z/p^a\mathbf Z
\times
\mathbf Z/p^g\mathbf Z
\]
has \(p^{a+g}\) elements, while the possible values of the left side lie in a subgroup of size at most
\[
p^{a+g-2}.
\]
Hence the kernel has at least \(p^2\) elements. Exact order \(p\) is impossible.

If \(g=1\), then the term \(Dp^a t\) vanishes modulo \(p^{a+1}\), and the remaining congruence is
\[
pLx_0\equiv0\pmod {p^{a+1}},
\]
where
\[
L
=
c-\frac{D}{p}\beta^{-1}A.
\]
Since \(A\) is divisible by \(p\),
\[
L\equiv c\not\equiv0\pmod p.
\]
Thus \(L\) is a unit, so
\[
x_0=0
\]
and \(t\) is arbitrary modulo \(p\). The fixed subgroup is exactly
\[
U_\infty.
\]
The number of automorphisms in this case is
\[
C_3
=
p^{a-1}\cdot p^a
\cdot p^{a-1}(p-1)
\cdot p^{a-1}(p-1)
=
p^{4a-3}(p-1)^2.
\]

Combining the three cases gives
\[
m_G(U_\infty)=C_1+\mathbf 1_{b=a+1}C_3
\]
and
\[
m_G(U_t)=C_2/p,
\]
which are exactly the stated formulas.

## Verification

The included replay exhaustively enumerates every automorphism and every group element for
\[
(p,a,b)
=
(2,1,2),
(2,1,3),
(2,2,3),
(3,1,2),
(3,1,3),
(3,2,3),
(5,1,2).
\]
For each automorphism it computes the fixed subgroup directly and, when that subgroup has order \(p\), identifies whether it is \(U_\infty\) or one of the \(U_t\).

The observed fiber multiplicities are:

\[
(2,1,2):
\quad
m(U_\infty)=2,\quad m(U_t)=0;
\]

\[
(2,1,3):
\quad
m(U_\infty)=m(U_t)=0;
\]

\[
(2,2,3):
\quad
m(U_\infty)=32,\quad m(U_t)=0;
\]

\[
(3,1,2):
\quad
m(U_\infty)=30,\quad m(U_t)=9;
\]

\[
(3,1,3):
\quad
m(U_\infty)=54,\quad m(U_t)=27;
\]

\[
(3,2,3):
\quad
m(U_\infty)=2430,\quad m(U_t)=486;
\]

\[
(5,1,2):
\quad
m(U_\infty)=380,\quad m(U_t)=75.
\]

The replay also verifies, for
\[
G=C_p\oplus C_{p^2},
\]
that the sum over all \(p+1\) order-\(p\) subgroup fibers equals the published formula
\[
p(2p^3-4p^2+1).
\]

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the formulas.

## Relationship to prior work

Mozafar and Taeri prove that for odd \(p\), every subgroup of a finite rank-two abelian \(p\)-group occurs as the fixed subgroup of some automorphism. They also classify which subgroups fail to occur for \(p=2\). Their theorem is an existence classification: it does not count how many automorphisms have a prescribed fixed subgroup.

Hayat, López-Aguayo, and Abbas define
\[
\theta(G,d)
\]
as the number of automorphisms fixing exactly \(d\) elements. They compute all \(\theta\)-values for
\[
C_p\oplus C_{p^2},
\]
obtain the fixed-point-free count for
\[
C_{p^a}\oplus C_{p^b},
\qquad
a<b,
\]
and pose a broader \(\theta\)-value problem for finite abelian \(p\)-groups with distinct cyclic exponents.

The theorem here refines both viewpoints on the smallest nontrivial fixed-subgroup order. It does not merely count automorphisms with \(p\) fixed elements; it resolves the fiber over each individual order-\(p\) subgroup. The result detects the unique long-factor socle line and quantifies its excess multiplicity.

A published database result gives exact fixed-point-free automorphism counts for arbitrary finite abelian groups. That concerns the fiber over the trivial subgroup only and does not cover prescribed nontrivial fixed subgroups.

Targeted searches using Acentralizer multiplicity, prescribed fixed subgroup, rank-two abelian \(p\)-groups, and exact automorphism-fiber terminology did not locate these formulas.

## Limitations

Only fixed subgroups of order \(p\) are counted. Larger fixed subgroups require additional valuation strata.

The theorem is for rank-two abelian \(p\)-groups with unequal exponents
\[
a<b.
\]
The homocyclic case
\[
C_{p^a}\oplus C_{p^a}
\]
has a larger automorphism symmetry and a different subgroup-orbit structure.

The formulas distinguish the long-factor socle line from the other \(p\) order-\(p\) subgroups, but do not attempt a complete multiplicity classification of all Acentralizers.

Failed searches do not prove novelty.

## References

1. Z. Mozafar and B. Taeri, “Acentralizers of Abelian groups of rank 2,” *Hacettepe Journal of Mathematics and Statistics* 49 (2020), 273–281, DOI 10.15672/hujms.546988. Primary MSC 20D45.
2. U. Hayat, D. López-Aguayo, and A. Abbas, “Fixed Points of Automorphisms of Certain Non-Cyclic \(p\)-Groups and the Dihedral Group,” *Symmetry* 10 (2018), 238, DOI 10.3390/sym10070238.
