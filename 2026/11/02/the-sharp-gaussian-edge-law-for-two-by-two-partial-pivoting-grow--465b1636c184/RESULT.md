# The sharp Gaussian edge law for two-by-two partial-pivoting growth

## Finding
Let \(A\) be a real \(2\times2\) matrix with four independent \(N(0,1)\) entries. Perform Gaussian elimination with partial pivoting (GEPP) in exact arithmetic, choosing the larger absolute entry of the first column as the first pivot, and define \(\rho(A)\) as the largest absolute value encountered during elimination, divided by the largest absolute entry of the original matrix. Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-2}\Pr\{\rho(A)>2-\varepsilon\}=\frac{1}{2\pi^2}.}
\]
In particular, the maximal possible two-by-two growth is \(2\), approached with positive probability at order \(\varepsilon^2\), and the leading coefficient is exact.

## Assumptions and scope
All entries are independent standard real Gaussians. The first pivot is the first-column entry of largest absolute magnitude; pivot ties and zero pivots have probability zero. The growth factor includes the original matrix and the sole updated trailing entry, hence is at least one. The limit is taken at fixed dimension two as the growth threshold approaches its exact deterministic maximum. No floating-point rounding or large-dimensional limit is involved.

## Proof
Let \(f(t)=\sqrt{2/\pi}\exp(-t^2/2)\) be the density of the absolute value of a standard Gaussian on \(t>0\). After first-column pivoting, write \(p>u>0\) for the pivot and unpivoted first-column magnitudes and \(B,D>0\) for the pivot-row and unpivoted-row second-column magnitudes. Their joint density is \(2f(p)f(u)f(B)f(D)\), on \(0<u<p\) with \(B,D>0\). Because the row selection depends only on the first column, the two second-column magnitudes are still independent standard half-normal variables. The four Gaussian signs are independent of these magnitudes.

The final trailing entry has absolute value \(|d-ub/p|\) with appropriate independent signs. With probability \(1/2\), the two signed terms subtract in absolute magnitude, yielding at most \(\max(B,D)\), so no growth greater than one. With complementary probability \(1/2\), the terms reinforce and the updated magnitude is \(D+(u/p)B\). Consequently, for \(0<\varepsilon<1\), the event \(\rho>2-\varepsilon\) can occur only in the reinforcing-sign case and is equivalent there to
\[
D+(u/p)B>(2-\varepsilon)M,\qquad M=\max(p,B,D).
\]
The inequality also establishes \(\rho\le2\) for every input, including nonsingular matrices.

Partition by the almost surely unique maximizer of \(M\). On \(M=B=t\), put \(D=t(1-v)\) and \(u=p(1-w)\). Then \(p<t\), \(v,w\ge0\), and the growth event becomes \(v+w<\varepsilon\). The relevant Jacobian is \(pt\); the factor of two from ordering \(p,u\) cancels the reinforcing-sign probability \(1/2\). Its probability is therefore
\[
I_B(\varepsilon)=\int_0^\infty\!\int_0^t pt f(t)f(p)\int_{v,w\ge0,\,v+w<\varepsilon}
 f(t(1-v))f(p(1-w))\,dv\,dw\,dp\,dt.
\]
On \(M=D=t\), put \(B=t(1-v)\) and \(u=p(1-w)\). The integrand and Jacobian remain the same, but the growth condition is \(v+w-vw<\varepsilon\). For \(0<\varepsilon<1/2\), this region lies inside \([0,\varepsilon]^2\); rescaling \((v,w)=\varepsilon(V,W)\), its indicator converges almost everywhere to that of \(\{V,W\ge0:V+W<1\}\). The same is immediately true for the first region. Since \(f\) decreases on positive arguments, for \(v,w\le1/2\) both rescaled integrands are dominated by an integrable multiple of \(ptf(t)f(p)f(t/2)f(p/2)\). Dominated convergence gives
\[
\lim_{\varepsilon\downarrow0}\frac{I_B(\varepsilon)}{\varepsilon^2}
=\lim_{\varepsilon\downarrow0}\frac{I_D(\varepsilon)}{\varepsilon^2}
=\frac12J,
\quad J=\int_0^\infty\!\int_0^t ptf(t)^2f(p)^2\,dp\,dt.
\]

In the remaining case \(M=p=t\), the growth inequality forces simultaneously \(u>(1-\varepsilon)t\), \(B>(1-\varepsilon)t\), and \(D>(1-\varepsilon)t\): if any one of the three normalized factors is at most \(1-\varepsilon\), then \(D/t+(u/t)(B/t)\le2-\varepsilon\). These three independent thin intervals contribute at most a constant multiple of
\[
\varepsilon^3\int_0^\infty t^3f(t)f(t/2)^3\,dt
\]
for \(0<\varepsilon<1/2\), and the integral is finite. Thus \(I_p(\varepsilon)=O(\varepsilon^3)\).

Finally, using \(f(t)^2=(2/\pi)e^{-t^2}\),
\[
J=\frac4{\pi^2}\int_0^\infty te^{-t^2}\left(\int_0^t pe^{-p^2}\,dp\right)dt
=\frac4{\pi^2}\cdot\frac18=\frac1{2\pi^2}.
\]
Combining \(I_B+I_D+I_p\) proves the asserted limit and its strictly positive constant. \(\square\)

## Verification
The analytical proof alone establishes the infinite-resolution limit. The companion `verify.py` independently checks the pivoting identity on explicit matrices; verifies the elementary integral determining the coefficient; checks the three-region inequalities on deterministic grids; and performs a reproducible Gaussian Monte Carlo sanity test. No sampling result is used as proof of the asymptotic formula.

## Relationship to prior work
Classical Wilkinson growth bounds imply the deterministic maximum \(2\) at dimension two; they do not yield its random near-extremal probability. Trefethen and Schreiber (1990) studied average-case Gaussian elimination and growth across many dimensions, emphasizing large-dimensional averages and multiplier distributions. Trefethen (2026) establishes a high-dimensional exponential rarity statement for a corner entry, while Urschel (2026) establishes high-dimensional partial-pivoting growth bounds. Their published scope does not directly imply the exact fixed-two-dimensional \(\varepsilon\downarrow0\) edge constant here. Driscoll and Maki (2007) use rare-event simulation at larger dimensions; the present fixed-dimension formula offers a transparent asymptotic benchmark for such methods. These comparisons are subject to the access caveats below.

## Limitations
The exact coefficient is proved only for an independent real Gaussian \(2\times2\) matrix with ordinary partial pivoting and the specified maximum-entry normalization. No assertion is made for dimension three or higher, non-Gaussian distributions, threshold pivoting, or computed floating-point error. The available Urschel (2026) abstract, but not its complete text, was inspected; consequently a residual historical-priority risk remains. Independently audited novelty and correctness are not asserted.

## References
1. L. N. Trefethen, “Instability of Gaussian elimination is exponentially rare (proof of partial result),” arXiv:2610.04761v1, posted 2026-10-03, https://arxiv.org/abs/2610.04761; author-hosted full text: https://people.maths.ox.ac.uk/trefethen/ge26.pdf.
2. L. N. Trefethen and R. S. Schreiber, “Average-case stability of Gaussian elimination,” *SIAM J. Matrix Anal. Appl.* 11 (1990), 335–360, doi:10.1137/0611023, author-hosted full text: https://people.maths.ox.ac.uk/~trefethen/publication/PDF/1990_44.pdf.
3. J. Urschel, “On the growth factor of random matrices,” arXiv:2610.06785v1, posted 2026-10-05, https://arxiv.org/abs/2610.06785 (abstract inspected; full text not verified).
4. T. A. Driscoll and K. L. Maki, “Searching for rare growth factors using multicanonical Monte Carlo methods,” *SIAM J. Matrix Anal. Appl.* (2007), prior rare-event numerical context; full text not verified.
