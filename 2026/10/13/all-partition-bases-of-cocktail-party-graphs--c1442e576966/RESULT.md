# All partition bases of cocktail-party graphs
## Finding
For every integer \(n\ge 3\), let \(CP_n=K_{2n}-M_n\), where \(M_n\) is a perfect matching whose deleted edges are \(P_i=\{a_i,b_i\}\) for \(1\le i\le n\). A partition basis means a resolving partition with the minimum possible number of parts.

The partition dimension is
\[
\operatorname{pd}(CP_n)=n+1.
\]
The scalar equality is already contained in the general complete-multipartite theorem of Darmaji, Uttunggadewa, Simanjuntak, and Baskoro. The new statement here is the complete equality-case classification and enumeration.

Every partition basis has exactly one of the following two forms.

**Type I.** There are \(n\) singleton parts and one nonsingleton part of size \(n\). The nonsingleton part contains exactly one endpoint from every deleted matching pair \(P_i\).

**Type II.** There are \(n-1\) singleton parts and two nonsingleton parts. There is a unique index \(r\) such that neither endpoint of \(P_r\) is singleton; the two endpoints of \(P_r\) lie in different nonsingleton parts. For every \(i\ne r\), exactly one endpoint of \(P_i\) is singleton and its mate lies in one of the two nonsingleton parts. Each nonsingleton part receives at least one such mate in addition to its endpoint of \(P_r\).

Thus the number of partition bases when the blocks themselves are regarded as unordered is
\[
B_n=2^n+n2^{n-1}\bigl(2^{n-1}-2\bigr).
\]
If an ordered list of the \(n+1\) blocks is counted separately, the number is \((n+1)!B_n\).

## Assumptions and scope
Graphs are finite, simple, and connected. The result concerns \(CP_n\) for \(n\ge3\). For a partition \(\Pi=\{Q_1,\ldots,Q_k\}\), the coordinate of a vertex \(v\) at \(Q_j\) is \(d(v,Q_j)=\min_{x\in Q_j}d(v,x)\). The partition resolves the graph when all distance vectors are distinct. The count \(B_n\) treats the collection of blocks as unordered, because permuting coordinates does not change the underlying resolving partition; the ordered count is stated separately.

## Proof
Write \(m(v)\) for the unique nonneighbor of a vertex \(v\), namely its partner in the deleted perfect matching. Distinct nonmatched vertices are adjacent, so for a part \(Q\) not containing \(v\),
\[
d(v,Q)=2
\]
if and only if \(Q=\{m(v)\}\); otherwise \(d(v,Q)=1\).

Consider two distinct vertices \(u,v\) lying in the same partition part \(C\). Their coordinate at \(C\) is \(0\) for both. For every other part, the preceding observation shows that they have different coordinates exactly when at least one of \(\{m(u)\}\) or \(\{m(v)\}\) is a singleton part. Therefore a partition resolves \(CP_n\) if and only if every nonsingleton part contains at most one vertex whose mate is not itself a singleton part. Vertices in different parts are automatically distinguished by a coordinate equal to \(0\) for one of them.

Let a resolving partition have \(k\) parts, of which \(s\) are singleton. If its nonsingleton parts have sizes \(r_1,\ldots,r_{k-s}\), each such part requires at least \(r_j-1\) vertices whose mates are singleton parts. Since distinct vertices have distinct mates,
\[
s\ge\sum_j(r_j-1)=(2n-s)-(k-s)=2n-k.
\]
As \(s\le k\), this gives \(k\ge n\). Equality \(k=n\) would force \(s=n\), so all \(n\) parts would be singletons and could cover only \(n\) of the \(2n\) vertices. Hence \(k\ge n+1\).

Now set \(k=n+1\). The inequality gives \(s\ge n-1\). Because at least one nonsingleton part is needed, only \(s=n\) or \(s=n-1\) is possible.

If \(s=n\), there is one nonsingleton part of size \(n\). It cannot contain both endpoints of any \(P_i\), because those two vertices would both have nonsingleton mates. Hence it contains exactly one endpoint from every \(P_i\), giving Type I. Conversely every Type I partition satisfies the local criterion above.

If \(s=n-1\), there are two nonsingleton parts with total size \(n+1\). The lower-bound inequality is then tight. Consequently every singleton vertex has its mate in a nonsingleton part, and each nonsingleton part contains exactly one vertex whose mate is nonsingleton. Thus exactly one matching pair \(P_r\) has both endpoints nonsingleton, and its endpoints must be split between the two nonsingleton parts. Every other pair contributes one singleton and its mate to a nonsingleton part. Since both large parts are genuinely nonsingleton, each must receive at least one of these \(n-1\) mates. This is precisely Type II, and the same local criterion proves the converse.

For Type I, choosing the endpoint placed in the large part independently in each \(P_i\) gives \(2^n\) bases. For Type II, choose \(r\) in \(n\) ways and choose the singleton endpoint in every other pair in \(2^{n-1}\) ways. Label the two large parts temporarily by which one contains \(a_r\). The \(n-1\) mates of the singleton vertices may be assigned to these two parts by any nonconstant binary assignment, giving \(2^{n-1}-2\) choices. This labeling is canonical, so it does not overcount unordered blocks. Summing the two types gives the stated \(B_n\).

## Verification
The accompanying `verify.py` independently constructs \(CP_n\), computes partition-distance vectors, exhaustively checks every set partition for \(3\le n\le5\), and compares the resulting minimum bases against the two-type classification. It also generates and checks every classified basis for \(3\le n\le8\). Its replay output is:

`VERIFY_OK exhaustive_n=3..5 partitions_tested=120318 basis_counts=32,208,1152 construction_n=3..8 construction_checks=164400`

The finite computation is a boundary and implementation check; the proof above establishes the result for all \(n\ge3\).

## Relationship to prior work
Chartrand, Salehi, and Zhang introduced partition dimension and resolving partitions. Darmaji, Uttunggadewa, Simanjuntak, and Baskoro proved the partition dimension of every complete multipartite graph. Specializing their theorem to \(K_{2,\ldots,2}\cong CP_n\) gives the already-known scalar equality \(\operatorname{pd}(CP_n)=n+1\). Their full proof supplies a normal-form existence argument and an extremal construction, but does not classify all equality partitions or enumerate them. A later paper by Zafari and Alikhani again states in its abstract that it determines the partition dimension of cocktail-party graphs; only its abstract and metadata were available for inspection here, so the possibility that its inaccessible body contains additional equality-case structure remains a residual literature risk. The present claim is therefore limited to the all-bases classification and exact count, together with an independent proof of the scalar value needed to make the classification self-contained.

## Limitations
The theorem excludes \(n<3\). The enumeration convention must be fixed: \(B_n\) counts unordered blocks, while ordered coordinate lists contribute a factor of \((n+1)!\). The computation checks only finite small orders and is not used as an infinite proof. The full text of the 2026 cocktail-party paper was not available through the public sources inspected, so its abstract-level comparison cannot eliminate the residual possibility that it contains a minimizer classification not advertised in the abstract.

## References
1. G. Chartrand, E. Salehi, and P. Zhang, “The partition dimension of a graph,” *Aequationes Mathematicae* 59 (2000), 45–54. DOI: 10.1007/PL00000127.
2. Darmaji, S. Uttunggadewa, R. Simanjuntak, and E. T. Baskoro, “The partition dimension of a complete multipartite graph, a special caterpillar and a windmill,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 71 (2009), 209–215.
3. A. Zafari and S. Alikhani, “The partition dimension and \(k\)-domination number of two specific graphs,” *Journal of Algebraic Systems* 14(2) (2026), 331–342. DOI: 10.22044/JAS.2024.14317.1816.
