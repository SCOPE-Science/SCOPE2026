# One-swap isolation of the \(166\)-word \(K_6(8,4)\) covering code
## Finding
Let \(H=\{0,1,2,3,4,5\}^8\) with Hamming distance, and let \(C\subset H\) be the explicit \(166\)-word code published with Marosi's covering-code bounds. The source verifies that \(C\) has covering radius \(4\), hence \(K_6(8,4)\le 166\).

For \(c\in C\), define its private region
\[
P_c=\{x\in H:d(x,c)\le 4\text{ and }d(x,C\setminus\{c\})>4\}.
\]
Every \(P_c\) is nonempty. In fact, \(|P_c|\) ranges from \(8\) to \(105\), and the private regions partition the \(7173\) ambient words having coverage multiplicity exactly \(1\).

Every point of every \(P_c\) has distance exactly \(5\) from its nearest codeword in \(C\setminus\{c\}\). Therefore deleting any single codeword raises the covering radius from \(4\) to exactly \(5\).

A replacement \(y\in H\) restores radius \(4\) after deleting \(c\) if and only if
\[
y\in I_c:=\bigcap_{x\in P_c}B_4(x).
\]
Exact enumeration gives \(I_c=\{c\}\) for \(165\) codewords. The unique exception is
\[
I_{\mathtt{51004501}}
=\{\mathtt{51004501},\mathtt{51004441}\}.
\]
Thus the only nontrivial one-for-one move from this published representative that preserves covering radius \(4\) is
\[
\mathtt{51004501}\longmapsto\mathtt{51004441}.
\]

## Assumptions and scope
The claim concerns the exact published \(166\)-word representative in the ancillary file `K6_8_4_M166.txt`, viewed in the ordinary \(6\)-ary Hamming space of length \(8\). Hamming isometries carry the statement to isometric copies of this representative.

No claim is made that \(166\) is the exact value of \(K_6(8,4)\), nor that every radius-\(4\), size-\(166\) covering code has the same one-swap neighborhood. The result classifies only single deletion and single replacement moves for this explicit code.

## Proof
For each \(z\in H\), let
\[
m(z)=|\{c\in C:d(z,c)\le4\}|.
\]
The checker generates every Hamming ball \(B_4(c)\) exactly. Since
\[
|B_4(c)|=\sum_{j=0}^4\binom{8}{j}5^j=51491,
\]
the complete incidence enumeration contains \(166\cdot51491=8547506\) codeword--ambient-word incidences. Accumulating these incidences over all \(6^8=1679616\) ambient words gives \(m(z)\ge1\) everywhere, independently reproducing covering radius at most \(4\). The exact multiplicity-one count is \(7173\).

For a fixed \(c\), the words that become uncovered when \(c\) is deleted are exactly those with \(m(z)=1\) lying in \(B_4(c)\); these are precisely \(P_c\). Exhaustive distance comparison of each private word with the other \(165\) codewords gives second-nearest distance \(5\) in every case. Hence \(C\setminus\{c\}\) has covering radius exactly \(5\) for every \(c\in C\).

Now delete \(c\) and insert a word \(y\). All points outside \(P_c\) retain some radius-\(4\) cover, so the modified code covers \(H\) with radius \(4\) exactly when \(d(y,x)\le4\) for every \(x\in P_c\). This is equivalent to \(y\in I_c\).

To compute \(I_c\) exhaustively, choose any \(p\in P_c\). Since \(I_c\subseteq B_4(p)\), it suffices to enumerate the \(51491\) words in \(B_4(p)\) and retain those within distance \(4\) of every point of \(P_c\). Performing this exact intersection for all \(166\) private regions yields \(165\) singleton intersections and one two-element intersection, exactly as stated. A final direct coverage recount verifies the exceptional replacement.

## Verification
Run `python3 artifacts/verify.py`. The verifier uses integer Hamming distances only and enumerates the complete ambient space through exact Hamming-ball incidence lists. It checks the full coverage-multiplicity histogram, every private region, every deletion radius, every one-word repair intersection, and the exceptional replacement. Its terminal line is `VERIFY_OK`.

The exact coverage-multiplicity histogram is
\[
(7173,53598,184112,358580,434466,348893,192658,74593,20757,4099,606,79,2)
\]
for multiplicities \(1,2,\ldots,13\), respectively.

## Relationship to prior work
Marosi's source establishes the record upper bound and publishes the exact code. Its search method explicitly uses private coverage in remove-and-repair descent, so single-deletion sensitivity is mathematically tied to the construction method. The inspected source text and repository describe private-coverage scoring and local search but do not state the exact private-region census, the all-deletions radius-\(5\) property, or the complete one-for-one replacement classification above.

The arXiv version first public on August 20, 2026 reported \(K_6(8,4)\le167\). The repository commit dated August 21, 2026 introduced the \(166\)-word code analyzed here. Searches of indexed mathematical records and the public source tree for this parameter set, private coverage, single-word replacement, exchange rigidity, and local optimality returned no statement implying this classification.

## Limitations
This is a finite structural theorem about one explicit covering code. It does not prove global optimality of size \(166\), classify multiword exchanges, or determine the full isometry group. The one-swap classification is exhaustive only for replacing exactly one deleted codeword by exactly one ambient word.

Novelty searches cannot logically prove absence from all literature. The residual originality risk is therefore that an unindexed source may have computed the same local exchange neighborhood without using the terminology searched here.

## References
1. Mark Marosi, *New upper and lower bounds on covering codes \(K_q(n,R)\) for alphabets of size \(5\le q\le21\)*, arXiv:2608.19872 and subsequent public source revisions.
2. Public ancillary record `cov/results/K6_8_4_M166.txt`, introduced in repository commit `8a7947b3e3f5e57779ef0c36c63440843f894cbc` on 2026-08-21.
