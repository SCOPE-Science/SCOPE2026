# Closed-range \(K\)-frame reconstruction requires range compression
## Finding
Let \(K\in B(\mathcal H)\) have closed range \(R=R(K)\), and let \(S\) be the frame operator of a \(K\)-g-fusion frame with lower \(K\)-frame bound \(A>0\). Closedness of \(R\) does not force \(S(R)\subseteq R\). Therefore, the inverse of the restriction \(S|_R\), when understood correctly as a map from \(S(R)\) back to \(R\), cannot in general be applied directly to a vector of \(R\).

This gives a concrete obstruction to reconstruction formula (2.10) in Huang and Yang, *K-g-fusion frames in Hilbert spaces* (2020), which applies \((S|_R)^{-1}\) to arbitrary \(f\in R\). A three-dimensional \(K\)-g-fusion frame already makes that expression undefined. The universally valid replacement is the compressed operator
\[
C=P_R S|_R:R\to R,
\]
where \(P_R\) is the orthogonal projection onto \(R\). It is positive, boundedly invertible, and satisfies
\[
C\ge A\|K^\dagger\|^{-2}I_R,
\qquad
\|C^{-1}\|\le \frac{\|K^\dagger\|^2}{A}.
\]
For every \(f\in R\), the corrected reconstruction identities are
\[
f=P_RS C^{-1}f=C^{-1}P_RSf.
\]

## Assumptions and scope
A \(K\)-g-fusion frame is taken in the standard sense: for closed subspaces \(W_j\subseteq\mathcal H\), coefficient Hilbert spaces \(\mathcal H_j\), operators \(\Lambda_j:\mathcal H\to\mathcal H_j\), and weights \(v_j>0\), there are \(A,B>0\) such that
\[
A\|K^*f\|^2\le \sum_j v_j^2\|\Lambda_jP_{W_j}f\|^2\le B\|f\|^2
\]
for every \(f\in\mathcal H\). Its frame operator is
\[
Sf=\sum_jv_j^2P_{W_j}\Lambda_j^*\Lambda_jP_{W_j}f.
\]
The claim requires only that \(K\) have closed range and that the lower bound \(A\) hold. No invariance assumption \(S(R(K))\subseteq R(K)\) is made.

## Proof
For the counterexample, take \(\mathcal H=\mathbb C^3\) with orthonormal basis \(e_1,e_2,e_3\), let \(K=P_R\) for \(R=\operatorname{span}\{e_1\}\), take \(W_1=W_2=\mathcal H\), coefficient spaces \(\mathcal H_1=\mathcal H_2=\mathbb C\), and unit weights. Define
\[
\Lambda_1x=x_1,
\qquad
\Lambda_2x=x_1+x_2.
\]
Then
\[
\sum_{j=1}^2\|\Lambda_jx\|^2
=|x_1|^2+|x_1+x_2|^2
\ge |x_1|^2
=\|K^*x\|^2.
\]
Thus \(A=1\) is a valid lower \(K\)-g-fusion-frame bound. The optimal Bessel upper bound is the top eigenvalue of the \(2\times2\) block \(\begin{pmatrix}2&1\\1&1\end{pmatrix}\), namely \((3+\sqrt5)/2\), so the family is indeed a \(K\)-g-fusion frame.

Its frame operator is
\[
S=
\begin{pmatrix}
2&1&0\\
1&1&0\\
0&0&0
\end{pmatrix}.
\]
Hence
\[
Se_1=2e_1+e_2\notin R,
\qquad
S(R)=\operatorname{span}\{2e_1+e_2\}.
\]
The restriction \(S|_R:R\to S(R)\) is a bijection, but its inverse has domain \(S(R)\), not \(R\). In particular, \(e_1\notin S(R)\), so \((S|_R)^{-1}e_1\) is undefined. This directly contradicts the domain required by formula (2.10), which applies that inverse to arbitrary \(f\in R\).

Now let \(K\) and the \(K\)-g-fusion frame be arbitrary under the stated assumptions, and set \(C=P_RS|_R\). For \(x\in R\), the Moore--Penrose inverse satisfies
\[
(K^\dagger)^*K^*x=x,
\]
because \(KK^\dagger=P_R\). Therefore
\[
\|K^*x\|\ge \|K^\dagger\|^{-1}\|x\|.
\]
Using the lower \(K\)-frame inequality,
\[
\langle Cx,x\rangle
=\langle Sx,x\rangle
\ge A\|K^*x\|^2
\ge A\|K^\dagger\|^{-2}\|x\|^2.
\]
The operator \(C\) is bounded, self-adjoint and positive on the Hilbert space \(R\). The displayed coercive estimate makes its range closed and its kernel zero; self-adjointness makes its range dense, so \(C\) is onto and hence boundedly invertible. The same estimate gives
\[
\|C^{-1}\|\le \frac{\|K^\dagger\|^2}{A}.
\]
Finally, for \(f\in R\),
\[
P_RSC^{-1}f=CC^{-1}f=f,
\qquad
C^{-1}P_RSf=C^{-1}Cf=f,
\]
which proves both corrected reconstruction formulas.

## Verification
The counterexample is symbolic and finite-dimensional. Direct multiplication gives \(Se_1=2e_1+e_2\), while \(R(K)=\operatorname{span}\{e_1\}\). The frame inequalities are exact: the lower constant \(A=1\) is attained when \(x_2=-x_1\), and the Bessel constant is the largest eigenvalue \((3+\sqrt5)/2\) of the displayed positive matrix.

For the general repair, every step is an operator identity or a norm inequality on the closed Hilbert subspace \(R(K)\). No finite experiment is used to infer an infinite-dimensional statement. The proof does not claim that \(S(R(K))=R(K)\); instead it avoids precisely that unnecessary condition by compressing \(S\) back to \(R(K)\).

## Relationship to prior work
Huang and Yang define the \(K\)-g-fusion-frame operator and state \(AKK^*\le S\le BI\). They then state that for closed-range \(K\), the restricted operator is invertible and use \((S|_{R(K)})^{-1}f\) for every \(f\in R(K)\) in formula (2.10). The counterexample above shows that this application of the inverse has the wrong domain unless the extra invariance condition \(S(R(K))=R(K)\) is imposed.

An earlier paper by Cheshmavar and Rezaei Sarkhaei on approximate \(K\)-g-duals uses the same shorthand that the frame operator is “invertible on” \(R(K)\) and subsequently writes unrestricted inverse expressions. In contrast, later literature explicitly distinguishes the correct map \(S:R(K)\to S(R(K))\). Alvani, Janfada and Sadeghi (2025) state exactly that codomain, and the 2022 paper *Equal-norm Parseval K-frames in Hilbert spaces with a new inequality* adds the separate hypothesis \(S(R(K))=R(K)\) before treating \(S\) as an operator on \(R(K)\). Neither checked source supplies the universal compression \(P_RS|_{R(K)}\) and its quantitative inverse bound above.

## Limitations
The finding does not assert that every result using \(S|_{R(K)}\) is false. If a theorem explicitly treats \(S|_{R(K)}\) as a map from \(R(K)\) onto \(S(R(K))\), that statement is compatible with the counterexample. If the additional invariance \(S(R(K))=R(K)\) holds, the usual inverse-on-\(R(K)\) notation is also legitimate. The new statement is the universal correction without that invariance assumption.

The literature comparison cannot rule out an unindexed note, thesis, or informal remark containing the same compression argument. The 2016 paper *Frame operators of K-frames* predates the target cohort and is relevant background; checked later sources cite its range-to-range invertibility result, but the material inspected here did not reveal the explicit compression theorem proved above.

## References
1. Yongdong Huang and Yuanyuan Yang, *K-g-fusion frames in Hilbert spaces*, Journal of Inequalities and Applications 2020, Article 57. DOI: 10.1186/s13660-020-02320-0.
2. Jahangir Cheshmavar and Maryam Rezaei Sarkhaei, *K-g-frames and approximate K-g-duals in Hilbert spaces*, arXiv:1810.03137; later published as *Approximate K-g-duals in Hilbert spaces*, U.P.B. Scientific Bulletin, Series A 83(2) (2021), 111--120.
3. Razieh Alvani, Mohammad Janfada and Ghadir Sadeghi, *On K-frames generated by operators on Hilbert spaces*, Operators and Matrices 19(3) (2025), 373--391. DOI: 10.7153/oam-2025-19-24.
4. *Equal-norm Parseval K-frames in Hilbert spaces with a new inequality*, Journal of Inequalities and Applications (2022), DOI: 10.1186/s13660-022-02862-5.
5. G. Ramu and P. Sam Johnson, *Frame operators of K-frames*, SeMA Journal 73(2) (2016), 171--181. DOI: 10.1007/s40324-016-0062-4.
