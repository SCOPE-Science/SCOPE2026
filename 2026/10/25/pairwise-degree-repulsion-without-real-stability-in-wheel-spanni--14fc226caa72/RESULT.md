# Pairwise degree repulsion without real stability in wheel spanning trees

## Finding
For every integer \(m\ge5\), the degrees of **every pair of distinct vertices** of a uniform random spanning tree of the wheel \(W_{m+1}=K_1\vee C_m\) have **strictly negative covariance**, although its spanning-tree degree enumerator is **not real stable**. In particular, for neighboring rim vertices \(0,1\),
\[
\operatorname{Cov}(D_0,D_1)=-\frac12(57x_m^2-50x_m+11)
=-\frac{57}{2}\left(x_m-\frac{25}{57}\right)^2-\frac1{57}<0,
\]
where
\[
q=\frac{3-\sqrt5}{2},\qquad x_m=\frac{1+q^m}{\sqrt5(1-q^m)}.
\]
The same pair in the **bare** uniform spanning tree of \(C_m\) has positive covariance \((m-4)/m^2\), for \(m\ge5\). Thus adjoining the hub reverses the adjacent degree-covariance sign without attaining real stability.

## Assumptions and scope
All graphs are finite, simple and labeled. The wheel has rim vertices \(0,1,\ldots,m-1\), rim edges \(\{i,i+1\bmod m\}\), and hub \(h\) connected to every rim vertex. \(T\) is uniform over all spanning trees, with no edge or degree external-field weights. Set \(D_v=\deg_T(v)\). The degree enumerator is
\[
F_W(z)=\sum_{T\text{ spanning tree}}\prod_{v\in V(W)} z_v^{D_v(T)-1}.
\]
Real stability means nonvanishing whenever every complex variable has strictly positive imaginary part. The negative covariances concern the single uniform measure; they do not claim uniform Rayleigh or strong Rayleigh inequalities under arbitrary tilts.

## Proof
**Transfer-current identity.** Ground the wheel Laplacian at its hub, obtaining the positive-definite \(m\times m\) matrix \(L=3I-A(C_m)\). Put \(H=L^{-1}\). Orient rim edges arbitrarily and orient spokes toward the hub, with grounded incidence columns \(b_e\); for a spoke \(b_{\{i,h\}}=e_i\). The weighted matrix-tree theorem gives \(Z(t)=\det(\sum_e t_eb_eb_e^{\mathsf T})\). Differentiate \(\log Z\) at \(t_e=1\): for distinct edges,
\[
\operatorname{Cov}(I_e,I_f)=-(b_e^{\mathsf T}Hb_f)^2,
\]
while \(\operatorname{Var}(I_e)=K_{ee}-K_{ee}^2\), where \(I_e=\mathbf1_{\{e\in T\}}\) and \(K_{ef}=b_e^{\mathsf T}Hb_f\). Consequently, for incident-edge sets \(S_u,S_v\),
\[
\operatorname{Cov}(D_u,D_v)=\sum_{e\in S_u\cap S_v}K_{ee}-\sum_{e\in S_u}\sum_{f\in S_v}K_{ef}^2.
\]

**Nonadjacent rim vertices.** Their incident-edge sets do not intersect. Furthermore,
\[
H=\frac13\sum_{k=0}^{\infty}(A(C_m)/3)^k
\]
is entrywise positive (the cycle is connected), so the spoke–spoke term \(K_{\{u,h\},\{v,h\}}=H_{uv}>0\) ensures strictly negative covariance.

**Adjacent rim vertices.** Let \(g_j=H_{0j}\), \(x=g_0\). Translation and reflection symmetry give \(g_1=(3x-1)/2\), \(g_2=3g_1-x\), and \(g_3=3g_2-g_1\), using \(LH=I\). For \(m\ge5\), all indices in these relations are well defined, including the antipodal coincidence when \(m=5\). Orient the three incident edges at vertex \(0\) as \(s_0=\{0,h\}\), \(b_{m-1,0}\), \(b_{0,1}\), and at vertex \(1\) as \(s_1\), \(b_{0,1}\), \(b_{1,2}\), with rim edges directed forward. The \(3\times3\) transfer-current block is
\[
\left(K_{ef}\right)_{e\in S_0,f\in S_1}
=\begin{pmatrix}
(3x-1)/2&(1-x)/2&1-2x\\
2x-1&-(3x-1)/2&(3-7x)/2\\
(x-1)/2&1-x&-(3x-1)/2
\end{pmatrix}.
\]
Its squared Frobenius norm is \((57x^2-52x+13)/2\), while the sole shared-edge diagonal \(K_{b_{0,1},b_{0,1}}=1-x\). Therefore
\[
\operatorname{Cov}(D_0,D_1)
=1-x-\frac{57x^2-52x+13}{2}
=-\frac{57x^2-50x+11}{2}.
\]
Completing the square gives the asserted strict negativity with no numerical estimates. The diagonal Green function has the explicit Fourier representation
\[
x=\frac1m\sum_{j=0}^{m-1}\frac1{3-2\cos(2\pi j/m)}
=\frac{1+q^m}{\sqrt5(1-q^m)},\quad q=\frac{3-\sqrt5}{2}.
\]
The last equality follows by periodizing the infinite-line Green function \(q^{|j|}/\sqrt5\), which solves the recurrence for \(3I-A\).

**Hub–rim pairs.** Every spanning tree has \(2m\) total degree, so \(D_h+\sum_{i=0}^{m-1}D_i=2m\) identically. Rotational symmetry yields \(\operatorname{Cov}(D_h,D_i)=-\operatorname{Var}(D_h)/m\). The hub-centered star and the tree made by replacing a spoke by its neighboring rim edge have different hub degrees and both have positive probability, whence \(\operatorname{Var}(D_h)>0\).

**Non-real-stability.** Cherkashin–Petrov–Prozorov (2022), Theorem 1, proves that the spanning-tree degree enumerator is real stable exactly for distance-hereditary graphs. A wheel with \(m\ge5\) has the chordless cycle \(C_m\) as an induced subgraph, so it is not distance hereditary. Their theorem therefore establishes non-real-stability; the new contribution here is not that non-stability criterion but the strict covariance separation and explicit adjacent certificate.

**Bare-cycle contrast.** A uniform spanning tree of \(C_m\) omits exactly one uniformly chosen edge. Each of two adjacent rim degrees is \(2\) minus the indicator that its respective incident edge is deleted. Hence their covariance is \(1/m-4/m^2=(m-4)/m^2>0\). This contrasts with the wheel formula for the same adjacent vertices.

## Verification
The standalone pure-standard-library script `verify.py` exactly inverts \(3I-A(C_m)\) over rational numbers and compares the full degree covariance matrix to edge-transfer-current formulas, the adjacent closed form, hub symmetry and strict signs for \(3\le m\le15\). It also enumerates every wheel spanning tree for \(3\le m\le8\), comparing empirical covariances to the independent kernel calculation. It reports `VERIFY_OK 1025 exact identities; enumerated 3548 wheel spanning trees`. These finite checks are supporting reproducibility, not substitutes for the all-\(m\) proof.

## Relationship to prior work
The stability/non-stability statement is a direct consequence of the **existing** graph classification in Cherkashin, Petrov and Prozorov (2022); the 2023 weighted extension by Cherkashin and Prozorov is also relevant. Neither inspected work supplies the explicit wheel UST adjacent degree covariance or establishes its simultaneous strict pairwise negativity under the unweighted law. The transfer-current identity is standard matrix-tree/DPP machinery and is not new. The additional content here is the exact spectral Green-function calculation establishing the uniform-measure phenomenon even in a nonstable degree-polynomial family.

## Limitations
The negative-covariance conclusion holds for **uniform** wheel spanning trees and does not imply negative correlations under arbitrary vertex-degree reweightings, negative association of the vector of degrees, or real stability. Historical uniqueness is not guaranteed: the covariance specialization may be implicit in earlier transfer-current calculations. The 2019 article on wheel subtrees could not be materially inspected because the publisher response was inaccessible, and a comprehensive historical audit remains outstanding. The proof is exact for all integers \(m\ge5\), with smaller values not used for the non-stability contrast.

## References
1. D. Cherkashin, F. Petrov and P. Prozorov, *On stability of spanning tree degree enumerators*, arXiv:2209.04413, first public 2022-09-09. https://arxiv.org/abs/2209.04413
2. D. Cherkashin and P. Prozorov, *On stability of weighted spanning tree degree enumerators*, arXiv:2310.18051, first public 2023-10-27. https://arxiv.org/abs/2310.18051
3. The matrix-tree theorem and the transfer-current identity for uniform spanning trees (standard results; derived by log-determinant differentiation above).
