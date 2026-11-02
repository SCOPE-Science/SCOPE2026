# Affine-hyperplane entanglement law for ternary Hamming graph states

## Finding

Let \(d\ge1\), and form the Hamming graph \(H(d,3)=K_3^{\square d}\): its vertices are \(\mathbb F_3^d\), with an edge precisely when two vertices differ in one coordinate. Place one **qubit** (not a qutrit) at every vertex and prepare the unweighted, pure graph state by controlled-\(Z\) gates on all graph edges. For any nonzero \(u\in\mathbb F_3^d\) and any \(c\in\mathbb F_3\), partition the qubits into \(A=\{x:u\cdot x=c\}\) and \(B=\mathbb F_3^d\setminus A\). Set \(s=|\{j:u_j\ne0\}|\), so \(1\le s\le d\).

The entropy of this partition, in bits, is exactly
\[
\boxed{r_{d,s}=\operatorname{rank}_{\mathbb F_2}\Gamma_{A,B}
=\frac{3^{d-s}}4\bigl(3^s+(-1)^{s-1}\bigr).}
\]
The reduced density matrix \(\rho_A\) has precisely \(2^{r_{d,s}}\) nonzero eigenvalues, all equal to \(2^{-r_{d,s}}\); every positive-order Rényi entropy and the von Neumann entropy equal \(r_{d,s}\) bits. The formula is independent of the nonzero coefficient values and the affine offset \(c\), depending on the normal only through its support size.

For \(d\ge2\), the minimum entropy over **all** affine-hyperplane cuts is \(2\cdot3^{d-2}\) bits, attained precisely by normals of support \(s=2\); the maximum is \(3^{d-1}\) bits, attained precisely at support \(s=1\). The rank fraction relative to the number \(|A|=3^{d-1}\) of qubits on the small side is
\[
\frac{r_{d,s}}{|A|}=\frac34+\frac{(-1)^{s-1}}{4\cdot3^{s-1}}.
\]
Thus the deficit oscillates with support parity and approaches one quarter of \(|A|\) as the normal support increases. These are exact finite-system statements, not asymptotic approximations.

## Assumptions and scope

The graph is a finite simple Hamming graph \(H(d,3)\), with every coordinate in the three-element field and one two-level quantum system at each graph vertex. Each edge applies exactly one ordinary qubit controlled-\(Z\) gate to \(|+\rangle^{\otimes3^d}\). The cut is any codimension-one affine \(\mathbb F_3\)-hyperplane and its complement. The affine-hyperplane size is \(3^{d-1}\), and the complement has \(2\cdot3^{d-1}\) vertices. No randomness, decoherence or weighted graph edges are assumed. Distinct notions of characteristic are important: the coordinate alphabet is \(\mathbb F_3\), while cut-adjacency ranks of qubit graph states are computed over \(\mathbb F_2\).

## Proof

**1. General graph-state cut spectrum.** Let \(\Gamma\) be the \(|A|\)-by-\(|B|\) cross-adjacency matrix over \(\mathbb F_2\). Controlled phases acting wholly within either side are local unitaries for this bipartition, so the Schmidt spectrum is unchanged if those edges are omitted. The resulting coefficient matrix in the computational basis is \(2^{-(|A|+|B|)/2}(-1)^{a^{\mathsf T}\Gamma b}\). Its reduced-density-matrix entries obey
\[
(\rho_A)_{a,a'}=2^{-|A|}\mathbf1_{\{\Gamma^{\mathsf T}(a+a')=0\}}.
\]
Writing \(r=\operatorname{rank}_{\mathbb F_2}\Gamma\), the computational labels \(a\) split into \(2^r\) cosets of \(\ker\Gamma^{\mathsf T}\), each of size \(2^{|A|-r}\). Each coset contributes one positive eigenvalue \(2^{-|A|}2^{|A|-r}=2^{-r}\), and its remaining eigenvalues vanish. This proves the spectral claim once the exact cut rank is determined.

**2. Reduce to active coordinates.** Every nonzero coefficient of \(u\) is \(1\) or \(-1\) in \(\mathbb F_3\). Coordinatewise multiplication by those coefficients, coordinate permutations and translation in one active coordinate are automorphisms of \(H(d,3)\), carrying the specified affine hyperplane to
\[
A_0=\{(x_1,\ldots,x_d):x_1+\cdots+x_s=0\pmod3\}.
\]
The inactive \(d-s\) coordinates never create a cross-edge, and fixing their values partitions \(\Gamma\) into \(3^{d-s}\) identical diagonal blocks. Therefore \(\operatorname{rank}\Gamma=3^{d-s}\operatorname{rank}\Gamma_s\), where \(\Gamma_s\) is the hyperplane cut matrix for \(H(s,3)\). It suffices to evaluate \(\Gamma_s\) for every \(s\ge1\).

**3. Convolution reduction.** Put \(m=s-1\) and identify each of the three residue classes of coordinate sum with \(\mathbb F_3^m\) by using the first \(m\) coordinates; the last coordinate is determined by the residue. A vertex with total residue \(1\) is adjacent to the residue-zero hyperplane exactly by decreasing any one of its \(s\) coordinates, and a vertex with residue \(2\) is adjacent exactly by increasing any one coordinate. Consequently the transpose cross matrix maps a function \(f\colon\mathbb F_3^m\to\mathbb F_2\) to two components
\[
T_-f(z)=f(z)+\sum_{j=1}^m f(z-e_j),\qquad
T_+f(z)=f(z)+\sum_{j=1}^m f(z+e_j).
\]
Its kernel is \(\ker T_-\cap\ker T_+\). In particular, this explicitly identifies the physical cut-rank problem with a pair of coupled three-torsion convolution constraints, rather than the spectrum of the full Hamming adjacency matrix.

**4. Common kernel in characteristic two.** Extend scalars from \(\mathbb F_2\) to \(\mathbb F_4=\{0,1,\omega,\omega^2\}\), where \(\omega^2+\omega+1=0\). Since \(3\) is prime to \(2\), the translations on \(\mathbb F_3^m\) admit a simultaneous character basis \(\chi_a(z)=\omega^{a\cdot z}\), indexed by \(a\in\mathbb F_3^m\). On such a character the eigenvalues of \(T_-\) and \(T_+\) are
\[
\lambda_-(a)=1+\sum_{j=1}^m\omega^{-a_j},\qquad
\lambda_+(a)=1+\sum_{j=1}^m\omega^{a_j}=\lambda_-(a)^2.
\]
The last equality is Frobenius squaring in \(\mathbb F_4\), not complex conjugation. Hence the two kernels are identical after scalar extension, so the common kernel has dimension equal to the number of \(m\)-tuples for which \(\sum_j\omega^{-a_j}=1\). Matrix ranks are unchanged under field extension, making this count valid over \(\mathbb F_2\).

**5. Exact character count.** The map \(a_j\mapsto\omega^{-a_j}\) bijects \(\mathbb F_3\) with \(\mathbb F_4^\times\). In the additive group of \(\mathbb F_4\), let \(N_m\) be the number of ordered sequences of \(m\) nonzero field elements summing to \(1\). Orthogonality of the four additive characters gives
\[
4N_m=3^m-(-1)^m.
\]
Indeed, the trivial additive character contributes \(3^m\); each of the other three has sum \(-1\) over \(\mathbb F_4^\times\), and the sum of their values at the nonzero element \(1\) is \(-1\). This also holds for \(m=0\), when \(N_0=0\). Therefore the cut-matrix rank for \(H(s,3)\) is
\[
3^{s-1}-N_{s-1}
=\frac{3^s+(-1)^{s-1}}4.
\]
Combining with the inactive-coordinate factor proves the boxed formula for all \(d,s\) and all affine hyperplanes.

**6. Extremal hyperplane entanglement.** The normalized entropy equals \(\frac34+(-1)^{s-1}/(4\cdot3^{s-1})\). For odd \(s\), it strictly decreases from \(1\) at \(s=1\) toward \(3/4\); for even \(s\), it strictly increases from \(2/3\) at \(s=2\) toward \(3/4\). Thus, for \(d\ge2\), the unique maximizing support size is \(s=1\) and the unique minimizing support size is \(s=2\), giving the announced sharp values. Different normals or offsets with the same support size are symmetry-equivalent.

## Verification

The standalone program `artifacts/check.py` independently constructs the physical Hamming graph and cut matrices, row-reduces their binary incidence masks, and checks the claimed ranks. It checks all \(3(3^d-1)\) nonzero-normal-and-offset choices for each dimension \(1\le d\le5\), plus all support sizes and three offsets in dimensions \(6\) and \(7\), for a total of \(1113\) affine cuts. It additionally constructs all coordinate-sum-zero cut matrices for \(1\le d\le8\), checking \(3280\) cut rows, and independently computes full computational-basis graph states and reduced-density-matrix spectra for \(d=1,2\), checking the equal-eigenvalue claim without invoking the Fourier proof. Running `python3 artifacts/check.py` with Python 3 and NumPy reproduces `artifacts/check_output.txt`. These finite tests confirm examples and implementation consistency; the all-dimensional result follows from Steps 1–6, not from enumerating finite dimensions.

## Relationship to prior work

Hein, Eisert and Briegel (2003) and Hein and collaborators (2006) establish the general binary cut-rank description of qubit graph-state entanglement. That foundational formula is used and credited here, not presented as new. The evaluated object here is instead the **explicit all-hyperplane rank and complete eigenvalue spectrum** for the ternary Hamming family, including the support-controlled extremal classification. The proof needs the specific paired-convolution reduction and an additive-character count in \(\mathbb F_4\).

Parez, Bernard, Crampé and Vinet (2022) analyze free-fermion ground-state entanglement on Hamming graphs. Their quantum state, correlation-matrix spectrum and tested subsystems differ from the unweighted qubit graph-state affine hyperplane cut. Known spectral formulas for the full Hamming adjacency operator do not by themselves state the rank of this characteristic-two cross block. The inspected sources do not contain the combined claim; this is a statement about the material examined and is not a guarantee of historical uniqueness.

## Limitations

Only unweighted pure **qubit** graph states on ternary Hamming graphs and hyperplane-versus-complement cuts are covered. Neither arbitrary vertex cuts nor qutrit graph states, weighted controlled-phase gates, noisy states or free-fermion ground states are classified. Finite exact checks are corroborative, not a proof of cases beyond those enumerated. The possibility of an equivalent result in specialized coding-theory or Hamming-graph cut-rank literature remains a historical-priority risk. There is no independent audit or independent validation in this package.

## References

1. M. Hein, J. Eisert, H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130, first posted 2003-07-18; see the bipartite split/cut-rank relation. https://arxiv.org/html/quant-ph/0307130v7
2. M. Hein et al., *Entanglement in Graph States and its Applications*, arXiv:quant-ph/0602096, first posted 2006-02-11; see Proposition 10 and its reduced-state discussion. https://ar5iv.labs.arxiv.org/html/quant-ph/0602096
3. G. Parez, P.-A. Bernard, N. Crampé, L. Vinet, *Multipartite information of free fermions on Hamming graphs*, arXiv:2212.09158, first posted 2022-12-18; see Sections II–III and the distinction between free-fermion and graph-state models. https://arxiv.org/html/2212.09158v2
