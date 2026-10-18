# A sharp attention-temperature threshold for coexisting attracting two-cycles

## Finding
Consider the two-token, full-softmax, residual and sphere-normalized discrete self-attention map defined below. For a value matrix with one positive and one larger-magnitude negative eigenvalue, there are two distinct exact period-two cycles: a synchronized sign flip and an antipodal sign flip. The antipodal flip is hyperbolically attracting **if and only if** its sharpness and step size satisfy
\[
 b\tanh\alpha>a,\qquad \eta>\frac{2}{b\tanh\alpha-a}.
\]
Whenever these inequalities hold, the synchronized flip is also hyperbolically attracting, giving two disjoint open basins of period-two attraction for the same fully self-inclusive attention map. Conversely, among parameters where the antipodal flip exists, its linearization is unstable whenever these strict inequalities fail, except at the stated equality boundary, where the return map has a unit multiplier and nonlinear stability is not decided here.

For fixed \(\eta>2/(b-a)\), the onset of this second attracting cycle occurs at the explicit softmax threshold
\[
 \alpha_c(\eta)=\operatorname{artanh}\!\left(\frac{a+2/\eta}{b}\right).
\]
The antipodal flip is hyperbolically attracting precisely for \(\alpha>\alpha_c(\eta)\). In contrast, the existence and hyperbolic stability of the synchronized flip do not depend on \(\alpha\).

## Assumptions and scope
Take two labeled tokens \(x_1,x_2\) on the Euclidean unit circle \(\mathbb S^1\), positive constants \(0<a<b\), attention inverse temperature \(\alpha>0\), and discrete step size \(\eta>0\). Let
\[
 V=\begin{pmatrix}a&0\\0&-b\end{pmatrix},\quad
 Q=K=\sqrt\alpha\,I_2,\quad
 A_{ij}(x)=\frac{\exp(\alpha\langle x_i,x_j\rangle)}{\exp(\alpha\langle x_i,x_1\rangle)+\exp(\alpha\langle x_i,x_2\rangle)},
\]
and define the map, whenever its normalization denominators are nonzero, by
\[
 T_i(x)=\frac{x_i+\eta V\sum_{j=1}^2 A_{ij}(x)x_j}{\left\|x_i+\eta V\sum_{j=1}^2 A_{ij}(x)x_j\right\|},\qquad i=1,2.
\]
Every token attends to **both** itself and the other token. Write \(e=(0,1)\), \(u=(1,0)\), and \(t=\tanh\alpha\in(0,1)\). The two candidate labeled period-two cycles are
\[
 C=\{(e,e),(-e,-e)\},\qquad B=\{(e,-e),(-e,e)\}.
\]
These are distinct subsets of \((\mathbb S^1)^2\), even after identifying a global sign or swapping token labels. Local hyperbolic attraction means both eigenvalues of the derivative of \(T^2\) in the two-dimensional tangent space have modulus strictly less than one. Claims concern local, not global, basins; there may be other attractors. The map need only be defined in neighborhoods of these cycles.

## Proof
**Step 1 (exact cycles).** At the synchronized configuration, every attention weight equals \(1/2\), and the pre-normalization vector of either token is \((1-\eta b)e\), or its global negative. Thus \(C\) is a genuine two-cycle if and only if \(\eta b>1\); it is undefined at \(\eta b=1\) and fixed for \(\eta b<1\).

At \((e,-e)\) the attention matrix is
\[
 A=\begin{pmatrix}p&1-p\\1-p&p\end{pmatrix},\qquad p=\frac{1+t}{2}.
\]
The attention-weighted token averages are \(t e\) and \(-t e\). Therefore the two pre-normalization vectors are \((1-\eta bt)e\) and its negative. Hence \(B\) is a genuine two-cycle exactly when \(\eta bt>1\); at equality its normalization vanishes, and below equality the two configurations are fixed rather than alternating.

**Step 2 (tangent linearization).** At any configuration \((\pm e,\pm e)\), every first derivative of the score \(\alpha\langle x_i,x_j\rangle\) vanishes on \(T_{(x_1,x_2)}(\mathbb S^1)^2\): a tangent perturbation is parallel to \(u\) and orthogonal to both base vectors. Consequently the first variation of every softmax weight vanishes. The first variations of the pre-normalization vectors, in the common tangent-coordinate basis \((u,u)\), are found by retaining just the explicit perturbed token vectors.

For a nonzero vector \(c e\), the derivative of normalization \(z\mapsto z/\|z\|\) on vectors parallel to \(u\) is multiplication by \(1/|c|\). Accordingly, in the flip regime the one-step tangent Jacobians at both points in the respective cycles are
\[
 J_B=\frac{1}{\eta bt-1}\begin{pmatrix}
 1+\eta ap&\eta a(1-p)\\
 \eta a(1-p)&1+\eta ap
 \end{pmatrix},\qquad
 J_C=\frac{1}{\eta b-1}\begin{pmatrix}
 1+\eta a/2&\eta a/2\\
 \eta a/2&1+\eta a/2
 \end{pmatrix}.
\]
These matrices are identical at the two points along each flip cycle, because simultaneous token sign reversal preserves dot-product attention and the underlying map is odd. Thus the two-step tangent derivatives are \(J_B^2\) and \(J_C^2\), respectively.

**Step 3 (sharp Floquet inequalities).** The symmetric and antisymmetric tangent modes diagonalize these matrices. The respective one-step eigenvalues are
\[
 \mu_{B,+}=\frac{1+\eta a}{\eta bt-1},\qquad
 \mu_{B,-}=\frac{1+\eta at}{\eta bt-1};\qquad
 \mu_{C,+}=\frac{1+\eta a}{\eta b-1},\qquad
 \mu_{C,-}=\frac{1}{\eta b-1}.
\]
Each displayed eigenvalue is positive in the pertinent flip regime, and the plus eigenvalue is the larger. Hence both Floquet multipliers \(\mu_{B,\pm}^2\) are smaller than one precisely when \(1+\eta a<\eta bt-1\), which is equivalent to \(bt>a\) and \(\eta>2/(bt-a)\). For the synchronized cycle the corresponding criterion is \(b>a\) and \(\eta>2/(b-a)\). If the respective leading eigenvalue exceeds one, that two-cycle is unstable. At equality the leading two-step multiplier is exactly one, so no assertion about nonlinear asymptotic stability is made.

Finally \(0<t<1\) implies \(bt-a<b-a\). Thus the strict antipodal-attraction criterion implies the synchronized-attraction criterion. At fixed \(\eta>2/(b-a)\), the antipodal condition is \(\tanh\alpha>(a+2/\eta)/b\), giving the stated sharp \(\alpha_c\). The usual local stable fixed-point theorem applied to \(T^2\) gives open neighborhoods attracted to each cycle. Distinctness and local attraction give disjoint subneighborhoods of the two basins.

## Verification
The self-contained standard-library program `attention_flip_check.py` computes the exact formulas above and compares them to independent central-difference derivatives of the full softmax update for 32 parameter/configuration tests. It also advances nearby initial conditions for 240 steps at the two cycles. Run `python attention_flip_check.py` using Python 3.9 or later. It returns `PASS` on successful checks.

For the reproducible choice \(a=1\), \(b=2\), \(\alpha=1\), \(\eta=10\), the largest one-step multipliers are approximately \(0.77291247\) for \(B\) and \(0.57894737\) for \(C\). The antipodal critical step at this sharpness is approximately \(3.82271537\), while the sharp critical value for \(\eta=10\) is \(\alpha_c=\operatorname{artanh}(3/5)=0.69314718\ldots\). The limiting necessary sharpness floor as \(\eta\to\infty\) is \(\operatorname{artanh}(1/2)=0.54930614\ldots\). These finite tests corroborate, but do not replace, the all-parameter tangent calculation.

## Relationship to prior work
Altafini (2026, arXiv:2610.13518v1) introduces the full, self-inclusive sphere-normalized discrete self-attention map and derives equilibrium and Jacobian stability results, with step restrictions used for bipartite equilibria. Its Lemma 14 treats the regime \(\eta<\min(1/a,1/b)\), which is disjoint from the attracting flip regime above; neither the two exact flipping cycles nor their coexistence phase boundary is stated there.

Gao, Yang and Chen (2026, arXiv:2609.28448v1) analyze flip dynamics with repulsive scalar value map, but explicitly mask the self-attention diagonal \(A_{ii}=0\). Their model and the resulting consensus flip do not imply this sharp temperature-dependent attracting **antipodal** flip under fully self-inclusive attention with an indefinite value matrix. Altafini (2025, arXiv:2511.11553v1) analyzes the continuous-time Oja/self-attention flow, for which the present finite-step sign-reversal mechanism is not a flow equilibrium classification.

The two-cycle stability thresholds here are deduced from the actual two-step map at sign-reversing configurations, not from stability of fixed points. Searches of published records for normalized self-attention, large-step antipodal flipping, and bistability found no covering same-model statement; the absence of a match is not proof of worldwide uniqueness.

## Limitations
The result classifies local hyperbolicity of **two explicit cycles** only, not every periodic orbit of the map and not the global phase portrait. At the threshold equality the linearization has a neutral multiplier, so nonlinear attraction at equality remains undetermined. At the parameters where a normalization denominator vanishes the map is undefined at the relevant state. The model is intentionally minimal (two tokens, unit-circle states, diagonal symmetric value matrix, isotropic query/key matrices); extensions to arbitrary matrices and many tokens are not claimed. Independent audit has not been performed.

## References
1. C. Altafini, *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers*, arXiv:2610.13518v1 (first public 2026-10-09), https://arxiv.org/html/2610.13518v1 . Relevant material: Sections II, IV-B and V-B.
2. Q. Gao, Z. Yang and X. Chen, *Nonequilibrium Phases of Repulsive Self-Attention: Chaos, Attention Condensation, and Emergent Locality*, arXiv:2609.28448v1 (2026), https://arxiv.org/html/2609.28448v1 . Relevant material: Sections II and Appendix B, and masking convention.
3. C. Altafini, *Multistability of Self-Attention Dynamics in Transformers*, arXiv:2511.11553v1 (2025), https://arxiv.org/html/2511.11553v1 . Relevant material: continuous-time formulation and stability.
