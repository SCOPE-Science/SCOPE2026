# The unique transposition extremizers of near-full-radius permutation Hamming balls

## Finding

For every integer \(n\ge5\), let \(S_n\) be the permutations of \(\{1,\ldots,n\}\), let \(d_H\) be Hamming distance, and let \(B_{n-1}(\pi)=\{\rho\in S_n:d_H(\rho,\pi)\le n-1\}\). Define the largest two-center ambiguity
\[
N(n,n-1)=\max_{\pi\ne\tau}|B_{n-1}(\pi)\cap B_{n-1}(\tau)|.
\]
Writing \(D_m\) for the number of derangements of \(m\) symbols, with \(D_0=1\), \(D_1=0\) and \(D_m=(m-1)(D_{m-1}+D_{m-2})\), the exact result is
\[
\boxed{N(n,n-1)=n!-D_n-2D_{n-1}-D_{n-2}\qquad(n\ge5).}
\]
**Moreover, the maximizing pairs are exactly those whose relative permutation is a transposition:** equality holds if and only if \(d_H(\pi,\tau)=2\). The uniqueness of the extremizing center-distance is sharp: at \(n=4\), transposition and double-transposition relative types tie, whereas at \(n=3\) a three-cycle is better.

## Assumptions and scope

Permutations are bijections on \(\{1,\ldots,n\}\). The Hamming distance counts coordinates at which two permutations disagree. A ball of radius \(n-1\) therefore contains all permutations agreeing with its center at least once. The maximum ranges over *distinct* centers with no prescribed mutual distance, as in permutation sequence reconstruction. Every assertion in the boxed theorem holds for every integer \(n\ge5\), without an upper-length restriction. No statement is made for other radii.

## Proof

By left multiplication, the Hamming-ball intersection for centers \(\pi,\tau\) equals that for \(e,\sigma\), where \(\sigma=\pi^{-1}\tau\ne e\). Let \(\mathcal D_n\) be the set of derangements, so \(|\mathcal D_n|=D_n\). The complement of \(B_{n-1}(e)\) is \(\mathcal D_n\), and the complement of \(B_{n-1}(\sigma)\) has the same size. Hence, with
\[
Q(\sigma)=|\{\rho\in S_n:\rho(i)\ne i\text{ and }\rho(i)\ne\sigma(i)\text{ for every }i\}|,
\]
inclusion-exclusion gives
\[
|B_{n-1}(e)\cap B_{n-1}(\sigma)|=n!-2D_n+Q(\sigma). \tag{1}
\]
For each point \(i\) moved by \(\sigma\), let \(E_i=\{\rho\in\mathcal D_n:\rho(i)=\sigma(i)\}\). In the bijection matrix for \(\rho\), imposing a prescribed off-diagonal edge deletes its row and column, leaving an \((n-1)\)-by-\((n-1)\) permutation problem with exactly \(n-2\) independent prohibited diagonal cells. More generally, if \(m\) rows and columns remain and exactly \(m-j\) disjoint row-column cells are forbidden, then
\[
R(m,j)=\sum_{t=0}^{m-j}(-1)^t\binom{m-j}{t}(m-t)!=\sum_{t=0}^j\binom jt D_{m-t}. \tag{2}
\]
The first equality is ordinary inclusion-exclusion; the second follows by adjoining \(j\) unrestricted diagonal cells and partitioning according to which of them are fixed. In particular, every \(E_i\) has the same size
\[
U=R(n-1,1)=D_{n-1}+D_{n-2}. \tag{3}
\]
For distinct moved points \(i,j\), the prescribed off-diagonal edges \(i\to\sigma(i)\) and \(j\to\sigma(j)\) have different tails and different heads. Their union uses exactly \(2\), \(3\), or \(4\) distinct symbols. Deleting both rows and columns leaves respectively \(n-2\), \(n-3\), or \(n-4\) prohibited diagonal cells. By (2) the intersection sizes are, respectively,
\[
|E_i\cap E_j|\in\{D_{n-2},\ D_{n-2}+D_{n-3},\ D_{n-2}+2D_{n-3}+D_{n-4}\}. \tag{4}
\]
Thus each pairwise intersection is at most
\[
V=D_{n-2}+2D_{n-3}+D_{n-4}. \tag{5}
\]
If \(\sigma\) is a transposition, its moved set is \(\{a,b\}\), the two prescribed edges form a two-cycle, and \(|E_a\cap E_b|=D_{n-2}\). Inclusion-exclusion within \(\mathcal D_n\) yields
\[
Q(\sigma)=D_n-2U+D_{n-2},
\]
which substituted into (1) gives the claimed formula for such centers.

It remains to rule out all other relative permutations. Every nonidentity permutation that is not a transposition moves at least three points. Choose any three distinct moved points \(i,j,k\). Since avoiding *all* events \(E_s\) implies avoiding these three, the second Bonferroni inequality, (3) and (5) give
\[
Q(\sigma)\le D_n-\left(3U-|E_i\cap E_j|-|E_i\cap E_k|-|E_j\cap E_k|\right)\le D_n-3U+3V. \tag{6}
\]
The corresponding transposition value exceeds this upper bound by at least
\[
\Delta_n=U-3V+D_{n-2}=D_{n-1}-D_{n-2}-6D_{n-3}-3D_{n-4}. \tag{7}
\]
For \(n=5,6,7\), these differences are respectively \(1,20,161\). For \(n\ge8\), the derangement recurrence turns (7) into
\[
\Delta_n=(n-3)D_{n-2}+(n-8)D_{n-3}-3D_{n-4}>0, \tag{8}
\]
because \(D_{n-2}\ge D_{n-4}>0\), \(n-3>3\), and \(n-8\ge0\). Hence \(Q(\sigma)<Q(\text{transposition})\) for every other nonidentity \(\sigma\). Equation (1) completes the global maximum and equality classification. \(\square\)

## Verification

Two independent standalone Python programs accompany this result. Run `python3 verify_direct.py` to enumerate every cycle type in \(S_n\), for \(3\le n\le8\), and count both-ball intersections by explicit permutation enumeration, with no reliance on the symbolic upper-bound derivation. It reproduces the formula and unique maximizing transposition type at \(5\le n\le8\), and the exceptional small cases. Run `python3 verify_structure.py` for independent brute-force checks of every one-edge and two-edge restriction formula through \(n=8\), positivity of the analytic gap through \(n=100\), and the published benchmark values \(N(9,8)=197864\) and \(N(10,9)=2012014\). Files `direct_output.txt` and `structure_output.txt` record executed outputs. These finite computations corroborate but are not substitutes for the all-length proof above.

## Relationship to prior work

Wang, Fu and Konstantinova (first online October 16, 2024) analyze permutation Hamming-ball intersections by prescribed center distances \(2,3,4\), resolve small fixed radii, and formulate the conjecture that a transposition maximizes the intersection for every admissible radius \(r\ge5\). In particular, prescribed-distance-two counts are prior work, not newly claimed here. Abdollahi and collaborators (first publicly available January 6, 2026) establish that conjecture for fixed \(r=5,6,7\), give a general character-theoretic maximum formula, and tabulate computations for \(8\le r\le14\). The current theorem proves the conjectured global transposition extremality and its strict uniqueness along the unbounded diagonal \(r=n-1\), with an explicit derangement expression and a short three-event argument. Earlier fixed-radius formulas and the finite tabulated diagonal values are thereby recovered, not claimed as independent discoveries. The specific infinite diagonal theorem and strict center-type classification were not found in the inspected full 2026 article or accessible older source excerpts. The predecessor's entire 2024/2025 article could not be inspected, so the possibility of implicit earlier coverage remains a priority risk.

## Limitations

The theorem does not solve the conjecture for arbitrary \(r<n-1\), nor does it classify intersections of nonextremal center pairs. The proof is rigorous for its stated domain; computational verification is finite. Published general character formulas can, in principle, calculate individual cases but do not by themselves imply the infinite family of strict maximizing types. Independent review of the priority comparison and of the mathematical proof has not been performed.

## References

1. A. Abdollahi, J. Bagherian, H. Eskandari, F. Jafari, M. Khatami, F. Parvaresh and R. Sobhani, *The Sequence Reconstruction of Permutations under Hamming Metric with Small Errors*, arXiv:2601.02844v1 (January 6, 2026), https://arxiv.org/html/2601.02844v1. Particularly Conjecture 2.1, Theorem 1.1, Theorem 4.2, and Tables 1–2.
2. X. Wang, F.-W. Fu and E. V. Konstantinova, *The sequence reconstruction of permutations with Hamming metric*, Designs, Codes and Cryptography 93 (2025), 11–37, first online October 16, 2024, DOI:10.1007/s10623-024-01509-4. Only its abstract and publisher preview were accessible.
3. X. Wang and E. V. Konstantinova, *The sequence reconstruction problem for permutations with the Hamming distance*, Cryptography and Communications 16 (2024), 1033–1057, DOI:10.1007/s12095-024-00717-y. Abstract and bibliographic description were compared.
