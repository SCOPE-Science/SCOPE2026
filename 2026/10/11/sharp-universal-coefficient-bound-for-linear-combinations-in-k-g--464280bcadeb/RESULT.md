# Sharp universal coefficient bound for linear combinations in \(K\)-\(g\)-fusion frames
## Finding
Let \(\Lambda=\{(W_j,\Lambda_j,v_j)\}_{j\in J}\) be a common \(K_i\)-\(g\)-fusion frame for \(i=1,\ldots,n\). Suppose \(A_i>0\) is a valid lower \(K_i\)-\(g\)-fusion-frame bound, so that for every \(f\) in the Hilbert space,
\[
A_i\|K_i^*f\|^2\le E(f),
\qquad
E(f):=\sum_{j\in J}v_j^2\|\Lambda_jP_{W_j}f\|^2.
\]
For scalars \(a_i\), not all zero, define \(K=\sum_{i=1}^n a_iK_i\). Then
\[
E(f)\ge L\|K^*f\|^2,
\qquad
L=\left(\sum_{i=1}^n\frac{|a_i|}{\sqrt{A_i}}\right)^{-2}.
\]
The constant \(L\) is the best universal lower bound determined solely by the certified lower bounds \(A_i\) and the coefficients \(a_i\). In particular, it improves the lower bound stated in Huang--Yang Theorem 3.4(1).

The conclusion of Huang--Yang Theorem 3.4(1) survives, but one displayed proof step does not. The proof estimates a weighted operator sum by a maximum coefficient times the corresponding unweighted sum. That inequality is false: with \(n=2\), \(a_1=1\), \(a_2=-1\), \(K_1=I\), and \(K_2=-I\), the weighted adjoint sum is \(2I\), whereas the unweighted adjoint sum is zero.

## Assumptions and scope
The result is for Hilbert-space \(K\)-\(g\)-fusion frames in the sense used by Huang and Yang. The same family \(\Lambda\) is assumed to satisfy
\[
A_i\|K_i^*f\|^2\le E(f)\le B\|f\|^2
\]
for every \(i=1,\ldots,n\) and every \(f\), with a common finite upper bound \(B\). No commutativity among the operators \(K_i\) is required for the linear-combination statement. The sharpness assertion is universal: it concerns what can be guaranteed from the data \(A_i\) and \(a_i\) alone, without additional geometric information about the operators.

## Proof
From the lower bounds,
\[
\|K_i^*f\|\le \frac{E(f)^{1/2}}{\sqrt{A_i}}.
\]
Therefore
\[
\begin{aligned}
\|K^*f\|
&=\left\|\sum_{i=1}^n\overline{a_i}K_i^*f\right\|\\
&\le\sum_{i=1}^n|a_i|\,\|K_i^*f\|\\
&\le\left(\sum_{i=1}^n\frac{|a_i|}{\sqrt{A_i}}\right)E(f)^{1/2}.
\end{aligned}
\]
Squaring and rearranging gives the stated lower bound \(L\). The original common upper bound \(B\) is unchanged, hence \(\Lambda\) is a \(K\)-\(g\)-fusion frame.

To prove sharpness, take the one-dimensional Hilbert space \(H=\mathbb C\), one index \(J=\{1\}\), \(W_1=H\), \(v_1=1\), and \(\Lambda_1=I\). Then \(E(f)=|f|^2\). For every nonzero coefficient write \(a_i=|a_i|e^{\mathrm i\theta_i}\), and let \(K_i\) be scalar multiplication by \(e^{-\mathrm i\theta_i}/\sqrt{A_i}\); for a zero coefficient choose any scalar of modulus \(1/\sqrt{A_i}\). Thus
\[
A_i\|K_i^*f\|^2=|f|^2=E(f)
\]
for every \(i\), while \(K\) is scalar multiplication by
\[
\sum_{i=1}^n\frac{|a_i|}{\sqrt{A_i}}.
\]
Consequently a lower \(K\)-\(g\)-fusion-frame bound \(C\) must satisfy
\[
C\left(\sum_{i=1}^n\frac{|a_i|}{\sqrt{A_i}}\right)^2\le1,
\]
so \(C\le L\). Hence \(L\) is optimal.

## Verification
The proof is symbolic. The invalid printed estimate can be checked in one dimension: with \(K_1=I\), \(K_2=-I\), \(a_1=1\), and \(a_2=-1\), its left side equals \(2\|f\|\) while the proposed right side equals zero for every nonzero \(f\). The replacement estimate is the ordinary triangle inequality followed by the individual \(K_i\)-frame lower bounds. Sharpness is witnessed by the one-dimensional construction above for every admissible parameter list.

The published bound is
\[
L_{\mathrm{pub}}=\left((\max_i|a_i|)^2 n\sum_{i=1}^n A_i^{-1}\right)^{-1}.
\]
Since
\[
\left(\sum_{i=1}^n\frac{|a_i|}{\sqrt{A_i}}\right)^2
\le n\sum_{i=1}^n\frac{|a_i|^2}{A_i}
\le (\max_i|a_i|)^2n\sum_{i=1}^nA_i^{-1},
\]
the sharp universal constant \(L\) is always at least the published one.

## Relationship to prior work
Huang and Yang state in Theorem 3.4(1) that a common \(K_i\)-\(g\)-fusion frame remains a \(\sum_i a_iK_i\)-\(g\)-fusion frame and provide an explicit lower bound. Their conclusion is correct, but the first norm comparison in the displayed proof is not. The argument above both repairs the proof and identifies the exact universal lower bound available from the same quantitative hypotheses.

The earlier construction paper by Sadri, Ahmadi, and Rahimi develops \(K\)-\(g\)-fusion frames, operator constructions, and duality, but the inspected theorem sequence does not give this sharp coefficient-dependent linear-combination constant. Searches of the indexed findings for the source title, theorem number, coefficient-weighted formulation, proof inequality, and sharp-bound aliases found related \(K\)-frame and \(g\)-fusion-frame results but no statement implying the exact constant above.

## Limitations
The value \(L\) is optimal only as a universal guarantee based on the listed lower bounds and coefficients. For a particular operator tuple, cancellation or additional geometry can yield a larger lower bound. No claim is made that every \(A_i\) supplied in an application is itself an optimal \(K_i\)-frame bound. The literature search cannot exclude an unindexed note or erratum containing the same sharpening.

## References
1. Y. Huang and Y. Yang, “K-g-fusion frames in Hilbert spaces,” *Journal of Inequalities and Applications* 2020, Article 57 (2020), doi:10.1186/s13660-020-02320-0. Theorem 3.4(1) and its proof.
2. V. Sadri, R. Ahmadi, and A. Rahimi, “Construction of k-g-fusion frames and their duals in Hilbert spaces,” arXiv:1806.03595, first posted 2018-06-10.
