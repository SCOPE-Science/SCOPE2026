# Sharp positivity frontier and uniqueness of prime-three cycles in a rational second-order map

## Finding
For the recurrence
\[
z_{n+1}=h+\frac{b z_n}{z_{n-1}-1},\qquad b>0,\quad 0<h<1,
\]
interpreted only on sequences whose denominators are nonzero, there is **exactly one strictly positive prime-period-three orbit**, up to cyclic permutation, **if and only if**
\[
\boxed{\;0<b<1,\qquad 1-b+b^2<h<1.\;}
\]
When this condition holds, its three distinct entries lie strictly between \(0\) and \(h\). When it fails, there is no strictly positive prime-period-three orbit. The frontier is sharp: at \(h=1-b+b^2\), \(0<b<1\), the published orbit \((0,h,h(1-b))\) is nonnegative but not strictly positive.

## Assumptions and scope
A prime-period-three orbit is a triple \((x,y,z)\) of real numbers for which the cyclic relations
\[
(x-1)(z-h)=by,\quad(y-1)(x-h)=bz,\quad(z-1)(y-h)=bx
\]
hold with \(x,y,z\ne1\), and the corresponding orbit of \(T(x,y)=(y,h+by/(x-1))\) has least period three. Strict positivity means \(x,y,z>0\). The result concerns periodic points of the rational map, not their attraction or stability and not trajectories that reach a pole. All parameter ranges are strict except for the explicitly excluded threshold equality.

## Proof
Put \(t=1-h\in(0,1)\) and define
\[
\begin{aligned}
A&=b^2-2b+bt+t^2,\\
B&=-b^3+b(1-t)-(2-t)t^2,\\
L&=b^2-b+t,\\
M&=t^2-(1-b)t-b(1-b),\\
C(X)&=bX^3+AX^2+BX-LM,\\
Q(X)&=X^2-(b+h+1)X+h,\\
K(X)&=b^2-(X-1)(X-h).
\end{aligned}
\]
**Algebraic elimination.** Eliminating \(y,z\) from the three cyclic relations gives the necessary equation \((x-1)Q(x)C(x)=0\). The factor \(Q\) is exactly the fixed-point polynomial. If \(Q(x)=0\) and \(K(x)\ne0\), the first two cyclic equations have unique solution \(y=z=x\), hence cannot describe prime period three. If \(Q(x)=K(x)=0\), direct substitution forces \(b=h/(1+h)\), \(x=h/(1+h)\), and then \(C(x)=0\). Thus **each coordinate of every prime-three orbit is a root of \(C\)**. These statements follow equally from the explicit linear solve given below; there are no divisions by zero on a genuine prime-three orbit.

The discriminant identity is
\[
\operatorname{disc}_X C=t^2P^2,\quad
P=b^2\left(2b-1+\frac t2\right)^2+
 t^2\left[\left(t-\frac b2\right)^2+\frac52b^2+2b\right]>0.
\]
It follows that \(C\) has three distinct real roots for every \(b>0\), \(0<h<1\). Any prime-three orbit has three distinct coordinates: otherwise after a cyclic relabeling \(x=y=a\ne z\), subtraction of the first two cyclic identities forces \(a=1-b\), \(z=h+b-1\); the third identity forces \((h-1)(2b+h-2)=0\). Because \(h\ne1\), this implies \(z=a\), a contradiction. Consequently the three entries of any prime-three orbit are precisely the three distinct roots of \(C\).

**Necessity.** If those entries are all positive, Vieta's formulas imply \(B>0\) and \(-LM<0\). For \(b\ge1\), however, \(B=b(1-b^2-t)-(2-t)t^2<0\), impossible. Suppose \(0<b<1\), and set \(c=b(1-b)\). If \(t\ge c\) then \(L=t-c\ge0\). If \(M\le0\), the constant coefficient \(-LM\ge0\) contradicts positivity of the product of all three roots; if \(M>0\), the identity \(B=(t-b-1)M-t<0\) contradicts positivity of the pairwise-root sum. Therefore \(t<c\), equivalently \(h>1-b+b^2\).

**Sufficiency and uniqueness.** Suppose \(0<b<1\) and \(t<c\). Then \(L<0\), and \(M<0\) because \(M(t)\) is convex, with both \(M(0)=-c\) and \(M(c)<0\). Direct substitution gives
\[
C(0)=-LM<0,\quad C(h-b)=bt^3>0,\quad
C(1-b)=-bt^3<0,\quad C(h)=-b^2L>0.
\]
The parameter inequalities imply \(0<h-b<1-b<h<1\). Hence the intermediate value theorem places the three simple roots of \(C\) in the disjoint intervals \((0,h-b)\), \((h-b,1-b)\), and \((1-b,h)\). In particular all roots are strictly positive and avoid the pole \(1\).

For existence as a **real orbit**, not just three algebraic roots, solve the first two cyclic equations wherever \(K(x)\ne0\):
\[
y=-\frac{(x-1)(x-h+bh)}{K(x)},\qquad
z=-\frac{(x-h)(b+hx-h)}{K(x)}.
\]
A direct identity gives \((z-1)(y-h)-bx=-Q(x)C(x)/K(x)^2\). Therefore any root \(x\) of \(C\) for which \(K(x)\ne0\) determines a real cyclic triple. If \(b\ne h/(1+h)\), the exact resultants \(\operatorname{Res}_X(C,K)=-b^4t^2(bh+b-h)\) and \(\operatorname{Res}_X(C,Q)=-b^2(bh+b-h)P\) do not vanish. Hence every resulting coordinate is a root of \(C\) rather than an extraneous fixed-point root; the three coordinates all lie in \((0,h)\), so no denominator vanishes, and they give prime period three.

At the exceptional value \(b=h/(1+h)\), the cyclic triple is given explicitly by
\[
\left(\frac{h}{1+h},\quad
\frac{h^3+h^2-1}{h(1+h)},\quad
\frac{1+h-h^3}{1+h}\right).
\]
It satisfies the three cyclic equations directly. On this exceptional parameter curve the strict threshold condition is equivalent to \(h^3+h^2>1\), so all three entries are positive and distinct. Thus the exceptional case is included. Finally, every prime-three orbit uses all three simple roots of \(C\). Pick one of these roots where \(K\ne0\) (all three work outside the exceptional parameter and at least two work on it). Its other two orbit entries are uniquely determined by the first two cyclic equations. Any other prime-three orbit must use that same chosen root and consequently has the same orientation up to cyclic permutation. This proves uniqueness and the iff statement.

## Verification
The included `check_period3.py` reproduces the elimination factorization, discriminant and sum-of-squares identity, sign evaluations, resultants used for generic reconstruction, and the exceptional orbit using exact SymPy arithmetic. Running `python check_period3.py` produced two PASS lines. Rational examples \((b,h)=(1/4,9/10)\), \((3/5,4/5)\), and \((9/19,9/10)\) test the admissible domain; additional rational examples test the excluded domain. These finite numerical roots are cross-checks, **not** the proof of the all-parameter theorem; the proof above is symbolic and analytic.

## Relationship to prior work
AlSharawi, Al-Ghassani, and Amleh study exactly \(z_{n+1}=h+bz_n/(z_{n-1}-1)\) for \(b>0\), including \(0<h<1\), in their 2015 paper. Their Section 3.1 analyzes two-cycles and states that three-cycles may be positive, but explicitly limits its three-cycle treatment to the nonnegative example \((0,h,h(1-b))\) at \(h=1-b(1-b)\). The finding here is the missing **necessary-and-sufficient strict positivity region and orbit uniqueness**, not a claim to discover the recurrence or the frontier example. Work on Lyness-type integrable recurrences treats related models, especially the distinct integrable regime \(h=1\), and does not by itself imply this strict \(0<h<1\) phase diagram. The published MSC2020 class \(37E15\) describes combinatorial dynamics and types of periodic orbits, matching the primary subject of this finding.

## Limitations
No classification of all bounded orbits, higher periods, invariant measures, basin geometry, cycle stability, or boundary poles is claimed. The existence of signed real three-cycles beyond the positive regime is not classified here. Literature comparisons do not establish absolute independence from all unindexed work. A separate independent audit has not been performed.

## References
1. Z. AlSharawi, A. Al-Ghassani, and A. M. Amleh, *Basin of Attraction through Invariant Curves and Dominant Functions*, Discrete Dynamics in Nature and Society, Article 160672 (first published 26 May 2015), https://doi.org/10.1155/2015/160672 .
2. G. Bastien and M. Rogalski, *Global Behavior of the Solutions of Lyness' Difference Equation*, Journal of Difference Equations and Applications (2004), https://doi.org/10.1080/10236190410001728104 .
3. MSC2020, subject class \(37E15\): combinatorial dynamics (types of periodic orbits), https://mathscinet.ams.org/msc/msc2020.html .
