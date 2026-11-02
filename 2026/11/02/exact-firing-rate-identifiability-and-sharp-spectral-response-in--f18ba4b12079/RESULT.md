# Exact firing-rate identifiability and sharp spectral response in weakly reinforced urn networks

## Finding

For the weakly reinforced edge-urn model on a **finite connected undirected simple graph**, the limiting edge reinforcement rates determine the vertex firing rates exactly if and only if the graph is nonbipartite. On a bipartite graph they determine precisely a one-dimensional positive affine family of firing rates; this is a complete description of every possible observational ambiguity, not merely an infinitesimal one.

For a cycle with \(n\ge3\) vertices, the rate-to-limit map has an explicit Fourier derivative at uniform firing. Its sharp Euclidean susceptibility has a size-dependent crossover at \(\alpha_n=1/(1+\cos(\pi/n))\), tending to \(1/2\) as the cycle grows. Even cycles hide the exactly alternating firing-rate perturbation **at every amplitude permitted by positivity**, although nearby Fourier modes exhibit arbitrarily strong amplification when cycle size is allowed to grow and \(\alpha\uparrow1\).

## Assumptions and scope

Let \(G=(V,E)\) be a finite connected simple graph with at least two vertices. Fix \(\alpha\in[0,1)\) and strictly positive firing rates \(q=(q_v)_{v\in V}\). Each vertex has an independent Poisson clock of rate \(q_v\). When the clock at vertex \(v\) fires, one incident edge is selected with probability proportional to its current positive weight raised to \(\alpha\), and that weight increases by one. All initial edge weights are deterministic and strictly positive. Denote the edge weights at time \(t\) by \(N_t(e)\).

By Qin's homogenization theorem [1], for every \(e\in E\), \(N_t(e)/t\to m_e\) almost surely, where \(m=\mathcal R_\alpha(q)\in(0,\infty)^E\) is the unique strictly positive solution of

\[
 m_e=m_e^\alpha\sum_{v\in e}\frac{q_v}{D_v(m)},\qquad
 D_v(m)=\sum_{f\ni v}m_f^\alpha.
\]

The observation is this *exact long-run edge vector* \(m\). No finite-observation, noisy-data, or infinite-graph inverse theorem is asserted. Define the unsigned edge-vertex incidence matrix \(B\in\{0,1\}^{E\times V}\) by \(B_{e,v}=1\) if \(v\in e\) and zero otherwise. For any such positive observation, define \(s_e=m_e^{1-\alpha}\) and \(r_v=q_v/D_v(m)>0\).

**Global inverse and all fibers.** One has \(Br=s\). Conversely, for fixed \(m=\mathcal R_\alpha(q)\), *every* strictly positive rate vector producing exactly this same limit is of the form \(q'_v=D_v(m)r'_v\), where \(r'>0\) solves \(Br'=s\). In particular:

- If \(G\) contains an odd cycle, \(\ker B=\{0\}\); hence \(q'=q\). The firing rates are uniquely identifiable from \(m\).
- If \(G\) is bipartite with classes \(V_+\) and \(V_-\), write \(\sigma_v=1\) on \(V_+\) and \(-1\) on \(V_-\). The complete fiber is

\[
 q'_v=(r_v+\tau\sigma_v)D_v(m),\qquad
 -\min_{v\in V_+}r_v<\tau<\min_{v\in V_-}r_v.
\]

All these rates are positive, genuinely distinct for distinct \(\tau\), and generate the same almost-sure limiting edge weights. Thus bipartiteness is the exact identifiability obstruction among finite connected graphs.

**Sharp response on cycles.** Now let \(G=C_n\), with vertices \(i\in\mathbb Z/n\mathbb Z\), edges \(e_i=\{i,i+1\}\), and baseline rates \(q_i=p>0\). For any \(h\in\mathbb R^n\), put \(q_i(\varepsilon)=p(1+\varepsilon h_i)\), which is positive for sufficiently small \(|\varepsilon|\). The map \(\varepsilon\mapsto m(\varepsilon)=\mathcal R_\alpha(q(\varepsilon))\) is real-analytic near zero. Writing \(x_i=m_i'(0)\), its derivative is the unique solution of

\[
 \left(1-\frac\alpha2\right)x_i+
 \frac\alpha4(x_{i-1}+x_{i+1})
 =\frac p2(h_i+h_{i+1}).
\]

For the complex Fourier input \(h_i=\exp(2\pi\mathrm{i}ki/n)\), \(k=0,\ldots,n-1\), the output is

\[
 x_i=p\,\frac{1+\exp(2\pi\mathrm{i}k/n)}
 {2[1-\alpha\sin^2(\pi k/n)]}\,
 \exp(2\pi\mathrm{i}ki/n).
\]

Consequently the exact induced \(\ell^2\)-operator norm is

\[
 \boxed{M_n(\alpha,p)=p\max_{0\le k<n}
 \frac{|\cos(\pi k/n)|}{1-\alpha\sin^2(\pi k/n)}.}
\]

Set \(\alpha_n=[1+\cos(\pi/n)]^{-1}\). For \(0\le\alpha<\alpha_n\), the constant-rate direction alone has maximal gain \(p\); at \(\alpha=\alpha_n\), the first nonconstant Fourier harmonics tie it; and for \(\alpha>\alpha_n\), at least one nonconstant harmonic has gain strictly exceeding \(p\). Moreover,

\[
 \alpha_n=\frac12+\frac{\pi^2}{8n^2}+O(n^{-4}),\qquad
 \lim_{n\to\infty}\frac{M_n(\alpha,p)}p
 =\begin{cases}1,&0\le\alpha\le\frac12,\\
 [2\sqrt{\alpha(1-\alpha)}]^{-1},&\frac12<\alpha<1.
 \end{cases}
\]

On every even cycle, the full nonlinear inverse fiber includes \(q_i=p(1+\varepsilon(-1)^i)\) for all \(|\varepsilon|<1\), with *exactly* \(m_i=p\) for every edge. The rate map's derivative has kernel spanned by this alternating direction on even cycles and is invertible on odd cycles. Although the alternating direction is invisible, the sharp gain has a finite fixed-size limit as \(\alpha\uparrow1\):

\[
 \lim_{\alpha\uparrow1}\frac{M_n(\alpha,p)}p=
 \begin{cases}\csc(\pi/n),&n\text{ even},\\
 \csc(\pi/(2n)),&n\text{ odd}.
 \end{cases}
\]

This is a crossover in *linear-response modal dominance*, not a loss of uniqueness or a dynamical phase transition within \(\alpha<1\).

## Proof

**1. Reduction to unsigned incidence.** The equilibrium equation from [1] holds with a positive unique solution for all stated graphs and firing rates. Divide its edge equation by \(m_e^\alpha>0\) to obtain

\[
 m_e^{1-\alpha}=\sum_{v\in e}\frac{q_v}{D_v(m)}
 =\sum_{v\in e}r_v=(Br)_e.
\]

If two positive firing-rate vectors \(q,q'\) yield the same \(m\), their flux difference belongs to \(\ker B\). Conversely, if \(r'>0\) satisfies \(Br'=s\), set \(q'_v=r'_vD_v(m)\). The same \(m\) then solves every equilibrium equation for \(q'\); uniqueness of the positive equilibrium in [1] forces \(\mathcal R_\alpha(q')=m\). This establishes *both* necessity and sufficiency, with no unproved inverse existence assertion.

**2. Rank and positivity classification.** If \(Bz=0\), then \(z_u+z_v=0\) on every edge \(\{u,v\}\). Connectedness makes all \(z_v\) alternate in sign along paths. An odd cycle forces \(z=0\). If the graph is bipartite, every path has consistent parity, and \(z=\tau\sigma\) for a unique scalar \(\tau\). Thus the kernel is zero precisely on nonbipartite graphs and one-dimensional otherwise. The strict positivity constraints \(r_v+\tau\sigma_v>0\) yield the displayed **open interval**, completing the global fiber theorem.

For odd \(C_n\), the inverse is particularly explicit: \(r_i=\frac12\sum_{j=0}^{n-1}(-1)^j s_{i+j}\), indices modulo \(n\), and \(q_i=r_iD_i(m)\). On even \(C_n\), \(\sum_i(-1)^i s_i=0\) is necessary for attainability (automatically fulfilled by any observed limit), and the fiber is as above. For constant observed weights \(m_i=p\), \(D_i=2p^\alpha\) and \(r_i=p^{1-\alpha}/2\), giving the exact alternating rates \(p(1+\varepsilon(-1)^i)\).

**3. Analytic differential.** Fix \(\alpha<1\) and define \(\Phi_i(m,q)=m_i^\alpha[q_i/(m_{i-1}^\alpha+m_i^\alpha)+q_{i+1}/(m_i^\alpha+m_{i+1}^\alpha)]\). At \(q_i=m_i=p\), direct differentiation gives

\[
 \partial_m(m-\Phi)x=\mathsf Lx,\qquad
 (\mathsf Lx)_i=\left(1-\frac\alpha2\right)x_i+
 \frac\alpha4(x_{i-1}+x_{i+1}),
\]

and \(\partial_q\Phi[p h]_i=p(h_i+h_{i+1})/2\). The circulant \(\mathsf L\) has eigenvalues \(1-\alpha\sin^2(\pi k/n)\), all at least \(1-\alpha>0\). The real-analytic implicit-function theorem therefore supplies a local positive analytic equilibrium branch. Its identification with \(\mathcal R_\alpha\) follows from the global uniqueness in [1]. Differentiation gives \(\mathsf Lx=(p/2)(h_i+h_{i+1})\) and the Fourier multiplier stated above. Complex modes are used only to diagonalize a real-linear operator; the resulting singular values are their absolute gains.

**4. Finite-size threshold and continuum envelope.** Put \(c_k=|\cos(\pi k/n)|\). The mode gain divided by \(p\) is \(c_k/[1-\alpha(1-c_k^2)]\). For \(k\ne0\), this exceeds one exactly when \(\alpha>1/(1+c_k)\); the greatest nonconstant \(c_k\) is \(\cos(\pi/n)\). This proves the exact first crossover \(\alpha_n\) and all equality cases. The Taylor expansion of cosine yields the stated \(n^{-2}\) correction.

As \(n\to\infty\), the Fourier mesh becomes dense and the maximum converges to the maximum of \(\sqrt{1-u}/(1-\alpha u)\) over \(u\in[0,1]\). For \(\alpha\le1/2\), the maximum is at \(u=0\) and equals one; for \(\alpha>1/2\), elementary differentiation gives \(u=2-1/\alpha\) and the value \([2\sqrt{\alpha(1-\alpha)}]^{-1}\). Finally, for fixed \(n\) as \(\alpha\uparrow1\), every mode with \(c_k>0\) tends to gain \(1/c_k\), while an exactly alternating mode has zero gain for all \(\alpha<1\). The smallest nonzero \(c_k\) equals \(\sin(\pi/n)\) when \(n\) is even and \(\sin(\pi/(2n))\) when \(n\) is odd. This proves the parity-dependent endpoint limit.

## Verification

`CHECK.py` is a standalone finite-instance corroboration script requiring Python, NumPy, and SciPy. It numerically solves positive equilibrium equations on representative cycles and other connected graphs, checks the global incidence inverse, odd-cycle reconstruction, even-cycle exact one-parameter fibers, analytic first derivatives against central finite differences, Fourier singular values against independently computed matrix norms, all finite-size modal crossover boundaries through 100 vertices, and the continuum/endpoint formulas. Replaying this exact script produces the recorded output in `CHECK_OUTPUT.txt`: **1,460 deterministic finite checks passed**.

The universal claims for arbitrary finite connected graphs, arbitrary \(n\), all positive firing-rate vectors, and every \(\alpha\in[0,1)\) follow from the preceding algebraic and analytic arguments plus [1], not from finite testing. No simulation is used as an infinite-state certification.

## Relationship to prior work

Qin [1] proves the existence, uniqueness, and almost-sure convergence of the positive edge equilibrium on countable networks with heterogeneous firing rates. Equation (1.4) and the power transform (2.6) are essential premises of the present inverse calculation; they are not claimed as discoveries here. The contribution is the complete **inverse firing-rate fiber** with its graph-bipartiteness criterion, together with the **sharp rate-to-equilibrium Fourier response**, finite-size crossover, and exact invisible modulation on cycles. These inverse and quantitative statements were not located in the inspected text of [1].

Couzinié and Hirsch [2] establish earlier homogeneous-rate weak-reinforcement results, rather than the nonuniform-rate inverse and response formulas. Van der Hofstad, Holmes, Kuznetsov and Ruszel [3] study cycle equilibria and their linear stability in the strong-reinforcement model; their cycle Jacobian comparison is relevant background but does not give the heterogeneous firing-rate response multiplier or the global inverse fiber described here. Benaïm, Benjamini, Chen and Lima [4] analyze a *different* graph interacting-urn model, with vertex-held rather than edge-held weights, so their nonbipartite/bipartite phenomena cannot be substituted for this one.

The fact that [1] already gives an implicit transformed equilibrium equation creates a genuine historical-priority risk for an implicit or unrecorded incidence-based inverse observation; similarly, earlier stability formulas may permit an alternative derivation of portions of the Fourier response. The complete explicit quantitative and inverse package is assessed as not directly covered by the inspected sources, not as independently certified novel.

## Limitations

The inversion assumes knowledge of the exact asymptotic edge vector and the reinforcement exponent. It makes no claims of statistical estimation from finite noisy observations, uniform nonlinear conditioning far from equal rates, infinite-graph inversion, or stability exactly at \(\alpha=1\). The spectral formula and sharp crossover are specific to cyclic graphs, although the inverse fiber dichotomy holds on all finite connected simple graphs. The sharp response concerns the derivative in a Euclidean norm, not a large-amplitude global Lipschitz constant. The model has an independent-review and historical-priority risk; no independent mathematical validation is asserted.

## References

1. Shuo Qin, *Homogenization of weakly reinforced Pólya urns on countable networks*, arXiv:2610.11780v1 (first public 2026-10-08), especially Theorem 1.1, (1.4), and (2.6). https://arxiv.org/html/2610.11780v1
2. Yannick Couzinié and Christian Hirsch, *Weakly reinforced Pólya urns on countable networks*, arXiv:2010.03347 (first public 2020-10-07), Sections 1–4. https://arxiv.org/abs/2010.03347
3. Remco van der Hofstad, Mark Holmes, Alexey Kuznetsov and Wioletta Ruszel, *Strongly reinforced Pólya urns with graph-based competition*, arXiv:1406.0449 (first public 2014-06-02), especially Example 1.8 and Proposition 1.20. https://arxiv.org/abs/1406.0449
4. Michel Benaïm, Itai Benjamini, Jun Chen and Yuri Lima, *A generalized Pólya's urn with graph based interactions*, arXiv:1211.1247v4 (originally public 2012-11-06), Sections 1–3. https://arxiv.org/html/1211.1247v4
