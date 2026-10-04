# Exact one-step strong-shift-equivalence criterion for a diagonal generalized Baker family
## Finding
For positive integers \(n,b,c\) with \(n^2\ne bc\), define
\[
A_{n;b,c}=\begin{pmatrix}n&b\\ c&n\end{pmatrix},\qquad
B_{n;b,c}=\begin{pmatrix}n&bc\\ 1&n\end{pmatrix}.
\]
Then \(A_{n;b,c}\) and \(B_{n;b,c}\) are elementary strong shift equivalent over \(\mathbb Z_+\) if and only if \(b\mid n\) or \(c\mid n\).

For the family highlighted by Jeandel,
\[
G_k=\begin{pmatrix}k&5\\4&k\end{pmatrix},\qquad
H_k=\begin{pmatrix}k&20\\1&k\end{pmatrix},
\]
the determinant is \(k^2-20\), which is nonzero for every integer \(k\). Hence \(G_k\) and \(H_k\) are elementary strong shift equivalent exactly for multiples of \(4\) or \(5\). In particular, this gives infinitely many one-step cases beyond the two small instances \(k=4,5\) explicitly noted in the motivating paper, and it rules out a one-step equivalence for every other \(k\).

## Assumptions and scope
Elementary strong shift equivalence means that there are nonnegative integer matrices \(R,S\) with \(A=RS\) and \(B=SR\). Since both displayed matrices are \(2\times2\), any such factorization between them uses \(2\times2\) matrices \(R,S\). The condition \(n^2\ne bc\) is used only in the necessity argument to ensure \(R\) is invertible over \(\mathbb Q\). The singular case \(n^2=bc\) is not classified here.

## Proof
First suppose \(c\mid n\), say \(n=cm\). Set
\[
R=\begin{pmatrix}1&0\\0&c\end{pmatrix},\qquad
S=\begin{pmatrix}n&b\\1&m\end{pmatrix}.
\]
Direct multiplication gives \(RS=A_{n;b,c}\) and \(SR=B_{n;b,c}\). Thus the pair is elementary strong shift equivalent. If instead \(b\mid n\), say \(n=bm\), take
\[
R=\begin{pmatrix}0&b\\1&0\end{pmatrix},\qquad
S=\begin{pmatrix}c&n\\m&1\end{pmatrix}.
\]
Again \(RS=A_{n;b,c}\) and \(SR=B_{n;b,c}\).

Conversely, assume \(A_{n;b,c}=RS\) and \(B_{n;b,c}=SR\) for \(R,S\in M_2(\mathbb Z_+)\). Since \(\det A_{n;b,c}=n^2-bc\ne0\), both \(R\) and \(S\) are nonsingular. Therefore \(A_{n;b,c}R=RB_{n;b,c}\). Write
\[
R=\begin{pmatrix}p&q\\r&s\end{pmatrix}.
\]
Equating the four entries of \(A_{n;b,c}R=RB_{n;b,c}\) gives
\[
q=br,\qquad s=cp,
\]
so
\[
R=\begin{pmatrix}p&br\\r&cp\end{pmatrix},\qquad
\Delta:=\det R=cp^2-br^2\ne0.
\]
Using \(S=R^{-1}A_{n;b,c}\), one obtains
\[
S=\frac1\Delta
\begin{pmatrix}
c(np-br)&b(cp-nr)\\
cp-nr&np-br
\end{pmatrix}.
\]
Because \(S\) is a nonnegative integer matrix, the quantities
\[
U:=\frac{cp-nr}\Delta,\qquad V:=\frac{np-br}\Delta
\]
are nonnegative integers, and
\[
S=\begin{pmatrix}cV&bU\\U&V\end{pmatrix}.
\]
Now the \((1,2)\)-entry of \(RS=A_{n;b,c}\) is
\[
b(pU+rV)=b,
\]
so \(pU+rV=1\). Since \(p,r,U,V\) are nonnegative integers, exactly one of the products \(pU\) and \(rV\) equals \(1\), and the other equals \(0\). The \((1,1)\)-entry gives
\[
n=cpV+brU.
\]
If \(pU=1\), then \(p=U=1\) and \(rV=0\); either \(r=0\), which gives \(n=cV\), or \(V=0\), which gives \(n=br\). If \(rV=1\), then \(r=V=1\) and \(pU=0\); either \(p=0\), which gives \(n=bU\), or \(U=0\), which gives \(n=cp\). Thus in every case \(b\mid n\) or \(c\mid n\), proving necessity.

## Verification
The proof is exact integer algebra. The two constructive factorizations were multiplied explicitly. For the converse, the intertwining equation \(AR=RB\) determines the shape of every possible nonsingular elementary factor \(R\), after which integrality and nonnegativity force the Diophantine identity \(pU+rV=1\). As a sanity check separate from the proof, bounded exhaustive searches over \(1\le n,b,c\le8\) with \(n^2\ne bc\) and candidate parameters \(0\le p,r\le30\) produced no disagreement with the divisibility criterion. This finite check is not used as proof.

## Relationship to prior work
Jeandel's 2026 preprint studies strong shift equivalence for Baker-type examples and introduces the special family \(G_k,H_k\) above. It explicitly observes that \(G_4,H_4\) and \(G_5,H_5\) are elementary strong shift equivalent, while for larger \(k\) it invokes general sufficient conditions for strong shift equivalence rather than classifying one-step equivalence. The criterion proved here identifies the complete elementary boundary for this family: all and only multiples of \(4\) or \(5\) are one-step cases.

The statement is narrower than the general strong-shift-equivalence problem. It does not decide whether non-elementary pairs are strongly shift equivalent, and it does not improve the long-chain constructions in the motivating paper except by recognizing when the chain can be replaced by one step.

## Limitations
The singular locus \(n^2=bc\) is excluded. The result concerns elementary strong shift equivalence only; nonmultiples of \(4\) and \(5\) may still be strongly shift equivalent through intermediate matrices. Literature searches did not locate this exact criterion, but absence from searches is not a proof of historical novelty; an unindexed or folklore observation remains a residual risk.

## References
1. Emmanuel Jeandel, *Combinatorial Search for Strong Shift Equivalence*, arXiv:2609.03567v1, first posted 2026-09-03.
2. Kirby A. Baker, *Strong shift equivalence of 2 x 2 matrices of non-negative integers*, Ergodic Theory and Dynamical Systems 3 (1983), 501-508, doi:10.1017/S0143385700002091.
3. Robert F. Williams, *Classification of subshifts of finite type*, Annals of Mathematics 98 (1973), 120-153.
