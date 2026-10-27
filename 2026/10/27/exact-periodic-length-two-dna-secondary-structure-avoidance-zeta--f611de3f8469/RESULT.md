# Exact periodic length-two DNA secondary-structure-avoidance zeta function

## Finding

Let \(\mathcal A=\{0,1,2,3\}\), equipped with the Watson–Crick complement \(\overline a=3-a\). For any integer \(n\ge1\), a positioned word \(w=w_0\cdots w_{n-1}\in\mathcal A^n\) is **periodically 2-SSA** if its bi-infinite periodic extension does not contain two disjoint length-two factors that are reverse complements. Let \(c_n\) count such positioned words.

Define \(Z(z)=\exp(\sum_{n\ge1}c_nz^n/n)\). Then the **exact all-length** identity is

\[
\boxed{Z(z)=\frac{(1-2z)^8(1-z)^6(1+z)^2(1-z-z^4)^8}{(1-2z-z^2+z^3)^8(1-z-z^2)^8(1-z+z^2)^8(1+z^2)^2}.}
\]

Equivalently, with the right-hand side \(Z(z)=1/Q(z)\), the ordinary count series is \(\sum_{n\ge1}c_nz^n=-zQ'(z)/Q(z)\). The first eighteen counts, for \(n=1,\ldots,18\), are

\[
4,12,28,84,244,612,1460,3412,8020,18812,43916,101964,235876,543996,1251148,2870100,6568668,15002316.
\]

The number \(N_n\) of admissible necklaces (words up to cyclic rotation, without reflection or reverse complement identification) is

\[
\boxed{N_n=\frac1n\sum_{d\mid n}\varphi(d)c_{n/d}.}
\]

If \(\alpha\) is the unique real root of \(X^3-2X^2-X+1\) exceeding \(2\), then \(\alpha=1+2\cos(2\pi/7)\approx2.2469796037\) and

\[
\boxed{c_n=8\alpha^n+O(2^n),\qquad N_n\sim8\alpha^n/n.}
\]

Thus the known length-two secondary-structure-avoidance exponential capacity is sharpened to exact periodic counts, exact necklace counts, and a leading multiplicity of eight.

## Assumptions and scope

The alphabet is the labeled four-letter Watson–Crick alphabet, with complement pairs \(0\leftrightarrow3\) and \(1\leftrightarrow2\). A consecutive dinucleotide \((a,b)\) has reverse complement \(R(a,b)=(3-b,3-a)\). “Disjoint” means nonoverlapping occurrences in the **bi-infinite periodic extension**, not merely two disjoint arcs within a single traversal of a finite circle. In particular, a dinucleotide occurring once in the circle has arbitrarily many disjoint translates in its periodic extension. The counts distinguish the \(n\) positions, even when the least period divides \(n\).

The result is not a count of finite *linear* 2-SSA words, and the \(n<4\) values are intentionally governed by the periodic-extension convention. It is a combinatorial model of constraints maintained across indefinitely repeated DNA storage blocks or across a periodic sequence. No biochemical claim of perfect suppression of all physical stem-loop structures is made.

## Proof

**1. Exact forbidden-edge characterization.** Let \(E(w)=\{(w_i,w_{i+1\bmod n}):0\le i<n\}\). A word is periodically 2-SSA if and only if \(E(w)\) does not contain any self-reverse-complement dinucleotide and does not contain both members of any other reverse-complement pair. Indeed, any edge of \(E(w)\) occurs at positions shifted by all multiples of \(n\) in the periodic extension, so occurrences of any two selected edge types can be made disjoint. Conversely, any violating disjoint pair has edge labels in \(E(w)\).

There are exactly four self-dual edges \((0,3),(1,2),(2,1),(3,0)\). The remaining twelve edges form these six pairs, shown in a deterministic order:

\[
\begin{aligned}
P_1&=\{(0,0),(3,3)\},&P_2&=\{(0,1),(2,3)\},\\
P_3&=\{(0,2),(1,3)\},&P_4&=\{(1,0),(3,2)\},\\
P_5&=\{(1,1),(2,2)\},&P_6&=\{(2,0),(3,1)\}.
\end{aligned}
\]

**2. Signed decomposition into finite-type subshifts.** For a word that avoids the four self-dual edges, write \(I_e\) for the indicator that edge \(e\) is absent from \(E(w)\). For each pair \(\{e,f\}\), exactly the indicator identity

\[
\mathbf1[\text{not both }e,f\text{ present}]=I_e+I_f-I_eI_f
\]

holds. Multiply it over the six pairs. Expanding gives \(3^6=729\) terms. A term \(\sigma\in\{0,1,2\}^6\) excludes, for each pair, its first edge, its second edge, or both edges, respectively; let \(b(\sigma)\) count choices of “both”. Its sign is \((-1)^{b(\sigma)}\). Let \(A_\sigma\) be the \(4\times4\) zero-one adjacency matrix of the surviving edges. Every positioned period-\(n\) word traverses one unique length-\(n\) vertex-labelled closed walk; hence, for all \(n\ge1\),

\[
c_n=\sum_{\sigma\in\{0,1,2\}^6}(-1)^{b(\sigma)}\operatorname{tr}(A_\sigma^n).
\]

The identity \(\exp(\sum_{n\ge1}\operatorname{tr}(A^n)z^n/n)=\det(I-zA)^{-1}\) is a formal power-series identity. Consequently,

\[
Z(z)=\prod_{\sigma\in\{0,1,2\}^6}\det(I-zA_\sigma)^{-(-1)^{b(\sigma)}}.
\]

**3. Exact finite determinant certificate.** The 729 explicit \(4\times4\) determinants can be grouped by their polynomial \(P(z)=\det(I-zA_\sigma)\). Their nonzero signed multiplicities \(\mu(P)=\sum_{\sigma:\det(I-zA_\sigma)=P}(-1)^{b(\sigma)}\) are completely specified below; coefficient lists are given in increasing powers of \(z\). There are exactly 18 such entries (including the constant polynomial).

| Coefficients of \(P(z)\), low to high | \(\mu(P)\) |
|---|---:|
| \((1)\) | \(-1\) |
| \((1,-2)\) | \(-4\) |
| \((1,-2,-1,1)\) | \(8\) |
| \((1,-2,-1,3,-1)\) | \(8\) |
| \((1,-2,0,1)\) | \(-8\) |
| \((1,-2,0,2,-1)\) | \(-4\) |
| \((1,-2,1)\) | \(-4\) |
| \((1,-2,1,0,-1)\) | \(8\) |
| \((1,-1)\) | \(4\) |
| \((1,-1,-2)\) | \(-4\) |
| \((1,-1,-2,1)\) | \(-8\) |
| \((1,-1,-2,2)\) | \(-4\) |
| \((1,-1,-1)\) | \(8\) |
| \((1,-1,-1,1)\) | \(8\) |
| \((1,-1,0,0,-1)\) | \(-8\) |
| \((1,0,-2)\) | \(4\) |
| \((1,0,-1)\) | \(-4\) |
| \((1,0,0,0,-1)\) | \(2\) |

This is a finite exact certificate, not an extrapolation from initial coefficients. To reproduce it without libraries, enumerate \(\sigma\) lexicographically; place an entry \(1\) at each retained directed edge; evaluate \(\det(I-zA_\sigma)\) using the signed sum over all \(24\) permutations of four columns; and aggregate coefficient tuples with the specified signs. The supplied standalone `verify_periodic_ssa2.py` does exactly this and then checks the complete polynomial identity by integer polynomial multiplication (not by numerical factor-fitting). The signed product \(\prod_P P(z)^{\mu(P)}\) reduces identically to the reciprocal of the boxed expression for \(Z(z)\). Combining with step 2 proves the rational formula for every positive length.

**4. Necklaces and growth.** Rotation by \(j\) positions of a period-\(n\) word fixes exactly the words obtained by repeating a word of length \(\gcd(n,j)\); periodic 2-SSA is invariant under this repetition. Burnside's lemma yields the stated totient divisor sum. The reciprocal roots of \(1-2z-z^2+z^3\) are the three roots of \(X^3-2X^2-X+1\), with absolute values approximately \(2.24698,0.80194,0.55496\). All the other denominator/numerator factors in the boxed zeta function have reciprocal roots of modulus at most \(2\). The logarithmic derivative therefore gives \(c_n=8\alpha^n+O(2^n)\). Proper-period contributions to the divisor sum are \(O(n\alpha^{n/2})\), establishing the necklace asymptotic.

## Verification

The standalone Python 3 checker `verify_periodic_ssa2.py` uses only the standard library and performs four independent forms of arithmetic checking: the 729-case signed determinant aggregation, an exact cross-multiplied polynomial identity verifying the displayed rational function, coefficient comparison through \(n=45\), and direct enumeration of all \(4^n\) words for \(1\le n\le10\). It also checks the integer Burnside expression for \(1\le n\le24\). The full theorem for arbitrary lengths follows from the formal series identity and finite determinant certificate, not from testing finitely many word lengths.

The first twelve necklace counts are \(4,8,12,26,52,112,212,442,900,1912,3996,8570\) for lengths \(1\) through \(12\).

## Relationship to prior work

Nguyen, Cai, Kiah, Dao, and Immink (2023) establish the finite linear SSA-code motivation and constructions. Chu, Wang, and Zhang (2023), followed by Wang, Chu, Ge, and Zhang (2024), study length-two DNA SSA through compatible dinucleotide generating sets and obtain its optimal asymptotic rate (approximately \(1.1679\) bits per nucleotide). Their published capacity value is recovered here as \(\log_2\alpha\); it is not newly claimed. The finite-size zeta identity, its signed overlap correction, the all-length positioned counts, the necklace count, and the leading coefficient eight are the new claims. Optimizing a Perron root for one generating set does not determine the finite counts of the union of all compatible sets, because their cycle languages overlap.

Earlier exact enumeration of cyclic words avoiding *one local reverse-complement-duplication factor* concerns an unrelated local forbidden block \(ab\overline b\overline a\); the present constraint instead forbids simultaneous reverse-complement dinucleotide **types at any separation**. Neither statement implies the other. The 2024 journal article's accessible abstract concerns capacity and an added homopolymer restriction; its full text was not available for inspection, so unrecognized finite-length prior coverage remains a risk.

## Limitations

This is an idealized, infinitely periodic, loop-separation-free, stem-length-two model. It does not count words constrained only within one finite circular traversal; it does not impose an empirical minimum loop length, higher stem lengths, GC balance, read errors, or arbitrary substitutions. The explicit 2024 journal article was not fully inspected, and equivalent finite-length enumerations elsewhere cannot be excluded without broader expert literature review. The symbolic determinant proof and code have undergone self-review only; there is no independent audit or external formal proof certificate.

## References

1. T. T. Nguyen, K. Cai, H. M. Kiah, D. T. Dao, and K. A. Schouhamer Immink, *On the Design of Codes for DNA Computing: Secondary Structure Avoidance Codes*, arXiv:2302.13714, first publicly submitted 27 February 2023. https://arxiv.org/abs/2302.13714
2. H. Chu, C. Wang, and Y. Zhang, *Improved constructions of secondary structure avoidance codes for DNA sequences*, arXiv:2304.11403, first publicly submitted 22 April 2023. https://arxiv.org/abs/2304.11403
3. C. Wang, H. Chu, G. Ge, and Y. Zhang, *The Capacity of Secondary Structure Avoidance Codes for DNA Sequences*, IEEE Trans. Mol. Biol. Multi-Scale Commun. 10 (2024), 359–367, DOI:10.1109/TMBMC.2024.3396404. (Abstract consulted; complete journal text not inspected.)
