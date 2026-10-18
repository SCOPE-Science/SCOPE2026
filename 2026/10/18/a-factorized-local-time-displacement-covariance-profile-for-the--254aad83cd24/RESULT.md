# A factorized local-time–displacement covariance profile for the Brownian bridge

## Finding

Let \(B=(B_t)_{0\le t\le1}\) be a standard real Brownian bridge, normalized by \(\mathbb E B_sB_t=\min(s,t)-st\). Let \(L=L^0_1\) be its local time at zero under occupation-density normalization. For every \(0<t<1\), write \(R_t=|B_t|\). Then the following conditional construction and exact covariance identity hold simultaneously:

\[
L\mid(R_t=r)\ \overset{d}=\ \sqrt{r^2+2tE_1}+\sqrt{r^2+2(1-t)E_2}-2r,
\qquad r\ge0,
\]
where \(E_1,E_2\) are independent rate-one exponentials, and
\[
\boxed{\operatorname{Cov}(L,R_t)=-(1-\sqrt t)(1-\sqrt{1-t}).}
\]

The conditional law of \(L\) strictly decreases in first-order stochastic order as \(r\) increases. In particular, if \(f\) and \(g\) are bounded nondecreasing functions on \([0,\infty)\), then
\[
\operatorname{Cov}(f(L),g(R_t))\le0.
\]
For nonconstant nondecreasing functions (nonconstant on sets of positive probability under the relevant distributions), the inequality is strict. The covariance is strictly negative for every interior time and its absolute value is uniquely maximal at \(t=1/2\), where it equals \(3/2-\sqrt2\).

For every deterministic integrable weight \(w:[0,1]\to\mathbb R\), the signed weighted absolute-area functional \(A_w=\int_0^1 w(t)|B_t|\,dt\) satisfies
\[
\boxed{\operatorname{Cov}(L,A_w)
=-\int_0^1 w(t)(1-\sqrt t)(1-\sqrt{1-t})\,dt.}
\]
In particular this covariance is strictly negative for every nonnegative \(w\) that is not zero almost everywhere, and for constant unit weight it is \(1/3-\pi/8\).

## Assumptions and scope

The Brownian bridge is the centered continuous Gaussian process pinned at zero at times zero and one. Local time is the jointly continuous occupation density satisfying \(\int_0^1 f(B_s)\,ds=\int_{\mathbb R}f(x)L_1^x\,dx\) for nonnegative Borel \(f\), equivalently the semimartingale local time normalized by \((2\varepsilon)^{-1}\int_0^1\mathbf1_{\{|B_s|<\varepsilon\}}ds\to L\). No doubling convention for reflecting local time is used. The conditional representation uses a regular conditional distribution given \(R_t=r\), valid for all \(r\ge0\) by the continuous version. Covariances at \(t=0\) and \(t=1\) are zero and follow by continuity. Bounded increasing transforms guarantee existence; the ordering extends to unbounded transforms whenever expectations and covariance exist. The weighted-area statement is defined for \(w\in L^1[0,1]\) because the bridge supremum has finite moments.

## Proof

**1. Conditional law and ordering.** The Markov-bridge decomposition at fixed \(t\) makes the restrictions of the bridge to \([0,t]\) and \([t,1]\), conditional on \(B_t=x\), independent Brownian bridges from \(0\) to \(x\) of duration \(t\) and from \(x\) to \(0\) of duration \(1-t\). The standard endpoint-local-time density, in the above normalization, gives for either segment of duration \(u>0\)
\[
\Pr\{L_u^0>z\mid\text{endpoint magnitude }r\}
=\exp\!\left(-\frac{z^2+2rz}{2u}\right),\quad z\ge0.
\]
Time reversal supplies the same formula for the second segment. Since \(\Pr\{\sqrt{r^2+2uE}-r>z\}=\exp(-(z^2+2rz)/(2u))\) for a rate-one exponential \(E\), conditional independence proves the claimed two-exponential representation. Its two summands are strictly decreasing in \(r\) under a common pair \((E_1,E_2)\): for every \(u,E>0\), the derivative of \(\sqrt{r^2+2uE}-r\) is \(r/\sqrt{r^2+2uE}-1<0\). Thus \(r\mapsto\mathbb E[f(L)\mid R_t=r]\) is decreasing for every increasing \(f\); the covariance inequality follows from the oppositely ordered conditional expectation and \(g(R_t)\) (or the independent-copy covariance identity). With the stated nondegeneracy this gives strict inequality.

**2. Occupation-density calculation of the mixed first moment.** Let \(v_s=s(1-s)\), \(v_t=t(1-t)\), and \(c_{s,t}=\min(s,t)-st\). Condition the Gaussian pair \((B_s,B_t)\) on \(B_s=0\), and use the occupation-density approximation with nonnegative integrands followed by dominated convergence. Then
\[
\begin{aligned}
\mathbb E[L|B_t|]
&=\int_0^1 p_{B_s}(0)\mathbb E[|B_t|\mid B_s=0]ds\\
&=\frac1\pi\int_0^1\frac{\sqrt{v_sv_t-c_{s,t}^2}}{v_s}\,ds.
\end{aligned}
\]
The Gaussian determinant is \(s(t-s)(1-t)\) if \(s<t\), and \(t(s-t)(1-s)\) if \(s>t\). Splitting the integral at \(t\) therefore yields
\[
\begin{aligned}
I_-&=\frac{\sqrt{1-t}}\pi\int_0^t\frac{\sqrt{t-s}}{\sqrt{s}(1-s)}ds
=\sqrt{1-t}-(1-t),\\
I_+&=\frac{\sqrt t}\pi\int_t^1\frac{\sqrt{s-t}}{s\sqrt{1-s}}ds
=\sqrt t-t.
\end{aligned}
\]
For example, substituting \(s=t\sin^2\theta\) into the first integral reduces it to \(2t\int_0^{\pi/2}\cos^2\theta/(1-t\sin^2\theta)\,d\theta=\pi(1-\sqrt{1-t})\). The second identity follows by the change \(s\mapsto1-s\), \(t\mapsto1-t\). Thus \(\mathbb E[L|B_t|]=\sqrt t+\sqrt{1-t}-1\).

**3. Centering, shape and weighted areas.** By Gaussian occupation density, \(\mathbb EL=\int_0^1(2\pi s(1-s))^{-1/2}ds=\sqrt{\pi/2}\). Since \(B_t\sim N(0,t(1-t))\), \(\mathbb E|B_t|=\sqrt{2/\pi}\sqrt{t(1-t)}\). Subtracting the product of means gives \(\sqrt t+\sqrt{1-t}-1-\sqrt{t(1-t)}=-(1-\sqrt t)(1-\sqrt{1-t})\). Its magnitude equals \(1+q-\sqrt{1+2q}\), where \(q=\sqrt{t(1-t)}\); this is strictly increasing in \(q>0\) and \(q\) has a unique maximum at \(t=1/2\). Finally, Fubini for \(w\in L^1\), using finite moments of the bridge supremum and local time, proves the weighted identity. Integrating the kernel for unit weight gives \(1/3-\pi/8\).

## Verification

Run \(`python verify.py`\) with Python 3 and \(`mpmath`\) installed. The script evaluates the mixed Gaussian conditional-density integral by an independent numerical quadrature at ten interior times, evaluates six conditional local-time means from direct tail integration and from Gaussian Mills ratios, checks twelve strict monotonicity comparisons in the exponential coupling, and checks the exact integrated-area constant. All numerical tests passed at high precision. The general proof is analytic; numerical tests are finite corroboration and are not claimed as exhaustive verification of continuous parameter ranges.

## Relationship to prior work

Pitman's 1998 report, especially its endpoint conditional local-time law (equations (1), (3) and (13)), supplies the key previously known segment distribution. The conditional two-piece representation is obtained by applying that endpoint law to the two pieces of an interior-pinned bridge; it is **not** presented as a new endpoint distribution. Gittenberger and Louchard (2000) derive multi-level local-time densities indexed by spatial level, rather than a time-resolved covariance with interior modulus. Knight (2000) studies the **integrated** reflected-bridge area conditional on local time, rather than the entire deterministic-time covariance profile. A global area covariance may be implicit in Knight's more general results, and is given above as a consequence rather than as an independently novel identity. The quantitative time-indexed factorization and its all-weight consequence are the precise additions assessed here. Earlier broad diffusion identities may still imply or tabulate them in a different notation.

## Limitations

This is a theorem for a standard one-dimensional pinned bridge and its occupation-density-normalized local time; it is not a claim for arbitrary diffusions, nonzero endpoint bridges, Brownian excursion or other local-time conventions. Stochastic ordering is one-dimensional negative regression dependence at each fixed \(t\), not independence or negative association of the full temporal path. The pathwise monotonic coupling is for conditional laws indexed by \(r\), not a coupling of original bridge sample paths. The supporting endpoint conditional law is classical. A search of accessible primary literature and published result summaries found no displayed equivalent factorized time-profile formula, but literature completeness and independent novelty certification are not claimed.

## References

1. J. Pitman, *The distribution of local times of a Brownian bridge*, Technical Report 539, University of California, Berkeley, cover dated 3 November 1998; later Séminaire de Probabilités XXXIII (1999), 388–394. https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/539.pdf
2. F. B. Knight, *The moments of the area under reflected Brownian bridge conditional on its local time at zero*, Journal of Applied Mathematics and Stochastic Analysis 13 (2000), 99–124. DOI:10.1155/S1048953300000137. https://www.researchgate.net/publication/41448675_The_moments_of_the_area_under_reflected_Brownian_bridge_conditional_on_its_local_time_at_zero
3. B. Gittenberger and G. Louchard, *On the local time density of the reflecting Brownian bridge*, Journal of Applied Mathematics and Stochastic Analysis 13 (2000), 125–136. DOI:10.1155/S1048953300000149. https://www.maths.tcd.ie/EMIS/journals/HOA/JAMSA/Volume13_2/136.pdf
