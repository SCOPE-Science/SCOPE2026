# Sharp three-regime minimum-cost law for migratory seasonal occupancy

## Finding

Consider two seasonal classes of habitat, breeding and nonbreeding, with respective occupied fractions \(p,q\). Given positive extinction rates \(e,f\), colonization rates \(a,b\), positive unit costs \(k_B,k_W\), and required long-run occupied fractions \(u,v\in(0,1)\), the coupled continuous-time occupancy system is
\[
\dot p=a q(1-p)-e p,\qquad \dot q=b p(1-q)-f q.
\]
The conservation-design problem is to minimize \(k_Ba+k_Wb\) over positive \(a,b\) for which the attracting positive equilibrium satisfies \(p_*\ge u\) and \(q_*\ge v\).

**Theorem (all-target optimum and three phases).** Set \(E=k_Be\), \(F=k_Wf\), and
\[
 r=u\sqrt{\frac{E}{F(1-u)}},\quad
 v_- =\frac{r}{1+r},\quad
 s=\frac{u}{1-u}\sqrt{\frac EF},\quad
 v_+=\frac{2s}{s+\sqrt{s^2+4}}.
\]
Then \(0<v_-<v_+<1\). For every positive parameter choice, the unique minimum-cost equilibrium and its exact cost are
\[
 (p_*,q_*,B_*)=\begin{cases}
 \left(u,v_-,\dfrac{Eu}{1-u}+2\sqrt{\dfrac{EF}{1-u}}\right),&0<v\le v_-,\\[6pt]
 \left(u,v,\dfrac{Eu}{v(1-u)}+\dfrac{Fv}{u(1-v)}\right),&v_-\le v\le v_+,\\[6pt]
 \left(\dfrac{t}{1+t},v,\dfrac{Fv}{1-v}+2\sqrt{\dfrac{EF}{1-v}}\right),&v_+\le v<1,
 \end{cases}
 \qquad t=v\sqrt{\frac{F}{E(1-v)}}.
\]
The branches agree at the boundaries. The unique optimal colonization rates are recovered by
\[
 a_* =\frac{e p_*}{q_*(1-p_*)},\qquad
 b_* =\frac{f q_*}{p_*(1-q_*)}.
\]
The lower-target phase overshoots the nonbreeding target \(q_*>v\); the middle phase meets both targets exactly; the upper-target phase overshoots the breeding target \(p_*>u\). All inequalities are strict away from phase boundaries. Every such optimal system has \(a_*b_*>ef\), so its positive equilibrium exists and attracts every initially positive state.

For \(E=F\) and \(u=1/2\), the phase boundaries have the simple exact values
\[
 v_-=\sqrt2-1,\qquad v_+=\frac{\sqrt5-1}{2}.
\]
Thus even the equal-cost, equal-extinction case has a nonempty interval where both target constraints bind, between two intervals where investing enough to meet one target automatically exceeds the other.

## Assumptions and scope

All six primitive parameters \(a,b,e,f,k_B,k_W\) are positive, and the two required fractions satisfy \(0<u,v<1\). The state is confined to the invariant square \([0,1]^2\). The two colonization rates are freely chosen positive continuous-time rate parameters, with *linear rate-unit costs* and with extinction rates held fixed. The theorem does not impose upper bounds on colonization intensities. It is an equilibrium threshold and allocation result; the cost is not a present-value or dynamic intervention cost.

The same two nonlinear colonization/extinction balance terms occur in the discrete-year migratory metapopulation model of Taylor and Hall (2011). In that original yearly model the transition coefficients have probability bounds. The current theorem uses its continuous-time counterpart, for which arbitrary positive rate intensities are valid. The equilibrium formula also applies algebraically to admissible parameters of the original map, but the unrestricted optimization does not automatically respect its per-year rate caps.

## Proof

**1. Positive equilibrium and its inverse.** Writing \(a,b\) for the chosen colonization rates, solving the two balance equations gives the only possible positive equilibrium
\[
 p_* =\frac{ab-ef}{b(a+e)},\qquad q_* =\frac{ab-ef}{a(b+f)}.
\]
This equilibrium belongs to \((0,1)^2\) precisely when \(ab>ef\); otherwise zero is the only equilibrium in the nonnegative square. Conversely, any \((p,q)\in(0,1)^2\) is uniquely realized as a positive equilibrium by
\[
 a(p,q)=\frac{ep}{q(1-p)},\qquad
 b(p,q)=\frac{fq}{p(1-q)}.
\]
Its product is \(ab=ef/[(1-p)(1-q)]>ef\), and its cost is
\[
 C(p,q)=\frac{Ep}{q(1-p)}+\frac{Fq}{p(1-q)}.
\]
Therefore optimizing rates is exactly the unconstrained two-variable minimization of \(C\) over \(u\le p<1\), \(v\le q<1\). The cost diverges as either coordinate tends to one with the other bounded below, so the minimum is attained. The inverse formulas show the rate optimizer will be unique if the equilibrium optimizer is unique.

**2. Every optimum is on the target boundary.** For any \(0<h<1\) and a feasible pair whose two coordinates can both be reduced by a common factor \(h\),
\[
 C(hp,hq)=\frac{Ep}{q(1-hp)}+\frac{Fq}{p(1-hq)},
\]
which strictly increases with \(h\). Hence a pair with both \(p>u\) and \(q>v\) cannot minimize the cost: reduce both proportionally until at least one target binds. It suffices to minimize on the two edges \(p=u\) and \(q=v\).

**3. Unique edge minimizers.** On \(p=u\), substitution \(z=q/(1-q)>0\) gives
\[
 C(u,q)=\frac{Eu}{1-u}
 +\frac{Eu}{(1-u)z}+\frac Fu z.
\]
The last two summands have their unique minimum, by the arithmetic-geometric mean inequality, at \(z=u\sqrt{E/[F(1-u)]}=r\), giving \(q=v_-\) and cost \(Eu/(1-u)+2\sqrt{EF/(1-u)}\). If \(v>v_-\), the constrained minimum on this edge is instead its endpoint \((u,v)\).

Symmetrically, on \(q=v\), substitution \(w=p/(1-p)>0\) yields
\[
 C(p,v)=\frac{Fv}{1-v}
 +\frac{Fv}{(1-v)w}+\frac Ev w.
\]
Its unique unconstrained minimum occurs at \(w=v\sqrt{F/[E(1-v)]}=t\), giving \(p=t/(1+t)\) and cost \(Fv/(1-v)+2\sqrt{EF/(1-v)}\). The condition \(t/(1+t)=u\) is equivalent to \(v/\sqrt{1-v}=s\), which has the unique solution \(v=v_+=2s/(s+\sqrt{s^2+4})\). For \(v<v_+\), this edge's constrained minimum is \((u,v)\).

**4. The two thresholds are strictly ordered.** The function \(p_0(v)=t/(1+t)\) is strictly increasing in \(v\). At \((u,v_-)\), the derivative \(\partial_q C\) vanishes. Since simultaneous radial scaling strictly increases \(C\), the directional derivative \(u\partial_p C+v_-\partial_q C\) is strictly positive there; therefore \(\partial_p C(u,v_-)>0\). The unique minimizer of the function \(p\mapsto C(p,v_-)\) lies strictly below \(u\), so \(p_0(v_-)<u=p_0(v_+)\). Thus \(v_-<v_+\). When \(v\le v_-\), the optimum on \(p=u\) beats the corner and the optimum on \(q=v\) is the corner. When \(v_-\le v\le v_+\), both edge minima are the corner. When \(v\ge v_+\), the symmetric statement holds. Strict edge convexity in odds coordinates proves uniqueness, including equality cases.

**5. Attractivity.** The square is forward invariant and the vector field is cooperative on it, with nonnegative off-diagonal derivatives \(a(1-p)\) and \(b(1-q)\). If \(ab>ef\), the strictly positive equilibrium just established is unique. At any factor \(0<h<1\), the vector field evaluated at \(h(p_*,q_*)\) has both components strictly positive, whereas at \((1,1)\) both are negative. Order preservation makes the solutions from these sub- and supersolutions increase and decrease respectively. Their limits are equilibria, and the lower solution excludes the origin; hence both limits are \((p_*,q_*)\). Every strictly positive initial state lies between a sufficiently small positive multiple of the equilibrium and \((1,1)\), so the comparison theorem gives global convergence to the positive equilibrium.

## Verification

Run `python3 VERIFY.py` using Python 3 with no third-party packages. The checker deterministically verifies balance equations, the exact inverse correspondence, strict threshold ordering, branch formulas, the weighted budget, and tens of thousands of sampled feasible perturbations across all three phases. It also checks an exact rational symmetric equilibrium and the radical thresholds for \(E=F\), \(u=1/2\). The expected terminal line begins `VERIFY_OK`. These finite tests are *not* the proof of universal optimality; the proof is the edge reduction, arithmetic-geometric mean and strict threshold ordering above.

For example, with \(e=f=1/5\), \(k_B=k_W=1\), \(u=1/2\), and \(v=1/4\), the first regime chooses \(p_*=1/2\), \(q_*=\sqrt2-1\), and
\[
 B_*=\frac15+\frac{2\sqrt2}{5}\approx0.7656854249.
\]
Both optimal colonization rates are below one in this example, so this particular equilibrium allocation is also admissible at the parameter level of the original discrete-year model.

## Relationship to prior work

Taylor and Hall's 2011 full article establishes the two-season migratory colonization model, the product persistence threshold, and the explicit steady-state occupancies. It does not give the minimum weighted expense for two simultaneously prescribed occupancy targets, the complete three-regime allocation, or the strict transition values above. The present result starts from their equilibrium balance rather than re-claiming it.

Ross and Pollett (2009) derive conservation rules for a stochastic one-habitat-type Levins model using *mean time to extinction* as the objective and a colonization-versus-extinction intervention. Their cost problem does not imply the fixed-extinction, two-season, joint-occupancy minimum here. Santika and colleagues (2015) address dynamic spatial prioritization of different recovery actions by numerical optimization for a large koala habitat landscape; their finite-horizon spatial objective and dynamics do not cover this exact two-season equilibrium problem. The equations are also mathematically equivalent to a two-type directed susceptible-infected-susceptible mean-field model, but controlling infections rather than establishing seasonal occupancy changes the ecological objective. The broader possibility of an equivalent elementary two-state allocation result remains a historical-priority limitation.

## Limitations

This is a deterministic, homogeneous two-season occupancy model with fixed extinction rates and continuously variable colonization rates. Resource cost is linear in rates, not a fitted economic expenditure function. The model neglects habitat heterogeneity within each season, random catastrophes, interseasonal delays and individual demography. It gives neither a finite-population extinction time nor a guaranteed empirically optimal conservation policy. The original discrete-year paper restricts coefficients to probability ranges; when the calculated optimal coefficients violate those bounds, the theorem applies to the continuous-time analog only. Historical priority has not been independently validated.

## References

1. Taylor, C. M., and Hall, R. J. (first public release 2011-11-16). *Metapopulation models for seasonally migratory animals*. Biology Letters 8, 477–480. DOI: https://doi.org/10.1098/rsbl.2011.0916 . Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3367723/ .
2. Ross, J. V., and Pollett, P. K. (2009). *Rules of thumb for metapopulation management*. Proceedings of MODSIM09, 1795–1801. Author-provided readable text: https://www.researchgate.net/publication/43511313_Rules_of_thumb_for_metapopulation_management .
3. Santika, T., et al. (first public release 2015-04-16). *Assessing spatio-temporal priorities for species’ recovery in broad-scale dynamic landscapes*. Journal of Applied Ecology 52, 832–840. DOI: https://doi.org/10.1111/1365-2664.12441 .
4. Zhang, W., Lu, S., and Pei, Y. (2018). *A geometric programming approach for optimal resource allocation to control epidemic outbreaks in arbitrary networks*. Communications in Mathematical Biology and Neuroscience, article 1. DOI: https://doi.org/10.28919/cmbn/3388 .
