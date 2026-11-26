# Independent mathematical audit

## correctness

PASS

The involution swapping partners splits the mean-zero Laplacian into eigenvalues N and b=N-2+2x^2. For a matched source the voltages are ±x/b on its endpoints, giving cut diagonal 2x^2/b and 2(N-2) off-diagonal contributions x/b. For an unmatched source the four voltages are ±(1/N+1/b)/2 and ±(1/N-1/b)/2, with the latter coefficient changing sign only at x=1. Counting the matching edges, links among these four vertices, and links to the other vertices gives the two cut branches. Each cycle sum equals the cut sum plus 1 minus twice the cut diagonal. The differences are negative below 1 and for x>=1 factor into x-1 times a decreasing linear factor for each projector; comparing their roots gives exactly the separate P and Q transitions and boundary ties. Differentiation gives the matching-branch maxima R_N at x=R_N and x=R_N-1 respectively. The nonmatching cut branches remain below R_8. With s=N-2 the two nonmatching cycle maxima are 1+(s-2+sqrt((s-2)^2+s/2))/s and 3-6/N+1/[2(1+sqrt(N/2))]. Direct comparison at N=8,10,12, and the strict bounds <3 on 14<=N<=18 and <7/2 on N>=20 establish all global optima, including only x=3 for the N=8 cycle value 29/12. The optimizer variable is the square root of the matching conductance. Symmetry gives equality of row and column endpoint norms. My exact replay inverted L+J rather than a grounded Laplacian and verified full columns in 21 configurations including both exact phase ties (python3 /workspace/review-checks.py, weighted section); the analytic argument covers unsampled x and N.

## originality

PASS

The electrical matrix and symmetry methods are prior. Close exact studies of one-edge weighting, clique/independent joins, and unweighted biclique prisms supply analogues of the optimization and switches, but none of their examined hypotheses gives the two-conductance perfect matching in a complete graph or its full quantitative classification.

## value

PASS

The perfect matching provides a natural symmetry-preserving perturbation of a dense network. The result gives a full orbit phase diagram and an exact interval of disagreement between complementary projection norms; the two equal sharp amplification heights at different weights and the exceptional order eight are useful quantitative benchmarks. It does not address arbitrary weights, nonorthogonal projection minima, or intermediate p norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
