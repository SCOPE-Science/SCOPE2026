# Exact quaternary length-five symbol-weight code at distance four
## Finding
Let the alphabet be \(Q=\{0,1,2,3\}\). The symbol weight of a word \(x\in Q^5\) is the largest multiplicity of a symbol in \(x\). Let \(A^{\mathrm{SW}}_4(5,4,2)\) be the largest size of a code \(C\subseteq Q^5\) in which every word has symbol weight exactly \(2\) and every two distinct words have Hamming distance at least \(4\). Since \(\lceil 5/4\rceil=2\), the conditions “symbol weight exactly \(2\)” and “symbol weight at most \(2\)” define the same feasible words.

Then
\[
A^{\mathrm{SW}}_4(5,4,2)=15.
\]
A maximum code is
\[
\begin{aligned}
C=\{&33221,32312,31030,30103,22001,23132,21323,20210,\\
&13300,12233,10022,03013,02120,01202,00331\}.
\end{aligned}
\]
In addition, every maximum code has the following forced structure: every codeword has composition type \((2,2,1,0)\), and for every two coordinate positions the projection of the code onto those positions contains \(15\) distinct ordered pairs and omits exactly one diagonal pair \((a,a)\).

## Assumptions and scope
Only Hamming distance and the symbol-weight restriction are used. The alphabet symbols are labels; no field structure is assumed. The structural assertion applies to every size-
\(15\) code satisfying the stated conditions. It does not classify maximum codes up to equivalence.

## Proof
Distance at least \(4\) in length \(5\) means that two distinct codewords agree in at most one coordinate. Hence projection onto any chosen pair of coordinates is injective. Since a two-coordinate projection takes values in \(Q^2\), the Singleton argument gives \(|C|\le 16\).

Suppose first that \(|C|=16\). For any fixed pair of coordinate positions, injectivity makes the projection a bijection onto all \(16\) ordered pairs in \(Q^2\). Exactly four of those pairs are diagonal, so across all \(\binom{5}{2}=10\) coordinate pairs there are exactly \(40\) incidences \((x,\{i,j\})\) with \(x_i=x_j\).

A length-five word of symbol weight at most \(2\) can have only composition type \((2,2,1,0)\) or \((2,1,1,1)\). Such a word contributes respectively \(2\) or \(1\) equal-coordinate pairs, hence at most \(2\). Thus \(16\) codewords contribute at most \(32\) equal-coordinate incidences, contradicting the required \(40\). Therefore \(|C|\le 15\).

The displayed set \(C\) has \(15\) distinct words, every word has symbol weight \(2\), and direct comparison shows that every two distinct words have Hamming distance at least \(4\). Hence \(|C|=15\) is attainable.

For the structural statement, let \(|C|=15\). Each two-coordinate projection is injective and therefore misses exactly one of the \(16\) ordered pairs. Consequently it contains at least three of the four diagonal pairs. Summed over the ten coordinate pairs, the code therefore has at least \(30\) equal-coordinate incidences. On the other hand, each codeword contributes at most \(2\), so there are at most \(30\). Equality holds throughout. Hence every codeword contributes exactly two equal-coordinate pairs, forcing composition type \((2,2,1,0)\), and every two-coordinate projection contains exactly three diagonal pairs. Its unique missing ordered pair is therefore diagonal.

## Verification
The accompanying `verify.py` checks the displayed witness directly: length, alphabet, distinctness, symbol weight, all pairwise distances, all ten two-coordinate projections, and the equal-coordinate incidence count. It also checks the integer counts used in the upper-bound and equality-case arguments. Running it prints `VERIFY_OK maximum=15 witness=15 projections=10 equal_incidence=30 missing_diagonal=11`.

## Relationship to prior work
Chee, Kiah, and Purkayastha introduced the constant and bounded symbol-weight spaces and the notation for their optimal code sizes, and explicitly identified finite optimal-code size and construction questions as a combinatorial direction. Their full text develops general upper and lower bounds and gives larger-parameter non-asymptotic examples, but it does not state the quaternary \((5,4,2)\) value considered here. Chee, Kiah, and Wang later used exact finite symbol-weight-code questions in their equivalence with generalized balanced tournament designs, including a clique computation for a different ternary parameter set. The present result is a small exact boundary instance: the unrestricted Singleton value \(16\) is impossible solely because of symbol multiplicity, and the deficit is exactly one.

## Limitations
No enumeration or equivalence classification of all maximum size-
\(15\) codes is claimed. The literature search cannot exclude an obscure or unindexed prior computation of this exact small parameter. The proof is specific to \(q=4\), length \(5\), distance \(4\), and symbol weight \(2\); it is not asserted as a general formula.

## References
[1] Y. M. Chee, H. M. Kiah, and P. Purkayastha, “Estimates on the Size of Symbol Weight Codes,” arXiv:1110.0911v1, first submitted 2011-10-05; later IEEE Transactions on Information Theory 59(1), 301–314.

[2] Y. M. Chee, H. M. Kiah, and C. Wang, “Generalized Balanced Tournament Designs with Block Size Four,” Electronic Journal of Combinatorics 20(2) (2013), Paper P51.
