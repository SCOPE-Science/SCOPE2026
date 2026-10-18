# A matched-apex gathering bound for graph pebbling

## Finding
Let \(G\) be a finite simple graph of odd order \(2r+1\), with \(r\ge1\). Suppose that it has a universal vertex \(z\) and that \(G-z\) contains a perfect matching. Under the pebbling rule that a move from \(u\) to its neighbour \(v\) replaces two pebbles at \(u\) by one pebble at \(v\), **every configuration of size at least \(4r\) can be stacked at the specified vertex \(z\)**. In particular,
\[
\operatorname{stack}(G)\le4r=2(|V(G)|-1).
\]
This applies, for example, to every friendship graph \(K_1\vee rK_2\), and to any graph obtained by adding edges among its outer vertices. The statement concerns stacking, not clearing.

## Assumptions and scope
A configuration assigns a nonnegative integer to each vertex. A configuration is stacked at \(z\) if its support is exactly \(\{z\}\). The stacking number is the least integer \(t\ge2\) such that every configuration of size \(t\) is stackable somewhere. We prove a stronger assertion with the destination fixed at \(z\), for every input size \(t\ge4r\). Label the matched pairs \(\{a_i,b_i\}\), for \(1\le i\le r\). All moves below use only matching edges and edges incident to \(z\); no other adjacency is needed.

## Proof
For initial hub load \(h\) and outer loads \(a_i,b_i\), let \(O\) denote the number of odd outer loads and \(u\) the number of matched pairs containing at least one odd load. First, for each outer vertex, repeatedly send two pebbles to \(z\). This leaves one pebble at each initially odd outer vertex, and gives the hub load
\[
H=h+\sum_{i=1}^{r}\left(\left\lfloor\frac{a_i}{2}\right\rfloor+\left\lfloor\frac{b_i}{2}\right\rfloor\right)=\frac{t+h-O}{2}.
\]
If \(H\ge u+1\), process the \(u\) active pairs as follows. A single residual pebble at \(a_i\) is cleared by the two moves \(z\to a_i\to z\); this changes the hub load from \(H\) to \(H-1\). The same works for \(b_i\). If both members of a pair carry one pebble, use \(z\to a_i\to b_i\to z\), again reducing the hub load by one. Every sequence is legal whenever the current hub has at least two pebbles. Starting at \(H\ge u+1\), this remains true until the last pair is cleared, after which the hub has at least one pebble. Therefore the configuration is stacked at \(z\).

It remains to show that the inequality \(H\ge u+1\) is available, with one explicit adjustment if necessary. For each pair the number of odd loads is \(0\), \(1\), or \(2\), contributing respectively \(0\), \(3\), or \(4\) to \(Q=O+2u\). Hence \(Q\le4r\), and the desired inequality is exactly \(t+h\ge Q+2\). If \(t+h\ge4r+2\), it follows immediately. For \(t=4r+1,h=0\), \(O\) is odd and therefore \(Q\le4r-1\), giving the inequality. For \(t=4r,h=1\), again \(O\) is odd and \(Q\le4r-1\), giving \(t+h\ge Q+2\). For \(t=4r,h=0\), \(O\) is even. Unless all \(2r\) outer loads are odd, \(Q\le4r-2\), so the inequality follows. The remaining cases with \(t\ge4r\) all satisfy \(t+h\ge4r+2\), or have already been covered.

In the exceptional case \(t=4r,h=0\) and every outer load is odd, at least one matched pair \((a_i,b_i)\) has, after possibly swapping its vertices, \(a_i\ge3\) and \(b_i\ge1\). Perform the two internal moves \(a_i\to b_i\) and \(b_i\to a_i\). The pair's new loads are \(a_i-1,b_i-1\), both even. Transfer all outer even pairs of pebbles to the hub as above. The chosen pair now contributes no residual pebbles; the other \(r-1\) pairs each contain two singletons. After the two internal moves and subsequent \(r\) outer-to-hub moves, the hub contains \(r\) pebbles and exactly \(2r-2\) outer singletons remain. This hub load satisfies \(r=(r-1)+1\), so the preceding clearing procedure finishes at \(z\). The construction terminates and uses only permitted edges, proving the claim for all \(r\ge1\). \(\square\)

## Verification
The accompanying standard-library program `verify_matched_apex.py` enumerates every weak composition of exactly \(4r\) pebbles on the friendship graph \(K_1\vee rK_2\) for \(1\le r\le4\), replays the construction step by step, and asserts that all outer vertices are emptied with a positive hub load. It also checks, by an independent memoized reachability recursion, a nonstackable size-\(4r-1\) example for each of those four small values. Those finite checks do not establish a universal lower bound.

## Relationship to prior work
Csernák and Soukup introduced \(\operatorname{stack}(G)\), established a general bound \(2|V(G)|2^{\operatorname{diam}(G)}\), and computed it on paths, complete graphs, and complete multipartite graphs [1]. Their results do not directly yield this matched-apex construction. The follow-up treatment of the Almost Stacked Hypothesis gives cycle and tree methods and conditional results about perfect pebblability [2]. Our proof is unconditional and concerns universal vertices with a matching in the remainder; it does not use that hypothesis. An older identically named stacking number from eternal domination is a different invariant [3].

## Limitations
The argument proves only the stated upper bound; it does **not** prove \(\operatorname{stack}(K_1\vee rK_2)=4r\) for all \(r\). The finite obstruction checks cover only \(r=1,2,3,4\). This proof does not determine the clearing number, treat an unmatched non-universal vertex, or imply the Almost Stacked Hypothesis. Bibliographic priority beyond the inspected sources is not independently established.

## References
[1] T. Csernák and L. Soukup, *Stacking and Clearing in Graph Pebbling*, arXiv:2604.22341, first posted 2026-04-24. https://arxiv.org/html/2604.22341v1

[2] T. Csernák and L. Soukup, *The Almost Stacked Hypothesis: A Conjectural Analogue of Sjöstrand's Cover Pebbling Theorem*, arXiv:2610.09650, first posted 2026-10-07. https://arxiv.org/abs/2610.09650

[3] *Stacking numbers for eternal domination*, Journal of Combinatorial Mathematics and Combinatorial Computing 124 (2025). https://doi.org/10.61091/jcmcc124-47
