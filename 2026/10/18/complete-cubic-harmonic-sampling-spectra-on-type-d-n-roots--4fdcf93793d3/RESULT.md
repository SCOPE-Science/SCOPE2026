# Complete cubic harmonic sampling spectra on type-\(D_n\) roots

## Finding
For every integer \(n\ge4\), take the normalized root configuration
\[
 X_n=\{(\pm e_i\pm e_j)/\sqrt2:1\le i<j\le n\}\subset S^{n-1},
 \qquad |X_n|=2n(n-1).
\]
Let \(\mathcal H_3(\mathbb R^n)\) be the complex vector space of homogeneous harmonic cubic polynomials, with the normalized \(L^2(S^{n-1})\) inner product. Let \(E_n\) evaluate these polynomials at all points of \(X_n\). Write \(J\) for the permutation interchanging every root with its negative, and \(P_{\rm odd}=(I-J)/2\). Let \(P_{\rm coord}\) be the orthogonal projector in sample space onto the span of the coordinate-value vectors \((x_i)_{x\in X_n}\), \(1\le i\le n\).

The matrix \(K_n\), whose \((x,y)\) entry is the normalized degree-three spherical-harmonic reproducing kernel, has the **complete spectrum**
\[
 K_n=\frac{3(n+2)}{2(n-1)}(P_{\rm odd}-P_{\rm coord})
       +\frac{(n-4)^2}{2(n-1)}P_{\rm coord}.
\]
The respective multiplicities are \(n(n-2)\) and \(n\); the antipodally even subspace of dimension \(n(n-1)\) has eigenvalue zero. In the first block both eigenvalues are positive for \(n\ge5\), whereas the coordinate eigenvalue vanishes for \(n=4\).

Consequently, for \(n\ge5\), **every antipodally odd complex sample assignment is interpolated by some harmonic cubic**, and
\[
 \operatorname{rank}(E_n)=n(n-1),\qquad
 \ker(E_n)=\operatorname{span}_{\mathbb C}\{u_i u_j u_k:i<j<k\}.
\]
At \(n=4\), the \(24\)-point root system (the regular 24-cell) has evaluation rank \(8\), and its image consists *exactly* of sample vectors \(y\) obeying
\[
 y_{-x}=-y_x\quad(x\in X_4),\qquad
 \sum_{x\in X_4}x_i y_x=0\quad(1\le i\le4).
\]
The nullspace is eight-dimensional: the four squarefree cubics plus the four harmonic cubics \(u_i(u_i^2-\sum_{j\ne i}u_j^2)\).

For \(n\ge5\), the two positive eigenvalues coincide **if and only if \(n=10\)**. At that dimension \(K_{10}=I-J\); equivalently, the normalized degree-three zonal harmonics centered at any one root from each of the \(90\) antipodal root pairs form a mutually orthogonal set. No other \(n\ge5\) gives a tight evaluation frame on the full antipodally odd data space. The squared nonzero evaluation singular values are the displayed kernel eigenvalues times \(n(n-1)(n+4)/6\).

## Assumptions and scope
The dimensions \(n\) are **integers at least four**. Harmonicity means Euclidean Laplacian zero. All harmonic polynomials and sample data may be complex; the points and inner products are real. Evaluation uses all \(2n(n-1)\) separately labeled signed roots, with no weights and no quotient by antipodal symmetry. Since degree three is odd, antipodally even data are always inaccessible. The Gram normalization is \(K_n(x,x)=1\), not the unnormalized reproducing kernel.

Writing \(D_n=\dim\mathcal H_3(\mathbb R^n)=n(n-1)(n+4)/6\), the actual Hilbert-space evaluation Gram is \(E_nE_n^*=D_n K_n\). For counting-measure-normalized sample norm, divide this by \(2n(n-1)\). Thus the condition number of nonzero evaluation singular values for \(n\ge5\) is
\[
 \kappa_n=\sqrt{\frac{\max\{(n-4)^2,3(n+2)\}}{\min\{(n-4)^2,3(n+2)\}}},
\]
with common denominator \(2(n-1)\) canceled. It equals one exactly when \(n=10\).

## Proof
**1. A normalized spherical harmonic kernel.** By the spherical-harmonic addition theorem, the normalized degree-three zonal reproducing kernel in dimension \(n\) is
\[
 k_n(t)=\frac{(n+2)t^3-3t}{n-1},\qquad -1\le t\le1.
\]
It satisfies \(k_n(1)=1\). Its homogeneous zonal representative
\[
 Z_x(u)=\frac{(n+2)\langle u,x\rangle^3-3\|u\|^2\langle u,x\rangle}{n-1}
\]
is harmonic: the numerator terms \( (n+2)\langle u,x\rangle^3\) and \(3\|u\|^2\langle u,x\rangle\) both have Laplacian \(6(n+2)\langle u,x\rangle\), so their difference is harmonic. Rotational invariance and \(k_n(1)=1\) fix its normalized reproducing-kernel scale. Thus \(K_n(x,y)=k_n(\langle x,y\rangle)\) and \(\operatorname{rank}K_n=\operatorname{rank}E_n\).

**2. Rank-two projector identity.** Let \(V\) be the integer matrix whose row at \(x\) equals \(\sqrt2 x\); thus each row has two \(\pm1\) entries. Directly counting signs gives \(V^TV=4(n-1)I_n\), hence
\[
 P_{\rm coord}=\frac{VV^T}{4(n-1)}
 =\frac{XX^T}{2(n-1)},
 \qquad \operatorname{rank}P_{\rm coord}=n,
\]
where \(X\) is the matrix of normalized root rows. All coordinate-value vectors are odd, so \(P_{\rm coord}\le P_{\rm odd}\). Distinct, nonantipodal roots have inner products in \(\{0,\pm1/2\}\), where \(t^3=t/4\). Matching the diagonal, antipodal and other entries therefore yields the exact matrix identity
\[
 K_n=\frac{3(n+2)}{4(n-1)}(I-J)
         +\frac{n-10}{4(n-1)}XX^T.
\]
Substitute \(I-J=2P_{\rm odd}\) and \(XX^T=2(n-1)P_{\rm coord}\), obtaining the stated two-eigenvalue formula; their difference is \((n-10)/2\). The odd space has dimension \(n(n-1)\), so its orthogonal complement to the \(n\) coordinate vectors has dimension \(n(n-2)\). Every even sample vector lies in the kernel because odd zonal harmonics evaluated at \(-x\) negate their values. This proves all eigenvalue multiplicities, the rank assertions and the unique tight dimension \(10\).

**3. Algebraic characterization of the full evaluation image and kernel.** Write a general cubic as
\[
 P(u)=\sum_i a_i u_i^3+\sum_{i\ne j}b_{ij}u_i^2u_j
       +\sum_{i<j<k}c_{ijk}u_iu_ju_k.
\]
The harmonicity equations, by applying the Laplacian and matching the coefficient of \(u_i\), are precisely
\[
 3a_i+\sum_{j\ne i}b_{ji}=0\qquad(1\le i\le n).
\]
For each ordered pair \(i\ne j\), put \(q_{i|j}=a_i+b_{ji}\). At any root \(x=(s e_i+t e_j)/\sqrt2\), \(s,t\in\{-1,1\}\), we have
\[
 P(x)=\frac{s q_{i|j}+t q_{j|i}}{2\sqrt2}.
\]
The harmonic equations are equivalent to the row-sum relations
\[
 \sum_{j\ne i}q_{i|j}=(n-4)a_i.
\]
If \(n\ge5\), arbitrary complex \(q_{i|j}\) are possible: take \(a_i=(n-4)^{-1}\sum_{j\ne i}q_{i|j}\) and \(b_{ji}=q_{i|j}-a_i\). Every odd assignment on the four sign roots in each coordinate plane has exactly two independent parameters, so these \(n(n-1)\) arbitrary ordered-pair variables realize all odd data. Vanishing on all roots forces all \(q_{i|j}=0\), hence all \(a_i=b_{ij}=0\). Thus exactly the \(\binom n3\) squarefree monomials comprise the kernel.

At \(n=4\), the equations instead require \(\sum_{j\ne i}q_{i|j}=0\) for all \(i\). There are four independent linear constraints on the twelve-dimensional odd sample space. The algebraic dual of each condition is the coordinate sample vector \((x_i)_{x\in X_4}\), giving precisely \(\sum_x x_i y_x=0\). Vanishing samples mean all \(q\)'s zero; now \(a_i\) are arbitrary, and \(b_{ji}=-a_i\), producing the four extra harmonic cubics \(u_i(u_i^2-\sum_{j\ne i}u_j^2)\). The \(\binom43=4\) squarefree cubics bring the kernel to dimension eight, as independently required by the Gram rank.

**4. Constructive minimum-norm interpolation.** The normalized kernel admits the Moore–Penrose inverse
\[
 K_n^\dagger=\frac{2(n-1)}{3(n+2)}(P_{\rm odd}-P_{\rm coord})
 +\begin{cases}0,&n=4,\\[2pt]\displaystyle\frac{2(n-1)}{(n-4)^2}P_{\rm coord},&n\ge5.\end{cases}
\]
For data in the image described above, \(K_nK_n^\dagger y=y\); hence
\[
 P_y(u)=\sum_{x\in X_n}(K_n^\dagger y)_x Z_x(u)
\]
is a harmonic cubic with \(P_y|_{X_n}=y\). Because this lies in the span of evaluation representers, it is the unique interpolant of minimum spherical \(L^2\) norm. No assumption of real-valued sample data was used.

## Verification
A standalone Python 3 standard-library checker (`check.py`) constructs each signed-root orbit; recomputes every zonal Gram entry from exact integer dot products; independently verifies the integer matrix identity, orthogonality of the coordinate columns, both eigenspaces, exact interpolation by the rational pseudoinverse, and matrix rank over a prime field. All cases \(n=4,5,6,7,8,9,10,12\) passed, including the \(n=10\) tightness identity. Finite case verification corroborates but does not replace the symbolic proof for all \(n\ge4\).

## Relationship to prior work
The harmonic addition theorem and zonal reproducing kernels are classical; see Dai–Xu. The signed-root configuration, the regular 24-cell, and spherical-design aspects appear in work of Cohn–Conway–Elkies–Kumar and Hirao–Nozaki–Tasaka. Delsarte–Goethals–Seidel established the general spherical-code and association-scheme framework. An earlier 24-cell sampling result gives cumulative harmonic-band ranks \(1,5,14,22,24\) through degrees \(0,1,2,3,4\). Together with the 24-cell 5-design orthogonality, this **already implies the numerical cubic rank \(8\) at \(n=4\)**; that rank is not claimed as new. The proposed contribution is instead the **uniform type-\(D_n\) pure-cubic spectral formula for all \(n\ge4\), the all-dimensional image and nullspace description, exact interpolation operator, and unique tight dimension \(10\)**. General association-scheme formulas may implicitly imply some of these equalities and warrant comparison.

## Limitations
No claim is made for harmonic degrees other than three, other spherical root systems, arbitrary perturbations of the roots, or nonlinear recovery. The \(n=4\) sample rank is eight rather than full odd rank twelve, and even samples are inaccessible in every dimension. The work has not undergone independent mathematical audit. While relevant primary works were compared, a complete text comparison with the foundational 1977 Delsarte–Goethals–Seidel article was unavailable; an earlier equivalent association-scheme specialization cannot be excluded merely by search.

## References
- H. Cohn, J. H. Conway, N. D. Elkies, A. Kumar, *The \(D_4\) root system is not universally optimal*, arXiv:math/0607447, first posted 2006-07-19. https://arxiv.org/abs/math/0607447
- F. Dai, Y. Xu, *Spherical Harmonics*, arXiv:1304.2585, first posted 2013-04-09. https://arxiv.org/abs/1304.2585
- H. Hirao, H. Nozaki, K. Tasaka, *Spherical designs and modular forms of the \(D_4\) lattice*, arXiv:2303.09000, first posted 2023-03-16. https://arxiv.org/abs/2303.09000
- P. Delsarte, J. M. Goethals, J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363–388. DOI:10.1007/BF03187604 (full text not examined).
