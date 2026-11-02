# Geometry-independent dark spectra for block-repetition-code absorbers on quantum hypercubes

## Finding
For any integers \(N\ge m\ge2\), partition the \(N\) binary-coordinate positions into \(m\) nonempty blocks of sizes \(b_1,\ldots,b_m\), with \(\sum_i b_i=N\). Place absorbing traps at all \(2^m\) vertices whose coordinates are constant within each block (a product of binary repetition codes). For the uniform-hopping, continuous-time one-particle quantum walk, define \(r_w\) as the dimension of the subspace in adjacency eigenvalue shell \(N-2w\) coupled to those traps. Then **independently of the block sizes**, for \(0\le w\le N\),
\[
\boxed{\sum_{w=0}^{N} r_w z^w=(1+z)^{m-1}\sum_{j=0}^{N-m+1}z^j.}
\]
Consequently, the dimension of the nondecaying (dark) subspace, the dimension of the decaying (bright) subspace, and the eventual capture fraction for a maximally mixed one-particle state are respectively
\[
\boxed{D_{N,m}=2^N-2^{m-1}(N-m+2),\quad B_{N,m}=2^{m-1}(N-m+2),\quad P_{\rm capture}=\frac{N-m+2}{2^{N-m+1}}.}
\]
The loss rates may be unequal, so long as all are strictly positive. These statements concern dimension and eventual capture probability, **not** the relaxation-time distribution. More precisely, the dark dimension in shell \(w\) is \(\binom Nw-r_w\), and the bright and dark subspaces are reducing subspaces of the effective loss Hamiltonian.

As a concrete geometry-independence test, in \(N=8\) dimensions both block patterns \((2,2,2,2)\) and \((1,1,3,3)\) produce \((r_0,\ldots,r_8)=(1,4,7,8,8,8,7,4,1)\), with \(B=48\), \(D=208\), and capture fraction \(3/16\). Their codeword trap sets are not related by hypercube isometries because their minimum nonzero codeword weights are \(2\) and \(1\), respectively.

## Assumptions and scope
Let \(V=\mathbb F_2^N\) and \(A\) be the adjacency matrix of the unweighted binary hypercube \(Q_N\). Define the trap set
\[
T=\{x\in V:\ x\text{ is constant within each of the }m\text{ blocks}\}.
\]
For \(J>0\), any real \(\varepsilon\), and strictly positive reals \(\kappa_x\) for \(x\in T\), consider the effective dissipative Hamiltonian on \(\mathbb C^V\)
\[
H=JA+\varepsilon I-i\Gamma,\qquad \Gamma=\sum_{x\in T}\kappa_x|x\rangle\langle x|.
\]
The nondecaying space is the maximal \(A\)-invariant space inside \(\ker\Gamma\). Evolution is \(e^{-itH}\); the survival probability of a normalized initial vector is its squared norm. For the maximally mixed one-particle initial density \(I/2^N\), the eventual capture probability is one minus its surviving trace. \(r_w\) refers to the rank of restrictions to \(T\) of Walsh characters of Hamming weight \(w\), equivalently the rank of the projection of \(\mathbb C^T\) onto that energy eigenspace. Throughout, the trap set includes **all** codewords of the specified product repetition code.

## Proof
**1. Eigenspace and trap restriction.** The \(2^N\) Walsh characters \(\chi_a(v)=(-1)^{a\cdot v}\), for \(a\in\mathbb F_2^N\), diagonalize \(A\), with eigenvalue \(N-2|a|\). Let \(E_w\) denote their span for \(|a|=w\). The dark subspace in this shell is the nullspace of the evaluation map \(E_w\to\mathbb C^T\); its dimension is \(\binom Nw-r_w\).

**2. Distinct block parities.** Encode any trap vertex by its \(m\)-bit block-value vector \(t\). Restriction of \(\chi_a\) to traps is the \(m\)-bit character \((-1)^{s\cdot t}\), where \(s_i\) is the parity of the number of selected coordinates of \(a\) in block \(i\). Distinct \(s\in\mathbb F_2^m\) give pairwise orthogonal nonzero vectors on \(T\). Thus \(r_w\) equals the number of block-parity syndromes \(s\) achievable by a vector \(a\) of total Hamming weight \(w\), with no multiplicity of that syndrome.

**3. All achievable weights.** Fix a syndrome \(s\) and write \(h(s)=\sum_i s_i\), \(u(s)=\sum_i\lfloor(b_i-s_i)/2\rfloor\). In block \(i\) the feasible numbers of ones are \(s_i,s_i+2,\ldots,s_i+2\lfloor(b_i-s_i)/2\rfloor\). Their Minkowski sum contains precisely every weight \(h(s)+2j\), \(0\le j\le u(s)\). Hence the rank generating polynomial obeys the finite, exact identity
\[
F(z)=\sum_{s\in\mathbb F_2^m}z^{h(s)}\frac{1-z^{2(u(s)+1)}}{1-z^2}.
\]
For a block of positive size \(b\), the two integers \(2\lfloor b/2\rfloor\) and \(1+2\lfloor(b-1)/2\rfloor\) are exactly \(b\) and \(b-1\), in some order. Therefore
\[
\sum_s z^{h(s)}=(1+z)^m,\qquad \sum_s z^{h(s)+2u(s)}=z^{N-m}(1+z)^m.
\]
Substitution gives, as a polynomial identity,
\[
F(z)=\frac{(1+z)^m(1-z^{N-m+2})}{1-z^2}=(1+z)^{m-1}\sum_{j=0}^{N-m+1}z^j.
\]
The apparent denominators cancel, so evaluation at \(z=1\) is legitimate and yields \(B=\sum_w r_w=2^{m-1}(N-m+2)\).

**4. Long-time decay and loss-rate independence.** Set \(H_0=JA+\varepsilon I\). The direct sum of the shells' evaluation kernels is the maximal \(H_0\)-invariant subspace \(\mathcal D\subseteq\ker\Gamma\). It is invariant under \(H_0\) and annihilated by \(\Gamma\). Both \(H_0\) and \(\Gamma\) are self-adjoint, so \(\mathcal D^\perp\) is invariant for both. If \(Hv=\lambda v\), then
\[
\operatorname{Im}\lambda\,\lVert v\rVert^2=-\langle v,\Gamma v\rangle\le0.
\]
Equality implies \(\Gamma v=0\), and then \(v\) is an \(H_0\) eigenvector in \(\mathcal D\). Hence the complementary restriction of \(H\) has no eigenvalues on the real axis; all have strictly negative imaginary parts. Its finite-dimensional semigroup decays to zero even with nontrivial Jordan blocks. The asymptotic survival projector is therefore the orthogonal projection onto \(\mathcal D\), and the maximally mixed capture fraction is \((2^N-D)/2^N\). This uses only positivity of each \(\kappa_x\), not their equality.

## Verification
Run \(\texttt{python3 verify.py}\) using the Python standard library. The standalone checker calculates ranks of explicitly constructed Walsh restriction matrices over \(\mathbb F_3\) for 134 ordered block partitions and compares them with the polynomial coefficients. This is exact for the tested cases: distinct restricted characters form columns of an invertible Walsh matrix over any odd field. For 30 additional small-size ordered partitions, an independent Krylov-span construction from the trap basis under the hypercube adjacency operator checks the bright dimension over \(\mathbb F_{101}\). It reports \(\texttt{VERIFY_OK spectral_partitions=134 krylov_partitions=30}\). These finite comparisons validate implementations and examples; the all-parameter statement follows from the proof above.

## Relationship to prior work
Moore and Russell [1] describe Fourier dynamics of continuous-time hypercube quantum walks, providing the unperturbed walk context, but not the present codeword-trap rank polynomial. Novo and collaborators [2] study symmetry reductions and transport, including hypercube transport toward a single target. Le and collaborators [3] characterize dark states and their suppression in quantum networks, but do not supply the all-block-repetition-code spectrum. Razzoli and collaborators [4] discuss continuous-time quantum-walk transport efficiency and trapping. The general energy-shell/observability viewpoint is standard; the statement assessed here is the simultaneous, block-geometry-independent shell-rank formula for complete product-repetition-code trap sets and its loss-rate-independent capture law. The case of one repetition block, corresponding to two antipodal traps, is elementary and is not asserted as a separate new finding. Historical novelty remains subject to discovery of an equivalent earlier coding-theory restriction-rank or quantum-transport formula.

## Limitations
The result assumes one particle, uniform undirected hypercube hopping, and strictly positive diagonal loss at **every** codeword in a product of disjoint binary repetition blocks. A zero absorber rate, dephasing, disorder in hopping or on-site energies, additional interactions, non-block codes, and multiple-particle models are not covered. It does not compare finite-time transport rates: different block geometries and heterogeneous losses can have different decay constants and transients despite identical dark spectra.

## References
[1] C. Moore and A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137, initially public 2001-04-29. https://arxiv.org/abs/quant-ph/0104137

[2] L. Novo et al., *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209, initially public 2014-12-22. https://arxiv.org/abs/1412.7209

[3] T. P. Le et al., *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482, initially public 2017-07-24. https://arxiv.org/abs/1707.07482

[4] L. Razzoli et al., *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, arXiv:2011.13794, initially public 2020-11-27. https://arxiv.org/abs/2011.13794
