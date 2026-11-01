# Sharp two-step Cesàro defect norms and finite-section convergence

## Finding
For every integer \(n\ge 1\), let \(C_n\) average the first \(i\) entries at coordinate \(i\), and set \(T_n=(I-C_n)^2\). Put \(H_0=0\) and \(H_m=\sum_{r=1}^{m}1/r\). Let \(k_n\) count the indices \(1\le j<n\) satisfying \(H_n-H_{j-1}>2\). Then the following exact, attained formula holds:
\[
\|T_n\|_{\ell_\infty^n\to\ell_\infty^n}=2(1-1/n)^2+\frac{2k_n}{n}(H_n-H_{k_n}-1).
\]
The unique norm-maximizing matrix row is the last row for every \(n\ge2\). In particular, the norms strictly increase with \(n\) and
\[
\|T_n\|=2+2e^{-2}-\frac{5-e^{-2}}{n}+O(n^{-2}),\qquad n\to\infty.
\]
The associated infinite two-step defect on \(\ell_\infty(\mathbb N)\) therefore has exact norm \(2+2e^{-2}\).

## Assumptions and scope
All spaces and operators are real. Define \((C_nf)_i=i^{-1}\sum_{j=1}^i f_j\) for \(1\le i\le n\), with the usual maximum norm. The infinite operator uses the identical coordinate formula on bounded sequences. For \(n=1\), the norm is zero and the formula uses \(k_1=0\). For \(n\ge2\), \(k_n\) is the length of an initial segment of \(\{1,\dots,n-1\}\); the strict inequality convention excludes zero kernel entries. The \(O\)-term is absolute.

## Proof
The exact twofold Cesàro kernel is \((C_n^2)_{ij}=\frac1i\sum_{r=j}^i\frac1r=(H_i-H_{j-1})/i\) when \(j\le i\), and zero otherwise. Thus \((T_n)_{ii}=(1-1/i)^2\), and for \(j<i\), \((T_n)_{ij}=(H_i-H_{j-1}-2)/i\). Every row of \(T_n\) sums to zero. If \(k_i\) is the number of strictly positive off-diagonal entries, the diagonal plus twice the total positive off-diagonal mass gives its absolute row sum. Since \(\sum_{j=0}^{k-1}H_j=k(H_k-1)\), this is exactly
\[
R_i=2(1-1/i)^2+\frac{2k_i}{i}(H_i-H_{k_i}-1).
\]

To prove strict row ordering, set \(P_i=\sum_{1\le j<i}(H_i-H_{j-1}-2)_+=k_i(H_i-H_{k_i}-1)\). Writing \(k=k_i\), \(\delta=1/(i+1)\), and \(\varepsilon=2-(H_i-H_k)\ge0\), precisely zero or one new index becomes positive on passing to row \(i+1\). Indeed, adjacent thresholds have gaps at least \(1/(i)\), exceeding \(\delta\). Consequently
\[
P_{i+1}-P_i=k\delta+(\delta-\varepsilon)_+,
\quad i(P_{i+1}-P_i)-P_i=k(\varepsilon-\delta)+i(\delta-\varepsilon)_+\ge0.
\]
In the case \(\varepsilon\ge\delta\), the last expression equals \(k(\varepsilon-\delta)\); otherwise it equals \((i-k)(\delta-\varepsilon)\). Hence \(P_i/i\) is nondecreasing. Since \((1-1/i)^2\) strictly increases from \(i=1\), the row norms \(R_i\) strictly increase for \(i\ge1\). The induced maximum-row-sum identity proves the formula and uniqueness of the maximizing row. Choosing signs of that last row gives an input attaining the norm.

For the asymptotic, harmonic-number comparison with the logarithm yields \(k_n=e^{-2}n+O(1)\). Uniformly for such integers,
\[
H_n-H_{k_n}=\log(n/k_n)+\frac1{2n}-\frac1{2k_n}+O(n^{-2}).
\]
Writing \(q=e^{-2}\) and \(k_n=qn+O(1)\), Taylor expansion gives
\[
\frac{k_n}{n}(H_n-H_{k_n}-1)=q+\frac{q-1}{2n}+O(n^{-2}).
\]
The possible integer rounding of \(k_n\) cancels at order \(1/n\) because \(q\) is the stationary point of \(x(\log(1/x)-1)\). Substitution yields the announced sharp correction. On \(\ell_\infty\), the operator norm is the supremum of the finite row norms, equal to their limit.

## Verification
The accompanying standalone program `cesaro_two_step_verify.py` constructs \(I-2C_n+C_n^2\) independently over exact rational numbers. It verifies individual kernel entries, the formula for every row, and strict row ordering across sizes \(1\le n\le28\), together with seven floating-point asymptotic profiles up to size \(8192\). It printed `PASSED ... 8505`. These finite checks corroborate but do not replace the proof for arbitrary sizes.

## Relationship to prior work
The finite discrete Cesàro operator and its spectral properties appear in the 2014 study of extended eigenvalues; that is the source for the operator setting, not a claimed derivation of this norm law. Sinnamon's 2021 analysis determines norms of the **first** defect \(C-I\), which does not imply the sharp norm of its square. Published records on finite Cesàro singular values and self-commutators concern Hilbert-space spectra or different bilinear objects, not the absolute row sums proved here. An earlier equivalent computation under the labels Hardy averaging or Hausdorff operators remains possible.

## Limitations
The exact law concerns the second power of the **unweighted prefix-average** Cesàro defect on real maximum-norm sequence spaces. It does not determine higher integer powers, weighted averages, \(\ell^p\) norms at finite \(p\), or the behavior of nonlinear averaging. The finite computations are not an exhaustive prior-literature search, and independent verification has not been performed.

## References
- Lacruz and collaborators, *Extended eigenvalues for Cesàro operators*, arXiv:1403.4844v1 (first publicly available 2014-03-19): https://arxiv.org/abs/1403.4844 .
- Gord Sinnamon, *Norm of the discrete Cesàro operator minus identity*, arXiv:2105.14200 (first publicly available 2021-05-29): https://arxiv.org/abs/2105.14200 .
