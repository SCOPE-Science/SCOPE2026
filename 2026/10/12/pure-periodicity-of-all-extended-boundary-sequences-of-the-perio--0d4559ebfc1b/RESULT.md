# Pure periodicity of all extended boundary sequences of the period-doubling word
## Finding
Let \(\mathbf p=p_0p_1p_2\cdots\) be the period-doubling word, the fixed point beginning with \(0\) of the substitution
\[
0\longmapsto01,\qquad1\longmapsto00.
\]
For any integers \(\ell\ge1\) and \(d\ge\ell\), define the extended boundary set
\[
\partial_{\mathbf p,\ell}[d]
=\bigl\{(p_i\cdots p_{i+\ell-1},\,
 p_{i+d}\cdots p_{i+d+\ell-1}):i\ge0\bigr\}.
\]
Put
\[
k=\lceil\log_2\ell\rceil,\qquad P=2^k,\qquad T_\ell=2P.
\]
Then, for **every** \(\ell\ge1\) and **every** \(d\ge\ell\),
\[
\boxed{\partial_{\mathbf p,\ell}[d+T_\ell]
=\partial_{\mathbf p,\ell}[d].}
\]
Thus every extended boundary sequence of this aperiodic automatic word is **purely periodic**, with an explicit period smaller than \(4\ell\). There is no exceptional initial range after \(d=\ell\).

Moreover, the proof gives an exact finite construction of every boundary set using at most \(P\) residue classes and four possible hole assignments per class. In particular,
\[
\bigl|\partial_{\mathbf p,\ell}[d]\bigr|\le4P<8\ell.
\]
These are valid periods and upper bounds; no claim is made that \(T_\ell\) is always the **least** period or that \(4P\) is the exact cardinality.

## Assumptions and scope
Indices begin at zero. The parameter \(d\) is the distance between the **starting positions** of the two length-\(\ell\) boundary blocks. Therefore the full factor has length \(d+\ell\), in agreement with the source definition of the \(\ell\)-boundary sequence; \(d\ge\ell\) ensures that the two blocks do not overlap.

Write \(\nu_2(t)\) for the exponent of \(2\) dividing a positive integer \(t\). The substitution recurrence
\[
p_{2j}=0,\qquad p_{2j+1}=1-p_j
\]
implies, for every \(j\ge0\), the exact arithmetic representation
\[
p_j\equiv\nu_2(j+1)\pmod2.
\]
The theorem concerns the complete sets of **ordered boundary pairs**, not simply the existence of a single given pair. It does not assert an analogous periodicity theorem for arbitrary automatic words, other Toeplitz words, or Sturmian words.

## Proof
We first establish an elementary valuation-pair lemma. For each positive integer \(\Delta\), define
\[
E_\Delta=\bigl\{(\nu_2(t)\bmod2,\,\nu_2(t+\Delta)\bmod2):t\ge1\bigr\}.
\]
Then
\[
E_\Delta=
\begin{cases}
\{(0,0),(0,1),(1,0)\},&\Delta\text{ odd},\\
\{0,1\}^2,&\Delta\text{ even}.
\end{cases}
\tag{1}
\]
Every displayed pair occurs for arbitrarily large \(t\). When \(\Delta\) is odd, one of \(t,t+\Delta\) is odd, so \((1,1)\) is impossible. The other three pairs are obtained by choosing \(t\) in suitable classes modulo \(8\). When \(\Delta\) is even, let \(s=\nu_2(\Delta)\ge1\). Odd \(t\) give \((0,0)\). Taking \(t\) with valuation \(s\) and \(t+\Delta\) with valuation \(s+1\), or reversing these valuations, gives both mixed parity pairs (interchanging their roles according to the parity of \(s\)). For \((1,1)\), if \(s\ge2\) take \(t\equiv2\pmod4\); if \(s=1\) take \(t+\Delta\equiv8\pmod{16}\), which forces \(\nu_2(t)=1\) and \(\nu_2(t+\Delta)=3\). Each prescription is a congruence class with arbitrarily large positive solutions. This proves (1).

Fix \(\ell\ge1\), and abbreviate \(P=2^k\) with \(k=\lceil\log_2\ell\rceil\). We inspect the two windows starting at \(i\) and \(i+d\) after fixing the residue
\[
r=i\bmod P,\qquad 0\le r<P.
\]
For a position \(j\) with \(P\nmid(j+1)\), the valuation \(\nu_2(j+1)\) is smaller than \(k\) and is completely determined by \(j\bmod P\). We call such a position *ordinary*. Positions satisfying \(P\mid(j+1)\) are *holes*. At a hole,
\[
p_j\equiv k+\nu_2\bigl((j+1)/P\bigr)\pmod2.
\tag{2}
\]
Each interval of \(\ell\le P\) consecutive positions contains **at most one** hole.

For fixed \(r\) and \(d\bmod P\), all ordinary letters in the two windows are fixed. There are at most two holes total.

If there are **no holes**, the two boundary blocks are determined. If there is **one hole**, writing \(i=r+Pt\), its quotient in (2) runs through all sufficiently large positive integers as \(t\) increases, so either bit is possible. Neither case depends on more than \(d\bmod P\).

If there is **one hole in each window**, let their offsets within their respective windows be \(a,b\in\{0,\ldots,\ell-1\}\). Their quotients in (2) are
\[
q=\frac{i+a+1}{P},\qquad
q+\Delta=\frac{i+d+b+1}{P},\qquad
\Delta=\frac{d+b-a}{P}.
\]
Both are integers, and \(\Delta\ge1\) because \(d\ge\ell\). As \(i\) ranges over its fixed residue class, \(q\) ranges through every sufficiently large positive integer. By (1), the attainable parity pairs of the two quotient valuations depend **only on the parity of** \(\Delta\), even after adding the same fixed \(k\) to both coordinates in (2).

Replace \(d\) by \(d+2P\). The ordinary letters and the locations of the holes inside the two windows remain unchanged, since the new separation has the same residue modulo \(P\). In the two-hole case, \(\Delta\) is replaced by \(\Delta+2\), which has the same parity; hence (1) supplies exactly the same possible hole-bit assignments. Consequently the set of boundary pairs arising from this fixed residue class \(r\) is identical for the separations \(d\) and \(d+2P\).

Taking the union over all \(P\) residues proves
\[
\partial_{\mathbf p,\ell}[d+2P]=\partial_{\mathbf p,\ell}[d]
\quad(d\ge\ell).
\]
For each fixed residue class there are at most four possible assignments to the at most two holes. Thus the union contains at most \(4P\) pairs. Finally \(P<2\ell\), so \(T_\ell=2P<4\ell\) and \(4P<8\ell\). The argument also gives an exact algorithm: enumerate residues \(r\), fill ordinary positions, and assign hole bits using (1) and (2). This completes the proof.

## Verification
Run `python3 verify.py` beside `certificate.json`; it uses only Python's standard library.

The verifier constructs the period-doubling word independently from both the substitution and the valuation formula and compares their first \(8192\) symbols. It exhaustively checks the valuation-pair lemma for \(1\le\Delta\le128\) and \(1\le t\le8192\). Its symbolic boundary constructor enumerates the ordinary residues and exact hole possibilities, verifies the claimed period for all widths \(1\le\ell\le16\) and two period lengths of separations, and checks the \(4P\) pair bound.

Independently, all boundary pairs found in a prefix of \(65536\) starting positions are compared with the symbolic constructor for widths \(1\le\ell\le12\) over a full period of separations. These finite regression checks test indexing and the parity construction; the universal statement follows from the proof above, not from extending a finite pattern.

## Relationship to prior work
Rigo, Stipulanti and Whiteland introduced and systematically studied the extended \(\ell\)-boundary sequence. For words automatic in an addable numeration system, their main theorem establishes automaticity of the associated boundary sequence. They explicitly compute low-width instances for Thue–Morse and Fibonacci and describe Sturmian boundary sequences. They do **not** state that every extended boundary sequence of the period-doubling word is purely periodic, nor give a uniform linear upper bound on a valid period. In fact, their Sturmian results illustrate that boundary sequences may remain aperiodic for all widths.

Guo, Lü and Wen earlier established the automaticity of ordinary one-letter boundary sequences and studied periodic boundary sequences for **generalized Cantor** sequences. Their accessible bibliographic description does not settle the all-width assertion for the period-doubling word. The full text of that article was not recovered; this is retained as a specific residual originality risk, especially for the special case \(\ell=1\).

The present proof exploits the complete two-hole arithmetic of the period-doubling word. It strengthens automaticity to **pure periodicity at every width**, and supplies an exact residue-based construction of the actual boundary sets.

## Limitations
The displayed period \(2^{1+\lceil\log_2\ell\rceil}\) is certified to work but is not asserted to be the minimal period for every \(\ell\). The bound \(4P\) on the number of boundary pairs is not claimed to be sharp.

The proof is specific to the valuation description of this period-doubling fixed point. It neither classifies all automatic words with periodic boundary sequences nor extends to arbitrary nonbinary substitutions. An earlier ordinary-boundary study remains a source-access risk for the width-one special case; the main all-width assertion is not dependent on claiming that special case as previously unknown.

## References
1. M. Rigo, M. Stipulanti, and M. A. Whiteland, *On extended boundary sequences of morphic and Sturmian words*, arXiv:2206.15319v1, first public 2022-06-30; MFCS 2022, DOI 10.4230/LIPIcs.MFCS.2022.79; *Electronic Journal of Combinatorics* 31(1) (2024), #P1.9, DOI 10.37236/11728.
2. Y. Guo, X.-T. Lü, and Z.-X. Wen, *On the boundary sequence of an automatic sequence*, *Discrete Mathematics* 345(1) (2022), 112632, DOI 10.1016/j.disc.2021.112632.
3. J. Chen and Z.-X. Wen, *On the abelian complexity of generalized Thue–Morse sequences*, *Theoretical Computer Science* 780 (2019), 66–73, DOI 10.1016/j.tcs.2019.02.014.
