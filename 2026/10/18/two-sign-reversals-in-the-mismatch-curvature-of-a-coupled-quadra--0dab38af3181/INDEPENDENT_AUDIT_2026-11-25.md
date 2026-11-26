# Independent mathematical audit

## correctness

PASS

Independent reduction of the prime swapping orbit: in midpoint/difference coordinates use the cycle labels (m±p,q±r) and parameter e=p/r. The difference equations give m=1/2+b/(1−e²), q=−be/(1−e²). Put s=r² and s0=(b+1)/2. The mean one-step determinant divided by 4 is m²−bm−q²+(e²−1)s; the half-difference divided by 4 is r[(2m−b)e−2q]. At e=0 these are −1/4 and 0. Imposing their squared difference equal to 1/16 gives s=s0+[b+s0+2s0(3b+1)²]e²+O(e⁴). Inserting this in a=m+m²+e²s+q²+s and δ=(1−2(b−m))q+2es gives coefficient (b+1)(3b+1)(3b+2) in e² and δ=(1−b)e+O(e³). This verifies the curvature, signs, and both zero couplings. The base trace is 4b²−2 and determinant 1, so the second iterate lacks multiplier +1 for fixed −1<b<0; the analytic cycle continuation remains prime. Along δ=0 the determinant slope is 8, giving the analytic threshold and the claimed attracting-to-repelling spectral crossing. The exchange symmetry gives the even remainder. The check does not assume a nonresonant normal form or assert uniformity near the endpoints. VERIFICATION.md and verify_curvature.py were inspected, not executed; the recorded finite checks are supplementary to the analytical reconstruction.

## originality

PASS

The equal-drive orbit and intercept are known. The supported distinction is the exact unequal-drive curvature and its two zeros for this coupling convention, not use of the determinant criterion or a general bifurcation theorem. The strongest inspected same-model references stop at equal drive, and the closest distinct indexed two-cycle claim concerns a different map and different spectral property.

## value

PASS

In a studied two-cycle problem where the effect of mismatched drive was explicitly posed, the exact signed curvature determines whether heterogeneity advances or delays the spectral loss of stability. The two reversals are not consequences of symmetry alone; the result is useful without asserting invariant circles or a global diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
