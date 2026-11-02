# Exact composition-multiset ambiguity spectrum for binary words of lengths \(1\)–\(23\)

## Finding
For every binary length \(1\le n\le23\), the exact distribution of the sizes of all fibers of the complete substring-composition observation is provided in `data/census.csv`. Only sizes \(1,2,4\) occur in this range. At \(n=23\) there are exactly \(4{,}096\) singleton fibers, \(4{,}191{,}936\) two-word fibers, and \(160\) four-word fibers; the complete list of those \(160\) exceptional fibers is in `data/fourfold_23.tsv`. Thus the number of distinct observations and the largest possible error-free reconstruction code (one representative per observation) are both
\[
  4{,}096+4{,}191{,}936+160=4{,}196{,}192.
\]
No fiber has more than four words. The exact exceptional-fiber counts by length are \(1\) at \(n=8\), \(4\) at \(n=11\), \(12\) at \(n=14\), \(4\) at \(n=15\), \(22\) at \(n=17\), \(24\) at \(n=19\), \(56\) at \(n=20\), and \(160\) at \(n=23\), and zero for all other lengths in the specified range.

Selected census rows (the complete census has all twenty-three orders):

| Length | Distinct observations | Size-one fibers | Size-two fibers | Size-four fibers |
|---:|---:|---:|---:|---:|
| 8 | 135 | 16 | 118 | 1 |
| 11 | 1,052 | 64 | 984 | 4 |
| 14 | 8,244 | 128 | 8,104 | 12 |
| 17 | 65,770 | 512 | 65,236 | 22 |
| 20 | 524,744 | 1,024 | 523,664 | 56 |
| 23 | 4,196,192 | 4,096 | 4,191,936 | 160 |

## Assumptions and scope
A binary word \(w=w_0\cdots w_{n-1}\) is a finite, linear word; its substrings are contiguous, not cyclic. For each \(1\le\ell\le n\) and \(0\le j\le\ell\), define
\[
 c_{\ell,j}(w)=\#\left\{i:0\le i\le n-\ell,\ \sum_{k=i}^{i+\ell-1}w_k=j\right\}.
\]
The **complete composition multiset** is equivalent to the tuple \(\bigl(c_{\ell,j}(w)\bigr)\) of nonnegative integers, because the number of zeros is \(\ell-j\) and the number of ones is \(j\). Its fiber consists of all words giving exactly the same tuple. Multiplicity of repeated substring compositions is retained. Reversal preserves the tuple. We count distinct ordered binary input words, including both members of a nonpalindromic reversal pair, rather than quotienting the input space by reversal. All statements are for \(1\le n\le23\) only.

## Proof
For any \(n\), represent a word by the integer \(0\le v<2^n\), with its bit in position \(i\) equal to \(w_i\). Its reversed word has an integer obtained by reversing exactly \(n\) bits. Select exactly the representative \(v\le\operatorname{rev}_n(v)\) from each reversal orbit. Every binary word belongs to precisely one such orbit, which has size one for a palindrome and two otherwise.

Compute the complete signature for every representative: initialize counters to zero and, for each start index, extend the right endpoint one position at a time while updating the number of ones. For a substring of length \(\ell\) containing \(j\) ones, increment the counter with index
\[
 I(\ell,j)=\frac{(\ell-1)(\ell+2)}2+j.
\]
The ranges of indices for consecutive lengths are disjoint and exhaust exactly \(n(n+3)/2\) entries. A counter is at most \(n\le23\) and therefore is exactly represented as one byte. Group orbit representatives by equality of the **complete byte signature**, not just by a hash value. For each group, the fiber size is exactly the sum of its reversal-orbit sizes. There is neither sampling nor discarded input: the integer loop visits every one of the \(2^n\) bit words and retains precisely one representative from each orbit. Hence this finite procedure proves the fiber histogram exhaustively at every tested length.

The supplied `build_census.cpp` implements these exact steps over all integers up to \(2^{23}-1\). It finds that the only fiber sizes are one, two, and four; records all histogram entries in `data/census.csv`; and outputs every four-word length-twenty-three fiber in `data/fourfold_23.tsv`. At \(n=23\), the population identity
\[
  1(4{,}096)+2(4{,}191{,}936)+4(160)=2^{23}
\]
provides an additional necessary check on exhaustiveness. Since a zero-error reconstruction code can contain at most one representative per equal-observation class and one from every class attains that bound, its exact optimum is the number of fibers, \(4{,}196{,}192\).

## Verification
`verify_independent.cpp` independently calculates every substring composition as a **difference of binary prefix sums** at pairs of endpoints; it uses a distinct traversal order and signature-index expression. It enumerates reversal orbits for every length from one through twenty-three and compares every census-field value, checks the word-total identity, and reproduces the complete sorted four-word class table. Both implementations were executed successfully, with the independent program reporting `CROSSCHECK_OK all orders 1..23, including every length-23 collision class`. This is a finite exhaustive proof, not an extrapolation of sampled instances. No external algorithm, solver, or unavailable certificate is required.

To reproduce using a standard C++17 compiler with sufficient memory (approximately two gigabytes at the largest order), in the directory containing the embedded files run:
```
c++ -O3 -std=c++17 build_census.cpp -o build_census
./build_census data/census.csv data/fourfold_23.tsv
c++ -O3 -std=c++17 verify_independent.cpp -o verify_independent
./verify_independent data/census.csv data/fourfold_23.tsv
```

## Relationship to prior work
Acharya, Das, Milenkovic, Orlitsky, and Pan introduced the full substring-composition reconstruction model, characterized equicomposable words algebraically, established universal up-to-reversal uniqueness at certain lengths, and bounded maximum fiber size. They gave non-reversal ambiguity examples beginning at length eight and described a structurally distinct example at length twenty-three. Their conclusion explicitly identifies counting distinct composition multisets as an interesting question. Their general theorems and examples do not supply the exact twenty-three-row fiber histogram or list all \(160\) four-word fibers at length twenty-three. Gupta and Mahdavifar studied algebraic reconstruction algorithms and code constructions; these do not imply the exact maximum reconstruction-code size at length twenty-three. Gabrys and Milenkovic studied a different observation, the multiset of **ordered substring strings**, not the multiset of unordered compositions. Reversal is treated explicitly here, so known reconstructability-up-to-reversal results do not themselves determine counts of distinct observations.

## Limitations
This is a finite classification through length twenty-three, not an all-length recurrence or an algorithm with proved polynomial resource bounds for arbitrary length. Hash tables are used solely to find exactly equal signatures, never as collision-free mathematical certificates. The full census and the length-twenty-three four-word witnesses can be recomputed from the embedded programs. External priority is not independently certified, and obscure historical tables may exist. The coding interpretation concerns noiseless complete composition measurements, not noisy spectra or partial observations.

## References
1. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439 (first posted 2014-03-10), https://arxiv.org/abs/1403.2439; *SIAM Journal on Discrete Mathematics* 29(3), 1340–1371 (2015), https://doi.org/10.1137/140962486.
2. U. Gupta and H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, arXiv:2201.09955, https://arxiv.org/abs/2201.09955.
3. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548, https://arxiv.org/abs/1804.04548.
