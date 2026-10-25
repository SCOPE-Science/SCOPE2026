# Exact low-list profile and fractional packing gap for seven-bit double-deletion codes

## Finding
Let \(A_2(7,2;L)\) be the maximum cardinality of a set \(C\subseteq\{0,1\}^7\) such that each five-bit word occurs as a scattered subsequence of at most \(L\) members of \(C\). For every integer \(1\le L\le6\),
\[
\bigl(A_2(7,2;1),A_2(7,2;2),A_2(7,2;3),A_2(7,2;4),A_2(7,2;5),A_2(7,2;6)\bigr)
=(5,11,16,21,26,32).
\]
Moreover, the standard linear relaxation of the corresponding \(32\)-constraint, \(128\)-variable incidence packing problem at \(L=2\) has exact optimum \(666/59\), while its integral optimum is \(11\), so its additive integrality gap equals \(17/59\).

## Assumptions and scope
A length-five word \(y\) is an output of length-seven \(x\) if deleting exactly two coordinates of \(x\) yields \(y\). Count distinct input words, not multiplicities of deletion-position choices. Define the binary incidence matrix \(M\), with rows \(y\in\{0,1\}^5\) and columns \(x\in\{0,1\}^7\), by \(M_{y,x}=1\) precisely when \(y\) is such an output of \(x\). A list-size-\(L\) code corresponds to a binary vector \(z\) satisfying \(Mz\le L\mathbf1\). The fractional relaxation replaces \(z\in\{0,1\}^{128}\) with \(0\le z\le1\).

## Proof
The file `seven_list_certificates.json` supplies six explicit codebooks, one for each \(L=1,\ldots,6\), encoded as seven-bit words. Direct enumeration of the \(\binom{7}{5}=21\) coordinate choices per word, identifying duplicate outputs, verifies that the codebooks have respectively \(5,11,16,21,26,32\) distinct members and no five-bit received word has more than \(L\) compatible members.

For matching upper bounds, the same file gives, for each \(L\), a positive integer denominator \(d\), a vector \(a\in\mathbb Z_{\ge0}^{32}\) and a vector \(b\in\mathbb Z_{\ge0}^{128}\). The exact, finite pointwise certificate is
\[
\sum_{y\in\{0,1\}^5}a_yM_{y,x}+b_x\ge d
\quad\text{for every }x\in\{0,1\}^7.
\]
For any admissible code \(C\), summation over its words gives
\[
|C|\le\frac{L\sum_y a_y+\sum_x b_x}{d}.
\]
The six exact rational right sides, in ascending order of \(L\), are
\[
\frac{256}{45},\quad\frac{666}{59},\quad\frac{452}{27},\quad\frac{1160}{53},\quad\frac{1430}{53},\quad\frac{2340}{73}.
\]
Each lies strictly below the next integer after its matching codebook cardinality. This proves the entire asserted integer profile without relying on the behavior of a numerical optimizer.

For \(L=2\), the same certificate file additionally gives a rational vector \(p\in[0,1]^{128}\) in numerator/denominator form. Direct exact arithmetic verifies \(Mp\le2\mathbf1\) and \(\sum_xp_x=666/59\). The matching dual certificate above proves this is the exact fractional optimum. Subtracting the proved integral optimum \(11\) gives \(17/59\).

## Verification
From the files alongside this document run `python3 verify.py`. The program uses only Python's standard library. It reconstructs the entire incidence matrix from first principles, checks all six codebooks and each of the \(128\) exact rational dual inequalities, evaluates every rational upper bound, and checks the complete rational primal vector at \(L=2\). Successful output terminates with `VERIFY_OK`. The standalone data are finite, complete, and included; no solver output or external files are necessary.

## Relationship to prior work
Lin's 2026 article formalizes the \((k,t)\)-deletion hypergraph and obtains asymptotic list-decodable code lower bounds; it does not determine these seven-bit integer optima or the fractional optimum. Guruswami and Håstad's earlier result constructs asymptotically efficient two-list, two-deletion codes and likewise does not provide this exact profile. The published six-bit calculation gives \(A_2(6,2;2)=7\), but neither that result nor length-based monotonicity implies the present six-value seven-bit list spectrum or the exact \(666/59\) fractional packing value. An existing eight-bit calculation with list allowance three uses a distinct received-word length and does not imply the present profile.

## Limitations
This theorem fixes the binary alphabet, transmitted length seven, two deletions, and list budgets \(1\) through \(6\). It does not determine the full spectrum for higher list budgets or an asymptotic rate. The fractional optimum is determined exactly only at \(L=2\), although valid rational upper bounds are supplied for all six budgets. The literature search cannot exclude an unindexed equivalent table.

## References
1. Andrew D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650v1, first submitted 22 September 2026, in particular Definition 2.1 and Theorem 1.1.
2. Venkatesan Guruswami and Johan Håstad, *Explicit two-deletion codes with redundancy matching the existential bound*, arXiv:2007.10592v1, 2020.
3. *Exact length-six binary two-list two-deletion code size*, published mathematical record, `2026/10/4/SCOPE-exact-length-six-binary-two-list-two-deletion-code-size--9d20b24dd814`.
