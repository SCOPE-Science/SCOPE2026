# Exact reentrant amplification window for maximal steered coherence in separable prolate qubit states

## Finding

For every parameter triple in the domain below, Bob's amplitude-damping channel has an **exactly determined** effect on maximal steered \(l_1\)-coherence. Let \(C_{\max}(\gamma)\) denote the maximal \(l_1\)-coherence of Bob's state conditioned on any nonzero-probability POVM outcome on Alice, measured in the eigenbasis of Bob's **post-channel, pre-steering** reduced state.

With \(q=1-\gamma\), the complete response law is
\[
C_{\max}(\gamma)^2=\max\left\{q\kappa^2,\ \frac{q\gamma^2\tau^2+q^3\beta^2\kappa^2}{\gamma^2+q\beta^2}\right\},\qquad 0\le\gamma\le1.
\]
In particular, \(C_{\max}(0)=\kappa\). Strict enhancement above this initial value occurs for at least one damping strength **if and only if**
\[
\boxed{\tau^2>\kappa^2(1+\beta^2+2\sqrt2\,\beta).}
\]
When the inequality holds, the entire enhancement set is the unique open interval \(\gamma_-<\gamma<\gamma_+\), where
\[
\gamma_\pm=\frac{\tau^2-\kappa^2+3\beta^2\kappa^2\pm\sqrt{\Delta}}{2(\tau^2+\beta^2\kappa^2)},
\quad
\Delta=(\tau^2-\kappa^2(1+\beta^2))^2-8\beta^2\kappa^4,
\quad 0<\gamma_-<\gamma_+<1.
\]
For parameter triples not meeting the strict inequality, \(C_{\max}(\gamma)\le C_{\max}(0)\) throughout. The initial states are all separable, so entanglement is not needed for this strictly nonmonotonic steered-coherence response.

## Assumptions and scope

The systems are qubits A and B, with conventional Pauli matrices \(\sigma_x,\sigma_y,\sigma_z\). Fix
\[
0<\beta<1,\qquad 0<\kappa<\tau,\qquad 1-\tau\ge\sqrt{\beta^2+4\kappa^2},
\]
and define
\[
\rho_{\beta,\kappa,\tau}=\frac14\bigl(I\otimes I+\beta I\otimes\sigma_x+
\tau\sigma_x\otimes\sigma_x+
\kappa\sigma_y\otimes\sigma_y+
\kappa\sigma_z\otimes\sigma_z\bigr).
\]
Alice's marginal is \(I/2\); Bob's Bloch vector is \((\beta,0,0)\), which is nonzero. Bob's standard amplitude-damping operation in the \(\sigma_z\) basis has Kraus operators
\[
K_0=\operatorname{diag}(1,\sqrt{1-\gamma}),\qquad
K_1=\sqrt\gamma\,|0\rangle\langle1|,\qquad 0\le\gamma\le1.
\]
The quantity optimized is **maximal steered coherence**, not measurement-averaged coherence, entanglement, discord, or a coherence measured in a fixed laboratory basis. The eigenbasis defining coherence is recomputed from Bob's post-channel marginal at each \(\gamma\).

## Proof

**1. Physicality and separability.** Rotate the local axes on both qubits so that the original \(x\) axes become \(z\) axes. The spectrum of the state comprises
\[
\frac{1+\tau\pm\beta}{4},\qquad
\frac{1-\tau\pm\sqrt{\beta^2+4\kappa^2}}4.
\]
These are nonnegative by the domain inequalities. In the rotated basis, its partial transpose has spectrum
\[
\frac{1-\tau\pm\beta}{4},\qquad
\frac{1+\tau\pm\sqrt{\beta^2+4\kappa^2}}4,
\]
which is also nonnegative. The two-qubit positive-partial-transpose criterion proves the states are separable.

**2. Exact maximization over Alice's POVMs.** With Alice marginal maximally mixed, an arbitrary nonzero Alice effect proportional to \(I+\mathbf m\cdot\boldsymbol\sigma\), \(\|\mathbf m\|\le1\), steers Bob to Bloch vector \(\mathbf b+T\mathbf m\), where \(\mathbf b=(\beta,0,0)\) and \(T=\operatorname{diag}(\tau,\kappa,\kappa)\). Every such effect is physically available after harmless scaling. For a qubit with Bloch vector \(\mathbf r\), \(l_1\)-coherence in the eigenbasis of a nondegenerate reference Bloch vector \(\mathbf b\) equals \(\|P_{\mathbf b^\perp}\mathbf r\|_2\), with \(P_{\mathbf b^\perp}=I-\hat{\mathbf b}\hat{\mathbf b}^{\mathsf T}\). Thus, for this family, the full POVM maximum is the operator norm of \(P_{\mathbf b^\perp}T\), attained on \(\|\mathbf m\|=1\).

Under Bob's amplitude damping, \(q=1-\gamma\), the Bloch data become
\[
\mathbf b_\gamma=(\sqrt q\,\beta,0,\gamma),\qquad
T_\gamma=\operatorname{diag}(\sqrt q\,\tau,\sqrt q\,\kappa,q\kappa).
\]
Bob's reference vector never vanishes on the stated domain. Writing \(N=\gamma^2+q\beta^2>0\), an orthonormal basis perpendicular to \(\mathbf b_\gamma\) is
\[
\mathbf e_y=(0,1,0),\qquad
\mathbf e_{xz}=N^{-1/2}(\gamma,0,-\sqrt q\,\beta).
\]
The two row vectors of the projected correlation operator are orthogonal. Their squared lengths, exactly its two nonzero squared singular values, are
\[
q\kappa^2\quad\text{and}\quad
\frac{q\gamma^2\tau^2+q^3\beta^2\kappa^2}{\gamma^2+q\beta^2}.
\]
Their maximum proves the full response law, including both channel endpoints. Initially the two transverse singular values both equal \(\kappa\).

**3. Sharp reentrant window.** For \(0<\gamma\le1\), the first singular-value branch is strictly below \(\kappa^2\). Subtracting \(\kappa^2\) from the second branch gives
\[
\frac{\gamma P(\gamma)}{\gamma^2+(1-\gamma)\beta^2},\quad
P(\gamma)=-(\tau^2+\beta^2\kappa^2)\gamma^2+
(\tau^2-\kappa^2+3\beta^2\kappa^2)\gamma-2\beta^2\kappa^2.
\]
The quadratic is strictly concave, \(P(0)=-2\beta^2\kappa^2<0\), and \(P(1)=-\kappa^2<0\). Its vertex lies strictly inside \((0,1)\): the vertex numerator is positive because \(\tau>\kappa\), and its difference from twice the positive leading magnitude is \((\beta^2-1)\kappa^2-\tau^2<0\). Its discriminant factors as
\[
\Delta=\bigl[\tau^2-\kappa^2(1+\beta^2+2\sqrt2\,\beta)\bigr]
\bigl[\tau^2-\kappa^2(1+\beta^2-2\sqrt2\,\beta)\bigr].
\]
The second factor is positive because \(\tau^2>\kappa^2\) and \(\beta<1<2\sqrt2\). Hence the vertex has positive height precisely under the displayed strict threshold. In that case both roots lie strictly in \((0,1)\), and solving the quadratic gives exactly \(\gamma_\pm\). If the discriminant vanishes the graph only touches its initial level, with no strict gain; otherwise there is no gain. This proves the claimed necessary and sufficient condition and the unique reentrant enhancement interval.

**4. Explicit separable witness.** Choose \((\beta,\kappa,\tau)=(1/4,1/8,1/2)\). The state is positive and PPT because \(1-\tau=1/2>\sqrt{(1/4)^2+4(1/8)^2}=\sqrt2/4\). Here the enhancement polynomial is \(P(\gamma)=-(257\gamma^2-243\gamma+2)/1024\), whose roots are \((243\pm\sqrt{56993})/514\). At \(\gamma=1/2\) the second squared singular value equals \(257/2304\), exceeding the original \(1/64\); thus \(C_{\max}(1/2)=\sqrt{257}/48>1/8=C_{\max}(0)\).

## Verification

The standalone file `verify.py` uses only the Python standard library. It recomputes the channel by Kraus multiplication, the conditional Bob density matrix from Alice projectors, and the coherence in Bob's reduced-state eigenbasis; it compares these direct calculations with both analytic singular-value branches for 32 physically admissible cases. Exact rational arithmetic independently reproduces the witness's response-square, polynomial, and discriminant. The reproducible terminal result is `VERIFY_OK exact_fraction_witness=passed direct_kraus_steering_cases=32 boundary=passed`. Finite test cases corroborate, but do not substitute for, the analytic proof above.

## Relationship to prior work

Hu, Milne, Zhang, and Fan introduced maximal steered coherence, derived its general steering-ellipsoid geometry, proved a criterion for **whether a channel can enhance it for some state**, and showed numerical damping curves for prolate two-qubit states (their Figure 2 and Theorem 1). The present result instead supplies a sharp **statewise** criterion, the full exact channel-response law, and two algebraic endpoints for **every** member of a continuous, explicitly separable, three-parameter prolate family. The underlying general geometric optimization principle is prior work; its evaluated statewise threshold is the result established here. Hu and Fan's earlier local-channel steering-ellipsoid work concerns quantum discord. Their later work on steering-induced coherence optimizes measurement-averaged rather than single-outcome maximal coherence. Later studies of squeezed, memory-bearing generalized amplitude-damping channels emphasize Bell-state inputs and distinct noise families.

## Limitations

No extension is claimed to arbitrary two-qubit inputs with a nonmaximally mixed Alice marginal, to arbitrary local qubit channels, to generalized finite-temperature damping, or to measurement-averaged coherence. The proof does not establish literature-wide uniqueness: a differently parameterized or less readily indexed derivation of the same special-case threshold may exist. The inequality at the critical surface allows equality with the original coherence at one interior damping value, not strict enhancement. The endpoint \(\gamma=1\) is well-defined and has zero coherence.

## References

- X. Hu, A. Milne, B. Zhang, and H. Fan, *Quantum coherence of steered states*, arXiv:1507.02358 (first public 2015-07-09); *Scientific Reports* **6**, 19365 (2016), DOI 10.1038/srep19365. Open full text: https://www.nature.com/articles/srep19365 .
- X. Hu and H. Fan, *Effect of local channels on quantum steering ellipsoids*, arXiv:1411.7449; *Physical Review A* **91**, 022301 (2015), DOI 10.1103/PhysRevA.91.022301.
- X. Hu and H. Fan, *Extracting quantum coherence via steering*, *Scientific Reports* **6**, 34380 (2016), DOI 10.1038/srep34380.
- Y.-T. Lan and M.-L. Hu, *Protecting steered coherence in squeezed generalized amplitude damping channel with memory*, *Results in Physics* **54**, 107050 (2023), DOI 10.1016/j.rinp.2023.107050.
