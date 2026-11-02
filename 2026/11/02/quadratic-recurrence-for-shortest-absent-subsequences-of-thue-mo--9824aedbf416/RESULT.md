# Quadratic recurrence for shortest absent subsequences of Thue–Morse prefixes

## Finding

Let \(T_0=0\) and \(T_{m+1}=\mu(T_m)\), where \(\mu(0)=01\) and \(\mu(1)=10\). For every integer \(m\ge0\), let \(A_m\) be the number of **distinct** binary strings of length \(2^m+1\) that are absent as scattered subsequences of \(T_{m+1}\). These are exactly the shortest absent scattered subsequences of this prefix.

The entire infinite sequence is given by the autonomous quadratic recurrence

\[
A_0=3,\qquad D_0=1,\qquad
A_{m+1}=2+A_mD_m,\qquad
D_{m+1}=D_m(A_m-D_m)\quad(m\ge0).
\]

In particular, its first six values are

\[
A_0,A_1,A_2,A_3,A_4,A_5=3,5,12,74,2666,3647090.
\]

This computes the exact count for a word of length \(2^{m+1}\) with only \(m\) iterations of two polynomial updates on integers. It does not require constructing that exponentially long prefix.

## Assumptions and scope

The alphabet is \(\{0,1\}\), subsequences preserve order but need not be contiguous, and different deletion embeddings of the same binary string count only once. All claims hold for integer \(m\ge0\). A string of length \(2^m\) embeds in \(T_{m+1}\) because that word is a concatenation of \(2^m\) blocks, each either `01` or `10`. No string of length \(2^m+1\) consisting entirely of zeros embeds, because the prefix contains exactly \(2^m\) zeros. Hence the shortest absent length really is \(2^m+1\).

## Proof

**1. A local exclusion characterization.** Let \(b=b_1\cdots b_h\) be any binary word and put \(W=\mu(b)\), where each block \(\mu(b_i)=b_i\overline{b_i}\). A target \(x=x_1\cdots x_{h+1}\) is absent as a subsequence of \(W\) precisely when, for all \(1\le i\le h\), its adjacent pair \(x_ix_{i+1}\) differs from the ordered block \(b_i\overline{b_i}\).

Indeed, greedily embed the target from the left. In each whole block, its next unmatched target symbol is always available. If the block begins with this symbol and ends with the following target symbol, the block consumes two target symbols. The first block that consumes two is necessarily block \(i\), and no previous block has consumed two, so the two consumed symbols are exactly \(x_i,x_{i+1}\). All remaining blocks consume at least one symbol, proving that the target then embeds fully. Conversely, if no block consumes two, exactly \(h\) of the \(h+1\) symbols can be consumed. This establishes both directions of the exclusion test.

**2. Transfer matrices.** Set

\[
L=\begin{pmatrix}1&0\\1&1\end{pmatrix},\quad
R=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\boldsymbol e=\begin{pmatrix}1\\1\end{pmatrix}.
\]

The entry \((u,v)\) of \(L\) is one except for transition `01`; the entry of \(R\) is one except for transition `10`. Therefore, with \(M_0=L,M_1=R\), step 1 implies

\[
\#\mathrm{SAS}(\mu(b))=\boldsymbol e^{\mathsf T}M_{b_1}\cdots M_{b_h}\boldsymbol e.
\]

**3. The Thue–Morse renormalization.** Write \(P_m=M_{T_m[1]}\cdots M_{T_m[2^m]}\). Bit complementation conjugates the matrices by \(J\): \(JM_0J=M_1\) and \(JM_1J=M_0\). The classical identity \(T_{m+1}=T_m\overline{T_m}\) thus yields

\[
P_{m+1}=P_mJP_mJ=(P_mJ)^2.
\]

Each \(P_m\) has determinant one. Put \(t_m=\operatorname{tr}(P_m)\), \(A_m=\boldsymbol e^{\mathsf T}P_m\boldsymbol e\), and \(D_m=A_m-t_m\). For a generic determinant-one matrix \(P=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\), note that \(D=b+c\). Direct multiplication and \(ad-bc=1\) give

\[
\boldsymbol e^{\mathsf T}(PJ)^2\boldsymbol e=2+(a+b+c+d)(b+c),
\quad
\operatorname{tr}((PJ)^2)=2+(b+c)^2.
\]

The second identity also follows from \(\operatorname{tr}(X^2)=\operatorname{tr}(X)^2-2\det X\), because \(\det(PJ)=-1\). Consequently

\[
A_{m+1}=2+A_mD_m,\qquad
D_{m+1}=A_{m+1}-t_{m+1}=D_m(A_m-D_m).
\]

Finally \(P_0=L\), so \(A_0=3\), \(t_0=2\), \(D_0=1\). By induction these identities prove the claimed recurrence for all \(m\). The matrices have nonnegative entries and trace at least two, so no hidden cancellation or division is required.

## Verification

The accompanying standalone `verify.py` tests three independent descriptions: the quadratic recurrence; the direct product of \(2^m\) local two-by-two matrices; and a next-occurrence automaton counting absent target strings with their actual greedy embeddings. They agree for \(0\le m\le8\). The script also directly enumerates all binary targets for \(m\le3\) and exhaustively checks the transfer-matrix characterization for every orientation string of length at most seven. Its recorded execution result is `VERIFY_OK 276 independent comparisons; exact quadratic recurrence to m=8`. These finite checks support, but do not replace, the all-\(m\) proof above.

To reproduce, run `python verify.py` using Python 3 and the standard library.

## Relationship to prior work

Kosche, Koß, Manea and Siemer (arXiv:2108.13968, first publicly posted August 31, 2021) introduce structural descriptions and algorithms for shortest absent subsequences. Adamson and collaborators (arXiv:2407.18599, publicly posted July 26, 2024) analyze maximum and minimum numbers of missing subsequences subject to universality constraints; those universal extremal bounds do not determine the particular counts for the nested Thue–Morse prefixes. Lejeune, Leroy and Rigo (arXiv:1812.07330) study occurrences of subsequences and \(k\)-binomial equivalence of Thue–Morse *factors* for a fixed comparison depth, rather than counting distinct shortest missing subsequences of its dyadic prefixes with a growing target length. The exact recurrence here distinguishes that previously studied subsequence data from the support-counting problem under substitution.

## Limitations

The theorem is restricted to dyadic substitution prefixes, not arbitrary factors or arbitrary lengths. It counts shortest missing subsequences, not all minimal absent subsequences or the complete set of missing words at longer lengths. It establishes a recurrence and exact values, not a closed elementary expression, asymptotic expansion, or any statistical assertion about randomly chosen words. Possible undiscovered equivalent formulations remain a literature risk.

## References

- M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (initial public version August 31, 2021). https://arxiv.org/abs/2108.13968
- D. Adamson et al., *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (initial public version July 26, 2024). https://arxiv.org/abs/2407.18599
- M. Lejeune, J. Leroy and M. Rigo, *Computing the \(k\)-binomial complexity of the Thue–Morse word*, arXiv:1812.07330 (initial public version December 18, 2018). https://arxiv.org/abs/1812.07330
