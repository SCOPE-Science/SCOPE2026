# Exact trace-preservation boundary and spurious two-qutrit entanglement signal

## Finding
Consider the six one-qutrit operators \(E_1,\ldots,E_6\) in Eqs. (1)--(6) of Guo, Fang, Wang and Zeng, arXiv:1506.02743, and the independent two-qutrit operation in their Eq. (7). With \(0\le r<1\), equal damping probabilities \(p_1=p_2=p=1-e^{-2t}\) and \(t\ge0\), this is a completely positive trace-preserving (CPTP) channel **if and only if**
\[
0\le t\le t_*:=\frac{\log 2}{2}.
\]
For larger times, the square root in \(E_4\) is no longer real. If it is interpreted as the principal complex square root, the sum of Kraus operators still defines a completely positive map, but it is not trace preserving. Define
\[
\delta=2(1-r)(2p-1)_+,
\qquad (z)_+=\max\{z,0\}.
\]
For the exact initial family \(\rho_\alpha\) in Eq. (8) of the source and \(2\le\alpha\le4\), the output \(R_\alpha=(\Phi\otimes\Phi)(\rho_\alpha)\) satisfies, at **every** finite \(t\ge0\),
\[
R_\alpha^{T_B}\succeq0,
\qquad \operatorname{Tr}R_\alpha=1+\frac{2\delta}{3}+\frac{\alpha\delta^2}{21}.
\]
Thus the physical channel never creates negative partial transpose (NPT) from these initially PPT states. If the formula \(\|R_\alpha^{T_B}\|_1-1\), valid as an entanglement negativity convention for trace-one matrices, is used on the **unnormalized** output instead, it produces the strictly positive but spurious signal
\[
\|R_\alpha^{T_B}\|_1-1=\frac{2\delta}{3}+\frac{\alpha\delta^2}{21}
\]
precisely when \(t>t_*\). After dividing by its positive trace, the physical negativity is zero. For the rational values \(p=3/4\), \(r=3/20\) and \(\alpha=5/2\), the unnormalized signal is exactly \(731/1120\), whereas normalized negativity remains zero. This gives an exact model-specific obstruction to the local-noise distillability-sudden-birth interpretation proposed for the separable and bound-entangled members of this family.

## Assumptions and scope
The local computational basis is \(|0\rangle,|1\rangle,|2\rangle\). For parameters \(0\le r<1\), \(0\le p_1,p_2\le1\), the source's operators are
\[
\begin{aligned}
E_1&=\sqrt r\operatorname{diag}(1,\sqrt{1-p_1},\sqrt{1-p_2}),\\
E_2&=\sqrt{rp_1}|0\rangle\langle1|,\quad
E_3=\sqrt{rp_2}|0\rangle\langle2|,\\
E_4&=\sqrt{1-r}\operatorname{diag}(\sqrt{1-p_1-p_2},1,1),\\
E_5&=\sqrt{(1-r)p_1}|1\rangle\langle0|,\quad
E_6=\sqrt{(1-r)p_2}|2\rangle\langle0|.
\end{aligned}
\]
Above the threshold \(p_1+p_2>1\), complex square roots mean the ordinary complex continuation; they are **not** interpreted as formal real square roots or negative probability weights. The state is
\[
\rho_\alpha=\frac27|\psi\rangle\langle\psi|+
\frac\alpha7\sigma_++\frac{5-\alpha}7\sigma_-,
\quad|\psi\rangle=\frac{|01\rangle+|10\rangle+|22\rangle}{\sqrt3},
\]
where \(\sigma_+=(|00\rangle\langle00|+|12\rangle\langle12|+|21\rangle\langle21|)/3\) and \(\sigma_-=(|11\rangle\langle11|+|20\rangle\langle20|+|02\rangle\langle02|)/3\). The parameter interval \(2\le\alpha\le4\) covers both separable (\(2\le\alpha\le3\)) and PPT-bound-entangled (\(3<\alpha\le4\)) cases. The assertion makes no claim about a globally coupled reservoir or about inputs initially NPT. The special endpoint \(r=1\) has no absorption branch and is excluded from the stated sharp time bound; there the displayed Kraus sum is trace preserving for all \(p\in[0,1]\).

## Proof
Write \(s=p_1+p_2\). Direct multiplication of the six matrices, with Hermitian adjoints rather than algebraic transposes, gives
\[
\sum_{j=1}^6 E_j^\dagger E_j
=rI+(1-r)\operatorname{diag}(|1-s|+s,1,1)
=I+2(1-r)(s-1)_+|0\rangle\langle0|.
\]
In the equal-rate specialization \(s=2p\), it follows that \(\delta=2(1-r)(2p-1)_+\). For \(r<1\), trace preservation holds precisely for \(p\le1/2\), namely \(t\le(\log2)/2\), and fails strictly for every greater time. Since each complex matrix \(E_j\) still defines a completely positive summand, positivity is not the issue; normalization is.

For the original Horodecki family, each marginal is exactly maximally mixed, and the weight of \(|00\rangle\langle00|\) is \(\alpha/21\):
\[
\operatorname{Tr}_A\rho_\alpha=\operatorname{Tr}_B\rho_\alpha=I/3,
\qquad \langle00|\rho_\alpha|00\rangle=\frac\alpha{21}.
\]
Using \(Q=\sum_jE_j^\dagger E_j=I+\delta P_0\), \(P_0=|0\rangle\langle0|\), cyclicity of trace therefore yields
\[
\begin{aligned}
\operatorname{Tr}R_\alpha
&=\operatorname{Tr}\bigl[\rho_\alpha(Q\otimes Q)\bigr]\\
&=1+\delta\operatorname{Tr}\rho_\alpha(P_0\otimes I+I\otimes P_0)
+\delta^2\operatorname{Tr}\rho_\alpha(P_0\otimes P_0)\\
&=1+\frac{2\delta}{3}+\frac{\alpha\delta^2}{21}.
\end{aligned}
\]

It remains to check the crucial PPT premise independently rather than deduce it from a label. The partial transpose of the explicit \(9\times9\) matrix \(\rho_\alpha\) has three eigenvalues \(2/21\), and two further eigenvalues each of multiplicity three:
\[
\lambda_\pm=\frac{5\pm\sqrt{(2\alpha-5)^2+16}}{42}.
\]
For \(2\le\alpha\le4\) one has \((2\alpha-5)^2\le9\); hence \(\lambda_-\ge0\). For **any** completely positive local operators, whether trace preserving or not,
\[
R_\alpha^{T_B}=\sum_{i,j}(E_i\otimes\overline{E_j})\rho_\alpha^{T_B}
(E_i\otimes\overline{E_j})^\dagger\succeq0.
\]
Thus all normalized outputs are PPT and none realizes PPT-to-NPT birth. For \(R_\alpha^{T_B}\succeq0\), its trace norm equals its trace, producing the stated false unnormalized quantity. At \(p=3/4\), \(r=3/20\), \(\delta=17/20\); for \(\alpha=5/2\),
\[
\frac{2\delta}{3}+\frac{\alpha\delta^2}{21}=\frac{731}{1120}>0.
\]
The cutoff is sharp because the coefficient \(1-r\) is strictly positive and \(p=1-e^{-2t}\) is strictly increasing.

## Verification
All identities follow by finite exact algebra and a positive-semidefinite congruence argument. The standalone `verify.py` reconstructs the rational initial density matrices, both maximally mixed marginals, their \(|00\rangle\) probabilities, the polynomial positivity condition for the partial-transpose eigenvalues, the Kraus completeness sums on both sides of the threshold, and both rational false-signal examples. Execute `python3 verify.py` with Python 3 and the standard library only. The verifier checks exact finite instances and algebraic identities; the proof above establishes the full parameter ranges.

## Relationship to prior work
The source's Eqs. (1)--(8) specify precisely the six matrices and initial family above, while its Fig. 5 and accompanying text interpret late-time curves for \(\alpha=2.5,3.5\) as a separable/PPT-to-NPT sudden birth. Those late-time curves extend beyond the mathematically allowed \(t_*\). The exact completeness and trace-defect computation is not stated in that work. Mazhar Ali's 2014 published comment concerns a different 2012 thermal-reservoir master equation, not these six 2015 Kraus matrices. Ali and Huang's 2014 sudden-birth result concerns **reservoir-reservoir** subsystems, not entanglement generation under independent local channels between the two primary qutrits. A 2020 study of correlated dephasing considers a different channel and does not derive the present cutoff. The general fact that local operations preserve PPT is established background, not claimed as novel here; the model-specific sharp boundary and trace-defect expression are the contribution.

## Limitations
This analysis does not reproduce the numerical implementation behind the source's plotted curves, so it does **not** assert that the formula for the unnormalized trace norm numerically reproduces those plots. It establishes that the model as printed cannot support the stated physical interpretation: for later times it is not trace preserving and its complex continuation cannot generate NPT from PPT. The calculation does not rule out genuinely nonlocal, reservoir-mediated, or initially NPT entanglement dynamics. Novelty cannot exclude all unindexed presentations of the same model-specific identity; the earlier 2014 comment has only been compared at the available abstract/preview level.

## References
1. Y.-n. Guo, M.-f. Fang, G.-y. Wang, K. Zeng, *Distillability sudden death and sudden birth in a two-qutrit system under decoherence of finite temperature*, arXiv:1506.02743 (first submitted 9 June 2015); Quantum Information Processing **15** (2016), 2851--2861, DOI:10.1007/s11128-016-1296-x.
2. M. Ali, *Comments on “Distillability sudden death in qutrit--qutrit systems under thermal reservoirs”*, Chinese Physics B **23** (2014), 090306, DOI:10.1088/1674-1056/23/9/090306.
3. M. Ali and J. Huang, *Distillability Sudden Birth of Entanglement for Qutrit--Qutrit Systems*, Chinese Physics Letters **31** (2014), 110301, DOI:10.1088/0256-307X/31/11/110301.
4. G. Xue and L. Qiu, *Postponing Distillability Sudden Death in a Correlated Dephasing Channel*, Entropy **22** (2020), 827, DOI:10.3390/e22080827.
