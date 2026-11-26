# Independent mathematical audit

## correctness

PASS

At a world w, a falsifying valuation must split each of its successors' successor sets between truth and falsity. If R(w) is empty this is vacuous and the axiom fails; if some R(v) for v in R(w) is empty the antecedent instead fails. A globally valid frame therefore has no empty rows. A singleton second-step set cannot split; if every one has size two, there are at most two distinct undirected edges and they admit a bipartition. This proves the exact criterion, loops included. With k singleton rows, their targets must belong to the same k-element set, giving k^k choices; every other row chooses a distinct unordered pair meeting that set, giving A(n,k)=k(2n-k-1)/2 choices. This counts each relation once. At n=5 the five summands are 1280, 13720, 21870, 12800 and 3125, summing to 52795. For all sufficiently large n, the function k+(n-k)log k is strictly concave with its unique maximum at k*=n/W_0(n), where log k*=W_0(n). The upper bound uses binom(n,k)<=(en/k)^k and A<=nk, plus log n for summation. The lower bound uses floor(k*) and binom(n,k)>=(n/k)^k, A>=k(n-k); the floor costs O(log n) and replacing n by n-k inside the pair-count factor costs O(n/W_0(n)). This gives the first displayed log law. Expanding W_0 and subtracting n log(1+n+binom(n,2)) gives the other two. At the degree-three example's root the three second-step pairs form a triangle; all other worlds see singleton rows, so the example has the required global validity. Proof checked against RESULT.md lines 39–83. The supplied n<=4 checker and verification notes were inspected, not executed; they cannot check the asymptotic.

## originality

PASS

Credit the labelled census and its sharp logarithmic asymptotics on the full degree-two class. The splitting reduction and the odd-cycle mechanism for sharpness are already present in prior statements, and the degree-two criterion is a short consequence of the local reduction. Neither the lattice of frame classes nor the similar integer sequence below covers the quantitative result. The six-world example is valid, but a maximum-outdegree-three obstruction as such is not new.

## value

PASS

The maximum-outdegree-two class is the last degree bound at which the singleton-access criterion is exact. Moving from a validity test to an exact census and the asymptotic rarity among all capped relations quantifies a natural modal constraint; the result is not just a small table or a rephrasing of the earlier splitting reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
