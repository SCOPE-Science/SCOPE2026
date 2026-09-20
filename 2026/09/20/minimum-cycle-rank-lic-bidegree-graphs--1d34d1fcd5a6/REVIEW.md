# Same-model scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** In a bidegree graph with degree classes X (degree b) and Y (degree
a), the irregular-edge spanning subgraph is exactly the bipartite graph between
X and Y. LIC therefore forces this bipartite graph to be connected. Writing
x=|X| and y=|Y| gives the exact identity

\[
\mu(G)=\frac{(b-2)x+(a-2)y}{2}+1.
\]

The maximum-degree condition gives x+y >= b+1. If x=1, LIC forces y=b and the
low-degree induced graph to be (a-1)-regular, which is possible exactly when
b(a-1) is even. These facts give the two parity regimes and the sharp lower
bounds. Equality conditions were followed separately for a>=3, a=1, and a=2.
The only non-rigid case is a=2 with b odd; there the cycle-rank identity depends
only on x, so equality means x=2, and the degree-2 vertices decompose exactly
into common neighbors plus matched private neighbors as stated.

The regular-graph constructions satisfy the required parity and degree bounds.
Exact finite enumeration over the NetworkX Graph Atlas agrees with the formulas
and the extremal structure, and deterministic constructions were checked over
a broad parameter range. Computation is supporting evidence only; the theorem
is proved symbolically.

## Originality

**PASS, to the best of our knowledge.** The closest primary source is Chartrand
and Zhang (2026). Its Theorem 5 determines minimum order for arbitrary positive
degree sets, and its Proposition 5 / Theorem 9 shows that among two-element
sets, cycle rank 2 occurs exactly for {2,3} and {2,4}. Its closing problem asks
for prescribed cycle rank r>=3. The present formula determines the minimum
attainable cycle rank for every two-element degree set and recovers the two
known rank-2 cases as exactly the pairs for which the formula equals 2.

The unrestricted least-size degree-set problem is older. Tripathi and Vijay
(2006) explicitly determine least size for degree sets of cardinality at most
three, and later work revisits the general problem. Accordingly, the least-size
formula is not claimed as a new unrestricted result; the record only notes that
adding the LIC requirement imposes no least-size penalty. Searches using
locally irregular-connected, bidegreed, degree-set, cyclomatic/cycle-rank, and
minimum/least-size terminology did not locate the minimum-cycle-rank formula or
classification stated here.

Residual risk remains from very recent follow-up work or differently indexed
bidegreed/cyclomatic literature. The complete 2006 paper was not inspected
page-by-page in this review, but its stated scope already establishes that the
unrestricted two-degree least-size problem is prior art, so that part is
conservatively excluded from the novelty claim.

## Value

**PASS.** The result supplies an exact threshold for the first possible cycle
rank of every LIC bidegree set, turning the isolated cycle-rank-2 classification
in the source paper into a closed all-parameter formula. The equality analysis
also gives the full minimum-cycle-rank structure, including a genuinely
non-rigid exceptional family for degree sets {2,b} with odd b. The theorem is
a direct, concrete bidegree advance toward the source paper's open higher-cycle-
rank program.

## Evidence and limitations

The result concerns two-element positive degree sets only. It does not classify
which larger cycle ranks r above the minimum are attainable, and it does not
solve the source paper's higher-cycle-rank problem for degree sets of three or
more values. The unrestricted least-size formula is prior art. Originality is
to the best of our knowledge, with residual risk from recent or differently
indexed literature.
