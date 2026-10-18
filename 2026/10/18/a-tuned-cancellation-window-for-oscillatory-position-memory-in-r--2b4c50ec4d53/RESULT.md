# A tuned-cancellation window for oscillatory position memory in run–pause–reverse transport

## Finding

The stationary position covariance of a harmonically confined four-state run–pause–reverse particle has infinitely many **strict sign changes** if and only if the parameter trichotomy below holds. Set \(\lambda=(\alpha+\beta)/2\), \(\chi=(\alpha-\beta)^2-4\alpha\beta\), and, when \(\chi<0\), \(\omega=\sqrt{-\chi}/2\). Assume \(\alpha,\beta,\kappa,v>0\).

* If \(\chi\ge0\), only finitely many strict sign changes occur.
* If \(\chi<0\) and \(\kappa>\lambda\), infinitely many strict sign changes occur.
* If \(\chi<0\) and \(\kappa<\lambda\), infinitely many strict sign changes occur **precisely when** \(\kappa=\sqrt2\,\beta\), i.e., the otherwise dominant trap-relaxation pole has zero residue.
* If \(\chi<0\) and \(\kappa=\lambda\), infinitely many strict sign changes occur **precisely when** \(\alpha/\beta>\sqrt5-2\). At equality there are infinitely many nontransversal zero touches, but no strict sign changes.

In particular, for \(\alpha=3\), \(\beta=1\), \(\kappa=\sqrt2\),
\[
 C(t)=v^2e^{-2t}\left(\frac{\cos(\sqrt2\,t)}{32}+\frac{\sin(\sqrt2\,t)}{16\sqrt2}\right),\qquad t\ge0.
\]
Even though the trap exponent \(\sqrt2\) is strictly slower than the orientation exponent \(2\), the slower exponential disappears **exactly**, leaving infinitely many anticorrelations.

## Assumptions and scope

The internal state is \(R_+,R_-,T_+,T_-\). In \(R_\pm\), the position evolves with velocity \(-\kappa X\pm v\); in \(T_\pm\), with velocity \(-\kappa X\). Transitions \(R_\pm\to T_\pm\) occur at rate \(\alpha\), and \(T_\pm\to R_\mp\) at rate \(\beta\). Thus each stationary rest period is followed by **mandatory direction reversal**, not an independent direction redraw. All waiting times are exponential; there is no additional translational Brownian forcing. The unique bounded stationary process is observed at arbitrary stationary times and \(C(t)=\operatorname{Cov}(X_t,X_0)\) for \(t\ge0\). By global reversal symmetry \(\mathbb E X=0\). A **strict sign change** means crossing between positive and negative values; an isolated tangent zero does not qualify.

## Proof

**Stationary construction.** The four-state internal chain is irreducible for \(\alpha,\beta>0\). Let \(F_t\) equal \(v\), \(-v\), or \(0\) in \(R_+\), \(R_-\), or a pause state. Its stationary distribution gives running probability \(\beta/(\alpha+\beta)\), split evenly among signs. The stable harmonic filter
\[
 X_t=\int_0^\infty e^{-\kappa u}F_{t-u}\,du
\]
exists and defines the unique stationary solution for the position, bounded in absolute value by \(v/\kappa\).

**Two-dimensional orientation sector.** On antisymmetric run and pause observables, the backward generator has matrix
\[
 B=\begin{pmatrix}-\alpha&\alpha\\-\beta&-\beta\end{pmatrix},\qquad
 D(s)=\det(sI-B)=(s+\alpha)(s+\beta)+\alpha\beta.
\]
With \(A=v^2\beta/(\alpha+\beta)\), the stationary forcing covariance is \(G(t)=A(e^{Bt})_{11}\) for \(t\ge0\). Its one-sided Laplace transform is \(A(s+\beta)/D(s)\). In the complex-eigenvalue regime \(\chi<0\), write \(z=-\lambda+i\omega\), \(c=1+i(\alpha-\beta)/(2\omega)\); then \(G(t)=A\operatorname{Re}(ce^{zt})\).

**Exact filtered covariance.** Directly integrating two exponential filter kernels, or equivalently solving the coupled covariance ODE, yields
\[
 \boxed{\displaystyle
 C(t)= A\operatorname{Re}\!\left(\frac{c e^{zt}}{\kappa^2-z^2}\right)
 +A\,\frac{\alpha(2\beta^2-\kappa^2)}{\kappa D(\kappa)D(-\kappa)}e^{-\kappa t}.}
\]
For \(\chi<0\), \(D(-\kappa)=(\kappa-\lambda)^2+\omega^2>0\), so there is no singularity. The oscillatory complex coefficient is nonzero, and
\[
 C(0)=A\frac{\kappa+\beta}{\kappa D(\kappa)}>0.
\]
The coefficient of \(e^{-\kappa t}\) vanishes exactly when \(\kappa=\sqrt2\beta\). This is a genuine pole-residue cancellation, not a limit that discards a positive mode.

**Distinct relaxation rates.** For \(\kappa>\lambda\) the nonzero oscillatory term dominates at large lag, forcing infinitely many strict crossings. For \(\kappa<\lambda\) a nonzero real exponential dominates and fixes the eventual sign; when it cancels, the exact remaining sinusoid has infinitely many strict crossings. In the real-eigenvalue regime \(\chi\ge0\), the entire covariance is a finite real exponential polynomial (allowing polynomial factors at repeated roots); any nonzero such function has only finitely many zeros. It is nonzero since \(C(0)>0\).

**Equal-rate boundary.** For \(\kappa=\lambda\), the two terms have the common envelope \(e^{-\lambda t}\). Write their signed constant amplitude as \(H\) and oscillatory amplitude as \(L>0\). With \(r=\alpha/\beta\), direct substitution yields
\[
 \frac{|H|}{L}=
 \frac{\sqrt r\,|8-(r+1)^2|}{(r+1)\sqrt{3r^2+14r+3}}.
\]
In the complex regime \(3-2\sqrt2<r<3+2\sqrt2\). The exact sign factorization
\[
 (r+1)^2(3r^2+14r+3)-r[8-(r+1)^2]^2
 =-(r+3)(r^2-6r+1)(r^2+4r-1)
\]
shows \(L>|H|\) precisely for \(r>\sqrt5-2\). In that case the sinusoid-plus-constant crosses zero twice per period. Otherwise its sign is fixed, apart from tangencies. At \(r=\sqrt5-2\), \(2\beta^2-\lambda^2>0\), so \(H=L>0\): zeros are tangential, and the covariance never becomes negative. This completes the necessary-and-sufficient classification.

## Verification

Execute `python verify_run_pause_reverse.py` with Python, NumPy, SciPy, and SymPy installed. It checks the antisymmetric generator determinant, resolvent, real-mode coefficient, boundary factorization, and independently compares the closed covariance formula with a separate matrix-exponential covariance ODE over a range of rates and lag values. The executable currently passes 82 checks. These finite computations check transcription and sampled parameters; the proof above supplies the all-parameter and infinite-crossing conclusions.

## Relationship to prior work

Sadjadi and Shaebani [1] derive orientational memory in multistate runs/tumbles, including persistent/antipersistent behavior, but do not establish the harmonic-trap positional covariance sign-change trichotomy or its tuned pole cancellation. Garcia-Millan and Pruessner [2] treat run-and-tumble transport and harmonic confinement, but not this four-state finite-pause mandatory-reversal mechanism. Sun, Ye, and Podgornik [3] study finite tumble periods in a harmonic trap with an independently redrawn return direction, which differs from direction-preserving pause memory and mandatory reversal. Their stationary-moment results do not establish this sign-change classification. The new statement is the precise spectral-cancellation and equal-decay boundary classification, **not** the standard harmonic filtering formula or the earlier existence of antipersistent orientation dynamics. These distinctions concern statements and implications, not title overlap.

## Limitations

The claim depends on exponential run and pause dwell times, mandatory reverse-on-return, linear harmonic confinement, and absence of independent translational Brownian forcing. Other orientation kernels, nonexponential pauses, and nonlinear traps are not covered. Although an additive independent thermal OU component leaves the internal forcing modes unchanged, its positive real covariance could change the exact cancellation boundary; no such extension is asserted. The conclusion concerns stationary lag covariance, not a transient covariance initialized at an arbitrary internal state. The source literature provides more general methods, so independent priority review should examine possible implicit spectral implications.

## References

[1] H. Sadjadi and M. R. Shaebani, “Orientational Memory of Active Particles in Multistate Non-Markovian Processes,” arXiv:1909.05033v1 (2019-09-11), https://arxiv.org/abs/1909.05033.

[2] R. Garcia-Millan and G. Pruessner, “Run-and-tumble motion: field theory and entropy production,” arXiv:2012.02900v1 (2020-12-04), https://arxiv.org/abs/2012.02900.

[3] Y. Sun, F. Ye, and R. Podgornik, “Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap,” arXiv:2409.00578v1 (2024-09-01), https://arxiv.org/abs/2409.00578.
