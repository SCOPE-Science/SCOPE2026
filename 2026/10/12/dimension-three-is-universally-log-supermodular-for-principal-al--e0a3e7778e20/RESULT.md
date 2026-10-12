# Dimension three is universally log-supermodular for principal alpha-permanents of inverse M-matrices
## Finding
Let \(\alpha>0\), and let \(A\) be an inverse \(M\)-matrix of order at most \(3\). Then the set function \(S\mapsto\operatorname{per}_{\alpha}(A_S)\) is log-supermodular. In order \(3\), after relabeling the only nontrivial overlapping incomparable case has \(S=\{1,2\}\), \(T=\{2,3\}\); writing \(A=\begin{pmatrix}a&u&r\\v&b&p\\s&q&c\end{pmatrix}\), its defect equals \(\alpha^2[\alpha b^2rs+bups+qv(br-up)]\ge0\), because \(A\ge0\) and \((A^{-1})_{13}=(up-br)/\det A\le0\). Thus the conclusion includes nonsymmetrizable inverse \(M\)-matrices and holds for every \(\alpha>0\). Dimension \(3\) is maximal for a statement uniform in both \(\alpha>0\) and all inverse \(M\)-matrices, since the four-vertex family in Sra's Appendix A fails log-supermodularity for sufficiently small positive parameters whenever \(\alpha<(\sqrt5-1)/2\).

This gives an exact low-dimensional answer to the fixed-dimension question raised in Sra's 2026 preprint: no lower cutoff on \(\alpha\) is needed in dimensions at most \(3\). It also covers genuinely nonsymmetrizable inverse \(M\)-matrices, not merely the symmetrizable or tree-graph cases treated by the existing positive results.

## Assumptions and scope
For a finite set \(S\), the \(\alpha\)-permanent is
\[
\operatorname{per}_{\alpha}(H)=\sum_{\pi\in\mathfrak S(S)}\alpha^{c(\pi)}\prod_{i\in S}H_{i,\pi(i)},
\]
where \(c(\pi)\) is the number of cycles of \(\pi\). An inverse \(M\)-matrix is \(A=M^{-1}\), where \(M\) is a nonsingular \(M\)-matrix; hence \(A\) is entrywise nonnegative, \(\det A>0\), and every off-diagonal entry of \(A^{-1}\) is nonpositive. Log-supermodularity means
\[
\operatorname{per}_{\alpha}(A_{S\cup T})\operatorname{per}_{\alpha}(A_{S\cap T})\ge
\operatorname{per}_{\alpha}(A_S)\operatorname{per}_{\alpha}(A_T)
\]
for all \(S,T\).

The theorem concerns orders \(1\), \(2\), and \(3\) over the real numbers, as in the standard inverse-\(M\)-matrix setting of the motivating source. No symmetry or symmetrizability hypothesis is assumed.

## Proof
Nested pairs \(S,T\) give equality. If \(S\cap T=\varnothing\), the block-preserving permutations in \(\operatorname{per}_{\alpha}(A_{S\cup T})\) contribute exactly \(\operatorname{per}_{\alpha}(A_S)\operatorname{per}_{\alpha}(A_T)\), because the number of cycles is additive over disjoint blocks. Every remaining permutation contributes a nonnegative term since \(A\ge0\) and \(\alpha>0\). Thus every disjoint pair satisfies the inequality.

For order at most \(2\), nested and disjoint pairs exhaust all possibilities. For order \(3\), any overlapping incomparable pair is, after relabeling, \(S=\{1,2\}\) and \(T=\{2,3\}\). Write
\[
A=\begin{pmatrix}
a&u&r\\
v&b&p\\
s&q&c
\end{pmatrix}.
\]
Direct expansion gives
\[
\operatorname{per}_{\alpha}(A)=
\alpha^3abc+\alpha^2(uvc+rsb+pqa)+\alpha(ups+rqv),
\]
\[
\operatorname{per}_{\alpha}(A_{\{1,2\}})=\alpha^2ab+\alpha uv,
\qquad
\operatorname{per}_{\alpha}(A_{\{2,3\}})=\alpha^2bc+\alpha pq,
\qquad
\operatorname{per}_{\alpha}(A_{\{2\}})=\alpha b.
\]
Therefore the log-supermodularity defect is
\[
\begin{aligned}
\Delta
&=\operatorname{per}_{\alpha}(A)\operatorname{per}_{\alpha}(A_{\{2\}})
 -\operatorname{per}_{\alpha}(A_{\{1,2\}})\operatorname{per}_{\alpha}(A_{\{2,3\}})\\
&=\alpha^2\bigl(\alpha b^2rs+bups+bqrv-uvpq\bigr)\\
&=\alpha^2\bigl(\alpha b^2rs+bups+qv(br-up)\bigr).
\end{aligned}
\]
The cofactor formula gives
\[
(A^{-1})_{13}=\frac{up-br}{\det A}.
\]
Because \(A^{-1}\) is an \(M\)-matrix and \(\det A>0\), one has \(br-up\ge0\). Every factor in the last expression for \(\Delta\) is nonnegative, proving \(\Delta\ge0\).

The conclusion genuinely extends beyond the symmetrizable cases. For example,
\[
M=\begin{pmatrix}1&-\tfrac12&0\\0&1&-\tfrac12\\-\tfrac12&0&1\end{pmatrix},
\qquad
A=M^{-1}=\frac17\begin{pmatrix}8&4&2\\2&8&4\\4&2&8\end{pmatrix}
\]
has a directed three-cycle zero pattern in \(M\), so no positive diagonal similarity can make \(A\) symmetric. For \(S=\{1,2\}\), \(T=\{2,3\}\), its defect is
\[
\Delta=\frac{512}{2401}\alpha^2(\alpha+1)>0.
\]

Finally, Sra's Appendix A gives four-vertex inverse \(M\)-matrices for which the corresponding defect is negative for sufficiently small positive family parameter whenever \(\alpha<(\sqrt5-1)/2\). Hence order \(4\) already prevents a theorem that is uniform for every \(\alpha>0\), making order \(3\) the maximal dimension for the universal statement proved here.

## Verification
The standalone `verify.py` reconstructs the \(3\times3\) \(\alpha\)-permanent symbolically in a small exact polynomial ring, verifies the displayed defect identity coefficient by coefficient, and checks the nonsymmetrizable directed-cycle example with exact rational arithmetic for several positive rational values of \(\alpha\). It also checks all subset pairs for that example. Running the file produces the saved `verification_output.txt`, ending in `CHECK_OK`.

The computation is supplementary: the universal theorem follows from the displayed symbolic expansion and the cofactor sign forced by the inverse \(M\)-matrix hypothesis.

## Relationship to prior work
Sra, *A Koteljanskii inequality for permanents* (arXiv:2609.39979v1, first public 2026-09-30), proves ordinary-permanent log-supermodularity for symmetrizable inverse \(M\)-matrices and gives a five-dimensional nonsymmetrizable counterexample. In its section on \(\alpha\)-permanents, the paper records positive results for \(\alpha=1\), \(\alpha=1/2\), and, via Royen, all \(\alpha>0\) for symmetric inverse \(M\)-matrices whose inverse graph is a tree. It explicitly asks whether a fixed dimension admits a threshold \(\alpha_n\) valid for every inverse \(M\)-matrix. The theorem here settles the entire \(n\le3\) range more strongly: every \(\alpha>0\) works, including on nonsymmetrizable directed-cycle examples.

Royen's 2025 work supplies the MTP2 result used by Sra for the symmetric tree-graph case. That result does not cover the nonsymmetrizable directed-cycle matrices used above.

## Limitations
The proof is dimension-specific. It does not determine the optimal threshold \(\alpha_n\) for any \(n\ge4\), characterize all higher-dimensional inverse \(M\)-matrices with log-supermodular principal \(\alpha\)-permanents, or settle Sra's symmetrizable cyclic-graph question for general \(\alpha\). The four-dimensional sharpness statement is only the stated obstruction to a theorem uniform over *all* positive \(\alpha\); it does not rule out a positive large-\(\alpha\) threshold in dimension \(4\).

## References
1. S. Sra, *A Koteljanskii inequality for permanents*, arXiv:2609.39979v1 [math.RA], 2026. First public 2026-09-30. MSC 2020 classes listed by arXiv: 15A15, 15A45, 15B48, 60E15.
2. T. Royen, *On improved Gaussian correlation inequalities for symmetrical n-rectangles extended to certain multivariate gamma distributions and some further probability inequalities*, Far East Journal of Theoretical Statistics 69(1), 1-38, 2025. DOI: 10.17654/0972086325001.
