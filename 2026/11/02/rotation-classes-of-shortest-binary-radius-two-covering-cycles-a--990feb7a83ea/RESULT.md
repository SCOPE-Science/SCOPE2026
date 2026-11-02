# Rotation classes of shortest binary radius-two covering cycles at window lengths seven through nine

## Finding
For a binary circular string \(s=(s_0,\ldots,s_{L-1})\), define its length-\(n\) windows \(W_i(s)=(s_i,\ldots,s_{i+n-1})\), with all subscripts modulo \(L\). We call \(s\) a radius-two covering cycle for order \(n\) when every \(u\in\{0,1\}^n\) has Hamming distance at most two from some \(W_i(s)\).

For the three consecutive orders \(n\in\{7,8,9\}\), the shortest covering cycle lengths and the complete numbers of shortest covering cycles are:

| Order \(n\) | Minimum cycle length \(L\) | Number of indexed binary cycles | Number of classes modulo cyclic rotation |
|---:|---:|---:|---:|
| 7 | 10 | 110 | **11** |
| 8 | 14 | 28 | **2** |
| 9 | 20 | 20 | **1** |

All rotation classes have full length \(L\). In particular, the **unique** shortest radius-two binary covering cycle for nine-bit windows, up to cyclic rotation, is `00010010001110110111`. Its complement and reversal are rotations of itself.

The complete 14 lexicographically least rotation representatives, with their orbit sizes, are in `orbits.csv`; no equivalence by complementation or reversal is imposed in the classification.

## Assumptions and scope
The alphabet is \(\{0,1\}\), the radius is exactly two, and only orders \(n=7,8,9\) are asserted. Cyclic windows wrap around the end, even when \(n>L\). Two indexed strings are equivalent only if one is a cyclic rotation of the other. The minimum lengths themselves were already established in the foundational work cited below; the newly assessed contribution is their complete orbit census and the resulting uniqueness assertion at order nine.

## Proof
For any integer \(L\geq1\), the \(2^L\) binary indexed cycles are in bijection with integers \(x\) satisfying \(0\leq x<2^L\): the bit at circular position \(i\) is the \(i\)-th low-order bit of \(x\). The window beginning at \(i\) is constructed by reading positions \((i+j)\bmod L\) for \(0\leq j<n\). Define the ball \(B_2(w)=\{u\in\{0,1\}^n:d_H(u,w)\leq2\}\). Therefore the covering predicate is precisely
\[
\bigcup_{i=0}^{L-1}B_2(W_i(s))=\{0,1\}^n.
\]
The first standalone C++17 implementation enumerates every integer \(x\) for every \(1\leq L\leq 10,14,20\), respectively. It precomputes each \(B_2(w)\) as a finite bitset, forms the union for every candidate cycle, and compares that union to the complete universe. No sampling or heuristic termination occurs. The second, separately implemented C++17 program instead loops over each target word \(u\), directly calculates its Hamming distance to every cyclic window, and rejects a candidate if any target has no suitable window. Both give identical counts at every examined length (the full 44-row census is in `checks.csv`). For each order, all shorter lengths give zero covers; the counts at the first attainable lengths are \(110,28,20\).

Rotation preserves the covering predicate. For each accepted indexed string, the verifier computes the lexicographically least of its \(L\) rotations, collecting representatives and verifying how many indexed strings map to each. Every class in the result has exactly \(L\) members: eleven such classes of size ten, two of size fourteen, and one of size twenty. The total counts agree with \(110,28,20\), showing that the representatives exhaust all shortest cycles. These are finite exhaustive proofs because each algorithm traverses the entire explicitly bounded input domain and tests a predicate logically equivalent to coverage. The source programs and their inputs are supplied without external dependencies.

## Verification
Compile both programs with a C++17 compiler, for example `g++ -std=c++17 -O2 enumerate.cpp -o enumerate` and `g++ -std=c++17 -O2 crosscheck.cpp -o crosscheck`. Running `./enumerate` and `./crosscheck` prints all lengths and their cover counts; the direct-method results coincide with `checks.csv`. Each source also prints the orbit representatives for the respective minimum length; compare to `orbits.csv`. The optimized method uses precomputed Hamming balls, whereas the cross-check computes Hamming distances directly and never uses the ball-bitset lookup. The programs enumerate \(2^{20}\) candidates at order nine and its minimum length, in addition to all shorter candidates.

## Relationship to prior work
Chung and Cooper, *De Bruijn Cycles for Covering Codes* (public preprint October 24, 2003), introduced this model and recorded the already known minimum lengths \(10,14,20\) at radius two and orders \(7,8,9\). Their numerical table and a general lower bound of \(L\) labeled rotations of any shortest cycle do not determine the number of rotation classes. The present result sharpens that generic lower bound to equality at order nine and classifies the three successive shortest-cycle families. Chee, Etzion, Ta and Vu (2025) exhibit the same twenty-bit example in their Appendix A; their full article supplies constructions and bounds, not a complete enumeration of shortest-cycle rotation classes. Ta and Vu (2026) address asymptotically efficient covering-sequence constructions rather than finite orbit classifications. The unpublished or unindexed existence of an older complete census cannot be excluded.

## Limitations
Only the precise finite orders and radius stated above are classified; no formula for other orders, other alphabets, or other radii is implied. The census certifies mathematical exhaustiveness of the specified bounded searches, but it does not independently certify historical priority. Reversal and bit complementation are not divided out; the uniqueness assertion for order nine is modulo rotation alone. Source programs are executable exhaustive certificates rather than an external independently reviewed proof.

## References
1. Fan Chung and Joshua N. Cooper, *De Bruijn Cycles for Covering Codes*, arXiv:math/0310385 (first public arXiv posting October 24, 2003), https://arxiv.org/abs/math/0310385, especially §5 and Table 1.
2. Yeow Meng Chee, Tuvi Etzion, Hoang Ta and Van Khu Vu, *Constructions of covering sequences and 2D-sequences*, Designs, Codes and Cryptography 93 (2025), 5445–5471, https://doi.org/10.1007/s10623-025-01726-5, §2 and Appendix A.
3. Hoang Ta and Van Khu Vu, *Near-Optimal Covering Sequences*, arXiv:2606.29236, public June 28, 2026, https://arxiv.org/abs/2606.29236 (asymptotic context; abstract inspected).
