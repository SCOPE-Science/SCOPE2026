# A sharp three-survey identifiability law for directed metapopulation dispersal

## Finding

For the normalized directed-dispersal Levins model of habitat occupancy, the unknown colonization scale and **both** independent patch-preference weights are globally identifiable from exact positive equilibrium observations if and only if the observed habitat-cover/occupancy pairs contain three noncollinear points. This gives a universal minimal three-survey protocol: measure positive equilibrium occupancy at \((h_1,e_1)\), \((h_2,e_1)\), and \((h_1,e_2)\), with \(h_1\ne h_2\) and \(e_1\ne e_2\). Whenever all three configurations sustain positive equilibrium occupancy, this protocol identifies the three unknown parameters exactly, with design determinant

\[
\det A=(h_2-h_1)\bigl[p^*(h_1,e_2)-p^*(h_1,e_1)\bigr]\ne0.
\]

Neither any two positive equilibrium surveys, nor arbitrarily many surveys changing only habitat cover at one fixed disturbance rate, nor arbitrarily many surveys changing only disturbance at one fixed habitat cover, can identify all three unknown parameters. The result concerns structural identification from exact equilibria, not finite-sample statistical estimation.

## Assumptions and scope

A homogeneous metapopulation occupies fraction \(p(t)\in[0,h]\) of the total landscape; fraction \(h\in(0,1]\) is suitable habitat. Propagules are directed toward three patch types, with normalized weights \(\phi>0\) for unsuitable patches, \(\gamma>0\) for occupied suitable patches, and \(1\) for empty suitable patches. The colonization/establishment scale is \(c>0\) and the independently known local extinction or disturbance rate is \(e>0\). The dynamics are

\[
\dot p=p\left(\frac{c(h-p)}{\phi(1-h)+\gamma p+(h-p)}-e\right).
\]

The parameter triple \((c,\phi,\gamma)\) is constant across the surveyed environments, while the chosen habitat fraction \(h\) and disturbance rate \(e\) may vary. Each survey reports exact equilibrium occupancy \(p^*(h,e)\), known to be strictly between zero and \(h\). The viability requirement is

\[
 c h>e\bigl[h+\phi(1-h)\bigr],
\]

and on this domain the unique positive equilibrium is

\[
 p^*(h,e)=\frac{ch-e\bigl[h+\phi(1-h)\bigr]}{c+e(\gamma-1)}.
\]

For a finite collection of such positive surveys, identification means uniqueness among all strictly positive triples \((c,\phi,\gamma)\) consistent with every survey. A nonidentifiable fiber is a continuous family of *strictly positive* parameter triples, not a formal algebraic solution outside the biological parameter domain.

## Proof

**1. The equilibrium law has exactly one relevant branch.** Set \(W(p)=\phi(1-h)+h+(\gamma-1)p\). For \(0\le p\le h\), \(W(p)>0\). The per-capita colonization contribution is strictly decreasing because

\[
\frac{d}{dp}\left(\frac{h-p}{W(p)}\right)=-\frac{\phi(1-h)+\gamma h}{W(p)^2}<0.
\]

Its value at \(p=0\) exceeds \(e/c\) precisely under the viability inequality, and its value at \(p=h\) is zero. Thus there is exactly one positive equilibrium, attracting all states in \((0,h]\). Solving its balance equation gives the stated formula. The viability inequality implies \(e<c\), hence \(c+e(\gamma-1)>c-e>0\). Moreover,

\[
\frac{\partial p^*(h,e)}{\partial e}
=-\frac{c[\phi(1-h)+\gamma h]}{[c+e(\gamma-1)]^2}<0
\]

throughout the positive-equilibrium domain. For fixed \(e\), the displayed equilibrium formula is affine in \(h\) over every interval where occupancy is positive.

**2. A data-driven linear identity is exact.** For an observation \((h_i,e_i,p_i)\) with \(p_i=p^*(h_i,e_i)>0\), define \(U_i=(h_i-p_i)/e_i\). Balance at positive equilibrium is equivalent to

\[
U_i=a(1-h_i)+b(h_i-p_i)+d p_i
   =a+\beta h_i+\delta p_i,
\]

where \(a=\phi/c>0\), \(b=1/c>0\), \(d=\gamma/c>0\), \(\beta=b-a\), and \(\delta=d-b\). The transformation \((c,\phi,\gamma)\leftrightarrow(a,\beta,\delta)\) is one-to-one over the positive model domain: put \(b=a+\beta\), \(d=b+\delta\), then \(c=1/b\), \(\phi=a/b\), \(\gamma=d/b\).

Consequently all observations constrain the three coefficients of one affine plane in the variables \((h,p)\). The associated design rows are \((1,h_i,p_i)\). They span three dimensions if and only if the observed \((h_i,p_i)\) are not all on one line. In that case the affine coefficients and hence \((c,\phi,\gamma)\) are uniquely recovered. If the rows have rank below three, every nonzero vector in their kernel produces an open interval of alternate coefficient triples around the true triple. For sufficiently small perturbations, \(a,b,d\) remain positive, and every observed \(p_i\) remains the unique positive equilibrium by Step 1. Thus rank failure is genuine biological nonidentifiability. In particular, at most two observations never suffice.

**3. The three-survey L-design has a universal nonzero determinant.** Label the surveys \((h_1,e_1,p_1)\), \((h_2,e_1,p_2)\), \((h_1,e_2,p_3)\). Subtract the first design row from the other two, giving \((0,h_2-h_1,p_2-p_1)\) and \((0,0,p_3-p_1)\). The determinant is exactly \((h_2-h_1)(p_3-p_1)\). Since occupancy is strictly decreasing in \(e\), the second factor cannot vanish when \(e_1\ne e_2\). Conversely, surveys with fixed \(h\) all have the same first two design coordinates, and surveys with fixed \(e\) lie on the graph of the affine function \(p^*(h,e)\). Each one-axis protocol has design rank at most two, however many positive surveys it contains.

**4. Explicit inversion.** For the L-design, calculate \(U_i=(h_i-p_i)/e_i\) and then

\[
\delta=\frac{U_3-U_1}{p_3-p_1},\qquad
\beta=\frac{U_2-U_1-\delta(p_2-p_1)}{h_2-h_1},\qquad
a=U_1-\beta h_1-\delta p_1.
\]

Recover \(b=a+\beta\), \(d=b+\delta\), and finally \((c,\phi,\gamma)=(1/b,a/b,d/b)\). The denominators are nonzero by Step 3; consistency with the stated positive model guarantees \(a,b,d>0\).

**5. Rational witness and sharp obstruction.** The triple \((c,\phi,\gamma)=(2,1/2,3/2)\) under environments \((h,e)=(3/4,1/4),(1/2,1/4),(3/4,1/2)\) gives occupancies

\[
(p_1,p_2,p_3)=(41/68,13/34,17/36),\qquad\det A=5/153,
\]

and the inverse formulas recover exactly \((2,1/2,3/2)\). By contrast, at the single fixed disturbance \(e=1/4\), two distinct triples \((2,1/2,3/2)\) and \((15/4,1,3)\) yield the *same whole positive habitat-response curve* \(p^*(h,1/4)=(15h-1)/17\) wherever \(h>1/15\). Changing disturbance distinguishes them. This illustrates why additional same-axis observations cannot replace the second perturbation.

## Verification

The standalone Python 3 script `checker.py` uses only the standard library `fractions`, `itertools`, and `random`. It checks the exact equilibrium balance, positivity, all three inverse parameters, the determinant identity, strict disturbance response, and fixed-disturbance nonidentifiability for an exact rational witness. It also exhausts 2,500 positive rational L-design parameter/environment choices across the explicit checker grids. These finite checks support and reproduce the calculations; the all-parameter statements rely on the preceding analytical proof, not on finite enumeration.

Run using `python checker.py` from the directory containing the extracted file. The checker does not download data or require network access.

## Relationship to prior work

Purves and Dushoff (2005) introduced the normalized directed-dispersal patch-preference model, solved its equilibrium occupancy law, and discussed habitat-cover and disturbance-response curves. Those model equations and qualitative response properties are prior work, not claimed here. The distinct question addressed here is **simultaneous global recovery** of the unknown colonization scale and both unknown preference weights: a complete rank criterion, an always-identifying feasible three-environment design, an explicit inverse, and impossibility for any one-axis design. The source paper's main text fits a restricted preference specification and explicitly notes families of models consistent with an individual baseline observation; its accessible main-text model and fitting sections do not state this complete identification theorem.

Harding and McNamara (2002) gave a broader metapopulation dynamics framework, but only their abstract could be examined for this comparison. Lele, Moreno, and Bayne (2012) address **occupancy versus detection error** and identifiability from survey protocols, whereas this theorem assumes exact occupancy and asks about three biological mechanism parameters. A source with a more general identification theorem could imply the present statement without matching its wording; no such covering result was established in the accessible comparisons. Historical priority is therefore provisional.

## Limitations

This is an exact deterministic structural-identification theorem. It assumes known disturbance rates, exactly measured positive equilibrium occupancies, three genuine positive-equilibrium regimes, a common colonization scale and common positive preference weights across environments, perfect detection, and the specific globally mixed normalized Levins mechanism. It does not address transient-only data, imperfect detection, observation error, statistical confidence intervals, field feasibility, or optimal noisy experimental design. A zero-occupancy observation cannot be substituted into the positive-equilibrium inversion. A very small nonzero determinant can still lead to severe numerical conditioning. An inaccessible older technical appendix and more general metapopulation literature leave historical-priority uncertainty.

## References

1. Purves, D. W., and Dushoff, J. (2005). *Directed seed dispersal and metapopulation response to habitat loss and disturbance: application to Eichhornia paniculata.* Journal of Ecology 93, 658–669. First published 19 April 2005. https://doi.org/10.1111/j.1365-2745.2005.00988.x
2. Harding, K. C., and McNamara, J. M. (2002). *A unifying framework for metapopulation dynamics.* American Naturalist 160, 173–185. https://doi.org/10.1086/341014
3. Lele, S. R., Moreno, M., and Bayne, E. (2012). *Dealing with detection error in site occupancy surveys: what can we do with a single survey?* Journal of Plant Ecology 5, 22–31. https://doi.org/10.1093/jpe/rtr042
4. Royle, J. A. (2006). *Site occupancy models with heterogeneous detection probabilities.* Biometrics 62, 97–102. https://doi.org/10.1111/j.1541-0420.2005.00439.x
