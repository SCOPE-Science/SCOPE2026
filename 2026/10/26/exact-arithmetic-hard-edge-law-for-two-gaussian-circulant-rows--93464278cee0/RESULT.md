# Exact arithmetic hard-edge law for two Gaussian circulant rows

## Finding
For each integer \(m\ge2\) and shift \(r\) with \(1\le r<m\), a real Gaussian circulant sketch formed by two rows has an exact least-singular-value hard-edge asymptotic. Let \(d=\gcd(m,r)\), \(L=m/d\), \(k=m-d\), and define \(q_L=1\) when \(L\) is odd and \(q_L=2\) when \(L\) is even. Then
\[
\Pr(\sigma_{\min}(H)\le t)=\frac{q_L}{L^d\Gamma(k/2+1)}t^k+o(t^k)\qquad(t\downarrow0).
\]
In particular, for every real \(p>0\),
\[
\mathbb E\|H^\dagger\|_2^p<\infty\quad\Longleftrightarrow\quad p<k,
\qquad\mathbb E\kappa_2(H)^p<\infty\quad\Longleftrightarrow\quad p<k.
\]
Equality \(p=k\) is divergent in both tests. The leading constant contains an exact parity factor and an arithmetic dependence on the row offset, not merely the number of columns.

## Assumptions and scope
Let \(g=(g_0,\dots,g_{m-1})^T\in\mathbb R^m\) have independent \(N(0,1)\) components. Let \(S\in\mathbb R^{m\times m}\) be the cyclic shift \((Sg)_j=g_{(j+r)\bmod m}\). Define the unnormalized sketch \(H\in\mathbb R^{2\times m}\) by stacking \(g^T\) and \((Sg)^T\). Singular values are ordinary Euclidean singular values, \(H^\dagger\) denotes the Moore–Penrose pseudoinverse, and \(\kappa_2(H)=\sigma_{\max}(H)/\sigma_{\min}(H)\) off its probability-zero rank-deficiency set. All statements hold for each fixed admissible \((m,r)\); the constants are not asserted uniform as dimension grows.

## Proof
**Step 1 — exact Gram reduction.** Since \(S\) is orthogonal, direct multiplication gives
\[
HH^T=\begin{pmatrix}\|g\|_2^2&g^TSg\\g^TSg&\|g\|_2^2\end{pmatrix}.
\]
With \(C=(S+S^T)/2\) and \(B_\pm=I\mp C\), the least squared singular value therefore satisfies the exact, non-asymptotic identity
\[
\sigma_{\min}(H)^2=\|g\|_2^2-|g^TSg|=\min\{g^TB_+g,g^TB_-g\}.
\]

**Step 2 — cyclic spectrum and Gaussian quadratic forms.** The permutation \(S\) splits into exactly \(d\) disjoint cycles of length \(L\). Hence the real symmetric matrix \(C\) has eigenvalues \(\cos(2\pi j/L)\), \(j=0,\dots,L-1\), each counted with multiplicity \(d\). Thus \(B_+\) is positive semidefinite with kernel dimension \(d\); \(B_-\) is positive definite when \(L\) is odd, and otherwise has kernel dimension \(d\). Each singular member has rank \(k=m-d\). The classical sine-product identity gives
\[
\prod_{j=1}^{L-1}(1-\cos(2\pi j/L))=\frac{L^2}{2^{L-1}},
\]
so the product of the nonzero eigenvalues of \(B_+\) is \((L^2/2^{L-1})^d\); by shifting Fourier indices, the same holds for \(B_-\) when \(L\) is even.

**Step 3 — sharp leading constant.** If \(Q=\sum_{i=1}^{k}\lambda_i Z_i^2\), where all \(\lambda_i>0\) and the \(Z_i\) are independent \(N(0,1)\), continuity of the Gaussian density at the origin and the ellipsoid volume formula show that
\[
\Pr(Q\le t^2)=\frac{t^k}{2^{k/2}\Gamma(k/2+1)\sqrt{\prod_i\lambda_i}}+o(t^k).
\]
Substitute the nonzero eigenvalue product from Step 2. Since \(k=d(L-1)\), the two powers of \(2\) cancel, leaving \(1/(L^d\Gamma(k/2+1))\) for each singular quadratic form. When \(L\) is odd, \(B_-\) is positive definite and its contribution is only \(O(t^m)=o(t^k)\). When \(L\) is even, both singular events contribute the same constant. Their intersection implies \(g^TB_+g\le t^2\) and \(g^TB_-g\le t^2\), whence \(2\|g\|_2^2=g^T(B_++B_-)g\le2t^2\); this has probability \(O(t^m)=o(t^k)\). Inclusion–exclusion therefore proves the asserted coefficient, without assuming independence of the two events.

**Step 4 — rank and moment endpoints.** A zero least singular value requires membership in one of the proper nullspaces in Step 2; both are Gaussian-null sets, so the sketch has full row rank almost surely. The hard-edge law and the layer-cake identity imply \(\mathbb E[\sigma_{\min}(H)^{-p}]<\infty\) exactly when \(p<k\), with logarithmic divergence at equality. Finally write \(g=Ru\), where \(R=\|g\|_2\) and \(u\) is uniform on the sphere, independently. The ratio \(\kappa_2(H)\) depends only on \(u\); near the rank-one subspaces its numerator stays bounded above and below by positive constants while its denominator is proportional to the distance to their union. The spherical small-tube probability has exponent \(k\), by the same transverse quadratic-form argument. Thus its inverse tail has the identical sharp moment cutoff. The Gaussian radial moment is finite for \(p<k<m\), and establishes the pseudoinverse cutoff without an additional origin obstruction.

## Verification
The accompanying `VERIFY.py` checks the Gram identity, the exact cyclic eigenvalue zero multiplicities, and the nonzero eigenvalue products for all \(2\le m\le30\) and admissible shifts. These finite checks are corroboration, not an infinite proof; the proof above handles all dimensions. A direct consistency check for \(m=2,r=1\) gives the exact small-tail coefficient \(2/\sqrt\pi\).

## Relationship to prior work
Krahmer, Mendelson, and Rauhut study restricted isometry for random partial circulant matrices and obtain high-probability bounds for sparse recovery. Their matrix-generation setting motivates studying structured dependence but their RIP bounds do not determine a two-row least-singular-value hard-edge constant or inverse moments. Saibaba and Międlar analyze randomized low-rank approximations under four independent-entry/column sampling classes; their general tail estimates do not specialize to the dependent two-row circulant Gaussian model here. Existing fixed-two-row Gaussian Hankel conditioning results involve a non-circular observation window and give no implication for the shift-gcd and cycle-parity structure. The new statement has been compared on the level of objects, assumptions, and implications; identification of a logically equivalent result in older specialized structured-random-matrix literature remains a possible originality risk.

## Limitations
The formula concerns exactly two unnormalized real Gaussian circulant rows. It does not establish the analogous constant for three or more sampled rows, non-Gaussian generators, complex Gaussian seeds, arbitrary noncyclic correlations, nor an upper bound uniform over growing dimension. For a sketch scaled by a deterministic factor, the threshold constant scales accordingly. No independence or external certification of this result is claimed.

## References
1. F. Krahmer, S. Mendelson, H. Rauhut, *Suprema of Chaos Processes and the Restricted Isometry Property*, arXiv:1207.0235, 2012/2013; https://arxiv.org/abs/1207.0235.
2. A. K. Saibaba, A. Międlar, *Randomized Low-Rank Approximations Beyond Gaussian Random Matrices*, arXiv:2308.05814, first posted 10 August 2023; https://arxiv.org/abs/2308.05814.
