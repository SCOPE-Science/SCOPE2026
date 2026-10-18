# Sharp alphabet threshold for insertion-covering versus deletion-covering implication

## Finding

For an alphabet \(\Sigma_q\) of \(q\ge2\) symbols and insertion/deletion radius \(R\ge1\), let \(\ell_q(R)\) be the least integer \(n>R\) for which there exists a code \(C\subseteq\Sigma_q^n\) that covers every \((n+R)\)-symbol word under \(R\) insertions but fails to cover some \((n-R)\)-symbol word under \(R\) deletions. Then
\[
\ell_q(R)=\begin{cases}R+4,&q=2,\\R+3,&q\ge3.\end{cases}
\]
All quantifiers here include *every* positive radius \(R\); in particular the binary/nonbinary transition is independent of \(R\).

## Assumptions and scope

A word \(u\) is a scattered subsequence of \(v\), written \(u\preceq v\), when some strictly increasing sequence of positions of \(v\) spells \(u\). An \(R\)-insertion-covering code \(C\subseteq\Sigma_q^n\) satisfies \(\forall z\in\Sigma_q^{n+R}\,\exists c\in C:\ c\preceq z\). An \(R\)-deletion-covering code satisfies \(\forall y\in\Sigma_q^{n-R}\,\exists c\in C:\ y\preceq c\). No requirement on the size of \(C\) is imposed. The threshold \(\ell_q(R)\) concerns the *logical implication* between covering properties, not the minimum codebook cardinality. The symbols \(0,1,2\) below denote any three distinct alphabet elements when available.

## Proof

**Robust-witness principle.** Put \(m=n-R\). Suppose that for every \(y\in\Sigma_q^m\) there is a word \(z_y\in\Sigma_q^{2R+m}\) such that every length-\((R+m)\) subsequence of \(z_y\) contains \(y\). Then every \(R\)-insertion-covering \(C\subseteq\Sigma_q^{R+m}\) is also \(R\)-deletion-covering: by insertion covering, some \(c\in C\) is a length-\((R+m)\) subsequence of \(z_y\), so \(y\preceq c\).

**Every alphabet, \(m\le2\).** For a one-letter target \(y=a\), take \(z_y=a^{2R+1}\). For \(y=aa\), take \(z_y=a^{2R+2}\). For distinct letters \(a,b\), take \(z_{ab}=a^{R+1}b^{R+1}\). A subsequence of the latter avoiding \(ab\) is constant, hence has length at most \(R+1\), whereas the required subsequence length is \(R+2\). Thus the robust-witness principle applies for every alphabet whenever \(n-R\le2\). Consequently \(\ell_q(R)\ge R+3\).

**Binary alphabet, \(m=3\).** Up to symbol interchange and word reversal the eight binary targets reduce to \(000\), \(001\), and \(010\). For \(000\), use \(z=0^{2R+3}\). For \(001\), use \(z=0^{R+2}1^{R+1}\): a subsequence avoiding \(001\) either uses no \(1\) or at most one \(0\), hence has length at most \(R+2\). For \(010\), use the alternating word \(z=(01)^{R+1}0\), of length \(2R+3\). Number its zeros from \(0\) to \(R+1\). A subsequence selecting zeros with first and last indices \(i\le j\) and avoiding \(010\) cannot select a one between those zeros; it can select at most \(j-i+1\) zeros and at most \(i+(R+1-j)\) outside ones, a total of \(R+2\). A subsequence selecting no zero is even shorter. Therefore every subsequence of length \(R+3\) of these words contains the corresponding target. Reversal and interchange supply the remaining witnesses. The robust-witness principle now yields \(\ell_2(R)\ge R+4\).

**Nonbinary upper bound at \(m=3\).** Suppose \(q\ge3\), and take the code
\[
C=\{c\in\Sigma_q^{R+3}:012\not\preceq c\}.
\]
This code is not deletion-covering: its members all omit \(012\) as a subsequence. Let \(z\) have length \(2R+3\). Among its counts of \(0\), \(1\), and \(2\), one is at most \(R\), since \(3(R+1)>2R+3\). Deleting every occurrence of that symbol, then additional arbitrary symbols until precisely \(R\) are deleted, leaves a length-\((R+3)\) subsequence of \(z\) belonging to \(C\). Hence \(C\) is insertion-covering and \(\ell_q(R)\le R+3\) for \(q\ge3\).

**Binary upper bound at \(m=4\).** Take
\[
C=\{c\in\{0,1\}^{R+4}:0110\not\preceq c\}.
\]
Again this is not deletion-covering. To prove insertion covering, suppose a binary word \(z\) of length \(2R+4\) had *every* length-\((R+4)\) subsequence containing \(0110\). If \(z\) contained at most \(R+1\) zeros, then at least \(R+3\) ones could be selected together with at most one zero to form a length-\((R+4)\) subsequence avoiding \(0110\), contradiction. Symmetrically, \(z\) contains at least \(R+2\) ones. Thus exactly \(R+2\) of each symbol occur. Choose any consecutive pair of zeros (consecutive in the subsequence of all zeros), retain those two zeros and *all* the \(R+2\) ones, and delete the other \(R\) zeros. This length-\((R+4)\) subsequence must contain \(0110\), which, because it has exactly two zeros, requires at least two ones between those selected zeros. There are \(R+1\) gaps between consecutive zeros, so \(z\) would have at least \(2(R+1)>R+2\) ones, impossible. Hence some length-\((R+4)\) subsequence of every \(z\) lies in \(C\); insertion covering holds. Therefore \(\ell_2(R)\le R+4\). Combining all inequalities proves the theorem. \(\square\)

## Verification

The standalone finite checker `verify.py` explicitly constructs each robust witness for the eight binary targets of length three and all shorter binary targets, and inspects all requisite subsequences for \(R=1,2,3,4\). It enumerates every binary ambient word at the proposed \(m=4\) boundary for \(R=1,2,3\), and every ternary ambient word for \(R=1,2\) plus every quaternary ambient word for \(R=1\) at the \(m=3\) boundary. The recorded output is in `verification_output.txt`. The infinite theorem is proved by the preceding pigeonhole and extremal subsequence arguments, not extrapolated from finite checks.

## Relationship to prior work

Lenz, Rashtchian, Siegel, and Yaakobi introduced systematic bounds and constructions for insertion- and deletion-covering codes [1]. Xie, Sun, and Ge [2, Section III] established that insertion covering does not in general imply deletion covering, exhibiting the binary avoiding-\(0110\) construction at \(n=R+4\). That counterexample is used here only as the boundary upper construction and is not claimed to be novel. The new assertion is the *exact minimum blocklength for the first failure* for all alphabets and every radius, with a separate nonbinary witness one symbol shorter and robust witnesses excluding every shorter possibility.

## Limitations

The theorem classifies the first failure of one implication between two covering properties, not the optimum cardinality of either type of covering code, the reverse logical implication, or the structure of every code attaining the boundary. Independent external mathematical validation is not claimed. An equivalent threshold in work using a different formulation of word containment remains a literature-search risk.

## References

[1] A. Lenz, C. Rashtchian, P. H. Siegel, E. Yaakobi, *Covering Codes using Insertions or Deletions*, arXiv:1911.09944 (initial public version, 2019), https://arxiv.org/abs/1911.09944.

[2] C. Xie, Y. Sun, G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379v1 (June 13, 2026), https://arxiv.org/abs/2606.15379.
