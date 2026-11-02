# Memoryless dispersal is the only gap-neutral exponential mixture: a sharp two-reserve spacing law

## Finding

For a circular coast, two positive-length habitat reserves, and a strictly clockwise dispersal law formed by **any probability mixture of wrapped exponential kernels**, the one-generation invasion growth factor is minimized when the two gaps are equal, and maximized when the reserves touch. The minimum and maximum are strict, apart from the two equivalent touching arrangements, **if and only if** the mixing law is not concentrated at one rate. For a single exponential rate, every spacing has precisely the same invasion spectrum. This classification remains true for unequal reserve lengths, unequal positive per-source reproduction, and unequal positive per-target survival.

Moreover, for an arbitrary number of fixed-width reserves, a single wrapped exponential gives **gap-independent complete characteristic polynomial**, not just the dominant eigenvalue. The one-rate statement is a structural baseline, whereas the universal strict optimality and the one-rate/nondegenerate-mixture dichotomy are the central two-reserve result.

A dimensionless example exhibits an actual invasion-threshold reversal without changing reserve widths: with circumference \(L=1\), two reserve widths \(\ell_1=\ell_2=0.1\), rate mixing \(\mu=(\delta_2+\delta_{12})/2\), and constant reproduction multiplier \(R=3\), the linear growth factor is \(1.0411713052546\ldots>1\) when the reserves touch, but \(0.9471851969386\ldots<1\) when their gaps are equal.

## Assumptions and scope

Fix \(L>0\). Points on the coastline are identified modulo \(L\), and displacement follows the positive (clockwise) direction. For each \(\kappa>0\), define the normalized wrapped density
\[
 k_\kappa(u)=\frac{\kappa e^{-\kappa u}}{1-e^{-\kappa L}},\qquad 0\le u<L.
\]
Let \(\mu\) be any Borel probability measure on \((0,\infty)\), with no moment or finite-support assumption. The dispersal kernel is \(k(u)=\int k_\kappa(u)\,\mu(d\kappa)\); it is a probability density in the Lebesgue sense, although its value at a single point need not be finite.

Take two labeled, non-overlapping intervals of lengths \(\ell_1,\ell_2>0\), with \(H=L-\ell_1-\ell_2>0\). Write
\[
 R_1=[0,\ell_1),\qquad R_2=[\ell_1+g,\ell_1+g+\ell_2),\quad 0\le g\le H.
\]
The two gaps are \(g\) and \(H-g\). A gap of zero is permitted: the reserves share a boundary but remain distinct, labeled reproductive populations. Assume propagule production is spatially uniform within each source interval and recruitment is spatially uniform in each target interval. For \(i,j\in\{1,2\}\), define
\[
 M_{ji}(g)=\frac1{\ell_i}\int_{R_i}\int_{R_j} k((y-x)\bmod L)\,dy\,dx.
\]
Here \(M\) is a per-individual recruitment probability matrix: column \(i\) is the source, row \(j\) is the target, and dispersers landing outside reserves are lost. Fixed positive settlement qualities \(s_i\) and fixed positive source outputs \(f_i\) give the nonnegative next-generation matrix \(N(g)=\operatorname{diag}(s_1,s_2)M(g)\operatorname{diag}(f_1,f_2)\). Persistence refers solely to the linear invasion criterion \(\rho(N)>1\); equality is marginal and nonlinear ecological persistence is not inferred.

For the additional many-reserve statement, take an integer \(m\ge2\), fixed positive widths \(\ell_i\) summing to less than \(L\), and non-overlapping reserves in a fixed cyclic order. Vary any gaps without changing the widths, cyclic order, or fixed positive site qualities; only the single-rate kernel is asserted in that part.

## Proof

**Step 1 (exact two-reserve factorization).** Set
\[
 b(\kappa)=\frac{(1-e^{-\kappa\ell_1})(1-e^{-\kappa\ell_2})}{\kappa(1-e^{-\kappa L})}>0,
 \qquad F(t)=\int_{(0,\infty)}b(\kappa)e^{-\kappa t}\,\mu(d\kappa),\quad t\ge0.
\]
Direct integration over source and target intervals, in that order, gives
\[
 M_{21}(g)=\frac{F(g)}{\ell_1},\qquad M_{12}(g)=\frac{F(H-g)}{\ell_2}.
\]
For example, the integrand for source 1 to target 2 has nonwrapped distance \(y-x\); the inner target integral is \(e^{-\kappa(\ell_1+g-x)}(1-e^{-\kappa\ell_2})/(1-e^{-\kappa L})\), and the source average produces precisely \(b(\kappa)e^{-\kappa g}/\ell_1\). The reverse passage wraps clockwise and produces the same \(b(\kappa)\) at gap \(H-g\). Translation invariance makes each self-recruitment probability \(d_i=M_{ii}\) independent of \(g\) and finite.

Put \(a_i=s_i f_i d_i\), \(Q=s_1s_2f_1f_2/(\ell_1\ell_2)>0\). The Perron root of the positive two-by-two matrix is exactly
\[
 \boxed{\rho(N(g))=\frac{a_1+a_2}{2}+\sqrt{\left(\frac{a_1-a_2}{2}\right)^2+QF(g)F(H-g)}.}
\]
Consequently, its ordering across placements is **exactly** the ordering of \(F(g)F(H-g)\), regardless of reserve widths or fixed site qualities.

**Step 2 (strict log-convexity and all equality cases).** The weight \(b(\kappa)\) is positive and bounded: as \(\kappa\downarrow0\), it tends to \(\ell_1\ell_2/L\), while it is \(O(1/\kappa)\) at infinity. Thus \(0<F(t)<\infty\) for every \(t\ge0\), including the endpoints, without a moment hypothesis. Hölder's inequality gives for distinct \(u,v\ge0\) and \(0<\theta<1\):
\[
 F(\theta u+(1-\theta)v)\le F(u)^\theta F(v)^{1-\theta}.
\]
Equality for \(u\ne v\) requires \(e^{-\kappa(u-v)}\) to be constant for \(b(\kappa)\mu(d\kappa)\)-almost every \(\kappa\), hence exactly that \(\mu\) is a Dirac mass at one rate. Therefore \(\log F\) is **strictly convex** for every non-Dirac \(\mu\).

The continuous function \(h(g)=\log F(g)+\log F(H-g)\) is symmetric about \(H/2\) and strictly convex if \(\mu\) has more than one supported rate. Strict convexity and symmetry show \(h\) is strictly decreasing on \([0,H/2]\), strictly increasing on \([H/2,H]\), has a unique minimum at \(H/2\), and has precisely two maximum points \(0,H\). This proves the claimed spectral optimality and uniqueness for every non-Dirac mixing law. If \(\mu=\delta_\kappa\), then \(F(g)F(H-g)=b(\kappa)^2e^{-\kappa H}\) is constant. Conversely, constant spectral radius on the entire gap interval contradicts strict convexity unless \(\mu\) is a Dirac mass. The endpoints are included; if physical constraints require both gaps to be strictly positive, the same extrema at contact are limiting suprema rather than attained maxima.

**Step 3 (any number of reserves, single rate).** Choose coordinates \(s_1<\cdots<s_m\) for the starts of intervals in fixed cyclic order. For \(j\ne i\), direct integration of the single-rate density yields
\[
 M_{ji}=e^{-\kappa s_j}\,C_{ji}\,e^{\kappa s_i},\qquad
 C_{ji}=\frac{(e^{\kappa\ell_i}-1)(1-e^{-\kappa\ell_j})}{\kappa\ell_i(1-e^{-\kappa L})}\begin{cases}1,&j>i,\\e^{-\kappa L},&j<i.\end{cases}
\]
Each diagonal \(M_{ii}\) depends only on \(\ell_i\). Let \(C_{ii}=M_{ii}\), and \(D=\operatorname{diag}(e^{-\kappa s_1},\ldots,e^{-\kappa s_m})\). Then \(M=DCD^{-1}\), where \(C\) depends on lengths and cyclic order but **not gaps**. Since all fixed site-quality matrices are diagonal, they commute with \(D\); thus \(\operatorname{diag}(s)M\operatorname{diag}(f)\) is similar to the fixed matrix \(\operatorname{diag}(s)C\operatorname{diag}(f)\). Its complete characteristic polynomial is independent of gap placement. This identity does not imply that the actual recruitment flows or patch-population eigenvectors are spacing-invariant.

**Step 4 (a realized invasion reversal).** For \(L=1\), \(\ell_1=\ell_2=1/10\), and \(\mu=(\delta_2+\delta_{12})/2\), direct substitution into the boxed formula gives \(\rho(M(0))=0.347057101751542\ldots\) and \(\rho(M(2/5))=0.315728398979521\ldots\). Taking \(s_i=1\) and \(f_i=3\) for both patches multiplies these eigenvalues by three, giving the strict threshold crossing stated above. All comparisons follow from explicit elementary integrals and the general theorem; the displayed decimals are reproducible numerical illustrations, not proof certificates for infinite families.

## Verification

The accompanying dependency-free `VERIFY.py` checks the off-diagonal integration formula against independent finite quadrature in sample layouts, the similarity conjugacy for four unequal reserve widths and multiple pure rates, the two-by-two root formula under randomly generated unequal widths and positive site qualities, strict monotonicity for finite multi-rate mixtures, the Dirac equality case, and the stated threshold-crossing example. Run `python3 VERIFY.py`. Its deterministic finite checks complement, but do not replace, the universal Hölder argument. The exact integration and matrix-similarity identities in the proof establish the infinite statements without numerical extrapolation.

## Relationship to prior work

Botsford, Hastings, and Gaines (2001) established the importance of reserve configuration and larval dispersal distance. Kaplan and Botsford (2005) modeled variable reserve spacing using a two-sided Laplacian kernel and numerical ecological dynamics; Kaplan (2006) studied advective shifts of such a Laplacian kernel with circular boundary conditions. Hastings and Botsford (2006) provided general closed-reproductive-path persistence criteria for patch matrices. White and colleagues (2010) modeled spatially heterogeneous advective-diffusive transport and numerical reserve persistence. Blowes and Connolly (2012) considered spacing, dispersal, and temporally correlated demographic risks; their accessible abstract does not resolve the present deterministic one-way complete-mixture problem. A prior point-site exponential spectral-invariance calculation covers a limiting baseline, not the strict two-interval classification for arbitrary mixing measures and heterogeneous positive site qualities.

This result applies to a very specific directional, translation-invariant, circular linear recruitment model, in contrast to the diffusive, stochastic, heterogeneous-current, and density-dependent settings of those papers. The claim is the **all-mixture exact spacing classification and its memoryless equality boundary**, not that connectivity or clustering effects are new.

## Limitations

The model assumes a closed circular coast, strictly one-way transport with no diffusion against flow, fixed nonoverlapping habitat widths, spatially uniform reproduction within patches, linear low-density recruitment, and positive **fixed** source/target quality multipliers. It ignores catastrophes, environmental covariances, larval mortality outside the modeled density, density-dependent population dynamics, adult movement, fishing yields, and the realism of an unrestricted mixture of exponential rates. A larger spectral radius is only a **linear invasion indicator**, not a guarantee of long-term ecological persistence or welfare. Equality and contact outcomes use the precise boundary convention above. The many-reserve invariance is asserted only for a single rate, not a mixture. Historical originality remains subject to fuller literature review, especially the inaccessible complete 2012 spacing paper and equivalent general kernel-optimization results.

## References

- Botsford, L. W., Hastings, A., and Gaines, S. D. (2001). *Dependence of sustainability on the configuration of marine reserves and larval dispersal distance*. Ecology Letters. DOI: 10.1046/j.1461-0248.2001.00208.x.
- Kaplan, D. M., and Botsford, L. W. (2005). *Effects of variability in spacing of coastal marine reserves on fisheries yield and sustainability*. Canadian Journal of Fisheries and Aquatic Sciences. DOI: 10.1139/F04-243.
- Hastings, A., and Botsford, L. W. (2006). *Persistence of spatial populations depends on returning home*. PNAS. DOI: 10.1073/pnas.0506651103.
- Kaplan, D. M. (2006). *Alongshore advection and marine reserves: consequences for modeling and management*. Marine Ecology Progress Series. DOI: 10.3354/meps309011.
- White, J. W., Botsford, L. W., Hastings, A., and Largier, J. L. (2010). *Population persistence in marine reserve networks: incorporating spatial heterogeneities in larval dispersal*. Marine Ecology Progress Series. DOI: 10.3354/meps08327.
- Blowes, S. A., and Connolly, S. R. (2012). *Risk spreading, connectivity, and optimal reserve spacing*. Ecological Applications. DOI: 10.1890/11-0952.1.
