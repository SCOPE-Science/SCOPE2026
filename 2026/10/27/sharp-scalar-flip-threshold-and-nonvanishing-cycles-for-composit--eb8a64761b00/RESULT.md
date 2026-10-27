# Sharp scalar flip threshold and nonvanishing cycles for composite ProxSPS

## Finding

Consider the deterministic capped proximal Polyak rule (ProxSPS) with the differentiable loss \(f(x)=\tfrac12(x-1)^2\), quadratic regularizer \(\varphi(x)=\tfrac\lambda2x^2\), exact nonnegative loss lower bound \(C=0\), constant cap \(\alpha>0\), and \(0<\lambda<1\). For initial points in \([0,1]\), its unique optimal point is \(x_*=1/(1+\lambda)\). The sharp threshold for **convergence from every such initial point** is
\[
\alpha_c=\frac{2}{1-\lambda}.
\]
For \(0<\alpha<\alpha_c\), every orbit starting in \([0,1]\) converges geometrically to \(x_*\). At \(\alpha=\alpha_c\), the entire interval
\[
I=\left[\frac{3-\lambda}{3(1+\lambda)},\frac{3+\lambda}{3(1+\lambda)}\right]
\]
is invariant and the rule acts on it as the reflection \(x\mapsto2x_*-x\), yielding a continuum of exact period-two orbits apart from the fixed point. For \(\alpha>\alpha_c\), a nonoptimal exact period-two orbit exists at
\[
x_- =\frac{1+\alpha}{1+\alpha+2\alpha\lambda},\qquad
x_+=\frac{1+\alpha+\alpha\lambda}{1+\alpha+2\alpha\lambda}.
\]
It has positive amplitude \(x_+-x_-=\alpha\lambda/(1+\alpha+2\alpha\lambda)\); its local two-step multiplier is \((1-\alpha)/(2(1+\alpha\lambda))\). The cycle is locally attracting exactly when \(\alpha(1-2\lambda)<3\), linearly neutral at equality, and repelling when \(\alpha(1-2\lambda)>3\). The optimal fixed point is repelling for every \(\alpha>\alpha_c\). These assertions concern the precise deterministic ProxSPS rule and do not describe all possible large-step orbits.

## Assumptions and scope

The objective is \(\psi=f+\varphi\) on the real line, with \(f(x)=\tfrac12(x-1)^2\), \(\varphi(x)=\tfrac\lambda2x^2\), \(0<\lambda<1\), and the exact loss lower bound \(C=0\). The constant cap \(\alpha>0\) is the same in every update. The source's gradient-regularizer correction is retained: for \(x\ne1\), set
\[
\tau(x)=\min\left\{\alpha,\max\left\{0,\frac{(1+\alpha\lambda)f(x)-\alpha\lambda f'(x)x}{(f'(x))^2}\right\}\right\}.
\]
Since \(f'(x)=x-1\), the fraction simplifies to \((1+\alpha\lambda)/2-\alpha\lambda x/(x-1)\). At \(x=1\) set \(\tau(1)=\alpha\), the source's zero-gradient convention. The exact update is
\[
F(x)=\operatorname{prox}_{\alpha\varphi}(x-\tau(x)f'(x))
=\frac{x-\tau(x)(x-1)}{1+\alpha\lambda}.
\]
Convergence from every start is claimed only for \(x_0\in[0,1]\). The cycle's local attraction is in the usual real-line dynamical sense in neighborhoods avoiding the switching point. Finite precision, stochastic sampling, unbounded caps, other source-model variants, and higher-dimensional objectives are excluded.

## Proof

**1. Piecewise-affine map and invariance.** For \(0\le x<1\), the unconstrained positive step is
\[
s(x)=\frac{1+\alpha\lambda}{2}+\frac{\alpha\lambda x}{1-x}>0.
\]
If \(s(x)<\alpha\), then substitution gives \(F(x)=(1+x)/2\). If \(s(x)\ge\alpha\), then \(F(x)=((1-\alpha)x+\alpha)/(1+\alpha\lambda)\). Both formulas agree at their switch and define a continuous piecewise-affine map on \([0,1]\) including \(F(1)=1/(1+\alpha\lambda)\). The first branch maps \([0,1]\) into \([1/2,1]\). If \(\alpha\le1\), the second branch maps \([0,1]\) into \([0,1]\); if \(\alpha>1\), it is decreasing, and its values at \(0,1\) might not both be applicable, but throughout the capped branch its maximum occurs at the switch (or \(x=0\) if there is no switch). At a switch the value is \((1+c)/2<1\), and at \(x=1\) it is positive. Thus \(F([0,1])\subseteq[0,1]\) in all cases. The unique minimizer \(x_*=1/(1+\lambda)\) is fixed, since \(s(x_*)=(1+\alpha\lambda)/2+\alpha\), so the capped branch applies there and \(F(x_*)=x_*\).

**2. Below threshold.** Every slope is either \(1/2\) or \(q=(1-\alpha)/(1+\alpha\lambda)\). If \(0<\alpha<2/(1-\lambda)\), then \(|q|<1\). Consequently the continuous piecewise-affine map is globally Lipschitz on \([0,1]\) with constant \(L=\max\{1/2,|q|\}<1\). Banach contraction gives geometric convergence to its unique fixed point \(x_*\), for every \(x_0\in[0,1]\).

**3. Critical case.** For \(\alpha=2/(1-\lambda)\) the capped slope is \(q=-1\); since \(x_*\) is fixed, this branch acts as \(2x_*-x\). Its switching point is \(c=(3-\lambda)/(3(1+\lambda))\), and the reflected endpoint is \(u=2x_*-c=(3+\lambda)/(3(1+\lambda))\). Since \(c<u<1\), the whole interval \([c,u]\) is within the capped branch and is mapped into itself by reflection. Hence \(F^2(x)=x\) for every \(x\in[c,u]\). Every noncentral point has exact period two, so global convergence fails at the threshold.

**4. Above threshold.** When \(\alpha>2/(1-\lambda)\), necessarily \(\alpha>1\) and the unique switch on \((0,1)\) is
\[
c=\frac{2\alpha-1-\alpha\lambda}{2\alpha-1+\alpha\lambda}.
\]
Let \(d=1+\alpha+2\alpha\lambda\) and define \(x_-=(1+\alpha)/d\), \(x_+=(1+\alpha+\alpha\lambda)/d\). Algebra gives
\[
c-x_- = \frac{2\alpha\lambda(\alpha(1-\lambda)-2)}{(2\alpha-1+\alpha\lambda)d}>0,
\qquad
x_+-c=\frac{3\alpha\lambda(1+\alpha\lambda)}{(2\alpha-1+\alpha\lambda)d}>0.
\]
Thus the uncapped midpoint branch applies to \(x_-\), giving \(F(x_-)=(1+x_-)/2=x_+\), while the capped branch applies to \(x_+\), giving \(F(x_+)=((1-\alpha)x_++\alpha)/(1+\alpha\lambda)=x_-\). The inequalities \(0<x_-<c<x_+<1\) make this a genuine two-cycle. Moreover
\[
x_- -x_*=-\frac{\lambda(\alpha-1)}{(1+\lambda)d}<0,
\qquad
x_+-x_*=\frac{\lambda(1+\alpha\lambda)}{(1+\lambda)d}>0.
\]
The fixed point lies in the capped branch and has derivative \(q=(1-\alpha)/(1+\alpha\lambda)<-1\), so it is repelling. The two points lie strictly inside their branches, so the derivative of the return map \(F^2\) at either is \(q/2\). A one-dimensional differentiable return map is locally attracting for \(|q/2|<1\), repelling for \(|q/2|>1\); at equality its linear multiplier is \(-1\), establishing *neutral linear stability only*, not nonlinear attraction or repulsion. Since \(\alpha>1\), \(|q/2|<1\) is equivalent to \(\alpha(1-2\lambda)<3\). The cycle's amplitude tends to \(2\lambda/[3(1+\lambda)]>0\) as \(\alpha\downarrow\alpha_c\), showing a nonvanishing onset at a continuum-of-cycles boundary.

**5. Nonoptimality and regularization role.** Because \(\psi(x)-\psi(x_*)=(1+\lambda)(x-x_*)^2/2\), each cycle point has positive objective error. In contrast, if \(\lambda=0\), then on \([0,1]\), \(F(x)=(1+x)/2\) whenever \(\alpha\ge1/2\), independently of how large the cap is; the instability is induced by the interplay of the regularizer and capped rule, not simply the loss quadratic.

## Verification

The standalone standard-library file `verify.py` evaluates the **source-rule formula** with rational arithmetic, separately verifies the formula at the switch, checks a strict two-cycle at \((\lambda,\alpha)=(1/5,3)\), confirms the interval of exact cycles at \((1/5,5/2)\), and compares the local multipliers on attracting and repelling examples. Its successful output is `VERIFY_OK; exact fractions, both cycle orientations, critical band and stable/unstable examples`. These finite exact checks corroborate, but cannot substitute for, the universal piecewise-affine proof above.

## Relationship to prior work

Schaipp, Gower, and Ulbrich's ProxSPS paper defines the capped proximal Polyak update and proves convergence under sufficient stepsize conditions; its results do not imply convergence at arbitrarily large fixed caps. The result here identifies a **sharp global-convergence frontier within a complete scalar strongly-convex composite family**, along with a continuum of critical two-cycles and an exact post-critical orbit and stability range. Asi and Duchi's broader model-based proximal convergence theory concerns general models and step-size conditions rather than this precise deterministic fixed-cap bifurcation. Other algorithm-specific periodicity results (including for Lion, a composite trust-region rule, and Bregman adaptive proximal gradient) use different maps and do not imply this source-update result. No claim of comprehensive literature uniqueness is made.

## Limitations

The guarantee is for the invariant interval \([0,1]\), not every real initial point. A locally attracting period-two orbit does not imply every nonfixed orbit converges to it. At the neutral multiplier boundary \(\alpha(1-2\lambda)=3\), nonlinear stability is unproved. The computation file verifies finitely many rational cases only. Other papers may contain equivalent bifurcations under changed notation; independent audit and external validation have not been performed. The result does not contradict published convergence theorems that impose a conservative upper bound on the cap.

## References

1. Fabian Schaipp, Robert M. Gower, Michael Ulbrich. *A Stochastic Proximal Polyak Step Size*. arXiv:2301.04935v1 (first public 2023-01-12); original ProxSPS model, Algorithm 3 and deterministic specialization. https://arxiv.org/abs/2301.04935
2. Hilal Asi, John C. Duchi. *Stochastic (Approximate) Proximal Point Methods*. arXiv:1810.05633. https://arxiv.org/abs/1810.05633
3. Fabian Schaipp, Robert M. Gower, Adrien Taylor. *Step-Size Stability in Stochastic Optimization: A Theoretical Perspective*. arXiv:2602.09842. https://arxiv.org/abs/2602.09842
