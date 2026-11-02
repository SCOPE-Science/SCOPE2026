# Strict gap-mass monotonicity for every discrete parking length

## Finding

For every integer \(k\ge2\), define the limiting density of gaps of length \(l\) in one-dimensional random sequential adsorption of length-\(k\) blocks by
\[
\Phi_k(s)=\exp\left(2\sum_{j=1}^{k-1}\frac{s^j-1}{j}\right),\qquad
 g_{k,l}=2\int_0^1(1-s)s^l\Phi_k(s)\,ds.
\]
Then the gap *mass* density is strictly increasing throughout the physical range:
\[
\boxed{(l+1)g_{k,l+1}>l g_{k,l}\quad(k\ge2,\ 0\le l\le k-2).}
\]
As a linked continuum consequence, let \(m_\infty>0\) be the Rényi parking constant, let
\[
J(x)=\int_0^x\frac{1-e^{-u}}{u}\,du,\qquad F(x)=e^{-2J(x)},
\quad f(\gamma)=\frac2{m_\infty}\int_0^\infty x e^{-\gamma x}F(x)\,dx.
\]
The limiting density from Pinsky's Theorem 3 satisfies \(\gamma f(\gamma)\) strictly increasing on \(0<\gamma\le1\). This is one gap-mass shape theorem: the continuous assertion follows from the same positivity inequality used for all discrete block lengths.

## Assumptions and scope

The model deposits nonoverlapping adjacent blocks of fixed integer length \(k\ge2\) uniformly among currently available blocks on an initially empty one-dimensional lattice interval, continuing until no placement is possible; the interval length tends to infinity before considering the limiting gap-density formulas. Only the physical gap lengths \(l=0,1,\ldots,k-1\) are asserted. The integral formula for \(g_{k,l}\) is the established Klaassen–Runnenburg/Pinsky formula. For the proof only, the formula also defines positive auxiliary integrals for all integers \(l\ge0\).

## Proof

**1. Exact reduction and the unique hardest index.** Write \(M_{k,r}=\int_0^1s^r\Phi_k(s)\,ds\). The derivative \(\Phi_k'(s)=2(1-s^{k-1})\Phi_k(s)/(1-s)\), followed by integration of \(\big[s^{r+1}(1-s)\Phi_k(s)\big]'\), gives
\[
(r+1)M_{k,r}-rM_{k,r+1}=2M_{k,r+k}.
\]
Thus, because \(g_{k,r}=2(M_{k,r}-M_{k,r+1})\),
\[
(r+1)g_{k,r+1}-rg_{k,r}=g_{k,r}-2g_{k,r+k}.
\]
These identities and the hardest-index observation were already recorded in the September 2026 partial solution cited below; they are used here as known reductions, not claimed as new results. Under the probability measure with density proportional to \((1-s)s^r\Phi_k(s)\) on \((0,1)\), the ratio \(g_{k,r+k}/g_{k,r}\) is \(\mathbb E[s^k]\). Raising \(r\) multiplies the density by \(s\); hence this expectation increases with \(r\) by positive covariance of increasing functions (equivalently, moment log-convexity). Therefore all desired steps follow strictly if
\[
\frac{g_{k,2k-2}}{g_{k,k-2}}<\frac12.
\]

**2. Uniform comparison to a continuum reference law.** Set \(s=e^{-x/k}\), \(S_k(x)=\sum_{j=1}^{k-1}(1-e^{-jx/k})/j\), and \(F(x)=e^{-2J(x)}\). The unnormalized image of the preceding probability measure at the hardest index \(r=k-2\) has density
\[
q_k(x)=\frac1k(1-e^{-x/k})e^{-(k-1)x/k}e^{-2S_k(x)},\qquad x>0.
\]
Compare it with \(q_\infty(x)=x e^{-x}F(x)\), which is integrable and positive. The likelihood ratio, up to a positive constant, is
\[
\frac{k^2q_k(x)}{q_\infty(x)}
=\frac{e^{x/k}-1}{x/k}\,e^{2(J(x)-S_k(x))}.
\]
Both factors are strictly increasing in \(x>0\): the first by its positive power series, and the second because
\[
(J-S_k)'(x)=\int_0^1e^{-xt}\,dt-\frac1k\sum_{j=1}^{k-1}e^{-jx/k}>0,
\]
by the strict right-Riemann-sum inequality (the last grid point is omitted). A strictly increasing likelihood ratio gives strict stochastic dominance toward larger \(x\). As \(e^{-x}\) is decreasing, it follows that
\[
\frac{g_{k,2k-2}}{g_{k,k-2}}=\mathbb E_{q_k}[e^{-x}]
<\frac{\int_0^\infty x e^{-2x}F(x)\,dx}
{\int_0^\infty x e^{-x}F(x)\,dx}.
\]

**3. One universal positive integral.** Since \(\big(x^2F(x)\big)'=2xe^{-x}F(x)\), integration by parts gives
\[
2\int_0^\infty xe^{-2x}F(x)\,dx
=\int_0^\infty x^2e^{-x}F(x)\,dx.
\]
The boundary terms vanish (\(0<F\le1\)). Therefore the required upper bound of \(1/2\) is equivalent to
\[
C:=\int_0^\infty x(1-x)e^{-x-2J(x)}\,dx>0.
\]
A complete, standalone, integer-only interval certificate proves the stronger inequality \(C>1/1000\); its replayable source and numeric enclosure are included in `rsa_monotonicity_checker.py` and `verification_log.txt`. Specifically, use \(750\) intervals of width \(1/50\) on \([0,15]\), outward fixed-point integer interval arithmetic with scale \(10^{38}\), Taylor bounds through orders \(80/81\) for \(J\) and \(100/101\) for the exponential, monotone endpoint rectangles on each side of \(x=1\), and the analytic tail bound \(241e^{-15}\). The computed rigorous lower enclosure exceeds \(0.001515\). All alternating-series tails have their stated signs because the term magnitudes decrease from those orders for the domain \(0\le x\le15\), \(0\le x+2J(x)\le23\). This proves the inequality for every \(k\), with no enumeration of \(k\), completing the discrete result.

**4. Continuous gap-mass monotonicity.** Put \(h(\gamma)=\gamma\int_0^\infty xe^{-\gamma x}F(x)\,dx\). For any \(0<\gamma\le1\), differentiation and the change \(t=\gamma x\) yield
\[
h'(\gamma)=\gamma^{-2}\int_0^\infty t(1-t)e^{-t}F(t/\gamma)\,dt.
\]
The positive ratio \(R_\gamma(t)=F(t/\gamma)/F(t)\) is nonincreasing in \(t\), since
\[
\frac{d}{dt}\log R_\gamma(t)=\frac{2(e^{-t/\gamma}-e^{-t})}{t}\le0.
\]
The baseline integrand \(t(1-t)e^{-t}F(t)\) has sign positive before \(1\), negative after \(1\), and total integral \(C>0\). Consequently
\[
h'(\gamma)\ge\gamma^{-2}R_\gamma(1)C>0.
\]
Multiplying by \(2/m_\infty>0\) proves the continuum corollary, including the derivative from the left at the endpoint \(\gamma=1\).

## Verification

Run `python3 rsa_monotonicity_checker.py` using the standard Python library. The program uses fixed-point integers exclusively in its asserted interval enclosures. It checks the alternating-series bounds, every integrand rectangle, a rigorous upper bound for the negative tail, and the strict inequality \(C>1/1000\). The observed output is included verbatim in `verification_log.txt`. This is a finite exact certificate for an analytic bound, not finite numerical evidence extrapolated to infinitely many lengths. The remaining steps are analytic identities and stochastic-order arguments displayed above.

## Relationship to prior work

Klaassen and Runnenburg established the exact finite-block gap-density formula and joint Gaussian fluctuations of gap counts. Pinsky (2026, arXiv:2608.04730, Theorem 2 and the remark after Table 1) explicitly observed numerical increase of \(l g_{k,l}\) but stated that he had no proof; his Theorem 3 gives the continuum gap-density integral. The September 2026 note *The bonded-molecule density of one-dimensional random sequential adsorption is decreasing in k, and an exact reduction for the gap densities* already derives the exact moment reduction and proves the conjecture for \(2\le k\le20\), expressly leaving general larger \(k\) open. The new ingredient is a uniform comparison of every hardest-case discrete measure with one continuum reference measure, together with the strict universal integral certificate. It proves the result for **all integers** \(k\ge2\), not just the finite window. Searches found no statement implying that generality; unindexed prior work remains a historical-priority possibility.

## Limitations

The result concerns limiting *expected* densities of maximal gaps in the one-dimensional single-block-length random sequential adsorption model, and its associated continuum gap law. It is not a concentration theorem for individual random configurations, not a statement about competing two-block adsorption, and not a claim that the auxiliary continuation \(l\mapsto l g_{k,l}\) is increasing after the physical endpoint. The positivity certificate is reproducible with exact integer arithmetic but has not undergone independent expert audit. Historical priority beyond the inspected sources remains provisional.

## References

1. R. G. Pinsky, *A new look at some aspects of one-dimensional random sequential adsorption and its continuum limit*, arXiv:2608.04730 (first public August 5, 2026), especially Theorems 2–3 and the comment after Table 1. https://arxiv.org/abs/2608.04730
2. C. A. J. Klaassen and J. T. Runnenburg, *Discrete Spacings*, arXiv:math/0112056 (first public December 6, 2001). https://arxiv.org/abs/math/0112056
3. *The bonded-molecule density of one-dimensional random sequential adsorption is decreasing in k, and an exact reduction for the gap densities*, publicly archived September 7, 2026, especially the finite-window theorem and the hardest-index reduction. https://ideosphere.ai/papers/pinsky-monotone
