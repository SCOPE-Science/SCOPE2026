# Exact shortest cyclic covers of binary reverse-complement palindromes through length eight

## Finding

A binary word \(w=w_0\cdots w_{2m-1}\) is a reverse-complement palindrome (also called an antipalindrome) if \(w_i=1-w_{2m-1-i}\) for every index \(i\). Denote the set of such words by \(A_m\), so \(|A_m|=2^m\). Let \(C_m\) be the least length of a **single** cyclic binary word containing every member of \(A_m\) among its cyclic length-\(2m\) windows. Let \(R_m\) count its optimal **indexed** cyclic binary words with the distinguished window at index zero equal to \(P_m=0^m1^m\); the count does not identify rotations or reversals.

The exact values are:

| \(m\) | Window length \(2m\) | Required words \(|A_m|\) | \(C_m\) | \(R_m\) |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 1 |
| 2 | 4 | 4 | 9 | 2 |
| 3 | 6 | 8 | 26 | 14 |
| 4 | 8 | 16 | **67** | **1232** |

One optimum for \(m=4\), rooted with `00001111`, is:

`0000111100001010101001010110010110011001101001101010001011100011101`

The finite enumeration is exact; the result makes no claim for \(m\ge5\).

## Assumptions and scope

All words use the labeled alphabet \(\{0,1\}\), with complement interchanging the symbols. A cyclic word of length \(N\ge2m\) is an indexed sequence \(c_0,\ldots,c_{N-1}\), and its window beginning at index \(i\) uses coordinates modulo \(N\). All required words must appear themselves, not merely up to reverse complementation. Covering words may contain arbitrary other windows and repeated required words. \(R_m\) counts indexed words with a specified first window; it is not a count of necklaces or bracelets.

## Proof

**Finite-state exact optimization.** Fix \(m\), put \(k=2m\), and enumerate \(A_m=\{a_0,\ldots,a_{2^m-1}\}\) lexicographically with \(a_0=P_m\). Let \(V=\{0,1\}^{k-1}\). In the ordinary directed binary de Bruijn graph a state records \((v,S)\), with \(v\in V\) the current suffix and \(S\subseteq A_m\) the set of required length-\(k\) edges already traversed. Appending \(b\in\{0,1\}\) moves to

\[
(v,S)\longmapsto\bigl(\operatorname{suffix}_{k-1}(vb),\ S\cup(\{vb\}\cap A_m)\bigr).
\]

Every feasible cyclic host contains \(P_m\); rotate its indices so that this word is the first window. Start at \(u=\operatorname{prefix}_{k-1}(P_m)\), force the first edge \(P_m\) (one step), and subsequently traverse unrestricted de Bruijn edges. An indexed cyclic host beginning in \(P_m\) has length \(N\) **if and only if** it corresponds to a walk of \(N\) appended bits whose starting and ending \((k-1)\)-suffixes are both \(u\), the first traversed edge is \(P_m\), and the union of its recorded required edges is all of \(A_m\). The forward construction reads cyclic windows; conversely, closure of the suffix makes the final \(k-1\) appended bits agree with the initial prefix, so the walk spells a cyclic host. The distinguished starting window gives a unique walk for each indexed host.

Run breadth-first search after the forced first edge on all \(2^{k-1}2^{2^m}\) possible states. Distances are initialized to one at \((\operatorname{suffix}_{k-1}(P_m),\{P_m\})\). The first terminal state with suffix \(u\) and recorded set \(A_m\) gives \(C_m\). For each newly discovered state set its shortest-path count equal to that of its predecessor, and for an additional edge entering at the same shortest distance add the predecessor count. This is an integer recurrence on distance layers, and all incoming shortest predecessors are processed before a state is removed from the BFS queue. Its terminal count is exactly \(R_m\).

**Independent overlap optimization.** For distinct \(a_i,a_j\in A_m\), let \(o_{ij}\) be their longest proper suffix-prefix overlap (possibly zero) and put \(d_{ij}=k-o_{ij}\). Fix \(a_0\) and define \(H(T,j)\) to be the minimum total overlap-transition cost of a route beginning in \(a_0\), visiting precisely the words indexed by \(T\), and ending in \(a_j\), where \(0,j\in T\). Then \(H(\{0\},0)=0\), and for all other states

\[
H(T,j)=\min_{i\in T\setminus\{j\}}\bigl(H(T\setminus\{j\},i)+d_{ij}\bigr).
\]

The exact cyclic optimum is \(\min_{j\ne0}(H(A_m,j)+d_{j0})\) when \(|A_m|>1\). To justify equality, select one occurrence of each required word along an arbitrary feasible cycle: consecutive chosen starts are separated by at least their minimal suffix-prefix transition costs, hence the Hamiltonian tour costs no more than the cycle length. Conversely a tour can be realized by maximal overlaps, including its closing edge, producing a cyclic word of exactly the tour cost that contains every required word. Thus this independent subset dynamic program must return \(C_m\).

Both finite recurrences are exhaustively evaluated by the standalone source file `verify.cpp`. The resulting \((C_m,R_m)\) values are exactly \((2,1),(9,2),(26,14),(67,1232)\), as stated.

## Verification

Build with `c++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify_antipal` and run `./verify_antipal`. This implementation enumerates anti-palindromic words from their defining bit symmetry, computes the required-edge subset BFS with exact integer path counts, independently computes all pairwise overlaps and Held–Karp tour minima, reconstructs witnesses, and tests every cyclic window of each witness against the target set.

The observed final line is `VERIFY_OK antipal_cover_k=2,4,6,8 independent_overlap_TSP_and_rooted_BFS`. For the sixteen-word case, BFS discovers 4,190,096 states before reaching its optimal terminal state; the ambient state space contains 8,388,608 states. The independently computed shortest overlap tour also has cost \(67\).

## Relationship to prior work

Moreno and Matamala (2007) study de Bruijn sequences of constrained languages, seeking an Eulerian cycle containing each admissible word exactly once. Their problem does not give shortest **repeat-permitting** one-cycle covers of the present small fixed set of reverse-complement palindromes. Orenstein and Shamir (2013) optimize an RC-complete sequence covering **one representative of each reverse-complement pair among every DNA \(k\)-mer**, rather than covering only the RC-fixed-point words (all of which are compulsory there) in a single binary cyclic host and counting such hosts. Fici and collaborators (2015) study approximation for a linear superstring problem with optional reversals, not the present compulsory anti-palindrome subset. Cazaux, Cánovas, and Rivals (2016) study the shortest DNA **cyclic cover**, permitting a collection of cycles and optional RC orientations; an optimal set of cycles does not determine the one-cycle optimum or its rooted multiplicity. These distinct optimization targets do not imply the displayed numerical table.

Ordinary palindromes satisfy \(w_i=w_{k-1-i}\), whereas the present required factors satisfy \(w_i=1-w_{k-1-i}\). The two target families are not interchangeable. Available mathematical-record and literature searches did not locate this particular finite table; that absence is not a proof of global novelty.

## Limitations

The proof is a reproducible finite dynamic-programming certificate, not a uniform closed-form theorem for all \(m\). The numbers \(R_m\) are rooted indexed multiplicities and should not be read as counts modulo rotation. The optimum is for binary reverse-complement-fixed words only; it is neither a DNA four-letter all-k-mer optimum nor the shortest cover of all binary words. Indexed publisher material was available for a directly related RC-complete paper, but its continuous full text could not be retrieved; overlapping examples in inaccessible material remain a residual originality risk.

## References

1. E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, 12 November 2007, arXiv:0711.1695v1. https://arxiv.org/abs/0711.1695
2. Y. Orenstein and R. Shamir, *Design of shortest double-stranded DNA sequences covering all k-mers with applications to protein-binding microarrays and synthetic enhancers*, *Bioinformatics* 29 (2013), i71–i79; online 19 June 2013. DOI:10.1093/bioinformatics/btt230.
3. G. Fici, T. Kociumaka, J. Radoszewski, W. Rytter, and T. Waleń, *On the Greedy Algorithm for the Shortest Common Superstring Problem with Reversals*, arXiv:1511.08431v1 (26 November 2015). https://arxiv.org/abs/1511.08431
4. B. Cazaux, R. Cánovas, and E. Rivals, *Shortest DNA Cyclic Cover in Compressed Space*, Data Compression Conference (2016), pp. 536–545. DOI:10.1109/DCC.2016.79.
