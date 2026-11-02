# Exact packing five-domatic chromatic numbers of cycles

## Finding
Let \(C_n\) be the simple cycle on \(n\ge5\) labelled vertices. Its packing five-domatic chromatic number is
\[
\chi_{\rho,5}(C_n)=
\begin{cases}
6,&n\in\{5,6\},\\
5,&n\in\{7,8,9,11,12,13,14,18\},\\
4,&n\in\{10,15,16,17\}\text{ or }n\ge19.
\end{cases}
\]
In particular, \(19\) is the sharp eventual four-color cutoff, and there are ten smaller exceptional cycle lengths at which four colors are insufficient.

## Assumptions and scope
For a finite simple graph \(G\), a packing coloring is \(f:V(G)\to\{1,\ldots,t\}\) such that vertices of a common color \(j\) have pairwise distance strictly greater than \(j\). A packing \(5\)-domatic coloring additionally has a partition \(V(G)=A_0\sqcup\cdots\sqcup A_4\) for which every \(A_a\) is a dominating broadcast: for each vertex \(v\) and each \(a\in\{0,1,2,3,4\}\), there is \(u\in A_a\) with \(d_G(u,v)\le f(u)\). The minimum palette size is \(\chi_{\rho,5}(G)\). Every cycle is labelled cyclically by \(\mathbb Z/n\mathbb Z\); indices and distances wrap around. All claims are for integer \(n\ge5\); no assertion is made for fewer than five vertices.

## Proof
**1. Universal four-color lower bound.** Suppose a packing coloring of \(C_n\) uses only colors \(1,2,3\), with \(c_j\) vertices of color \(j\). Separation on the cycle gives \(c_2\le\lfloor n/3\rfloor\) and \(c_3\le\lfloor n/4\rfloor\), hence \(c_1=n-c_2-c_3>c_3\): indeed, \(\lfloor n/3\rfloor+2\lfloor n/4\rfloor<n\). Each vertex of color \(j\) broadcasts to at most \(2j+1\) vertices. The total number of broadcasting incidences is therefore at most
\[
3c_1+5c_2+7c_3=5n+2(c_3-c_1)<5n.
\]
Five pairwise disjoint dominating broadcast layers would require at least \(5n\) incidences, contradiction. Thus \(\chi_{\rho,5}(C_n)\ge4\) for every \(n\ge5\).

**2. The five-vertex and six-vertex cases.** With exactly five layers on \(C_5\), each layer is a singleton and must broadcast across eccentricity two. All five labels are at least \(2\); because the diameter is two, distinct vertices cannot share any such label. A five-color palette has only four labels \(2,3,4,5\), so \(\chi_{\rho,5}(C_5)\ge6\). On \(C_6\), at least four of five nonempty layers must be singletons, each with label at least three. Since the diameter is three, these four labels must be distinct, but a five-color palette has only three labels \(3,4,5\). Hence \(\chi_{\rho,5}(C_6)\ge6\).

**3. Exhaustive four-color obstructions at the exceptional lengths.** A four-palette packing word \(f\) is enumerated by assigning colors in \(\{1,2,3,4\}\) sequentially and rejecting a repeat of color \(j\) within the last \(j\) positions; on completion, every circular pair at distance at most its color is checked. These tests enumerate *all* valid packing words without omissions. For each word and vertex \(v\), let \(B_v=\{u:d(u,v)\le f(u)\}\). A necessary condition for five dominating broadcast layers is \(|B_v|\ge5\) for all \(v\). The verifier exhausts the following counts (number of packing words; number surviving all depth tests):

| \(n\) | 7 | 8 | 9 | 11 | 12 | 13 | 14 | 18 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Packing words | 28 | 68 | 72 | 440 | 760 | 1092 | 1554 | 17172 |
| Minimum depth at least five | 0 | 0 | 0 | 44 | 0 | 0 | 0 | 0 |

The \(44\) survivors on \(C_{11}\) are all ruled out as follows. Whenever \(|B_v|=5\), its five vertices must be in *five different layers*. Join every pair of vertices in such a five-element \(B_v\) to form a forced-distinct graph. Each of the \(44\) cases contains a six-vertex clique, hence cannot have a five-layer assignment. This obstruction is fully reproduced from definitions by `verify.py`, using standard-library enumeration of every packing word and six-subset; no solver or unexamined log is used. Therefore each of the eight lengths in the table needs at least five colors.

**4. Finite positive certificates.** For each of the \(35\) lengths \(5\le n\le39\), `witnesses.json` gives a length-\(n\) radii word and a length-\(n\) layer word with symbols in \(\{0,1,2,3,4\}\). The pair represents \(f(i)\) and the layer containing vertex \(i\). `verify.py` independently reconstructs cycle distances and checks all distinct equal-color vertex pairs and all \(5n\) broadcast coverage requirements. The maximum labels are \(6\) for \(n=5,6\), \(5\) for the eight lengths in the table, and \(4\) for \(n=10,15,16,17,19,\ldots,39\). For the eight exceptional lengths, the lower and upper bounds therefore coincide. For the displayed four-color lengths, the universal lower bound is sharp.

**5. Eight-symbol splicing, proving the infinite tail.** Encode a radii/layer pair at a vertex by one symbol \((f(i),a(i))\). With all radii at most four, both packing legality and five-layer coverage at a vertex depend only on its centered nine-symbol cyclic window: packing forbids an equal-radius pair at distance at most four, and each possible broadcaster lies within distance four. Thus any cyclic word in which all centered nine-windows are legal is a solution. If two such cyclic words, of lengths at least ten, have an identical eight-consecutive-symbol block, cut both immediately *after* that block and concatenate the two resulting complete cyclic traversals. Every nine-window away from a join occurs unchanged in one original cycle. Every nine-window crossing a join also occurs in one original cycle, since the eight symbols immediately before each corresponding cut agree. Hence the concatenated cyclic word is legal, with length equal to the *sum* of the two original lengths; its palette remains at most four. The common eight-symbol block remains present, so this operation can be repeated.

The ten-vertex base word from `witnesses.json` begins with the radii \((2,1,4,3,1,2,1,4)\) and layer labels \((3,1,4,0,2,3,4,1)\). Each of the ten certified words of lengths \(30,31,\ldots,39\) has precisely this eight-symbol prefix. Every integer \(n\ge30\) is uniquely \(s+10q\) with \(30\le s\le39\), \(q\ge0\); splice the certified length-\(s\) word with \(q\) copies of the ten-vertex word. This gives a four-color five-domatic coloring of every such cycle. Together with the checked certificates for \(19\le n\le29\), this proves the formula for all \(n\ge5\).

## Verification
Run `python3 verify.py` in a directory containing `verify.py` and `witnesses.json` from this finding. The program uses only the Python standard library. It reports `BASE_WITNESSES_OK 35`, `EXHAUSTIVE_NEGATIVE_FOUR_PALETTE_OK 21186`, `ELEVEN_VERTEX_K6_OBSTRUCTION_OK 44`, `SPLICING_CONSTRUCTION_TEST_OK 191`, and `VERIFY_OK`. The explicit infinite deduction rests on the proved eight-symbol splicing lemma and the ten mutually compatible length-\(30\)-to-\(39\) certificates, not on testing finitely many long cycles. No external solver is necessary for proof replay.

## Relationship to prior work
Brešar, Ferme and Hu (arXiv:2610.03477v1, first submitted 2026-10-02) introduced packing \(k\)-domatic colorings, determined the path cases \(k\in\{3,4,5\}\), and the cycle cases \(k\in\{3,4\}\). Their Section 3.3 does not state a five-domatic cycle classification, and a path result does not imply the cyclic closing conditions here. The earlier survey of packing colorings by Brešar, Ferme, Klavžar and Rall discusses the packing condition without this later five-layer broadcast invariant. The present result gives the previously untreated complete cycle spectrum for \(k=5\), with a nontrivial exceptional set and a constructive eventual cutoff.

## Limitations
The result is for finite simple cycles only, using the fixed five-layer requirement and the ordinary increasing packing radii. It does not classify other values of \(k\), paths, or arbitrary regular graphs. The finite obstruction uses transparent exhaustive enumeration for eight small orders; the statement is not a purely symbolic classification at those orders. Historical-priority searches are not a proof of absolute novelty, and no independent mathematical audit has been performed.

## References
1. B. Brešar, J. Ferme and W. Hu, *Partitioning an S-packing coloring into broadcast dominating sets*, arXiv:2610.03477v1 (2026-10-02), https://arxiv.org/abs/2610.03477 and https://arxiv.org/html/2610.03477v1.
2. B. Brešar, J. Ferme, S. Klavžar and D. F. Rall, *A survey on packing colorings*, Discussiones Mathematicae Graph Theory **40** (2020), 923–970, DOI:10.7151/dmgt.2320.
