# Exact exhaustive Lempel–Ziv phrase boundaries of generalized Cantor words

## Finding
Let \(q\ge3\) be an integer and let \(C_q\) be the binary infinite fixed point beginning in \(1\) of \(\mu_q(1)=10^{q-2}1\), \(\mu_q(0)=0^q\). Index symbols and factor starts from zero. Under the **exhaustive-history** (LZ76) convention—each next phrase is the shortest nonempty factor not previously occurring with an earlier starting position, with overlaps allowed—the complete set of phrase starts is, for \(q\ge4\),
\[
\{0,1,2\}\ \cup\ \bigcup_{m\ge0}\{(q-1)q^m+1,\ 2(q-1)q^m+1\}.
\]
For \(q=3\) the complete set is
\[
\{0,1,2,5,9\}\ \cup\ \{4\cdot3^m+1:m\ge1\}\ \cup\ \{2\cdot3^m+1:m\ge2\}.
\]
Every boundary is exact, not just asymptotic. In particular, if \(W_{q,k}=\mu_q^k(1)\), then its finite exhaustive-history phrase count (including a possibly truncated final phrase) is
\[
\operatorname{lz}(W_{q,k})=2k+2\quad(q\ge4,\ k\ge2),
\qquad
\operatorname{lz}(W_{3,k})=2k+1\quad(k\ge3).
\]
The small-depth cases are \(\operatorname{lz}(W_{q,0})=1\) and \(\operatorname{lz}(W_{q,1})=3\) for every \(q\ge3\), with \(\operatorname{lz}(W_{3,2})=4\).

## Assumptions and scope
Only the integer parameters and precisely defined morphic words above are involved. For a phrase beginning at index \(i\), an occurrence starting at \(j<i\) may extend beyond \(i\), but must be contained in the already observed prefix together with the portion being tested: equivalently, a length-\(r\) phrase is innovative when it has no occurrence starting at \(j<i\), and its length-\((r-1)\) prefix has one. This is the exhaustive-history convention of Constantinescu and Ilie, not the different nonoverlapping-dictionary or maximal-old-factor parsing conventions. The last phrase of a finite prefix may be reproductive because truncation is allowed.

The fixed point has \(C_q(t)=1\) exactly when every base-\(q\) digit of \(t\) is \(0\) or \(q-1\). Hence \(W_{q,k}\) has length \(q^k\), starts and ends in \(1\), and the maximum internal run of zeros in \(W_{q,k}\) is \((q-2)q^{k-1}\) for \(k\ge1\).

## Proof
Write \(L=q^m\) and \(W=W_{q,m}\). At block scale \(L\), the first nonzero blocks of the fixed point are at block positions \(0,q-1,q(q-1)\). Consequently its initial block pattern is
\[
W\,0^{(q-2)L}\,W\,0^{q(q-2)L}\,W\cdots.
\]
The internal-zero-run assertion in the previous section follows inductively from \(W_{q,m+1}=W_{q,m}0^{(q-2)q^m}W_{q,m}\); this relation also proves the base-\(q\) digit characterization.

**First family of phrases.** Put \(A_m=(q-1)L+1\). The factor starting at \(A_m\) and having length \((q-1)L\) is
\[
P_m=W[1:L]0^{(q-2)L+1},
\]
where the bracket denotes the suffix after deleting the first symbol; when \(m=0\), this suffix is empty. The proper prefix \(W[1:L]0^{(q-2)L}\) occurs at position \(1<A_m\). For \(m\ge1\), an earlier occurrence of \(P_m\) would have its last \(1\) at some position strictly before the last \(1\) of the second copy of \(W\), and that \(1\) would have to be followed by \((q-2)L+1\) consecutive zeros. No earlier \(1\) has that many subsequent zeros: all internal runs of \(W\) are shorter, and the gap after the first \(W\) has exactly \((q-2)L\) zeros. Thus \(P_m\) is innovative. For \(m=0\), it is \(0^{q-1}\), whose proper prefix occurs at position \(1\), whereas no earlier start yields \(q-1\) zeros. The first-family boundaries therefore constitute genuine exhaustive phrases whenever the parser reaches them.

**Second family of phrases.** Put \(B_m=2(q-1)L+1\) and \(R=(q-1)(q-2)L\). The factor of length \(R\) beginning at \(B_m\) is \(0^{R-1}1\); the terminal \(1\) is at position \(q(q-1)L\), the beginning of the third nonzero block. The prefix \(0^{R-1}\) occurs starting at \(qL<B_m\), inside the large zero gap. Every earlier \(1\) has at most \((q-2)L\) immediately preceding zeros. Hence this phrase cannot have occurred with an earlier start provided \(R-1>(q-2)L\), which holds for every \(q\ge4,m\ge0\) and for \(q=3,m\ge1\). These second-family phrases are therefore innovative in precisely the parameter ranges asserted.

The end of the first-family phrase is \(A_m+(q-1)L=B_m\). The end of the second-family phrase is \(B_m+(q-1)(q-2)L=A_{m+1}\). Thus the innovative phrases tile the entire remaining tail in order. For \(q\ge4\), the first three phrases begin at \(0,1,2\) and are \(1\), \(0\), and \(0^{q-3}1\), ending at \(A_0=q\). Their proper-prefix reproduction and whole-phrase novelty are immediate from the initial \(10^{q-2}1\) block.

For \(q=3\), direct comparison of earlier-starting factors within the first 19 symbols \(1010001010000000001\) gives the initial exhaustive phrases
\[
1\mid0\mid100\mid0101\mid0000\mid000001,
\]
with starts \(0,1,2,5,9,13\). The last begins at \(B_1=13\) and ends at \(A_2=19\). The established two-family argument thereafter applies to \(A_m\) for \(m\ge2\) and \(B_m\) for \(m\ge1\), proving the exceptional formula. At each boundary, proper prefixes of the new phrase occur at earlier starts, and the whole phrase does not, so this establishes the actual unique exhaustive history rather than merely a convenient partition.

Finally, count the starts strictly before \(q^k\). For \(q\ge4\) and \(k\ge2\), there are the first three, two starts per scale \(m=0,\ldots,k-2\), and the first-family start at scale \(k-1\): \(3+2(k-1)+1=2k+2\). For \(q=3\) and \(k\ge3\), there are five exceptional starts, one second-family start at scale \(1\), two starts at scales \(2,\ldots,k-2\) (when this range is nonempty), and the first-family start at scale \(k-1\), giving \(2k+1\). The remaining small-depth counts follow directly from the displayed phrases.

## Verification
The standalone \(\texttt{verify_parsing.py}\) independently constructs \(C_q\) by two methods: iterative substitution and the base-\(q\) digit test. It implements the exhaustive-history minimal-new-phrase condition with earlier starting positions and permitted overlap, then compares every actual phrase start with the formulas for \(q=3,\ldots,12\) at specified powers up to 100,000 symbols. Execution returns \(\texttt{VERIFY_OK}\). These finite tests corroborate the infinite structural proof; they do not replace it.

## Relationship to prior work
Constantinescu and Ilie gave the exhaustive-history definitions and a classification of asymptotic Lempel–Ziv complexity for fixed points of morphisms, including the logarithmic order appropriate to exponentially growing nonperiodic substitutions. Their more general asymptotic statement does not determine exact phrase positions, phase lengths, exceptional parameters, or additive constants at substitution depths. Berstel and Savelli studied **Crochemore** factorization of several other famous infinite words, a different parsing rule. The result here is the explicit exhaustive-history evaluation for the generalized Cantor family.

## Limitations
The formulas depend on the precise exhaustive-history convention, particularly permitting a previous occurrence to overlap the position at which a new phrase begins. They do not assert the same boundaries for other LZ77/LZ78 or Crochemore conventions, other morphisms, or arbitrary shifted factors of \(C_q\). The full-text comparison with one closely related Crochemore-factorization paper was limited; equivalences in unindexed literature remain a residual originality risk. No external independent audit has been performed.

## References
1. S. Constantinescu and L. Ilie, *The Lempel–Ziv Complexity of Fixed Points of Morphisms*, MFCS 2006, LNCS 4162, pp. 280–291, DOI: 10.1007/11821069_25 (proceedings print edition published 11 August 2006). Expanded journal version: *SIAM Journal on Discrete Mathematics* 21 (2007), 466–481, DOI: 10.1137/050646846. Author's lawful full text: https://www.csd.uwo.ca/~ilie/SIDMA07.pdf.
2. J. Berstel and A. Savelli, *Crochemore Factorization of Sturmian and Other Infinite Words*, MFCS 2006, LNCS 4162, pp. 157–166.
3. A. Lempel and J. Ziv, *On the Complexity of Finite Sequences*, *IEEE Transactions on Information Theory* 22 (1976), 75–81, DOI: 10.1109/TIT.1976.1055501.
