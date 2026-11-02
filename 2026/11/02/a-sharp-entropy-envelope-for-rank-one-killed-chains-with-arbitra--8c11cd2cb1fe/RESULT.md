# A sharp entropy envelope for rank-one killed chains with arbitrary memory laws

## Finding

Let \(S\) be a finite state space with at least two elements, let \(\pi\) be a strictly positive probability distribution on \(S\), and let \(k:S\to(0,1]\). Set \(\sigma(s,t)=k(s)\pi(t)\), a strictly positive substochastic transition matrix. Given any probability law \(\tau\) on the nonnegative integers, let \(K_\tau\) be the associated preferential-relocation killed operator defined below and let \(r(\tau)\) be its spectral radius. Put

\[
m(q)=\sum_{s\in S}q(s)k(s),\qquad D(q\|\pi)=\sum_{s\in S}q(s)\log\frac{q(s)}{\pi(s)},\qquad B=\max_{q\in\mathcal P(S)}m(q)e^{-D(q\|\pi)}.
\]

Let \(q_*\) be the unique maximizer, let \(k_{\min}=\min_s k(s)>0\), and write \(v_*=\operatorname{Var}_{q_*}(k)\). **For every probability law \(\tau\), without any tail or moment condition,**

\[
\boxed{B\exp\left(-\frac{v_*}{2k_{\min}^2}\sum_{i\ge0}\tau(i)^2\right)\le r(\tau)\le B.}
\]

Consequently, for every family \((\tau_\varepsilon)\) satisfying \(\sup_i\tau_\varepsilon(i)\to0\),

\[
\boxed{r(\tau_\varepsilon)\longrightarrow B.}
\]

This solves the proposed all-relocation-law upper inequality for the rank-one subclass and identifies the exact dispersed-relocation limit, including for heavy-tailed laws. The constant \(B\) equals the Perron-tilt expression in Question 5.3 of the source paper:

\[
B=\sup_{a:S\to(0,\infty)}r_a\exp\bigl(-\rho_a(\log a)\bigr),
\]

where \(r_a\) and \(\rho_a\) are the Perron root and normalized left Perron vector of the column-tilted matrix \(\sigma_a(s,t)=\sigma(s,t)a(t)\).

If \(k\) is nonconstant, \(B>\sum_s\pi(s)k(s)\). The single-lag laws \(\tau=\delta_L\) satisfy exactly \(r(\delta_L)=\sum_s\pi(s)k(s)\) for every finite \(L\); simply moving relocation mass to increasingly remote *single* generations does not attain \(B\). Thus spreading the mass, rather than merely moving it outward, is the essential condition.

## Assumptions and scope

All statements concern a finite \(S\), fully supported \(\pi\), strictly positive survival probabilities \(k(s)\le1\), and arbitrary fixed probability laws on \(\mathbb N_0\). No finite-mean, exponential-tail, or nonzero-at-the-origin assumption is imposed. The space of histories is \(\Omega=S^{\mathbb N_0}\) with its product topology. For \(\mathbf s=(s_0,s_1,\ldots)\), let \(t\mathbf s=(t,s_0,s_1,\ldots)\) and define the positive Feller operator on \(C(\Omega)\) by

\[
(K_\tau f)(\mathbf s)=\left(\sum_{i=0}^\infty\tau(i)k(s_i)\right)\sum_{t\in S}\pi(t)f(t\mathbf s).
\]

The sum defining \(K_\tau\) is uniformly convergent, and \(r(\tau)=\lim_{n\to\infty}\|K_\tau^n\|_\infty^{1/n}\) exists by the spectral-radius formula. For strictly positive operators, \(\|K_\tau^n\|_\infty=\|K_\tau^n\mathbf1\|_\infty\).

The maximizer \(q_*\) has full support and is the unique solution of

\[
q_*(s)=\frac{\pi(s)\exp(k(s)/m_*)}{\sum_t\pi(t)\exp(k(t)/m_*)},\qquad m_*=\sum_s q_*(s)k(s).
\]

For nonconstant \(k\), the fixed-point equation for \(m_*\) has a unique solution in the open interval between \(\min_s k(s)\) and \(\max_s k(s)\). For constant \(k\), the theorem holds with \(v_*=0\) and \(B=k(s)\).

## Proof

**1. Independent-mark representation.** Fix a deterministic prehistory \(\mathbf s=(s_0,s_1,\ldots)\). Take \(X_1,\ldots,X_n\) independently with law \(\pi\), and set \(X_{-i}=s_i\) for every \(i\ge0\). Define

\[
A_j=\sum_{i\ge0}\tau(i)k(X_{j-1-i}),\qquad 1\le j\le n.
\]

Iterating the rank-one operator gives the exact identity

\[
(K_\tau^n\mathbf1)(\mathbf s)=\mathbb E_{\pi^{\otimes n}}\prod_{j=1}^n A_j.
\]

Every factor lies in \([k_{\min},k_{\max}]\), so all logarithms below are bounded.

**2. Uniform entropy upper bound.** Let \(Q\) be any probability law on \(S^n\), with coordinate marginals \(q_1,\ldots,q_n\) and their mean \(\bar q=n^{-1}\sum_jq_j\). The finite Gibbs variational identity and the entropy chain rule give

\[
\log(K_\tau^n\mathbf1)(\mathbf s)=\sup_Q\left\{\sum_{j=1}^n\mathbb E_Q\log A_j-D(Q\|\pi^{\otimes n})\right\},
\]

\[
D(Q\|\pi^{\otimes n})\ge\sum_{j=1}^nD(q_j\|\pi)\ge nD(\bar q\|\pi).
\]

Let \(T\) have law \(\tau\) and define

\[
b_n=\frac1n\sum_{j=1}^n\Pr(T\ge j-1)=\frac{\mathbb E\min(T+1,n)}n.
\]

Since \(\Pr(T\ge j)\to0\), Cesàro summation gives \(b_n\to0\) without requiring \(\mathbb ET<\infty\). In \(\sum_{j=1}^n\mathbb E_Q A_j\), the total coefficient of each newly generated \(X_t\) is at most one, while the combined weight of all prehistory positions is \(nb_n\). Therefore

\[
\frac1n\sum_{j=1}^n\mathbb E_Q A_j\le m(\bar q)+k_{\max}b_n.
\]

Two applications of Jensen's inequality yield

\[
\frac1n\sum_{j=1}^n\mathbb E_Q\log A_j\le\log\left(m(\bar q)+k_{\max}b_n\right).
\]

Combining these inequalities gives a bound uniform in the starting history:

\[
\|K_\tau^n\|_\infty^{1/n}\le\max_{q\in\mathcal P(S)}\left(m(q)+k_{\max}b_n\right)e^{-D(q\|\pi)}.
\]

The simplex is compact, its displayed objective is continuous, and \(b_n\to0\), so taking \(n\to\infty\) proves \(r(\tau)\le B\).

**3. Independent-tilt lower bound.** Fix any probability vector \(q\) on \(S\) and use the admissible product law \(Q=q^{\otimes n}\) in the same Gibbs variational formula. Under an independent two-sided iid \(q\)-sequence \((\xi_j)_{j\in\mathbb Z}\), set

\[
W_{\tau,q}=\sum_{i\ge0}\tau(i)k(\xi_{-i}).
\]

Replace the deterministic prehistory in \(A_j\) by the stationary iid past. The resulting expected logarithm equals \(\mathbb E_q\log W_{\tau,q}\) at every \(j\). Because logarithm is \(1/k_{\min}\)-Lipschitz on \([k_{\min},k_{\max}]\), the replacement changes \(\mathbb E\log A_j\) by at most

\[
\frac{k_{\max}-k_{\min}}{k_{\min}}\Pr(T\ge j-1).
\]

The average difference vanishes by \(b_n\to0\). Thus for every deterministic prehistory,

\[
\liminf_{n\to\infty}\frac1n\log(K_\tau^n\mathbf1)(\mathbf s)
\ge\mathbb E_q\log W_{\tau,q}-D(q\|\pi),
\]

and in particular

\[
r(\tau)\ge\exp\left(\mathbb E_q\log W_{\tau,q}-D(q\|\pi)\right).
\]

**4. Collision-probability stability and dispersion.** By independence,

\[
\mathbb E_q W_{\tau,q}=m(q),\qquad
\operatorname{Var}_q(W_{\tau,q})=\operatorname{Var}_q(k)\sum_i\tau(i)^2.
\]

Taylor's theorem and the uniform lower bound on survival imply, for all \(x,y\in[k_{\min},k_{\max}]\),

\[
\log x\ge\log y+\frac{x-y}{y}-\frac{(x-y)^2}{2k_{\min}^2}.
\]

Apply this with \(x=W_{\tau,q}\), \(y=m(q)\) and take expectations to obtain

\[
\mathbb E_q\log W_{\tau,q}\ge
\log m(q)-\frac{\operatorname{Var}_q(k)}{2k_{\min}^2}\sum_i\tau(i)^2.
\]

Choosing \(q=q_*\) proves the stated lower bound. If \(\sup_i\tau_\varepsilon(i)\to0\), then \(\sum_i\tau_\varepsilon(i)^2\le\sup_i\tau_\varepsilon(i)\to0\), and squeezing with the universal upper bound proves the exact dispersed-relocation limit.

**5. Optimizer, comparison, and concentrated-memory boundary.** The function \(q\mapsto\log m(q)-D(q\|\pi)\) is strictly concave on the probability simplex and attains its unique maximum in its interior. Lagrange multipliers give the formula for \(q_*\). The map sending a positive \(m\) to the mean of \(k\) under the tilt proportional to \(\pi(s)e^{k(s)/m}\) is strictly decreasing when \(k\) is nonconstant, so its intersection with the increasing identity map is unique. The benchmark value is \(r_0=m(\pi)\); the directional derivative of \(\log m-D\) at \(\pi\) toward higher-survival states is positive if \(k\) varies, hence \(B>r_0\).

For a point mass \(\tau=\delta_L\), the first \(L+1\) survival factors in a finite path depend on the deterministic prehistory, and all later factors depend on distinct iid generated coordinates. Therefore, for \(n\ge L+1\), the expectation in step 1 equals \(\bigl(\prod_{i=0}^{L}k(s_i)\bigr)r_0^{n-L-1}\). Its \(n\)-th root tends to \(r_0\) uniformly over initial histories, proving \(r(\delta_L)=r_0\).

Finally, for \(\sigma_a(s,t)=k(s)\pi(t)a(t)\), normalize \(a\) so that \(\sum_s\pi(s)a(s)=1\). The normalized left Perron vector is \(\rho_a(s)=\pi(s)a(s)\) and the Perron root is \(r_a=\sum_s\rho_a(s)k(s)=m(\rho_a)\). Also \(\rho_a(\log a)=D(\rho_a\|\pi)\). The change of variables \(q=\rho_a\) identifies the published proposed constant with \(B\), completing the proof.

## Verification

A standalone Python checker, `check.py`, verifies the rank-one optimization formula, compares spectral radii of finite-memory transfer matrices with both analytical bounds over 90 independently seeded two-state cases, and checks exact rational equality of path enumeration and transfer-operator iteration in 3 families over all initial histories through horizon 6. Its recorded output is included in `check_output.txt`. The checker uses only Python's standard library. These are finite consistency tests; the inequalities for all laws and the infinite-memory limit follow from the analytical proof above.

For \(S=\{0,1\}\), \(\pi=(1/2,1/2)\), and \(k=(1,1/5)\), the benchmark is \(0.6\), while the entropy envelope is

\[
B\approx0.7024504925079701,\qquad q_*\approx(0.73420265,0.26579735).
\]

Uniform lag laws on one, two, four, and eight consecutive lags give finite-memory spectral radii approximately \(0.600000000000\), \(0.660555127546\), \(0.683995611200\), and \(0.693716614260\), consistent with convergence toward \(B\).

## Relationship to prior work

Bertoin and Minchev, *Preferential relocations enhance survival for Markov chains with killing*, arXiv:2605.29030v1, establish that relocation can increase persistence and in Corollary 5.2 prove a dispersed-law lower bound. Their discussion immediately after Figure 2 explicitly asks whether the same Perron-tilt expression is a universal upper bound, even for laws with exponential tails. The result here answers that question for strictly positive rank-one substochastic matrices, and does so for **every** probability law on nonnegative lags, including heavy tails. It does not resolve their general-matrix question.

Bertoin, *On a population model with memory*, arXiv:2501.00306v1, studies fixed-law ancestral recollection and proves a lower comparison to the benchmark; its displayed upper estimate in Section 3 is not the sharp entropy envelope obtained here. Bertoin, *Another solvable population dynamic with uniform ancestral memory*, arXiv:2608.24356v1, is a closely related rank-one model, but samples an ancestor uniformly from the entire *current finite lineage* at each generation, with a sampling law depending on generation. Its explicit Malthusian constant does not concern one fixed lag distribution \(\tau\), the universal bound here, or the small-maximal-atom limit of a family of stationary-lag operators. Standard Gibbs and relative-entropy inequalities are proof ingredients, not themselves a statement of this sharp spectral result.

## Limitations

The theorem applies only to rank-one transition matrices with strictly positive entries and survival probabilities bounded below by a positive constant. It does not prove the proposed inequality for arbitrary irreducible substochastic matrices, does not claim an exact spectral radius for each finite law \(\tau\), and does not make a claim about individual pointwise long-time survival asymptotics under arbitrary non-Hölder memories. The quantitative collision bound need not have the optimal prefactor. Historical priority outside the inspected accessible literature remains open to independent examination.

## References

1. Jean Bertoin and Martin Minchev, *Preferential relocations enhance survival for Markov chains with killing*, arXiv:2605.29030v1, 27 May 2026. https://arxiv.org/html/2605.29030v1
2. Jean Bertoin, *On a population model with memory*, arXiv:2501.00306v1, 31 December 2024. https://arxiv.org/html/2501.00306v1
3. Jean Bertoin, *Another solvable population dynamic with uniform ancestral memory*, arXiv:2608.24356v1, 25 August 2026. https://arxiv.org/abs/2608.24356
