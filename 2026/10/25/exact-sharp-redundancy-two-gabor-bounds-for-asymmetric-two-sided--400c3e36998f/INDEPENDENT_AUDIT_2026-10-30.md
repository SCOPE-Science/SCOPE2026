# Independent mathematical audit

## correctness

PASS

At x∈[0,1] the Zak transform is the sum of two convergent geometric series U/(1−r/z)+Vz/(1−sz); the unitary Zak representation for modulation step 1/2 has multiplier |Zg(x,ω)|²+|Zg(x,ω+1/2)|² without extra factor. Writing u=cos(2πω), the rational function F_x(u) has strictly positive second derivative on [−1,1] because its numerator is nonnegative and nondecreasing and its denominator is the product of two positive decreasing affine terms. Therefore F_x(u)+F_x(−u) is strictly increasing with |u|, establishing frequency min at 1/4 and max at 0 modulo 1/2. The maximum spatial fiber is a strictly convex positive combination of e^(−2ax),e^(2bx),e^((b−a)x) with equal endpoint values, hence x=0 on the Zak torus. At ω=1/4, the matrix [[D,−H],[−H,E]] has determinant (1−rs)²/((1+r²)²(1+s²)²)>0; its derivative becomes bE τ²−(b−a)Hτ−aD with exactly one positive root τ=V/U, giving the unique interior minimum x_*. Fresh independent Zak multiplier checks on 5,766 space-frequency samples over six asymmetric/equal decay pairs and 49 exact rational Gram determinant identities all passed. These bounded checks corroborate, but do not replace, the continuous full-parameter proof.

## originality

PASS

A fresh closest-prior comparison finds no accessible theorem or database record implying the final all-parameter conclusion. The exact overlap/special-case antecedents are credited and remaining literature-access or terminology risks are recorded; PASS is a best-of-knowledge judgment, not external historical certification. Exact sharp redundancy-two Gabor bounds for asymmetric two-sided exponentials: For all real a,b>0, the unnormalized piecewise-exponential window e^(−at) for t≥0, e^(bt) for t<0 generates a Gabor frame on translations 1 and modulations 1/2 with explicit optimal bounds A=2(DU_*²+EV_*²−2HU_*V_*) and B=(1−rs)²[(1−r)^(−2)(1−s)^(−2)+(1+r)^(−2)(1+s)^(−2)], where the minimizing Zak fiber x_* is a unique quadratic-root expression and ω=1/4; the maximizing fiber is x=0,ω=0.

## value

PASS

Sharp two-parameter spectral frame bounds for non-even exponential windows quantify exact stability and an asymmetric drift of the worst Zak fiber. This natural frame-design question goes beyond mere frame existence and the known symmetric one-parameter results; exact extremal constants and the minimizing fiber can be reused for fixed-lattice conditioning calculations. The lattice is fixed at redundancy two and no optimality over all lattices is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
