# Woven \(K\)-frames need partition-dependent reconstruction families
## Finding
The common-reconstruction characterizations in Theorem 3.1 of Xiang, *Some new results on the weaving of \(K\)-\(g\)-frames in Hilbert spaces* (Open Mathematics 19 (2021), 1315--1329, doi:10.1515/math-2021-0103), and Theorem 5.1 of Wang, *Some properties of weaving \(K\)-frames in \(n\)-Hilbert space* (AIMS Mathematics 9 (2024), 25438--25456, doi:10.3934/math.20241242), are false in the implication from wovenness to the existence of one Bessel reconstruction family that works for every partition. Already on \(H=\mathbb C\) with \(K=I\), let \(\Lambda_j z=2^{-j}z\) and \(\Gamma_j z=2^{1-j}z\) for \(j\ge1\). Every weaving is a frame, uniformly with bounds \(1/3\) and \(4/3\). If one \(g\)-Bessel family \(\Theta_j z=t_jz\) reconstructed \(K\) for every subset \(\sigma\subseteq\mathbb N\), then comparison of two subsets differing only at \(j\) would give \(t_j(2^{-j}-2^{1-j})=0\), so \(t_j=0\) for every \(j\), contradicting the reconstruction identity. The same scalar example embeds in Wang's \(2\)-Hilbert setting by taking the standard \(2\)-inner product on \(\mathbb R^2\), fixing \(c_2=e_2\), and identifying the associated Hilbert space \(H_C\) with \(\operatorname{span}\{e_1\}\). The exact repair is: two \(K\)-\(g\)-frames are \(K\)-woven with a uniform lower bound if and only if, for every partition \(\sigma\), there exists a partition-dependent \(g\)-Bessel family \(\{\Theta_i^{\sigma}\}\) with one Bessel bound valid uniformly in \(\sigma\) and satisfying \[Kf=\sum_{i\in\sigma}\Lambda_i^*\Theta_i^{\sigma}f+\sum_{i\notin\sigma}\Gamma_i^*\Theta_i^{\sigma}f.\] If the universal weaving lower bound is \(C\), the families can be chosen with Bessel bound at most \(1/C\); conversely a uniform Bessel bound \(B\) yields a universal weaving lower bound at least \(1/B\).

The obstruction is a quantifier mismatch. A single reconstruction family valid for every partition forces, for each index \(i\),
\[
(\Lambda_i^*-\Gamma_i^*)\Theta_i=0.
\]
Indeed, compare the all-\(\Lambda\) partition with the partition in which only index \(i\) is switched to \(\Gamma\). Thus the published common-family condition is substantially stronger than wovenness: it requires termwise compatibility of the two analysis families with one fixed reconstruction family.

## Assumptions and scope
Let \(H\) be a complex separable Hilbert space, let \(K\in\mathcal B(H)\), and let \(\{\Lambda_i\}_{i\in I}\) and \(\{\Gamma_i\}_{i\in I}\) be \(K\)-\(g\)-frames with respect to Hilbert spaces \(\{\mathcal K_i\}_{i\in I}\). For a subset \(\sigma\subseteq I\), write \(T_\sigma\) for the synthesis operator of the weaving that uses \(\Lambda_i\) on \(\sigma\) and \(\Gamma_i\) on \(I\setminus\sigma\).

The corrected characterization concerns a uniform lower weaving bound. If \(C>0\) satisfies
\[
C\|K^*f\|^2\le \sum_{i\in\sigma}\|\Lambda_i f\|^2+\sum_{i\notin\sigma}\|\Gamma_i f\|^2
\]
for every \(f\in H\) and every \(\sigma\subseteq I\), then the reconstruction families below can be chosen with a common Bessel bound \(1/C\). Conversely, if a constant \(B<\infty\) bounds all partition-dependent reconstruction families, then the weaving lower bound \(1/B\) is valid. The usual upper bound is supplied by the two original \(g\)-Bessel bounds.

## Proof
Take \(H=\mathbb C\), \(K=I\), \(I=\mathbb N\), and \(\mathcal K_j=\mathbb C\), and define
\[
\Lambda_j z=2^{-j}z,\qquad \Gamma_j z=2^{1-j}z \qquad (j\ge1).
\]
For every \(\sigma\subseteq\mathbb N\), the weave coefficient energy is
\[
\left(\sum_{j\in\sigma}4^{-j}+\sum_{j\notin\sigma}4^{1-j}\right)|z|^2.
\]
Since \(4^{-j}\le4^{1-j}\), this lies between
\[
\sum_{j=1}^{\infty}4^{-j}=\frac13
\quad\text{and}\quad
\sum_{j=1}^{\infty}4^{1-j}=\frac43.
\]
Hence the two families are woven with uniform bounds \(1/3\) and \(4/3\).

Assume one \(g\)-Bessel sequence \(\Theta_j z=t_jz\) satisfies the common reconstruction identity for every partition. The Bessel property gives \(\{t_j\}\in\ell^2\), so the scalar reconstruction series are absolutely convergent by Cauchy--Schwarz. For a fixed \(j\), compare partitions differing only at that index. Subtraction gives
\[
t_j2^{-j}-t_j2^{1-j}=0,
\]
so \(t_j=0\). This holds for every \(j\), contradicting reconstruction.

For Wang's \(n\)-Hilbert formulation, take \(n=2\), the standard \(2\)-inner product
\[
\langle x,y\mid c\rangle=\langle x,y\rangle\langle c,c\rangle-\langle x,c\rangle\langle c,y\rangle
\]
on \(\mathbb R^2\), and fix \(c_2=e_2\). The associated Hilbert space is represented by \(\operatorname{span}\{e_1\}\), where \(\langle ae_1,be_1\mid e_2\rangle=ab\). Taking \(f_{pj}=2^{-j}e_1\), \(f_{qj}=2^{1-j}e_1\), and \(K=I\) reproduces the same weave bounds and the same contradiction.

For the repair, suppose first that the pair is \(K\)-woven with universal lower bound \(C\). For each partition \(\sigma\),
\[
C K K^*\le T_\sigma T_\sigma^*.
\]
Douglas factorization gives \(U_\sigma:H\to\bigoplus_{i\in I}\mathcal K_i\) with
\[
K=T_\sigma U_\sigma,\qquad \|U_\sigma\|^2\le\frac1C.
\]
With \(P_i\) the coordinate projection, set \(\Theta_i^{\sigma}=P_iU_\sigma\). Then
\[
\sum_i\|\Theta_i^{\sigma}f\|^2=\|U_\sigma f\|^2\le\frac1C\|f\|^2,
\]
and expanding \(T_\sigma U_\sigma=K\) gives the asserted reconstruction.

Conversely, suppose that for every \(\sigma\) there is a family \(\{\Theta_i^{\sigma}\}\) with uniform Bessel bound \(B\) and the displayed reconstruction identity. If \(U_\sigma f=(\Theta_i^{\sigma}f)_i\), then \(K=T_\sigma U_\sigma\) and \(\|U_\sigma\|^2\le B\). Hence
\[
\|K^*f\|=\|U_\sigma^*T_\sigma^*f\|\le\sqrt B\,\|T_\sigma^*f\|,
\]
which yields the uniform lower weaving bound \(1/B\).

## Verification
The scalar counterexample was checked directly from the defining sums, including absolute convergence. The partition-toggle argument is exact and requires no numerical experiment. The repaired theorem was reconstructed from \(C K K^*\le T_\sigma T_\sigma^*\), Douglas factorization, and synthesis/analysis operator norms.

The 2021 source was materially inspected at Definition 1.2 and Theorem 3.1. In its forward proof a partition is fixed, its synthesis operator \(T\) is formed, and a factor \(U\) satisfying \(K=TU\) is then chosen; the resulting \(\Theta_i=P_iU\) therefore depends on that partition. The proof establishes \(\forall\sigma\,\exists\Theta^{\sigma}\), not the stated \(\exists\Theta\,\forall\sigma\). The 2024 source was materially inspected at the associated Hilbert-space construction, Definition 3.2, Theorem 4.2, and Theorem 5.1. Its proof similarly forms a partition-specific preframe operator \(T_F\), factors \(K=T_FW\), and defines \(g_j=W^*e_j\).

## Relationship to prior work
Xiang's Theorem 3.1 states the stronger common-family equivalence for \(K\)-\(g\)-frames. Wang's Theorem 5.1 repeats the same common-family quantifier pattern for \(K\)-frames in \(n\)-Hilbert spaces. Wang's Theorem 4.2, by contrast, uses a synthesis operator \(L_\sigma\) indexed by the partition, which is consistent with the repaired statement.

A 2024 paper on redundancy, weaving, and \(Q\)-duals of \(K\)-\(g\)-frames studies duality and weaving but does not state this uniform partition-dependent characterization. A 2025 paper by Xiang corrects a different operator-preservation assertion for woven \(g\)-frames and does not address the common reconstruction family in the 2021 theorem.

## Limitations
The counterexample disproves only the implication from wovenness to one common reconstruction family. The reverse implication remains valid. The repaired equivalence requires a Bessel bound uniform over partitions; arbitrary partition-dependent bounds would not imply a uniform weaving lower bound. No unrelated downstream theorem is assessed here.

## References
1. Zhong-Qi Xiang, *Some new results on the weaving of K-g-frames in Hilbert spaces*, Open Mathematics 19 (2021), 1315--1329. doi:10.1515/math-2021-0103.
2. Gang Wang, *Some properties of weaving K-frames in n-Hilbert space*, AIMS Mathematics 9 (2024), 25438--25456. doi:10.3934/math.20241242.
3. Xiang Chun Xiao, Guo Ping Zhao, Guorong Zhou, *Redundancy, weaving and Q-dual of K-g-frames in Hilbert spaces*, Hacettepe Journal of Mathematics and Statistics 53 (2024), 595--607. doi:10.15672/hujms.1130102.
4. Zhong-Qi Xiang, *A New View on the Wovenness of g-Frames Under Operators*, Journal of Mathematics (2025). doi:10.1155/jom/7185421.
