# Nilpotent partial-permutation conjugacy is determined by its centralizer rank spectrum

## Finding
Let \(X\) be a finite set, let \(\mathcal I(X)\) be its symmetric inverse monoid, and let \(\alpha\in\mathcal I(X)\) be nilpotent. Define
\[
C_\alpha(t)=\sum_{\beta\in\mathcal I(X),\ \alpha\beta=\beta\alpha}t^{|\operatorname{dom}\beta|}.
\]
**Rank-spectral rigidity:** for nilpotent \(\alpha,\gamma\) (even on initially unspecified finite sets), equality \(C_\alpha(t)=C_\gamma(t)\) holds if and only if they have the same multiset of nilpotent-chain lengths. Hence this single polynomial determines the nilpotent conjugacy class and ambient set size.

A constructive formula also computes every coefficient. If the chain-length partition is \(\lambda=(\lambda_1,\ldots,\lambda_s)\), put \(W_{ij}(t)=t+t^2+\cdots+t^{\min(\lambda_i,\lambda_j)}\). Then
\[
C_\alpha(t)=\sum_{M}\prod_{(i,j)\in M}W_{ij}(t),
\]
where \(M\) ranges over all matchings of the \(s\)-by-\(s\) bipartite board (each source and target index used at most once), including the empty matching.

## Assumptions and scope
Partial injections compose as ordinary partial functions, and rank means domain size. A chain of length \(L\) means \(L\) *vertices*, with arrows from the first to the second and so forth, and the last vertex undefined under \(\alpha\). An isolated vertex is a chain with \(L=1\). Every nilpotent partial injection decomposes uniquely into such disjoint chains. The result holds for all \(|X|\ge0\); \(C_\alpha(t)=1\) for the empty set. No hypothesis on a field is needed.

## Proof
1. Write the source chains \(S_i=(x_{i,1},\ldots,x_{i,\lambda_i})\) and target chains \(S_j=(y_{j,1},\ldots,y_{j,\lambda_j})\). If a commuting partial injection \(\beta\) is nonempty on \(S_i\), commutation forces its domain intersection with \(S_i\) to be precisely an initial segment of \(\ell\) vertices. Its image is the terminal segment of \(\ell\) vertices of one target chain, in the unique arrow-respecting order. Here \(1\le\ell\le\min(\lambda_i,\lambda_j)\). This statement also includes isolated-vertex chains. To see the initial-segment necessity, if \(x_{i,k}\) is defined under \(\beta\) but its predecessor is not, commutation fails at that predecessor. For successive defined vertices, commutation forces successive images. The image of the last defined vertex must be the terminal vertex, since the next source vertex has no \(\beta\)-image. Conversely such a prefix-to-suffix map commutes with \(\alpha\), including the zero cases at all endpoints.
2. Images of two nonempty source chains cannot lie in one target chain: every nonempty terminal segment contains that target chain's last vertex, contradicting injectivity. Thus a commuting \(\beta\) consists uniquely of a matching of source to target chains and, on each matched edge, one choice of \(\ell\) in the stated interval. Conversely all these choices produce commuting partial injections. Multiplying their rank weights proves the matching formula.
3. Let \(c_j=|\{i:\lambda_i\ge j\}|\) and let \(\lambda^{<j}\) be obtained by replacing each chain size \(\lambda_i\) by \(\min(\lambda_i,j-1)\), preserving the number of chains. For \(j\ge2\), every matched edge of length less than \(j\) contributes equally to \(C_\lambda\) and \(C_{\lambda^{<j}}\). Their coefficient of \(t^j\) differs only through one-edge matchings of exact length \(j\): there are exactly \(c_j^2\) such edges. Thus
\[
c_j^2=[t^j]\bigl(C_\lambda(t)-C_{\lambda^{<j}}(t)\bigr)\quad(j\ge2).
\]
For \(j=1\), \([t]C_\lambda(t)=c_1^2\). Starting at \(j=1\), these identities determine \(c_1,c_2,\ldots\) successively: \(\lambda^{<j}\) is determined by the already recovered \(c_1,\ldots,c_{j-1}\). Choose the nonnegative integer square root at each stage. Once \(c_j=0\), all further counts vanish. The number of chains of length exactly \(j\) is \(c_j-c_{j+1}\), recovering \(\lambda\) and \(|X|=\sum_j c_j\). Equal polynomials therefore force equal chain partitions; the converse follows from the matching formula. QED.

## Verification
The accompanying standalone `verify.py` directly enumerates partial injections and checks commutation independently of the matching formula for every integer partition of \(0\le n\le6\), comparing each rank coefficient. It also checks the coefficient-recovery identities for all partitions of \(1\le n\le7\). Its final success marker is `ALL_NILPOTENT_CENTRALIZER_RANK_CHECKS_PASSED 18348`. These computations are finite corroboration; the proof above is uniform in \(n\).

## Relationship to prior work
The chain/cycle decomposition and the commuting-map characterization are classical. Araújo, Bentz and Konieczny (2012), Proposition 2.2, explicitly identifies initial-chain to terminal-chain maps; it is the established input, not a new classification. Konieczny (2013, 2020) studies centralizers and their Green structure; the present claim is specifically that the *single polynomial of centralizer element ranks* is a complete invariant among nilpotent partial injections, with a coefficientwise reconstruction. The 2020 article's full text was not accessible during this comparison, so potential implicit or explicit prior recognition of the reconstruction remains a priority risk.

## Limitations
The rigidity statement is restricted to nilpotent elements; it is not asserted for maps with cycles. It is not claimed that the basic commuting criterion or general rook-polynomial machinery is new. Published works not accessible in full may contain equivalent centralizer-rank invariants. No independent validation has occurred.

## References
- J. Araújo, W. Bentz, J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664 (first public 2012-05-08), especially Proposition 2.2; https://arxiv.org/pdf/1205.1664.
- J. Konieczny, *Centralisers in the Infinite Symmetric Inverse Semigroup*, Bull. Austral. Math. Soc. 87 (2013), 462–479, doi:10.1017/S0004972712000779.
- J. Konieczny, *The structure of centralizers in the finite symmetric inverse semigroup*, Comm. Algebra 48 (2020), 5181–5194, online 2020-07-07, doi:10.1080/00927872.2020.1782926.
