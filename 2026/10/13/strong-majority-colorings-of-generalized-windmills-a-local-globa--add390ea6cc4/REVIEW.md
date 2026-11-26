# Independent mathematical audit

## correctness

PASS

Let α be the center color. A vertex with color γ in a blade where β occurs a_β times sees a_β+1_{β=α}−1_{β=γ} neighbors of color β. For m=2 either blade vertex fails if its mate has center color, otherwise both pass regardless of whether their own colors agree; the center then imposes the sole global per-color cap n. For m≥3 a monochromatic blade fails (m−1>floor(m/2)). Therefore each β has a witness γ≠β in each blade, giving exactly the stated individual caps h−1 and h. Conversely those caps suffice there and imply the center cap since nh≤floor(nm/2). For a fixed center label the multinomial count gives the restricted sum for m=2 or m![x^m]E_{h−1}E_h^{q−1} per labeled blade for m≥3; only the latter factors by blade. Multiplication by q, then inclusion-exclusion over unused labels, gives A_q and S_q, including the empty-sum and A_0 conventions. At most two colors fail by the total occupancy caps in either case. For m=3 four colors are needed and suffice with each blade a permutation of three other colors; for m=2 two non-center colors can each occur n times; for m≥4 the blade profile (1,h,m−1−h) proves three suffice. At the minimum the maps are surjective, giving the two balanced non-center counts at m=2, permutations at m=3, 6+24 one-blade maps for m=4 and 30 for m=5 with fixed center label. Splitting a nontrivial color class preserves the cap and reaches every larger used-color count. Fresh direct enumeration of neighborhood caps for (n,m)=(2,2),(3,2),(2,3) with q=2,3,4 and (2,4),(2,5) with q=2,3 matched the claimed count, including 18, 60, 144, 2700 and 2700 at the respective minima. These are finite checks, not the universal proof. Replay: RESULT.md lines 45–80; the separate artifacts/verify.py and logged finite replay in VERIFICATION.md were inspected, not run.

## originality

PASS

Pass for the exact structural and counting statement on n≥2 clique windmills. The complete-graph minimum and the ordinary palette-splitting and inclusion-exclusion tools are prior or routine; the distinct content is precisely when the center couples blades, when the local caps suffice, and the resulting all-palette evaluation. The closest windmill treatments compared impose inequivalent vertex or edge constraints.

## value

PASS

This treats a natural vertex-cut family for a recently defined coloring invariant. The exact change from a coupled global constraint for two-vertex blades to independent local constraints for larger blades explains the exceptional optimal palette and supplies labeled palette counts, which the scalar minimum cannot recover. The content is the structural dichotomy and evaluation, not the routine final use of inclusion-exclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
