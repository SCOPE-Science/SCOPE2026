# Sharp Lipschitz budgets and lattice-phase convergence for nonattaining hyperplane projections

## Finding
Let \(0<q<1\) and \(\beta>0\). On the **real** Banach space \(X=C([0,1])\), define
\[
w_m=(1-q)q^{m-1},\qquad a_m=m^{-\beta},\qquad
\mu=\frac12\left(\sum_{m=1}^{\infty}w_m\delta_{a_m}-\delta_0\right),\qquad Y=\ker\mu.
\]
Thus \(\|\mu\|=1\). Every bounded projection onto \(Y\) is uniquely \(P_hf=f-\mu(f)h\), where \(\mu(h)=1\). For \(L\ge0\), let
\[
\Lambda_{q,\beta}(L)=\inf\{\|P_h\|:\mu(h)=1,\ h\in\operatorname{Lip}([0,1]),\ \operatorname{Lip}(h)\le L\},
\]
with infimum of the empty set equal to \(+\infty\). Put
\[
B_{q,\beta}=\sum_{m=1}^{\infty}\frac{w_m}{m^\beta},\qquad L_c=\frac2{B_{q,\beta}},\qquad
\Phi_L(t)=\sum_{m=1}^{\infty}w_m\min\left\{t,\frac L{2m^\beta}\right\}.
\]
The exact feasibility and optimum are
\[
\boxed{\Lambda_{q,\beta}(L)=+\infty\quad(0\le L<L_c),\qquad
\Lambda_{q,\beta}(L)=1+t_L\quad(L\ge L_c),}
\]
where \(t_L\) is the unique solution of \(\Phi_L(t_L)=1\) in \((0,L/2]\). It is achieved by
\[
h_L(x)=\min\{t_L,-t_L+Lx\},\qquad \|h_L\|_\infty=t_L,\quad \mu(h_L)=1.
\]
In particular \(t_{L_c}=L_c/2\), \(t_L>1\) for every finite feasible \(L\), and \(t_L\downarrow1\), so the unconstrained projection constant is \(2\) and is not attained.

There is a sharp **lattice-phase asymptotic**. Set \(s=(L/2)^{1/\beta}\), \(N=\lfloor s\rfloor\), and \(r=s-N\in[0,1)\). Uniformly in \(r\) as \(L\to\infty\),
\[
\boxed{\Lambda_{q,\beta}(L)-2=
\frac{\beta q^N}{N}\left(\frac1{1-q}-r\right)
+O_{q,\beta}\!\left(\frac{q^N}{N^2}\right).}
\]
Equivalently,
\[
\boxed{s q^{-s}(\Lambda_{q,\beta}(L)-2)
=\beta q^{-r}\left(\frac1{1-q}-r\right)+o(1).}
\]
The nonconstant phase profile has exact envelopes
\[
\boxed{\liminf_{L\to\infty}s q^{-s}(\Lambda_{q,\beta}(L)-2)
=\frac\beta{1-q},\qquad
\limsup_{L\to\infty}s q^{-s}(\Lambda_{q,\beta}(L)-2)
=\frac{\beta\exp\!\left(\frac{-\log q}{1-q}-1\right)}{-\log q}.}
\]
For the particular atomic nonattainment example \(q=1/2,\ \beta=1\), the threshold is \(L_c=2/\log2\). Writing \(s=L/2\),
\[
\boxed{\liminf_{L\to\infty}s2^s(\Lambda_{1/2,1}(L)-2)=2,\qquad
\limsup_{L\to\infty}s2^s(\Lambda_{1/2,1}(L)-2)=\frac4{e\log2}.}
\]
An exact finite expression for this case is given under Verification.

## Assumptions and scope
All functions and operators are real-linear, and \(C([0,1])\) has the supremum norm. The Lipschitz seminorm is \(\operatorname{Lip}(h)=\sup_{x\ne y}|h(x)-h(y)|/|x-y|\); it is imposed on the unique correction function \(h\) satisfying \(\mu(h)=1\), not on \(P_h\) as a map into the Lipschitz space. The parameters \(q\) and \(\beta\) are fixed before taking \(L\to\infty\). The infimum is taken over all bounded projections with a Lipschitz correction, not merely a chosen finite-parameter family. The symbols \(N\) and \(r\) are determined by the real variable \(s\); the error term is uniform across integer thresholds.

## Proof
**1. Projection parametrization and norm.** The atoms \(a_m>0\) are distinct and tend to zero; the positive and negative parts of \(\mu\) are supported on disjoint sets, each of mass \(1/2\). Hence \(\|\mu\|=1\). For a projection \(P\) onto the codimension-one kernel \(Y\), \(I-P\) has one-dimensional range, \(\mu\circ(I-P)=\mu\), and thus uniquely \(I-P=\mu\otimes h\) with \(\mu(h)=1\).

The norm identity \(\|P_h\|=1+\|h\|_\infty\) follows from the Daugavet property of \(C([0,1])\), applied to \(-\mu\otimes h\). It can also be checked directly for the present \(\mu\): the triangle inequality gives the upper bound. For the lower bound choose a non-atomic point \(z\notin\{0,a_1,a_2,\ldots\}\) with \(|h(z)|\) arbitrarily close to \(\|h\|_\infty\). For each fixed \(M\), continuity permits a norm-one test function with a prescribed sign at \(z\), the opposite desired sign at each of the finitely many \(a_m\) for \(m\le M\), and the corresponding sign at zero. Its \(\mu\)-integral is within \(q^M\) of the desired extreme value; taking \(M\to\infty\) gives \(\|I-\mu\otimes h\|\ge1+\|h\|_\infty\). This argument works even when the norm of \(h\) is maximized at an atom, by continuity and density of non-atoms.

**2. Exact bounded-amplitude Lipschitz extremum.** For any \(t\ge0\), any continuous \(h\) with \(\|h\|_\infty\le t\) and \(\operatorname{Lip}(h)\le L\) satisfies
\[
|\mu(h)|\le\frac12\sum_{m\ge1}w_m|h(a_m)-h(0)|
\le\sum_{m\ge1}w_m\min\{t,L/(2m^\beta)\}=\Phi_L(t).
\]
For \(t>0\), the explicit ramp \(h_{t,L}(x)=\min\{t,-t+Lx\}\) attains equality termwise; its supremum norm is \(t\), including at \(x=0\). Thus \(\Phi_L(t)\) is the **exact**, not merely upper-bounding, extremal functional value.

For every \(h\) with \(\operatorname{Lip}(h)\le L\), the same estimate without the amplitude cap gives \(|\mu(h)|\le L B_{q,\beta}/2\). This excludes projections when \(L<L_c\). At \(L=L_c\), the affine function \(h(x)=L_c(x-1/2)\) satisfies \(\mu(h)=1\) and has minimal norm \(L_c/2\). For \(L>L_c\), \(\Phi_L(1)<1\) (because infinitely many positive-weight atoms have \(L/(2m^\beta)<1\)) and \(\Phi_L(L/2)=LB_{q,\beta}/2>1\). Moreover \(\Phi_L\) is strictly increasing on \([0,L/2]\): its \(m=1\) summand grows strictly there. There is therefore exactly one \(t_L\in(1,L/2)\) with \(\Phi_L(t_L)=1\). The termwise extremal ramp yields a feasible projection of norm \(1+t_L\), and the same extremal inequality rules out every smaller correction norm. The same argument covers the endpoint \(L=L_c\).

As \(L\to\infty\), for each fixed \(t>1\) dominated convergence gives \(\Phi_L(t)\to t\), hence \(t_L\to1\). Every finite \(L\) has \(t_L>1\), and every bounded projection has \(\|h\|_\infty>1\) by the accumulation-point continuity obstruction; the unconstrained infimum \(2\) is unattained.

**3. Uniform boundary-layer expansion.** Define for \(s>0\)
\[
\eta(s)=\sum_{m\ge1}w_m\left(1-(s/m)^\beta\right)_+.
\]
Here \((v)_+=\max(v,0)\). For \(s=(L/2)^{1/\beta}\), the root equation is exactly
\[
1=t_L\bigl(1-\eta(s t_L^{-1/\beta})\bigr),
\qquad t_L-1=t_L\eta(s t_L^{-1/\beta}).
\]
Writing \(s=N+r\), substitute \(m=N+j\) to obtain the **exact** tail identity
\[
\eta(s)=(1-q)q^N\sum_{j=1}^\infty q^{j-1}
\left[1-\left(\frac{N+r}{N+j}\right)^\beta\right].
\]
Taylor expansion of \((1+v)^{-\beta}\) at \(v=0\), with its globally bounded second derivative for \(v\ge0\), and the finite second moment of the geometric weights give uniformly in \(r\in[0,1)\)
\[
\eta(s)=\frac{\beta q^N}{N}\left(\frac1{1-q}-r\right)
+O_{q,\beta}(q^N/N^2).
\]
For completeness, its piecewise derivative obeys \(|\eta'(z)|\le\beta q^{\lfloor z\rfloor}/z\) for \(z>0\) off the integer breakpoints, by bounding \(m^{-\beta}\le z^{-\beta}\) in the tail. Since \(\eta(s)=O(q^N/N)\), a trial value \(t=1+2\eta(s)\) has \(s t^{-1/\beta}=s+O(q^N)\). The derivative bound then gives \(\eta(s t^{-1/\beta})=\eta(s)+O(q^{2N}/N)\). Therefore \(t(1-\eta(s t^{-1/\beta}))>1\) for all large \(N\), implying \(1<t_L\le1+2\eta(s)\). Applying the same estimate at the true root yields
\[
t_L-1=\eta(s)+O_{q,\beta}(q^{2N}/N),
\]
which combined with the tail expansion proves the stated uniform asymptotic. The derivative estimate may be integrated over integer breakpoints, where \(\eta\) remains continuous.

**4. Exact extremal phase.** Multiplication by \(s q^{-s}\) gives the continuous periodic-phase profile \(F(r)=\beta q^{-r}(1/(1-q)-r)\), with matching endpoint values \(F(0)=F(1)=\beta/(1-q)\). Let \(c=-\log q>0\). Differentiation shows its only interior critical point is \(r_*=1/(1-q)-1/c\). The strict inequalities \(c>1-q\) and \(cq<1-q\) place \(r_*\) in \((0,1)\), and \(F\) increases then decreases. The endpoint value is the minimum, and \(F(r_*)=\beta e^{c/(1-q)-1}/c\) is the maximum. Each phase is realized along \(L=2(N+r)^\beta\), proving the liminf and limsup formulas.

## Verification
The supplied standalone `check.py` exercises the bounded-amplitude extremal formula, the finite-L root equation, the exact threshold, and the phase asymptotic with high-precision decimal arithmetic on two parameter pairs. Its finite computations are supplementary; Steps 1–4 above prove the infinitely indexed statements.

For the original \(q=1/2,\beta=1\) measure, let \(t=t_L\) and \(K=\lfloor L/(2t)\rfloor\). Then the root can also be evaluated exactly from the finite formula
\[
\boxed{t(1-2^{-K})+\frac L2\left(\log2-\sum_{m=1}^{K}\frac{2^{-m}}m\right)=1,\qquad K=\left\lfloor\frac L{2t}\right\rfloor.}
\]
This is a self-contained piecewise finite evaluation rule: choose the integer \(K\) consistent with the displayed floor and compute the unique \(t>0\). The formula holds at integer thresholds as well, since the entering term contributes the same value on both branches.

## Relationship to prior work
Kania and Lewicki (2026), Example 3.4(a), give precisely the case \(q=1/2,\beta=1\) and establish that its hyperplane has projection constant \(2\) but has no minimizing projection. Their Theorem 3.1 supplies the Daugavet duality; the present result concerns the **different** quantitative problem of the least projection norm under an explicit Lipschitz regularity budget, its sharp feasibility threshold, and its nonconstant lattice-phase asymptotic. These quantitative assertions are not stated in the inspected sections of their article.

Bounded-Lipschitz extremal integrals are classical and have a transport dual interpretation. For example, the dual program in Heinemann, Klatt, and Munk (2022), Section 2.1, treats finite supported transport measures. No new general transport duality is asserted here. The computation instead isolates the exact regularity tradeoff for countably infinitely many accumulating atoms and identifies its exponentially small, phase-dependent convergence law. Related regularization laws for distinct, absolutely continuous moment-annihilator subspaces do not imply the present atomic profile.

## Limitations
The result concerns real \(C([0,1])\), the specified accumulating atomic family, and global Lipschitz correction functions. It does not cover arbitrary nonattaining functionals, other moduli of continuity, or quantitative stability under perturbations of the locations and weights. The term \(O_{q,\beta}\) is not uniform as \(q\to0,1\) or \(\beta\to0,\infty\). The exact oscillatory profile follows from the geometric atomic weights; its persistence for irregular weights is not proved. A publication-priority search cannot rule out older differently named formulas for this same constrained extremal problem.

## References
1. T. Kania and G. Lewicki, *Finite-codimensional subspaces of Daugavet spaces: projection constants and minimal projections*, arXiv:2604.10771v1 (first submitted 12 April 2026), particularly Theorem 3.1 and Example 3.4(a). https://arxiv.org/html/2604.10771v1
2. F. Heinemann, M. Klatt, and A. Munk, *Kantorovich–Rubinstein Distance and Barycenter for Finitely Supported Measures: Foundations and Algorithms*, Applied Mathematics & Optimization 87 (2023), article 4 (first published 7 November 2022), especially the bounded-Lipschitz dual discussion in Section 2.1. https://doi.org/10.1007/s00245-022-09911-x
