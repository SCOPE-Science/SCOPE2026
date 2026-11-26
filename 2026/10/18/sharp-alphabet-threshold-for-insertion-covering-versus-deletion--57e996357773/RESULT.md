# Sharp alphabet threshold for insertion-covering versus deletion-covering implication

## Finding

For an alphabet \(\Sigma_q\) with \(q\ge3\) and any integer radius \(R\ge1\), the least integer \(n>R\) for which an \(R\)-insertion-covering code \(C\subseteq\Sigma_q^n\) can fail to be \(R\)-deletion-covering is exactly \(\ell_q(R)=R+3\). Compared with the indexed binary threshold \(\ell_2(R)=R+4\) [3], this is a one-symbol difference at every positive radius. The distinct claim here is the nonbinary threshold.

## Assumptions and scope

A word \(u\) is a scattered subsequence of \(v\), written \(u\preceq v\), when some strictly increasing sequence of positions of \(v\) spells \(u\). An \(R\)-insertion-covering code \(C\subseteq\Sigma_q^n\) satisfies \(\forall z\in\Sigma_q^{n+R}\,\exists c\in C:\ c\preceq z\). An \(R\)-deletion-covering code satisfies \(\forall y\in\Sigma_q^{n-R}\,\exists c\in C:\ y\preceq c\). No requirement on the size of \(C\) is imposed. The threshold \(\ell_q(R)\) concerns the *logical implication* between covering properties, not the minimum codebook cardinality. The symbols \(0,1,2\) below denote any three distinct alphabet elements when available.

## Proof

**Robust-witness principle.** Put \(m=n-R\). Suppose that for every \(y\in\Sigma_q^m\) there is a word \(z_y\in\Sigma_q^{2R+m}\) such that every length-\((R+m)\) subsequence of \(z_y\) contains \(y\). Then every \(R\)-insertion-covering \(C\subseteq\Sigma_q^{R+m}\) is also \(R\)-deletion-covering: by insertion covering, some \(c\in C\) is a length-\((R+m)\) subsequence of \(z_y\), so \(y\preceq c\).

**Every alphabet, \(m\le2\).** For a one-letter target \(y=a\), take \(z_y=a^{2R+1}\). For \(y=aa\), take \(z_y=a^{2R+2}\). For distinct letters \(a,b\), take \(z_{ab}=a^{R+1}b^{R+1}\). A subsequence of the latter avoiding \(ab\) is constant, hence has length at most \(R+1\), whereas the required subsequence length is \(R+2\). Thus the robust-witness principle applies for every alphabet whenever \(n-R\le2\). Consequently \(\ell_q(R)\ge R+3\).

**Nonbinary upper bound at \(m=3\).** Suppose \(q\ge3\), and take the code
\[
C=\{c\in\Sigma_q^{R+3}:012\not\preceq c\}.
\]
This code is not deletion-covering: its members all omit \(012\) as a subsequence. Let \(z\) have length \(2R+3\). Among its counts of \(0\), \(1\), and \(2\), one is at most \(R\), since \(3(R+1)>2R+3\). Deleting every occurrence of that symbol, then additional arbitrary symbols until precisely \(R\) are deleted, leaves a length-\((R+3)\) subsequence of \(z\) belonging to \(C\). Hence \(C\) is insertion-covering and \(\ell_q(R)\le R+3\) for \(q\ge3\).

## Verification

The standalone finite checker `verify.py` checks explicit short robust witnesses over two symbols (including the representatives of lengths one and two) for \(R=1,2,3,4\). It enumerates every ternary ambient word for \(R=1,2\) and every quaternary ambient word for \(R=1\) at the \(m=3\) boundary. Its other binary diagnostics are retained as comparison data. The recorded output is in `verification_output.txt`. The theorem follows from the universal witness and pigeonhole arguments, not extrapolation.

## Relationship to prior work

Lenz, Rashtchian, Siegel, and Yaakobi introduced systematic bounds and constructions for insertion- and deletion-covering codes [1]. Xie, Sun, and Ge [2, Section III] established non-implication by exhibiting the binary avoiding-\(0110\) family at \(n=R+4\). The indexed record [3] gives the exact binary onset and goes further by classifying maximal boundary codes. It does not give the nonbinary onset. The indexed ternary cardinality study [4] includes a separation witness at \(q=3, R=1, n=4\); its cardinality theorem on that slice does not establish the first blocklength for general \(q\ge3\) and \(R\ge1\). The statement established here is the exact nonbinary onset, with a distinct-symbol obstruction one symbol shorter than the binary threshold and universal robust witnesses excluding shorter lengths.

## Limitations

The theorem classifies the first failure of one implication between two covering properties, not the optimum cardinality of either type of covering code, the reverse logical implication, or the structure of every code attaining the boundary. Independent external mathematical validation is not claimed. An equivalent threshold in work using a different formulation of word containment remains a literature-search risk.

## References

[1] A. Lenz, C. Rashtchian, P. H. Siegel, E. Yaakobi, *Covering Codes using Insertions or Deletions*, arXiv:1911.09944 (initial public version, 2019), https://arxiv.org/abs/1911.09944.

[2] C. Xie, Y. Sun, G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379v1 (June 13, 2026), https://arxiv.org/abs/2606.15379.

[3] *Sharp onset and maximal binary insertion/deletion covering separators*, https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-sharp-onset-and-maximal-binary-insertion-deletion-covering-separ--09950c1acd62/RESULT.md.

[4] *Exact ternary length-four insertion-covering threshold and the two-codeword cost of non-equivalence*, https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-exact-ternary-length-four-insertion-covering-threshold-and-the-t--2ff15d49787f/RESULT.md.
