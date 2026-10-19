# A cosine staircase of sharp Haar Gabor frame bounds

## Finding
Let \(g:\mathbb R\to\mathbb R\) be the unit-height translated Haar window
\[
g(x)=-\mathbf1_{[0,1/2)}(x)+\mathbf1_{[1/2,1)}(x).
\]
For \(b>0\), consider the standard Gabor system
\[
\mathcal G_b=\bigl\{e^{2\pi i m b x}g(x-n/2):m,n\in\mathbb Z\bigr\}\subset L^2(\mathbb R).
\]
Write \(A(b)\) and \(B(b)\) for its **optimal** lower and upper frame bounds, with squared-norm normalization. For every \(0<b\le1\), the system is tight and
\[
A(b)=B(b)=\frac2b.
\]
For every \(1<b<2\), put
\[
L(b)=\left\lceil\frac{b}{2-b}\right\rceil.
\]
Then \(\mathcal G_b\) is a frame and its sharp bounds are
\[
\boxed{A(b)=\frac{2-2\cos(\pi/(L(b)+1))}{b},\quad
B(b)=\frac{2+2\cos(\pi/(L(b)+1))}{b}.}
\]
The sharp condition number is
\[
\frac{B(b)}{A(b)}=\cot^2\!\left(\frac{\pi}{2(L(b)+1)}\right).
\]
The constants have one-sided discontinuities at \(b_m=2m/(m+1)\), \(m=1,2,\ldots\): at \(b_m\) the relevant chain length is \(m\), and immediately to its right it is \(m+1\). These transitions accumulate at critical density \(b=2\). Moreover
\[
\boxed{\lim_{b\uparrow2}\frac{A(b)}{(2-b)^2}=\frac{\pi^2}{8}.}
\]
At \(b=2\) the lower bound vanishes, so the system is not a frame.

## Assumptions and scope
The window is as displayed (its translate is the usual centered Haar function), modulation is \(e^{2\pi i m b x}\), and the translation step is fixed at \(1/2\). Equalities of operator coefficients are interpreted almost everywhere, so half-open interval endpoints do not affect the spectrum. The result holds for **every real** \(b\) in the indicated ranges; no rationality assumption is made. Frame bounds are those in
\[
A(b)\|f\|_2^2\le\sum_{m,n\in\mathbb Z}|\langle f,e^{2\pi i m b\cdot}g(\cdot-n/2)\rangle|^2\le B(b)\|f\|_2^2.
\]

## Proof
**1. Exact frame operator.** For a bounded compactly supported window, Poisson summation in the modulation index gives the Walnut identity (initially for compactly supported test functions, then by bounded extension):
\[
(S_bf)(x)=\frac1b\sum_{k\in\mathbb Z}C_k(x)f(x-k/b),\quad
C_k(x)=\sum_{n\in\mathbb Z}g(x-n/2)\overline{g(x-n/2-k/b)}.
\]
The coefficient \(C_0\) is identically \(2\) almost everywhere because exactly two translates of \(g\) cover each point. If \(0<b\le1\), the overlap of a window and its nonzero integer frequency-lattice translates is null, so all \(C_k\), \(k\ne0\), vanish. Hence \(S_b=(2/b)I\).

Assume henceforth \(1<b<2\). Set \(d=1/b\), \(a=1/2\), and \(\alpha=d-a\in(0,a)\). Because \(2d>1\), all \(C_k\) vanish for \(|k|\ge2\). For \(t=x\pmod a\), \(0\le t<a\), inspecting the two contributing translates gives, away from a null set,
\[
C_1(x)=-\mathbf1_{(\alpha,a)}(t),\qquad
C_{-1}(x)=-\mathbf1_{(0,a-\alpha)}(t).
\]
Thus
\[
(b S_bf)(x)=2f(x)-\mathbf1_{t>\alpha}f(x-d)-\mathbf1_{t<a-\alpha}f(x+d).
\]
**2. Exact finite-chain decomposition.** Decompose \(L^2(\mathbb R)\) as the direct integral of \(\ell^2(\mathbb Z)\) along the arithmetic progressions \(x+kd\) for \(x\in[0,d)\). In each fiber the preceding operator has diagonal entries \(2\) and an edge of weight \(-1\) from \(x+kd\) to \(x+(k+1)d\) precisely when
\[
(x+kd)\pmod a\ <a-\alpha.
\]
Indeed the residues advance by \(\alpha\pmod a\), and an edge is present precisely when the advance does **not** wrap from the upper end of \([0,a)\) to the lower end. Every connected component is consequently a finite path: beginning with some \(t_0\in[0,\alpha)\), its consecutive residues are
\[
t_0,\ t_0+\alpha,\ldots,t_0+(N-1)\alpha<a.
\]
The number of vertices is \(N=\lceil(a-t_0)/\alpha\rceil\), except for immaterial boundary conventions. Therefore \(N\le L=\lceil a/\alpha\rceil\). Conversely the interval
\[
0<t_0<\min\{\alpha,\ a-(L-1)\alpha\}
\]
has strictly positive length and gives paths of exactly \(L\) vertices; those paths occur on positive-measure fibers. Since \(a/\alpha=b/(2-b)\), this \(L\) equals \(L(b)\).

**3. Spectral endpoints and sharpness.** On a path of \(N\) vertices, the fiber matrix of \(bS_b\) is the Jacobi matrix with diagonal \(2\) and nearest-neighbor entries \(-1\). The sine eigenvectors with components \(\sin(j\ell\pi/(N+1))\) yield all eigenvalues
\[
\lambda_{N,\ell}=2-2\cos\frac{\ell\pi}{N+1},\qquad \ell=1,\ldots,N.
\]
The lower endpoint \(2-2\cos(\pi/(N+1))\) decreases with \(N\), while the upper endpoint \(2+2\cos(\pi/(N+1))\) increases. All paths have \(N\le L\), so the displayed quantities at \(N=L\), divided by \(b\), bound the frame operator. Path components with \(N=L\) occur on sets of positive measure, so both bounds are attained in the operator spectrum and hence are optimal.

**4. Transition and critical limit.** The ceiling changes immediately to the right of \(b_m=2m/(m+1)\). At \(b=1\) the overlap appears immediately to its right, producing the first discontinuity. Since \(L(b)\sim2/(2-b)\) as \(b\uparrow2\), and \(2-2\cos u\sim u^2\) for \(u\to0\), the lower-bound limit is \(\pi^2/8\). At \(b=2\) one has \(d=a\), and the fiber operator is the bilateral discrete Laplacian \(2I-T-T^*\), whose spectrum is \([0,4]\). Its lower endpoint is zero, proving the endpoint failure.

## Verification
Run \(\texttt{python3 verify_haar.py}\) from the directory containing this document and the standalone script. The accompanying \(\texttt{verification_output.txt}\) records the execution. The script checks exact rational Walnut coefficients at 128,282 point/shift instances over 257 distinct rational modulation steps, finite-chain lengths and presence of longest paths, and eight independent finite periodic-grid realizations of the operator. These finite checks test identities and boundaries, but the direct-integral and Jacobi arguments above prove the theorem for all real parameters.

## Relationship to prior work
Dai and Zhu, *Frame set for Gabor systems with Haar window* (first arXiv posting 2022-05-13, arXiv:2205.06479), determine which parameters produce frames. Their Theorem 1.1 and Section 6 establish qualitative frame criteria but do not supply the sharp one-parameter spectral staircase stated here. Faulhuber and Shafkulovska, *Gabor frame bound optimizations* (arXiv:2204.02917), study sharp frame bounds for hyperbolic secants and exponential-type windows at integer oversampling; their window families and conclusions differ. The formula here is an exact spectral refinement for the canonical Haar window at one fixed translation step, not a claim to rediscover the frame set.

## Limitations
Only the translation step \(a=1/2\) and the unit-height Haar window are treated. No statement is made for arbitrary \(a\), nonuniform lattices, smooth windows, or stability of reconstruction under lattice jitter. The exact discontinuities reflect the discontinuous window and do not imply analogous behavior for smooth windows. A broader literature search did not rule out an earlier equivalent path-decomposition formula in older frame-operator calculations.

## References
1. X.-R. Dai and M. Zhu, *Frame set for Gabor systems with Haar window*, arXiv:2205.06479, first posted 2022-05-13. https://arxiv.org/abs/2205.06479
2. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, first posted 2022-04-06. https://arxiv.org/abs/2204.02917
3. I. Daubechies, A. Grossmann, and Y. Meyer, *Painless nonorthogonal expansions*, J. Math. Phys. 27 (1986), 1271–1283. (Classical compact-window Gabor frame-operator method.)
