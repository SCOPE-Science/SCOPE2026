# Independent mathematical audit

## correctness

PASS

The disjoint pair difference vectors are orthogonal left-zero-sum eigenvectors of the unmodified biclique Laplacian with eigenvalue n; adding the matching changes just those eigenvalues to n+2. For an unmatched cross-edge source the added edges carry no current; the plain biclique cut sum is q0 and its diagonal is (m+n-1)/(mn), giving p0. A matched cross-edge source from a to w has a component on just its own pair difference, so the potential at a goes down by delta=1/[n(n+2)], its mate b goes up by delta, and other potentials are unchanged. Relative to the plain biclique the new internal edge contributes n*delta, and the cross currents change the absolute sum by -(2n-2)*delta before any sign flip. Only the b-to-other-right currents can flip, from -1/(mn) to delta-1/(mn), adding 2(n-1) max(0,delta-1/(mn)). This gives precisely d_Q and its continuity at m=n+2; the diagonal falls by delta, yielding d_P=d_Q+2*delta. A matching-edge source is supported on its pair and gives q_M=2(n+1)/(n+2), p_M=3n/(n+2). Both paired cross sums are nondecreasing in m (baseline plus nondecreasing hinge correction); their excesses over the matching-edge sums at m=4 are (n-1)/(2n) and 2(n-1)/[n(n+2)], both positive, excluding internal edges from either maximum. Thus the unmatched baseline column is available until saturation and absent after, with all cross column values unchanged as other pairs are added. Saturation changes the norms by min(0,d_Q), min(0,d_P); their critical sign boundaries for even m and n>=5 give the three claimed regimes. The even/odd and n=2 cases are included in the general norm formula. Verified 114 exact orbit columns across branch and saturation boundaries by grounded graph-Laplacian solves; replay: python3 /workspace/branches/frozen_math_recheck.py 3. The frozen checker was read, not run.

## originality

PASS

The exact single internal edge case is directly covered by indexed record 06f1b4795168 and is not original. The supported distinct result is the simultaneous invariance for any number of further disjoint pairs before saturation, with the sharp terminal saturation thresholds and strict drops. The existing electrical literature plausibly includes the same graph family but the inaccessible papers do not establish overlap with this norm result on current evidence.

## value

PASS

This complete classification isolates a concrete failure of edge-addition monotonicity for two complementary canonical projections, on a natural perturbation by disjoint edges rather than one example. The plateau and the terminal drop are explained by the survival and eventual disappearance of a source-edge orbit, with separate exact parameter thresholds for the two projections. These findings extend materially beyond the known first-insertion formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
