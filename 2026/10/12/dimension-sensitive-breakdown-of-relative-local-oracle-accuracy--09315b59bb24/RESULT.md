# Dimension-sensitive breakdown of relative local-oracle accuracy at active constraints

## Finding

For a local linear minimization oracle on a Euclidean ball centered at a feasible iterate, the distinction between *absolute* and *relative* subproblem accuracy is structural, even for perfectly conditioned strongly convex quadratics. At the ideal radius used for the sharp strongly convex Broximal Gradient Descent benchmark, every exact local oracle reaches the minimizer of an isotropic quadratic in one step. The sharp worst-case distance amplification of a relative-accuracy oracle is instead

\[
\mathcal A_d(\eta)=\begin{cases}
0,&\eta=0,\\
\eta,&d=1\text{ and }0<\eta\le1,\\
2,&d\ge2\text{ and }0<\eta\le1.
\end{cases}
\]

The value for dimension at least two is a supremum over admissible problem instances and oracle outputs; it need not be attained in a fixed instance. The result includes a globally sharp absolute-subproblem-gap certificate

\[
\boxed{\|y-x_\star\|^2\le\frac{2}{\mu}E},
\]

so an absolute accuracy target \(E<\mu\|x-x_\star\|^2/2\) suffices for a strict distance decrease. A relative target \(E\le\eta\Delta\) with any fixed \(\eta>0\) cannot replace it on arbitrary closed convex feasible sets in dimension at least two.

## Assumptions and scope

Fix an integer \(d\ge1\), a number \(\mu>0\), and a nonempty closed convex set \(X\subseteq\mathbb R^d\). The objective is

\[
f(z)=\frac{\mu}{2}\|z\|^2+\langle c,z\rangle,
\qquad c\in\mathbb R^d.
\]

The minimizer \(x_\star=\operatorname{argmin}_{z\in X}f(z)\) is unique. Choose any \(x\in X\), \(x\ne x_\star\), and set \(R=\|x-x_\star\|>0\), \(g=\nabla f(x)=\mu x+c\), and \(K=X\cap\overline B(x,R)\), where the ball is closed. Since \(x_\star\in K\), the linear oracle value \(m=\min_{z\in K}\langle g,z\rangle\) exists. Define the model improvement \(\Delta=\langle g,x\rangle-m\) and the absolute subproblem gap \(E=\langle g,y\rangle-m\) of any \(y\in K\). An \(\eta\)-relative output satisfies \(E\le\eta\Delta\), with \(0\le\eta\le1\). Relative accuracy refers to improvement in the **linear oracle objective**, not to accuracy in objective function values or Euclidean distance.

The universal worst-case factor \(\mathcal A_d(\eta)\) is the supremum of \(\|y-x_\star\|/R\) over all such \(X,c,\mu,x,y\) satisfying the stated conditions. The radius \(R\) depends on the unknown solution and is a theoretical benchmark; an implementation need not know \(R\) for the geometric statements to be valid.

## Proof

**1. Exact oracle and absolute-gap inequality.** The constrained first-order optimality condition for \(x_\star\) states that \(\langle\mu x_\star+c,z-x_\star\rangle\ge0\) for all \(z\in X\). For \(z\in K\), expansion of the squared ball constraint gives

\[
\|z-x\|^2\le R^2
\quad\Longrightarrow\quad
2\langle x-x_\star,z-x_\star\rangle\ge\|z-x_\star\|^2.
\]

Adding the first-order optimality inequality after multiplying this relation by \(\mu/2\) yields

\[
\langle g,z-x_\star\rangle
=\langle\mu x_\star+c,z-x_\star\rangle
 +\mu\langle x-x_\star,z-x_\star\rangle
\ge\frac\mu2\|z-x_\star\|^2.
\tag{1}
\]

In particular, \(x_\star\) is the *unique* minimizer of the linear form over \(K\), hence \(m=\langle g,x_\star\rangle\). For the input point, first-order optimality gives

\[
\Delta=\langle g,x-x_\star\rangle
=\mu R^2+\langle\mu x_\star+c,x-x_\star\rangle
\ge\mu R^2>0.
\tag{2}
\]

Taking \(z=y\) in (1) proves \(\|y-x_\star\|^2\le2E/\mu\). The constant 2 cannot be decreased: take \(X=\mathbb R^2\), \(\mu=1\), \(c=0\), \(x=(1,1)\), and \(y=(2,0)\). Both \(x_\star=0\) and \(y\) lie in \(K=\overline B((1,1),\sqrt2)\), and \(E=\langle x,y\rangle=2\) whereas \(\|y\|^2=4\). Thus equality holds in (1).

**2. Zero relative error.** At \(\eta=0\), nonnegativity of \(E\) and (1) force \(y=x_\star\) in every dimension. Hence \(\mathcal A_d(0)=0\).

**3. One dimension.** Let \(d=1\). If \(x>x_\star\), the interval \(\overline B(x,R)=[x_\star,2x-x_\star]\) implies that every \(z\in K\) satisfies \(z\ge x_\star\). The constrained first-order condition gives \(g\ge\mu(x-x_\star)>0\). Consequently,

\[
\frac{E}{\Delta}
=\frac{g(y-x_\star)}{g(x-x_\star)}
=\frac{|y-x_\star|}{R}.
\]

The case \(x<x_\star\) is identical after reflection. Thus \(\|y-x_\star\|/R\le\eta\). Equality is obtained for \(X=\mathbb R\), \(f(z)=z^2/2\), \(x=1\), \(x_\star=0\), and \(y=\eta\). Therefore \(\mathcal A_1(\eta)=\eta\) for \(0\le\eta\le1\).

**4. At least two dimensions.** The triangle inequality and the radius constraint give

\[
\|y-x_\star\|\le\|y-x\|+\|x-x_\star\|\le2R.
\tag{3}
\]

To show that 2 is optimal for every positive tolerance, it suffices to work in the first two coordinates. Given any \(a>0\) and \(0<\eta\le1\), take

\[
X=\{z\in\mathbb R^d:z_2\ge0\},\quad
\mu=1,\quad c=(0,C,0,\ldots,0),
\quad x=(1,a,0,\ldots,0),\quad y=(2,0,0,\ldots,0),
\]

where \(C\ge\max\{0,(2/\eta-1-a^2)/a\}\). Since \(C\ge0\), the constrained minimizer is \(x_\star=0\). The trust ball has radius \(R=\sqrt{1+a^2}\) and \(\|y-x\|=R\), so \(y\in K\). By the exact-oracle result in Step 1,

\[
E=\langle x+c,y\rangle=2,\qquad
\Delta=\langle x+c,x\rangle=1+a^2+Ca\ge2/\eta.
\]

Thus \(E\le\eta\Delta\), despite

\[
\frac{\|y-x_\star\|}{R}=\frac{2}{\sqrt{1+a^2}}\longrightarrow2
\quad\text{as }a\downarrow0.
\tag{4}
\]

Every instance has a Hessian equal to the identity, so neither poor conditioning nor nonconvexity explains the obstruction. The growing outward normal component \(C\) inflates the reference linear model improvement while leaving the tangent displacement of \(y\) underpenalized. Combining (3)–(4) proves \(\mathcal A_d(\eta)=2\) for all \(d\ge2\) and \(\eta>0\).

**5. Absolute accuracy as a replacement.** Step 1 immediately gives

\[
E\le\varepsilon\mu R^2
\quad\Longrightarrow\quad
\frac{\|y-x_\star\|}{R}\le\sqrt{2\varepsilon}.
\]

In particular, \(\varepsilon<1/2\) guarantees strict distance contraction. The optimal coefficient 2 in the underlying inequality is established by the equality example in Step 1. This proves the advertised boundary between the two error models.

## Verification

The proof above is universal and uses no numerical approximation. The accompanying standalone `verify.py` performs 536 exact-rational checks: explicit halfspace witnesses at five positive tolerances, one-dimensional equality examples, and selected feasible two-dimensional ball points. Running `python verify.py` prints `VERIFY_OK 536 exact-rational checks`. The finite tests are supplementary; they do not prove the quantified statements.

## Relationship to prior work

Richtárik, Gruntkowska, and Li (arXiv:2605.08850, first publicly posted May 9, 2026) introduce a local linear oracle and prove a sharp distance contraction for **exact** subproblem solutions in their Theorem 3.7. In the isotropic case \(L=\mu\), their ideal radius equals \(\|x-x_\star\|\) and the exact step reaches the solution in one iteration. The theorem here does not repropose that exact result: it classifies precisely what occurs when the local linear subproblem is solved only to a specified *relative improvement tolerance*, gives a worst-case jump from zero to two in higher dimensions, and supplies an absolute-gap remedy. Their Appendix B.7 distinguishes Ferris–Zavriev's exact trust-ball linear subproblem from Garber–Hazan's relaxed local linear optimization oracle: the latter permits an output in an expanded ball but requires a comparison no worse than the original ball optimum, unlike the nonzero positive model gap considered here.

Ferris and Zavriev (1996) analyze exact local linear trust-region subproblems with an Armijo radius mechanism and error-bound-based convergence. Garber and Hazan (2016) analyze a different relaxed LLOO specification for polytopes, not the relative positive model gap inside the original ball. Richtárik and Mahran (arXiv:2609.33383, September 27, 2026) study a projection interpretation and rates of exact local LMO; the abstract is accessible but the complete preprint was not available to inspect during this comparison. Related error-model literature does not, in the inspected material, establish the joint \(d=1\) versus \(d\ge2\) sharp worst-case classification above.

## Limitations

The result covers the **isotropic quadratic** subclass, all closed convex feasible sets, and one prescribed theoretical trust radius; it does not establish any multi-step convergence guarantee under approximate oracles. It is a worst-case statement across optimization problems, not a claim that every approximate oracle will amplify the error. The sharp factor two in higher dimensions is generally a supremum approached by a sequence of problem instances, not a universal attained maximum. The absolute accuracy certificate also depends on the unknown current solution distance and can require very tight subproblem solves. This result does not describe approximate projections, function-value errors, noisy gradient oracles, or the different relaxed-feasibility oracle of Garber and Hazan. An unindexed equivalent treatment of inexact local trust-ball linearization is a residual originality risk, especially given inaccessible portions of related recent work.

## References

1. P. Richtárik, K. Gruntkowska, and H. Li, *Broximal Gradient Descent: A Projection-Free Sister of Projected Gradient Descent* (previous title *Local LMO: Constrained Gradient Optimization via a Local Linear Minimization Oracle*), arXiv:2605.08850, first version 2026-05-09, revised 2026-09-28. Theorem 3.7, Appendix B.7, Appendix D.2.4, and Appendix H.5. https://arxiv.org/abs/2605.08850
2. M. C. Ferris and S. K. Zavriev, *The Linear Convergence of a Successive Linear Programming Algorithm*, 1996. Ferris--Zavriev (1996), posted text at studylib.net document 27985712
3. D. Garber and E. Hazan, *A Linearly Convergent Variant of the Conditional Gradient Algorithm under Strong Convexity, with Applications to Online and Stochastic Optimization*, SIAM Journal on Optimization **26** (2016), 1493–1528. DOI:10.1137/140985366.
4. P. Richtárik and A. Mahran, *Local LMO is Secretly a Projection Method!*, arXiv:2609.33383, first version 2026-09-27. https://arxiv.org/abs/2609.33383
