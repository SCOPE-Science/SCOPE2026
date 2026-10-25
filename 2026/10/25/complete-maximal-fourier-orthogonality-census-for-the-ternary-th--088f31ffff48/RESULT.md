# Complete maximal Fourier-orthogonality census for the ternary three-cube

## Finding

Let \(G=(\mathbb Z/6\mathbb Z)^3\) and \(D=\{0,1,2\}^3\subset G\). Write
\[
\chi_v(x)=\exp\bigl(2\pi i(v\cdot x)/6\bigr),\qquad v\in G,\quad x\in D.
\]
A subset \(\Lambda\subset G\) is *maximal orthogonal* when the restrictions \(\chi_v|_D\), for \(v\in\Lambda\), are pairwise orthogonal in \(\ell^2(D)\), but no frequency in \(G\setminus\Lambda\) can be added while maintaining that property. Distinct labeled frequency subsets are counted separately, without quotienting by symmetries.

**Exact census.** The complete distribution of maximal orthogonal families is

| Cardinality | Number of maximal families |
| ---: | ---: |
| 12 | 34,992 |
| 13 | 11,664 |
| 14 | 11,664 |
| 15 | 34,992 |
| 27 | 154,952 |

There are exactly **248,264** maximal families. Of these, exactly **93,312** are incomplete, with no possible incomplete size between 16 and 26; the 154,952 families of size 27 are orthogonal bases. In particular, the minimum cardinality of a maximal orthogonal family is exactly 12, rather than the dimension 27.

## Assumptions and scope

All statements concern the finite group \(G\), the 27-point set \(D\), the complete character-frequency grid consisting of all 216 residues, and counting measure on \(D\). Complex phases are the usual group characters, not arbitrary coefficient phases. Maximality means no *single additional character from this finite frequency grid* can be included; since pairwise orthogonality is hereditary, it is equivalent to inclusion-maximality. The result does not concern arbitrary frequencies in \(\mathbb R^3\).

## Proof

Put \(\zeta=\exp(2\pi i/6)\). For distinct \(v,w\in G\), the unnormalized character inner product factors exactly:
\[
\langle\chi_v,\chi_w\rangle_{\ell^2(D)}
=\prod_{j=1}^{3}\bigl(1+\zeta^{v_j-w_j}+\zeta^{2(v_j-w_j)}\bigr).
\]
The factor vanishes if and only if \(\zeta^{v_j-w_j}\) is a nontrivial cube root of unity, equivalently \(v_j-w_j\equiv 2\) or \(4\pmod6\). Therefore construct the **integer-defined graph** \(H\) whose 216 vertices are the ordered triples with coordinates 0 through 5, with an edge between \(v\ne w\) exactly when at least one coordinate difference is 2 or 4 modulo 6. Mutual orthogonality of a frequency family is equivalent to being a clique in \(H\); maximal orthogonality is equivalent to being a maximal clique.

The bundled file `verify.py` constructs this adjacency without floating-point arithmetic, using only integer residues. It exhaustively visits all maximal cliques via the pivoted Bron--Kerbosch recursion. For a current clique \(R\), its two disjoint sets \(P\) and \(X\) are respectively the vertices that may be appended and the vertices already considered at this depth; all of them are adjacent to every vertex of \(R\). Each step chooses a pivot \(u\in P\cup X\), branches over every \(v\in P\setminus N(u)\), and recurses with \(R\cup\{v\}\), \(P\cap N(v)\), and \(X\cap N(v)\). A terminal branch with \(P=X=\varnothing\) records one maximal clique.

For completeness of this search, every as-yet-unreported maximal clique containing \(R\) must contain a member of \(P\setminus N(u)\): if not, the clique would be either extendible by the pivot or already covered through \(X\). Thus the branch set covers all new maximal extensions. Moving each explored candidate from \(P\) to \(X\) avoids duplicate reports. Induction on the remaining candidate set proves that every maximal clique is reported once and only once. All input vertices and all branches are finite, and the exact Python program computes an integer counter for each resulting size.

The full exhaustive run has 1,951,000 recursion calls for \(q=3\) and dimension three, and reports 34,992, 11,664, 11,664, 34,992, and 154,952 maximal cliques for sizes 12, 13, 14, 15, and 27, respectively. No branches are sampled or truncated; the program terminates after exhausting its search tree. Every 27-element clique is an orthogonal basis, since \(\dim\ell^2(D)=27\). Every smaller maximal clique is an incomplete unextendible family. Summation yields the asserted totals and strict gap.

## Verification

Run `python3 verify.py` from the extracted bundle; this requires the Python standard library only. The file `verification_output.txt` supplies the recorded output. It includes exact low-dimensional controls, confirms one sample clique for each occurring cardinality is both pairwise orthogonal and not extendible, and checks the entire distribution.

A separately implemented full enumeration with `networkx.find_cliques` is reproducible by `crosscheck.py` (requires NetworkX 3.6.1), whose recorded output is `crosscheck_output.txt`. It independently returned a 216-vertex, 16,416-edge graph with exactly 248,264 maximal cliques and the same five-entry size distribution. This secondary implementation is a cross-check, not a replacement for the exhaustive-search proof. The exact enumeration is a finite theorem, not evidence for an unbounded dimension statement.

## Relationship to prior work

Kolountzakis--Lev--Matolcsi (first public version October 16, 2024) study when maximal orthogonal exponential sets for continuous cubes may be incomplete, and give finite-group examples based on products of distinct prime squares. Their statements establish the conceptual question but do not provide the five-entry maximal-clique distribution for the specified ternary finite digit cube. Agora--Grepstad--Kolountzakis determine when full spectra of finite cyclic-group cubes correspond to tiling complements; a classification of *complete* spectra does not imply the enumerated cardinalities and multiplicities of maximal **incomplete** families. Dutour Sikirić--Itoh study related cube packings on a different torus graph with antipodal coordinate differences; its orthogonality graph is not the present one. The earlier Łysakowska--Przesławski work gives a structural classification of unextendible unit-cube systems in dimension three, but its full text was unavailable during the comparison; possible consequences for this finite numerical census are an explicit unresolved bibliographic risk.

## Limitations

This is a fixed finite-dimensional exact census; it does not imply a formula for general digit widths, dimensions, or moduli. Counts depend on including all 216 labeled frequencies and are not symmetry-orbit counts. The all-maximal-family computation is independently replayable, but the exact numerical census does not by itself prove new structural implications for continuous cube packings. No independent outside scientific audit has been performed. Complete priority over older packings literature is not asserted.

## References

- M. N. Kolountzakis, N. Lev, and M. Matolcsi, *Maximality and completeness of orthogonal exponentials on the cube*, arXiv:2410.12387, first submitted October 16, 2024, especially §§4, 7 and the note added in proof.
- E. Agora, S. Grepstad, and M. N. Kolountzakis, *Spectra for cubes in products of finite cyclic groups*, arXiv:1602.03165; Proc. Amer. Math. Soc. 146 (2018), 2417–2423.
- M. Dutour Sikirić and Y. Itoh, *Combinatorial cube packings in cube and torus*, arXiv:0805.2493, especially §§2 and 5.
- M. Łysakowska and K. Przesławski, *On the structure of cube tilings and unextendible systems of cubes in low dimensions*, European J. Combin. 32 (2011), 1417–1427, doi:10.1016/j.ejc.2011.07.003 (bibliographic description and abstract; full paper not inspected).
