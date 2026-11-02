# Universal inverse-exponential timing and hidden-drift factorization of rare Pólya-urn returns

## Finding

Conditioning a self-reinforcing Pólya urn walk on at least \(k\) returns reveals two linked universal phenomena: the time of its \(k\)-th return grows on the \(k^2\) scale with an **inverse-exponential** limit, while the hidden drift and additional future returns admit an asymptotically **independent exponential** representation.

Let the urn start with positive white and black masses \(a,b>0\), return the drawn ball and add one ball of its colour after each draw, and let \(S_0=0\) and \(S_n\) be the white-minus-black draw count. Write
\[
N=\#\{n\geq1:S_n=0\},\qquad
\Theta=\lim_{n\to\infty}\frac{a+\#\{j\leq n:\text{white at }j\}}{a+b+n},
\]
and set \(U=|2\Theta-1|\), \(\sigma=\operatorname{sgn}(2\Theta-1)\). In particular, \(N\) excludes the deterministic visit at time zero. For each integer \(k\geq1\), put \(E_k=\{N\geq k\}\) and \(R_k=N-k\). On \(E_k\), let \(\tau_k=\inf\{n\geq1:\#\{1\leq j\leq n:S_j=0\}=k\}\) be the epoch of the \(k\)-th return.

**Rare-return joint theorem.** For every fixed \(a,b>0\), as \(k\to\infty\), jointly under the conditional law given \(E_k\),
\[
\boxed{(\sigma,\ kU,\ UR_k,\ \tau_k/k^2)
\ \Longrightarrow\ (\Sigma,E_1,E_2,T).}
\]
Here \(\Sigma\) is a fair random sign, \(E_1,E_2\) are independent standard exponential variables, and \(\Sigma\) is independent of \((E_1,E_2,T)\). Conditional on \(E_1=x>0\), \(T\) is independent of \(E_2\) and has Laplace transform \(\exp(x-\sqrt{x^2+2s})\) at \(s\geq0\). Thus the extra-return mark is independent of the limiting scaled return epoch once the hidden drift has been accounted for.

The joint conditional limit is universal: it does not depend on \(a\) or \(b\). The signed posterior imbalance \(k(2\Theta-1)\mid E_k\) actually converges **in total variation** to a centered Laplace law with density \(e^{-|x|}/2\).

Consequently,
\[
\left(k(2\Theta-1),\ \frac Nk\right)\Bigm|E_k
\ \Longrightarrow\
\left(\Sigma E_1,\ 1+\frac{E_2}{E_1}\right).
\]
The second coordinate has the Pareto survival law \(\Pr(1+E_2/E_1\geq t)=1/t\), for \(t\geq1\). More precisely, conditioned on signed limiting imbalance \(Y=y\neq0\), the limiting probability of at least a factor \(t\) as many total returns is \(e^{-(t-1)|y|}\).

The return epoch has the simultaneous conditional limit
\[
\boxed{\frac{\tau_k}{k^2}\Bigm|E_k\ \Longrightarrow\ T,\qquad
\Pr(T\leq t)=\exp\!\left(-\frac1{2t}\right),\quad t>0.}
\]
Equivalently, \(T\stackrel{d}{=}1/(2E)\) for a standard exponential variable \(E\). Jointly with the latent drift \(kU\Longrightarrow E_1\), the limiting return epoch has the conditional Laplace transform
\[
\mathbb E[e^{-sT}\mid E_1=x]
=\exp\!\left(x-\sqrt{x^2+2s}\right),
\qquad x>0,\ s\geq0.
\]
The last expression is the first-passage-time transform for a unit level of Brownian motion with positive drift \(x\). The limiting future-return mark \(E_2\) is independent of \((\Sigma,E_1,T)\). All of these laws, including the \(k^2\) timing scale and its constant, hold for arbitrary fixed positive \(a,b\).

There is an exact finite-sample refinement in the balanced unit urn. When \(a=b=1\), for every integer \(k\geq1\), integer \(m\geq0\), and \(0\leq u\leq1\),
\[
\boxed{\Pr(U>u,\ R_k\geq m\mid E_k)
=\frac{k+1}{k+m+1}(1-u)^{k+m+1}.}
\]
This gives a direct finite-level joint prediction for the unobserved limiting drift and the additional future returns, not just a marginal tail estimate.

## Assumptions and scope

The masses \(a,b\) are arbitrary fixed positive real numbers and the reinforcement is one unit of the sampled colour at each draw. All return counts include every strictly positive time over an infinite walk and are finite almost surely. The event \(E_k\) is conditioning on **at least** \(k\) returns, not on exactly \(k\) returns and not on a large finite-time count. The limiting sign is defined almost surely because the beta-distributed \(\Theta\) is not exactly \(1/2\).

The fixed-mass restriction is essential to the stated universality: the theorem does not assert a limit uniform over triangular arrays in which \(a\) or \(b\) vary with \(k\). No corresponding theorem for nonlinear, fitness-biased, or dependent-reinforcement urns is claimed.

## Proof

**Step 1: The conditional geometric structure.** The Pólya–Eggenberger exchangeability representation gives
\[
\Theta\sim\operatorname{Beta}(a,b),\qquad
f_{a,b}(p)=\frac{p^{a-1}(1-p)^{b-1}}{B(a,b)},\quad0<p<1,
\]
and, conditional on \(\Theta=p\), the walk has independent increments \(+1\) with probability \(p\) and \(-1\) with probability \(1-p\). Here \(B(a,b)\) is the beta function. For the fixed-bias simple walk, a one-step first-return decomposition and gambler's-ruin hitting probabilities show that the probability of another return to zero is
\[
r(p)=2\min\{p,1-p\}=1-|2p-1|.
\]
The strong Markov property applies to the *conditional* fixed-bias walk. Therefore
\[
\Pr(N\geq k\mid\Theta=p)=r(p)^k,
\qquad
\Pr(R_k\geq m\mid\Theta=p,E_k)=r(p)^m.
\]
Since \(\Theta\) has no atom at \(1/2\), \(N<\infty\) almost surely. This does not require incorrectly applying a homogeneous Markov recurrence criterion to the unconditioned urn-position process.

**Step 2: Exact rare-event posterior and normalization.** Define
\[
H(u)=\frac12\left[f_{a,b}\!\left(\frac{1+u}{2}\right)+f_{a,b}\!\left(\frac{1-u}{2}\right)\right],\quad0<u<1.
\]
The variable \(U\) has density \(H\). Thus
\[
Q_k:=\Pr(E_k)=\int_0^1(1-u)^kH(u)\,du
=\frac{2^k}{B(a,b)}\left[
B_{1/2}(a+k,b)+B_{1/2}(b+k,a)\right],
\]
where \(B_z(s,t)=\int_0^z v^{s-1}(1-v)^{t-1}\,dv\). Because \(H\) is continuous at zero with \(H(0)=f_{a,b}(1/2)>0\), the change of variables \(v=ku\), with a split at a fixed small \(u\), yields
\[
kQ_k\longrightarrow f_{a,b}(1/2).
\]
Indeed, on a compact neighborhood of zero the density is bounded and the kernel is dominated by \(e^{-ku}\); on the complement its mass is exponentially small, even when the beta density is unbounded at an endpoint.

Conditioned on \(E_k\), the density of the signed random variable \(Y_k=k(2\Theta-1)\) is exactly
\[
g_k(y)=\frac{f_{a,b}((1+y/k)/2)}{2kQ_k}
\left(1-\frac{|y|}{k}\right)^k\mathbf1_{\{|y|<k\}}.
\]
For each fixed real \(y\), it tends to \(\tfrac12e^{-|y|}\). The functions \(g_k\) and their pointwise limit all integrate to one; Scheffé's lemma therefore proves convergence in total variation. It follows that \((\sigma,kU)\mid E_k\) converges to an independent fair sign and standard exponential magnitude. In particular, \(U\to0\) in probability under \(E_k\).

**Step 3: Asymptotically independent extra-return marks.** Conditional on \(\Theta\) and \(E_k\), \(R_k\) has a geometric distribution on \(\{0,1,\ldots\}\) with success parameter \(U\):
\[
\Pr(R_k=m\mid\Theta,E_k)=U(1-U)^m.
\]
For each \(z\geq0\) and \(u\downarrow0\),
\[
\Pr(uR_k>z\mid U=u,E_k)
=(1-u)^{\lfloor z/u\rfloor+1}\longrightarrow e^{-z}.
\]
The convergence is uniform for sufficiently small \(u\), with \(z\) fixed. Combining this with \(U\to0\) under \(E_k\), and testing bounded continuous functions, proves the asymptotic independence of \(UR_k\) from the two limiting variables \(\sigma\) and \(kU\). The joint limit is therefore \((\Sigma,E_1,E_2)\) as stated.

**Step 4: Ratio and conditional Pareto law.** The relation
\[
\frac Nk=1+\frac{UR_k}{kU}
\]
holds whenever \(U>0\). Since the limiting denominator is strictly positive almost surely, the continuous-mapping theorem proves the displayed bivariate limit. Conditional on \(E_1=x>0\), the limiting excess ratio has survival \(\Pr(E_2/x\geq t-1)=e^{-(t-1)x}\). Integrating over \(E_1\sim\operatorname{Exp}(1)\) gives \(1/t\) for \(t\geq1\).

**Step 5: The conditional return-epoch scaling.** Let \(\tau_1\) be the first strictly positive return time. Conditional on \(\Theta=p\), it has the *defective* probability-generating function
\[
F_p(z)=\mathbb E_p[z^{\tau_1};\tau_1<\infty]
=1-\sqrt{1-4p(1-p)z^2},\qquad 0\leq z\leq1.
\]
Indeed, the probability of first returning in \(2n\) steps is \(2C_{n-1}[p(1-p)]^n\), where \(C_j\) denotes the \(j\)-th Catalan number. Since \(F_p(1)=1-|2p-1|\), conditioning on the first \(k\) excursions returning gives the exact conditional transform
\[
\mathbb E[e^{-s\tau_k/k^2}\mid\Theta=p,E_k]
=\left[\frac{1-\sqrt{1-(1-U^2)e^{-2s/k^2}}}{1-U}\right]^k.
\]
For any fixed \(x\geq0\), substituting \(U=x/k\) and taking logarithms gives the limit
\[
\exp\!\left(x-\sqrt{x^2+2s}\right).
\]
The expansion is uniform for \(x\) in compact sets; the conditional posterior of \(kU\) is tight by Step 2. The bounded-transform argument therefore proves joint weak convergence of \((kU,\tau_k/k^2)\) to \((E_1,T)\), with the stated conditional transform. Conditional on the latent coin and on \(E_k\), the completed first \(k\) excursions and the future number of returns are independent by renewal at \(\tau_k\). Explicitly, for \(z\geq0\), their joint conditional Laplace transform is the displayed \(k\)-excursion factor times
\[
\mathbb E[e^{-zUR_k}\mid\Theta,E_k]
=\frac{U}{1-(1-U)e^{-zU}}\longrightarrow\frac1{1+z},
\]
uniformly when \(U=x/k\) with bounded positive \(x\). This factors in the joint limit, giving an \(\operatorname{Exp}(1)\) future-return mark independent of the limiting conditional time and drift; the limiting sign also factors because the conditional time law depends on \(U\), not on the sign of the bias. This establishes all four coordinates in the joint claim.

To identify the marginal timing law explicitly, the conditional transform corresponds to the hitting time of level one by Brownian motion of drift \(x\geq0\), whose density at \(t>0\) is
\[
q_x(t)=\frac{1}{\sqrt{2\pi t^3}}
\exp\!\left(-\frac{(1-xt)^2}{2t}\right).
\]
Mix over \(x\sim\operatorname{Exp}(1)\) and complete the square:
\[
\begin{aligned}
q(t)&=\int_0^\infty e^{-x}q_x(t)\,dx\\
&=\frac{e^{-1/(2t)}}{\sqrt{2\pi t^3}}
\int_0^\infty e^{-tx^2/2}\,dx
=\frac{e^{-1/(2t)}}{2t^2}.
\end{aligned}
\]
Integrating this density gives \(\Pr(T\leq t)=e^{-1/(2t)}\), including the precise scaling constant \(1/2\). No finite-horizon truncation appears in the conditioning.

**Step 6: Exact finite-level law for unit initial masses.** If \(a=b=1\), the latent \(\Theta\) is uniform, hence so is \(U\), and \(Q_k=\int_0^1(1-u)^kdu=1/(k+1)\). The conditional density of \(U\) given \(E_k\) equals \((k+1)(1-u)^k\). Weighting by the survival probability \((1-u)^m\) of \(R_k\) and integrating over \(u\in(v,1)\) yields
\[
\frac{\int_v^1(1-u)^{k+m}\,du}{Q_k}
=\frac{k+1}{k+m+1}(1-v)^{k+m+1}.
\]
No finite truncation is used in these infinite-walk identities.

## Verification

The self-contained Python file `checker.py`, using only the standard library, runs with `python3 checker.py` and reports `PASS: 2335 reproducible exact/numerical assertions`. It checks rational beta integrals, independent polynomial computations of return-event probabilities, exhaustive first-return enumeration, the exact finite-level posterior survival formula, and the Laplace transform of the scaled return epoch against two independent limiting integrals. It includes asymmetric urns. These finite computations and numerical quadratures are diagnostic only: the convergence statements rely on the analytic arguments above and cannot be proven by these checks.

## Relationship to prior work

Balaji and Mahmoud (2025) introduce and investigate the urn-driven random-walk viewpoint. Earlier, Jiang, Sun, Figueiredo, Ribeiro and Towsley (2014) already studied the equal-fitness Pólya urn competition (directly coinciding with the present return-count event for equal initial masses) in terms of **duration** (last tie) and **intensity** (number of ties); their Theorems 1 and 3 establish the sharp marginal tail orders and leading constants, and their equations for tie times provide extensive finite-time information. Consequently neither almost-sure eventual escape nor the \(1/k\) tail of return intensity, nor the finite last-tie law is claimed as new here. The **joint latent-drift, return-epoch and future-return conditional limit** for arbitrary fixed initial masses is the precise central claim. The inverse-exponential marginal is a consequence that is also potentially derivable in the balanced special case by asymptotic analysis of the older exact return-index kernels; it is not presented as independent novelty in that special case. The older formulas do not specify the joint posterior bias or its conditional coupling with future returns, and the general unequal-mass draw-count return event is distinct from a competition tie event. A separate simultaneous scaling argument is given here.

Antal, Ben-Naim and Krapivsky (2010) treat first-passage/tie events in a Pólya urn. Jiang, Figueiredo, Ribeiro and Towsley (2016) generalize the intensity and duration questions to nonlinear reinforcement and fitness effects. Mookerjee and Kostinski (2024) give biased simple-walk return and survival formulas, supplying the fixed-bias ingredient but not the rare-urn posterior problem. General exchangeability and geometric-mixture results are background ingredients rather than independent novelty claims.

## Limitations

The posterior is conditioned on an **infinite-horizon return count**, which is a mathematically well-defined statistic but not observable from a fixed finite segment. The theorem does not provide an estimation procedure from censored paths, convergence rates, or an unconditional scaling limit for the indexed return time. The Brownian hitting-time description is a conditional limit under rare-return selection, not a claim about ordinary urn-walk diffusive convergence. Its limits require fixed positive initial masses and linear Pólya reinforcement. The sign-and-exponential limit does not extend automatically to non-beta latent distributions without a positive continuous density at the balancing point. General random-environment geometric-mixture theory might subsume this particular asymptotic under a different formulation; no priority beyond the inspected material is asserted. Historical-priority checks are not independent mathematical certification.

## References

- Srinivasan Balaji and Hosam Mahmoud, *Urn-driven random walks*, arXiv:2504.14813, first publicly posted 2025-04-21, https://arxiv.org/abs/2504.14813.
- Bo Jiang, Liyuan Sun, Daniel R. Figueiredo, Bruno Ribeiro and Don Towsley, *On the duration and intensity of cumulative advantage competitions*, arXiv:1402.4536, first posted 2014-02-19, https://arxiv.org/abs/1402.4536.
- Tibor Antal, E. Ben-Naim and P. L. Krapivsky, *First Passage Properties of the Polya Urn Process*, arXiv:1005.0867, first posted 2010-05-05, https://arxiv.org/abs/1005.0867.
- Bo Jiang, Daniel R. Figueiredo, Bruno Ribeiro and Don Towsley, *On the Duration and Intensity of Competitions in Nonlinear Pólya Urn Processes with Fitness*, arXiv:1604.02097, first posted 2016-04-06, https://arxiv.org/abs/1604.02097.
- Debendro Mookerjee and Sarah Kostinski, *Exact closed-form recurrence probabilities for biased random walks at any step number*, arXiv:2412.17994, first posted 2024-12-23, https://arxiv.org/abs/2412.17994.
