# Lattice plateaus in horizon-optimal flattened Bernoulli e-tests
## Finding
Consider simple Bernoulli hypotheses \(P_0=\operatorname{Bern}(p_0)\) and \(P_1=\operatorname{Bern}(p_1)\) with \(0<p_0<p_1<1\). Let \(R=dP_1/dP_0\), let \(\alpha\in(0,1)\), and for \(\beta>0\) use the normalized power-likelihood e-variable
\[
E_\beta=\frac{R^\beta}{\mathbb E_{P_0}[R^\beta]}.
\]
For the wealth process \(W_s^{(\beta)}=\prod_{i=1}^s E_\beta(X_i)\), define the finite-horizon sequential type-II error
\[
\gamma_t(\beta)=P_1\!\left(\max_{1\le s\le t}W_s^{(\beta)}<\alpha^{-1}\right).
\]
Then \(\gamma_t(\beta)\) is a piecewise-constant function of \(\beta\) with finitely many effective cells on \((0,\infty)\). Every cell boundary is a solution of an explicit scalar equation \(q_s(\beta)=k\) for some \(1\le s\le t\) and integer \(1\le k\le s\), where
\[
q_s(\beta)=\frac{\log(1/\alpha)+s\kappa(\beta)-\beta s\log r_0}{\beta\Delta},
\quad
\kappa(\beta)=\log\!\left(p_0r_1^\beta+(1-p_0)r_0^\beta\right),
\]
\[
r_1=\frac{p_1}{p_0},\qquad r_0=\frac{1-p_1}{1-p_0},\qquad \Delta=\log(r_1/r_0).
\]
Hence exact sequential type-II optimization over \(\beta\) is a finite staircase problem, not a smooth one-dimensional optimization problem.

For the concrete design
\[
p_0=\frac25,\qquad p_1=\frac35,\qquad \alpha=\frac1{20},\qquad t=30,
\]
complete enumeration of the effective cells gives the exact optimizer set
\[
\beta\in[\beta_-,\beta_+],
\]
where \(\beta_-\) is the left-branch solution of \(q_{10}(\beta)=8\) and \(\beta_+\) is the right-branch solution of \(q_{21}(\beta)=14\). Numerically,
\[
\beta_-=1.4377067867164328\ldots,\qquad
\beta_+=1.5201316458803258\ldots.
\]
Throughout this entire interval,
\[
\gamma_{30}(\beta)
=
\frac{424022988283968360448}{931322574615478515625}
=0.4552912168579588\ldots.
\]
The smooth fixed-horizon threshold criterion associated with the same flattened family has its stationary point at
\[
\beta_{\mathrm{smooth}}=1.1136398811625186\ldots,
\]
for these parameters, but its actual first-passage type-II error is
\[
\gamma_{30}(\beta_{\mathrm{smooth}})
=
\frac{448493759336008032256}{931322574615478515625}
=0.4815665072020623\ldots,
\]
which is strictly larger. Thus lattice path geometry can move the exact sequentially optimal tilt away from the smooth horizon optimizer and can make the optimum nonunique over a macroscopic interval.

## Assumptions and scope
The observations are i.i.d. under each simple Bernoulli hypothesis. The rejection rule is the genuine first-passage rule \(\max_{s\le t}W_s^{(\beta)}\ge\alpha^{-1}\), not merely a terminal comparison at time \(t\). The parameter \(\beta\) is fixed in advance. The theorem concerns the normalized power-likelihood family above; it does not claim optimality among all possible e-variables or all sequential tests.

The exact numerical optimizer interval is specific to \((p_0,p_1,\alpha,t)=(2/5,3/5,1/20,30)\). The structural finite-staircase theorem holds for every \(0<p_0<p_1<1\), \(\alpha\in(0,1)\), and positive integer \(t\).

## Proof
Let \(K_s=\sum_{i=1}^s X_i\). Since the Bernoulli likelihood ratio takes the two values \(r_1\) and \(r_0\),
\[
\log W_s^{(\beta)}
=
\beta\{K_s\log r_1+(s-K_s)\log r_0\}-s\kappa(\beta).
\]
Therefore \(W_s^{(\beta)}\ge\alpha^{-1}\) is equivalent to \(K_s\ge q_s(\beta)\), hence, because \(K_s\) is integer, to
\[
K_s\ge m_s(\beta),\qquad m_s(\beta)=\lceil q_s(\beta)\rceil.
\]
Thresholds above \(s\) are all equivalent, so define the effective boundary \(\bar m_s(\beta)=\min\{s+1,m_s(\beta)\}\). The event defining \(\gamma_t(\beta)\) depends on \(\beta\) only through the finite vector \((\bar m_1(\beta),\ldots,\bar m_t(\beta))\). Consequently \(\gamma_t\) is constant wherever that vector is constant.

It remains to show that only finitely many changes can occur. Write
\[
g(\beta)=\beta\kappa'(\beta)-\kappa(\beta).
\]
A direct differentiation gives
\[
q_s'(\beta)=\frac{s\,g(\beta)-\log(1/\alpha)}{\beta^2\Delta}.
\]
For nondegenerate Bernoulli hypotheses, \(\kappa''(\beta)>0\), so
\[
g'(\beta)=\beta\kappa''(\beta)>0.
\]
Thus each \(q_s\) is either strictly decreasing or decreases to one strict minimum and then increases. For every relevant integer level \(k\in\{1,\ldots,s\}\), the equation \(q_s(\beta)=k\) therefore has at most two positive solutions. Across \(1\le s\le t\), only finitely many effective boundary changes exist. Between consecutive changes, the full first-passage event is identical, proving the staircase claim.

For the displayed \(t=30\) example, every relevant root \(q_s(\beta)=k\) is isolated by monotonicity on the two sides of the unique minimum of \(q_s\). On each resulting cell, the survival probability is computed exactly by the recursion
\[
D_s(j)=\mathbf 1\{j<\bar m_s\}\left(\frac25D_{s-1}(j)+\frac35D_{s-1}(j-1)\right),
\]
with \(D_0(0)=1\) and out-of-range terms zero. Summing \(D_{30}(j)\) gives \(\gamma_{30}\). Exact rational arithmetic over all effective cells produces one minimizing plateau. Its left endpoint is the root \(q_{10}(\beta)=8\), its right endpoint is the root \(q_{21}(\beta)=14\), and the common exact probability is the fraction stated above.

The smooth comparison point solves
\[
g(\beta)=\frac{\log(1/\alpha)}{t},
\]
which gives \(\beta_{\mathrm{smooth}}=1.1136398811625186\ldots\). Replaying the same exact path recursion at the integer boundary vector induced by that tilt gives the second displayed fraction, strictly above the optimum.

## Verification
The standalone script `verify_plateau.py` reconstructs all relevant scalar roots using the proved one-minimum structure, checks root residuals and separation, enumerates every effective boundary cell through horizon \(30\), and computes every first-passage probability using exact `Fraction` arithmetic. It verifies the unique minimizing interval, both endpoint equations, the exact optimum fraction, the smooth stationary point, and the strict probability gap. Running

`python3 verify_plateau.py`

prints `VERIFY_OK`.

The computation is only used to certify the finite \(t=30\) example. The finite-staircase theorem is proved analytically above and does not rely on enumeration.

## Relationship to prior work
Forré (2026) studies type-II error for test supermartingales and highlights the normalized flattened likelihood-ratio family \(R^\beta/\mathbb E_{P_0}[R^\beta]\). Its horizon analysis singles out a smooth tilt, with the ordinary likelihood ratio at \(\beta=1\) at one transition horizon and sharpening or flattening on opposite sides. The present result keeps exactly that family but examines the exact Bernoulli first-passage event. Integer path boundaries turn the dependence on \(\beta\) into a staircase, and the displayed example shows that the exact sequential optimizer can be a whole interval separated from the smooth stationary point.

Exact binomial testing and randomized tests for discrete data are classical themes. Awan and Slavković (2018), for example, derive exact finite-sample binomial tests under differential privacy. That literature does not, in the inspected material, analyze the tilt parameter of normalized power-likelihood e-processes or the first-passage boundary-cell geometry above.

## Limitations
The structural theorem uses the two-point Bernoulli likelihood ratio. Multinomial or more general lattice models lead to higher-dimensional path regions and are not covered here. The numerical optimizer interval is not asserted to persist under perturbation of the design parameters, although the staircase mechanism itself is structural.

The originality search did not establish mathematical uniqueness in the literature. The principal residual risk is that the finite-cell observation may appear elsewhere under different terminology in work on discrete sequential likelihood-ratio boundaries. No such statement or the exact \(t=30\) optimizer interval was found in the inspected source, targeted database searches, or the comparison literature checked for this result.

## References
1. Patrick Forré, *The Type-II Error of Test Supermartingales: e-Power versus the Chernoff-Stein Exponent*, arXiv:2609.27765, first public version 2026-08-19.
2. Jordan Awan and Aleksandra Slavković, *Differentially Private Uniformly Most Powerful Tests for Binomial Data*, arXiv:1805.09236, 2018.
