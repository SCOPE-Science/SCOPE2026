# A two-dimensional noncommuting-controller obstruction to a controlled fusion-frame equivalence

## Finding
A published equivalence between ordinary \(K\)-\(g\)-fusion frames and \((T,U)\)-controlled \(K\)-\(g\)-fusion frames fails under its stated hypotheses. The theorem appears as Theorem 3.10 in the earliest preprint and as Theorem 3.7 in the journal version.

Let
\[
H=\mathbb R^2,\qquad K=I,\qquad J=\{1\},\qquad W_1=H,\qquad v_1=1,
\]
and let
\[
\Lambda_1=\begin{pmatrix}2&0\\0&1\end{pmatrix}.
\]
Then
\[
S_\Lambda=\Lambda_1^*\Lambda_1
=\begin{pmatrix}4&0\\0&1\end{pmatrix}.
\]
For every \(f=(x,y)\),
\[
\|\Lambda_1f\|^2=4x^2+y^2,
\]
so the family is an ordinary \(K\)-\(g\)-fusion frame with bounds \(1\) and \(4\).

Choose
\[
T=I,\qquad
U=\begin{pmatrix}1&9/10\\9/10&1\end{pmatrix}.
\]
The eigenvalues of \(U\) are \(1/10\) and \(19/10\), so \(U\) is positive and invertible. Since \(K=I\), it commutes with both controllers, and
\[
S_\Lambda T=T S_\Lambda.
\]
Thus all explicit hypotheses of the cited theorem hold.

Nevertheless, for
\[
f=(1,-2),
\]
one has
\[
Uf=(-4/5,-11/10),
\]
and hence
\[
\Lambda_1Uf=(-8/5,-11/10),\qquad
\Lambda_1Tf=(2,-2).
\]
Therefore
\[
\langle\Lambda_1Uf,\Lambda_1Tf\rangle
=-16/5+22/10=-1.
\]
The controlled quadratic form is negative, so it cannot satisfy a positive lower controlled-frame inequality. The ordinary \(K\)-\(g\)-fusion frame is therefore not a \((T,U)\)-controlled \(K\)-\(g\)-fusion frame.

A natural repair is to add the two missing commutation relations
\[
S_\Lambda U=U S_\Lambda,\qquad TU=UT.
\]
Together with the source hypothesis \(S_\Lambda T=T S_\Lambda\), the three positive operators \(T,U,S_\Lambda\) then commute pairwise. Put
\[
c_-=\|T^{-1}\|^{-1}\|U^{-1}\|^{-1},
\qquad
c_+=\|T\|\,\|U\|.
\]
Pairwise commutation gives
\[
c_-S_\Lambda
\le
TU S_\Lambda=T S_\Lambda U
\le
c_+S_\Lambda.
\]
Thus the source equivalence becomes valid, with explicit transfer of frame bounds.

## Assumptions and scope
The example uses the one-component \(g\)-fusion specialization \(W_1=H\), so no convergence or projection issue is involved. The controller \(U\) is positive definite rather than merely invertible. The failure is therefore caused by noncommutation with \(S_\Lambda\), not by an exotic controller class.

The theorem itself already assumes that \(K\) commutes with \(T\) and \(U\), and that \(S_\Lambda\) commutes with \(T\). The example satisfies those assumptions because \(K=T=I\). The omitted relation is visible directly:
\[
S_\Lambda U\ne U S_\Lambda.
\]

The repair stated here is sufficient and structurally transparent. It is not claimed to be the weakest possible hypothesis for every fixed quadruple \((K,S_\Lambda,T,U)\). More generally, any hypotheses that make \(T S_\Lambda U\) a positive operator uniformly comparable with \(S_\Lambda\) also permit the same transfer argument.

## Proof
The ordinary \(K\)-\(g\)-fusion inequalities are immediate:
\[
\|f\|^2\le\|\Lambda_1f\|^2\le4\|f\|^2,
\]
because \(K=I\).

The characteristic polynomial of \(U\) is
\[
\lambda^2-2\lambda+19/100,
\]
whose roots are \(1/10\) and \(19/10\). Hence \(U\in GL^+(H)\).

For the test vector \(f=(1,-2)\), the exact calculation above gives the controlled sum \(-1\). Since the definition of a controlled \(K\)-\(g\)-fusion frame requires
\[
A\|K^*f\|^2
\le
\sum_jv_j^2\langle\Lambda_jP_{W_j}Uf,\Lambda_jP_{W_j}Tf\rangle
\]
for some \(A>0\) and every \(f\), the example violates the definition.

Now assume the repaired pairwise commutation conditions. Since \(T\) and \(U\) are positive invertible and commute,
\[
c_-I\le TU\le c_+I.
\]
Because \(TU\) commutes with \(S_\Lambda\),
\[
c_-S_\Lambda\le TU S_\Lambda\le c_+S_\Lambda.
\]
The controlled quadratic form is the quadratic form of
\[
T S_\Lambda U=TU S_\Lambda.
\]

If the ordinary \(K\)-\(g\)-fusion frame has bounds \(A,B\), then
\[
A K K^*\le S_\Lambda\le BI.
\]
Therefore
\[
c_-A K K^*
\le
TU S_\Lambda
\le
c_+BI,
\]
which gives controlled bounds \(c_-A,c_+B\).

Conversely, if the controlled family has bounds \(A_c,B_c\), then
\[
A_c K K^*
\le
TU S_\Lambda
\le
B_cI.
\]
Using
\[
TU S_\Lambda\le c_+S_\Lambda
\]
for the lower ordinary bound and
\[
c_-S_\Lambda\le TU S_\Lambda
\]
for the upper ordinary bound gives
\[
\frac{A_c}{c_+}K K^*
\le
S_\Lambda
\le
\frac{B_c}{c_-}I.
\]
Hence the ordinary \(K\)-\(g\)-fusion bounds are \(A_c/c_+\) and \(B_c/c_-\).

## Verification
The earliest public preprint was read at the corresponding theorem, numbered Theorem 3.10 there. It states the same equivalence and assumes that \(K\) commutes with \(T\) and \(U\) and that \(S_\Lambda T=T S_\Lambda\). The proof invokes a controlled-\(K\)-fusion lemma to assert an operator inequality involving \(T S_\Lambda U\), and its converse uses expressions involving \((TU)^{1/2}\).

The journal full text was inspected at Definition 2.3, Definition 2.5, Theorem 3.7, and the complete two-page proof. The theorem again omits \(S_\Lambda U=U S_\Lambda\) and \(TU=UT\). The paper's preliminaries also state that positive operators commute, which is not true in general; the displayed counterexample consists of positive matrices and demonstrates exactly why that step cannot be assumed.

The cited precursor, Assila--Kabbaj--Moalige's controlled \(K\)-fusion lemma, was inspected at its corresponding equivalence and proof. It provides the immediate source of the comparison used in the target proof but does not supply a published correction of the noncommuting-controller case.

All calculations in the counterexample are exact \(2\times2\) matrix identities. No numerical approximation or finite sampling is used as evidence for an infinite-dimensional statement.

## Relationship to prior work
Controlled-frame literature commonly imposes commutation when products of positive controllers are treated as positive operators. For example, later controlled \(g\)-frame work explicitly records commutation of the positive controllers before using their product as a positive invertible operator. This is consistent with the repaired hypothesis above.

The closest indexed research findings located in the literature search concern compact perturbations of controlled \(K\)-frames, reconstruction range compression, woven \(K\)-frames, diagonal scaling of \(K\)-frames, and a distinct dual-\(g\)-frame eigenspace obstruction. None states the present source-specific two-dimensional counterexample or the pairwise-commutation repair of the cited equivalence.

The contribution here is therefore the exact falsification of the named theorem under its printed hypotheses and a direct quantitative repair. No novelty is claimed for the general fact that commuting positive operators have positive products.

## Limitations
Pairwise commutation is a clean sufficient repair, not claimed to be logically minimal. A weaker source-specific condition could replace it if it guarantees positivity and two-sided comparison of \(T S_\Lambda U\) with \(S_\Lambda\).

The result does not audit every theorem in the source and does not claim that all controlled \(K\)-\(g\)-fusion constructions fail without pairwise commutation. An unindexed erratum, thesis remark, or informal correction may already contain the same source-specific observation.

## References
1. P. Ghosh and T. K. Samanta, *Controlled g-atomic subspaces for operators in Hilbert spaces*, arXiv:2108.01467v1, first posted 2 August 2021.
2. P. Ghosh and T. K. Samanta, *Stability of dual controlled g-fusion frames in Hilbert spaces*, TWMS Journal of Applied and Engineering Mathematics 14(1) (2024), 154--172.
3. N. Assila, S. Kabbaj and B. Moalige, *Controlled K-Fusion Frame for Hilbert Spaces*, Moroccan Journal of Pure and Applied Analysis 7(1) (2021), 116--133, DOI 10.2478/mjpaa-2021-0011.
4. H.-M. Liu, Y.-L. Fu and Y. Tian, *Controlled g-frames and dual g-frames in Hilbert spaces*, Journal of Inequalities and Applications 2023:64, DOI 10.1186/s13660-023-02972-8.
