# Symmetry-protected photonic Mpemba acceleration for every dephasing strength on a three-site chain

## Finding

For the single-particle, continuous-time dephasing quantum walk on a three-site open path, the pure center-localized state is initially farther from equilibrium than every nontrivial sufficiently mixed reflection-odd diagonal perturbation, yet relaxes strictly faster in relative entropy at late times **for every finite positive dephasing-to-hopping ratio**. This claim is exact, not an asymptotic strong-dephasing approximation.

Write \(q=\gamma/J>0\). Define \(r(q)\) as the unique real zero of
\[
 p_q(z)=z^3+2qz^2+(q^2+8)z+6q.
\]
The exact dimensionless leading decay exponents in the even and odd reflection sectors are
\[
 \alpha_{\mathrm e}(q)=
 \begin{cases}-q-r(q)/2,&0<q\leq3,\\r(q),&q\geq3,\end{cases}
 \qquad
 \alpha_{\mathrm o}(q)=
 \begin{cases}-q/2,&0<q\leq2\sqrt2,\\(-q+\sqrt{q^2-8})/2,&q>2\sqrt2.\end{cases}
\]
For all \(q>0\), \(\alpha_{\mathrm e}(q)<\alpha_{\mathrm o}(q)<0\). The leading even sector changes from an oscillatory conjugate pair to a real eigenvalue at \(q=3\), while the odd quadratic sector has an exceptional point at \(q=2\sqrt2\). Neither event closes the full Liouvillian relaxation gap. As \(q\downarrow0\) and \(q\to\infty\), respectively, the acceleration exponent ratio \(\alpha_{\mathrm e}/\alpha_{\mathrm o}\) tends to \(5/4\) and \(3\).

For any \(0<|\varepsilon|<1/3\), the initial states
\[
 \rho_{\mathrm{far}}(0)=|2\rangle\langle2|,\qquad
 \rho_{\mathrm{near}}(0)=I_3/3+\varepsilon(|1\rangle\langle1|-|3\rangle\langle3|)
\]
satisfy \(F_{\mathrm{far}}(0)=\log3>F_{\mathrm{near}}(0)>0\), whereas there exists a finite \(T\), depending on \(J,\gamma,\varepsilon\), such that \(F_{\mathrm{far}}(t)<F_{\mathrm{near}}(t)\) for all \(t>T\). Here \(F_\rho(t)=\operatorname{Tr}(\rho(t)\log\rho(t))+\log3\), and
\[
 \lim_{t\to\infty}t^{-1}\log F_{\mathrm{far}}(t)=2J\alpha_{\mathrm e}(q),\qquad
 \lim_{t\to\infty}t^{-1}\log F_{\mathrm{near}}(t)=2J\alpha_{\mathrm o}(q).
\]

## Assumptions and scope

The Hilbert space is \(\mathbb C^3\), with orthonormal site vectors \(|1\rangle,|2\rangle,|3\rangle\). Fix any \(J>0\) and \(\gamma>0\). Set \(E_{jk}=|j\rangle\langle k|\),
\[
 H=J(E_{12}+E_{21}+E_{23}+E_{32}),\quad
 \dot\rho=-i[H,\rho]-\gamma\bigl(\rho-\operatorname{diag}\rho\bigr).
\]
All matrix entries and logs are in the site basis; the logarithm is natural with \(0\log0=0\). The dynamics preserves positive trace-one states and has unique stationary state \(I_3/3\). The theorem refers to a single particle, an open three-vertex path, uniform nearest-neighbor hopping, local Markovian pure dephasing, and the two explicit initial-state families above. No zero-dephasing statement is made.

## Proof

**1. Exact parity decomposition.** Scale time by \(\tau=Jt\). Denote the dimensionless generator by \(\mathcal L_q(X)=-i[H/J,X]-q(X-\operatorname{diag}X)\). Define Hermitian matrices
\[
 \begin{aligned}
 P&=E_{11}-2E_{22}+E_{33},\\
 A&=i(E_{12}-E_{21}-E_{23}+E_{32}),\\
 C&=E_{13}+E_{31},\\
 U&=E_{11}-E_{33},\\
 V&=i(E_{12}-E_{21}+E_{23}-E_{32}),\\
 Z&=E_{12}+E_{21}-E_{23}-E_{32},\\
 W&=i(E_{13}-E_{31}).
 \end{aligned}
\]
In the basis \((I_3,H/J;P,A,C;U,V;Z,W)\), the nine-dimensional generator is the direct sum of the scalar blocks \(0\), \(-q\), and
\[
 M_{\mathrm e}=\begin{pmatrix}0&-2&0\\3&-q&1\\0&-2&-q\end{pmatrix},\quad
 M_{\mathrm o}=\begin{pmatrix}0&-2\\1&-q\end{pmatrix},\quad
 M'_{\mathrm o}=\begin{pmatrix}-q&-1\\2&-q\end{pmatrix}.
\]
Reflection \(|1\rangle\leftrightarrow|3\rangle\) leaves the first three blocks even and the final two odd. The full characteristic polynomial is
\[
 z(z+q)p_q(z)(z^2+qz+2)((z+q)^2+2).
\]
Since all nonzero eigenvalues are strictly stable (proved below), the sole zero eigenvector \(I_3\) gives the unique stationary state.

**2. Sector leaders.** Direct calculation gives
\[
 \operatorname{disc}_z p_q=-4(2q^4-61q^2+512)<0.
\]
Indeed the quadratic \(2u^2-61u+512\) has negative discriminant \(-375\) and positive leading coefficient. Therefore \(p_q\) has one negative real root \(r(q)\) and a nonreal conjugate pair with real part \(-q-r(q)/2\). The comparison follows from
\[
 p_q(-2q/3)=-\frac{2q(q-3)(q+3)}{27}.
\]
The odd quadratic has leading real part \(\alpha_{\mathrm o}\) stated above, and the other odd block has real part \(-q\). The extra even scalar also has eigenvalue \(-q\).

**3. Strict spectral separation for every \(q>0\).** Put \(a=\alpha_{\mathrm o}(q)\) and shift the cubic: \(p_q(w+a)=w^3+Aw^2+Bw+C\). By the cubic Routh–Hurwitz criterion, every root has negative real part if \(A,B,C>0\) and \(AB>C\). For \(0<q\leq2\sqrt2\), \(a=-q/2\) and
\[
 A=q/2,\quad B=(32-q^2)/4,\quad C=q(16-q^2)/8,\quad AB-C=2q>0.
\]
For \(q\geq2\sqrt2\), put \(b=-a=(q-\sqrt{q^2-8})/2\), so \(0<b\leq\sqrt2\) and \(q=b+2/b\). Then
\[
 A=(4-b^2)/b,\quad B=4(b^2+1)/b^2,\quad C=2(4-b^2)/b,\quad
 AB-C=2(4-b^2)(b^2+2)/b^3>0.
\]
Thus all three cubic roots have real part strictly less than \(a\). The remaining even eigenvalue \(-q<a\), and both remaining odd eigenvalues \(-q\pm i\sqrt2\) are also faster. In particular \(\alpha_{\mathrm e}<\alpha_{\mathrm o}<0\).

**4. Excitation of leading modes.** The center deviation is \(-P/3\) and the near deviation is \(\varepsilon U\). The pairs of block identities
\[
 \mathcal L_qP=3A,\quad \mathcal L_q^2P=-6P-3qA-6C;
 \qquad \mathcal L_qU=V,\quad\mathcal L_q^2U=-2U-qV
\]
show that \(P\) is cyclic in the full cubic sector and \(U\) is cyclic in the full odd quadratic sector. Consequently neither initial deviation loses any leading sector mode, even when the odd quadratic becomes defective at \(q=2\sqrt2\). The log-rate of the Hilbert–Schmidt norm of each deviation is its respective spectral abscissa times \(J\). This remains true at repeated real parts because the leading finite-dimensional spectral subspace has uniformly bounded invertible oscillatory evolution after removal of the common exponential, up to polynomial Jordan factors.

**5. Entropy comparison and asymptotics.** If \(\rho=I_3/3+X\) with Hermitian trace-zero \(X\to0\), eigenvalue-wise Taylor expansion yields
\[
 F_\rho=\frac32\operatorname{Tr}(X^2)+O(\|X\|^3).
\]
Combining with step 4 yields both exact logarithmic entropy slopes and hence their strict eventual ordering. At time zero the center state is pure, so \(F=\log3\); the other state is a distinct strictly positive density matrix with smaller entropy deficit. Taylor expansion of \(p_q\) as \(q\downarrow0\) gives \(r(q)=-3q/4+O(q^3)\), whence \(\alpha_{\mathrm e}=-5q/8+O(q^3)\) and \(\alpha_{\mathrm o}=-q/2\). As \(q\to\infty\), \(r(q)=-6/q+O(q^{-3})\) and \(\alpha_{\mathrm o}=-2/q+O(q^{-3})\). The asserted ratios follow.

## Verification

Run the standalone `check.py` with Python 3 and SymPy, NumPy, and SciPy: `python check.py`. It constructs all nine Hermitian basis matrices, independently builds the complete Liouvillian, checks every block and characteristic polynomial symbolically, verifies the shifted-cubic Hurwitz coefficient identities, compares the exact and directly computed spectra over a logarithmic parameter grid, and tests density-matrix positivity and reflection symmetry for explicit initial states. It reports 387 passed symbolic and numerical checks. The proof above, not finite sampling, establishes the all-parameter inequalities.

For example, at \(q=1\), the even and odd leading exponents are approximately \(-0.62804937\) and \(-0.5\), respectively; at \(q=3\), they are exactly \(-2\) and \(-1\). Near the odd exceptional point the physical-state asymptotics may carry polynomial factors, which do not affect the logarithmic limits.

## Relationship to prior work

Longhi (2024) introduces this precise continuous-time dephasing quantum-walk generator, the entropy-distance criterion, examples of accelerated relaxation, and a strong-dephasing classical argument that center localization avoids the slow spatial mode for odd chains. That work does not provide the exact three-site parity-block factorization or an all-positive-dephasing proof of the strict two-sector rate gap. The new claim concerns those quantitative results and the resulting explicit state-pair theorem, not the photonic Mpemba effect or the underlying model in general.

Longhi (2025) develops dynamical spectral transitions in discrete-time dephasing maps on gauge-flux networks and walks with internal degrees of freedom. Huang and collaborators (2026) experimentally study a *discrete-time triangular three-node Floquet map*, with an additional closing link and gauge flux. Neither setup is the continuous-time nearest-neighbor three-site Lindblad path treated here. A general symmetry-filtered fast-relaxation mechanism is also known in other many-body systems, so the new mathematical point is the exact rate comparison for this concrete generator across the complete open parameter range.

## Limitations

This is a theorem for the specified three-site continuous-time path, two initial-state families, and \(J,\gamma>0\). It does not establish a uniform crossing time in \(q\), a claim at \(\gamma=0\), an extension to unequal hopping, photonic interactions or longer chains, or a global dynamical phase transition at either spectral rearrangement. The source's supplementary material was not independently available for line-by-line inspection; this leaves a residual priority risk, although its described calculation concerns the strong-dephasing limit. Mathematical priority beyond the directly compared literature is not independently certified.

## References

1. Stefano Longhi, *Photonic Mpemba effect*, Optics Letters **49** (2024), 5188–5191; earliest public preprint 2024-08-06, https://arxiv.org/abs/2408.03296v1 ; DOI: https://doi.org/10.1364/OL.532503.
2. Stefano Longhi, *Dynamical Phase Transitions in Open Quantum Walks*, Advanced Quantum Technologies **8** (2025), e00539, https://arxiv.org/abs/2508.11947v1 ; DOI: https://doi.org/10.1002/qute.202500539.
3. Xiaojian Huang, Lei Xiao, Bingzi Huo, Xiaowei Wang, Stefano Longhi, Peng Xue, *Experimental Observation of Dynamical Phase Transitions in a Dephased Photonic Quantum Walk*, Physical Review Letters **137** (2026), 110804; https://arxiv.org/abs/2606.15935 ; DOI: https://doi.org/10.1103/nqmq-8zsl.
4. Zijun Wei, Mingdi Xu, Yefeng Song, Yangqian Yan, Lei Pan, *Symmetry-Protected Fast Relaxation and the Strong Quantum Mpemba Effect*, preprint (2026), https://arxiv.org/abs/2605.20930.
