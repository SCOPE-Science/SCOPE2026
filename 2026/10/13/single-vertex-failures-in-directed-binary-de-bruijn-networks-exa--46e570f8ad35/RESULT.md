# Single-vertex failures in directed binary de Bruijn networks: exact cuts and finite fault diameters

## Finding

Let \(B_k\) be the **directed** binary de Bruijn digraph on all words in \(\{0,1\}^k\), with an arc \(x_1\cdots x_k\to x_2\cdots x_kb\) for each \(b\in\{0,1\}\). Loops are retained. For a vertex \(v\), delete \(v\) and its incident arcs, obtaining \(B_k-v\). Let \(\delta_k(v)\) be the directed diameter of the induced survivor digraph when it is strongly connected, and \(\infty\) otherwise.

**Theorem (all orders).** For every integer \(k\ge2\), the exceptional deletion set is exactly
\[
E_k=\{0^{k-1}1,\ 01^{k-1},\ 10^{k-1},\ 1^{k-1}0\}.
\]
The digraph \(B_k-v\) fails to be strongly connected precisely for \(v\in E_k\). Each such failure leaves exactly three strongly connected components, of sizes \(1,1,2^k-3\). For \(k=2\), the four displayed descriptions yield two **distinct** words; for \(k\ge3\), all four are distinct. For every \(k\ge2\), failure of either constant vertex \(0^k\) or \(1^k\) retains diameter exactly \(k\).

**Exact finite-window diameter profile.** For every \(2\le k\le10\), define \(H_k(d)=|\{v:\delta_k(v)=d\}|\). The complete profiles, writing `inf` for disconnection, are:

| \(k\) | \(H_k(\infty)\) | finite diameter : multiplicity |
| --- | ---: | --- |
| 2 | 2 | 2:2 |
| 3 | 4 | 3:2, 4:2 |
| 4 | 4 | 4:2, 5:2, 6:8 |
| 5 | 4 | 5:2, 6:10, 7:12, 8:4 |
| 6 | 4 | 6:2, 7:16, 8:42 |
| 7 | 4 | 7:2, 8:50, 9:64, 10:8 |
| 8 | 4 | 8:2, 9:104, 10:142, 11:4 |
| 9 | 4 | 9:2, 10:234, 11:264, 12:8 |
| 10 | 4 | 10:2, 11:496, 12:518, 13:4 |

Thus worst **surviving** fault diameter first reaches an overhead of three at \(k=5\), then drops to overhead two at \(k=6\); the worst-diameter function and the diameter overhead must not be confused. At \(k=5\) exactly four failed vertices attain diameter eight: `00101`, `01011`, `10100`, and `11010`. These are finite assertions only; no extrapolation of the table beyond \(k=10\) is claimed.

## Assumptions and scope

Vertices are **indexed** binary words, not rotation classes. Paths follow **forward shifts only**; no reverse edges, undirected edges, replacement routing overlays, or edge faults are included. Directed distance is the length of a shortest forward directed path, with loops irrelevant to shortest paths between distinct vertices. Diameter is the maximum over all ordered surviving vertex pairs; it is set to \(\infty\) if any ordered pair is unreachable. The infinite structural statement begins at \(k=2\); the exhaustive finite statement has precisely the range stated above. MSC2020 subject: 68M10 (interconnection networks).

## Proof

### 1. Access to constant hubs

Write \(z=0^k\) and \(o=1^k\). Given any surviving word \(x\), appending \(k\) zeros produces a walk from \(x\) to \(z\); every vertex after the initial one ends in zero. Appending \(k\) ones instead produces a walk to \(o\) with every subsequent vertex ending in one. Since the failed word has only one last bit, at least one of those two walks avoids it, provided its endpoint survives. Similarly, from \(z\) to any target \(y\), appending the bits of \(y\) generates intermediate words beginning in zero; from \(o\) to \(y\), the corresponding intermediates begin in one. At least one such route avoids the failure. These observations apply when both hubs survive.

If \(v=z\), every surviving word reaches \(o\) by appending \(k\) ones, and \(o\) reaches every surviving word by appending that word: the intermediate vertices begin with one, while the failed word is all zero. Thus \(B_k-z\) is strongly connected. The complementary argument handles \(v=o\).

### 2. Mutual hub connectivity and the exceptional set

Assume neither constant hub was deleted. There are two explicit forward routes from \(z\) to \(o\). The first appends \(1^k\). Its nonconstant internal vertices are precisely \(0^{k-i}1^i\) for \(1\le i<k\). The second appends \(10\) followed by \(1^k\). After repeated-state/loop trimming if necessary, it is also a walk from \(z\) to \(o\). The common **internal** vertices of these two walks are exactly \(0^{k-1}1\) and \(01^{k-1}\) (coinciding when \(k=2\)). Consequently, deletion of a vertex other than these two leaves at least one route from \(z\) to \(o\). Complementing bits yields two routes from \(o\) to \(z\), whose common internal vertices are \(1^{k-1}0\) and \(10^{k-1}\).

If \(v\notin E_k\), both hub-to-hub directions survive. The hub-access observations in Part 1 then connect any surviving source to any surviving destination through the two mutually reachable hubs. Hence no other deleted vertex is a strong articulation point.

### 3. Three-component decomposition at a cut

Take \(v=0^{k-1}1\). Among survivors, \(z=0^k\) has no outgoing arc except its loop, and \(t=10^{k-1}\) can move only to \(z\) (its other outgoing arc goes to the deleted vertex). These are distinct singleton strongly connected components. Put \(R=\{0,1\}^k\setminus\{v,z,t\}\).

For any \(x\in R\), appending ones until reaching \(o\) never visits \(v\). Indeed, a visit to \(v=0^{k-1}1\) while appending ones requires that the current state immediately before the **first** appended one ends in \(k-1\) zeros. The only two such length-\(k\) initial states are \(z\) and \(t\), both excluded from \(R\); after one appended one, the newly appended run contains no zeros. Conversely, from \(o\), appending any \(y\in R\) yields a path to \(y\) avoiding \(v\): before the last step each vertex starts in one, whereas \(v\) starts in zero, and the last vertex \(y\) is not deleted. Thus all of \(R\) is one strongly connected component, of size \(2^k-3\). The two singletons have no return route to \(R\), so the component partition is exact. Complementing all bits and reversing words (the latter reverses every arc) transfer the partition to the other members of \(E_k\). This proves the structural claim for every \(k\ge2\).

### 4. Constant-hub failure costs no additional hops

Suppose \(v=z\). Given surviving words \(x,y\), the usual route appending the whole of \(y\) reaches \(y\) from \(x\) in exactly \(k\) shifts. If it avoids \(z\), the desired distance bound follows. Otherwise let \(a\) be the length of the maximal terminal zero-run of \(x\), and \(b\) the length of the maximal initial zero-run of \(y\). Because neither word is zero, \(a,b\le k-1\). Encountering \(z\) on the length-\(k\) route forces \(a+b\ge k\), so \(r=\min(a,b)\ge1\). The suffix of \(x\) and prefix of \(y\) then agree on their \(r\) zeros: appending only the last \(k-r\) bits of \(y\) gives a shorter route. If \(a\ge b\), its first appended bit is one; if \(a<b\), the rightmost original one in \(x\) remains in the sliding window until the first one from \(y\) enters (because \(b<k\)). In either case no state on this shorter route equals \(z\). Thus \(\delta_k(z)\le k\).

For the reverse inequality, the surviving ordered pair \(x=1^k\), \(y=0^{k-1}1\) has no nonempty suffix/prefix overlap, hence cannot be connected in fewer than \(k\) shifts. Its direct length-\(k\) path avoids \(z\), proving \(\delta_k(z)=k\). Complementation establishes \(\delta_k(o)=k\).

### 5. Exhaustive finite profile

For each stated \(k\), the program `verify_fault_profile.cpp` constructs every one of the \(2^k\) deleted-vertex instances. For each instance it runs ordinary queue-based shortest-path search from **every** surviving source. If any target is unreachable, the deletion is classified as infinite diameter. Otherwise it takes the maximum of all attained distances. This enumerates all ordered source-target pairs in all deletions, not a sample, and asserts equality to every table entry.

The separately written `verify_scc_independent.py` constructs the adjacency relation directly using string operations, finds strong components by two-pass depth-first search, and independently checks every ordered-pair diameter for \(2\le k\le7\). It also checks the exceptional-set and component-size formulas throughout its range. Both methods have finite, explicit ranges. The infinite proofs are Parts 1–4, not the programs.

## Verification

Compile and run `verify_fault_profile.cpp` using `g++ -std=c++17 -O3 verify_fault_profile.cpp -o verify_fault_profile && ./verify_fault_profile`. The program exits unsuccessfully on any histogram mismatch and prints `PROFILE_VERIFIED` on success. Run `python3 verify_scc_independent.py` for the independent string-graph reachability and SCC check; it ends with `INDEPENDENT_VERIFIED`. Both were executed from standalone source files, with the reported outcomes reproduced from the actual package files.

## Relationship to prior work

It is classical that \(B_k\) has diameter \(k\) and vertex-strong-connectivity one in the binary case; neither statement is new. Bang-Jensen and Gutin [1, §4.6] explicitly derive the general alphabet connectivity bound. Muñoz and Gómez [2, §3] prove internally disjoint-route properties and discuss fault-tolerant constructed networks, but their displayed corollary does not classify the **one-vertex-deleted directed binary graph** or enumerate its exact survivor diameters. Loguinov and collaborators [3, §VI] explain resilience limitations caused by weak self-loop vertices but do not, in the inspected section, provide these component partitions and fault histograms. Mao and Yang [4] investigate an **undirected** binary de Bruijn routing network, which does not imply results for ordered-pair forward-shift distances. Padró, Morillo and Muñoz [5] study the diameter of a **surviving route digraph** with replacement arcs for predetermined routes, rather than the induced survivor graph considered here.

## Limitations

The exact diameter distribution is established only for \(2\le k\le10\); neither a general closed form nor an eventual law for maximum survivor diameter is proved. The finite claim uses reproducible exhaustive integer algorithms rather than a closed-form symbolic derivation of every count. Historical literature on generalized de Bruijn digraph connectivity [6] and possible unpublished routing tables remains a bibliographic risk: its full text could not be inspected; the accessible abstract alone cannot certify noncoverage. The statements apply to directed binary graphs with loops, not undirected, loop-rewired, multi-vertex-failure, or larger-alphabet networks.

## References

1. J. Bang-Jensen and G. Gutin, *Digraphs: Theory, Algorithms and Applications*, 2nd edition, Springer (2008), §4.6, pp. 187–190. Public full-text PDF: https://www.cs.rhul.ac.uk/books/dbook/mainNP.pdf
2. X. Muñoz and J. Gómez, “Asymptotically Optimal \((\Delta,D',s)\)-Digraphs,” *Ars Combinatoria* **49** (1998), 97–111, esp. §3 and Corollary 1. https://combinatorialpress.com/article/ars/Volume%20049/volume-49-paper-9.pdf
3. D. Loguinov et al., “Graph-Theoretic Analysis of Structured Peer-to-Peer Systems: Routing Distances and Fault Resilience,” *IEEE/ACM Transactions on Networking* **13** (2005), §VI. https://irl.cs.tamu.edu/people/dmitri/papers/ton2005.pdf
4. J.-W. Mao and C.-B. Yang, “Shortest path routing and fault-tolerant routing on de Bruijn networks,” *Networks* **35** (2000), 207–215, DOI: 10.1002/(SICI)1097-0037(200005)35:3<207::AID-NET4>3.0.CO;2-F (official first-online date 2000-04-12).
5. C. Padró, P. Morillo and X. Muñoz, “Fault-Tolerant Fixed Routings in Some Families of Digraphs,” *SIAM Journal on Discrete Mathematics* **11** (1998), 501–509, DOI: 10.1137/S0895480195280940.
6. D. Z. Du and F. K. Hwang, “Generalized de Bruijn digraphs,” *Networks* **18** (1988), 27–38, DOI: 10.1002/net.3230180105 (full text not obtained).
