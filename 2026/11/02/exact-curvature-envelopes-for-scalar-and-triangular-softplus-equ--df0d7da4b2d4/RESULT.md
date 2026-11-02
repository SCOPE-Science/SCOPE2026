# Exact curvature envelopes for scalar and triangular softplus equilibria

## Finding

Fix \(0<q<1\) and write \(\delta=1-q\). For \(\phi(v)=\log(1+e^v)\), consider exact nonnegative softplus equilibria with a single input \(x\), nonnegative recurrent weights, and unit input and output norms. Two natural network architectures exhibit different sharp curvature constants.

1. **One unit.** If \(z_1=\phi(qz_1+x+b_1)\) and \(u=z_1\), then
   \[
   \max_{b_1\in\mathbb R}u''(0)=\frac{t_*(1-t_*)}{(1-qt_*)^3},\qquad
   t_* =\frac{1}{\delta+\sqrt{\delta^2+q}},\qquad
   \lim_{q\uparrow1}\delta^2\max_{b_1}u''(0)=\frac4{27}.
   \]
2. **Triangular two-unit coupling.** If
   \[
   z_1=\phi(qz_1+x+b_1),\qquad
   z_2=\phi(qz_1+x+b_2),\qquad u=z_2,
   \]
   then, for every \(0<q<1\),
   \[
   \boxed{\sup_{b_1,b_2\in\mathbb R}u''(0)=\frac{1}{4(1-q)^2}.}
   \]
   The supremum is strict for all finite biases but is approached as the first unit saturates and the second stays near its maximal activation curvature. Hence the optimized two-unit asymptotic coefficient is \(27/16\) times the optimized one-unit coefficient, at fixed \(\|W\|_\infty=q\), \(K_A=1\), and \(\|w\|_1=1\).

Two independent copies of the triangular construction, one for each coordinate in \(\mathbb R^2\), produce a four-unit convex equilibrium potential with \(K_A=1\), \(\|w\|_1=2\), and
\[
\boxed{\sup_b\det D^2u(0)=\frac{1}{16(1-q)^4}.}
\]
In particular, the coefficient of the inverse-fourth-power determinant scale can be four times the coefficient \(1/64\) of the two-independent-one-unit construction in the motivating source, even under the same input/readout norm bounds. These are architecture-specific exact suprema, not claims of the globally sharp width-independent constant.

## Assumptions and scope

The exact-state equilibrium is \(z=\phi(Wz+Ax+b)\), with componentwise softplus and fixed parameters \(W,A,b,w\), and output \(u=w^{\mathsf T}z\). The original normalized hypotheses are \(W\ge0\), \(w\ge0\), \(\|W\|_\infty\le q<1\), \(K_A=\max_i\|A_{i,:}\|_2=1\). The single-unit model uses \(W=(q)\), \(A=w=(1)\). The triangular model uses
\[
W=\begin{pmatrix}q&0\\q&0\end{pmatrix},\qquad
A=\begin{pmatrix}1\\1\end{pmatrix},\qquad
w=\begin{pmatrix}0\\1\end{pmatrix}.
\]
Here \(\|W\|_\infty=q\) exactly. The input location is fixed to \(x=0\) without loss for maximization over the unrestricted finite biases. The two-dimensional construction is the block-diagonal direct sum of two triangular models, with independent inputs and output sum; it has four hidden units and readout vector \((0,1,0,1)^{\mathsf T}\). Both independent copies share the same \(q\).

The supremum is over the entire real bias parameter space; biases may depend on \(q\). Neither the two-unit nor the four-unit supremum is attained at finite bias. Every displayed finite-parameter instance has a unique smooth convex equilibrium by contraction. No result is claimed for optimal training, finite-iteration unrolling, roundoff certification, or arbitrary recurrent matrices.

## Proof

**1. Exact derivatives and realizable slopes.** Let \(t=\phi'(qz_1+x+b_1)\) and \(s=\phi'(qz_1+x+b_2)\) at \(x=0\). Both lie strictly between zero and one. Conversely, for arbitrary \(t,s\in(0,1)\), define \(z_1=-\log(1-t)\) and choose
\[
b_1=\log\frac{t}{1-t}-qz_1,\qquad
b_2=\log\frac{s}{1-s}-qz_1.
\]
Then the unique equilibrium has these activation slopes. The same construction with only \(b_1\) proves the slope range in the one-unit case.

Write \(d=1-qt\), so \(d>\delta>0\) for finite bias. Implicit differentiation of the first state gives
\[
z_1'=\frac{t}{d},\qquad
z_1''=\frac{t(1-t)}{d^3},\qquad
1+qz_1'=\frac1d.
\]
For the second state \(u=z_2\), direct chain-rule differentiation yields
\[
\begin{aligned}
u''&=s(1-s)(1+qz_1')^2+sqz_1''\\
&=\frac{s(1-s)}{d^2}+\frac{qst(1-t)}{d^3}
=\frac{s(1-qt^2-ds)}{d^3}.
\end{aligned}
\]
These are exact equalities at the fixed point, not finite-unrolling approximations.

**2. One-unit maximization.** The curvature as a function of its freely realizable slope is
\[
H_1(t)=\frac{t(1-t)}{(1-qt)^3}.
\]
Its derivative is
\[
H_1'(t)=\frac{1-2(1-q)t-qt^2}{(1-qt)^4}.
\]
The numerator decreases strictly on \([0,1]\), is positive at zero, and equals \(-\delta\) at one. Its unique zero is \(t_*=1/(\delta+\sqrt{\delta^2+q})\); the endpoints have zero curvature, proving the asserted **maximum**, with finite realizing bias. As \(\delta\downarrow0\), \(t_*=1-\delta/2+O(\delta^2)\), so \(1-qt_*=3\delta/2+O(\delta^2)\), and hence \(\delta^2H_1(t_*)\to4/27\).

**3. Two-unit maximization.** For fixed \(t\), the second-unit expression is a strictly concave quadratic in \(s\). Its unique optimum is
\[
s_*(t)=\frac{1-qt^2}{2(1-qt)}.
\]
It lies in \((0,1)\): positivity follows from \(qt^2<1\), and
\[
2(1-qt)-(1-qt^2)=\delta+q(1-t)^2>0.
\]
Therefore
\[
\max_{0<s<1}H_2(t,s)=\frac{(1-qt^2)^2}{4(1-qt)^4}.
\]
The ratio \(R(t)=(1-qt^2)/(1-qt)^2\) has derivative
\[
R'(t)=\frac{2q(1-t)}{(1-qt)^3}>0\qquad(0<t<1),
\]
so the joint supremum is the limit as \(t\uparrow1\), equal to \(1/(4\delta^2)\). Since the derivative is strict in the open interval, the supremum is not attained. The realizing sequence \(s=s_*(t)\) is valid because both slopes can be prescribed by finite biases for every \(t<1\). Dividing the inverse-square coefficients gives \((1/4)/(4/27)=27/16\), and every width-uniform bound with normalization \(\|w\|_1K_A^2\delta^{-2}\) must permit a prefactor of at least \(1/4\).

**4. Two-dimensional determinant.** Take independent triangular copies indexed by input coordinates, with all cross-coordinate recurrent and input coefficients zero. Their Hessian is exactly
\[
D^2u(0)=\operatorname{diag}\bigl(H_2(t_1,s_1),H_2(t_2,s_2)\bigr).
\]
The determinant is their product; the biases of the two copies are independent. The product of the two one-dimensional suprema is \(1/(16\delta^4)\), approached simultaneously, and is an upper bound within this precise four-unit architecture. The source construction has determinant asymptotic \(1/(64\delta^4)\). Their ratio of asymptotic coefficients is exactly four. Both constructions satisfy \(K_A=1\), \(\|w\|_1=2\), and the same row-sum contraction factor.

## Verification

Run `python verify.py` with SymPy and mpmath available. The reproducible checker verifies seven symbolic identities, 1,500 deterministic high-precision parameter triples, five singular-gap limits, and three finite-difference comparisons with independently reconstructed exact equilibria. Those finite checks support the algebra; the proofs of continuous optimization, strictness, and parameter asymptotics are the analytic arguments above, not finite enumeration.

## Relationship to prior work

Vázquez, Lu, and Nowicki (arXiv:2610.31386v1/v2, Theorem 4.2) establish a general \(\|w\|_1K_A^2\min\{\delta^{-2},(4\delta^3)^{-1}\}\) curvature bound. Their Theorem 4.4 provides a specific one-unit sequence of inverse-square coefficient \(1/8\); Remark 4.5 takes two independent copies with determinant coefficient \(1/64\), and explicitly does not assert the optimality of the prefactor. The result here optimizes the *whole one-unit family* to \(4/27\), solves an entire triangular two-unit bias optimization to coefficient \(1/4\), and constructs the corresponding determinant envelope. It neither contradicts nor improves the published universal upper bound; it gives a stricter lower barrier on any possible optimal universal prefactor.

Nyström and Vestberg (arXiv:2110.03310v3, Sections 3.2 and 6.3) use finite-depth input-convex networks and prove derivative estimates through finite layer products, not this recurrent fixed-point extremum. General implicit-differentiation identities in Huang et al. (ICLR 2024) do not by themselves provide these bias-optimized constants. Entesari et al. (ICML 2024) treat curvature propagation in explicit networks. The algebraic derivatives here are specializations of established identities, but the exact optimization and width comparison require the separate proof above.

## Limitations

The sharp values are only for the stated scalar one-unit, triangular two-unit, and independent four-unit architectures. The global best width-independent curvature prefactor may exceed \(1/4\); no global upper bound sharper than the motivating general result is established here. The bias limit includes parameters diverging in magnitude, not a fixed trained network, and does not imply a PDE solver's convergence, stability under finite precision, or superiority in actual numerical residual minimization. Historical-priority uncertainty remains for older specialized implicit-network curvature optimization, despite the comparisons described.

## References

- Edison Vázquez, Yingdong Lu, and Tomasz Nowicki, *Convex Equilibrium Potentials for Monge–Ampère: Curvature Bounds and A Posteriori Evaluation*, arXiv:2610.31386v1 (public 2026-10-22), revised v2 (2026-10-23). Full texts: https://arxiv.org/html/2610.31386v1 and https://arxiv.org/html/2610.31386v2.
- Kaj Nyström and Matias Vestberg, *Solving the Dirichlet problem for the Monge–Ampère equation using neural networks*, arXiv:2110.03310v3, Section 6.3. https://arxiv.org/html/2110.03310v3.
- Yuhao Huang, Qingsong Wang, Akwum Onwunta, and Bao Wang, *Efficient Score Matching with Deep Equilibrium Layers*, ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/b73442f01ee75616fad938e1eb1f2427-Abstract-Conference.html.
- Taha Entesari, Sina Sharifi, and Mahyar Fazlyab, *Compositional Curvature Bounds for Deep Neural Networks*, ICML 2024. https://proceedings.mlr.press/v235/entesari24a.html.
