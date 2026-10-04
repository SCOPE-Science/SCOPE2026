# Exact product-test frontier for generalized three-qubit W states
## Finding
Consider the closed generalized three-qubit W family
\[
|W(p,q,r)\rangle=\sqrt{p}\,|100\rangle+\sqrt{q}\,|010\rangle+\sqrt{r}\,|001\rangle,
\qquad p,q,r\ge 0,\qquad p+q+r=1.
\]
Let \(\omega\) be the squared maximal overlap with a fully product state and let \(P_{\mathrm{PT}}\) be the acceptance probability of the standard two-copy product test. The feasible overlap range in this family is \([4/9,1]\).

For
\[
\frac49\le\omega\le\frac12,
\]
define
\[
T(\omega)=\frac{9\omega-4+3\sqrt{\omega(9\omega-4)}}{2}.
\]
Then the exact frontier within the generalized W family is
\[
P_{\mathrm{PT}}\le \frac{8+T(\omega)^2}{12}.
\]
Equality holds exactly, up to permutation of the qubits and removable local phases, for
\[
(p,q,r)=\left(\frac{1-T}{3},\frac{2+T}{6},\frac{2+T}{6}\right),
\qquad T=T(\omega).
\]
For
\[
\frac12\le\omega\le1,
\]
the exact frontier is
\[
P_{\mathrm{PT}}\le1-\omega+\omega^2,
\]
with equality exactly, up to permutation and local phases, at
\[
(p,q,r)=(\omega,1-\omega,0).
\]

On the genuinely three-qubit low-overlap interval \([4/9,1/2)\), the W-family frontier is strictly below the dimension-free curve of Beckey, Granha Jeronimo, and Wu,
\[
1-2\omega+3\omega^2.
\]
Writing \(t=T(\omega)\), the exact deficit is
\[
\frac{(1-t)(t+2)(5t^2+5t+2)}{108(1+t)^2}>0.
\]
At the symmetric W state, \(\omega=4/9\), the W-family acceptance is \(2/3\), while the dimension-free value is \(19/27\), giving deficit \(1/27\). The deficit vanishes continuously at \(\omega=1/2\).

## Assumptions and scope
The result concerns only the closed generalized three-qubit W family above; it does not claim the exact fixed-\((2,2,2)\) frontier over all pure three-qubit states. Zero coefficients are allowed so that the family is closed and includes the bipartite boundary. The maximal product overlap is squared fidelity, matching the convention in arXiv:2607.21477 and the quantity denoted \(P_{\max}\) in arXiv:0806.1314.

For a generalized W state, the older exact geometric-overlap formula states that if the largest of \(p,q,r\) is at least \(1/2\), then \(\omega\) equals that largest probability; if all three are at most \(1/2\), then \(\omega=4R^2\), where \(R\) is the circumradius of the triangle with side lengths \(\sqrt p,\sqrt q,\sqrt r\). This published formula is used as an input.

## Proof
Set
\[
s=p^2+q^2+r^2.
\]
For a pure three-party state, the product-test identity is
\[
P_{\mathrm{PT}}=2^-3\sum_{S\subseteq\{1,2,3\}}\operatorname{Tr}(\rho_S^2).
\]
For the W family, the one-qubit reduced-state purities are \(p^2+(1-p)^2\), \(q^2+(1-q)^2\), and \(r^2+(1-r)^2\). Purity equality for complementary reductions therefore gives
\[
P_{\mathrm{PT}}=\frac{1+s}{2}.
\]
Thus maximizing acceptance at fixed \(\omega\) is exactly maximizing \(s\).

First suppose \(p,q,r\le1/2\). Heron's identity for the triangle with squared side lengths \(p,q,r\) gives
\[
16\Delta^2=1-2s.
\]
Since \(R=\sqrt{pqr}/(4\Delta)\), the published circumradius formula becomes
\[
\omega=\frac{4pqr}{1-2s}.
\]
For \(1/3\le s<1/2\), put
\[
t=\sqrt{6s-2}\in[0,1).
\]
Every real triple with sum one and this value of \(s\) can be parameterized, for some real \(\theta\), by
\[
\begin{aligned}
p&=\frac{1+t\cos\theta}{3},\\
q&=\frac{1+t\cos(\theta+2\pi/3)}{3},\\
r&=\frac{1+t\cos(\theta-2\pi/3)}{3}.
\end{aligned}
\]
Multiplying the three factors gives
\[
pqr=\frac{1-3t^2/4+(t^3/4)\cos(3\theta)}{27}
\ge \frac{(1-t)(2+t)^2}{108}.
\]
Equality holds exactly when \(\cos(3\theta)=-1\), which yields, up to permutation,
\[
(p,q,r)=\left(\frac{1-t}{3},\frac{2+t}{6},\frac{2+t}{6}\right).
\]
Because \(1-2s=(1-t^2)/3\), it follows that
\[
\omega\ge w(t):=\frac{(2+t)^2}{9(1+t)}.
\]
Moreover
\[
w'(t)=\frac{t(t+2)}{9(1+t)^2}\ge0,
\]
with strict inequality for \(t>0\). The range of \(w\) on \([0,1]\) is \([4/9,1/2]\). Solving \(w(t)=\omega\) gives
\[
t=T(\omega)=\frac{9\omega-4+3\sqrt{\omega(9\omega-4)}}{2}.
\]
Hence any state with the prescribed \(\omega\) has \(t\le T(\omega)\), and therefore
\[
P_{\mathrm{PT}}=\frac{8+t^2}{12}\le\frac{8+T(\omega)^2}{12}.
\]
The equality conditions above give the stated maximizing family. The endpoint \(t=1\) is obtained by continuity and is the state with probabilities \((0,1/2,1/2)\).

Now suppose \(\omega\ge1/2\). The generalized-W overlap formula gives, after a permutation, \(p=\omega\) and \(q+r=1-\omega\). Thus
\[
s=\omega^2+q^2+r^2\le\omega^2+(1-\omega)^2,
\]
with equality exactly when \(qr=0\). Therefore
\[
P_{\mathrm{PT}}\le1-\omega+\omega^2,
\]
and the boundary family \((\omega,1-\omega,0)\) attains equality.

Finally, on \(4/9\le\omega\le1/2\), the dimension-free theorem has \(m=2\), hence value \(1-2\omega+3\omega^2\). Substituting \(\omega=(t+2)^2/[9(t+1)]\) and subtracting the W-family frontier gives exactly
\[
\left(1-2\omega+3\omega^2\right)-\frac{8+t^2}{12}
=\frac{(1-t)(t+2)(5t^2+5t+2)}{108(1+t)^2},
\]
which is positive for \(0\le t<1\).

## Verification
The proof is analytic. The bundled script `artifacts/verify.py` checks the algebraic identities, both endpoints, the strict deficit formula, the equality family, and the claimed upper bound on deterministic random W triples. These finite checks are corroborative only and are not used to infer the universal quantifiers.

The critical nonstandard input is the exact generalized three-qubit W-state product-overlap formula. It was checked against the full arXiv text of arXiv:0806.1314, Section III, which states the circumradius branch and the largest-coefficient branch and also gives the one-parameter formula used by the equality family. The fixed-dimension motivation was checked in the full PDF of arXiv:2607.21477, whose discussion explicitly separates the fixed-local-dimension extremal problem from its dimension-free theorem.

## Relationship to prior work
Beckey, Granha Jeronimo, and Wu determine the exact product-test curve when arbitrary finite local dimensions are allowed. They explicitly note that fixing local dimensions can invalidate the matching lower construction and leaves a separate finite-dimensional extremal problem. The present result does not alter their dimension-free theorem; it solves the exact product-test/overlap Pareto problem on the canonical closed generalized three-qubit W family.

Tamaryan et al. give the exact maximal product overlap for generalized three-qubit W states, including the circumradius formula and the special two-equal-coefficient expression. They do not optimize the product-test acceptance at fixed overlap, do not derive the W-family Pareto frontier above, and do not compare that frontier with the 2026 dimension-free product-test curve.

Chen, Xu, and Zhu show that the symmetric W state is, up to local unitaries, the maximally geometrically entangled pure three-qubit state, with squared maximal product overlap \(4/9\). This makes the W family a natural low-overlap boundary family rather than an arbitrary parameter slice.

## Limitations
This is not a solution of the full fixed-\((2,2,2)\) extremal problem over all pure three-qubit states. The equality classification is within the closed generalized W family only. The originality search found no equivalent frontier, but older literature relating geometric entanglement to one-qubit linear-entropy or Meyer-Wallach measures could conceivably contain an equivalent reformulation under different terminology; no such statement was located in the inspected primary sources or targeted searches.

## References
1. J. Beckey, F. Granha Jeronimo, and P. Wu, “An Optimal Analysis of the Product Test,” arXiv:2607.21477 (first public 2026-07-23).
2. L. Tamaryan, H. Kim, E. Jung, M.-R. Hwang, D. Park, and S. Tamaryan, “Toward an understanding of entanglement for generalized n-qubit W-states,” arXiv:0806.1314; J. Phys. A 42, 475303 (2009).
3. L. Chen, A. Xu, and H. Zhu, “Computation of the geometric measure of entanglement for pure multiqubit states,” arXiv:0911.1493; Phys. Rev. A 82, 032301 (2010).
