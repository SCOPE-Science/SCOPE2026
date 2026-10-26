# Two sharp flip thresholds and a resonant circle in two-token self-attention

## Finding

Consider the two-token normalized residual self-attention dynamics in the next section. Its positive-eigenvector consensus loses hyperbolic attraction at the sharp step-size threshold
\[
\eta_c=\frac{2}{M-\lambda}.
\]
Beyond it, a synchronized negative-eigenvector sign-flip orbit becomes a hyperbolic sink. An antipodal negative-eigenvector flip orbit becomes a second, distinct hyperbolic sink exactly when \(qM>\lambda\) and
\[
\eta>\eta_a=\frac{2}{qM-\lambda},\qquad q=\tanh\kappa.
\]
The second threshold strictly exceeds the first. At the first threshold the complete diagonal circle consists of fixed points and genuine period-two points, with the second iterate uniformly contracting the transverse direction. All statements concern the specified configurations and their local dynamics; no census of all attractors is asserted.

## Assumptions and scope

Let \(\lambda>0\), \(M>\lambda\), \(\kappa>0\), and \(\eta>0\). Set \(V=\operatorname{diag}(\lambda,-M)\), \(q=\tanh\kappa\in(0,1)\), and let \(x_1,x_2\in\mathbb S^1\subset\mathbb R^2\) be labeled unit vectors. The full, self-including attention weights and residual-normalized update are
\[
a_{ij}(x)=\frac{\exp(\kappa\langle x_i,x_j\rangle)}{\exp(\kappa\langle x_i,x_1\rangle)+\exp(\kappa\langle x_i,x_2\rangle)},\qquad
F_\eta(x)_i=\frac{z_i(x)}{\|z_i(x)\|},\quad
z_i(x)=x_i+\eta V\sum_{j=1}^2a_{ij}(x)x_j.
\]
The map is defined wherever both \(z_i\) are nonzero; all named orbits have a smooth neighborhood of definition. Write \(e_1=(1,0)\), \(e_2=(0,1)\), and
\[
\mathcal S=\{(e_2,e_2),(-e_2,-e_2)\},\qquad
\mathcal A=\{(e_2,-e_2),(-e_2,e_2)\}.
\]
A *hyperbolic attracting two-cycle* means a two-point orbit whose return derivative has all multipliers strictly inside the open unit disk. At a threshold no hyperbolic-attraction claim is made.

The complete canonical phase statements are:

1. Both positive-axis consensus points \((e_1,e_1)\) and \((-e_1,-e_1)\) are fixed. Their one-step tangent multipliers are \((1-\eta M)/(1+\eta\lambda)\) and \(1/(1+\eta\lambda)\). They are hyperbolic sinks exactly when \(0<\eta<\eta_c\); for \(\eta>\eta_c\), each has an expanding tangent direction.
2. The pair \(\mathcal S\) is a genuine two-cycle for \(\eta>1/M\). Its return multipliers are
\[
\left(\frac{1+\eta\lambda}{\eta M-1}\right)^2,\qquad\frac{1}{(\eta M-1)^2}.
\]
It is hyperbolically attracting exactly when \(\eta>\eta_c\), and has an expanding direction for \(1/M<\eta<\eta_c\).
3. The pair \(\mathcal A\) is a genuine two-cycle for \(\eta>1/(qM)\). Its return multipliers are
\[
\left(\frac{1+\eta\lambda}{\eta qM-1}\right)^2,\qquad
\left(\frac{1+\eta q\lambda}{\eta qM-1}\right)^2.
\]
It is hyperbolically attracting exactly if \(qM>\lambda\) and \(\eta>\eta_a\). Otherwise, throughout its strict existence range outside the threshold, it has a multiplier greater than one. When \(qM>\lambda\), \(\eta_a>\eta_c\), and \(\mathcal S\) and \(\mathcal A\) have disjoint open local attraction basins for every \(\eta>\eta_a\).
4. At \(\eta=\eta_c\), the synchronized diagonal circle \(\mathcal D=\{(x,x):x\in\mathbb S^1\}\) satisfies \(F_\eta(x,x)=(Rx,Rx)\), with \(R=\operatorname{diag}(1,-1)\), so \(F_\eta^2\) fixes \(\mathcal D\) pointwise. Only \((\pm e_1,\pm e_1)\) are fixed by one step on \(\mathcal D\); all other points are of least period two. Set \(A=(M+\lambda)/(M-\lambda)\). At \(x=(\cos\theta,\sin\theta)\), the derivative of the second iterate has tangential and normal eigenvalues \(1\) and \(\cos^2(2\theta)/A^2\), respectively. Thus the full circle is normally attracting with a uniform transverse bound \(A^{-2}<1\).

In particular, with \(\lambda=1\), \(M=4\), \(\kappa=(\log3)/2\), and \(\eta=3\), both two-cycles are hyperbolic sinks: \(\mathcal S\) has return multipliers \(16/121,1/121\), whereas \(\mathcal A\) has \(16/25,1/4\).

## Proof

**Softmax differentials at collinear tokens.** If every token is parallel or antiparallel to the same unit vector \(e\), then its infinitesimal tangent perturbations are perpendicular to \(e\). Consequently every first derivative of every dot product \(\langle x_i,x_j\rangle\) vanishes. The attention weights therefore have zero first variation at each named configuration. For synchronized tokens the attention matrix is \(P=\tfrac12\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\), with eigenvalues \(1,0\). For antipodal tokens it is \(P_q=\tfrac12\begin{psmallmatrix}1+q&1-q\\1-q&1+q\end{psmallmatrix}\), with eigenvalues \(1,q\). Indeed \(q=(e^\kappa-e^{-\kappa})/(e^\kappa+e^{-\kappa})=\tanh\kappa\).

**Positive-axis consensus.** At \((\pm e_1,\pm e_1)\) the unnormalized vector is \((1+\eta\lambda)(\pm e_1)\); its norm is \(1+\eta\lambda\). The tangent direction is \(e_2\). Using the vanishing attention variation, the linearized update on the two tangent coefficients is \((I-\eta M P)/(1+\eta\lambda)\). Hence the eigenvalues are \((1-\eta M)/(1+\eta\lambda)\) and \(1/(1+\eta\lambda)\). The latter is always strictly between zero and one; the former has modulus below one exactly when \(\eta(M-\lambda)<2\). This proves the first phase boundary and the instability beyond it.

**Synchronized sign flip.** At either point of \(\mathcal S\), the unnormalized vector is \((1-\eta M)x_i\). If \(\eta M>1\), normalization changes its sign. The tangent direction is the horizontal \(e_1\) line; the one-step tangent coefficients are acted on by \((I+\eta\lambda P)/(\eta M-1)\) in an ambient horizontal frame. The same matrix applies at the other endpoint. Thus the two-step multipliers are the squares of \((1+\eta\lambda)/(\eta M-1)\) and \(1/(\eta M-1)\). Since the former dominates the latter, both are below one exactly when \(\eta M-1>1+\eta\lambda\), equivalently \(\eta>\eta_c\). When the inequality is reversed, the first multiplier is greater than one.

**Antipodal sign flip.** At either point of \(\mathcal A\), the attention-weighted mean equals \(qx_i\). The unnormalized vector is \((1-\eta qM)x_i\). Hence the configuration switches endpoints of \(\mathcal A\) precisely when \(\eta qM>1\). Horizontal tangent perturbations are governed by \((I+\eta\lambda P_q)/(\eta qM-1)\), again identical at both endpoints. Its eigenvalues are \((1+\eta\lambda)/(\eta qM-1)\) and \((1+\eta q\lambda)/(\eta qM-1)\); squaring proves the stated Floquet spectrum. The first is strictly larger and positive, so strict attraction is equivalent to \(\eta qM-1>1+\eta\lambda\). This can hold precisely if \(qM>\lambda\), and then is equivalent to \(\eta>2/(qM-\lambda)\). Finally \(q<1\) gives \(\eta_a>\eta_c\). Smoothness near the two hyperbolic orbits and the return-map contraction theorem yield separate open attraction neighborhoods.

**Resonant circle.** At synchronized configurations the update is independent of attention sharpness: \(F_\eta(x,x)=(Bx/\|Bx\|,Bx/\|Bx\|)\) for \(B=I+\eta V\). At \(\eta=\eta_c\), direct substitution gives \(B=A R\) with \(A=(M+\lambda)/(M-\lambda)>1\) and \(R=\operatorname{diag}(1,-1)\). Since \(R^2=I\), the entire diagonal circle is fixed under two steps, and the stated fixed/period-two distinction follows.

For the return derivative, split tangent perturbations at \((x,x)\) into synchronized and antisynchronized components. A synchronized component is tangent to \(\mathcal D\); as the restriction of \(F_\eta^2\) is the identity, its return multiplier is \(1\). For an antisynchronized component, the attention-weighted mean has zero first variation, so the first-step derivative is projection of its tangent vector onto \(T_{Rx}\mathbb S^1\), divided by \(A\). Writing \(x=(\cos\theta,\sin\theta)\), the corresponding unit tangent vectors have inner product \(\cos(2\theta)\). At the second step the same factor recurs (with angle \(-\theta\)), yielding normal return multiplier \(\cos^2(2\theta)/A^2\). Because this is uniformly less than one, \(\mathcal D\) is normally attracting. This is a statement of transverse contraction, not convergence to a single point of the circle.

## Verification

Run `python3 verify.py` in a directory containing the two bundled verification files. The checker independently implements the full softmax map in angular variables, uses central differences to test one- and two-step Jacobian eigenvalues over multiple parameter sets, tests the resonant-circle identities at fifty-seven distinct parameter-angle cases, and checks an explicit co-attracting example using exact rational fractions. Its output is in `verification_output.txt`. This finite numerical verification supplements, but cannot replace, the parameter-uniform proof above. The Python standard library suffices.

## Relationship to prior work

Altafini (2026), arXiv:2610.13518v1, defines the normalized residual discrete self-attention dynamics, gives a broad equilibrium classification, and studies local equilibrium stability under principal-positive-eigenvalue assumptions. The elementary consensus linearization belongs to that framework. It does not give the two simultaneous sign-flip attractors, the separate softmax-dependent antipodal threshold, or the neutral resonant circle of this explicit two-token indefinite-value system.

Gao, Yang and Chen (2026), arXiv:2609.28448v1, analyze period-two and cluster-flip behavior for an *isotropic negative* value matrix, primarily with diagonal-masked self-attention. Their Section V A also gives an aligned-cluster linear spectral-selection formula for general matrices and an invariant-subspace reduction. That prior formula already anticipates the synchronized flipping branch as a special case. Neither their general discussion nor the inspected primary results give the sharp transverse stability of both flipping patterns under *full self-including* softmax and a *mixed-sign* value matrix. In particular the distinct threshold involving \(\tanh\kappa\) and the normally attracting resonance circle are not stated there. The result does not claim that the general normalization mechanism or the existence of flipping orbits is new.

## Limitations

The map may be undefined at other inputs for which an unnormalized update vanishes. The theorem applies locally to the specified fixed points, two-cycles, and invariant synchronized circle. It does not classify all periodic or chaotic attractors or their global basins; it does not assert attracting behavior at the nonhyperbolic threshold itself. It is a two-token, two-dimensional single-head model with fixed matrices, not a theorem about trained transformers or arbitrary attention kernels. Historical priority beyond the inspected sources requires independent literature assessment.

## References

1. Claudio Altafini, *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers*, arXiv:2610.13518v1 (first posted 9 October 2026), https://arxiv.org/abs/2610.13518.
2. Qucheng Gao, Zuyi Yang, and Xiao Chen, *Nonequilibrium Phases of Repulsive Self-Attention: Chaos, Attention Condensation, and Emergent Locality*, arXiv:2609.28448v1 (first posted 23 September 2026), https://arxiv.org/abs/2609.28448.
