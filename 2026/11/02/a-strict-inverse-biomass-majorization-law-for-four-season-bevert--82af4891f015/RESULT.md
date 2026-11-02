# A strict inverse-biomass majorization law for four-season Beverton–Holt populations

## Finding

Fix an intrinsic growth factor \(r>1\) and two positive environmental carrying capacities \(0<L<H\). In the unharvested four-season Beverton–Holt recurrence
\[
x_{t+1}=\frac{rK_tx_t}{K_t+(r-1)x_t},\qquad x_0>0,
\]
compare the grouped schedule \(G=(L,L,H,H)\) with the alternating schedule \(A=(L,H,L,H)\), repeated periodically. Let \((x^G_0,\ldots,x^G_3)\) and \((x^A_0,\ldots,x^A_3)\) be their attracting positive cycles and write \(y^S_i=1/x^S_i\) for \(S\in\{G,A\}\).

**Theorem (strict majorization and conflicting biomass objectives).** The four-component inverse-biomass vector \(y^G\) strictly majorizes \(y^A\): after sorting the entries in decreasing order, its first, first two, and first three partial sums are strictly greater, whereas both complete sums coincide. Consequently, for every strictly convex real function \(\Phi\) on an interval containing their inverse-biomass coordinates,
\[
\frac14\sum_{i=0}^3\Phi(y^G_i)>\frac14\sum_{i=0}^3\Phi(y^A_i).
\]
In particular,
\[
\boxed{\frac14\sum_{i=0}^3x^G_i>\frac14\sum_{i=0}^3x^A_i,\qquad
\min_i x^G_i<\min_i x^A_i,\qquad \max_i x^G_i>\max_i x^A_i.}
\]
Nevertheless both arrangements have exactly the same inverse-biomass average:
\[
\frac14\sum_{i=0}^3\frac1{x_i^G}=\frac14\sum_{i=0}^3\frac1{x_i^A}
=\frac12\left(\frac1L+\frac1H\right).
\]
There are exactly two schedules up to cyclic rotation with two occurrences of each capacity, so grouping uniquely maximizes arithmetic mean biomass and uniquely minimizes trough biomass among those schedules, apart from cyclic phase changes.

## Assumptions and scope

The parameters satisfy \(r>1\) and \(0<L<H\). The growth factor is constant, capacities are deterministic and periodic, and no removals, migration, environmental noise, or demographic stochasticity are present. Census time \(t\) is immediately before the seasonal update with capacity \(K_t\). Means, extrema, and majorization concern one complete periodic attractor, not finite transients. The grouped and alternating schedules represent all permutations of the multiset \(\{L,L,H,H\}\) up to rotation. In the degenerate cases \(L=H\) or the excluded boundary \(r=1\), strictness does not follow.

## Proof

**Step 1: positive, globally attracting periodic orbit.** Put \(y_t=1/x_t\) and \(\gamma_t=(r-1)/K_t\). The recurrence transforms exactly into the positive affine contraction
\[
y_{t+1}=\frac{y_t+\gamma_t}{r}.
\]
Its four-step iterate has slope \(r^{-4}\), strictly between zero and one. It has a unique strictly positive fixed point and attracts every positive initial reciprocal population, proving existence and global attraction of the positive four-periodic state. At each phase its explicit formula, with subscripts understood cyclically, is
\[
(r^4-1)y_t=\gamma_t+r\gamma_{t+1}+r^2\gamma_{t+2}+r^3\gamma_{t+3}.
\]
The orientation of the indices is immaterial when taking the multiset of the four cycle values.

**Step 2: exact seasonal reciprocal spectra.** Set
\[
b=\frac{r-1}{H},\quad \delta=(r-1)\left(\frac1L-\frac1H\right)>0,\quad Q=1+r+r^2+r^3.
\]
Each inverse-biomass entry has the form \((bQ+\delta s)/(r^4-1)\), where \(s\) is the sum of the two weights among \(1,r,r^2,r^3\) corresponding to occurrences of \(L\). Directly taking the four cyclic windows gives the multisets
\[
\{s_i^G\}=\{1+r,\ r+r^2,\ 1+r^3,\ r^2+r^3\},
\qquad \{s_i^A\}=\{1+r^2,\ 1+r^2,\ r+r^3,\ r+r^3\}.
\]
For every \(r>1\), the grouped weights are already in strictly increasing order as displayed, and the alternating weights have two smaller and two larger entries. Their total sums both equal \(2Q\). After sorting in *decreasing* order, the grouped-minus-alternating partial-sum differences for the first one, two, and three entries are exactly
\[
\frac{\delta}{r^4-1}(r^2-r),\qquad
\frac{\delta}{r^4-1}(r-1)^2,\qquad
\frac{\delta}{r^4-1}(r^2-r),
\]
respectively. Each is strictly positive; the four-entry difference is zero. The common positive affine scaling preserves these strict partial-sum inequalities. This is strict majorization.

**Step 3: objectives.** The finite-vector majorization inequality applied to any strictly convex \(\Phi\) gives the strict convex-average comparison. Since \(z\mapsto 1/z\) is strictly convex for \(z>0\), its choice yields the strict arithmetic mean population comparison. The largest grouped reciprocal is strictly larger and the smallest strictly smaller than the corresponding alternating reciprocals; inversion gives the strict trough and crest inequalities. Summing the periodic reciprocal recurrences and cancelling their cyclic left and right sums yields \(\sum y_i=\sum 1/K_i=2/L+2/H\), proving the common inverse-biomass average. The six permutations of two \(L\)'s and two \(H\)'s consist of four cyclic rotations of \(G\) and two of \(A\), which proves the stated finite-design optimality without any additional patterns.

## Verification

For exact parameters \(r=2\), \(L=1/3\), and \(H=1\), the unordered grouped population cycle is
\[
\left\{\frac57,\frac59,\frac5{11},\frac5{13}\right\},
\]
whereas the alternating cycle is \(\{3/5,3/5,3/7,3/7\}\). The means and their difference are
\[
\overline x^G=\frac{4750}{9009},\qquad \overline x^A=\frac{18}{35},\qquad
\overline x^G-\overline x^A=\frac{584}{45045}>0.
\]
The troughs are \(5/13\) versus \(3/7\), in the opposite order. The standalone `verify.py` computes periodic solutions independently by rational arithmetic and checks positive recurrence, all cyclic schedules, strict majorization and the exact example for 640 nondegenerate rational parameter triples; it reports 41,615 passing exact-rational assertions. These finite checks test implementation and examples, not the theorem over all real parameters; the universal proof is the algebraic argument above.

## Relationship to prior work

The periodic Beverton–Holt model and its global attracting positive cycle are established results. AlSharawi and Ben Haj Rhouma (2010), particularly Example 3.4 and Theorem 3.5, already study effects of permuting carrying capacities: they report an unharvested period-three numerical change in mean population and analyze the maximum constant sustainable harvest for period-four schedules. Yang and Sacker (2013), with Haskell's appendix, derive general formulas connecting periodic mean population and environmental capacities, including a four-period formula, and analyze resonance/attenuation. Those are not claimed here as new. The present statement is a strict four-coordinate **convex-order theorem on inverse biomass** for the two-valued four-season census and the resulting uniform opposition of mean versus minimum biomass. The general prior formulas can evaluate the special-case means, but do not themselves state this majorization or the objective conflict. Existing work on permutation of harvesting quotas concerns a different intervention and geometric-mean criterion.

## Limitations

The result is a deterministic, scalar, no-harvest comparison for exactly two high- and two low-capacity seasons and a fixed growth factor. Convex order is asserted for inverse biomass, not for biomass itself. The higher grouped mean does not imply greater persistence under stochastic shocks or greater sustainable yield, and a lower modeled trough does not establish actual extinction. For arbitrary periods, more than two capacity levels, or seasonal growth factors, the ordering need not persist and no such extension is claimed. The attribution of a wholly new result remains subject to independent literature-priority review, particularly the exact implications of more general periodic mean formulas and inaccessible relevant literature.

## References

1. Z. AlSharawi and M. Ben Haj Rhouma, “The Discrete Beverton-Holt Model with Periodic Harvesting in a Periodically Fluctuating Environment,” *Advances in Difference Equations* (2010), article 215875, published 8 March 2010. DOI: https://doi.org/10.1155/2010/215875.
2. Y. Yang and R. J. Sacker, with appendix by C. Haskell, “Resonance and attenuation in the n-periodic Beverton–Holt equation,” *Journal of Difference Equations and Applications* **19** (2013), 1174–1191, first online 9 October 2012. DOI: https://doi.org/10.1080/10236198.2012.726988.
3. A. S. Al-Ghassani and Z. AlSharawi, “The effect of maps permutation on the global attractor of a periodic Beverton–Holt model,” *Applied Mathematics and Computation* **370** (2020), 124905. DOI: https://doi.org/10.1016/j.amc.2019.124905. Abstract inspected; full technical text unavailable.
4. C. Allen and V. Kocic, “Resonance in Beverton-Holt population models with periodic and random coefficients,” *Journal of Difference Equations and Applications* (2013). DOI: https://doi.org/10.1080/10236198.2013.854779. Abstract inspected; full technical text unavailable.
