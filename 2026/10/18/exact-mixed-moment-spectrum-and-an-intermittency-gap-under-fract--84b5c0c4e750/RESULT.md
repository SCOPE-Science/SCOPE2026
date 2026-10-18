# Exact mixed-moment spectrum and an intermittency gap under fractional batch resetting

## Finding

Consider \(N\ge2\) independent Brownian coordinates with diffusivity \(D>0\) and linear between-event drift \(\gamma X_i\). At the event times of a common Poisson clock of rate \(r>0\), an independently and uniformly sampled subset of \(m\in\{1,\ldots,N\}\) coordinates is multiplied by \(a\in(0,1)\); the other coordinates are unchanged. This combines *batch selection* with *fractional* (rather than complete) resetting.

Let \(p=m/N\). Assume the second-moment stability inequality
\[
 d_1:=rp(1-a^2)-2\gamma>0.
\]
There is then a unique stationary law. For \(1\le j\le N\), let \(H_j\) be the number of elements of a uniformly random \(m\)-subset of \(\{1,\ldots,N\}\) among its first \(j\) elements, and set
\[
 F_j=1-\mathbb E[a^{2H_j}]
 =1-\sum_h\frac{\binom jh\binom{N-j}{m-h}}{\binom Nm}a^{2h},\qquad
 d_j=rF_j-2j\gamma,\qquad b_j=rp(1-a^{2j})-2j\gamma.
\]
Binomial coefficients with inadmissible lower indices vanish. For every \(1\le k\le N\), the following statements are **exact, including their finiteness conditions**:
\[
 \boxed{\quad
 \mathbb E\left[\prod_{i=1}^k X_i^2\right]
 =\frac{(2D)^k k!}{\prod_{j=1}^k d_j}
 \quad\Longleftrightarrow\quad d_k>0,\quad}
\]
\[
 \boxed{\quad
 \mathbb E[X_1^{2k}]
 =\frac{(2k-1)!!(2D)^k k!}{\prod_{j=1}^k b_j}
 \quad\Longleftrightarrow\quad b_k>0.\quad}
\]
Here the displayed equalities apply in the finite regime; when the inequality fails, the respective nonnegative moment is infinite. Thus all orders of the *distinct-particle quadratic mixed-moment spectrum* and the matching one-particle even-moment spectrum are determined.

For every \(2\le k\le N\) and every **proper batch** \(1\le m<N\), the thresholds
\[
 \gamma_{\mathrm{pure},k}=\frac{rp(1-a^{2k})}{2k},
 \qquad
 \gamma_{\mathrm{joint},k}=\frac{rF_k}{2k}
\]
satisfy \(\gamma_{\mathrm{pure},k}<\gamma_{\mathrm{joint},k}\). Hence throughout the nonempty interval
\[
 \boxed{\quad
 \gamma_{\mathrm{pure},k}\le\gamma<\gamma_{\mathrm{joint},k},\quad}
\]
the unique stationary state has a **finite product of squared positions of \(k\) distinct particles** but an **infinite single-particle \(2k\)-th moment**. This separation disappears exactly for completely synchronized batches \(m=N\). In particular, stability of one-particle variance need not imply the existence of its fourth moment, even when the two-particle product of squares is integrable.

An exact weak-reset near-critical law makes the separation quantitative. Hold \(N,m,k,D,\lambda>0\) fixed, put \(a=1-s\), \(r=\lambda/(ps)\), \(\gamma=\lambda(1-\kappa s)\), and write \(u=(m-1)/(N-1)\). For each fixed \(\kappa>1/2+(k-1)u\),
\[
 \boxed{\quad
 \lim_{s\downarrow0}s^k\mathbb E\left[\prod_{i=1}^kX_i^2\right]
 =\frac{(2D/\lambda)^k}{\prod_{j=1}^k[2\kappa-1-2(j-1)u]}.\quad}
\]
For fixed \(1/2<\kappa<1/2+(k-1)u\), this mixed moment is infinite at all sufficiently small positive \(s\) (this interval is empty when \(m=1\)). The corresponding pure-moment boundary is \(\kappa=k-1/2\), strictly higher when \(m<N\). No assertion is made at either equality boundary in this limiting parametrization; the finite-\(s\) formulas above resolve it directly.

## Assumptions and scope

All rates are constant; event times are Poisson, event subsets are independently resampled, and between events the Brownian noises are independent of each other and of the event clock. The drift coefficient \(\gamma\) can be positive: the fractional catastrophes stabilize otherwise expanding linear motion. The model is on the real line, without particle-particle forces. The expectation always refers to the unique stationary law, not to a finite-time snapshot. Only moments of the forms explicitly stated above are classified; arbitrary mixed monomials and distributional tail constants are not claimed.

## Proof

**1. Stationary construction and integrability.** For each coordinate let \(N_i(t)\) count selected resets during a backward interval of length \(t\). Thinning makes its marginal intensity \(rp\). The two-sided stationary solution, conditioned on the entire marked event history, is centered Gaussian and has variance
\[
 V_i=2D\int_0^\infty e^{2\gamma t}a^{2N_i(t)}\,dt.
\]
Indeed the propagator from a time \(t\) in the past is \(e^{\gamma t}a^{N_i(t)}\), and independent Brownian increments yield the stated Itô-isometry integral. Since \(1-a^2<-2\log a\), the assumption \(d_1>0\) implies \(\gamma<-rp\log a\). The strong law \(N_i(t)/t\to rp\) therefore gives pathwise exponential decay of this propagator. The integral is finite almost surely, and coupling two solutions to the same marks and Brownian paths makes their difference decay almost surely. This proves existence and uniqueness of the stationary law in the stated regime. Conditional independence of the Gaussian coordinates gives
\[
 \mathbb E[\prod_{i=1}^kX_i^2\mid\text{marks}]=\prod_{i=1}^kV_i,
 \quad \mathbb E[X_1^{2k}\mid\text{marks}]=(2k-1)!!V_1^k.
\]

**2. Exact distinct-coordinate moments, including infinity.** Expand \(\mathbb E[\prod_{i=1}^kV_i]\) as a nonnegative \(k\)-fold integral over backward times. Divide the integral into the \(k!\) order regions. In one such region, after ordering the times increasingly, the successive interval lengths carry \(k,k-1,\ldots,1\) still-active coordinate factors. By independent Poisson increments the expectation over an interval of length \(t\) with \(j\) active factors is
\[
 \mathbb E[e^{2j\gamma t}a^{2H_j(t)}]
 =\exp\{-[r(1-\mathbb E a^{2H_j})-2j\gamma]t\}=e^{-d_jt}.
\]
Here \(H_j(t)\) is the sum of selected tagged coordinates over the Poisson marks in that interval. Exchangeability makes the factor depend only on \(j\). Tonelli's theorem converts each ordered region to \(\prod_{j=1}^k\int_0^\infty e^{-d_jt}\,dt\), which is \(\prod_jd_j^{-1}\) if all \(d_j>0\) and infinity otherwise. Multiplying by \((2D)^kk!\) yields the first formula with its exact necessity condition once Step 4 proves that \(d_k>0\) is equivalent to positivity of all the earlier \(d_j\).

**3. Exact pure moments.** In the same ordered-integral argument for \(V_1^k\), a time interval containing \(j\) factors receives multiplier \(a^{2j}\) whenever the single coordinate is selected. Its Poisson transform is \(\exp\{-[rp(1-a^{2j})-2j\gamma]t\}\). Consequently
\[
 \mathbb E[V_1^k]=(2D)^kk!\prod_{j=1}^kb_j^{-1}
\]
when all denominators are positive and infinity otherwise. Multiplication by the conditional Gaussian factor \((2k-1)!!\) gives the second formula. The decreasing-slope argument of Step 4 also applies to \(j\mapsto p(1-a^{2j})\), so the last denominator alone characterizes finiteness.

**4. Last-order tests and strict separation.** For one reset subset \(S\), set \(I_i=\mathbf1_{\{i\in S\}}\) and \(H_j=\sum_{i=1}^jI_i\). The increments of \(F_j=\mathbb E[1-a^{2H_j}]\) are
\[
 F_{j+1}-F_j=(1-a^2)\mathbb E[I_{j+1}a^{2H_j}].
\]
By exchangeability, the next increment replaces the last factor by \(I_{j+1}a^{2H_j}a^{2I_{j+2}}\); it cannot be larger. Hence \(F_0=0\) and \(F_j\) is concave in the integer argument, so \(F_j/j\) is nonincreasing. It follows immediately that \(d_k>0\) implies \(d_j>0\) for all \(j\le k\); the converse is tautological. The same proof, or elementary convexity, applies to \(p(1-a^{2j})\).

For fixed \(k\ge2\), strict convexity of \(h\mapsto a^{2h}\) places its graph strictly below the chord joining \(h=0\) and \(h=k\) at every integer \(0<h<k\). Thus
\[
 \mathbb E[a^{2H_k}]\le1-\frac{\mathbb EH_k}{k}(1-a^{2k})
 =1-p(1-a^{2k}),
\]
with strict inequality whenever \(\mathbb P(0<H_k<k)>0\). This probability is positive for all \(k\ge2\) and \(1\le m<N\), because some admissible subset meets but does not contain the full tagged set. Therefore \(F_k>p(1-a^{2k})\), proving the strictly positive parameter interval. Its upper endpoint is at most \(rp(1-a^2)/2\), by concavity, so throughout the claimed interval \(d_1>0\) and the stationary construction applies. For \(m=N\), every selected subset is full, \(H_k=k\), and the two thresholds coincide.

**5. Singular weak-reset scaling.** For fixed \(j,N,m\), writing \(q=m(m-1)/(N(N-1))\), hypergeometric first and factorial-second moments give \(\mathbb EH_j=jp\) and \(\mathbb E[H_j(H_j-1)]=j(j-1)q\). Consequently
\[
 F_j=2jp\,s-[jp+2j(j-1)q]s^2+O(s^3),
\]
and in the stated scaling
\[
 d_j=\lambda js[2\kappa-1-2(j-1)q/p]+O(s^2).
\]
The exact moment formula and the monotonicity of its last-order threshold yield the limiting product and the strict off-boundary divergence regime. Likewise \(b_j=\lambda js[2\kappa-(2j-1)]+O(s^2)\), giving the pure boundary. All expansions are finite polynomials in \(s\) for the fixed finite model; no uncontrolled continuum approximation is used.

## Verification

The accompanying standalone Python program `verify.py` checks the hypergeometric reset transform against independent exact subset enumeration, verifies discrete concavity, verifies both stationary moment-generator recursions with exact rational arithmetic, constructs exact parameter witnesses of the strict mixed/pure separation, and checks the weak-reset coefficient against the finite-\(s\) formulas. Its run reported 817 exact-combinatorial/recurrence/strict-band cases plus four critical-window checks. These checks test the proof but do not replace the arbitrary-\(N\) Tonelli and concavity arguments.

For example, with \(N=3\), \(m=2\), \(a=1/2\), \(r=D=1\), and \(k=2\), the pure-fourth threshold is \(5/32\), the two-coordinate mixed threshold is \(13/64\), and choosing \(\gamma=23/128\) gives \(\mathbb E[X_1^2X_2^2]=16384/27\) but \(\mathbb E[X_1^4]=\infty\). The second moment is finite.

## Relationship to prior work

Galla (arXiv:2602.21635, first posted 25 February 2026) develops a diffusion approximation for frequent weak fractional resets and explicitly computes lower-order correlations for a fully synchronized multiparticle example; the paper's conclusion proposes studying multiparticle *batch* resetting. Its approximation does not establish finite-rate mixed-moment integrability boundaries or the exact all-order product formula here. De Mauro, Majumdar and Schehr (arXiv:2601.20077, first posted 27 January 2026) analyze *batch* selection with **complete** resets to zero and derive exact stationary and time-dependent correlations. Their paper explicitly distinguishes complete batch resetting from fractional resetting. The present exact moments use **both fractional amplitudes and proper random batches**, with a linearly expanding drift in the intermittent regime; neither cited formulation implies these stationary moment thresholds under its stated hypotheses. A general linear jump-process moment theorem could potentially yield related recurrences; no claim is made that the underlying generator or Poisson transform is new.

## Limitations

The theorem is confined to symmetric uniform-size batch selection, independent Brownian noises, fixed partial-reset factor, linear drift, and stationary moments of the two specified forms. It does not establish pointwise density tails, first-passage laws, or behavior at the weak-reset limiting equality values without using the finite-size exact criterion. The finite-state enumeration tests are not an exhaustive literature search or a proof of originality. Prior work on linear multiplicative jump systems may contain a more general statement that implicitly covers this special model; this remains a residual literature risk. No independent scientific audit has been performed.

## References

1. T. Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635 (first public version 2026-02-25), https://arxiv.org/html/2602.21635 . Main text and supplemental sections S1–S2 examined.
2. G. de Mauro, S. N. Majumdar and G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077 (first public version 2026-01-27), https://arxiv.org/pdf/2601.20077 . Main model, moment/correlation analysis and supplemental derivations examined.
3. S. C. Manrubia and D. H. Zanette, *Stochastic multiplicative processes with reset events*, Physical Review E 59 (1999), 4945–4951, DOI:10.1103/PhysRevE.59.4945. Abstract consulted as broader background, not treated as a full-text exclusion.
