# A unique four-coordinate dual circuit in an extremal ternary length-25 code
## Finding
For the second generator matrix in Araya--Harada's electronic list of the 26 extremal ternary maximal self-orthogonal \([25,12,9]_3\) codes, let \(C\) be the generated code. Then \(C^\perp\) has minimum distance \(4\) and exactly two weight-\(4\) codewords, which are negatives of each other. Their common support is the unique dependent four-set of generator-matrix columns, namely coordinates \(\{1,19,20,21\}\); with this coordinate order one word has entries \((1,2,2,2)\) on that support and the other is its negative. Consequently every monomial automorphism of \(C\) stabilizes this four-coordinate set. The complete Hamming weight enumerators are \[W_C(z)=1+2158z^9+39522z^{12}+202272z^{15}+236692z^{18}+49992z^{21}+804z^{24},\] and \[W_{C^\perp}(z)=1+2z^4+168z^7+2158z^9+12828z^{10}+39522z^{12}+159908z^{13}+202272z^{15}+504408z^{16}+236692z^{18}+348936z^{19}+49992z^{21}+36560z^{22}+804z^{24}+72z^{25}.\]

## Assumptions and scope
The object is the second `LinearCode<GF(3),25|...>` entry in the electronic file `25-12-9.txt` accompanying Makoto Araya and Masaaki Harada's classification of ternary maximal self-orthogonal codes of length \(25\). Coordinates are numbered \(1,\ldots,25\) in the order printed in that database entry. The claim concerns this specific equivalence-class representative; it does not assert that all 26 extremal classes have the same dual spectrum.

## Proof
Let \(G\) be the printed \(12\times25\) generator matrix. Exact arithmetic over \(\mathbb F_3\) gives \(\operatorname{rank}(G)=12\) and \(GG^T=0\), so its row space \(C\) is a self-orthogonal \([25,12]_3\) code. Exhausting all \(3^{12}\) row combinations gives
\[
W_C(z)=1+2158z^9+39522z^{12}+202272z^{15}+236692z^{18}+49992z^{21}+804z^{24},
\]
so the minimum distance is \(9\), in agreement with the database stratum.

A dual word of support \(S\) is exactly a linear dependence among the columns indexed by \(S\). To remove scalar duplication, normalize the first nonzero coefficient to \(1\). Exhausting every normalized dependence on at most four columns finds no dependence of sizes \(1,2,3\) and exactly one of size \(4\): on \(\{1,19,20,21\}\) the coefficients are \((1,2,2,2)\). Multiplication by \(2\) gives the only other weight-\(4\) dual word. Hence \(d(C^\perp)=4\) and the support \(\{1,19,20,21\}\) is the unique dependent four-set.

The MacWilliams transform of the independently enumerated \(W_C\) yields
\[
W_{C^\perp}(z)=1+2z^4+168z^7+2158z^9+12828z^{10}+39522z^{12}+159908z^{13}+202272z^{15}+504408z^{16}+236692z^{18}+348936z^{19}+49992z^{21}+36560z^{22}+804z^{24}+72z^{25}.
\]
Its coefficients sum to \(3^{13}\), as required because \(\dim C^\perp=13\). Finally, a monomial automorphism of \(C\) also preserves \(C^\perp\), Hamming weight, and supports up to coordinate permutation. Since the weight-\(4\) projective dual word has a unique support, that support must be stabilized setwise.

## Verification
`verify.py` contains the exact database matrix and uses only Python's standard library. It checks rank and self-orthogonality, exhausts all \(3^{12}\) words of \(C\), searches every normalized dual dependence on supports of size at most \(4\), computes the exact ternary MacWilliams transform, and compares all resulting coefficients with the stated enumerators. Running `python verify.py` returns `VERIFY_OK`; `verification_output.txt` records the replay output.

## Relationship to prior work
Araya--Harada prove that there are exactly 26 inequivalent ternary maximal self-orthogonal \([25,12,9]_3\) codes and publish generator matrices for all 26. Their Section 3.1 separately identifies the two extremal classes having dual distance \(1\), but the paper does not print the dual distance, low-weight dual multiplicity, or full weight enumerators of this second electronic representative. The electronic database supplies the matrix from which the present invariant is computed. Classical work of Mallows and Sloane gives general constraints on weight enumerators of ternary self-orthogonal codes; those constraints do not specify the code-dependent coefficients above or the unique four-coordinate circuit.

Searches for the exact parameter set, dual-distance phrase, low-weight spectrum, and equivalent dependent-column formulation found no indexed source stating this record-specific result. The closest published-finding corpus records concerned unrelated ternary deep-hole multiplicities, q-ary weight-gap phenomena, and ternary self-dual design constructions; none implies the stated enumerators or unique four-set.

## Limitations
The calculation is for one explicitly identified representative from the 26-code extremal database. It does not classify the dual distances or complete dual spectra of the other 25 classes. The originality comparison is limited to the inspected primary paper, its electronic database, relevant classical enumerator literature, current published-finding corpus records, and indexed web literature; an unindexed independent computation could in principle coincide. Independent audit has not been performed.

## References
1. M. Araya and M. Harada, *Classification of ternary maximal self-orthogonal codes of length 25*, arXiv:2605.13007, first public 2026-05-13.
2. M. Harada, electronic data file `25-12-9.txt`, accompanying the length-25 classification: https://www.math.is.tohoku.ac.jp/~mharada/T25/25-12-9.txt
3. C. L. Mallows and N. J. A. Sloane, *Weight Enumerators of Self-Orthogonal Codes over GF(3)*, SIAM Journal on Algebraic and Discrete Methods 2 (1981), 452--460, DOI 10.1137/0602048.
