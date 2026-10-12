# Hamming-one detector shells on hypercubes: exact capture and a parity-protected mode

## Finding
For every integer \(n\ge2\), let \(Q_n\) be the hypercube with vertices \(x\in\{0,1\}^n\), let \(H=J\sum_{i=1}^n X_i\) with real \(J\ne0\), and install a positive local loss at **each** of the \(n\) vertices \(e_i\) of Hamming weight one. Each loss strength may be different. Write \(\mathcal B\) for the eventually absorbed (bright) subspace and \(\mathcal D\) for its orthogonal complement. Then
\[
\dim\mathcal B=n^2-n+2-\mathbf1_{\{2\mid n\}},\qquad
\dim\mathcal D=2^n-n^2+n-2+\mathbf1_{\{2\mid n\}}.
\]
For a walker initially localized at a vertex \(x\) of Hamming weight \(d\), the eventual capture probability depends only on \(d\) and equals
\[
C_n(d)=\frac{1+(n-1)\mathbf1_{\{1\le d\le n-1\}}}{\binom nd}
-\mathbf1_{\{2\mid n\}}\frac{K_{n/2}(d)^2}{2^n\binom n{n/2}},
\qquad 0\le d\le n,
\]
where \(K_k(d)=\sum_{j=0}^k(-1)^j\binom dj\binom{n-d}{k-j}\), with out-of-range binomial coefficients defined to be zero. In particular, for odd \(n\), the capture probability is \(1\) at either antipode and is \(n/\binom nd\) at intermediate distances. For even \(n\), the second term is nonzero only at even distances, and
\[
C_n(0)=C_n(n)=1-\frac{\binom n{n/2}}{2^n}.
\]
As a detector-placement consequence, adding losses at **all** antipodes of the weight-one detector vertices (the entire weight-\(n-1\) layer) adds no new absorbing directions. Adding a loss at the origin adds exactly one absorbing direction for even \(n\), but none for odd \(n\). The latter assertion concerns subspace dimension, not finite-time absorption rate.

## Assumptions and scope
The Hilbert space has dimension \(2^n\) with orthonormal vertex basis \(\{|x\rangle\}\). Let \(\gamma_i>0\) be arbitrary, not necessarily equal, and define
\[
K=H-\frac{i}{2}\sum_{i=1}^n\gamma_i|e_i\rangle\langle e_i|,
\qquad T(t)=e^{-iKt}.
\]
The survival probability of a density matrix \(\rho\ge0\), \(\operatorname{Tr}\rho=1\), is \(\operatorname{Tr}[T(t)\rho T(t)^\dagger]\), with capture probability its complement. Define
\[
\mathcal B=\operatorname{span}\{H^r|e_i\rangle:0\le r<2^n,\ 1\le i\le n\},\qquad
\mathcal D=\mathcal B^\perp.
\]
For every such density matrix, the eventual capture probability equals \(\operatorname{Tr}(P_{\mathcal B}\rho)\). No convergence of the **unnormalized density matrix itself** is asserted: the protected component can continue unitary oscillation. There are no onsite potentials, dephasing, interactions, or additional couplings; the limit is taken at fixed strictly positive loss rates.

## Proof
**1. Decay reduces to a spectral span.** The cyclic subspace \(\mathcal B\) is invariant under Hermitian \(H\) and therefore reducing. It contains the supports of all loss projectors; its orthogonal complement \(\mathcal D\) is reducing for \(H\), annihilated by each loss projector, and hence evolves unitarily. An eigenvector \(v\) of \(K|_{\mathcal B}\) with eigenvalue \(z\) satisfies
\[
\operatorname{Im}z\,\|v\|^2=-\frac12\sum_i\gamma_i|\langle e_i|v\rangle|^2\le0.
\]
Equality would force \(v\perp e_i\) for every detector and \(Hv=zv\), hence \(v\perp H^r e_i\) for all \(r\), contradicting \(v\in\mathcal B\) unless \(v=0\). Thus all eigenvalues of \(K|_{\mathcal B}\) have strictly negative imaginary parts. Finite-dimensional Jordan theory gives exponential decay on \(\mathcal B\); only the \(\mathcal D\) norm survives. This establishes the capture-projector rule and the independence of all positive \(\gamma_i\).

**2. Exact Fourier rank in each energy.** The normalized Walsh characters
\[
\chi_S(x)=2^{-n/2}(-1)^{|S\cap\operatorname{supp}x|},\qquad S\subseteq\{1,\ldots,n\},
\]
are eigenvectors of \(H\) with eigenvalue \(J(n-2|S|)\). On the eigenspace with \(|S|=k\), the detector columns have entries proportional to \(v_i(S)=1-2\mathbf1_{\{i\in S\}}\). If \(1\le k\le n-1\) and \(\sum_i a_i v_i(S)=0\) for all \(k\)-subsets \(S\), comparing \(k\)-subsets that differ by exchanging \(i\) and \(j\) yields \(a_i=a_j\) for all indices. The constant coefficient vector then yields \(a_i(n-2k)=0\). Thus the detector projections have rank \(n\) unless \(2k=n\), when the rank is \(n-1\). At \(k=0,n\), the rank is one. Orthogonality of the distinct eigenspaces gives
\[
\dim\mathcal B=1+\sum_{k=1}^{n-1}\bigl(n-\mathbf1_{\{2k=n\}}\bigr)+1
=n^2-n+2-\mathbf1_{\{2\mid n\}}.
\]

**3. A geometric realization of the full captured projector.** For each Hamming layer \(L_d=\{x:|x|=d\}\), define \(E_d\) as the functions on \(L_d\) expressible as
\[
f(x)=a_d+\sum_{i=1}^n b_{d,i}x_i,\qquad\sum_i b_{d,i}=0.
\]
At the two singleton layers \(d=0,n\), this space is just the constants. On every interior layer, the centered coordinate restrictions are independent and have dimension \(n-1\), so \(\dim E_d=n\). Write \(E=\bigoplus_{d=0}^n E_d\), of dimension \(n^2-n+2\). Every detector vector \(|e_i\rangle\) lies in \(E\). Moreover \(E\) is invariant under \(H\): with \(b_{0,i}=b_{n,i}=0\), summing over the neighbors of a vertex of weight \(d\) gives a new scalar coefficient \(J[d a_{d-1}+(n-d)a_{d+1}]\) and a new centered coefficient vector
\[
J[(d-1)b_{d-1}+(n-d-1)b_{d+1}],
\]
where terms at nonexistent layers are omitted. Consequently \(\mathcal B\subseteq E\), and the rank count above implies \(\mathcal B=E\) for odd \(n\).

For even \(n\), the normalized middle-energy radial eigenvector is
\[
q(x)=\frac{K_{n/2}(|x|)}{\sqrt{2^n\binom n{n/2}}}.
\]
It lies in \(E\), has unit norm by Walsh orthogonality, and satisfies \(Hq=0\). The identity \(K_{n/2}(1)=0\) makes it orthogonal to each \(|e_i\rangle\); hence \(q\in\mathcal D\). Since \(\mathcal B\) has codimension one in \(E\), this identifies
\[
\mathcal B=E\cap q^\perp\qquad\text{for even }n.
\]

**4. Exact sitewise diagonal.** Within each layer \(L_d\), the projector onto \(E_d\) has constant diagonal by coordinate-permutation symmetry, equal to \(\dim E_d/\binom nd\) because the diagonal sum equals its rank. The projector onto \(E\) is the direct sum of these layer projectors. Subtracting \(|q\rangle\langle q|\) precisely when \(n\) is even gives the displayed formula for \(C_n(d)=\langle x|P_{\mathcal B}|x\rangle\). The Krawtchouk identity
\[
\binom nd K_{n/2}(d)=\binom n{n/2}K_d(n/2)
\]
and \(\sum_{d=0}^n K_d(n/2)t^d=(1-t^2)^{n/2}\) imply that, for even \(n\), \(K_{n/2}(d)=0\) for odd \(d\), and give the equivalent correction
\[
\frac{K_{n/2}(d)^2}{2^n\binom n{n/2}}
=\frac{\binom n{n/2}}{2^n}
\left(\frac{\binom{n/2}{d/2}}{\binom nd}\right)^2
\quad\text{for even }d.
\]

**5. Detector redundancy and one-dimensional parity repair.** Adding detector vertices augments the bright space by their \(H\)-cyclic spans. Every vertex vector on \(L_{n-1}\) lies in \(E\). If \(n\) is even, \(n-1\) is odd, so \(q\) vanishes on this layer; hence all these vertices already lie in \(\mathcal B=E\cap q^\perp\). If \(n\) is odd, \(\mathcal B=E\) directly. Thus the antipodal weight-\(n-1\) shell changes no bright dimension. Similarly, the origin vector belongs to \(E\); it belongs to \(\mathcal B\) if \(n\) is odd, but if \(n\) is even its overlap \(q(0)=\sqrt{\binom n{n/2}/2^n}\) is nonzero. Adding it therefore restores exactly the missing one-dimensional direction, independently of any strictly positive rates. This completes the proof.

## Verification
The accompanying `verify.py` constructs the full \(2^n\)-vertex adjacency matrix and projects onto the detector-visible eigenvectors of each exactly identified energy. It independently checks all \(252\) sitewise probabilities and six bright dimensions for \(2\le n\le7\), and ten comparisons after adding the origin or antipodal shell for \(2\le n\le6\). It reports:

`VERIFY_OK_shell_probabilities=252_dimensions=6_auxiliary=10`

Run `python verify.py` after installing the packages in `requirements.txt`. Numeric eigenspaces are matched at tolerance \(10^{-8}\), and probabilities are compared at tolerance \(5\cdot10^{-9}\); the exact general statements follow from the preceding proof rather than this finite test. For orientation, \(\dim\mathcal B=13\) on the four-cube, whereas \(\dim\mathcal B=22\) on the five-cube.

## Relationship to prior work
Yamasaki, Kobayashi, and Imai studied absorbing **discrete-time coined** quantum walks on a hypercube, including a one-target Hamming-distance formula conjecture that numerically matches the **odd-dimensional** value above. Their walk model, detector geometry, and result status differ: it is not the continuous-time, all-neighbor-shell theorem here. Krovi and Brun analyzed general degeneracy and infinite-hitting-time mechanisms, including continuous-time walks. Razzoli, Paris, and Bordone provide the continuous-time single-trap projector method and examples; their general methodology underlies the spectral-reduction step, but their treated detector sets do not evaluate the present hypercube shell. Agliari, Mülken, and Blumen studied continuous-time trapping on other graphs. The specific evaluated contributions claimed here are the all-neighbor-shell rank, the exact parity-corrected sitewise law, and the redundancy/one-dimensional repair classification for the two additional detector geometries; the general bright/dark formalism itself is not claimed as new.

## Limitations
The result requires uniform nearest-neighbor hypercube hopping, all weight-one vertices as absorbers, and positive sitewise loss strengths. It says nothing about finite-time decay constants as loss rates tend to zero, interactions, disorder, dephasing, or stability under unequal edge weights. The result does not establish a minimum-cardinality detector set among arbitrary placements. The odd-dimensional sitewise expression coincides numerically with an earlier conjectural expression from a different discrete-time model; the distinction is the quantum dynamics and detector arrangement, not numerical novelty of that special formula. Although relevant prior full texts and mathematical records were compared, the possibility of an unlocated equivalent specialization remains a publication-priority risk; no independent priority audit is asserted.

## References
1. T. Yamasaki, H. Kobayashi, H. Imai, *Analysis of Absorbing Times of Quantum Walks*, arXiv:quant-ph/0205045, version 1 first public 2002-05-09. https://arxiv.org/abs/quant-ph/0205045
2. H. Krovi, T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094 (2006). https://arxiv.org/abs/quant-ph/0606094
3. V. Varbanov, H. Krovi, T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446 (2008). https://arxiv.org/abs/0803.3446
4. E. Agliari, O. Mülken, A. Blumen, *Continuous-Time Quantum Walks and Trapping*, arXiv:0903.3288 (2009). https://arxiv.org/abs/0903.3288
5. L. Razzoli, M. G. A. Paris, B. Bordone, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, Entropy 23 (2021), 85. https://doi.org/10.3390/e23010085
