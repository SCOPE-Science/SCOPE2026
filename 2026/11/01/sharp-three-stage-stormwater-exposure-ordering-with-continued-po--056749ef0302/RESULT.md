# Sharp three-stage stormwater exposure ordering with continued pollutant supply

## Finding

Consider one pollutant held in a well-mixed surface stock, washed out at a rate proportional to the stock and to a prescribed runoff-dependent coefficient. During one observation period the coefficient takes each of three distinct positive values \(a>b>c>0\) for exactly one stage of the same length \(h>0\); the six stage orders are the only admissible alternatives. A constant positive fresh supply acts at the surface while wash-off occurs. Measure the time-integrated stock of pollutant already exported to a nonflushing receiving pool, rather than just its terminal exported mass.

Write \(m>0\) for initial surface mass and \(s>0\) for its constant supply rate, and let
\[
 z_r=\frac{1-e^{-rh}}{r}=\int_0^h e^{-rt}\,dt \qquad(r>0).
\]
Then \(0<z_a<z_b<z_c\). The **complete sharp maximum and minimum classification**, where a tuple lists the successive wash-off rates, is:

| Initial loading relative to continuing supply | Unique maximum | Unique minimum |
| --- | --- | --- |
| \(0<m/s<z_a\) | \((b,a,c)\) | \((b,c,a)\) |
| \(m/s=z_a\) | \((b,a,c)\) | Tie: \((b,c,a)\), \((c,b,a)\) |
| \(z_a<m/s<z_c\) | \((b,a,c)\) | \((c,b,a)\) |
| \(m/s=z_c\) | Tie: \((b,a,c)\), \((a,b,c)\) | \((c,b,a)\) |
| \(m/s>z_c\) | \((a,b,c)\) | \((c,b,a)\) |

All the indicated ties are exact, and there are no other maximizers or minimizers under the stated strict positivity and distinct-rate assumptions. The middle rate \(b\) affects the magnitudes but **neither of the switching thresholds**.

The two competing maximum orders and two competing minimum orders have exact gaps
\[
\begin{aligned}
 E(b,a,c)-E(a,b,c)&=(a-b)z_a z_b(s z_c-m),\\
 E(b,c,a)-E(c,b,a)&=(b-c)z_b z_c(m-s z_a).
\end{aligned}
\]
This three-stage competition is minimal: with just two prescribed positive wash-off stages, their order changes the corresponding exposure by a quantity proportional to initial mass alone; continuing supply cancels identically and therefore cannot reverse the preferred ordering.

## Assumptions and scope

The physical state is a nonnegative surface pollutant mass \(M(t)\), satisfying
\[
 M'(t)=s-k(t)M(t),\qquad M(0)=m>0,
\]
where \(k(t)>0\) is piecewise constant. A second stock \(P(t)\), initially zero, counts pollutant exported from that surface:
\[
 P'(t)=k(t)M(t),\qquad P(0)=0.
\]
There is no loss, dilution, travel-time delay, or chemical transformation in this receiving stock during the observation interval. Thus \(P\) is cumulative exported mass, not a measured concentration, and the explicitly defined exposure proxy is
\[
 E=\int_0^{3h}P(t)\,dt
   =\int_0^{3h}(3h-t)k(t)M(t)\,dt.
\]
It has dimensions mass multiplied by time. In particular, the theorem is *not* a statement about the maximum instantaneous runoff pollutant flux, total event load, clinical exposure, pollutant toxicity, or a routed/nonlinear watershed. The constant supply represents idealized continuing introduction to the same removable stock, not the separate wet-deposition routing compartments in a full stormwater simulator. The three stage durations are all \(h\); only their order is allowed to vary. All parameters are deterministic, positive, and known.

## Proof

**1. Conservation and local interval formula.** Put \(T=3h\). Since \((P+M)'=s\) and \(P(0)=0\), one has \(P(t)=m+st-M(t)\). Consequently
\[
 E=mT+\frac{sT^2}{2}-\int_0^T M(t)\,dt.
\]
For a constant rate \(r>0\) over one interval of length \(h\), let \(u_r=e^{-rh}\), \(z_r=(1-u_r)/r\), and \(w_r=(h-z_r)/r\). With incoming stock \(M_{\mathrm{in}}\), direct integration of the scalar equation gives
\[
 M_{\mathrm{out}}=u_rM_{\mathrm{in}}+sz_r,
 \qquad\int_{\mathrm{stage}}M(t)\,dt=z_rM_{\mathrm{in}}+sw_r.
\]
All these identities hold without an approximation.

**2. Exact order-dependent expression.** For a stage order \((r_1,r_2,r_3)\), successive substitution gives
\[
\begin{split}
 \int_0^T M(t)\,dt={}&m\bigl(z_{r_1}+u_{r_1}z_{r_2}+u_{r_1}u_{r_2}z_{r_3}\bigr)\\
 &+s\Bigl(\sum_{j=1}^3w_{r_j}
 +z_{r_1}z_{r_2}+z_{r_2}z_{r_3}
 +u_{r_2}z_{r_1}z_{r_3}\Bigr).
\end{split}
\]
Since \(1-u_{r_2}=r_2z_{r_2}\), the supply term is exactly
\[
 s\Bigl(\sum_{r\in\{a,b,c\}}w_r
  +z_az_b+z_az_c+z_bz_c-r_2z_az_bz_c\Bigr).
\]
In particular, defining \(Z=z_az_bz_c>0\), the *entire* permutation-dependent part of exposure is
\[
 E(r_1,r_2,r_3)
 \equiv-m\bigl(z_{r_1}+u_{r_1}z_{r_2}+u_{r_1}u_{r_2}z_{r_3}\bigr)
 +sZr_2,
\]
where \(\equiv\) means equality after adding the **same** order-independent constant to both sides. The continued-supply contribution depends only on the middle rate.

**3. Comparison at fixed middle rate.** Suppose the two outer rates are \(r>q>0\) and the middle rate is fixed at \(v\). Because every stage has length \(h\), at each \(t\in[0,T]\) the cumulative integral of the rate in the ordering \((r,v,q)\) is at least that for \((q,v,r)\), and it is strictly larger on a set of positive measure. Their integrals are equal at time \(T\). The portion of \(M(t)\) evolving from the initial mass is \(m\exp(-\int_0^t k)\), so its time integral is strictly *smaller* for \((r,v,q)\). The supply contribution to exposure is equal because the middle rate is unchanged. Therefore
\[
 E(r,v,q)>E(q,v,r).
\]
It follows that the best and worst orders within each fixed-middle class put the larger and the smaller of the two outer rates first, respectively.

**4. Eliminate dominated classes.** The best order with middle \(c\) is \((a,c,b)\). Replacing it by \((a,b,c)\) swaps the second and third rates into descending order, strictly reducing the time integral of the remaining *initial* mass; it also raises the middle rate from \(c\) to \(b\), strictly increasing the supply contribution \(sZr_2\). Thus \((a,c,b)\) cannot maximize exposure. The only maximum candidates are \((a,b,c)\) and \((b,a,c)\).

Similarly, the worst order with middle \(a\) is \((c,a,b)\). Replacing it by \((c,b,a)\) reverses the final pair to put the smaller rate first; it strictly increases the integrated residual initial mass and lowers the supply contribution. Thus \((c,a,b)\) cannot minimize exposure. The only minimum candidates are \((c,b,a)\) and \((b,c,a)\). All eliminations are strict since \(m,s>0\) and \(a,b,c\) are distinct.

**5. Compute the two exact boundaries.** For any rates \(r>q>0\), the difference between the residual-initial-mass integrals for orders beginning \((r,q)\) and \((q,r)\), with a common subsequent stage, is
\[
 (z_r+u_rz_q)-(z_q+u_qz_r)
 =-(r-q)z_rz_q.
\]
Applying the formula in Step 2 to the remaining candidate pairs yields exactly the two exposure-gap identities in the Finding section. Because their coefficients are strictly positive, their signs give precisely the displayed five cases and all equality boundaries.

**6. Why three stages are minimal.** With two positive constant-rate stages \((r,q)\), the corresponding integrated residual-stock supply term is \(s(w_r+w_q+z_rz_q)\), invariant under reversing their order, even if each stage is assigned its own positive duration. Hence the exposure difference is \(m(r-q)z_rz_q\), with the appropriate duration inserted into each \(z\). For \(m>0\), the larger wash-off rate first always gives greater time-integrated exported mass, independently of \(s\). When \(m=0\), the two orders tie. This proves the minimal three-stage reversal statement.

## Verification

The standalone file `verify.py` reconstructs the exact stagewise ODE integrals and the simplified permutation scores separately. It tests all six orders against the optimal-order classification over 2,200 deterministic random positive parameter choices, verifies the two gap identities at each parameter choice, and checks an exact rational example including both equality boundaries. Run `python verify.py` with a standard Python 3 installation; it prints `VERIFY_OK assertions=22058` if all checks succeed.

An exact reproducible example uses time units with \(h=\log 2\), \((a,b,c)=(3,2,1)\), and \(s=1\). Then \((z_a,z_b,z_c)=(7/24,3/8,1/2)\). For \(m=1/3\), the unique maximum is \((2,3,1)\) and the unique minimum is \((1,2,3)\). The respective strict advantage over the adjacent competing candidate is exactly \(7/384\) and \(1/128\) units of mass-time. The threshold values \(m/s=7/24\) and \(m/s=1/2\) generate exactly the ties in the theorem. The exact fractions are checked, not inferred from floating-point comparisons.

The checker is a finite reproducibility test, not an exhaustive proof over the continuous parameter domain; the analytic ordering and equality proofs are in Steps 1–6.

## Relationship to prior work

Sartor and Boyd's 1972 U.S. Environmental Protection Agency study established the empirical basis for exponential wash-off dependent on rainfall intensity. Vaze and Chiew (first published 19 June 2003) experimentally examined the dependence of pollutant wash-off on rainfall and runoff intensities; their full article studies measured loads, not the permutation optimization here. Soonthornnonda, Christensen, Liu, and Li (online article date 12 June 2008) derived and calibrated a first-order exponential washoff model with initial loading determined by antecedent dry-weather deposition. Their stated within-event differential equation has no simultaneous constant fresh loading and their full article does not supply this three-block integrated-exposure ordering classification. SWMM-type implementations also recognize rainfall/runon pollutant supplies, but generally route them through additional surface water compartments; the simplified single-stock system in this theorem is not claimed to coincide with full SWMM.

Classical variation of constants solves the scalar differential equation, and ordinary pairwise rearrangement explains part of the initial-mass behavior. Neither fact by itself states the exact competing maximum/minimum stage orders, two distinct loading thresholds, equality cases, and middle-rate independence as one complete classification. These are the specific claims assessed here; there is no novelty claim for the exponential washoff law or the general ODE solution.

## Limitations

The result is exact only for one linear well-mixed surface stock with an additive constant fresh supply, three stages of equal duration, and an unflushed accumulating receiving pool. Other choices of exposure kernel, supply varying with rainfall, nonlinear runoff response, sediment-size heterogeneity, catchment routing, water residence time, and unequal stage lengths may change the optimal orders. The toy model does not quantify an actual hydrological treatment recommendation or public-health risk. Although primary hydrological papers and broad sequencing alternatives were compared, an earlier equivalent result in linear-control or scheduling theory remains possible; independent priority verification has not been performed.

## References

1. Sartor, J. D. and Boyd, G. B. (1972), *Water Pollution Aspects of Street Surface Contaminants*, U.S. Environmental Protection Agency, EPA-R2-72-081, November 1972. https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9100TDJJ.TXT
2. Vaze, J. and Chiew, F. H. S. (2003), *Study of pollutant washoff from small impervious experimental plots*, Water Resources Research 39(6), first published 19 June 2003. https://doi.org/10.1029/2002WR001786
3. Soonthornnonda, P., Christensen, E. R., Liu, Y., and Li, J. (2008), *A washoff model for stormwater pollutants*, Science of the Total Environment 402, 248–256; PubMed article date 12 June 2008. https://doi.org/10.1016/j.scitotenv.2008.04.036
4. OpenSWMM Engine, *Chapter 4: Surface Washoff*, Sections 4.2.1 and 4.2.5, online technical documentation, https://www.hydrocouple.org/openswmm.engine/df/d15/quality_ref_ch4_surface_washoff.html (accessed 31 October 2026 UTC).
