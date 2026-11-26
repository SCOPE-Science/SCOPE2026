# Independent mathematical audit

## correctness

PASS

Increasing nonnegative functions decompose as nonnegative sums of indicators of increasing upper level sets, and the displayed E3 is trilinear. Each term in the given three-replica kernel has the stated expectation by independence; the number of ones in each coordinate of the replicas determines its probability weight. I independently generated the 20 upsets by closing under unions of principal upper sets, then cleared denominators in the odds variables t_i=p_i/(1-p_i). If Q=product_i(1+t_i) and P_A enumerates the monomials of event A, the cleared numerator is 2P_ABC Q^2 + P_A P_B P_C - Q(P_A P_BC + P_B P_AC + P_C P_AB). Separate exact polynomial convolution exhausts the 1540 unordered triples, each with 64 coordinate-degree cells; it gives 33057 positive and 65503 zero coefficients, with positive range 1 to 18. These coefficients are precisely the unnormalized Bernstein cells of the source. Nonnegative odds give nonnegativity for 0<=p_i<1; continuity or the Bernstein form covers deterministic coordinates including p_i=1. The overlapping example has event sizes 6, pairwise sizes 5 and triple size 4, yielding 1/64 at the uniform law.

## originality

PASS

Kahn states the broader event inequality as a conjecture, and Richards's earlier Theorem 1.1 claims exactly a stronger inequality but has a gap even on product cubes: its proof verifies the conditional inequality for one-coordinate elimination and then substitutes an empty retained set without a valid induction. The checked established results do not cover arbitrary increasing functions on three independent bits. Credit for the formulation belongs to the prior work; the distinct content is the valid proof of the full three-coordinate product case.

## value

PASS

The first product-cube dimension beyond the prior two-dimensional result is a natural finite case of a general conjecture. The proof covers the entire heterogeneous Bernoulli parameter space and every monotone event triple with an exact sign certificate, rather than adding a parameter sample or repeating a known inequality for cumulations. It can serve as a baseline for higher-dimensional tests or symbolic proofs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
