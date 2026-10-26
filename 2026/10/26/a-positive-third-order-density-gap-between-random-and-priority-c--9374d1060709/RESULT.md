# A positive third-order density gap between random and priority colouring in two-layer adsorption

## Finding

In two-colour continuum random sequential adsorption, **randomly choosing an available colour and always taking the first available colour do not preserve the total accepted-particle density**. The discrepancy appears at the first order at which deposition can be rejected. More precisely, let proposals have spatial intensity \(r>0\) per unit volume per unit time. Let \(E\subset\mathbb R^d\) be a bounded measurable symmetric exclusion neighbourhood, with volume \(|E|\), so that two proposed objects conflict exactly when the difference of their centres belongs to \(E\). Let \(\rho_{\mathrm{rnd}}(t)\) and \(\rho_{\mathrm{pri}}(t)\) be the total expected accepted-centre intensities when two colours are assigned, respectively, uniformly among available colours and in the fixed order first then second. Set

\[
T(E)=\int_E\!\int_E \mathbf1_{\{y-z\in E\}}\,dy\,dz.
\]

For fixed \(r,E\), as \(t\downarrow0\),

\[
\begin{aligned}
\rho_{\mathrm{rnd}}(t)&=rt-\frac{r^3t^3}{12}(|E|^2+T(E))+O_{r,E}(t^4),\\
\rho_{\mathrm{pri}}(t)&=rt-\frac{r^3t^3}{6}T(E)+O_{r,E}(t^4),\\
\rho_{\mathrm{pri}}(t)-\rho_{\mathrm{rnd}}(t)&=\frac{r^3t^3}{12}(|E|^2-T(E))+O_{r,E}(t^4).
\end{aligned}
\]

For rods of fixed length \(\sigma>0\) on the line, \(E=(-\sigma,\sigma)\), so

\[
\rho_{\mathrm{rnd}}(t)=rt-\frac7{12}r^3\sigma^2t^3+O(t^4),\qquad
\rho_{\mathrm{pri}}(t)=rt-\frac12r^3\sigma^2t^3+O(t^4),
\]
\[
\boxed{\rho_{\mathrm{pri}}(t)-\rho_{\mathrm{rnd}}(t)
=\frac1{12}r^3\sigma^2t^3+O(t^4).}
\]

For disks of diameter \(\sigma>0\) in the plane, \(E\) is the disk of radius \(\sigma\), and

\[
\begin{aligned}
\rho_{\mathrm{rnd}}(t)&=rt-r^3\sigma^4\left(\frac{\pi^2}{6}-\frac{\sqrt3\pi}{16}\right)t^3+O(t^4),\\
\rho_{\mathrm{pri}}(t)&=rt-r^3\sigma^4\left(\frac{\pi^2}{6}-\frac{\sqrt3\pi}{8}\right)t^3+O(t^4),\\
\rho_{\mathrm{pri}}(t)-\rho_{\mathrm{rnd}}(t)&=\frac{\sqrt3\pi}{16}r^3\sigma^4t^3+O(t^4).
\end{aligned}
\]

Both displayed gaps have strictly positive leading coefficients. Thus the non-equivalence is a quantitative density effect, not merely a change in colour labels.

## Assumptions and scope

Start from no deposited objects at time zero. Proposals form a homogeneous space-time Poisson process on \(\mathbb R^d\times(0,\infty)\) with intensity \(r\,dx\,dt\). Each accepted object retains its assigned colour forever. An arriving object may receive a colour precisely when no previously accepted object of that colour overlaps it; it is rejected only when both colours are unavailable. In the random protocol, choose uniformly from the colours currently available, with independent auxiliary random draws. In the priority protocol, always choose colour 1 when available, otherwise colour 2. Both protocols are driven by the same proposal intensity and geometrical conflict rule. Tangencies are immaterial under the continuous Poisson process.

The leading formulas hold for every fixed bounded measurable symmetric exclusion set \(E\) with \(0<|E|<\infty\) (in the usual setting the exclusion set contains a neighbourhood of zero). The remainder constants may depend on \(r\), the geometry and the dimension; the result is a short-time expansion at fixed parameters, not a claimed uniform bound in dimension, time or density. Expected density is the mean number of retained centres per unit volume, **summed over both colours**, and is not the fraction of space covered by the geometric objects.

## Proof

**1. Reduction to three proposals.** Insert a test proposal at the origin at time \(s>0\). Let \(U=E+E\), which has finite volume. All earlier proposals whose centres directly conflict with the test proposal lie in \(E\). Any earlier proposal capable of directly altering the admission or colour of such a proposal has centre in \(U\). On the event that the entire set \(U\) contains exactly two earlier proposals, both must lie in \(E\) for the test proposal to be rejected, and their colours and admissions depend only on their mutual overlap. Earlier proposals outside \(U\) cannot directly conflict with either of these two. The probability of at least three earlier proposals in \(U\) is \(O_{r,E}(s^3)\), by the Poisson tail. The factor for exactly two includes \(e^{-rs|U|}=1+O_{r,E}(s)\). Consequently, to order \(s^2\) the test rejection probability is obtained by integrating the two-proposal histories in \(E\times E\) with a factor \(r^2s^2/2\). The earlier arrival order is uniform, and the admission probability of the first two is one at this order.

**2. Exact two-proposal colour calculation.** Suppose the two earlier centres are \(y,z\in E\). If \(y-z\in E\), they overlap and are necessarily given opposite colours under both protocols. The test proposal is then rejected. If \(y-z\notin E\), the two earlier objects do not overlap. Under random assignment they independently take uniformly random colours, and the test proposal is rejected with probability \(1/2\); under priority assignment both receive colour 1, leaving colour 2 available, so the test proposal is accepted. Therefore, writing \(F_{\mathrm{rnd}}(s)\) and \(F_{\mathrm{pri}}(s)\) for the rejection probabilities of the test proposal,

\[
\begin{aligned}
F_{\mathrm{rnd}}(s)
&=\frac{r^2s^2}{2}\left(T(E)+\frac{|E|^2-T(E)}2\right)+O(s^3)
=\frac{r^2s^2}{4}(|E|^2+T(E))+O(s^3),\\
F_{\mathrm{pri}}(s)&=\frac{r^2s^2}{2}T(E)+O(s^3).
\end{aligned}
\]

**3. Convert acceptance to density.** Poisson insertion (equivalently, the intensity balance for accepted arrivals) yields the exact identity

\[
\rho_{\mathrm{protocol}}(t)=r\int_0^t(1-F_{\mathrm{protocol}}(s))\,ds.
\]

Integration of the preceding two expansions yields the three claimed formulas with \(O(t^4)\) remainders. A graphical construction is well defined at each fixed time: the expected number of backward dependency paths of length \(n\) through the finite conflict neighbourhood is bounded by \((r|E|t)^n/n!\), which tends to zero. This also justifies taking stationary spatial intensities on infinite space.

**4. Evaluate the geometry.** For rods, \(|E|=2\sigma\). The region of \((y,z)\in E^2\) satisfying \(|y-z|<\sigma\) has area \(3\sigma^2\), hence \(T(E)=3\sigma^2\) and \(|E|^2-T(E)=\sigma^2\). For disks, \(|E|=\pi\sigma^2\), and using the intersection area of two radius-\(\sigma\) disks whose centres are distance \(u\) apart gives

\[
T(E)=2\pi\int_0^\sigma u\left(2\sigma^2\arccos\frac{u}{2\sigma}-\frac u2\sqrt{4\sigma^2-u^2}\right)\,du
=\sigma^4\left(\pi^2-\frac{3\sqrt3\pi}{4}\right).
\]

Substitution gives all one- and two-dimensional coefficients. The witness \(y=-0.9\sigma\), \(z=0.9\sigma\), followed by a test arrival at the origin makes the mechanism explicit: the first two rods conflict with the third but not with each other. The fixed-priority protocol accepts the third; random assignment rejects it whenever the earlier colours differ. The set of such triples has positive volume.

## Verification

Run `python verify.py` from the same directory as this file, with Python 3 and `mpmath` installed. The checker verifies the rational one-dimensional coefficients, the two-dimensional overlap integral to high precision, strict positivity and consistency of the two-dimensional coefficients, an explicit ordered three-arrival witness, and independent seeded Monte Carlo evaluations of both geometric overlap probabilities. Its output is in `CHECK_OUTPUT.txt`.

The integral identities and Poisson short-time argument are analytic proofs; the Monte Carlo calculations are *not* used to infer any infinite-volume theorem. The numerical sample sizes and randomness seed are stated in the checker. Numerical checks cannot establish originality.

## Relationship to prior work

Parida and Dhillon introduced the random-available-colour multilayer adsorption model and, in their Section II and equation (1), proposed that using the first available colour instead would preserve the **total** density. Their one-dimensional density results use a recursive monolayer approximation after this proposed equivalence, and their two-dimensional extension likewise uses that procedure. The complete relevant preprint defines the two schemes explicitly; it does not establish the positive discrepancy displayed here. The present result identifies the first order of failure and evaluates its coefficient for the actual continuum rod and disk models.

Fleurke and Külske analysed a discrete two-row nearest-neighbour parking process with deterministic first-row priority and with/without screening, via closed equations for local-pattern densities. That is a related priority-allocation system, not a comparison with *random choice among available colours* for continuum Poisson rods or disks. The qualitative fact that greedy colouring may depend on colour selection does not supply the evaluated space-time density coefficients.

## Limitations

No finite-time global ordering \(\rho_{\mathrm{pri}}(t)>\rho_{\mathrm{rnd}}(t)\) is established beyond sufficiently small positive times. No jammed-state density, multi-colour extension, or higher-order coefficient is claimed. The source's full approximate density curves are not proved globally wrong by a local asymptotic gap; the claim specifically addresses the stated exact equivalence and its leading density consequence. The result does not assess empirical accuracy of other approximation methods. The priority relation to wider greedy-colouring or adsorption literature remains subject to independent scholarly assessment.

## References

1. P. Parida and H. S. Dhillon, *Multilayer Random Sequential Adsorption*, arXiv:2202.10547v1, first posted 21 February 2022, https://arxiv.org/abs/2202.10547 ; full open preprint https://arxiv.org/pdf/2202.10547 (model rules in Section I-B; claimed density equivalence in Section II, equation (1); gap-density approximation in Section III; disk extension in Section IV).
2. S. R. Fleurke and C. Külske, *A Second-row Parking Paradox*, Journal of Statistical Physics 136 (2009), 285–295, https://doi.org/10.1007/s10955-009-9775-4 ; open full text https://link.springer.com/content/pdf/10.1007/s10955-009-9775-4.pdf .
