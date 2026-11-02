# Exact quadratic embedding constants and maximizing Fourier modes of Möbius ladders

## Finding
For each integer \(n\geq3\), let \(M_{2n}\) be the unit-edge Möbius ladder with vertex set \(\mathbb Z/(2n)\), cycle edges \(\{k,k+1\}\), and opposite-vertex edges \(\{k,k+n\}\). Write \(D_n=(d_{M_{2n}}(u,v))_{u,v}\) for its shortest-path distance matrix. The quadratic embedding constant is
\[
\operatorname{QEC}(M_{2n})=\max\{z^{\mathsf T}D_nz:\ z\in\mathbb R^{2n},\ \|z\|_2=1,\ \mathbf1^{\mathsf T}z=0\}.
\]
It has the exact parity-dependent value
\[
\boxed{\operatorname{QEC}(M_{2n})=\begin{cases}
\csc\bigl(3\pi/(2n)\bigr),&n\text{ odd},\\
\cot\bigl(3\pi/(2n)\bigr),&n\text{ even}.
\end{cases}}
\]
The maximum is attained precisely on the real Fourier-frequency-three subspace: when \(n\ge4\) it is the two-dimensional span of \(k\mapsto\cos(3\pi k/n)\) and \(k\mapsto\sin(3\pi k/n)\), and for \(n=3\) it is the one-dimensional alternating subspace. Consequently every \(M_{2n}\) has a strictly positive quadratic embedding constant and therefore its graph distance is **not** a squared Euclidean distance. As \(n\to\infty\),
\[
\operatorname{QEC}(M_{2n})=\begin{cases}
2n/(3\pi)+\pi/(4n)+O(n^{-3}),&n\text{ odd},\\
2n/(3\pi)-\pi/(2n)+O(n^{-3}),&n\text{ even}.
\end{cases}
\]
The six-vertex case \(M_6=K_{3,3}\), with constant \(1\), is a known special case of the complete-bipartite formula and is not a priority claim by itself.

## Assumptions and scope
The result concerns **finite, simple, unweighted** Möbius ladders with \(n\ge3\), ordinary shortest-path distance, the **real** zero-sum quadratic form, and the normalization \(\|z\|_2=1\). We use \(M_{2n}\) to denote the graph with exactly \(2n\) vertices; some literature calls it \(M_n\). No assertion is made for effective resistance, normalized graph distance, weighted ladders, or powered distances. Throughout, \(\Delta^2f(k)=f(k+1)-2f(k)+f(k-1)\) is the circular second difference, with indices modulo \(2n\).

## Proof
**1. Exact graph distances.** For \(0\le k\le n\), any path from \(0\) to \(k\) using no opposite-vertex edge has length at least \(k\), with equality on the cycle. Using an odd number of opposite-vertex edges has length at least \(1+n-k\), attained by one opposite edge followed by the shorter cycle arc. An even number of opposite edges can be removed in pairs without increasing length: in the Cayley-graph representation each opposite jump adds \(n\) modulo \(2n\), so an even number cancels and each remaining cycle step contributes at most one unit of cyclic displacement. Thus
\[
 f(k):=d_{M_{2n}}(0,k)=\min\{k,n+1-k\}\quad (0\le k\le n),\qquad f(2n-k)=f(k).
\]
In particular \(D_n\) is a real symmetric circulant matrix. Its Fourier eigenvectors are \(\exp(\pi\mathrm{i}jk/n)\), with eigenvalues
\[
 \lambda_j=\sum_{k=0}^{2n-1} f(k)\exp(-\pi\mathrm{i}jk/n),\qquad j=0,1,\ldots,2n-1.
\]
The constant vector is the \(j=0\) mode, so the constrained quadratic maximum is exactly \(\max_{1\le j<2n}\lambda_j\).

**2. Locate the corners of the distance profile.** Put \(\theta=\pi j/n\) and \(\phi=\theta/2=\pi j/(2n)\). For \(1\le j\le n\), \(\sin\phi>0\). The Fourier multiplier of the second difference is \(-4\sin^2\phi\).

If \(n=2m+1\) is odd, direct differences of the exact profile give two positive point masses of magnitude \(2\), at \(0,n\), and two negative point masses of magnitude \(2\), at \(m+1,2n-m-1\). Therefore
\[
 \lambda_j=\frac{\cos((m+1)\theta)-(1+(-1)^j)/2}{\sin^2\phi}.
\]
If \(n=2m\) is even, the positive point masses remain at \(0,n\), and four negative point masses, each of magnitude \(1\), occur at \(m,m+1,3m-1,3m\). Consequently
\[
 \lambda_j=\frac{\cos((m+1/2)\theta)\cos\phi-(1+(-1)^j)/2}{\sin^2\phi}.
\]
Both identities follow by taking the discrete Fourier transform of \(\Delta^2 f\), with no division by zero because \(j\ne0\).

**3. Compare every nonconstant Fourier frequency.** Since \((m+1)\theta=\pi j/2+\phi\) for odd \(n\), and \((m+1/2)\theta=\pi j/2+\phi\) for even \(n\), the formulas simplify for odd \(j\) to
\[
 \lambda_j=(-1)^{(j+1)/2}\begin{cases}\csc\phi,&n\text{ odd},\\\cot\phi,&n\text{ even}.
 \end{cases}
\]
For even \(j\), they become
\[
 \lambda_j=\begin{cases}
 \bigl((-1)^{j/2}\cos\phi-1\bigr)/\sin^2\phi,&n\text{ odd},\\
 \bigl((-1)^{j/2}\cos^2\phi-1\bigr)/\sin^2\phi,&n\text{ even},
 \end{cases}
\]
which are nonpositive. For odd \(j\le n\), both \(\csc\phi\) and \(\cot\phi\) are positive (allowing \(\cot(\pi/2)=0\)) and decreasing in \(j\). Positive eigenvalues therefore arise precisely at the admissible indices \(j\equiv3\pmod4\); their largest occurs at the smallest such index, \(j=3\). The reflection identity \(\lambda_{2n-j}=\lambda_j\) handles the remaining indices, and strict decrease determines the stated maximal eigenspaces. This proves the closed formula and all equality directions.

**4. Hilbert obstruction and parity asymptotics.** Schoenberg's finite-metric criterion identifies squared-Hilbert embeddability with conditional negative definiteness of the distance matrix, equivalently \(\operatorname{QEC}\le0\). Here \(\lambda_3>0\) for every \(n\ge3\), ruling out such an embedding. Taylor series at zero, \(\csc x=x^{-1}+x/6+O(x^3)\) and \(\cot x=x^{-1}-x/3+O(x^3)\), with \(x=3\pi/(2n)\), give both displayed asymptotic expansions.

## Verification
The standalone standard-library Python script `verify.py` builds the graph independently, computes every shortest-path distance by breadth-first search, compares the resulting distance matrix with the explicit profile, and evaluates all nonconstant discrete Fourier eigenvalues against the piecewise formulas for \(3\le n\le60\). It separately verifies maximal-frequency multiplicities, Rayleigh witnesses for \(3\le n\le24\), and sampled asymptotic coefficients. A replay passed **298,986 finite assertions**. Those finite computations are independent implementations of the formulas but are **not** a proof for all \(n\); the all-size proof is the Fourier/corner argument above.

## Relationship to prior work
Obata and Zakiyyah (2018) introduced the quadratic embedding constant and established its identification with the second-largest distance eigenvalue for graph distance matrices with constant row sums, which is used here. Choudhury and Nandi (2023) investigated QEC and distance spectra, including bounds for trees and formulas for cluster graphs. Azimi and Farrokhi (2023) explicitly studied Möbius ladders, but the matrices calculated there use **effective resistance distance**, rather than unweighted geodesic distance. Indulal and Gutman (2008) established distance spectra for graph products including double graphs, coronas, Cartesian products and lexicographic products; those constructions do not directly give the present Möbius-ladder geodesic spectrum. Aalipour et al. (2015) studied other graph families including Doob and double-odd graphs; Młotkowski, Skrzypczyk and Wojtylak (2024) studied complete bipartite graphs with deleted edges and theta graphs. No inspected primary result directly states this Möbius-ladder parity formula with its sharp maximizing frequency and asymptotics.

## Limitations
The formula is asserted only for shortest-path metric on the precisely defined family, not for electrical-resistance distances or the spectrum of the adjacency/Laplacian operator. The known \(M_6=K_{3,3}\) specialization is not new. General Fourier diagonalization of circulant matrices and the constant-row-sum reduction are prior methods, not novelty claims. A search cannot establish historical uniqueness, so an unlocated earlier geodesic distance-spectrum treatment of Möbius ladders remains a genuine priority risk. Independent mathematical validation has not been performed.

## References
1. N. Obata and A. Y. Zakiyyah, *Distance matrices and quadratic embedding of graphs*, Electronic Journal of Graph Theory and Applications 6 (2018), 37–60. DOI: 10.5614/ejgta.2018.6.1.4. https://www.ejgta.org/index.php/ejgta/article/download/435/pdf_64
2. P. N. Choudhury and R. Nandi, *Quadratic embedding constants of graphs: Bounds and distance spectra*, arXiv:2306.15589, first posted 2023-06-27. https://arxiv.org/pdf/2306.15589
3. A. Azimi and M. Farrokhi D. G., *Explicit formulas for matrices associated to ladder, circular ladder, and Mobius ladder graphs*, arXiv:2306.10497, first posted 2023-06-18. https://arxiv.org/pdf/2306.10497
4. G. Indulal and I. Gutman, *On the distance spectra of some graphs*, Mathematical Communications 13 (2008), 123–131. https://hrcak.srce.hr/en/clanak/37132
5. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196, first posted 2015-09-03. https://arxiv.org/pdf/1509.01196
6. W. Młotkowski, M. Skrzypczyk and M. Wojtylak, *On quadratic embeddability of bipartite graphs and theta graphs*, arXiv:2409.17662, first posted 2024-09-26. https://arxiv.org/pdf/2409.17662
