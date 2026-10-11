# Universal endpoint optimality for dynamical sampling on normalized paths

## Finding
Let \(P_{M+1}\) be the unweighted path on \(M+1\) vertices \(0,\ldots,M\), where \(M\ge1\). Write \(D\) for its degree matrix, \(A\) for its adjacency matrix, and \(S=D^{-1/2}AD^{-1/2}\) for the symmetric normalized adjacency. Fix any real function \(\phi\) defined on the \(M+1\) distinct eigenvalues of \(S\), with pairwise distinct values. Put \(T=\phi(S)\), and define the square \((M+1)\)-sample observation matrix at vertex \(j\) by
\[
\mathcal O_j(T)=\begin{bmatrix}e_j^{\mathsf T}\\e_j^{\mathsf T}T\\ \vdots\\ e_j^{\mathsf T}T^M\end{bmatrix}.
\]
Thus \(\mathcal O_j(T)f\) lists successive measurements of an unknown signal \(f\) at \(j\). Let \(d_j\) be the graph degree of \(j\) (\(1\) at endpoints; \(2\) otherwise) and \(g_j=\gcd(j,M)\), with \(\gcd(0,M)=M\). Define \(V_\phi=\prod_{0\le a<b\le M}(\phi(\cos(\pi a/M))-\phi(\cos(\pi b/M)))^2\). Then
\[
\boxed{\det(\mathcal O_j(T)^{\mathsf T}\mathcal O_j(T))=
\begin{cases}
0,&M/g_j\text{ even},\\[3pt]
\dfrac{V_\phi}{4M^{M+1}}\;d_j^{M+1}2^{2(g_j-M)},&M/g_j\text{ odd}.
\end{cases}}
\]
In the zero case \(\operatorname{rank}\mathcal O_j(T)=M+1-g_j\); in the other case the matrix is invertible. At an endpoint the determinant equals \(V_\phi/(4M^{M+1})\). Consequently **both endpoints maximize the information determinant simultaneously for every injective spectral evolution \(\phi\)**. When \(M\ge4\), they are the unique maximizers. When \(M=3\), every vertex is a maximizer. For \(M=1,2\), the endpoints are the only maximizers. For the adjacency evolution \(\phi(s)=s\), the endpoint determinant simplifies to the exact power
\[
\boxed{\det(\mathcal O_0(S)^{\mathsf T}\mathcal O_0(S))=2^{1-M^2}.}
\]
This holds, in particular, for normalized heat evolution \(T=\exp(-\tau(I-S))\) at any \(\tau>0\); its endpoint determinant is obtained by replacing \(\phi\) in \(V_\phi\) by \(s\mapsto\exp(-\tau(1-s))\).

## Assumptions and scope
The path has \(M+1\ge2\) vertices, unit edges and no self-loops. There is one unit-amplitude vertex sensor, \(M+1\) consecutive measurements beginning at time zero, standard Euclidean coordinates, and an evolution obtained as a real spectral function of the symmetric normalized adjacency. Pairwise distinct spectral values of \(T\) are essential: they hold for the identity spectral function and for normalized heat evolution with any positive time parameter. The objective is determinant of the full information Gramian, not the smallest eigenvalue or condition number.

## Proof
**1. Diagonalization.** The eigenvalues of \(S\) are the simple numbers \(\mu_k=\cos(\pi k/M)\), \(0\le k\le M\). An orthonormal eigenbasis is
\[
 v_k(j)=\frac{\sqrt{d_j}\cos(\pi kj/M)}{\sqrt{M}},\quad 1\le k\le M-1;
 \qquad v_0(j)=\frac{\sqrt{d_j}}{\sqrt{2M}},\quad
 v_M(j)=\frac{(-1)^j\sqrt{d_j}}{\sqrt{2M}}.
\]
Indeed, on interior vertices the eigenvalue equation is the cosine addition formula, and at endpoints the degree normalization gives exactly the same eigenvalue. Orthogonality and the constants follow by summing \(d_j\cos(\pi kj/M)\cos(\pi \ell j/M)\) over \(j=0,\ldots,M\): the sum is \(M\) for equal nonendpoint modes, \(2M\) for either endpoint mode, and zero for distinct modes.

**2. Spectral Vandermonde determinant.** Let \(U\) be the orthogonal matrix whose columns are \(v_k\), and set \(\lambda_k=\phi(\mu_k)\). The \((t,k)\) entry of \(\mathcal O_j(T)U\) equals \(\lambda_k^t v_k(j)\), for \(0\le t,k\le M\). Since all \(\lambda_k\) are distinct, the Vandermonde determinant gives
\[
 \det(\mathcal O_j(T)^{\mathsf T}\mathcal O_j(T))
 =V_\phi\prod_{k=0}^M|v_k(j)|^2.
\]
At the endpoint \(j=0\), the eigenvector product is \(1/(4M^{M+1})\). At any other vertex its ratio to the endpoint product is \(d_j^{M+1}\prod_{k=0}^M\cos^2(\pi kj/M)\).

**3. Arithmetic cosine product and exact rank.** Set \(g=\gcd(j,M)\), \(b=M/g\), and \(a=j/g\), so \(\gcd(a,b)=1\). As \(k\) runs from \(0\) through \(M-1\), the residues \(ak\pmod b\) exhaust each residue class exactly \(g\) times, and the extra factor at \(k=M\) has modulus one. Therefore
\[
\prod_{k=0}^M|\cos(\pi kj/M)|
 =\left(\prod_{r=0}^{b-1}|\cos(\pi r/b)|\right)^g.
\]
If \(b\) is even, the factor at \(r=b/2\) vanishes. More precisely, the vanishing eigenvector indices are the \(g\) distinct odd multiples of \(b/2\) between \(0\) and \(M\); each zero removes exactly one Vandermonde column, so the rank is \(M+1-g\). If \(b\) is odd, evaluation of \(\prod_{r=0}^{b-1}|1+e^{2\pi ir/b}|=2\) (by \(z^b-1\) at \(z=-1\)) yields \(\prod_{r=0}^{b-1}|\cos(\pi r/b)|=2^{1-b}\). Hence the product over \(k\) is \(2^{g-M}\). Squaring proves the exact determinant formula.

**4. Universal placement.** Endpoints have multiplicative ratio one. For an interior vertex with nonzero determinant, \(b=M/g\) is an odd integer greater than one, so \(b\ge3\) and \(g\le M/3\). Its determinant ratio to an endpoint is
\[
 2^{M+1+2(g-M)}=2^{1-M+2g}\le2^{1-M/3}.
\]
For \(M\ge4\) this is strictly less than one. For \(M=3\), both interior vertices have \(g=1\) and ratio one. For \(M=2\), the interior vertex has zero determinant. The case \(M=1\) has only endpoints. This proves all optimizer assertions. The \(\phi\)-dependence cancels in every vertex ratio, so the optimality holds simultaneously for every injective spectral function.

**5. The exact adjacency constant.** The Lobatto polynomial \(R(x)=(x^2-1)U_{M-1}(x)\), where \(U_{M-1}(\cos\theta)=\sin(M\theta)/\sin\theta\), has roots \(\mu_0,\ldots,\mu_M\) and leading coefficient \(2^{M-1}\). Direct differentiation gives \(|R'(\mu_0)|=|R'(\mu_M)|=2M\) and \(|R'(\mu_k)|=M\) for \(1\le k\le M-1\). The elementary discriminant product for a monic polynomial gives
\[
\prod_{a<b}(\mu_a-\mu_b)^2
=\frac{(2M)^2M^{M-1}}{(2^{M-1})^{M+1}}
=2^{3-M^2}M^{M+1}.
\]
Combining with the endpoint eigenvector product \(1/(4M^{M+1})\) gives \(2^{1-M^2}\). This derivation also covers \(M=1\) directly, taking \(U_0=1\).

## Verification
The accompanying dependency-free file `verify_path_sampling.py` independently evaluates finite spectral-Vandermonde matrices by Gaussian elimination for the identity, an affine spectral filter, and a heat-type exponential filter on paths of small size, and checks the exact determinant formulas. It also checks the arithmetic optimizer inequality for all path lengths through \(M=49\). These checks are supplemental; the formulas for all sizes and filters follow from the proof, not finite experiments.

## Relationship to prior work
Bulai, Cabrelli, Cordero, Molter, and Saliani (arXiv:2609.25472v1, publicly available September 21, 2026) study graph Paley–Wiener dynamical sampling and report numerical path-graph experiments on time iterates and sensor locations. The present theorem provides an exact finite-path placement and information-determinant classification and extends it to every injective spectral evolution; it does not purport to replace their infinite-lattice sampling theorems. The usual Popov–Belevitch–Hautus eigenvector-visibility criterion and Vandermonde determinant are general background tools. Earlier path-controllability work concerns primarily the combinatorial graph Laplacian, whereas this result treats the **symmetric normalized adjacency** and an exact determinant spectrum. The specific source's complete manuscript was not materially accessible during the comparison, so duplication inside uninspected sections cannot be excluded.

## Limitations
The source paper's full text was inaccessible in the available lawful routes, and the originality judgment has this explicit residual risk. The theorem concerns the determinant (D-optimality), not a best lower frame bound, a minimum condition number, minimum-noise sensor placement under nonuniform noise, arbitrary observation times, or multi-sensor placement. A spectral function collapsing any two eigenvalues invalidates the stated positive determinant formula. The theorem does not assert independent expert audit or formal certification.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, and S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472v1 (September 21, 2026), https://arxiv.org/abs/2609.25472.
2. S.-P. Hsu and P.-Y. Yang, *Generalizing Laplacian Controllability of Paths*, arXiv:1902.05671 (2019), https://arxiv.org/abs/1902.05671. Distinct operator and qualitative observability context.
3. Classical Chebyshev second-kind identity, Vandermonde determinant, and finite-dimensional spectral theorem (used with complete derivations above).
