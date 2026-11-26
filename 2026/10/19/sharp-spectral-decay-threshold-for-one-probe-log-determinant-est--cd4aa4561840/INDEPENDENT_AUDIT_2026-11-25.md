# Independent mathematical audit

## correctness

PASS

For the repaired power-law claim take L>0 and p>1: e^{a_j}−1≤e^L a_j ensures trace class. The residual is a sum of independent real Gaussian squares, finite almost surely by the finite expectation, and its centered version converges in L². The exact risk is 2L²/N times the j^{−2p} tail. Integral upper and lower bounds at k and k+1 give the same B^{2p}-scaled objective uniformly in k/B on interior compact sets. The lower bound alone gives divergence at both endpoints, including bounded or zero deflation rank and bounded or sublinear probe counts. The admissible spacing c/B lets a sequence approach the unique minimizer x=(2p−1)/(2p) of x^{1−2p}/(1−x); every discrete minimizer approaches it. Evaluating there gives the repaired leading constant and the claimed probe budget share; holding N fixed gives the stated slower rate. The proof is self-contained in the repaired RESULT.md and does not rely on the inspected but unrun frozen script. The rejected threshold is mathematically supported by tail shifting and the geometric witness; its rejection is for coverage, not falsity. The original strictness argument with trailing zeros can use the last positive coefficient as the effective tail endpoint.

## originality

PASS

Originality FAIL for the frozen headline and geometric claims: an earlier Resultary theorem on the same exact risk makes the sharp uniform threshold a direct corollary, and its geometric allocation law is the same under reparameterization. The corrected files remove these claims. PASS is for the distinct power-law asymptotic of every exact optimal budget split and its leading risk; the inspected exact finite criterion and primary risk comparison do not themselves furnish this interior large-budget limit.

## value

PASS

The repaired result identifies a regime where spending essentially all growing budget on exact deflation and using a bounded number of probes is asymptotically suboptimal by a factor of order B. It quantifies the unique limiting split and the optimal leading error for a canonical slow spectral decay, a meaningful contrast to the known geometric allocation law. The endpoint analysis makes the conclusion about true integer optimizers rather than just a stationary point of a continuous relaxation. It has no claimed transfer to approximate randomized deflation or Lanczos.

The dated certificate retains the supplied scientific assessment, sources and limitations.
