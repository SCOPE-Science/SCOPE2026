# Exact winner basins and inoculum probabilities in multistrain simplicial SIS dynamics

## Finding

Consider \(m\ge 2\) mutually exclusive SIS strains sharing a well-mixed susceptible class, with identical recovery rate and pairwise transmission rate but strain-specific positive triangle-reinforcement rates. When the common pairwise process is supercritical, the epidemic that wins from any strictly positive initial state is determined *exactly* by the largest initial reinforcement-weighted prevalence. If there are several joint maxima, precisely those strains coexist in the limit. This gives explicit polyhedral basin boundaries, endemic fractions, and extinction exponents for any number of strains; it also gives exact winner probabilities for uniformly sampled initial strain mixtures.

Write \(T=\sum_{i=1}^{m}x_i\), \(s=1-T\), with \(x_i\) the fraction infected by strain \(i\). The system is
\[
\dot x_i=x_i\left[-\delta+s(\beta+\gamma_i x_i)\right],\quad i=1,\ldots,m.
\]
Assume \(\beta>\delta>0\), every \(\gamma_i>0\), and every \(x_i(0)>0\) with \(T(0)<1\). Let
\[
A_i=\gamma_i x_i(0),\qquad M=\max_i A_i,\qquad S=\{i:A_i=M\},\qquad c_S=\sum_{i\in S}\frac1{\gamma_i}.
\]
Define
\[
K_S=\frac{1-c_S\beta+\sqrt{(1-c_S\beta)^2+4c_S(\beta-\delta)}}2.
\]
Then \(0<K_S<1\) and for *every* such initial condition,
\[
\lim_{t\to\infty}x_i(t)=
\begin{cases}
K_S/(c_S\gamma_i),&i\in S,\\
0,&i\notin S.
\end{cases}
\]
In particular, a unique maximal \(\gamma_i x_i(0)\) gives the unique surviving strain. Every strict losing strain \(j\notin S\), measured relative to any \(k\in S\), obeys the exact logarithmic elimination law
\[
\lim_{t\to\infty}\frac1t\log\frac{\gamma_j x_j(t)}{\gamma_k x_k(t)}
=-\frac{(1-K_S)K_S}{c_S}.
\]
The nonempty-support equilibria with more than one active strain have exactly \(\lvert S\rvert-1\) unstable eigenvalues within that support; single-strain equilibria are locally asymptotically stable. The basin boundaries in the strictly positive initial simplex are exactly the portions of \(\gamma_i x_i(0)=\gamma_j x_j(0)\) on which this common value is maximal.

For a fixed initial total infected fraction \(0<T(0)<1\), suppose the strain composition is uniform on the \((m-1)\)-simplex (Dirichlet distribution with all concentration parameters equal to one). A unique winner then occurs almost surely, independently of \(T(0)\), \(\beta\), and \(\delta\). Writing \(\lambda_i=1/\gamma_i\), its probability is
\[
\Pr(i\text{ wins})=\sum_{B\subseteq\{1,\ldots,m\}\setminus\{i\}}(-1)^{|B|}
\frac{\lambda_i}{\lambda_i+\sum_{j\in B}\lambda_j}.
\]
For example, at \((\gamma_1,\gamma_2,\gamma_3)=(8,2,1)\), the exact probability vector is
\[
(448/585,\ 34/195,\ 7/117).
\]

## Assumptions and scope

The equations describe a **deterministic, homogeneous mean-field extension** to \(m\) mutually exclusive strains of the two-strain first- and second-order incidence equations in Li et al. Here \(\beta\) denotes their common *effective* mean-field pairwise transmission coefficient, \(\delta\) their common effective recovery rate, and \(\gamma_i\) the corresponding effective second-order coefficient. No claim is made for heterogeneous pairwise coefficients, unequal recovery rates, discrete network realizations, finite-population Markov paths, or \(\beta\le\delta\). Initial coordinates are strictly positive; zero coordinates restrict the same argument to their initially occupied support.

The positive state space \(\{x_i>0,\ \sum_i x_i<1\}\) is forward-invariant: coordinate derivatives vanish on \(x_i=0\), and at \(s=0\), \(\dot s=\delta T>0\). As all trajectories remain in the compact closed simplex, they exist for all forward time.

## Proof

**Step 1: Non-extinction and uniformly positive susceptible fraction.** Summing the equations gives
\[
\dot T=T[-\delta+\beta(1-T)]+s\sum_i\gamma_i x_i^2
\ge T[(\beta-\delta)-\beta T].
\]
The scalar logistic comparison shows
\(\liminf_{t\to\infty}T(t)\ge1-\delta/\beta>0\).
Set \(\gamma_{\max}=\max_i\gamma_i\). The susceptible equation satisfies
\[
\dot s=\delta(1-s)-\beta sT-s\sum_i\gamma_i x_i^2
\ge\delta-(\delta+\beta+\gamma_{\max})s.
\]
Hence \(\liminf_{t\to\infty}s(t)\ge\delta/(\delta+\beta+\gamma_{\max})>0\). Both comparisons use only the stated hypotheses and positivity.

**Step 2: Exact winner ordering.** Set \(a_i(t)=\gamma_i x_i(t)\). Direct differentiation yields
\[
\frac{d}{dt}(a_i-a_j)=(a_i-a_j)[-\delta+s(\beta+a_i+a_j)]
\]
and
\[
\frac{d}{dt}\log\frac{a_j}{a_k}=s(a_j-a_k).
\]
Therefore equality and strict ordering among the \(a_i\) are invariant. For every \(k\in S\) and \(j\notin S\), \(r_j(t)=a_j(t)/a_k(t)\) decreases and is bounded above by \(r_j(0)<1\). If \(C=\sum_i1/\gamma_i\), then \(T\le Ca_k\) because \(a_k\) is always a maximum. Step 1 therefore bounds \(s a_k\) below by a positive constant for all sufficiently large \(t\). Consequently
\[
\frac{d}{dt}\log r_j=-sa_k(1-r_j)
\le-\eta(1-r_j(0))<0
\]
for some fixed \(\eta>0\) and all sufficiently large \(t\). Every \(r_j\), and therefore every losing \(x_j\), converges to zero exponentially.

**Step 3: Limit on the surviving face.** For all \(i,k\in S\), \(a_i(t)=a_k(t)\) exactly. Set \(U=\sum_{i\in S}x_i\) and \(V=\sum_{j\notin S}x_j\). Then \(a_i=U/c_S\) on \(S\), \(V(t)\to0\), and
\[
\dot U=U\left[-\delta+(1-U-V)\left(\beta+\frac{U}{c_S}\right)\right].
\]
Since \(U=T-V\) and Step 1 bounds \(T\) from zero, \(U\) has a positive eventual lower bound. The limiting scalar bracket
\(f(U)=-\delta+(1-U)(\beta+U/c_S)\)
is strictly positive at zero, strictly negative at one, and has exactly one root in \((0,1)\): its zero equation is a quadratic with negative constant term, hence one positive and one negative root. Solving gives \(K_S\). For every sufficiently small \(\varepsilon>0\), the bracket for the actual \(U\) is positive on the interval below \(K_S-\varepsilon\) and negative above \(K_S+\varepsilon\) for all sufficiently large times because \(V\to0\). Standard one-dimensional inward-pointing barriers force \(U(t)\to K_S\). This proves the limit formula and excludes nonstationary omega-limit sets for every interior initial condition.

**Step 4: Linear stability of the tied limit.** At the fixed point on support \(S\), write \(a=K_S/c_S\), \(s=1-K_S\), and \(q=|S|\). Differentiating the right-hand side on the active coordinates gives
\[
J_S=asI_q-a(\beta+a)\operatorname{diag}(1/\gamma_i)_{i\in S}\mathbf1\mathbf1^{\mathsf T}.
\]
Its spectrum is \(as>0\) with multiplicity \(q-1\), together with \(a[1-c_S\beta-2K_S]<0\). Each absent strain contributes an eigenvalue \(-sa<0\). Thus a coexistence equilibrium with multiple active strains is unstable in the active face, whereas every single-strain equilibrium is a hyperbolic sink in the full epidemic simplex. This matches, and does not replace, the global tie classification above.

**Step 5: Exact disappearance exponent.** In the second identity in Step 2, \(a_k(t)\to K_S/c_S\), \(s(t)\to1-K_S\), and \(a_j(t)\to0\) for \(j\notin S\). Therefore the derivative of \(\log(a_j/a_k)\) converges to \(-(1-K_S)K_S/c_S\). Integration followed by division by \(t\) proves the claimed limit. No finite simulation substitutes for this infinite-time step.

**Step 6: Uniformly mixed seeds.** The Dirichlet composition of all-ones parameters can be written \(x_i(0)=T(0)E_i/\sum_j E_j\), where the \(E_i\) are independent unit-rate exponential variables. Maximizing \(\gamma_i x_i(0)\) is therefore equivalent to maximizing \(\gamma_i E_i\), independent exponential variables having rates \(\lambda_i=1/\gamma_i\). Conditioning on the value of \(\gamma_i E_i\) and applying inclusion-exclusion gives the stated formula:
\[
\Pr(i\text{ wins})=\int_0^\infty\lambda_i e^{-\lambda_i u}
\prod_{j\ne i}(1-e^{-\lambda_j u})\,du.
\]
The integral yields the finite subset sum; ties have probability zero. Rational arithmetic gives the three stated example probabilities, which sum to one.

## Verification

The accompanying standalone `verify.py` independently implements the ODE's vector field, exact rational pairwise sign and logarithmic-ratio identities, the surviving-face Jacobian rank-one identity, finite exact exponential inclusion-exclusion calculations, and fourth-order Runge--Kutta integration for a range of initial conditions with two to six competing strains. It also checks an exact-tie coexistence case and a case where the initially least prevalent strain defeats a more numerous rival. Execution on the packaged source produces 12,600 exact pair identities, 4,424 additional exact Jacobian or winning-probability identities, and 67 numerical limiting-state checks. The proof, not the finite checks, covers arbitrary \(m\) and infinite time.

## Relationship to prior work

Li et al. [1] formulate and study two competing simplicial SIS epidemics and their parameter-space phase diagram. Their equations (3)--(4) yield this model when rates are specialized to common \(\beta,\delta\); the new theorem additionally considers \(m\ge2\), gives *every* strictly positive initial-condition basin, exact coexistence boundaries, convergence and loss rates, and the random-seeding winner law. It neither revises nor challenges their different-rate phase diagram. Gracy et al. [2] analyze networked two-virus higher-order transmission with multi-node rate arrays and typical convergence, not this explicit homogeneous multi-strain initial-value partition. Cisneros-Velarde and Bullo [3] concern multi-group spread of a single contagion rather than mutually exclusive strains.

There is an important **equivalent mathematical formulation**: writing \(p_i=x_i/T\) gives
\[
\dot p_i=sT\,p_i\left(\gamma_i p_i-\sum_j\gamma_j p_j^2\right).
\]
Thus the composition dynamics are a positive time change of a **classical diagonal-payoff replicator equation**. Classical replicator convergence and potential-game methods are pertinent prior theory. The point here is the complete explicit strain-seeding basin formula and the epidemic-specific endemic size, physical-time elimination exponent, and Dirichlet seeding law. An unlocated prior derivation for diagonal coordination games might imply the composition part of the result; this remains an originality risk, not proof that the composition theorem was unknown.

## Limitations

The result requires identical positive recovery and pairwise transmission parameters across strains and a *supercritical pairwise regime* \(\beta>\delta\). If the pairwise reproduction rate is subcritical, sufficiently small initial seeds can go extinct and the winner rule no longer applies generally. It concerns deterministic infinite-population mean-field trajectories, not the probability of eventual fixation or extinction in a finite stochastic epidemic. The probability formula assumes an explicitly uniform Dirichlet distribution of initial strain proportions; other seeding laws lead to other probabilities. The simplest composition component is mathematically conjugate to well-known replicator dynamics; general replicator literature might already imply a close equivalent. No independent review has been conducted.

## References

[1] W. Li, X. Xue, L. Pan, T. Lin, and W. Wang, "Competing spreading dynamics in simplicial complex," arXiv:2105.08234v1 (first public 2021-05-18), subsequently *Applied Mathematics and Computation* 412 (2022), 126595. https://arxiv.org/abs/2105.08234

[2] S. Gracy, B. D. O. Anderson, M. Ye, and C. A. Uribe, "Competitive Networked Bivirus SIS Spread over Hypergraphs," arXiv:2309.14230v1 (2023). https://arxiv.org/abs/2309.14230

[3] P. Cisneros-Velarde and F. Bullo, "Multi-group SIS Epidemics with Simplicial and Higher-Order Interactions," arXiv:2005.11404 (2020). https://arxiv.org/abs/2005.11404
