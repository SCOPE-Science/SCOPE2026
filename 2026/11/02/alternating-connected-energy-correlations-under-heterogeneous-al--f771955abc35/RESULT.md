# Alternating connected-energy correlations under heterogeneous all-but-one resetting

## Finding

**Theorem (heterogeneous all-but-one reset hierarchy).** Let \(N\ge2\) and \(r>0\). Let particle \(i\) diffuse on the real line with generator \(D_i\partial_{x_i}^2\), where every \(D_i>0\), and independent Brownian drivers. At the times of an independent rate-\(r\) Poisson process, draw a label \(J\) independently with probabilities \(w_i\in(0,1)\), \(\sum_{i=1}^{N}w_i=1\), and reset every particle **except** \(J\) to zero. The selected particle is untouched. There is a unique stationary joint law.

Write \(Y_i=X_i^2/(2D_i)\) for the stationary, diffusion-normalized squared position and let \(I=\{i_1,\ldots,i_k\}\) be any set of \(k\) **distinct** labels, \(1\le k\le N\). Its joint cumulant is exactly

\[
\boxed{\kappa(Y_{i_1},\ldots,Y_{i_k})=\frac{(k-1)!}{r^k}\left[1+(-1)^{k-1}\prod_{i\in I}\frac{w_i}{1-w_i}\right].}
\]

For \(k\ge2\), the nontrivial correction has the **sharp** universal envelope

\[
0<\prod_{i\in I}\frac{w_i}{1-w_i}\le\frac{1}{(k-1)^k}.
\]

The upper bound is attained for \(N=k\) and all exemption probabilities equal to \(1/k\), with the additional \(k=2\) equality cases described below. For \(N>k\) with strictly positive weights, the bound is a supremum, not a maximum. In comparison, resetting all particles at each event of the same rate \(r\) gives \(\kappa_{\mathrm{all}}=(k-1)!/r^k\). Hence the **absolute, diffusion-normalized connected fluctuation** decreases for every even \(k\ge2\) and increases for every odd \(k\ge3\) when exactly one particle is spared. In particular, pairwise connected fluctuations are weakened while three-particle connected fluctuations are strengthened, independently of exposure heterogeneity.

The corresponding connected cumulant of the unnormalized squared displacements is obtained by multiplying by \(\prod_{i\in I}(2D_i)\). Normalizing instead by the product of the individual means gives the distinct formula

\[
\frac{\kappa(Y_{i_1},\ldots,Y_{i_k})}{\prod_{i\in I}\mathbb E Y_i}
=(k-1)!\left[\prod_{i\in I}(1-w_i)+(-1)^{k-1}\prod_{i\in I}w_i\right],
\]

which is nonnegative and strictly smaller than \((k-1)!\) for \(k\ge2\). Therefore enhancement of an *unnormalized* odd-order connected fluctuation must not be confused with enhancement after normalization by the enlarged one-particle variances.

## Assumptions and scope

The theorem concerns \(N\ge2\) free, independently driven one-dimensional Brownian particles, deterministic zero resets, a single homogeneous Poisson event stream of rate \(r>0\), and i.i.d. choices of the sole exempt particle with fixed strictly positive probabilities strictly below one. No particle interactions, confinement, age-dependent reset rates, or random reset positions are assumed. Cumulant arguments must reference distinct particle labels; repeated-label cumulants are not asserted. All statements refer to the unique stationary distribution, not transient fluctuations. The comparison with full resetting uses the same event rate and diffusion constants, not matched single-particle reset rates.

## Proof

**1. Stationarity and conditional Gaussian structure.** Construct a two-sided stationary marked Poisson process with rate \(r\) and independent categorical marks \(J\) of law \(w\), independent of all Brownian motions. Each coordinate \(i\) is reset on a thinned Poisson process of rate \(a_i=r(1-w_i)>0\); its last reset in the past exists almost surely. Brownian evolution from those last resets defines a stationary vector. Coupling two copies by using the same future Brownian drivers and reset events shows that they coincide once every coordinate has been reset, which occurs almost surely and has tail at most \(\sum_i e^{-a_i t}\). This proves uniqueness.

Let \(G\) be the backward time to the most recent global event. Then \(G\sim\operatorname{Exp}(r)\) and is independent of that event's exempt mark \(J\), which has law \(w\). All coordinates other than \(J\) were reset at this event and have age \(G\). Conditional on \(J=j\), the interval \(H\) from that event backward to the most recent event that did reset \(j\) is independent of \(G\) and exponential of rate \(a_j=r(1-w_j)\), by independent Poisson thinning. Thus the vector of ages has the exact representation

\[
A_i=G+\mathbf1_{\{J=i\}}H,\qquad
H\mid\{J=j\}\sim\operatorname{Exp}(r(1-w_j)).
\]

Conditional on the ages, the particle positions are independent centered Gaussians with variances \(2D_iA_i\). Consequently, for every set \(S\) of distinct labels,

\[
\mathbb E\prod_{i\in S}Y_i=\mathbb E\prod_{i\in S}A_i.
\]

The defining set-partition polynomial for a mixed cumulant uses only moments of these distinct-label subsets; therefore \(\kappa(Y_{i_1},\ldots,Y_{i_k})=\kappa(A_{i_1},\ldots,A_{i_k})\).

**2. Joint cumulant generating function.** In a neighborhood of the origin, for any set \(I\) of distinct labels and real parameters \(t_i\) sufficiently small,

\[
\mathbb E\exp\!\left(\sum_{i\in I}t_i A_i\right)
=\frac{r}{r-\sum_{i\in I}t_i}\left[1+\sum_{i\in I}\frac{w_i t_i}{r(1-w_i)-t_i}\right].
\]

The logarithm of the first factor gives the mixed derivative \((k-1)!/r^k\), including \(k=1\). Write \(b_i=w_i/[r(1-w_i)]\). In the logarithm of the second factor, the coefficient of \(\prod_{i\in I}t_i\) comes *only* from the \(k\)-th term of \(\log(1+u)=\sum_{j\ge1}(-1)^{j-1}u^j/j\), using exactly once the linear term \(b_it_i\) of each summand. Its coefficient is \((-1)^{k-1}(k-1)!\prod_{i\in I}b_i\). Taking the mixed derivative proves the displayed cumulant formula for all \(1\le k\le N\).

For completeness, the stationary characteristic function is

\[
\mathbb E\exp\!\left(i\sum_{i=1}^N s_iX_i\right)
=\frac{r}{r+\sum_{i=1}^ND_i s_i^2}
\sum_{j=1}^Nw_j\frac{r(1-w_j)}{r(1-w_j)+D_js_j^2}.
\]

This identity also displays the precise distinction from uniform selection of the exempt label.

**3. The sharp parity envelope.** Fix \(k\ge2\) selected labels. Since \(\sum_{i=1}^{N}w_i=1\), for each selected \(i\),

\[
1-w_i\ge\sum_{j\in I\setminus\{i\}}w_j\ge
(k-1)\left(\prod_{j\in I\setminus\{i\}}w_j\right)^{1/(k-1)}.
\]

Multiplication over \(i\in I\) gives \(\prod_{i\in I}(1-w_i)\ge(k-1)^k\prod_{i\in I}w_i\), proving the claimed bound. Equality requires no weight outside \(I\), and for \(k\ge3\) equal weights within \(I\). For \(k=2\), the arithmetic-geometric-mean inequality contains only a single term, so equality holds for any two positive weights summing to one. If \(N>k\), the upper bound is approached by sending the total weight outside \(I\) to zero while the weights on \(I\) approach \(1/k\). The alternating-sign conclusion follows from the exact cumulant formula. Finally, \(\mathbb EY_i=[r(1-w_i)]^{-1}\), giving the normalized formula. Its strict sub-unit bound for \(k\ge2\) follows by viewing \(\prod(1-w_i)+\prod w_i\) as the probability that \(k\) independent Bernoulli variables with success probabilities \(w_i\) are either all zero or all one, which is strictly less than one.

## Verification

Run `python3 verify.py` using Python 3.10 or newer; no external packages are required. The script independently obtains distinct-label joint age moments by a stationary generator recursion, converts those moments to cumulants using the set-partition formula, and compares the resulting exact rational numbers with the closed expression for multiple nonuniform weight vectors, dimensions, orders, and reset rates. It separately checks the sharp envelope, attainment at balanced weights, and heterogeneous diffusion rescaling. In the actual run the verifier reported **798 exact-rational checks passed**. This is finite corroboration, not a proof of the unrestricted statements; the full derivation above supplies the proof.

## Relationship to prior work

De Mauro, Majumdar and Schehr (2026) introduce the *uniformly sampled* batch-reset gas, prove an exact recursive stationary Fourier-marginal closure, and explicitly derive its full stationary joint characteristic function in the special case \(m=N-1\) (their supplement, equations S40–S43). Their two-particle correlation formula and its batch-size optimization are prior results. Those formulas already determine the uniform-exemption specialization of the present cumulants; **no novelty is claimed for that specialization in isolation**. Here the model allows arbitrary, fixed *unequal* exemptions and heterogeneous diffusivities, and the specific contribution is the full cross-particle mixed-cumulant hierarchy plus the optimal parity envelope over the weight simplex. The stationary single-clock simultaneous-reset gas and its conditional-independence representation were introduced earlier by Biroli, Larralde, Majumdar and Schehr (2023), and are acknowledged as the full-reset benchmark.

A general Markov-generator or Fourier-transform method could be specialized to obtain these results; no claim is made that the analytic tools are new. The searched research records and primary works did not establish the stated heterogeneous hierarchy and sharp envelope in the inspected material. This is a best-knowledge literature comparison, not a proof of worldwide priority.

## Limitations

Only stationary distinct-label cumulants of squared positions are treated. The law is not asserted for repeated-label cumulants, non-Poisson events, imperfect resets, correlated Brownian drivers, confinement, time-dependent weights, or spatially coupled particles. The improvement for odd orders is in absolute connected cumulants at a fixed global reset-event rate; the mean-normalized connected cumulants are smaller, as the theorem explicitly shows. While the analytic proof is complete under its hypotheses, independent scientific validation and literature-wide priority certification have not been performed.

## References

1. G. de Mauro, S. N. Majumdar and G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077 (first public 2026-01-27), especially the main-text marginal closure and supplementary equations S40–S43. https://arxiv.org/abs/2601.20077 ; full accessible text: https://arxiv.org/html/2601.20077v3
2. M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, *Physical Review Letters* **130**, 207101 (2023), arXiv:2211.00563. https://arxiv.org/abs/2211.00563
3. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, *Physical Review E* **113**, 014120 (2026), arXiv:2509.06658. https://arxiv.org/abs/2509.06658
