# A sharp fixed-Poisson phase boundary for zero–two atom reversals

## Finding

Let \(Z\sim\operatorname{Poisson}(\lambda)\), with \(\lambda>0\), and let \(B_1,\ldots,B_m\) be independent Bernoulli random variables of probabilities \(p_1,\ldots,p_m\in[0,1]\), independent of \(Z\). Here \(m\) is any finite nonnegative integer. Write \(S=Z+\sum_i B_i\) and \(\alpha=\sum_i p_i\).

**A sharp one-coin envelope.** For each fixed \(0<\alpha<1\), the bound
\[
\frac{\Pr(S=2)}{\Pr(S=0)}\le \frac{\lambda^2}{2}+\frac{\lambda\alpha}{1-\alpha}
\]
holds for **every** Bernoulli profile of total mean \(\alpha\) if and only if
\[
\lambda\ge g(\alpha):=\frac{1-\alpha}{2-\alpha}.
\]
Equality is attained by a single nonzero coin of parameter \(\alpha\). Above the phase boundary, this is the only equality configuration, up to zero-probability coins. On the boundary \(\lambda=g(\alpha)\), equality holds exactly for configurations with at most two nonzero coins. Below the boundary, every nontrivial division of \(\alpha\) between two coins gives a strictly larger ratio than the one-coin value.

**The exact prescribed-rate reversal threshold.** For \(0<\lambda<\sqrt2\), set
\[
 c_\lambda=1-\frac{\lambda^2}{2},\qquad
 a_\lambda=\frac{c_\lambda}{\lambda+c_\lambda}.
\]
Then
\[
\inf\left\{\mathbb ES:\ m<\infty,\ p_i\in[0,1],\ \Pr(S=2)>\Pr(S=0)\right\}
=\lambda+a_\lambda.
\]
At the boundary \(\alpha=a_\lambda\), equality \(\Pr(S=2)=\Pr(S=0)\) occurs precisely when one coin has parameter \(a_\lambda\) and all other parameters vanish. Consequently the infimum for **strict** reversal is not attained in this regime. At \(\lambda=\sqrt2\), the threshold infimum is \(\lambda\), pure Poisson gives equality and arbitrarily small positive Bernoulli mass gives strict reversal. At \(\lambda>\sqrt2\), the threshold infimum is \(\lambda\) and pure Poisson already satisfies strict reversal.

## Assumptions and scope

The Poisson rate is externally fixed rather than optimized, and the number and success probabilities of independent Bernoulli summands may vary subject to finite length and the stated constraints. Ratios of point probabilities are used only when \(\alpha<1\), so all \(p_i<1\) and \(\Pr(S=0)>0\). The threshold statement includes vectors with entries equal to one, handled separately by their mean. A zero-length Bernoulli vector is allowed. All probabilities are ordinary, unconditioned point masses of the independent sum.

## Proof

**1. Exact normalized point masses.** Set \(t_i=p_i/(1-p_i)\). The probability generating function is
\[
\mathbb E z^S=e^{\lambda(z-1)}\prod_{i=1}^m(1-p_i+p_i z).
\]
Dividing its coefficient at \(z^2\) by its positive constant coefficient gives
\[
R_\lambda(\boldsymbol p):=\frac{\Pr(S=2)}{\Pr(S=0)}
=\frac{\lambda^2}{2}+\lambda\sum_i t_i+\sum_{i<j}t_it_j.\tag{1}
\]

**2. Pair-merging identity.** For two positive parameters \(x,y\) with \(s=x+y<1\), replace \((x,y)\) by \((s,0)\). Let \(T\) denote the sum of odds of the unaffected coordinates. Direct rational algebra gives
\[
\frac{s}{1-s}-\frac{x}{1-x}-\frac{y}{1-y}
=\frac{x}{1-x}\frac{y}{1-y}\frac{2-s}{1-s}.
\]
Using (1), the increase in the zero–two ratio is exactly
\[
 R_\lambda(s,0,\boldsymbol r)-R_\lambda(x,y,\boldsymbol r)
=\frac{x}{1-x}\frac{y}{1-y}
 \left[\frac{2-s}{1-s}(\lambda+T)-1\right].\tag{2}
\]
Its sign is the sign of \(\lambda+T-g(s)\), with \(g(s)=(1-s)/(2-s)\).

**3. Global one-coin envelope and equality cases.** Fix \(0<\alpha<1\) and \(\lambda\ge g(\alpha)\). The unaffected odds obey \(T\ge\alpha-s\). Moreover \(h(s)=g(s)-(\alpha-s)\) has derivative
\[
h'(s)=1-\frac1{(2-s)^2}>0\quad(0<s<1),
\]
so \(g(s)-(\alpha-s)\le g(\alpha)\) for \(s\le\alpha\). Therefore
\[
\lambda+T-g(s)\ge\lambda+\alpha-s-g(s)\ge\lambda-g(\alpha)\ge0.
\]
Repeatedly merge positive pairs. This leaves a single Bernoulli parameter \(\alpha\) without decreasing (1), proving the bound. If \(\lambda>g(\alpha)\), each merger of two strictly positive parameters is strictly increasing. If \(\lambda=g(\alpha)\), (2) vanishes for a merger exactly when there are no other strictly positive coordinates, i.e. \(s=\alpha\). Thus one- and two-coin profiles are the only boundary equality cases.

Conversely, if \(\lambda<g(\alpha)\), choose any \(x,y>0\) with \(x+y=\alpha\). Equation (2) with \(T=0\) is strictly negative, so the split profile has larger ratio than the single coin. This proves both necessity and all equality cases of the phase diagram.

**4. Fixed-rate minimal mean.** Let \(0<\lambda<\sqrt2\). For one coin of parameter \(a\in[0,1)\), equation (1) becomes
\[
 R_\lambda(a)=\frac{\lambda^2}{2}+\frac{\lambda a}{1-a}.
\]
This is strictly increasing in \(a\), and equals one exactly at \(a=a_\lambda\in(0,1)\). Since \(c_\lambda>0\), we have \(1-a_\lambda=\lambda/(\lambda+c_\lambda)\) and \(2-a_\lambda=(2\lambda+c_\lambda)/(\lambda+c_\lambda)\). Consequently,
\[
g(a_\lambda)=\frac{\lambda}{2\lambda+c_\lambda}<\lambda,
\]
so the strict-equality case of step 3 applies at the threshold.

For every profile with \(\alpha=a_\lambda\), step 3 yields \(R_\lambda\le1\), with equality only for one nonzero coin. If \(\alpha<a_\lambda\), adjoin an independent coin with parameter \(a_\lambda-\alpha\); the enlarged profile has mean \(a_\lambda\) and obeys the bound. Equation (1) shows that adjoining this coin strictly raises \(R_\lambda\), because \(\lambda>0\). Therefore the original ratio is strictly below one. Profiles with \(\alpha\ge1\) cannot challenge the threshold because \(a_\lambda<1\). A single coin with \(p>a_\lambda\) arbitrarily close to \(a_\lambda\) has ratio above one. These facts give the claimed sharp infimum and equality classification.

If \(\lambda=\sqrt2\), the pure Poisson ratio is one and any positive coin raises it. If \(\lambda>\sqrt2\), the pure Poisson ratio already exceeds one, and no Bernoulli profile can have mean less than \(\lambda\). These prove the remaining cases.

## Verification

The executable `verify.py` uses exact rational arithmetic for 10,390 assertions covering pair-merging identities, the entire phase boundary on rational parameter grids, strictness/equality distinctions, two-coin counterexamples below the boundary and fixed-rate threshold equality. Run `python verify.py` from the containing directory. These finite assertions are diagnostics; the infinite parameter statements follow from equations (1) and (2) and the inequalities in step 3. The proof does not depend on floating-point optimization, numerical limiting arguments, or unverified empirical extrapolation.

## Relationship to prior work

Kleiner, *Why Distance Two Is Exceptional for Poisson-Binomial Point Probabilities* (arXiv:2610.10664v1, 7 October 2026), studies sharp mean thresholds for distance-two point-mass reversals in finite Bernoulli sums; its extension allowing a Poisson component concerns a rate that is free to vary. Here the rate is prescribed, and the result identifies an additional exact phase boundary determining when a single Bernoulli summand globally maximizes the zero–two ratio at fixed Bernoulli mean. Kleiner's unrestricted-rate threshold does not determine the sharp prescribed-rate value.

Gnedin, *Cross Modality of the Extended Binomial Sums* (arXiv:2408.06477v1, 12 August 2024), develops the general Poisson-plus-Bernoulli family, likelihood geometry and mean/mode transport. Its mode-transport analysis concerns equality of adjacent modal probabilities, not the global fixed-rate zero–two ratio envelope (1), the splitting boundary, or the corresponding exact prescribed-rate strict-reversal threshold. Standard coefficient expansions for Poisson and Bernoulli sums are prior ingredients; the claim is the sharp envelope and its optimizers.

## Limitations

The envelope is classified for \(0<\alpha<1\); it makes no assertion about maximizing the ratio at larger fixed Bernoulli mean. The strict-reversal threshold is treated only for the comparison of atoms zero and two and for fixed \(\lambda>0\). The proof allows any finite number of independent Bernoulli summands but does not address dependence among them. The phase diagram is a self-contained exact mathematical statement; independent priority validation has not been performed.

## References

1. I. Kleiner, *Why Distance Two Is Exceptional for Poisson-Binomial Point Probabilities*, arXiv:2610.10664v1 (submitted 7 October 2026). https://arxiv.org/abs/2610.10664
2. A. Gnedin, *Cross Modality of the Extended Binomial Sums*, arXiv:2408.06477v1 (submitted 12 August 2024). https://arxiv.org/pdf/2408.06477
3. W. Hoeffding, *On the Distribution of the Number of Successes in Independent Trials*, Annals of Mathematical Statistics 27 (1956), 713–721.
