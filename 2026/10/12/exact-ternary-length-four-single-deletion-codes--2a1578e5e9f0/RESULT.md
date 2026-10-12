# Exact ternary length-four single-deletion codes
## Finding
For ternary length-four single-deletion-correcting codes \(C\subseteq\{0,1,2\}^4\), the exact maximum is \(|C|=11\), and exactly six labeled codes attain equality. Every maximum contains
\[
K=\{aabb:a,b\in\{0,1,2\}\}.
\]
Its other two words are the endpoints of one edge of the six-cycle
\[
0120-1021-2012-0210-1201-2102-0120.
\]
Conversely, adjoining the endpoints of any one of these six edges to \(K\) gives a single-deletion-correcting code of size \(11\). Under simultaneous alphabet permutations and reversal of all words, the resulting order-\(12\) symmetry group is transitive on the six maxima; a maximum has stabilizer order \(2\).

## Assumptions and scope
The alphabet is exactly \(\{0,1,2\}\), codewords have length exactly \(4\), and the channel makes exactly one deletion at an arbitrary position. For a word \(w\), let \(D(w)\) be the set of distinct length-three words obtained by deleting one coordinate. A code is single-deletion-correcting exactly when \(D(u)\cap D(v)=\varnothing\) for all distinct \(u,v\in C\). No claim is made for other alphabet sizes, other block lengths, or multiple deletions.

## Proof
Build a graph on all \(3^4=81\) words, joining two distinct words exactly when their one-deletion sets are disjoint. Single-deletion-correcting codes are exactly cliques of this graph.

The supplied verifier performs two exact exhaustive searches on this graph. First, Bron--Kerbosch enumeration visits every maximal clique and finds \(306490\) maximal cliques, with size distribution \(60,15712,142824,126546,20292,1050,6\) at sizes \(5,6,7,8,9,10,11\), respectively. Hence the largest size found is \(11\), attained six times. Second, an independent increasing-vertex clique recursion counts exactly six \(11\)-cliques and zero \(12\)-cliques. Since every clique of size greater than \(12\) contains a \(12\)-clique, this independently certifies the upper bound \(|C|\le11\).

Intersecting the six maxima gives exactly the nine words \(aabb\). Their union outside this core consists exactly of the six words \((a,b,c,a)\) with \(a,b,c\) pairwise distinct. The compatibility edges among these six words form exactly the displayed six-cycle, and the two noncore words of each maximum form one cycle edge. This proves the structural classification.

Finally, the verifier enumerates all six alphabet permutations and both choices of reversal. The resulting \(12\) maps send the six maxima to themselves transitively. A representative has orbit size \(6\), hence stabilizer order \(12/6=2\); the stabilizer is also checked directly.

## Verification
Run `python verify.py` using a standard Python 3 interpreter. The program reconstructs all \(81\) words and deletion sets from definitions, performs both exhaustive clique searches, checks the core and six-cycle description, exhausts the order-\(12\) symmetry group, and hashes the sorted census. The expected census SHA-256 is `0fdfab77f115f24f9c37c8cf153819f8d380b7e269ae7be3a039a018133a0a16`.

The two exhaustive routes have different terminal conditions: one enumerates all maximal cliques, while the other directly counts cliques of sizes \(11\) and \(12\). Both use the same independently reconstructed compatibility relation, so they jointly check the finite extremal statement without treating a partial search or timeout as a proof.

## Relationship to prior work
Kim, Lee, and Oh study exactly length-four single-deletion codes and prove a sharp formula when the alphabet size is even. Their full preprint states that for odd alphabet size their bound coincides with Levenshtein's bound, is not sharp, and that obtaining a sharp odd-alphabet bound appears difficult. For the present smallest odd nonbinary alphabet, that bound gives \(N(4,3,1)\le12\), while the finding above proves the exact value \(11\) and classifies all equality cases.

Kulkarni and Kiyavash define the same deletion-set model for general \(q\) and \(n\) and prove the nonasymptotic bound
\[
|C|\le \frac{q^n-q}{(q-1)(n-1)}.
\]
At \((q,n)=(3,4)\) this gives \(|C|\le13\), so it does not imply the exact value or the equality classification here. Searches under the aliases single-deletion code, deletion-set packing, edit-distance code, and \(N(4,3,1)\), together with comparison against the closest exact length-four result for alphabet size five, found no statement implying the six-code census or its symmetry classification.

## Limitations
The originality conclusion is literature-based rather than a proof of bibliographic uniqueness. An obscure or unindexed enumeration of the ternary length-four case could exist. The scientific theorem itself is finite and exact; its proof does not depend on heuristic search. The result does not extend the exact formula to general odd alphabet size.

## References
1. H. K. Kim, J. Y. Lee, and D. Y. Oh, *Construction of optimal codes in deletion and insertion metric*, arXiv:1003.4057v1, 2010. Published as *Optimal Single Deletion Correcting Code of Length Four Over an Alphabet of Even Size*, IEEE Transactions on Information Theory 56(7), 3217--3220.
2. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128v1, 2012; IEEE Transactions on Information Theory 59(8), 5115--5130.
