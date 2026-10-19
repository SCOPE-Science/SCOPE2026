# Reverse-complement-closed non-overlapping binary codes: an exact initial spectrum and an odd-length threshold

## Finding

For binary blocklength \(n\ge2\), let \(M_{\mathrm{RC}}(n)\) be the maximum number of words in a code \(C\subseteq\{0,1\}^n\) satisfying both conditions:

1. For every \(u,v\in C\), including \(u=v\), and every \(1\le j<n\), the length-\(j\) prefix of \(u\) differs from the length-\(j\) suffix of \(v\).
2. \(C\) is invariant under reverse complement \(\rho(u)=\overline{u^{\mathrm{rev}}}\), so \(\rho(C)=C\).

Then the complete exact initial spectrum is:

| \(n\) | \(M_{\mathrm{RC}}(n)\) | Admissible reverse-complement orbits in one orientation | Conflict edges | Certificate clique cost |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 0 | 1 |
| 3 | 0 | 0 | 0 | 0 |
| 4 | 1 | 1 | 0 | 1 |
| 5 | 0 | 0 | 0 | 0 |
| 6 | 2 | 2 | 0 | 2 |
| 7 | 0 | 0 | 0 | 0 |
| 8 | 5 | 4 | 0 | 5 |
| 9 | 2 | 2 | 1 | 2 |
| 10 | 14 | 12 | 3 | 14 |
| 11 | 10 | 12 | 12 | 10 |
| 12 | 42 | 40 | 35 | 42 |
| 13 | 44 | 60 | 120 | 44 |
| 14 | 132 | 152 | 364 | 132 |
| 15 | 170 | 264 | 1236 | 170 |
| 16 | 430 | 592 | 4034 | 430 |

In particular, the existence problem has an all-length answer:

\[
M_{\mathrm{RC}}(n)>0\quad\Longleftrightarrow\quad n\text{ is even or }n\ge9,
\qquad(n\ge2).
\]

The exceptional odd blocklengths are exactly \(3,5,7\). This result concerns *closure* under reverse complement, not the different constraint that a code avoid reverse-complement matches. For the trivial blocklength \(n=1\), the entire binary alphabet is allowed and \(M_{\mathrm{RC}}(1)=2\).

## Assumptions and scope

Words have exactly \(n\) binary symbols. All forbidden overlaps are nonempty and proper, and self-overlaps count. Reverse complement first reverses symbol order and then exchanges \(0\) and \(1\). Code size counts actual words, not reverse-complement pairs. No Hamming-distance, run-length, or balanced-composition constraint is imposed.

Every nonempty binary non-overlapping code of length at least two has all codewords beginning with one symbol and ending with the other: the sets of first and final symbols must be disjoint nonempty subsets of \(\{0,1\}\). Complementing all words exchanges the two possible orientations and commutes with reverse complement. It therefore suffices to classify codewords beginning in \(0\) and ending in \(1\).

## Proof

**All-length existence.** At every even length \(n=2k\), \(k\ge1\), the word \(0^k1^k\) is unbordered and fixed by reverse complement, hence its singleton is an admissible code.

For odd lengths \(n=2k+1\) with \(k\ge4\), consider the pair

\[
u_k=0^k1101^{k-2},\qquad \rho(u_k)=0^{k-2}1001^k.
\]

For \(k\ge5\), both prefixes start with at least \(k-2\) zeros and both suffixes end with at least \(k-2\) ones, so an overlap of length smaller than \(k-2\) is impossible. For a longer overlap, any matching proper suffix must begin with at least \(k-2\) zeros. In \(\rho(u_k)\) no proper suffix has such a starting run, because its only other zero-run has length two. In \(u_k\), the only possible proper suffixes begin at positions one or two of its leading zero-run. A suffix beginning at position one has \(k-1\) initial zeros, and a suffix beginning at position two has \(k-2\) initial zeros followed by `11`; neither equals a prefix of \(u_k\) or \(\rho(u_k)\), whose respective initial patterns are \(0^k1\) and \(0^{k-2}10\). Thus the pair has no forbidden overlaps. The remaining case \(k=4\) consists of `000011011` and `001001111`, directly checked for every overlap length from one to eight by `verify.py`. This establishes existence for every odd \(n\ge9\).

For odd \(n=3,5,7\), any admissible nonempty reverse-complement-closed code would contain a single admissible orbit \(\{w,\rho(w)\}\), after choosing an orientation. Directly enumerate every one of the \(2^{n-2}\) strings of the form \(0x1\), retaining a word only when both \(w\) and \(\rho(w)\) avoid self-overlaps and mutual overlaps. The resulting orbit sets are empty at all three lengths, as exhaustively checked by `verify.py` and independently implicit in the full graph certificates. Hence no nonempty such code exists at \(n=3,5,7\).

**Exact finite maxima.** For each \(2\le n\le16\), define a vertex for every reverse-complement orbit \(Q\subseteq\{0,1\}^n\) having only words starting with \(0\) and ending with \(1\), and with no forbidden overlaps internally. Its weight is \(|Q|\), either one or two. Join two vertices if any word in one orbit has a forbidden prefix/suffix overlap with a word in the other orbit. Then admissible codes in this orientation are in one-to-one correspondence with independent vertex sets, and their codeword cardinalities equal total vertex weight.

The embedded `certificates.json` lists, at each of the fifteen blocklengths, both an independent set \(I\) and a nonnegative *integer multicover* of the conflict graph by cliques. If \(y_K\) is the multiplicity assigned to clique \(K\), every vertex \(v\) is covered with total multiplicity at least its weight \(|v|\), and

\[
\sum_K y_K=\sum_{v\in I}|v|=M.
\]

For any independent set \(J\), each clique contains at most one vertex of \(J\), so

\[
\sum_{v\in J}|v|\le\sum_{v\in J}\sum_{K\ni v}y_K
=\sum_K y_K|J\cap K|\le\sum_Ky_K=M.
\]

This finite combinatorial certificate proves optimality, not merely lower bounds from a solver. The listed witnesses attain all fifteen upper bounds, establishing the table.

## Verification

`verify.py` and `certificates.json` are fully self-contained, and the verifier uses only the Python standard library. From the definitions it regenerates every orientation-normalized word, tests all proper self-overlaps and overlaps with its reverse complement, reconstructs all admissible orbits and conflict edges, checks every selected code for reverse-complement closure and prefix/suffix disjointness, validates that each advertised upper-bound set is a clique, and verifies the exact integer vertex-coverage inequalities and equality of the primal and dual totals. It also directly checks the explicit all-length constructions over a broad finite range. Run in the directory containing both files:

```sh
python3 verify.py certificates.json
```

The checker is an independent *certificate checker*: it does not run a linear or integer programming solver or assume its correctness. The full infinite family is proved by the preceding run argument; finite testing of that family is only corroboration.

## Relationship to prior work

Chee, Kiah, Purkayastha, and Wang introduced useful large cross-bifix-free code constructions and asymptotic estimates (arXiv:1209.0236, publicly available on 2012-09-03). Blackburn studied non-overlapping codes under the equivalent name, their bounds, and the unrestricted binary optimum through length sixteen (arXiv:1303.1026, first posted 2013-03-05). Their unrestricted optimum table concerns \(\max |C|\) without reverse-complement closure and does not determine this table. For example, an unrestricted binary length-three non-overlapping code has size one, whereas the reverse-complement-closed optimum is zero.

Yazdi, Kiah, Gabrys, and Milenkovic studied mutually uncorrelated DNA primers and a *reverse-complement avoidance* constraint, rather than forcing every reverse-complement partner to belong to the same code (arXiv:1709.05214). Stanovnik, Moškon, and Mraz computed and classified further unrestricted non-overlapping code optima (DOI:10.1007/s10623-023-01344-z); their tabulation does not impose this involution. General unrestricted upper bounds still apply but do not imply the sharp symmetry-restricted optima here.

## Limitations

This gives exact capacities only through length sixteen. The positivity threshold is valid for all lengths, but no formula or asymptotic bound for \(M_{\mathrm{RC}}(n)\) at arbitrary larger lengths is asserted. These results are specific to the binary alphabet with bitwise complementation; quaternary DNA alphabets are not covered. The certificate verifies mathematical optimality of the finite graph reductions but is not an independent external scientific audit. Earlier unindexed tables of involution-stable synchronization codes could affect historical priority.

## References

1. Y. M. Chee, H. M. Kiah, P. Purkayastha and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236, first posted 2012-09-03. https://arxiv.org/abs/1209.0236
2. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, first posted 2013-03-05. https://arxiv.org/abs/1303.1026
3. S. M. H. T. Yazdi, H. M. Kiah, R. Gabrys and O. Milenkovic, *Mutually Uncorrelated Primers for DNA-Based Data Storage*, arXiv:1709.05214, 2017. https://arxiv.org/abs/1709.05214
4. L. Stanovnik, M. Moškon and M. Mraz, *In search of maximum non-overlapping codes*, *Designs, Codes and Cryptography* 92 (2024), 1299–1326. https://doi.org/10.1007/s10623-023-01344-z
