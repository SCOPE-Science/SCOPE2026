# Independent mathematical audit

## correctness

PASS

Independently reconstructed the full symbolic transfer and variance argument. For the seven intervals in RESULT.md, the lengths in order are 2(beta-2), 6-2beta, beta-2, beta-2, 6-2beta, beta-2, beta-2, all strictly positive. With equal fifth and sixth source values, the positive-branch inverse falls in source 7 on target 1, sources 5–6 on targets 2–5, and source 4 on targets 6–7, with weight 1/2; the negative branch adds source values 1,1,2,3 on targets 3–6. This gives the claimed transfer chart and, after substituting rho and w, invariance and w-Lw=rho h. Integration gives stationary mass 1 and positive-branch mass 2/3. Integrating the Poisson identity gives mean-zero h; the stated w integrates to zero, and its integral over the positive side is [(beta-2)(30-6beta)+(4-beta)(18-6beta)]/81=4/27. Thus the h-w pairing is 4/27. With g=w/rho, the normalized transfer P satisfies (I-P)g=h and P(f composed with T)=f. The centered m=g-(Pg) composed with T is killed by P, so its time translates are pairwise orthogonal. Their sum differs from the centered occupation sum by a bounded telescoping term. Its own variance contributes O(1/n) after normalization and its cross term is O(n^-1/2). The limiting variance is ||g||^2-||Pg||^2=2(4/27)-2/9=2/27. The joint-positive interval (0,beta/2) has mass (beta+4)/18, giving covariance (beta-4)/18, and the derivative observable multiplies H by log 2 almost everywhere. This proves the result for the stated stationary density and open interval without an ergodicity, mixing-rate, or CLT assumption. The frozen checker tests the symbolic chart given the chart's entries; positivity of the lengths and the chart itself are justified here for all parameters, not by sampling.

## originality

PASS

The invariant law, map and mean plateau are definitively antecedent. The supported distinction is the evaluated second-order variance over the entire interval together with the varying one-lag covariance; the closest accessible primary claims and inspected local indexed results do not establish it.

## value

PASS

This is a second-order analogue of a well-motivated known mean plateau, not just another calculation of the stationary density. The exact constant controls stationary finite-time derivative variability while the changing one-lag term establishes that individual temporal dependencies need not share the plateau. The bounded explicit transfer solution is reusable in this family and establishes the full interval without statistical extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
