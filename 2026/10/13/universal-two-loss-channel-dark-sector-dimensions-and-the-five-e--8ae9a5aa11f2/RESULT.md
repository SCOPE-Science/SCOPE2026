# Universal two-loss-channel dark-sector dimensions and the five-emitter threshold

## Finding

Two independent collective-emission profiles can retain exact two-excitation dark vectors even when their spatial couplings are completely different. The common dark-space dimension depends **only on multiplicities of the ratios of the two profiles**, and admits a complete classification for all emitter counts.

Let \(n\ge 2\), and write
\[
 L_c=\sum_{i=1}^{n}c_i\sigma_i^-,\qquad
 L_d=\sum_{i=1}^{n}d_i\sigma_i^- ,\qquad
 c_i d_i\ne0.
\]
On the two-excitation sector \(\mathcal H_{n,2}=\operatorname{span}\{|ij\rangle:1\le i<j\le n\}\), set
\[\mathcal D_{n,2}=\ker(L_c|_{\mathcal H_{n,2}})\cap\ker(L_d|_{\mathcal H_{n,2}}).\]
Write \(r_i=d_i/c_i\); let \(h=|\{r_i\}|\) and \(m=\max_z|\{i:r_i=z\}|\). The complete formula is
\[
\dim\mathcal D_{n,2}=
\begin{cases}
0,& n=2,3,\\
2,& n=4,\ h=1,\\
1,& n=4,\ \{r_i\}\text{ consists of two distinct equal pairs},\\
0,& n=4,\text{ otherwise},\\
\binom n2-n,&n\ge5,\ h=1,\\
\binom n2-2n+2,&n\ge5,\ h\ge2,\ m\ge n-2,\\
\binom n2-2n+1,&n\ge5,\ h\ge2,\ m\le n-3.
\end{cases}
\]
Thus at five sites with pairwise distinct ratios the common dark space is exactly one-dimensional, whereas at four sites it is zero-dimensional unless the ratios arrange into two equal pairs. All coefficients may be arbitrary nonzero complex numbers.

For example, with \(n=5\), \(c_i=1\) and \(d_i=i\), in the lexicographically ordered basis \((|12\rangle,|13\rangle,|14\rangle,|15\rangle,|23\rangle,|24\rangle,|25\rangle,|34\rangle,|35\rangle,|45\rangle)\), a nonzero common dark vector has amplitudes
\[
(1,-6,9,-4,6,-16,9,6,-6,1).
\]
For \(n=4\) and \((r_1,r_2,r_3,r_4)=(1,1,2,2)\), the vector \(|13\rangle-|14\rangle-|23\rangle+|24\rangle\) is dark for both profiles when \(c_i=1\).

## Assumptions and scope

Each emitter is a two-level system, with \(\sigma_i^- = |0\rangle_i\langle1|\). Both jumps contain only lowering operators; **every site coefficient in each jump is nonzero**. All kernel dimensions are over \(\mathbb C\). Their values do not depend on the jump rates. A jump profile may be proportional to the other; the theorem explicitly includes that case. No assumptions of periodicity, equal coupling or positive-real coefficients are needed.

For the dynamical corollary, additionally assume a Markovian Lindblad generator with strictly positive rates multiplying only dissipators for \(L_c,L_d\), and Hamiltonian \(H=\omega\sum_i |1\rangle_i\langle1|\), with no interactions or other terms. Then every density matrix supported in \(\mathcal D_{n,2}\) is stationary, since both jumps annihilate its support and the Hamiltonian is scalar on the two-excitation sector.

## Proof

Let \(|\psi\rangle=\sum_{i<j}x_{ij}|ij\rangle\) and extend \(x_{ij}=x_{ji}\), \(x_{ii}=0\). Its one-excitation amplitudes after the two jumps are
\[
\langle i|L_c|\psi\rangle=\sum_{j\ne i}c_jx_{ij},\qquad
\langle i|L_d|\psi\rangle=\sum_{j\ne i}d_jx_{ij}.
\]
The invertible change of variables \(y_{ij}=c_ic_jx_{ij}\) turns the common kernel conditions into
\[
\sum_{j\ne i}y_{ij}=0,\qquad \sum_{j\ne i}r_jy_{ij}=0
\quad\text{for every }i.
\]
Let \(B\) be this \(2n\)-row linear system on the \(\binom n2\) edge variables \(y_{ij}\). Its left null vectors are pairs of scalars \((\alpha_i,\beta_i)\), one pair for each vertex, satisfying
\[
\alpha_i+\alpha_j+\beta_i r_j+\beta_j r_i=0
\quad\text{for every }i<j.
\tag{1}
\]
Writing \(u_i=(1,r_i)^\top\) and \(\ell_i=(\alpha_i,\beta_i)^\top\), equation (1) becomes \(\ell_i^\top u_j+\ell_j^\top u_i=0\).

When all ratios coincide, the second set of constraints is redundant. For \(n\ge3\), the signless incidence matrix of the complete graph has row rank \(n\): its left-null equations \(\alpha_i+\alpha_j=0\) for all pairs force every \(\alpha_i=0\), using any triangle and characteristic zero. Therefore the dimension is \(\binom n2-n\). For \(n=2\), the single edge has nonzero image; for \(n=3\), the first jump alone is injective on the three-dimensional edge space. This already proves the small cases.

Suppose henceforth that at least two ratios differ, and select distinct anchor vertices \(a,b\) with \(r_a\ne r_b\). The vectors \(u_a,u_b\) are a basis of \(\mathbb C^2\). Any possible left null vector has a **unique** representation
\[
\ell_a=-A^\top u_a,\quad \ell_b=-A^\top u_b,
\quad \ell_k=A u_k\quad(k\notin\{a,b\}),
\]
for a \(2\times2\) matrix \(A\): the anchor components uniquely determine \(A\), and the anchor-to-other equations uniquely determine each \(\ell_k\). The equations remaining are
\[
u_a^\top(A+A^\top)u_b=0,\qquad
u_k^\top(A+A^\top)u_l=0\quad(k<l,\ k,l\notin\{a,b\}).
\]
The skew-symmetric part of \(A\) is unconstrained (one degree of freedom). A symmetric \(2\times2\) matrix has three entries, and each remaining pair with ratios \(s,t\) supplies the linear row
\[
v(s,t)=(1,s+t,st).
\]
If \(T\) is the matrix of these rows for the anchor pair and **all** pairs of nonanchor vertices, the left-null dimension is \(4-\operatorname{rank}T\), whence
\[
\operatorname{rank}B=2n-4+\operatorname{rank}T,\qquad
\dim\mathcal D_{n,2}=\binom n2-2n+4-\operatorname{rank}T.
\tag{2}
\]

For \(n=4\), \(T\) contains precisely \(v(r_a,r_b)\) and the row for the other two vertices. Two such rows, both beginning with \(1\), coincide precisely when their unordered ratio pairs coincide (their sums and products agree). As the anchors have distinct ratios, this is possible exactly for two distinct equal pairs. Hence \(\operatorname{rank}T=1\) in that exceptional case and \(2\) otherwise. Formula (2) proves the four-emitter classification.

For \(n\ge5\), at least two distinct rows occur, so \(\operatorname{rank}T\ge2\). If a ratio occurs at least \(n-2\) times, choose the anchors so that the nonanchor ratios all coincide when possible, or consist of that dominant ratio plus at most one exception. Indeed, the nonanchor pair rows are either a single type \(v(s,s)\) or a pair of types \(v(s,s),v(s,t)\); the anchor row provides at most one further type, but when \(v(s,t)\) appears among nonanchors the anchor row is also \(v(s,t)\). Hence there are at most two independent rows and \(\operatorname{rank}T=2\). If the ratio distribution is nonconstant and no ratio occurs more than \(n-3\) times, proceed by the number of distinct ratios. For exactly two distinct values \(s\ne t\), each multiplicity is at least three; choosing one anchor of each value leaves rows \(v(s,s),v(s,t),v(t,t)\), which are independent. For at least three distinct values, choose the two anchors so the \(n-2\) nonanchors still contain three distinct ratio values \(s,t,u\). This is possible: with three values and at least five vertices, the bound \(m\le n-3\) prevents two singleton classes from being the only classes outside a dominant one, and with four or more values one can discard two without losing three distinct values. The three rows \(v(s,t),v(s,u),v(t,u)\) have nonzero determinant for pairwise distinct \(s,t,u\) (a Vandermonde factor). Thus \(\operatorname{rank}T=3\). Applying (2) proves every remaining dimension formula.

Finally, on the stated number Hamiltonian, every vector in \(\mathcal H_{n,2}\) is an eigenvector with the same energy \(2\omega\). For a density operator supported on the common kernel, the two dissipators vanish because \(L_c\rho=\rho L_c^\dagger=L_d\rho=\rho L_d^\dagger=0\), while \([H,\rho]=0\). Therefore the state is stationary.

## Verification

Run `python3 verify.py` using the Python standard library. It builds the two-jump maps directly in the computational basis and uses exact-rational row reduction, not floating-point thresholds. It checked every integer partition of ratio multiplicities for \(2\le n\le10\), additional seeded nonuniform rational coupling profiles for \(4\le n\le9\), and both explicit dark vectors: `VERIFY_OK 379 exact rational rank and vector checks`. The proof establishes the formula over \(\mathbb C\) for all permitted \(n\); finite rational tests do not prove the infinite theorem or certify novelty.

## Relationship to prior work

Khoudiri, Ullah, El Allati, and Müstecaplıoğlu (arXiv:2608.09693v1) study dark and metastable collective-dissipative states and a uniform-spin singlet decomposition with raising and lowering. That source motivates protection under collective environmental loss, but its operators and sectors do not include the full pair of arbitrary nonproportional weighted lowering jumps studied here. Hebenstreit et al. (arXiv:1701.01471v1) analyze several independent decay channels in multilevel emitters, rather than two independent spatial decay profiles on qubits. Holzinger et al. (arXiv:2209.09212v3) study localized multiphoton dark states in a waveguide setting with a different single-channel collective structure. The result here is the exact two-excitation common-kernel dimension, its exceptional ratio-multiplicity loci, and the minimum generic emitter number. No universality, robustness or priority is inferred from failed indexing searches.

## Limitations

The statement assumes every coefficient is nonzero and only two lowering jumps. The stationary-state corollary assumes no additional Hamiltonian interaction, raising jump, independent local decay or other dissipator. The classification makes no claims about how to prepare the vectors, whether the dark states remain stable under coefficient errors, or the dimensions of higher-excitation dark spaces. Novelty assessment may be affected by unindexed results, and related recent manuscripts without accessible complete text remain potential overlap risks.

## References

- Khoudiri, Ullah, El Allati, and Müstecaplıoğlu, *Collective-dissipation-induced dark and metastable-like states for enhanced quantum battery performance*, arXiv:2608.09693v1 (first public 2026-08-10), https://arxiv.org/abs/2608.09693.
- Hebenstreit and coauthors, *Subradiance and entanglement in atoms with several independent decay channels*, arXiv:1701.01471v1, https://arxiv.org/abs/1701.01471.
- Holzinger and coauthors, *Control of Localized Multiple Excitation Dark States in Waveguide QED*, arXiv:2209.09212v3, https://arxiv.org/abs/2209.09212.
- Rubies-Bigorda and coauthors, *Stabilization of dark states in emitter arrays coupled to a half-waveguide*, arXiv:2609.03040v1, https://arxiv.org/abs/2609.03040 (abstract-level contextual comparison only).
