# Sharp Mpemba crossing times in finite photonic diffusion chains

## Finding

Fix an odd integer \(N\geq5\) and a nearest-neighbor incoherent hopping rate \(\omega>0\). On the path with sites \(1,\ldots,N\), let \(P^{\mathrm I}(t)\) start as a unit mass at the central site \((N+1)/2\), and let \(P^{\mathrm{II}}(t)\) start uniformly on the first \(N-1\) sites, with the last site empty. Both evolve under the reflecting-boundary nearest-neighbor Markov generator. Write \(\pi_j=1/N\) and
\[
\mathcal H_X(t)=\frac N2\sum_{j=1}^{N}(P_j^X(t)-\pi_j)^2,
\qquad
\mathcal K_X(t)=\sum_{j=1}^{N}P_j^X(t)\log(NP_j^X(t)),
\]
where \(X\in\{\mathrm I,\mathrm{II}\}\) and \(0\log0=0\).

**Theorem.** For every odd \(N\geq5\), there is exactly one time \(s_N>0\) at which \(\mathcal H_{\mathrm I}(s_N)=\mathcal H_{\mathrm{II}}(s_N)\). Before this crossing the initially localized state is farther from equilibrium in squared Hilbert--Schmidt distance; afterward it is strictly closer. Put
\[
\theta_N=\frac{\pi}{2N},\quad
\lambda_k=4\omega\sin^2(k\theta_N),\quad
T_N=\frac{\log((N-1)/\cos\theta_N)}{\lambda_2-\lambda_1}.
\]
Then, along odd \(N\to\infty\),
\[
\boxed{s_N=T_N-\frac1{6\pi^2\omega}+o(1)},
\qquad
\boxed{\frac{s_N}{N^2\log N}\longrightarrow\frac1{3\pi^2\omega}}.
\]

Moreover, for all sufficiently large odd \(N\), there is exactly one relative-entropy crossing \(u_N\) in the interval
\[
\left(s_N-\frac{N^{-1/4}}{\omega},\;s_N+\frac{N^{-1/4}}{\omega}\right),
\]
and it obeys the sharper metric-dependent displacement
\[
\boxed{u_N-s_N=-\frac{N^{-1/3}}{6\pi^2\omega}+o(N^{-1/3})}.
\]
This is **local uniqueness** of the relative-entropy crossing in the stated window, not a claim that no other relative-entropy crossings exist at arbitrary earlier times.

## Assumptions and scope

The generator \(Q_N\) acts on a site distribution \(P\) by
\[
(Q_NP)_j=\begin{cases}
\omega(P_2-P_1),&j=1,\\
\omega(P_{j-1}-2P_j+P_{j+1}),&1<j<N,\\
\omega(P_{N-1}-P_N),&j=N.
\end{cases}
\]
All statements concern the exact continuous-time classical chain \(P(t)=e^{tQ_N}P(0)\). This is the incoherent strong-dephasing reduction of a photonic open-path model, with effective rate \(\omega=2J^2/\gamma\) at leading order when the dephasing rate \(\gamma\) is large compared with coherent coupling \(J\). No assertion of uniformity in the simultaneous \(N\to\infty\), \(\gamma/J\to\infty\) regime is made.

## Proof

**1. Exact spectral distances.** The orthonormal nonconstant path eigenvectors and decay rates are
\[
\varphi_k(j)=\sqrt{\frac2N}\cos\!\left(\frac{k\pi(j-1/2)}N\right),
\qquad \lambda_k=4\omega\sin^2(k\theta_N),\qquad 1\leq k<N.
\]
For the central point mass, the mode coefficient is \(\sqrt{2/N}\cos(k\pi/2)\), so only even indices occur. For the missing-endpoint initial law, the coefficient is \(-\varphi_k(N)/(N-1)\). If \(N=2M+1\), \(c_k=\cos(k\theta_N)\), and \(\varepsilon=(N-1)^{-2}\), Parseval therefore gives the **exact** formulas
\[
\mathcal H_{\mathrm I}(t)=\sum_{m=1}^{M}e^{-2\lambda_{2m}t},
\qquad
\mathcal H_{\mathrm{II}}(t)=\varepsilon\sum_{k=1}^{N-1}c_k^2e^{-2\lambda_kt}.
\]

**2. Exactly one Hilbert--Schmidt crossing.** Let \(F_N(t)=e^{2\lambda_1t}(\mathcal H_{\mathrm I}(t)-\mathcal H_{\mathrm{II}}(t))\). Separate the negative \(k=1\) term, pair each even \(k=2,4,\ldots,N-3\) with the subsequent odd \(k+1\), and leave the final even mode. The paired terms have the form
\[
(1-\varepsilon c_k^2)e^{-2(\lambda_k-\lambda_1)t}
-\varepsilon c_{k+1}^2e^{-2(\lambda_{k+1}-\lambda_1)t}.
\]
The elementary identity \(\lambda_k-\lambda_1=4\omega\sin((k-1)\theta_N)\sin((k+1)\theta_N)\) and monotonicity of \(\sin x/x\) yield
\[
\frac{\lambda_{k+1}-\lambda_1}{\lambda_k-\lambda_1}
\leq\frac{k(k+2)}{(k-1)(k+1)}\leq\frac83.
\]
Since \(\varepsilon\leq1/16\), one has
\[
(1-\varepsilon c_k^2)(\lambda_k-\lambda_1)
>\varepsilon c_{k+1}^2(\lambda_{k+1}-\lambda_1).
\]
Consequently each paired expression is strictly positive and strictly decreasing for all \(t\geq0\); the remaining even term is also positive and decreasing. Hence \(F_N\) is strictly decreasing. Its initial sign is positive because \(\mathcal H_{\mathrm I}(0)=(N-1)/2\) and \(\mathcal H_{\mathrm{II}}(0)=1/[2(N-1)]\), while its limit is \(-\varepsilon c_1^2<0\). There is exactly one crossing and its sign changes once.

**3. Sharp macroscopic time.** At \(t=T_N+O(1)\), for every fixed mode index \(k\),
\[
e^{-\lambda_kt}=N^{-k^2/3}(1+o(1)),
\]
and the combined tails beyond modes \(2\) and \(1\), respectively, are bounded in absolute value by \(N e^{-2\lambda_4t}+\varepsilon N e^{-2\lambda_3t}=O(N^{-7+o(1)})\). The two leading terms solve exactly
\[
(1-\varepsilon c_2^2)e^{-2\lambda_2t}=\varepsilon c_1^2e^{-2\lambda_1t}
\]
at
\[
t=T_N+\frac{\log(1-\varepsilon c_2^2)}{2(\lambda_2-\lambda_1)}.
\]
Their derivative difference has order \(N^{-14/3}\). The tail bound therefore perturbs the unique zero by \(o(1)\). Finally \(\lambda_2-\lambda_1\sim3\pi^2\omega/N^2\) and \(\varepsilon c_2^2\sim N^{-2}\), giving the displayed additive constant and \(N^2\log N\) law.

**4. Relative-entropy crossing and its displacement.** Write \(x_j=\pi(j-1/2)/N\) and \(z_j^X=NP_j^X-1\). At \(t=s_N+O(N^{-1/4}/\omega)\), let
\[
a=e^{-\lambda_2t},\qquad
b=\frac{c_1e^{-\lambda_1t}}{N-1},\qquad
c=\frac{c_2e^{-\lambda_2t}}{N-1}.
\]
Uniform Fourier-tail estimates imply
\[
z_j^{\mathrm I}=-2a\cos(2x_j)+O(Ne^{-\lambda_4t}),\quad
z_j^{\mathrm{II}}=2b\cos x_j-2c\cos(2x_j)+O(e^{-\lambda_3t}).
\]
At the Hilbert--Schmidt crossing, \(a\sim b\sim N^{-4/3}\), \(c\sim N^{-7/3}\), and \(b^2=a^2(1+O(N^{-2}))\). For \(|z|<1/2\),
\[
(1+z)\log(1+z)-z=\tfrac12z^2-\tfrac16z^3+\tfrac1{12}z^4+O(|z|^5).
\]
In these expansions the omitted nonleading Fourier modes contribute only \(o(N^{-5})\) to the entropy difference at the quadratic crossing: all quadratic cross terms cancel by discrete orthogonality, while higher-degree terms involving the omitted modes are \(O(N^{-17/3})\). Their differentiated contributions in the shrinking time window are \(o(N^{-14/3})\). The discrete midpoint cosine averages are exactly \(\langle\cos^3x\rangle=\langle\cos^3(2x)\rangle=0\), \(\langle\cos^2x\cos2x\rangle=1/4\), and \(\langle\cos^4x\rangle=\langle\cos^4(2x)\rangle=3/8\) for odd \(N\geq5\). Since the quadratic pieces are equal at \(s_N\), the leading fourth-order pieces cancel, and the mixed cubic term gives
\[
(\mathcal K_{\mathrm I}-\mathcal K_{\mathrm{II}})(s_N)=-b^2c+o(N^{-5})=-N^{-5}(1+o(1)).
\]
Differentiating the same controlled Fourier expansions shows, uniformly on the stated shrinking interval,
\[
(\mathcal K_{\mathrm I}-\mathcal K_{\mathrm{II}})'(t)
=-2(\lambda_2-\lambda_1)a^2(1+o(1))<0.
\]
At the two window endpoints the leading linear variation dominates the \(N^{-5}\) offset, so there is exactly one local relative-entropy zero. The mean-value theorem gives
\[
u_N-s_N=-\frac{a}{2(\lambda_2-\lambda_1)(N-1)}(1+o(1))
=-\frac{N^{-1/3}}{6\pi^2\omega}+o(N^{-1/3}).
\]
All asymptotics are for the odd sequence \(N\to\infty\) with fixed \(\omega>0\).

## Verification

The standalone program `verify.py` uses only the Python standard library. Run `python verify.py`. It checks the path eigenvalue equations, paired-mode derivative inequalities, normalization and nonnegativity of the evolved laws, agreement of spectral and direct quadratic norms, and finite numerical crossings for odd sizes through \(N=201\). It reports 16,333 finite diagnostic assertions. This is numerical and finite algebraic corroboration; the proof above supplies the statements for every admissible size and the limit.

## Relationship to prior work

Longhi's *Photonic Mpemba effect* (2024), arXiv:2408.03296v1, derives the photonic dephasing model and its classical reflecting-path limit, compares the same central and near-uniform initial laws, and describes a crossing that becomes rapidly delayed as size increases. Its main text does not provide a unique-crossing theorem, a sharp \(N^2\log N\) law, an additive constant, or the relative-entropy/Hilbert--Schmidt difference. Lu and Raz (2017) explain the general Markovian spectral mechanism for Mpemba inversions, but do not specialize to these exact path laws or determine the quantitative crossing. The current proof exploits their familiar slow-mode mechanism together with a mode-by-mode sign pairing and a discrete cubic entropy correction.

## Limitations

The result is about the exact **classical** incoherent path semigroup. It does not prove the same formulas for the finite-dephasing Lindblad quantum walk, arbitrary site-dependent couplings, other initial laws, even chains, or a joint dephasing/size limit. Global uniqueness of relative-entropy crossing outside the stated shrinking neighborhood is not asserted. The 2024 article's separately hosted supplemental file was not materially accessible in this comparison; although its main text identifies a qualitative delay, publication-priority uncertainty remains until that supplement and broader unpublished work are checked independently.

## References

1. S. Longhi, *Photonic Mpemba effect*, arXiv:2408.03296v1 (first public August 6, 2024), https://arxiv.org/html/2408.03296v1 ; *Optics Letters* **49**, 5188–5191 (2024), https://doi.org/10.1364/OL.532503.
2. Z. Lu and O. Raz, *Nonequilibrium thermodynamics of the Markovian Mpemba effect and its inverse*, *Proceedings of the National Academy of Sciences* **114**, 5083–5088 (2017), https://doi.org/10.1073/pnas.1701264114 ; arXiv:1609.05271.
