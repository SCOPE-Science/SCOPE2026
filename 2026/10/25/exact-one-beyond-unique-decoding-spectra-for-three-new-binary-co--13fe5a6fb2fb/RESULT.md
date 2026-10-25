# Exact one-beyond-unique-decoding spectra for three new binary codes

## Finding
Let \(C_{22}\), \(C_{24}\), and \(C_{25}\) denote the exact binary codeword sets printed in Section 4 of Ota--Osa--Harada (arXiv:2610.11609), with respective length, cardinality, and minimum Hamming distance \((22,84,9)\), \((24,196,9)\), and \((25,65,11)\). Their integer-form codeword lists are reproduced in `verify_list_profiles.py`.

For each \(C\subseteq\{0,1\}^n\), radius \(r\), and \(j\ge0\), put
\[
N_j(C,r)=\#\{y\in\{0,1\}^n:\#\{c\in C:d_H(y,c)\le r\}=j\}.
\]
The complete spectra, at **one error beyond the respective guaranteed unique-decoding radii**, are:

| Code | Radius | \(N_0\) | \(N_1\) | \(N_2\) | \(N_3\) | \(N_4\) | \(N_{\ge5}\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| \(C_{22}\) | 5 | 1,716,840 | 1,998,088 | 459,012 | 20,356 | 8 | 0 |
| \(C_{24}\) | 5 | 7,665,396 | 7,433,580 | 1,599,216 | 78,928 | 96 | 0 |
| \(C_{25}\) | 6 | 18,981,285 | 13,205,369 | 1,350,813 | 16,965 | 0 | 0 |

Thus the largest radius-5 lists for \(C_{22}\) and \(C_{24}\) have size four; the largest radius-6 list for \(C_{25}\) has size three. These assertions concern these three particular codebooks, not all codes with the same parameters.

## Assumptions and scope
Binary Hamming distance is \(d_H(u,v)=\#\{i:u_i\ne v_i\}\); the integer decimal lists in the accompanying standalone checker are interpreted as length-\(n\) binary words padded with leading zero bits. The three codebooks are the published, explicitly listed sets, with no linearity assumption. Decoder lists include all codewords at distance at most \(r\) from a received word; the received space is the full uniform binary Hamming cube. No probability model for a transmitted codeword is assumed.

## Proof
First, a structural lemma for any binary code with minimum distance at least \(2r-1\), with \(r\ge1\). For a fixed received word \(y\), the error sets \(E_c=\{i:y_i\ne c_i\}\), for \(c\in C\cap B_r(y)\), have size at most \(r\). Any two are disjoint: otherwise their symmetric-difference distance would be at most \(2r-2\). Consequently every pair of codewords that can share an \(r\)-ball center lies at distance \(2r-1\) or \(2r\). Conversely, at either distance the intersection of their radius-\(r\) balls has exactly \(\binom{2r}{r}\) centers. Indeed, the center must agree outside their differing coordinates, and the differing coordinates must be divided into parts of sizes \(r\) and \(r-1\), or \(r\) and \(r\), respectively.

For any three distinct codewords with all three pair distances in \(\{2r-1,2r\}\), their unique simultaneous radius-\(r\) center is the coordinatewise majority word \(\operatorname{maj}(a,b,c)=(a\land b)\lor(a\land c)\lor(b\land c)\), with bitwise operations on length-\(n\) words. Uniqueness follows because all error supports relative to any common center must be pairwise disjoint. Existence follows by writing the majority-to-codeword distances as half of sums and differences of the three pair distances. Their sum is even (each coordinate contributes zero or two), so either all three pair distances equal \(2r\), giving distances \((r,r,r)\) from the majority, or exactly two equal \(2r-1\), giving some permutation of \((r,r-1,r-1)\).

Let \(G\) be the graph on the published codewords with an edge exactly when their distance is at most \(2r\). Write \(E\) for its number of edges, \(T\) for its number of triangles, and \(Q\) for the number of its four-vertex cliques whose first three vertices' majority is within radius \(r\) of the fourth. The preceding lemma shows that \(E,T,Q\) are exactly the second-, third-, and fourth-order list-incidence moments up to the known pair intersection factor:
\[
\sum_y\binom{L(y)}1=|C|\sum_{i=0}^r\binom ni,\quad
\sum_y\binom{L(y)}2=E\binom{2r}{r},\quad
\sum_y\binom{L(y)}3=T,\quad
\sum_y\binom{L(y)}4=Q,
\]
where \(L(y)=|C\cap B_r(y)|\). Each qualifying four-clique has exactly one center, necessarily the majority of any three of its vertices. Its candidate is counted once because vertices are indexed in increasing order.

The complete, exhaustive finite graph computations from the given codeword lists yield:

| Code | Minimum distance checked | \(E\) | \(T\) | \(Q\) | Distinct qualifying four-clique centers |
|---|---:|---:|---:|---:|---:|
| \(C_{22}\) | 9 | 2,064 | 20,388 | 8 | 8 |
| \(C_{24}\) | 9 | 7,288 | 79,312 | 96 | 96 |
| \(C_{25}\) | 11 | 1,517 | 16,965 | 0 | 0 |

These counts and the distinctness assertions follow from explicit integer-arithmetic enumeration in `verify_list_profiles.py`. The loops enumerate every unordered pair, every increasing-index triangle of \(G\), and every increasing-index four-clique. Each codeword set's claimed size and minimum distance are also recomputed. The distinctness of all \(Q\) qualifying centers excludes lists of size five or greater: such a list would generate at least five four-cliques with the same center, contradicting distinctness. For \(Q=0\), lists of size four or greater are immediately excluded.

With no lists beyond size four, the four moments plus \(\sum_{j=0}^4 N_j=2^n\) are an upper-triangular integer system. Solve in descending order:
\[
N_4=Q,\quad N_3=T-4Q,\quad
N_2=E\binom{2r}{r}-3N_3-6N_4,\quad
N_1=|C|\sum_{i=0}^r\binom ni-2N_2-3N_3-4N_4,
\]
followed by \(N_0=2^n-N_1-N_2-N_3-N_4\). Substituting the verified edge, triangle, and four-clique counts gives precisely the table in the Finding section. This completes the exact finite proof.

## Verification
Run `python3 verify_list_profiles.py` with Python 3.10 or newer. It uses only the Python standard library and prints `VERIFY_OK` after checking the entire computation and each expected spectrum. In addition to the small-clique enumeration, independent full-cube Hamming-ball accumulation was performed for each code and reproduced all three reported spectra; the standalone proof does not depend on that auxiliary accumulation. The checker needs no internet, external data files, third-party packages, or randomized inputs.

## Relationship to prior work
Ota, Osa and Harada (arXiv:2610.11609, first public version October 8, 2026) give the three explicit codebooks and establish their sizes and minimum distances. Section 4 includes the complete integer lists but neither the radius-5/radius-6 list-size distributions nor the higher-order codeword-incidence counts above. Brouwer's general binary-code bounds table addresses maximum code sizes, not these precise received-word multiplicities. The new finite computation concerns a decoding property immediately beyond guaranteed unique correction, and the majority-center lemma reduces an apparently full-cube census to low-order cliques. The published codeword lists determine these quantities in principle; the new claim is the explicit, checked exact spectra and their structural certificate, not priority over the underlying code constructions.

## Limitations
Only the three specified codebooks and their indicated radii are covered. No statement is made about optimality of their list sizes among all binary codes with matching length, size, and distance. Full numerical spectra are exhaustive finite facts, not consequences of an asymptotic theorem. The result does not give a bound on block-error probability for a particular communication channel without an additional input/noise distribution. Earlier independently unpublished calculations of the same spectra could exist.

## References
1. K. Ota, T. Osa and T. Harada, *Three Improved Lower Bounds for Binary Error-Correcting Codes*, arXiv:2610.11609, first submitted October 8, 2026, Sections 1--4, https://arxiv.org/abs/2610.11609.
2. A. E. Brouwer, *Small binary codes: Table of general binary codes*, https://aeb.win.tue.nl/codes/binary-1.html.
