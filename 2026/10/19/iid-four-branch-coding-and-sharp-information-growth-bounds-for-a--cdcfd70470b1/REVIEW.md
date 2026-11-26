# Independent mathematical audit

## correctness

PASS

The weights are positive, k_1+k_2=1/2 and k_1 b_1+k_2 b_2=1, so the affine switching probabilities sum to one at every y. Both branch slopes have positive endpoint values b_i and 4-b_i and the maps take the half interval onto the whole interval. Integrating k_i times the branch derivative over an inverse image gives k_i times the target measure. Inductively, conditional on any past label block, the current state is uniform and the next label and next state have the same product law, proving IID and stationarity. The four weights are k_1,k_2 each repeated twice, and equality is equivalent to b_1+b_2=4. Given the initial coordinate and previous labels the present coordinate and its half are known, so only the fresh Bernoulli map choice contributes conditional entropy. Stationarity and the discrete entropy chain rule give n times the stationary mean choice entropy, with no differential-entropy subtraction. Expanding the log of k_i r_i leaves the derivative integral Lambda and the linear block identity. For amplitude a=|b-2| the sign-symmetric derivative distribution is 2+aU for U uniform on [-1,1]. Pairing U=v and U=-v in the derivative of the mean of r log r gives a strictly positive multiple of v log((2+a v)/(2-a v)) for 0<a<2 and v>0. Endpoints of the mean integral are log 2 at a=0 and (1/8) times the integral of r log r from 0 to 4, namely log 4-1/2, at a=2. Continuity uses the continuous extension of r log r at zero; the two symmetric parameter paths give both sharp limits. The attached code checks normalization and quadratures; it was inspected, not executed.

## originality

PASS

The random-map family, the affine switching law and uniform invariance are prior. The stationary four-symbol IID law follows directly from a Jacobian rewrite of the source and is not by itself enough for the pass. The distinct part supported by the checked evidence is the exact initial-coordinate information law with its sharp strict global rate interval for the full nonlinear two-parameter family.

## value

PASS

For a canonical explicit nonlinear example, the observable label combines location and actual random choice, but its total symbol entropy is not its information about the initial coordinate. The all-horizon identity gives that information exactly, and the sharp uniform bounds quantify how much the rate can exceed the spatial-bit baseline while separating the effect from uniform invariance. The value rests on this quantitative profile, not on rechecking the known invariant density or merely labeling four branches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
