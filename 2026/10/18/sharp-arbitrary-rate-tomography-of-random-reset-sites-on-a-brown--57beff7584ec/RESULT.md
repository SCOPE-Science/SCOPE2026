# Sharp arbitrary-rate tomography of random reset sites on a Brownian ring

## Finding
Consider a Brownian particle on a circular ring of known circumference \(L>0\), with known diffusivity \(D>0\), killed on first hitting one fixed point. Its starting position is chosen from an unknown probability distribution \(\mu\); independent Poisson resets of rate \(r>0\) draw fresh positions independently from the **same** distribution. Write \(\mathcal T_\mu(r)\) for the mean time to absorption. For \(x\in(0,L)\), put \(t(x)=|x-L/2|\), and let \(\nu=t_*\mu\) be the probability distribution of folded reset-site distances from the antipode of the target.

**Optimal finite-rate reconstruction theorem.** Suppose that \(\nu\) has exactly \(N\geq1\) distinct atoms \(0\leq t_1<\cdots<t_N<L/2\), with positive unknown weights \(w_i\) summing to one. For **any** \(2N-1\) pairwise distinct positive reset rates \(r_1,\ldots,r_{2N-1}\), their exact mean absorption times uniquely determine the number, folded distances, and weights of all reset sites. This holds for arbitrarily placed rate probes, not only a special grid. When \(r_j=Dj^2q^2\) with any \(q>0\), an explicit Chebyshev-moment/Hankel algorithm reconstructs the unknown parameters. This count is **sharp** for generic unknown \(N\)-atom laws: no choice of fewer than \(2N-1\) scalar rate probes can injectively identify every such law by any continuous observation scheme. No finite or infinite collection of these mean-time probes can distinguish two spatial laws having the same folded distribution \(\nu\). Conversely, knowledge of \(\mathcal T_\mu(r)\) on **any nonempty open interval** of positive rates determines \(\nu\) for every probability distribution supported in \((0,L)\), without a finite-atomic assumption.

Thus a full rate-response curve identifies exactly the distribution of *distance to the target*, not the orientation around the ring; when the folded distribution has \(N\) atoms at unknown locations, the necessary and sufficient number of **arbitrary distinct** positive rates is \(2N-1\).

## Assumptions and scope
The ring is unwrapped at the absorbing target to \((0,L)\). Between resets, the particle has infinitesimal generator \(D\partial_{xx}\) and is absorbed on reaching either endpoint. Every reset is instantaneous and independently samples \(\mu\); the initial position has law \(\mu\). All reset intervals are independent exponentials of rate \(r\). In particular, this is an **averaged** mean first-passage protocol, not a fixed separate starting site. The parameters \(L,D\), and the chosen rates are known; the reset-site law is unknown. For finite reconstruction, exact measurements and the upper bound \(N\) (or the fact of exactly \(N\) distinct folded atoms) are available. The uniqueness result uses any distinct rates, while the closed-form reconstruction algorithm uses a convenient quadratically spaced rate grid. Only **folded atoms** are counted: two sites symmetric about \(L/2\) constitute one indistinguishable folded location, with combined weight. Sites at the target itself are excluded, so the folding parameter belongs to \([0,L/2)\).

The theorem concerns exact identifiability, not stable statistical estimation under noisy finite data. The shortest geodesic distance from the target is \(d_i=L/2-t_i\). Each \(t_i>0\) corresponds to two physically distinct, mirror-related ring sites.

## Proof
**1. The forward transform.** Write \(\tau_0\) for the no-resetting absorption time, \(q_r=\sqrt{r/D}\), and \(u_r(x)=\mathbb E_x[e^{-r\tau_0}]\). Standard killing theory yields \(Du_r''=ru_r\) on \((0,L)\), with \(u_r(0)=u_r(L)=1\), hence
\[
u_r(x)=\frac{\cosh(q_r(x-L/2))}{\cosh(q_rL/2)}.
\]
For an independent exponential reset time \(E_r\), one attempted excursion succeeds before resetting with probability \(a_r=\int u_r(x)\,\mu(dx)\). Its expected length is \((1-a_r)/r\), by integrating the survival law against the exponential tail. Renewal at an unsuccessful reset gives
\[
\mathcal T_\mu(r)=\frac{1-a_r}{r a_r},\qquad
\underbrace{\int\cosh(q_r t)\,\nu(dt)}_{=:C_\nu(q_r)}
=\frac{\cosh(q_rL/2)}{1+r\mathcal T_\mu(r)}.\tag{1}
\]
The denominator is positive. This identity is the published forward relation for ring resetting, here rewritten for inverse identification.

**2. A strict total-positivity lemma for arbitrary rates.** For every integer \(K\geq1\) and strictly increasing nonnegative lists \(0\leq q_0<\cdots<q_{K-1}\) and \(0\leq t_0<\cdots<t_{K-1}\),
\[
\det[\cosh(q_i t_j)]_{0\leq i,j<K}>0.\tag{2}
\]
To prove this, truncate the absolutely convergent expansion \(\cosh(qt)=\sum_{n\geq0}q^{2n}t^{2n}/(2n)!\) and apply the finite Cauchy–Binet formula:
\[
\det[\cosh(q_i t_j)]
=\sum_{0\leq n_0<\cdots<n_{K-1}}
\frac{\det[q_i^{2n_j}]\,\det[t_i^{2n_j}]}{\prod_{j=0}^{K-1}(2n_j)!}.\tag{3}
\]
All summands are nonnegative. Indeed, generalized Vandermonde alternants of increasing nonnegative arguments and increasing nonnegative integral exponents are the ordinary Vandermonde in the squared arguments multiplied by a Schur polynomial with nonnegative coefficients. The summand \(n_j=j\) is strictly positive: both alternants reduce to ordinary Vandermondes in \(q_i^2\) and \(t_i^2\). Monotone convergence of the nonnegative Cauchy–Binet expansion proves (2). Thus every square submatrix with increasing nodes is nonsingular, even if the smallest rate or distance is zero.

**3. Arbitrary-rate uniqueness.** Suppose two folded distributions each have at most \(N\) atoms and produce the same mean times at \(2N-1\) distinct positive rates. By (1), they produce the same transform at \(q_i=\sqrt{r_i/D}\) and at \(q_0=0\), where normalization fixes \(C_\nu(0)=1\). Their signed difference has at most \(K\leq2N\) distinct folded support nodes \(t_j\). Evaluate its zero transform at the first \(K\) elements of the ordered \(2N\) values \(0,q_1,\ldots,q_{2N-1}\). The coefficient vector lies in the kernel of the \(K\)-by-\(K\) matrix of (2), which is invertible. Every signed weight vanishes, so the folded laws coincide. This proves sufficiency for **every** distinct positive-rate design. Since the rate-response is injective on the folded laws, the count of distinct folded sites is also recovered (up to the assumed upper bound).

**4. A specially selected rate grid is a constructive moment grid.** Fix \(q>0\), let \(Z=\cosh(qt)\), and define the probability measure \(\lambda\) as the pushforward of \(\nu\) under this strictly increasing map on \([0,L/2)\). The values in (1) at \(r_j=Dj^2q^2\) give exactly
\[
c_j=\int\cosh(jqt)\,\nu(dt)=\int T_j(Z)\,\lambda(dZ),\qquad 1\leq j\leq2N-1,\tag{4}
\]
where \(T_j\) is the ordinary first-kind Chebyshev polynomial, characterized by \(T_j(\cosh s)=\cosh(js)\). Also \(c_0=1\), since \(\lambda\) is a probability measure. Since \(T_j\) has degree \(j\) and leading coefficient \(2^{j-1}\) for \(j\geq1\), triangular elimination of (4) yields all ordinary moments
\[
m_k=\int Z^k\,\lambda(dZ),\qquad 0\leq k\leq2N-1.\tag{5}
\]
No high-rate limiting approximation is used.

**5. Constructive reconstruction on the quadratic rate grid.** For exactly \(N\) distinct atoms \(Z_i=\cosh(qt_i)\) of positive masses \(w_i\), define the \(N\)-by-\(N\) Hankel matrix \(H=(m_{a+b})_{0\leq a,b<N}\). It is positive definite: for any nonzero polynomial \(Q\) of degree below \(N\),
\[
\mathbf v^TH\mathbf v=\sum_{i=1}^Nw_i Q(Z_i)^2>0,
\]
because a nonzero polynomial of degree less than \(N\) cannot vanish at all \(N\) distinct nodes. Solve
\[
H(c_0,\ldots,c_{N-1})^T=-(m_N,\ldots,m_{2N-1})^T.
\]
Here the polynomial coefficients \(c_k\) are *different symbols* from the measured Chebyshev integrals in (4). The monic polynomial \(P(Z)=Z^N+\sum_{k=0}^{N-1}c_kZ^k\) satisfies
\[
\sum_{i=1}^N w_iZ_i^aP(Z_i)=0,\qquad a=0,\ldots,N-1.
\]
Vandermonde invertibility forces \(P(Z_i)=0\) for every \(i\). Its \(N\) distinct real roots are precisely the unknown \(Z_i\). The first \(N\) equations \(m_k=\sum_iw_iZ_i^k\) then give the unique weights by a Vandermonde solve. Recover
\[
t_i=q^{-1}\operatorname{arcosh}(Z_i),\qquad d_i=L/2-t_i.
\]
For at most \(N\) atoms rather than exactly \(N\), the actual atom count is detected by the rank of the available Hankel moments, and the same method uses its nonsingular leading principal block.

**6. Independent moment-route uniqueness, including the atom-count edge cases.** More generally, if two probability measures each supported on at most \(N\) distinct \(Z\)-values have identical moments through order \(2N-1\), their difference has at most \(2N\) atoms. Its weights annihilate the powers \(1,Z,\ldots,Z^{K-1}\), where \(K\leq2N\) is the number of distinct nodes in the union. The corresponding square Vandermonde matrix is invertible, so the difference is zero. This proves exact uniqueness, including sparse and zero-weight limiting representations. Values at \(t=0\) (the target antipode) are valid because \(Z=1\) causes no singularity.

**7. Sharpness of the measurement count.** Consider the open family of reset laws with exactly \(N\) ordered **strictly interior**, distinct folded sites \(0<t_1<\cdots<t_N<L/2\) and strictly positive weights \(w_1,\ldots,w_N\), summing to one. Its free parameters occupy a nonempty open subset of \(\mathbb R^{2N-1}\). For any fixed collection of \(k<2N-1\) positive rates, the map from these parameters to \(k\) mean times is continuous. A continuous injection from an open subset of \(\mathbb R^{2N-1}\) into \(\mathbb R^k\) is impossible: compose with the standard inclusion into \(\mathbb R^{2N-1}\); invariance of domain would make its image open although it lies in a proper linear subspace. Thus no universal scheme with fewer than \(2N-1\) prechosen scalar probes can be injective, regardless of how their rates are selected. Together with Step 3 this establishes the exact arbitrary-rate optimal measurement threshold. The same topological argument applies to any continuously varying collection of fewer scalar observables; it is not a claim about discontinuous oracle measurements or auxiliary measurements.

**8. Exact unavoidable reflection ambiguity and continuous-curve completeness.** The right side of (1) depends on the physical law \(\mu\) only through \(\nu=t_*\mu\). Therefore reflection \(x\mapsto L-x\), and arbitrary transfers of weight between mirror pairs, leave *every* mean-time response unchanged. Conversely, if two such responses agree on an open interval of \(r>0\), the corresponding entire even functions \(q\mapsto C_\nu(q)\) agree by the identity theorem. Their Taylor series at \(q=0\) give identical moments \(\int t^{2k}\,\nu(dt)\), \(k\geq0\). Compactness and the polynomial density theorem applied to \(s=t^2\) show that the pushforward measures coincide, hence \(\nu\) itself coincides because squaring is injective on \([0,L/2]\). This identifies the complete information content of the entire rate-response curve.

## Verification
Run `python verify.py` in the same directory. The script performs exact rational symbolic reconstruction for two, three, and four unknown folded sites, using \(q=\log 2\) and integer folded distances. It constructs the finite-rate forward mean responses, recomputes Chebyshev moments, inverts the triangular basis transformation, solves the Hankel system, factors the annihilating polynomial, and recovers the weights exactly. Separately, a 75-decimal-digit three-atom example with noninteger site positions tests the forward renewal response and inverse moments at five rates, and finite differences separately check the killed-diffusion boundary-value equation. It also numerically tests positive determinants of the arbitrary-rate cosh-kernel at sizes two through five. The printed outcomes are `all checks PASSED`. These computations illustrate, but do not substitute for, the proof above.

As a compact exact example, take \(L=4\), \(D=1\), \(q=\log 2\), and folded atoms \(t_1=0,t_2=1\) of weights \(1/3,2/3\). The measured values \(r_j\mathcal T_\mu(r_j)\) at the three rates \(r_j=j^2(\log2)^2\) are \(23/28,201/56,11123/1168\), respectively. The reconstruction outputs exactly \(Z_1=1,Z_2=5/4\) and weights \(1/3,2/3\). The two physical sides of the ring remain indistinguishable.

## Relationship to prior work
Julián-Salgado, Castro-Villarreal, Dagdug, and Boyer (arXiv:2605.08414v1, May 8, 2026) derive precisely the general averaged ring reset first-passage transform used in (1) (their equations (27)–(28)), and study optimal reset rates, mirror-symmetric phase diagrams, and two-site tricriticality. The forward identity and mirror symmetry are **prior results**, not new contributions. The contribution here is the inverse identification problem: exact **arbitrary-rate** recovery of *unknown* support and weights using the strict total positivity of the cosh kernel, a constructive special-grid algorithm, a sharp universal measurement threshold, and complete classification of information lost even under the full rate curve. No rate-optimization phase-transition claim is being made.

Evans and Majumdar (2011), and Méndez, Flaquer-Galmés, and Campos (arXiv:2401.01125), previously consider random resetting locations and associated forward first-passage formulae. Abundo (arXiv:2410.16889) studies inverse first-passage questions, but specifies full time/exit distributions at fixed parameters; its accessible description does not assert the present finite collection of scalar *rate-response means* and sharp \(2N-1\) inverse. Prony/Hankel reconstruction of atomic measures from moments is classical, and the connection to the Chebyshev basis is a known algebraic identity (cf. Kunis, Möller, and von der Ohe, 2020). These methods are credited as ingredients, not asserted as new general mathematics. The modeled experiment and its optimal information threshold are the assessed contribution.

## Limitations
This is an ideal, noise-free identifiability result. Moment inversion can be ill-conditioned when folded sites nearly coincide or sampled means have measurement error; neither statistical rates nor uniform condition-number bounds are claimed. The physical orientation of a site about the absorbing target is intrinsically unrecoverable from these mean measurements. For arbitrary distinct measurement rates, uniqueness is exact but an explicit algebraic extraction formula is only supplied for the quadratically spaced design. The theorem requires the initial law to equal the law sampled independently at each reset, and requires known \(L,D\). It does not claim recovery of non-Poisson reset dynamics, of an unknown diffusivity, or of a distinct initial distribution. The sharpness statement covers scalar rate measurements on an open unknown-parameter family. Nothing is asserted about recovery from other kinds of observations.

## References
1. P. Julián-Salgado, P. Castro-Villarreal, L. Dagdug, D. Boyer, *Mirror transitions in diffusion with stochastic resetting confined on a ring*, arXiv:2605.08414v1 (first public May 8, 2026), https://arxiv.org/abs/2605.08414 ; author manuscript full text https://www.researchgate.net/publication/404751813_Mirror_transitions_in_diffusion_with_stochastic_resetting_confined_on_a_ring .
2. M. R. Evans, S. N. Majumdar, *Diffusion with optimal resetting*, J. Phys. A: Math. Theor. 44 (2011), 435001.
3. V. Méndez, R. Flaquer-Galmés, D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125, https://arxiv.org/abs/2401.01125 .
4. M. Abundo, *Inverse first-passage problems of a diffusion with resetting*, arXiv:2410.16889 (2024); Theory Probab. Math. Statist. 112 (2025), 17–36, https://arxiv.org/abs/2410.16889 .
5. S. Kunis, H. M. Möller, U. von der Ohe, *Prony's method on the sphere*, SMAI J. Comput. Math. 6 (2020), 87–97, DOI:10.5802/smai-jcm.53 .
