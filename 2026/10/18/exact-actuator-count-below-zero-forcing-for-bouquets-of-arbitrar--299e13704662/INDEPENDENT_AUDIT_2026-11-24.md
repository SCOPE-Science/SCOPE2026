# Independent mathematical audit

## correctness

PASS

Symmetric PBH applies to −L with independent coordinate columns. Each petal's first sine mode is nonzero for m_i≥3, has zero hub coordinate and opposite values at the two hub neighbors, and extends by zero to an eigenvector on the bouquet. Missing a petal therefore obstructs control irrespective of eigenvalue coincidences. For the proposed actuator set, an invisible eigenvector with zero hub value propagates zero on every petal. Otherwise the common normalized recurrence f_(j+1)=t f_j−f_(j−1) starts at (1,0) and closes at f_m=1. For |t|≥2, the absolute Chebyshev value |U_(m−2)(t/2)| is at least m−1 (also at t=±2), ruling out closure. Independently the recurrence preserves f_j²+f_(j+1)²−t f_j f_(j+1)=1, so f_m=1 forces f_(m−1)∈{0,t}, including t=0 where the options coincide. The hub equation 2(k−1)=(s−1)t contradicts |t|<2 since |s−1|≤k−1. This proves sufficiency for all lengths. For zero forcing each petal needs a nonhub seed; with exactly one each the hub and all initial neighbors of every seed are white, so no force starts. Adding the hub gives forcing chains. Symmetry gives the corresponding observability. The supplied modular certificate was inspected, not run; its full ranks are valid characteristic-zero witnesses, but its deficient ranks alone are not. The verifier explicitly checks sets of size k−1, not all sets smaller than the k+1 upper construction as VERIFICATION.md loosely suggests; the universal analytic lower bound covers size k.

## originality

PASS

The supported distinct advance is the minimum of k independent coordinate actuators and explicit placement for the fixed unit Laplacian with arbitrary, including unequal, petal lengths, and hence the exact gap from zero forcing. Credit Z=k+1 on the whole bouquet family to prior work, not just the triangle subclass; that component is a known comparator, not the originality basis. No inspected exact result or stronger theorem covers the arbitrary-length actuator count. The strongest exact actuator match covers equal-length petals only and is later-dated.

## value

PASS

The exact actuator optimum and a uniform placement for a natural fixed-Laplacian family give a useful, sharp gap between dedicated-input control and a structural zero-forcing certificate. Removing equal-length or arithmetic restrictions is meaningful because the necessary local obstructions and global hub equation must hold even with coincident or incommensurate petal spectra. It tells a researcher precisely when a hub actuator is avoidable in this family. The already-known forcing count is useful as the comparator but adds no independent value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
