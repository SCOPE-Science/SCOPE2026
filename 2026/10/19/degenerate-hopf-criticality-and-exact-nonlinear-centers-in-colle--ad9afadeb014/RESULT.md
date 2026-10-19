# Degenerate Hopf criticality and exact nonlinear centers in collective-risk games

## Finding
For both linear and sigmoidal adaptive-risk feedback systems of Liu, Chen, and Szolnoki (2023), the **first Lyapunov coefficient vanishes identically** on the entire interior oscillatory threshold, for every admissible group size and all positive biological parameters for which the interior equilibrium exists. Consequently, the usual nondegenerate supercritical/subcritical Hopf test cannot determine the critical dynamics. In the natural balanced-majority regime (odd group size \(N=2m+1\), threshold \(M=m+1\)), both systems have an **exact nonlinear center** at the critical parameter: a punctured neighborhood of the interior equilibrium is foliated by nonisolated periodic trajectories. This is stronger than vanishing of the cubic focus quantity, and it rules out a locally attracting isolated cycle at the critical parameter in this balanced subfamily.

## Assumptions and scope
Fix integers \(N\ge3\) and \(1<M<N\). Put \(n=N-1\), \(m=M-1\), \(k=N-M\), \(p=m/n\). Thus \(m,k\ge1\) and \(m+k=n\). Choose \(b,c,\varepsilon>0\), and define
\[
 g(x)=x(1-x),\qquad P(x)=b\binom{n}{m}x^m(1-x)^k,\qquad r_*=\frac{c}{P(p)}.
\]
Assume \(0<c<P(p)\), equivalently \(0<r_*<1\). On the open unit square \(0<x,r<1\), consider
\[
 \varepsilon\dot x=g(x)[P(x)r-c],\qquad \dot r=r(1-r)H(x).
\]
Exactly two original feedback laws at their critical settings are considered:

* **Linear:** \(H(x)=u(1-x)-x\), \(u=m/k\).
* **Sigmoidal:** \(H(x)=-\tanh(\beta(x-T)/2)\), \(\beta>0\), \(T=p\).

Both satisfy \(H(p)=H''(p)=0\) and \(H'(p)<0\). The critical interior equilibrium is \((p,r_*)\). The word *critical* means that the linear trace vanishes and the linear eigenvalues are imaginary; no nondegenerate Hopf conclusion is assumed.

## Proof
**1. Linear center frequency.** The mode condition gives \(P'(p)=0\). Put
\[
 a=\frac{g(p)P(p)}{\varepsilon}>0,\qquad d=-r_*(1-r_*)H'(p)>0,\qquad \omega=\sqrt{ad}.
\]
At \((p,r_*)\), the Jacobian is \(\bigl(\begin{smallmatrix}0&a\\-d&0\end{smallmatrix}\bigr)\); its eigenvalues are \(\pm i\omega\). This holds for both listed feedbacks. For linear feedback, \(\omega^2=mc(1-r_*)/(n\varepsilon)\); for sigmoidal feedback, \(\omega^2=\beta mkc(1-r_*)/(2n^2\varepsilon)\).

**2. An exact binomial derivative identity.** Direct logarithmic differentiation (valid on \(0<x<1\), and then polynomially at all \(x\)) gives
\[
 g(x)P'(x)=(m-nx)P(x).
\]
Differentiate twice and evaluate at \(x=p=m/n\). Since \(P'(p)=0\) and \(m-np=0\), this yields the decisive identity
\[
 \boxed{g(p)P'''(p)+2g'(p)P''(p)=0.}
\]
No symmetry of \(P\) is assumed: this holds also when \(m\ne k\).

**3. The cubic focus coefficient.** Set \(U=x-p\) and \(V=-\sqrt{a/d}(r-r_*)\). Then the transformed vector field is \(\dot U=-\omega V+f(U,V)\), \(\dot V=\omega U+h(U,V)\), with \(f,h\) containing only terms of total order at least two. All derivatives below are evaluated at \(U=V=0\):
\[
 f_{UU}=\frac{r_*g(p)P''(p)}{\varepsilon},\quad
 f_{UV}=-\sqrt{\frac da}\frac{g'(p)P(p)}{\varepsilon},\quad
 f_{UUU}=\frac{r_*}{\varepsilon}[g(p)P'''(p)+3g'(p)P''(p)].
\]
Because \(H(p)=H''(p)=0\) and the risk equation is quadratic in \(r\), one also has \(h_{UU}=h_{UUV}=h_{VV}=h_{VVV}=f_{VV}=f_{UVV}=0\). The standard planar first-focus formula for the stated rotation normalization is
\[
 16L_1=f_{UUU}+f_{UVV}+h_{UUV}+h_{VVV}
 +\omega^{-1}\{f_{UV}(f_{UU}+f_{VV})-h_{UV}(h_{UU}+h_{VV})-f_{UU}h_{UU}+f_{VV}h_{VV}\}.
\]
The displayed zero derivatives reduce this exactly to \(16L_1=f_{UUU}+\omega^{-1}f_{UV}f_{UU}\). Since \(\omega=\sqrt{ad}\) and \(a=g(p)P(p)/\varepsilon\),
\[
 \frac{f_{UV}}{\omega}=-\frac{g'(p)}{g(p)},\qquad
 16L_1=\frac{r_*}{\varepsilon}[g(p)P'''(p)+2g'(p)P''(p)]=0.
\]
Every standard smooth positive rescaling of eigenvectors and time preserves the vanishing, although it changes the numerical normalization of \(L_1\). Thus the first Lyapunov coefficient in the usual nondegenerate Hopf criterion is zero for all admissible \(m,k,b,c,\varepsilon\) and every positive sigmoid steepness \(\beta\).

**4. Exact centers when the threshold is balanced.** Suppose \(m=k\), so \(p=1/2\), \(N=2m+1\) and \(M=m+1\). Then \(P(1-x)=P(x)\), \(g(1-x)=g(x)\), and in *both* critical feedback systems \(H(1-x)=-H(x)\). Writing the full vector field as \(F\) and \(R(x,r)=(1-x,r)\), these identities are exactly
\[
 F(Rz)=-DR\,F(z),\qquad R^2=\mathrm{id}.
\]
Hence the flow is reversible: \(R\phi_t=\phi_{-t}R\) wherever it exists. The fixed line of the involution is \(x=1/2\). The linear center has frequency \(\omega>0\). For each sufficiently small nonzero displacement \(\delta\), the solution starting at \((1/2,r_*+\delta)\) crosses the same fixed line transversely at a time \(\tau(\delta)\) approaching \(\pi/\omega\). To justify existence uniformly near \(\delta=0\), divide its first-coordinate displacement by \(\delta\); smooth dependence of solutions extends that quotient to \(\delta=0\), where its time dependence has a simple zero at \(\pi/\omega\). The implicit-function theorem supplies \(\tau(\delta)\). Reversibility about both crossings implies \(\phi_{2\tau(\delta)}(1/2,r_*+\delta)=(1/2,r_*+\delta)\). Nearby cycles continuously fill a punctured neighborhood because the linearized center has nonzero angular speed, and their periods converge to \(2\pi/\omega\). The equilibrium is therefore a nonlinear center, and no one of these small cycles is an isolated attracting limit cycle.

For the balanced case, \(\omega^2=c(1-r_*)/(2\varepsilon)\) under linear feedback and \(\omega^2=\beta c(1-r_*)/(8\varepsilon)\) under sigmoidal feedback.

## Verification
The accompanying standalone `verify.py` uses exact SymPy Hessian/third-derivative tensors and the independent complex-eigenvector normal-form contraction, rather than directly substituting the preceding planar derivative formula. It confirms vanishing exactly at the rational parameter choices \((N,M)=(5,3),(6,3),(8,5)\) for both feedback types. It also checks reflection reversibility symbolically and integrates four balanced-case periodic returns with endpoint errors below \(5\times10^{-13}\). These finite computations corroborate, but do not substitute for, the general polynomial identity and reversible-center proof.

For example, for \(N=5\), \(M=3\), \(b=1\), \(c=1/10\), \(\varepsilon=1/10\), and \(\beta=3\), one finds \(p=1/2\), \(r_*=4/15\). The two exact squared linear frequencies are \(\omega^2=11/30\) (linear) and \(\omega^2=11/40\) (sigmoidal).

## Relationship to prior work
Liu, Chen, and Szolnoki (arXiv:2305.00253v1, 2023), equations (5) and (7), introduce precisely these two systems. Their Section 3 and detailed appendices locate the imaginary-eigenvalue thresholds and assert a supercritical Hopf on the basis of numerically evaluated **negative** first Lyapunov coefficients (linear: approximately \(-1.407\times10^{-8}\); sigmoidal: approximately \(-1.876\times10^{-8}\)). Those tiny computed signs do not establish nondegenerate Hopf criticality: the all-parameter exact result above gives zero. The present conclusion **does not** refute their numerical trajectory plots or establish what higher-order nonlinear terms do for asymmetric group sizes. It instead replaces the purported cubic Hopf classification with an exact degeneracy and exhibits a natural entire balanced-majority center family.

Earlier work on feedback-evolving games by Weitz et al. (2016) and Tilman, Plotkin, and Akçay (2020) concerns differently specified payoff and feedback systems and does not directly classify the cubic focus coefficient of the binomial collective-risk system. The exact binomial identity is an application-specific cancellation, not a claim that reversibility or the general first-focus formula is itself new.

## Limitations
The existence, uniqueness, amplitudes and stability of possible *isolated* periodic orbits **away from the exactly critical parameter** are not resolved. For unbalanced groups \(m\ne k\), the vanishing cubic coefficient does not by itself prove a center: higher-order focus quantities could be nonzero. The center assertion is local and concerns exact balanced-majority critical parameters; it is not a global statement about the entire risk-cooperation square. The result concerns deterministic infinite-population ordinary differential equations, not finite-population stochastic games. Specialist work outside inspected sources may contain related cancellations; independent audit has not been performed.

## References
1. L. Liu, X. Chen, A. Szolnoki, *Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game*, arXiv:2305.00253v1 (first public 2023-04-29), https://arxiv.org/html/2305.00253v1 ; published in eLife, DOI:10.7554/eLife.82954. Equations (5), (7); Sections 3.1–3.2 and their mathematical appendices.
2. J. S. Weitz et al., *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*, Proceedings of the National Academy of Sciences 113 (2016), 7518–7523, DOI:10.1073/pnas.1604096113.
3. A. R. Tilman, J. B. Plotkin, E. Akçay, *Evolutionary games with environmental feedbacks*, Nature Communications 11 (2020), article 915, DOI:10.1038/s41467-020-14531-6.
4. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, third edition, Springer (2004), normal-form and Lyapunov-coefficient conventions.
