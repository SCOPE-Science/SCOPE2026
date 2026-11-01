# Sharp endpoint profiles of quadratic-residue phase multipliers on prime cycles

## Finding
Let \(p\) be any odd prime, and let \(\chi_p\) be its quadratic character. On complex-valued functions on \(\mathbb F_p\), define the convolution Fourier multiplier \(T_{p;u,v}\) by the Fourier symbol
\[
m(0)=0,\qquad m(\xi)=\begin{cases}u,&\chi_p(\xi)=1,\\v,&\chi_p(\xi)=-1,\end{cases}\qquad |u|=|v|=1.
\]
Here the zero-frequency multiplier **is zero**, not a freely chosen unit complex number. Put \(v/u=e^{i\theta}\), and define \(c=|\cos(\theta/2)|\), \(s=|\sin(\theta/2)|\). Then the complete complex \(\ell^\infty\)-operator-norm profile is
\[
\boxed{\|T_{p;u,v}\|_{\infty\to\infty}=\frac{p-1}{p}\begin{cases}
c+\sqrt{c^2+ps^2},&p\equiv1\pmod4,\\
c+\max\{c,\sqrt p\,s\},&p\equiv3\pmod4.
\end{cases}}
\]
Consequently, the **sharp phase-optimized norm** and **all relative maximizing phases** are
\[
\boxed{\max_{|u|=|v|=1}\|T_{p;u,v}\|_{\infty\to\infty}=\begin{cases}
\sqrt{p-1},&p\equiv1\pmod4,\\
\frac{p-1}{p}\sqrt{p+1},&p\equiv3\pmod4,\ p\ge7,\\
\frac43,&p=3.
\end{cases}}
\]
For \(p\equiv1\pmod4\), equality holds exactly when \(\cos\theta=(3-p)/(p-1)\). For \(p\equiv3\pmod4\) and \(p\ge7\), equality holds exactly when \(\cos\theta=(1-p)/(p+1)\). For \(p=3\), equality holds exactly when \(\theta\equiv0,\ 2\pi/3,\ -2\pi/3\pmod{2\pi}\). A common phase multiplying \(u,v\) is arbitrary throughout.

The universal zero-mean-unitary Fourier-multiplier upper bound \(\sqrt{p-1}\) is attained by this quadratic-residue family **if and only if \(p\equiv1\pmod4\)**. At those maximizing phases every convolution-kernel coefficient has the same modulus \(\sqrt{p-1}/p\). For \(p\equiv3\pmod4\), the sharp deficit is strictly positive; in particular for \(p\ge7\) it is
\[
\sqrt{p-1}-\frac{p-1}{p}\sqrt{p+1}>0.
\]
The maximizing input functions for the induced complex \(\ell^\infty\) norm are also classified: for each maximizing phase pair, they are exactly the unimodular translates of the conjugate-phase pattern of the convolution kernel, as specified in the proof.

**Application to imaginary powers.** For the five-vertex cycle, define the reduced discrete-Laplacian imaginary power \(L^{i\gamma}_{\mathrm{red}}\) by multiplier zero on constants and \(\lambda^{i\gamma}\) on every positive Laplacian eigenspace. Writing \(h=\log((3+\sqrt5)/2)\), one has
\[
\boxed{\|L^{i\gamma}_{\mathrm{red}}\|_{\infty\to\infty}
=\frac25\left[\sqrt{2+2\cos(\gamma h)}+2\sqrt{3-2\cos(\gamma h)}\right].}
\]
Its full range as \(\gamma\in\mathbb R\) is \([8/5,2]\); norm \(2\) occurs exactly when \(\gamma h\equiv\pm2\pi/3\pmod{2\pi}\), and norm \(8/5\) exactly when \(\gamma h\equiv0\pmod{2\pi}\).

## Assumptions and scope
All primes \(p\ge3\) are allowed, with both congruence classes covered. The domain and codomain are \(\mathbb C^{\mathbb F_p}\) with \(\|f\|_\infty=\max_x|f(x)|\); the norm is the **complex induced** norm, not the norm on the mean-zero subspace equipped with its inherited \(\ell^\infty\) norm. Fourier inversion uses
\[
\widehat f(\xi)=\sum_{x\in\mathbb F_p}f(x)e^{-2\pi ix\xi/p},\qquad
f(x)=\frac1p\sum_{\xi\in\mathbb F_p}\widehat f(\xi)e^{2\pi ix\xi/p}.
\]
Thus \((Tf)(x)=\sum_y k(x-y)f(y)\) with \(k(x)=p^{-1}\sum_\xi m(\xi)e^{2\pi ix\xi/p}\). Constants are annihilated, while the other \(p-1\) Fourier directions are multiplied by unit scalars. The five-cycle application uses \(Lf(x)=2f(x)-f(x+1)-f(x-1)\); the convention on its zero eigenspace is essential. No claim is made about arbitrary prime powers, composite cyclic groups, or exact finite-cycle imaginary-power norms beyond the five-cycle example.

## Proof
**1. Gauss sums and exact kernel.** Set \(S=(u+v)/2\), \(D=(u-v)/2\) and \(\zeta=e^{2\pi i/p}\). Then \(m(\xi)=S+D\chi_p(\xi)\) at nonzero \(\xi\), and \(m(0)=0\). The classical quadratic Gauss evaluation is
\[
\sum_{\xi\ne0}\chi_p(\xi)\zeta^{x\xi}
=\epsilon_p\sqrt p\,\chi_p(x)\quad(x\ne0),
\qquad\epsilon_p=\begin{cases}1,&p\equiv1\pmod4,\\i,&p\equiv3\pmod4.\end{cases}
\]
Together with \(\sum_{\xi\ne0}\zeta^{x\xi}=-1\) for \(x\ne0\), this yields
\[
k(0)=\frac{p-1}{p}S,\qquad
k(x)=\frac{-S+\epsilon_p\sqrt p\,\chi_p(x)D}{p}\quad(x\ne0).
\]
Up to a common unimodular factor \(e^{i(\arg u+\arg v)/2}\), one has \(S=\cos(\theta/2)\), \(D=-i\sin(\theta/2)\). For \(p\equiv1\pmod4\), the two nonzero quadratic-character classes therefore have the common kernel modulus \(p^{-1}\sqrt{c^2+ps^2}\). For \(p\equiv3\pmod4\), their moduli are \(p^{-1}|\cos(\theta/2)\mp\sqrt p\sin(\theta/2)|\). Each class occurs \((p-1)/2\) times, so their sum is \((p-1)p^{-1}\max\{c,\sqrt p\,s\}\), by \(|a+b|+|a-b|=2\max\{|a|,|b|\}\) for real \(a,b\). The displayed norm formulas follow from the elementary identity
\[
\|T\|_{\infty\to\infty}=\sum_{x\in\mathbb F_p}|k(x)|.
\]
For the reverse inequality in this identity, fix any output vertex \(x_0\) and choose each input value \(f(y)\) to have the conjugate phase of \(k(x_0-y)\) (with modulus one). The operator attains the row sum exactly.

**2. Exact optimization for primes one modulo four.** Parseval and the symbol moduli give \(\sum_x|k(x)|^2=(p-1)/p\), so Cauchy–Schwarz gives \(\sum_x|k(x)|\le\sqrt{p-1}\) for every \(p\) and every phase pair. Equality holds precisely when the \(p\) kernel moduli are all \(\sqrt{p-1}/p\). In the congruence-one case this is equivalent to
\[
(p-1)^2c^2=c^2+ps^2,
\]
which, using \(s^2=1-c^2\), is equivalent to \(c^2=1/(p-1)\). As \(p\ge5\), the equation has exactly two relative phase solutions modulo \(2\pi\), characterized by \(\cos\theta=2c^2-1=(3-p)/(p-1)\). Every such solution makes the kernel flat and gives equality in the universal bound. There are no other maximizing phases by the equality condition of Cauchy–Schwarz.

**3. Exact optimization for primes three modulo four.** If \(c\ge\sqrt p\,s\), the profile is \(2(p-1)c/p\), at most \(2(p-1)/p\), attained only at \(c=1\). If \(c\le\sqrt p\,s\), ordinary planar Cauchy–Schwarz gives
\[
c+\sqrt p\,s\le\sqrt{p+1},
\]
with equality precisely at \(c=1/\sqrt{p+1}\), \(s=\sqrt p/\sqrt{p+1}\). This point lies strictly in the indicated region for each prime \(p\ge3\). For \(p\ge7\), \(\sqrt{p+1}>2\), so only the latter branch maximizes, giving the two phases \(\cos\theta=(1-p)/(1+p)\). For \(p=3\), both branches attain \(4/3\): \(c=1\) means \(\theta\equiv0\), while the second equality condition yields \(\theta\equiv\pm2\pi/3\). No further equality cases occur. Finally, for \(p\ge7\),
\[
\left(\frac{p-1}{p}\sqrt{p+1}\right)^2
=(p-1)\left(1-\frac1{p^2}\right)<p-1.
\]
For \(p=3\), \(4/3<\sqrt2\). This proves the universal-bound parity dichotomy with strict odd-three-class gaps.

**4. Equality vectors and spectral interpretation.** At every maximizing relative phase in steps 2–3, all kernel coefficients are nonzero (because \(c>0\), and \(c\ne\sqrt p\,s\) in the congruence-three large-prime case). Equality in the triangle inequality in any row, together with \(\|f\|_\infty=1\), forces \(|f(y)|=1\) for every \(y\) and identical phases for the products \(k(x_0-y)f(y)\). Therefore all nonzero maximizing vectors are exactly scalar multiples of
\[
f_{x_0}(y)=\frac{\overline{k(x_0-y)}}{|k(x_0-y)|},\qquad x_0\in\mathbb F_p,
\]
with an arbitrary unimodular scalar and (for this classification) normalized input supremum norm one. Conversely all those vectors attain the norm. This is an equality classification of the **induced** endpoint operator norm, not of a restricted mean-zero problem.

**5. Five-cycle imaginary powers.** On the cyclic graph of order five the nonzero Laplacian eigenvalues are \(\lambda_1=\lambda_4=(5-\sqrt5)/2\) and \(\lambda_2=\lambda_3=(5+\sqrt5)/2\). The frequencies \(\{1,4\}\) are precisely the nonzero quadratic residues and \(\{2,3\}\) the nonresidues modulo five. Therefore \(L^{i\gamma}_{\mathrm{red}}\) is exactly \(T_{5;u,v}\) with \(u=\lambda_1^{i\gamma}\), \(v=\lambda_2^{i\gamma}\), and \(\theta=\gamma h\) modulo \(2\pi\), where \(h=\log(\lambda_2/\lambda_1)=\log((3+\sqrt5)/2)>0\). Substitution in the congruence-one formula gives the displayed expression. The maximum and its complete parameter set follow from step 2; the minimum occurs at \(c=1\), because the profile \((4/5)(c+\sqrt{5-4c^2})\) on \([0,1]\) has one interior critical point, a strict maximum, and its endpoint values are \(8/5\) (at \(c=1\)) and \(4\sqrt5/5\) (at \(c=0\)). Continuity gives every intermediate value.

## Verification
Run `python3 CHECK.py` from the directory containing this document. The checker uses only the Python standard library and independently constructs the inverse discrete Fourier kernels for every odd prime below two hundred at multiple relative phases. It verifies the two exact formulas numerically to fixed tolerances and tests the maximizing phase sets and flat-kernel property. It additionally constructs the five-cycle reduced imaginary power directly in the Fourier basis and compares against the closed expression. The checker is supplementary: all-prime correctness comes from the Gauss-sum identities and exact analytic optimizations above; floating-point tests do not certify infinitely many primes.

## Relationship to prior work
Bui, Bui and Cao (2026) study sharp *growth rates* for imaginary powers of the discrete Laplacian on the infinite lattice \(\mathbb Z^d\), in Hardy spaces and \(\ell^p\) for \(1<p<\infty\); their operator has no nontrivial constant eigenspace in \(\ell^2\). That theorem does not determine finite prime-cycle zero-mode-killed endpoint norms or their optimizing Paley phases. Benedetto, Benedetto and Woodworth (2011) describe Björck and Legendre-character sequences with a *unit* zeroth value and study constant-amplitude, zero-autocorrelation signals and ambiguity bounds; the present symbol has **zero zeroth value** and solves a different exact endpoint optimization. In the congruence-three case, the resulting optimal nonresidue phase coincides with a classical Björck phase, which is credited as a genuine shared parameter, not as a separate newly discovered phase formula. Green and Green (2003) treat root-of-unity phase alphabets, multiplicative residue cosets and periodic autocorrelation; they do not state the continuously optimized two-band zero-DC Fourier-algebra norm or the congruence-class sharp equality classification. Sahasranand (2021) studies induced norms of a special *real* constant-off-diagonal circulant family, which cannot imply the complex two-band profile. Existing work on Paley fourth moments, multiplicative-character restriction spectra and cubic-residue Fourier projection Lebesgue constants concerns different norms or supports. The classical Gauss evaluation, Fourier inversion and Cauchy–Schwarz are prerequisites, not new contributions.

## Limitations
The exact endpoint result is for two unimodular quadratic-residue phase bands and a vanishing DC multiplier, not arbitrary multipliers, nor arbitrary distributions of spectral phases. The equality characterization is for complex \(\ell^\infty\), not real inputs or the inherited norm on the mean-zero subspace. The five-cycle example is not a general theorem about imaginary powers on all finite cycles. The explicit parity split uses primality and the classical sign of quadratic Gauss sums. Related Björck, Paley and difference-set constructions are classical, and a previously unindexed equivalent endpoint-norm calculation remains a bibliographic risk; novelty is assessed only relative to the specifically inspected sources.

## References
1. T. A. Bui, T. Q. Bui and T. T. Cao, *Sharp estimates for imaginary powers of discrete Laplacians*, arXiv:2610.27385, initially posted 2026-10-19, especially Theorems 1.1–1.2 and Section 3.4.
2. J. J. Benedetto, R. L. Benedetto and J. T. Woodworth, *Optimal ambiguity functions and Weil's exponential sum bound*, arXiv:1107.1887, initially posted 2011-07-10, especially Section 2 on Björck sequences and Section 3 on character sums.
3. D. H. Green and P. R. Green, *Polyphase power-residue sequences*, Proceedings of the Royal Society A **459** (2003), 817–827, DOI:10.1098/rspa.2002.1065, especially Sections 2–4 and 7 on residue cosets and correlations.
4. K. R. Sahasranand, *The p-norm of circulant matrices via Fourier analysis*, arXiv:2111.11389, initially posted 2021-11-22.
5. Standard quadratic Gauss-sum identity: \(\sum_{x\in\mathbb F_p}\chi_p(x)e^{2\pi i ax/p}=\epsilon_p\chi_p(a)\sqrt p\) for nonzero \(a\), where \(\epsilon_p=1\) or \(i\) according as \(p\equiv1\) or \(3\pmod4\).
