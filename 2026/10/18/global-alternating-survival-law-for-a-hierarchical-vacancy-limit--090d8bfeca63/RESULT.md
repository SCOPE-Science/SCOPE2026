# Global alternating-survival law for a hierarchical vacancy-limited community

## Finding
A directed predation chain with a shared vacancy-limited reproduction pool selects a **specific surviving independent set**, not merely an arbitrary feasible independent set. The selection is exact for arbitrary chain length, unequal positive reproduction and predation rates, and every nonempty nonnegative initial condition, provided all species have the same break-even vacant-site fraction.

**Theorem (global run-parity selection and extinction rates).** Let \(n\ge 2\), let \(r_i>0\) for \(1\le i\le n\), let \(p_i>0\) for \(1\le i<n\), and fix \(0<\delta<1\). For densities \(x_i\), set \(S=\sum_{j=1}^n x_j\), \(x_0=0\), \(p_0=0\), and consider
\[
\dot x_i=x_i\bigl[r_i(1-\delta-S)-p_{i-1}x_{i-1}\bigr],\qquad 1\le i\le n.
\]
Assume \(x_i(0)\ge0\), \(0<S(0)\le1\). Partition the initially occupied indices \(J=\{i:x_i(0)>0\}\) into maximal consecutive runs \([a,b]\). From each run retain precisely \(a,a+2,a+4,\ldots\le b\), and write \(T\) for the union of these retained indices.

Then every coordinate has an exponentially attained limit \(\ell_i\), with
\[
\ell_i>0\quad\Longleftrightarrow\quad i\in T,\qquad
\sum_{i\in T}\ell_i=1-\delta.
\]
Every initially present but eliminated species \(i\in J\setminus T\) obeys the **exact extinction exponent**
\[
\lim_{t\to\infty}\frac{\log x_i(t)}{t}=-p_{i-1}\ell_{i-1}<0.
\]
The limiting composition, although dependent on initial abundances, is uniquely determined by the convergent quadratures below. In particular, from strictly positive initial conditions on all \(n\) species, exactly the odd-indexed species \(1,3,5,\ldots\) persist, whatever the positive predation rates and however unequal the reproduction rates may be.

**Limit-composition formula.** Let \(a=\min J\), \(Z(t)=x_a(t)^{1/r_a}\), and for \(i\in J\) write \(y_i(t)=x_i(t)^{1/r_i}/Z(t)\). For surviving indices define
\[
c_i=\frac{x_i(0)^{1/r_i}}{x_a(0)^{1/r_a}}
\exp\!\left(-\frac{p_{i-1}}{r_i}\int_0^\infty x_{i-1}(s)\,ds\right)>0,
\qquad i\in T.
\]
For \(i=a\) or for the first index of any run, the predecessor is identically zero, so the integral vanishes. There is a unique \(z>0\) satisfying
\[
\sum_{i\in T}(c_i z)^{r_i}=1-\delta,
\qquad \ell_i=(c_i z)^{r_i}\ (i\in T).
\]
Thus initial zeros are treated exactly: each initially occupied run starts its own alternating survival pattern, with the earlier member of every adjacent pair selected.

**Transverse stability in the fully occupied case.** At any equilibrium having every odd coordinate positive, every even coordinate zero, and total occupancy \(1-\delta\), the Jacobian has \(\lceil n/2\rceil-1\) zero eigenvalues tangent to the continuum of equilibria. Its remaining eigenvalues are precisely
\[
-\sum_{i\ \mathrm{odd}}r_i\ell_i
\quad\text{and}\quad
-p_{2j-1}\ell_{2j-1}\quad (2j\le n),
\]
all strictly negative. Hence the interior of this odd-coordinate equilibrium manifold is normally attracting; individual points on the manifold are not claimed to be asymptotically attracting as isolated equilibria.

## Assumptions and scope
The state space is the closed occupancy simplex \(\{x_i\ge0,\ \sum x_i\le1\}\). Each individual species has positive reproduction rate \(r_i\), mortality \(d_i=\delta r_i\), and only species \(i-1\) preys on species \(i\) with rate \(p_{i-1}\), creating a vacant site. Reproduction requires vacancy, with vacancy \(1-S\). All species therefore have the same break-even vacancy \(\delta\), but their turnover and attack rates are otherwise arbitrary. The chain is finite and directed, and species do not spontaneously recolonize a coordinate that is initially zero. The theorem concerns deterministic mean-field densities, not finite-population survival probabilities.

The assumption \(0<\delta<1\) excludes the subcritical empty-community regime. Strict positivity of every predation edge is essential; without it, two adjacent species can survive. For the all-positive corollary, strictly positive initial densities are essential: a missing species remains absent and changes the run decomposition.

## Proof
**1. Positivity, global solutions, and a population floor.** Each coordinate equation has the form \(\dot x_i=x_i f_i(x)\), so nonnegativity, positivity of initially positive coordinates for finite time, and all initially empty faces are preserved. At \(S=1\), every nonzero coordinate contributes a strictly negative mortality term to \(\dot S\); the simplex is forward invariant. Polynomial local Lipschitz continuity and compact invariance yield global solutions.

Put \(s_*=1-\delta>0\), \(W(t)=\sum_i r_i x_i(t)\), \(G(t)=\sum_{i=1}^{n-1}p_i x_i(t)x_{i+1}(t)\), \(r_-=\min_i r_i\), \(r_+=\max_i r_i\), and \(P=\sum_i p_i\). Direct summation gives
\[
\dot S=(s_*-S)W-G.
\]
Because \(W\ge r_-S\), \(W\le r_+S\), and \(0\le G\le P S^2\),
\[
\dot S\ge r_-s_*S-(r_++P)S^2.
\]
Scalar logistic comparison therefore gives
\[
\liminf_{t\to\infty}S(t)\ge\frac{r_-s_*}{r_++P}>0.
\]
This floor is positive for each fixed admissible parameter vector and initial condition; it is not asserted uniform in parameters.

**2. Exact weighted-ratio law and positive roots.** Let \(a=\min J\). Since its preceding index is absent, \(x_a(t)>0\) and \(\dot x_a/r_ax_a=s_*-S\). Define \(Z=x_a^{1/r_a}\) and \(y_i=x_i^{1/r_i}/Z\) for \(i\in J\). Subtracting normalized per-capita growth rates yields the exact identity
\[
\frac{d}{dt}\log y_i(t)=-\frac{p_{i-1}}{r_i}x_{i-1}(t),
\qquad
 y_i(t)=y_i(0)\exp\!\left(-\frac{p_{i-1}}{r_i}\int_0^t x_{i-1}(s)\,ds\right).
\]
Every \(y_i\) is nonincreasing and bounded by \(y_i(0)\). Consequently
\[
S(t)=\sum_{i\in J}[y_i(t)Z(t)]^{r_i}
\le F_0(Z(t)),\qquad F_0(z)=\sum_{i\in J}[y_i(0)z]^{r_i}.
\]
The strictly increasing continuous function \(F_0\) vanishes at zero. The population floor therefore forces \(Z(t)\), and hence \(x_a(t)\), to be bounded away from zero eventually. For every run root \(b\), its preceding coordinate is identically zero, so \(y_b(t)=y_b(0)>0\), and \(x_b(t)=[y_b(0)Z(t)]^{r_b}\) is likewise eventually bounded below.

**3. Induction along every occupied run.** The first member \(b\) of a run is eventually bounded below by a positive constant. Since \(p_b>0\), the weighted ratio for its successor \(b+1\) decays exponentially, so \(x_{b+1}\) decays exponentially and has finite time integral. For the next member \(b+2\), the preceding population has finite integral; its ratio \(y_{b+2}\) therefore converges to a strictly positive constant, and \(x_{b+2}\) is eventually bounded below. Repeating alternately proves that precisely the indices \(b,b+2,\ldots\) in that run retain positive lower bounds; every other initially present index decays exponentially. Initially absent indices stay identically zero. This finite induction applies separately to all runs and establishes that \(G(t)\) decays exponentially, since every adjacent initially occupied pair includes an eliminated coordinate.

**4. Convergence of total occupancy and individual densities.** The logistic floor implies \(W(t)\ge w_0>0\) for all sufficiently large \(t\). Writing \(u(t)=S(t)-s_*\) gives an exact stable linear equation with a decaying forcing:
\[
\dot u=-W(t)u-G(t).
\]
Variation of constants, \(W\ge w_0\), and exponential decay of \(G\) imply \(u(t)\to0\) exponentially. For \(i\in T\), its predecessor either was absent or has exponentially decayed, so the integral defining \(c_i=\lim y_i(t)\) is finite and \(c_i>0\). For \(i\in J\setminus T\), the preceding population is eventually bounded below, so \(y_i(t)\to0\) exponentially. The total-density identity becomes
\[
\sum_{i\in T}[c_i Z(t)]^{r_i}+o(1)=s_*.
\]
Its left-hand limiting function is strictly increasing in positive \(Z\), is zero at \(Z=0\), and tends to infinity as \(Z\to\infty\). It has a unique root \(z\), and \(Z(t)\to z\). The convergence is exponential: all \(y_i(t)-c_i\) for \(i\in T\) are exponentially small, the eliminated terms are exponentially small, \(S-s_*\) is exponentially small, and the limiting function has strictly positive derivative near \(z\) (the term from \(i=a\) suffices). Therefore \(x_i(t)=[y_i(t)Z(t)]^{r_i}\to\ell_i\) exponentially, with the asserted support and composition.

**5. Sharp logarithmic extinction exponents.** For any eliminated but initially present \(i\), the ratio identity implies
\[
\log x_i(t)=r_i\log Z(t)+r_i\log y_i(0)
-p_{i-1}\int_0^t x_{i-1}(s)\,ds.
\]
The first two terms stay bounded, while \(x_{i-1}(t)\to\ell_{i-1}>0\). Divide by \(t\) and use convergence of time averages to obtain \(t^{-1}\log x_i(t)\to-p_{i-1}\ell_{i-1}\). This is an exact limit, not an assertion inferred from a finite simulation.

**6. Spectrum on the fully occupied attracting face.** At an odd-only equilibrium in the relative interior of \(\sum_{i\ \mathrm{odd}}x_i=s_*\), every even row of the Jacobian has just its diagonal entry \(-p_{i-1}\ell_{i-1}\), while the odd-to-odd block is the rank-one matrix with entries \(-r_i\ell_i\). The block-triangular characteristic polynomial gives one eigenvalue \(-\sum_{i\ \mathrm{odd}}r_i\ell_i\), the even invasion eigenvalues, and the stated tangent zeros. All transverse eigenvalues are strictly negative, completing the proof.

## Verification
The standalone, Python-standard-library script `verify_selection.py` checks 420 rational instances of the exact normalized-ratio derivative and population-balance identities, then integrates four distinct parameter examples with fourth-order Runge–Kutta, including unequal reproduction rates, seven species, and disconnected initial occupancy runs. Every integrated example exhibits the predicted surviving support and limiting total occupancy within the stated numerical tolerance. Run with `python3 verify_selection.py` in a directory containing the script. Finite testing supplements and does not replace the analytical arguments above.

For one five-species example, \((r_1,\ldots,r_5)=(2,2.1,2.2,2.3,2.4)\), \(\delta=1/3\), \((p_1,\ldots,p_4)=(4,5,3,4)\), and initial densities \((.15,.05,.12,.05,.1)\), numerical integration gives the approximate limiting vector \((.3439589521,0,.1957654675,0,.1269422471)\); its total is \(2/3\), as required. These decimals are illustrative, not exact algebraic constants.

## Relationship to prior work
Samanta et al., arXiv:2609.09027v1 (2026), introduce the directed hierarchical May–Leonard vacancy model. Their Section VI bounds the number of possible coexisting species by an independent-set count and proves that equal-reproduction/equal-mortality equilibria cannot contain adjacent species; their Appendix A describes three-species coexistence manifolds and transverse eigenvalues. Those are prior results. The present theorem instead provides the **globally selected** independent set from every initial support face, exponential convergence and sharp extinction exponents for arbitrary chain length, and permits unequal rates \(r_i\) under a common break-even vacancy \(d_i/r_i=\delta\). Neither an equilibrium adjacency restriction nor a maximal-cardinality independent-set bound implies which of several admissible configurations is approached from positive initial data.

Poley, Baron, and Galla (arXiv:2208.01569v1, 2022) study a generalized Lotka–Volterra cascade with random interaction coefficients and a large-population statistical limit. Their mean-field stability and abundance results do not give the deterministic fixed-chain all-initial-state parity-selection theorem. Baigent and Ching (2020) establish a balance simplex for general three-species May–Leonard systems, but an attracting invariant manifold alone does not specify exact species support or extinction exponents for finite chains of unrestricted length. The present argument uses an exact normalized-ratio identity adapted to the special one-sided predation structure and makes no general claim for those wider models.

## Limitations
The equality of break-even vacancies is structural. It can fail under small changes of individual mortality-to-reproduction ratios, in which case the fixed parity-selection conclusion need not hold. The theorem assumes strictly positive predation coefficients and no recruitment of species absent initially. Rate bounds can become arbitrarily slow if an initially present upstream species is extremely rare; the theorem is asymptotic and does not guarantee rapid observation of the final pattern. The continuum of odd-only equilibria means individual selected equilibrium compositions are non-universal. This is deterministic, well-mixed ecology; finite stochastic populations, spatial dispersal, trophic feedback and environmental forcing are not covered. The literature comparison is extensive but cannot rule out an older, unindexed general convergence theorem with equivalent specialization; no independent audit has been performed.

## References
1. R. Samanta, S. Dawn, S. Jahiruddin, S. Bhattacharyya, C. Hens and S. N. Chowdhury, *Selection Rules for Species Coexistence in a Hierarchical May–Leonard Model*, arXiv:2609.09027v1, first public 2026-09-08. https://arxiv.org/abs/2609.09027
2. L. Poley, J. W. Baron and T. Galla, *Generalised Lotka–Volterra model with hierarchical interactions*, arXiv:2208.01569v1 (2022); *Physical Review E* 107, 024313 (2023). https://arxiv.org/abs/2208.01569
3. S. Baigent and A. Ching, *Balance simplices of 3-species May–Leonard systems*, *Journal of Biological Dynamics* 14 (2020), 187–199, DOI: 10.1080/17513758.2020.1736656. https://discovery.ucl.ac.uk/id/eprint/10093501/
