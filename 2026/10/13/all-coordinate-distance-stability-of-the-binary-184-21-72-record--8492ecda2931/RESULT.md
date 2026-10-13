# All-coordinate distance stability of the binary \( [184,21,72] \) record code
## Finding
For the explicit binary \( [184,21,72] \) code \(C\) specified in Appendix A of Seddas--Shashkov--Viazovska--Abbe, exhaustive reconstruction gives exactly 9,826 words of weight \(72\). If \(r_j\) is the number of those minimum words containing coordinate \(j\), then the multiset of the 184 values is
\[
\{2108^1,2346^2,2482^2,2516^3,2550^6,3940^{17},3956^{17},3958^{102},3968^{34}\}.
\]
Thus every coordinate occurs in at least one and in fewer than all minimum words. It follows that every one-coordinate puncture has parameters \( [183,21,71] \), and every one-coordinate shortening has parameters \( [183,20,72] \). The minimum supports are therefore not a 1-design, but the code has uniform one-coordinate distance behavior despite strongly nonuniform minimum-support incidence.

## Assumptions and scope
The object is exactly the printed \( [184,21,72] \) construction over \(\mathbb F_2\): block length \(m=85\), dimension \(21\), the four printed factors of \(h\), \(g=(x^{85}-1)/h\), \(f_1=1\), the printed polynomial \(f_2\), and the fourteen printed five-bit tail patterns. Arithmetic uses \(x^{85}=1\). The conclusion concerns this one explicit code, not all codes with the same parameters and not all outputs of the construction scheme.

## Proof
For \(b\in\mathbb F_2[x]\) with \(\deg b<21\), reconstruct the two cyclic blocks as \(bg\) and \(bgf_2\bmod(x^{85}-1)\), and the fourteen tail coordinates as the printed linear forms evaluated on \(b\bmod(x^5-1)\). The first block has degree below \(85\), so multiplication by the nonzero polynomial \(g\) is injective on this 21-dimensional message space. Hence the reconstructed code has dimension \(21\).

Enumerating all \(2^{21}-1\) nonzero messages gives minimum weight \(72\), exactly 9,826 minimum words, and the complete weight distribution printed by the source. Counting, for each of the 184 coordinates, how many of those 9,826 words contain that coordinate gives the displayed nine-valued incidence multiset. As a consistency check, the incidence sum is \(72\cdot 9826=707472\).

Fix a coordinate \(j\). Since \(r_j>0\), some weight-72 word has a 1 at \(j\); puncturing there produces weight \(71\). Puncturing cannot lower any nonzero weight by more than one, so the punctured minimum distance is exactly \(71\). Its dimension remains \(21\), because a dimension drop would require a nonzero codeword supported only at \(j\), impossible when the original minimum distance is \(72\).

Since \(r_j<9826\), some minimum word has a 0 at \(j\), so it survives shortening with weight \(72\). The shortening is a subcode of \(C\), hence has minimum distance at least \(72\), and therefore exactly \(72\). Because \(r_j>0\), the \(j\)-th coordinate functional is nonzero on \(C\), so its kernel has dimension \(20\). These arguments hold for every \(j\).

## Verification
The accompanying `verify.py` reconstructs the code from the published algebraic data, exhausts all messages by Gray-code traversal, checks the source weight distribution, recomputes the minimum-support incidence spectrum, verifies the identity \(\sum_j r_j=72\cdot9826\), and checks \(0<r_j<9826\) for all coordinates. The finite exhaustive computation establishes the stated facts for this explicit finite code only.

## Relationship to prior work
The source establishes the new \( [184,21,72] \) record code, gives its quasi-cyclic description and global weight distribution, and notes that standard code modifications propagate record improvements. A global weight enumerator does not determine the coordinatewise incidence numbers \(r_j\), and a generic puncturing or shortening argument does not imply that *every* coordinate has the claimed exact outcome. Searches by the exact parameters, support-incidence terminology, design terminology, and all-coordinate puncturing/shortening formulations found no prior statement of the nine-valued spectrum or the universal one-coordinate conclusion. CodeTables records code parameters and constructions rather than this minimum-support incidence invariant.

## Limitations
This is a finite structural census for one newly published code. It does not determine higher support-design parameters, the full automorphism group, multi-coordinate puncturing/shortening behavior, or analogous spectra for the other record codes. The source's released construction data make independent recomputation possible, so an unindexed companion analysis could in principle contain the same invariant; none was located in the checked sources.

## References
1. A. Seddas, V. Shashkov, M. Viazovska, E. Abbe, *Evolving Towards Better Codes: LLM-Guided Search for High-Distance Binary Linear Codes*, arXiv:2609.37056, first public 2026-09-29.
2. M. Grassl, *Bounds on the minimum distance of linear codes*, CodeTables, https://codetables.de/.
