# Independent mathematical audit

## correctness

PASS

Away from dyadics, reflect every odd iterate to fold the phased restrictions to E=(h,1) for F(x)=(-2x) mod 1. This preserves the initial coordinate, changes finite measures on no positive-measure set, and loses no infinite survivors: every original dyadic orbit hits 0 at an even time, and every dyadic orbit of the folded map with this mod-1 convention hits 0. The upper inverse branch g(t)=1-t/2 maps all of E back to E for h≤1/2. The lower inverse branch b(t)=(1-t)/2 returns to E precisely on I=(h,1-2h) when h<1/3 and nowhere otherwise. In the two-branch regime b(I)⊆I and g(E) is disjoint from I. If m_n is the measure surviving n observations and i_n the part in I, then m_{n+1}=(m_n+i_n)/2 and i_{n+1}=i_n/2, with m_1=1-h and i_1=1-3h. This yields the linear factor. The 2×2 recurrence and its square have a genuine Jordan block; equivalently the frozen pair map’s open transfer operator on functions constant on each of L_h,R_h has matrix [[1,2],[0,1]]/4. For 1/3≤h≤1/2 only g survives and each step halves length. For 1/2<h<2/3, g is admissible exactly on (h,2-2h) and maps this interval into itself, giving length (2-3h)/2 after two observations and a factor 1/2 for each later one. For h≥2/3 strict exclusions leave no admissible point for the second observation. In the low regime, an infinite survivor visiting the lower branch must thereafter stay in I (the image of I has upper endpoint 1-2h), which by contraction of b forces the fixed point 1/3 upon entry. Its only surviving upper prehistories are g^m(1/3)=2/3+(-1)^(m+1)/(3·2^m); the forever-upper orbit is the fixed point 2/3. This latter point is the unique survivor from h=1/3 through h<2/3. The formula is continuous at 1/3, 1/2 and 2/3, and its nonzero asymptotic rates are log 2. Two minor proof-text corrections do not change the finding: x=1/2 passes the first pair when h<1/2 (but never survives infinitely), and the Step 2 power describes the intersection over all intermediate pair constraints, not merely the intersection of initial and kth pair constraints.

## originality

PASS

The supported distinct contribution is the exact finite-time and endpoint-sensitive infinite-time phase diagram for the entire h range. The alternating protocol is a boundary-touching special case of a preexisting oscillating-hole model; the model itself is not new. Folding to a negative doubling map reveals a close negative-map literature, but the inspected primary results concern interior holes crossing the discontinuity, not this stationary endpoint-hole problem. Neither comparison supplies the statement or a direct evaluation of its measures and survivor sets.

## value

PASS

This is an exactly solvable boundary protocol within a motivated moving-hole family. It separates two effects that an escape exponent alone misses: disappearance of a countable family of survivors and loss of a positive linear-in-time factor while the exponential rate remains constant. The sharp complete h and n diagram provides a benchmark for transfer-operator and numerical escape-rate analyses and specifies open/closed boundary effects on survival.

The dated certificate retains the supplied scientific assessment, sources and limitations.
