# Independent mathematical audit

## correctness

PASS

For s=x+y and f=x/s one has s'=fr+(1−f)g(s), g(s)=s exp(r−s). After the first step x≤r and y≤exp(r−1). If s≤r/2 then s'>s; on the rest of that bounded interval both terms in the convex combination have positive minima, giving a positive lower bound for all subsequent masses. For Q=x/y^(1/r), direct substitution gives Δlog Q=s/r−1−log(s/r)≥0 with equality only at s=r. When Q has a finite positive limit, its log increments tend to zero, so s tends to r and the strictly increasing map x↦x/(s−x)^(1/r) gives convergence to a unique interior composition. If Q tends to infinity, bounded x forces y→0; the positive mass lower bound and the x update then force x→r, which is enough for the stated conclusion with y∞≥0. The continuous extension at (r,0) fixes it. A convergent orbit can recur to its initial point only if that point is fixed. Integration of the nonnegative log increment under a compactly supported invariant law gives zero and forces support on the fixed line. At an interior fixed point the normal multiplier in s−r is (1−f)(1−r). For nonlanding starts the mass-deviation quotient is defined at every step and tends to this multiplier; eventual growth when its absolute value exceeds one contradicts convergence. For sharpness, pick any f* strictly above the barrier and below 1. In a small strip about (r,f*) the exact mass factor is bounded in modulus by k<1 and log Q has quadratic drift at most C(s−r)^2. Starting at s=r+ε gives geometric mass contraction and total drift O(ε²)/(1−k²) through the first candidate exit. The smooth inverse from (s,log Q) is unique since log Q=(1−1/r)log s+log f−(1/r)log(1−f) is strictly increasing in f. It gives |f−f*|=O(|ε|+ε²/(1−k²)), a strict interior bound for small enough ε, closing the induction. The strip excludes all roots of g(s)=r except r, so ε≠0 cannot land; the limiting composition tends to f* as ε→0. Taking f* down to the barrier proves the infimum. Finally for r>2, unimodality and g(1)>r show that g(s)=r has roots u_r∈(0,1) and r only. At (fu_r,(1−f)u_r) the image is exactly (rf,r(1−f)). The endpoint (r,0) is not the image of a strictly positive state.

## originality

PASS

The supported distinct claim is the global pointwise equality-parameter classification combined with the sharp nonlanding composition infimum for r>2. The weighted monomial identity and model themselves are already in Kang–Smith, as the frozen record acknowledges. The elementary one-step preimage is part of the correct explanation of the exception, but priority for that fact by itself is not certified: the most relevant preimage paper could not be checked in full. The inspected closest catalogue statements change the map, and those changes affect the dynamics central to the theorem.

## value

PASS

The equality locus separates the commonly analyzed exclusion and persistence regimes, making it a natural boundary rather than an arbitrary parameter slice. An all-start convergence result on a neutral continuum together with a sharp accessible-composition infimum and explicit finite-time exceptions describes which repelling equilibria can be selected and why. It is stronger than a local multiplier computation or the prior weighted identity by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
