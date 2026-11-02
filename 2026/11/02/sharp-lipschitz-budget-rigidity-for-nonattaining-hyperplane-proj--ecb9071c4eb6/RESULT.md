# Sharp Lipschitz-budget rigidity for nonattaining hyperplane projections

## Finding
Let \(\alpha>-1\). The norm-one signed-power functional on the real Banach space \(X=C([0,1];\mathbb R)\) is
\[
\mu_\alpha(f)=2^\alpha(\alpha+1)\int_0^1\operatorname{sgn}(t-\tfrac12)|t-\tfrac12|^\alpha f(t)\,dt.
\]
Set \(Y_\alpha=\ker\mu_\alpha\). For a projection \(P:X\to Y_\alpha\), write uniquely \(P=I-\mu_\alpha\otimes h\), where \(\mu_\alpha(h)=1\). Its coefficient Lipschitz constant is \(\operatorname{Lip}(h)=\sup_{s\ne t}|h(s)-h(t)|/|s-t|\). At each budget \(L\ge0\), define
\[
\Pi_\alpha(L)=\inf\{\|P\|:P^2=P,\ \operatorname{ran}P=Y_\alpha,\ \operatorname{Lip}(h)\le L\},
\]
where the infimum of an empty family is \(+\infty\). Put
\[
L_* = \frac{2(\alpha+2)}{\alpha+1},\qquad C_\alpha=\frac{2^{\alpha+1}}{\alpha+2}.
\]
Then (i) \(\Pi_\alpha(L)=+\infty\) exactly for \(0\le L<L_*\); (ii) for every \(L\ge L_*\), there is a unique optimal projection, and
\[
\boxed{\Pi_\alpha(L)=1+R_\alpha(L)},\qquad
\boxed{R_\alpha(L)-C_\alpha\frac{R_\alpha(L)^{\alpha+2}}{L^{\alpha+1}}=1},
\]
where the scalar equation has a unique solution \(1<R_\alpha(L)\le L/2\) if \(L<\infty\), and the projection's coefficient is exactly
\[
h_{\alpha,L}(t)=\max\{-R_\alpha(L),\min\{L(t-\tfrac12),R_\alpha(L)\}\}.
\]
At the critical budget, \(R_\alpha(L_*)=(\alpha+2)/(\alpha+1)\) and the coefficient is affine, while for \(L>L_*\) it has two nonempty constant plateaus. The sharp asymptotic regimes are
\[
\boxed{\Pi_\alpha(L)-2=C_\alpha L^{-(\alpha+1)}+O(L^{-2(\alpha+1)})\quad (L\to\infty)}
\]
and, writing \(\delta=L-L_*\downarrow0\),
\[
\boxed{\Pi_\alpha(L)=1+\frac{\alpha+2}{\alpha+1}-\sqrt{\frac{\delta}{\alpha+1}}+O(\delta)}.
\]
The unconstrained projection constant of \(Y_\alpha\) is \(2\), but no projection realizes it. The Lipschitz-budget minimum exists uniquely for each feasible finite budget.

## Assumptions and scope
Everything is over the real scalars. The Banach-space norm is the ordinary supremum norm. The coefficient \(h\) is determined without ambiguity because \(\mu_\alpha\) has the specified normalization and every projection onto its kernel has the form stated above. The parameter \(\alpha\) is any real number strictly greater than \(-1\); the Lipschitz budget is nonnegative and finite. An absent optimizer below \(L_*\) is a feasibility statement, not an assertion about numerical solvers. The notation \(O(\cdot)\) concerns fixed \(\alpha\); no uniformity near \(\alpha=-1\) is claimed.

## Proof
**Step 1: Norm of projections.** The total variation of \(\mu_\alpha\) equals one, since each half of the interval has total variation \(1/2\). The functional does not attain its norm in \(C([0,1])\): equality would require a continuous unit vector to agree almost everywhere with the sign of \(t-1/2\), impossible at the midpoint. Any bounded projection onto \(\ker\mu_\alpha\) has kernel of dimension one. Hence it can and must be written \(P=I-\mu_\alpha\otimes h\) with \(\mu_\alpha(h)=1\). The space \(C([0,1])\) has the Daugavet property, so the rank-one Daugavet identity gives
\[
\|P\|=\|I-\mu_\alpha\otimes h\|=1+\|\mu_\alpha\|\,\|h\|_\infty=1+\|h\|_\infty.
\]
Thus the exact projection problem reduces to minimizing the supremum norm of a continuous Lipschitz norming vector.

**Step 2: A pointwise sharp envelope.** Suppose \(\operatorname{Lip}(h)\le L\) and \(\|h\|_\infty\le R\). For all \(0\le u\le1/2\),
\[
h(\tfrac12+u)-h(\tfrac12-u)\le\min\{2R,2Lu\}.
\]
The signed integral and positive density imply
\[
\mu_\alpha(h)\le M_\alpha(R,L):=2^{\alpha+1}(\alpha+1)\int_0^{1/2}u^\alpha\min\{R,Lu\}\,du.
\]
For every \(R,L\ge0\), equality is attained by the explicit centered clipped ramp \(t\mapsto\max\{-R,\min\{L(t-1/2),R\}\}\). An elementary integral gives, for positive \(L\),
\[
M_\alpha(R,L)=
\begin{cases}
R-C_\alpha R^{\alpha+2}/L^{\alpha+1},&0\le R\le L/2,\\
L(\alpha+1)/(2(\alpha+2)),&R\ge L/2.
\end{cases}
\]
For \(L=0\), \(M_\alpha=0\). In particular, \(\sup_R M_\alpha(R,L)=L/L_*\). This proves infeasibility below \(L_*\). For feasible \(L\), the first branch is strictly increasing for \(0\le R<L/2\), since its derivative is \(1-(2R/L)^{\alpha+1}\). It has a unique solution \(M_\alpha(R,L)=1\) in \((0,L/2]\), and the root exceeds one because \(M_\alpha(1,L)<1\). The clipped ramp with this \(R\) is feasible and minimizes \(\|h\|_\infty\).

**Step 3: Uniqueness, including the endpoint.** Equality at the sharp norm forces equality in the integrated nonnegative difference in Step 2. At any strictly supercritical budget \(L>L_*\), put \(a=R/L<1/2\). For almost every \(a<u<1/2\), the two values \(h(1/2\pm u)\) must equal \(\pm R\), respectively. Continuity extends the plateaus to their entire outer intervals. The two saturated values at \(1/2\pm a\), separated by distance \(2a\), have difference \(2R=2La\). The Lipschitz inequality therefore saturates at every intermediate point; hence \(h(t)=L(t-1/2)\) in the middle. At \(L=L_*\), equality in the integral forces the symmetric differences to be exactly \(2Lu\) for all \(u<1/2\). The Lipschitz bound is saturated across every centered interval, so \(h\) is affine with slope \(L\). The bound \(\|h\|_\infty\le L/2\) forces zero intercept. Thus the optimizing coefficient, and hence the projection, is unique for every feasible finite budget.

**Step 4: Asymptotic regimes.** Write \(R=1+e\). The exact equation is \(e=C_\alpha (1+e)^{\alpha+2} L^{-(\alpha+1)}\); the root tends to one and a Taylor expansion gives \(e=C_\alpha L^{-(\alpha+1)}+O(L^{-2(\alpha+1)})\). At the finite feasibility boundary, write \(R_*=L_*/2=(\alpha+2)/(\alpha+1)\) and
\[
F(R,L)=R-C_\alpha R^{\alpha+2}L^{-(\alpha+1)}-1.
\]
At \((R_*,L_*)\), direct differentiation gives \(F=F_R=0\), \(F_L=1/L_*\), and \(F_{RR}=-2(\alpha+1)/L_*\). The negative branch of the resulting quadratic fold, selected by \(R<L/2\), yields
\[
R=R_*-\sqrt{(L-L_*)/(\alpha+1)}+O(L-L_*),
\]
as claimed. In particular, the exponent of the high-budget deficit is exactly \(\alpha+1\), whereas the critical feasibility endpoint always has a square-root law.

## Verification
The proof covers all real \(\alpha>-1\) and every finite budget. The accompanying standard-library program `checker.py` compares the explicit envelope with a separate transformed numerical quadrature, tests root/feasibility inequalities, and checks the two asymptotic scalings on multiple parameter samples. It reports 4,971 passed deterministic assertions. Those finite calculations only supplement the symbolic integral, strict equality case, and Taylor argument; they do not certify any infinite quantifier. Run `python3 checker.py` from the extracted package directory.

## Relationship to prior work
Kania and Lewicki establish the finite-codimensional Daugavet projection-constant identity and the criterion that a hyperplane has a minimal projection precisely when its defining functional attains its norm. This result accepts that classification and supplies a new quantitative regularity constraint for an explicit nonattaining family: the exact feasibility threshold, optimal projection, uniqueness, optimal convergence exponent, and cusp law. Hille and Theewis develop general extremal/norming methods for bounded-Lipschitz functions acting on signed measures. Those methods concern the unit balls of two combined bounded-Lipschitz norms, rather than the two separately constrained quantities in the present optimization. No general classification of minimal projections or exact bounded-Lipschitz dual norm is asserted here.

## Limitations
The family consists of the specified symmetric signed-power functionals on the real continuous-function space; asymmetry, multiple sign changes, and vector-valued functionals are not treated. The regularity budget is imposed on the uniquely normalized coefficient \(h\), not on the projection's operator-valued modulus of continuity. The high-budget constant and exponent are for fixed \(\alpha\), with no uniformity near the limiting singular density. A mathematical priority check cannot rule out unpublished or differently named earlier solutions; independent mathematical validation has not been carried out.

## References
1. T. Kania and G. Lewicki, *Finite-codimensional subspaces of Daugavet spaces: projection constants and minimal projections*, arXiv:2604.10771v1, first public 2026-04-12, https://arxiv.org/abs/2604.10771 (especially Section 3 and Corollary 3.3).
2. S. C. Hille and E. S. Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions*, arXiv:2305.08500v1, first public 2023-05-15, https://arxiv.org/html/2305.08500v1 (especially Sections 4–6).
