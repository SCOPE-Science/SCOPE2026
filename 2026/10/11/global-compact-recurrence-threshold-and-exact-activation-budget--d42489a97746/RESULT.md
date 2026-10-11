# Global compact-recurrence threshold and exact activation budget for the zero-bias Chialvo map

## Finding

The zero-bias Chialvo map has an exact, global activation budget that simultaneously identifies its compact-recurrence threshold and constrains *all* compact stationary states, rather than just equilibria. Put \(t=1-a\), \(q=t+b\), \(x_*=t/q\), and
\[
c_*=t\left(1+\log\frac{q}{t}\right),\qquad
\Phi(u)=u-1-\log u\quad(u>0).
\]
For the map \(F(x,y)=(x^2e^{y-x},ay-bx+c)\), the following statements hold for every \(0<a<1\), \(0<b<1\), \(c>0\).

1. If \(c<c_*\), the **only nonempty compact set** \(K\subset\mathbb R^2\) satisfying \(F(K)=K\) is \(\{(0,c/t)\}\). In particular there is no nonzero bounded bi-infinite orbit and no nonconstant periodic orbit at such parameters. Forward-invariant transient sets with \(F(K)\subsetneq K\) are **not** excluded.
2. If \(c=c_*\), every compactly supported \(F\)-invariant probability measure is a convex combination of the equilibrium masses at \(O=(0,c/t)\) and \(E_*=(x_*,x_*-\log x_*)\).
3. For \(c>c_*\), let \(\mu\) be any compactly supported \(F\)-invariant probability measure with \(\mu(x>0)>0\), and let \(\mu_+\) be its normalized restriction to \(\{x>0\}\). Then the exact stationary activation budget is
\[
\boxed{\displaystyle \int\Phi(x/x_*)\,d\mu_+ =\frac{c-c_*}{1-a}.}
\]
Consequently, for every \(0<\eta<1\),
\[
\mu_+\bigl(\lvert x/x_*-1\rvert\ge\eta\bigr)
\le\min\!\left\{1,\frac{c-c_*}{t\,\Phi(1+\eta)}\right\}.
\]
The threshold is sharp as a **positive-equilibrium** onset: at \(c=c_*\) the map has \(E_*\), and at every \(c>c_*\) it has two positive equilibria. The fold value itself is **already known** from Chialvo's original work; the new content is the all-compact-dynamics exclusion and invariant-measure identity.

## Assumptions and scope

Iterates are defined on \(\mathbb R^2\) at constant parameters \(0<a<1\), \(0<b<1\), \(c>0\) and zero additive bias \(k=0\). An invariant compact set means \(F(K)=K\), not only \(F(K)\subset K\). Stationarity means \(F_*\mu=\mu\), with compact support. The map is generally noninvertible, so a bounded full orbit is a sequence indexed by all integers satisfying the recurrence at every index. On \(\{x>0\}\), the restriction of an invariant probability measure is again invariant whenever it has positive mass, since both the axis \(\{x=0\}\) and the open half-plane \(\{x>0\}\) are forward invariant and neither maps into the other.

## Proof

**Exact coboundary.** On \(x>0\), define \(V(x,y)=\log x+y/t\). Direct substitution of \(x'=x^2e^{y-x}\) and \(y'=(1-t)y-bx+c\) gives
\[
V(F(x,y))-V(x,y)=\log x-\frac{q}{t}x+\frac{c}{t}
=\frac{c-c_*}{t}-\Phi(x/x_*).
\tag{1}
\]
The elementary inequality \(\Phi(u)\ge0\), with equality precisely when \(u=1\), follows from strict convexity of \(u-1-\log u\).

**Compact recurrence strictly below the fold.** Every image has nonnegative first coordinate. If \(F(K)=K\) and \(K\) is compact, each point admits a bounded full prehistory in \(K\). For such a full orbit, either every activation coordinate is positive, or every activation coordinate is zero: \(x_{n+1}=0\) exactly when \(x_n=0\). In the positive case, (1) and \(c<c_*\) yield \(V(x_{n+1},y_{n+1})-V(x_n,y_n)\le-\epsilon\) for \(\epsilon=(c_*-c)/t>0\). Iteration backward forces \(V(x_{-N},y_{-N})\ge V(x_0,y_0)+N\epsilon\), contradicting the uniform **upper** bound on \(V\) over all positive points of a compact set (since \(x\) is bounded above and \(y\) is bounded). In the zero-activation case, \(y_{n+1}=ay_n+c\), whose unique bounded bi-infinite orbit is \(y_n=c/t\). Thus \(K=\{O\}\).

**Integrability at positive stationary states.** Let \(\mu_+\) be the normalized positive-activation component of an arbitrary compactly supported invariant probability measure \(\mu\). Its support may initially accumulate at the zero-activation axis. Fix \(M\ge\sup_{\operatorname{supp}\mu}|y|\) and choose \(0<r<e^{-M}/2\). Along a forward trajectory contained in the support, whenever \(0<x_n<r\),
\[
0<x_{n+1}=x_n^2e^{y_n-x_n}\le r e^M x_n <\tfrac12 x_n.
\]
Therefore such a trajectory has \(x_n\to0\) geometrically and cannot be recurrent to its initial positive point. Poincaré recurrence for \(\mu_+\) implies \(\mu_+(0<x<r)=0\). Hence \(\log x\), \(V\), and \(\Phi(x/x_*)\) are bounded and integrable \(\mu_+\)-almost surely, and invariance permits integrating (1):
\[
0=\int(V\circ F-V)\,d\mu_+
=\frac{c-c_*}{t}-\int\Phi(x/x_*)\,d\mu_+.
\tag{2}
\]
For \(c=c_*\), (2) forces \(x=x_*\) almost surely. The first-coordinate equation and invariance then force \(y=x_*-\log x_*\) almost surely, so \(\mu_+=\delta_{E_*}\). On \(\{x=0\}\), the remaining affine contraction has the unique invariant probability measure \(\delta_O\). Decomposing across the two invariant regions gives the stated two-point mixture.

For \(c>c_*\), (2) proves the exact budget. Since \(\Phi\) decreases on \((0,1)\), increases on \((1,\infty)\), and \(\Phi(1-\eta)>\Phi(1+\eta)>0\) for \(0<\eta<1\), Markov's inequality yields the concentration bound.

**Sharpness and provenance of the fold.** Positive fixed points satisfy \(y=x-\log x\) and
\[
c= qx-t\log x.
\tag{3}
\]
The right-hand side is strictly convex, has its unique minimum at \(x=t/q=x_*\), and takes the minimum value \(c_*\). Thus exactly one positive fixed point exists at equality and two for \(c>c_*\). Formula (3) and this positive fixed-point threshold were already given in the source literature; they are used here solely to demonstrate sharpness of the new global/measure consequences.

## Verification

The included standalone `checks/chialvo_identity.py` verifies the symbolic coboundary (1), the convex fixed-point profile (3), the zero-bias fold values at two classical parameter examples, and the strict scalar inequalities underlying the concentration bound. Run `python checks/chialvo_identity.py` with Python 3 and SymPy 1.14 or compatible. Computations validate identities, **not** the infinite-dimensional consequences; those follow from the bounded-full-orbit and Poincaré-recurrence arguments above.

## Relationship to prior work

Chialvo's 1993 public working paper and 1995 article give the precise model and **already derive the positive-equilibrium fold** \(c_*\), so no novelty is asserted for that formula. They present phase-plane and numerical excitable regimes but not equation (1) as a compact-dynamics obstruction or (2) as an all-invariant-measure identity. Jing–Yang–Feng (2006) studies fixed-point bifurcations and chaos for the same map; the accessible abstract does not settle the present compact-set and stationary-measure statements, but its full text remains a comparison risk. Pilarczyk–Signerska-Rynkowska–Graff (arXiv:2209.03443v2) uses rigorous finite-resolution Morse analysis, mainly for positive bias and fixed numerical ranges, including a broader coarse preliminary parameter grid; these finite-parameter computations do not imply a global symbolic identity for all \(0<a,b<1\) at zero bias. The one-dimensional reduced Chialvo voltage map analyzed in arXiv:2111.14499v3 holds recovery fixed, so its fixed-point and chaos theorems do not imply the coupled recovery budget.

## Limitations

The result applies only to the original **uncoupled zero-bias map**, not to any nonzero bias, forcing, diffusion, network coupling, noise, or modified activation law. Compact exact invariance must not be confused with forward invariance. It does not establish global convergence from every initial state, existence or uniqueness of chaotic measures above the fold, or absolute absence of unbounded trajectories. The stationary budget requires compactly supported invariant measures; it does not assert that every initial condition has such a measure. The fold formula and equilibrium counts are prior facts. An inaccessible full text concerning local bifurcations for the exact system creates a residual literature-comparison risk, not an assertion of independence or exhaustive novelty certification.

## References

1. D. R. Chialvo, *Generic Excitable Dynamics on a Two-Dimensional Map*, Santa Fe Institute Working Paper 93-03-013, manuscript dated 12 March 1993, https://www.santafe.edu/research/results/working-papers/generic-excitable-dynamics-on-a-two-dimensional-ma .
2. D. R. Chialvo, *Generic excitable dynamics on a two-dimensional map*, *Chaos, Solitons & Fractals* 5 (1995), 461–479, https://doi.org/10.1016/0960-0779(93)E0056-H .
3. P. Pilarczyk, J. Signerska-Rynkowska, G. Graff, *Topological-numerical analysis of a two-dimensional discrete neuron model*, arXiv:2209.03443v2, https://arxiv.org/html/2209.03443v2 .
4. Z. Jing, J. Yang, W. Feng, *Bifurcation and chaos in neural excitable system*, *Chaos, Solitons & Fractals* 27 (2006), 197–215, https://doi.org/10.1016/j.chaos.2005.04.060 .
5. *Periodic and chaotic dynamics in a map-based neuron model*, arXiv:2111.14499v3, https://arxiv.org/html/2111.14499v3 .
