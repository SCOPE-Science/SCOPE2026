# A sharp spectral-gap allocation crossover for a single-edge-deficient biclique

## Finding
For an integer \(n\ge3\), remove one edge \(e\) from the complete bipartite graph \(K_{n,n}\). Assign nonnegative, symmetric conductances to every remaining edge, with total \(B>0\). Let \(\lambda_2(L)\) denote the second-smallest eigenvalue of its weighted combinatorial Laplacian. Then
\[
\max_{\substack{w\ge0\\\sum_e w_e=B}}\lambda_2(L(w))=\frac{B}{D_n},\qquad
D_n=\begin{cases}
(n+8)/2,&3\le n\le7,\\
n-1+(n-\sqrt{n^2-8n+8})/4,&n\ge8.
\end{cases}
\]
An optimal allocation has precisely two weights: \(aB/D_n\) on the \((n-1)^2\) edges joining ordinary vertices and \(bB/D_n\) on the \(2(n-1)\) edges incident to either endpoint of the deleted edge. Set \(m=n-1\). For \(3\le n\le7\), take
\[
a=\frac{m+3}{2m^2},\quad b=\frac3{2m}.
\]
For \(n\ge8\), take
\[
b=\frac{m+1-\sqrt{m^2-6m+1}}{4m},\quad a=\frac{1-b}{m}.
\]
These are strictly positive conductances on every existing edge. The Fiedler eigenvalue at this optimal allocation is simple for \(3\le n\le6\), whereas its multiplicity is \(2n-3\) for \(n\ge7\). Thus the eigenspace collision occurs at seven vertices per side and the optimal weight formula changes at eight. No uniqueness claim is made for arbitrary nonsymmetric optimizers.

## Assumptions and scope
The graph has \(2n\) labeled vertices, two classes of \(n\) vertices each, and exactly one forbidden cross-class edge. The Laplacian satisfies \(L_{ii}=\sum_{j\ne i}w_{ij}\) and \(L_{ij}=-w_{ij}\) on edges. Conductances are nonnegative real numbers and the budget is the sum over each **undirected edge once**. No row-stochastic normalization, holding probabilities, or minimum edge weight is imposed. The graph remains connected at the exhibited positive allocation. The theorem concerns continuous-time relaxation rate \(\lambda_2(L)\), not the two-sided eigenvalue modulus of a discrete-time chain.

## Proof
**Reduction without symmetry assumptions.** The function \(w\mapsto\lambda_2(L(w))=\min_{x\perp\mathbf1,\|x\|=1}x^TL(w)x\) is concave in conductances. Average an arbitrary feasible design over permutations of the \(m=n-1\) ordinary vertices of each side and over interchange of the two sides. Concavity shows that this orbit-average has at least as large a gap and the same budget. There are exactly two edge orbits: \(m^2\) ordinary-to-ordinary edges of weight \(a\), and \(2m\) exceptional-to-ordinary edges of weight \(b\). This proves that solving the two-variable problem suffices for the unrestricted global optimum.

**Spectrum.** With this symmetry, \(2(m-1)\) independent vectors that sum to zero among ordinary vertices on one side are eigenvectors with eigenvalue \(ma+b\). In the four-dimensional subspace of vectors constant on ordinary vertices of each side, exchanging sides decomposes it into even and odd parts. The even part has eigenvalues \(0\) and \((m+1)b\). In normalized odd coordinates, the remaining eigenvalues are those of the real symmetric matrix
\[
H=\begin{pmatrix}mb&-\sqrt m\,b\\-\sqrt m\,b&2ma+b\end{pmatrix}.
\]
Consequently \(\lambda_2\ge1\) if and only if \(ma+b\ge1\), \((m+1)b\ge1\), and \(H\succeq I\). The latter condition forces \(mb>1\) (equality would leave a nonzero off-diagonal in \(H-I\)), which makes \((m+1)b\ge1\) automatic. Its Schur complement is
\[
a\ge a_{\rm odd}(b):=\frac{(m+1)b-1}{2m(mb-1)}.
\]
The internal-mode constraint is \(a\ge a_{\rm int}(b):=(1-b)/m\). Thus for \(b>1/m\) the smallest admissible ordinary conductance is \(a=\max\{a_{\rm odd}(b),a_{\rm int}(b)\}\), and the exact normalized budget problem is
\[
\min_{b>1/m}\bigl[m^2\max\{a_{\rm odd}(b),a_{\rm int}(b)\}+2mb\bigr].
\]
All admissible weights are automatically nonnegative because \(a_{\rm odd}(b)>0\).

**Scalar minimization.** The budget along the odd constraint is
\[
D_{\rm odd}(b)=m^2 a_{\rm odd}(b)+2mb=\frac{m+5}{2}+2(mb-1)+\frac1{2(mb-1)}.
\]
Writing \(t=mb-1>0\), its unique minimum is at \(t=1/2\), namely \(b=3/(2m)\), \(a=(m+3)/(2m^2)\), and cost \(D_{\rm odd}=(m+9)/2\). The internal constraint at this candidate is \(ma+b=(m+6)/(2m)\ge1\), exactly when \(m\le6\). This establishes the first branch, including \(m=6\).

When \(m\ge7\), the two lower bounds differ by
\[
a_{\rm odd}(b)-a_{\rm int}(b)=\frac{2mb^2-(m+1)b+1}{2m(mb-1)}.
\]
The numerator has roots \(b_\pm=(m+1\pm\sqrt{m^2-6m+1})/(4m)\), satisfying \(1/m<b_-<3/(2m)<b_+\). On \([b_-,b_+]\), the internal bound is stronger, so budget is \(D_{\rm int}(b)=m(1+b)\), strictly increasing; outside, the odd bound is stronger, and \(D_{\rm odd}(b)\) decreases up to \(b_-\) and increases from \(b_+\) onward. Therefore the unique symmetric minimizer is \(b=b_-\), \(a=(1-b_-)/m\), with budget
\[
D_n=m(1+b_-)=m+\frac{m+1-\sqrt{m^2-6m+1}}4.
\]
By positive scaling, a unit-gap minimum budget \(D_n\) is equivalent to a budget-\(B\) maximum gap \(B/D_n\). This proves unrestricted global optimality.

**Eigenvalue collision.** For \(m\le5\), at the minimizer the internal eigenvalue \((m+6)/(2m)>1\), whereas the smaller odd eigenvalue equals one; the even eigenvalue and larger odd eigenvalue exceed one. For \(m=6\), internal and lower odd eigenvalues both equal one. For \(m\ge7\), the minimizer imposes \(ma+b=1\) and \(\det(H-I)=0\), so these two types coincide. Their multiplicities add to \(2(m-1)+1=2n-3\); the even mode remains greater than one, and the other odd eigenvalue is greater than one.

## Verification
A standalone Python 3 program `verify_gap.py` uses exact fractions for the rational branch and an independent Jacobi diagonalization of directly assembled matrices. Execute `python3 verify_gap.py` alongside this file. Successful checks include exact identities at \(2\le m\le6\), 493 further root-branch evaluations, 30 complete matrix spectra, and 1600 randomized two-orbit comparisons. These finite checks supplement the analytic proof; they do not establish the all-integer result by enumeration.

## Relationship to prior work
Sun, Boyd, Xiao, and Diaconis (2006) formulate continuous-time fastest mixing as maximizing the weighted Laplacian spectral gap with a total-rate budget and give general semidefinite/duality tools; their inspected examples do not give the present exact broken-biclique classification. Boyd, Diaconis, Parrilo, and Xiao (2007) analyze discrete-time fastest mixing on symmetric graphs, including intact complete bipartite examples; their stochastic nonnegativity constraints and two-sided eigenvalue-modulus objective differ from the present problem. For the deleted-edge biclique, a discrete-time spectral-radius optimum can exhibit an eight-vertex-per-side transition and even coincide with the present weight ratios in some regimes, but it does not imply the budget-normalized continuous-time optimum: for \(n=3\), discrete-time and continuous-time defect-to-ordinary weight ratios are respectively \(4/3\) and \(6/5\). The continuous-time formula, eigenvalue-collision multiplicities, and budget-optimal rates require the separate calculation above.

## Limitations
The theorem treats balanced bicliques with precisely one deleted edge, no vertex-specific rate caps, and continuous-time Laplacian convergence. It does not classify every possible nonsymmetric maximizer. General minimax literature may contain an equivalent specialization not identified in accessible full texts; in particular, a relevant early minimax paper was not available in full for decisive comparison. The originality assessment remains subject to independent literature review.

## References
1. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The fastest mixing Markov process on a graph and a connection to a maximum variance unfolding problem*, SIAM Review 48 (2006), 681–699. DOI: 10.1137/S0036144504443821. First public online date recorded by publisher: 2006-11-02. Author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf
2. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest mixing Markov chain on graphs with symmetries*, arXiv:0709.0955 (first submitted 2007-09-06), https://arxiv.org/abs/0709.0955
3. M. Fiedler, *Some minimax problems for graphs*, Discrete Mathematics 121 (1993), 65–72. DOI: 10.1016/0012-365X(93)90538-5 (bibliographic record; complete article not verified).
