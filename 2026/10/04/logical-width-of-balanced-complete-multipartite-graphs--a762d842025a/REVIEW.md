# Review

## Correctness
**PASS.** The upper bound uses the equivalence relation \((x=y)\lor\neg E(x,y)\) to characterize complete multipartite graphs, then separately fixes the number of parts and the common part size. Every conjunct fits in a common pool of \(\max\{r,s\}+1\) variables. The lower bound uses two explicit nonisomorphic comparison graphs and standard finite-variable pebble games. In each case the resource that differs—one extra vertex per part or one extra part—cannot be exposed with only \(\max\{r,s\}\) pebbles. Edge cases \(r=1\), \(s=1\), and \(r=s=1\) were checked separately.

## Originality
**PASS, with residual bibliographic risk.** Targeted searches covered exact-formula variants (“logical width” with complete multipartite, complete bipartite, balanced Turán, and \(k\)-variable terminology), broader descriptive-complexity formulations, and semantic-index records. The principal surveys inspected establish the general finite-variable framework and the definition of logical width but do not state this family formula. No equivalent or stronger published statement was located. Because the argument is elementary, an unindexed appearance in lecture notes or a textbook remains possible.

## Value
**PASS.** Balanced complete multipartite graphs are the Turán graphs, a standard two-parameter family. The formula isolates two distinct finite-variable bottlenecks and simultaneously recovers exact widths for complete graphs, edgeless graphs, and balanced complete bipartite graphs. It therefore provides a clean calibration example for finite-variable definability rather than a sporadic small case.

Same-model review: passed. Independent audit: not yet performed.
