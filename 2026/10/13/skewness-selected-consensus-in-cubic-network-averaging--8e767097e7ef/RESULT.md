# Skewness-selected consensus in cubic network averaging

## Finding

A symmetric complete influence graph does not in general conserve the population's mean opinion when interactions include a cubic disagreement term. The limiting consensus, rather than the one-step increment alone, has a universal leading displacement determined by the initial centered third moment. Precisely, for the discrete minimally nonlinear update below,
\[
 m_\infty-m_0=\frac{b}{N(1-\lambda^3)}\sum_{i=1}^N z_i(0)^3+R,
 \qquad |R|\leq\frac{6b^2\delta^5}{(1-|\lambda|)(1-\theta^3)}.
\]
For three or more agents, nonzero cubic skewness produces a signed consensus shift even on a doubly stochastic complete graph. For two agents the mean is conserved exactly.

## Assumptions and scope

Fix any integer \(N\geq2\), any cubic coefficient \(a>0\), and any step parameter \(0<\gamma<2(N-1)/N\). Opinions \(v_t\in\mathbb R^N\) evolve deterministically by
\[
 v_{t+1}=v_t-\gamma Cv_t+\gamma a(Cv_t)^{\circ3},\qquad C=I-W,\quad W=(J-I)/(N-1).
\]
Here \(J\) is the all-ones matrix and the cube is componentwise. The fixed points \(m\mathbf1\) form a translation-invariant consensus line. Define
\[
 c=\frac N{N-1},\quad \lambda=1-\gamma c\in(-1,1),\quad b=\gamma ac^3>0,\quad
 m_t=\frac1N\sum_i v_{i,t},\quad z_t=v_t-m_t\mathbf1,
\]
with \(\delta=\|z_0\|_\infty\), \(\theta=(1+|\lambda|)/2\), and the explicit small-disagreement condition \(\delta^2\leq(\theta-|\lambda|)/(2b)\). There is no restriction on the initial common mean. These conditions concern an open neighborhood of the consensus line and do not assert global attraction for arbitrary disagreement.

## Proof

**Exact mean and centered equations.** Since \(C=c(I-J/N)\), \(Cv_t=cz_t\) and \(\sum_i z_{i,t}=0\). Set \(s_3(z)=N^{-1}\sum_i z_i^3\). Taking the mean and subtracting it from the network update gives the exact, *unrestricted* identities
\[
 m_{t+1}=m_t+b\,s_3(z_t),\qquad
 z_{t+1}=\lambda z_t+bq(z_t),\quad q_i(z)=z_i^3-s_3(z).
\]
The source paper's mean-conservation conclusion is explicitly conditional on vanishing cubic sum; no such condition is assumed here.

**Contraction.** For every vector, \(\|q(z)\|_\infty\leq2\|z\|_\infty^3\). Thus, under the stated small-disagreement inequality,
\[
 \|z_{t+1}\|_\infty\leq(|\lambda|+2b\delta^2)\|z_t\|_\infty\leq\theta\|z_t\|_\infty.
\]
Induction yields \(\|z_t\|_\infty\leq\delta\theta^t\). The increments in \(m_t\) are absolutely summable, so all coordinates approach \(m_\infty\), and convergence is exponential.

**Coefficient and certified error.** Let \(e_t=z_t-\lambda^tz_0\). Variation of constants, followed by summation in nonnegative indices, gives
\[
 \sum_{t=0}^\infty\|e_t\|_\infty
 \leq 2b\delta^3\sum_{k=0}^\infty\theta^{3k}\sum_{j=0}^\infty|\lambda|^j
 =\frac{2b\delta^3}{(1-\theta^3)(1-|\lambda|)}.
\]
Both \(z_t\) and \(\lambda^tz_0\) have coordinate absolute values at most \(\delta\). The elementary factorization of a difference of cubes then shows
\[
 |s_3(z_t)-\lambda^{3t}s_3(z_0)|\leq3\delta^2\|e_t\|_\infty.
\]
Summing \(m_{t+1}-m_t=b s_3(z_t)\) and the geometric series \(\sum_{t\geq0}\lambda^{3t}=1/(1-\lambda^3)\) establishes the claimed coefficient and the explicit fifth-order remainder bound.

**Dimension threshold and sign.** When \(N=2\), the centered components are \((h,-h)\), so \(s_3(z_t)=0\) identically for every state and time; therefore \(m_t=m_0\) without the small-disagreement hypothesis. When \(N\geq3\), take \(z_0=(2h,-h,-h,0,\ldots,0)\). Then \(\sum_i z_i(0)^3=6h^3\), giving
\[
 m_\infty-m_0=\frac{6b}{N(1-\lambda^3)}h^3+O(h^5).
\]
Because \(b>0\) and \(1-\lambda^3>0\), this has the same strict sign as \(h\) for all sufficiently small nonzero \(h\). The result holds for both signs of the linear contraction factor, including alternating convergence.

## Verification

Run the standalone standard-library script `verify.py` with Python 3. It checks the center/mean identity in exact rational arithmetic for finite examples, the exact cubic coefficient from the initial skewness, and decreasing numerical fifth-order remainders on a three-agent example. The unrestricted theorem is supplied by the analytic argument above; finite checks alone are not an infinite proof. No external data or packages are needed.

## Relationship to prior work

Kumar and Yao, arXiv:2608.09724v1, introduce this minimally nonlinear network update and explicitly derive the *one-step* mean increment as a cubic sum in their Section III, equations around their Lemma 1. Their analysis then restricts to balanced zero-cubic-sum trajectories on which the mean stays fixed. The present theorem instead characterizes the **eventual consensus location for nonbalanced initial conditions**, with a quantified cubic coefficient and rigorous remainder for every finite population size. It neither presents the one-step identity as new nor claims that general weakly nonlinear perturbation methods are new.

Cannon, Bondurant, Whyte, and Scheel, arXiv:2302.04214, study bias-induced drift in a different bounded-confidence kinetic lattice model; their macroscopic drifting parties are not this exact finite-dimensional synchronous cubic map, and their theorems do not furnish its third-moment consensus-selection coefficient. General work on symmetric and nonlinear averaging addresses different interaction rules or qualitative consensus, not this particular coefficient. These comparisons do not rule out unidentified work applying generic center-manifold expansions to this precise system.

## Limitations

The estimate is local in initial disagreement, for a fixed finite \(N\), fixed \(a\), and a step strictly inside the linear consensus-stability interval. It does not give global basins, uniform control as \(|\lambda|\to1\), or stochastic finite-population assertions. The \(O(h^5)\) notation means a parameter-dependent bounded fifth-order remainder; the displayed inequality is the effective version. The coefficient is a model-specific Taylor effect, not a universal law for other nonlinear update rules. Independent validation has not been performed.

## References

1. R. Kumar and N. Yao, *Analysis and Consensus Control of Emergent Dynamic Polarization in Minimally-Nonlinear Opinion Dynamics*, arXiv:2608.09724v1, 2026-08-10. https://arxiv.org/html/2608.09724v1
2. O. Cannon, T. Bondurant, M. Whyte, A. Scheel, *Shifting consensus in a biased compromise model*, arXiv:2302.04214, 2023. https://ar5iv.labs.arxiv.org/html/2302.04214
