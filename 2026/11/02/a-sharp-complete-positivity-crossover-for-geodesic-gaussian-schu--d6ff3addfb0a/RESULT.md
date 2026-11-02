# A sharp complete-positivity crossover for geodesic Gaussian Schur multipliers on cycles

## Finding

Let \(C_n=\mathbb Z/n\mathbb Z\), where \(n\ge3\), carry its unit-edge shortest-path metric
\[
d_n(a,b)=\min\{|a-b|,n-|a-b|\}.
\]
For \(t>0\), set \(K_n(t)_{ab}=\exp(-t d_n(a,b)^2)\), and define the Schur transformation on the complex matrix algebra \(M_n\) by \(\mathcal M_{n,t}(X)=K_n(t)\circ X\). For **each fixed** \(c>0\), as \(n\to\infty\):

* If \(c>\pi\), then \(K_n(c/n)\) is strictly positive definite for all sufficiently large \(n\), and \(\mathcal M_{n,c/n}\) is unital completely positive.
* If \(0<c<\pi\), then \(K_n(c/n)\) has a strictly negative eigenvalue for all sufficiently large \(n\), and \(\mathcal M_{n,c/n}\) is not a positive map.

The number \(\pi\) is therefore the sharp boundary in the scale \(t=c/n\). The negative witnesses also have parity-sensitive leading terms. If \(n=2m\), choose the largest even \(j_n\le m\), and put \(\theta_n=2\pi j_n/n\). The Fourier eigenvalue \(\lambda_{n,j_n}\) obeys, for \(0<c<\pi\),
\[
\lambda_{n,j_n}(c/n)=-\tanh(c/2)\,e^{-cn/4}(1+o(1)).
\]
If \(n=2m+1\), choose the largest even \(j_n\le m\) and write \(\delta_n=n-2j_n\in\{1,3\}\). Then
\[
\lambda_{n,j_n}(c/n)
=-\frac{\pi\delta_n}{n}\frac{e^{-c/2}(1-e^{-c})}{(1+e^{-c})^2}
 e^{-cn/4}(1+o(1)).
\]
The last relative asymptotic is uniform across the two residue classes yielding \(\delta_n=1\) and \(\delta_n=3\).

## Assumptions and scope

Matrices act on \(\mathbb C^n\), the graph edge lengths are all one, \(c\) is fixed independently of \(n\), and limits include both parities. A Hermitian matrix is positive definite here if all its eigenvalues are strictly positive. The Schur map is completely positive precisely when its symbol matrix is positive semidefinite: sufficiency is the Schur-product/Kraus factorization, and necessity follows from applying a positive Schur map to the rank-one all-ones matrix. The theorem does **not** resolve the critical scaling \(c=\pi\), nor assert a global finite-\(n\) monotonicity theorem in the bandwidth parameter.

## Proof

**1. A positive periodization and a small tail.** Write \(t=c/n\) and \(\theta_j=2\pi j/n\). The circulant eigenvalues of \(K_n(t)\) are
\[
\lambda_{n,j}(t)=\sum_{k=0}^{n-1}e^{-t\min(k,n-k)^2}e^{-i\theta_j k}.
\]
Represent the distinct residues by \(I_n=\{-m+1,\ldots,m\}\) for \(n=2m\), and by \(I_n=\{-m,\ldots,m\}\) for \(n=2m+1\). Define
\[
P_t(\theta)=\sum_{k\in\mathbb Z}e^{-tk^2}e^{-i\theta k},\qquad
E_{n,t}(\theta)=\sum_{k\notin I_n}e^{-tk^2}e^{-i\theta k}.
\]
At grid frequencies, \(\lambda_{n,j}(t)=P_t(\theta_j)-E_{n,t}(\theta_j)\). Poisson summation gives the strictly positive expansion
\[
P_t(\theta)=\sqrt{\frac\pi t}\sum_{q\in\mathbb Z}
 \exp\left(-\frac{(\theta-2\pi q)^2}{4t}\right).
\]
Every frequency has a representative of absolute value at most \(\pi\), so
\[
P_{c/n}(\theta_j)\ge\sqrt{\frac{\pi n}{c}}e^{-\pi^2n/(4c)}.
\]
Since any omitted integer has \(|k|\ge n/2\), and the Gaussian terms beyond the boundary decay by at least a factor \(e^{-c}\) per unit step,
\[
|E_{n,c/n}(\theta_j)|\le\frac{2e^{-cn/4}}{1-e^{-c}}.
\]
For \(c>\pi\), the ratio between the lower bound on \(P\) and upper bound on \(|E|\) grows exponentially because \(c/4>\pi^2/(4c)\). Thus all Fourier eigenvalues are eventually strictly positive.

**2. Even cycles below the boundary.** Let \(n=2m\) and take the even integer \(j_n\le m\) nearest to \(m\), so \(\theta_n\to\pi\). The omitted tail has the *exact* identity
\[
E_{n,c/n}(\theta_n)=(-1)^{j_n}e^{-cn/4}
\left[1+2\sum_{r=1}^{\infty}e^{-cr-cr^2/n}\cos(r\theta_n)\right].
\]
Here \(j_n\) is even. Dominated convergence for the absolutely summable geometric majorant gives
\[
e^{cn/4}E_{n,c/n}(\theta_n)\longrightarrow
1+2\sum_{r\ge1}(-e^{-c})^r=\tanh(c/2)>0.
\]
At these frequencies \(|\theta_n-\pi|=O(1/n)\). The Poisson formula bounds \(P_{c/n}(\theta_n)\) by \(O_c(\sqrt n\,e^{-\pi^2n/(4c)+O_c(1)})\). When \(c<\pi\), this is \(o(e^{-cn/4})\), yielding the even-cycle negative-eigenvalue asymptotic.

**3. Odd cycles below the boundary.** Put \(n=2m+1\), choose the largest even \(j_n\le m\), and set \(\delta_n=n-2j_n\in\{1,3\}\). Then \(\theta_n=\pi-\pi\delta_n/n\), and pair the two omitted tails to obtain
\[
E_{n,c/n}(\theta_n)
=2e^{-cn/4}\sum_{r=0}^{\infty}(-1)^r
 e^{-c(r+1/2)-c(r+1/2)^2/n}
 \sin\left(\frac{\pi\delta_n(r+1/2)}n\right).
\]
Multiplying by \(ne^{cn/4}\), the bound \(|\sin u|\le |u|\) and an absolutely convergent exponential majorant justify passage to the limit, separately for \(\delta_n=1\) and \(3\). With \(q=e^{-c}\), the resulting geometric-derivative sum is
\[
2\pi\delta\sum_{r\ge0}(-1)^r(r+1/2)q^{r+1/2}
=\pi\delta\frac{q^{1/2}(1-q)}{(1+q)^2}>0.
\]
Again \(P_{c/n}(\theta_n)=O_c(\sqrt n\,e^{-\pi^2n/(4c)+O_c(1)})=o(e^{-cn/4}/n)\) when \(c<\pi\). Subtracting \(E\) proves the odd-cycle formula. Together with step 1, this proves the transition and the Schur-map conclusions. \(\square\)

## Verification

`verify_gaussian_cycle.py` is a standalone finite-precision and high-precision cross-check, requiring Python 3 and `mpmath`. It compares direct circulant Fourier eigenvalues with the periodized-Gaussian-minus-tail identity, verifies positive spectra above \(\pi\) and negative witness spectra below \(\pi\) at selected dimensions, and tests the two parity-dependent asymptotic constants. It does not treat finite numerical tests as proof of the all-dimensional assertions; those follow from the preceding uniform bounds and dominated-convergence arguments.

## Relationship to prior work

Da Costa, Mostajeran and Ortega (arXiv:2302.10623, first posted 2023-02-21) prove that the Gaussian kernel of *fixed physical scale* is not positive definite on the continuous geodesic circle, by finding negative eigenvalues on sufficiently fine equally spaced grids. They explicitly note that fixed finite grids recover positivity at sufficiently large Gaussian parameters. Li (arXiv:2303.06558, first posted 2023-03-12) extends the continuous non-positivity obstruction to compact non-simply-connected Riemannian manifolds and poses a quantitative coarse-versus-fine-scale question. Here the physical Gaussian parameter grows with sample size and the finite-grid phase boundary is the explicit constant \(\pi\) in graph-unit scaling, with sharp negative-mode asymptotics for both parities. Neither of those published statements determines this moving-parameter threshold.

Circulant embedding and covariance periodization are classical; Graham, Kuo, Nuyens, Scheichl and Sloan (arXiv:1710.00751) treat positivity of circulant embeddings of stationary random-field covariance functions, including Matérn examples, under different periodization/parameter hypotheses. Wood (1995) studies periodic truncation of covariance functions on the continuous circle; its abstract does not determine this finite sampling threshold, but the unavailable full text remains a comparison risk.

## Limitations

The crossover is asymptotic for fixed \(c\neq\pi\); neither the sign exactly at \(c=\pi\), the finite-\(n\) exact critical bandwidth, nor a uniform window shrinking toward \(\pi\) is claimed. The proof exploits equal spacing and the one-dimensional geodesic cycle; no general graph or manifold theorem is claimed. Priority remains subject to searching other terminology for circulant covariance extensions, geodesic Gaussian sampling, and Fourier aliasing.

## References

1. N. Da Costa, C. Mostajeran, J.-P. Ortega, *The Gaussian kernel on the circle and spaces that admit isometric embeddings of the circle*, arXiv:2302.10623 (version 1, 2023-02-21), https://arxiv.org/abs/2302.10623.
2. S. Li, *Gaussian kernels on non-simply-connected closed Riemannian manifolds are never positive definite*, arXiv:2303.06558 (version 1, 2023-03-12), https://arxiv.org/abs/2303.06558.
3. I. G. Graham, F. Y. Kuo, D. Nuyens, R. Scheichl, I. H. Sloan, *Analysis of circulant embedding methods for sampling stationary random fields*, arXiv:1710.00751 (2017), https://arxiv.org/abs/1710.00751.
4. A. T. A. Wood, *When is a truncated covariance function on the line a covariance function on the circle?*, Statistics & Probability Letters 24 (1995), 157–164, DOI:10.1016/0167-7152(94)00162-2.
