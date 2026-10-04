# Exact preasymptotic profile for \(N(n,3,3)\) in binary deletion reconstruction
## Finding
For a binary word \(x\), let \(\mathcal D_t(x)\) denote the set of distinct subsequences obtained by deleting exactly \(t\) symbols. For equal-length binary words define \(d_L(x,y)\) as the minimum \(s\) for which \(\mathcal D_s(x)\cap\mathcal D_s(y)\neq\varnothing\), and define
\[
N(n,\ell,t)=\max_{x,y\in\{0,1\}^n,\ d_L(x,y)\ge \ell}|\mathcal D_t(x)\cap\mathcal D_t(y)|.
\]
Then, for every integer \(n\ge4\),
\[
N(n,3,3)=
\begin{cases}
2,&n=4,\\
4,&n=5,\\
6,&n=6,\\
8,&n=7,\\
11,&n=8,\\
15,&n=9,\\
20,&n\ge10.
\end{cases}
\]
Thus the known constant diagonal value \(20\) first occurs exactly at \(n=10\); the sufficient threshold \(n\ge4t-2\) from the published diagonal theorem is sharp when \(t=3\).

## Assumptions and scope
The alphabet is binary, the two centers have the same length \(n\), exactly three deletions occur in each channel output, and the admissible center pairs satisfy \(d_L(x,y)\ge3\). The definition is the deletion-reconstruction parameter used by Pham, Goyal, and Kiah. The finite cases here begin at \(n=4\), because the defining regime requires \(t<n\).

The new finite content is the complete preasymptotic segment \(4\le n\le9\). The value \(N(n,3,3)=20\) for \(n\ge10\) is prior work and is included only to state the completed all-length profile and identify the sharp stabilization threshold.

## Proof
For equal-length words, \(d_L(x,y)\ge3\) is equivalent to
\[
\mathcal D_2(x)\cap\mathcal D_2(y)=\varnothing.
\]
Indeed, if a common subsequence can be obtained using at most two deletions from each word, then deleting additional symbols if necessary yields a common length-\(n-2\) subsequence. Conversely, a common member of the two radius-two deletion balls directly gives \(d_L(x,y)\le2\).

Therefore each finite value can be certified without any heuristic distance calculation: enumerate every unordered pair \(\{x,y\}\subset\{0,1\}^n\); retain precisely those pairs with disjoint \(\mathcal D_2\) balls; and maximize \(|\mathcal D_3(x)\cap\mathcal D_3(y)|\). The exhaustive maxima are
\[
2,4,6,8,11,15
\]
for \(n=4,5,6,7,8,9\), respectively. Witness pairs are
\[
\begin{array}{c|c}
n& (x,y)\\ \hline
4&(0001,1110)\\
5&(01110,10001)\\
6&(001110,101001)\\
7&(0011010,1010011)\\
8&(00110101,10100110)\\
9&(010100110,100110101).
\end{array}
\]
The verifier checks all \(174216\) unordered pairs in these six lengths, including an independent longest-common-subsequence equivalence check for the eligibility condition. There are \(94949\) eligible pairs in total.

For the tail, Theorem 4 of Pham--Goyal--Kiah gives, after setting \(k=0\) and \(\ell=t=3\), the universal upper bound
\[
N(n,3,3)\le \binom{6}{3}=20.
\]
Their Proposition 5 and Corollary 6 provide a matching construction whenever \(n\ge4\cdot3-2=10\), hence \(N(n,3,3)=20\) for every \(n\ge10\). The packaged verifier also checks directly that the length-ten construction \(1010101010\) and \(0110011001\) has deletion distance at least three and exactly twenty common three-deletion outputs. Combining the exhaustive short-length certificate with the published tail theorem proves the displayed profile.

## Verification
Run `python3 verify.py`. It regenerates deletion balls from the words themselves, not from stored tables. For every \(4\le n\le9\), it enumerates all \(2^n\) words and every unordered pair, verifies that disjoint radius-two deletion balls agree with the independent longest-common-subsequence test, computes the radius-three intersection, and checks both the exact maximum and an explicit maximizing pair. It then checks the boundary construction at \(n=10\).

A successful replay ends with:

`VERIFY_OK n=4..9 pair_checks=174216 eligible_pairs=94949 maximizing_pairs=20 boundary_n10=20`

The finite computation is exhaustive only for \(4\le n\le9\). The infinite tail is not inferred from computation; it uses the cited all-parameter theorem and construction.

## Relationship to prior work
Pham, Goyal, and Kiah define \(N(n,\ell,t)\), state that before their work exact values were known only for \(\ell\in\{1,2\}\), prove a general upper bound, and prove that on the diagonal \(\ell=t\),
\[
N(n,t,t)=\binom{2t}{t}
\]
for \(n\ge4t-2\). Specializing gives the already-known tail \(N(n,3,3)=20\) for \(n\ge10\). Their paper does not state the six values below that threshold. Gabrys and Yaakobi treat the earlier \(\ell=2\) reconstruction regime. Later list-reconstruction work concerns intersections of three or more distinct deletion balls and is not an implication of the two-center, distance-constrained parameter here.

Targeted searches under exact \(N(n,3,3)\), pairwise three-deletion-ball intersections, shortest-common-supersequence aliases, and the concrete values at \(n=8\) and \(n=9\) located no published table or theorem covering the preasymptotic profile. This negative search is not by itself evidence of originality; the principal evidence is the statement-level gap in the closest full-text source.

## Limitations
This result concerns only the binary diagonal parameter \(\ell=t=3\). It does not give formulas for \(N(n,\ell,t)\) off the diagonal, for larger alphabets, or for multi-center list reconstruction. The preasymptotic part is a finite exhaustive theorem rather than a structural closed-form derivation. A residual originality risk remains that the six short values may appear in an unindexed computation, note, thesis, or supplementary table using different notation.

## References
1. V. L. P. Pham, K. Goyal, and H. M. Kiah, “Sequence Reconstruction Problem for Deletion Channels: A Complete Asymptotic Solution,” arXiv:2111.04255v1, 2021. In particular, Definition (1), Theorem 4, Proposition 5, and Corollary 6.
2. R. Gabrys and E. Yaakobi, “Sequence Reconstruction over the Deletion Channel,” IEEE Transactions on Information Theory 64(4), 2924–2931, 2018, DOI:10.1109/TIT.2018.2800044.
3. F. Zhu, “Sequence Reconstruction over the Deletion Channel,” arXiv:2511.01071, 2025, for the distinct multi-center list-reconstruction variant.
