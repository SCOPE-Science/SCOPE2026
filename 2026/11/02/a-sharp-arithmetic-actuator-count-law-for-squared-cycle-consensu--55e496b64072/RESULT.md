# A sharp arithmetic actuator-count law for squared-cycle consensus networks

## Finding

For each integer \(n\ge5\), the undirected squared cycle \(C_n^2\) has vertices \(\mathbb Z/n\mathbb Z\), with an edge between vertices whose cyclic distance is one or two. Its unit-weight Laplacian is \(L_n=4I-A_n\). Consider
\[
\dot z(t)=-L_nz(t)+B_Uu(t),\qquad
B_U=[e_j]_{j\in U},\quad U\subseteq\mathbb Z/n\mathbb Z,
\]
where each selected vertex has one independent scalar control input. Write \(q(n)\) for the smallest \(|U|\) making \((-L_n,B_U)\) Kalman controllable. Then
\[
\boxed{q(n)=\begin{cases}
4,&5\mid n\ \text{or}\ 12\mid n,\\
3,&6\mid n,\ 5\nmid n,\ 12\nmid n,\\
2,&\text{otherwise}.
\end{cases}}
\]
A constructive minimum-size selection is the consecutive vertex set \(U=\{0,1,\dots,q(n)-1\}\); no smaller selection works. In particular, \(q(5)=4\), \(q(6)=3\), \(q(7)=2\), \(q(10)=4\), and \(q(12)=4\). This law concerns exactly the fixed, unit-weight squared cycle, not a generic perturbation of its edge weights or strong structural controllability over all weights.

## Assumptions and scope

All graphs are undirected and simple, all existing edges have weight one, \(n\ge5\), and \(u\) has \(|U|\) independent channels, one per controlled vertex. The terms *controllable* and *minimum* refer to the ordinary finite-dimensional Kalman/PBH test over \(\mathbb R\) (equivalently over \(\mathbb C\)). No bounds on input energy are claimed. The matrix \(L_n\) is symmetric and the constant eigenvector may be directly actuated. The adjacency spectrum is used only because subtracting from \(4I\) preserves eigenspaces.

## Proof

**1. The Fourier spectrum.** Let \(\zeta=\exp(2\pi i/n)\) and \(f_k(j)=\zeta^{kj}\). The Fourier eigenvalues of \(A_n\) are
\[
a_k=\zeta^k+\zeta^{-k}+\zeta^{2k}+\zeta^{-2k}
=4c_k^2+2c_k-2,\qquad c_k=\cos(2\pi k/n).
\]
For different cosine values \(c_k\ne c_l\), the equality \(a_k=a_l\) factors as
\[
0=(c_k-c_l)\big(4(c_k+c_l)+2\big),
\]
so the sole possible *extra* coincidence is \(c_k+c_l=-1/2\). Equal cosine values already account for the paired indices \(k\) and \(-k\), except the self-paired indices \(0\), and \(n/2\) when \(n\) is even.

**2. Excluding every other algebraic coincidence.** The complex numbers \(\zeta^k\), \(\zeta^l\) have respective exact orders \(r=n/\gcd(n,k)\) and \(s=n/\gcd(n,l)\). Here \(\gcd(n,0)=n\), so the constant frequency has order one. Suppose \(c_k+c_l=-1/2\), or
\[
\zeta^k+\zeta^{-k}+\zeta^l+\zeta^{-l}=-1.
\]
Take the average of all automorphisms \(\zeta\mapsto\zeta^a\), for \(a\in(\mathbb Z/n\mathbb Z)^\times\). The image of this group on units modulo each divisor \(r\mid n\) is surjective. The mean of a primitive \(r\)-th root over these automorphisms is \(\mu(r)/\varphi(r)\), by the Ramanujan sum \(\sum_{\gcd(a,r)=1}e^{2\pi ia/r}=\mu(r)\). Thus
\[
\frac{\mu(r)}{\varphi(r)}+\frac{\mu(s)}{\varphi(s)}=-\frac12. \tag{1}
\]
For orders other than \(1,2,3,6\), the values \(\mu(d)/\varphi(d)\) lie in \([-1/4,1/4]\); equality \(-1/4\) is possible only for \(d=5\), since \(\varphi(d)=4\) for \(d\in\{5,8,10,12\}\) and among these only \(\mu(5)=-1\). The exceptional values are \(1\) at order one, \(-1\) at order two, \(-1/2\) at order three, and \(1/2\) at order six. Hence (1) has only three candidate patterns: \((r,s)=(2,6)\), one order three and the other with zero Möbius function, or \((r,s)=(5,5)\). In the order-three case \(c_k=-1/2\) forces \(c_l=0\), so the other order is exactly four. In the order-five case there are exactly two distinct cosine values, \((\sqrt5-1)/4\) and \(-(\sqrt5+1)/4\), whose sum is \(-1/2\); the pair must use one of each. Consequently the complete list of extra cross-cosine coincidences is
\[
(r,s)=(2,6),\ (3,4),\ (5,5)\text{ with distinct cosine values}. \tag{2}
\]
They exist precisely when \(6\mid n\), \(12\mid n\), and \(5\mid n\), respectively.

**3. Exact dimensions of the exceptional eigenspaces.** In (2), order two contributes one Fourier index and order six contributes two; both have adjacency eigenvalue \(0\), giving multiplicity three if \(6\mid n\). Orders three and four contribute two indices each at adjacency eigenvalue \(-2\), giving multiplicity four if \(12\mid n\). The two order-five cosine values each represent two Fourier indices and share adjacency eigenvalue \(-1\), giving multiplicity four if \(5\mid n\). These three eigenvalues are distinct and no additional coincidences can occur by step 2. Every other nonconstant spectral eigenspace has dimension at most two, and at least one conjugate pair exists because \(n\ge5\). Therefore the maximum adjacency (and Laplacian) eigenvalue multiplicity equals the displayed \(q(n)\).

**4. Lower and matching upper bounds for vertex inputs.** For any eigenspace of dimension \(d\), an input matrix with fewer than \(d\) columns fails the Popov–Belevitch–Hautus (PBH) test: some nonzero eigenvector is orthogonal to its columns. Thus every controllable vertex set has size at least \(q(n)\). Conversely, let \(U=\{0,1,\dots,q(n)-1\}\). If an eigenspace has Fourier modes with distinct indices \(k_1,\dots,k_d\), \(d\le q(n)\), restriction of these eigenvectors to the first \(d\) selected vertices is the Vandermonde matrix
\[
V=(\zeta^{jk_a})_{0\le j<d,\,1\le a\le d},\qquad
\det V=\prod_{1\le a<b\le d}(\zeta^{k_b}-\zeta^{k_a})\ne0.
\]
Hence restriction to the selected inputs is injective on every eigenspace. The PBH test proves the pair \((-L_n,B_U)\) controllable, attaining the lower bound. This establishes the result for all integers \(n\ge5\).

## Verification

The accompanying standalone Python script `verify.py` uses the standard library. It independently groups numerically evaluated Fourier eigenvalues for every \(5\le n\le250\), constructs the integer adjacency matrix and checks the Kalman ranks modulo the prime \(1000003\) for \(5\le n\le34\), and checks the orders of every numerically detected cross-cosine collision for \(5\le n\le180\). Replaying `python3 verify.py` gave **816 passed assertions**. Full modular rank implies full rational rank for these tested instances. Neither the finite calculations nor floating-point collision grouping substitutes for the all-dimensional proof in the previous section.

## Relationship to prior work

Parlangeli and Notarstefano (2011) characterized input locations on *ordinary* path and cycle Laplacians. Yuan et al. (2013) prove the general minimum-number-of-inputs/multiplicity principle; Nabi-Abdolyousefi and Mesbahi (2013) apply the principle to circulant networks, and their abstract states the same general rule. These results account for the general PBH part of step 4 and are **not** claimed as original here. Monshizadeh, Zhang and Camlibel (2014) study zero forcing and graph-structural variants, which differ from the exact homogeneous-weight problem.

Saha and Das (2025), Theorem 3.2, give the same Fourier eigenvalue expression for \(C_n^2\). Their Corollary 3.3 lists the usual conjugate pairs but does not give the complete accidental-cross-frequency multiplicity classification. Indeed their worked six-cycle eigenvalue list includes adjacency eigenvalue \(0\) three times. The contribution here is the exhaustive cyclotomic classification of all extra collisions, its arithmetic all-dimension leader count, and an explicit minimum-size placement. A general spectral formula alone does not enumerate the exact degeneracies.

## Limitations

The result does not address optimal input effort, robustness, arbitrary edge weights, distinct weights on length-one versus length-two edges, other powers of cycles, or zero-forcing requirements over an entire qualitative matrix class. The six-page 2013 circulant-controllability article and the 2014 expanded chapter could not be inspected in full; they may contain examples or special cases overlapping this arithmetic classification. The published 2025 Fourier-spectrum treatment was available and its stated multiplicities were compared directly. No independent mathematical validation has been performed.

## References

1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556, first public 2011-09-16, https://arxiv.org/abs/1109.3556 .
2. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang and Y.-C. Lai, *Exact controllability of complex networks*, Nature Communications 4 (2013), 2447, DOI:10.1038/ncomms3447, https://pmc.ncbi.nlm.nih.gov/articles/PMC3945876/ .
3. M. Nabi-Abdolyousefi and M. Mesbahi, *On the Controllability Properties of Circulant Networks*, IEEE Transactions on Automatic Control 58 (2013), 3179–3184, DOI:10.1109/TAC.2013.2259992 (abstract accessible; full text not inspected).
4. N. Monshizadeh, S. Zhang and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868, first public 2014-03-19, https://arxiv.org/abs/1403.4868 .
5. N. Saha and M. Das, *The Square Graph of a Cycle Graph*, Communications in Mathematics and Applications 16 (2025), 1107–1117, DOI:10.26713/cma.v16i4.3246, https://www.rgnpublications.com/journals/index.php/cma/article/download/3246/1927/13255 .
