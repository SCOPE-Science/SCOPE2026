# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

PASS. The hard family has exact doubling constant \(2^{m+1}/(2^m+1)<2\) and an admissible two-coset cover by the known subspace \(H\). The key structural bound is dimension-theoretic: if \(L\) cosets of an admissible \(V\) cover \(H\), then \(2^{m-\dim(H\cap V)}\le L\), while the image of \(V\) in \(G/H\) has dimension at most \(m-\dim(H\cap V)\). Hence the projected union contains at most \(L^2\) quotient classes. The oracle argument then reduces the hidden outlier to equality testing among \(2^m-1\) candidates, except when a uniform sample directly hits it. The quantitative success bound follows by conditioning on whether either access method hits the outlier. Finite exhaustive checks support the dimension calculation but are not used as a substitute for the proof.

Adversarial checks considered alternative subspaces, noncanonical translate representatives, overlapping cover cosets, adaptive membership queries, and randomized strategies. None changes the argument: admissibility forces \(\dim V\le m\), projection controls every possible output, and before the first outlier hit all informative membership answers are identical negatives. The free basis of \(H\) only strengthens the lower bound.

## Originality

PASS, to the best of our knowledge. The inspected algorithmic PFR theorems formulate their output as an explicit basis for a subspace \(V\) whose polynomially many translates cover \(A\); they do not require the algorithm to output those translating representatives. Their proofs use covering lemmas existentially at the final covering step. The August 2026 robust PFR work similarly outputs a subspace or list of subspaces and controls the covering number \(\mathcal N_V(A)\), rather than materializing a cover.

Targeted searches for algorithmic PFR combined with explicit translates, cover representatives, witness recovery, membership-oracle lower bounds, and Ruzsa-cover query complexity found no equivalent lower bound. Searches of the current SCOPE archive by the motivating arXiv identifier, Algorithmic PFR terminology, small doubling, Freiman--Ruzsa, and translate-cover terminology found no overlapping record.

The main residual risk is folklore: the hard instance is intentionally simple, and the distinction between outputting a covering subspace and outputting an explicit translating set is natural once noticed. The motivating polynomial-time PFR paper is also very recent, so near-simultaneous observation remains possible. No inaccessible paper produced concrete evidence of prior coverage.

## Value

PASS. The theorem identifies an information-theoretic boundary in the natural oracle formulation of algorithmic PFR. It explains why a polynomial-time theorem can construct the structured subspace while leaving the translating set existential: the latter can encode an exponentially rare outlier even at doubling constant below two. The separation holds when the correct subspace is given for free and when an optimal two-coset cover exists, so it isolates witness materialization rather than subspace learning as the source of hardness.

## Limitations

The result applies to explicit lists of translate representatives in the sample-plus-point-membership oracle model. Stronger access primitives, compressed symbolic cover representations, or additional regularity assumptions may avoid the barrier. The proof does not give a lower bound for merely outputting a PFR subspace, which is intentionally the task solved by the cited algorithmic PFR results.
