# Sharp periodic-erasure bounds for hat-spline Gabor systems

## Finding
For each integer \(m\ge2\), and each nonempty subset \(J\subset\{0,\ldots,m-1\}\) of cardinality \(k\), take the unnormalized hat spline \(g(t)=(1-|t|)_+\), retain the time translations \(\Lambda_J=\bigcup_{j\in J}(j/m+\mathbb Z)\), and keep all integer-frequency modulations. The Gabor family
\[
\mathcal G_J=\{e^{2\pi int}g(t-(\ell+j/m)):\ n,\ell\in\mathbb Z,\ j\in J\}
\]
has optimal upper Bessel bound \(B_J=k\). Its exact optimal lower frame bound is the following **finite, arithmetic, all-mask formula**. Write \(J=\{j_1<\cdots<j_k\}\). For every cyclic cut \(r\in\{1,\ldots,k\}\), let
\[
(z^{(r)}_1,\ldots,z^{(r)}_k)
 =(j_r,\ldots,j_k,j_1+m,\ldots,j_{r-1}+m),
\qquad \overline z^{(r)}=\frac1k\sum_{a=1}^k z^{(r)}_a.
\]
Then
\[
\boxed{A_J=\frac4{m^2}\min_{1\le r\le k}\sum_{a=1}^k(z^{(r)}_a-\overline z^{(r)})^2
=\frac4{km^2}\min_{1\le r\le k}\sum_{a<b}(z^{(r)}_b-z^{(r)}_a)^2.}
\]
In particular, the exact **worst retained lower bound** among all size-\(k\) periodic erasure masks is
\[
\boxed{\min_{|J|=k}A_J=\frac{k(k^2-1)}{3m^2}.}
\]
Equality holds if and only if \(J\) is a cyclic block of \(k\) consecutive residues modulo \(m\). If \(k<m\), there are exactly \(m\) such labelled residue masks; if \(k=m\), there is exactly one. In particular, one surviving coset is not a frame, while **every selection of at least two cosets** yields a frame, and the sharp worst-case upper/lower bound ratio is \(3m^2/(k^2-1)\) for \(k\ge2\).

## Assumptions and scope
The Hilbert space is \(L^2(\mathbb R)\), with Fourier modulation \(M_n f(t)=e^{2\pi int}f(t)\) and translation \(T_a f(t)=f(t-a)\). The sums of squared coefficient magnitudes are over every integer modulation and the indicated surviving translations, counting every pair \((n,\ell+j/m)\) once. There are no normalization factors on the hat window. The lower bound is the largest \(A_J\ge0\) for which
\[
A_J\|f\|_2^2\le\sum_{j\in J}\sum_{\ell,n\in\mathbb Z}
|\langle f,M_nT_{\ell+j/m}g\rangle|^2\le B_J\|f\|_2^2
\]
holds for every \(f\in L^2(\mathbb R)\); the upper bound is the smallest admissible \(B_J\). A cyclic block is \(\{a,a+1,\ldots,a+k-1\}\pmod m\). For \(k=1\), the expression for the optimal lower bound is zero and no positive lower frame constant exists.

## Proof
**1. Exact Zak diagonalization.** On the unit square let
\[
(Zf)(x,\nu)=\sum_{\ell\in\mathbb Z}f(x-\ell)e^{2\pi i\ell\nu},\qquad 0\le x,\nu<1.
\]
This is unitary from \(L^2(\mathbb R)\) onto \(L^2([0,1)^2)\). Since \(ZT_{\ell+j/m}g(x,\nu)=e^{-2\pi i\ell\nu} Zg(x-j/m,\nu)\) and integer modulation acts by \(e^{2\pi inx}\), the time-frequency analysis coefficients are the two-dimensional Fourier coefficients of \(Zf\) multiplied by each \(\overline{Zg(x-j/m,\nu)}\), up to unimodular factors. Parseval gives the *exact* operator identity
\[
\sum_{j\in J}\sum_{\ell,n\in\mathbb Z}|\langle f,M_nT_{\ell+j/m}g\rangle|^2
=\int_{[0,1)^2}|Zf(x,\nu)|^2 F_J(x,\nu)\,dx\,d\nu,
\quad F_J(x,\nu)=\sum_{j\in J}|Zg(x-j/m,\nu)|^2.
\]
By unitarity and continuity, the exact frame bounds are the global minimum and maximum of this symbol.

**2. The hat-spline symbol is a quadratic circular potential.** If \(u=\{x-j/m\}\in[0,1)\), exactly two integer translates of the tent contribute and
\[
Zg(x-j/m,\nu)=e^{i\vartheta(x,j,\nu)}\big((1-u)+u e^{2\pi i\nu}\big)
\]
for a phase \(\vartheta\) irrelevant to the modulus. Hence
\[
F_J(x,\nu)=k-2(1-\cos(2\pi\nu))\sum_{j\in J}u_j(1-u_j),
\quad u_j=\{x-j/m\}.
\]
At \(\nu=0\), the symbol equals \(k\) everywhere, so \(B_J=k\); at \(\nu=1/2\) it is minimized, and \(1-4u(1-u)=(1-2u)^2\). Define the circle distance \(d_{\mathbb T}(v,w)=\min_{a\in\mathbb Z}|v-w-a|\). Since \(|1-2\{x-j/m\}|=2d_{\mathbb T}(x-1/2,j/m)\),
\[
A_J=4\min_{y\in\mathbb R/\mathbb Z}\sum_{j\in J}d_{\mathbb T}(y,j/m)^2.
\tag{1}
\]

**3. Complete finite reduction by cyclic cuts.** Fix a real lift \(v=my\). For each \(j\in J\), choose an integer \(z_j\equiv j\pmod m\) nearest to \(v\). Every such chosen lift lies in \([v-m/2,v+m/2]\), so the distinct lifts, in circular order, constitute one of the cyclic lists \(z^{(r)}\), up to a common integer multiple of \(m\). (At a tie, either adjacent cyclic cut can be selected.) Thus
\[
\sum_j m^2d_{\mathbb T}(y,j/m)^2
=\sum_{a=1}^k(v-z_a)^2
\ge\sum_{a=1}^k(z_a-\overline z)^2
\ge\min_r\sum_{a=1}^k(z_a^{(r)}-\overline z^{(r)})^2.
\]
Conversely, choose a cyclic cut attaining the rightmost minimum, set \(v=\overline z^{(r)}\), and use the corresponding lifted representatives. Circular nearest-representative distances are no larger than the chosen representative distances. Hence the opposite inequality holds after minimizing over \(y\), proving the first equality in the finding. The classical identity \(\sum_a(z_a-\overline z)^2=k^{-1}\sum_{a<b}(z_b-z_a)^2\) gives the second equality.

**4. The sharp adversarial value and equality.** For any strictly increasing \(k\)-tuple of integers \(z_1<\cdots<z_k\), one has \(z_b-z_a\ge b-a\) for all \(a<b\). Consequently
\[
\frac1k\sum_{a<b}(z_b-z_a)^2\ge
\frac1k\sum_{a<b}(b-a)^2=\frac{k(k^2-1)}{12}.
\]
For \(k\ge2\), equality holds if and only if every consecutive gap is one. Thus the cyclic-cut formula yields \(A_J\ge k(k^2-1)/(3m^2)\), with equality precisely when one cyclic lifting is \(k\) consecutive integers, equivalently when \(J\) is a circularly consecutive block. Such masks exist for every admissible \(m,k\), proving sharpness. Distinct circular blocks are counted by their starting residue when \(k<m\), but all starts describe the same entire residue set when \(k=m\). The case \(k=1\) gives zero directly from (1).

**5. Frame survival and optimal conditioning.** For \(k\ge2\), the sharp bound in Step 4 is strictly positive for every retained mask; the multiplier identity in Step 1 therefore makes each system a frame. The common sharp upper bound is \(k\), so the largest possible ratio is \(k/[k(k^2-1)/(3m^2)]=3m^2/(k^2-1)\), with the same exact equality masks. This concludes the proof for every integer \(m\ge2\).

## Verification
The standard-library-only `checker.py` executes `python3 checker.py`. Its independently coded piecewise-quadratic maximization over circle cells agrees with the cyclic-cut variance formula on **2,035 exact-rational subsets**, exhaustively covering all nonempty masks for \(2\le m\le10\). In the same exact loops, it checks the uniform sharp value, exact equality-mask census, and positive lower bounds when \(k\ge2\). Separately, **1,300 seeded complex Zak-symbol comparisons** check the phase-dependent Fourier formula. The program reports `VERIFY_OK`. These are supplementary finite checks; the all-dimension claim is proved in Steps 1–5.

## Relationship to prior work
Hasannasab and Lemvig (first public arXiv version September 11, 2026) analyze zeros of Zak transforms of B-splines and derive regular Gabor-frame lattice membership for the tent spline. Stangl and Frederick (first public August 31, 2026) characterize the regular integer-oversampling frame set for the same spline. Neither lattice-membership question determines the **full spectrum after periodic deletion of an arbitrary set of translation cosets**, the exact surviving-mask arithmetic formula, or the worst-mask equality classification.

Prior published sharp Gabor-bound results for the hat spline treat a full regular lattice at a different modulation spacing, and a published sharp lower-bound onset treats a moving lattice parameter near a zero threshold. Both share Zak fiberization but neither specializes to these periodically erased \(b=1\) systems. A related finite cyclic harmonic-frame erasure theorem addresses two Fourier rows and circular complex phase sums, rather than the real-line Gabor translation problem or squared circle-distance potential in (1). Hardin–Kendall–Saff's circle-polarization theorem optimizes a *best* configuration of points on a circle; it does not determine the *worst* \(k\)-element subset of a fixed \(m\)-grid or its equality masks. The elementary integer spacing inequality is not claimed as new; its consequence for sharp periodic Gabor erasures is the contribution.

## Limitations
The result concerns exact integer modulation spacing, the unnormalized second-order cardinal B-spline, periodic removal of whole translation cosets, and no additional coefficient weighting. It does not classify arbitrary nonperiodic deletions, nonlinear phase retrieval, or other spline degrees. Existing qualitative regular-lattice frame results are credited as prior work. No assertion of historical uniqueness is made: an unindexed equivalent observation in earlier shift-invariant-frame or circular polarization literature could change priority. The proof and finite verification are not independently audited.

## References
1. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116 (first submitted September 11, 2026). https://arxiv.org/abs/2609.13116
2. A. Stangl and C. Frederick, *The frameset of the second-order B-Spline along \(ab=1/q\)*, arXiv:2609.00481 (first submitted August 31, 2026). https://arxiv.org/abs/2609.00481
3. D. P. Hardin, A. P. Kendall, and E. B. Saff, *Polarization optimality of equally spaced points on the circle for discrete potentials*, Discrete Comput. Geom. 50 (2013), 236–243. https://arxiv.org/abs/1208.5261
4. M. Zibulski and Y. Y. Zeevi, *Analysis of multiwindow Gabor-type schemes by frame methods*, Appl. Comput. Harmon. Anal. 4 (1997), 188–221.
5. *Sharp Gabor frame bounds and quadratic collapse for the hat spline at half-density* (2026), published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-gabor-frame-bounds-and-quadratic-collapse-for-the-hat-spli--c8f151d17e5c
6. *Sharp quadratic onset of the tent-spline Gabor lower frame bound* (2026), published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-quadratic-onset-of-the-tent-spline-gabor-lower-frame-bound--9587a4647148
7. *Exact adversarial-erasure spectra for two-character cyclic harmonic frames* (2026), published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-adversarial-erasure-spectra-for-two-character-cyclic-harmo--e1e03f96b6f0
