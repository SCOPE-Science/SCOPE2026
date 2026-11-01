# Two Poisson wavelets suffice for sampled sign retrieval without bandlimiting

## Finding
Fix a real number \(p>0\). Define the order-\(p\) Poisson wavelet by the Fourier convention \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i t\xi}\,dt\) and
\[
\widehat{P_p}(\xi)=(2\pi)^{p+1/2}|\xi|^p e^{-2\pi|\xi|}.
\]
Let \(\mathcal H\) denote the real Hilbert transform, with Fourier multiplier \(-i\operatorname{sgn}(\xi)\). For every \(\alpha>1\), \(\beta>0\), put
\[
\Lambda_{\alpha,\beta}=\{(\beta n\alpha^m,\alpha^m):m,n\in\mathbb Z\}.
\]
**Theorem.** If
\[
\boxed{\beta+\log\alpha\le \frac{e^{-4p}}{200},}
\]
then for every pair of **real-valued** signals \(f,g\in L^2(\mathbb R)\), the identities
\[
|\mathcal W_{P_p}f(b,a)|=|\mathcal W_{P_p}g(b,a)|,\qquad
|\mathcal W_{\mathcal HP_p}f(b,a)|=|\mathcal W_{\mathcal HP_p}g(b,a)|
\quad((b,a)\in\Lambda_{\alpha,\beta})
\]
imply \(f=g\) or \(f=-g\), almost everywhere. Thus **two** fixed real-valued analyzing wavelets, with a fully discrete and explicitly sufficiently dense sampling lattice, uniquely recover every real square-integrable signal up to global sign, without a bandlimit hypothesis.

## Assumptions and scope
The continuous wavelet transform uses the standard dilation normalization
\[
\mathcal W_{\phi}f(b,a)=a^{-1/2}\int_{\mathbb R}f(t)\overline{\phi((t-b)/a)}\,dt,
\qquad b\in\mathbb R,\quad a>0.
\]
The assertion is for the **two separate magnitude channels**, not the magnitude of their complex sum. The lattice contains every integer scale index \(m\in\mathbb Z\); the parameter condition is sufficient, not asserted sharp. No signal-specific assumptions, finite support, decay, nonvanishing, or bandlimiting are imposed beyond real-valued \(L^2\) membership.

For \(q>1\), write \(\mathcal A_q(\mathbb H)\) for the holomorphic weighted Bergman space on \(\mathbb H=\{x+iy:y>0\}\) with squared norm
\[
\|F\|_{\mathcal A_q}^2=\int_{\mathbb H}|F(x+iy)|^2 y^{q-2}\,dx\,dy.
\]

## Proof
**Step 1: a quantitatively dense real-harmonic uniqueness lattice.** We prove the following lemma for all real \(s\ge0\). If \(u\) is real-valued, harmonic on \(\mathbb H\), has finite \(\int_{\mathbb H}|u(z)|^2(\Im z)^s\,dA(z)\), and vanishes at every \(\beta n\alpha^m+i\alpha^m\), then
\[
\beta+\log\alpha\le e^{-s}/200\quad\Longrightarrow\quad u\equiv0.
\]
Set \(t=\log\alpha\), \(\delta=\beta+t\), \(h_m=e^{mt}\), and \(z_{mn}=h_m(\beta n+i)\). The half-plane, up to null boundaries, is tiled by
\[
Q_{mn}=\left\{x+iy:\ \beta h_m(n-1/2)\le x<\beta h_m(n+1/2),\quad h_me^{-t/2}\le y<h_me^{t/2}\right\}.
\]
The hypothesis gives \(0<t,\beta\le\delta\le1/200\). Each tile point is within \(\delta h_m\) of its node; indeed the horizontal deviation is at most \(\beta h_m/2\) and the vertical deviation at most \((t/2)e^{t/2}h_m\). Consequently, for every point \(w\) on the segment from \(z_{mn}\) to a point of \(Q_{mn}\), the Euclidean disk \(B(w,h_m/4)\) lies within \(B(z_{mn},h_m/3)\subset\mathbb H\).

For any real harmonic function and a disk of radius \(R\) contained in its domain, differentiation of the disk mean-value identity, followed by Cauchy–Schwarz, yields
\[
|\nabla u(w)|^2\le\frac8{\pi R^4}\int_{B(w,R)}|u(\zeta)|^2\,dA(\zeta).
\]
Explicitly, each partial derivative equals \(4/(\pi R^4)\) times the disk integral of the corresponding centered coordinate multiplied by \(u\); the disk second moment is \(\pi R^4/4\). Since \(u(z_{mn})=0\), the preceding disk inclusion and the mean-value estimate imply, for every \(z\in Q_{mn}\),
\[
|u(z)|^2\le \frac{2048}{\pi}\delta^2h_m^{-2}
\int_{B(z_{mn},h_m/3)}|u(\zeta)|^2\,dA(\zeta).
\tag{1}
\]
For \(s\ge0\), the weighted area of a tile obeys
\[
\int_{Q_{mn}}y^s\,dA\le e^{s+1}\beta t h_m^{s+2}.
\tag{2}
\]
Each point \(x+iy\) belongs to at most \(3/(\beta t)\) of the disks \(B(z_{mn},h_m/3)\). Indeed, membership forces \(3y/4<h_m<3y/2\) (fewer than \((\log2)/t+1\) values of \(m\)); for each such \(m\), fewer than \(2/(3\beta)+1\) integers \(n\) can have \(|x-\beta n h_m|<h_m/3\). Their product is below \(3/(\beta t)\) since \(\beta,t\le1/200\). Moreover, membership implies \(h_m^s\le(3/2)^s y^s\). Multiplying (1) by \(y^s\), integrating using (2), and summing tiles gives
\[
\|u\|_{L^2(y^s)}^2\le
\frac{6144}{\pi}e^{s+1}(3/2)^s\delta^2\|u\|_{L^2(y^s)}^2.
\tag{3}
\]
Under \(\delta\le e^{-s}/200\), the numerical coefficient in (3) is at most
\[
\frac{6144e}{40000\pi}\left(\frac{3}{2e}\right)^s
\le\frac{6144e}{40000\pi}<0.134<1.
\]
The norm is finite by hypothesis, hence must vanish. Harmonic continuity then gives \(u\equiv0\), proving the lemma.

**Step 2: squaring transfers the two channels to one harmonic sampled quantity.** Define the Cauchy wavelet \(\psi_p=(P_p+i\mathcal HP_p)/2\), and, for a real signal \(f\), define
\[
F_f(b+ia)=a^{-p-1/2}\mathcal W_{\psi_p}f(b,a).
\]
The Cauchy-wavelet/Bergman isometry identifies \(F_f\) with an element of \(\mathcal A_{2p+1}(\mathbb H)\), and the map \(f\mapsto F_f\) is injective on real \(L^2\) signals (see the first reference). The exact real/imaginary relations are
\[
\mathcal W_{P_p}f(b,a)=2a^{p+1/2}\Re F_f(b+ia),\qquad
\mathcal W_{\mathcal HP_p}f(b,a)=-2a^{p+1/2}\Im F_f(b+ia).
\]
The two magnitude equalities therefore force
\[
\Re\bigl(F_f(z)^2-F_g(z)^2\bigr)=0
\qquad(z=\beta n\alpha^m+i\alpha^m).
\tag{4}
\]
Here the elementary identity is \(\Re((a+ib)^2)=a^2-b^2\): the two separate magnitudes determine this difference of squares without determining either sign.

**Step 3: the square belongs to the necessary weighted space.** For every \(q>1\), the standard disk mean-value estimate yields the uniform point-evaluation bound
\[
|F(x+iy)|^2\le C_q y^{-q}\|F\|_{\mathcal A_q}^2.
\]
Consequently \(F\in\mathcal A_q\) implies \(F^2\in\mathcal A_{2q}\), since
\[
\int_{\mathbb H}|F|^4y^{2q-2}\,dA
\le C_q\|F\|_{\mathcal A_q}^2\int_{\mathbb H}|F|^2y^{q-2}\,dA<\infty.
\]
In particular \(G=F_f^2-F_g^2\in\mathcal A_{4p+2}\), and its real part \(u=\Re G\) is a real harmonic function with finite \(\int_{\mathbb H}|u|^2y^{4p}\,dA\).

**Step 4: finish by holomorphic rigidity.** Apply the lemma with \(s=4p\) to (4). It gives \(\Re G\equiv0\). A holomorphic function whose real part vanishes identically is a purely imaginary constant. The only constant in \(\mathcal A_{4p+2}(\mathbb H)\) is zero, so \(F_f^2=F_g^2\). Factoring holomorphically gives \(F_f=F_g\) identically or \(F_f=-F_g\) identically. Injectivity of the Cauchy transform on real \(L^2\) yields \(f=\pm g\) almost everywhere, as claimed.

## Verification
The proof uses an exact disk mean-value derivative identity, an explicit tile-and-overlap estimate, weighted Bergman point evaluation, and an elementary holomorphic factorization. The downloadable accompanying standard-library script `checks/proof_checks.py` checks the decisive numerical constants, tile geometry, overlap upper bound, and quadratic identity on representative parameters. It is **supplementary**: no finite test or numeric computation establishes the quantified harmonic sampling lemma or the theorem; those are proved above.

## Relationship to prior work
Alaifari, Bartolucci and Wellershoff (first publicly posted February 16, 2023; journal publication 2024) prove a **three**-real-wavelet theorem for the same Poisson/Hilbert-transform family on a hyperbolic lattice. Their Theorem 3.3 assumes \(\beta\log\alpha\le4\pi/(1+4p)\); the published introduction explicitly asks whether **two** such wavelets could suffice. Their two-window *linear frame* condition does not imply two-window *phaseless* injectivity. Here the independent harmonic real-part sampling lemma supplies the missing implication at the considerably stronger density condition \(\beta+\log\alpha\le e^{-4p}/200\).

Their earlier paper on wavelet phase retrieval of bandlimited signals (arXiv:2009.05029) does not assert the universal real \(L^2\), no-bandlimit conclusion. Chen's 2026 multi-wavelet discrete theorem, according to its accessible abstract, uses eight windows and a connectivity assumption for complex signals; it is not a two-Poisson-window theorem. Searches of relevant published and indexed mathematical records did not identify an equivalent two-window statement. That does not establish exhaustive historical priority; the result remains subject to independent literature verification.

## Limitations
Only **real-valued** signals are treated; no analogous complex-signal conclusion follows. The explicit sampling requirement is intentionally conservative and far denser than the earlier three-wavelet result; there is no claim of optimal density, numerical reconstruction, noise stability, a single-window theorem, or finite-sample recovery. The harmonic lemma assumes a globally finite weighted area norm, verified here for the squared Cauchy transforms rather than for arbitrary harmonic functions outside that class. Historical novelty and the mathematical argument have not been independently audited.

## References
1. R. Alaifari, F. Bartolucci and M. Wellershoff, *Unique wavelet sign retrieval from samples without bandlimiting*, arXiv:2302.08129 (first posted February 16, 2023); *Proceedings of the American Mathematical Society, Series B* **11** (2024), 330–344; DOI: 10.1090/bproc/201. Final open-access paper: https://pure.tudelft.nl/ws/portalfiles/portal/221817149/S2330-1511-2024-00201-4.pdf.
2. R. Alaifari, F. Bartolucci and M. Wellershoff, *Phase retrieval of bandlimited functions for the wavelet transform*, arXiv:2009.05029; DOI: 10.1016/j.acha.2023.01.002.
3. G. Chen, *Stable Multi-Wavelet Phase Retrieval under Discrete Sampling*, SSRN:6088707 (posted January 18, 2026); DOI: 10.1016/j.rinam.2026.100706 (2026). The accessible abstract concerns eight windows and additional assumptions.
