# Strongly extreme Hardy quotients with uniquely minimizing non-inner functions

## Finding

For every integer \(N\geq1\) and every \(c\in(0,1)\), there is an explicitly defined weak-star closed linear subspace \(E_{N,c}\subset H^\infty(\mathbb D)\) of codimension exactly \(N\) with a norm-one coset \(x_{N,c}\in H^\infty/E_{N,c}\) satisfying all of the following:

1. \(x_{N,c}\) is a **strongly extreme** point of the quotient unit ball.
2. Its set of minimum-norm representatives is the singleton \(\mathcal M(x_{N,c})=\{F_c\}\).
3. \(F_c\) is invertible and outer, but is **not inner**: its radial boundary modulus is \(c\) on one semicircle and \(1\) on the other. In particular,
   \[
   \inf_{\Theta\ \mathrm{inner}}\|F_c-\Theta\|_\infty\geq1-c.
   \]

The construction disproves the proposed characterization of strongly extreme points of arbitrary Hardy-space quotients by the existence of a unique **inner** minimum-norm representative (Dyakonov, arXiv:2603.29103v1, final paragraph of Section 1). Its failure occurs in every positive finite quotient dimension and can be arbitrarily far from inner boundary modulus.

## Assumptions and scope

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), let \(\mathbb T\) be its boundary, and let \(dm(e^{it})=dt/(2\pi)\). All Hardy-space norms are supremum norms and all boundary functions below are radial limits (which exist almost everywhere).

For \(0<c<1\), set \(a=-\log c/\pi>0\) and define, with the principal logarithm on the right half-plane,
\[
W(z)=\frac{1+z}{1-z},\qquad F_c(z)=\sqrt c\,\exp\bigl(ia\Log W(z)\bigr).
\]
Write \(I=\{e^{it}:\pi<t<2\pi\}\), the lower open semicircle, and define the complex-linear functional
\[
L_c(g)=2\int_I g^*(\zeta)\overline{F_c^*(\zeta)}\,dm(\zeta),\qquad g\in H^\infty.
\]
For every integer \(N\geq1\), put
\[
E_{N,c}=z^{N-1}H^\infty\cap\ker L_c,\qquad x_{N,c}=F_c+E_{N,c}.
\]
For \(N=1\), the factor \(z^{N-1}H^\infty\) means all of \(H^\infty\). Strong extremity means: for each \(\varepsilon>0\) there is \(\delta>0\) such that \(\|x_{N,c}\pm y\|<1+\delta\) forces \(\|y\|<\varepsilon\) in the quotient.

## Proof

**1. Boundary geometry and outer property.** For \(z\in\mathbb D\), \(\Re W(z)>0\), hence \(-\pi/2<\Arg W(z)<\pi/2\). Therefore
\[
|F_c(z)|=\sqrt c\,\exp(-a\Arg W(z)),\qquad c<|F_c(z)|<1.
\]
In particular both \(F_c\) and its reciprocal are bounded analytic, so \(F_c\) is invertible in \(H^\infty\) and hence outer. For \(z=e^{it}\) away from the endpoints, \(W(e^{it})=i\cot(t/2)\). Its argument is \(\pi/2\) for \(0<t<\pi\) and \(-\pi/2\) for \(\pi<t<2\pi\); consequently,
\[
|F_c^*(e^{it})|=\begin{cases}c,&0<t<\pi,\\1,&\pi<t<2\pi.\end{cases}
\]
Thus \(\|F_c\|_\infty=1\), \(F_c\) is not inner, and on the upper semicircle \(|F_c^*-\Theta^*|\geq\bigl||\Theta^*|-|F_c^*|\bigr|=1-c\) for every inner \(\Theta\). This proves the asserted distance lower bound.

**2. Weak-star closure and exact codimension.** The functional \(L_c\) is a weak-star continuous functional on \(H^\infty\), because its boundary density \(2\mathbf 1_I\overline{F_c^*}\) belongs to \(L^1(\mathbb T)\). Since \(|F_c^*|=1\) on \(I\) and \(m(I)=1/2\), one has
\[
|L_c(g)|\leq\|g\|_\infty,\qquad L_c(F_c)=1.
\]
The subspace \(z^{N-1}H^\infty\) is the common kernel of the first \(N-1\) Taylor coefficient functionals at the origin; these are weak-star continuous. Thus \(E_{N,c}\) is weak-star closed.

Choose any odd integer \(k\geq N-1\). Since \(z^kF_c\in z^{N-1}H^\infty\), direct Fourier integration on \(I\) gives
\[
L_c(z^kF_c)=2\int_I\zeta^k\,dm(\zeta)=\frac{1-(-1)^k}{\pi i k}=\frac{2}{\pi i k}\neq0.
\]
Thus \(L_c\) is linearly independent of the first \(N-1\) Taylor coefficient functionals, and \(E_{N,c}\) has codimension exactly \(N\).

**3. Unique minimum-norm lift.** Since \(L_c\) vanishes on \(E_{N,c}\), every \(h\in F_c+E_{N,c}\) satisfies \(L_c(h)=1\). By the norm bound in Step 2, \(\|h\|_\infty\geq1\), with equality achieved by \(F_c\). Suppose \(\|h\|_\infty=1\). Then \(h^*\overline{F_c^*}\) takes values in the closed unit disk almost everywhere on \(I\), and its average there is \(1\). Since \(1\) is an extreme point of the closed disk, equality forces
\[
h^*(\zeta)\overline{F_c^*(\zeta)}=1\quad\text{for almost every }\zeta\in I.
\]
As \(|F_c^*|=1\) on \(I\), this says \(h^*=F_c^*\) almost everywhere on a set of positive arclength. Boundary uniqueness for bounded holomorphic functions then yields \(h\equiv F_c\). Therefore \(\mathcal M(x_{N,c})=\{F_c\}\) and \(\|x_{N,c}\|=1\).

**4. Strong extremity.** Since \(E_{N,c}\) is weak-star closed, every coset in \(H^\infty/E_{N,c}\) contains a minimum-norm representative (weak-star compactness of bounded balls). Suppose \(\|x_{N,c}\pm y\|\leq1\). Take minimum-norm representatives \(u\) and \(v\) of these two cosets with \(\|u\|_\infty,\|v\|_\infty\leq1\). Their average represents \(x_{N,c}\), so \(L_c((u+v)/2)=1\); hence \(L_c(u)=L_c(v)=1\). By Step 3's uniqueness argument, \(u=v=F_c\). Thus \(y=0\), proving \(x_{N,c}\) is extreme.

Finally, the quotient has finite dimension \(N\). In any finite-dimensional normed space every extreme point of the closed unit ball is strongly extreme: otherwise a sequence of perturbations \(y_j\) with \(\|y_j\|\geq\varepsilon>0\) and \(\|x\pm y_j\|\leq1+1/j\) would have a convergent subsequence with a nonzero limit contradicting extremity. (The perturbations are bounded by \(\|y_j\|\leq1+1/j\).) Therefore \(x_{N,c}\) is strongly extreme, as asserted.

## Verification

The branch identity, two boundary moduli, nonzero exact Fourier moment, and all quantifiers in the proof were independently checked algebraically. For the illustrative value \(c=0.3\), direct complex-arithmetic evaluations at three points in each open semicircle gave boundary moduli \(0.3\) and \(1.0\), respectively; the first five Fourier moments agree with \((1-(-1)^k)/(\pi i k)\). These finite evaluations are consistency checks only: Steps 1–4, not sampling, prove the result for every \(N\) and every \(c\in(0,1)\).

## Relationship to prior work

Dyakonov's 2026 Theorem 1.3 characterizes **ordinary** extreme points of Hardy quotients by a unique minimizing representative satisfying the usual logarithmic boundary criterion. Its final introductory paragraph proposes an analogous characterization for **strongly** extreme points with a unique *inner* minimizing representative. The present construction defeats the necessity of innerness for the stated class of arbitrary proper weak-star closed subspaces. That paper already discusses non-inner outer minimizers for certain infinite-Blaschke quotients, but neither asserts strong extremity for them nor provides the finite-codimensional construction here.

Dyakonov's 2023 theorem concerns strongly extreme points of finite-codimensional **subspaces** of \(H^\infty\), not finite-dimensional **quotients**. The distinction is essential: ordinary extremity automatically becomes strong extremity in finite-dimensional quotient spaces. No conclusion is claimed for the special class of shift-invariant quotients, where additional rigidity may survive.

## Limitations

This disproves only the **necessity** of an inner unique minimizer in the conjectured equivalence for unrestricted weak-star closed subspaces. It does not resolve the sufficiency direction, characterize arbitrary infinite-dimensional quotients, or give a criterion for quotients by invariant ideals. The constructions use non-invariant subspaces and the finite dimensionality of their quotients. They do not assert sharp upper bounds for the distance to inner functions, only the displayed lower bound. The origin of the counterexample is a boundary-exposing functional; the argument is elementary but structurally tied to the question's unrestricted hypothesis.

## References

1. K. M. Dyakonov, *Extreme points in quotients of Hardy spaces*, arXiv:2603.29103v1, first publicly submitted 31 March 2026, Section 1 (Theorem 1.3 and strong-extremity question). https://arxiv.org/html/2603.29103v1
2. K. M. Dyakonov, *Inner functions as strongly extreme points: stability properties*, arXiv:2301.11162v2, 2023, Theorem 1.1 (finite-codimensional subspaces, contrasted with quotients here). https://arxiv.org/html/2301.11162v2
