# Golden-ratio optimality for resonant three-line exponential phase retrieval

## Finding
Fix \(h>0\) and a third-line ratio \(0<\alpha<1\). For each integer \(k\ge1\), set \(a_k=\pi k/(2h)\) and consider the two-dimensional entire-function space
\[
\mathcal E_k=\{F(z)=c e^{a_k z}+d e^{-a_k z}:c,d\in\mathbb C\}.
\]
The three horizontal measurement lines have heights \(0,h,\alpha h\). The following statements hold, with all singular values taken in ordinary Euclidean norms and equal weight for each line.

**Four-point phase retrieval.** For any fixed \(r>0\), the four squared-magnitude samples at \(-r/a_k,0,r/a_k,i\alpha h\) determine every member of \(\mathcal E_k\) up to one constant unimodular factor if and only if \(\sin(\pi k\alpha)\ne0\). No three point-evaluation magnitudes anywhere in the complex plane can do this for every member of \(\mathcal E_k\). In particular, this four-point scheme works at every positive frequency index \(k\) exactly when \(\alpha\) is irrational.

**Exact interference spectrum.** Write \(u=|c|^2\), \(v=|d|^2\), \(U=\operatorname{Re}(c\overline d)\), \(V=\operatorname{Im}(c\overline d)\). The coefficient of the constant-in-\(x\) interference in \(|F(x+iy)|^2\), divided by two, is \(U\cos(2a_k y)-V\sin(2a_k y)\). Its three-line measurement matrix is
\[
A_{k,\alpha}=\begin{pmatrix}1&0\\(-1)^k&0\\\cos(\pi k\alpha)&-\sin(\pi k\alpha)\end{pmatrix}.
\]
Consequently the exact squared singular values are
\[
\lambda_\pm(k,\alpha)=\frac{3\pm\sqrt{9-8\sin^2(\pi k\alpha)}}2.
\]
This spectrum concerns the interference-coefficient map, **not** the unprocessed full-line intensity map.

**Sharp arithmetic design law.** Put \(s_k(\alpha)=\sqrt{\lambda_-(k,\alpha)}\) and \(\gamma_N(\alpha)=\min_{1\le k\le N}s_k(\alpha)\). For every irrational \(\alpha\in(0,1)\),
\[
\boxed{\liminf_{N\to\infty}N\gamma_N(\alpha)
=\pi\sqrt{\frac23}\liminf_{q\to\infty}q\,\|q\alpha\|_{\mathbb R/\mathbb Z}.}
\]
The left side is positive if and only if \(\alpha\) is badly approximable. Among all irrational choices of the third-line ratio, its sharp supremum is
\[
\boxed{\sup_{\alpha\in(0,1)\setminus\mathbb Q}\liminf_{N\to\infty}N\gamma_N(\alpha)
=\pi\sqrt{\frac{2}{15}},}
\]
attained at the golden-ratio conjugate \(\alpha=(\sqrt5-1)/2\). For rational \(\alpha\), some \(s_k\) vanish identically; for every irrational \(\alpha\), the condition numbers are nevertheless unbounded with \(k\).

**Concrete phase-separated near-collisions.** Define \(F_k(z)=e^{a_kz}+i e^{-a_kz}\) and \(G_k(z)=e^{a_kz}-i e^{-a_kz}\). They are never unimodular multiples. At the first two lines their squared magnitudes agree for every real \(x\); at the third line their squared-intensity difference is exactly \(4\sin(\pi k\alpha)\), independent of \(x\). Yet, with \(r=(\log2)/2\), the two vectors of values at \(\pm r/a_k\) have phase-quotient distance exactly \(\sqrt2\) in \(\mathbb C^2\). Thus the small interference singular values represent genuine near-indistinguishability, not convergence of the underlying functions modulo phase.

## Assumptions and scope
All coefficients \(c,d\) are arbitrary complex numbers, including zero; \(r>0\) is fixed but arbitrary; the exponential frequency \(a_k\) is real and positive. The measured magnitudes are squared. On the three infinite lines we extract the constant-in-\(x\) interference coefficient; the three-line spectral law uses that *derived* data with equal weights. The four-point statement uses raw squared magnitudes. The result concerns only the indicated two-exponential entire-function sectors; it is not a uniform stability theorem for general entire functions or Gabor phase retrieval in an infinite-dimensional signal space.

## Proof
**1. Exact intensity decomposition.** Direct multiplication gives, for real \(x,y\),
\[
|F(x+iy)|^2=u e^{2a_kx}+v e^{-2a_kx}+2\bigl[U\cos(2a_ky)-V\sin(2a_ky)\bigr].
\]
This identifies the phase-invariant Hermitian rank-one matrix \(\begin{psmallmatrix}u&U+iV\\U-iV&v\end{psmallmatrix}\), with \(uv=U^2+V^2\), and proves the formula for \(A_{k,\alpha}\).

**2. Four raw samples and minimality.** Denote the three intensities on height zero at real arguments \(0,\pm r/a_k\) by \(I_0,I_+,I_-\). Then
\[
u+v=\frac{I_++I_--2I_0}{2(\cosh(2r)-1)},\quad
u-v=\frac{I_+-I_-}{2\sinh(2r)},\quad
U=\frac{I_0-u-v}{2}.
\]
The fourth intensity \(J=|F(i\alpha h)|^2\) gives
\[
V=\frac{U\cos(\pi k\alpha)-(J-u-v)/2}{\sin(\pi k\alpha)}.
\]
All denominators are nonzero precisely in the asserted case. The recovered \(u,v,U,V\) determine \((c,d)\) modulo phase: for \(u>0\), choose \(c=\sqrt u\) and \(d=(U-iV)/\sqrt u\); for \(u=0\) take \(c=0\) and recover \(|d|=\sqrt v\). Conversely, if the sine vanishes, the measurements depend only on \(u,v,U\); choosing \(c=1,d=\pm i\) gives a nontrivial indistinguishable pair.

For the three-measurement lower bound, lift any three point intensities to real linear functionals on the four-real-dimensional space of Hermitian \(2\times2\) matrices. Their common kernel contains a nonzero Hermitian matrix \(H\). If the three evaluation vectors fail to span \(\mathbb C^2\), injectivity already fails. Otherwise \(H\) cannot be positive or negative semidefinite, since all three corresponding nonnegative quadratic forms would have to vanish on spanning vectors. Therefore \(H\) is indefinite, so its positive and negative rank-one spectral parts are the lifts of two vectors with identical three intensities but not the same unimodular phase. This proves minimality.

**3. Singular values.** The two columns of \(A_{k,\alpha}\) have Gram matrix with trace \(3\) and determinant \(2\sin^2(\pi k\alpha)\). The quadratic formula gives \(\lambda_\pm\). For \(d\downarrow0\) with \(0\le d\le1/2\), the increasing function
\[
g(d)=\sqrt{\frac{3-\sqrt{9-8\sin^2(\pi d)}}2}
\]
satisfies \(g(d)/d\to\pi\sqrt{2/3}\). Hence \(s_k(\alpha)=g(\|k\alpha\|_{\mathbb R/\mathbb Z})\).

**4. Sharp arithmetic limit.** For irrational \(\alpha\), Dirichlet approximation provides arbitrarily small \(\|k\alpha\|\), so the running minimum \(\gamma_N\) tends to zero. For any nonnegative sequence \(b_k\to0\) along a subsequence, with positive terms and running minima \(B_N=\min_{k\le N}b_k\), the minimizing indices tend to infinity and
\[
\liminf_{N\to\infty}N B_N=\liminf_{k\to\infty}k b_k.
\]
Indeed \(B_N\le b_N\) gives one direction; for a minimizing index \(j_N\le N\), \(N B_N\ge j_N b_{j_N}\) gives the other. Applying this identity to \(b_k=g(\|k\alpha\|)\), and using \(g(d)/d\to\pi\sqrt{2/3}\) on all subsequences of bounded \(k\|k\alpha\|\), yields the first boxed formula. The latter liminf is finite by Dirichlet approximation. The same formula proves the badly approximable equivalence.

The classical sharp Hurwitz approximation theorem asserts \(\liminf_{k\to\infty}k\|k\alpha\|\le1/\sqrt5\) for every irrational \(\alpha\). Sharpness is realized by \(\alpha=(\sqrt5-1)/2\): its best-approximation denominators are Fibonacci integers, and the identity \(\|F_n\alpha\|=\varphi^{-n}\), together with \(F_n\varphi^{-n}\to1/\sqrt5\), gives the required liminf (the best-approximation property excludes smaller values between successive denominators). Multiplication by \(\pi\sqrt{2/3}\) completes the sharp design law.

**5. Witness separation.** The first intensity identity, with \(c=1,d=\pm i\), gives \(|F_k(x+iy)|^2-|G_k(x+iy)|^2=4\sin(2a_ky)\), independent of \(x\). At the two real sites \(\pm r/a_k\), \(r=(\log2)/2\), both vectors have squared Euclidean norm \(5\) and their inner-product magnitude is \(4\); the optimal-phase squared distance is therefore \(5+5-2\cdot4=2\).

## Verification
Run `python3 verify.py` with Python 3 and its standard library. It checks the intensity inversion for random complex coefficients and several line ratios, the Gram trace/determinant formula, the witnesses' phase-quotient separation, and finite Fibonacci approximations. On the completed package it passed 8144 finite assertions. These finite checks do not establish the limiting Hurwitz constant; that step is mathematical, using the stated classical approximation theorem. There is no infinite computation or numerical certificate being treated as proof.

## Relationship to prior work
Liehr's *Arithmetic progressions and holomorphic phase retrieval* (first publicly posted August 10, 2023; arXiv:2308.05722, Theorems 1.1–1.2 and the explicit two-exponential ambiguity construction in the proof) establishes the qualitative irrational-spacing uniqueness criterion for entire-function moduli. The present theorem does **not** claim that criterion, the two-exponential witness family, or basic phase lifting as new. Its distinguishing content is an exact, frequency-by-frequency interference singular spectrum, the sharp minimax rate over all choices of a third line, and a minimally sampled raw-intensity realization for the resonant sectors. The four-measurement lower bound is classical for complex two-dimensional phase retrieval; see Wang and Xu (2016). Grohs and Liehr (2021) give a separate stable Gabor reconstruction framework on Gaussian shift-invariant spaces, without this three-line arithmetic optimization. The standard Hurwitz theorem and Fibonacci approximation properties are acknowledged as classical ingredients.

## Limitations
The sharp conditioning constant concerns the extracted three-line **interference coefficient**, with equal line weights; arbitrary weighting or raw-intensity noise uses a different singular spectrum. The four physical sample locations depend on the known frequency \(k\). The proof makes no assertion of uniformly stable recovery in the full entire-function or Gabor space, or of uniqueness of the golden-ratio conjugate as a maximizing spacing modulo all fractional-linear equivalences. The first-public date is that of the motivating source, not the date of this result. Historical priority for an equivalent, previously published frame-conditioning formulation has not been independently established.

## References
- L. Liehr, *Arithmetic progressions and holomorphic phase retrieval*, arXiv:2308.05722 (first posted 2023-08-10); *Bulletin of the London Mathematical Society* 56 (2024), 3316–3330, DOI 10.1112/blms.13134.
- Y. Wang and Z. Xu, *Generalized phase retrieval: measurement number, matrix recovery and beyond*, arXiv:1605.08034 (2016).
- P. Grohs and L. Liehr, *Stable Gabor phase retrieval in Gaussian shift-invariant spaces via biorthogonality*, arXiv:2109.02494 (first posted 2021-09-06).
- A. Hurwitz, classical sharp irrational-approximation theorem; the constant \(1/\sqrt5\) and its Fibonacci sharpness are standard continued-fraction results.
