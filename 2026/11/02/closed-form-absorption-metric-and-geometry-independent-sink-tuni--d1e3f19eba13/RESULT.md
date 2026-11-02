# Closed-form absorption metric and geometry-independent sink tuning on a finite quantum path

## Finding

For every integer \(N\geq2\), coherent hopping frequency \(\Omega>0\), sink strength \(\kappa>0\), and normalized initial state on a length-\(N\) path, the mean time to absorption at its first site is an explicit quadratic form. In the site basis, the complete Hermitian mean-time kernel \(X\), for \(1\leq j\leq k\leq N\), is

\[
 X_{jk}=(N+1-k)
 \begin{cases}
 \dfrac{j}{\kappa}+\dfrac{\kappa(j-1)}{\Omega^2},& k-j\text{ even},\\[3pt]
 -\dfrac{i}{\Omega},& k-j\text{ odd},
 \end{cases}
 \qquad X_{kj}=\overline{X_{jk}}.
\]

In particular, for a walker initially localized at site \(j\),

\[
 \mathbb E_j[\tau]=(N+1-j)\left(\frac{j}{\kappa}+\frac{\kappa(j-1)}{\Omega^2}\right).
\]

For every \(2\leq j\leq N\), the **unique global optimum** over positive sink strengths is

\[
 \boxed{\kappa_{\mathrm{opt}}(j)=\Omega\sqrt{\frac{j}{j-1}}},
 \qquad
 \boxed{\inf_{\kappa>0}\mathbb E_j[\tau]=\frac{2(N+1-j)\sqrt{j(j-1)}}{\Omega}}.
\]

The optimal absorption rate depends on the initial distance from the sink but **not** on the total length of the path. At the sink itself, \(j=1\), the law instead is \(\mathbb E_1[\tau]=N/\kappa\), with no finite optimum or large-\(\kappa\) Zeno upturn. For all other sites, both weak and very strong absorption make the mean diverge.

## Assumptions and scope

The one-particle Hilbert space has orthonormal basis \(\{|1\rangle,\ldots,|N\rangle\}\). Its coherent Hamiltonian and sole quantum jump operator are

\[
 H=\Omega I-\frac{\Omega}{2}\sum_{r=1}^{N-1}
 (|r\rangle\langle r+1|+|r+1\rangle\langle r|),
 \qquad L=\sqrt\kappa\,|\emptyset\rangle\langle1|.
\]

The sink state \(|\emptyset\rangle\) is absorbing; there is no dephasing, injection, further sink, or detuning. Units set \(\hbar=1\). The initial state \(\rho_0\) is any positive semidefinite \(N\times N\) matrix of unit trace, confined initially to the surviving sector. Let \(\tau\) denote its first jump into the sink. Define the nearest-neighbor adjacency matrix \(T\) and endpoint projector \(E=|1\rangle\langle1|\). Removing the harmless scalar phase \(\Omega I\), the unnormalized no-jump propagator is \(e^{At}\), with

\[
 A=\frac{i\Omega}{2}T-\frac{\kappa}{2}E,
 \quad S_{\rho_0}(t)=\operatorname{Tr}(e^{At}\rho_0e^{A^\dagger t}),
 \quad \mathbb E_{\rho_0}[\tau]=\int_0^\infty S_{\rho_0}(t)\,dt=\operatorname{Tr}(X\rho_0).
\]

The theorem includes all real positive \(\Omega,\kappa\), all path lengths \(N\ge2\), and all such initial density matrices. It does not assert any explicit higher hitting-time moments or analogous formula for nonuniform hopping, rings, or additional sinks.

## Proof

**1. Strict decay and normalization.** For every eigenpair \(Av=\lambda v\),

\[
 2\operatorname{Re}\lambda\,\|v\|^2
 =v^\dagger(A+A^\dagger)v=-\kappa|v_1|^2.
\]

A purely imaginary eigenvalue would therefore require \(v_1=0\). The first row of the eigenvalue equation forces \(v_2=0\), and the subsequent tridiagonal rows inductively force every component to vanish. Hence every eigenvalue of \(A\) has strictly negative real part. It follows that \(e^{At}\to0\) exponentially; the first-jump density \(-S'_{\rho_0}(t)=\kappa(e^{At}\rho_0e^{A^\dagger t})_{11}\) integrates to one. The positive definite matrix

\[
 X=\int_0^\infty e^{A^\dagger t}e^{At}\,dt
\]

is the **unique** Hermitian solution of

\[
 A^\dagger X+XA=-I,
 \quad\text{equivalently}\quad
 \frac{i\Omega}{2}(XT-TX)-\frac\kappa2(EX+XE)=-I.
 \tag{1}
\]

Existence and uniqueness here follow from strict decay, not from a finite computational experiment.

**2. Verification of the exact kernel for every dimension.** Set \(s_r=N+1-r\) for \(1\le r\le N+1\), so \(s_{N+1}=0\), and \(f_r=r/\kappa+\kappa(r-1)/\Omega^2\). Both sequences are affine and obey

\[
 s_{r-1}+s_{r+1}=2s_r,\qquad
 f_{r-1}+f_{r+1}=2f_r
\]

whenever the indicated indices are valid. Define \(X_{jk}=s_k f_j\) for \(j\le k\) of equal parity, and \(X_{jk}=-is_k/\Omega\) for \(j<k\) of opposite parity, extending by Hermitian conjugation. Direct substitution into \(XT-TX\) yields these complete entrywise identities:

\[
 \begin{aligned}
 [X,T]_{11}&=-\frac{2i(N-1)}{\Omega},\\
 [X,T]_{jj}&=\frac{2i}{\Omega} &&(2\le j\le N),\\
 [X,T]_{jk}&=0 &&(2\le j<k\le N),\\
 [X,T]_{1k}&=-\frac{i\kappa}{\Omega}X_{1k} &&(2\le k\le N).
 \end{aligned}
 \tag{2}
\]

For clarity, the third line follows for a gap of at least two by the two affine second-difference identities; for a gap of one it follows by \(s_j+s_{j+2}=2s_{j+1}\) and \(f_{j-1}+f_{j+1}=2f_j\). At the right endpoint, missing terms vanish because \(s_{N+1}=0\). For the last line, when \(k\) is odd the direct commutator is \(-is_k/\Omega\), and when \(k\) is even it is \(-\kappa s_k/\Omega^2\); these are precisely \(-i\kappa X_{1k}/\Omega\) in the two parity cases, including \(k=2\).

Substituting (2) into (1), the \((1,1)\) entry is \((N-1)-\kappa(N/\kappa)=-1\), each other diagonal is \(-1\), and all off-diagonals vanish. Therefore the asserted matrix solves (1) exactly for every \(N\), and uniqueness identifies it with the integral defining \(X\).

**3. Extraction and global optimization.** Inserting a site state \(|j\rangle\langle j|\) into \(\operatorname{Tr}(X\rho_0)\) gives the diagonal formula. If \(j\ge2\), the dependence on \(\kappa>0\) has the strictly convex form \(a/\kappa+b\kappa\), where \(a=(N+1-j)j>0\) and \(b=(N+1-j)(j-1)/\Omega^2>0\). Its derivative vanishes only at \(\Omega\sqrt{j/(j-1)}\), and it diverges at both endpoints, proving the unique global minimum and value by arithmetic-geometric mean. For \(j=1\), the linear-in-\(\kappa\) coefficient vanishes and the mean decreases strictly as \(N/\kappa\).

## Verification

`verify.py` reconstructs \(X\) and \(A\) independently for multiple finite dimensions and positive rate combinations, checks equation (1) numerically, compares with SciPy's independently solved continuous Lyapunov equation, verifies positive definiteness and optimality, and uses SymPy to verify every entry of (1) as a rational function of two symbolic positive parameters for each \(2\le N\le8\). The recorded run produced `PASS: 1267 deterministic numerical and finite-size symbolic consistency checks` in `verification_output.txt`. The all-\(N\) proof is the direct algebra above; finite computations are not claimed to establish the universal quantifiers.

## Relationship to prior work

Riberi (2026) establishes the same coherent hopping and Lindblad boundary-sink normalization on the **semi-infinite** chain, giving exact propagator and first-passage results there. Its discussion explicitly identifies finite geometry as a separate extension. It does not present the finite-path all-initial-state mean-time kernel or the size-independent optimal sink rate proved here.

Varbanov, Krovi and Brun (2008) develop a general continuous-measurement quantum-walk hitting-time superoperator and analyze small finite graphs, including a three-site path with a **graph-Laplacian**, rather than uniform-onsite adjacency, Hamiltonian. Their broad inverse framework makes finite-path calculations possible in principle; the present result does not claim that the Lyapunov representation itself is new. Instead it supplies a full explicit \(N\)-uniform evaluation and sharp dimension-independent optimization that the inspected examples do not provide. Differences between continuous monitoring and explicit boundary jump dynamics must be accounted for when comparing protocols.

Krapivsky, Luck and Mallick (2013) study quantum survival for a single trap on an infinite line and on finite **rings**, among other geometries. Their finite-ring model retains dark antisymmetric states and has non-unit absorption, unlike this path with a sink at an endpoint. Their inspected spectral and survival results do not state the full endpoint-path mean-time metric or this optimum. General quantum Markov-chain treatments of finite segments with completely positive intersite channels are likewise not the same coherent hopping plus endpoint-loss model.

## Limitations

Only finite, open, uniform paths with a single endpoint Lindblad sink are proved. The mean is for the first quantum jump (equivalently, integrated no-jump survival), not a projectively sampled discrete-time first detection protocol. A general inverse/superoperator identity for hitting time was known; the originality claim is the explicit all-size solution and sink optimization, not the existence of an inverse. The finite-ring literature and older coherent exciton-quenching literature are related but differ in topology and/or dynamical generator; undiscovered implicit coverage remains a priority risk. No independent proof review or publication-priority certification is asserted.

## References

1. F. Riberi, *An Exactly Solvable Absorbing Quantum Walk*, first version May 8, 2026, https://arxiv.org/abs/2605.08056 (the subsequent journal version uses the title *Boundary-localized non-Hermitian mode in an absorbing quantum walk*).
2. M. Varbanov, H. Krovi, and T. A. Brun, *Hitting time for the continuous quantum walk*, Phys. Rev. A **78**, 022324 (2008), https://arxiv.org/abs/0803.3446.
3. P. L. Krapivsky, J. M. Luck, and K. Mallick, *Survival of classical and quantum particles in the presence of traps*, arXiv:1311.6298 (2013), https://arxiv.org/abs/1311.6298.
4. *One-dimensional continuous-time quantum Markov chains: qubit probabilities and measures*, J. Phys. A (2024), https://doi.org/10.1088/1751-8121/ad5bcb (contrasting completely positive intersite dynamics).
