# Sharp trace-moment thresholds and an anisotropic tail transition for two-sided Gaussian Nyström

## Finding
For every integer \(s\ge1\) and \(0<\varepsilon<1\), let \(A=\operatorname{diag}(1,\varepsilon)\), \(g\sim N(0,I_2)\), and independently \(\Psi\in\mathbb R^{2\times s}\) with iid standard Gaussian entries. Define the rank-one, two-sided generalized Nyström approximant and its trace by
\[
\widehat A_s=Ag\,(\Psi^{\mathsf T}Ag)^\dagger\Psi^{\mathsf T}A,\qquad T_s=\operatorname{tr}\widehat A_s.
\]
Here the pseudoinverse acts on an \(s\times1\) column. For independent \(X,Y\sim N(0,1)\), define
\[
\mu_\varepsilon=\frac{X^2+\varepsilon^3Y^2}{X^2+\varepsilon^2Y^2},\qquad
\tau_\varepsilon=\frac{\varepsilon(1-\varepsilon)|XY|}{X^2+\varepsilon^2Y^2}.
\]
Conditionally on \((X,Y)\), the *exact* distribution is
\[
T_s\ \stackrel d=\ \mu_\varepsilon+\tau_\varepsilon\frac{Z}{\sqrt{W_s}},
\]
where \(Z\sim N(0,1)\) and \(W_s\sim\chi^2_s\) are mutually independent and independent of \((X,Y)\). Thus, at every fixed nondegenerate \(\varepsilon\),
\[
\mathbb E|T_s|^p<\infty\quad\Longleftrightarrow\quad 0<p<s.
\]
For \(s\ge2\), \(\mathbb ET_s=(1+\varepsilon^2)/(1+\varepsilon)\). For \(s\ge3\),
\[
\operatorname{Var}(T_s)=\frac{s-1}{s-2}\frac{\varepsilon(1-\varepsilon)^2}{2(1+\varepsilon)^2}.
\]
The variance remains bounded below by \(\varepsilon(1-\varepsilon)^2/[2(1+\varepsilon)^2]>0\) no matter how many left sketch rows are added.

Both signed tails have the same sharp constant. For
\[
k_s=\frac{\Gamma((s+1)/2)}{s\sqrt\pi\,\Gamma(s/2)},\qquad C_s(\varepsilon)=k_s\,\mathbb E\tau_\varepsilon^s,
\]
we have
\[
\lim_{t\to\infty}t^s\Pr(T_s>t)
=\lim_{t\to\infty}t^s\Pr(T_s<-t)=C_s(\varepsilon)>0.
\]
At the two smallest left-sketch sizes the constants are explicit:
\[
C_1(\varepsilon)=\frac{2\varepsilon\log(1/\varepsilon)}{\pi^2(1+\varepsilon)},\qquad
C_2(\varepsilon)=\frac{\varepsilon(1-\varepsilon)^2}{8(1+\varepsilon)^2}.
\]
For each fixed integer \(s\ge2\), the sharp near-rank-one limit is
\[
\lim_{\varepsilon\downarrow0}\frac{C_s(\varepsilon)}{\varepsilon}=
\frac{k_s}{\pi}\,B\!\left(\frac{s+1}{2},\frac{s-1}{2}\right).
\]
Therefore one left row produces a logarithmically amplified near-rank-one tail, while two or more left rows have ordinary linear scaling. A finite absolute mean first appears at \(s=2\), and a finite variance first appears at \(s=3\).

## Assumptions and scope
All matrices and Gaussian variables are real, independent as stated, and evaluated in exact arithmetic. The right sketch has exactly one column; the \(s\) left columns are independent Gaussian probes. No rank truncation changes the already rank-one output. These results concern the signed *trace of the oblique approximation*, not the trace of a positive semidefinite symmetric Nyström approximation. The source matrix is positive definite for every fixed \(0<\varepsilon<1\). The endpoint \(\varepsilon=0\) is not included in moment or tail statements.

## Proof
**Gaussian reduction.** Write \(g=(X,Y)^{\mathsf T}\), \(v=Ag\), and \(w=A^2g\). The pseudoinverse identity for a nonzero column \(a=\Psi^{\mathsf T}v\) gives
\[
T_s=\frac{(\Psi^{\mathsf T}v)^{\mathsf T}(\Psi^{\mathsf T}w)}{\|\Psi^{\mathsf T}v\|^2}.
\]
Conditionally on \(g\), orthogonally decompose \(w=\mu v+w_\perp\), where \(\mu=v^{\mathsf T}w/\|v\|^2=\mu_\varepsilon\). The two Gaussian columns \(\Psi^{\mathsf T}v/\|v\|\) and \(\Psi^{\mathsf T}w_\perp/\|w_\perp\|\) are independent standard Gaussian \(s\)-vectors. Rotational invariance gives their normalized inner product as \(Z/\sqrt{W_s}\), and \(\|w_\perp\|/\|v\|=\tau_\varepsilon\); the latter identity follows by expanding the two-by-two Gram determinant as \(\varepsilon^2(1-\varepsilon)^2X^2Y^2\).

**Moment and tails.** With \(Z\) and \(W_s\) independent, \(\mathbb E|Z/\sqrt{W_s}|^p\) is finite precisely when \(p<s\); \(\mu_\varepsilon\in[\varepsilon,1]\), and \(0<\tau_\varepsilon\le(1-\varepsilon)/2\) almost surely. The positive-tail coefficient of \(Z/\sqrt{W_s}\) is \(k_s\): the \(\chi_s\) distribution near zero has CDF \(r^s/[2^{s/2}\Gamma(s/2+1)]+o(r^s)\), and \(\mathbb E(Z_+)^s=2^{s/2-1}\Gamma((s+1)/2)/\sqrt\pi\). Dominated convergence after conditioning, using the bounded location and scale, yields both signed constants.

**Exact angular integrals.** Write \((X,Y)=R(\cos\phi,\sin\phi)\), with \(\phi\) uniform on \([0,2\pi)\), and put \(Q=\varepsilon^2Y^2/(X^2+\varepsilon^2Y^2)\). Substituting \(u=\tan\phi\) in the angular integral gives
\[
\mathbb EQ=\frac\varepsilon{1+\varepsilon},\quad
\mathbb EQ^2=\frac{\varepsilon(1+2\varepsilon)}{2(1+\varepsilon)^2},\quad
\mathbb E\tau_\varepsilon=\frac{2\varepsilon\log(1/\varepsilon)}{\pi(1+\varepsilon)}.
\]
Here \(\mu_\varepsilon=1-(1-\varepsilon)Q\) and \(\tau_\varepsilon^2=(1-\varepsilon)^2Q(1-Q)\), so
\[
\operatorname{Var}(\mu_\varepsilon)=\mathbb E\tau_\varepsilon^2=
\frac{\varepsilon(1-\varepsilon)^2}{2(1+\varepsilon)^2}.
\]
The location gives the stated mean for \(s>1\). For \(s>2\), \(\mathbb E(1/W_s)=1/(s-2)\); conditional variance and total variance give the exact formula. The \(s=1\) and \(s=2\) tail constants follow from \(k_1=1/\pi\) and \(k_2=1/4\).

**Near-rank-one tail phase.** For integer \(s>1\), concentrate the angular integral defining \(\mathbb E\tau_\varepsilon^s\) near the two points where \(\cos\phi=0\). At each such point set \(\cos\phi=\varepsilon u\); dominated convergence (the limiting integrand decays as \(|u|^{-s}\), integrable exactly for \(s>1\)) yields
\[
\lim_{\varepsilon\downarrow0}\frac{\mathbb E\tau_\varepsilon^s}{\varepsilon}
=\frac1\pi\int_{-\infty}^{\infty}\frac{|u|^s}{(1+u^2)^s}\,du
=\frac1\pi B\!\left(\frac{s+1}{2},\frac{s-1}{2}\right).
\]
At \(s=1\), the integral has logarithmic divergence instead, and the exact angular expression supplies the sharp logarithmic factor. This proves all assertions.

## Verification
`VERIFY.py` (Python with NumPy and SciPy) numerically integrates the angular identities across five positive spectral ratios, checks the exact two-sided pseudoinverse trace against direct dense computations at four sketch sizes, verifies the orthogonal Gaussian scale identity, and compares the near-rank-one constants for four integer orders. All 64 assertions passed; see `VERIFICATION_OUTPUT.txt`. These finite checks support the formulas but do not substitute for the proof of tail limits or infinite moments.

## Relationship to prior work
Nakatsukasa (arXiv:2009.11392v1, §2) introduced and analyzed generalized Nyström approximations, including the oblique sketch and stabilization. Lam, Ceruti and Kressner (arXiv:2409.06384v1, §2.3) use generalized Nyström in randomized low-rank integrators and provide oversampled moment bounds. Those sources do not state an exact conditional Student law for the trace on this positive-definite family, the sharp one-, two-, and three-left-row moment boundaries, the finite-left-oversampling variance floor, or the logarithmic-to-linear near-rank-one tail transition. Classical Student-ratio and Gaussian angular identities are used as proof ingredients and are not claimed new. The comparison concerns the specifically stated unsafeguarded one-right-column, varying-left-row regime; it does not contradict the sources' oversampled matrix-error guarantees.

## Limitations
The conclusions are about a signed scalar trace of an oblique rank-one approximation in dimension two. They do not imply analogous moment thresholds for the matrix operator norm in all dimensions, or behavior of a complete differential-equation solver. Stabilized pseudoinverses, correlated left and right sketches, the symmetric PSD Nyström method, and floating-point behavior are not analyzed. Larger literature on Gaussian ratio distributions and oblique-projection statistics may contain equivalent formulations; scientific novelty is provisional pending independent literature review.

## References
1. Yuji Nakatsukasa, *Fast and stable randomized low-rank matrix approximation*, arXiv:2009.11392v1 (first public 2020-09-23), §2, https://arxiv.org/abs/2009.11392.
2. Hei Yin Lam, Gianluca Ceruti, Daniel Kressner, *Randomized low-rank Runge-Kutta methods*, arXiv:2409.06384v1 (first public 2024-09-10), §2.3, https://arxiv.org/abs/2409.06384.
