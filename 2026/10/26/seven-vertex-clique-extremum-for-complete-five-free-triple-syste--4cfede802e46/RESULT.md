# Seven-vertex clique extremum for complete-five-free triple systems

## Finding
Let \(G\) be a simple \(3\)-uniform hypergraph on a set \(V\) of seven labelled vertices. A *clique* is a subset \(S\subseteq V\) for which every triple of \(S\) is an edge; thus all sets of sizes zero, one and two are automatically cliques. Assume that \(G\) contains no complete \(3\)-uniform hypergraph on five vertices, denoted \(K_5^{(3)}\). Then the total number \(c(G)\) of cliques satisfies
\[
 c(G)\le 77.
\]
Equality holds **if and only if** there is a partition \(V=A\sqcup B\) with \(|A|=3\) and \(|B|=4\) such that
\[
 E(G)=\{e\in\tbinom V3:e\cap A\ne\varnothing\text{ and }e\cap B\ne\varnothing\}.
\]
Consequently there are exactly \(\binom73=35\) labelled extremizers and one isomorphism type.

## Assumptions and scope
Hypergraphs have no repeated triples and are considered on exactly seven vertices, including isolated vertices if any. *Free* means containing no (not necessarily induced) complete five-vertex triple system. The clique count includes the empty set and all small subsets as above. The classification does not assert anything for larger orders.

## Proof
Set \(M=\binom V3\setminus E(G)\), the family of missing triples, and put \(t=|M|\). Its *upper four-shadow* is
\[
 \partial^+_4M=\{Q\in\tbinom V4:\exists T\in M\text{ with }T\subseteq Q\},\qquad s=|\partial^+_4M|.
\]
The graph \(G\) is \(K_5^{(3)}\)-free if and only if every one of the \(\binom75=21\) five-sets contains at least one member of \(M\). In that case there are no cliques on five or more vertices. Exactly \(35-t\) triples and \(35-s\) four-sets are cliques. Therefore
\[
 c(G)=1+7+21+(35-t)+(35-s)=99-t-s.
\]
It remains to prove that every missing-triple family meeting all five-sets satisfies \(t+s\ge22\), with the required equality cases.

The following is a finite but *complete* certificate. Since any such \(M\) is nonempty, permuting the vertices sends one of its members to \(\{0,1,2\}\). Order the \(35\) triples lexicographically, so this is triple zero. For each \(1\le t\le8\), the supplied C++17 checker enumerates **every** family containing this triple with \(t\) members by choosing the other \(t-1\) indices among the remaining \(34\). It constructs exact bitsets for the \(35\) four-sets and \(21\) five-sets containing each triple. The five-set union tests feasibility, and the four-set union counts \(s\). No random search, pruning, or numerical approximation is used. The exhaustive results are:

| \(t\) | All normalized families | Five-covering families | Least \(s\) among five-covering families |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 0 | none |
| 2 | 34 | 0 | none |
| 3 | 561 | 0 | none |
| 4 | 5,984 | 0 | none |
| 5 | 46,376 | 245 | 17 |
| 6 | 278,256 | 15,300 | 19 |
| 7 | 1,344,904 | 235,992 | 20 |
| 8 | 5,379,616 | 1,861,744 | 20 |

In particular, feasible cases with \(t\le7\) have \(t+s\ge22\), and equality occurs only when \(t=5\) and \(s=17\). Among all \(5,379,616\) normalized eight-triple families, **including infeasible ones**, the minimum upper-four-shadow size is exactly \(16\). Every family with \(t\ge8\) contains some eight-member subfamily; by relabelling it is isomorphic to one in this exhaustive list. Its shadow therefore contains at least \(16\) four-sets, so \(t+s\ge8+16=24>22\). Thus the finite checks cover the entire infinite-looking family of cases \(1\le t\le35\) and constitute an exhaustive proof, not a truncated search.

The checker records exactly **five** normalized feasible equality families. It verifies by exact set equality that each consists of all triples wholly within the parts of a partition with sizes \(3\) and \(4\); no other normalized family attains \(t+s=22\). Conversely, such a partition has exactly \(\binom33+\binom43=5\) missing triples. Its upper-four-shadow has \(17\) members, and any five vertices meet at least one part in at least three vertices, so it covers every five-set. Hence it attains \(c(G)=99-5-17=77\). The \(\binom73=35\) choices for its unique three-element part give distinct labelled extremizers. This finishes the classification.

## Verification
The standalone files `verify_clique7.cpp` and `check_independent.py` are included. Run:

```sh
g++ -O2 -std=c++17 -Wall -Wextra verify_clique7.cpp -o verify_clique7
./verify_clique7
python3 check_independent.py
```

The C++ program exhausts \(\sum_{t=1}^{8}\binom{34}{t-1}\) normalized cases, verifies the covering counts and shadow cutoffs, and checks equality shapes. It prints `CERTIFICATE_OK maximum_cliques=77 normalized_optima=5 labeled_optima=35`. Independently written Python enumerates all feasible normalized families with up to seven missing triples and checks the equality classes and thirty-five labelled constructions; it prints `PYTHON_CHECK_OK normalized_optima 5 all_bipartite_templates 35 score 22`. The eight-triple cutoff is verified by the C++ program and logically extends the finite search to every larger missing-triple family.

## Relationship to prior work
Frankl, Gryaznov and Talebanfard formulated a clique-count conjecture for forbidden complete uniform hypergraphs. Chen, Deng, Hou, Liu and Zhang proved that the balanced complete bipartite triple system is the unique clique-count maximizer among \(K_5^{(3)}\)-free systems for **all sufficiently large** vertex orders (Theorem 1.5 of the 2026 paper). Their proof does not specify a numerical threshold that covers seven vertices. The present statement settles precisely that finite order and the complete equality classification. Bodnár's earlier generalized Turán work concerns a different asymptotic counting comparison and does not give this seven-vertex equality classification. A separately indexed six-vertex extremal determination addresses an earlier order and does not directly imply this result.

## Limitations
The result is a computationally assisted exhaustive **finite** theorem. It does not provide a uniform proof for general vertex orders or a minimum valid order for the large-order result. The originality comparison includes full-text inspection of the relevant primary preprints and targeted literature and public-results searches; historical priority has not been independently certified. The C++ certificate assumes a conforming C++17 compiler with ordinary assertions enabled, and can be independently reconstructed from the declared finite index loops. No independent external audit is claimed.

## References
1. W. Chen, J. Deng, J. Hou, X. Liu and Y. Zhang, *Vertex-colored Turán theorems with applications in extremal hypergraph problems*, arXiv:2606.02210v2 (2026), Theorem 1.5 and Section 5; initially public June 1, 2026.
2. P. Frankl, S. Gryaznov and N. Talebanfard, *A Variant of the VC-dimension with Applications to Depth-3 Circuits*, arXiv:2111.09671v1 (2021), Conjecture 14.
3. L. Bodnár, *Generalized Turán Problem for Complete Hypergraphs*, arXiv:2302.07571v2 (2023), generalized clique-count bounds.
