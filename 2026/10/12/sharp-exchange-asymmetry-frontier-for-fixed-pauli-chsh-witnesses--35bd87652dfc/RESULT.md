# Sharp exchange-asymmetry frontier for fixed-Pauli CHSH witnesses

## Finding
Let \(S\) be the two-qubit exchange (SWAP) operator, \(X,Z\) the usual Pauli matrices, and let
\[
 B_0=X\otimes X+X\otimes Z-Z\otimes X+Z\otimes Z.
\]
For a density operator \(\rho\) on \(\mathbb C^2\otimes\mathbb C^2\), define its exchange-asymmetry trace distance
\[
 \delta(\rho)=\frac12\|\rho-S\rho S\|_1.
\]
Then for **every** \(d\in[0,1]\), the **exact signed and absolute Bell frontiers** are
\[
 \max_{\rho\ge0,\ \operatorname{Tr}\rho=1,\ \delta(\rho)=d}
 \operatorname{Tr}(B_0\rho)
 =\max_{\rho\ge0,\ \operatorname{Tr}\rho=1,\ \delta(\rho)=d}
 |\operatorname{Tr}(B_0\rho)|
 =2\bigl(d+\sqrt{1-d^2}\bigr).
\]
Both maxima are attained by pure states. In particular, the maximal value is \(2\) at both \(d=0\) and \(d=1\), and equals the Tsirelson bound \(2\sqrt2\) only at \(d=1/\sqrt2\).

An exact inverse form quantifies exchange-symmetry breaking from an observed fixed-setting Bell value: for every \(2<\beta\le2\sqrt2\),
\[
 |\operatorname{Tr}(B_0\rho)|\ge\beta
 \quad\Longrightarrow\quad
 \frac{\beta-\sqrt{8-\beta^2}}4
 \le\delta(\rho)\le
 \frac{\beta+\sqrt{8-\beta^2}}4.
\]
The endpoints of these necessary bounds are attainable by pure states with Bell value \(\beta\). Thus the sharp constraint is **nonmonotone**: both nearly symmetric and nearly maximally exchange-asymmetric states have limited fixed-Pauli CHSH violation.

## Assumptions and scope
Qubits are distinguishable two-level subsystems and \(\rho\) is any positive semidefinite \(4\times4\) matrix with unit trace, including mixed states. \(S|i,j\rangle=|j,i\rangle\); the trace norm is the sum of singular values. The Bell operator and Pauli axes are **fixed** (not optimized over local measurement directions). The normed asymmetry is state-based, not an arbitrary operator norm for a channel.

Put
\[
 |\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2,\qquad
 |\Psi^-\rangle=(|01\rangle-|10\rangle)/\sqrt2.
\]
For \(d\in[0,1]\), let \(q=\sqrt{1-d^2}\), \(r=\sqrt{(1+q)/2}\), and \(s=\sqrt{(1-q)/2}\). An equality state for the positive frontier is
\[
 |\psi_d\rangle=r|\Phi^+\rangle-s|\Psi^-\rangle.
\]
The analogous negative extremizer is \(s|\Phi^+\rangle+r|\Psi^-\rangle\).

## Proof
Let \(P_+=(I+S)/2\) and \(P_-=(I-S)/2\). The symmetric subspace has dimension three, while \(P_-\) is the rank-one projector onto \(|\Psi^-\rangle\). Express \(\rho\) in this orthogonal decomposition as
\[
 \rho=\begin{pmatrix}A&w\\w^\dagger&b\end{pmatrix},\qquad
 A\ge0,\quad b\ge0,\quad\operatorname{Tr}A+b=1,
\]
with \(w\) a three-component column. Since
\[
 \rho-S\rho S=\begin{pmatrix}0&2w\\2w^\dagger&0\end{pmatrix},
\]
its only possibly nonzero eigenvalues are \(\pm2\|w\|_2\), and hence \(d=2\|w\|_2\). Positivity (the Schur complement when \(b>0\), and continuity at \(b=0\)) gives
\[
 \|w\|_2^2\le b(1-b),\quad
 b_-\le b\le b_+,\quad
 b_\pm=(1\pm\sqrt{1-d^2})/2.
\]
The exact Bell-basis matrix in the ordered basis \((|\Phi^+\rangle,|\Psi^+\rangle,|\Phi^-\rangle,|\Psi^-\rangle)\) is
\[
 B_0=\begin{pmatrix}2&0&0&-2\\0&0&0&0\\0&0&0&0\\-2&0&0&-2\end{pmatrix}.
\]
Write \(a=\langle\Phi^+|A|\Phi^+\rangle\) and \(c=\langle\Phi^+|w\rangle\). Then \(|c|\le\|w\|_2=d/2\), \(a\le1-b\), and
\[
 \operatorname{Tr}(B_0\rho)=2(a-b)-4\operatorname{Re}c
 \le2(1-2b+d)
 \le2(\sqrt{1-d^2}+d).
\]
To cover the **absolute** bound, suppose first \(d>0\). Then \(b>0\), and the positive semidefinite \(2\times2\) principal submatrix on \((|\Phi^+\rangle,|\Psi^-\rangle)\) implies \(a\ge|c|^2/b\). Putting \(t=|c|\le d/2\) yields
\[
 -\tfrac12\operatorname{Tr}(B_0\rho)
 \le b-\frac{t^2}{b}+2t.
\]
The right side increases with \(b\), so replace \(b\) by \(b_+\). Since \(b_+\ge d/2\), its derivative in \(t\) is \(2-2t/b_+\ge0\) for \(0\le t\le d/2\). It is therefore at most
\[
 b_+-\frac{d^2}{4b_+}+d
 =b_+-b_-+d=\sqrt{1-d^2}+d.
\]
At \(d=0\), the off-diagonal block vanishes and \(2(a-b)\in[-2,2]\), proving the same bound.

For the stated positive witness, \(b=s^2=b_-\), \(w=-rs|\Phi^+\rangle\), \(d=2rs\), and \(a=r^2\). Direct evaluation gives \(\operatorname{Tr}(B_0|\psi_d\rangle\langle\psi_d|)=2(r^2-s^2+2rs)=2(\sqrt{1-d^2}+d)\). The negative witness analogously attains the negative of this number. This proves both exact maxima for **all** \(d\). Differentiation shows a unique maximum at \(d=1/\sqrt2\). Solving \(d+\sqrt{1-d^2}\ge\beta/2\) gives the inverse interval, with endpoint attainment as above.

## Verification
The accompanying standalone standard-library Python script `verify.py` checks the full Bell-basis matrix exactly, 1,720 exact-rational extremizer evaluations, and 12,000 deterministic random positive density matrices of ranks one to four. Each random case verifies both the signed absolute frontier and the squared Frobenius norm identity \(\|\rho-S\rho S\|_2^2=2d^2\). The executed script printed `VERIFY_OK 13720 exact-rational witness and numerical-state checks`. Computations are finite corroboration; the all-state conclusion comes from the preceding block-positivity proof.

## Relationship to prior work
Cusumano and collaborators, *Non-stabilizerness and violations of CHSH inequalities* (arXiv:2504.03351, first public 2025-04-04), define precisely this resource-free Pauli CHSH operator. Their Theorem 2 proves **qualitative** nonviolation for the output of a swap-covariant channel acting on a swap-invariant input. The present exact all-density-operator frontier at a fixed, nonzero **trace-norm exchange defect** is a quantitative refinement, not a claim to the previously known qualitative symmetry obstruction. Their Schmidt-coefficient optimization over all measurement directions addresses a different optimization domain.

Lyyra and collaborators (2017) analyze swap symmetry in **noise-location dependence** of optimized Bell functions for particular channels and X states; their trace-distance discord is not the trace distance to the swapped state. Their results neither state nor determine this sharp fixed-observable frontier. The Horodecki optimized-setting criterion is likewise different because local axes vary, and here they do not. Literature and published-record searches did not identify a statement-equivalent all-state frontier; derivation through unindexed norm-constrained semidefinite duality remains a residual originality risk.

## Limitations
The inverse bounds require a Bell value in the stated range and apply **only** to the fixed operator \(B_0\). A swap-symmetric maximally entangled state can violate a differently oriented CHSH test. Exchange-asymmetry alone does not guarantee violation for a particular state: the theorem is a sharp maximum at each prescribed asymmetry. There is no assertion concerning efficiency of preparing extremizers, robustness under arbitrary measurement drift, or any independent external validation.

## References
1. S. Cusumano et al., *Non-stabilizerness and violations of CHSH inequalities*, arXiv:2504.03351v1 (2025-04-04), current full text v3 (2026-09-07), *Quantum* **10**, 2214 (2026), DOI: 10.22331/q-2026-09-21-2214. Theorem 2 and Sections 2, 4; appendices checked. https://arxiv.org/html/2504.03351v3
2. H. Lyyra, G. Karpat, C.-F. Li, G.-C. Guo, J. Piilo, and S. Maniscalco, *Symmetry in the open-system dynamics of quantum correlations*, *Scientific Reports* **7**, 8367 (2017), DOI: 10.1038/s41598-017-08457-1. https://www.nature.com/articles/s41598-017-08457-1
3. R. Horodecki, P. Horodecki, and M. Horodecki, *Violating Bell inequality by mixed spin-1/2 states: necessary and sufficient condition*, *Physics Letters A* **200**, 340–344 (1995). Measurement-optimized CHSH criterion, used only as contrast.
