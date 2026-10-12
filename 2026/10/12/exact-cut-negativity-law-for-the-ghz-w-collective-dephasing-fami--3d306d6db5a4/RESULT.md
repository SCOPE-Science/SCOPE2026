# Exact cut-negativity law for the GHZ--W collective-dephasing family
## Finding
For \(0\le \eta\le1\) and \(0\le s\le1\), define the three-qubit GHZ--W dephasing family
\[\rho_{\eta,s}=\frac{1-\eta}{2}\bigl(|000\rangle\langle000|+|111\rangle\langle111|+s|000\rangle\langle111|+s|111\rangle\langle000|\bigr)+\eta|W\rangle\langle W|,\]
where \(|W\rangle=(|001\rangle+|010\rangle+|100\rangle)/\sqrt3\). Across every one-qubit-versus-two-qubit bipartition its negativity is exactly
\[\mathcal N(\rho_{\eta,s})=\frac{\sqrt{41\eta^2-18\eta+9}-3(1-\eta)}{12}+\frac{\sqrt{\eta^2+9(1-\eta)^2s^2}-\eta}{6}.\]
For \(0\le\eta<1\) this quantity is strictly increasing in \(s\) on \((0,1]\). Hence along any collective-dephasing trajectory for which the GHZ coherence parameter \(s(t)\) strictly decreases, every one-versus-two cut negativity strictly decreases; there is no cut-negativity plateau. For every \(\eta>0\) the asymptotic value at \(s=0\) remains positive and equals \([\sqrt{41\eta^2-18\eta+9}-3(1-\eta)]/12\). This is an exact analytic bipartition-entanglement baseline for the GHZ--W family used to probe time-invariant genuine tripartite entanglement; it does not assert an analytic formula for the genuine-negativity SDP.

## Assumptions and scope
The state family is the permutation-symmetric mixture singled out in the three-qubit collective-dephasing literature. The scalar \(s\in[0,1]\) is the surviving real GHZ coherence relative to its initial value. Negativity is \(\mathcal N(\rho)=(\|\rho^{T_A}\|_1-1)/2\). Permutation symmetry makes all three one-versus-two cuts identical.

## Proof
Partially transposing the first qubit in the computational basis splits the matrix into elementary blocks. Its eigenvalues are
\[0,0,\frac{2\eta}{3},\frac{1-\eta}{2},\frac{3(1-\eta)\pm\sqrt{41\eta^2-18\eta+9}}{12},\frac{\eta\pm\sqrt{\eta^2+9(1-\eta)^2s^2}}{6}.\]
The minus member of the first square-root pair is nonpositive because
\[41\eta^2-18\eta+9-9(1-\eta)^2=32\eta^2,\]
and is strictly negative for \(\eta>0\). The minus member of the second pair is nonpositive and is strictly negative exactly when \(s>0\) and \(\eta<1\). Summing the absolute values of the negative eigenvalues yields the formula.

For \(0\le\eta<1\) and \(s>0\),
\[\frac{\partial\mathcal N}{\partial s}=\frac{3(1-\eta)^2s}{2\sqrt{\eta^2+9(1-\eta)^2s^2}}>0.\]
Thus any trajectory with strictly decreasing \(s(t)\) has strictly decreasing cut negativity. Setting \(s=0\) gives the exact asymptotic floor.

## Verification
The companion `verify.py` reconstructs representative partial-transpose matrices, diagonalizes them with a standard-library Jacobi routine, and compares the resulting negativity with the closed formula. These finite checks supplement, but do not replace, the analytic block-spectrum proof.

## Relationship to prior work
Carnio, Buchleitner and Gessner developed a broad collective-dephasing framework and emphasized protection and time-invariant entanglement. Ali later selected the GHZ--W mixture for three qubits, stated that analytic genuine negativity was difficult, and reported numerical genuine-negativity curves. The present claim concerns ordinary one-versus-two negativity, not genuine negativity, and supplies its complete closed form for that same family. Ali's later follow-up concerns freezing of genuine multipartite entanglement and does not imply this cut-negativity spectrum.

## Limitations
The result does not evaluate the genuine-negativity semidefinite program and therefore neither proves nor disproves the three-qubit genuine-entanglement conjecture. It is restricted to this GHZ--W family and ordinary one-versus-two negativity. A residual originality risk remains for an equivalent formula under different notation in later dephasing literature.

## References
1. E. G. Carnio, A. Buchleitner, M. Gessner, "Generating and protecting correlated quantum states under collective dephasing," arXiv:1602.08973; New J. Phys. 18, 073010 (2016).
2. M. Ali, "Time-invariant entanglement and sudden death of nonlocality for multipartite systems under collective dephasing," arXiv:1609.01031; Eur. Phys. J. D 71, 40 (2017).
3. M. Ali, "Freezing dynamics of genuine entanglement and loss of genuine nonlocality under collective dephasing," arXiv:1703.09932; Int. J. Quantum Inf. 15, 1750022 (2017).
4. G. Vidal, R. F. Werner, "Computable measure of entanglement," Phys. Rev. A 65, 032314 (2002).
