# Exact two-helper repair-availability spectra for three-subspace punctured binary simplex codes

## Finding

Delete the nonzero points of three pairwise disjoint, equal-dimensional linear subspaces from a binary simplex generator matrix. For every surviving coordinate, the number of pairwise disjoint two-coordinate repair alternatives takes at most four consecutive values. Its **complete coordinate-frequency distribution** depends only on the dimension of the span of the three removed subspaces, not on their individual position.

Let \(V=\mathbb F_2^k\), and let \(U_1,U_2,U_3\le V\) each have dimension \(u\ge2\) and satisfy \(U_i\cap U_j=\{0\}\) for distinct indices. Require \(2^{k-1}>3(2^u-1)\). Form the binary code \(C\) whose generator columns, appearing exactly once each, are the elements of
\[
S=V\setminus (U_1\cup U_2\cup U_3).
\]
The zero vector does not belong to \(S\). Put
\[
\rho=3u-\dim(U_1+U_2+U_3),\quad t=u-\rho,\quad B=2^{k-1}-1-3(2^u-1).
\]
Then \(0\le\rho\le u\). For each \(v\in S\), let \(a(v)\) count all unordered pairs of *other* surviving columns \(\{x,y\}\subset S\setminus\{v\}\) satisfying \(x+y=v\). These pairs are automatically mutually disjoint as sets of helpers. Thus \(a(v)\) is the maximal number of disjoint two-helper recovery sets for coordinate \(v\).

**Theorem.** For \(j=0,1,2,3\), the number \(N_j=|\{v\in S:a(v)=B+j\}|\) equals
\[
\begin{aligned}
N_0&=2^k-2^{3u-\rho}+2^{2\rho}(2^t-1)^3,\\
N_1&=3\,2^{2\rho}(2^t-1)^2,\\
N_2&=3\,2^\rho(2^\rho-1)(2^t-1),\\
N_3&=(2^\rho-1)(2^\rho-2).
\end{aligned}
\]
Zero populations are allowed, and the four populations sum to the blocklength \(2^k-1-3(2^u-1)\). In particular, for \(k=5,u=2\), the two possible values \(\rho=1,2\) give the same optimal parameters \([22,5,10]_2\) but distinct availability histograms:
\[
\rho=1:\ \{6:4,\ 7:12,\ 8:6\};\qquad
\rho=2:\ \{6:16,\ 9:6\}.
\]
This proves these two codes are not permutation equivalent, despite equal length, dimension and minimum distance.

## Assumptions and scope

The code is over \(\mathbb F_2\), not a general \(q\)-ary field; the three deleted subspaces have the same dimension and pairwise trivial intersections, but need **not** form a direct sum. The dimension parameter \(\rho\) distinguishes the possible triple-span geometries. The inequality on \(k,u\) guarantees the surviving vectors span \(V\) and ensures the construction has the stated dimension. Only repair sets of cardinality exactly two are counted, without using larger repair sets, simultaneously lost helpers, or constrained helper availability.

Each code is an \([n,k,d]_2\) code with
\[
n=2^k-1-3(2^u-1),\qquad d=2^{k-1}-3\cdot2^{u-1},
\]
and is distance-optimal within the class of binary linear \([n,k]_2\) codes by the Griesmer criterion. The code-parameter construction and its distance-optimality are from Wang, Chen and Wu (2026); they are **not** claimed as new. The new claim is the exact coordinatewise two-helper repair spectrum, including non-direct-sum triples, and its structural classification.

## Proof

**1. Exact helper-pair identity.** Set \(D=U_1\cup U_2\cup U_3\). Since the three intersections are \(\{0\}\), we have \(|D|=1+3(2^u-1)\) and \(S=V\setminus D\). For fixed \(v\in S\), the pairs \(\{x,x+v\}\) with \(x\in S\) are automatically disjoint: translation by nonzero \(v\) partitions \(V\) into two-element orbits. Therefore
\[
a(v)=\frac12|S\cap(v+S)|
=2^{k-1}-|D|+\frac12|D\cap(v+D)|.
\]
Because \(v\notin D\), the identity \(x+y=v\) with \(x,y\in D\) is possible only with nonzero \(x,y\) from *different* deleted subspaces. For each unordered pair \(i<j\), such a pair exists exactly when \(v\in U_i+U_j\), and then it is unique: the sum map from \(U_i\times U_j\) is bijective onto \(U_i+U_j\). A pair cannot be counted for two choices of \(i,j\), as the removed subspaces have no common nonzero points. Consequently
\[
\tfrac12|D\cap(v+D)|
=J(v):=\sum_{1\le i<j\le3}\mathbf1_{\{v\in U_i+U_j\}},
\qquad a(v)=B+J(v).
\]

**2. Normal form and the three tests.** Write \(W=U_1\oplus U_2\) and \(T=U_3\cap W\). The restrictions to \(T\) of the two projections \(W\to U_i\) are injective: a vector of \(T\) having one zero projection would lie in \(U_3\cap U_j=\{0\}\). Hence \(\dim T=\rho\le u\), and bases can be selected such that
\[
\begin{aligned}
U_1&=\langle a_1,\ldots,a_u\rangle,\quad
U_2=\langle b_1,\ldots,b_u\rangle,\\
U_3&=\langle a_1+b_1,\ldots,a_\rho+b_\rho,c_1,\ldots,c_t\rangle,
\end{aligned}
\]
where \(t=u-\rho\), the \(c_i\) are independent modulo \(W\), and these displayed vectors span \(H=U_1+U_2+U_3\), of dimension \(3u-\rho=2\rho+3t\). The coordinates of a vector in \(H\) split into two unrestricted \(\rho\)-blocks and three \(t\)-blocks, denoted \(a_{\rm tail},b_{\rm tail},c_{\rm tail}\). Membership in the three pair sums is equivalent respectively to
\[
\begin{array}{c|c}
U_1+U_2&c_{\rm tail}=0\\
U_1+U_3&b_{\rm tail}=0\\
U_2+U_3&a_{\rm tail}=0.
\end{array}
\]
Outside \(H\), all three membership tests fail. Thus the distribution of \(J(v)\), *before* deleting \(D\), has generating polynomial
\[
(2^k-2^{3u-\rho})+2^{2\rho}\bigl((2^t-1)+z\bigr)^3.
\]

**3. Remove deleted vectors.** Inside \(D\), the zero vector contributes once to the class \(J=3\). In each of the three \(U_i\), exactly \(2^\rho-1\) nonzero vectors belong to all three pair sums and exactly \(2^\rho(2^t-1)\) nonzero vectors belong to precisely two pair sums. No element of \(D\) has \(J=0\) or \(J=1\). Subtracting these counts from the preceding generating polynomial gives, successively, the four stated values \(N_0,N_1,N_2,N_3\). The formula is valid for every integer \(\rho\in[0,u]\) for which the configuration fits in \(V\).

**4. Parameters and inequivalence.** The punctured full simplex has dimension \(k\) because \(|S|>2^{k-1}-1\), which is more points than any linear hyperplane contains. Every nonzero linear functional is nonzero at exactly \(2^{k-1}\) points of \(V\), and at either zero or \(2^{u-1}\) points of each deleted subspace. Since \(3<2^u\), some nonzero functional is nonzero on every \(U_i\), giving the claimed minimum distance. Griesmer optimality of these parameters follows from Theorems 2.2–2.3 of Wang, Chen and Wu (2026), or directly by comparing the Griesmer sum at the next distance. For \(k=5,u=2\), both \(\rho=1\) and \(\rho=2\) configurations exist in the given normal form. Substitution into the four formulas gives the two stated histograms, which cannot be equal under a coordinate permutation.

## Verification

The accompanying standalone `verify.py` independently constructs every deleted subspace, enumerates *all* surviving columns and *all* unordered helper pairs for each column, and compares these counts to the theorem. It tests \(36\) configurations (two values of \(u\), feasible \(k,\rho\), and three coordinate representations), including independent invertible coordinate changes. It also enumerates all nonzero message vectors for the two \([22,5,10]_2\) examples. Running `python verify.py` produces the attached `verification_output.txt`, ending in `DISTANCE_EXAMPLES_OK` and `RECOVERY_SPECTRA_OK 36 exact tests`. The general theorem is proved above; finite checks are corroboration only.

## Relationship to prior work

Wang, Chen and Wu (2026, arXiv:2605.11431v1) construct the three-subspace-deleted binary simplex codes (within a general multiple-subspace construction), establish their distance optimality, give weight distributions for direct-sum configurations, and show locality two. They do not state a coordinatewise distribution of maximum disjoint two-helper alternatives. The current theorem allows non-direct-sum triples and separates two optimal codes sharing \([22,5,10]_2\) parameters.

Silberstein and Zeh (2015, arXiv:1501.07114) study optimal punctured-simplex locality constructions, and their 2018 article studies anticode-based high availability; these establish the surrounding area, not a verified copy of the four-level triple-span formula. The full 2018 article could not be inspected, and equivalent implicit coverage remains a specific priority risk. Kim, Song and Song (2018) study different weight-pattern block punctures; Grezet and Hollanti (2020) study one deleted simplex subspace; Kuijper, Lieb and Napp (2025) analyze simplex-related easy repairs and multi-erasure recovery. The readily inspected claims and constructions differ from the present three-deleted-subspace coordinatewise spectrum. This comparison is provisional rather than a guarantee of first discovery.

## Limitations

The result concerns linear binary codes, three equally sized pairwise disjoint removed subspaces, and exactly two surviving helper coordinates. It neither counts repair sets of larger sizes nor determines optimal sequential repair under arbitrary erasure patterns. For \(u\ge2\) the four support levels may collapse because some \(N_j\) vanish. No claim of improving coding rate, distance, or practical decoding complexity is made. Independent review and exhaustive priority verification have not been performed. An inaccessible relevant 2018 full article remains a material literature risk.

## References

1. Y. Wang, H. Chen, X. Wu, *Optimal Codes with Positive Griesmer Defects, Related Optimal and Almost Optimal LRC Codes*, arXiv:2605.11431v1, first posted 2026-05-12, https://arxiv.org/html/2605.11431v1.
2. N. Silberstein, A. Zeh, *Optimal Binary Locally Repairable Codes via Anticodes*, arXiv:1501.07114v1, 2015, https://arxiv.org/pdf/1501.07114.
3. N. Silberstein, A. Zeh, *Anticode-based locally repairable codes with high availability*, Designs, Codes and Cryptography 86 (2018), 419–445, https://doi.org/10.1007/s10623-017-0358-0.
4. J. Kim, W. Song, J. Song, *Block-Punctured Binary Simplex Codes for Local and Parallel Repair in Distributed Storage Systems*, IEEE Transactions on Information Theory, 2018, https://coding.yonsei.ac.kr/publications/international_journal/pdf/57.pdf.
5. C. Grezet, C. Hollanti, *The complete hierarchical locality of the punctured Simplex code*, Designs, Codes and Cryptography (2020), https://doi.org/10.1007/s10623-020-00810-2.
6. M. Kuijper, J. Lieb, D. Napp, *Easy repair via codes with simplex locality*, arXiv:2504.11251v1, 2025, https://arxiv.org/pdf/2504.11251.
