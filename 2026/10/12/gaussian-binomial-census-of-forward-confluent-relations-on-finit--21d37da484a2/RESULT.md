# Gaussian-binomial census of forward-confluent relations on finite intuitionistic chains
## Finding
Let \(C_n=\{0<1<\cdots<n-1}\) with \(n\ge 1\). A binary relation \(R\subseteq C_n^2\) is forward confluent when
\[
z\le x\ \&\ zRy\quad\Longrightarrow\quad \exists t\,(xRt\ \&\ y\le t).
\]
On a chain this relational condition has a complete one-dimensional description: the nonempty rows of \(R\) form a final segment, and their row maxima are weakly increasing. Therefore the number \(F_n\) of forward-confluent relations on the fixed labeled chain is
\[
F_n=1+\sum_{r=1}^n\left[\begin{smallmatrix}n+r-1\\r\end{smallmatrix}\right]_2,
\]
where \(\left[\begin{smallmatrix}N\\K\end{smallmatrix}\right]_q\) denotes the Gaussian binomial coefficient. The first eight values are
\[
2,\ 11,\ 198,\ 13377,\ 3523028,\ 3661468103,\ 15111867969754,\ 248548812768592621.
\]

## Assumptions and scope
The order is the fixed labeled \(n\)-element chain and no conditions beyond forward confluence are imposed on \(R\). The empty relation is allowed and accounts for the initial \(1\) in the formula. The result concerns frame enumeration, not logical equivalence classes of frames and not arbitrary finite preorders.

Forward confluence is not a new condition. In the FIK paper it is the semantic frame condition ensuring heredity for the local diamond forcing clause, and the authors note that it is Simpson's earlier condition (F1). The new claim here is only the exact structural reduction and census for finite chains.

## Proof
Write \(R_i=\{y:iRy}\) for the row at \(i\). Suppose forward confluence holds. If \(R_z\ne\varnothing\) and \(z\le x\), choose \(y\in R_z\). Forward confluence supplies \(t\in R_x\), so \(R_x\ne\varnothing\). Hence all nonempty rows form a final segment.

For two nonempty rows with \(z\le x\), put \(m_z=\max R_z\). Applying forward confluence to \(y=m_z\) gives some \(t\in R_x\) with \(t\ge m_z\), hence \(m_x\ge m_z\). Thus row maxima are weakly increasing.

Conversely, suppose the nonempty rows form a final segment and their maxima are weakly increasing. If \(z\le x\) and \(zRy\), then both rows are nonempty and \(m_z\le m_x\). Choosing \(t=m_x\) gives \(xRt\) and \(y\le m_z\le t\), which is exactly forward confluence.

Now suppose there are \(r\) nonempty rows. Their positions are forced: they are the last \(r\) rows. Fix weakly increasing maxima
\[
0\le m_1\le\cdots\le m_r\le n-1.
\]
A row with maximum \(m_i\) contains \(m_i\) and may contain any subset of \(\{0,\ldots,m_i-1}\), so there are exactly \(2^{m_i}\) choices for that row. The number for this maxima sequence is therefore \(2^{m_1+\cdots+m_r}\). Summing gives
\[
\sum_{0\le m_1\le\cdots\le m_r\le n-1}2^{m_1+\cdots+m_r}
=\left[\begin{smallmatrix}n+r-1\\r\end{smallmatrix}\right]_2,
\]
the standard partition-in-a-rectangle generating function for Gaussian binomial coefficients. Summing over \(r=1,\ldots,n\) and adding the empty relation proves the formula.

## Verification
The accompanying `verify.py` checks the frame condition directly on every binary relation on chains of sizes \(1\) through \(4\), checking \(2+16+512+65536\) relations in total. For every relation it independently compares forward confluence with the final-segment/row-maximum characterization. It then verifies the Gaussian-binomial sum by explicit weakly increasing maxima through \(n=10\), checks both standard Gaussian recurrences through ambient size \(30\), and checks the first eight displayed values. Its terminal output is:

`VERIFY_OK 67010 exact assertions; exhaustive all relations through n=4`

The exhaustive computation is a finite check of the proof's boundary cases, not a substitute for the general argument.

## Relationship to prior work
Balbiani, Gao, Gencer, and Olivetti introduce FIK and define its frames using forward confluence. They explicitly note that the condition itself is older and appears as Simpson's (F1). Their paper proves soundness, completeness, and the finite model property; it does not state an enumeration of forward-confluent relations on chains. Direct full-text checks found no occurrence of “Gaussian” or “enumerat”. Targeted searches under “forward confluence”, “forward-confluent”, “F1”, “finite chain”, “row maxima”, “Gaussian binomial”, and the initial integer sequence did not locate the displayed census or an equivalent chain characterization.

The Gaussian-binomial identity used after the structural reduction is classical. No novelty is claimed for that identity by itself.

## Limitations
This result is specific to a fixed total intuitionistic order. On general finite preorders, a row cannot be summarized by a single maximum, so the proof does not provide an enumeration there. The search evidence cannot exclude uncatalogued folklore, especially because the characterization is short once forward confluence is specialized to a chain.

## References
1. P. Balbiani, H. Gao, Ç. Gencer, N. Olivetti, “A Natural Intuitionistic Modal Logic: Axiomatization and Bi-nested Calculus,” arXiv:2309.06309, first posted 2023-09-12; CSL 2024, DOI 10.4230/LIPIcs.CSL.2024.13.
2. A. Simpson, “The Proof Theory and Semantics of Intuitionistic Modal Logic,” PhD thesis, University of Edinburgh, 1994. Forward confluence is identified as condition (F1) by the FIK authors.
