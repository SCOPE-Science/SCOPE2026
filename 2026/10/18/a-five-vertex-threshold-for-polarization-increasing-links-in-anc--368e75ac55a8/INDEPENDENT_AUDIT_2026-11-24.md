# Independent mathematical audit

## correctness

PASS

The update is a contraction in sup norm (row sums d_i/(a+d_i)<1), and the Laplacian equation preserves the innate mean. Reproduced the exact lower bound independently of the frozen adjugate code. Relabel the nonedge as 01; enumerate all connected masks on the remaining pairs with no graph-isomorphism quotient, and all nonzero binary opinions with s_0=0 by complement symmetry. In difference coordinates y_i=z_i-z_0, solve (a I+Q)y=a(s_i-s_0)_{i>0}, where Q_ij=L_ij-L_0j for i,j>0. Compute polarization as sum y_i^2-(sum y_i)^2/n. For each rational difference that is not identically zero, remove powers of a from its reduced numerator, test that the numerator has no positive Sturm roots, and check that Delta(1)<0; the rational function has no positive pole since the original Laplacian resolvents are nonsingular. This gave (graphs, identically zero, strictly negative) = (1,1,2) for n=3 and (14,18,80) for n=4, with n<=2 vacuous. Replay: python3 /workspace/check_opinion.py (independent SymPy reproduction, unexecuted frozen verifier). For the specified five-vertex witness, reflecting 0 with 2 and 4 with 3 leaves the symmetric component unchanged under the edge update. On antisymmetric coordinates at 0 and 4, the system has matrix with diagonals (a+2,a+1), off-diagonal -1, and input (-a/2,a/2); the new edge replaces a+2 by a+4. Subtracting twice the squared solution norms produces the stated rational difference. Exact evaluations yield 2/405 and -496/34969; the quartic's one sign variation and its opposite signs at 1 and 2 give the unique positive crossover (approximately 1.32018042507931). The obstruction is binary and homogeneous; it does not assert monotonicity for arbitrary real opinions.

## originality

PASS

Pass for the sharp obstruction simultaneously for every positive common anchor, and the unique reversal in the specified path as that anchor varies. The indexed unit-anchor threshold and witness match exactly after opinion re-encoding. General weighted-edge formulas and prior increases for real innate opinions are antecedents, not the all-anchor binary theorem or the exact crossover.

## value

PASS

The uniform obstruction rules out counterexamples below five agents at every positive homogeneous anchor, not merely at the standard unit normalization. The path example then identifies a true reversal under global social-to-innate scaling, with an exact threshold that separates improvement from worsening in a minimal example. The binary restriction is substantive in view of smaller nonbinary examples; no empirical claim follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
