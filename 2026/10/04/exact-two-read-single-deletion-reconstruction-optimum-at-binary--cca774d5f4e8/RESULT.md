# Exact two-read single-deletion reconstruction optimum at binary length \(7\)
## Finding
Let \(D_1(x)\) be the set of distinct length-\(6\) words obtained by deleting one coordinate from \(x\in\{0,1\}^7\). Among all codes \(C\subseteq\{0,1\}^7\) such that \(|D_1(x)\cap D_1(y)|<2\) for every distinct \(x,y\in C\), the maximum cardinality is exactly \(70\). Equivalently, the optimal two-read single-deletion reconstruction redundancy at length \(7\) is \(\rho(7,2;D_1)=7-\log_2 70\approx0.8707169831\) bits.

A concrete optimal code of size \(70\) and a matching \(70\)-class cover certificate are stored in `certificate.json`.

## Assumptions and scope
For a binary word \(x=x_1\cdots x_7\), define \(D_1(x)\) to be the set of distinct words obtained by deleting exactly one coordinate. A code is required to reconstruct uniquely from any two distinct single-deletion reads. Thus for every two distinct codewords \(x,y\), the two deletion balls must have fewer than two common outputs:
\[
|D_1(x)\cap D_1(y)|<2.
\]
The claim concerns exactly binary blocklength \(7\), one deletion per read, and two distinct reads. It does not cover insertions, substitutions, repeated identical reads, larger blocklengths, or list decoding.

## Proof
Form the compatibility graph \(H\) on the \(128\) binary words of length \(7\): two distinct vertices \(x,y\) are adjacent exactly when \(|D_1(x)\cap D_1(y)|<2\). Valid two-read reconstruction codes are precisely cliques of \(H\).

The certificate contains \(70\) explicit codewords. Direct recomputation of all deletion balls shows that every pair among these words is adjacent in \(H\), so \(\omega(H)\ge 70\).

The same certificate assigns one of \(70\) colors to every vertex of \(H\). Direct recomputation of every pair shows that adjacent vertices always receive different colors. Therefore this is a proper \(70\)-coloring of \(H\), and every clique of \(H\) has at most one vertex of each color. Hence \(\omega(H)\le 70\). Combining the two inequalities gives \(\omega(H)=70\).

Equivalently, in the confusability graph \(G(7)=\overline H\) used in the deletion-reconstruction literature, the \(70\) codewords form an independent set and the \(70\) color classes form a clique cover. The lower and upper certificates therefore meet exactly.

By the standard redundancy definition for a binary length-\(n\) code, \(\rho=n-\log_2|C|\), which gives \(\rho(7,2;D_1)=7-\log_2 70\).

## Verification
Run `python3 verify.py`. It rebuilds all \(128\) deletion balls from the definition, checks every pair of the \(70\)-word witness, checks every edge against the \(70\)-color assignment, and also checks the equivalent clique-cover condition in the confusability graph.

Run `python3 search.py` for an independent exact branch-and-bound computation. It reconstructs the graph from scratch and uses a greedy-color upper bound inside maximum-clique search; it terminates with `MAX=70` and `SEARCH_OK`. This exact search is finite and exhaustive for length \(7\); no claim for unsearched lengths is inferred from it.

## Relationship to prior work
Cai, Kiah, Nguyen, and Yaakobi introduced the fixed-read reconstruction-code formulation and explicitly singled out the two-read single-deletion quantity \(\rho(n,2;D_1)\) as a central case. Chrisnata, Kiah, and Yaakobi then characterized the forbidden pairs by Type-A confusability, defined the associated graph on binary words of length \(n\), and proved the asymptotic law \(\rho(n,2;D_1)=\log_2\log_2 n+\Theta(1)\) using clique covers.

The inspected full texts do not state the exact length-\(7\) optimum or a finite table containing \(70\). The present certificate resolves that finite instance in exactly the same graph-theoretic framework: a size-\(70\) independent set in the literature's confusability graph and a matching \(70\)-clique cover.

## Limitations
This is a finite exact result only at blocklength \(7\). It does not establish a formula for other blocklengths, classify all optimal codes, or improve the published asymptotic order. A poorly indexed or unpublished finite computation could contain the same value; no such source was found in the inspected primary literature or exact-parameter searches. Independent audit has not been performed.

## References
1. K. Cai, H. M. Kiah, T. T. Nguyen, and E. Yaakobi, “Coding for Sequence Reconstruction for Single Edits,” arXiv:2001.01376v1, first public version 2020-01-06.
2. J. Chrisnata, H. M. Kiah, and E. Yaakobi, “Optimal Reconstruction Codes for Deletion Channels,” arXiv:2004.06032v1, first public version 2020-04-13.
