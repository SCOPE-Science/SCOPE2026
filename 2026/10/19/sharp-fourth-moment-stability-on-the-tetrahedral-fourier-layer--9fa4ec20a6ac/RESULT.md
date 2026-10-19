# Sharp fourth-moment stability on the tetrahedral Fourier layer

## Finding

Consider the six square-free homogeneous quadratic characters of the four-dimensional torus. For arbitrary complex coefficients \(a_{ij}\), define
\[
P(z)=\sum_{1\le i<j\le4}a_{ij}z_i z_j,
\qquad S=\sum_{1\le i<j\le4}|a_{ij}|^2.
\]
With normalized Haar measure, the **sharp complex-coefficient Fourier fourth-moment inequality** is
\[
\boxed{\int_{\mathbb T^4}|P|^4\,dm\le\frac52 S^2.}
\]
Equality holds exactly for the zero array or arrays of the form \(a_{ij}=c u_i u_j\) with \(c\in\mathbb C\setminus\{0\}\) and \(|u_i|=1\) for every vertex. This is an unrestricted complex phase-and-amplitude optimization, not merely a positive- or equal-coefficient energy count.

The conclusion is strengthened by an **exact global nonnegative deficit decomposition**. Put
\[
(t_1,t_2,t_3)=(|a_{12}|^2+|a_{34}|^2,|a_{13}|^2+|a_{24}|^2,|a_{14}|^2+|a_{23}|^2),
\]
\[
(\delta_1,\delta_2,\delta_3)=(|a_{12}|^2-|a_{34}|^2,|a_{13}|^2-|a_{24}|^2,|a_{14}|^2-|a_{23}|^2)
\]
and \((p_1,p_2,p_3)=(a_{12}a_{34},a_{13}a_{24},a_{14}a_{23})\). Then
\[
\boxed{\begin{aligned}
\frac52 S^2-\int_{\mathbb T^4}|P|^4\,dm
={}&\frac12\sum_{r<s}(t_r-t_s)^2+\frac12\sum_{r=1}^3\delta_r^2\\
&+8\sum_{r<s}\left(\frac{t_rt_s}{4}-\Re(p_r\overline{p_s})\right).
\end{aligned}}
\tag{1}
\]
Every summand on the right is nonnegative. In particular,
\[
\frac52 S^2-\int|P|^4\,dm\ge \sum_{i<j}\left(|a_{ij}|^2-\frac S6\right)^2.
\]
Exactly the same results hold for Fourier averages on \((\mathbb Z/M\mathbb Z)^4\) whenever \(M\ge3\).

## Assumptions and scope

The coefficient field is \(\mathbb C\); all six coefficients may vanish independently. The characters are \(z_i z_j\) with distinct indices, not Walsh sign-products; the measure is Haar probability so \(\|P\|_2^2=S\). In the discrete version each \(z_i\) ranges independently over the \(M\)-th roots of unity with uniform probability. Neither complex conjugation nor any special reality condition is imposed on coefficients. The sharp constant is the fourth power of the coefficient-\(\ell^2\)-to-\(L^4\) operator norm.

## Proof

**Pair-sum structure.** Associate the edge \(\{i,j\}\) of the complete four-vertex graph with its frequency vector \(e_i+e_j\). Orthogonality identifies the fourth moment with the squared \(\ell^2\) norm of the pair-sum convolution. Apart from permutation of each ordered pair, the only repeated pair sum occurs at \((1,1,1,1)\): the three opposite-edge matchings have products \(p_1,p_2,p_3\). All other unordered edge pairs have different sum vectors, and none of the six diagonal edge doubles collides with a different unordered pair. Thus the exact expansion is
\[
\int_{\mathbb T^4}|P|^4\,dm=2S^2-\sum_{i<j}|a_{ij}|^4+8\Re(p_1\overline{p_2}+p_1\overline{p_3}+p_2\overline{p_3}).\tag{2}
\]
For the finite torus with \(M\ge3\), every coordinate of a pair sum belongs to \(\{0,1,2\}\), which embeds injectively modulo \(M\). The same exact expansion therefore holds.

**Nonnegative decomposition.** The six squared coefficient magnitudes obey
\[
S=t_1+t_2+t_3,\qquad
\sum_{i<j}|a_{ij}|^4=\frac12\sum_{r=1}^3(t_r^2+\delta_r^2).
\]
Substituting in (2) and using
\[\frac12\sum_{r<s}(t_r-t_s)^2=\sum_rt_r^2-\sum_{r<s}t_rt_s\]
gives (1) by direct expansion. By the arithmetic–geometric mean inequality,
\[
|p_r|=|a_{ij}a_{k\ell}|\le\frac12(|a_{ij}|^2+|a_{k\ell}|^2)=t_r/2.
\]
Consequently \(\Re(p_r\overline{p_s})\le |p_r||p_s|\le t_rt_s/4\), and (1) proves the moment inequality without restrictions on coefficient phases. To obtain the displayed magnitude-stability corollary, note that
\[
\sum_{i<j}\left(|a_{ij}|^2-\frac S6\right)^2
=\frac12\sum_r\delta_r^2+\frac12\sum_r(t_r-S/3)^2,
\]
whereas \(\frac12\sum_{r<s}(t_r-t_s)^2=\frac32\sum_r(t_r-S/3)^2\).

**Sharpness and equality.** The choice \(a_{ij}=1\) gives \(S=6\), all \(t_r=2\), all \(\delta_r=0\), and \(p_1=p_2=p_3=1\). Equation (1) vanishes, so the moment is \(90=(5/2)\cdot 36\). For any nonzero equality array, the first two groups in (1) vanish, forcing each \(t_r=S/3>0\) and each \(\delta_r=0\). Therefore all six coefficients have the same nonzero magnitude \(\rho=\sqrt{S/6}\). The three remaining terms vanish precisely when the unit-modulus numbers \(p_1,p_2,p_3\) have a common argument, equivalently \(p_1=p_2=p_3\).

Write \(b_{ij}=a_{ij}/\rho\). For an explicit factorization, take \(u_1=1\), \(c_0=b_{12}b_{13}/b_{23}\), and \(u_j=b_{1j}/c_0\) for \(j=2,3,4\). All these numbers have unit modulus. The equalities \(b_{12}b_{34}=b_{13}b_{24}=b_{14}b_{23}\) give \(b_{ij}=c_0u_i u_j\) for the three remaining edges, and they are already true for edges incident to vertex one. Setting \(c=\rho c_0\) proves the asserted parameterization. Conversely any such coefficient family is a simultaneous common-phase and torus translation of the uniform array and attains equality.

## Verification

Run the standalone dependency-free file `verify_k4.py` with `python3 verify_k4.py`. The checker independently groups every ordered coefficient pair by its four-dimensional Fourier sum, compares the result to (2), verifies (1) on random integer-complex arrays, and checks the same Fourier sums on finite tori of orders three and four. It also tests the full 729-element signed ternary coefficient cube, and 100 randomly chosen equality phases. One completed run passed 5,029 direct comparisons. The all-coefficient theorem is proved by the combinatorial orthogonality and exact algebra above; the finite computations are diagnostics, not extrapolation.

## Relationship to prior work

Shao and Sun, *Higher additive energies on discrete cubes* (initial preprint of October 5, 2026), study extremal exponents for additive energies of arbitrary subsets of discrete cubes and asymptotic one-dimensional Fourier interpolation. Their Theorem 1.2 and Proposition 5.1 do not determine the complex-coefficient fourth-moment operator norm, full equality family or exact stability remainder for the six-frequency second Hamming layer in four dimensions. The equal-coefficient case here is an additive-energy count, but arbitrary complex coefficient phases and magnitudes require the further optimization proved above.

A related full-quadratic Walsh-chaos result for real random signs in at least six variables has a different character group, coefficient field and fourth-moment pairing law; it does not specialize to the four-variable complex torus theorem. The six-frequency triangular Fourier aperture has a different sum-collision pattern and fixes all magnitudes to one. An earlier general single-pair-product-collision norm result also does not cover the three opposite-edge collisions present here. Searches and full-text comparisons identified no source implying (1) or the unrestricted sharp constant on this exact Fourier layer; this is a bounded literature assessment, not a proof of historical priority.

## Limitations

The result concerns the second square-free homogeneous layer in exactly four torus variables (or finite character orders at least three). It is not an all-dimensional Hamming-sphere theorem, does not cover order-two Walsh characters, and does not prove sharp constants for other even moments. The explicit nonnegative identity and equality are complete for the stated model, but historical originality cannot be certified by incomplete bibliographic coverage. Independent mathematical audit has not been performed.

## References

1. X. Shao and Y.-C. Sun, *Higher additive energies on discrete cubes*, arXiv:2610.07490v1 (first public October 5, 2026), https://arxiv.org/abs/2610.07490 (Theorem 1.2 and Proposition 5.1).
2. *Sharp fourth moments and Euclidean distortion of complete quadratic Walsh chaoses*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moments-and-euclidean-distortion-of-complete-quadra--5d09daee1c04 (RESULT.md, real sign character setting).
3. *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-phase-rigidity-for-the-six-point-triangular--bea9cf2ed885 (RESULT.md, different six-frequency support).
4. *Sharp \(\Lambda(4)\) constants for a single pair-product collision*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-lambda-4-constants-for-a-single-pair-product-collision--b11b0dc59997 (distinct one-collision hypothesis).
