# Self-review

## Correctness
PASS. The canonical coordinates \(P(r,x)\) give the integer rank
\[
D(P(r,x))=(r-1)n+n-x.
\]
A direct transition analysis shows that neither generator can lower \(D\) by more than one. When \(x<n-1\), the cyclic letter lowers it by one; when \(x=n-1\), the singular letter lowers it by one, eventually synchronizing at \(r=1\). Hence \(D\) is a lower bound on every synchronizing word and is attained by the explicit greedy word. Converting the two circular orientations gives the closed formula for every labeled pair.

The verifier independently computes all shortest pair-to-singleton distances by reverse breadth-first search for every \(2\le n\le80\), checks both generator inequalities, and matches the closed formula.

## Originality
PASS for the narrowed final claim. Behague–Johnson already prove that the maximum pair weight is \(\binom n2\). A geodesic of that length necessarily visits every pair state, so the abstract spectrum \(1,\ldots,\binom n2\) is already an immediate consequence of their result and is explicitly credited as prior coverage.

The surviving statement is the state-by-state assignment
\[
t_n(\{i,j\})=\min\{(j-i)n-i,\ (n-j+i)n-j\}.
\]
Targeted searches under pair weight, power-automaton distance, exact-coordinate, average, and Černý aliases found no inspected source giving this formula. Cardoso's 2014 thesis is a residual risk: repository metadata was located and its extremal \(k\)-set result is summarized in the later primary paper, but the thesis body was not recovered through the bounded public route.

## Value
PASS. This is a natural complete classification of the pair layer of the canonical extremal synchronizing automaton, not an arbitrary finite parameter. It gives every target's shortest synchronization time and a simple rank certificate, refining a worst-case rendezvous result into an exact metric description.

Self-review: passed. Independent audit: not yet performed.
