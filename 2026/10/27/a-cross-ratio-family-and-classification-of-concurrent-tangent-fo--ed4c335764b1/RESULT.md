# A cross-ratio family and classification of concurrent-tangent four-conic arrangements

## Finding
Over \(\mathbb C\), consider an **ordered** cycle \((C_1,C_2,C_3,C_4)\) of distinct smooth plane conics. Suppose consecutive conics \((C_1,C_2)\), \((C_2,C_3)\), \((C_3,C_4)\), \((C_4,C_1)\) have intersection multiplicity four at four distinct points, those points lie on one line \(L\), and the four common tangent lines pass through one point \(Q\notin L\). Then, up to projective equivalence preserving the order of the cycle, the arrangement has the following normal form, for a unique cross-ratio parameter \(t\in\mathbb C\setminus\{0,1\}\):

\[
\begin{aligned}
F_1&=y^2+(t-1)x(x-tz),\\
F_2&=y^2-t(t-1)xz,\\
F_3&=y^2-t(t-1)z(x-z),\\
F_4&=y^2+t(x-z)(x-tz).
\end{aligned}
\]

In the indicated normalization, the ordered contact points are \([0:0:1]\), \([1:0:0]\), \([1:0:1]\), \([t:0:1]\), and their tangent lines are the respective lines through \(Q=[0:1:0]\). For **every** admissible parameter \(t\), the reduced octic \(F_1F_2F_3F_4=0\) has exactly four \(A_7\) singularities and eight \(A_1\) singularities, with no triple intersections or other singular points. Its minimum Jacobian syzygy degree is exactly three and it is **nearly free**, with exponents \((3,5)\). Different cross-ratio parameters give different ordered projective configurations.

This classifies the entire geometrically specified family, not all four-conic arrangements with four \(A_7\) singularities. Its parameter is intrinsic: the ordered cross-ratio of the contact points on \(L\).

## Assumptions and scope
The base field is \(\mathbb C\). The conics are smooth and distinct; the contact points and the contact tangent lines are indexed by the four edges of an ordered cycle. The tangent concurrency point \(Q\) is assumed off the line \(L\) containing the contact points. Contact multiplicity four means local intersection multiplicity four between the corresponding two smooth conics. Parameter \(t=0\) or \(t=1\) is excluded, and the normal form is unique with the four chosen ordered contact points sent to \(0,\infty,1,t\) in this order. The assertion makes no claim about arrangements not obeying these incidence assumptions.

## Proof
**Coordinate normalization and classification.** A projective transformation sends \(L\) to \(y=0\) and \(Q\) to \([0:1:0]\). The four ordered points of \(L\cong\mathbb P^1\) can then be placed at \([x:z]=[0:1],[1:0],[1:1],[t:1]\), with \(t\notin\{0,1\}\). Each conic in the cycle is tangent, at its two adjacent contact points, to two distinct lines in the pencil through \(Q\). Hence the polar line of \(Q\) with respect to that conic is exactly \(L\). Smoothness and those two distinct tangencies imply \(Q\) is not on any conic. Each defining quadratic therefore has a nonzero coefficient of \(y^2\), zero coefficients of \(xy\) and \(yz\), and can be normalized uniquely as \(y^2+B_i(x,z)\).

For two consecutive conics, their difference \(B_i-B_{i+1}\) is a binary quadratic. Their common tangent at the assigned point is the relevant pencil line \(\ell\), and on either smooth conic \(\ell\) vanishes to order two. If \(B_i-B_{i+1}\) had only a simple root at that contact direction, the local conic intersection would have multiplicity two, contrary to the assumed four. Thus the difference is a nonzero multiple of \(\ell^2\). Consequently there are nonzero scalars \(a,b,c,d\) satisfying
\[
 B_1-B_2=ax^2,\quad B_2-B_3=bz^2,\quad
 B_3-B_4=c(x-z)^2,\quad B_4-B_1=d(x-tz)^2.
\]
Their sum vanishes identically, giving \(a=(t-1)d\), \(b=t(1-t)d\), \(c=-td\). Rescaling \(y\) relative to \((x,z)\), together with a common scalar normalization, sets \(d=1\). Imposing \(B_1(0,1)=B_2(1,0)=B_3(1,1)=B_4(t,1)=0\) then determines the four displayed \(B_i\) uniquely. Conversely these equations satisfy the incidence assumptions, so the parametrization is exhaustive.

**Complete singularity list.** Every \(B_i\) is a product of two distinct nonproportional linear forms for \(t\notin\{0,1\}\), hence \(y^2+B_i\) is a smooth conic. The four consecutive differences factor as
\[
\begin{split}
 B_1-B_2&=(t-1)x^2,\qquad B_2-B_3=-t(t-1)z^2,\\
 B_3-B_4&=-t(x-z)^2,\qquad B_4-B_1=(x-tz)^2.
\end{split}
\]
At each corresponding point the tangent pencil line meets either smooth conic with multiplicity two, so its square gives pairwise intersection multiplicity four; locally this is precisely the two-branch singularity \(A_7\). The remaining conics do not contain those points: direct substitution yields nonzero products of powers of \(t\) and \(t-1\). The opposite differences are
\[
 B_1-B_3=(t-1)(x^2-tz^2),\qquad
 B_2-B_4=-t(x^2-2xz+tz^2).
\]
For admissible \(t\), each has two simple roots on \(\mathbb P^1\). None is a zero of the corresponding \(B_i\): for example, after \(z=1\), the resultants of the opposite differences with \(B_1\) and \(B_3\) are respectively \(-t^2(t-1)^5\) and \(-t^2(t-1)^4\); for \(B_2,B_4\) they are \(-t^4(t-1)^2\) and \(t^5(t-1)^2\). Thus each root lifts to two points with \(y\ne0\), giving four transverse intersections for each opposite pair. These are all the intersections by Bézout; no triple intersection occurs. Therefore the singularity inventory is precisely four \(A_7\) points and eight nodes, and the total Tjurina number is \(4\cdot7+8=36\).

**An all-parameter cubic syzygy and near freeness.** Put \(f=\prod_{i=1}^4F_i\), and define the cubics
\[
\begin{aligned}
 A={}&-t(t-1)x^3+2t(t-1)(t+1)x^2z-2txy^2\\
    &-3t^2(t-1)xz^2+2ty^2z,\\
 C={}&3t(t-1)x^2z-2xy^2-2t(t-1)(t+1)xz^2\\
    &+2ty^2z+t^2(t-1)z^3.
\end{aligned}
\]
Direct polynomial expansion in \(\mathbb Z[t,x,y,z]\) establishes the identity \(A f_x+C f_z=0\); the triple \((A,0,C)\) is nonzero for each admissible \(t\). Thus \(\operatorname{mdr}(f)\le3\). The Dimca–Sernesi bound for a reduced curve with quasihomogeneous singularities gives \(\operatorname{mdr}(f)\ge \alpha\deg(f)-2\). Here \(\alpha=5/8\), the minimum local log-canonical threshold (attained at \(A_7\)), and \(\deg(f)=8\). Hence \(\operatorname{mdr}(f)\ge3\) and equality holds. Finally, the nearly-free numerical criterion for reduced plane curves with \(\operatorname{mdr}(f)\le\deg(f)/2\) applies because
\[
 (8-1)^2-3(8-3-1)=37=\tau(f)+1.
\]
It follows that every member is nearly free with exponents \((3,5)\).

The ordered cross-ratio of the four contact points is invariant under projective equivalences preserving the cycle ordering; hence the parameter is a genuine nonconstant moduli coordinate.

## Verification
The standalone `verify.py` requires Python 3 and SymPy. It expands and checks \(A f_x+C f_z=0\) **symbolically in the parameter** (not at finitely many parameter values), verifies all six pair-difference identities, checks four contact-point incidences and nonincidences, and computes the opposite-pair resultants. Run `python verify.py` from the directory containing the script. The expected final message begins `VERIFY_OK`. The geometric multiplicity, classification, and near-freeness claims additionally require the mathematical arguments above; a symbolic check alone does not establish them.

## Relationship to prior work
Piotr Pokora, *On free and nearly free arrangements of conics admitting certain ADE singularities* (arXiv:2303.08584, §2 Example 2.6), supplies a **single** nearly-free four-conic example described as having four collinear \(A_7\) points and eight nodes. It does not state the all-cross-ratio normal-form classification, the parameter-uniform cubic syzygy, or an all-parameter near-freeness result. The general minimal-syzygy bound and numerical criterion used here are established tools rather than new assertions. Marcin Zieliński, *On plane conic arrangements with A5 and A7 singularities* (DOI:10.1007/s12215-023-00890-8), provides numerical bounds and a three-conic example, not this four-conic incidence classification. The new contribution is the intrinsic moduli parametrization, complete incidence/singularity classification under explicit geometric hypotheses, and uniform freeness type—not the numerical existence of one example.

## Limitations
The result is conditional on four collinear contacts and one off-line common tangent-pencil center. It does not classify arbitrary four-conic arrangements with four \(A_7\) points and does not resolve the broader open problem of free four-conic arrangements. The criterion invoked is characteristic-zero and the statement is over \(\mathbb C\), not arbitrary characteristic. Literature overlap beyond the inspected original sources and relevant indexed records is possible. No independent audit or validation is asserted.

## References
- P. Pokora, *On free and nearly free arrangements of conics admitting certain ADE singularities*, arXiv:2303.08584 (initial public posting 15 March 2023), https://arxiv.org/abs/2303.08584 ; journal DOI:10.1007/s11565-023-00481-6, Example 2.6, Theorem 2.3, Definition 1.3.
- M. Zieliński, *On plane conic arrangements with A5 and A7 singularities*, DOI:10.1007/s12215-023-00890-8 (first published 17 May 2023), sections 1 and 4.
- Dimca–Sernesi minimal Jacobian syzygy bound, as precisely quoted in Pokora, Theorem 2.3.
- Dimca's nearly-free criterion, as quoted in Pokora, Definition 1.3, equation (2).
