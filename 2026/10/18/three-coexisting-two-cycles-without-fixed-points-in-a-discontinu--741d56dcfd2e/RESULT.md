# Three coexisting two-cycles without fixed points in a discontinuous power map

## Finding
For the two-branch power map introduced by Lawnik, Moysis and Volos, **three** is a sharp global upper bound on the number of distinct primitive two-cycles when the exponent differs from one. The sharpness witness has no fixed points yet has two repelling primitive two-cycles and one attracting primitive two-cycle. These three hyperbolic cycles and the absence of fixed points coexist on an open region of the map's four-parameter space.

## Assumptions and scope
For real parameters \(a,b,c\in(0,1)\) and \(d>0\), define \(F:[0,1]\to[0,1]\) by
\[
F(x)=\begin{cases}
1-(1-a)((b-x)/b)^d,&0\le x\le b,\\
c((x-b)/(1-b))^d,&b<x\le1.
\end{cases}
\]
Write \(L\) for the left branch and \(R\) for the right formula. The value at the switching point is \(F(b)=1\), not the right-hand limit \(0\). A primitive two-cycle means an unordered pair of distinct states \(\{x,y\}\) with \(F(x)=y\) and \(F(y)=x\). The upper bound concerns **all** primitive two-cycles on the real interval, for every admissible \((a,b,c,d)\) with \(d\ne1\); it does not assert an upper bound on higher-period cycles.

## Proof
**Reduction to a scalar equation.** Both branch maps are strictly increasing. Thus a primitive two-cycle cannot have both points in the same branch, since for \(x<y\) strict increase would force \(F(x)<F(y)\) instead of \(y>x\). Write the left point \(x\in[0,b]\) and right point \(y\in(b,1]\). As \(R(y)>0\) for \(y>b\), we must have \(x>0\), and \(R(y)=x\) requires \(x\le c\). The right inverse is
\[
R^{-1}(x)=b+(1-b)(x/c)^{1/d}.
\]
The cycle equations are therefore equivalent, without multiplicity loss, to zeros on \((0,\min\{b,c\}]\) of
\[
D(x)=1-b-(1-a)(1-x/b)^d-(1-b)(x/c)^{1/d}.
\]
For each zero, \(y=R^{-1}(x)\) is uniquely determined and belongs to \((b,1]\), and the condition \(D(x)=0\) gives \(L(x)=y\).

**Global three-cycle bound.** For \(0<x<\min\{b,c\}\), differentiation yields
\[
D'(x)=\frac{d(1-a)}{b}(1-x/b)^{d-1}-\frac{1-b}{d\,c^{1/d}}x^{1/d-1}.
\]
When \(d\ne1\), critical points satisfy
\[
\left[x^{1/d}(1-x/b)\right]^{1-d}
=\frac{d^2(1-a)c^{1/d}}{b(1-b)}.
\]
The positive base \(\phi(x)=x^{1/d}(1-x/b)\) increases strictly up to \(b/(d+1)\) and decreases strictly thereafter, as follows from \(\phi'(x)/\phi(x)=1/(dx)-1/(b-x)\). Raising this base to any nonzero real power preserves having at most two intersections with a horizontal line. Hence \(D'\) has at most two zeros in its open domain. Rolle's theorem rules out four distinct zeros of \(D\), even when its last allowed zero is at a domain endpoint. Therefore the full map has at most three primitive two-cycles.

**Sharp fixed-point-free example.** Set
\[
(a,b,c,d)=(1/20,1/10,21/200,1/2).
\]
Here \(c>b\), and the scalar equation is defined through \(x=b\). Four exact signs are
\[
\begin{aligned}
D(0)&=-1/20<0,\\
D(b/4)&=208/245-19\sqrt3/40>0,\\
D(3b/4)&=-67/1960<0,\\
D(b)&=41/490>0.
\end{aligned}
\]
The only nonrational sign follows by comparing positive squares:
\[
(208/245)^2-3(19/40)^2=168613/3841600>0.
\]
Although \(D(0)\) is a continuous endpoint extension rather than a permissible cycle state, it proves one zero in the open interval \((0,b/4)\). The other changes give zeros in \((b/4,3b/4)\) and \((3b/4,b)\). The global bound implies that these are precisely the three primitive two-cycles. They are all simple: there must already be a zero of \(D'\) between each consecutive pair, so a zero of \(D'\) at any root would produce at least three distinct critical points, impossible.

The map has **no fixed point**. On the left, its derivative is
\[
L'(x)=\frac{19}{4\sqrt{1-10x}}>1\quad(0\le x<b),
\]
so \(L(x)-x\) is increasing and starts at \(L(0)-0=1/20>0\); the inequality also holds at \(x=b\) by continuity. On the right, for all \(b<y\le1\), the elementary inequality \(y^2\ge4b(y-b)\) gives
\[
\frac{R(y)}{y}\le\frac{c}{2\sqrt{b(1-b)}}=\frac7{40}<1.
\]
Thus \(R(y)<y\) everywhere on the right. Neither branch contains a fixed point.

**Stability and robustness.** At any interior two-cycle root, \(R'(L(x))>0\), and
\[
\mu(x)-1=R'(L(x))D'(x),
\qquad \mu(x)=L'(x)R'(L(x))>0.
\]
Three simple roots of \(D\) with alternating signs force \(D'(x)>0,<0,>0\) in increasing root order. Hence their two-step multipliers respectively lie in \((1,\infty)\), \((0,1)\), and \((1,\infty)\). The outer cycles are hyperbolic repellers and the middle cycle a hyperbolic attractor.

All four strict sign tests and the fixed-point-free inequalities persist under sufficiently small parameter changes. For the latter assertion, write the left difference as a continuous function of \((a,b,d,t)\) on \(t=x/b\in[0,1]\), and the right difference as a continuous function of \((b,c,d,y)\) on the corresponding parameter-dependent compact right branch. Both differences are uniformly strict at the displayed witness. Nearby parameters therefore retain three simple two-cycles, their stability types, and no fixed points.

**Sharp exception at the linear exponent.** If \(d=1\) and \(a=b=c\), then for every \(x\in(0,b]\) the pair
\[
\bigl\{x,\,b+(1-b)x/b\bigr\}
\]
is a primitive two-cycle. Thus a finite universal bound across \(d=1\) would be false.

## Verification
The accompanying standalone script `verify.py` uses rational arithmetic and high-precision decimal evaluation. It tests the four signs and exact square comparison, brackets all three roots independently, checks the computed two-step multipliers, and tests the strict no-fixed-point estimates. Such finite evaluations are auxiliary consistency tests, not a substitute for the Rolle-theoretic global bound and exact inequalities above.

## Relationship to prior work
Lawnik–Moysis–Volos (2023), equation (15), introduces exactly this two-branch power family; its published treatment emphasizes a fixed-point-free regime and numerical chaotic dynamics, rather than a sharp **global two-cycle multiplicity theorem** and an explicit triple-coexistence parameter witness. Hogan–Higham–Griffin (2007) study the presence of period-two solutions in piecewise-linear discontinuous maps: the present power-law case is not affine and has three simultaneous two-cycles. Gaivão–Nogueira (2022) show an upper bound equal to the number of branches under the stronger **piecewise Lipschitz contraction** hypothesis; that theorem does not apply here because the left derivative blows up as the switching point is approached and the demonstrated repelling cycles have multipliers greater than one. A related publicly indexed fixed-point classification of the same power family does not cover the separate primitive two-cycle count.

## Limitations
No statement is made about chaos, topological entropy, all basins, invariant measures, global convergence, periods above two, or time-dependent perturbations. The result is new only relative to the checked sources; equivalently formulated antecedents not found in the accessible literature remain a priority risk. At the example the fractional exponent \(1/2\) falls outside the paper's particularly simple sufficient regime \(d\ge1\) for no fixed points, but the absence of fixed points is proved directly for the displayed parameter values. No independent mathematical audit is claimed.

## References
1. M. Lawnik, L. Moysis, C. Volos, *A Family of 1D Chaotic Maps without Equilibria*, **Symmetry** 15 (2023), article 1311, DOI `10.3390/sym15071311`, first publicly available 2023-06-27.
2. S. J. Hogan, L. Higham, T. C. L. Griffin, *Dynamics of a piecewise linear map with a gap*, **Proc. R. Soc. A** 463 (2007), 49–65, DOI `10.1098/rspa.2006.1735`.
3. J. P. Gaivão, A. Nogueira, *Dynamics of piecewise increasing contractions*, **Bull. London Math. Soc.** 54 (2022), 482–500, DOI `10.1112/blms.12577`, arXiv `2007.08014`.
