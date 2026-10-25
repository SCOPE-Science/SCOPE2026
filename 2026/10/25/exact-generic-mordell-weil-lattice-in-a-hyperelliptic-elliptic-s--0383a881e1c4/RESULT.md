# Exact generic Mordell–Weil lattice in a hyperelliptic elliptic-surface family

## Finding
Let \(g\geq 2\), put \(d=2g+1\), and let \(c_0,\ldots,c_{d-1}\) be algebraically independent over \(\mathbb C\). Write
\[
F=\mathbb C(c_0,\ldots,c_{d-1}),\qquad
B/F:\quad w^2=t^d+\sum_{j=0}^{d-1}c_jt^j.
\]
Let \(E\) be the generic elliptic fiber
\[
E:\quad y^2=x^3+(t^2+1)x+1
\]
over \(F(B)\). Then the full Mordell–Weil group \(E(F(B))\) is torsion-free of rank \(4\). Its canonical height lattice is \(D_4^*(2)\), the dual \(D_4\)-lattice with pairing multiplied by \(2\).

Let \(r_1,r_2,r_3\) be the roots in \(\mathbb C\) of \(r^3+r+1=0\), and choose one square root \(s_i\in\mathbb C\) of each \(r_i\). The four explicit sections
\[
P_0=(0,1),\qquad P_i=(r_i,s_it)\quad (1\leq i\leq3)
\]
have canonical height Gram matrix \(2I_4\) over \(B\). They generate an index-two subgroup of \(E(F(B))\). Their rank-four subgroup persists for **every** complex hyperelliptic specialization with distinct branch points avoiding \(t=0\) and the roots of \(4(t^2+1)^3+27\). The full Mordell–Weil rank of a special complex fiber may exceed four; only the stated generic coefficient-field rank is asserted exactly.

## Assumptions and scope
All fields are of characteristic zero. The complete generic coefficient field is \(F\), rather than an arbitrary algebraically closed field after fixing the coefficients. The curve \(B\) has genus \(g\): its defining polynomial has odd degree \(2g+1\), is separable at the generic point, and its unique point above infinity has \(\operatorname{ord}_\infty(t)=-2\). The elliptic surface over \(B\) is the relatively minimal Jacobian elliptic model with fundamental line bundle \(\mathcal O_B(\infty)\), whose degree is one. The arbitrary complex specializations have \(2g+1\) finite branch points distinct from one another and from zero and all six discriminant roots. No assertion is made about reductions in positive characteristic or specialized rank equality.

The dual \(D_4\)-lattice can be represented as
\[
D_4^*=\mathbb Z^4+\mathbb Z\bigl(\tfrac12,\tfrac12,\tfrac12,\tfrac12\bigr)
\]
with the ordinary Euclidean inner product. The notation \(D_4^*(2)\) means that every inner product is doubled. A height lattice is specified after factoring out torsion; here torsion is absent.

## Proof
**1. The rational elliptic source.** Over \(\mathbb C(t)\), first consider \(E_0:y^2=x^3+(t^2+1)x+1\) and its relatively minimal Weierstrass surface \(S\to\mathbb P^1\) with fundamental line bundle \(\mathcal O_{\mathbb P^1}(1)\). The polynomial
\[
D(t)=4(t^2+1)^3+27=4t^6+12t^4+12t^2+31
\]
has six simple roots: its derivative is \(24t(t^2+1)^2\), whereas \(D(0)=31\) and \(D(t)=27\) when \(t^2+1=0\). Hence there are six finite \(I_1\)-fibers. At infinity put \(u=1/t\), \(X=u^2x\), \(Y=u^3y\). The local coefficients are \(a_4=u^2+u^4\), \(a_6=u^6\), and \(\operatorname{ord}_u(\Delta)=6\). The residual cubic is \(T^3+T\), with three distinct roots, so Tate's algorithm yields one split \(I_0^*\)-fiber. The data are minimal. Thus \(\chi(\mathcal O_S)=1\), the canonical bundle formula gives \(K_S=-F_S\) for a fiber \(F_S\), and \(S\) is a rational elliptic surface. Its Néron–Severi group is unimodular of rank \(10\).

The unique reducible fiber contributes root lattice \(D_4\) of rank four. Shioda–Tate gives
\[
\operatorname{rank}E_0(\mathbb C(t))=10-2-4=4.
\]
Moreover, for any nonzero section \(Q\), the self-height formula and the \(I_0^*\) correction bound give
\[
\langle Q,Q\rangle=2+2(Q\cdot O)-\operatorname{contr}_\infty(Q)\geq1,
\]
since a section can meet only a multiplicity-one component and the correction is \(0\) or \(1\). Thus there is no nonzero torsion. Alternatively, Oguiso–Shioda's rational-elliptic lattice classification assigns exactly \(D_4^*\), without torsion, to the single \(D_4\)-fiber configuration (their Main Theorem, row 9). This proves the source height-lattice classification. The lattice determinant is \(1/4\).

**2. Four explicit orthogonal sections on every admissible cover.** The cubic \(r^3+r+1\) has discriminant \(-31\), so the \(r_i\) are distinct and nonzero. Substitution into the equation of \(E_0\) gives
\[
(s_it)^2=r_it^2=r_i^3+(t^2+1)r_i+1;
\]
so all \(P_i\), along with \(P_0\), are rational sections. For every admissible \(B\), its minimal elliptic surface \(X\to B\) has exactly twelve \(I_1\)-fibers and no reducible ones, with \(\chi(\mathcal O_X)=1\) (the discriminant has twelve distinct zeros and the line bundle has degree one).

Write \(v\) for a formal uniformizer at the unique point of \(B\) at infinity, chosen so \(t=v^{-2}\). In the smooth local Weierstrass chart \(X'=v^2x\), \(Y'=v^3y\), the equation becomes
\[
Y'^2=X'^3+(1+v^4)X'+v^6.
\]
The special point \((X',Y',v)=(0,0,0)\) is smooth, and \((v,Y')\) form regular local coordinates there because the partial derivative of the equation with respect to \(X'\) is a unit. At this point the four sections are
\[
P_0:(X',Y')=(0,v^3),\qquad
P_i:(X',Y')=(r_iv^2,s_iv).
\]
Their \(Y'\)-slopes are \(0,s_1,s_2,s_3\), pairwise distinct. Every pair therefore intersects transversely exactly once at infinity, with no other intersections because their affine \(x\)-coordinates are pairwise distinct. The sections are all disjoint from the zero section \(O\). Consequently, the explicit Shioda height formula, with no reducible fibers, yields
\[
\langle P_i,P_i\rangle=2,\qquad
\langle P_i,P_j\rangle=1-(P_i\cdot P_j)=0\quad(i\ne j).
\]
The four sections are independent. Their height matrix is \(2I_4\) for every admissible complex specialization.

**3. Exact index on the rational source.** Canonical heights scale by the degree of a finite base change. The displayed degree-two cover therefore shows that the four points in \(E_0(\mathbb C(t))\) have Gram matrix \(I_4\). This sublattice has determinant \(1\). Since the entire source lattice \(D_4^*\) has determinant \(1/4\), its index is \(\sqrt{1/(1/4)}=2\). It follows that these four sections generate the standard coordinate sublattice of index two in \(D_4^*\).

**4. Generic base change creates no extra rational sections.** The field \(F(B)\) has the presentation
\[
F(B)=\mathbb C(c_0,\ldots,c_{d-1},t,w)\big/
\bigl(w^2-t^d-\sum_{j=0}^{d-1}c_jt^j\bigr).
\]
Eliminating the unrestricted parameter \(c_0\) gives the field isomorphism
\[
F(B)\cong\mathbb C(t)(c_1,\ldots,c_{d-1},w),\qquad
c_0=w^2-t^d-\sum_{j=1}^{d-1}c_jt^j.
\]
The right side is **purely transcendental** over \(\mathbb C(t)\). An elliptic curve has no nonconstant rational map from \(\mathbb P^1\), even after arbitrary field extension in characteristic zero. Applied successively to the transcendental variables, this implies
\[
E_0\bigl(\mathbb C(t)(c_1,\ldots,c_{d-1},w)\bigr)
=E_0(\mathbb C(t)).
\]
Thus \(E(F(B))=E_0(\mathbb C(t))\), including all torsion and all rational points. Under degree-two base change its height pairing doubles. The exact full generic height lattice is therefore \(D_4^*(2)\), and the explicit four sections have index two as claimed.

## Verification
Run \(\texttt{python3 artifacts/verify.py}\) in a standard Python 3 environment. The independent-from-external-packages exact arithmetic checker validates the discriminant polynomial and its critical values, separability of the auxiliary cubic, the two point identities, and the elementary lattice rank/index arithmetic. It prints \(\texttt{VERIFY\_OK}\). The classification and no-new-points argument are deductive proofs above, **not** inferred from finite computation. The smooth local chart, intersection multiplicities, Shioda–Tate hypotheses, and purely transcendental field identification are stated explicitly to make the non-computational steps checkable.

## Relationship to prior work
Li–Liu (first posted 27 May 2026) introduce the elliptic surface over arbitrary genus-\(g\) hyperelliptic bases, prove twelve \(I_1\)-fibers and \(\chi=1\), and exhibit \(P_0=(0,1)\) as a non-torsion section. Their article does **not** assert a complete Mordell–Weil lattice or four independent sections. The rational-source classification \(D_4^*\) follows already from the Oguiso–Shioda table and is acknowledged here as classical, not new. The added result is the explicit index-two rank-four subsystem on the high-genus surfaces, together with the **exact full Mordell–Weil lattice over the universal generic hyperelliptic coefficient field**, established by the coefficient-elimination argument. The combination is an invariant of the proposed higher-genus family, not a new general Shioda–Tate theorem.

## Limitations
The equality of full Mordell–Weil groups is over the **generic coefficient field** \(F(B)\), not over the function field of every fixed complex cover. Special members can have additional sections. No assertion is made that the rank equals four over the geometric generic fiber after extending the coefficient field to an algebraic closure. The four-section lower bound and height matrix do hold on every admissible complex member. Lattice classification uses established elliptic-surface theorems; the supplied program does not independently certify them. The rational-source lattice is covered by preexisting work. An unindexed derivation of this precise hyperelliptic generic-field consequence is an originality risk.

## References
1. S. Li and J. Liu, *Examples of infinitely many \((-1)\)-curves with higher genus on elliptic surfaces*, arXiv:2605.27926v1 (27 May 2026), with updated exposition v2 (26 Aug 2026), https://arxiv.org/html/2605.27926v2.
2. K. Oguiso and T. Shioda, *The Mordell–Weil lattice of a rational elliptic surface*, Comment. Math. Univ. St. Paul **40** (1991), 83–99, DOI:10.14992/00009974; in particular Main Theorem row 9 and Section 3.
3. T. Shioda, *On the Mordell–Weil lattices*, Comment. Math. Univ. St. Paul **39** (1990), 211–240, DOI:10.14992/00009994.
4. M. Schütt and T. Shioda, *Mordell–Weil Lattices*, Springer (2019), standard height and base-change formulas as cited by Li–Liu.
