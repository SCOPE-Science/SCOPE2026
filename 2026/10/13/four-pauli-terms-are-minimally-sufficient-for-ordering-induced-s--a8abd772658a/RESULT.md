# Four Pauli terms are minimally sufficient for ordering-induced second-order Lie–Trotter accuracy
## Finding
Let \(P,Q,R\) be Hermitian Pauli strings satisfying \(PQ=-QP\), \([P,R]=[Q,R]=0\), and suppose the four Pauli directions \(P,Q,PR,QR\) are distinct. For nonzero real \(a,b\), set
\[
H=aP+bQ+aPR+bQR=(I+R)(aP+bQ).
\]
Consider the one-pass product in which every Hamiltonian term is evolved for the full step size,
\[
S_h=e^{-ihaP}e^{-ihbQ}e^{-ihbQR}e^{-ihaPR}.
\]
Although this is the ordinary first-order Lie–Trotter construction for the displayed four-term decomposition, its actual local error is
\[
\|S_h-e^{-ihH}\|=\frac{4|ab|}{3}\sqrt{a^2+4b^2}\,|h|^3+O(|h|^4).
\]
Thus the ordering is genuinely second order. Repeating it \(r\) times with \(h=t/r\) gives
\[
\|S_{t/r}^{r}-e^{-itH}\|=O(t^3/r^2)
\]
for fixed \(t\).

Moreover, four terms are minimal for this phenomenon among nonredundant Pauli decompositions. If a Hamiltonian contains at most three distinct Pauli directions, all with nonzero coefficients, then a one-pass Lie–Trotter ordering can have vanishing quadratic BCH error only when every pair of terms commutes. Therefore no genuinely noncommuting example exists with one, two, or three distinct Pauli terms.

A concrete two-qubit instance is obtained from \(P=X\otimes I\), \(Q=Y\otimes I\), and \(R=I\otimes Z\). The four terms are then \(XI,YI,XZ,YZ\), and the ordering \(XI,YI,YZ,XZ\) has exact cancellation of its quadratic BCH commutator sum.
## Assumptions and scope
A Pauli direction means a tensor-product Pauli operator modulo an overall scalar sign; repeated directions are first combined into a single Hamiltonian term. The minimality statement assumes distinct nonzero Pauli directions and nonzero real coefficients. It concerns a single deterministic one-pass Lie–Trotter sweep in which each term appears once with its full step duration. It does not address randomized mixtures, linear combinations of circuits, negative-time formulas, formulas with repeated factors, or state-dependent/observable-dependent error.

The construction is not claimed to be generic. It is a structured algebraic family showing that ordering can raise the actual order of a nominal first-order Pauli product formula.
## Proof
Because \(R\) commutes with \(P\) and \(Q\), the Hilbert space decomposes into the \(R=+1\) and \(R=-1\) eigenspaces. On the positive sector,
\[
H_+=2(aP+bQ),
\]
and the product reduces exactly to
\[
(S_h)_+=e^{-ihaP}e^{-i2hbQ}e^{-ihaP},
\]
which is the symmetric Strang splitting for \(H_+\). On the negative sector,
\[
H_-=0,
\]
and
\[
(S_h)_-=e^{-ihaP}e^{-ihbQ}e^{+ihbQ}e^{+ihaP}=I.
\]
Therefore the full local error is exactly the positive-sector Strang error, proving \(O(h^3)\) local accuracy.

The order is genuinely two rather than higher. Using only \(P^2=Q^2=I\) and \(PQ=-QP\), direct Taylor expansion on the positive sector gives
\[
(S_h)_+-e^{-ihH_+}
=
\frac{4iab}{3}(2bP-aQ)h^3+O(h^4).
\]
Since \((2bP-aQ)^2=(a^2+4b^2)I\), its spectral norm is
\[
\frac{4|ab|}{3}\sqrt{a^2+4b^2}\,|h|^3+O(|h|^4),
\]
which is nonzero for \(ab\ne0\).

For the repeated formula, write \(h=t/r\). Unitarity and telescoping imply
\[
\|S_h^r-e^{-irhH}\|\le r\|S_h-e^{-ihH}\|,
\]
so the cubic one-step bound yields \(O(t^3/r^2)\).

It remains to prove minimality. For a one-pass product of distinct Pauli directions \(P_1,\ldots,P_m\) with coefficients \(c_j\), the degree-two BCH term is, up to an overall nonzero scalar,
\[
\sum_{i<j} \epsilon_{ij}c_ic_j[P_i,P_j],
\]
where each \(\epsilon_{ij}\in\{+1,-1\}\) is determined by the ordering. A commuting pair contributes zero. An anticommuting pair contributes a nonzero multiple of the Pauli direction \(P_iP_j\).

When \(m\le3\), any two different unordered pairs share an index. If two corresponding Pauli products were proportional, for example \(P_iP_j\propto P_iP_k\), multiplication by \(P_i\) would force \(P_j\propto P_k\), contradicting distinctness. Hence all nonzero commutator directions are distinct Pauli directions and are Hilbert–Schmidt orthogonal. They cannot cancel. Thus the quadratic BCH term vanishes only if there are no anticommuting pairs at all, in which case the terms commute and the product is exact. The four-term construction above therefore attains the smallest possible noncommuting term count.
## Verification
The analytic proof uses only Pauli multiplication, the two eigenspaces of a commuting involution, the standard symmetric Strang identity, and the degree-two BCH term. No finite experiment is used to establish the infinite statement.

The accompanying checker uses the explicit realization \(P=X\otimes I\), \(Q=Y\otimes I\), \(R=I\otimes Z\). It verifies the algebraic assumptions, exact cancellation of the quadratic commutator sum for the ordering \(P,Q,QR,PR\), the positive/negative sector identities, the predicted nonzero cubic coefficient, and the \(r^{-2}\) repeated-step scaling numerically. These calculations are corroborative only.
## Relationship to prior work
Liu, Wei, Foss-Feig, Gorshkov, and Childs introduced an ordering-aware theory of Trotter error and emphasized that term ordering can strongly change finite-step error; their framework keeps cancellations that separate commutator bounds can lose. The inspected full text treats general ordering-sensitive bounds and optimization, primarily for Suzuki formulas on local chains, but does not state a deterministic four-Pauli one-pass order elevation or a sharp minimal term count.

Layden related repeated first-order Trotter circuits with two Hamiltonian blocks to second-order formulas and explained anomalously favorable global regimes. That result retains a boundary contribution for the generic first-order circuit and does not make a single one-pass first-order step locally cubic. Childs and Su proved ordering robustness of asymptotic first-order bounds for nearest-neighbor lattice Hamiltonians, while Childs, Ostrander, and Su used randomization of orderings to improve simulation bounds. None of these inspected results implies the present exact deterministic Pauli-sector construction or the three-versus-four minimality theorem.
## Limitations
The result is an existence and minimality theorem for nonredundant Pauli decompositions, not a claim that useful physical Hamiltonians generically admit such an ordering. The four-term family has a commuting involution \(R\) that makes the mechanism transparent, and additional constraints such as geometric locality, hardware connectivity, prescribed coefficient patterns, or translation invariance can rule out the construction. The theorem also does not characterize all four-term Pauli decompositions whose quadratic BCH term cancels.

A residual originality risk remains that abstract operator-splitting literature may contain the general observation that algebraic dependence among commutators can raise the realized order of a nominal Lie product. The specific Pauli minimality statement and the displayed sector-exact family were not found in the inspected sources or searches.
## References
1. Z. Liu, Z.-Y. Wei, M. Foss-Feig, A. V. Gorshkov, and A. M. Childs, “Ordering-Aware Theory of Trotter Error,” arXiv:2610.03672v1 (2026).
2. D. Layden, “First-Order Trotter Error from a Second-Order Perspective,” arXiv:2107.08032; Physical Review Letters 128, 210501 (2022).
3. A. M. Childs and Y. Su, “Nearly Optimal Lattice Simulation by Product Formulas,” arXiv:1901.00564; Physical Review Letters 123, 050503 (2019).
4. A. M. Childs, A. Ostrander, and Y. Su, “Faster Quantum Simulation by Randomization,” arXiv:1805.08385; Quantum 3, 182 (2019).
