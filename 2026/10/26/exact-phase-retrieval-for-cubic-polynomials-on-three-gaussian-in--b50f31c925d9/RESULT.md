# Exact phase retrieval for cubic polynomials on three Gaussian-integer squares

## Finding

Let \(\mathcal P_3=\{p(\zeta)=\sum_{j=0}^3 a_j\zeta^j:a_j\in\mathbb C\}\). Define the twelve-point Gaussian-integer set
\[
\Omega=\bigcup_{b\in\{1,1+i,2+i\}}\{b,ib,-b,-ib\}.
\]
For any \(p,q\in\mathcal P_3\), the twelve equalities \(|p(\omega)|=|q(\omega)|\) for \(\omega\in\Omega\) imply \(p=\tau q\) for some \(\tau\in\mathbb C\), \(|\tau|=1\). This includes the zero polynomial.

Moreover, the maximum modulus \(\sqrt5\) is the smallest achievable maximum modulus among all twelve-point sets comprising exactly three complete, distinct, fourfold rotational orbits of nonzero Gaussian integers. At maximum modulus at most \(2\), the only candidate is the union of the orbits of \(1,1+i,2\), and this candidate is noninjective.

## Assumptions and scope

A fourfold Gaussian-integer orbit means the four distinct sites \(\{b,ib,-b,-ib\}\) with \(b\in\mathbb Z[i]\setminus\{0\}\). All comparisons use exact pointwise complex modulus, not noisy measurements. The assertion is universal over all coefficients of every complex polynomial of degree at most three. The minimal-radius assertion applies only to twelve-node sets made from three distinct full orbits; it does not claim minimum cardinality among unrestricted complex frames or arbitrary sample sets.

## Proof

Put \(v(\zeta)=(1,\zeta,\zeta^2,\zeta^3)^T\). For a Hermitian matrix \(Q\), define its real sampling map by
\[
\mathcal A(Q)_\omega=\sum_{j,k=0}^3 Q_{jk}\omega^j\overline\omega^{\,k}.
\]
If \(p_a(\zeta)=\sum a_j\zeta^j\), then \(|p_a(\omega)|^2=\mathcal A(aa^*)_\omega\). Thus two polynomials have equal intensities exactly when \(aa^*-bb^*\) belongs to \(\ker\mathcal A\). Any such difference has Hermitian rank at most two. If the kernel has no nonzero matrix of rank at most two, then \(aa^*=bb^*\), and elementary rank-one factorization gives \(a=\tau b\) with \(|\tau|=1\) unless both are zero.

A rational row reduction of the twelve real equations in sixteen real Hermitian coordinates shows \(\operatorname{rank}_{\mathbb R}\mathcal A=12\). Its four-dimensional kernel is precisely the following real-linear pencil \(H(w,x,y,t)\), with \(w,x,y,t\in\mathbb R\):
\[
\begin{aligned}
&H_{00}=-20w,\quad H_{11}=34w,\quad H_{22}=-16w,\quad H_{33}=2w,\\
&H_{01}=12y+4t+i(-4y+12t),\\
&H_{02}=2x(1-2i),\\
&H_{03}=-2y-t+i(-y+2t),\\
&H_{12}=-12y-3t+i(3y-12t),\\
&H_{13}=2x(-1+i),\qquad H_{23}=2y+2it,
\end{aligned}
\]
with \(H_{kj}=\overline{H_{jk}}\) for \(k>j\). The accompanying exact-arithmetic checker independently reconstructs the twelve-by-sixteen real sampling matrix, verifies its rank, and confirms that each displayed direction belongs to the kernel. Hence these four independent directions exhaust the kernel.

To exclude rank at most two, form the sixteen three-by-three minors of \(H(w,x,y,t)\), then take real and imaginary parts. Their ideal \(I\subset\mathbb Q[w,x,y,t]\) contains the following four explicit polynomials:
\[
\begin{aligned}
&t^5,\\
&4w^3+wt^2,\\
&3x^3+12xt^2+85wt^2,\\
&81y^3-1237yt^2-306t^3.
\end{aligned}
\]
This is an exact rational Gröbner-basis ideal-membership certificate, not a numerical observation: `checker.py` recomputes all minors and the basis using graded reverse lexicographic order and verifies zero reduction of each of these four polynomials. At any simultaneous zero of all minors, the first equation gives \(t=0\), and the remaining three give \(w=x=y=0\). This argument even holds for complex parameter values. Therefore no nonzero Hermitian kernel matrix has rank at most two, proving universal phase retrieval.

For radius optimality, the only nonzero Gaussian-integer orbits contained in \(\{\zeta:|\zeta|\le2\}\) have squared radii \(1,2,4\), represented by \(1,1+i,2\). Define
\[
 p_-(\zeta)=2\sqrt7\,\zeta-i\sqrt2\,\zeta^3,
 \qquad p_+(\zeta)=4-i\sqrt{14}\,\zeta^2.
\]
Direct exact substitution gives \(|p_-(\zeta)|^2=|p_+(\zeta)|^2\) on each of the twelve sites in those three orbits; the checker verifies all twelve identities. The two polynomials cannot differ by a global phase because one has only odd-degree coefficients and the other only even-degree coefficients. Hence radius \(2\) fails, and every smaller radius contains fewer than three full nonzero orbits. The successful displayed set has maximal modulus \(\sqrt5\), completing the optimality proof.

## Verification

Run `python checker.py` with SymPy installed. This performs exact rational matrix-rank calculation, exact Hermitian-kernel substitution, exact Gröbner ideal reductions of the sixteen minors, and exact substitution of the twelve radius-two counterexample nodes. It prints four `PASS` lines on success. No floating-point approximation or finite sampling of coefficient space is used in the certificate. The proof's universal quantifier follows from symbolic elimination; the twelve-node loop certifies only the explicitly stated negative example.

## Relationship to prior work

Bodmann and Hammen (2013) construct universal polynomial magnitude frames with \(4d-4\) samples from two specially intersecting circles; their particular sampling construction does not imply universal phase retrieval for the present three concentric square orbits. Vinzant (2015) constructs an eleven-vector frame in \(\mathbb C^4\), showing that twelve is not an unrestricted cardinality minimum; her frame is not this monomial-evaluation design. Chalendar and Partington (2024) analyze analytic phase retrieval on complete circles and lines, including two-circle uniqueness. Liehr (2023, published 2024) analyzes uniqueness on unions of parallel lines and arithmetic progressions. These continuous geometric uniqueness theorems do not give this discrete twelve-node lattice certificate or the three-square radius boundary. These comparisons rely on the stated full-text sections and do not claim a complete worldwide priority search.

## Limitations

The asserted radius optimum is relative to three complete, distinct Gaussian-integer square orbits. Neither optimal noise amplification nor the smallest number of arbitrary complex evaluation nodes is determined. The exact symbolic certificate uses a Gröbner-basis computation, so independent implementation or hand-derived ideal identities would strengthen verification. Algebraic elimination establishes injectivity, but this paper does not supply a numerical global conditioning constant. The possibility of an equivalent unindexed earlier integer-lattice frame remains a priority risk.

## References

1. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (first posted 24 March 2024), especially §§2.1–2.4.
2. B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487 (2013), §2.
3. C. Vinzant, *A small frame and a certificate of its injectivity*, arXiv:1502.04656 (2015), §§I–II.
4. L. Liehr, *Arithmetic progressions and holomorphic phase retrieval*, arXiv:2308.05722 (2023), *Bull. Lond. Math. Soc.* 56 (2024), §§1–2.
