# Exact coordinate-budget profile and divisibility rigidity of a regular two-row Fourier matrix

## Finding

For an integer \(n\geq2\), put \(\omega=\exp(2\pi i/n)\) and define the complex \(2\times n\) matrix \(F_n=(a_{ij})\) by \(a_{1,j}=1\) and \(a_{2,j}=\omega^j\) for \(0\leq j<n\). For an integer \(r\geq1\), define the endpoint vector-valued bilinear norm
\[
G_{\infty}^{(r)}(F_n)=\sup_{\substack{x_1,x_2\in\mathbb C^r\\ \|x_1\|_\infty,\|x_2\|_\infty\leq1}}
\sum_{j=0}^{n-1}\left\|x_1+\omega^j x_2\right\|_\infty.
\]
Set \(s=\min\{r,n\}\), write \(n=qs+t\) with integers \(q\geq1\) and \(0\leq t<s\), and put \(h=\pi/(2n)\). Then the **exact pointwise endpoint profile** is
\[
\boxed{G_\infty^{(r)}(F_n)=\frac{2}{\sin h}\left[(s-t)\sin(qh)+t\sin((q+1)h)\right].}
\]
The maximum is achieved by assigning the columns to \(s\) consecutive cyclic blocks, \(t\) of length \(q+1\) and \(s-t\) of length \(q\), and choosing one coordinate phase at the midpoint of each block.

The scalar endpoint norm and full-coordinate value are, respectively,
\[
\|F_n\|_{\infty,1}=G_\infty^{(1)}(F_n)=\frac{2}{\sin h},\qquad
G_\infty^{(r)}(F_n)=2n\quad(r\geq n).
\]
Consequently the normalized profile is exactly
\[
\boxed{R_{n,r}:=\frac{G_\infty^{(r)}(F_n)}{\|F_n\|_{\infty,1}}
=(s-t)\sin(qh)+t\sin((q+1)h).}
\]
For \(1\leq r\leq n\), the published sharp two-row complex rectangular constant is \(\Gamma_\infty^{\mathbb C}(r;2,n)=r\sin(\pi/(2r))\). The regular Fourier matrix \(F_n\) attains this global constant **if and only if \(r\mid n\)**. For \(r\geq n\), it always attains the corresponding global constant \(n\sin(\pi/(2n))\). For each fixed \(r\) and a fixed residue \(t=n\bmod r\), as \(n\to\infty\),
\[
\boxed{r\sin\frac{\pi}{2r}-R_{n,r}
=\frac{\pi^2t(r-t)}{8rn^2}\sin\frac{\pi}{2r}+O_r(n^{-3}).}
\]
The difference is identically zero when \(t=0\). In the continuous-density limit the recovered fraction of the full mass is
\[
\lim_{n\to\infty}\frac{G_\infty^{(r)}(F_n)}{2n}
=\frac{2r}{\pi}\sin\frac{\pi}{2r}
=1-\frac{\pi^2}{24r^2}+O(r^{-4})\quad(r\to\infty).
\]

## Assumptions and scope

All scalar and vector spaces here are over \(\mathbb C\). The norm \(\|F_n\|_{\infty,1}\) is \(\sup_{|z_j|\leq1}\sum_{i=1}^2|\sum_ja_{ij}z_j|\), equivalently the scalar \(G_\infty^{(1)}\) norm by duality. The sharp rectangular comparison constant \(\Gamma_\infty^{\mathbb C}\) is the supremum of \(G_\infty^{(r)}(A)/\|A\|_{\infty,1}\) over nonzero complex \(2\times n\) matrices \(A\). The finding determines the value on the distinguished fully populated Fourier matrix, not on arbitrary matrices; the global rectangular constant is a credited earlier result.

## Proof

**Step 1: reduction to coordinate phases.** By coordinatewise complex \(\ell_1\)-\(\ell_\infty\) duality, the displayed supremum is the original vector-valued endpoint bilinear supremum. Its objective is convex in each scalar coordinate of \(x_1,x_2\). Maximizing successively on the boundary of every unit disk permits \(|(x_1)_\ell|=|(x_2)_\ell|=1\). Factoring the phase of \((x_1)_\ell\) gives unit phases \(\eta_1,\ldots,\eta_r\) and
\[
G_\infty^{(r)}(F_n)=\max_{|\eta_\ell|=1}\sum_{j=0}^{n-1}
\max_{1\leq\ell\leq r}|1+\eta_\ell\omega^j|.
\]
Write \(\eta_\ell=e^{-2i\alpha_\ell}\) and \(\phi_j=\pi j/n\) as points on the circle of circumference \(\pi\). If \(d_\pi\) is geodesic distance on that circle, then
\[
|1+\eta_\ell\omega^j|=2\cos d_\pi(\phi_j,\alpha_\ell).
\]
The finite interchange \(\sum_j\max_\ell=\max_{\sigma}\sum_j\) allows arbitrary assignments of the \(n\) indices to at most \(r\) centers.

**Step 2: sharp bound for one cluster.** Fix a center \(\alpha\), an arbitrary set \(S\) of \(k\) indices and \(1\leq k\leq n\). The \(k\) largest values among \(\cos d_\pi(\phi_j,\alpha)\) occur at \(k\) cyclically consecutive grid points (ties can be resolved consecutively). Lift their angles into the interval of length \(\pi\) centered at \(\alpha\). All the cosines are then nonnegative, the lifted angles form an arithmetic progression with spacing \(\pi/n=2h\), and the elementary geometric-sum identity yields
\[
\sum_{j\in S}\cos d_\pi(\phi_j,\alpha)
\leq\max_{\beta}\sum_{v=0}^{k-1}\cos(\beta+2vh)
=\frac{\sin(kh)}{\sin h}.
\]
The bound is attained for any \(k\) consecutive indices by putting the center at their angular midpoint: the maximal distance from that midpoint is \((k-1)h<\pi/2\), so no absolute-value branch change occurs. Hence the exact optimal contribution of a cluster of cardinality \(k\), maximized also over its placement, is \(f_n(k)=2\sin(kh)/\sin h\).

**Step 3: optimize integer partitions.** Any allocation with \(s'\leq\min\{r,n\}\) nonempty clusters has total at most \(\sum_{a=1}^{s'} f_n(k_a)\), where the positive integers sum to \(n\). Since \(k\mapsto\sin(kh)\) is strictly increasing and strictly concave on the relevant integer interval, splitting a block of cardinality at least two increases this sum. Thus all \(s=\min\{r,n\}\) available nonempty clusters are used. If two block sizes differ by at least two, shifting one index from the larger block to the smaller strictly increases the sum. The maximizing sizes are therefore precisely \(q\) and \(q+1\), with multiplicities \(s-t\) and \(t\). Choosing consecutive blocks of those sizes and the midpoint phase for each simultaneously attains the sum of all cluster bounds. This proves the exact formula without making any assumption on the shape of an initially maximizing assignment.

**Step 4: arithmetic saturation and limits.** The scalar and full-coordinate formulas follow by putting \(s=1\) and \(s=n\). For \(r\leq n\), strict Jensen concavity gives
\[
R_{n,r}=\sum_{\ell=1}^{r}\sin(k_\ell h)
\leq r\sin\left(\frac{nh}{r}\right)
=r\sin\frac{\pi}{2r},
\]
with equality exactly when all the integer block sizes \(k_\ell\) are equal, i.e., \(r\mid n\). The right-hand side is the earlier sharp rectangular constant for arbitrary complex two-row matrices, so this is exactly the stated saturation criterion. For \(r\geq n\), each column reaches its individual maximum of two. For the asymptotic, with \(n=qr+t\), expand the sine terms about \(a=\pi/(2r)\); the linear terms cancel and the weighted quadratic deviations sum to \(t(r-t)h^2/r\). Taylor's theorem gives the displayed deficit, uniformly for fixed \(r\) and residue. Finally, \(n\sin(\pi/(2n))\to\pi/2\) gives the recovered-fraction limit, and Taylor expansion of sine supplies its large-budget expansion.

## Verification

The standalone `verify.py` evaluates the balanced formula against a separately implemented exhaustive dynamic program over all positive integer compositions, checks the explicit midpoint witnesses and the arithmetic saturation criterion, and tests the original phase optimization on deterministic finite grids. It passed 75,263 assertions, including the earlier \(n=3,r=2\) case \(G_\infty^{(2)}(F_3)=2+2\sqrt3\). Every finite numerical comparison is supplementary: the arbitrary-dimension statement, continuous phase supremum, and strict divisibility criterion are established by the preceding analytic proof.

## Relationship to prior work

Santos and Serrano-Rodríguez (2026), Proposition 4.6, prove the optimal **matrix-uniform** two-row endpoint value \(\Gamma_\infty^{\mathbb C}(r;2,n)=s\sin(\pi/(2s))\); Lemma 4.1 gives the general endpoint partition representation. Their Remark 4.11 explicitly computes the \(n=3,r=2\) instance for the same Fourier family. Those results are credited and not claimed as new. The present result instead computes the entire **pointwise** budget profile of the regular \(2\times n\) Fourier matrix, finds all optimal block sizes, and proves the residue-dependent equality/deficit law against the matrix-uniform constant. Ambrus and Grundbacher's signed-sum work supplies a related one-center planar sharp bound, but does not state this multi-coordinate Fourier profile. Literature and public index searches did not locate the full claimed budget-and-divisibility theorem; they do not establish worldwide priority.

## Limitations

The theorem concerns the complex two-row full Fourier family only and the \(\ell_\infty\)-endpoint norm. It does not determine \(G_p^{(r)}\) for interior exponents or arbitrary matrices. The arithmetic deficit concerns this distinguished family and is not a stability bound over all matrix perturbations. Older formulations in circular facility-location, regular-polygon quantization, or tensor-norm literature might be equivalent; an independent publication-priority examination is still needed.

## References

1. J. Santos and D. Serrano-Rodríguez, *Effective Dimensions in Grothendieck–Hölder Inequalities*, arXiv:2610.04398v1, first public 2026-10-03; in particular Lemma 4.1, Proposition 4.6, and Remark 4.11. https://arxiv.org/abs/2610.04398
2. G. Ambrus and F. Grundbacher, *Large Signed Sums and the Polarization Constant of Convex Bodies*, arXiv:2502.13752v2, especially the cited weighted planar signed-sum result. https://arxiv.org/abs/2502.13752
