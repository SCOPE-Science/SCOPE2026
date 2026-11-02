# Exact sparse-observation memory in symmetric exclusion: a uniform-hub criterion and charge crossover

## Finding

Let \(G=(V,E)\) be a finite connected undirected graph, \(L=|V|\ge 2\), with symmetric edge-exchange conductances \(c_{xy}=c_{yx}\ge 0\) (strictly positive exactly on its edges). In the stationary symmetric simple exclusion process (SEP), occupation variables \(\eta_s(y)\in\{0,1\}\) exchange across each edge \(\{x,y\}\) at rate \(c_{xy}\). Fix a vertex \(x\) and a sampling separation \(t>0\), and set
\[
\mathcal I_x(t)=I\!\left(\eta_0(x):\eta_{2t}(x)\mid\eta_t(x)\right),
\]
using natural logarithms (nats) and **only one intermediate observation**.

Define the single-particle symmetric random-walk generator \(Q\) by \(Q_{xy}=c_{xy}\) for \(y\ne x\) and \(Q_{xx}=-\sum_{y\ne x}c_{xy}\), and its return probability \(p_s=(e^{sQ})_{xx}\). Set
\[
\begin{aligned}
\mathcal F(a,b)=\frac14\bigg[& (1+2a+b)\log\frac{1+2a+b}{(1+a)^2}
 +(1-2a+b)\log\frac{1-2a+b}{(1-a)^2}\\
&+2(1-b)\log\frac{1-b}{1-a^2}\bigg].
\end{aligned}
\]
For stationary independent Bernoulli occupation of density \(1/2\) (the **grand-canonical ensemble**), the exact formula and strict memory criterion are
\[
\boxed{\mathcal I_x^{\rm G}(t)=\mathcal F(p_t,p_{2t})>0\qquad(t>0).}
\]
For even \(L\) and the stationary uniform ensemble with exactly \(L/2\) particles (the **canonical ensemble**), put \(a_s=(Lp_s-1)/(L-1)\). Then
\[
\boxed{\mathcal I_x^{\rm C}(t)=\mathcal F(a_t,a_{2t}),\qquad
\mathcal I_x^{\rm C}(t)=0\iff c_{xy}=c>0\ \text{for all }y\ne x.}
\]
In other words, a fixed-charge local occupation is (exactly) a two-state Markov process precisely at a uniformly weighted *universal hub*. Otherwise every positive sampling lag has strictly positive three-observation CMI. The equivalence includes arbitrary non-hub edges and does not require the whole graph to be complete.

For the nearest-neighbor ring \(C_L\), even \(L\ge4\), take rate \(D>0\) on each of the \(L\) bonds and define
\[
\lambda_k=2D\left(1-\cos\frac{2\pi k}{L}\right),\qquad
p_s=\frac1L\sum_{k=0}^{L-1}e^{-\lambda_ks},\qquad
\Theta_D(u)=\sum_{m\in\mathbb Z}e^{-4\pi^2Du m^2}.
\]
Then the **exact hydrodynamic crossover**, at every fixed \(u>0\), is
\[
\boxed{\lim_{L\to\infty\atop L\ \rm even}L^2\mathcal I^{\rm G}(uL^2)=\tfrac12\Theta_D(2u)^2,
\qquad \lim_{L\to\infty\atop L\ \rm even}L^2\mathcal I^{\rm C}(uL^2)=\tfrac12[\Theta_D(2u)-1]^2.}
\]
For every fixed even \(L\ge4\), the respective long-lag asymptotics are
\[
\boxed{\lim_{t\to\infty}\mathcal I^{\rm G}(t)=\mathcal F(1/L,1/L)>0,\qquad
\mathcal I^{\rm C}(t)\sim\frac{2(L-3)^2}{(L-1)^4}\,e^{-4\lambda_1t}.}
\]
The grand-canonical plateau is \(1/(2L^2)+O(L^{-3})\) as \(L\to\infty\). On the infinite lattice \(\mathbb Z\), with independent Bernoulli initial law and rate \(D\) on nearest-neighbor bonds,
\[
\boxed{\mathcal I_{\mathbb Z}(t)=\mathcal F\!\left(e^{-2Dt}I_0(2Dt),\ e^{-4Dt}I_0(4Dt)\right)
\sim\frac{1}{16\pi Dt}\qquad(t\to\infty),}
\]
where \(I_0\) is the modified Bessel function of the first kind.

## Assumptions and scope

All finite graphs are connected, with a symmetric conductance on each edge, and \(L\ge2\). The canonical results require even \(L\) and exactly \(L/2\) occupied sites; the grand-canonical results use independently occupied sites with probability \(1/2\). The generator acts on functions of configurations by
\[
(\mathcal L f)(\eta)=\sum_{\{i,j\}\in E}c_{ij}[f(\eta^{ij})-f(\eta)],
\]
where \(\eta^{ij}\) swaps the two occupations. All statements about strict positivity apply to \(t>0\), not the coincident-time limit \(t=0\). No assumption of a single Markovian local trace is made. All information quantities use natural logarithms.

## Proof

**1. Exact two-time law from one-particle duality.** The SEP generator satisfies
\[
\mathcal L\eta(x)=\sum_yQ_{xy}\eta(y).
\]
Consequently, \(\mathbb E[\eta_s(x)\mid\eta_0]=\sum_y(e^{sQ})_{xy}\eta_0(y)\). For grand-canonical half filling, independence at time zero gives \(\operatorname{Cov}(\eta_0(x),\eta_s(x))=p_s/4\). For canonical half filling, the one-site variance is \(1/4\), and the covariance of different initial sites is \(-1/[4(L-1)]\). Thus the corresponding covariance is \((Lp_s-1)/[4(L-1)]\).

Write \(Y_j=2\eta_{jt}(x)-1\in\{-1,1\}\) for \(j=0,1,2\). Each ensemble is stationary and invariant under global particle-hole complementation, so \(\mathbb E Y_j=\mathbb E(Y_0Y_1Y_2)=0\). The pair moments are \(\mathbb E(Y_0Y_1)=\mathbb E(Y_1Y_2)=a\) and \(\mathbb E(Y_0Y_2)=b\), with \((a,b)=(p_t,p_{2t})\) or \((a_t,a_{2t})\), respectively. The Walsh expansion on three binary variables therefore determines their **entire** joint law:
\[
\Pr(Y_0=r,Y_1=s,Y_2=w)=\frac{1+a(rs+sw)+b\,rw}{8},\quad r,s,w\in\{\pm1\}.
\]
Conditioning on \(Y_1=s\) and replacing the endpoints by \((r',w')=(rs,ws)\) gives probabilities \((1+2a+b)/4\), \((1-b)/4\), \((1-b)/4\), \((1-2a+b)/4\). The endpoints both have marginal probability \((1+a)/2\) of \(+1\); substituting into the definition of conditional mutual information yields \(\mathcal F(a,b)\) exactly. Conditional independence of these two binary endpoints is equivalent to \(b=a^2\).

**2. Strict positivity and the universal-hub criterion.** Since \(Q\) is a real symmetric generator, the spectral resolution of \(p_t\) at \(x\) has the form
\[
p_t=\sum_{j=0}^{L-1}w_j e^{-\mu_jt},\qquad
w_j\ge0,\quad\sum_jw_j=1,\quad w_{\rm zero}=1/L,
\]
where the \(\mu_j\ge0\) are Laplacian eigenvalues. In the grand-canonical case,
\[
p_{2t}-p_t^2=\operatorname{Var}_{w}(e^{-\mu_jt})>0,
\]
because a connected graph has positive spectral weight at the zero eigenvalue and at least one positive eigenvalue. Thus the grand-canonical information is strictly positive for every \(t>0\).

For the canonical ensemble, the normalized spectral weights on positive eigenvalues are \(\widehat w_j=Lw_j/(L-1)\), and \(a_t=\sum_{\mu_j>0}\widehat w_j e^{-\mu_jt}\). Hence \(a_{2t}-a_t^2\) is their spectral variance. It vanishes for one (equivalently, every) \(t>0\) exactly when every eigenvalue with spectral support in \(e_x-L^{-1}\mathbf 1\) is identical, i.e., \(Q(e_x-L^{-1}\mathbf 1)=-\mu(e_x-L^{-1}\mathbf 1)\) for some \(\mu>0\). Evaluating this vector identity at any \(y\ne x\) gives \(c_{xy}=\mu/L\), equal and strictly positive for every other vertex. Conversely such conductances make this vector an eigenvector, proving the if-and-only-if statement. More directly, when they are all equal to \(c\), the fixed-number occupation at \(x\) flips from occupied to vacant at rate \(c(L-N)\) and from vacant to occupied at rate \(cN\), independently of the other sites' arrangement; this proves the actual local two-state Markov property, not merely the vanishing of one chosen triple CMI.

**3. Ring crossover.** Fourier diagonalization of the nearest-neighbor walk gives the stated \(p_s\) and \(\lambda_k\). At \(s=uL^2\), a dominated discrete Fourier limit yields \(Lp_{uL^2}\to\Theta_D(u)\) for each fixed \(u>0\). Hence
\[
\begin{aligned}
L\,a_{uL^2}^{\rm G}&\to\Theta_D(u),&L\,b_{uL^2}^{\rm G}&\to\Theta_D(2u),\\
L\,a_{uL^2}^{\rm C}&\to\Theta_D(u)-1,&L\,b_{uL^2}^{\rm C}&\to\Theta_D(2u)-1.
\end{aligned}
\]
Taylor expansion of the explicit information formula at \((a,b)=(0,0)\) gives \(\mathcal F(a,b)=b^2/2+O((|a|+|b|)^3)\). Applying this to the displayed limits establishes both crossover profiles.

For fixed \(L\), \(p_t\to1/L\), proving the grand-canonical plateau. On an even cycle \(L\ge4\), the first nonzero random-walk eigenvalue \(\lambda_1\) has multiplicity two and is separated from the remaining spectrum. Therefore, for \(z=e^{-\lambda_1t}\), canonical correlations satisfy \(a_t=2z/(L-1)+o(z)\), \(a_{2t}=2z^2/(L-1)+o(z^2)\), and
\[
a_{2t}-a_t^2=\frac{2(L-3)}{(L-1)^2}z^2+o(z^2).
\]
The conditional binary mutual-information expansion at a near-independent joint law is \(\mathcal F(a,b)=\tfrac12(b-a^2)^2[1+o(1)]\) for \(a,b\to0\) with \(b-a^2\ne0\) and \(b=O(a^2)\). The claimed exact exponential leading term follows. Expanding \(\mathcal F(1/L,1/L)\) gives the plateau's \(1/(2L^2)+O(L^{-3})\) asymptotic.

**4. Infinite-line tail.** On \(\mathbb Z\), the rate-\(D\) symmetric nearest-neighbor random walk has return probability \(p_t=e^{-2Dt}I_0(2Dt)\). Standard Bessel asymptotics give \(p_t=(4\pi Dt)^{-1/2}[1+O(t^{-1})]\) and \(p_{2t}=(8\pi Dt)^{-1/2}[1+O(t^{-1})]\). Since \(\mathcal F(a,b)=b^2/2+O((|a|+|b|)^3)\) at zero, \(\mathcal I_{\mathbb Z}(t)=1/(16\pi Dt)+O(t^{-3/2})\). This result uses only three observations, not an entire observed time series.

## Verification

A standalone Python script, `verify_sparse_cmi.py`, constructs exact finite-state SEP generators on cycles with four and six vertices in both ensembles; evaluates all eight three-time joint probabilities using matrix exponentials; compares their CMI and correlations with the spectral formula; checks the uniform-hub and perturbed-hub boundary cases; and evaluates the hydrodynamic theta-function and infinite-line Bessel asymptotics. The script has passed 90 deterministic assertions and runs with NumPy and SciPy. These are finite consistency checks; the preceding spectral and symmetry arguments, rather than numerical sampling, prove the general and infinite-dimensional limits.

## Relationship to prior work

Iadecola (2026, arXiv:2607.06689v1) studies single-site measurement records of the symmetric exclusion process and demonstrates memory dependent on knowledge of globally conserved particle number. Its local observation protocol includes an entire intermediate record in a discrete-time alternating-bond process; it does not state the exact **single-midpoint** conditional distribution, weighted-graph zero-memory criterion, or theta-function grand/canonical crossover derived here. These are different conditioning experiments, so the present formula is not a restatement of its finite-record Markovization law. The well-known one-particle SEP duality is used directly and is not claimed as new.

Wang, Liang and Yang (2026, arXiv:2610.36058v1), publicly posted October 26, 2026, also study **full-intermediate-record** temporal CMI and give a Gaussian hydrodynamic \(t^{-2}\) tail in a discrete-time Floquet model. The present **three-observation** CMI has a \(t^{-1}\) tail in a continuous-time process. The differing conditioning set and clock convention prevent either asymptotic from directly asserting the other.

## Limitations

The formulas require stationary half-filling, symmetric exchange rates, and a single binary probe. They do not cover asymmetric exclusion, nonstationary preparations, unequal densities without modification, quantum projective backaction, or full-history conditional mutual information. The claimed novelty is the combined sharp single-midpoint CMI / universal-hub / ensemble-crossover statement, not the underlying standard SEP covariance duality or generic spectral inequalities. A broader, unlocated theorem on binary traces of reversible particle systems might contain the result in an equivalent form; independent verification of publication priority has not been carried out.

## References

1. T. Iadecola, *Local Markov Order and Global Inference in Many-Body Dynamics*, arXiv:2607.06689v1 (first public July 7, 2026), https://arxiv.org/html/2607.06689v1 .
2. S. Wang, C. Liang and Z.-C. Yang, *Universal Scaling of Conditional Mutual Information in Classical Stochastic Dynamics*, arXiv:2610.36058v1 (October 26, 2026; comparison only), https://arxiv.org/html/2610.36058v1 .
3. Standard symmetric-exclusion one-particle duality and the continuous-time simple random-walk heat kernel are derived explicitly for the required observables above; no external identity beyond standard Fourier and Bessel asymptotics is assumed in the proof.
