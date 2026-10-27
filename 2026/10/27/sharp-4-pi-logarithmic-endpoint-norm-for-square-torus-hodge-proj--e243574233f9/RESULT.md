# Sharp \(4/\pi\) logarithmic endpoint norm for square-torus Hodge projections

## Finding
For every integer \(n\ge3\), let \(G_n=C_n\mathbin\square C_n\) be the simple undirected square torus with unit edge lengths. Give its \(2n^2\) edges any orientation. Let \(B_n\) be its vertex-edge incidence matrix, and let \(Q_n=B_n^{\mathsf T}(B_nB_n^{\mathsf T})^+B_n\) be the Euclidean-orthogonal projection onto the cut space. Its complementary projection onto the cycle-flow space is \(P_n=I-Q_n\).

The induced endpoint norms have the sharp logarithmic asymptotics
\[
\|Q_n\|_{1\to1}=\frac4\pi\log n+O(1),\qquad
\|P_n\|_{1\to1}=\frac4\pi\log n+O(1).
\]
Here \(\log\) is the natural logarithm, and the bounds implicit in \(O(1)\) are absolute. Because both matrices are symmetric, the same statements hold for their induced \(\ell_\infty\) norms. Equivalently,
\[
\lim_{n\to\infty}\frac{\|Q_n\|_{1\to1}}{\log n}
=\lim_{n\to\infty}\frac{\|P_n\|_{1\to1}}{\log n}=\frac4\pi.
\]
The exact identity \(\|P_n\|_{1\to1}=\|Q_n\|_{1\to1}+n^{-2}\) also holds; this finite-size identity is already implicit in the trace argument of Dilworth--Kutzarova--Ostrovskii (2023, Proposition 27) and is stated for completeness, **not** as a new result. The contribution claimed here is the sharp leading logarithmic coefficient with a bounded additive remainder.

## Assumptions and scope
All graphs are unweighted, undirected, connected square tori with \(n\ge3\). All edge spaces are real and carry the standard coordinate \(\ell_1\) or \(\ell_\infty\) norm. The projections are Euclidean-orthogonal, not arbitrary minimum-norm projections. For clarity the proof fixes each positive-coordinate edge orientation \((x,x+e_j)\), where \(x\in(\mathbb Z/n\mathbb Z)^2\) and \(j\in\{1,2\}\); reversing orientations only conjugates the matrices by a diagonal sign matrix and does not change the endpoint norms.

## Proof
**1. Reduction to a transfer-current kernel.** Put \(V_n=(\mathbb Z/n\mathbb Z)^2\) and \(\lambda(\theta)=4-2\cos\theta_1-2\cos\theta_2\). Define \(a_j(\theta)=e^{i\theta_j}-1\). The matrix \(Q_n\), viewed as a translation-invariant matrix with two oriented edge types at each vertex, has Fourier multipliers
\[
M_{ij}(\theta)=\frac{\overline{a_i(\theta)}a_j(\theta)}{|a_1(\theta)|^2+|a_2(\theta)|^2}
\quad(\theta\ne0),\qquad M_{ij}(0)=0.
\]
Thus its column from a horizontal edge is the two-component kernel
\[
K^{(n)}_{i1}(x)=\frac1{n^2}\sum_{k\in\{0,\ldots,n-1\}^2}
 e^{2\pi i k\cdot x/n}M_{i1}(2\pi k/n).
\]
Translations, quarter-turns and reflections act transitively on unoriented edges, with orientation changes affecting only signs. Therefore every column has the same absolute sum, and
\[
\|Q_n\|_{1\to1}=\sum_{x\in V_n}\bigl(|K^{(n)}_{11}(x)|+|K^{(n)}_{21}(x)|\bigr).
\tag{1}
\]

**2. Infinite-lattice kernel and its second-derivative tail.** Regard \(M_{ij}\) as a bounded function on the continuous frequency torus \([-\pi,\pi]^2\), with any chosen value at its single singular point, and let
\[
K_{ij}(x)=\frac1{(2\pi)^2}\int_{[-\pi,\pi]^2}
 e^{i x\cdot\theta}M_{ij}(\theta)\,d\theta,\qquad x\in\mathbb Z^2.
\]
As \(\theta\to0\), \(M_{ij}(\theta)=\theta_i\theta_j/|\theta|^2+R_{ij}(\theta)\), where the remainder is a smooth angular symbol of degree at least one: for every multi-index \(\alpha\),
\[
|\partial^\alpha R_{ij}(\theta)|\le C_\alpha|\theta|^{1-|\alpha|}
\]
near but away from zero. A smooth cutoff and dyadic annuli show that the Fourier coefficients of this remainder are \(O((1+|x|)^{-3})\): on a frequency annulus of radius \(s\), the integral is bounded by \(C_N s^3(1+s|x|)^{-N}\), and summing dyadic radii gives the asserted decay. The cutoff homogeneous term has, away from the origin, the usual distributional inverse transform of \(\theta_i\theta_j/|\theta|^2\), with a rapidly decaying cutoff error. As \(\mathcal F^{-1}(|\theta|^{-2})=-(2\pi)^{-1}\log|x|\) modulo a constant, differentiation gives
\[
K_{ij}(x)=\frac1{2\pi}\frac{\delta_{ij}|x|^2-2x_ix_j}{|x|^4}
+O(|x|^{-3}),\qquad |x|\ge2.
\tag{2}
\]
This also supplies the needed difference bound on the leading homogeneous function \(H_{ij}(x)=(2\pi)^{-1}(\delta_{ij}|x|^2-2x_ix_j)/|x|^4\): \(|\nabla H_{ij}(x)|\le C|x|^{-3}\) away from zero. Formula (2) may alternatively be obtained by taking two differences of the standard square-lattice potential-kernel expansion; see Gurevich (2018) for related lattice Green-function asymptotics.

**3. Uniform comparison with the finite torus.** Represent a residue \(x\in V_n\) by an integer point in the centered half-open square \([-n/2,n/2)^2\). We claim
\[
K^{(n)}_{ij}(x)=K_{ij}(x)+O(n^{-2})
\tag{3}
\]
uniformly in \(x,n\ge3\). Here is the image-summation justification, including the zero-mode normalization. Gaussian-Abel summation of the Fourier series of \(M_{ij}\), followed by averaging at the \(n\)-th roots of unity in both coordinates, gives
\[
K^{(n)}_{ij}(x)=\mathop{\sum_{m\in\mathbb Z^2}}{}^{\rm Abel}
 K_{ij}(x+nm)-\frac{\delta_{ij}}{2n^2}.
\tag{4}
\]
Indeed, at every nonzero frequency the Gaussian-Abel limit is \(M_{ij}\); at frequency zero it is the angular mean of \(\theta_i\theta_j/|\theta|^2\), namely \(\delta_{ij}/2\), whereas the finite-torus multiplier was set to zero. The equality for positive Abel parameters is ordinary Fourier orthogonality, before taking the limit.

For nonzero image indices \(m\), the centered-square condition yields \(|x+nm|\ge c n|m|\). By (2),
\[
K_{ij}(x+nm)=H_{ij}(nm)
+O\bigl((1+|x|)n^{-3}|m|^{-3}\bigr).
\]
The error series is absolutely summable and \(O(n^{-2})\). For each \(i,j\), the homogeneous terms \(H_{ij}(nm)\) cancel in every square-symmetric collection of images: a quarter-turn cancels the diagonal second-harmonic terms, while a reflection cancels the off-diagonal terms. The Gaussian-Abel weights preserve this symmetry at \(x=0\); replacing the Gaussian weight at \(nm\) by the weight at \(x+nm\) has vanishing effect as the Abel parameter tends to zero (apply the mean-value theorem and sum the Gaussian majorant). Hence the image contribution is \(O(n^{-2})\), proving (3). This argument does not incorrectly sum the \(|m|^{-2}\) leading term absolutely: its angular cancellation is essential.

**4. Summing the angular tail.** At \(x=r(\cos\phi,\sin\phi)\), equation (2) implies
\[
|K_{11}(x)|+|K_{21}(x)|
=\frac{|\cos(2\phi)|+|\sin(2\phi)|}{2\pi r^2}+O(r^{-3}).
\tag{5}
\]
The sum of \(O(r^{-3})\) over the integer lattice is finite. Summing (3) over the \(n^2\) residues changes the absolute column sum by at most \(O(1)\). To sum the leading homogeneous expression (5), compare its value at each nonzero lattice point with its integral over the unit square centered there. Outside a fixed ball its gradient is \(O(r^{-3})\) wherever defined and its angular absolute-value cusps are Lipschitz, so the total quadrature error is \(O(1)\). Polar integration over a centered square of side length \(n\) has radial upper limit \(n\) times a positive bounded function of angle. Consequently
\[
\sum_{x\in[-n/2,n/2)^2\cap\mathbb Z^2\setminus\{0\}}
\frac{|\cos(2\phi_x)|+|\sin(2\phi_x)|}{2\pi|x|^2}
=\frac{\log n}{2\pi}\int_0^{2\pi}
 (|\cos(2\phi)|+|\sin(2\phi)|)\,d\phi+O(1).
\]
Each angular absolute-value integral equals \(4\), so their sum is \(8\). Inserting this in (1) proves \(\|Q_n\|_{1\to1}=(4/\pi)\log n+O(1)\).

**5. Complementary projection and endpoint duality.** The graph has \(n^2\) vertices and \(2n^2\) edges; therefore \(\operatorname{tr}Q_n=n^2-1\). Edge transitivity forces every diagonal entry to equal \((n^2-1)/(2n^2)\). Each off-diagonal column entry of \(P_n=I-Q_n\) has the same absolute value as the corresponding entry of \(Q_n\). Since both diagonal entries lie between zero and one, the column sums differ by \(1-2(n^2-1)/(2n^2)=1/n^2\). This exact relation agrees with the previously published trace relation in Dilworth--Kutzarova--Ostrovskii (Proposition 27). Symmetry of the matrices identifies their induced \(\ell_1\) and \(\ell_\infty\) norms. All assertions follow.

## Verification
The standalone script `verify_torus.py` uses only Python's standard library. It reconstructs the grounded graph Laplacian and its rational inverse, checks every edge column for \(n=3,4,5,6\), and compares those exact norms against an independently computed discrete Fourier multiplier. It additionally prints Fourier-column norms for \(n=8,12,16,24,32\) and their differences from \((4/\pi)\log n\). Representative exact rational cut/cycle norms for \(n=3,4,5,6\) are respectively \((2,19/9)\), \((5/2,41/16)\), \((68/25,69/25)\), and \((317/105,3839/1260)\), agreeing with the small-order values in the 2023 primary source. Larger numerical Fourier tests support the coefficient but are not a proof; the proof is the uniform kernel comparison (3) and angular lattice summation.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (arXiv:2305.12582, first posted May 21, 2023), Section 2.4.3, calculate small-order torus projection norms, establish the exact complementary-norm trace relation in Proposition 27, and explicitly request sharper asymptotics for the orthogonal and/or minimum cycle projection in Question 32. Their cited bounds do not give the leading coefficient for the orthogonal projection. Gurevich (arXiv:1809.04850, first posted September 13, 2018) develops square-lattice Green-function expansions; its stationary spatial asymptotic is relevant to the kernel input, not an evaluation of the finite-torus endpoint projection norm. The new claim is the sharp \(4/\pi\) coefficient and bounded additive error for the orthogonal cut and cycle projections, not the trace identity or the standard infinite-lattice Green asymptotic.

## Limitations
No asymptotic is asserted for the *minimum over all* projections onto the cycle space; orthogonal projection need not minimize the \(\ell_1\) norm at finite orders. The bounded remainder is not claimed to converge or to have an identified constant. The result concerns real standard edge-coordinate norms on square tori only; it does not imply the same coefficient for rectangular, twisted, weighted or higher-dimensional tori. Literature searching cannot exclude unindexed equivalent derivations. Independent mathematical validation has not been performed.

## References
1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1, May 21, 2023, Section 2.4.3, Proposition 27 and Question 32, https://arxiv.org/abs/2305.12582.
2. P. Gurevich, *Asymptotics of the heat kernels on 2D lattices*, arXiv:1809.04850v1, September 13, 2018, Sections 2, 4 and 5, https://arxiv.org/abs/1809.04850.
