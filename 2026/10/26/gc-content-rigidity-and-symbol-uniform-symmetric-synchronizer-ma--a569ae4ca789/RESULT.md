# GC-content rigidity and symbol-uniform symmetric synchronizer markers

## Finding
Consider the four-letter alphabet \(\Sigma=\{0,1,2,3\}\) with Watson–Crick complement \(\overline{0}=1\), \(\overline{1}=0\), \(\overline{2}=3\), and \(\overline{3}=2\). The letters \(0,1\) represent the A/T class, and \(2,3\) the C/G class. A marker lookup table is a function \(f:\Sigma^2\to\Sigma\). Call it *admissible* when, for every ordered pair \((a,b)\),
\[
f(a,b)\notin\{a,b\},\qquad
f(\overline a,\overline b)\ne\overline{f(a,b)}.
\]
These are the four-letter synchronizer-table constraints introduced in the cited 2026 construction.

Define \(G(f)=|\{(a,b)\in\Sigma^2:f(a,b)\in\{2,3\}\}|\). Define *symbol-uniform* to mean that each element of \(\Sigma\) appears exactly four times in the sixteen entries. Define *transpose-symmetric* by \(f(a,b)=f(b,a)\) for every ordered pair.

**Theorem (joint GC and symbol-balance spectrum).** Across all admissible tables on this fixed labeled alphabet, \(G(f)\) can only be \(7,8,9\), and the respective numbers of tables are
\[
\#\{f:G(f)=7\}=512,\quad
\#\{f:G(f)=8\}=1280,\quad
\#\{f:G(f)=9\}=512.
\]
Exactly \(80\) admissible tables are symbol-uniform; of those, exactly \(16\) are also transpose-symmetric. Each of these sixteen is in particular exactly GC-balanced, and the class is nonempty.

The previously established unweighted total \(2304\) is used as a consistency baseline, **not** claimed as a new result. All counts are for distinct labeled lookup tables; no relabeling, reversal, or other equivalence is factored out.

## Assumptions and scope
The field realization \(\mathbb F_4=\{0,1,\omega,\omega+1\}\) corresponds to the displayed alphabet by identifying \(2=\omega\), \(3=\omega+1\); adding field \(1\) is the complement involution. No further field algebra is needed. There are precisely sixteen equally weighted *possible input pairs* for the lookup table. If these pairs are uniformly distributed, the inserted marker lies in the C/G class with probability \(G(f)/16\), hence within \(1/16\) of one half for every admissible table. This is a statement about the lookup table under uniformly sampled flanks, not a claim that arbitrary encoded DNA strands or arbitrary input codes have exactly balanced GC content. Transpose symmetry concerns the lookup rule alone, not the entire block code.

## Proof
The involution \(T(a,b)=(\overline a,\overline b)\) has eight orbits of size two on the ordered pairs. Fix an orbit \(\{(a,b),(\overline a,\overline b)\}\). If its outputs are \((c,d)\), admissibility means
\[
c\notin\{a,b\},\quad d\notin\{\overline a,\overline b\},\quad d\ne\overline c.
\]
There are no conditions linking different orbits. We can list the orbit representatives, then list **all** permitted ordered outputs. This is a complete enumeration because each original input pair lies in one of the eight orbits:

| Input orbit representatives | All possible ordered outputs \((c,d)\) |
| --- | --- |
| \((0,0)\), \((1,1)\) | \((1,2),(1,3),(2,0),(2,2),(3,0),(3,3)\) |
| \((0,1)\), \((1,0)\) | \((2,2),(3,3)\) |
| \((0,2)\), \((1,3)\) | \((1,2),(3,0)\) |
| \((0,3)\), \((1,2)\) | \((1,3),(2,0)\) |
| \((2,0)\), \((3,1)\) | \((1,2),(3,0)\) |
| \((2,1)\), \((3,0)\) | \((0,2),(3,1)\) |
| \((2,2)\), \((3,3)\) | \((0,0),(0,2),(1,1),(1,2),(3,0),(3,1)\) |
| \((2,3)\), \((3,2)\) | \((0,0),(1,1)\) |

The two off-diagonal same-class orbits contribute exactly two and zero C/G-valued outputs, respectively; the four mixed-class orbits contribute one each. Thus these six orbits contribute six C/G outputs in every admissible table. The \((0,0)\) diagonal orbit contributes one C/G output in four of its six choices, or two in its other two choices. The \((2,2)\) diagonal orbit contributes zero in two choices, or one in four choices. Therefore the complete weighted count is
\[
(2u^2)(2)(2u)^4(4u+2u^2)(2+4u)
=512u^7+1280u^8+512u^9.
\]
This proves the GC restriction and all three counts.

For the finer symbol-uniform count, let \(x_i\) record one occurrence of output symbol \(i\). Introduce the two diagonal-orbit polynomials
\[
A=x_1x_2+x_1x_3+x_0x_2+x_2^2+x_0x_3+x_3^2,
\]
\[
C=x_0^2+x_0x_2+x_1^2+x_1x_2+x_0x_3+x_1x_3.
\]
The complete enumerator of admissible tables, with one monomial for their sixteen output entries, is the following **explicit finite polynomial**:
\[
\begin{aligned}
P={}&AC(x_2^2+x_3^2)(x_0^2+x_1^2)\\
&\cdot(x_1x_2+x_0x_3)^2(x_1x_3+x_0x_2)^2.
\end{aligned}
\]
Each factor follows directly from one or two of the eight lines of the exhaustive orbit table. Ordinary integer polynomial multiplication gives
\[
[x_0^4x_1^4x_2^4x_3^4]P=80.
\]

Under transpose symmetry, the third and fifth input orbits must make the same choice, as must the fourth and sixth; the other four orbits are already independently transpose-compatible. Thus their weighted enumerator becomes
\[
\begin{aligned}
P_{\mathrm{sym}}={}&AC(x_2^2+x_3^2)(x_0^2+x_1^2)\\
&\cdot(x_1^2x_2^2+x_0^2x_3^2)
(x_1^2x_3^2+x_0^2x_2^2),
\end{aligned}
\]
and exact coefficient extraction gives
\[
[x_0^4x_1^4x_2^4x_3^4]P_{\mathrm{sym}}=16.
\]
For complete transparency, these coefficients are also evaluated by standalone integer-polynomial convolution with no numerical approximation or external package; an independent direct enumeration checks the input-pair inequalities for each table. This proves both coefficient counts.

One explicit symbol-uniform transpose-symmetric admissible table, with rows and columns indexed \(0,1,2,3\) in order, is
\[
\begin{pmatrix}
1&2&3&1\\
2&2&3&0\\
3&3&1&0\\
1&0&0&2
\end{pmatrix}.
\]
Its admissibility, symmetry, and four occurrences of each output symbol can be checked entry by entry.

## Verification
Run `python3 verify_marker_balance.py` using only the standard library. It performs two separately specified exact calculations: multiplication of the eight explicitly listed orbit-polynomial factors and direct enumeration of every admissible sixteen-entry table. Both routes return \(80\) symbol-uniform and \(16\) symbol-uniform transpose-symmetric tables. The direct route checks all defining inequalities for all \(2304\) possibilities and verifies the GC histogram \((512,1280,512)\); it also checks that there are \(576\) transpose-symmetric admissible tables regardless of symbol frequencies. The emitted `VERIFY_OK` requires agreement across the routes. The proof is a complete finite exhaustive argument, not an extrapolation from a partial sample.

## Relationship to prior work
Choi (2026, Theorem 10 and Definition 11) introduces the admissibility conditions, constructs a particular four-symbol table, and describes self-synchronizing deletion correction; the corresponding lookup-table GC statistics are not stated in the inspected sections. The prior research record *Exact enumeration and alphabet threshold for Choi synchronizer maps* proves the general unweighted map count, including \(2304\) four-symbol maps. That total and its cycle-coloring method are acknowledged: an unweighted total **does not determine** which admissible functions are GC-balanced, symbol-uniform, or transpose-symmetric. The present statement concerns this additional constrained enumerator and sharp GC bias. Zhang and Wu (2025) motivate GC balance for DNA storage in a different polar-code setting and do not study these local lookup-table constraints.

## Limitations
This result covers the four-symbol table conditions, not a new self-synchronizing decoder, a full codeword-level GC-balance guarantee, improved correction radius, or experimentally measured biochemical performance. Independence/uniformity of the input flanks is necessary for the probabilistic marker interpretation. The literature comparison cannot establish absolute novelty: unindexed investigations of balanced local DNA marker tables may exist, and the earlier general enumeration suggests a method for deriving the refined coefficients. The exact identities above are nonetheless not consequences of its stated total count alone. The finite verifier supplements rather than replaces the complete orbit proof.

## References
1. W.-H. Choi, *Algorithms of self-synchronizing single-deletion-correcting codes*, arXiv:2603.27271v1, first public 28 March 2026. Theorem 10, Definition 11, and Section 3.
2. *Exact enumeration and alphabet threshold for Choi synchronizer maps*, publicly indexed 2026 research record, identifier 406f1f4dc0ca. Establishes the unrestricted count of admissible lookup functions.
3. R. Zhang and H. Wu, *GC-balanced polar codes correcting insertions, deletions and substitutions for DNA storage*, Briefings in Bioinformatics 26 (2025), bbaf278, DOI: 10.1093/bib/bbaf278.
4. W.-H. Choi, H. J. Kim, and Y. Lee, *Construction of single-deletion-correcting DNA codes using CIS codes*, Designs, Codes and Cryptography 88 (2020), 2581–2596, DOI: 10.1007/s10623-020-00802-2.
