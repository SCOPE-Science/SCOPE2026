# Twisted-diagonal trace spectra and arithmetic Schatten thresholds in analytic kernel spaces

## Finding
Let \(r>0\), let \(\mathcal H_r\) be the reproducing-kernel Hilbert space on \(\mathbb D\) with kernel \((1-z\overline w)^{-r}\), and let \(\mathcal S_r\) be the coordinate-symmetric subspace of \(\mathcal H_r\widehat\otimes\mathcal H_r\). For \(0\le\theta\le\pi\), the twisted diagonal trace
\[
R_\theta F(z)=F(z,e^{i\theta}z):\mathcal S_r\longrightarrow\mathcal H_{2r}
\]
is a well-defined contraction. In the normalized monomial basis of \(\mathcal H_{2r}\), the positive operator \(R_\theta R_\theta^*\) is diagonal, with *complete exact eigenvalue sequence*
\[
\lambda_n(r,\theta)=\frac12\left[1+\frac{C_n^{(r)}(\cos\theta)}{(2r)_n/n!}\right],\qquad n=0,1,2,\ldots,
\]
where \(C_n^{(r)}\) is the Gegenbauer polynomial specified by \((1-2xt+t^2)^{-r}=\sum_{n\ge0}C_n^{(r)}(x)t^n\), and \((a)_n\) is the rising factorial. In particular, \(R_0R_0^*=I\), whereas \(R_\pi R_\pi^*\) is the orthogonal projection onto even functions. For \(0<\theta<\pi\), the trace is surjective, all \(\lambda_n\) are strictly positive, and \(\lambda_n\to1/2\).

For fixed \(0<\theta<\pi\), put \(D_{r,\theta}=R_\theta R_\theta^*-\tfrac12I\),
\[
\beta_{r,\theta}=\frac{\Gamma(2r)}{\Gamma(r)(2\sin\theta)^r},\qquad
\Phi_n=(n+r)\theta-\frac{\pi r}{2},
\]
and let \(M_{r,\theta}>0\) be the mean of \(|\cos\Phi_n|^{1/r}\). Explicitly, if \(\theta/\pi=u/v\) in lowest terms, take
\[
M_{r,\theta}=\frac1v\sum_{j=1}^v\left|\cos\left((j+r)\theta-\frac{\pi r}{2}\right)\right|^{1/r};
\]
if \(\theta/\pi\) is irrational, take
\[
M_{r,\theta}=\frac{\Gamma((1+1/r)/2)}{\sqrt\pi\,\Gamma(1+1/(2r))}.
\]
Then the **ordered singular values** satisfy the sharp limit
\[
\boxed{\lim_{k\to\infty}k^r s_k(D_{r,\theta})=\beta_{r,\theta}M_{r,\theta}^{r}>0.}
\]
Consequently, for every finite \(p>0\),
\[
\boxed{D_{r,\theta}\in\mathcal S_p\quad\Longleftrightarrow\quad p>1/r,}
\]
and at the critical exponent
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{k=1}^N s_k(D_{r,\theta})^{1/r}
=\beta_{r,\theta}^{1/r}M_{r,\theta}.
\]
For the Hardy exponent \(r=1\), \(\lambda_n=\tfrac12[1+\sin((n+1)\theta)/((n+1)\sin\theta)]\). The sharp ordered coefficient is \(1/(\pi\sin\theta)\) for irrational \(\theta/\pi\), but is \(1/4\) at the right-angle twist \(\theta=\pi/2\). Thus the exact high-rank coefficient detects arithmetic resonances, despite an unchanged critical Schatten exponent.

## Assumptions and scope
The parameter \(r\) is any fixed positive real number; for \(r>1\), \(\mathcal H_r\) is the probability-normalized weighted Bergman space with planar weight \((r-1)(1-|z|^2)^{r-2}dA/\pi\). The case \(r=1\) is Hardy space, and \(0<r<1\) is a Dirichlet-type kernel space. The source is the **symmetric**, rather than antisymmetric, Hilbert tensor subspace. Every limit holds with \(r,\theta\) fixed, and the asymptotic is not claimed uniform as \(\theta\) approaches \(0\) or \(\pi\). Singular values \(s_k\) are ordered nonincreasingly and include multiplicity, indexed from \(k=1\). At the two exceptional angles, \(D_{r,\theta}\) is not compact and the singular-value asymptotic above is not asserted.

## Proof
**1. Contractive restriction and exact diagonalization.** Set \(c_n(r)=(r)_n/n!\). The monomials \(\sqrt{c_n(r)}z^n\) form an orthonormal basis of \(\mathcal H_r\). The swap \(U F(z_1,z_2)=F(z_2,z_1)\) is a unitary involution on the tensor product; its symmetric projection is \(P_+=(I+U)/2\). The full tensor evaluation along \(z\mapsto(z,e^{i\theta}z)\) has pullback kernel \((1-z\overline w)^{-2r}\), so restriction is coisometric from the full product onto \(\mathcal H_{2r}\), and its restriction to \(\operatorname{ran}P_+\) is contractive. Applying \(P_+\) in the source kernel gives the exact target kernel of \(R_\theta R_\theta^*\):
\[
\frac12\left[(1-z\overline w)^{-2r}+
(1-e^{i\theta}z\overline w)^{-r}(1-e^{-i\theta}z\overline w)^{-r}\right].
\]
Both terms are radial in \(z\overline w\), and the stated Gegenbauer generating identity gives the eigenvalues after dividing each coefficient by \(c_n(2r)\).

**2. Range and exceptional angles.** Expanding the second kernel coefficient yields
\[
C_n^{(r)}(\cos\theta)=\sum_{j=0}^n c_j(r)c_{n-j}(r)e^{i(n-2j)\theta}.
\]
This is real by symmetry, and its modulus is at most \(\sum_j c_j(r)c_{n-j}(r)=c_n(2r)\). For \(n\ge1\) and \(0<\theta<\pi\), the terms with adjacent \(j\) have unequal phases (their ratio is \(e^{-2i\theta}\ne1\)), so the triangle inequality is strict. Thus \(0<\lambda_n<1\) for \(n\ge1\). The asymptotic in step 3 gives \(\lambda_n\to1/2\), hence their infimum is positive and \(R_\theta\) is onto. At \(\theta=0\), the second generating function equals \((1-t)^{-2r}\). At \(\theta=\pi\), it equals \((1+t)^{-2r}\), giving \(\lambda_n=(1+(-1)^n)/2\).

**3. Fixed-angle Darboux expansion.** For \(0<\theta<\pi\), the generating function \((1-e^{i\theta}t)^{-r}(1-e^{-i\theta}t)^{-r}\) has precisely two distinct algebraic singularities on its unit circle. Expanding the analytic factor at each singularity, and applying the binomial coefficient asymptotic \((r)_n/n!=n^{r-1}/\Gamma(r)+O(n^{r-2})\), gives
\[
C_n^{(r)}(\cos\theta)=\frac{2n^{r-1}}{\Gamma(r)(2\sin\theta)^r}
\cos\left((n+r)\theta-\frac{\pi r}{2}\right)+O_{r,\theta}(n^{r-2}).
\]
The transfer remainder follows, for example, by analytic continuation to a dented annulus around each singularity, subtraction of the leading local singular terms, and a Cauchy-coefficient bound for the first neglected powers. This applies to every real \(r>0\); when \(r\) is integral the same estimate follows by partial fractions. Using \(c_n(2r)=n^{2r-1}/\Gamma(2r)+O(n^{2r-2})\), one obtains the crucial signed diagonal expansion
\[
\lambda_n-\frac12=\beta_{r,\theta}n^{-r}\cos\Phi_n+O_{r,\theta}(n^{-r-1}).
\]
The exact Hardy formula follows from \(C_n^{(1)}(\cos\theta)=\sin((n+1)\theta)/\sin\theta\).

**4. Counting and ordered singular values.** For the nonnegative sequence \(a_n=|\lambda_n-1/2|\), let \(N(t)=\#\{n\ge0:a_n>t\}\). Set \(L=(\beta_{r,\theta}/t)^{1/r}\). After discarding finitely many indices, the expansion in step 3 reduces the scaled count to the fraction of indices with \(n/L\) in a bounded interval and \(|\cos\Phi_n|>(n/L)^r\). If \(\theta/\pi\) is rational, split indices into their finitely many residue classes; each has natural density \(1/v\). If irrational, Weyl's geometric-sum criterion, followed by block approximation in \(n/L\), shows that \((n/L,\Phi_n\bmod\pi)\) becomes product-uniform on each bounded rectangle. Boundary curves have zero limiting measure, including in each rational residue class. Consequently,
\[
\lim_{t\downarrow0}\frac{N(t)}{L}=
\begin{cases}
\frac1v\sum_{j=1}^v|\cos\Phi_j|^{1/r}, &\theta/\pi\in\mathbb Q,\\[2pt]
\frac1\pi\int_0^\pi|\cos u|^{1/r}du, &\theta/\pi\notin\mathbb Q,
\end{cases}
=M_{r,\theta}.
\]
Indeed the integral over the scaled index coordinate of the indicator \(x<|\cos u|^{1/r}\) equals \(|\cos u|^{1/r}\). Strict positivity of the mean follows because consecutive phases cannot both yield zero cosine for a nonexceptional angle. Thus \(N(t)\sim\beta_{r,\theta}^{1/r}M_{r,\theta}t^{-1/r}\). Inverting this monotone counting asymptotic yields \(s_k(D_{r,\theta})\sim\beta_{r,\theta}M_{r,\theta}^r k^{-r}\). The Schatten condition follows from comparison with \(\sum k^{-rp}\), and the logarithmic coefficient at \(rp=1\) follows from the harmonic-series asymptotic. This also proves that the critical weak Schatten inclusion is sharp.

## Verification
The accompanying standard-library checker computes monomial-basis restriction rows independently of the Gegenbauer formula for several kernel exponents and angles. It checks the exceptional angles, the exact right-angle integer-weight formula, the Chebyshev/Hardy reduction, and representative fixed-angle Darboux values. Run `python3 checker.py` in the directory containing this document. In the recorded replay the checker passed **1,446 finite assertions**. These checks validate normalization and sample identities but are not the proof of the coefficient asymptotic, equidistribution or infinite-dimensional classification.

## Relationship to prior work
Misra, Shyam Roy and Zhang (2011) construct weighted Bergman kernels on the symmetrized polydisc using antisymmetric functions and a Jacobian factor. Ghosh and Narayanan (initial preprint February 4, 2022) develop quotient-domain weighted Bergman representation decompositions and Toeplitz algebraic identities, explicitly treating both symmetric-group representations. Bhattacharyya, Das and Sau (initial preprint June 12, 2017) analyze Hardy-space Toeplitz operators on the symmetrized bidisc. These works supply context for invariant holomorphic spaces, but the present object is the **twisted curve trace of the symmetric tensor component**, and the claimed conclusion concerns its exact Gegenbauer spectrum and the rational-versus-irrational coefficient of ordered approximation numbers. The Gegenbauer generating identity, binomial asymptotics and Weyl equidistribution are classical ingredients, not claimed as new. No claim of definitive historical priority is made.

## Limitations
The ordered limit is a fixed-angle statement and is not uniform at the coalescing singularities \(\theta=0,\pi\). The source is the symmetric tensor product with identical scalar kernels; asymmetric weights, higher coordinate permutation groups and nonlinear curves are not treated. The proof shows spectral compactness only for the *centered positive trace operator* \(D_{r,\theta}\), not for the restriction \(R_\theta\) itself. No independent audit or external validation has been performed. Historical-priority risk remains, particularly through other descriptions of kernel compression and Darboux coefficients.

## References
1. G. Ghosh and E. K. Narayanan, *Toeplitz operators on the weighted Bergman spaces of quotient domains*, arXiv:2202.03184, first posted February 4, 2022, https://arxiv.org/abs/2202.03184.
2. G. Misra, S. Shyam Roy and G. Zhang, *Reproducing kernel for a class of weighted Bergman spaces on the symmetrized polydisc*, arXiv:1106.3868, first posted June 20, 2011, https://arxiv.org/abs/1106.3868.
3. T. Bhattacharyya, B. K. Das and H. Sau, *Toeplitz operators on the symmetrized bidisc*, arXiv:1706.03463, first posted June 12, 2017, https://arxiv.org/abs/1706.03463.
4. G. Szegő, *Orthogonal Polynomials*, fourth edition, American Mathematical Society, 1975, standard Gegenbauer generating functions and asymptotics.
