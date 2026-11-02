# Gaussian positivity on squared cycles: an isolated nine-vertex exception

## Finding
Let \(C_n^2\) be the square of the cycle on \(n\ge3\) vertices: vertices are the residue classes \(\mathbb Z/n\mathbb Z\), joined when their cyclic difference has minimum absolute residue \(1\) or \(2\). Let \(d_n\) be the ordinary shortest-path distance in this graph. Then
\[
\boxed{\ e^{-t d_n(u,v)}\text{ is positive semidefinite for every }t>0
\quad\Longleftrightarrow\quad n\text{ is even, or }n\in\{3,5,9\}.\ }
\]
For all orders on the right, the kernel matrix is actually strictly positive definite for every \(t>0\). For every other order there exists \(\varepsilon_n>0\) such that it is not positive semidefinite whenever \(0<t<\varepsilon_n\).

The following Fourier formulas give the complete distance-matrix spectrum (and constitute a more detailed form of the classification). For \(0\le j<n\), write \(\lambda_j\) for the eigenvalue corresponding to \(u\mapsto e^{2\pi iju/n}\). At frequency zero the row sum is
\[
\lambda_0=
\begin{cases}
N(N+1)/2,&n=2N,\\
N(N+1)/2+\lceil N/2\rceil,&n=2N+1.
\end{cases}
\]
For \(1\le j<n\), when \(n\) is even,
\[
\boxed{\lambda_j=-\frac{1-(-1)^j}{4\sin^2(\pi j/n)}-\frac n4\mathbf 1_{\{j=n/2\}}.}
\]
For odd \(n=2N+1\),
\[
\boxed{\lambda_j=-\frac14\left(\frac1{1+(-1)^j\cos(\pi j/n)}+
\frac{(-1)^{N+j}}{\cos(\pi j/n)}\right).}
\]
In particular, the squared-Euclidean embedding dimensions of \(d_n\) in the admissible cases are \(n/2+1\) for \(n\equiv0\pmod4\), \(n/2\) for \(n\equiv2\pmod4\), and respectively \(2,4,6\) for \(n=3,5,9\).

## Assumptions and scope
The graph power is taken before measuring shortest paths; its distance is not the square of an ordinary cycle distance. Explicitly, for representatives \(k\in\{0,\dots,n-1\}\),
\[
d_n(0,k)=\left\lceil\frac{\min(k,n-k)}2\right\rceil.
\]
The matrix \(D_n=(d_n(u,v))\) is real symmetric and circulant. A finite metric \(d\) is conditionally negative semidefinite when \(\sum_{u,v}a_u a_vd(u,v)\le0\) for every real vector \(a\) with \(\sum a_u=0\). The finite Schoenberg criterion equates this property with positive semidefiniteness of \((e^{-td(u,v)})\) for all \(t>0\); it also equates it with the existence of a squared-Euclidean realization of \(d\).

## Proof
**1. Fourier reduction.** Put \(\delta(k)=\min(k,n-k)\) and \(h(k)=\delta(k)\bmod2\). Pointwise on the cycle,
\[
d_n(0,k)=\tfrac12\bigl(\delta(k)+h(k)\bigr).
\]
The characters \(\chi_j(k)=e^{2\pi ijk/n}\) diagonalize every circulant matrix, with eigenvalues \(\widehat d(j)=\sum_{k=0}^{n-1}d_n(0,k)e^{-2\pi ijk/n}\). All the nonconstant eigenvectors are orthogonal to the constants. The row sums follow by summing \(\delta\) and \(h\) separately.

**2. Even cycles.** For \(n=2N\), the parity of the shortest cyclic distance agrees with the parity of \(k\). Hence \(h(k)=(1-(-1)^k)/2\). Its nonconstant Fourier transform vanishes except at \(j=N\), where it is \(-N\). For the ordinary even-cycle distance, the cyclic second difference has mass \(2\) at zero and \(-2\) at the antipode, and its Fourier transform gives
\[
\widehat\delta(j)=-\frac{1-(-1)^j}{2\sin^2(\pi j/n)}\qquad(1\le j<n).
\]
Combining the two transforms proves the displayed even-order formula. Every nonconstant eigenvalue is nonpositive. The zero modes are exactly the even \(j\) other than \(j=N\) when \(N\) is even: their number is \(n/2-2\) if \(4\mid n\), or \(n/2-1\) if \(n\equiv2\pmod4\).

**3. Odd cycles.** Write \(n=2N+1\) and \(\theta=2\pi j/n\), \(c=\cos(\theta/2)\). The ordinary cycle distance has cyclic second difference \(2\delta_0-\delta_N-\delta_{N+1}\), so for nonzero frequencies,
\[
\widehat\delta(j)=-\frac{1-(-1)^jc}{2\sin^2(\theta/2)}.
\]
Moreover \(g(k)=(-1)^{\delta(k)}\) equals \((-1)^k\) on the symmetric representative interval \(-N\le k\le N\). Its Dirichlet sum is
\[
\widehat g(j)=\sum_{k=-N}^{N}(-1)^k e^{-ik\theta}
=\frac{(-1)^{N+j}}{\cos(\theta/2)}.
\]
Because \(h=(1-g)/2\), we have \(\widehat h(j)=-\widehat g(j)/2\) at nonzero frequencies. The identity \((1-(-1)^jc)/\sin^2(\theta/2)=1/(1+(-1)^jc)\) gives the displayed odd-order formula. Every denominator is nonzero, since \(n\) is odd.

**4. Exhaustive sign classification.** It suffices to examine \(1\le j\le N\), for which \(0<c<1\); the partner mode \(n-j\) has the same eigenvalue.

If \(N\) is odd (\(n\equiv3\pmod4\)), odd \(j\) give a negative eigenvalue, whereas every even \(j\) gives
\[
\lambda_j=\frac1{4c(1+c)}>0.
\]
There is such a mode exactly when \(n\ge7\). Thus the sole admissible order in this congruence class is \(n=3\).

If \(N\) is even (\(n\equiv1\pmod4\)), even \(j\) give negative eigenvalues, whereas for odd \(j\)
\[
\lambda_j=\frac{1-2c}{4c(1-c)}.
\]
This is positive exactly when \(j>n/3\), zero exactly when \(j=n/3\), and negative below. The largest eligible odd \(j\le N\) is \((n-3)/2\), which exceeds \(n/3\) exactly when \(n>9\). Thus \(n=5\) has no positive nonconstant mode, \(n=9\) has two zero modes and no positive one, and every \(n\equiv1\pmod4\) with \(n\ge13\) has a positive nonconstant mode. This proves the classification.

**5. Gaussian equivalence and rank.** Negative semidefiniteness of \(D_n\) on the zero-sum space is equivalent to nonpositivity of all its nonconstant Fourier eigenvalues. By the finite Schoenberg theorem this is equivalent to universal Gaussian positive semidefiniteness. Distinct vertices have strictly positive distance, so their squared-Euclidean images are distinct; the Gaussian matrix of distinct Euclidean points is strictly positive definite for every \(t>0\). Conversely a positive nonconstant eigenvalue \(\lambda_j\) produces a negative Gaussian eigenvalue \(-t\lambda_j+O(t^2)\) for sufficiently small \(t>0\). The minimal Euclidean dimension is the rank of \(-\tfrac12 H D_n H\), with \(H=I-J/n\), and the zero-mode counts in steps 2 and 4 give the stated dimensions. At \(n=9\), the two zero frequencies are exactly \(j=3,6\).

## Verification
Run \(`python3 check.py`\) with Python 3 and no external packages. The checker separately constructs shortest paths by breadth-first search on the graph, verifies translation invariance, computes every discrete Fourier eigenvalue directly, and compares these against both analytic formulas for every \(3\le n\le128\). It also checks the predicted positive and zero frequency sets, and the exact three-residue cancellation at \(n=9\). The run produced \(`CHECK_OK 732270`\). These are finite corroborations, not substitutes for the all-order Fourier proof.

## Relationship to prior work
Atik and Panigrahi (2016), Theorem 2.2, already determine the full distance spectrum for **even** squared cycles. That entire even-order spectral component is prior art; the proof here rederives it only to give a self-contained treatment and a negative-type formulation. The distinctive result assessed here is the complementary **odd-order** formula and the resulting all-order Gaussian-positivity classification, particularly the otherwise isolated \(n=9\) admissible odd cycle. Zhou (2014) studies distance spectral radii of circulants, not their centered Fourier spectra. Aalipour and collaborators (2015) study distance inertia and other graph families but do not state the odd square-cycle result. All these papers provide relevant context and machinery; they should not be represented as proving the new odd-order classification.

## Limitations
The theorem concerns the graph power two and the ordinary distance exponent one. It does not determine the sharp powered-distance exponent outside this exponent, nor all positive bandwidths in inadmissible orders: it proves Gaussian failure for sufficiently small bandwidth only. The available literature comparison is bounded and is not proof of absolute historical novelty; a different-name formulation of the odd square-cycle distance spectrum could exist.

## References
1. Houqing Zhou, *The Wiener Index of Circulant Graphs*, Journal of Chemistry (2014), DOI: 10.1155/2014/742121. First publicly dated 2014-04-09. https://doi.org/10.1155/2014/742121
2. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196v1 (public 2015-09-03), https://arxiv.org/abs/1509.01196
3. Fouzul Atik and Pratima Panigrahi, *Families of graphs having few distinct distance eigenvalues with arbitrary diameter*, Electronic Journal of Linear Algebra 29 (2016), 194–205, Theorem 2.2. https://journals.uwyo.edu/index.php/ela/article/download/1493/1493/1493
4. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536. The standard finite negative-type/Gaussian equivalence is used, not claimed as new.
