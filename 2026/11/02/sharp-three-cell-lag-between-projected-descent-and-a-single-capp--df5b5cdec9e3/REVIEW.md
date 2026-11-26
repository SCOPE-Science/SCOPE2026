# Independent mathematical audit

## correctness

PASS

The flow segments satisfy the inclusion and minimal tangent projection: for velocity (H/2,0,−H/2) the residual −c−v is −(H/2)1+(H/2−a)e_2, an outward normal on the upper second-coordinate face. At time 2b/H the third coordinate hits zero while the first remains below one. For the next velocity (a/2,−a/2,0) the residual is −(a/2)1−(H−a/2)e_3 and is normal on the third-coordinate lower face. Both velocities are tangent and orthogonal to their residuals. At (1,p+b,0), −c itself is normal. Monotonicity gives uniqueness across the concatenated phases. For the one-shot path a clipping level is successively −Ht/2, −b, −(at+b)/2, and 1−at−p−b, with transitions 2b/H, b/a and b/a+L. Substitution verifies each cap and the mass in its region, including the last phase. After the common first phase the difference is a pair of opposite signs times the difference of the two clipped ramps: its height is bounded by both ramp height and slope times release delay, with equality at min(b/a,2b/H+L). Each bound is strictly improved by p>0 and H finite relative to a, so the gap is less than min(b/2,1−b)<=1/3, with a sequence attaining the limit at b=2/3, a=1, p→0, H→∞. The release time ratio is H/(2a); the delay itself is b/a−2b/H. In two cells the feasible segment has metric factor two in its first coordinate, giving the identical scalar clipping of a constant-speed drift for both paths. Degenerate one- and two-cell feasible sets are singletons and cannot give a discrepancy.

## originality

PASS

Minimal selection, projected gradient flow, and the capped-simplex projector are known. The distinct supported result is the minimum cell count and quantified, sharp three-cell separation between the two specific trajectories, including the release-time ratio and the family envelope. No inspected general theorem supplies this exact comparison; the closest actual indexed statement concerns sensitivity of a single projector, not a comparison of evolutions.

## value

PASS

A single accumulated projection is a simple candidate shortcut for a projected flow under constant forcing. The minimal-size counterexample pinpoints why it fails: the secondary cap releases under flow but remains active under accumulated drift. The exact max-norm gap and unbounded release-time ratio quantify the effect in the natural first-saturation family, while two-cell equivalence shows it cannot be seen in a smaller feasible system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
