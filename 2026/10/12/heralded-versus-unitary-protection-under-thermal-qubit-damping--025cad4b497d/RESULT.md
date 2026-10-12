# Heralded versus unitary protection under thermal qubit damping

## Finding

Let \(\Phi_{p,\gamma}\) be a generalized amplitude-damping qubit channel with survival parameter \(0<p<1\) and bath parameter \(0<\gamma<1\), specified below. Consider two consecutive applications of the *same* channel, and allow one operation between them. There is a sharp criterion for an intervening *diagonal, heralded, single-Kraus* operation to preserve entanglement of a maximally entangled input:

\[
\exists\,k>0,\ K\propto\operatorname{diag}(k,1),\ K^\dagger K\le I:\quad
J(\Phi_{p,\gamma}\circ\mathcal K\circ\Phi_{p,\gamma})^{T_{\mathrm{ref}}}\not\ge 0
\quad\Longleftrightarrow\quad
p^2>4ABCD,
\]

where \(K\) is the nonzero contraction proportional to the displayed diagonal matrix, \(\mathcal K(X)=KXK^\dagger\), and
\[
A=\gamma+(1-\gamma)p,\quad B=(1-\gamma)(1-p),\quad
C=\gamma(1-p),\quad D=1-\gamma+\gamma p.
\]
The optimal diagonal ratio is \(k^2=D/A\). This is an exact criterion **within diagonal heralded filters**, not an optimization over arbitrary intermediate quantum operations.

More strikingly, the rational choice
\[
p=\frac7{20},\qquad \gamma=\frac45
\]
has the following simultaneous properties:

**(i)** \(\Phi_{p,\gamma}\circ\mathcal U\circ\Phi_{p,\gamma}\) is entanglement breaking for **every** unitary qubit operation \(\mathcal U(X)=UXU^\dagger\).

**(ii)** The physically admissible selective operation with \(K=\operatorname{diag}(3/4,1)\) gives an entangled, unnormalized output on a maximally entangled two-qubit input. Its positive-trace branch probability for that input is exactly \(2227/3200\).

Thus a single heralded outcome preserves entanglement through two finite-temperature damping steps even though no intermediate unitary can do so. Strict inequalities yield the same separation on a nonempty open neighborhood of these channel parameters and filter coefficients.

## Assumptions and scope

The channel is defined by the four Kraus operators
\[
\begin{aligned}
E_0&=\sqrt\gamma\,\operatorname{diag}(1,\sqrt p),&
E_1&=\sqrt{\gamma(1-p)}\,|0\rangle\langle1|,\\
E_2&=\sqrt{1-\gamma}\,\operatorname{diag}(\sqrt p,1),&
E_3&=\sqrt{(1-\gamma)(1-p)}\,|1\rangle\langle0|.
\end{aligned}
\]
These satisfy \(\sum_j E_j^\dagger E_j=I_2\). A single intermediate selective outcome is modeled by a trace-nonincreasing completely positive map \(\mathcal K(X)=KXK^\dagger\). Its normalized output is conditioned on observing that outcome; failures are discarded. No deterministic channel is being attributed to this selected outcome. Entanglement survival means the unnormalized Choi operator, obtained using \(|\Omega\rangle=(|00\rangle+|11\rangle)/\sqrt2\), is nonseparable, equivalently has nonpositive partial transpose in the two-qubit setting.

## Proof

**Diagonal-filter criterion.** Direct composition gives, in reference–output order \((00,01,10,11)\),
\[
J(\Phi\circ\mathcal K\circ\Phi)
=\frac12\begin{pmatrix}
k^2A^2+BC&0&0&kp\\
0&B(k^2A+D)&0&0\\
0&0&C(k^2A+D)&0\\
kp&0&0&k^2BC+D^2
\end{pmatrix}.
\]
Partial transposition moves the off-diagonal term to the central block. Both outer eigenvalues are positive; the central block has negative determinant exactly when
\[
k^2p^2>BC(k^2A+D)^2.
\]
For \(x=k^2>0\), minimizing \((Ax+D)^2/x\) gives \(x=D/A\) by the arithmetic–geometric mean inequality. The optimal value is \(4AD\), proving the claimed if-and-only-if. The matrix formula uses the representative \(\operatorname{diag}(k,1)\); multiplying by any positive scalar \(c\le1/\max\{1,k\}\) makes the Kraus operator a contraction and scales the Choi matrix by \(c^2\), without changing a partial-transpose eigenvalue sign. Without a filter, the same argument shows that \(\Phi^2\) is entanglement breaking if and only if \(p^2\le BC(A+D)^2=\gamma(1-\gamma)(1-p^2)^2\).

**Exact heralded witness.** For \(p=7/20\), \(\gamma=4/5\), and \(k=3/4\), the constants are \(A=87/100\), \(B=13/100\), \(C=13/25\), \(D=12/25\). The unnormalized Choi operator is
\[
J=\begin{pmatrix}
78937/320000&0&0&21/160\\
0&20163/320000&0&0\\
0&0&20163/80000&0\\
21/160&0&0&10737/80000
\end{pmatrix}.
\]
Its trace is \(2227/3200\). The central principal minor of its partial transpose is
\[
\frac{20163}{320000}\cdot\frac{20163}{80000}
-\left(\frac{21}{160}\right)^2
=-\frac{34453431}{25600000000}<0,
\]
so the successful branch is entangled. In contrast, the corresponding central partial-transpose minor for the **unfiltered** two-step channel is \(701/4000000>0\), and all other partial-transpose eigenvalues are nonnegative.

**Every unitary fails at the witness.** In Bloch coordinates the channel has linear part \(L=\operatorname{diag}(\sqrt p,\sqrt p,p)\) and translation \((0,0,t)\), with \(t=(1-p)(2\gamma-1)=39/100\). Axial covariance and Euler decomposition reduce any intermediate unitary, up to external unitary conjugations that leave entanglement-breaking status unchanged, to a rotation about the \(y\)-axis through some \(\theta\). Put \(u=\cos\theta\in[-1,1]\) and \(v=\sin\theta\). The Choi partial transpose \(H(u,v)\), expressed in output–reference tensor order, is Hermitian and obeys
\[
\begin{aligned}
4H={}&I\otimes I+t\sqrt p\,v\,X\otimes I
+t(1+pu)Z\otimes I+pu\,X\otimes X\\
&+p\sqrt p\,v(X\otimes Z-Z\otimes X)
+pY\otimes Y+p^2u\,Z\otimes Z.
\end{aligned}
\]
Here \(X,Y,Z\) denote the standard Pauli matrices. Expanding principal minors and using \(v^2=1-u^2\), the elementary symmetric functions of the four real eigenvalues of \(H\) are
\[
\begin{aligned}
e_1&=1,\\
e_2&=\frac{13(397910-16380u-2639u^2)}{16000000},\\
e_3&=\frac{1112805-212940u-34307u^2}{32000000},\\
e_4&=\frac{P(u)}{256000000000000},
\end{aligned}
\]
with
\[
P(u)=7457876881u^4-18389285460u^3-16339726130u^2
-109220120100u+139247037225.
\]
Both \(e_2\) and \(e_3\) are strictly decreasing on \([-1,1]\) and remain positive at \(u=1\). To certify positivity of \(e_4\) without numerical optimization, set \(u=2y-1\). The polynomial \(P(2y-1)\) has Bernstein coefficients of degree four
\[
\left(257974593536,\ 177204577664,\
\frac{456454468448}{3},\ 86373743024,\ 2755782416\right),
\]
all positive, so \(P(u)>0\) for \(-1\le u\le1\). Thus every elementary symmetric function is positive. Indeed, if a Hermitian matrix had a nonpositive eigenvalue, \(\det(zI+H)=z^4+e_1z^3+e_2z^2+e_3z+e_4\) would vanish for some \(z\ge0\), impossible because all coefficients are positive. Hence \(H(u,v)\) is positive definite for **every** angle. By the Peres–Horodecki PPT criterion in \(2\times2\), every unitary-filtered composition is entanglement breaking.

The positive all-unitary margin is uniform by compactness of \(U(2)\), while the heralded partial-transpose determinant is strictly negative. Continuity therefore extends the separation to an open neighborhood of the rational witness.

## Verification

Run `python3 verify.py` using Python's standard library. It recomputes the rational two-step Choi entries and negative partial-transpose minor, reconstructs the all-unitary Choi partial-transpose principal-minor sums as exact polynomials in the quotient ring \(w^2=p(1-u^2)\), and verifies the positive Bernstein expansion exactly. The expected terminal marker is `VERIFY_OK rational_choi=passed unitary_all_angles=passed bernstein=passed`. The proof does not infer all-angle positivity from finite angle sampling; the exact polynomial identities cover the full continuum of unitaries.

## Relationship to prior work

Lami and Giovannetti, *Entanglement-Breaking Indices* (arXiv:1411.2517, first posted 10 November 2014), provide the generalized-amplitude-damping channel and its **unfiltered** iteration index (Example 1), and formulate a conjecture about **trace-preserving qubit filters** (Conjecture 1). The selective, trace-decreasing filter proved here is **outside the conjecture's stated class**, so this result is not a counterexample to that conjecture. Their qubit results do not give the single-outcome phase criterion or the rational all-unitary versus heralded separation above.

Filippov, Rybár and Ziman, *Local two-qubit entanglement-annihilating channels* (arXiv:1110.3757, Section V.B), analyze tensor products of local damping channels and their action on bipartite input states. That is a distinct map-composition question from placing a selective Kraus outcome **between serial channel uses**. Goswami, Ghosh and Majumdar (arXiv:1903.03550) and Wang et al. (DOI:10.3390/e27040350) analyze weak-measurement protection in generalized amplitude damping, typically with filtering before and/or after a noise interval, not this all-intermediate-unitary non-amendability certificate. None of the inspected material states the exact present theorem. A more abstract equivalence within the large quantum-filtering literature remains possible.

## Limitations

The optimized criterion holds only for diagonal single-Kraus interventions. The no-unitary statement is proved only at the specified rational channel parameters and nearby channels, not for every generalized-amplitude-damping channel. No claim is made about the efficacy of arbitrary deterministic nonunitary (trace-preserving) intermediate operations, optimal success probabilities, repeated selections, or general quantum-capacity restoration. Discarding failed outcomes is essential; treating the successful branch as a deterministic operation would be incorrect. Literature completeness cannot be guaranteed.

## References

1. L. Lami and V. Giovannetti, *Entanglement-Breaking Indices*, arXiv:1411.2517, https://arxiv.org/abs/1411.2517; *Journal of Mathematical Physics* **56**, 092201 (2015).
2. S. N. Filippov, T. Rybár and M. Ziman, *Local two-qubit entanglement-annihilating channels*, arXiv:1110.3757, https://arxiv.org/abs/1110.3757; *Physical Review A* **85**, 012303 (2012).
3. S. Goswami, S. Ghosh and A. S. Majumdar, *Protecting quantum correlations in presence of generalised amplitude damping channel: the two-qubit case*, arXiv:1903.03550, https://arxiv.org/abs/1903.03550.
4. M. Wang et al., *Protecting the Entanglement of X-Type Systems via Weak Measurement and Reversal in the Generalized Amplitude Damping Channel*, *Entropy* **27**, 350 (2025), https://doi.org/10.3390/e27040350.
