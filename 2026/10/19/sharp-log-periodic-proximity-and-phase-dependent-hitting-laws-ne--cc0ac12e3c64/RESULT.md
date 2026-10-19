# Sharp log-periodic proximity and phase-dependent hitting laws near a Cantor singular set

## Finding
For the centered affine Cantor-gap expanding map defined below, let \(m_r\) be its normalized invariant conformal measure and let \(C\) be the middle-third Cantor set. For every real \(r>3\), put
\[
\delta=\frac{\log(3/2)}{\log3},\qquad D(x)=\operatorname{dist}(x,C),\qquad q=\frac23.
\]
The invariant probability of a small singular-set neighborhood obeys the **sharp, unequal** asymptotic envelopes
\[
\liminf_{\varepsilon\downarrow0}\frac{m_r(D<\varepsilon)}{\varepsilon^\delta}=2^\delta,
\qquad
\limsup_{\varepsilon\downarrow0}\frac{m_r(D<\varepsilon)}{\varepsilon^\delta}=\frac32\,2^\delta.
\]
For every fixed \(f\in(0,1)\), on the geometric scales \(\varepsilon_{j,f}=\tfrac12 3^{-(j+f)}\) there is an integer \(j_0(r,f)\) such that for every integer \(j\ge j_0\),
\[
m_r(D<\varepsilon_{j,f})=q^j,
\qquad
\frac{m_r(D<\varepsilon_{j,f})}{\varepsilon_{j,f}^\delta}
=2^\delta(3/2)^f.
\]
Define the first hitting time \(\tau_\varepsilon(x)=\min\{n\ge1:D(T^{n-1}x)<\varepsilon\}\). On those same scales, for every nonnegative integer \(N\), its **entire** law is exactly
\[
m_r(\tau_{\varepsilon_{j,f}}>N)=(1-q^j)^N.
\]
Consequently, for every fixed \(t\ge0\) and \(f\in(0,1)\),
\[
\lim_{j\to\infty}m_r\!\left(\varepsilon_{j,f}^{\delta}\tau_{\varepsilon_{j,f}}>t\right)
=\exp\!\left[-2^\delta(3/2)^f t\right].
\]
The scale-normalized entrance law therefore has no phase-independent limit as arbitrary \(\varepsilon\downarrow0\). In contrast, normalization by the *actual* target mass has the usual mean-one exponential limit. These conclusions hold uniformly in the sense of validity of the formulas for each fixed \(r>3\), but do not assert uniform asymptotics as \(r\downarrow3\).

## Assumptions and scope
Work on \([0,1]\), rather than the affinely equivalent \([-1,1]\) interval. At level \(k\ge1\), the standard middle-third Cantor construction removes \(2^{k-1}\) disjoint open gaps \(G_{k,j}\) of length \(3^{-k}\), with centers \(c_{k,j}\). Fix \(r>3\). In each gap choose the **centered** closed interval
\[
J_{k,j}=c_{k,j}+r^{-k}[-\tfrac12,\tfrac12],
\quad 1\le j\le2^{k-1}.
\]
The intervals are pairwise disjoint because \(r^{-k}<3^{-k}\). Define inverse branches \(\psi_{k,j}:[0,1]\to J_{k,j}\) and the piecewise expanding map \(T\) by
\[
\psi_{k,j}(x)=c_{k,j}+r^{-k}(x-\tfrac12),
\quad T|_{J_{k,j}}=\psi_{k,j}^{-1}.
\]
Write \(W=\bigcup_{k,j}J_{k,j}\), \(\Lambda=\{x\in W:T^n(x)\in W\text{ for every }n\ge0\}\), and \(C=\overline W\setminus W\). The last equality holds since branch centers are dense at the Cantor set and the branch intervals lie strictly inside separate removed gaps. On \(\Lambda\), the coding by all infinite branch sequences is unique. The similarity dimension
\[
s=\frac{\log3}{\log r}\in(0,1)
\]
is the unique root of \(\sum_{k\ge1}2^{k-1}r^{-ks}=1\). The normalized \(s\)-conformal measure \(m_r\) is the pushforward of the Bernoulli measure with one-symbol weights \(r^{-ks}=3^{-k}\), independently of \(j\). It is also \(T\)-invariant, since each inverse branch is a similarity, and the first-coordinate branch sequence is iid. We use strict neighborhoods \(D<\varepsilon\); changing the convention at isolated critical radii does not affect the asserted limits.

## Proof
**1. Exact symbolic weights.** Each level-\(k\) branch has mass \(3^{-k}\), and there are \(2^{k-1}\) such branches, so the level \(K\) of the current point obeys
\[
\mathbb P(K=k)=2^{k-1}3^{-k}
=\frac13\left(\frac23\right)^{k-1},
\quad
\mathbb P(K\ge j+1)=q^j.
\]
The same law holds independently at every iterate of \(T\) because the probability of an arbitrary finite coding cylinder is the product of its similarity factors raised to \(s\). This is an identity for the present explicitly defined map, not a universal feature of nonaffine countable maps.

**2. Gap geometry.** On the entire centered branch interval \(J_{k,j}\), the nearest points of \(C\) are the two endpoints of the parent gap. Therefore every such \(x\) satisfies
\[
a_k^-:=\frac{3^{-k}-r^{-k}}2\le D(x)
\le\frac{3^{-k}+r^{-k}}2=:a_k^+.
\]
(The actual maximum is \(3^{-k}/2\); the displayed slightly looser upper bound is convenient.) Both \(a_k^-\) and \(a_k^+\) decrease strictly with \(k\ge1\). For the lower sequence, this follows from \(2(r/3)^{k+1}>r-1\), which at \(k=1\) reduces to \((2r-3)(r-3)>0\) after multiplying by \(9\), and strengthens with \(k\). Thus the bounds allow whole levels to be compared monotonically.

**3. Eventual exactness along geometric phases.** Fix \(f\in(0,1)\). With \(\varepsilon_{j,f}=3^{-j-f}/2\), since \((3/r)^j\to0\), for sufficiently large \(j\) we have
\[
a_{j+1}^+<\varepsilon_{j,f}<a_j^-.
\]
By the monotonicity in step 2, every point in a level \(k\ge j+1\) branch is within \(\varepsilon_{j,f}\) of \(C\), and every point in a level \(k\le j\) branch lies outside. The neighborhood event is *exactly* \(K\ge j+1\), apart from no points because the inequalities are strict. Step 1 gives mass \(q^j\). The phase amplitude follows from \(3^{-\delta}=q\):
\[
\frac{q^j}{(3^{-j-f}/2)^\delta}=2^\delta 3^{f\delta}=2^\delta(3/2)^f.
\]

**4. Complete lower and upper envelopes.** Define the ideal geometric step function
\[
S(\varepsilon)=\mathbb P\big(3^{-K}/2<\varepsilon\big)
=q^{\lfloor\log_3(1/(2\varepsilon))\rfloor}
\]
for sufficiently small \(\varepsilon>0\). Its normalized value is
\[
\frac{S(\varepsilon)}{\varepsilon^\delta}
=2^\delta(3/2)^{\{\log_3(1/(2\varepsilon))\}},
\]
where the braces denote fractional part, hence its sharp limiting envelopes are \(2^\delta\) and \(3\,2^\delta/2\). To pass from ideal branch centers to all points of \(\Lambda\), fix \(\eta\in(0,1)\). For all sufficiently large \(k\), \((3/r)^k\le\eta\), so \((1-\eta)3^{-k}/2\le D(x)\le(1+\eta)3^{-k}/2\) on every level-\(k\) branch. Finitely many small levels are irrelevant for sufficiently small \(\varepsilon\). Consequently,
\[
S\left(\frac{\varepsilon}{1+\eta}\right)
\le m_r(D<\varepsilon)
\le S\left(\frac{\varepsilon}{1-\eta}\right).
\]
Dividing by \(\varepsilon^\delta\) and letting first \(\varepsilon\downarrow0\), then \(\eta\downarrow0\), gives a lower bound \(2^\delta\) on the liminf and an upper bound \(3\,2^\delta/2\) on the limsup. By step 3, fixed phase limits attain \(2^\delta(3/2)^f\); letting \(f\downarrow0\) or \(f\uparrow1\) gives the reverse inequalities, proving both sharp envelopes.

**5. Exact first visits and phase-dependent limits.** Along a fixed phase, the target event depends only on the first branch-level symbol \(K\). The events at successive iterates are independent, each with probability \(q^j\). Hence the waiting time beginning at time zero has exact geometric survival probability \((1-q^j)^N\). For \(N=\lfloor t/\varepsilon_{j,f}^\delta\rfloor\), use \(q^j/\varepsilon_{j,f}^\delta=2^\delta(3/2)^f\) and \(q^j\to0\) to obtain the stated exponential limit. For \(t>0\), changing \(f\) changes the rate strictly, so no universal \(\varepsilon^\delta\)-normalized limit can hold. Replacing \(\varepsilon^\delta\) by \(m_r(D<\varepsilon)\) yields the standard mean-one exponential law along these phases. No first-hit limit at arbitrary intermediate radii is asserted here. \(\square\)

## Verification
The companion `verify.py` computes the upper/lower level bounds using exact fractions for integer parameters \(r\in\{4,5,7,11\}\), numerous cutoff levels and rational intermediate phases. It sums exact geometric branch masses and verifies phase-window inclusion, exclusion, and two-sided near-boundary masses. Independent floating-point diagnostics test amplitude identities and geometric-to-exponential approximation with a numerically stable logarithm. These finite checks do not replace the symbolic and geometric proof for all real \(r>3\).

## Relationship to prior work
Cunha–Novaes–Ponce, arXiv:2608.00398v1, Appendix B.1, constructs the triadic Cantor-gap infinite expanding system with the same level multiplicities and contraction factors; their Appendix computes its survivor dimension, and their Section 5.6 establishes conformal/invariant measures in the general class. **The system, dimension, conformality, and Bernoulli coding are prior work.** Our specialization chooses the canonical *centered* placement and determines the sharp singular-neighborhood conformal mass, the log-periodic oscillation amplitude and exact phase-dependent entrance clock. Keller's general exponential hitting-time theory supplies a broader conceptual normalization-by-measure framework, but not these constants for this singular-neighborhood target. Lapidus–Radunović–Žubrinić give fractal tube formulas and oscillations for Lebesgue-volume neighborhoods of fractals; this is a distinct, dynamically invariant probability measure and a first-hitting law. The geometric-tail and geometric-waiting mechanisms are elementary and classical; their exact synthesis at this singular-set boundary is the specific assessed contribution.

## Limitations
The result applies to centered affine branches, not arbitrary placements in the parent gaps, nonaffine inverse branches, nonstationary symbolic laws, or an arbitrary conformal measure. The first hitting time law is exactly geometric only for the separated whole-level windows. The sharp exponent \(\delta\) is a neighborhood-mass exponent, not the Hausdorff dimension \(s\) of the survivor or the dimension of \(C\). No assertion about stochastic perturbations or nontrivial extremal indices is made. Possible equivalent historical descriptions of these log-periodic constants under fractal renewal terminology remain a bibliographic priority risk.

## References
1. M. G. C. Cunha, D. D. Novaes, G. Ponce, *Infinite-Piecewise Expanding Maps: Chaos, Ergodicity and Invariant-Set Complexity*, arXiv:2608.00398v1 (first public version, 2026-08-01), especially Sections 1 and 5.6 and Appendix B.1. https://arxiv.org/html/2608.00398v1
2. G. Keller, *Rare events, exponential hitting times and extremal indices via spectral perturbation*, arXiv:1202.3900 (2012). https://arxiv.org/abs/1202.3900
3. M. L. Lapidus, G. Radunović, D. Žubrinić, *Fractal Tube Formulas for Compact Sets and Relative Fractal Drums: Oscillations, Complex Dimensions and Fractality*, arXiv:1604.08014 (2016). https://arxiv.org/abs/1604.08014
