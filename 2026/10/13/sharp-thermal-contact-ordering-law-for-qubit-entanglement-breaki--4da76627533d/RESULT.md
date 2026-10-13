# Sharp thermal-contact ordering law for qubit entanglement breaking

## Finding
Consider a finite list of qubit generalized amplitude-damping channels, each characterized by a damping strength \(0<\gamma_i<1\) and a stationary excited-state population \(0\leq\nu_i\leq1/2\). All channels act on the same qubit, sequentially, with no intermediate controls or auxiliary quantum systems. Their multiset is fixed but their temporal order may vary.

**Theorem (exact order envelope and entanglement-breaking phase diagram).** For each permutation \(\pi\), with \(\pi(1)\) acting first, define
\[
R=\prod_{i=1}^{m}(1-\gamma_i),\qquad \Gamma=1-R,\qquad
s_\pi=\sum_{j=1}^{m}\gamma_{\pi(j)}\nu_{\pi(j)}\prod_{k=j+1}^{m}(1-\gamma_{\pi(k)}).
\]
Then the normalized Choi-state negativity of the ordered composition is exactly
\[
\mathcal N_\pi=\frac14\left[\sqrt{(\Gamma-2s_\pi)^2+4R}-\Gamma\right]_+,
\]
where \([u]_+=\max\{u,0\}\). The composition is entanglement-breaking if and only if
\[
s_\pi(\Gamma-s_\pi)\ge R.
\]
Applying the contacts in nondecreasing order of \(\nu_i\) (cold before hot) maximizes \(s_\pi\), minimizes \(\mathcal N_\pi\), and is the most favorable ordering for entanglement breaking. Nonincreasing order (hot before cold) reverses these extrema. All permutation outcomes are bounded by these two sorted orders. If \(\Gamma^2<4R\), none of the orders is entanglement-breaking. Otherwise, setting
\[
s_*=\frac{\Gamma-\sqrt{\Gamma^2-4R}}2,
\]
all orders are entanglement-breaking exactly when the hot-to-cold order has \(s\ge s_*\); no order is entanglement-breaking exactly when the cold-to-hot order has \(s<s_*\); and some but not all orders are entanglement-breaking exactly when the hot-to-cold offset is below \(s_*\) and the cold-to-hot offset is at least \(s_*\).

**Sharp two-contact order window.** Take a cold channel \(\nu_c=0\) and an infinite-temperature channel \(\nu_h=1/2\), with equal damping \(\gamma_c=\gamma_h=g\in(0,1)\). Let \(g_-\) and \(g_+\) be the unique roots in \((0,1)\) of, respectively,
\[
g^2(3-2g)-4(1-g)^2=0,\qquad g^2(3-g)-4(1-g)=0.
\]
They satisfy \(g_-\approx0.598278796872\) and \(g_+\approx0.710831453552\). Cold-then-hot is entanglement-breaking exactly for \(g\ge g_-\); hot-then-cold is entanglement-breaking exactly for \(g\ge g_+\). Thus for every \(g\in[g_-,g_+)\), changing **only the order** switches entanglement breaking on or off; neither constituent channel is itself entanglement-breaking there. The inequalities persist under small independent perturbations of the channel parameters when \(g\) lies strictly inside this interval. At \(g=2/3\), the respective Choi negativities are exactly \(0\) and \((3\sqrt2-4)/18>0\).

## Assumptions and scope
For a qubit density operator written as \(\rho=\bigl(\begin{smallmatrix}1-q&z\\\overline z&q\end{smallmatrix}\bigr)\), the channel \(\mathcal G_{\gamma,\nu}\) is defined by
\[
q\longmapsto (1-\gamma)q+\gamma\nu,\qquad
z\longmapsto\sqrt{1-\gamma}\,z.
\]
The linear extension to arbitrary matrices uses \(\gamma\nu\operatorname{Tr}(X)\) in its lower-right entry. The population \(\nu\) is that of the excited level, so nonnegative-temperature baths correspond to \(0\le\nu\le1/2\); the endpoint \(\nu=1/2\) is infinite temperature. The damping strengths are strictly between zero and one; boundaries in the theorem refer to exact inequalities inside these ranges. The channels are applied consecutively to one system; this is neither a quantum switch nor a tensor product of channels. Entanglement breaking means destroying entanglement with every reference system. Negativity is \((\|J^{T_{\mathrm{out}}}\|_1-1)/2\) for the normalized Choi state \(J\).

## Proof
**Composition and its effective parameter.** Write \(\eta_i=1-\gamma_i\). Induction through the scalar population update gives \(q_{\mathrm{out}}=Rq_{\mathrm{in}}+s_\pi\); multiplication of off-diagonal damping factors gives \(z_{\mathrm{out}}=\sqrt R\,z_{\mathrm{in}}\). The nonnegative weights \(w_j=\gamma_{\pi(j)}\prod_{k>j}\eta_{\pi(k)}\) telescope to \(\sum_jw_j=1-R=\Gamma\). Consequently \(0\le s_\pi\le\Gamma/2\), and the ordered composition is \(\mathcal G_{\Gamma,s_\pi/\Gamma}\).

**Choi test.** Applying the composite map to one half of \((|00\rangle+|11\rangle)/\sqrt2\), and partially transposing the output, gives in the ordered computational basis
\[
J_\pi^{T_{\mathrm{out}}}=\frac12\begin{pmatrix}
1-s_\pi&0&0&0\\
0&s_\pi&\sqrt R&0\\
0&\sqrt R&\Gamma-s_\pi&0\\
0&0&0&R+s_\pi
\end{pmatrix}.
\]
The two scalar eigenvalues are \((1-s_\pi)/2\) and \((R+s_\pi)/2\); the other two are \(\bigl(\Gamma\pm\sqrt{(\Gamma-2s_\pi)^2+4R}\bigr)/4\). The only possibly negative eigenvalue is the latter minus branch. Its nonnegativity is equivalent to \(s_\pi(\Gamma-s_\pi)\ge R\). By the two-qubit positive-partial-transpose separability criterion and the Choi criterion for entanglement-breaking channels, this is a necessary and sufficient condition. Its negative part yields the displayed negativity formula.

**Ordering.** Suppose neighboring channels \(a,b\) are applied in that temporal order and the multiset of later channels has damping product \(D=\prod_{k\text{ later}}(1-\gamma_k)>0\). Direct subtraction of the two affine compositions gives
\[
s_{\ldots a,b\ldots}-s_{\ldots b,a\ldots}=D\gamma_a\gamma_b(\nu_b-\nu_a).
\]
Repeated removal of adjacent inversions proves that cold-to-hot maximizes the offset, while hot-to-cold minimizes it. On \(0\le s\le\Gamma/2\), the function \(s(\Gamma-s)\) is nondecreasing and \(\sqrt{(\Gamma-2s)^2+4R}\) is nonincreasing. Therefore the extremal offsets simultaneously extremize the entanglement-breaking test and the Choi negativity in the stated directions. Maximizing \(s(\Gamma-s)\) over the allowed interval yields \(\Gamma^2/4\); when \(\Gamma^2\ge4R\), its lower threshold is precisely \(s_*\). This proves every phase assertion, including equality boundaries.

**Two-contact transition.** With common damping \(g\), the residual factor is \(R=(1-g)^2\) and \(\Gamma=2g-g^2\). Cold-then-hot gives \(s=g/2\), while hot-then-cold gives \(s=g(1-g)/2\). Substitution into the Choi determinant criterion, and in the second case division by the positive \(1-g\), yields the two cubic inequalities from the finding. Their left-hand sides minus right-hand sides have derivatives \((1-g)(6g+8)>0\) and \(-3g^2+6g+4>0\) on \((0,1)\). Each changes sign between zero and one, so each has a unique root; the first root precedes the second because the cold-then-hot offset is strictly larger. The second root is below \(3/4\), as can be verified by evaluating its cubic at \(3/4\). Neither constituent is entanglement-breaking on the intervening window: the cold contact has \(\nu=0\) and \(g<1\); the hot contact would require \(g^2/4\ge1-g\), which fails for \(g<3/4\). For \(g=2/3\), \(R=1/9\), \(\Gamma=8/9\), and the two offsets are \(1/3\) and \(1/9\), giving the exact claimed Choi negativities. The strict determinant inequalities in the interior imply persistence under sufficiently small perturbations by continuity.

## Verification
The standalone file `artifacts/verify.py` directly applies explicit four-Kraus-operator matrices to one half of a Bell state and checks the partial-transpose negativity against the formula above. It also uses exact rational arithmetic to check all permutations in deterministic small-instance samples, both extremal orderings, the neighboring-swap identity, and the two-contact example. With `numpy>=1.24`, running `python artifacts/verify.py` returned `VERIFY_OK 5320 permutation matrices; exact rational composition/EB checks; example verified`. This finite check is corroboration; all-size validity follows from the analytic proof.

## Relationship to prior work
Aslanbaş–Alkan–Karpat, arXiv:2609.00168v1, studies **coherently** controlled order and derives the two-channel generalized amplitude-damping composition commutator in Appendix E, equation (181). That exact local affine identity is prior work, not claimed as a new commutator theorem. Their analyzed entanglement is between switch control and target and is quantified by concurrence; the present question instead concerns preservation of an external reference by a **definite-order**, arbitrarily long concatenation, optimizing its normalized Choi negativity and entanglement-breaking status over permutations. Khatri–Sharma–Wilde, arXiv:1903.07747, establishes the entanglement-breaking boundary for a single generalized amplitude-damping channel. Lami–Giovannetti, arXiv:1411.2517, studies indices of repeated channels and filtering. These established ingredients motivate—but do not state—the all-permutation sharp envelope, its three-way phase diagram, or the exact interval of opposite-order entanglement-breaking outcomes for two individually non-entanglement-breaking thermal contacts. The result also differs from unitary-filter amendment protocols, which change the available operations instead of merely reordering a fixed multiset of thermal contacts.

## Limitations
The result holds only for phase-aligned, generalized amplitude-damping qubit channels with noninverted stationary populations. The monotonic sorting statement may fail if stationary excited populations extend above \(1/2\), because the Choi negativity then need not be monotone across the entire accessible offset interval. No claim is made about coherent switches, arbitrary qubit channels, non-Markovian reservoirs, feedback, filters, or parallel applications. The sorted permutation need not be a unique *negativity* optimizer on an entanglement-breaking plateau. An earlier work expressing the same permutation classification in different thermal parametrization would affect the originality assessment even though no such statement was located in the sources inspected here.

## References
1. B. Aslanbaş, B. Alkan, and G. Karpat, *Entangling capability of coherently controlled quantum processes*, arXiv:2609.00168v1 (first publicly posted August 31, 2026), especially Sec. III.E and Appendix E, eqs. (178)–(181). https://arxiv.org/html/2609.00168v1
2. S. Khatri, K. Sharma, and M. M. Wilde, *Information-theoretic aspects of the generalized amplitude-damping channel*, Phys. Rev. A **102**, 012401 (2020), arXiv:1903.07747, especially Sec. IV and Choi/PPT calculation. https://arxiv.org/abs/1903.07747
3. L. Lami and V. Giovannetti, *Entanglement-Breaking Indices*, J. Math. Phys. **56**, 092201 (2015), arXiv:1411.2517, especially Secs. II–III. https://arxiv.org/html/1411.2517v4
4. S. Cuevas et al., *Amending entanglement-breaking channels via intermediate unitary operations*, Phys. Rev. A **96**, 022322 (2017). https://doi.org/10.1103/PhysRevA.96.022322
