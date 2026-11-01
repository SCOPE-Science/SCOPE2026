# A sharp logarithmic spectral-gap law for rational-angle random circular billiards

## Finding

For each integer \(n\ge7\), set \(\alpha=\pi/n\) and consider the rational-angle Feres random reflection operator \(P_n\) on the finite angular orbit
\[\Theta_n=\{\theta_j=(j+\tfrac12)\alpha:0\le j<n\}.\]
This is an invariant angle class of the random circular billiard of Vales and Pinto-de-Carvalho [1], whose angular part is the triangular-microstructure random billiard law originally introduced by Feres [2]. Write \(\lambda_2(P_n)\) for the second-largest **algebraic** eigenvalue, counting multiplicity. Then
\[
\boxed{\lim_{n\to\infty}n^2\log n\,[1-\lambda_2(P_n)]=2\pi^2.}
\]
Consequently, the lazy operator \(Q_n=(I+P_n)/2\) has
\[\boxed{1-\lambda_2(Q_n)\sim\frac{\pi^2}{n^2\log n}},\]
so its \(L^2\) relaxation time is \(\sim n^2\log n/\pi^2\). This is a *within-class* rate, not a claim of global rational-angle mixing.

## Assumptions and scope

The parameter satisfies \(0<\alpha<\pi/6\), hence \(n\ge7\). For an incoming angle \(\theta\in(0,\pi)\), the four possible angular maps and corresponding probabilities are precisely those in [1, §3.1], also [2, §2.2]:
\[
T_1(\theta)=\theta+2\alpha,\quad T_2(\theta)=-\theta+2\pi-4\alpha,\quad
T_3(\theta)=\theta-2\alpha,\quad T_4(\theta)=-\theta+4\alpha.
\]
Their state-dependent probabilities are the four piecewise functions in those references, defined using
\[u_\beta(\theta)=\tfrac12\left(1+\frac{\tan\beta}{\tan\theta}\right).\]
The kernel \(P_n(j,k)=\sum_{i=1}^4p_i(\theta_j)\mathbf1_{\{T_i(\theta_j)=\theta_k\}}\) is an \(n\times n\) stochastic matrix. The closed class \(\Theta_n\) has positive transition probabilities only along the edges enumerated below. The discussion concerns only the angular Markov marginal and not the spatial angular skew product, other rational-angle classes, or invariant Liouville measure on all angles.

## Proof

**1. Exact reversible graph.** Let \(s_j=\sin((j+\tfrac12)\alpha)\) and \(S_n=\sum_{j=0}^{n-1}s_j=1/\sin(\alpha/2)\). Direct substitution in [1]'s four branch probabilities gives the invariant distribution
\[\pi_j=s_j/S_n,\qquad \pi_jP_n(j,k)=\pi_kP_n(k,j).\]
To fix conductance normalization, put \(c_{jk}=s_jP_n(j,k)\) and \(w_{jk}=c_{jk}/S_n=\pi_jP_n(j,k)\). Every nonzero off-diagonal edge (listed once, with \(j<k\)) is exactly:
\[
\begin{aligned}
c_{j,j+2}&=\frac{\sin((j+\tfrac32)\alpha)}{2\cos\alpha}, &&1\le j\le n-4,\
c_{0,2}&=c_{n-3,n-1}=\sin(\alpha/2),\
c_{1,2}&=c_{n-3,n-2}=\frac{\sin(\alpha/2)}{2\cos\alpha}.
\end{aligned}
\]
(The bridge at the right is written as an unordered edge; its endpoints should be ordered when implementing the matrix.) All these conductances are positive, all other off-diagonal entries vanish, and there are no self-loops. The core \(1,\ldots,n-2\) is a single cycle: its two step-two strands of opposite index parity meet at the bridge edges \(\{1,2\}\) and \(\{n-3,n-2\}\). Vertices \(0,n-1\) are leaves. The graph is connected, hence \(1\) is a simple eigenvalue. For even \(n\) the original chain is bipartite (and has eigenvalue \(-1\)); laziness removes that periodicity.

**2. The two electrical arms.** Choose one odd-index and one even-index vertex \(a_n,b_n\in\{1,\ldots,n-2\}\) within two indices of \(n/2\). Removing the leaves, the cycle splits into two edge-disjoint paths between \(a_n\) and \(b_n\), one crossing the left bridge and the other the right bridge. Let their total resistances be \(R_{L,n},R_{R,n}\), with edge resistance \(w_{jk}^{-1}\). Both satisfy the sharp logarithmic estimates
\[R_{L,n}=\frac{4\log n}{\alpha^2}+O(\alpha^{-2}),\qquad
R_{R,n}=\frac{4\log n}{\alpha^2}+O(\alpha^{-2}).\]
Indeed an internal edge starting at index \(j\) has resistance
\[r_j=\frac{2S_n\cos\alpha}{\sin((j+\tfrac32)\alpha)}.\]
For fixed parity indices near the left endpoint, \(r_j=(4/\alpha^2)[(j+\tfrac32)^{-1}+O(\alpha^2(j+1))]\), and the two alternating sums (odd and even indices) up to the middle each contribute \((2/\alpha^2)\log n+O(\alpha^{-2})\). The same estimate holds after reflection at the right endpoint; contributions away from grazing angles are \(O(\alpha^{-2})\). Each bridge resistance is \(2S_n\cos\alpha/\sin(\alpha/2)=O(\alpha^{-2})\). Uniformity of the error follows by comparison of \(\sin t\) with \(t\) near zero and boundedness of its reciprocal on compact subintervals of \((0,\pi)\).

The effective conductance between the two mid-angle vertices is exactly
\[G_n=\frac1{R_{L,n}}+\frac1{R_{R,n}}=\frac{\alpha^2}{2\log n}(1+O(1/\log n)).\]
The leaves contribute no current when their potentials equal those of their neighbors.

**3. Parity sectors equilibrate much faster.** Put \(\mathcal E_n(f)=\sum_{j<k}w_{jk}[f(j)-f(k)]^2=\langle f,(I-P_n)f\rangle_\pi\). If \(a_n\) is the odd representative and \(b_n\) the even one, then for a numerical constant \(C\), independent of \(n\ge7\) and \(f\),
\[
\sum_{j\ \mathrm{odd}}\pi_j[f(j)-f(a_n)]^2+
\sum_{j\ \mathrm{even}}\pi_j[f(j)-f(b_n)]^2
\le C\alpha^{-2}\mathcal E_n(f).
\]
For each same-parity vertex, use the unique step-two path to its representative (and for the two leaves, add their leaf edge). Cauchy--Schwarz bounds the squared difference by the path resistance times the total edge energy. The resistance of a path extending from a mid-angle representative to \(\theta_j\) is bounded by \(C\alpha^{-2}[1+|\log\sin\theta_j|]\). Summing these path bounds against \(\pi_j\) gives \(O(\alpha^{-2})\), since \(\pi_j=\sin\theta_j/S_n\), \(S_n\asymp\alpha^{-1}\), and \(\int_0^\pi\sin t\,|\log\sin t|\,dt<\infty\). The parity masses \(m_{0,n}=\sum_{j\ \mathrm{even}}\pi_j\) and \(m_{1,n}=\sum_{j\ \mathrm{odd}}\pi_j\) both tend to \(1/2\) by Riemann sums (indeed here both equal \(1/2\) exactly).

**4. Matching Rayleigh bounds.** Set \(f(a_n)=1\), \(f(b_n)=-1\), interpolate electrically (harmonically, i.e. linearly in cumulative resistance) on each of the two arms, and give the leaves their neighbors' values. Effective-network reduction yields \(\mathcal E_n(f)=4G_n\). The parity-sector estimate above implies that \(f\) differs from the ideal values \(\pm1\) by \(o(1)\) in \(L^2(\pi)\); thus \(\operatorname{Var}_\pi(f)=1+o(1)\). Consequently
\[1-\lambda_2(P_n)\le\frac{4G_n}{1+o(1)}=\frac{2\alpha^2}{\log n}(1+o(1)).\]

For the lower bound, take a mean-zero eigenfunction \(g_n\) for \(\lambda_2(P_n)\) with \(\operatorname{Var}_\pi(g_n)=1\). The preceding upper bound and parity-sector inequality give
\[\sum_j\pi_j|g_n(j)-g_n(r(j))|^2=O(1/\log n)=o(1),\]
where \(r(j)\) is the appropriate parity representative. By the mean-zero normalization and variance decomposition,
\[m_{0,n}m_{1,n}[g_n(a_n)-g_n(b_n)]^2=1+o(1),\]
so the squared anchor difference is \(4+o(1)\). Thomson's/Dirichlet's principle for the two parallel arms then gives \(\mathcal E_n(g_n)\ge G_n[g_n(a_n)-g_n(b_n)]^2=4G_n(1+o(1))\). Therefore
\[1-\lambda_2(P_n)=\frac{2\alpha^2}{\log n}(1+o(1))
=\frac{2\pi^2}{n^2\log n}(1+o(1)),\]
as asserted. The eigenvalues of \((I+P_n)/2\) are \((1+\lambda_i(P_n))/2\), proving the lazy-chain statement. No infinite conclusion relies on numerical eigenvalues.

## Verification

The standalone `check_feres.py` derives the finite kernel from all four original piecewise billiard probability functions, independently constructs the asserted sine-conductance graph, checks stochasticity, invariance, detailed balance, graph weights, and computes the symmetric conjugate's second eigenvalue for \(n=7,8,9,12,20,40,80,120\). It also checks the exact eigenvalue \(-1\) for even \(n\). The displayed scaled values tend toward \(2\pi^2\); these finite calculations corroborate the formulas only. The infinite spectral result is proved above by effective resistance and a weighted parity-sector inequality. Run with `python check_feres.py` using NumPy and SciPy.

## Relationship to prior work

Feres [2] derived the same four-branch triangular-cell random reflection law, and explicitly recognized finite dihedral angle orbits when \(\alpha/\pi\) is rational. Vales and Pinto-de-Carvalho [1] embedded that law in a circular billiard and proved qualitative rational-versus-irrational mixing conclusions. The later constant-curvature treatment [3] extends the qualitative billiard dynamics. The exact \(n^{-2}(\log n)^{-1}\) spectral-gap law, leading constant, and electrical two-arm explanation are **not statements located** in those inspected accounts.

Feres--Zhang [4] and Chumley--Feres--Garcia German [5] investigate spectral gaps and diffusion approximations of random-billiard scattering operators for other microstructures. In particular, [5] obtains a weak-scattering Legendre-operator approximation; its hypotheses and operator family are not the present finite rational triangular angular class. Their techniques and spectral-gap questions are acknowledged, not treated as a novelty by themselves.

## Limitations

This result applies only to the specified half-offset \(n\)-point invariant angular class and to the restricted Markov operator. It does not assert a spectral gap in the ambient continuously supported angle space, mixing of rational-angle circular billiards, the location of all eigenvalues by modulus, or a total-variation cutoff profile. The real-valued graph identity and asymptotic are analytic; numerical checks are finite only. The original Feres angular law predates the 2020 circular-billiard application and is fully attributed. Publication-priority searches are not an exhaustive proof of novelty; an equivalently formulated spectral result in older billiard/Markov literature remains possible. Independent scientific validation has not been performed.

## References

[1] T. Vales and S. Pinto-de-Carvalho, *A Random Billiard Map in the Circle*, arXiv:2005.01892 (first posted 2020-05-05), §§3–4, https://arxiv.org/abs/2005.01892 .

[2] R. Feres, *Random Walks Derived from Billiards*, in *Dynamics, Ergodic Theory, and Geometry* (2007), §§2.2, 6; https://www.math.wustl.edu/~feres/random_billiard.pdf .

[3] T. Vales, *Random circular billiards on surfaces of constant curvature: Pseudo integrability and mixing*, arXiv:2212.00872 (first posted 2022-12-01), §§3, 6; https://arxiv.org/abs/2212.00872 .

[4] R. Feres and H.-K. Zhang, *Spectral gap for a class of random billiards*, Comm. Math. Phys. 313 (2012), 479–515; https://www.math.wustl.edu/~feres/spectralgapnew.pdf .

[5] T. Chumley, R. Feres and L. A. Garcia German, *Knudsen Diffusivity in Random Billiards: Spectrum, Geometry, and Computation*, arXiv:2005.14318 (2020), §§2, 4; https://arxiv.org/abs/2005.14318 .
