# Exact Hilbert–Schmidt negativity law in the GHZ cat-state Bloch ball
## Finding
For every integer \(N\ge 2\), let
\[
\mathcal C_N=\operatorname{span}\{|0\rangle^{\otimes N},|1\rangle^{\otimes N}\}
\]
and consider density matrices supported on \(\mathcal C_N\). Sample this three-dimensional state space using its normalized Hilbert–Schmidt volume. For any nontrivial bipartition \(A|B\), define the standard negativity
\[
E=\mathcal N(\rho)=\frac{\|\rho^{T_A}\|_1-1}{2}.
\]
Then the normalized squared negativity
\[
X=4E^2
\]
has the exact distribution
\[
X\sim\operatorname{Beta}(1,3/2),
\]
independently of the number of qubits and independently of the chosen nontrivial bipartition. Thus, for \(0\le e\le1/2\),
\[
\Pr(E\le e)=1-(1-4e^2)^{3/2},
\qquad
f_E(e)=12e\sqrt{1-4e^2}.
\]
The law also factorizes exactly into radial purity and angular entanglement. If \(P=\operatorname{Tr}(\rho^2)\), then
\[
R^2=2P-1\sim\operatorname{Beta}(3/2,1),
\]
while
\[
U=\frac{4E^2}{2P-1}
\]
(on the measure-zero maximally mixed state its value may be assigned arbitrarily) is independent of \(P\) and obeys
\[
U\sim\operatorname{Beta}(1,1/2).
\]
Consequently,
\[
\mathbb E[E\mid P]=\frac{\pi}{8}\sqrt{2P-1},
\qquad
\mathbb E E=\frac{3\pi}{32},
\qquad
\mathbb E E^2=\frac{1}{10}.
\]
The exact low-entanglement tube law is
\[
\Pr(E\le\varepsilon)
=6\varepsilon^2-6\varepsilon^4+O(\varepsilon^6),
\qquad \varepsilon\downarrow0.
\]
This quantitatively sharpens the codimension-two geometry of the separable diameter in the GHZ cat-state Bloch ball.

## Assumptions and scope
The ensemble is **not** the Hilbert–Schmidt ensemble on the full \(2^N\)-dimensional quantum state space. It is normalized Hilbert–Schmidt volume restricted to the affine state space of density matrices whose support is contained in \(\mathcal C_N\). The bipartition \(A|B\) may be any split with both sides nonempty. Negativity uses the normalization \(\mathcal N(\rho)=(\|\rho^{T_A}\|_1-1)/2\), so a maximally entangled state of Schmidt rank two has negativity \(1/2\).

Write every state in the logical cat basis as
\[
\rho(\mathbf n)=\frac12
\begin{pmatrix}
1+n_z & n_x-i n_y\\
n_x+i n_y & 1-n_z
\end{pmatrix},
\qquad \|\mathbf n\|\le1.
\]
Zhou and Joynt identify this GHZ dynamical state space with a three-dimensional Bloch ball and its zero-negativity states with the vertical symmetry axis. Their geometric setup is the motivating object; the probability law stated here is a volume refinement, not a claim about their dynamical dephasing trajectories.

## Proof
For any nontrivial split \(A|B\), the two cat basis vectors become \(|0_A0_B\rangle\) and \(|1_A1_B\rangle\). Put \(c=(n_x-i n_y)/2\). After partial transpose on \(A\), the two off-diagonal cat terms form a \(2\times2\) block with eigenvalues \(\pm|c|\), while the remaining nonzero eigenvalues are \((1+n_z)/2\) and \((1-n_z)/2\). Hence
\[
E=|c|=\frac12\sqrt{n_x^2+n_y^2}.
\]
This argument does not depend on the sizes of \(A\) and \(B\), proving bipartition and qubit-count invariance of the pointwise formula.

The Hilbert–Schmidt line element on this affine space is
\[
\operatorname{Tr}(d\rho^2)=\frac12(dn_x^2+dn_y^2+dn_z^2),
\]
so normalized Hilbert–Schmidt volume is exactly normalized Euclidean volume on the unit Bloch ball. In spherical variables, write \(R=\|\mathbf n\|\) and let \(Z=n_z/R\) away from the origin. Uniform ball volume factorizes into an independent radius and direction: \(R\) has density \(3r^2\) on \([0,1]\), while \(Z\) is uniform on \([-1,1]\). Therefore
\[
R^2\sim\operatorname{Beta}(3/2,1),
\qquad
U=1-Z^2\sim\operatorname{Beta}(1,1/2),
\]
and these variables are independent. Since
\[
4E^2=R^2(1-Z^2)=R^2U,
\]
we obtain the purity–entanglement factorization, using \(P=(1+R^2)/2\).

For the marginal law, set \(s=\sqrt{n_x^2+n_y^2}=2E\). A cylindrical shell of radius \(s\) and thickness \(ds\) in the unit ball has volume
\[
4\pi s\sqrt{1-s^2}\,ds.
\]
Dividing by the ball volume \(4\pi/3\) gives \(f_s(s)=3s\sqrt{1-s^2}\). The change of variables \(s=2e\) yields
\[
f_E(e)=12e\sqrt{1-4e^2},
\]
and integration gives
\[
F_E(e)=1-(1-4e^2)^{3/2}.
\]
Equivalently, \(X=4E^2\) has density \((3/2)\sqrt{1-x}\), which is \(\operatorname{Beta}(1,3/2)\).

At fixed \(R=r\), direction remains uniform, so \(\mathbb E[\sqrt{1-Z^2}]=\pi/4\), giving \(\mathbb E[E\mid P]=\pi\sqrt{2P-1}/8\). Direct integration then gives \(\mathbb E E=3\pi/32\) and \(\mathbb E E^2=1/10\). Expanding the exact CDF at the origin gives the stated tube law.

## Verification
The accompanying `verify.py` independently checks the density normalization, the first two moments, the CDF derivative at interior points, the conditional-to-marginal integration, and the beta-factor moment identity using deterministic high-accuracy quadrature. It is supplementary: the proof above is analytic and does not rely on finite sampling or numerical extrapolation.

## Relationship to prior work
Zhou and Joynt's GHZ section identifies the relevant cat-state support with a Bloch ball and states that zero-negativity states lie on its vertical axis. Their paper is qualitative/topological rather than a probability-law calculation. The GHZ section first appears in the 2011 revision, while the underlying public preprint dates to 2010; the source date recorded here is the earliest public date of that work, not a revision or journal date.

Zhu, Hayashi, and Chen establish general connections between \(l_1\)-coherence and negativity, including maximally correlated structures. That broader pointwise relation is consistent with, and can supply an alternative route to, the pointwise identity \(2E=\sqrt{n_x^2+n_y^2}\); it does not provide the restricted Hilbert–Schmidt distribution, purity factorization, or exact small-entanglement tube law claimed here.

Maziero numerically studies random-state generators and reports sampled average \(l_1\)-coherence, including a figure based on \(10^4\) samples. Zhang, Singh, and Pati derive averages for subentropy and relative-entropy coherence of random mixed states. Neither inspected source gives the exact \(l_1\)/negativity law above. Searches also checked the aliases “random qubit Hilbert–Schmidt \(l_1\) coherence,” “maximally correlated qubit negativity distribution,” and “GHZ cat-subspace negativity distribution.”

## Limitations
The result concerns Hilbert–Schmidt volume conditioned on the two-dimensional GHZ cat support; it makes no statement about the full \(N\)-qubit Hilbert–Schmidt ensemble, Bures measure, induced measures with other ancilla dimensions, or genuine multipartite entanglement measures not reducible to bipartite negativity. The originality assessment retains a residual literature risk that the same elementary beta law may have appeared under a different random-qubit coherence terminology. No independent audit has been performed.

## References
1. D. Zhou and R. Joynt, “Disappearance of entanglement: a topological point of view,” arXiv:1006.5474; *Quantum Information Processing* **11**, 571–583 (2012), DOI 10.1007/s11128-011-0272-8.
2. H. Zhu, M. Hayashi, and L. Chen, “Axiomatic and operational connections between \(l_1\)-norm of coherence and negativity,” arXiv:1704.02896; *Physical Review A* **97**, 022342 (2018).
3. J. Maziero, “Fortran code for generating random probability vectors, unitaries, and quantum states,” arXiv:1512.05173; *Frontiers in ICT* **3**, 4 (2016).
4. L. Zhang, U. Singh, and A. K. Pati, “Average subentropy, coherence and entanglement of random mixed quantum states,” arXiv:1510.08859.
