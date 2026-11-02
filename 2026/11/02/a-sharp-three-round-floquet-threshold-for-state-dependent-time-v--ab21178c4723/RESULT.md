# A sharp three-round Floquet threshold for state-dependent time-varying proximal acceleration

## Finding

For every parameter \(0<s<1\), consider the one-step-per-round TV-APG method of Kamijima, Marumo, and Takeda (Algorithm 3, with its APG2 operator from Proposition 3.5), using \(L=1\), \(D=2\), \(g=\iota_{[-1,1]}\), and the three-periodic smooth objectives
\[
 f_{3m}(u)=\frac{1-s}{2}u^2,\qquad
 f_{3m+1}(u)=f_{3m+2}(u)=\frac{1}{10}u^2
 \quad (m\geq0).
\]
All objectives are strongly convex and have the *same unique minimizer* \(u_*=0\); there is no movement of the optimizer. Nevertheless, the full three-round APG2 return map is locally exponentially attracting at the zero state **if and only if** \(7/64<s<1\). For \(0<s<7/64\), the zero state is a hyperbolic saddle; even under the *prescribed initial proximal-gradient step* of Algorithm 3, every sufficiently small, nonzero scalar starting point eventually produces a state, and an optimization iterate, outside a fixed positive neighborhood of zero. At \(s=7/64\), the return derivative has a simple eigenvalue \(-1\) and a second eigenvalue \(-7/100\); no nonlinear stability assertion is made at this equality case.

On precisely the same objectives and domain, one ordinary proximal-gradient step per round is a *globally contracting* method, with three-round contraction factor \(16s/25<1\). Hence the accelerated iteration can be locally unstable despite a stationary optimal solution and a contracting proximal-gradient baseline.

For example, at \(s=1/10\), the three-round derivative has eigenvalues
\[
 \lambda_{\pm}=\frac{-68\pm2\sqrt{906}}{125},
 \qquad \lambda_-<-1<\lambda_+<0,
\]
whereas the baseline three-round contraction factor is exactly \(8/125\).

## Assumptions and scope

The ambient space is \(\mathbb R\), the compact convex domain is \(\mathcal X=[-1,1]\), the nonsmooth term is its indicator \(g=\iota_{\mathcal X}\), and the Lipschitz gradient bound is \(L=1\). The diameter is \(D=2\). The number of APG2 steps per round is \(n=1\). Every curvature lies strictly between zero and one, so all objectives are \(L\)-smooth and strongly convex with common minimizer zero. The temporal variation condition from Assumption 2.1 is met with any positive \(\delta\) satisfying
\[
 2\delta\geq \frac12\left|\frac45-s\right|.
\]
In the displayed witness \(s=1/10\), the exact smallest permissible bound is \(\delta=7/40\).

Write \(S_a(x,z)=(x^+,z^+)\) for one APG2 step applied to \(f(u)=au^2/2\). Its exact update is
\[
 \beta=\frac1{1+|x-z|},\quad
 y=(1-\beta)x+\beta z,\quad
 z^+=\operatorname{proj}_{[-1,1]}\bigl(2(1-a)y-x\bigr),\quad
 x^+=\frac{x+z^+}{2}.
\]
Algorithm 3 first takes a proximal-gradient step using \(f_0\), then applies the above update once at each subsequent round, beginning with \(f_1\). Thus an arbitrary scalar initialization \(x_0\in[-1,1]\) creates \((x_1,z_1)=(s x_0,s x_0)\), and the three-round return map at these starting phases is \(F_s=S_{1-s}\circ S_{1/5}\circ S_{1/5}\).

Throughout, *local exponential attraction* and *Lyapunov instability* refer to the exact two-coordinate recurrence in a neighborhood of \((0,0)\). The instability statement concerning optimization iterates includes the prescribed algorithmic initialization, not arbitrary independent states.

## Proof

**1. Legal data and differentiability.** The quadratic curvatures are \(1-s\) and \(1/5\), both in \((0,1)\). For \(u,v\in[-1,1]\), the variation in objective differences between adjoining rounds is bounded by
\[
 \left|[f_{k+1}(u)-f_{k+1}(v)]-[f_k(u)-f_k(v)]\right|
 \leq \frac12\left|\frac45-s\right|,
\]
which proves the stated variation bound. The projection is inactive in a sufficiently small neighborhood of the zero state. The scalar map \(h\mapsto h/(1+|h|)\) is continuously differentiable, with derivative one at zero. Consequently, every \(S_a\) and \(F_s\) is \(C^1\) near the origin. Each fixes \((0,0)\).

**2. Exact linearization.** Set \(t=1-a\). Near zero,
\[
 y=x+\frac{z-x}{1+|z-x|}=z+O((|x|+|z|)^2),
\]
so \(x^+=t z+O(\|(x,z)\|^2)\) and \(z^+=-x+2t z+O(\|(x,z)\|^2)\). Thus
\[
 \mathrm DS_a(0,0)=M_t=\begin{pmatrix}0&t\\-1&2t\end{pmatrix}.
\]
The three-round order, determined by Algorithm 3's initial step and the periodic objectives, yields
\[
 T_s:=\mathrm DF_s(0,0)=M_sM_{4/5}^2
 =\begin{pmatrix}
 -8s/5&44s/25\\
 4/5-16s/5&(88s-32)/25
 \end{pmatrix}.
\]
Direct multiplication gives
\[
 \operatorname{tr}T_s=\frac{48s-32}{25},\qquad
 \det T_s=\frac{16s}{25}>0.
\]
In particular \(F_s\) is a local \(C^1\) diffeomorphism at the origin for \(s>0\).

**3. Exact stability frontier.** A real monic quadratic \(\lambda^2-p\lambda+d\) has both roots strictly inside the unit disk exactly when \(1-d>0\), \(1-p+d>0\), and \(1+p+d>0\). Applied to the characteristic polynomial of \(T_s\), these quantities are, respectively,
\[
 \frac{25-16s}{25},\qquad
 \frac{57-32s}{25},\qquad
 \frac{64s-7}{25}.
\]
For \(0<s<1\) the first two are strictly positive, so strict Schur stability is equivalent to \(s>7/64\). A \(C^1\) map with strictly Schur-stable derivative at a fixed point is locally exponentially attracting, and this proves attraction for \(7/64<s<1\). At \(s=7/64\), the characteristic polynomial factors as \((\lambda+1)(\lambda+7/100)\). For \(0<s<7/64\), its value at \(-1\) is negative and its value at zero is positive; hence one real root is smaller than \(-1\) and the other is in \((-1,0)\). This establishes a hyperbolic saddle.

**4. The actual initialization is transverse to the stable manifold.** The one-step initial proximal-gradient operation is exactly \(x_0\mapsto s x_0\) on \([-1,1]\), giving starting states \(s x_0(1,1)\). For any \(0<s<7/64\),
\[
 T_s\binom11=\binom{4s/25}{(8s-12)/25},\qquad
 \det\left[\binom11,\,T_s\binom11\right]=\frac{4s-12}{25}\ne0.
\]
Therefore the diagonal line is transverse to the one-dimensional stable eigenspace of \(T_s\). The local stable-manifold theorem for the hyperbolic local diffeomorphism \(F_s\) supplies a \(C^1\) local stable manifold tangent to that eigenspace. In a sufficiently small fixed neighborhood, its only intersection with the diagonal is the origin. The standard local stable-set characterization then implies that any sufficiently small nonzero \(s x_0(1,1)\) must eventually leave some fixed neighborhood under three-round returns; otherwise it would belong to that local stable manifold. This is Lyapunov instability **under valid Algorithm 3 initializations**, not merely a property of an unreachable auxiliary state.

Moreover, the algorithm always maintains \(z_{k}=2x_{k}-x_{k-1}\) for \(k\geq2\), with \(z_1=x_1\). If every optimization iterate \(x_k\) remained uniformly arbitrarily small, so would the entire state \((x_k,z_k)\). Thus a fixed state-neighborhood exit forces some scalar optimization iterate to leave a fixed positive neighborhood of zero. Because all curvatures are bounded away from zero for each fixed \(s\), this also forces a positive objective gap at some (initialization-dependent) later round. It does **not** prove persistent or asymptotic nonconvergence.

**5. Ordinary proximal gradient.** On \([-1,1]\), one PG step for curvature \(a\in(0,1)\) is \(u\mapsto(1-a)u\); projection never activates. Three consecutive rounds therefore multiply the iterate by \((4/5)^2s=16s/25\), strictly between zero and one for every \(0<s<1\). This is a global geometric contraction to the same optimum, completing the comparison.

## Verification

The attached standalone `verify_floquet.py` uses exact SymPy arithmetic to recompute the monodromy matrix, trace, determinant, Jury expressions, transversality determinant, witness eigenvalues, and equality boundary. It tests the exact Schur classification at 999 rational parameter values; 64 separately implemented nonlinear finite-difference comparisons supplement the analytic derivative. The script was executed successfully. Only the analytic derivative, Schur criterion, and stable-manifold argument prove the universally quantified claims; finite checks are not a substitute for them. Run with `python verify_floquet.py` in an environment with SymPy.

## Relationship to prior work

Kamijima, Marumo, and Takeda [1] define the exact APG2 and TV-APG updates in Proposition 3.5 and Algorithms 2–3, and establish a uniform objective-gap bound under bounded objective variation (Theorem 3.7). Their result neither asserts convergence to a stationary common minimizer under arbitrary fixed positive variation nor supplies the three-periodic local Floquet threshold above. The present finding does not dispute that objective-gap estimate: it concerns stability of the actual iterates about a common minimizer.

Classical Floquet and Jury/Schur theory already explains stability of periodic linear recurrences and is used as a proof tool, not claimed as new. Gökçek [2] studies stability conditions for periodically switched linear systems in general; it does not specifically identify the APG2 map, its initialized nonlinear dynamics, or the threshold \(7/64\). Related accelerated schemes in the optimization literature have distinct recurrences. The new application-specific claim is the exact stable/unstable phase frontier and the initialized accelerated-versus-PG separation, under the stated source algorithm and assumptions.

## Limitations

The theorem treats scalar quadratic objectives, a three-periodic curvature schedule, one APG2 step per round, exact arithmetic, and a fixed compact interval. At the critical parameter \(s=7/64\), nonlinear attraction or repulsion is not resolved. For \(s<7/64\), the proof establishes local Lyapunov instability and finite-time neighborhood exits, **not** global divergence, existence of a periodic attractor, or nonconvergence of every initial state. Its use of the classical stable-manifold theorem is a standard analytical ingredient. Searches and source comparisons cannot establish exhaustive historical priority; independent validation has not been performed.

## References

[1] T. Kamijima, N. Marumo, and A. Takeda, *Accelerated Proximal Gradient Method for Non-Strongly Convex Time-Varying Optimization*, arXiv:2610.11425v1, publicly submitted 2026-10-08, https://arxiv.org/abs/2610.11425. See Assumption 2.1, Proposition 3.5, Algorithms 2–3, Theorem 3.7, and the corresponding appendices.

[2] C. Gökçek, *Stability analysis of periodically switched linear systems using Floquet theory*, Mathematical Problems in Engineering, 2004, article 521989, DOI: 10.1155/S1024123X04401069. General linear switched-system background.
