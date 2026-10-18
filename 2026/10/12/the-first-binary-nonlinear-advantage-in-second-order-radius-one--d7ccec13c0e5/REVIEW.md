# Independent mathematical audit

## correctness

PASS

The shared-column definition is equivalent to the projection test: for x,y in forbidden complement S, there is a common allowable coordinate iff B_S(x) union B_S(y) is not all of [n]. For affine C=w+L with parity-check rank r>=2, choose two independent syndromes; no single parity-check column can simultaneously span both, hence affine |C|>=2^(n-1); coordinate hyperplanes attain the bound. For all n<5, a hypothetical code smaller than 2^(n-1) lifts by C_n × F_2^(5-n) to a length-five code of size <16, preserving the shared-coordinate covering property; this reduces all smaller-length obstructions to the n=5 bound (and agrees with the source direct searches through n=4). Independently compiled and executed an independently written monotone depth-first search for n=5: translate a 17-word forbidden subset to contain zero (preserving the property); adding forbidden words cannot repair a bad pair, so DFS search with inclusion pruning exhausts all possibilities. It visited 16,829,638 nodes and found no valid forbidden 17-set, proving K2(5,1)=16. Independently enumerated literal 2-row target matrices for the 29 distinct length-six witness words, yielding exactly all 4096 target pairs, hence K2(6,1)<=29<32. This proves earliest gap n=6 without asserting exact K2(6,1).

## originality

PASS

Best-of-knowledge originality judged against exact antecedent model, broader results, tables and mathematical implication. The new complete statement is not covered by the inspected sources; the named residual risks and incomplete full-text material prevent any claim of exhaustive priority or external certification.

## value

PASS

The first finite blocklength where binary product-form generalized covering breaks the affine-linear optimum is a natural finite-versus-asymptotic threshold, motivated by existing asymptotic linearity-cost theorems. The complete n<=5 obstruction and an explicit 29-word n=6 witness are substantive discrete information with a reproducible exhaustive certificate; lack of an exact n=6 optimum does not destroy the sharply defined first-separation fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
