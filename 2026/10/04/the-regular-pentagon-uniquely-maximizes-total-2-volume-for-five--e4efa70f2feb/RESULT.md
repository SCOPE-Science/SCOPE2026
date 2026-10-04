# The regular pentagon uniquely maximizes total \(2\)-volume for five-vector Parseval frames in \(\mathbb R^2\)
## Finding
For a real Parseval frame \(\Phi=\{\varphi_i\}_{i=1}^5\subset\mathbb R^2\), set
\[
V_2(\Phi)=\sum_{1\le i<j\le5}\left|\det(\varphi_i,\varphi_j)\right|.
\]
Then
\[
\max_\Phi V_2(\Phi)=\sqrt{5+2\sqrt5}.
\]
Every maximizer is equivalent, under an orthogonal transformation of \(\mathbb R^2\), a permutation, and independent sign changes of the five vectors, to
\[
\varphi_j=\sqrt{\frac25}\bigl(\cos(2\pi j/5),\sin(2\pi j/5)\bigr),
\qquad j=0,\ldots,4.
\]
Hence the optimizer is equal norm, has two absolute inner-product values rather than one, and is full spark.

## Assumptions and scope
The field is real, the ambient dimension is exactly \(2\), and the frame has exactly five vectors. Parseval means
\[
\sum_{j=1}^5\varphi_j\varphi_j^{\mathsf T}=I_2.
\]
The objective is the total \(2\)-volume from Cahill--Casazza: the sum of the absolute determinants over all unordered pairs. The theorem does not assert the corresponding optimum for other frame lengths or dimensions.

## Proof
Write the \(2\times5\) synthesis matrix as \(X\), with orthonormal rows \(u,v\in\mathbb R^5\); this is equivalent to \(XX^{\mathsf T}=I_2\). For each pair \(i<j\),
\[
\det(\varphi_i,\varphi_j)=u_i v_j-v_i u_j.
\]
For a skew-symmetric sign matrix \(S\) with \(S_{ij}\in\{-1,1\}\) for \(i<j\),
\[
u^{\mathsf T}Sv=\sum_{i<j}S_{ij}(u_i v_j-v_i u_j).
\]
Choosing the signs pairwise therefore gives
\[
V_2(\Phi)=\max_S u^{\mathsf T}Sv.
\]
For fixed real skew-symmetric \(S\), the maximum of \(u^{\mathsf T}Sv\) over orthonormal \(u,v\) is the largest singular value \(\sigma_1(S)\). The upper bound is the operator-norm inequality. Equality is attained by taking a unit right singular vector \(v\) for \(\sigma_1(S)\) and \(u=Sv/\sigma_1(S)\); skew-symmetry gives \(u\perp v\). Thus
\[
\max_\Phi V_2(\Phi)=\max_S\sigma_1(S).
\]

For any such \(5\times5\) skew sign matrix, the nonzero eigenvalues are \(\pm i\sigma_1\) and \(\pm i\sigma_2\). Since every off-diagonal entry has absolute value one,
\[
\sigma_1^2+\sigma_2^2=10.
\]
Its characteristic polynomial is
\[
\lambda\bigl(\lambda^4+10\lambda^2+C(S)\bigr),
\]
where \(C(S)\) is the sum of the squares of the five principal \(4\times4\) Pfaffians. Switching signs by \(S\mapsto DSD\), with diagonal \(D\) having entries \(\pm1\), does not change the singular values. We may therefore normalize the first row above the diagonal to all \(+1\), leaving only six binary signs. Exact enumeration of those \(64\) normalized matrices gives only
\[
C(S)=5\quad\text{or}\quad C(S)=21,
\]
with counts \(24\) and \(40\), respectively. Hence \(\sigma_1^2\) is the larger root of
\[
t^2-10t+C(S)=0.
\]
The two possibilities are
\[
\sigma_1^2=5+2\sqrt5\quad\text{or}\quad \sigma_1^2=7.
\]
Therefore the global upper bound is \(\sqrt{5+2\sqrt5}\).

The regular-pentagon frame is Parseval because the five equally spaced unit directions have second moment \(I_2/2\). Its ten unordered pairs consist of five angular separations of \(2\pi/5\) and five whose absolute sine is \(\sin(\pi/5)\). Thus
\[
V_2=2\bigl(\sin(2\pi/5)+\sin(\pi/5)\bigr)=\sqrt{5+2\sqrt5},
\]
so the upper bound is attained.

It remains to identify equality. Exact signed-permutation enumeration shows that all \(384\) skew sign matrices with \(C(S)=5\) form one orbit under coordinate permutations and diagonal sign switching. For any one of them, \(\sigma_1^2=5+2\sqrt5\) is strictly larger than \(\sigma_2^2=5-2\sqrt5\), so its maximizing real two-plane is unique: it is the top eigenspace of \(-S^2\). Hence all maximizing row spaces are carried into one another by signed coordinate permutations. Changing the orthonormal basis of a fixed row space is exactly a left orthogonal transformation of \(\mathbb R^2\). Since the regular pentagon attains the bound, every maximizer is equivalent to it under the stated operations.

## Verification
The accompanying verifier uses exact integer arithmetic for the finite part of the proof. It enumerates all \(64\) switching-normalized skew sign matrices, computes their five principal Pfaffians, and obtains exactly \(24\) cases with \(C=5\) and \(40\) with \(C=21\). It also enumerates all \(2^{10}=1024\) sign matrices, obtaining \(384\) maximizing matrices and \(640\) matrices in the other spectral class, and verifies that the maximizing \(384\) matrices form one signed-permutation orbit. The continuous reduction from Parseval frames to these sign matrices is analytic; the finite enumeration is exhaustive, not sampled.

## Relationship to prior work
Cahill and Casazza introduced the total-volume optimization problem for Parseval frames and proved that equiangular Parseval frames maximize total \(2\)-volume when such frames exist. In their Section 6 they explicitly ask for explicit solutions of the optimization problem in non-equiangular cases, including small values of the dimension, frame length, and volume order, and ask what structural properties optimizers must have. The present theorem solves the real parameter triple \(N=2\), \(M=5\), \(k=2\), where a five-vector real equiangular tight frame in \(\mathbb R^2\) does not exist. It gives the exact optimum and the complete optimizer class rather than only an example.

Literature searches were also made under the equivalent exterior-algebra formulation: maximizing the \(\ell^1\)-norm of the Plücker coordinates of a decomposable unit bivector in \(\mathbb R^5\), and under the equivalent skew-sign-matrix spectral formulation. No inspected source supplied this exact \(\operatorname{Gr}(2,5)\) value together with the Parseval-frame equality classification. An obscure result in exterior-algebra or tournament-spectral terminology remains the principal originality risk.

## Limitations
The theorem is restricted to real five-vector Parseval frames in dimension two. The exact signed-matrix enumeration is special to order five and does not by itself produce a general formula for other frame lengths. The literature comparison cannot exclude unindexed or differently phrased prior work, especially in exterior algebra, Grassmannian optimization, or skew-tournament spectral theory.

## References
1. J. Cahill and P. G. Casazza, *Optimal Parseval frames: Total coherence and total volume*, arXiv:1910.01733, first submitted 2019-10-03; published in *Linear and Multilinear Algebra*, DOI: 10.1080/03081087.2022.2093320. Primary MSC 42C15.
