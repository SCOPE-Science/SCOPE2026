# Exact angle modulus of smoothness at unit separation for the regular octagonal plane
## Finding
Let \(X_8=(\mathbb R^2,N)\), where
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For the angle modulus of smoothness introduced by Du, Ahmad, Din, and Li,
\[
\rho_X^a(\varepsilon)=\sup\left\{1-\frac12\|x+y\|^2:x,y\in S_X,\ \|x-y\|=\varepsilon\right\},
\]
the exact value at unit separation is
\[
\rho_{X_8}^a(1)=3\sqrt2-\frac92.
\]
Equivalently,
\[
\min\{N(x+y):N(x)=N(y)=N(x-y)=1\}=3-\sqrt2.
\]
Equality is attained by
\[
x=(1,2\sqrt2-3),\qquad y=(2-\sqrt2,2\sqrt2-2).
\]

## Assumptions and scope
The space is the real two-dimensional Banach space whose unit ball is the regular octagon represented by the displayed norm. The assertion concerns exactly the parameter value \(\varepsilon=1\) in the angle modulus \(\rho_X^a\). No claim is made here about the full function \(\varepsilon\mapsto\rho_{X_8}^a(\varepsilon)\), other polygonal norms, or higher dimensions.

## Proof
The norm is the maximum of eight linear support functionals,
\[
\pm s,\quad \pm t,\quad \frac{\pm s\pm t}{\sqrt2}.
\]
By the definition of \(\rho_X^a\), determining \(\rho_{X_8}^a(1)\) is equivalent to minimizing \(N(x+y)\) subject to
\[
N(x)=N(y)=N(x-y)=1.
\]
For every feasible pair, at least one of the eight support functionals is active at each of \(x\), \(y\), and \(x-y\). Choose one active facet for each. There are therefore \(8^3=512\) active-facet triples, and this choice is exhaustive even when a point lies at a vertex and has more than one active facet.

For a fixed active-facet triple the three boundary equalities are linear equations in the four coordinates of \((x,y)\). Exact row reduction over \(\mathbb Q(\sqrt2)\) shows that 32 triples are inconsistent and every consistent triple has rank three. Imposing all remaining support inequalities cuts the resulting affine line to an interval or makes it empty; exactly 48 feasible one-parameter branches remain.

On each feasible branch every support functional of \(x+y\) is affine in the branch parameter, so \(N(x+y)\) is the maximum of eight affine functions. A convex piecewise-affine function on an interval can attain its minimum only at an interval endpoint or at an intersection of two of its affine pieces. Checking precisely those finitely many points on all 48 branches gives
\[
N(x+y)\ge 3-\sqrt2.
\]
The displayed pair satisfies
\[
N(x)=N(y)=N(x-y)=1,\qquad N(x+y)=3-\sqrt2,
\]
so the lower bound is sharp. Consequently,
\[
\rho_{X_8}^a(1)=1-\frac12(3-\sqrt2)^2=3\sqrt2-\frac92.
\]

## Verification
The accompanying standard-library checker `verify_octagon_angle.py` performs the active-facet enumeration in exact arithmetic over \(\mathbb Q(\sqrt2)\). It reports 512 active-facet triples, 32 inconsistent triples, 48 feasible branches, and 32 branches attaining the common global minimum \(3-\sqrt2\). It also verifies the explicit equality pair and the final algebraic conversion to \(3\sqrt2-9/2\). The computation is finite and exhaustive for the stated polyhedral norm; no floating-point optimization is used.

## Relationship to prior work
Du, Ahmad, Din, and Li define \(\rho_X^a\), give the equivalent constrained-infimum formulation at \(\varepsilon=1\), and relate this value to uniform non-squareness. Their paper does not give the exact regular-octagon value above. Yang and Wang compute a generalized von Neumann--Jordan constant for the regular octagon, but that is a different supremal functional. Yang, Li, and Yang compute exact \(L_{YJ}\) and \(L'_{YJ}\) constants for the same regular-octagonal space, again with different objectives and constraints. Thus those exact octagon formulas do not imply the constrained minimum used here.

## Limitations
The proof is specific to \(\varepsilon=1\) and to the regular-octagonal norm. The literature comparison is based on the defining angle-modulus paper, two highly relevant exact regular-octagon papers, and targeted database searches; an unindexed source using an unexpected alias remains a residual novelty risk. The accompanying finite checker verifies the polyhedral optimization but is not an independent audit.

## References
D. Du, A. Ahmad, A. Din, and Y. Li, “Some Moduli of Angles in Banach Spaces,” *Mathematics* 10 (2022), 2965, DOI 10.3390/math10162965.

C. Yang and T. Wang, “Generalized von Neumann–Jordan constant \(C_{NJ}^{(p)}(X)\) for the regular octagon space,” *Mathematical Inequalities & Applications* 20 (2017), 483–490, DOI 10.7153/mia-20-32.

X. Yang, H. Li, and C. Yang, “On the \(L_{YJ}(\lambda,\mu,X)\) constant for the regular octagon space,” *Filomat* 38 (2024), 1583–1593, DOI 10.2298/FIL2405583Y.
