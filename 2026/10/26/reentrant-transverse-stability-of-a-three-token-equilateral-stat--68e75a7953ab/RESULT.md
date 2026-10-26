# Reentrant transverse stability of a three-token equilateral state under full repulsive softmax attention

## Finding
For the normalized full-attention repulsive map on three unit planar tokens, the equilateral equilibrium family is transversely attracting at sufficiently low **and** sufficiently high positive attention sharpness, but transversely repelling at intermediate sharpness whenever the residual step lies in an explicitly determined nonempty interval. The transition parameters and both nontrivial Jacobian multipliers are exact.

\[
S(\beta)=2+\frac{9(\beta-2)}{4(\exp(3\beta/2)+2)}.
\]
There is a unique maximizer \(\beta_*>2\), characterized by
\[
2+(4-3\beta_*/2)\exp(3\beta_*/2)=0,
\]
and a sharp step boundary \(h_c=2/S(\beta_*)\), numerically \(h_c\approx0.986914010353021\).
For \(0<h<h_c\), the family is transversely linearly attracting for every finite \(\beta>0\). At \(h=h_c\), the shape multipliers equal \(-1\) exactly at \(\beta_*\), with strict attraction elsewhere. For every \(h_c<h<1\), there are exactly two values
\[
2<\beta_-(h)<\beta_*<\beta_+(h)<\infty,
\qquad S(\beta_\pm(h))=2/h.
\]
The family is transversely attracting for \(0<\beta<\beta_-(h)\) and for \(\beta>\beta_+(h)\), and transversely repelling for \(\beta_-(h)<\beta<\beta_+(h)\). At both boundaries the two shape multipliers are exactly \(-1\). No nonlinear period-doubling claim is made at the critical boundaries.

## Assumptions and scope
Fix \(0<h<1\) and \(\beta>0\). Let \(u(\theta)=(\cos\theta,\sin\theta)\) and let \(x=(x_0,x_1,x_2)\in(S^1)^3\). All three self-edges are included in the attention weights:
\[
 a_{ij}(x)=\frac{\exp(\beta\langle x_i,x_j\rangle)}{\sum_{k=0}^2\exp(\beta\langle x_i,x_k\rangle)},\qquad
 F_{h,\beta}(x)_i=\frac{x_i-h\sum_{j=0}^2 a_{ij}(x)x_j}{\left\|x_i-h\sum_{j=0}^2 a_{ij}(x)x_j\right\|}.
\]
This is globally well-defined because the denominator is at least \(1-h>0\). The equilibria of interest are \(x_i=u(\theta+2\pi i/3)\) for arbitrary \(\theta\in\mathbb R/2\pi\mathbb Z\). 'Transversely attracting' means the linearization has shape-spectrum strictly inside the unit circle after quotienting the neutral common-rotation direction. It also implies local attraction to the circle of equilibria in a neighborhood. 'Transversely repelling' means shape-spectrum has modulus greater than one and the equilibrium is linearly unstable transverse to rotations. The parameter thresholds refer to finite positive \(\beta\).

## Proof
At an equilateral state, the diagonal attention weight is \(p=\exp(3\beta/2)/(\exp(3\beta/2)+2)\), and both off-diagonal weights equal \(q=1/(\exp(3\beta/2)+2)\). Since the other two unit vectors sum to \(-x_i\), the attention field is \(Kx_i\), where \(K=1-3q\). Thus the pre-normalized vector is \((1-hK)x_i\), and \(1-hK>0\); every equilateral state is indeed fixed.

We compute the complete angular derivative, not just its restriction to an ansatz. Write \(x_i=u(\theta_i)\), \(m_i=\sum_j a_{ij}u(\theta_j)\), and consider a perturbation \(\delta=(\delta_0,\delta_1,\delta_2)\). The tangential component relative to the moving direction \(u(\theta_i)\) is
\[
 t_i=\langle m_i,u'(\theta_i)\rangle=\sum_j a_{ij}\sin(\theta_j-\theta_i).
\]
At the regular triangle, \(t_i=0\), and the weighted average of the neighbor sines is zero. Differentiating the softmax and the sines gives the exact relation
\[
\delta t_i=\left(\frac q2+\frac{3q\beta}{4}\right)\sum_{j\ne i}(\delta_i-\delta_j).
\]
Indeed, the direct sine derivative contributes \(q\sum_{j\ne i}(-1/2)(\delta_j-\delta_i)\); the weight derivative contributes \(q\beta\sum_{j\ne i}(3/4)(\delta_i-\delta_j)\), with the softmax normalizing derivative canceling in the sum because the base weighted sine sum vanishes. Therefore the tangential component of the variation of \(m_i\) in ambient coordinates is
\[
 K\delta_i+\delta t_i.
\]
For common rotation \(\delta_0=\delta_1=\delta_2\), this equals \(K\delta_i\). On the two-dimensional zero-sum shape space \(\sum_i\delta_i=0\), it equals \(L\delta_i\), where
\[
 L=K+3q\left(\frac12+\frac{3\beta}{4}\right)=1+\frac{3q}{4}(3\beta-2).
\]
Differentiating normalization at the positive radial factor \(1-hK\) gives one angular multiplier \(1\) and exactly two equal shape multipliers
\[
\lambda(h,\beta)=\frac{1-hL}{1-hK}.
\]
The denominator is positive. Since
\[
 K-L=-\frac{3q}{4}(2+3\beta)<0,
\]
the strict comparison between the squares of the numerator and denominator reads
\[
 (1-hL)^2-(1-hK)^2=h(K-L)[2-h(K+L)].
\]
Thus \(|\lambda|<1\) holds precisely when \(hS(\beta)<2\), where
\[
 S=K+L=2+\frac{9(\beta-2)}{4(\exp(3\beta/2)+2)};
\]
correspondingly \(|\lambda|>1\) exactly when \(hS>2\). Equality gives \(\lambda=-1\), since \(\lambda<1\) for every \(h,\beta>0\). Note that \(S(0)=1/2\), \(S(2)=2\), \(S(\beta)>2\) for \(\beta>2\), and \(S(\beta)\to2\) from above as \(\beta\to\infty\).

The sign of \(S'(\beta)\) is the sign of
\[
 H(\beta)=2+(4-3\beta/2)\exp(3\beta/2).
\]
Here \(H'(\beta)=(9/4)(2-\beta)\exp(3\beta/2)\). Hence \(H\) first increases on \((0,2)\), then strictly decreases from \(H(2)>0\) to \(-\infty\). It has exactly one zero \(\beta_*>2\). Thus \(S\) increases strictly until \(\beta_*\) and decreases strictly afterward. Its maximum is strictly above \(2\), so \(0<h_c=2/S(\beta_*)<1\). The complete claimed regimes follow by intersecting the graph of \(S\) with the level \(2/h>2\).

For strict shape contraction, use the local angle chart \((\theta,\delta_1-\delta_0,\delta_2-\delta_0)\). The fixed equilateral circle is invariant; its transverse derivative is \(\lambda I_2\), with \(|\lambda|<1\). Continuity gives a uniformly attracting neighborhood modulo the rotation symmetry. When \(|\lambda|>1\), the transverse derivative expands both shape directions, proving transverse linear instability. At the equality boundaries the derivative test alone cannot classify nonlinear stability.

## Verification
A standalone Python checker recomputes the closed-form threshold numerically by bisection, evaluates angular derivatives of the **three-token normalized map itself** by symmetric perturbations, verifies both shape eigendirections, the neutral rotation, and the low/intermediate/high regime signs for several step sizes. It also checks the denominator bound and the exact algebraic identity using rational samples of the independent symbolic parameters. In particular, for \(h=0.995\), the thresholds are approximately \(\beta_-=2.115645828146\) and \(\beta_+=4.098788273707\), enclosing an interval of repulsion. Finite numerical tests are not the proof of the all-parameter result; the preceding calculations establish it.

## Relationship to prior work
Altafini's 2026 study of discrete-time full self-attention develops equilibrium and stability classifications under a symmetric value matrix with a simple **positive** dominant eigenvalue. Its hypotheses exclude the scalar negative value map used here, and they do not imply the present high-sharpness stabilization of the equilateral three-token state. Gao, Yang and Chen's 2026 study uses negative values and regular polygons, but imposes the structurally different diagonal masking \(a_{ii}=0\) in its repulsive attention, while the present theorem critically includes the self edge. The spectra and thresholds of the masked and unmasked systems are distinct; the cited flip phenomena do not imply this all-sharpness two-threshold reentrance. The result concerns local fixed-family stability, not global convergence or the existence of nonlinear attracting two-cycles.

## Limitations
The analysis applies exactly to three planar unit tokens, full softmax attention with \(Q=K=I\), scalar negative value \(-I\), and steps \(0<h<1\). It does not classify all fixed points, all global attractors, or nonlinear dynamics at the two flip-neutral thresholds. The window of steps exhibiting reentrance is nonempty but close to one. Broad historical priority under another terminology for full repulsive normalized softmax remains possible; no independent audit has been performed.

## References
- C. Altafini, *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers*, arXiv:2610.13518v1 (first posted 2026-10-09), https://arxiv.org/abs/2610.13518.
- Q. Gao, Z. Yang and X. Chen, *Nonequilibrium Phases of Repulsive Self-Attention: Chaos, Attention Condensation, and Emergent Locality*, arXiv:2609.28448v1 (first posted 2026-09-23), https://arxiv.org/abs/2609.28448.
