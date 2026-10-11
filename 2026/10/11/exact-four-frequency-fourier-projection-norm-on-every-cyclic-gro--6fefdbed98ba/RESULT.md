# Exact four-frequency Fourier projection norm on every cyclic group
## Finding
For every integer \(N\ge 4\), equip \(\mathbb Z_N\) with normalized counting measure and write
\[
\widehat f(k)=\frac1N\sum_{x\in\mathbb Z_N}f(x)e^{-2\pi i kx/N}.
\]
Let
\[
(P_Nf)(x)=\sum_{k=0}^3\widehat f(k)e^{2\pi i kx/N}.
\]
Put \(u=\pi/(2N)\), \(q=\lfloor (N-1)/4\rfloor\), \(r=2q+1\), and
\[
T_N(x)=\begin{cases}\csc x,&N\text{ odd},\\[2mm]\cot x,&N\text{ even}.
\end{cases}
\]
Then
\[
\|P_N\|_{\ell^\infty(\mathbb Z_N)\to\ell^\infty(\mathbb Z_N)}
=\|P_N\|_{\ell^1(\mathbb Z_N)\to\ell^1(\mathbb Z_N)}
=\Lambda_N,
\]
with the exact formula
\[
\boxed{\Lambda_N=\frac4N\left(\frac{\sin(ru)}{\sin u}+\frac{\sin(3ru)}{\sin(3u)}-\frac12T_N(u)+\frac12T_N(3u)\right).}
\]
The continuous four-term Lebesgue constant is
\[
\Lambda_\infty=\int_0^1\left|1+e^{2\pi i t}+e^{4\pi i t}+e^{6\pi i t}\right|\,dt
=\frac{8(2\sqrt2-1)}{3\pi}.
\]
The exact finite formula yields three second-order regimes:
\[
\Lambda_N=\Lambda_\infty-\frac{2\pi(2\sqrt2+1)}{3N^2}+O(N^{-4})
\quad\text{if }N\equiv0\pmod4,
\]
\[
\Lambda_N=\Lambda_\infty+\frac{2\pi(\sqrt2-1)}{3N^2}+O(N^{-4})
\quad\text{if }N\equiv2\pmod4,
\]
and
\[
\Lambda_N=\Lambda_\infty+\frac{\pi(\sqrt2+2)}{6N^2}+O(N^{-3})
\quad\text{if }N\text{ is odd}.
\]
Hence the quarter-period zero alignment on meshes with \(4\mid N\) reverses the sign of the leading sampling defect: that subsequence approaches the continuous constant from below, while the other residue classes approach it from above.

## Assumptions and scope
Only the cyclic group \(\mathbb Z_N\), \(N\ge4\), normalized counting measure, and the four consecutive frequencies \(\{0,1,2,3\}\) are considered. Translation of the frequency block and multiplication by a unit modulo \(N\) preserve the norm whenever they preserve four distinct frequencies, but no classification of arbitrary four-point spectra is claimed. The asymptotic statements concern \(N\to\infty\) inside the indicated residue classes.

## Proof
Let
\[
D_{4,N}(j)=\sum_{k=0}^3e^{2\pi i kj/N}.
\]
Then
\[
(P_Nf)(x)=\frac1N\sum_{y\in\mathbb Z_N}f(y)D_{4,N}(x-y).
\]
Therefore Young's inequality gives the upper bound \(\|P_N\|_{\infty\to\infty}\le N^{-1}\sum_j|D_{4,N}(j)|\). Equality holds by choosing a unimodular \(f\) whose phases align all summands at one output point. For the \(\ell^1\) norm, the normalized point mass \(N\mathbf 1_{\{0\}}\) has norm one and its image is \(D_{4,N}\), so equality holds there as well. Thus
\[
\Lambda_N=\frac1N\sum_{j=0}^{N-1}|D_{4,N}(j)|.
\]
The geometric sum factors as
\[
D_{4,N}(j)=e^{3\pi i j/N}\frac{\sin(4\pi j/N)}{\sin(\pi j/N)},
\]
with the value at \(j=0\) understood by continuity. Hence
\[
|D_{4,N}(j)|=4\left|\cos\frac{\pi j}{N}\cos\frac{2\pi j}{N}\right|.
\]
Let \(m=\lfloor(N-1)/2\rfloor\) and \(x_j=\pi j/N\). Symmetry gives
\[
\Lambda_N=\frac4N\left(1+2\sum_{j=1}^m\cos x_j\,|\cos 2x_j|\right).
\]
On this half-grid \(\cos x_j>0\), while \(\cos2x_j\) changes sign at \(j=N/4\). With \(q=\lfloor(N-1)/4\rfloor\), set
\[
A=\sum_{j=1}^q\cos x_j\cos2x_j,
\qquad
B=\sum_{j=1}^m\cos x_j\cos2x_j.
\]
Then the absolute-value sum is \(2A-B\). Product-to-sum and the finite cosine-sum identity give
\[
4A=\frac{\sin(ru)}{\sin u}+\frac{\sin(3ru)}{\sin(3u)}-2.
\]
For the full half-grid, the same identity gives
\[
4B=\csc u-\csc(3u)-2
\]
when \(N\) is odd, and
\[
4B=\cot u-\cot(3u)-2
\]
when \(N\) is even. Substitution into \(1+2(2A-B)\) proves the boxed formula.

For the continuous value, symmetry and the same factorization reduce the integral to elementary integrals of \(4\cos(\pi t)|\cos(2\pi t)|\), split at \(t=1/4\), which gives \(8(2\sqrt2-1)/(3\pi)\).

For the asymptotics, the master formula simplifies for the two even residue classes to
\[
\Lambda_N=\frac2N\left((\sqrt2-1)\cot u+(\sqrt2+1)\cot(3u)\right)
\quad (N\equiv0\pmod4),
\]
and
\[
\Lambda_N=\frac2N\left(\sqrt2\bigl(\csc u+\csc(3u)\bigr)-\cot u+\cot(3u)\right)
\quad (N\equiv2\pmod4).
\]
For odd \(N\), writing \(s=1\) when \(N\equiv1\pmod4\) and \(s=-1\) when \(N\equiv3\pmod4\), it becomes
\[
\Lambda_N=\frac2N\left[\frac1{\sqrt2}\left(\csc\frac u2+\csc\frac{3u}2+s\left(\sec\frac u2-\sec\frac{3u}2\right)\right)-\csc u+\csc(3u)\right].
\]
Taylor expansion of these exact identities at \(u=0\), with \(u=\pi/(2N)\), gives the three stated defect coefficients. In particular their signs are exact and nonzero.

## Verification
The accompanying `verify.py` evaluates the original discrete kernel sum and the closed formula independently for every \(4\le N\le500\), checks the even residue-class simplifications, and checks the predicted scaled second-order limits at large representative meshes. These computations are consistency checks; the proof above establishes the identities for every \(N\ge4\) without finite enumeration.

## Relationship to prior work
Bonami and Révész study idempotent trigonometric polynomials on finite cyclic groups, explicitly use Dirichlet kernels, and frame finite-grid concentration questions. Their results provide the natural finite-cyclic context but do not state the exact endpoint projection norm of the four-term consecutive block or the residue-dependent sampling defect derived here. Ash studies Lebesgue constants and Dirichlet kernels, including the classical one-dimensional setting and higher-dimensional polygonal kernels, but not this exact finite-cyclic four-term sampled norm.

A published result titled *Exact three-frequency Fourier projection norm on every cyclic group* gives the analogous three-character endpoint norm. Its stated three-frequency theorem does not imply the four-frequency identity here: the four-term kernel has the additional quarter-period zero geometry responsible for the modulo-four sign change. Full-text retrieval of that published comparison was unavailable during this check, so possible stronger material elsewhere in that source remains a residual literature risk rather than being silently treated as absent.

## Limitations
No claim is made for arbitrary four-point frequency sets, for blocks longer than four, or for intermediate \(\ell^p\) operator norms. The literature comparison cannot exclude an older equivalent finite-trigonometric-sum identity under different terminology; the result asserted here is the exact theorem and proof above, not a priority claim.

## References
A. Bonami and Sz. Gy. Révész, *Concentration of the integral norm of idempotents*, arXiv:0811.4576v1, first public 27 November 2008, MSC 42A05;42A16.

M. Ash, *Triangular Dirichlet Kernels and Growth of Lp Lebesgue Constants*, Journal of Fourier Analysis and Applications 16 (2010), 1053–1069, DOI 10.1007/s00041-009-9115-8.
