# Cooperative stabilization of an antipodal pair by two unstable attention heads

## Finding

In the full-self-attention, residual, unit-normalized, **two-head** discrete-time model, two distinct attention heads can jointly make an antipodal pair of tokens an exponentially attracting fixed point, although **each isolated head has an expanding transverse multiplier at that same antipodal fixed point**. The following exact construction has two tokens of ambient dimension four and two heads of width two. Its joint tangent spectrum is

\[
\operatorname{spec}(D\mathcal F(e_1,-e_1)|_{T(\mathbb S^3)^2})=
\{0,\underbrace{4/9,4/9,4/9,4/9,4/9}_{\text{five times}}\}.
\]

Keeping only head one gives an intrinsic multiplier \(10/3>1\), while keeping only head two gives an intrinsic multiplier \(-12/7<-1\). Thus neither isolated head attracts this pair; their combination does. The resulting attracting fixed point persists uniquely near \((e_1,-e_1)\) under all sufficiently small smooth parameter perturbations (with the nearby fixed point not necessarily remaining antipodal).

## Assumptions and scope

Let \(x_1,x_2\in\mathbb S^3\subset\mathbb R^4\) be column tokens. Put \(\eta=1\), take two heads of width \(m=2\), and write \(e_1=(1,0,0,0)^\top\). Let

\[
\kappa_1=\tfrac12\log3,\qquad \kappa_2=\tfrac12\log7,\qquad
R=\begin{pmatrix}1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
Q^{(h)}=K^{(h)}=\sqrt{\kappa_h}\,R.
\]

The value matrices of the two heads and the common output map are

\[
W_1=\begin{pmatrix}1&0&0&0\\0&4&0&0\end{pmatrix},\quad
W_2=\begin{pmatrix}1&0&0&0\\0&-4&0&0\end{pmatrix},\quad
O=\begin{pmatrix}1&0&1&0\\0&1&0&1\\0&0&0&0\\0&0&0&0\end{pmatrix}.
\]

The score and full softmax weight in head \(h\in\{1,2\}\) are

\[
s_{ij}^{(h)}=\langle Q^{(h)}x_i,K^{(h)}x_j\rangle,
\qquad a_{ij}^{(h)}=\frac{\exp(s_{ij}^{(h)})}
{\exp(s_{i1}^{(h)})+\exp(s_{i2}^{(h)})}.
\]

Define the pre-normalized update and the map on the open domain where neither pre-normalized vector vanishes by

\[
y_i=x_i+O\begin{pmatrix}\sum_{j=1}^{2}a_{ij}^{(1)}W_1x_j\\[2pt]
\sum_{j=1}^{2}a_{ij}^{(2)}W_2x_j\end{pmatrix},
\qquad \mathcal F_i(x_1,x_2)=\frac{y_i}{\|y_i\|_2}.
\]

The displayed column is the ordinary concatenation of two length-two head outputs. This is precisely the two-head residual-and-normalization form considered in Section V-A, equation (13), of Altafini [1]; no claim is made about feed-forward sublayers, masked attention, or other normalizations. The attention is self-inclusive and full in both heads.

For comparison, \(\mathcal F^{\{h\}}\) means the same map and parameters but with the other head contribution omitted, **without renormalizing the residual coefficient or the retained head**.

## Proof

**1. Fixed point and radial gain.** At \(p=(e_1,-e_1)\), the two within-token scores are \(\kappa_h\) and the cross-token scores are \(-\kappa_h\). Hence

\[
a_{11}^{(1)}=a_{22}^{(1)}=\tfrac34,\qquad
 a_{11}^{(2)}=a_{22}^{(2)}=\tfrac78,
\]

with complementary cross-weights. Writing \(q_h=2a_{11}^{(h)}-1=\tanh\kappa_h\), one has \(q_1=1/2\) and \(q_2=3/4\). Each head acts as \(q_he_1\) on token one and \(-q_he_1\) on token two in the first output coordinate. Therefore

\[
y_1=(1+q_1+q_2)e_1=\tfrac94e_1,
\qquad y_2=-\tfrac94e_1.
\]

Normalization gives \(\mathcal F(p)=p\). Both normalizing denominators are strictly positive, so the map is real-analytic near \(p\).

**2. No first-order softmax variation.** All tangent directions at \(\pm e_1\) lie in \(e_1^\perp\). For a perturbation \(u_i\perp e_1\), the derivative of
\(s_{ij}^{(h)}=\kappa_h[(x_i)_1(x_j)_1+(x_i)_2(x_j)_2]\)
at \(p\) is zero: the first-coordinate tangent perturbations vanish and the base second coordinates vanish. Thus the derivatives of all \(a_{ij}^{(h)}\) vanish on the product tangent space.

**3. Exact joint tangent Jacobian.** Set \(B_1=OW_1^{\mathrm{pad}}=\operatorname{diag}(1,4,0,0)\) and \(B_2=OW_2^{\mathrm{pad}}=\operatorname{diag}(1,-4,0,0)\), using the evident zero-padding into their respective head slots. For the second-coordinate perturbations \((u_1,u_2)\) the pre-normalized differential is

\[
\begin{pmatrix}\delta(y_1)_2\\\delta(y_2)_2\end{pmatrix}
=\begin{pmatrix}
1+4(\frac34-\frac78)&4(\frac14-\frac18)\\[1pt]
4(\frac14-\frac18)&1+4(\frac34-\frac78)
\end{pmatrix}
\begin{pmatrix}u_1\\u_2\end{pmatrix}
=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}
\begin{pmatrix}u_1\\u_2\end{pmatrix}.
\]

The derivative of \(y\mapsto y/\|y\|_2\) at \(\pm(9/4)e_1\) restricts to multiplication by \(4/9\) on \(e_1^\perp\). Hence the full second-coordinate tangent block is

\[
J_{(2)}=\frac29\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad \operatorname{spec}J_{(2)}=\{4/9,0\}.
\]

Both value/output compositions vanish in coordinates three and four, so each of the other two tangent blocks equals \(\frac49I_2\). Their eigenvalues provide the four additional copies of \(4/9\). In these orthonormal tangent coordinates, the real symmetric Jacobian has Euclidean operator norm \(4/9<1\). By continuity the smooth map is a strict contraction in a sufficiently small tangent chart around \(p\), proving local exponential attraction.

**4. Each isolated head expands.** With head one alone, the normalization denominator at \(p\) is \(1+q_1=3/2\). Its second-coordinate symmetric tangent vector \((u_1,u_2)=(1,1)\) is multiplied by

\[
\lambda_{\mathrm{sym},1}=\frac{1+4}{1+q_1}=\frac{10}{3}>1.
\]

With head two alone, the denominator is \(1+q_2=7/4\), and the same tangent vector is multiplied by

\[
\lambda_{\mathrm{sym},2}=\frac{1-4}{1+q_2}=-\frac{12}{7},
\qquad |\lambda_{\mathrm{sym},2}|>1.
\]

Thus \(p\) is a (linearly) unstable fixed point for each isolated-head map, even though it is exponentially attracting for the joint map. This is a genuinely two-head statement because the score sharpnesses are different, and the opposite-sign transverse actions would be collapsed by replacing the heads with a single common-attention average.

**5. Persistence.** All six eigenvalues of the joint differential lie strictly inside the unit disk. The derivative of \((x,\vartheta)\mapsto\mathcal F_{\vartheta}(x)-x\) in local coordinates is \(D\mathcal F(p)-I\), which is invertible. The implicit function theorem supplies a unique nearby fixed point for all sufficiently small coefficient perturbations, while continuity of the differential preserves its spectral contraction. This persistence is local and does not assert that the perturbed fixed point remains precisely antipodal.

## Verification

The standalone program `check.py` implements the complete softmax/concatenation/normalization map directly using standard-library floating point operations. It verifies the exact rational coefficient identities independently with `fractions.Fraction`; evaluates central-difference derivatives in all six tangent coordinate directions; checks the full joint Jacobian and isolated-head symmetric multipliers to numerical tolerance \(10^{-6}\); and checks 24 nearby random trajectories for decay over 24 iterates. Its observed output is in `checker_output.txt`.

The numerical checks do not prove the infinite-time theorem. The universal local exponential claim follows instead from the exact six-dimensional Jacobian and the contraction/implicit-function arguments above.

## Relationship to prior work

Altafini [1, Section V-A, equation (13), Theorem 3] proves multihead **consensus** stability under spectral assumptions. The same section explicitly says there is then no analytic or numerical evidence for stable **multihead bipartite** equilibria. The present example addresses precisely that unresolved phenomenon in the same discrete normalized architecture. The single-head bipartite stability theory in [1, Sections IV-B and V-A] and its continuous-time predecessor [2] are not claimed as new.

Pendharkar [3] studies interacting **continuous-time multihead gradient flows**, including inter-head radial effects and clustering rates; those results do not give this fixed point of a residual discrete-time map nor the exact head-by-head versus combined multipliers. Gao–Yang–Chen [4] analyze **single-head self-masked** normalized attention with high-dimensional clustering and inter-cluster leakage; the two-token, self-inclusive two-head map here is outside that mechanism. Abella–Silvestre–Tabuada [5] study continuous-time consensus regimes (their multihead full-attention guarantee takes identity value map and hemisphere hypotheses), not a result excluding the present arbitrary-sign output matrices.

## Limitations

The example proves local, not global, attraction and does not estimate its basin beyond the existence of a neighborhood. The conclusion is for two tokens, ambient dimension four, width-two heads, full self-including attention, and spherical normalization, not for causal masking, layer norm, or feed-forward sublayers. The specific matrices have deliberately selected opposite-sign second-coordinate value weights, and the output matrix has rank two; the theorem does not claim genericity among all attention architectures. Robustness is local in parameter space. No claim is made that a model with two arbitrary different heads behaves this way. Historical-priority searching is not exhaustive and independent verification has not been performed.

## References

[1] C. Altafini, *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers*, arXiv:2610.13518v1 (first posted 2026-10-09), Section V-A, equation (13), Theorem 3, and discussion after it. https://arxiv.org/html/2610.13518v1

[2] C. Altafini, *Multistability of Self-Attention Dynamics in Transformers*, arXiv:2511.11553v1 (2025), Sections 2 and 5. https://arxiv.org/html/2511.11553v1

[3] A. Pendharkar, *Gradient Flow Structure and Quantitative Dynamics of Multi-Head Self-Attention*, arXiv:2605.04279v2 (2026), Sections 2–4 and 7–11. https://arxiv.org/html/2605.04279v2

[4] Q. Gao, Z. Yang, X. Chen, *Clustered Attractor Manifolds and Dynamical Condensation in Self-Attention*, arXiv:2608.08922v1 (2026), main model and Supplemental Section III. https://arxiv.org/html/2608.08922v1

[5] Á. Rodríguez Abella, J. P. Silvestre, P. Tabuada, *The Asymptotic Behavior of Attention in Transformers*, arXiv:2412.02682v2 (2025), Table 1 and Sections 2–5. https://arxiv.org/html/2412.02682v2
