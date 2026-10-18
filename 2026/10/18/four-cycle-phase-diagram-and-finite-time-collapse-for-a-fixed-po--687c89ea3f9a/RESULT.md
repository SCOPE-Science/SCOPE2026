# Four-cycle phase diagram and finite-time collapse for a fixed-point-free tent-seed map

## Finding
Let \(T(u)=2\min\{u,1-u\}\) on \([0,1]\), and consider the interval map
\[
F(x)=\begin{cases}
1-(1-a)T(x/p),&0\le x\le p,\\
bT((x-p)/(1-p)),&p<x\le1,
\end{cases}
\]
where the exact strict hypotheses throughout are \(0<b<p<a<1\). Define
\[
c=\frac{1-a}{1-p},\qquad d=\frac bp,\qquad K=4cd,
\]
so \(0<c,d<1\). The map has no fixed points, and every periodic orbit has even least period. Its complete primitive period-two census is as follows.

* If \(K<1\), the orbit \(0\leftrightarrow1\) is the only primitive two-cycle. Every orbit converges to it.
* If \(K=1\), there is an interval of primitive two-cycles parameterized without duplication by \(t\in[0,u]\), where \(u=\min\{1/2,1/(4c)\}\): each consists of \(pt\) and \(F(pt)\). In fact \(F^5=F^3\) on \([0,1]\); every orbit reaches a primitive two-cycle after at most three iterations.
* If \(K>1\) and \(c\le1/2\), there are exactly two primitive two-cycles, corresponding to \(t=0\) and \(t=K/(1+K)\).
* If \(K>1\) and \(c>1/2\), set
\[
B=1-\frac1{4c},\qquad A=\frac1{4(1-c)},\qquad B<A.
\]
Besides \(t=0\), the set of distinct normalized left coordinates \(t\in(0,1]\) is precisely the union of these conditional values:
\[
\begin{aligned}
t_L&=\frac{2d}{1+K}&&\text{if }d\le A,\\
t_M&=\frac{2d(2c-1)}{K-1}&&\text{if }B\le d\le A,\\
t_R&=\frac K{1+K}&&\text{if }d\ge B.
\end{aligned}
\]
At \(d=B\) the values \(t_M\) and \(t_R\) coincide; at \(d=A\) the values \(t_L\) and \(t_M\) coincide. Thus the total number of primitive two-cycles is \(2\) for \(d<B\), \(3\) for \(d=B\), \(4\) for \(B<d<A\), \(3\) for \(d=A\), and \(2\) for \(d>A\); empty parameter regimes are ignored because \(d<1\). All isolated period-two cycles when \(K>1\) are locally repelling, including those at turning points.

For example, \((p,a,b)=(1/2,3/5,9/20)\) gives \((c,d)=(4/5,9/10)\) and exactly four period-two cycles, with normalized left coordinates \(0,45/97,27/47,72/97\). At \((p,a,b)=(1/2,5/8,1/6)\), there are continuously many period-two cycles.

## Assumptions and scope
The domain includes both endpoints and uses the explicit branch assignment at \(x=p\). The strict inequalities \(0<b<p<a<1\) are essential: the left branch maps entirely into \((p,1]\), and the right branch maps entirely into \([0,p)\). The map is generally discontinuous at \(p\), so we do not use continuity-based fixed-point or global-bifurcation theorems. The proof classifies every least-period-two orbit throughout this strict three-parameter box, not longer cycles or invariant measures.

## Proof
First, for \(x\le p\), \(F(x)\ge a>p\), while for \(x>p\), \(F(x)\le b<p\). Hence all iterates alternate between the two sides, no fixed point exists, and any primitive two-cycle has exactly one point on each side. Writing that left point as \(x=pt\), we obtain
\[
\frac{F^2(pt)}p=\frac bp T\!\left(\frac{1-(1-a)T(t)-p}{1-p}\right)
=dT(1-cT(t))=dT(cT(t))=:H(t),
\]
using \(T(1-z)=T(z)\) for \(z\in[0,1]\). Thus primitive two-cycles correspond bijectively to fixed points of \(H\) on \([0,1]\), with no cyclic overcounting because exactly one point lies on the left.

For all \(t\ge0\), \(T(z)\le2z\) implies \(0\le H(t)\le4cdt=Kt\). If \(K<1\), the only fixed point is zero, and the iterates of \(H\) tend to zero geometrically. Therefore all orbits converge alternately to \(0\) and \(1\).

If \(K=1\), then for every \(0\le t\le u=\min\{1/2,1/(4c)\}\), both tent evaluations are on their increasing branches, so \(H(t)=Kt=t\). Conversely, when \(c\le1/2\), we have \(H(t)=T(t)/2\le1/2=u\) for all \(t\). When \(c>1/2\), \(H(t)\le d=1/(4c)=u\). Hence \(H([0,1])\subset[0,u]\) and \(H^2=H\) identically. A left starting state reaches a periodic pair after two \(F\)-steps; a right starting state reaches the left after one and requires at most two more. Consequently \(F^5=F^3\) globally, and no other period-two cycles exist beyond the displayed interval.

Assume \(K>1\). If \(c\le1/2\), then \(cT(t)\le1/2\) everywhere and \(H(t)=2cdT(t)\). Its two affine pieces are \(Kt\) for \(0\le t\le1/2\) and \(K(1-t)\) for \(1/2\le t\le1\). Their only fixed points are \(0\) and \(K/(1+K)\), respectively.

If \(c>1/2\), let \(r=1/(4c)\in(1/4,1/2)\). The five affine breakpoints are \(0,r,1/2,1-r,1\). On the four successive open pieces, \(H(t)\) equals
\[
Kt,\quad 2d-Kt,\quad 2d(1-2c)+Kt,\quad K(1-t).
\]
The corresponding fixed-point candidates are \(0,t_L,t_M,t_R\). Direct substitution into their respective closed piece intervals yields the exact admissibility conditions: \(t_L\in[r,1/2]\) iff \(1/(4c)\le d\le A\); \(t_M\in[1/2,1-r]\) iff \(B\le d\le A\); \(t_R\in[1-r,1]\) iff \(d\ge B\). The common condition \(K>1\) already ensures \(d>1/(4c)\). Also \(B<A\) because \((2c-1)^2>0\). At each threshold a pair of adjacent affine formulas meets at a breakpoint, so its shared root represents only one orbit. The census follows. All slopes of \(H\) away from its breakpoints have modulus \(K>1\); at a breakpoint both one-sided slopes also have modulus \(K\), hence all isolated fixed points are repelling in the relative topology and so are their two-cycles under \(F\).

## Verification
A standalone exact-rational script, `verify.py`, constructs \(H\) both directly and by affine-branch root extraction. It compares the closed-form classification with independent rational breakpoint enumeration for \(3481\) parameter pairs and all relevant equality thresholds. It also checks the two-step reduction and critical idempotence on several rational examples. It completed \(7006\) assertions/tests successfully using `python3 verify.py`. The claims for all real parameters and the global iteration identity are proved in the preceding algebra, not inferred from the finite tests.

## Relationship to prior work
Lawnik, Moysis, Baptista, and Volos (2024) introduced the fixed-point-free family, examining logistic and tent seeds, parameter diagrams, and pseudorandom generation. The 2025 open-access review by several of the same authors restates the general family as its Eq. (70), which fixes the present map's normalization, and identifies fixed-point conditions and chaotic numerical behavior as central concerns. The contribution here is the *complete* primitive period-two classification in the strict alternating region, including an exact four-cycle phase, a continuum of two-cycles at the critical surface, and the uniform finite-time identity there. It does not claim originality for the tent map, the family itself, or generic affine breakpoint methods.

## Limitations
The published 2024 article's full text was not accessible in the checked sources; only its publisher abstract, associated bibliographic material, and the later open-access full review were available for detailed comparison. A priority-equivalent formulation in the uninspected original article or elsewhere is therefore a residual risk. The parameter box \(0<b<p<a<1\) need not be chaotic; subcritical members converge to a two-cycle. No claim about chaotic invariant measures, higher periods, or the entire original parameter domain is made. The finding has not undergone an independent audit.

## References
1. M. Lawnik, L. Moysis, M. S. Baptista, C. Volos, “Discrete one-dimensional piecewise chaotic systems without fixed points,” *Nonlinear Dynamics* 112 (2024), 6679–6693. DOI: 10.1007/s11071-024-09349-6 (first public online February 24, 2024).
2. L. Moysis, M. Lawnik, M. S. Baptista, C. Volos, G. F. Fragulis, “A review of chaotification techniques for discrete-time systems,” *Nonlinear Dynamics* 113 (2025), 14103–14119. DOI: 10.1007/s11071-025-10934-6, Section 4.4, Equation (70).
