# Independent mathematical audit

## correctness

PASS

Rechecked the original and the narrowed proof from the labelled vertex rules. A clique vertex of bit x sees c+s−x ones out of 2n−1, so the clique goes to 0, complements, or goes to 1 according to the sign of c+s−n. The independent side goes to 0, stays unchanged, or goes to 1 according to 2c−n. For positive total sign, negative clique sign sends the state to opposite constant shores, positive sign to consensus, and the clique tie keeps a nonempty independent word so the next step is consensus; the negative total sign is complementary. At total equality, the endpoints already alternate, the even midpoint flips the labelled clique with the independent word fixed, and 0<c<n/2 gives (n−c,0) and then opposite constant shores, with the other branch complementary. Thus the basin is precisely the total-equality layer plus the two strict opposite-sign regions. The Vandermonde layer contributes binom(2n,n). In the upper-total strict region j=n−s gives 0≤j<c<n/2; exchange symmetry doubles its mass to the entire weighted binomial square minus the diagonal, A_n²−Q_n. Odd/even symmetry yields the two closed forms. For even n the linear central-binomial term contributes −sqrt(2)/(2 sqrt(πn)), the central-square term contributes 3/(2πn), and the remaining central binomial contributes 1/(2 sqrt(πn)); the displayed error bounds follow from central-binomial Stirling with relative O(1/n). The repaired proof retains all sizes, including B₁=2 and B₂=6, and does not conflate fixed occupancies with fixed configurations. In the original, the same rule confirms the known recurrent census, and checks the sharp boundary transients directly: n=1 all states are periodic; for n=2 a clique tie is either already balanced or gives consensus in one step, and constant-clique cases take at most one; c=1,s=n−1 needs two steps for n≥3. None of these prior structural facts is sold as novelty in the repair.

## originality

PASS

PASS only the repaired finding: the closed weighted count of all initial configurations attracted to oscillation and the parity-dependent quantitative approach to one quarter. Not a PASS for the original census/entry novelty package. The exact split-graph comparators permit identification of the eventual outcome from their update analysis but do not state or evaluate the weighted basin sum. The repaired theorem adds this enumeration, rather than rebranding the known local or recurrent dynamics.

## value

PASS

The balanced graph is a natural family and basin mass is an independent dynamical observable: the known exponential difference in the number of recurrent cycles does not translate to a different limiting chance of oscillation. The closed all-size enumeration and opposite finite-size parity deviations quantify the distinction for unbiased initial opinions. This is not value assigned to recomputing the known orbit count or convergence depth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
