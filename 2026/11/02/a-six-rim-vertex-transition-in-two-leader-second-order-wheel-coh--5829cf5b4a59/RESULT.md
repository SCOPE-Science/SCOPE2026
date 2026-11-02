# A six-rim-vertex transition in two-leader second-order wheel coherence

## Finding
Let \(W_n=K_1\vee C_n\) be the unweighted wheel with one hub and \(n\ge3\) rim vertices. For each unordered two-vertex leader set \(S\), let \(F=V(W_n)\setminus S\), let \(L_{FF}\) be the **principal grounded** (unnormalized) graph Laplacian, retaining the diagonal contributions from edges to leaders, and put
\[
J_2(S)=\operatorname{tr}(L_{FF}^{-2}).
\]
All and only the following leader sets minimize \(J_2\):

- \(n=3\): every one of the six pairs (all tie);
- \(n=4\): the two pairs of opposite rim vertices;
- \(n=5\): the five rim pairs at cyclic distance two;
- every \(n\ge6\): the \(n\) pairs consisting of the hub and one rim vertex.

The minimum is respectively \(5/16\), \(361/900\), \(1497/1936\), and, for \(n\ge6\),
\[
J_2^*(n)=\sum_{j=1}^{n-1}\frac{1}{[3-2\cos(j\pi/n)]^2}.
\]
This transition differs from the first-inverse grounded-Laplacian objective: on \(W_6\), hub–rim leaders have \(\operatorname{tr}(L_{FF}^{-1})=25/12\) versus \(2\) for opposite rim leaders, but the inverse-square values are \(157/144\) versus \(9/8\), with the strict preference reversed. Thus the two noise models can prescribe distinct leader placements on the same graph.

## Assumptions and scope
The graph is simple, undirected, connected, and has unit conductance on every edge. Exactly two *noise-free, grounded* leaders are selected, and all other vertices are followers. The choice is unrestricted; neither the hub nor rim positions are prescribed. The quantity \(J_2\) is the unnormalized trace of the inverse square, **not** the trace of the inverse. For example, for second-order follower dynamics with relative position and relative velocity feedback,
\[
\ddot x+\eta L_{FF}\dot x+L_{FF}x=\dot W,\qquad \eta>0,
\]
with independent unit-intensity white acceleration noises, diagonalizing the positive definite \(L_{FF}\) and solving each modal Lyapunov equation gives stationary total positional variance \(J_2(S)/(2\eta)\). The theorem therefore characterizes the minimizers for every fixed \(\eta>0\); it makes no claim for independent absolute velocity damping, correlated noise, weighted wheels, or more than two leaders.

## Proof
**Reduction to finitely many orbit types.** Label the hub \(0\) and the rim \(1,\ldots,n\) cyclically. Wheel automorphisms leave one hub–rim type and \(\lfloor n/2\rfloor\) two-rim types indexed by cyclic distance \(d=1,\ldots,\lfloor n/2\rfloor\). Every grounded matrix is positive definite, because the connected wheel has a nonempty grounded set.

**Hub–rim formula.** Grounding the hub and one rim vertex leaves the remaining \(n-1\) rim vertices as a path, with the hub edges retained in the diagonal. Hence
\[
L_{FF}=T_{n-1},\qquad T_\ell=3I_\ell-A(P_\ell),
\]
where the empty matrix \(T_0\) contributes zero. Its eigenvalues are \(3-2\cos(j\pi/(\ell+1))\), giving the stated sum for hub–rim pairs.

**Two-rim formula.** Ground rim vertices at cyclic distance \(d\), leaving path intervals of lengths \(d-1\) and \(n-d-1\) as well as the hub. Write
\[
D=T_{d-1}\oplus T_{n-d-1},\quad u=D^{-1}\mathbf{1},\quad s=(n-\mathbf{1}^{\mathsf T}u)^{-1}.
\]
The grounded matrix, ordered with hub first, is \(\left(\begin{smallmatrix}n&-\mathbf{1}^{\mathsf T}\\-\mathbf{1}&D\end{smallmatrix}\right)\). Its Schur complement is strictly positive, and the block inverse is
\[
L_{FF}^{-1}=\begin{pmatrix}s&su^{\mathsf T}\\su&D^{-1}+suu^{\mathsf T}\end{pmatrix}.
\]
Taking the squared Frobenius norm yields the exact expression
\[
J_2(n,d)=\operatorname{tr}(D^{-2})+2s\,u^{\mathsf T}D^{-1}u+s^2(1+u^{\mathsf T}u)^2.
\]
This also covers adjacent leaders, since an empty path is omitted. It gives an exact rational expression for every integer \(n,d\), with only inverses of explicitly specified tridiagonal integer matrices.

**Exact bounded cases.** For \(3\le n\le10\), every symmetry orbit is checked by rational Gaussian elimination, using either the grounded matrix directly or the independent Schur-complement expression above. The results are fully specified in `finite_cases.csv`; the standalone `verify.py` reconstructs all \(216\) labelled two-leader matrices, checks every resulting trace with exact fractions, tests every winner and tie, and cross-checks each two-rim orbit using the Schur formula. The finite table gives all the asserted minimizers for \(3\le n\le10\), in particular the strict switch between \(n=5\) and \(n=6\).

**Uniform all-size bound for \(n\ge11\).** Let \(\ell=n-1\ge10\). If both leaders are on the rim, the \(\ell\)-vector of ones on all followers has Rayleigh quotient equal to the number of edges crossing from followers to leaders divided by \(\ell\). Every rim vertex has degree three, so there are at most six crossing edges. Thus
\[
\lambda_{\min}(L_{FF})\le6/\ell,\qquad J_2(n,d)\ge\lambda_{\min}^{-2}\ge\ell^2/36.
\]
For hub–rim leaders, write \(q=(3-\sqrt5)/2\in(0,1)\). The positive inverse kernel of \(3I-A(\mathbb Z)\) on the infinite path is \(G(i,j)=q^{|i-j|}/\sqrt5\). Both the finite-path and infinite-path resolvents admit convergent nonnegative walk-series expansions. Every walk contained in the finite path is also a walk on the infinite path; hence \(0\le(T_\ell^{-1})_{ij}\le G(i,j)\). Consequently
\[
\begin{aligned}
J_2(\text{hub,rim})&=\sum_{i,j=1}^{\ell}(T_\ell^{-1})_{ij}^{2}
\le\frac{\ell}{5}\left(1+2\sum_{m\ge1}q^{2m}\right)
=\frac{3\ell}{5\sqrt5}.
\end{aligned}
\]
Finally, \(3/(5\sqrt5)<27/100<10/36\le\ell/36\): the first strict inequality is equivalent to \(400<405\), and the second is rational. Therefore \(J_2(\text{hub,rim})<\ell^2/36\le J_2(n,d)\) for every two-rim pair and every \(n\ge11\). Combined with the exact bounded cases, this proves the complete classification, including all ties and the absence of any other optimizers.

## Verification
`verify.py` requires Python 3.8 or later and uses only the standard library. Run `python verify.py`; its final lines are `BASE_CASES_OK` and `TAIL_CERTIFICATE_OK`. It forms the original unnormalized grounded matrices afresh for \(n=3,\ldots,10\), computes exact rational inverses, checks \(216\) labelled pairs, independently evaluates every two-rim orbit through the block Schur formula, and confirms the rational tail inequalities. The infinity-range conclusion comes from the analytic Green-kernel and Rayleigh bounds above, **not** from extrapolating this bounded enumeration. `finite_cases.csv` records the exact orbit values so the finite comparisons can also be independently inspected.

## Relationship to prior work
Lin, Fardad and Jovanović (arXiv:1302.0450, first public version 2013-02-03) formulate general noisy leader-selection optimization with the *first-inverse* performance criterion and semidefinite relaxations, but do not give this wheel inverse-square classification. Patterson, McGlohon and Dyagilev (arXiv:1412.6595, first public version 2014-12-20) optimize the first-inverse leader criterion on one-dimensional paths and rings, not the hub-joined wheel or the inverse-square objective. Earlier second-order network-coherence studies motivate spectral inverse-square metrics but need not address optimal pinning pairs. The present result identifies the exact change in optimal leader geometry when the criterion changes, using a finite exact calculation matched to a uniform infinite-family proof. No absolute priority claim is made.

## Limitations
The result concerns one particular unweighted wheel family, exactly two perfectly grounded leaders, independent unit acceleration noise, and the stated relative-damping dynamics. It does not classify two-rim pair rankings for arbitrary large \(n\), nor weighted wheels or other damping/noise models. The infinity-range argument establishes global optimality but not an elementary closed form for all suboptimal orbit costs beyond the displayed block-matrix formula. Potential specialized prior coverage not located by the documented searches remains a residual originality risk. No independent external mathematical audit has been performed.

## References
1. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (initial posting 2013-02-03), https://arxiv.org/abs/1302.0450 .
2. S. Patterson, N. McGlohon, and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (initial posting 2014-12-20), https://arxiv.org/abs/1412.6595 .
3. W. Sun, Q. Ding, J. Zhang, and F. Chen, *Coherence in a family of tree networks with an application of Laplacian spectrum*, Chaos 24 (2014), 043112, https://doi.org/10.1063/1.4897568 (related inverse-square coherence on tree networks, not wheel leader placement).
