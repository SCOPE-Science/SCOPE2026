# Exact minimal cycle-flow projection constants of complete graphs \(K_n\)

## Finding
For every integer \(n\ge3\), let \(G=K_n\) be the complete simple graph, orient each edge \(i\to j\) for \(i<j\), and equip the real edge-flow space \(X_n=\mathbb R^{E(G)}\) with \(\|x\|_1=\sum_{e\in E(G)}|x_e|\). Let \(B:\mathbb R^{E(G)}\to\mathbb R^n\) be the incidence map whose column at \(\{i,j\}\) is \(e_i-e_j\). The cycle/circulation space is \(Z(G)=\ker B\), of dimension \(\binom{n-1}{2}\).

Define the *relative projection constant*
\[
\lambda(Z(G),X_n)=\inf\{\|P\|_{X_n\to X_n}:P^2=P,\;\operatorname{ran}P=Z(G)\}.
\]
Then the exact formula, valid without any restriction beyond \(n\ge3\), is
\[
\boxed{\lambda(Z(K_n),\ell_1(E(K_n)))=3-\frac6n.}
\]
An attaining projection is the Euclidean orthogonal cycle projection \(Q=I-n^{-1}B^{\mathsf T}B\), viewed as an operator on the edge \(\ell_1\) space. It is also the only projection commuting with the signed edge representation of every vertex permutation. In particular, the cycle space is \(1\)-complemented when \(n=3\), but not when \(n\ge4\); the sharp constants tend to \(3\) from below as \(n\to\infty\).

## Assumptions and scope
All spaces and linear maps are **real** and finite-dimensional. We use the unweighted complete graph and the edge-coordinate \(\ell_1\) norm, not the \(\ell_2\) operator norm. The notation \(Z(G)\) refers to real signed circulations, not the binary cycle space. The projection constant is *relative to the given ambient edge space*, not the absolute projection constant of the abstract Banach space. The condition \(n\ge3\) is essential because for \(n=2\) the cycle space vanishes. Each vertex permutation acts isometrically on \(X_n\) by permuting edges with the sign induced by their chosen orientations.

## Proof
**1. Candidate and its exact norm.** For the complete graph, the vertex Laplacian is \(BB^{\mathsf T}=nI-J\), where \(J\) is the all-ones matrix. Since \(B^{\mathsf T}J=0\), the operator \(Q=I-n^{-1}B^{\mathsf T}B\) satisfies \(BQ=0\) and \(Qz=z\) whenever \(Bz=0\). Thus \(Q^2=Q\) and \(\operatorname{ran}Q=Z(G)\).

For a fixed edge \(e=\{a,b\}\), the corresponding column of \(B^{\mathsf T}B\) has diagonal entry \(2\), has modulus \(1\) at each of the \(2(n-2)\) other edges incident with exactly one endpoint of \(e\), and is \(0\) elsewhere. Since \(n\ge3\), \(1-2/n\ge0\). Consequently every column of \(Q\) has absolute sum
\[
\|Qe\|_1=1-\frac2n+\frac{2(n-2)}n=3-\frac6n.
\]
The operator norm of a matrix on \(\ell_1\) equals its maximum column absolute sum, so \(\|Q\|=3-6/n\).

**2. Optimality among all projections.** Let \(P:X_n\to Z(G)\) be any projection. The symmetric group \(S_n\) acts on \(X_n\) through the signed edge permutation isometries \(U_\sigma\), and preserves \(Z(G)\). The averaged operator
\[
\overline P=\frac1{n!}\sum_{\sigma\in S_n}U_\sigma^{-1}PU_\sigma
\]
is a projection onto \(Z(G)\), commutes with every \(U_\sigma\), and has norm at most \(\|P\|\).

To prove this average equals \(Q\), consider an arbitrary equivariant operator \(T:X_n\to Z(G)\). Let \(p=Te_{12}\), with edges always oriented from lower to higher labels. The transposition interchanging vertices \(1\) and \(2\) maps \(e_{12}\) to \(-e_{12}\), whence it maps \(p\) to \(-p\). Every permutation fixing \(1,2\) preserves \(e_{12}\) and hence fixes \(p\). Writing \(p_{ij}\) for edge coordinates, these two stabilizer conditions give
\[
 p_{12}=a,\qquad p_{1k}=b,\qquad p_{2k}=-b\quad(3\le k\le n),\qquad p_{kl}=0\quad(3\le k<l\le n).
\]
Here \(p_{kl}=0\) follows directly because swapping \(1,2\) fixes such an edge while negating \(p\). Since \(Bp=0\), its first vertex equation is \(a+(n-2)b=0\). Therefore the possible vector \(p\) lies on a one-dimensional line. The nonzero vector \(Qe_{12}\) lies on this line, so \(Te_{12}=cQe_{12}\) for some scalar \(c\). Edge transitivity of \(S_n\), equivariance, and the equivariance of \(Q\) imply \(T=cQ\) on every coordinate basis vector.

Apply this to \(T=\overline P\). Because \(Z(G)\) is nonzero for \(n\ge3\) and \(\overline P\) is the identity on it, \(c=1\), and hence \(\overline P=Q\). It follows that \(\|P\|\ge\|\overline P\|=\|Q\|=3-6/n\), proving the exact formula and uniqueness among equivariant projections.

## Verification
The standalone file `VERIFY.py`, using only exact integers and rational arithmetic from the Python standard library, constructs \(B\) and \(Q\) for every \(3\le n\le12\). It checks divergence zero, idempotence, fixation of every elementary triangle circulation, all column norm identities, and commutation with adjacent vertex transpositions for \(3\le n\le8\). A direct execution completed **59,831 exact comparisons** and returned `VERIFY_OK`. Finite checking is supplementary; the proof above covers all integers \(n\ge3\). To reproduce: `python3 VERIFY.py`.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii [1] identify the Lipschitz-free space of a finite unit-edge graph with the edge \(\ell_1\) quotient by its real cycle space, and develop symmetrization for projection constants on recursively built graphs. They explicitly contrast the nontrivial cycle space of \(K_n\) with that of a star but do not state its exact relative cycle-space projection constant. Novotný [2] studies retractional Schauder bases on cycle metrics rather than a projection from all complete-graph edge flows onto their full circulation space. Kobos [3] gives results about relative projections onto *hyperplanes* in finite-dimensional normed spaces; for \(n\ge4\) the present subspace has codimension \(n-1\), so the hyperplane formulas do not evaluate it. The general averaging principle in [1] supplies a method, not the particular stabilizer classification and sharp numeric constant established here.

## Limitations
This theorem applies only to complete simple graphs with uniform unit edge weights, and does not give constants for arbitrary or weighted graphs. It determines the relative \(\ell_1\) cycle-space projection constant, not the Banach–Mazur distance or the absolute projection constant of a Lipschitz-free space. It proves uniqueness only among vertex-permutation-equivariant projections; other minimizers are not classified. An equivalent result under older norm-one Hodge decomposition or approximation-theoretic terminology may remain unindexed. No independent external audit has been performed.

## References
[1] S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1 (public 2018-07-10); Sections 1.1, 1.3, 2, 4 and 6.

[2] M. Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces*, arXiv:1905.13188v1 (public 2019-05-30); Sections 1–4.

[3] T. Kobos, *Hyperplanes of finite-dimensional normed spaces with the maximal relative projection constant*, arXiv:1411.6214v1 (public 2014-11-23); Introduction and Theorem 2.2.
