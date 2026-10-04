# Exact total-coherence maximizers for four real planar Parseval vectors
## Finding
Let \(\Phi=\{\varphi_i\}_{i=1}^4\subset\mathbb R^2\) be a real Parseval frame, so
\[
\sum_{i=1}^4 \varphi_i\varphi_i^{\mathsf T}=I_2,
\]
and define the ordered total coherence
\[
TC(\Phi)=\sum_{i\ne j}|\langle\varphi_i,\varphi_j\rangle|.
\]
Then
\[
\max_\Phi TC(\Phi)=1+\sqrt5.
\]
All maximizers are equivalent, under an orthogonal transformation of \(\mathbb R^2\), a permutation of the four frame vectors, and independent sign changes, to the Gram matrix
\[
P_0=\begin{pmatrix}
a&a&c&c\\
a&a&c&c\\
c&c&b&-a\\
c&c&-a&b
\end{pmatrix},
\qquad
a=\frac{5+\sqrt5}{20},\quad
b=\frac{15-\sqrt5}{20},\quad
c=\frac{\sqrt5}{10}.
\]
Thus the squared norms of every maximizing frame form the multiset \(\{a,a,b,b\}\). In particular, no maximizer is equal norm, and every maximizer contains a parallel pair. An explicit maximizer is
\[
\varphi_1=\varphi_2=(\sqrt a,0),
\]
\[
\varphi_3=\left(\sqrt{\frac{5-\sqrt5}{20}},\frac1{\sqrt2}\right),\qquad
\varphi_4=\left(\sqrt{\frac{5-\sqrt5}{20}},-\frac1{\sqrt2}\right).
\]

## Assumptions and scope
The result is for real Parseval frames of exactly four vectors in \(\mathbb R^2\), with total coherence counting ordered pairs, as in the cited total-coherence problem. It does not assert the corresponding optimum for complex frames or for other pairs of frame size and dimension.

## Proof
Let \(F\) be the \(2\times4\) synthesis matrix with columns \(\varphi_i\). Parseval tightness is \(FF^{\mathsf T}=I_2\). Hence the Gram matrix
\[
P=F^{\mathsf T}F
\]
is a rank-two orthogonal projection in \(\mathbb R^4\). Conversely, every rank-two orthogonal projection is the Gram matrix of a real Parseval frame in \(\mathbb R^2\).

Let \(\mathcal S_4\) be the set of real symmetric \(4\times4\) matrices with zero diagonal and off-diagonal entries in \(\{-1,1\}\). For any fixed projection \(P\), choose the off-diagonal signs of \(S\in\mathcal S_4\) to match those of \(P\). Then
\[
TC(P)=\max_{S\in\mathcal S_4}\operatorname{tr}(SP).
\]
Therefore
\[
\max_P TC(P)
=\max_{S\in\mathcal S_4}\max_{\substack{P^2=P=P^{\mathsf T}\\\operatorname{rank}P=2}}\operatorname{tr}(SP).
\]
By the Ky Fan variational principle, the inner maximum is \(\lambda_1(S)+\lambda_2(S)\), where the eigenvalues are in decreasing order.

Diagonal sign switching and simultaneous row-column permutation preserve the spectrum of \(S\). Switching can normalize the first row above the diagonal to \((1,1,1)\), leaving
\[
S(a_1,a_2,a_3)=
\begin{pmatrix}
0&1&1&1\\
1&0&a_1&a_2\\
1&a_1&0&a_3\\
1&a_2&a_3&0
\end{pmatrix},\qquad a_1,a_2,a_3\in\{-1,1\}.
\]
Using \(a_j^2=1\), its characteristic polynomial is
\[
x^4-6x^2-2(a_1a_2a_3+a_1+a_2+a_3)x+3-2(a_1a_2+a_1a_3+a_2a_3).
\]
If none of the \(a_j\) are negative, the spectrum is \(\{3,-1,-1,-1\}\); if all three are negative, it is \(\{1,1,1,-3\}\). If exactly one or exactly two are negative, the characteristic polynomial is
\[
(x^2-1)(x^2-5),
\]
so the spectrum is \(\{\sqrt5,1,-1,-\sqrt5\}\). Consequently the largest possible sum of the two top eigenvalues is
\[
1+\sqrt5,
\]
which proves the sharp upper bound.

For equality, the sign matrix attached to a maximizing projection must be in the middle switching class. Because its second and third eigenvalues satisfy \(1>-1\), equality in the Ky Fan principle has a unique maximizing rank-two projection: the spectral projection onto the positive eigenspace. Every sign matrix in this middle class is switching-permutation equivalent to
\[
S_0=
\begin{pmatrix}
0&1&1&1\\
1&0&1&1\\
1&1&0&-1\\
1&1&-1&0
\end{pmatrix}.
\]
On the spectrum \(\{\pm1,\pm\sqrt5\}\), the matrix sign function is the cubic polynomial
\[
\operatorname{sgn}(S_0)=\alpha S_0+\beta S_0^3,
\qquad
\beta=\frac{1/\sqrt5-1}4,
\qquad
\alpha=1-\beta.
\]
Thus its positive spectral projection is \((I+\operatorname{sgn}(S_0))/2\). Direct multiplication gives exactly \(P_0\) displayed above. Signed-permutation conjugacy of the Gram matrix is precisely permutation and independent sign changes of the frame vectors; two spanning real frames with the same Gram matrix differ by an orthogonal transformation. This proves the equality classification.

For the displayed explicit frame, put \(d=(5-\sqrt5)/20\). The identities
\[
a+d=\frac12,\qquad ad=c^2,
\]
show directly that its Gram matrix is \(P_0\), and the two second-coordinate contributions sum to one while the mixed terms cancel. Hence it is Parseval and realizes the bound.

## Verification
The accompanying `verify.py` performs two independent finite consistency checks using exact arithmetic. It enumerates all \(64\) Seidel sign matrices, switching each to the normalized three-sign form, and obtains class counts \(8,24,24,8\) according to the number of negative residual signs; the middle \(48\) matrices are exactly those with characteristic polynomial \((x^2-1)(x^2-5)\). It also checks \(P_0^2=P_0\), \(\operatorname{tr}P_0=2\), and \(TC(P_0)=1+\sqrt5\) inside the exact quadratic field \(\mathbb Q(\sqrt5)\). These finite checks replay the algebra; the proof of optimality is the analytic Ky Fan and switching argument above.

## Relationship to prior work
Cahill and Casazza introduced total coherence and showed that equiangular Parseval frames are maximizers when such frames exist. Their paper then asks for non-equiangular solutions and raises structural questions about whether total-coherence maximizers must be equal norm and whether they can contain parallel vectors. The first public version is arXiv:1910.01733 (2019-10-03), and the published article is classified under MSC 42C15.

Nguyen's 2025 dissertation studies the same optimization problems in non-equiangular regimes. For the specific real case of four vectors in dimension two, Proposition 2.16 proves that maximizers are not equal norm by showing the best equal-norm value is \(2\sqrt2\) and exhibiting random non-equal-norm Parseval frames with total coherence exceeding \(3\). The inspected dissertation excerpt does not give the unrestricted exact maximum or classify all maximizers. The theorem here sharpens that case to the exact value \(1+\sqrt5\), classifies all equality cases, and shows that every equality case contains a parallel pair.

## Limitations
The theorem is restricted to real \(4\)-vector Parseval frames in dimension \(2\). No claim is made here about the complex version, higher dimensions, other frame sizes, or a general formula for total-coherence maximizers. The later dissertation was available through indexed text excerpts; direct retrieval of the full PDF was not available during the literature comparison, so an unindexed statement elsewhere in that dissertation remains a residual priority risk. Exact-phrase and semantic searches found no statement of the sharp constant or equality classification.

## References
1. J. Cahill and P. G. Casazza, *Optimal Parseval frames: Total coherence and total volume*, arXiv:1910.01733, first submitted 2019-10-03; later published in *Linear and Multilinear Algebra* 71 (2023), 2067–2092, DOI 10.1080/03081087.2022.2093320.
2. R. Nguyen, *Optimal frames, the Hadamard conjecture, and Williamson matrices of order an odd multiple of 4*, Ph.D. dissertation, University of Missouri, 2025, DOI 10.32469/10355/109492.
