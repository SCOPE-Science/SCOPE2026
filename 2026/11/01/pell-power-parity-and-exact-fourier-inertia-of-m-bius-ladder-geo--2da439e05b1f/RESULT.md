# Pell–power parity and exact Fourier inertia of Möbius-ladder geodesic matrices

## Finding

For every integer \(n\ge3\), let \(M_{2n}\) be the Möbius ladder with vertex set \(\mathbb Z/(2n)\mathbb Z\) and undirected edges with increments \(\pm1\) and \(n\). Let \(D_n=(d(i,j))\) be its ordinary **shortest-path** distance matrix, not its electrical-resistance matrix. Its Fourier eigenvalues are completely explicit, the matrix is nonsingular for every \(n\), and its determinant obeys an unexpected parity dichotomy.

Put \(x_k=\pi k/(2n)\) and \(R_n=\lfloor(n^2+2n-1)/2\rfloor\). For \(1\le k\le2n-1\), the eigenvalue corresponding to the character \(j\mapsto\exp(\pi i k j/n)\) is
\[
\lambda_k=\begin{cases}
(-1)^{(k+1)/2}\cot x_k,&n\ \text{even},\ k\ \text{odd},\\
-1,&n\ \text{even},\ k\ \text{even},\ k/2\ \text{even},\\
-1-2\cot^2x_k,&n\ \text{even},\ k\ \text{even},\ k/2\ \text{odd},\\
(-1)^{(k+1)/2}\csc x_k,&n\ \text{odd},\ k\ \text{odd},\\
-\bigl(1+(-1)^{k/2}\cos x_k\bigr)^{-1},&n\ \text{odd},\ k\ \text{even}.
\end{cases}
\]
The constant-character eigenvalue is \(\lambda_0=R_n>0\). The eigenvalues are counted with their Fourier frequencies, so equal numerical values at distinct frequencies retain their full multiplicities.

Let \(P_1=1\), \(P_2=3\), and \(P_{m}=2P_{m-1}+P_{m-2}\) for \(m\ge3\). Then
\[
\boxed{\det D_n=\begin{cases}
(-1)^{(n+1)/2}R_n\,2^{2n-2},&n\ \text{odd},\\
-R_n\,P_{n/2}^{\,2},&n\ \text{even}.
\end{cases}}
\]
Equivalently, \(P_m=((1+\sqrt2)^m+(1-\sqrt2)^m)/2\), a positive integer.

With inertia ordered as (positive, zero, negative),
\[
\boxed{\operatorname{In}(D_n)=
\begin{cases}
((n+1)/2,\,0,\,(3n-1)/2),&n\ \text{odd},\\
(1+2\lfloor n/4\rfloor,\,0,\,2n-1-2\lfloor n/4\rfloor),&n\ \text{even}.
\end{cases}}
\]
In particular, the Fourier restriction of \(D_n\) to the coefficient-zero subspace always has a strictly positive eigenvalue. Thus \(d\) is **not of 1-negative type** on any Möbius ladder, and \(\exp(-t d(i,j))\) is not positive semidefinite for every \(t>0\). By contrast, the ordinary circular ladder \(C_n\square K_2\) has a conditionally negative-semidefinite graph-distance matrix at exponent one. The obstruction introduced by the Möbius twist therefore occurs in a linearly growing number of Fourier dimensions.

## Assumptions and scope

All graph edges have unit length; the distance is ordinary geodesic (minimum edge count), and \(n\) is an integer at least three. We use the unnormalized discrete Fourier transform, so \(\lambda_0\) is the row sum of \(D_n\). In the determinant formula, \(P_m\) is the half-Pell–Lucas sequence defined above, not a graph parameter. The claim is an exact statement for every finite order, not a large-order asymptotic.

For the negative-type conclusion, a real symmetric zero-diagonal matrix \(D\) is conditionally negative semidefinite if \(\sum_{i,j}c_i c_j D_{ij}\le0\) for all real vectors \(c\) with \(\sum c_i=0\). The standard finite Schoenberg equivalence says this is equivalent to positive semidefiniteness of \(\exp(-tD_{ij})\) for every \(t>0\).

## Proof

**1. Shortest paths and distance shells.** Each word in the generators \(\{\pm1,n\}\) can be shortened to one using either zero or one \(n\)-step, since two such steps cancel. Thus, for \(0\le j<2n\),
\[
d(0,j)=\min\bigl\{\min(j,2n-j),\ 1+|n-j|\bigr\}.
\]
The maximum distance is \(L=\lfloor(n+1)/2\rfloor\). For each integer \(2\le t\le L\), the exact level set \(S_t=\{j:d(0,j)\ge t\}\) is the disjoint union
\[
\{t,t+1,\ldots,n-t+1\}\ \cup\ \{n+t-1,\ldots,2n-t\}.
\]
The first level is \(S_1=\{1,\ldots,2n-1\}\). Consequently, \(d(0,j)=\sum_{t=1}^L\mathbf1_{S_t}(j)\). Counting the shells gives \(R_n=\lfloor(n^2+2n-1)/2\rfloor\).

**2. Fourier diagonalization.** Set \(z=\exp(-\pi i k/n)\) and \(\theta=\pi k/n\), with \(1\le k<2n\). Since \(D_n\) is circulant, its character eigenvalue equals \(\sum_j d(0,j)z^j\). The first level contributes \(-1\). Summing the two geometric progressions in each remaining shell gives
\[
\sum_{j\in S_t}z^j=z^{t-1}(z+(-1)^k)\sum_{a=0}^{n-2t+1}z^a.
\]
For odd \(k\) this equals \(-2\cos((t-1)\theta)\); for even \(k\) it equals \(-2\cot(\theta/2)\sin((t-1)\theta)\). Therefore
\[
\lambda_k=\begin{cases}
-1-2\sum_{a=1}^{L-1}\cos(a\theta),&k\text{ odd},\\
-1-2\cot(\theta/2)\sum_{a=1}^{L-1}\sin(a\theta),&k\text{ even}.
\end{cases}
\]
Apply the exact identities
\[
1+2\sum_{a=1}^{L-1}\cos(a\theta)=\frac{\sin((L-1/2)\theta)}{\sin(\theta/2)},\quad
2\sum_{a=1}^{L-1}\sin(a\theta)=\frac{\cos(\theta/2)-\cos((L-1/2)\theta)}{\sin(\theta/2)}.
\]
If \(n\) is odd, then \(L-1/2=n/2\); if \(n\) is even, \(L-1/2=(n-1)/2\). Substituting \(\sin(\pi k/2)\) and \(\cos(\pi k/2)\) gives precisely the five cases stated in the finding. Their denominators cannot vanish at an admissible frequency.

**3. Exact inertia.** Every nonzero even-frequency eigenvalue is negative. When \(n\) is odd, the odd-frequency eigenvalues are positive exactly for \(k\equiv3\pmod4\), giving \((n-1)/2\) positive nonconstant frequencies. When \(n\) is even, the conjugate pairs \(k\) and \(2n-k\) are positive exactly when the representative \(1\le k<n\) obeys \(k\equiv3\pmod4\), giving \(2\lfloor n/4\rfloor\) positive nonconstant frequencies. Add the positive constant eigenvalue. None of the eigenvalues vanishes.

**4. The odd determinant.** Suppose \(n\) is odd. The odd-frequency eigenvalues have product
\[
(-1)^{(n+1)/2}\Biggl(\prod_{j=1}^{n}\sin\frac{(2j-1)\pi}{2n}\Biggr)^{-1}
=(-1)^{(n+1)/2}2^{n-1}.
\]
Here the standard odd-sine product is \(2^{1-n}\). The even-frequency eigenvalue factors, indexed by \(k=2h\), have denominators \(1+(-1)^h\cos(\pi h/n)\). Because \(n\) is odd, the substitution \(h\mapsto n-h\) and the odd-sine product give
\[
\prod_{h=1}^{n-1}\bigl(1+(-1)^h\cos(\pi h/n)\bigr)=2^{1-n}.
\]
More explicitly, when \(n\) is odd the factors with odd \(h\) are \(2\sin^2(\pi h/(2n))\), while those with even \(h\) are \(2\sin^2(\pi(n-h)/(2n))\). The first-half odd-sine product is \(2^{-(n-1)/2}\), giving the displayed denominator product \(2^{1-n}\). There are an even number of even-frequency negative eigenvalues, so their product is \(2^{n-1}\). Multiplication by \(R_n\) proves the odd determinant formula.

**5. The even determinant and Pell factor.** Suppose \(n=2m\) is even. Pairing conjugate odd frequencies shows that their complete product equals one: in the half-range \(1\le k<n\), the odd-index cotangents pair by \(k\leftrightarrow n-k\), with reciprocal positive factors, including the possible unit central factor. For even frequencies the central factor is \(-1\) and the remaining conjugate pairs give
\[
\prod_{k\text{ even},\ k\ne0}\lambda_k=-A_m^2,
\qquad
A_m=\prod_{\substack{1\le h<m\\h\text{ odd}}}\left(1+2\cot^2\frac{\pi h}{2m}\right).
\]
Since \(1+2\cot^2x=(3+\cos2x)/(1-\cos2x)\), extending the product by reflection gives
\[
A_m^2=\prod_{\substack{1\le h<2m\\h\text{ odd}}}\frac{3+\cos(\pi h/m)}{1-\cos(\pi h/m)}
=\frac{T_m(3)+(-1)^m}{2},
\]
where \(T_m\) is the degree-\(m\) Chebyshev polynomial and the last identity follows from the roots of \(T_m(x)+1\), namely \(\cos((2j-1)\pi/m)\), counted with multiplicities. Writing \(r=1+\sqrt2\), \(s=1-\sqrt2\), we have \(r^{2m}+s^{2m}=2T_m(3)\) and \((rs)^m=(-1)^m\). Hence \(A_m^2=((r^m+s^m)/2)^2=P_m^2\). Both \(A_m\) and \(P_m\) are positive, so \(A_m=P_m\), proving the even determinant formula.

**6. The Gaussian and untwisted-ladder contrast.** Every positive nonconstant Fourier eigenvalue gives a real zero-sum Fourier sine or cosine eigenvector \(c\) with \(c^TD_nc>0\). Thus the matrix is not conditionally negative semidefinite. For small enough \(t>0\), the same vector gives \(c^T(\exp(-td(i,j)))c=-t\,c^TD_nc+O(t^2)<0\), proving failure of universal Gaussian positivity.

By contrast, on a cycle \(C_n\), let \(A_j\) range over the \(n\) cyclic arcs of length \(\lfloor n/2\rfloor\). Exactly \(2d_{C_n}(u,v)\) arcs separate vertices \(u,v\), so
\[
d_{C_n}(u,v)=\frac12\sum_j\lvert\mathbf1_{A_j}(u)-\mathbf1_{A_j}(v)\rvert.
\]
Each cut semimetric is conditionally negative semidefinite because for zero-sum real coefficients \(c\), its quadratic form equals \(-2(\sum_{u\in A_j}c_u)^2\). The metric on \(C_n\square K_2\) is the sum of this cycle distance and a two-point cut distance, hence remains conditionally negative semidefinite. This proves the claimed twist-versus-product distinction.

## Verification

The standalone program `check_mobius.py` constructs graph distances independently by breadth-first search, compares every Fourier eigenvalue against the closed formulas for \(3\le n\le71\), checks nonzero inertia and row sums, computes exact integer determinants for \(3\le n\le16\), and checks the Pell product for \(2\le m\le79\). It completed 437 assertion groups without a discrepancy. In particular, the first determinant values at \(n=3,4,5,6\) are \(112,-99,-4352,-1127\), agreeing with the formulas. All finite tests are checks, not substitutes for the proof for arbitrary \(n\).

## Relationship to prior work

The motivation is the classical use of graph-distance spectra and the Schoenberg finite negative-type criterion. Ilić (2011) determines distance spectra for **integral circulant graphs** using gcd-based generator structures; that class does not encompass the general opposite-chord Möbius family. Aalipour and coauthors (2015) determine distance-matrix determinants and inertias for other graph families, including lollipop and barbell graphs; their results do not give this full Möbius-ladder formula. Azimi and Farrokhi (2023) explicitly study Möbius ladders, but their matrices encode **electrical resistance** and Laplacian pseudoinverses, not the ordinary shortest-path distance matrix in this claim. Classical cyclic Fourier diagonalization is an established input, not itself a novelty claim. The assessed contribution is the explicit five-case geodesic spectrum, the opposite-parity determinant factors, the complete inertia, and the Gaussian obstruction contrast.

## Limitations

The proof concerns unweighted ordinary graph distance on the specified Möbius ladders only. It **does not** calculate the sharp exponent below one for which \(d^p\) becomes conditionally negative semidefinite, nor the bandwidth set for a fixed exponent outside the universal condition. It does not address electrical-resistance distance. Finite computational checks do not establish literature originality, and an earlier equivalent result under a different graph naming convention remains possible. The work has not undergone independent external mathematical audit.

## References

- A. Ilić, *Distance spectra and Distance energy of Integral Circulant Graphs*, arXiv:1104.1097, first posted 2011-04-06. https://arxiv.org/abs/1104.1097
- G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196, first posted 2015-09-03. https://arxiv.org/abs/1509.01196
- A. Azimi and M. Farrokhi D. G., *Explicit formulas for matrices associated to ladder, circular ladder, and Möbius ladder graphs*, arXiv:2306.10497, first posted 2023-06-18. https://arxiv.org/html/2306.10497v1
- I. J. Schoenberg, *Metric spaces and positive definite functions*, Trans. Amer. Math. Soc. **44** (1938), 522–536; finite-space conditional-negative-type criterion.
