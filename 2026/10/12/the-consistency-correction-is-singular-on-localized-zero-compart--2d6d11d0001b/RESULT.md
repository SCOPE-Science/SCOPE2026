# The consistency correction is singular on localized zero compartments
## Finding
Consider the consistency-corrected two-dimensional nonstandard finite-difference scheme of Zinihi, Ehrhardt and Sidi Ammi. For each compartment \(U\), Eq. (25) defines
\[
\nu(U^n_{j,\ell})=-\frac{U^n_{j,\ell}-U^{n-1}_{j,\ell}}{kU^n_{j,\ell}},\qquad n\ge 1,
\]
with the separate convention \(\nu(U^0_{j,\ell})=0\). Consequently the printed recurrence is not defined at a node with \(U^{n-1}_{j,\ell}=U^n_{j,\ell}=0\).

The paper's two-dimensional experiment initializes every noncentral cell as entirely susceptible, while the central source contains susceptible, exposed and infected populations. Thus \(Q^0=R^0=0\) everywhere, and \(E^0=I^0=0\) away from the central source. Eq. (26) has a nearest-neighbor stencil evaluated at the old time level. After one step, any node more than one lattice edge from the initial exposed/infected source still satisfies
\[
E^1=I^1=Q^1=R^1=0.
\]
At such a node, the coefficient required before the next step is \(\nu=0/0\). Therefore Eqs. (25)–(26), together with the stated localized initialization, do not by themselves define the long-time two-dimensional trajectory reported in the numerical section. A further zero-state rule, regularization, or strictly positive seed is mathematically necessary.

## Assumptions and scope
The statement is about the printed two-dimensional recurrence (25)–(26), its stated nearest-neighbor stencil, and the localized initialization in Section 5.2. It assumes only nonnegative parameters, positive time and space steps, and that the initial exposed/infected source is localized so that the grid contains at least one node more than one lattice edge from it, as described in the article's numerical setup.

No assertion is made that the plotted trajectories are numerically false. An implementation may have inserted a positive floor, replaced the ratio at zero, or used different initial data. The point is that none of those choices is specified by the printed scheme, and different zero-state extensions are not forced by Eq. (25).

## Proof
At \(n=0\), the article sets \(\nu(U^0)=0\), so the first update is defined. Let \(C\) denote the set of grid nodes where \(E^0\) or \(I^0\) is nonzero. Take a node \(z\) whose lattice distance from \(C\) exceeds one.

For the exposed update, the numerator in Eq. (26) uses \(E^0(z)\), the four nearest-neighbor values of \(E^0\), and the local product \(E^0(z)S^1(z)\). All are zero at \(z\), hence \(E^1(z)=0\). For the infected update, the old infected value, its four old-time neighbors, and the local incidence term all vanish, while the progression term is proportional to \(E^1(z)=0\). Hence \(I^1(z)=0\).

The paper initializes \(Q^0=R^0=0\) throughout the grid. The quarantined update at \(z\) therefore has zero old value, zero old-time neighboring values, and source \(\gamma I^1(z)=0\), giving \(Q^1(z)=0\). The recovered update similarly has zero old value and neighbors and source \(\alpha Q^1(z)=0\), giving \(R^1(z)=0\).

Before the \(n=1\) to \(n=2\) update, Eq. (25) asks, for example,
\[
\nu(Q^1(z))=-\frac{Q^1(z)-Q^0(z)}{kQ^1(z)}=-\frac00,
\]
and the same obstruction occurs for \(E\), \(I\), and \(R\) at that node. Thus the printed recurrence is undefined there.

There is no canonical continuous extension hidden in the algebra. When \(U^n\ne0\), Eq. (25) gives \(1+k\nu=U^{n-1}/U^n\). Approaching \((U^{n-1},U^n)=(0,0)\) along \(U^{n-1}=U^n\) gives limit \(1\), whereas approaching along \(U^{n-1}=2U^n\) gives limit \(2\). Therefore the missing value is not determined by continuity.

## Verification
The accompanying `verify.py` checks the algebraic nonuniqueness of the zero-state extension and performs one published-form nearest-neighbor update on a finite grid with a localized exposed/infected source and zero quarantined/recovered states. It verifies that remote nodes remain exactly zero after the first update and that the next evaluation of Eq. (25) is undefined there.

The calculation uses only the recurrence structure; the numerical parameter values are chosen positive and do not affect the support argument.

## Relationship to prior work
The motivating article explicitly identifies a consistency problem in its first nonstandard Laplacian and introduces Eqs. (25)–(26) as a correction, then states that this corrected approach is used for the numerical experiments. The zero-state singularity identified here is different from the truncation-error issue already discussed by the authors: it concerns whether the corrected recurrence is a defined map on biologically natural nonnegative data with empty compartments.

General NSFD literature emphasizes positivity and dynamic consistency, including work by Mickens on denominator functions and by Anguelov, Dumont, Lubuma and Shillor on dynamically consistent epidemiological schemes. Those sources motivate preserving the nonnegative state space, but the inspected material does not state this source-specific successive-value ratio correction or resolve its \(0/0\) value on localized zero compartments.

## Limitations
The full implementation used to create the article's figures was not available in the inspected public materials. It may contain an undocumented zero-state convention. Accordingly, the finding is a specification and reproducibility result about the printed recurrence, not a claim that the figures were necessarily generated incorrectly.

The argument concerns the corrected scheme (26) and the localized nonnegative initialization. It does not challenge the continuous SEIQR model's well-posedness, the reproduction-number calculation, or NSFD methods that use denominator functions without division by the current state.

## References
1. A. Zinihi, M. Ehrhardt, M. R. Sidi Ammi, "A nonstandard finite difference scheme for an SEIQR epidemiological PDE model," *Applied Mathematics and Computation* 520 (2026), 129953. DOI: 10.1016/j.amc.2026.129953. See Eqs. (25)–(26) and Section 5.2.
2. R. E. Mickens, "Calculation of denominator functions for nonstandard finite difference schemes for differential equations satisfying a positivity condition," *Numerical Methods for Partial Differential Equations* 23 (2007), 672–691. DOI: 10.1002/num.20198.
3. R. Anguelov, Y. Dumont, J. M.-S. Lubuma, M. Shillor, "Dynamically consistent nonstandard finite difference schemes for epidemiological models," *Journal of Computational and Applied Mathematics* 255 (2014), 161–182. DOI: 10.1016/j.cam.2013.04.042.
