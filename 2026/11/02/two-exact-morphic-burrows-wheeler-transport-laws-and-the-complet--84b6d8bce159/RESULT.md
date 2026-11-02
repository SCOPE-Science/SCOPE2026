# Two exact morphic Burrows–Wheeler transport laws and the complete Chacon transform

## Finding
For every nonempty binary word \(v\), let \(\mathcal B(v)\) denote its **circular**, sentinel-free Burrows–Wheeler transform: sort its cyclic rotations lexicographically with \(0<1\), then concatenate the symbols preceding their starting positions. Write \(z=|v|_0\) and \(o=|v|_1\). For the morphisms
\[
\tau(0)=010,\quad\tau(1)=011,\qquad
\eta(0)=0,\quad\eta(1)=01,
\]
we obtain the **universal identities**
\[
\boxed{\mathcal B(\tau(v))=1^z\,\mathcal B(v)\,0^z1^o0^o,\qquad
\mathcal B(\eta(v))=\mathcal B(v)0^o.}
\]
Now set \(\sigma(0)=0010\), \(\sigma(1)=1\) and \(C_n=\sigma^n(0)\) for each integer \(n\ge0\). Then \(\mathcal B(C_0)=0\), \(\mathcal B(C_1)=1000\), and \(\mathcal B(C_n)\) has **exactly \(2n\) equal-symbol runs for all \(n\ge1\)**. Furthermore, for every \(n\ge2\), its entire transform is the explicit run-length word
\[
\boxed{\mathcal B(C_n)=1^{(3^n+2n-1)/4}
 \left(\prod_{j=1}^{n-1}0^{d_j}1^{(3^j-1)/2}\right)
 0^{2\cdot3^{n-1}-1},\qquad
 d_1=4,\quad d_j=2\cdot3^{j-1}\ (j\ge2).}
\]
The product is concatenation in increasing \(j\), not ordinary multiplication. In particular \(|C_n|=(3^{n+1}-1)/2\).

## Assumptions and scope
The alphabet is \(\{0,1\}\), ordered \(0<1\); \(v\ne\varepsilon\) may be periodic. A cyclic rotation starts at an indexed position and its predecessor is the symbol at the previous indexed position modulo the word length. Identical rotation strings may be ordered arbitrarily, because their predecessor symbols coincide (the periodic rotations of a word have identical preceding symbols). No unique terminal symbol is inserted. Superscripts on letters mean repetition; \(\prod\) is ordered concatenation. All claims are exact for the stated integer ranges.

## Proof
**Lemma 1 (uniform transport).** Let \(v=v_0\cdots v_{m-1}\), indices cyclically modulo \(m\). Every cyclic rotation of \(\tau(v)\) begins at exactly one of three positions within a codeword. Partition those rotations according to their first codeword position and, for interior positions, the corresponding input bit. In lexicographic order the five disjoint groups have initial prefixes \(001\), \(01\), \(100\), \(101\), \(110\). Specifically:

- The third position of a \(\tau(0)=010\) block starts \(001\), and the preceding letter is \(1\). There are \(z\) such rows.
- A block-boundary row starts \(01\). The map \(v_i v_{i+1}\ldots\mapsto\tau(v_i v_{i+1}\ldots)\) preserves lexicographic order for periodic infinite strings because the images \(010\) and \(011\) first differ at their third symbol. The preceding letter is \(v_{i-1}\), so the last-column segment is exactly \(\mathcal B(v)\).
- The second position of a \(\tau(0)\) block starts \(100\), has predecessor \(0\), and occurs \(z\) times.
- The third position of a \(\tau(1)=011\) block starts \(101\), has predecessor \(1\), and occurs \(o\) times.
- The second position of a \(\tau(1)\) block starts \(110\), has predecessor \(0\), and occurs \(o\) times.

These initial prefixes separate all five classes, proving \(\mathcal B(\tau(v))=1^z\mathcal B(v)0^z1^o0^o\). This reasoning also handles repeated letters and periodic input.

**Lemma 2 (nonuniform transport).** Every \(\eta\)-block starts with zero. The rows of \(\eta(v)\) starting at codeword boundaries therefore all begin with zero, whereas the single internal position of an \(\eta(1)=01\) block starts with one and has predecessor zero. The internal rows are last in lexicographic order and contribute \(0^o\). Among boundary rows, the order is inherited from the cyclic shifts of \(v\): for unequal first input symbols, the corresponding encoded periodic strings begin \(00\) and \(01\), respectively; after equal symbols, remove their common encoded block and compare again. The predecessor of a boundary row is the final symbol of the previous block, namely \(v_{i-1}\). Thus boundary rows contribute \(\mathcal B(v)\), establishing \(\mathcal B(\eta(v))=\mathcal B(v)0^o\).

**Application to Chacon iterates.** Directly on both input letters, \(\eta\circ\tau=\sigma\circ\eta\), because \(\eta(010)=0010\) and \(\eta(011)=00101\), while \(\sigma(01)=00101\). Also \(\eta(0)=0\). Hence \(C_n=\eta(H_n)\) for \(H_n=\tau^n(0)\). Put \(U_n=\mathcal B(H_n)\), \(z_n=|H_n|_0\), \(o_n=|H_n|_1\). Each application of \(\tau\) triples length and preserves the difference of symbol counts, so
\[
 z_n=(3^n+1)/2,\qquad o_n=(3^n-1)/2.
\]
The two transport laws give, with \(U_0=0\),
\[
 U_{n+1}=1^{z_n}U_n0^{z_n}1^{o_n}0^{o_n},\qquad
 \mathcal B(C_n)=U_n0^{o_n}.
\]
Here \(U_1=100\). Every \(U_n\) for \(n\ge1\) begins with one and ends with zero. For \(n\ge1\), its transition to \(U_{n+1}\) extends its leading one-run and trailing zero-run, then appends one new positive one-run and one positive zero-run. Thus the number of runs grows by two from the two runs of \(U_1\). Appending \(0^{o_n}\) does not change this count.

For completeness, the first run of \(U_n\) has length \(a_1=1\) and \(a_{n+1}=a_n+z_n\), hence \(a_n=(3^n+2n-1)/4\). The zero-runs between successive interior one-runs are \(d_1=4\) and \(d_j=2\cdot3^{j-1}\) for \(j\ge2\): this follows by iterating the displayed recurrence, because the current last zero-run merges with the next \(0^{z_n}\) before the new \(1^{o_n}\) is inserted. The positive one-run inserted at stage \(j\) has length \(o_j=(3^j-1)/2\); after the final \(0^{o_n}\) is appended via \(\eta\), the terminal zero-run has length \(2\cdot3^{n-1}-1\) for \(n\ge2\). This proves the explicit concatenation expression and its stated exceptions at ranks zero and one. Finally, \(|C_n|=|H_n|+o_n=(3^{n+1}-1)/2\). \(\square\)

## Verification
The attached standalone `checker.py` reconstructs the cyclic rotations without relying on a BWT library, exhaustively verifies both universal morphic identities over every nonempty binary word of lengths one through nine (\(1022\) inputs), and compares the complete Chacon BWT expression and run counts through rank seven, including the separate ranks zero and one. All these checks passed. They are corroboration, **not** the infinite proof, which is the two lemmas and the induction above. Run it with `python3 checker.py`.

## Relationship to prior work
Currie, Rampersad, Saari and Zamboni (2013) investigate lexicographically extremal infinite words in morphic subshifts and specifically the Chacon word (their Section 7); the finite rotation-order partition and circular BWT formula above are different conclusions. Frosini, Mancini, Rinaldi, Romana and Sciortino (2022) establish logarithmic upper bounds and broad matching lower bounds for BWT run counts of binary purely morphic words. Those bounds alone do not give the exact \(2n\) law or the complete transformed string. Searches of the cited sources, relevant published research records, and accessible earlier claim summaries did not identify an implication covering both transport laws or this Chacon classification. Absence from searches is not a proof of historical novelty.

## Limitations
This uses the sentinel-free circular BWT, not the sentinel-terminated transform; its exact Chacon formula concerns complete substitution iterates, not arbitrary prefixes. The universal transport laws apply to all finite nonempty binary words for the two specified morphisms. Independent mathematical validation and exhaustive historical-priority review have not been performed.

## References
1. James D. Currie, Narad Rampersad, Kalle Saari, Luca Q. Zamboni, *Extremal words in morphic subshifts*, arXiv:1301.4972, publicly available 2013-01-21. https://arxiv.org/abs/1301.4972
2. Andrea Frosini, Ilaria Mancini, Simone Rinaldi, Giuseppe Romana, Marinella Sciortino, *Logarithmic equal-letter runs for BWT of purely morphic words*, arXiv:2202.02609, 2022. https://arxiv.org/abs/2202.02609
