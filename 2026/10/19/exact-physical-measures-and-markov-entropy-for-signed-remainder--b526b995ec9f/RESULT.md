# Exact physical measures and Markov entropy for signed-remainder chaotification

## Finding
For every integer \(m\geq2\), define the signed remainder by
\[\operatorname{rem}(t,1)=t-\operatorname{trunc}(t),\]
where truncation is toward zero, and define the real map
\[H_m(x)=\frac{x}{2}+\operatorname{rem}\!\left(\left(m-\frac12\right)x,1\right).\]
Put \(d=2m-1\) and \(C_m=[1/d,\,2-1/d]\). Every initial condition \(x\ne0\) enters either \(C_m\) or \(-C_m\) in finite time, according to its sign, and stays there. On each core there is exactly one absolutely continuous invariant probability \(\mu_m^\pm\); each is mixing, is physical for Lebesgue-almost every initial condition of its sign, and has metric entropy and almost-everywhere Lyapunov exponent both equal to \(\log m\). The measures are mirror images and **are not uniform**.

More precisely, the positive core has \(4m-4\) equal cells
\[I_j=\left(\frac j d,\frac{j+1}d\right),\qquad 1\le j\le4m-4.\]
Define \(s_j=mj-d\lfloor j/2\rfloor\), and the \((4m-4)\)-square zero-one matrix
\[B_{j\ell}=\mathbf1\{s_j\le\ell<s_j+m\}.\]
Every row of \(B\) has exactly \(m\) ones, and \(B\) is primitive. The unique strictly positive rational probability vector \(\pi\) satisfying
\[\pi_\ell=\frac1m\sum_j\pi_j B_{j\ell},\qquad\sum_j\pi_j=1\]
gives the exact physical density \(\rho_m(x)=d\pi_j\) on \(I_j\), zero outside \(C_m\). (Values at the finitely many boundaries are immaterial to the density.) The partition itinerary is a stationary mixing Markov chain with transition matrix \(B/m\).

For \(m=2\), the four cell probabilities are exactly
\[\pi=(1/6,\,1/3,\,1/3,\,1/6).\]
Thus the positive stationary density on successive thirds of \([1/3,5/3]\) is \((1/2,1,1,1/2)\); the middle two cells carry probability \(2/3\), the mean is \(1\), and the variance is \(1/9\). The corresponding negative stationary density is its reflection.

## Assumptions and scope
All dynamics and measures refer to **exact real arithmetic** and truncation-toward-zero signed remainder. The integer \(m\) is arbitrary subject to \(m\ge2\); there is no random forcing. Invariance, mixing, physicality and entropy are claims about the stated invariant real intervals; the basin statement concerns Lebesgue-almost every real initial condition, separately on each sign half-line. The singular fixed point at zero is not a physical attractor. No claim concerns floating-point implementations or cryptographic security.

## Proof
**1. Sign and global entry.** For \(x>0\), the remainder is a fractional part and
\[H_m(x)=mx-\left\lfloor\frac{dx}{2}\right\rfloor>0.\]
The signed-remainder definition makes \(H_m\) odd. For \(x>2\), \(0<H_m(x)<x/2+1<x\). If an orbit remained above \(2\) forever, its values would decrease to \(2\); however, for sufficiently small \(\varepsilon>0\), \(H_m(2+\varepsilon)=1+m\varepsilon<2\), a contradiction. Also \(H_m(2)=1\).

Within \((0,1/d)\), the map is \(H_m(x)=mx\). Repeated multiplication by \(m\) eventually enters \([1/d,m/d)\subset C_m\). Within \((2-1/d,2)\), the map obeys \(2-H_m(x)=m(2-x)\). Thus the distance to \(2\) multiplies by \(m\) until the first entry into \((2-m/d,2-1/d]\subset C_m\). At all remaining points of \([0,2]\), the initial state is already in the core or is zero. The branch formulas in step 2 show that the core is forward invariant, including its endpoints and jump values. Oddness gives the negative assertion.

**2. Exact Markov branches.** For \(j=2r\), truncation on \(I_j\) equals \(r\) and
\[H_m(I_{2r})=\left(\frac r d,\frac{r+m}d\right).\]
For \(j=2r+1\), truncation is again \(r\), and
\[H_m(I_{2r+1})=\left(\frac{r+m}d,\frac{r+2m}d\right).\]
Every branch has derivative \(m\) and maps onto exactly the \(m\) successive cells indicated by \(B\). The least image-cell index is \(1\) (from \(j=2\)); the largest is \(4m-4\) (from \(j=4m-5\)). These formulas also verify the image of each boundary lies within the closed core.

**3. Primitivity.** Let \(e=2m-2\). Every even cell \(j=2r\) with \(r\ge m-1\) has \(e\) among its successors. If \(r\le m-2\), it reaches an odd cell \(q=m\) for odd \(m\), or \(q=m-1\) for even \(m\), whose successors contain \(e\). Every odd cell \(j=2r+1\) with \(r\le m-2\) reaches \(e\) directly; those with \(r\ge m-1\) reach an even cell at least \(2m\), which in turn reaches \(e\). Hence every cell reaches \(e\) within two steps.

Conversely, \(e\) reaches cell \(2\): if \(m>2\), select an even cell smaller than \(e\) among its successors and repeatedly select from an even cell \(2r\ge4\) the smaller even successor \(2\lceil r/2\rceil\), until \(2\) is reached; for \(m=2\), \(e=2\) already. Cell \(2\) reaches all cells \(1,\ldots,m\). Inductively, a cell \(j\) with \(m+1\le j\le2m-3\) is reached from the smaller even cell \(2(j-m+1)\); cell \(2m-2\) is \(e\) itself. Thus \(e\) reaches the whole left half. Its successors include \(2m-3\), whose successors include \(e'=2m-1\). Away from branch boundaries, \(H_m(2-x)=2-H_m(x)\), so the Markov graph is symmetric under \(j\mapsto4m-3-j\): \(e'\) reaches the right half. The graph is strongly connected. Since \(e\) is a successor of itself, it is aperiodic and hence primitive.

**4. Physical measures and entropy.** The primitive row-stochastic matrix \(P=B/m\) has a unique strictly positive stationary vector \(\pi\), which is rational because its defining equations have rational coefficients and a unique solution. The transfer operator sends the density \(d\pi_j\) on \(I_j\) to
\[\rho'_\ell=\frac d m\sum_j\pi_j B_{j\ell}=d\pi_\ell.\]
Thus the asserted invariant probability exists. Under it, conditional on the current cell, each of the \(m\) successor cells has probability \(1/m\). A finite cell itinerary determines an interval whose length shrinks geometrically as \(m^{-n}\); hence the cell partition generates the Borel sigma-algebra modulo null sets. The primitive Markov chain is mixing, so the interval map is mixing and ergodic for this measure. The density is strictly positive on all core cells, making this measure equivalent to core Lebesgue measure. Any other invariant probability absolutely continuous with respect to Lebesgue measure is absolutely continuous with respect to this ergodic measure and must equal it. Birkhoff's theorem, together with nonsingularity of all branches and finite-time entry into the core, proves the two physical-basins assertion. Since each next-cell conditional law has \(m\) equiprobable possibilities, the generating Markov entropy is \(\log m\). The a.e. derivative equals \(m\), so the Lyapunov exponent is also \(\log m\).

**5. Bias and the small exact example.** Cell \(1\) has only cell \(2\) as an incoming predecessor. Consequently \(\pi_1=\pi_2/m\), excluding a uniform density for every \(m\ge2\). Solving the four-state balance for \(m=2\) gives the claimed probabilities. Integrating the resulting four-step density gives mean \(1\), second moment \(10/9\), and variance \(1/9\).

## Verification
Run `python3 verify.py` using the standalone Python 3 standard library. It checks the exact cell formulas and signed symmetry, the finite transition graphs for integers \(2\le m\le40\), exact stationary vectors for \(2\le m\le8\), finite sample basin entry, and the stated \(m=2\) moments. The reproduced run passed **13,078 exact finite checks**. These finite checks are supplementary and are not a substitute for the proof for arbitrary \(m\) or the ergodic argument.

## Relationship to prior work
Moysis, Kafetzis, Baptista and Volos (2022), equations (4), (22) and (23), introduce remainder-addition chaotification and study the linear seed chiefly using Lyapunov exponents, bifurcation figures and randomness tests. Their positive linear branch specializes to the map here when the seed factor is \(1/2\), the remainder modulus is \(1\), and the multiplier is \(m-1/2\). The accessible article does not give this integer-slope core, primitive Markov graph, two physical measures or exact invariant densities. General theorems on invariant densities of piecewise-linear Markov maps provide the standard transfer-operator framework, but do not identify the invariant cores and strongly connected transition graphs of this concrete infinite parameter family. The calculation therefore refines the measurable-dynamics description of the published model rather than asserting a new general Markov theorem.

## Limitations
The theorem uses the integer-resonant slope family only; no result is asserted for arbitrary continuous multiplier or seed factor. Discontinuities and their exact signed-remainder convention matter. Other singular invariant measures (for example the fixed point at zero and measures on periodic orbits) are not ruled out; uniqueness is only among absolutely continuous invariant probabilities on each core. Metric entropy is asserted for the two physical measures, not as an unrestricted notion of topological entropy on a discontinuous map of the whole real line. A nonuniform physical density by itself says nothing about practical cryptographic security or finite-precision randomness. Literature priority outside the inspected sources remains a possibility.

## References
1. L. Moysis, I. Kafetzis, M. S. Baptista and C. Volos, *Chaotification of One-Dimensional Maps Based on Remainder Operator Addition*, Mathematics **10** (2022), 2801. DOI: `10.3390/math10152801` (publicly available August 7, 2022).
2. G. Haddad and A. Boyarsky, *All invariant densities of piecewise linear Markov maps are piecewise constant*, Advances in Applied Mathematics **2** (1981). DOI: `10.1016/0196-8858(81)90008-7`.
3. P. Góra, *Invariant densities for piecewise linear maps of the unit interval*, Ergodic Theory and Dynamical Systems (2009). The general framework is not claimed as new.
4. L. Moysis et al., *Chaotification of 1D Maps by Multiple Remainder Operator Additions—Application to B-Spline Curve Encryption*, Symmetry **15** (2023), 726. DOI: `10.3390/sym15030726` (related multiremainder family; full text inspected).
