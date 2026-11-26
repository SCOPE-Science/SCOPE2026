# Independent mathematical audit

## correctness

PASS

With gauge spins r_i=(-1)^i s_i, the model is antiferromagnetic in a uniform field. A physical antiparallel exchange flips two equal gauge spins b, changing energy by −2Jb(a+d)+4hb, where a,d are the exterior gauge spins. For 0<h<J the sign is constant and nonzero for each local pattern. Two alternating weighted transitions count physical up-spins once each; closed walks based at the fixed even site are in bijection with labeled ring configurations for 2m≥4. An independent gauge construction and exact trace Newton identities recover det(I−tT)=1−(1+z²)t−(z+z²+z³)t²−z⁵t⁵. The negative logarithmic derivative gives the trace series, and subtracting the formal m=1 term gives the physical series. At z=1 the positive root is simple because 2/r+3/r²+1/r⁵ strictly decreases through 1; comparison of root moduli and equality of the phases of powers 3 and 4 make it strictly dominant. At h=0, a spin singleton admits a nonincreasing exchange, and with no singletons every antiparallel exchange increases energy. In the no-singleton two-spin transfer matrix the even/odd sectors under spin inversion have polynomials x²−x−1 and x²−x+1. Thus the golden mean is the baseline and the jump is strict because the positive two-step root exceeds 3. Independent bounded replay: /workspace/branches/independent_replay.py, kawasaki(), exact determinant and full Hamiltonian counts for N=4,6,8,10 at two weak fields and zero including neutral moves; no extrapolation from finite lengths.

## originality

PASS

Accept the weak alternating on-site-field census and its comparison to a known zero-field baseline, not the zero-field golden-mean result or the transfer-matrix method as new. The inspected nearest results use a different field/coupling, neutral-move constraint, or move rule.

## value

PASS

The alternating bias selects which former neutral moves survive while leaving the signs of nonneutral ferromagnetic moves unchanged. The count shows that arbitrarily weak bias changes the exponential number of absorbing states, and its complete magnetization weighting matters because exchanges conserve magnetization. This is a benchmark for sector-resolved arrest, not a claim about the probabilities of the different absorbing states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
