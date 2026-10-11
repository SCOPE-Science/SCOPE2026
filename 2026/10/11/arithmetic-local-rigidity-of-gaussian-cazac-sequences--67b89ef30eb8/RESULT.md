# Arithmetic local rigidity of Gaussian CAZAC sequences

## Finding

Let \(N\ge2\), let \(a\in\mathbb Z\) be coprime to \(N\), and set \(\varepsilon=N\bmod 2\). On \(\mathbb Z/N\mathbb Z\), define the Gaussian chirp
\[
 u_j=\exp\!\left(\frac{\pi i a}{N}j(j+\varepsilon)\right),\qquad j=0,\ldots,N-1.
\]
This is a well-defined periodic constant-amplitude zero-autocorrelation (CAZAC) vector. Let \(d=d(N)=\prod_{p^v\parallel N}p^{\lfloor v/2\rfloor}\), so that \(d^2\mid N\), and let \(T_d\subset\mathbb R^N\) be the \(d\)-dimensional space of real \(d\)-periodic vectors. For real phases \(\theta\), write \(u^\theta_j=u_je^{i\theta_j}\) and define the unnormalized correlation energy
\[
 \mathcal E(\theta)=\sum_{s=1}^{N-1}\left|\sum_{j=0}^{N-1}u^\theta_{j+s}\overline{u^\theta_j}\right|^2.
\]
All indices are interpreted modulo \(N\). There is a neighborhood \(U\) of the origin in \(\mathbb R^N\) such that
\[
 \{\theta\in U:\mathcal E(\theta)=0\}=U\cap T_d.
\]
Thus, **every** CAZAC sequence sufficiently close in coordinate phases to the Gaussian chirp is obtained by multiplying it by an arbitrary \(d\)-periodic unimodular sequence. Modulo global phase, the local solution space is a smooth torus germ of dimension \(d-1\). It is discrete at the chirp for squarefree \(N\), without claiming global finiteness of all CAZAC vectors.

The proof also yields the *exact real Hessian*. For the unitary Fourier transform
\[
 \widehat h(k)=N^{-1/2}\sum_{j=0}^{N-1}h_j\exp(-2\pi i k j/N),
\]
we have, for every \(h\in\mathbb R^N\),
\[
 \mathcal E(th)=4Nt^2\sum_{s=1}^{N-1}\sin^2\!\left(\frac{\pi a s^2}{N}\right)|\widehat h(-as)|^2+O_h(t^3).
\]
Consequently, the Hessian has, at Fourier frequency \(k\), eigenvalue
\[
 \mu_k=8N\sin^2\!\left(\frac{\pi a^{-1}k^2}{N}\right),
\]
where \(a^{-1}\) is any inverse of \(a\) modulo \(N\) (the value is independent of the representative), and its kernel is **exactly** \(T_d\), of dimension \(d\). These frequency labels give the real spectrum, with the usual conjugate-pair interpretation for real Fourier modes.

Writing \(\sigma_{N,a}=\min_{1\le s<N,\ N\nmid s^2}\sin^2(\pi a s^2/N)>0\), a possibly smaller neighborhood \(U\) satisfies the quantitative local error bound
\[
 \mathcal E(\theta)\ge 2N\sigma_{N,a}\,\operatorname{dist}(\theta,T_d)^2\qquad(\theta\in U),
\]
where distance is Euclidean in the real phase coordinates.

## Assumptions and scope

The integer \(N\) may be composite and may be even. Only \(\gcd(a,N)=1\) is required. For odd \(N\), using \(j(j+1)\) ensures periodicity; for even \(N\), using \(j^2\) does so. The Fourier transform and correlation energy use the normalizations displayed above; in particular, autocorrelations are *not* divided by \(N\). Locality is in a sufficiently small real coordinate-phase neighborhood. The assertion is not a classification of all CAZAC sequences of length \(N\).

## Proof

**1. Chirp periodicity and cancellation.** One computes
\[
 \frac{u_{j+N}}{u_j}=\exp(\pi i a(2j+N+\varepsilon))=1
\]
and, for a shift \(s\),
\[
 u_{j+s}\overline{u_j}=\gamma_s\exp(2\pi i a s j/N),\qquad
 \gamma_s=\exp\!\left(\frac{\pi i a}{N}s(s+\varepsilon)\right).
\]
Since \(a\) is invertible modulo \(N\), this sum vanishes for every nonzero shift.

**2. The full periodic phase family consists of CAZAC vectors.** Set \(m=N/d\). The definition of \(d\) gives \(d\mid m\). For \(\phi\in T_d\), group the correlation sum for \(u^\phi\) into \(j=r+dt\), with \(0\le r<d\) and \(0\le t<m\). The inner geometric sum in \(t\) is zero unless \(m\mid as\), equivalently \(m\mid s\). In that remaining case \(d\mid m\mid s\), so \(\phi_{j+s}-\phi_j=0\) and the correlation is exactly that of \(u\), namely zero for nonzero \(s\). Therefore \(\mathcal E(\phi)=0\) for all \(\phi\in T_d\).

**3. Linearization and Fourier diagonalization.** Differentiating the shift correlation at zero in any direction \(h\in\mathbb R^N\) yields
\[
 D A_s(0)[h]
 =i\gamma_s\sum_j e^{2\pi i a s j/N}(h_{j+s}-h_j)
 =i\gamma_s\bigl(e^{-2\pi i a s^2/N}-1\bigr)\sqrt N\,\widehat h(-as).
\]
Every \(A_s(0)\) is zero. Squaring these differentials proves the displayed quadratic Taylor expansion. Because \(s\mapsto -as\) permutes the nonzero Fourier frequencies, this also proves the exact Hessian spectrum. If \(k=-as\pmod N\), the factor \(\sin^2(\pi a s^2/N)\) equals \(\sin^2(\pi a^{-1}k^2/N)\). No imaginary-versus-real rank doubling is used: the Fourier transform is unitary on the complexification and diagonalizes a real circulant quadratic form.

**4. Arithmetic nullity.** The multiplier vanishes exactly for \(N\mid s^2\). For each prime power \(p^v\parallel N\), this is equivalent to \(p^{\lceil v/2\rceil}\mid s\). Hence \(m=N/d=\prod p^{\lceil v/2\rceil}\) divides \(s\). There are precisely \(d\) such residues \(s\) modulo \(N\), including zero. Their corresponding Fourier indices \(-as\) are precisely the multiples of \(m\), which characterize real \(d\)-periodic vectors. Thus \(\ker D^2\mathcal E(0)=T_d\).

**5. Local exhaustion and stability.** Orthogonally decompose \(\theta=x+y\), where \(x\in T_d\) and \(y\perp T_d\). The smooth nonnegative function \(\mathcal E\) is identically zero on \(T_d\) by Step 2. Thus \(\nabla\mathcal E(x)=0\) at every such \(x\). At the origin its Hessian, restricted to \(T_d^\perp\), has smallest eigenvalue \(8N\sigma_{N,a}\). By continuity, on a small enough ball the same restricted quadratic form is bounded below by \(4N\sigma_{N,a}\|y\|_2^2\). Integrating the second derivative along \(x+ty\) gives
\[
 \mathcal E(x+y)=\int_0^1(1-t)D^2\mathcal E(x+ty)[y,y]dt
 \ge2N\sigma_{N,a}\|y\|_2^2.
\]
It follows that \(\mathcal E(x+y)=0\) locally if and only if \(y=0\); equality for \(y=0\) is already proved. Quotienting the \(d\)-periodic phases by their common constant phase gives dimension \(d-1\). This argument establishes all quantifiers for each fixed \(N,a\), without asserting a neighborhood uniform in \(N\).

## Verification

Run `python3 verify.py` using Python 3 and only its standard library. The checker computes complex periodic autocorrelations, tests arbitrary nontrivial periodic phase modulations, compares the analytic Fourier quadratic form with the direct first derivative of every autocorrelation, and checks centered finite differences. It tests every invertible chirp multiplier for lengths \(2\le N\le26\), including squareful lengths and both parities. Expected output is of the form `VERIFY_OK n=2..26 units_checked=211 squareful_cases=66` followed by numerical error bounds. The finite sample is illustrative only; the proof covers every integer length and every coprime multiplier.

## Relationship to prior work

Gilbert and Rzeszotnik's harmonic-analysis paper (2010, primary classification 42C40) characterizes finite-group Fourier extremizers involving biunimodular functions and discusses Gauss sequences; it does not supply a general phase-Hessian spectrum or a local chirp-moduli theorem. Führ and Rzeszotnik's arXiv preprint (first public June 19, 2015) reviews Gaussian biunimodular vectors and the Björck–Saffari finiteness conjecture, and studies generic unitary matrices; its results do not state this arithmetic local classification at Gaussian vectors. Benedetto, Cordwell, and Magsino (2018), especially Theorems 2.9 and 2.11, construct continuous families for squareful lengths. The present result *does not claim that construction as new*: it adds a precise Gaussian-point tangent dimension, an exact transverse Hessian spectrum, a stability inequality, and **local exhaustiveness**, which is not a consequence merely of constructing examples. A preexisting equivalent special-point deformation theorem under circulant-Hadamard terminology remains possible.

## Limitations

This theorem is local at Gaussian chirps. It does not prove that the full squarefree CAZAC moduli set is finite or classify its other points, nor does it determine a global lower energy bound. The stability radius is existential and depends on \(N,a\); no optimal radius is claimed. The numerical checker does not prove the theorem or exhaust larger lengths. An independent literature audit has not been performed.

## References

1. J. Gilbert and Z. Rzeszotnik, *The norm of the Fourier transform on finite abelian groups*, Annales de l'Institut Fourier **60** (2010), 1317–1346, DOI `10.5802/aif.2556`, primary MSC 42C40. Full text: `https://www.numdam.org/article/AIF_2010__60_4_1317_0.pdf`.
2. H. Führ and Z. Rzeszotnik, *On biunimodular vectors for unitary matrices*, arXiv `1506.06738v1`, first public 2015-06-19, `https://arxiv.org/abs/1506.06738`.
3. J. J. Benedetto, K. Cordwell, and M. Magsino, *CAZAC sequences and Haagerup's characterization of cyclic N-roots*, 2018 manuscript, `https://www.math.umd.edu/~jjb/2018-03-17BCMcazac.pdf`, notably §2.4.
4. G. Björck and B. Saffari, *New classes of finite unimodular sequences with unimodular Fourier transforms: circulant Hadamard matrices with complex entries*, C. R. Acad. Sci. Paris Sér. I **320** (1995), 319–324 (cited via the primary full-text sources above).
