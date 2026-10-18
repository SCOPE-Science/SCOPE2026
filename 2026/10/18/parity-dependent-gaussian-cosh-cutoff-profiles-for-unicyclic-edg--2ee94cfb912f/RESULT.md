# Parity-dependent Gaussian–cosh cutoff profiles for unicyclic edge-toggle walks

## Finding
Let \(G_m\) be any finite connected simple unicyclic graph with exactly \(m\) edges and \(m\) vertices, and let \(\ell_m\) be its unique cycle length. Beginning with the all-zero vertex labeling, repeatedly choose an edge uniformly and **toggle** the two endpoint bits; toggling means \(0\leftrightarrow1\), not assigning a common random color. Write \(\mu_{m,t}\) for the law after \(t\) toggles. The accessible group consists of the even-weight vertex labels.

If \(\ell_m\) is odd, the chain is aperiodic. Let \(\pi_m\) be uniform on its accessible group. At *every* finite \(m\) and \(t\), the distance \(\|\mu_{m,t}-\pi_m\|_{\mathrm{TV}}\) equals the distance from a nonlazy single-coordinate random walk on the \(m\)-cube at time \(t\) to the uniform distribution on its time-\(t\) parity layer. In particular, with
\[
 t_m(c)=\left\lfloor\frac m4\log m+cm\right\rfloor,\qquad s=e^{-2c},
\]
for every fixed real \(c\),
\[
\lim_{m\to\infty}\|\mu_{m,t_m(c)}-\pi_m\|_{\mathrm{TV}}
=2\Phi(s/2)-1,
\qquad
\lim_{m\to\infty}\chi^2(\mu_{m,t_m(c)}\|\pi_m)=e^{s^2}-1.
\]
Both limits hold for every sequence of odd-cycle unicyclic graphs, irrespective of their cycle lengths or branching shapes.

If \(\ell_m\) is even, the vertex walk has period two. Denote by \(\pi_{m,t}\) the *uniform law on the parity class accessible at step* \(t\), which has \(2^{m-2}\) states. For any even-cycle sequence with \(\ell_m/m\to\alpha\in[0,1]\), define independent standard normal variables \(Z_1,Z_2\) and
\[
L_{\alpha,s}=\exp\bigl(-s^2/2+s\sqrt{1-\alpha}\,Z_1\bigr)
\cosh\bigl(s\sqrt\alpha\,Z_2\bigr).
\]
Then the complete cutoff profiles relative to the *current periodic class* are
\[
\lim_{m\to\infty}\|\mu_{m,t_m(c)}-\pi_{m,t_m(c)}\|_{\mathrm{TV}}
=\frac12\mathbb E|L_{\alpha,s}-1|,
\]
\[
\lim_{m\to\infty}\chi^2(\mu_{m,t_m(c)}\|\pi_{m,t_m(c)})
=\frac{e^{s^2}+e^{(1-2\alpha)s^2}}2-1.
\]
In both parity regimes the centered cutoff is \(\frac m4\log m\), with window of order \(m\), for the stated target distributions. In the even-cycle regime, ordinary total variation to the full stationary uniform law is always at least \(1/2\), so ordinary aperiodic mixing is **not** claimed.

## Assumptions and scope
Graphs are connected, undirected, loopless, and unicyclic. All vertex bits and edge-incidence vectors are over \(\mathbb F_2\); natural logarithms are used. The edge at each step is sampled independently and uniformly, and the starting vertex configuration is deterministic zero. Translation invariance gives the same distances for any deterministic start. In the asymptotic assertions, \(m\to\infty\) through compatible graph sizes; \(c\) is fixed; for the even-cycle case \(\ell_m\) is even and the real limit \(\alpha\) exists. \(\Phi\) is the standard normal distribution function. The chi-square divergence is relative to the explicitly named reference law and equals \(\int(L-1)^2\,d\pi\).

## Proof
**1. Incidence quotient and the parity dichotomy.** Index the \(m\) edges and let \(B:\mathbb F_2^m\to\mathbb F_2^m\) be the unoriented incidence map. Each column is one edge's two-endpoint indicator. Connectedness gives \(\operatorname{rank}B=m-1\), and the kernel is \(\{0,z\}\), where \(z\) is the indicator of the unique \(\ell_m\)-edge cycle. If \(Y_t\) is the single-coordinate cube walk started at zero, the vertex chain is exactly \(B Y_t\). The edge process lives in \(P_t=\{y:\sum_j y_j\equiv t\pmod2\}\). For odd \(\ell_m\), translation by \(z\) changes parity; consequently \(B|_{P_t}\) is a bijection from \(P_t\) onto the even-vertex-label group. For even \(\ell_m\), translation by \(z\) preserves parity; consequently \(B|_{P_t}\) is two-to-one onto its image of size \(2^{m-2}\). Those two images alternate with \(t\), proving period two. This also proves the claimed exact odd-cycle finite-time distance identity, because bijections preserve total variation and chi-square divergence.

**2. An \(L^2\) product approximation on a parity layer.** Let \(U_{m,t}\) be uniform on \(P_t\), and \(Q_{m,t}\) be the law of \(Y_t\). Put \(b_m=(1-2/m)^{t_m(c)}\), so \(\sqrt m\,b_m\to s\). Let \(R_{m,t}\) be the product law with independent coordinate signs \(\sigma_j=(-1)^{Y_j}\) of mean \(b_m\), conditioned on membership of \(P_t\). For \(y\in P_t\), its density relative to \(U_{m,t}\) is
\[
R_{m,t}(y)/U_{m,t}(y)=\frac{\prod_{j=1}^m(1+b_m\sigma_j)}{1+(-1)^t b_m^m}.
\]
We claim
\[
\left\|Q_{m,t_m(c)}/U_{m,t_m(c)}-R_{m,t_m(c)}/U_{m,t_m(c)}\right\|_{L^2(U_{m,t_m(c)})}\longrightarrow0.
\]
Indeed the Walsh coefficient of \(Q_{m,t}\) on a set of cardinality \(k\) is \(\lambda_k^t\), where \(\lambda_k=1-2k/m\), and the coefficient of \(R_{m,t}\) is
\[
\frac{b_m^k+(-1)^t b_m^{m-k}}{1+(-1)^t b_m^m}.
\]
On \(P_t\), complementary Walsh characters differ by the constant \((-1)^t\); Parseval therefore has exactly half the full-cube sum of squared coefficient differences. For each fixed \(k\), \(\lambda_k^{t_m(c)}-b_m^k=o(m^{-k/2})\); the same estimate follows at \(m-k\) by complement symmetry. For \(0\le k\le m/2\), the squared spectral contributions multiplied by \(\binom mk\) are bounded by \(C_c^k/k!\) using \(|\lambda_k|^{2t}\le\exp(-4kt/m)\); the product coefficients obey the same summable bound, including the complementary term. Split the sum at a fixed \(K\) and let \(K\to\infty\). The claimed \(L^2\) approximation follows. In particular, all first and second moments of the resulting densities have the required limits.

**3. Odd-cycle limit.** On \(P_t\), the product density in Step 2 has logarithm \(b_m\sum_j\sigma_j-mb_m^2/2+o_{U}(1)\). Uniform parity conditioning changes the usual central limit theorem for \(m^{-1/2}\sum_j\sigma_j\) by nothing in the limit (its joint Fourier characteristic function differs by a vanishing parity-character term). The density therefore converges in distribution, with uniform integrability inherited from Step 2, to \(\exp(sZ-s^2/2)\). Gaussian likelihood-ratio calculus gives \(\frac12\mathbb E|e^{sZ-s^2/2}-1|=2\Phi(s/2)-1\), and its second moment is \(e^{s^2}\). The incidence bijection completes this case.

**4. Even-cycle limit.** The fiber of \(B|_{P_t}\) is exactly \(\{y,y+z\}\). The density relative to the uniform law on the quotient equals the average of the two densities relative to \(U_{m,t}\). Conditional expectation contracts \(L^2\), so Step 2 remains valid after this projection. Separate edge signs into the \(m-\ell_m\) bridge indices and the \(\ell_m\) cycle indices. The projected product density is
\[
\frac{\prod_{j\notin C}(1+b_m\sigma_j)}{2(1+(-1)^t b_m^m)}
\left[\prod_{j\in C}(1+b_m\sigma_j)+\prod_{j\in C}(1-b_m\sigma_j)\right].
\]
Its logarithmic expansion is \( -mb_m^2/2+b_m\sum_{j\notin C}\sigma_j+\log\cosh(b_m\sum_{j\in C}\sigma_j)+o_U(1)\). Under uniform parity conditioning, the two normalized sign sums converge jointly to independent normals with respective variances \(1-\alpha\) and \(\alpha\); this statement includes either degenerate endpoint. Hence the density converges in law to \(L_{\alpha,s}\), and the \(L^2\) approximation plus bounded second moments gives both the total-variation limit and convergence of second moments. Direct Gaussian integration gives
\[
\mathbb E L_{\alpha,s}=1,\qquad
\mathbb E L_{\alpha,s}^2=	frac12(e^{s^2}+e^{(1-2\alpha)s^2}).
\]
The cutoff assertions follow because the corresponding TV profiles tend to zero as \(s\downarrow0\) and to one as \(s\uparrow\infty\) (the nonnegative density tends to zero in probability under the reference law), with \(s=e^{-2c}\). The even-cycle target is periodic-class uniform, never the full stationary law.

## Verification
Run `python3 verify.py` with a standard-library Python interpreter. Its exact-rational finite-state enumerations cover every feasible cycle length from three through eight total edges, at times zero through four, and verify: the one-dimensional incidence kernel; push-forward from the cube; and the Fourier formula for chi-square divergence for each parity case. The program completed 2,757 exact checks. This finite check is corroboration, not the proof of the limits. The asymptotic conclusions rest on Steps 2–4 and the stated uniform summability and Gaussian integrals.

## Relationship to prior work
The exact cutoff profile for the ordinary hypercube walk is classical (Diaconis, Graham, Morrison, 1990), and binary hypercube spectral decompositions are well established; we do not claim either ingredient. Collevecchio and Griffiths (2020) study broad hypercube walks, not incidence-code quotients of a two-vertex-toggle walk. Hermon and Olesker-Taylor (2021) analyze *random* Cayley generators in regimes such as growing generator excess, whereas a unicyclic incidence walk has the **deterministic** single-relation excess of one. Demirci, Işlak and Özdemir (2022) analyze a different operation called edge flipping, which **recolors both endpoints to one common new color** rather than toggling both bits. Their result must not be conflated with the present walk. The claims here concern the graph-incidence parity dichotomy and the explicit \(\alpha\)-dependent Gaussian–cosh law after quotient projection, not novelty of cube mixing itself.

## Limitations
No assertion is made for multiple-cycle graphs, weighted-edge selection, nonuniform initial *random* laws, or nonuniform toggling. For even cycles, full-stationary TV does not converge to zero because the chain remains periodic; all even-cycle cutoff language explicitly refers to the currently reachable periodic class. The result establishes analytical asymptotics and finite-state identities but not an independent historical-priority certification. Closely related results could exist in coding-theoretic quotient walks or earlier studies of folded hypercubes.

## References
- A. Collevecchio and R. Griffiths, *Three steps mixing for general random walks on the hypercube at criticality*, arXiv:2002.09059 (first public 2020-02-20), Sections 1–3. https://arxiv.org/abs/2002.09059
- J. Hermon and S. Olesker-Taylor, *Cutoff for Almost All Random Walks on Abelian Groups*, arXiv:2102.02809 (first public 2021-02-04), Sections 1–2. https://arxiv.org/abs/2102.02809
- Y. E. Demirci, Ü. Işlak and A. Y. Özdemir, *Mixing time bounds for edge flipping on regular graphs*, arXiv:2201.03315 (first public 2022-01-10), Sections 1–3. https://arxiv.org/abs/2201.03315
- P. Diaconis, R. L. Graham and J. A. Morrison, *Asymptotic analysis of a random walk on a hypercube with many dimensions*, Random Structures & Algorithms 1 (1990), 51–72. DOI:10.1002/rsa.3240010105.
