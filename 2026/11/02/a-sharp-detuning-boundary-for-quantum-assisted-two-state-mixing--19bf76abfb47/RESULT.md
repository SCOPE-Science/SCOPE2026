# A sharp detuning boundary for quantum-assisted two-state mixing

## Finding

Consider the two-state quantum stochastic walk with bit-flip noise, with an additional constant diagonal energy detuning. Its computational-basis output is accelerated relative to the classical bit-flip walk **at every time** if and only if at least one of coherent hopping and detuning vanishes. Whenever both are nonzero, the coherent evolution initially improves mixing but eventually becomes arbitrarily slower *relative to the classical distance*, in the following precise sense.

**Theorem.** Let \(\gamma>0\), \(a,b\in\mathbb R\), and let \(\rho_{a,b}(t)\) solve
\[
\dot\rho_{a,b}=-i[a\sigma_x+b\sigma_z,\rho_{a,b}]
 +\gamma(\sigma_x\rho_{a,b}\sigma_x-\rho_{a,b}),
\qquad \rho_{a,b}(0)=|0\rangle\langle0|.
\]
Write \(z_{a,b}(t)=\operatorname{tr}(\sigma_z\rho_{a,b}(t))\). The total-variation distance of its computational-basis measurement distribution from the uniform binary distribution is \(D_{a,b}(t)=|z_{a,b}(t)|/2\). The classical reference distance is \(D_{\mathrm{cl}}(t)=e^{-2\gamma t}/2\). Then:

1. If \(a=0\), \(D_{a,b}(t)=D_{\mathrm{cl}}(t)\) for every \(t\ge0\). If \(b=0\), \(D_{a,0}(t)=D_{\mathrm{cl}}(t)|\cos(2at)|\). Hence \(D_{a,b}(t)\le D_{\mathrm{cl}}(t)\) for every \(t\ge0\) whenever \(ab=0\).
2. If \(ab\ne0\), then \(D_{a,b}(t)<D_{\mathrm{cl}}(t)\) for all sufficiently small \(t>0\), but
\[
\limsup_{t\to\infty}\frac{D_{a,b}(t)}{D_{\mathrm{cl}}(t)}=+\infty.
\]
In particular, the **global-in-time** mixing-improvement inequality holds for all \(t\ge0\) **if and only if** \(ab=0\).
3. Fix \(\gamma>0\) and \(a\ne0\). As \(b\to0\), the distinguished real slow eigenvalue \(\lambda_s(b)\) of the Bloch generator and its population residue \(A_s(b)\) obey
\[
\lambda_s(b)=-\frac{2\gamma}{\gamma^2+a^2}b^2+O(b^4),
\qquad
A_s(b)=\frac{a^2}{(\gamma^2+a^2)^2}b^2+O(b^4).
\]
For every sufficiently small fixed nonzero \(b\), \(A_s(b)>0\), \(\lambda_s(b)\in(-\gamma,0)\), and \(z_{a,b}(t)\sim A_s(b)e^{\lambda_s(b)t}\) as \(t\to\infty\). Thus the late-time observed relaxation exponent is quadratic in an arbitrarily weak detuning, even though its spectral weight is also quadratic.

## Assumptions and scope

Use the standard Pauli matrices \(\sigma_x,\sigma_y,\sigma_z\), with \(\sigma_z|0\rangle=|0\rangle\), and set \(\hbar=1\). The bit-flip channel occurs at Poisson rate \(\gamma\); its jump operation is conjugation by \(\sigma_x\). The coherent Hamiltonian has real, time-independent hopping coefficient \(a\) and detuning coefficient \(b\). No control, reset, measurement feedback, or additional noise channels are included. Both output probabilities correspond to measurement in the fixed \(\sigma_z\) basis. All inequalities and limits in the theorem refer to this output total variation, not the trace distance between full density matrices or to a first-hitting mixing-time convention.

## Proof

Expand \(\rho=(I+x\sigma_x+y\sigma_y+z\sigma_z)/2\). The Pauli commutators and the bit-flip conjugation give
\[
\frac{d}{dt}\begin{pmatrix}x\\y\\z\end{pmatrix}
=M\begin{pmatrix}x\\y\\z\end{pmatrix},\quad
M=\begin{pmatrix}
0&-2b&0\\2b&-2\gamma&-2a\\0&2a&-2\gamma
\end{pmatrix},\qquad (x(0),y(0),z(0))=(0,0,1).
\]
For a binary distribution with difference \(z\) between the two probabilities, the distance to uniform is \(|z|/2\). With \(a=b=0\), the last equation is \(\dot z=-2\gamma z\), giving the reference. If \(a=0\), it remains a closed scalar equation regardless of \(b\). If \(b=0\), the \((y,z)\) subsystem is a damped planar rotation and \(z(t)=e^{-2\gamma t}\cos(2at)\). This proves the stated two axis formulas.

For \(a\ne0\), the initial derivatives satisfy \(z(0)=1\), \(z'(0)=-2\gamma\), and \(z''(0)=4\gamma^2-4a^2\). Consequently
\[
z_{a,b}(t)-e^{-2\gamma t}=-2a^2t^2+O(t^3).
\]
Since \(z_{a,b}(t)>0\) close to zero, coherent hopping strictly improves the output distribution at sufficiently small positive times, independently of detuning.

Now assume \(ab\ne0\), and define \(N=M+2\gamma I\). Its symmetric part obeys
\[
N+N^*=\operatorname{diag}(4\gamma,0,0).
\]
For any nonzero complex eigenvector \(v=(v_1,v_2,v_3)\) with eigenvalue \(\nu\),
\[
\operatorname{Re}\nu=\frac{2\gamma|v_1|^2}{\|v\|_2^2}.
\]
If \(v_1=0\), the first row of the eigenvector equation, using \(b\ne0\), forces \(v_2=0\); then its second row, using \(a\ne0\), forces \(v_3=0\), a contradiction. Therefore **every eigenvalue of \(N\) has strictly positive real part**. Similarly, since \(M+M^*=\operatorname{diag}(0,-4\gamma,-4\gamma)\) and a nonzero eigenvector cannot have only its first component nonzero when \(b\ne0\), every eigenvalue of \(M\) has strictly negative real part. Thus each Bloch eigenvalue has real part strictly between \(-2\gamma\) and zero.

The rescaled output
\[
f(t)=e^{2\gamma t}z_{a,b}(t)=e_3^\top e^{Nt}e_3
\]
is a finite exponential polynomial whose possible exponents are the eigenvalues of \(N\), all with strictly positive real part. It is nonzero because \(f(0)=1\). A nonzero exponential polynomial with all exponents in the open right half-plane is unbounded on \([0,\infty)\): among its nonzero Jordan terms, choose those with maximal exponential real part and maximal polynomial degree; after removing these growth factors, the leading expression is a nonzero finite trigonometric polynomial plus a vanishing remainder. Its long-interval mean square is positive, so its absolute value has positive limsup. Hence \(\limsup_{t\to\infty}|f(t)|=\infty\). Because \(D_{a,b}(t)/D_{\mathrm{cl}}(t)=|f(t)|\), the claimed eventual unbounded relative slowdown and the exact axis-only characterization follow.

To obtain the weak-detuning asymptotics, solve the transformed Bloch equations. For sufficiently large real \(s\), the Laplace transform of \(z_{a,b}\) is
\[
\widehat z(s)=\frac{Q_b(s)}{P_b(s)},\quad
Q_b(s)=s(s+2\gamma)+4b^2,
\quad P_b(s)=s\bigl((s+2\gamma)^2+4a^2\bigr)+4b^2(s+2\gamma).
\]
At \(b=0\), the poles are \(0\) and \(-2\gamma\pm2ia\), all simple when \(a\ne0\). The implicit-function theorem applied to the simple root at zero gives
\[
\lambda_s(b)=-\frac{\partial_{b^2}P_b(0)|_{b=0}}{\partial_sP_0(0)}b^2+O(b^4)
=-\frac{2\gamma}{\gamma^2+a^2}b^2+O(b^4).
\]
The coefficient of this pole is its residue
\[
A_s(b)=\frac{Q_b(\lambda_s(b))}{P'_b(\lambda_s(b))}
=\frac{a^2}{(\gamma^2+a^2)^2}b^2+O(b^4).
\]
The remaining two poles stay near \(-2\gamma\pm2ia\), while \(\lambda_s(b)\to0\). For sufficiently small fixed \(b\ne0\), the corresponding non-slow terms decay exponentially faster. The residue is strictly positive, proving the final assertion.

## Verification

The accompanying `verify.py` is self-contained and uses Python's exact rational arithmetic. It verifies the characteristic-matrix identity for a finite integer parameter grid, verifies the Laplace numerator and denominator by a second determinant calculation, and certifies a strict finite-time slowdown at \(a=b=\gamma=1\), \(t=2\) without relying on floating-point signs. It encloses the two required matrix exponentials by rational Taylor polynomials with explicit norm remainders, obtaining \(z_{1,1}(2)-e^{-4}>0.0782\). The displayed decimal is only an illustrative lower truncation; the assertion uses exact fractions. Finite checks do **not** establish the theorem for arbitrary parameters: the universal proof is the analytic argument above.

To reproduce: run `python3 verify.py` from a directory containing the supplied standalone artifact. No external packages, unavailable data files, or unstated inputs are needed.

## Relationship to prior work

He, Hutsalyuk, Mussardo and Stampiggi (2026) formulate a two-state quantum stochastic walk with bit-flip jumps and a commuting permutation Hamiltonian. Their explicit formula \(D(t)=\frac12e^{-2\gamma t}|\cos(2at)|\) and their all-time acceleration theorem for central class Hamiltonians are prior results, not claimed here. Their discussion notes that commutativity need not survive a general Hamiltonian, but does not supply the present sharp two-parameter all-time classification, asymptotic unbounded ratio or quadratic small-detuning residue. For \(S_2\), all permutation-group-algebra Hamiltonians are combinations of the identity and \(\sigma_x\); the detuning \(b\sigma_z\) is an **additional on-site energy term, outside that group-algebra family**. Thus the present result is a boundary for a physically natural perturbation beyond their central-Hamiltonian hypotheses, not a counterexample to their theorem.

Whitfield, Rodríguez-Rosario and Aspuru-Guzik (2010) supply the general quantum stochastic walk framework. Saurav and Lidar (2025) analyze bit-flip noise with designed time-dependent Hamiltonian controls for preserving quantum properties; their control objective is different from a fixed Hamiltonian's output-mixing comparison. Bressanini, Benedetti and Paris (2022) analyze quantum-walk decoherence and classicalization using a fidelity-based *quantum-versus-classical dynamical distance*, graph Laplacian hopping, and dephasing or separate site-jump channels. They do not establish the present fixed-output-to-uniform comparison for a unitary bit-flip jump and a detuned two-site Hamiltonian. Generic slow-mode and decoherence-free-subspace mechanisms are established in open-system theory; the novelty assessed here is the exact conditional comparison with the classical output distance for all times and the singular weak-detuning amplitude–rate pair.

## Limitations

The theorem concerns only a single qubit initialized in a computational-basis state, a single Poisson bit-flip jump channel, and a constant real Hamiltonian restricted to the \(\sigma_x\)–\(\sigma_z\) plane. It does not claim that noncommuting Hamiltonians always slow mixing at every time: short-time improvement occurs even in the off-axis case. The asymptotic ratio being unbounded does not imply that the absolute distance fails to converge to zero; in fact all nonzero off-axis Bloch eigenvalues have negative real parts. The weak-detuning asymptotic gives a very slow decay with a simultaneously small amplitude; it does not establish a larger fixed-tolerance first-hitting mixing time. Independent mathematical checking and comprehensive priority certification have not been performed.

## References

1. F. He, A. Hutsalyuk, G. Mussardo and A. Stampiggi, *Quantum Stochastic Walks on the Permutation Group*, arXiv:2609.13387, first publicly submitted 2026-09-11, https://arxiv.org/abs/2609.13387 . See Section 5, especially the two-state computation and the central-Hamiltonian limitation.
2. J. D. Whitfield, C. A. Rodríguez-Rosario and A. Aspuru-Guzik, *Quantum stochastic walks: A generalization of classical random walks and quantum walks*, Physical Review A 81, 022323 (2010), https://doi.org/10.1103/PhysRevA.81.022323 ; preprint https://arxiv.org/abs/0905.2942 .
3. K. Saurav and D. A. Lidar, *Quantum Property Preservation*, PRX Quantum 6, 010335 (2025), https://doi.org/10.1103/PRXQuantum.6.010335 ; preprint https://arxiv.org/abs/2408.11262 .
4. G. Bressanini, C. Benedetti and M. G. A. Paris, *Decoherence and classicalization of continuous-time quantum walks on graphs*, Quantum Information Processing 21, 317 (2022), https://doi.org/10.1007/s11128-022-03647-x ; open-access full text https://link.springer.com/article/10.1007/s11128-022-03647-x .
5. B. Avnit and D. Cohen, *Quantum walk in stochastic environment*, Physical Review E 108, 054111 (2023), https://doi.org/10.1103/PhysRevE.108.054111 .
