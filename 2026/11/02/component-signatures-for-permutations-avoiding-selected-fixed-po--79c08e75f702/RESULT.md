# Component signatures for permutations avoiding selected fixed points

## Finding
For every integer \(n\ge2\) and subset \(F\subseteq[n]\), form the graph \(G(n,F)\) of permutations \(\pi\in S_n\) satisfying \(\pi(i)\ne i\) for each \(i\in F\). Two permutations are adjacent exactly when one is obtained from the other by exchanging values in consecutive positions and the new permutation remains feasible. For every internal forbidden value \(j\in F\cap\{2,\ldots,n-1\}\), write \(\epsilon_j(\pi)=L\) if the value \(j\) occurs before position \(j\), and \(R\) if it occurs after that position.

**Theorem.** These signatures classify all connected components, each possible signature occurs, and their number is exactly
\[
  \#\operatorname{components}(G(n,F))=2^{|F\cap\{2,\ldots,n-1\}|}.
\]
Every vertex can be transformed to its signature's canonical representative using at most \(\binom n2\) legal adjacent swaps, so each component has diameter at most \(n(n-1)\). In particular the adjacent-swap graph of classical derangements has exactly \(2^{n-2}\) connected components for \(n\ge2\).

## Assumptions and scope
Labels and positions are both \([n]=\{1,\ldots,n\}\), and \(\operatorname{pos}_{\pi}(j)\) denotes the unique position occupied by value \(j\). The condition \(\pi(i)\ne i\) is imposed only when \(i\in F\). The moves exchange entries at positions \(i,i+1\), not arbitrary-position transpositions. The theorem includes empty \(F\), endpoint-only \(F\), and full \(F\), with \(n\ge2\). It does not address Hamilton paths or exact component diameters.

## Proof
Let \(L\) be all values \(j\in F\) lying strictly left of their forbidden position, let \(R=F\setminus L\), and let \(U=[n]\setminus F\). A single adjacent swap moves any value by one position. If \(j\in F\), its relative side of position \(j\) cannot change through a sequence of feasible swaps, since changing the side would require occupying forbidden position \(j\). Hence the sets \(L,R\), or equivalently the internal signature, are invariant. For endpoints, \(1\in F\) is forced into \(R\), and \(n\in F\) is forced into \(L\); there are no choices there.

For any prescribed assignment of sides to the internal members of \(F\), define \(L,R\) accordingly, including the forced endpoint assignments, and set \(U=[n]\setminus F\). Consider the canonical word \(c(L,R)\) obtained by listing the elements of \(L\) increasingly, then \(U\) increasingly, then \(R\) increasingly. If \(j\in L\), its position is \(|\{\ell\in L:\ell\le j\}|\le j-1\), because \(1\notin L\). If \(j\in R\), its position is \(n-|\{r\in R:r>j\}|\ge j+1\), because \(n\notin R\). Thus this word is feasible and realizes the prescribed signature, proving every signature occurs.

It remains to connect every feasible word with its canonical word. Order labels by the total order: first \(L\) in increasing order, then \(U\) in increasing order, then \(R\) in increasing order. Bubble-sort a feasible word by swapping every adjacent pair appearing in the wrong order. Each such swap is feasible. Across blocks, an \(L\)-label only moves left and an \(R\)-label only moves right; an \(U\)-label is unrestricted. Within \(L\), a wrongly ordered pair \(x>y\) at consecutive positions \(t,t+1\) has \(t+1<y<x\), because \(y\in L\) was valid before the swap. After swapping, \(x\) lies at position \(t+1<x\) and \(y\) lies even farther left, hence both stay valid. Within \(R\), a wrongly ordered pair \(x>y\) at \(t,t+1\) has \(t>x>y\), because \(x\in R\) was valid before the swap. After swapping, \(y\) lies at \(t>y\) and \(x\) moves farther right, so both stay valid. Pairs within \(U\) are unconstrained. Consequently every bubble-sort swap stays inside \(G(n,F)\).

Bubble sorting reaches \(c(L,R)\) and uses precisely the inversion count relative to the target order, at most \(\binom n2\) swaps. Two vertices having the same signature may be joined through that canonical word using at most \(2\binom n2=n(n-1)\) swaps. Different signatures cannot be connected. This proves all conclusions. \(\square\)

## Verification
The accompanying Python verifier independently enumerates every forbidden-position mask for each \(2\le n\le7\), constructs every feasible permutation and adjacent exchange, computes graph components by breadth-first search, checks all signatures and replays canonical sorting. The separate C++17 implementation exhaustively tests all masks for \(2\le n\le8\), constructs components using a disjoint-set union and confirms that components and signatures coincide. Both pass. The all-parameter result is proved above; finite tests alone would not establish it.

## Relationship to prior work
Baril and Vajnovszki (2004) give Gray-code generation of derangements using unrestricted transpositions and three-cycles. Vajnovszki (2010) gives ECO generation algorithms for derangements and related permutation classes, also using operations broader than feasible consecutive-position swaps. Clark (2013) studies graph derangements and their existence properties, not connected components of this forbidden-diagonal induced subgraph of the permutahedron. The present result distinguishes adjacent-swap mobility from those broader generating operations and proves an exact component classification for arbitrary subsets of diagonal restrictions. A search of available literature did not reveal a theorem whose statement implies this complete adjacent-swap classification; this observation is not a proof of global novelty.

## Limitations
The diameter estimate is an upper bound, not a claim of sharpness. Exact sizes and shapes of individual components, shortest paths between arbitrary configurations and other restrictions on allowed positions are not classified here. An equivalent formulation may exist in older adjacent-exchange or permutation-poset literature. The conclusions do not apply when transpositions of arbitrary positions are allowed.

## References
- Baril, J.-L. and Vajnovszki, V., *Gray code for derangements*, Discrete Applied Mathematics **140** (2004), 207–221, doi:10.1016/j.dam.2003.06.002. https://jl.baril.u-bourgogne.fr/derange.pdf
- Vajnovszki, V., *Generating involutions, derangements, and relatives by ECO*, DMTCS **12**(1) (2010), 109–122, doi:10.46298/dmtcs.479. https://dmtcs.episciences.org/en/articles/479/download
- Clark, P. L., *Graph Derangements*, arXiv:1306.6436 (v1 June 27, 2013). https://arxiv.org/abs/1306.6436
