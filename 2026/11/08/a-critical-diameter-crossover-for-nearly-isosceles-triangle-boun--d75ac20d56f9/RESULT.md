# A critical diameter crossover for nearly isosceles triangle boundaries

## Finding
Let \(0<c<1\), \(\lambda\ge0\), and, for all sufficiently large integers \(N\), let \(T_N=ABC\) have side lengths \(|AB|=1\), \(|AC|=1-\lambda/N\), and \(|BC|=c\). Sample \(N\) independent points uniformly by arclength on the entire boundary of \(T_N\), and denote their greatest pairwise Euclidean distance by \(M_N\). Put
\[
 a=1-\frac{c^2}{2},\quad P=2+c,\quad \kappa=\frac{2-c}{2-c^2},\quad \beta=\frac1c.
\]
Let \(X,Y\) be independent exponential random variables of rate \(1/P\), and let \(B,C\) be independent exponentials of rate \(\beta\), independent of \((X,Y)\). Define \(U=\min(X,aY)\), \(V=\min(Y,aX)\). Then
\[
 N(1-M_N)\ \xrightarrow{\mathrm d}\ W_{c,\lambda}:=\min\{U+B,\lambda+V+C\}.
\]
For \(u,v\ge0\), the two correlated apex costs satisfy
\[
 \Pr(U>u,V>v)=\exp\!\left[-\frac{\max(u,v/a)+\max(v,u/a)}{P}\right],
 \qquad \operatorname{Corr}(U,V)=a(2-a).
\]
For \(t\ge0\), this gives the complete limiting distribution
\[
 F_{c,\lambda}(t)=1-\mathbb E\exp\!\left[-\beta(t-U)_+-\beta(t-\lambda-V)_+\right].
\]
Define the single-competing-edge comparison law
\[
 F_{\mathrm{single}}(t)=1-\frac{\beta e^{-\kappa t}-\kappa e^{-\beta t}}{\beta-\kappa}\quad(t\ge0).
\]
For every \(\lambda>0\), one has \(F_{c,\lambda}(t)=F_{\mathrm{single}}(t)\) throughout \(0\le t\le\lambda\), and, as \(h\downarrow0\),
\[
 F_{c,\lambda}(\lambda+h)-F_{\mathrm{single}}(\lambda+h)
 =\frac{\kappa\beta}{2}e^{-\beta\lambda}h^2+O_{c,\lambda}(h^3).
\]
Thus the cumulative distribution has a genuine positive jump of size \(\kappa\beta e^{-\beta\lambda}\) in its second derivative at the competing-side threshold. For coincident longest sides (\(\lambda=0\)), the lower tail instead obeys
\[
 F_{c,0}(t)=\kappa\beta t^2+O_c(t^3),\qquad
 F_{\mathrm{single}}(t)=\tfrac12\kappa\beta t^2+O_c(t^3).
\]
In the family \(|AC|=1-\lambda_N/N\), bounded limits \(\lambda_N\to\lambda\) produce the above crossover; if \(\lambda_N\to+\infty\) while \(\lambda_N=o(N)\), then \(N(1-M_N)\) converges to the single-edge law. Hence \(1/N\) is the critical splitting scale for the two competing diametral sides.

## Assumptions and scope
The triangle must be nondegenerate, and \(N\) must be large enough that the three specified lengths satisfy the strict triangle inequalities. In particular, \(0<c<1\) is fixed independently of \(N\). Uniformity always means normalized Euclidean boundary arclength; the entire sample is independent. All exponential random variables are parameterized by *rate*, so \(\Pr(X>x)=e^{-x/P}\). The limiting diametral chords of the underlying isosceles triangle are exactly \(AB\) and \(AC\). The theorem concerns weak convergence and the exact limiting law; it does not claim a uniform error estimate in \(N\), \(c\), or \(\lambda\).

## Proof
**1. Joint endpoint gaps.** For each of the six oriented half-edges \(i\to j\) of \(T_N\), let \(G_{i\to j,N}\) be \(N\) times the smallest arclength distance from vertex \(i\) to any sampled point on edge \(ij\) (arbitrarily truncate it at the edge length times \(N\) if that edge is empty). At any fixed positive gap thresholds, the prescribed tiny endpoint arcs are disjoint for all sufficiently large \(N\). Their joint avoidance probability equals \((1-\sum s_i/(NP_N))^N\), where \(P_N=1+(1-\lambda/N)+c\to P\). Consequently the six rescaled endpoint gaps converge jointly to *independent* exponentials of rate \(1/P\). The probability of any edge being empty is exponentially small, so the arbitrary truncation is asymptotically immaterial.

**2. Geometric localization.** Since \(c<1\), in the limiting isosceles triangle the only vertex pairs achieving maximal distance \(1\) are \(A,B\) and \(A,C\). Distances along convex polygon edges are separately convex in each argument; thus, uniformly away from neighborhoods of the three vertices, any boundary pair has distance bounded by \(1-\delta\) for some \(\delta>0\), unless it approaches one of those two diametral pairs. The sampled diameter is at least \(1-O_{\mathbb P}(N^{-1})\) using the nearest points to \(A,B\) along \(AB\). Therefore its maximizing pair lies, with probability tending to one, in arbitrarily small neighborhoods of \(A,B\) or \(A,C\). Near those pairs the directional first-order derivatives of the Euclidean distance deficit are uniformly positive. The local second-order remainder is \(O((r+s)^2)\), with \(r,s\) the endpoint arclength offsets. As the nearest gaps are \(O_{\mathbb P}(N^{-1})\), minimization of the deficit chooses, on each side of the limiting vertex pair, the best among the two available outgoing edge rays. This yields an \(o_{\mathbb P}(N^{-1})\) error after localization. Non-nearest points cannot improve the first-order minimum, by the same positive derivative bound.

**3. Angular coefficients.** The cosine of the apex angle tends to \(\cos\angle BAC=a=1-c^2/2\). The base-angle cosine tends to \(\cos\angle ABC=\cos\angle BCA=c/2\). Write the two independent apex-ray limits as \(X=G_{A\to B}\), \(Y=G_{A\to C}\). The first-order apex deficits for \(AB\) and \(AC\) are \(U=\min(X,aY)\) and \(V=\min(Y,aX)\), respectively. At \(B\) the deficit is \(\min(G_{B\to A},(c/2)G_{B\to C})\); at \(C\) it is \(\min(G_{C\to A},(c/2)G_{C\to B})\). Each base-endpoint minimum is exponential with rate \((1+2/c)/P=1/c=\beta\). These two minima and the apex pair are mutually independent because they involve disjoint half-edges. The first diametral side has length \(1\), while the second has length \(1-\lambda/N\). Taking the smaller rescaled deficit proves the stated weak limit by the continuous mapping theorem. The same proof applies to \(\lambda_N\to\lambda<\infty\), and the competing chord is excluded when \(\lambda_N\to\infty\), \(\lambda_N=o(N)\).

**4. Joint apex law.** The event \(U>u,V>v\) is equivalent to \(X>\max(u,v/a)\) and \(Y>\max(v,u/a)\), giving the joint survivor displayed above. The marginals have rate \(\kappa=(1+1/a)/P=(2-c)/(2-c^2)\). A direct integration over the three regions \(X\le aY\), \(aY<X<Y/a\), and \(Y\le aX\) gives \(\mathbb E[UV]=(1+a(2-a))/\kappa^2\). Since both variances equal \(1/\kappa^2\), the correlation is \(a(2-a)\). Conditioning on \(U,V\) and then on the independent base exponentials proves the stated formula for \(F_{c,\lambda}\).

**5. Critical threshold and regularity.** When \(t\le\lambda\), the second competing deficit cannot be smaller than \(t\), so the law is the convolution of independent rate-\(\kappa\) and rate-\(\beta\) exponentials, giving \(F_{\mathrm{single}}\). For \(h>0\), conditioning as above gives the exact identity
\[
 F_{c,\lambda}(\lambda+h)-F_{\mathrm{single}}(\lambda+h)
 =\mathbb E\bigl[(1-e^{-\beta(h-V)_+})e^{-\beta(\lambda+h-U)_+}\bigr].
\]
On \(V\le h\), one always has \(U\le V/a\le h/a\). For fixed \(\lambda>0\), the second factor is therefore \(e^{-\beta\lambda}(1+O_{c,\lambda}(h))\), uniformly on that event. As \(V\) is rate-\(\kappa\) exponential, integrating the first factor gives
\[
 \int_0^h (1-e^{-\beta(h-v)})\kappa e^{-\kappa v}\,dv
 =\frac{\kappa\beta}{2}h^2+O_c(h^3).
\]
The stated cusp follows. The same calculation with \(\lambda=0\) gives an additional \(\kappa\beta t^2/2\) contribution above the single-edge lower-tail coefficient, establishing the doubled onset. The factor \(\beta-\kappa>0\) because \(c<1\). Thus the density is continuous at positive \(\lambda\), while the second derivative has the claimed one-sided jump.

## Verification
Run the standalone accompanying `verify.py` with NumPy and SciPy: `python verify.py`. It checks the angular rate identities, correlated-apex joint survival and correlation by independent simulation, the single-side distribution for thresholds below the transition, the predicted quadratic onset by low-discrepancy integration, and nine comparisons with direct finite-sample boundary geometries. The finite-sample calculation uses the two extremal sampled points of each edge: the maximum distance between two points on straight edges is convex in each edge parameter, hence is attained among those edgewise extrema. Expected output:

`VERIFY_OK rate_identities=6 joint_law=6 correlation=3 onset=3 finite_sample_comparisons=9`

These computations crosscheck formulas, but only the preceding analytic argument proves the all-parameter weak convergence and threshold asymptotics.

## Relationship to prior work
Wei Lao, *Some weak limit laws for the diameter of random point sets in bounded regions* (2010), Chapter 5.2 and Theorem 5.2, supplies the **fixed equilateral** triangular-boundary diameter limit; its appendix explicitly computes that symmetric limit. The present result instead fixes any \(0<c<1\), lets the second longest side approach the first at the critical rate \(\lambda/N\), and derives an explicit correlated-exponential crossover with a characteristic second-derivative jump. The equilateral case \(c=1\) is deliberately excluded, and no claim is made to supersede that case. Mayer and Molchanov (first preprint 2006) analyze largest distances in balls, with a distinct point geometry and asymptotic mechanism. Nearby work on small random chords, sampled polygon Hausdorff errors, and volume-interior diameters does not contain this perturbative two-chord boundary law. No historical priority beyond the inspected sources is claimed.

## Limitations
Historical originality is provisional, especially against earlier extreme-value theory under alternate terminology. The result covers boundary-arclength-uniform independent points, not area-uniform samples. The parameter \(c\) is fixed strictly between zero and one, so degenerating triangles and the equilateral three-way competition require separate analysis. The proven assertions are weak limits and limiting-law regularity, not finite-sample confidence intervals or uniform quantitative convergence rates. Independent external validation has not been performed.

## References
1. W. Lao, *Some weak limit laws for the diameter of random point sets in bounded regions*, KIT Scientific Publishing, 2010, Chapter 5.2 and Appendix D.2. Full text: https://publikationen.bibliothek.kit.edu/1000019800/105664897.
2. M. Mayer and I. Molchanov, *A limit theorem for the maximal interpoint distance of a random sample in the unit ball*, arXiv:math/0605289, first posted 2006-05-11. https://arxiv.org/abs/math/0605289.
3. S. R. Jammalamadaka and S. Janson, *Asymptotic distribution of the maximum interpoint distance in a sample of random vectors with a spherically symmetric distribution*, arXiv:1211.0822, first posted 2012-11-05. https://arxiv.org/abs/1211.0822.
