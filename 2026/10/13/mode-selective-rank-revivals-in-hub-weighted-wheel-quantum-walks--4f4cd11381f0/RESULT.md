# Mode-selective rank revivals in hub-weighted wheel quantum walks

## Finding

Let \(n\ge3\) be an integer and \(g>0\) a real coupling. A hub-weighted wheel is a cycle \(C_n\) with one additional hub joined to each rim vertex by an edge of weight \(g\), while each cycle edge has weight one. Relative to the hub and cyclically ordered rim vertices, its real symmetric Hamiltonian is
\[
H_{n,g}=\begin{pmatrix}0&g\mathbf1_n^{\mathsf T}\\g\mathbf1_n&A(C_n)\end{pmatrix}.
\]
Its continuous-time walk is \(U(t)=e^{itH_{n,g}}\). The Cesàro average mixing matrix, with entrywise (Hadamard) multiplication \(\circ\), is
\[
\widehat M_{n,g}=\lim_{T\to\infty}\frac1T\int_0^T U(t)\circ\overline{U(t)}\,dt.
\]

Define \(\sigma=\sqrt{1+ng^2}\), \(\beta=(2+(n-1)g^2)/(2(1+ng^2))\), and \(\alpha=(1-\sigma^{-1})/n>0\). For \(1\le k\le\lfloor n/2\rfloor\), put \(\mu_k=2\cos(2\pi k/n)\). Every \(\mu_k<0\) determines exactly one **resonant coupling**
\[
g_k=\sqrt{\frac{\mu_k(\mu_k-2)}{n}}.
\]
The values \(g_k\) are mutually distinct. At a given \(g>0\), write \(k_*=k\) if \(g=g_k\) for some negative \(\mu_k\); otherwise \(k_*\) is absent. For each integer \(1\le j\le n-1\) define
\[
c_n(j)=\begin{cases}1/n,&n\text{ odd},\\2/n,&n\text{ even and }j\text{ even},\\0,&n\text{ even and }j\text{ odd}.
\end{cases}
\]
Then the **entire spectrum**, with every eigenvalue listed according to multiplicity, is
\[
\operatorname{Spec}(\widehat M_{n,g})
=\{1,\beta\}\mathbin{\uplus}
\left\{c_n(j)+\alpha\,\mathbf1_{\{k_*\text{ exists, }j\equiv\pm k_*\ (\mathrm{mod}\ n)\}}:1\le j<n\right\}.
\tag{1}
\]
Here \(\uplus\) denotes multiset union, and the indicator is zero if no resonance occurs. The exact rank follows:
\[
\operatorname{rank}\widehat M_{n,g}
=\begin{cases}
n+1,&n\text{ odd},\\
\dfrac n2+1+\mathbf1_{\{k_*\text{ exists and odd}\}}\bigl(2-\mathbf1_{\{2k_*=n\}}\bigr),&n\text{ even}.
\end{cases}
\tag{2}
\]
The second-case increment is understood as zero when \(k_*\) does not exist. Thus every odd-rim weighted wheel has positive-definite average mixing; for an even rim, odd Fourier modes are dark generically, but one or two become strictly positive at isolated, explicitly known spoke weights. Eigenvalue crossings at even \(k_*\) change positive eigenvalues but not the rank.

Moreover, the **complete kernel** is the span over \(\mathbb R\) of hub-zero real Fourier sine/cosine rim vectors with *odd* frequencies, excluding the resonant frequency \(k_*\) and its conjugate \(n-k_*\) if \(k_*\) is odd. For odd \(n\), the kernel is zero. Complex Fourier characters provide the equivalent complexified kernel statement.

For example, if \(n=8\), the generic rank is \(5\) on \(9\) vertices, whereas at \(k_*=3\),
\[
g^2=\frac{1+\sqrt2}{4},\qquad\operatorname{rank}\widehat M_{8,g}=7,
\qquad\alpha=\frac{2-\sqrt2}{8}.
\]
This is an isolated two-mode rank revival; arbitrary positive nonresonant perturbations of this coupling restore rank \(5\). For \(n=6\), the unique mode \(k_*=3=n/2\) at \(g^2=4/3\) adds one rank, giving \(5\) on \(7\) vertices.

## Assumptions and scope

The theorem concerns real, undirected, weighted adjacency Hamiltonians only, with \(g>0\), unit rim weights, one hub and \(n\ge3\). All averages are infinite-time Cesàro means. A zero or negative spoke coupling, magnetic phases, onsite energies and other rim graphs are not within the asserted domain. Normalizations fix the standard orthonormal vertex basis; no division by elapsed time occurs after taking the limit. Rank and kernel are over the real numbers (or equivalently the complexification). The resonance criterion uses exact equality of real numbers, not numerical tolerance. The limit always exists because the Hamiltonian has finitely many real eigenvalues.

## Proof

**1. Projectors and the only possible degeneracy.** Let \(e_0\) be the hub basis vector and \(v=(0,\mathbf1_n/\sqrt n)\) the normalized uniform rim vector. Their invariant two-plane carries
\[
\begin{pmatrix}0&g\sqrt n\\g\sqrt n&2\end{pmatrix},
\qquad \lambda_\pm=1\pm\sigma.
\]
The remaining mutually orthogonal rim subspaces are Fourier modes. Write \(Q_k\), \(1\le k\le\lfloor n/2\rfloor\), for the rim orthogonal projector whose matrix entries at cycle positions \(a,b\in\{0,\ldots,n-1\}\) are
\[
Q_k(a,b)=\begin{cases}
\dfrac2n\cos\bigl(2\pi k(a-b)/n\bigr),&2k<n,\\
\dfrac1n(-1)^{a-b},&2k=n.
\end{cases}
\tag{3}
\]
The \(Q_k\) are pairwise orthogonal, and \(\sum_kQ_k=I_n-J_n/n\). They have distinct adjacency energies \(\mu_k\), strictly decreasing with \(k\) along \([0,\pi]\). Denote their lifts to the full vertex space by \(\widetilde Q_k=\operatorname{diag}(0,Q_k)\).

Let \(E_+\), \(E_-\) be the rank-one projectors of the two-plane, extended by zero on its complement, and set \(b_\pm=(1\pm\sigma^{-1})/2\). Direct diagonalization gives
\[
(E_\pm)_{00}=\frac{1\mp\sigma^{-1}}2,
\quad (E_\pm)_{0a}=\pm\frac{g}{2\sigma},
\quad (E_\pm)_{ab}=\frac{b_\pm}{n}.
\tag{4}
\]
Because \(\lambda_+>2\), no Fourier energy equals \(\lambda_+\). As \(\lambda_-<0\), an equality \(\lambda_-=\mu_k\) is possible only for \(\mu_k<0\) and is equivalent to \(ng^2=\mu_k(\mu_k-2)\), yielding precisely \(g_k\). Strict monotonicity of \(\mu_k\) makes the collision index unique. In the absence of a collision the distinct spectral projectors are \(E_+\), \(E_-\), and the lifted \(Q_k\); at a collision, replace \(E_-\) and \(\widetilde Q_{k_*}\) by their sum. These are *full* orthogonal eigenspace projectors, including at degeneracy.

**2. The exact average mixing matrix.** For any finite real symmetric Hamiltonian \(H=\sum_\lambda\lambda F_\lambda\) with distinct-energy orthogonal projectors \(F_\lambda\), finite Fourier averaging gives
\[
\widehat M(H)=\sum_\lambda F_\lambda\circ F_\lambda.
\tag{5}
\]
Indeed, every off-diagonal frequency \(e^{it(\lambda-\nu)}\) has zero Cesàro mean when \(\lambda\ne\nu\). In the noncollision notation (evaluated algebraically even at resonant \(g\)), let
\[
M_0=E_+\circ E_+ +E_-\circ E_-+
\sum_{k=1}^{\lfloor n/2\rfloor}\widetilde Q_k\circ\widetilde Q_k.
\]
Writing \(a=(1+\sigma^{-2})/2\), \(b=g^2/(2\sigma^2)\), and \(S=\sum_k Q_k\circ Q_k\), equation (4) gives the block identity
\[
M_0=\begin{pmatrix}
a&b\mathbf1_n^{\mathsf T}\\
b\mathbf1_n&\dfrac{a}{n^2}J_n+S
\end{pmatrix}.
\tag{6}
\]
At resonance the projector fusion produces the extra two cross-Schur terms:
\[
\widehat M_{n,g}-M_0
=2 E_-\circ\widetilde Q_{k_*}
=\alpha\widetilde Q_{k_*},
\qquad\alpha=\frac{2b_-}{n}=\frac{1-\sigma^{-1}}{n}>0.
\tag{7}
\]
Off resonance, \(\widehat M_{n,g}=M_0\). The contribution in (7) is positive semidefinite. This is the spectral origin of the isolated rank revival.

**3. Uniform sector and all nonconstant Fourier eigenvalues.** Each projector has the idempotence property \(\sum_bQ_k(a,b)^2=Q_k(a,a)\); therefore \(S\mathbf1_n=(n-1)\mathbf1_n/n\), while \(Q_k\mathbf1_n=0\). The hub-plus-uniform-rim subspace of (6) has matrix, in an orthonormal basis,
\[
\begin{pmatrix}a&\sqrt n\,b\\\sqrt n\,b&1-b\end{pmatrix}.
\]
Since \(1-a=nb\), its two eigenvalues are \(1\) and
\[
a-b=\frac{2+(n-1)g^2}{2(1+ng^2)}=\beta>0.
\tag{8}
\]
The resonant correction annihilates this sector.

For the rim-only sector, use complex Fourier rank-one projectors \(P_j(a,b)=e^{2\pi i j(a-b)/n}/n\), with indices taken modulo \(n\). The simple Schur-product identity
\[
P_j\circ P_l=\frac1nP_{j+l}
\tag{9}
\]
implies that \(S=\sum Q_k\circ Q_k\) has eigenvalue \(1/n\) on every nonconstant Fourier frequency if \(n\) is odd. For even \(n\), it has eigenvalue \(2/n\) on nonzero even frequencies and \(0\) on odd frequencies. To see this exhaustively, for \(2k<n\) write \(Q_k=P_k+P_{n-k}\), and for \(2k=n\) write \(Q_k=P_{n/2}\). Expansion using (9) gives terms \(P_{2k}\), \(P_{-2k}\) and \(2P_0\), with the antipodal projector contributing only \(P_0/n\). Multiplication by two permutes the nonzero residues modulo odd \(n\); for even \(n\), it hits only even residues, each exactly twice when both signs and all \(k\) are counted. The \(J_n\) term has zero nonconstant Fourier eigenvalues. Finally, \(Q_{k_*}\) acts as the identity exactly at Fourier frequencies congruent to \(\pm k_*\), with one frequency for \(2k_*=n\). Equation (7) therefore adds exactly \(\alpha\) at those frequencies. This proves the full multiset formula (1).

**4. Rank and nullspace.** Both uniform-sector eigenvalues are positive, and \(\alpha>0\). If \(n\) is odd, all \(n-1\) nonconstant values \(c_n(j)\) are \(1/n>0\), giving full rank \(n+1\). If \(n\) is even, exactly \(n/2-1\) nonzero even frequencies have baseline eigenvalue \(2/n\); the other \(n/2\) odd frequencies have baseline zero. Thus generic rank is \(2+n/2-1=n/2+1\). Resonance at an even frequency only changes existing positive eigenvalues; resonance at an odd frequency makes exactly the two conjugate modes positive, except for the unique self-conjugate antipodal index \(k_*=n/2\), which adds one. Since the Fourier basis diagonalizes the entire matrix, its remaining odd-frequency zero modes are *all* the kernel. This proves (2) and the kernel statement.

## Verification

The accompanying `verify.py` constructs Hamiltonians directly, groups numerical adjacency eigenvalues to form *full* orthogonal spectral projectors, and sums their entrywise squares independently of the Fourier formula. It compares these matrices and eigenvalues with (6)-(7) and (1), checks the predicted exact ranks and nullspace residuals, and tests several exact symbolic resonances using rational/algebraic arithmetic. A successful replay using Python, NumPy and SymPy produced `VERIFY_OK numerical_cases=442 exact_symbolic_cases=3 exact_matrix_identities=3 resonances=105 worst_matrix_error=2.23e-14 worst_spectrum_error=1.65e-14 worst_kernel_residual=1.17e-13 n6_k3_rank=5/7 n8_k3_rank=7/9`.

For an independent reproduction, run `python verify.py` in the same directory, with NumPy and SymPy available. Numeric comparisons include nonresonant perturbations of exact collision couplings; resonant values are identified algebraically before numerical eigenspace grouping. The script supplies finite corroboration only; equations (3)-(9) prove the statement for all integer rim sizes and all positive spoke weights.

## Relationship to prior work

Godsil's average-mixing spectral-projector formula (2011), together with cycle Fourier calculations, gives the basic Schur-square method. The 2005 work by Lo, Rajaram, Schepens, Sullivan, Tamon and Ward computes long-time quantum mixing for joins of circulants, but explicitly excludes coincidences between the two join-specific eigenvalues and nonconstant base eigenvalues in its relevant join theorem. The exceptional, spoke-weight-tunable coincidences are essential here. Coutinho, Godsil, Guo and Zhan (2018) give a general commutant interpretation of average mixing and its rank, not the present weighted wheel spectrum.

Kimmerling's 2023 dissertation establishes the unweighted Kulli-cycle windmill rank parity (including the one-blade wheel). **That unweighted rank formula is prior work, not a new result here.** At \(g=1\), the present classification is consistent with it, including collisions that add only already-positive even modes. The assessed new content is the full *weighted* family, its precise resonance locus, the isolated jump formula, and the mode-selective rank-revival phenomenon. These formulas follow by making the degenerate spectral-projector fusion explicit; a more general implicit treatment in unindexed literature may exist.

Irrational Quantum Walks (Coutinho, Baptista, Godsil, Spier and Werner; first posted August 18, 2022, primary MSC 81P68) motivates exact analysis of long-time quantum transport beyond purely numerical approximations. The present theorem uses weighted Hamiltonians rather than the integer-Hamiltonian algorithms that work develops.

## Limitations

The averages here concern the ordinary infinite-time Cesàro limit, not convergence rates or physical finite-time observations. The discontinuous spectral jump at an exact resonance disappears under any fixed positive detuning, but convergence near resonance is not quantified. No statement is made for magnetic or directed walks, vertex potentials, variable rim weights, or the degenerate \(g=0\) case. The exact spectral formula has a self-contained proof, but originality cannot be certified solely by a failed database search; broader join-eigenspace and Bose–Mesner methods might contain an equivalent statement. The complete Kimmerling dissertation was not available for page-by-page examination during the comparison, although its theorem and abstract were checked via its repository/indexed portions.

## References

1. Chris Godsil, *Average Mixing of Continuous Quantum Walks*, arXiv:1103.2578 (2011), https://arxiv.org/abs/1103.2578.
2. Peter Lo, Siddharth Rajaram, Diana Schepens, Daniel Sullivan, Christino Tamon, and Jeffrey Ward, *Mixing of Quantum Walk on Circulant Bunkbeds*, arXiv:quant-ph/0509059 (2005), https://arxiv.org/abs/quant-ph/0509059.
3. Gabriel Coutinho, Chris Godsil, Krystal Guo, and Hanmeng Zhan, *A New Perspective on the Average Mixing Matrix*, *Electronic Journal of Combinatorics* 25(4), P4.14 (2018), https://doi.org/10.37236/7867.
4. Paula Rachael Kimmerling, *Continuous-Time Quantum Walks on Windmill Graphs*, Washington State University PhD thesis (2023), https://doi.org/10.7273/000006322.
5. Gabriel Coutinho, Pedro Ferreira Baptista, Chris Godsil, Thomás Jung Spier, and Reinhard Werner, *Irrational Quantum Walks*, arXiv:2208.08971v1 (first public August 18, 2022), https://arxiv.org/abs/2208.08971.
