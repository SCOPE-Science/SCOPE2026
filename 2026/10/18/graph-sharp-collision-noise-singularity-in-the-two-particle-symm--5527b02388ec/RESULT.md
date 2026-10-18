# Graph-sharp collision-noise singularity in the two-particle symmetric inclusion process

## Finding

Let \(G=(V,E)\) be a finite connected simple undirected graph on \(n\ge3\) vertices. For \(a>0\), run the **two-particle symmetric inclusion process** in which a particle moves from \(x\) to a neighboring \(y\) at total rate \(\eta_x(a+\eta_y)\). Start in its unique stationary distribution. Let \(C_t\) equal one when the two particles occupy the same vertex and zero otherwise, and put \(H_T=\int_0^T C_t\,dt\). Define the integrated collision covariance
\[
V_G(a)=\int_0^\infty\operatorname{Cov}(C_0,C_t)\,dt
=\lim_{T\to\infty}\frac{\operatorname{Var}(H_T)}{2T}.
\]

Write \(\mathcal N_G\) for the unordered pairs \(\{x,y\}\) of distinct **nonadjacent** vertices. On this set, define a killed Markov generator \(K_G\): two independent particles each jump across each incident graph edge at rate one; kill the process at its first visit to a pair of adjacent vertices. Let \(\tau_{\rm adj}\) be that hitting time. Then
\[
\boxed{\lim_{a\downarrow0}V_G(a)=\frac2n\sum_{\{x,y\}\in\mathcal N_G}\mathbb E_{\{x,y\}}\tau_{\rm adj}.}
\]
The sum is zero if \(\mathcal N_G\) is empty. Every expectation in a nonempty sum is finite and strictly positive. In particular, the limit is positive **if and only if the graph is not complete**. At the same time, the instantaneous stationary variance of \(C_t\) tends to zero for *every* graph:
\[
\operatorname{Var}(C_0)=\frac{(n-1)a(a+1)}{(na+1)^2}\longrightarrow0.
\]
Thus the normalized integrated autocorrelation time \(V_G(a)/\operatorname{Var}(C_0)\) diverges like \(1/a\) on every noncomplete connected graph, but stays finite on a complete graph. More precisely, if \(G\) is noncomplete and the displayed weak-diffusion limit is \(L_G>0\), this time is asymptotic to \(L_G/[(n-1)a]\). For \(G=K_n\) it is exactly \(1/[2(na+1)]\).

Two explicit families illustrate the sharp distinction. On the complete graph,
\[
\boxed{V_{K_n}(a)=\frac{(n-1)a(a+1)}{2(na+1)^3}.}
\]
For the cycle \(C_n\), with \(n\ge3\),
\[
\boxed{V_{C_n}(a)=\frac{(a+1)\big[n(n^2-1)a+(n-1)(n-2)(n-3)\big]}{24(na+1)^3}.}
\]
For \(n\ge4\) this is strictly decreasing in \(a>0\), with weak-diffusion limit \((n-1)(n-2)(n-3)/24\). The triangle has zero weak-diffusion limit and, exceptionally, one strict maximum at \(a=(\sqrt7-2)/3\).

## Assumptions and scope

The graph is fixed, connected, simple, unweighted, and undirected, with at least three vertices. There are **exactly two indistinguishable conserved particles**, each vertex may hold zero, one, or two particles, and each directed graph edge has the specified inclusion jump rate. The parameter \(a\) is positive and tends to zero *after* taking the long-time stationary covariance limit. All hitting times in the theorem use unordered pairs of independent rate-one-per-edge walkers, killed upon first becoming adjacent. This killed walk is defined only on nonadjacent pairs, and is absent for complete graphs. The time normalization is the one in the displayed generator; changing the overall jump-rate multiplier rescales the covariance integral inversely.

The observable is **whether the two particles coincide**, not the occupation of any prespecified site. Consequently this is an observable-specific dynamical statement, not a general spectral-gap theorem. The stationary distribution and instantaneous variance do not depend on the edges of the graph, provided it is connected, whereas the integrated covariance does.

## Proof

**1. Exact reversible weights.** Denote a double-occupied configuration by \(D_x=2\delta_x\), and a separated configuration by \(S_{xy}=\delta_x+\delta_y\), \(x\ne y\), with unordered subscripts. Direct detailed balance gives
\[
\pi_a(D_x)=\frac{a+1}{n(na+1)},\qquad
\pi_a(S_{xy})=\frac{2a}{n(na+1)}.
\]
Indeed, for \(xy\in E\), the transition \(D_x\to S_{xy}\) has rate \(2a\) and its reverse rate is \(a+1\); between separated configurations a single particle moves to an empty vertex at rate \(a\) in either direction. Summation of the displayed weights is one. Connectivity and \(a>0\) imply irreducibility, hence uniqueness. Summing the double-occupied weights gives \(p_a=\mathbb E C_0=(a+1)/(na+1)\), and the stated instantaneous variance follows.

**2. Reversible covariance variational identity.** On a finite irreducible reversible continuous-time Markov chain, with \(f=C-p_a\), the Poisson equation \(-L_a u=f\), normalized by \(\langle u\rangle_{\pi_a}=0\), has a unique solution. Spectral decomposition yields \(V_G(a)=\langle f,u\rangle_{\pi_a}\) and the asymptotic occupation-time variance. Equivalently,
\[
V_G(a)=\sup_h\left\{2\langle f,h\rangle_{\pi_a}-\mathcal E_a(h,h)\right\},\qquad
\mathcal E_a(h,h)=-\langle h,L_ah\rangle_{\pi_a}.
\]
The supremum is invariant under addition of constants to \(h\).

**3. Separation of scales in the Dirichlet form.** Write \(z=ah\) and fix the additive constant by setting \(z(D_{x_0})=0\) at one vertex. Let \(\mathcal F\) be the collection of all double-occupied states and all separated states corresponding to *edges* of \(G\). The graph of transitions between members of \(\mathcal F\), using \(D_x\leftrightarrow S_{xy}\) whenever \(xy\in E\), is connected. In terms of \(z\), the unordered-edge conductances in \(\mathcal E_a(h,h)\) have the exact values
\[
\frac{2(a+1)}{n(na+1)a}\quad\text{for }D_x\leftrightarrow S_{xy}\ (xy\in E),
\qquad
\frac{2}{n(na+1)}\quad\text{for every }S\leftrightarrow S'\text{ move into an empty site}.
\]
There are no other nontrivial state transitions. The first set of conductances diverges as \(a\downarrow0\), while the second set tends to \(2/n\). Since the entire finite configuration transition graph is connected, these conductances are bounded below uniformly for \(0<a\le1\). On the gauge-fixed finite-dimensional subspace this implies a uniform Poincaré/coercivity bound on \(z\).

The linear term becomes exactly
\[
\langle f,h\rangle_{\pi_a}
=\frac{a+1}{n(na+1)^2}
\left[(n-1)\sum_x z(D_x)-2\sum_{x<y}z(S_{xy})\right].
\]
Uniform coercivity and the bounded linear functional force every maximizing \(z\) to stay bounded as \(a\downarrow0\). The diverging first conductances force all its coordinates on \(\mathcal F\) to coincide in the limit, hence to vanish by the gauge choice. The only possible nonzero limiting coordinates are therefore \(z_s\), for \(s\in\mathcal N_G\).

The limiting Dirichlet energy is \((2/n)z^{\mathsf T}(-K_G)z\), where the killed boundary at adjacent pairs has value zero. The limiting linear term is \(-(2/n)\mathbf1^{\mathsf T}z\). The admissible limiting variational problem is consequently
\[
\sup_{z\in\mathbb R^{\mathcal N_G}}
\left[-\frac4n\mathbf1^{\mathsf T}z
-\frac2n z^{\mathsf T}(-K_G)z\right].
\]
Uniform coercivity proves the upper limit by compactness of maximizers; extending any fixed \(z\) by zero on \(\mathcal F\) supplies the matching lower limit. Connectivity of \(G\) ensures that two independently moving particles from any nonadjacent pair eventually become adjacent, so \(-K_G\) is positive definite. The unique optimizer is \(z=-(-K_G)^{-1}\mathbf1\), and the maximum equals
\[
\frac2n\mathbf1^{\mathsf T}(-K_G)^{-1}\mathbf1.
\]
By the elementary hitting-time backward equation, \((-K_G)^{-1}\mathbf1\) has entries \(\mathbb E_s\tau_{\rm adj}\). This completes the graph classification and the noncomplete-graph autocorrelation asymptotic. If the nonadjacent set is empty, the limiting variational space is trivial and its maximum is zero.

**4. Complete graphs.** On \(K_n\), the collision indicator itself is a two-state Markov chain: collision-to-separation rate \(2a(n-1)\), separation-to-collision rate \(2(a+1)\). Its covariance is \(p_a(1-p_a)e^{-2(na+1)t}\). Integration proves the stated complete-graph formula and autocorrelation time.

**5. Cycles.** Mark the two particles temporarily by distinct labels and follow their relative displacement \(R_t\in\mathbb Z/n\mathbb Z\). The stationary weights are \(\rho_0=(a+1)/(na+1)\) and \(\rho_r=a/(na+1)\) for \(1\le r<n\). From displacement zero the process jumps to each of \(\pm1\) at rate \(2a\); from displacement \(1\) or \(n-1\) it hits zero at rate \(2(a+1)\); other steps to neighboring nonzero displacements occur at rate \(2a\). Thus the expected hitting time \(t_r=\mathbb E_rT_0\) solves the one-dimensional backward equations, with solution
\[
t_r=\frac{r(n-r)-(n-1)/(a+1)}{4a},\qquad 1\le r<n.
\]
The Poisson equation for \(\mathbf1_{\{R=0\}}-\rho_0\) gives the identity
\[
V_{C_n}(a)=\rho_0^2\sum_{r=1}^{n-1}\rho_r t_r.
\]
Since \(\sum_{r=1}^{n-1}r(n-r)=n(n^2-1)/6\), simplification yields the displayed rational formula. Differentiating gives
\[
\frac{dV_{C_n}}{da}=-\frac{(n-1)P_n(a)}{24(na+1)^4},
\]
where
\[
P_n(a)=n^2(n+1)a^2+2n(2n^2-5n+5)a+3n^3-17n^2+22n-6.
\]
For \(n\ge4\), every coefficient is positive: the constant term, with \(m=n-4\ge0\), is \(3m^3+19m^2+30m+2\). For \(n=3\), \(P_3(a)=12(3a^2+4a-1)\), which has the unique positive zero \((\sqrt7-2)/3\). The asserted strict monotonicity and exceptional triangular maximum follow.

## Verification

The accompanying `verify.py` uses only Python's standard library, constructs the full two-particle generator with exact rational arithmetic, verifies the displayed stationary weights against every state-balance equation, solves the centered Poisson equation, and compares the resulting integrated covariance against the exact cycle and complete-graph formulas. It also constructs the killed pair-walk Green function and tests its weak-diffusion prediction on representative paths, stars, cycles and complete graphs. On replay, it printed `PASS: 42 full-generator exact-rational and singular-limit tests` and the limits \(11/8\), \(1/4\), and \(0\) on the four-vertex path, cycle, and complete graph, respectively. The exact finite-case tests are supporting checks; the arbitrary-graph limit and all-size cycle formula are proved above, not inferred from those tests.

Reproduce by running `python3 verify.py` in a directory containing that standalone file. No external packages, data downloads, or randomness are required.

## Relationship to prior work

Giardinà, Redig and Vafayi developed the symmetric inclusion process, its stationary measures, duality, and correlation inequalities. Grosskinsky, Redig and Vafayi studied finite-graph condensation dynamics in a joint many-particle and weak-diffusion regime. Bianchi, Dommers and Giardinà analyzed condensate metastability as particle count becomes large. Carinci, Giardinà and Redig gave a two-particle Fourier–Laplace transition formula on the *infinite translation-invariant integer lattice* and applications to coarsening. Kim and Sau obtained finite-graph spectral-gap and weak-diffusivity results. Those contributions are prior foundations, not assigned to the present result.

The present claim instead fixes **two particles** and an **arbitrary finite connected simple graph**, takes the stationary long-time limit first, and evaluates the small-diffusivity *integrated co-location covariance* through a Dirichlet killed-pair Green operator. In particular it resolves the graph-completeness boundary for this observable and gives the all-size cycle rational formula with a three-versus-four-vertex response distinction. Neither a general spectral-gap bound nor an infinite-line transition transform by itself evaluates this graph-specific covariance or its killed-nonedge coefficient. Nevertheless, an equivalent calculation in another published finite-state or potential-theoretic treatment cannot be ruled out without independent exhaustive bibliographic review.

## Limitations

The statement does not extend automatically to more than two particles, directed or weighted edges, nonuniform free-diffusion rates, time-dependent graphs, different observables, or nonstationary initial conditions. The two limits \(T\to\infty\) and \(a\downarrow0\) are taken in the specified order and generally do not commute. A nonzero limiting covariance integral does **not** mean a nonzero instantaneous variance at \(a=0\). The graph Green expression is an exact finite-dimensional characterization, not a universal elementary formula in the size alone. There is no claim about infinite-volume condensation or a thermodynamic phase transition.

## References

1. C. Giardinà, F. Redig, K. Vafayi, *Correlation inequalities for interacting particle systems with duality*, arXiv:0906.4664, first public version 25 June 2009; published as *Journal of Statistical Physics* 141 (2010). https://arxiv.org/abs/0906.4664
2. S. Grosskinsky, F. Redig, K. Vafayi, *Dynamics of condensation in the symmetric inclusion process*, arXiv:1210.3827, first public version 14 October 2012; *Electronic Journal of Probability* 18 (2013), article 66. https://arxiv.org/abs/1210.3827
3. A. Bianchi, S. Dommers, C. Giardinà, *Metastability in the reversible inclusion process*, arXiv:1605.05140 (2016), *Electronic Journal of Probability* 22 (2017). https://arxiv.org/abs/1605.05140
4. G. Carinci, C. Giardinà, F. Redig, *Exact formulas for two interacting particles and applications in particle systems with duality*, arXiv:1711.11283 (2017), *Annals of Applied Probability* 30 (2020), 1934–1970. https://arxiv.org/abs/1711.11283
5. S. Kim, F. Sau, *One- and two-particle spectral gap identities for the symmetric inclusion process and related models*, arXiv:2412.01489 (2024). https://arxiv.org/abs/2412.01489
