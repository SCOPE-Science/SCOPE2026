# Sharp transient norm and a modulo-four resonance in a non-Hermitian Aharonov–Bohm diamond cage

## Finding
For the clean non-Hermitian diamond chain of Liu, Lu, Xia and Xu [1] at flux \(\theta=\pi\), all three energy bands are known to be real and flat. Nevertheless the evolution can amplify the Euclidean norm of a coherent excitation before returning periodically. Its **global worst-case transient amplitude gain**, maximized over all initial unit vectors and all real times, is exactly
\[
G_N(h)=\sup_{t\in\mathbb R}\|e^{-itH_N}\|_{2\to2}
=Q_N+\sqrt{Q_N^2-1},\quad
Q_N=\sqrt{\cosh^4h-\sinh^2h\,c_N},
\]
where
\[
c_N=\min_{0\le m<N}\cos^2\!\left(\frac{2\pi m}{N}\right)
=\begin{cases}
0,&N\equiv0\pmod4,\\
\sin^2(\pi/(2N)),&N\text{ odd},\\
\sin^2(\pi/N),&N\equiv2\pmod4.
\end{cases}
\]
For \(h\ne0\), all optimal times are \(t=(2j+1)\pi/(2J)\), with \(j\in\mathbb Z\); an optimal unit input is a right singular vector of an optimal Bloch block. For \(h=0\), the evolution is unitary and \(G_N(0)=1\) at every time.

The **exact finite-ring resonance** is that \(4\mid N\) if and only if the finite ring attains the continuous-momentum bound for \(h\ne0\):
\[
G_N(h)=G_\infty(h):=\cosh^2h+\sqrt{\cosh^4h-1}.
\]
Otherwise the finite-ring value is strictly smaller. At fixed \(h\ne0\) the finite-size deficit is of order \(N^{-2}\) along each nonresonant residue class, and for each fixed \(N\ge2\), \(G_N(h)\sim e^{2|h|}/2\) as \(|h|\to\infty\). The maximal coherent power ratio is \(G_N(h)^2\).

## Assumptions and scope
Let \(N\ge2\) be an integer, \(J>0\), and \(h\in\mathbb R\). Use periodic boundary conditions on \(N\) three-site unit cells with the clean one-particle Hamiltonian of [1], Eq. (1), and set every on-site potential to zero and the Peierls flux to \(\theta=\pi\). In site order \((a_n,b_n,c_n)\), its equation is
\[
H_N\psi_n=-J\big(V\psi_n+T_1\psi_{n-1}+T_2\psi_{n+1}\big),
\]
with indices modulo \(N\) and
\[
V=\begin{pmatrix}0&0&e^{-h}\\0&0&-1\\e^h&-1&0\end{pmatrix},\quad
T_1=\begin{pmatrix}0&0&0\\0&0&0\\1&e^{-h}&0\end{pmatrix},\quad
T_2=\begin{pmatrix}0&0&1\\0&0&e^h\\0&0&0\end{pmatrix}.
\]
The norm is the induced operator norm on the standard Euclidean Hilbert space \(\mathbb C^{3N}\) with no nonunitary change of metric. Here \(e^{-itH_N}\) is an amplitude propagator; as \(H_N\) need not be Hermitian it is not a quantum channel and need not preserve total norm.

## Proof
**1. Exact three-mode Bloch reduction.** The unitary discrete Fourier transform gives a direct sum \(H_N\cong\bigoplus_{m=0}^{N-1}B(k_m)\), \(k_m=2\pi m/N\), where
\[
B(k)=-J\begin{pmatrix}
0&0&e^{-h}+e^{ik}\\
0&0&-1+e^{h+ik}\\
e^h+e^{-ik}&-1+e^{-h-ik}&0
\end{pmatrix}.
\]
Write the upper-right column and bottom-left row as \(r\) and \(\ell\). Direct multiplication gives \(\ell r=4J^2\) for every real \(k,h\), so \(B^3=4J^2B\), \(\operatorname{tr}B=0\), \(\operatorname{tr}B^2=8J^2\), and the three eigenvalues are exactly \(0,2J,-2J\). Consequently the propagator is the exact degree-two polynomial
\[
E(k,t)=e^{-itB(k)}=I-\frac{i\sin(2Jt)}{2J}B(k)+\frac{\cos(2Jt)-1}{4J^2}B(k)^2.
\]

**2. Singular-value reciprocity.** The unitary chiral involution \(\Gamma=\operatorname{diag}(1,1,-1)\) obeys \(\Gamma B\Gamma=-B\), whence \(\Gamma E\Gamma=E^{-1}\). Unitary left-right multiplication does not change singular values, so the three singular values of the invertible \(E\) are invariant under reciprocation. As there are three, they must be \(g,1,g^{-1}\), \(g\ge1\). Therefore \(\operatorname{tr}(E^\dagger E)=g^2+1+g^{-2}\), and
\[
g=Q+\sqrt{Q^2-1},\qquad Q=\sqrt{\frac{\operatorname{tr}(E^\dagger E)+1}{4}}.
\]
This uses the original physical Euclidean norm, not the nonunitary similarity transform used for spectral decoupling in [1].

**3. Exact Frobenius identity.** Elementary multiplication yields
\[
\|B\|_F^2=8J^2\cosh^2h,\qquad
\|B^2\|_F^2=16J^4\big(\cosh^4h-\sinh^2h\cos^2k+1\big).
\]
The interference term between \(B\) and \(B^2\) has zero trace by chiral parity; linear terms in \(B\) have zero trace. Writing \(u=\sinh^2h\), \(v=\cos^2k\), \(s=\sin^2(Jt)\), expansion of the polynomial propagator gives the **exact identity**
\[
F(k,t):=\operatorname{tr}(E(k,t)^\dagger E(k,t))
=3+8us+4u(u-v)s^2.
\]
For \(h\ne0\) one has \(u>0\), and on \(0\le s,v\le1\),
\[
\frac{\partial F}{\partial s}=8u\bigl(1+(u-v)s\bigr)>0,\qquad
\frac{\partial F}{\partial v}=-4us^2\le0.
\]
Strict positivity follows because \(1+(u-v)s\ge\min\{1,u\}>0\). Thus the unique maximizing time variable is \(s=1\), i.e. \(t=(2j+1)\pi/(2J)\), and the maximizing momenta minimize \(v=\cos^2 k_m\). At these values, \(F=3+8u+4u(u-c_N)\), and the formula for \(G_N\) follows from Step 2. For \(h=0\), \(B=B^\dagger\) and the norm is identically one.

**4. Arithmetic optimization and boundaries.** The nearest discrete momenta \(2\pi m/N\) to \(\pi/2\) modulo \(\pi\) yield the displayed three cases for \(c_N\). Since \(Q_N^2=\cosh^4h-\sinh^2h\,c_N\), strict monotonicity of \(g(Q)\) gives strict finite-size loss whenever \(h\ne0\) and \(4\nmid N\). The small-angle expansion of \(c_N\) gives the \(N^{-2}\) nonresonant deficit; \(\cosh^2h\sim e^{2|h|}/4\) gives \(G_N(h)\sim e^{2|h|}/2\). All limits are derived from the exact closed formula.

## Verification
The standalone `verify_gain.py` uses Python's standard library. It checks the cubic Bloch identity, both Frobenius identities, exact propagator trace, global optimization inequalities, finite-ring residue cases, direct power-method singular norms, and Hermitian-limit unitarity. Run `python3 verify_gain.py`; the current file passed **35,620 finite checks**. These finite checks are not substituted for the proof over all integers, parameters and times.

## Relationship to prior work
Liu et al. [1] introduce this exact nonreciprocal magnetic diamond Hamiltonian, establish the three real flat bands \(0,\pm2J\) at flux \(\pi\), and construct compact localized states and a nonunitary local decoupling. Those spectral and localization statements are not claimed new here. The new observable is the **sharp physical-site Euclidean transient propagator norm**, including global time and input optimization and the finite-size modulo-four effect.

Zhang, Xu and Jin [2] study intensity dynamics in an anti-PT non-Hermitian Creutz-ladder cage with a different two-band Bloch Hamiltonian, while Leykam, Flach and Chong [3] discuss amplification and exceptional-point effects in different non-Hermitian flat-band lattices. Martínez-Strasser et al. [4] examine topological and skin features in distinct diamond-chain coupling configurations; Li, Liu and Liu [5] study disorder-induced localization transitions. Their statements do not imply the displayed model-specific sharp formula without an additional calculation. More general operator-theoretic results might furnish alternative derivations; no claim is made that the elementary matrix methods are new.

## Limitations
The formula assumes *zero* on-site potentials, exact \(\theta=\pi\) flux, spatially uniform real \(h\), periodic boundary conditions, and the standard Euclidean norm. It does not describe open chains, disorder, nonzero detuning, arbitrary flux, nonlinearities, environmental noise, or time-dependent parameters. A finite-dimensional unnormalized non-Hermitian propagator is not a physical trace-preserving quantum process. The original source's spectral decomposition and standard singular-value algebra are established background; publication priority versus unindexed or implicit prior transient-norm analyses remains subject to external verification. No independent scientific audit is asserted.

## References
[1] H. Liu, Z. Lu, X. Xia, Z. Xu, *Fate of localization features in a one-dimensional non-Hermitian flat-band lattice with quasiperiodic modulations*, arXiv:2311.03166, first posted 2023-11-06, https://arxiv.org/abs/2311.03166.

[2] S. M. Zhang, H. S. Xu, L. Jin, *Tunable Aharonov–Bohm cages through anti-PT-symmetric imaginary couplings*, arXiv:2308.11968, https://arxiv.org/abs/2308.11968.

[3] D. Leykam, S. Flach, Y. D. Chong, *Flat bands in lattices with non-Hermitian coupling*, arXiv:1704.00896, https://arxiv.org/abs/1704.00896.

[4] C. Martínez-Strasser et al., *Topological properties of a non-Hermitian quasi-1D chain with a flat band*, arXiv:2307.08754, https://arxiv.org/abs/2307.08754.

[5] X. Li, J. Liu, T. Liu, *Localization-Delocalization Transitions in Non-Hermitian Aharonov–Bohm Cages*, arXiv:2403.07459, https://arxiv.org/abs/2403.07459.
