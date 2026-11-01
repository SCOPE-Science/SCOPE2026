# Odd-divisor spectrum and exact cycle laws for crossing random circle chords

## Finding

Independently select the endpoints of each of several straight chords uniformly by angle on the unit circle. Let \(W\) be the symmetric indicator that two resulting chords cross in the open disk. The compact self-adjoint crossing operator \(T\) defined by this geometric kernel has a complete explicit spectral decomposition. For every positive odd integer \(d\), its nonzero eigenvalues and multiplicities are

\[
\lambda_d^+=\frac{4}{\pi^2d}\quad\text{with multiplicity }\tau(d),\qquad
\lambda_d^-=-\frac{4}{\pi^2d}\quad\text{with multiplicity }\tau(d)-\mathbf1_{\{d\text{ is a square}\}}.
\]

Here \(\tau(d)\) is the number of positive divisors of \(d\), and eigenvalues with zero multiplicity are absent. All nonzero eigenvalues are listed; zero is an accumulation point, not an eigenvalue. In particular, \(\|T\|=4/\pi^2\), and the largest eigenvalue is simple.

For each integer \(r\ge3\), let \(p_r\) be the probability that \(r\) independently sampled chords cross according to all edges of a labeled cycle (the last chord crosses the first, while crossings between nonadjacent chords are unrestricted). The entire sequence is

\[
p_r=\left(\frac4{\pi^2}\right)^r
\begin{cases}
(1-2^{-2r})\zeta(2r),&r\text{ odd},\\
2(1-2^{-r})^2\zeta(r)^2-(1-2^{-2r})\zeta(2r),&r\text{ even}.
\end{cases}
\]

In particular, every \(p_r\) is rational, with \(p_3=1/15\), \(p_4=1/35\), and \(p_5=31/2835\). The first-order crossing probability \(\Pr(W=1)=1/3\) is classical and is **not** claimed as new.

## Assumptions and scope

A chord is defined by two independent uniform points on the unit circle, and different chords are independent. All boundary coincidences (identical endpoints, coinciding midpoints at an exceptional distance, tangencies) are null events. This is *endpoint-uniform* chord sampling, not a Euclidean-motion-invariant random-line sampling convention. All results hold for the stated exact distribution, and the cycle event permits crossings among nonadjacent chords.

Represent almost every unordered chord uniquely by the midpoint \(\theta\in[0,2\pi)\) of its *shorter* circular boundary arc and that arc's half-angle \(h\in(0,\pi/2)\). Then \(\theta\) and \(h\) are independent and uniform with probability measure

\[
d\mu(\theta,h)=\frac{d\theta}{2\pi}\,\frac{2\,dh}{\pi}.
\]

Let \(\delta(\theta,\phi)\in[0,\pi]\) denote the smaller absolute angular separation. The geometric crossing kernel is

\[
W((\theta,h),(\phi,k))=\mathbf1_{\{|h-k|<\delta(\theta,\phi)<h+k\}}.
\]

The operator \(T\colon L^2(\mu)\to L^2(\mu)\) acts by \((Tf)(x)=\int W(x,y)f(y)\,d\mu(y)\). It is compact, Hilbert--Schmidt and self-adjoint, but not asserted to be trace class. Powers \(T^r\) are trace class for \(r\ge2\).

## Proof

**1. Parameterization and geometric crossing criterion.** For two independent circular endpoint angles, the shorter angular separation is uniform on \([0,\pi]\), and rotational symmetry makes its midpoint independent and uniform on the circle. Two chords cross exactly when their four endpoints alternate in cyclic order. In the shorter-arc coordinates, this is equivalent to \(|h-k|<\delta(\theta,\phi)<h+k\), since \(h+k\le\pi\).

**2. Fourier reduction.** Decompose \(L^2(\mu)\) into angular Fourier modes \(e^{im\theta}\), \(m\in\mathbb Z\). Integrating the crossing indicator over the relative midpoint angle gives the mode kernel, for \(0<h,k<L:=\pi/2\),

\[
\widehat W_0(h,k)=\frac2\pi\min(h,k),\qquad
\widehat W_m(h,k)=\frac{2}{\pi|m|}\sin(|m|\min(h,k))\cos(|m|\max(h,k))\quad(m\ne0).
\]

After including the radial probability density \(2/\pi\), the mode operator is \(4/\pi^2\) times the Green operator of \(\mathcal L_m=-\partial_h^2-m^2\), with a Dirichlet condition at \(h=0\). At \(h=L\), its condition is Neumann when \(m\) is even and Dirichlet when \(m\) is odd. The derivative jump of the Green kernel at \(h=k\) is \(-1\); this fixes the normalization and sign, including at \(m=0\) by continuity.

The boundary-value eigenfunctions are \(\sin(kh)\) with integer \(k\ge1\) satisfying \(m+k\) odd. Since \(k^2\ne m^2\) by parity, the Green inverse is defined. The orthonormal functions

\[
\psi_{m,k}(\theta,h)=\sqrt2\,e^{im\theta}\sin(kh),
\qquad m\in\mathbb Z,\ k\ge1,\ m+k\text{ odd},
\]

form a complete basis of \(L^2(\mu)\), and

\[
T\psi_{m,k}=\frac4{\pi^2(k^2-m^2)}\psi_{m,k}.
\]

This proves the exact signed eigenvalue formula, the absence of a kernel, compactness, and the operator norm.

**3. Divisor multiplicities.** Because \(k+m\) and \(k-m\) have odd parity, every nonzero \(|k^2-m^2|\) is an odd positive integer \(d\). For \(k>|m|\), the positive odd factors \(k-|m|\) and \(k+|m|\) multiply to \(d\). Every unordered distinct factor pair gives the two angular modes \(m=\pm|m|\); when \(d\) is an odd square, its equal-factor pair produces the unique mode \(m=0\). Thus the positive eigenvalue has multiplicity \(\tau(d)\). For \(|m|>k\), the factors \(|m|-k\) and \(|m|+k\) must be distinct, so the negative eigenvalue has multiplicity \(\tau(d)-\mathbf1_{\{d\text{ square}\}}\).

**4. All cyclic crossing events.** Independence of the chords and Fubini's theorem give \(p_r=\operatorname{tr}(T^r)\) for integers \(r\ge3\). Absolute convergence follows from the Hilbert--Schmidt property and bounded operator norm. Consequently,

\[
p_r=\left(\frac4{\pi^2}\right)^r\sum_{\substack{d\ge1\\d\text{ odd}}}
\frac{\tau(d)+(-1)^r[\tau(d)-\mathbf1_{\{d\text{ square}\}}]}{d^r}.
\]

For odd \(r\), only odd-square terms survive, yielding \((1-2^{-2r})\zeta(2r)\). For even \(r\), use the classical Dirichlet-series identity \(\sum_{d\text{ odd}}\tau(d)d^{-r}=(1-2^{-r})^2\zeta(r)^2\) and the odd-square series. This gives the displayed formula. Every zeta value has even integer argument and is a rational multiple of the appropriate power of \(\pi\), proving rationality of every cyclic probability. Substitution gives the stated examples.

## Verification

A standalone Python 3 checker (`verification/check_chord_spectrum.py`) carries out independent endpoint-order and midpoint-coordinate crossing comparisons; Fourier interval integrals; numerical residuals for both boundary-condition families; exact finite chord-diagram enumerations of cycles with \(r=3,4,5\); divisor-multiplicity counts; and truncated spectral-sum diagnostics. For three, four and five labeled chords, the exhaustive cycle counts are respectively \(6/90=1/15\), \(72/2520=1/35\), and \(1240/113400=31/2835\). These finite checks corroborate, but do not replace, the exact infinite-dimensional proof above.

Run the checker with `python3 verification/check_chord_spectrum.py` after extracting the embedded files. It has no third-party dependencies. The exact proof supplies the universal quantifiers and convergence; numerical quadrature or finite enumeration alone would not suffice.

## Relationship to prior work

The chord crossing event, the probability \(1/3\) for two endpoint-uniform chords, and circle-graph kernels have known antecedents. Bortolotto and Ramos (2024) study extremal probabilities for two random chord-supporting lines intersecting in prescribed concentric disks, establishing the boundary value \(1/3\) for atomless endpoint laws. Their operator is not diagonalized into the signed odd-divisor spectrum above and their assertions do not give the cycle-probability formula. Bortolotto and Souza (2025) investigate spatial distributions of intersection points, likewise without a crossing-operator spectral classification in the inspected version.

Diaconis, Holmes and Janson (2011), section 10.2, provide the general circle-graph limit representation via chord pairs; that representation supplies the general kernel framework but not the present explicit spectrum for the endpoint-uniform distribution. Acan (2015) analyzes degrees, cores and connected components of uniformly random chord diagrams rather than these spectral multiplicities or the entire cycle-density sequence. The independent endpoint-uniform model induces the uniform perfect-matching circular chord diagram after forgetting actual endpoint angles; this equivalence is used only as a check and not presented as new.

Gates (1982) calculates finite-chord intersection-count distributions and moments under a random-chord convention; accessible metadata does not establish whether every finite cycle value is already contained. In any event the main claim is the complete signed operator spectrum and the unbounded exact cycle-law family, not isolated small-cycle counts. An unavailable full text and unlocated earlier spectral treatment remain historical-priority risks.

## Limitations

This does not address other sampling conventions, unequal endpoint laws, noncircular convex curves, or higher-dimensional chord analogues. The claim does not assert historical priority for the two-chord probability or general circle-graph representations. Historical novelty is provisional; the full 1982 Gates article was not obtainable through the accessible sources. No independent mathematical audit has been performed.

## References

- Cynthia Bortolotto and João P. G. Ramos, *On Extremal Problems Associated with Random Chords on a Circle*, arXiv:2406.06771v1 (first posted June 10, 2024), https://arxiv.org/abs/2406.06771.
- Cynthia Bortolotto and Victor Souza, *Intersections of Random Chords of a Circle*, arXiv:2504.12866v1 (first posted April 17, 2025), https://arxiv.org/abs/2504.12866.
- Persi Diaconis, Susan Holmes and Svante Janson, *Interval Graph Limits*, arXiv:1102.2841v1 (2011), section 10.2, https://arxiv.org/abs/1102.2841.
- Hüseyin Acan, *On a Uniformly Random Chord Diagram and Its Intersection Graph*, arXiv:1501.01489v1 (2015), https://arxiv.org/abs/1501.01489.
- John Gates, *The Number of Intersections of Random Chords to a Circle — Third and Fourth Moments*, *Journal of Applied Probability* 19 (1982), 355--372, https://doi.org/10.2307/3213487 (full text not accessible in this review).
