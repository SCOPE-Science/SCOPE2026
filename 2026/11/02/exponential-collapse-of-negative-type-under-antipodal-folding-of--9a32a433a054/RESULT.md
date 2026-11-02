# Exponential collapse of negative type under antipodal folding of Hamming cubes

## Finding
For every integer \(d\ge4\), let \(P_d\) be the graph obtained from the binary Hamming cube \(Q_d\) by identifying each antipodal pair. Let \(\delta_d\) be its shortest-path metric and let \(\wp_d\) be the supremum of all \(p\ge0\) for which \((P_d,\delta_d)\) has \(p\)-negative type. Put \(M_d=\lfloor d/2\rfloor\). Then
\[
\frac{\log(1+2^{1-d})}{\log M_d}\le\wp_d,
\qquad
\limsup_{d\to\infty}\frac{2^d\wp_d}{d^{5/2}}\le\sqrt{2\pi},
\qquad
\lim_{d\to\infty}\frac{\log_2\wp_d}{d}=-1.
\]
The explicit upper constant comes from an asymptotically positive *weight-four* Walsh coefficient. In fact, with the convention that a binomial coefficient with an inadmissible lower index is zero, let
\[
 B_d=\sum_{k=1}^{d-1}\sum_{r=0}^4(-1)^r\binom4r\binom{d-4}{k-r}
 \log\bigl(\min\{k,d-k\}\bigr).
\]
Then the sharper spectral statement holds:
\[
\lim_{d\to\infty}\frac{d^{5/2}B_d}{2^d}=\sqrt{\frac2\pi}.
\]
In particular, while the original Hamming metric on \(Q_d\) has supremal negative type \(1\) for \(d\ge2\), antipodal identification reduces the critical exponent to \(2^{-d+o(d)}\). Equivalently, the maximal Hilbert-isometric snowflake exponent of \((P_d,\delta_d)\) is \(\wp_d/2\).

## Assumptions and scope
All metric spaces are finite, real-valued, and unweighted. The quotient vertex set is \(G_d=\mathbb F_2^d/\langle\mathbf1\rangle\), of order \(N_d=2^{d-1}\). For representatives \(x,y\in\mathbb F_2^d\), the graph metric is exactly
\[
\delta_d([x],[y])=\min\{\lvert x-y\rvert,d-\lvert x-y\rvert\},
\]
where \(\lvert\cdot\rvert\) is Hamming weight. For \(p>0\), \(p\)-negative type means that for every real coefficient family \((c_g)_{g\in G_d}\) with \(\sum_g c_g=0\),
\[
\sum_{g,h\in G_d}c_gc_h\,\delta_d(g,h)^p\le0.
\]
At \(p=0\), distinct points have distance power \(1\) and diagonal terms have distance power \(0\). The statement concerns the supremal exponent, not its exact finite-dimensional value.

## Proof
**Step 1: the lower bound.** For any finite \(N\)-point metric whose nonzero distances lie in \([1,M]\), its zero-diagonal \(p\)-distance matrix \(D_p\) satisfies, on the zero-sum coefficient subspace,
\[
 c^\top D_0c=-\|c\|_2^2,
 \quad
 \bigl|c^\top(D_p-D_0)c\bigr|
 \le(M^p-1)\|c\|_1^2
 \le N(M^p-1)\|c\|_2^2.
\]
Consequently, \(N(M^p-1)\le1\) implies \(p\)-negative type, and strict inequality implies strict negative type. Substitute \(N=N_d=2^{d-1}\) and \(M=M_d\). This proves the claimed explicit lower bound for all \(d\ge4\).

**Step 2: one Fourier obstruction.** Every character of \(G_d\) is induced by an even-weight vector \(\xi\in\mathbb F_2^d\), with \(\chi_\xi([x])=(-1)^{\xi\cdot x}\). A translation-invariant real symmetric distance-power matrix is negative semidefinite on the zero-sum subspace exactly when its Fourier coefficients at all nontrivial characters are nonpositive (the diagonalization follows by Fourier orthogonality). Choose \(\lvert\xi\rvert=4\). Define
\[
 K_{d,4}(k)=\sum_{r=0}^4(-1)^r\binom4r\binom{d-4}{k-r},
 \quad
 F_d(p)=\sum_{k=1}^{d-1}K_{d,4}(k)\min\{k,d-k\}^p.
\]
The Fourier eigenvalue on \(G_d\) is \(F_d(p)/2\), since each class has two binary representatives. A *positive* value of \(F_d(p)\) therefore precludes \(p\)-negative type. For every \(d\ge5\), binomial orthogonality and \(K_{d,4}(0)=K_{d,4}(d)=1\) give
\[
 F_d(0)=-2,\qquad F_d'(0)=B_d.
\]
The same identities hold at \(d=4\), though only the asymptotic dimensions are used below.

**Step 3: sharp asymptotics of the weight-four derivative.** Let \(X_d\sim\operatorname{Bin}(d,1/2)\) and \(Z_d=(d-2X_d)/\sqrt d\). The dual Krawtchouk polynomial
\[
 \mathcal K_4(k)=\sum_{r=0}^4(-1)^r\binom kr\binom{d-k}{4-r}
 =\frac{T^4-(6d-8)T^2+3d(d-2)}{24},\quad T=d-2k,
\]
satisfies the exact double-counting relation
\[
 K_{d,4}(k)=\frac{\binom dk}{\binom d4}\,\mathcal K_4(k).
\]
Set \(A_d=\mathcal K_4(X_d)/\binom d4\). Fourier orthogonality gives \(\mathbb E A_d=0\), while the displayed polynomial gives
\[
 d^2A_d
 =\frac{d^4}{d(d-1)(d-2)(d-3)}
 \left(Z_d^4-\left(6-\frac8d\right)Z_d^2+3\left(1-\frac2d\right)\right).
\]
If \(L_d(k)=\log\min\{k,d-k\}\) for \(1\le k\le d-1\) and \(L_d(0)=L_d(d)=0\), then
\[
 \frac{d^{5/2}B_d}{2^d}
 =\mathbb E\left[d^2A_d\sqrt d\bigl(L_d(X_d)-\log(d/2)\bigr)\right].
\]
By the binomial central limit theorem \(Z_d\Rightarrow Z\sim N(0,1)\). When \(\lvert Z_d\rvert\le\sqrt d/2\), the second factor equals \(\sqrt d\log(1-\lvert Z_d\rvert/\sqrt d)\), tends to \(-\lvert Z\rvert\), and is dominated in magnitude by \(2\lvert Z_d\rvert\). The polynomial factor is bounded by a fixed multiple of \(1+\lvert Z_d\rvert^4\). Standard binomial subgaussian tails uniformly control their product; on the complementary event, the product has polynomial growth in \(d\) and that event has exponentially small probability. This also disposes of the two endpoints, so convergence of expectations is justified without ignoring the logarithmic singularity.

The limit is therefore
\[
 -\mathbb E[(Z^4-6Z^2+3)\lvert Z\rvert]
 =-\left(8-12+3\right)\sqrt{\frac2\pi}
 =\sqrt{\frac2\pi},
\]
where the three absolute Gaussian moments have orders \(5,3,1\). This proves the asserted limit for \(B_d\).

**Step 4: transfer the spectral slope to the critical exponent.** The generating-polynomial representation
\[
 \sum_kK_{d,4}(k)z^k=(1-z)^4(1+z)^{d-4}
\]
ensures \(\sum_k\lvert K_{d,4}(k)\rvert\le2^d\). Taylor's theorem, uniformly for \(p\ge0\), gives
\[
 \left|F_d(p)+2-pB_d\right|
 \le\frac12\,2^d p^2(\log M_d)^2 M_d^p.
\]
Choose any fixed \(\varepsilon>0\) and put
\[
 p_d=(\sqrt{2\pi}+\varepsilon)d^{5/2}2^{-d}.
\]
The error above tends to zero, while the spectral asymptotic yields
\[
 F_d(p_d)=-2+(\sqrt{2\pi}+\varepsilon)\sqrt{2/\pi}+o(1)>0.
\]
Thus \(P_d\) does not have \(p_d\)-negative type for sufficiently large \(d\). The nesting property of negative type implies \(\wp_d\le p_d\), proving the stated \(\limsup\) bound. Combined with the explicit lower bound, which is asymptotic to \(2^{1-d}/\log(d/2)\), this yields \(\log_2\wp_d=-d+O(\log d)\) and hence the claimed exponential rate. Schoenberg's embedding theorem identifies the maximal isometric Hilbert-snowflake exponent as \(\wp_d/2\).

## Verification
A standalone Python checker (`checker.py`) enumerates the weight-four Krawtchouk coefficients, independently matches quotient-character sums against direct vertex enumeration for small dimensions, checks the exact identity \(F_d(0)=-2\), evaluates the normalized derivative with high precision through dimension \(128\), and tests positive Fourier witnesses beyond the asymptotic upper threshold. It also verifies the algebraic lower-bound identity for a finite parameter range. The script relies on the external Python package `mpmath` for high-precision arithmetic; the rest uses Python's standard library. Finite checks cannot certify the central-limit passage or the infinite asymptotic assertion; those are proved above.

## Relationship to prior work
Robertson (2023) establishes the negative-type/Hilbert-embedding connection and exact power-distortion behavior for the *unfolded* Hamming cube, where the supremal negative type is \(1\). Chen, Naserasr and Sarti (2024) give multiple descriptions of projective cubes and an exact quotient-distance formula; their subject is graph structure and homomorphisms, not negative-type asymptotics. Weston (2008) establishes a stronger *universal* lower bound for finite metric spaces in terms of cardinality and diameter; the elementary lower bound in the present proof is used only to secure the exponential rate and is not claimed as new. Murugan (2011) and Sánchez (2011) establish general determinant and spectral tools for maximal negative type of finite metrics, but do not give the exponential rate of the antipodal quotient. The result uses standard harmonic and probabilistic tools in a new quantitative comparison for this graph family. A previously unknown equivalent asymptotic result under projective-cube or folded-cube terminology cannot be ruled out absolutely.

## Limitations
No sharp leading constant for \(\wp_d\) itself is proved: the asymptotically sharp constant \(\sqrt{2\pi}\) belongs to the specific weight-four *obstruction scale*, not necessarily to the globally critical exponent. Other Fourier characters can yield stronger obstructions, especially in certain residue classes. There is no claim of a complete finite-dimensional classification or of an independently audited novelty priority. The theorem concerns unweighted binary cubes modulo the all-one antipodal symmetry, not arbitrary quotient codes or weighted folded graphs.

## References
- Gavin Robertson, *Negative Type and Bi-lipschitz Embeddings Into Hilbert Space*, arXiv:2309.16070v1 (first posted September 27, 2023), especially Sections 1 and 4.2. https://arxiv.org/html/2309.16070v1
- Meirun Chen, Reza Naserasr and Alessandra Sarti, *Signed projective cubes, a homomorphism point of view*, arXiv:2406.10814 (first posted June 16, 2024), especially Section 2, Definitions 3 and 5 and Proposition 9. https://arxiv.org/abs/2406.10814
- Anthony Weston, *Optimal lower bounds on the maximal p-negative type of finite metric spaces*, arXiv:0807.2705v1 (first posted July 17, 2008), especially Theorem 4.1. https://arxiv.org/abs/0807.2705
- Mathav Kishore Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1 (first posted December 23, 2011), especially Theorem 3.1. https://arxiv.org/abs/1112.5657
- Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1 (first posted August 2, 2011), especially the finite-metric distance-matrix characterization. https://arxiv.org/html/1108.0451v1
- I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536.
