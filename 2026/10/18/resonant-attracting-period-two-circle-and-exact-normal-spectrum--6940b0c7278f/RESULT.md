# Resonant attracting period-two circle and exact normal spectrum in discrete self-attention

## Finding

For the full, self-inclusive, normalized residual multihead attention map defined below, a mixed-sign spectral tie at the precise step-size stability boundary produces an **entire normally contracting circle of synchronized period-two trajectories**. The circle has a nontrivial, explicit, phase-dependent normal Floquet spectrum; every sufficiently nearby token configuration converges exponentially on even iterates to a selected point of that circle. These statements hold with arbitrary query and key matrices and arbitrarily many attention heads, subject only to a symmetric effective value matrix with simple spectral endpoints.

Let the effective value matrix have eigenvalues \(\lambda_1>\lambda_2\ge\cdots\ge\lambda_d\), with \(\lambda_1>0\), \(\lambda_d<-\lambda_1\), and simple \(\lambda_d\). Define
\[
\eta_c=\frac{2}{-\lambda_1-\lambda_d},\qquad
r=1+\eta_c\lambda_1=-(1+\eta_c\lambda_d)>1.
\]
Choose orthonormal extreme eigenvectors \(v_1,v_d\). On the synchronized circle
\[
\mathcal C=\{(v_\theta,\ldots,v_\theta):v_\theta=\cos\theta\,v_1+\sin\theta\,v_d,\ \theta\in\mathbb R/(2\pi\mathbb Z)\},
\]
the update is exactly \(v_\theta\mapsto v_{-\theta}\). Thus the second iterate fixes \(\mathcal C\) pointwise. Exactly the two points \(\pm v_1\) are fixed by one iteration; every other point has prime period two.

At phase \(\theta\), the complete intrinsic spectrum of the derivative of the **second iterate** is
\[
\begin{array}{c|c}
\text{multiplier}&\text{multiplicity}\\\hline
1&1\\
\big((1+\eta_c\lambda_j)/r\big)^2&1\quad(j=2,\ldots,d-1)\\
\cos^2(2\theta)/r^2&n-1\\
1/r^2&(n-1)(d-2).
\end{array}
\]
Entries with zero multiplicity are omitted, and coincident values have their multiplicities added. All multipliers except the circle-tangent \(1\) are strictly smaller than \(1\) in modulus, uniformly over the circle.

Set
\[
q_*=\max\left\{r^{-2},\ \max_{2\le j\le d-1}\left(\frac{1+\eta_c\lambda_j}{r}\right)^2\right\}<1,
\]
where the inner maximum is omitted when \(d=2\). For every \(q\in(q_*,1)\), some neighborhood of \(\mathcal C\) has the following property: the even iterates of each initial token configuration converge to a **single** point of \(\mathcal C\), with transverse distance \(O(q^k)\) after \(2k\) updates; the odd iterates converge to its reflected image. With nearest-circle phase \(\theta_0\) as initial coordinate, the selected asymptotic phase obeys \(\theta_\infty=\theta_0+O(\operatorname{dist}(X_0,\mathcal C)^2)\) in a local angular chart. The bound is uniform as \(X_0\) tends to \(\mathcal C\).

## Assumptions and scope

Fix integers \(n,d\ge2\) and a finite head count \(H\ge1\). Every token \(x_i\) lies on the Euclidean unit sphere \(S^{d-1}\). For each head \(h\), let \(Q_h,K_h\) be arbitrary compatible finite real query/key matrices and let \(B_h\) be any real \(d\times d\) matrix. The attention weights and update are
\[
A_{ij}^{(h)}(X)=\frac{\exp\langle Q_h x_i,K_h x_j\rangle}{\sum_{\ell=1}^n\exp\langle Q_h x_i,K_h x_\ell\rangle},\quad
F_i(X)=\frac{x_i+\eta\sum_{h=1}^H B_h\sum_{j=1}^n A_{ij}^{(h)}(X)x_j}{\left\|x_i+\eta\sum_{h=1}^H B_h\sum_{j=1}^n A_{ij}^{(h)}(X)x_j\right\|}.
\]
This is the full self-inclusive model, without a diagonal attention mask or external positional biases. Suppose the effective matrix \(V=\sum_h B_h\) is real symmetric, with a simple largest eigenvalue \(\lambda_1>0\), a simple smallest eigenvalue \(\lambda_d<-\lambda_1\), and all other eigenvalues strictly between those endpoints. The theorem fixes \(\eta=\eta_c\) exactly. It asserts only local dynamics near \(\mathcal C\), where all normalization denominators are nonzero.

## Proof

**1. Exact synchronized restriction.** For \(X=(v,\ldots,v)\), every logit in a given attention row and head is identical, so \(A_{ij}^{(h)}=1/n\). The numerator of each token update equals \((I+\eta V)v\). Denote this matrix by \(B=I+\eta_c V\). On the extreme eigenplane \(E=\operatorname{span}\{v_1,v_d\}\), the spectral relations at \(\eta_c\) give \(Bv_1=rv_1\), \(Bv_d=-rv_d\). Hence for \(v\in E\cap S^{d-1}\), \(Bv=rRv\), where \(R\) is the reflection fixing \(v_1\) and negating \(v_d\). Normalization yields \(F(v,\ldots,v)=(Rv,\ldots,Rv)\), proving every assertion about periods.

**2. Attention derivatives cancel at synchronization.** Let \((h_1,\ldots,h_n)\) be a tangent perturbation and \(\bar h=n^{-1}\sum_i h_i\). In each head and row, differentiation of the attention-weighted sum at synchronization gives
\[
D\left[\sum_j A_{ij}^{(h)}(X)x_j\right](h)
=\sum_j\big(DA_{ij}^{(h)}(h)\big)v+\frac1n\sum_j h_j
=v\,D\left(\sum_j A_{ij}^{(h)}\right)(h)+\bar h=\bar h.
\]
The identity uses only row stochasticity and the equality \(A_{ij}^{(h)}=1/n\) at synchronization. The derivative of Euclidean normalization at \(rv'\), with \(\|v'\|=1\), is \((I-v'v'^{\mathsf T})/r\). Consequently the exact intrinsic one-step tangent derivative at \(X_\theta=(v_\theta,\ldots,v_\theta)\) is
\[
(DF_{X_\theta}h)_i
=\frac1r P_{v_{-\theta}}\big(h_i+\eta_c V\bar h\big),\qquad P_w=I-ww^{\mathsf T}.
\]
In particular it depends on none of the individual attention-head matrices beyond the symmetric effective \(V\).

**3. Orthogonal mean/difference decomposition.** Put \(w_\theta=-\sin\theta\,v_1+\cos\theta\,v_d\), the unit tangent within \(E\). Decompose \(T_{X_\theta}(S^{d-1})^n\) orthogonally into: (a) the common \(w_\theta\) direction; (b) each common \(v_j\), \(2\le j\le d-1\); (c) \(n-1\) independent zero-sum token deviations parallel to \(w_\theta\); and (d) \((n-1)(d-2)\) zero-sum deviations in \(E^\perp\). The derivative preserves the mean versus zero-sum splitting at either synchronized point.

In common directions the derivative is the restriction of \(B/r\) followed by tangent projection. On \(E\) it maps the circle tangent by the reflection, so the two-step multiplier is \(1\). On the common \(v_j\) direction it multiplies by \((1+\eta_c\lambda_j)/r\) on each step, giving its square. For zero-sum deviations the \(\bar h\) term vanishes and each step is simply \(P_{v_{-\theta}}/r\). Since
\[
\langle w_\theta,w_{-\theta}\rangle=\cos(2\theta),
\]
the two-step multiplier for each of the \(n-1\) zero-sum \(E\)-tangent directions is \(\cos^2(2\theta)/r^2\). Every zero-sum \(E^\perp\) direction gets \(1/r^2\). The multiplicities sum to \(n(d-1)\), the full phase-space tangent dimension. This proves the displayed spectrum without assuming a special query/key choice.

**4. Uniform local attraction and phase selection.** The endpoint eigenvalues are simple, so each intermediate \(b_j=1+\eta_c\lambda_j\) lies strictly between \(-r\) and \(r\). Also \(r>1\); hence \(q_*<1\). In the orthogonal splitting of step 3, the two-step derivative fixes the circle tangent, acts diagonally on its normal complement, and has uniformly bounded normal norm at most \(q_*\). The compact embedded circle admits a smooth tubular angular/normal chart \((\theta,z)\). Taylor expansion of \(F^2\), uniform in \(\theta\), gives
\[
\|z^+\|\le q\|z\|,\qquad
\theta^+-\theta=O(\|z\|^2)
\]
for any chosen \(q_*<q<1\) and sufficiently small \(\|z\|\). The second estimate holds because the linearized normal bundle has no tangential component. A smaller tube is forward invariant. Iteration gives \(\|z_k\|\le q^k\|z_0\|\); the angular increments are summable and bounded in total by \(O(\|z_0\|^2)\). Thus \(\theta_k\to\theta_\infty\) and the even iterates converge exponentially to one circle point, with odd iterates converging to its reflected image. This completes the proof.

## Verification

The accompanying standalone `verify.py` evaluates the exact nonlinear multihead map, not a linear proxy. Its 135 finite-difference comparisons span 2, 3 and 4 dimensions with random orthogonal eigenbases, 2, 3 and 5 tokens, 1, 2 and 3 independently randomized attention heads, and five phases per configuration. Every two-step return and the full intrinsic Floquet spectra matched the formulas to the stated numerical tolerances. Three additional rational checks verify the representative spectral values \(4/49\), \(9/49\), and \(0\) at the appropriate phase. These numerical tests provide diagnostic evidence only; the universal assertion is proved by steps 1–4.

For instance, take \(V=\operatorname{diag}(2,-1/2,-5)\), \(\eta_c=2/3\), and \(r=7/3\). At \(\theta=\pi/4\), for arbitrary \(n\ge2\), the two-step intrinsic spectrum is exactly \(1\), \(4/49\), \(n-1\) zeros, and \(n-1\) copies of \(9/49\). The zero multipliers describe first-order annihilation of particular token-disagreement directions; they are not a claim of finite-time synchronization.

## Relationship to prior work

Altafini (2026, arXiv:2610.13518v1) formulates the same normalized discrete attention system and gives a principal-consensus stability condition with the strict inequality \(\eta<\eta_c\), including an effective symmetric matrix in the multihead setting. Its source theorem, Jacobian calculations, and longer-step discussion do not state the boundary's pointwise-fixed second-iterate circle, its phase-dependent intrinsic Floquet spectrum, or asymptotic phase selection. The below-threshold stability criterion itself is not claimed as new.

Gao, Yang, and Chen (2026, arXiv:2609.28448v1, especially Appendix B and Section V.1) obtain consensus-flip dynamics and spectra for a repulsive normalized attention model with negative scalar value and a diagonal attention mask; they also discuss spectral selection by a degenerate negative eigenspace. Their hypotheses do not include a simple positive maximum eigenvalue tied in amplification magnitude with a distinct simple negative minimum, and their results do not give the present mixed-sign resonant circle's transverse multihead formula. The existence of synchronized sign flips in related systems is known.

Tsuzuki and Ohki (2025, arXiv:2512.21469v1) analyze normalized power iteration and invariant dominant spectral subspaces. The synchronized restriction here is itself normalized power iteration, so its reflection on an equal-modulus two-plane is a classical linear-algebra consequence. The contribution of the present theorem is the **full interacting-token** local result: its universal, phase-resolved *normal* spectrum and nonlinear convergence to a phase-selected periodic state despite arbitrary state-dependent query/key attention.

## Limitations

The result is local to a neighborhood of the synchronized circle and holds at the exact resonance \(\eta=\eta_c\), not throughout a finite step-size interval. Each particular period-two orbit is neutral along the circle, so the theorem does **not** claim asymptotic attraction to a prescribed individual orbit independent of initialization. It does not classify other invariant sets or basins, non-symmetric effective matrices, diagonal attention masks, positional biases, actual layer-normalization layers, or feedforward components. Its bibliographic originality comparison is limited to the inspected sources and searchable records; an equivalent general theorem may exist elsewhere. No independent audit is claimed.

## References

1. C. Altafini, *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers*, arXiv:2610.13518v1 (first posted 2026-10-09), Sections II–V. https://arxiv.org/html/2610.13518v1
2. Q. Gao, Z. Yang, and X. Chen, *Nonequilibrium Phases of Repulsive Self-Attention: Chaos, Attention Condensation, and Emergent Locality*, arXiv:2609.28448v1 (first posted 2026-09-23), Appendix B and Section V.1. https://arxiv.org/html/2609.28448v1
3. D. Tsuzuki and K. Ohki, *Convergence Analysis of Natural Power Method and Its Applications to Control*, arXiv:2512.21469v1 (first posted 2025-12-25), Section 3. https://arxiv.org/abs/2512.21469
