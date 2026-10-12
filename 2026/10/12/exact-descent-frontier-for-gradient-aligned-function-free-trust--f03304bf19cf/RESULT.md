# Exact descent frontier for gradient-aligned function-free trust-region steps

## Finding

For the explicitly prescribed gradient-aligned Cauchy step used in the decentralized objective-function-free trust-region method of Bellavia, Malaspina, and Morini [1], the sharp one-step objective-descent envelope is
\[
\Phi(x+d)\le\Phi(x)-\sum_{i=1}^N\frac{\|g_i\|^2}{b_i}\,\Gamma(L,M,b_i),
\]
where, for \(L,M,b>0\),
\[
\Gamma(L,M,b)=
\begin{cases}
1-\dfrac{L}{2b}, & b\ge M,\\[3pt]
\min\!\left\{1-\dfrac{L}{2b},\ \dfrac{b}{M}\!\left(1-\dfrac{L}{2M}\right)\right\}, & 0<b<M.
\end{cases}
\]
In particular the quarter-descent certificate from [1, Lemma 4.2] holds for these concrete Cauchy steps with the **smallest universally sufficient threshold**
\[
\boxed{b_i\ge b_*(L,M):=
\begin{cases}
\dfrac{M^2}{4M-2L},&0<L\le M/2,\\[4pt]
\dfrac{2L}{3},&L\ge M/2.
\end{cases}}
\]
This threshold may be a factor of **nine smaller** than the published sufficient bound \(2(L+M)\), with the ratio equal to nine when \(L=M/2\). The improvement applies to the explicit ray-minimizing direction [1, Eq. (30)], not to every step satisfying the weaker abstract model-decrease condition [1, Eq. (13)].

## Assumptions and scope

Let \(N\ge1\), \(X=\prod_{i=1}^N\mathbb R^{n_i}\), and let \(\Phi:X\to\mathbb R\) be continuously differentiable with globally \(L\)-Lipschitz gradient in the product Euclidean norm, \(L>0\). Set \(g=\nabla\Phi(x)=(g_1,\dots,g_N)\). For each \(i\), choose \(b_i>0\) and any real symmetric \(B_i\) with \(\|B_i\|_2\le M\), \(M>0\). For \(g_i\ne0\) define
\[
\rho_i=\frac{g_i^\top B_i g_i}{\|g_i\|^2},\qquad
\alpha_i=\begin{cases}1,&\rho_i\le b_i,\\b_i/\rho_i,&\rho_i>b_i,\end{cases}
\qquad d_i=-\frac{\alpha_i}{b_i}g_i.
\]
For \(g_i=0\), define \(d_i=0\). This is precisely the gradient-aligned Cauchy rule in [1, Eq. (30)], including negative model curvature. Each direction satisfies the model sufficient-decrease and trust-radius conditions [1, Eq. (13)]; our theorem uses its more specific formula.

The distributed application has equal-dimensional blocks, objective \(\Phi(x)=\sum_i f_i(x_i)+\frac1{2\beta}x^\top(I-W\otimes I)x\), and a declared smoothness bound \(L=\sum_i L_i+\beta^{-1}\|I-W\|_2\), as in [1]. The general statement above also applies outside that special structure.

## Proof

**1. Sharp envelope.** For nonzero \(g_i\), the Rayleigh quotient satisfies \(-M\le\rho_i\le M\). Consequently
\[
\min\{1,b_i/M\}\le\alpha_i\le1.
\]
The descent lemma and orthogonality of coordinate blocks give
\[
\begin{aligned}
\Phi(x+d)-\Phi(x)
&\le \langle g,d\rangle+\frac L2\|d\|^2\\
&= -\sum_i\frac{\|g_i\|^2}{b_i}
\left(\alpha_i-\frac{L}{2b_i}\alpha_i^2\right).
\end{aligned}
\]
For fixed \(L,b_i\), the polynomial \(u\mapsto u-Lu^2/(2b_i)\) is concave, so its minimum on \([\min\{1,b_i/M\},1]\) occurs at an endpoint. At \(u=1\) it equals \(1-L/(2b_i)\); at \(u=b_i/M\), when \(b_i<M\), it equals \((b_i/M)(1-L/(2M))\). This is exactly \(\Gamma(L,M,b_i)\).

**2. Sharpness.** Take a scalar quadratic \(\Phi(z)=Lz^2/2+z\), at \(z=0\), so \(g=1\). The allowed model \(B=0\) realizes \(\alpha=1\); the allowed model \(B=M\) realizes \(\alpha=\min\{1,b/M\}\). Since the descent lemma is an equality for this quadratic, each candidate endpoint coefficient is attained exactly. Thus the pointwise minimum is the true universal coefficient, not merely an estimate.

**3. Exact quarter-descent threshold.** If \(b\ge M\), the condition \(\Gamma(L,M,b)\ge1/4\) is \(b\ge2L/3\). For \(0<b<M\), it is equivalent to the simultaneous inequalities
\[
b\ge2L/3,\qquad
b\left(1-\frac{L}{2M}\right)\ge\frac M4.
\]
For \(0<L\le M/2\), the second is the binding inequality and yields \(b_*=M^2/(4M-2L)\). For \(M/2\le L<3M/2\), the first binds because \(\frac{2L}{3M}(1-\frac{L}{2M})\ge1/4\); when \(L\ge3M/2\), \(2L/3\ge M\) and only the first remains relevant. At equality the relevant scalar endpoint model attains coefficient \(1/4\). For any smaller \(b\), that endpoint violates the target quarter-descent bound. Therefore \(b_*\) is exact. Direct algebra shows that \(2(L+M)/b_*\le9\), with equality at \(L=M/2\).

**4. Genuine two-agent sharpness.** The preceding equality models fit a one-block smooth objective. To show that the bound cannot be uniformly lowered even on connected decentralized quadratic-consensus problems with two agents, fix \(L,M>0\), a denominator \(0<b<b_*(L,M)\), and let \(\delta,\epsilon>0\) tend to zero with \(\delta+\epsilon<L\). Put
\[
W=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix},\quad
\beta=1/\delta,\quad
f_1(t)=\frac{L-\delta-\epsilon}{2}t^2+t,\quad
f_2(t)=\frac{\epsilon}{2}t^2.
\]
The graph is connected and all mixing weights are positive. The published bound for the full penalized gradient is exactly \((L-\delta)+\delta\|I-W\|_2=L\). At \(x=(0,0)\), the block gradients are \((1,0)\). Choose \(B_1=0\) or \(B_1=M\) to realize the endpoint witnessing \(\Gamma(L,M,b)<1/4\); choose \(B_2=0\). The step has only its first coordinate nonzero. Along that coordinate the actual quadratic curvature is \(L-\delta/2-\epsilon\), tending to \(L\). Hence its normalized objective decrease tends to the violating coefficient \(\Gamma(L,M,b)<1/4\), and is strictly below a quarter for all sufficiently small positive \(\delta,\epsilon\). Both local functions have positive quadratic curvature. This shows the same sharp universal frontier for genuine connected two-agent instances, in the sense of an attainable infimum, without relying on a disconnected or zero-penalty graph. \(\square\)

## Verification

Run the enclosed Python standard-library program using `python3 verify.py`. It evaluates the step and exact quadratic objective decrease with rational arithmetic, confirms both endpoint witnesses and the piecewise frontier on 400 positive rational pairs of \((L,M)\), tests nearby denominators on each side of the threshold, checks two connected-agent witnesses, and confirms the factor-nine equality. Output: `VERIFY_OK`. These finite checks corroborate the formulas; the preceding argument proves the statement for all positive real parameters and all finite block dimensions.

## Relationship to prior work

Bellavia, Malaspina, and Morini [1, Lemma 3.4] establish that the explicit Cauchy step satisfies their model conditions; [1, Lemma 4.2] uses those abstract conditions to infer quarter-descent from \(b_i\ge2(L+M)\). The earlier single-agent function-free trust-region paper [2, Lemma 6] uses the same conservative threshold for arbitrary accepted approximate model steps. Neither statement characterizes the sharp descent coefficient for the particular gradient-aligned ray minimizer or the transition at \(L=M/2\). A published result on the fraction-of-optimal *predicted model decrease* for SPD trust-region Cauchy points [3] addresses a distinct comparison and does not bound the decrease in an external \(L\)-smooth objective with indefinite model blocks.

## Limitations

This is a one-step universal guarantee for the specific implementable ray-minimizing direction, not an improvement to the weaker condition for arbitrary approximate trust-region solvers. No new outer-iteration convergence or evaluation-complexity theorem is asserted; replacing the threshold in such proofs requires checking every downstream use separately. The equality examples for general smooth objectives are scalar; for strictly decentralized two-agent penalty problems sharpness is via an explicit limiting family. The literature comparison is not an exhaustive independence certificate, and no independent audit has been performed.

## References

1. S. Bellavia, G. Malaspina, B. Morini, *DOFFO_TR: a Decentralized Objective Function-Free Optimization method with Trust-Region*, arXiv:2609.00878v1, first posted 2026-09-01; especially Eqs. (13), (30), and Lemmas 3.4 and 4.2. https://arxiv.org/abs/2609.00878
2. G. N. Grapiglia, G. F. D. Stella, *An Adaptive Trust-Region Method Without Function Evaluations*, Optimization Online (2022-02-04), Lemma 6. https://optimization-online.org/2022/02/8787/
3. *Sharp fraction-of-optimal decrease for the SPD Cauchy trust-region point*, published research record (2026-09-20), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-cauchy-trust-region-optimal-decrease-ratio--0eec6412acfe
