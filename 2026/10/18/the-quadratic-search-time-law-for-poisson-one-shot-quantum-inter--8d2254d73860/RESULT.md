# The quadratic search-time law for Poisson one-shot quantum interrogations

## Finding

Consider a continuous-time coherent nearest-neighbor walk on the integer lattice, interrogated at a single target vertex after an exponentially distributed waiting time. A failed interrogation triggers **immediate re-preparation of the original state**, rather than continued evolution of the post-measurement state. For a target at integer distance \(n\geq1\), nonzero real hopping amplitude \(h\), and interrogation rate \(r>0\), write \(T_n(r)\) for the total physical time until the first successful interrogation, including all failed trials and assuming zero re-preparation overhead. Then

\[
\mathbb E T_n(r)=\frac{2\pi |h|}{r^2 Q_{n-1/2}\!\left(1+\frac{r^2}{8h^2}\right)},
\]

where \(Q_\nu(z)\) is the real Legendre function of the second kind for \(z>1\). Every \(n\geq1\) has at least one rate \(r_n>0\) that globally minimizes this mean. Define \(K_0,K_1\) as the modified Bessel functions of the second kind, and let \(\alpha_*\) be the unique positive root of

\[
2K_0(\alpha_*)=\alpha_*K_1(\alpha_*),\qquad
\alpha_*=1.552651255645\ldots .
\]

**The sharp large-distance optimization theorem** is that for *every choice* of global minimizing rates \(r_n\),

\[
\lim_{n\to\infty}\frac{n r_n}{2|h|}=\alpha_* ,\qquad
\lim_{n\to\infty}\frac{|h|}{n^2}\min_{r>0}\mathbb E T_n(r)
=\frac{\pi}{2\alpha_*^2 K_0(\alpha_*)}
=3.26221174933594\ldots .
\]

Thus the fastest one-shot exponential-interrogation protocol has a **quadratic** rather than linear asymptotic mean-detection time, despite the ballistic free propagation of the quantum walker. The theorem does *not* claim uniqueness of each finite-distance minimizer or optimality over different measurement/restart protocols.

## Assumptions and scope

The Hilbert space is \(\ell^2(\mathbb Z)\), with site basis \(|j\rangle\). The Hamiltonian is the bounded self-adjoint operator

\[
H=h\sum_{j\in\mathbb Z} \bigl(|j+1\rangle\langle j|+|j\rangle\langle j+1|\bigr),\quad h\in\mathbb R\setminus\{0\}.
\]

Each trial independently starts in \(|0\rangle\). Draw \(\tau\) with exponential density \(re^{-r\tau}\) on \((0,\infty)\), evolve by \(e^{-iH\tau}\), and perform one projective test \(\{|n\rangle\langle n|,I-|n\rangle\langle n|\}\). On success, stop. On failure, discard the post-measurement state, reprepare \(|0\rangle\) immediately, and draw a new independent waiting time. The clock records all waiting periods; preparation and readout time costs are defined to vanish. This protocol is *not* repeated quantum monitoring of a surviving state, and is *not* random resetting without target interrogation.

Set \(a=r/(2|h|)\). All formulas below are for \(n\in\{1,2,\ldots\}\), \(r>0\), \(h\ne0\). The special functions use their standard positive real branches.

## Proof

**1. Exact renewal mean.** Fourier diagonalization of the lattice Hamiltonian gives the transition amplitude \(\langle n|e^{-iHt}|0\rangle=(-i\operatorname{sgn}h)^nJ_n(2|h|t)\). One trial succeeds with probability

\[
q_n(r)=r\int_0^\infty e^{-rt} J_n(2|h|t)^2\,dt>0.
\]

The pairs (trial duration, trial outcome) are independent between trials, though the duration and outcome *within* a trial are correlated. Conditioning on the first trial, using its unconditioned mean duration \(1/r\), gives the renewal equation \(\mathbb ET_n(r)=1/r+(1-q_n(r))\mathbb ET_n(r)\). Hence \(\mathbb ET_n(r)=1/(rq_n(r))\). The geometric number of trials is almost surely finite because \(q_n(r)>0\).

**2. Exact Laplace transform.** For \(a>0\), the classical Bessel addition identity and Laplace transform of \(J_0\) yield

\[
\int_0^\infty e^{-au}J_n(u)^2\,du
=\frac{1}{\pi}\int_0^\pi\frac{\cos(n\theta)}{\sqrt{a^2+4\sin^2(\theta/2)}}\,d\theta
=\frac{1}{\pi}Q_{n-1/2}(1+a^2/2).
\]

Substitution \(u=2|h|t\) into the renewal mean gives the exact formula above. Existence of a finite minimizing rate follows by continuity and divergence at both endpoints: as \(r\downarrow0\), \(rq_n(r)=O(r^2\log(1/r))\to0\), using the standard large-argument Bessel bound; as \(r\to\infty\), the small-argument expansion of \(J_n\) gives \(q_n(r)\sim \binom{2n}{n}(|h|/r)^{2n}\), so \(rq_n(r)\to0\) for every \(n\geq1\).

**3. The uniform Legendre-to-Bessel limit.** Define \(\alpha=na=nr/(2|h|)\), and \(\eta(a)=2\operatorname{arsinh}(a/2)\), so \(\cosh\eta(a)=1+a^2/2\). The positive integral representation of the same Legendre function is

\[
Q_{n-1/2}(\cosh\eta)=\frac1{\sqrt2}
\int_\eta^\infty \frac{e^{-nt}}{\sqrt{\cosh t-\cosh\eta}}\,dt.
\]

For \(\alpha\) in a compact subset of \((0,\infty)\), substitute \(t=z/n\). Since \(n\eta(\alpha/n)\to\alpha\) and \(n^2(\cosh(z/n)-\cosh\eta)\to(z^2-\alpha^2)/2\), dominated convergence after translating the square-root endpoint yields, locally uniformly in \(\alpha\),

\[
Q_{n-1/2}\left(1+\frac{\alpha^2}{2n^2}\right)
\longrightarrow \int_\alpha^\infty\frac{e^{-z}}{\sqrt{z^2-\alpha^2}}\,dz=K_0(\alpha).
\]

Consequently \(\mathbb ET_n(2|h|\alpha/n)\,|h|/n^2\to \pi/[2\alpha^2K_0(\alpha)]\) uniformly for \(\alpha\) in such compact subsets.

**4. No escaping optimizers.** Since \(\cosh t-\cosh\eta\ge(t^2-\eta^2)/2\) for \(t\ge\eta\ge0\), the preceding representation implies

\[
0<Q_{n-1/2}(\cosh\eta)\le K_0(n\eta).
\]

Set \(c=2\operatorname{arsinh}(1/2)>0\). For \(0<a\le1\), concavity of \(\operatorname{arsinh}\) gives \(\eta(a)\ge ca\). Thus

\[
\alpha^2 Q_{n-1/2}(1+\alpha^2/(2n^2))
\le\alpha^2K_0(c\alpha)
\quad (\alpha/n\le1),
\]

which tends to zero both as \(\alpha\downarrow0\) and as \(\alpha\to\infty\), uniformly in \(n\). For \(a\ge1\), \(\eta(a)\ge c\), while \(a^2\le e^{\eta(a)}\); the elementary bound \(K_0(v)\le C e^{-v}\) for \(v\ge c\) consequently gives

\[
\alpha^2Q_{n-1/2}(1+a^2/2)
\le Cn^2 e^{-(n-1)c}\longrightarrow0
\quad (a\ge1).
\]

A fixed positive comparison value at \(\alpha=1\), combined with these estimates, confines *every* global maximizer of \(\alpha^2Q_{n-1/2}(1+\alpha^2/(2n^2))\) to a common compact subinterval of \((0,\infty)\) once \(n\) is sufficiently large. Hence each subsequential limit maximizes \(\alpha^2K_0(\alpha)\).

**5. Unique limiting optimizer.** Differentiating \(f(\alpha)=\alpha^2K_0(\alpha)\) gives \(f'(\alpha)=\alpha[2K_0(\alpha)-\alpha K_1(\alpha)]\). For \(R(\alpha)=\alpha K_1(\alpha)/K_0(\alpha)\), the modified-Bessel recurrences imply

\[
R'(\alpha)=\alpha\left[\left(\frac{K_1(\alpha)}{K_0(\alpha)}\right)^2-1\right]>0.
\]

Indeed \(K_1(\alpha)>K_0(\alpha)>0\), as follows directly from the positive integral representation \(K_\nu(\alpha)=\int_0^\infty e^{-\alpha\cosh t}\cosh(\nu t)\,dt\). Also \(R(\alpha)\to0\) as \(\alpha\downarrow0\) and \(R(\alpha)\to\infty\) as \(\alpha\to\infty\). Thus \(R=2\) has exactly one positive solution, the unique global maximum of \(f\). Compactness and the locally uniform limit prove both asserted limits for **every** minimizing-rate sequence.

## Verification

The standalone numerical program `verify.py` independently evaluates the Bessel-square Laplace integral, the principal Legendre \(Q\) representation, the positive toroidal integral, finite-path matrix exponentials approximating the infinite lattice, finite-distance minimizing rates, and the asymptotic \(K_0\) scaling. It uses Python with `numpy`, `scipy`, and `mpmath`, as specified in `requirements.txt`. Execute `python verify.py` in the directory containing both files. The verified execution produced:

`VERIFY_OK bessel_legendre=15 legendre_integrals=8 finite_path=16 optima=5 scaling=4 root=1.552651255645 constant=3.262211749336 max_error=1.65e-09`

The independent representations agree on the tested parameter grid; the numerical checks do not substitute for the proof of limits over unbounded distance and all positive rates.

## Relationship to prior work

Varbanov, Krovi and Brun (arXiv:0803.3446, first public 2008-03-24) initiated Poisson-time monitoring of continuous-time quantum walks, but their failed measurements leave the surviving state in the complementary space; they do not discard and reprepare after **each** miss. Friedman, Kessler and Barkai (arXiv:1603.02046, first public 2016-03-07) developed quantum first-detection renewal equations under fixed sampling, likewise without the trial-by-trial re-preparation used here. Yin and Barkai (arXiv:2205.01974, first public 2022-05-04) introduced explicit restarts after a prescribed number of repeated fixed-time interrogations, including a one-step special protocol; their principal analysis and reported optimizers concern the restart count at a fixed sampling time, not the optimized *exponential* one-shot waiting law at growing target distance. Yin, Wang and Barkai (arXiv:2301.06100, first public 2023-01-15) examine noisy observation times in a repeatedly monitored, periodically restarted lattice walk, including an immediate-restart special case, but their numerical timing noise is bounded uniform jitter rather than exponentially distributed one-shot trials and their optimization does not derive the globally optimal growing-distance Poisson rate or its quadratic constant. Kulkarni and Majumdar (arXiv:2305.15123) and Del Vecchio Del Vecchio and Majumdar (arXiv:2509.08556) study random projective measurements and their post-measurement survival state in two-level and fully connected models, not the infinite-lattice re-preparation protocol here.

Standard renewal formulas, free-lattice Bessel propagation, and the Bessel-to-Legendre integral identity are **not** asserted as new. The specific contribution assessed here is their combination with a *uniform, globally optimized* large-distance theorem, including the unique transcendental asymptotic rate and exact quadratic constant. More general first-detection or renewal results may cover nearby protocols; the comparisons here do not establish exhaustive publication priority.

## Limitations

This statement assumes zero re-preparation/readout overhead, instantaneous ideal target projective measurement, independent exponential trial intervals, a fixed localized re-preparation state and target, homogeneous nearest-neighbor coherent hopping, and the infinite one-dimensional lattice. The optimum is only among interrogation rates **within this one-shot exponential family**. In particular, it does not compare favorably against all possible deterministic-interrogation or multi-measurement restart protocols; some such protocols can exploit coherent propagation more efficiently. The theorem does not give a closed expression for finite-distance optimizing rates or claim their uniqueness. Independent literature-priority assessment remains outstanding.

## References

1. M. Varbanov, H. Krovi, T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446 (first submitted 2008-03-24), https://arxiv.org/abs/0803.3446.
2. H. Friedman, D. A. Kessler, E. Barkai, *Quantum Renewal Equation for the first detection time of a quantum walk*, arXiv:1603.02046 (first submitted 2016-03-07), https://arxiv.org/abs/1603.02046.
3. R. Yin, E. Barkai, *Restart expedites quantum walk hitting times*, arXiv:2205.01974 (first submitted 2022-05-04), https://arxiv.org/abs/2205.01974.
4. M. Kulkarni, S. N. Majumdar, *First detection probability in quantum resetting via random projective measurements*, arXiv:2305.15123 (first submitted 2023-05-24), https://arxiv.org/abs/2305.15123.
5. G. Del Vecchio Del Vecchio, S. N. Majumdar, *Optimal detection of quantum states via projective measurements*, arXiv:2509.08556 (first submitted 2025-09-10), https://arxiv.org/abs/2509.08556.
6. R. Yin, Q. Wang, E. Barkai, *Instability in the quantum restart problem*, arXiv:2301.06100 (first submitted 2023-01-15), https://arxiv.org/abs/2301.06100.
7. NIST Digital Library of Mathematical Functions, Bessel and Legendre-function integral and recurrence identities, https://dlmf.nist.gov/.
