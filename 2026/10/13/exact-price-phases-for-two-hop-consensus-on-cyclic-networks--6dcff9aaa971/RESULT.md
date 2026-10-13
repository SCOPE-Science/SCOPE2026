# Exact price phases for two-hop consensus on cyclic networks

## Finding

For every integer \(n\ge5\), let the vertices be \(\mathbb Z/n\mathbb Z\). Between \(j\) and \(j+1\) there is a unit-price edge, and between \(j\) and \(j+2\) an edge of price \(t>0\). Each edge has an independently chosen nonnegative symmetric conductance, subject to the exact total price-weighted budget \(1\). Let \(L\) be the weighted combinatorial Laplacian and \(\lambda_2(L)\) its second-smallest eigenvalue, counting zero multiplicity. This is the exponential consensus rate of \(\dot u=-Lu\) on the mean-zero subspace.

Define the two Fourier endpoint eigenvalues of the ordinary unit-rate cycle,
\[
\mu=4\sin^2(\pi/n),\qquad
\nu=4\sin^2\!\bigl(\pi\lfloor n/2\rfloor/n\bigr),
\]
and the positive parameters
\[
\eta=\mu+\nu-4,\qquad r=4-\nu,\qquad q=4-\mu.
\]
For \(n\ge5\) they satisfy \(\eta>0\) and \(0\le r<q\). The **unrestricted global optimum** over all independent conductances is
\[
\boxed{\quad
\Gamma_n(t)=\max \lambda_2(L)=
\begin{cases}
\displaystyle\frac{\nu r}{nt},& 0<t\le r,\\[5pt]
\displaystyle\frac{\mu\nu}{n(t+\eta)},&r\le t\le q,\\[5pt]
\displaystyle\frac{\mu}{n},&t\ge q.
\end{cases}\quad}
\]
The first interval is empty when \(n\) is even. The expressions agree on any shared boundary.

Write \(a\) for the common conductance on each of the \(n\) distance-one edges and \(b\) for the common conductance on each of the \(n\) distance-two edges. **Every edge-class-uniform optimal allocation, and no other edge-class-uniform allocation,** appears in the following exhaustive classification:

- \(0<t<r\): \(a=0\), \(b=1/(nt)\). This regime occurs only for odd \(n\).
- \(r<t<q\): \(a=\eta/[n(t+\eta)]\), \(b=1/[n(t+\eta)]\).
- \(t>q\): \(a=1/n\), \(b=0\).
- \(t=r>0\): every and only \(a,b\ge0\) with \(n(a+tb)=1\) and \(a\le\eta b\).
- \(t=q\): every and only \(a,b\ge0\) with \(n(a+tb)=1\) and \(a\ge\eta b\).

These class-uniform allocations attain the unrestricted optimum. The assertion does **not** classify all potentially nonuniform optimal allocations.

**Parity and asymptotic consequences.** Since \(r=0\) for even \(n\), every positive price requires some distance-one conductance at a class-uniform optimum. For odd \(n\), \(r=4\sin^2(\pi/(2n))>0\); if \(t<r\), the optimum discards every distance-one edge and retains only the connected distance-two cycle. For even \(n\), the distance-two subgraph instead has two connected components. For each fixed \(0<t<4\), as \(n\to\infty\), the middle phase eventually applies and
\[
\Gamma_n(t)\sim\frac{16\pi^2}{tn^3},\qquad
\frac{\Gamma_n(t)}{\mu/n}\longrightarrow\frac4t,
\]
where \(\mu/n\) is the best rate with only ordinary cycle edges. For fixed \(t\ge4\) the nearest-neighbor-only design is optimal for every \(n\ge5\). For example, on six vertices at \(t=1\), the unique class-uniform optimum assigns \(a=b=1/12\), giving gap \(1/3\) rather than the nearest-neighbor-only gap \(1/6\).

## Assumptions and scope

The graph is precisely the undirected simple square of a cycle: the \(2n\) edges of lengths one and two modulo \(n\) are distinct because \(n\ge5\). The conductance of each undirected edge is nonnegative and its cost is its stated price multiplied by its conductance. Every feasible design spends exactly \(1\). The Laplacian is the ordinary unnormalized graph Laplacian \(L=\sum_{\{i,j\}}w_{ij}(e_i-e_j)(e_i-e_j)^{\mathsf T}\), not a normalized random-walk Laplacian. The continuous-time dynamics is symmetric and mass-preserving. No stochastic transition-probability bound is imposed on a rate.

## Proof

**1. Symmetry reduction without an assumption on edge rates.** The variational formula
\[
\lambda_2(L)=\min_{v\perp\mathbf1,\,\|v\|_2=1}v^{\mathsf T}Lv
\]
shows that \(\lambda_2\) is concave in the edge conductances. Cyclically rotate any feasible conductance assignment through all \(n\) positions and average it. The average remains feasible and has a constant conductance \(a\) on distance-one edges and \(b\) on distance-two edges. Every rotated Laplacian has the original spectral gap, hence concavity gives \(\lambda_2(L_{\rm avg})\ge\lambda_2(L)\). It therefore suffices to solve the class-uniform problem to establish the **global value**, though averaging alone says nothing about uniqueness of nonuniform maximizers.

**2. Two Fourier modes suffice.** For class-uniform \(a,b\), the Fourier mode \(v_k(j)=\exp(2\pi i kj/n)\) has Laplacian eigenvalue
\[
\Lambda_k=a x_k+b x_k(4-x_k),\qquad
x_k=4\sin^2(\pi k/n),\qquad k=0,\ldots,n-1.
\]
Indeed, the distance-two eigenvalue is \(4\sin^2(2\pi k/n)=x_k(4-x_k)\). For nonconstant modes \(\mu\le x_k\le\nu\), and both endpoints occur. For \(b\ge0\), the polynomial \(x\mapsto ax+b x(4-x)\) is concave on \([\mu,\nu]\); it is therefore at least the smaller endpoint value. Thus exactly
\[
\lambda_2(L(a,b))=\min\{\mu(a+qb),\ \nu(a+rb)\}.
\]
There are no hidden interior Fourier constraints.

**3. Exhaustive price optimization.** The budget is \(n(a+tb)=1\), so \(a=1/n-tb\) with \(0\le b\le1/(nt)\). The two endpoint branches become
\[
G_\mu(b)=\frac\mu n+\mu(q-t)b,\qquad
G_\nu(b)=\frac\nu n+\nu(r-t)b.
\]
Their difference vanishes exactly when \(a=\eta b\), equivalently \(b=1/[n(t+\eta)]\). Here \(\eta=\mu-r>0\) and \(r<q\). When \(t<r\), both branches increase, forcing the unique uniform optimum at the largest \(b\). When \(r<t<q\), the first increases and the second decreases; their intersection is the unique maximizer. When \(t>q\), both branches decrease, forcing \(b=0\). If \(t=r>0\), the second branch is constant and the optimum is its full plateau where \(a\le\eta b\). If \(t=q\), the first branch is constant and the optimum is its full plateau where \(a\ge\eta b\). Substitution yields the claimed formulas and all boundary equalities. For even \(n\), \(r=0\), so the first phase is empty for positive prices. This proves the complete uniform-face classification and global value.

**4. Parity and limits.** If \(n\) is even, \(\nu=4\) and \(r=0\); the distance-two graph splits by vertex parity. If \(n\) is odd, \(\nu=4\cos^2(\pi/(2n))\) and \(r>0\); multiplication by two permutes the cyclic vertices, so those edges form a Hamiltonian cycle. Finally \(\mu\sim4\pi^2/n^2\), \(\nu\to4\), \(r\to0\), \(q\to4\), and \(\eta\to0\), which give the stated fixed-price asymptotics.

## Verification

Run `python3 verify.py` using the standard Python 3 library. The checker independently constructs Fourier eigenvalues, checks the predicted optimum against many feasible class-uniform designs, computes full Laplacian eigenvalues by a standalone Jacobi eigensolver for independently weighted nonuniform designs, and checks transition and parity cases. Its observed result is

`VERIFY_OK uniform_tests=23760 nonuniform_matrix_tests=972 boundary_tests=54 parity_tests=9`.

These are finite consistency checks. The proof above, not finite enumeration or numerical tolerances, establishes the universal assertion for every admissible integer \(n\) and real \(t\).

## Relationship to prior work

Saha and Das (2025, DOI:10.26713/cma.v16i4.3246, Theorem 3.4) determine the unweighted Laplacian spectrum of **this same cycle-square graph**; thus neither the underlying circulant eigenvalue technique nor its unit-conductance spectrum is claimed as new. Their paper does not assign independent priced conductances to the two edge types, maximize the gap, or derive a price-phase classification. Boyd, Diaconis, Parrilo, and Xiao (2007, arXiv:0709.0955) develop group-averaging and symmetry-reduced optimization for **discrete-time** fastest-mixing chains; their cycle analysis does not assert the exact price-dependent two-hop **continuous-time** Laplacian-gap law above. Shakeri and collaborators (2015, arXiv:1510.06785) maximize Laplacian algebraic connectivity under a budget for **one-to-one interlayer links with fixed within-layer Laplacians**, a different feasible set and graph family. Gerencsér (2014, arXiv:1401.1692) studies random sublinear-count long-range shortcuts and order-of-magnitude mixing times rather than the deterministic full set of nearest and second-nearest links. Apers and Sarlette (2015, arXiv:1503.01269) optimize a filtered **discrete-time** consensus objective. These works supply motivation and methods, not a proved implication giving the displayed three-phase diagram; hidden equivalent specializations in further literature remain a historical risk.

## Limitations

The theorem fixes unit total conductance expenditure and costs that are uniform within the two edge-length classes. It does not cover directed or nonnormal dynamics, prescribed positive lower bounds on every edge, normalized Markov generators with fixed exit rates, general shortcut lengths, or classification of every nonuniform maximizer. The conclusions are exact-arithmetic mathematical statements; the auxiliary floating-point verification does not certify arbitrary dimensions. Novelty is assessed against the inspected material, not independently established historical priority.

## References

1. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries* (public preprint 2007), arXiv:0709.0955, https://arxiv.org/abs/0709.0955.
2. H. Shakeri, N. Albin, F. Darabi Sahneh, P. Poggi-Corradini, C. Scoglio, *Maximizing Algebraic Connectivity in Interconnected Networks* (public preprint 2015), arXiv:1510.06785, https://arxiv.org/abs/1510.06785.
3. B. Gerencsér, *Mixing Times of Markov Chains on a Cycle with Additional Long Range Connections* (public preprint 2014), arXiv:1401.1692, https://arxiv.org/abs/1401.1692.
4. S. Apers, A. Sarlette, *Accelerating Consensus by Spectral Clustering and Polynomial Filters* (public preprint 2015), arXiv:1503.01269, https://arxiv.org/abs/1503.01269.
5. B. Gerencsér, J. M. Hendrickx, P. Van Dooren, *Spectral Gap of Markov Chains on a Cycle* (2015), https://real.mtak.hu/173919/1/cycle_spectral_gap.pdf.
6. N. Saha, M. Das, *The Square Graph of a Cycle Graph* (2025), DOI:10.26713/cma.v16i4.3246, https://www.rgnpublications.com/journals/index.php/cma/article/view/3246.
