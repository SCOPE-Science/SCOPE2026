# A one-crossing law for catastrophe-sensitive persistence rankings of two-patch metapopulations

## Finding

Consider a two-patch occupancy metapopulation that starts with both patches occupied. Patch 1 has local extinction rate \(u>0\), patch 2 has local extinction rate \(v>0\); an occupied patch 1 colonizes an empty patch 2 at rate \(a>0\), while occupied patch 2 colonizes empty patch 1 at rate \(b>0\). Independently, while the metapopulation is nonempty, a regional catastrophic event occurs at rate \(r\geq0\) and immediately empties all occupied patches. The empty state is absorbing. Let \(T(r)\) be the expected time until regional extinction.

Define \(E=u+v\), \(K=a+b\), \(U=uv\), and \(A=ab\). Then the extinction time has the exact expression

\[
T(r;U,A)=\frac{r^2+(2E+K)r+E^2-U+EK+A}{r^3+(2E+K)r^2+(E^2+U+EK+A)r+U(E+K)}.
\]

Compare two designs \(P,Q\) with the **same** local-extinction sum \(E>0\) and **same** recolonization sum \(K>0\). Write their rate products as \((U,A)\) and \((V,B)\), respectively, and let \(D_P,D_Q\) be the strictly positive denominators in the displayed formula. Then

\[
\boxed{T_P(r)-T_Q(r)=-\frac{(E+K+2r)\big[(U-V)(r+E)(r+E+K)+BU-AV\big]}{D_P(r)D_Q(r)}.}
\]

Consequently, the ranking of two matched-total designs **reverses at most once** as \(r\) increases through \([0,\infty)\). If \(U\ne V\), the designs have a unique strict ranking reversal at some \(r_*>0\) if and only if

\[
\frac{AV-BU}{U-V}>E(E+K).
\]

In that case the sole crossover is

\[
\boxed{r_*=-E-\frac K2+\sqrt{\frac{K^2}{4}+\frac{AV-BU}{U-V}}.}
\]

If \(U=V\), the ranking is constant, with equality for all \(r\) exactly when \(A=B\). If \(U\ne V\) and the threshold inequality is an equality, there is a tie only at \(r=0\); if it is reversed, no tie occurs on \([0,\infty)\).

The one-reversal bound is attained by designs with the same total rates. Design \(P\) has \((u,v,a,b)=(1,1,2,2)\), while \(Q\) has \((u,v,a,b)=(4/5,6/5,1,3)\). Both have \(E=2\) and \(K=4\), and

\[
\boxed{T_P(r)-T_Q(r)=-\frac{2(r-1)(r+9)}{(r^2+5r+2)(25r^3+200r^2+399r+144)}.}
\]

Thus \(P\) persists longer for \(0\le r<1\), both designs tie at \(r=1\), and \(Q\) persists longer for \(r>1\).

## Assumptions and scope

All local transitions are independent exponential clocks with the stated strictly positive rates; colonization is possible only when exactly one patch is occupied. The common shock is an independent exponential clock that sends each nonempty state directly to complete extinction. No immigration is allowed from the empty state. The result concerns the expectation of the absorption time, not a quantile or a fixed-time survival probability. Rate totals are matched between compared designs, with no assertion that arbitrary product pairs are independently feasible outside positive rate choices. The comparison includes \(r=0\) and holds for all finite \(r\ge0\).

## Proof

Use states \(11,10,01,00\), where the first bit indicates occupancy of patch 1. The state \(00\) is absorbing. Write \(t_{11},t_{10},t_{01}\) for the expected absorption times from the respective nonempty states. First-step conditioning gives the exact equations

\[
\begin{aligned}
(r+u+v)t_{11}&=1+v t_{10}+u t_{01},\\
(r+u+a)t_{10}&=1+a t_{11},\\
(r+v+b)t_{01}&=1+b t_{11}.
\end{aligned}
\]

Solve the last two equations to obtain \(t_{10}=(1+a t_{11})/(r+u+a)\) and \(t_{01}=(1+b t_{11})/(r+v+b)\). Substitution gives

\[
t_{11}=\frac{1+v/(r+u+a)+u/(r+v+b)}{r+u+v-va/(r+u+a)-ub/(r+v+b)}.
\]

The denominator is strictly positive: in fact, each of the subtracted terms satisfies \(va/(r+u+a)<v\) and \(ub/(r+v+b)<u\), since \(u,v>0\). Multiplying the expression by \((r+u+a)(r+v+b)\), collecting coefficients, and using \(E=u+v\), \(K=a+b\), \(U=uv\), \(A=ab\), gives the rational expression stated above. The denominator polynomial \(D(r)\) has strictly positive coefficients (and a positive constant term \(U(E+K)\)), so \(D(r)>0\) for all \(r\ge0\). Regional extinction is almost sure, even when \(r=0\), because each local extinction has positive rate and complete extinction is accessible from all transient states; the finite-state transient chain has finite mean absorption time.

For two designs with matched \(E,K\), cross-multiply the rational expressions. Direct coefficient collection yields exactly

\[
N_P(r)D_Q(r)-N_Q(r)D_P(r)=-(E+K+2r)\big[(U-V)(r+E)(r+E+K)+BU-AV\big].
\]

Since \(E+K+2r>0\) and both denominator polynomials are positive, the sign of the difference is the negative sign of the bracket. If \(U=V\), that bracket is constant; since \(U=V>0\), its vanishing is equivalent to \(A=B\). If \(U\ne V\), its unique possible zero is determined by the strictly increasing function \(h(r)=(r+E)(r+E+K)\) on \([0,\infty)\). Its range is \([E(E+K),\infty)\); solving \(h(r)=(AV-BU)/(U-V)\) proves the necessary-and-sufficient threshold and crossover formula. For strict inequality the root is simple because \(h'(r)=2r+2E+K>0\); hence the sign genuinely reverses. Equality at the endpoint is a tie only at \(r=0\), with no interior crossing.

Finally, substitute the two specified rational rate quadruples into the rational formula. Exact factorization gives the displayed difference with positive denominator for every \(r\ge0\). The factor \((r-1)(r+9)\) establishes the strict sign reversal and completes the example.

## Verification

The companion `verify_two_patch.py` uses only Python 3 standard-library rational arithmetic. Run `python3 verify_two_patch.py` from the directory containing this result. It checks \(3125\) rational first-step systems against the closed expression, compares \(729\) exact integer-coefficient polynomials under matched rate totals, and checks the sharp example at five rational catastrophe rates; expected output is `VERIFY_OK first_step_exact=3125 comparison_polynomials=729 sharp_example=5`. These finite checks test independent algebraic implementations and examples; the universal conclusions follow from the displayed first-step equations and exact polynomial factorization, not finite sampling.

## Relationship to prior work

Lande (1993) analytically investigates stochastic population extinction and catastrophes for one density-regulated population; it does not treat the two-patch colonization chain or matched-budget ranking comparison. Etienne and Heesterbeek (2001) study management of a stochastic metapopulation by changing extinction and colonization parameters; the accessible abstract and relevant thesis summaries do not establish a universal single-reversal comparison indexed by regional-catastrophe intensity. Johst and Drechsler (2003) examine spatial correlation of habitat disturbances by spatially explicit modeling; their accessible abstract concerns a different source of environmental variation and does not assert this exact matched-total classification. Drake and Griffen (2013) experimentally test source–sink effects on metapopulation extinction; it is a different experimental model and does not imply the algebraic comparison. The exact first-step calculation itself is a standard finite-state Markov-chain technique and is not claimed as novel. The specific matched-total one-crossing law and explicit reversible ordering are the assessed contributions.

## Limitations

The result is confined to two patches with memoryless local transitions, independent fully destructive regional shocks, and comparison of mean absorption times. More patches, nonexponential holding times, partial catastrophes, time-varying rates, fixed-time persistence probabilities, and biologically calibrated intervention costs are not covered. Full text of the historical articles by Etienne and Heesterbeek (2001) and Johst and Drechsler (2003) was not accessible during the literature assessment; equivalent previously published coverage remains a residual originality risk. No empirical validation is established.

## References

1. Lande, R. (1993). “Risks of Population Extinction from Demographic and Environmental Stochasticity and Random Catastrophes.” *The American Naturalist* **142**, 911–927. Lawful full text: https://ms.mcmaster.ca/~bolker/misc/lande1993.pdf .
2. Etienne, R. S., and Heesterbeek, J. A. P. (2001). “Rules of Thumb for Conservation of Metapopulations Based on a Stochastic Winking-Patch Model.” *The American Naturalist* **158**, 389–407. DOI: https://doi.org/10.1086/321986 .
3. Johst, K., and Drechsler, M. (2003). “Are spatially correlated or uncorrelated disturbance regimes better for the survival of species?” *Oikos* **103**, 449–456. First published 2003-10-21. DOI: https://doi.org/10.1034/j.1600-0706.2003.12770.x .
4. Drake, J. M., and Griffen, B. D. (2013). “Experimental demonstration of accelerated extinction in source-sink metapopulations.” *Ecology and Evolution* **3**, 3369–3378. DOI: https://doi.org/10.1002/ece3.713 . Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3797484/ .
