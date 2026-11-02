# A complete negative-type classification for higher powers of finite cycles

## Finding

Let \(C_n^k\) be the \(k\)-th graph power of the \(n\)-cycle, for integers \(k\ge3\) and \(n\ge 2k+1\). Its vertices form \(\mathbb Z/n\mathbb Z\), and distinct vertices are adjacent when their original circular separation is at most \(k\). Let \(d_{n,k}\) be the new shortest-path metric. **The following conditions are equivalent:**

1. \(d_{n,k}\) has conditional negative type, meaning \(\sum_{u,v}c_uc_vd_{n,k}(u,v)\le0\) whenever real coefficients satisfy \(\sum_uc_u=0\).
2. \(\exp(-t d_{n,k}(u,v))\), indexed by all vertices, is positive semidefinite for every \(t>0\).
3. Either \(n=2k+1\), \(n=2k+2\), or
   \[
   (k,n)\in\{(3,12),(3,14),(3,20),(4,18)\}.
   \]

In each admitted case the exponential kernel is **strictly** positive definite at every fixed \(t>0\). For every excluded case it is indefinite at every sufficiently small positive \(t\).

The minimum real Euclidean dimension required for representing \(d_{n,k}\) **as a squared Euclidean distance** is \(2k\) when \(n=2k+1\), and \(k+1\) when \(n=2k+2\). In the four sporadic cases, respectively, the dimensions are \(6,7,8,7\). These ranks follow from exact centered-distance nullities \(5,6,11,10\), respectively.

## Assumptions and scope

All integers \(k\ge3\), \(n\ge2k+1\), and all real \(t>0\) are quantified. For vertices represented by integers from \(0\) through \(n-1\), write
\[
 \delta_n(u,v)=\min(|u-v|,n-|u-v|),\qquad
 d_{n,k}(u,v)=\left\lceil\frac{\delta_n(u,v)}{k}\right\rceil.
\]
The second identity follows by taking successive steps along a shortest circular arc, each covering at most \(k\) original edges. Conversely, each graph-power step covers at most \(k\) original edges, giving the opposite bound. The powers with \(n=2k+1\) are complete; those with \(n=2k+2\) are complete graphs with a perfect matching deleted. This result concerns the **ordinary, unpowered** shortest-path distance of each graph power, not the adjacency spectrum of that graph and not the complete range of Schoenberg powers \(d_{n,k}^{p}\) for arbitrary \(p\).

## Proof

**1. Cyclic Fourier criterion.** Put \(m=\lfloor n/2\rfloor\), \(h=\lceil m/k\rceil\), and \(\theta_j=\pi j/n\). The distance matrix is real symmetric and circulant. For every nontrivial Fourier frequency \(j=1,\ldots,n-1\), its distance eigenvalue is
\[
 \lambda_j=-\frac{1}{\sin\theta_j}
 \sum_{r=0}^{h-1}\sin((2rk+1)\theta_j).
 \tag{1}
\]
Indeed, the identity \(d_{n,k}(a,0)=\sum_{r=0}^{h-1}\mathbf 1_{\{\delta_n(a,0)>rk\}}\) expresses distance as a sum of complements of centered circular intervals. Every radius \(rk\) in this sum is strictly below \(m\). The nonconstant Fourier transform of each interval complement is minus its Dirichlet kernel, giving (1). The finite arithmetic-progression identity then yields
\[
 \lambda_j=-\frac{\sin(hk\theta_j)\,
 \sin(((h-1)k+1)\theta_j)}
 {\sin(k\theta_j)\sin\theta_j},
 \tag{2}
\]
with continuous interpretation where a denominator vanishes. When \(\sin(k\theta_j)=0\), formula (1) gives \(\lambda_j=-h\). Because Fourier characters diagonalize the matrix and the constant character is excluded by \(\sum_uc_u=0\), conditional negative type is equivalent to \(\lambda_j\le0\) for every nonzero \(j\).

**2. The complete and near-complete orders.** If \(n=2k+1\), every off-diagonal distance is one and all nonconstant eigenvalues equal \(-1\). If \(n=2k+2\), the distance matrix is \(J-I+P\), where \(P\) swaps antipodal pairs and \(J\) is the all-ones matrix. On the mean-zero subspace it is \(-I+P\), hence negative semidefinite. Its kernel on that subspace has dimension \(k\), leaving squared-Euclidean embedding dimension \(n-1-k=k+1\).

**3. Uniform short-diameter obstructions for \(k\ge4\).** For \(2k+3\le n\le4k+1\), one has \(h=2\), and (1) simplifies to
\[
 \lambda_j=-\frac{2\sin((k+1)\theta_j)\cos(k\theta_j)}{\sin\theta_j}.
 \tag{3}
\]
When \(n<4k\), the frequency \(j=2\) has \(\sin(2\pi(k+1)/n)>0\) and \(\cos(2\pi k/n)<0\); hence \(\lambda_2>0\). For \(n=4k\) or \(4k+1\), frequency \(j=3\) has \(\sin(3\pi(k+1)/n)>0\) and \(\cos(3\pi k/n)<0\), provided \(k\ge4\); thus \(\lambda_3>0\).

For \(n=4k+2\), \(h=3\), and the second numerator factor in (2) at \(j=3\) equals \(\sin(3\pi/2)=-1\). The first factor equals \(\sin(9k\pi/(4k+2))>0\) for \(k\ge5\), while both denominator factors are positive. Thus \(\lambda_3>0\) for \(k\ge5\). At \(n=4k+3\), take \(j=2\): the two numerator factors are negative and positive, respectively, and the denominator factors are positive, yielding \(\lambda_2>0\) for every \(k\ge4\).

**4. A local certificate for every larger order.** For \(k=4\), choose the six residues
\[
 (0,2,k-1,k+1,2k,2k+2),
\]
whereas for \(k\ge5\), choose
\[
 (0,2,k-2,k+1,2k-1,2k+2).
\]
When \(n\ge4k+4\), their circular distances equal their straight differences. In either case, the induced six-point distance matrix is
\[
 T=\begin{pmatrix}
 0&1&1&2&2&3\\1&0&1&1&2&2\\1&1&0&1&2&2\\
 2&1&1&0&1&2\\2&2&2&1&0&1\\3&2&2&2&1&0
 \end{pmatrix}.
\]
For \(w=(2,-2,-2,3,-3,2)^{\mathsf T}\), one has \(\sum w_i=0\) but **\(w^{\mathsf T}Tw=2>0\)**. Therefore none of these metrics has conditional negative type. Combined with paragraph 3, this excludes every nonlisted \(k\ge4\) order apart from the single boundary \((k,n)=(4,18)\).

**5. The cubic power.** For \(k=3\), (3) at \(j=2\) gives a positive eigenvalue for \(n=9,10,11\), and at \(j=3\) gives one for \(n=13\). Formula (2) supplies the following further strictly positive modes:

| Orders \(n\) | Mode \(j\) |
| --- | --- |
| \(15,16,17\) | \(2\) |
| \(18,19\) | \(5\) |
| \(21\) | \(2\) |

For example, when \(n=18,19\) at \(j=5\), \(\sin(45\pi/n)>0\), \(\sin(35\pi/n)<0\), and both denominator factors in (2) are positive. The other table entries follow by substituting the stated small integers and checking which multiple-of-\(\pi\) interval contains each argument.

For every \(n\ge22\), use twelve consecutive vertices \(0,1,\ldots,11\) with zero-sum weights
\[
 (2,-1,-2,1,2,-2,-2,2,1,-2,-1,2).
\]
All their circular separations are at most \(11\le n/2\), so their distances are \(\lceil |u-v|/3\rceil\). Their weighted distance quadratic form is exactly \(2>0\), excluding all these orders.

**6. The four exceptional noncomplete orders.** In the following table, the sets list Fourier frequencies \(1\le j\le\lfloor n/2\rfloor\) at which \(\lambda_j=0\). At every other displayed positive frequency, \(\lambda_j<0\). This is an exact sign calculation from (1)–(2), by reducing integer multiples of \(\pi/n\) modulo \(2\pi\); it is independently replayed by the included checker. The frequencies \(n-j\) have the same eigenvalue as \(j\).

| \((k,n)\) | Zero frequencies in first half | Mean-zero nullity | Squared-Euclidean dimension |
| --- | --- | ---: | ---: |
| \((3,12)\) | \(2,3,6\) | \(5\) | \(6\) |
| \((3,14)\) | \(2,4,6\) | \(6\) | \(7\) |
| \((3,20)\) | \(2,4,5,6,8,10\) | \(11\) | \(8\) |
| \((4,18)\) | \(2,3,4,6,8\) | \(10\) | \(7\) |

The cases \(n=2k+1,2k+2\), this exact table, and the preceding positive-eigenvalue or finite-submetric certificates exhaust all admissible and inadmissible parameters.

**7. Kernels and embedding dimensions.** The finite-group version of Schoenberg's negative-type criterion identifies conditional negative type of \(d_{n,k}\) with positive semidefiniteness of \(e^{-td_{n,k}}\) for every \(t>0\). A conditionally negative definite distance with distinct points admits an injective representation \(d_{n,k}(u,v)=\|y_u-y_v\|^2\); the Gaussian kernel on any finite collection of distinct Euclidean points is strictly positive definite. Conversely, whenever \(w\) is zero-sum and \(w^{\mathsf T}Dw>0\), one has \(w^{\mathsf T}(e^{-tD})w=-t\,w^{\mathsf T}Dw+O(t^2)<0\) for all sufficiently small positive \(t\). The minimum squared-Euclidean embedding dimension equals the rank of \(-\tfrac12 HDH\), with \(H=I-J/n\), which is \(n-1\) minus the mean-zero nullity read from the Fourier spectrum.

## Verification

Run \(\texttt{python3 verify_cycle_power.py}\) from the directory containing this document and the included script. The checker uses integer arithmetic to determine exact signs of rational-angle sines; it confirms the exceptional spectral zero sets and bounded-diameter sign witnesses, verifies the six- and twelve-point quadratic forms using integers, independently reconstructs shortest paths by breadth-first search, and cross-checks finite Fourier transforms numerically. A successful replay emits \(\texttt{CHECK_OK}\). Its bounded loops serve as reproducibility checks, not as substitutes for the universal arguments in the proof.

## Relationship to prior work

Lin, Rautenbach, Soulignac and Szwarcfiter (online April 21, 2010) characterize **which graphs are powers of cycles and paths**, not which of their shortest-path metrics have negative type. Sander and Sander (arXiv December 14, 2011; a preprint of a 2010 article) compute **adjacency** eigenvalues of the graph powers, not the distance-matrix eigenvalues here. Sánchez (arXiv August 2, 2011) gives a general finite-distance-matrix criterion and evaluates complete bipartite graphs, without a classification of higher cycle powers. Aouchiche and Hansen (available June 26, 2014) survey graph distance spectra, but the inspected treatment does not furnish this parameter classification. A separate earlier analysis of \(C_n^2\) treats the square alone; that case is deliberately outside the domain \(k\ge3\) of the present result.

The general Fourier diagonalization and Dirichlet identity are classical. The contribution assessed here is their combination with **uniform local counterexamples and a complete arithmetic list of the surviving orders**. We do not claim that numerical searches establish novelty or that all obscure sources have been exhausted.

## Limitations

The theorem gives a complete yes/no classification at exponent one and the associated endpoint embedding ranks. It does **not** determine the optimal subunit negative-type exponent for the excluded graphs, nor every scale \(t\) at which their exponential kernels can become positive semidefinite. Finite reproductions support, but do not independently certify, the infinite-parameter proof. A specialized historical distance-spectral treatment not recovered in the bounded literature search could contain an equivalent statement. Independent mathematical validation remains outstanding.

## References

1. M. C. Lin, D. Rautenbach, F. J. Soulignac and J. L. Szwarcfiter, *Powers of cycles, powers of paths, and distance graphs*, Discrete Applied Mathematics **159** (2011), 621–627, DOI 10.1016/j.dam.2010.03.012. Public online date: April 21, 2010. Full text: https://bibliotecadigital.exactas.uba.ar/download/paper/paper_0166218X_v159_n7_p621_Lin.pdf.
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, first submitted August 2, 2011. https://arxiv.org/abs/1108.0451.
3. J. W. Sander and T. Sander, *On the eigenvalues of distance powers of circuits*, Linear Algebra and its Applications **432** (2010), 3132–3140; arXiv:1112.3202 first posted December 14, 2011. https://arxiv.org/abs/1112.3202.
4. M. Aouchiche and P. Hansen, *Distance spectra of graphs: A survey*, Linear Algebra and its Applications **458** (2014), 301–386, online June 26, 2014. https://www.math.ucdavis.edu/~saito/data/distmat/aouchiche-hansen_dist-spec-graphs-survey.pdf.
5. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society **44** (1938), 522–536 (classical negative-type criterion).
