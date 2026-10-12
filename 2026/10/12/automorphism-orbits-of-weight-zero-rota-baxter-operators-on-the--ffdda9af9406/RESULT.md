# Automorphism orbits of weight-zero Rota–Baxter operators on the real Grassmann plane

## Finding
Let \(E=\Lambda_{\mathbb R}(\mathbb R^2)\) have basis \(1,x,y,z\), with
\[
xy=z,\qquad yx=-z,
\]
and with every other product among \(x,y,z\) equal to zero. A linear map \(R:E\to E\) is a weight-zero Rota–Baxter operator when
\[
R(a)R(b)=R\bigl(R(a)b+aR(b)\bigr)
\]
for all \(a,b\in E\).

Every such \(R\) satisfies \(R^2=0\) and \(\operatorname{rank}R\le 2\). Up to conjugation by \(\operatorname{Aut}(E)\), the nonzero rank-one operators are exactly the following six isolated classes, where basis images not displayed are zero:
\[
\begin{array}{lll}
S_1(1)=z, & S_2(x)=z, & S_3(1)=S_3(x)=z,\\
N_1(1)=x, & N_2(y)=x, & N_3(1)=N_3(y)=x.
\end{array}
\]
The rank-two operators are uniquely represented by
\[
A_t(1)=y,\qquad A_t(x)=t z,\qquad t\in\mathbb R^\times,
\]
\[
B_\sigma(1)=\sigma z,\qquad B_\sigma(x)=y,\qquad \sigma\in\{+1,-1\},
\]
and
\[
C_t(1)=y,\qquad C_t(x)=y+t z,\qquad t\in\mathbb R^\times,
\]
with the remaining basis images zero. Distinct displayed representatives are not conjugate. Thus the nonzero rank-two moduli set is two copies of \(\mathbb R^\times\) together with two isolated points, and the nonzero rank-one moduli set has six points.

## Assumptions and scope
The ground field is \(\mathbb R\). The algebra is the unital four-dimensional exterior algebra on a two-dimensional real vector space, viewed as an ordinary associative algebra. Equivalence means conjugacy \(R\mapsto\phi R\phi^{-1}\) by an algebra automorphism \(\phi\in\operatorname{Aut}(E)\). The zero operator is an additional singleton orbit and is omitted from the displayed nonzero list.

The real-field assumption matters. In the rank-two stratum represented by \(B_\sigma\), the sign of a nonzero scalar product is invariant because the stabilizer changes it by a positive square. Over a different field the corresponding square-class analysis can change.

## Proof
Write \(J=\operatorname{span}\{x,y,z\}\). Then \(J^2=\mathbb R z\), every element of \(J\) squares to zero, and for \(r,j\in J\) one has \(rj+jr=0\).

First, \(\operatorname{Im}R\subseteq J\). Indeed, \(\operatorname{Im}R\) is a subalgebra. If it contained \(w=\alpha 1+j\) with \(\alpha\ne0\), then \(w^2=2\alpha w-\alpha^2 1\) would imply \(1\in\operatorname{Im}R\). If \(R(a)=1\), the Rota–Baxter identity at \((a,a)\) gives \(1=R(2a)=2\), a contradiction in the real algebra.

For \(a=\alpha1+j\), put \(r=R(a)\in J\). The identity at \((a,a)\) becomes
\[
0=R(ra+ar)=2\alpha R^2(a).
\]
Taking \(a=1\) and then \(a=1+j\) shows \(R^2=0\). Hence \(\operatorname{Im}R\subseteq\ker R\), so \(\operatorname{rank}R\le2\).

Suppose first that \(\operatorname{rank}R=2\). Then \(W=\operatorname{Im}R=\ker R\) is a two-dimensional subalgebra of \(J\). Its image in \(J/J^2\) cannot be two-dimensional: two elements with independent degree-one parts have a nonzero product proportional to \(z\), which would force \(W\) to contain those two independent degree-one directions and \(z\), contradicting \(\dim W=2\). Therefore
\[
W=\operatorname{span}\{u,z\}
\]
for a nonzero degree-one element \(u\). Automorphisms act transitively on such planes, so normalize \(W=\operatorname{span}\{y,z\}\).

Relative to the quotient basis \((1,x)\) and the image basis \((y,z)\), the operator is an invertible matrix
\[
M=\begin{pmatrix}a&c\\ b&d\end{pmatrix}.
\]
The stabilizer of \(W\) consists of automorphisms of the form
\[
\phi(x)=s x+h y+\alpha z,\qquad
\phi(y)=u y+\beta z,\qquad
\phi(z)=su z,
\]
where \(s,u\ne0\). Conjugation sends
\[
(a,b,c,d)\longmapsto
\left(ua,\ \beta a+su b,\ \frac{u c}{s},\ \frac{\beta c}{s}+u d\right).
\]
There are exactly three disjoint cases.

If \(a\ne0\) and \(c=0\), the complete invariant is \(t=d/a\ne0\), and the orbit has representative \(A_t\). If \(a=0\) and \(c\ne0\), the complete invariant is \(\sigma=\operatorname{sign}(bc)\), because \(bc\) changes by the positive factor \(u^2\); the representative is \(B_\sigma\). If \(a\ne0\) and \(c\ne0\), the complete invariant is
\[
t=\frac{\det M}{a^2}\ne0,
\]
and the representative is \(C_t\). Direct choices of \(s,u,\beta\) reduce every invertible \(M\) to the stated representative, while the displayed invariants prove uniqueness.

Now suppose \(\operatorname{rank}R=1\). Write \(R(w)=f(w)v\) with nonzero \(f\in E^*\) and nonzero \(v\in J\). The Rota–Baxter identity is equivalent to
\[
f(a)f(vb)+f(b)f(av)=0
\]
for all \(a,b\). Choosing a point where \(f\ne0\) shows that \(f\circ L_v\) and \(f\circ R_v\) are scalar multiples of \(f\). Since \(L_v^2=R_v^2=0\), both scalars vanish. Thus rank-one operators are exactly those with
\[
f(vE+Ev)=0.
\]
If \(v\in J^2=\mathbb Rz\), normalize \(v=z\). Then the condition is \(f(z)=0\), and the automorphism action has exactly three orbits according as \(f(1)\) and the restriction of \(f\) to \(\operatorname{span}\{x,y\}\) are zero or nonzero, giving \(S_1,S_2,S_3\). If \(v\notin J^2\), normalize the image line to \(\mathbb Rx\). Then \(f(x)=f(z)=0\), and the line stabilizer has exactly three orbits according as \(f(1)\) and \(f(y)\) are zero or nonzero, giving \(N_1,N_2,N_3\). The two triples cannot mix because \(J^2\) is characteristic.

## Verification
The accompanying exact symbolic checker works directly from the multiplication table. It verifies the Rota–Baxter identity on all ordered basis pairs for all six rank-one representatives and the three symbolic rank-two strata; verifies the general automorphism formula and its determinant; derives the rank-two stabilizer conjugation formula; and checks the three stated invariants symbolically. Its terminal output is `CHECK_OK`.

The computation is a consistency check. Completeness of the infinite real classification is supplied by the proof above rather than by finite enumeration.

## Relationship to prior work
The 2026 paper *The Classification of the Rota-Baxter Operators on Four-dimensional Grassmann Algebra* (arXiv:2609.07377, first public 2026-09-07) gives a raw matrix classification of weight-zero operators over the real four-dimensional Grassmann algebra. The inspected text does not quotient that list by algebra automorphisms.

An earlier paper, *Rota-Baxter Operators on Quadratic Algebras* (arXiv:1801.07037), proves a strong partial normal form for this same algebra: up to automorphism, a weight-zero operator may be arranged so that \(R(1)\) and \(R(e_1)\) lie in \(\operatorname{span}\{e_2,e_1\wedge e_2\}\), while \(R(e_2)=R(e_1\wedge e_2)=0\). That result supplies a normal slice but does not identify when two points of the slice are conjugate. The present classification determines the quotient of that slice exactly, including the two continuous real invariants and the discrete sign stratum.

A published finite-field computation over \(\mathbb F_2\) gives twelve conjugacy classes for the same four-dimensional exterior algebra in characteristic two. That result is not comparable by specialization to the real classification because the multiplication signs and square-class behavior change in characteristic two.

## Limitations
The theorem is only for weight zero and for the real four-dimensional exterior algebra. It does not claim an orbit classification over arbitrary fields, where the \(B\)-stratum is governed by square classes rather than real sign alone. It also does not classify the induced dendriform or pre-Lie structures up to their own possibly coarser isomorphism relations.

The strongest prior overlap is the 2018 automorphism normal slice. The originality claim is specifically the complete and unique orbit reduction of that slice. A residual literature risk is that an unindexed source may have carried that reduction further; the inspected primary sources and targeted published-result searches did not reveal one.

## References
1. *The Classification of the Rota-Baxter Operators on Four-dimensional Grassmann Algebra*, arXiv:2609.07377, first version 2026-09-07.
2. *Rota-Baxter Operators on Quadratic Algebras*, arXiv:1801.07037.
