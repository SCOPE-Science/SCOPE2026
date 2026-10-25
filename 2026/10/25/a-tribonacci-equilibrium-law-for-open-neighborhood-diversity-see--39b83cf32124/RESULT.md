# A tribonacci equilibrium law for open-neighborhood diversity-seeking swaps on cycles

## Finding
Fix an integer \(n\ge3\) and the labeled cycle \(C_n\). Each vertex contains one agent of one of two colors \(0,1\). An agent receives utility \(1\) exactly when one of its two neighbors has its own color and the other has the opposite color; otherwise it receives utility \(0\). Any two agents may exchange vertices only when **both** strictly improve. Agents of the same color are strategically interchangeable; the statements count vertex-labeled colorings, not permutations of individually named agents.

**Theorem.** For every binary coloring \(x=(x_i)_{i\in\mathbb Z/n\mathbb Z}\):

1. Every profitable exchange is between **adjacent** agents and occurs if and only if the four consecutive colors are \(0101\) or \(1010\), with the middle pair exchanged. Consequently a coloring is a swap equilibrium if and only if it avoids both alternating four-letter words cyclically, equivalently if no two consecutive maximal monochromatic runs have length one.
2. Every maximal sequence of profitable exchanges terminates. If \(x\) contains both colors and has \(b(x)\) bichromatic edges, the number of exchanges is at most \((b(x)-2)/2\), hence at most \(\lfloor(n-2)/2\rfloor\). A monochromatic coloring has no improving exchange.
3. Let \(E_n(z)=\sum_{k=0}^{n} e_{n,k}z^k\) count equilibria by the number \(k\) of color-\(1\) vertices. Define the eight states \(\mathcal S=\{000,001,010,011,100,101,110,111\}\), and define an \(8\times8\) weighted transition matrix \(T(z)\) by
   \[
   T(z)_{abc,bcd}=z^d \quad\text{if }(a,b,c,d)\notin\{0101,1010\},
   \]
   with all other entries zero, including both forbidden transitions. Then, for all \(n\ge3\),
   \[
   E_n(z)=\operatorname{tr}(T(z)^n),\qquad
   \det(I-tT(z))=(1+zt^2)(1-(1+z)t+z^2t^4).
   \]
   In particular, if \(U_0=3\), \(U_1=1\), \(U_2=3\), and \(U_n=U_{n-1}+U_{n-2}+U_{n-3}\) for \(n\ge3\), then
   \[
   E_n(1)=U_n+1+2\cos(n\pi/2).
   \]
   With \(\tau\approx1.839286755214161\) the positive root of \(\tau^3-\tau^2-\tau-1=0\), the total equilibrium count is \(\tau^n+O(1)\). Thus independent fair initial colors give equilibrium probability \((\tau/2)^n(1+O(\tau^{-n}))\).

For example, \(E_8(z)=1+8z+20z^2+24z^3+28z^4+24z^5+20z^6+8z^7+z^8\), so there are exactly \(134\) equilibrium colorings among the \(256\) colorings of the eight-vertex cycle.

## Assumptions and scope
The network is the simple undirected labeled cycle \(C_n\) for \(n\ge3\). Its two neighbors are distinct even when \(n=3\). Every vertex is occupied; there are exactly two types, and both types share the **open-neighborhood** symmetric utility with unique maximum when exactly one of the two neighbors has the agent's color. Every permitted move swaps a pair of agents at distinct vertices, without restrictions on their distance, and both must strictly improve. The equilibrium polynomial counts the induced colorings, preserving their labeled vertex positions and not quotienting by rotation or color complement. No stochastic selection of moves is assumed.

## Proof
**Step 1: locality and the forbidden words.** The utility at vertex \(i\) is simply
\[
 u_i(x)=\mathbf1\{x_{i-1}\ne x_{i+1}\}.
\]
For opposite-color agents at **nonadjacent** vertices \(i,j\), swapping them leaves the two neighbor-color multisets at their destination vertices unchanged. In this binary two-neighbor setting, both agents' utilities exchange values: the agent arriving at \(j\) receives the former utility of the occupant at \(j\), and conversely. They cannot both strictly improve. Same-color swaps leave the coloring unchanged and also cannot improve.

For adjacent opposite-color agents at \(i,i+1\), write the four consecutive colors as \((a,r,s,d)\) at vertices \(i-1,i,i+1,i+2\), with \(r\ne s\). Before the move their utilities are \(\mathbf1\{a\ne s\}\) and \(\mathbf1\{r\ne d\}\); after exchanging them, their utilities are \(\mathbf1\{s\ne d\}\) and \(\mathbf1\{a\ne r\}\), in the corresponding destinations. Both strictly improve precisely when \(a=s\) and \(d=r\). Hence the four colors alternate, and exchanging the central pair makes both agents satisfied. This proves the exact local criterion, including the triangle boundary \(n=3\), for which no cyclic four-letter alternating block can occur. A cyclic alternating block corresponds exactly to two adjacent runs of length one (the two central singleton runs), proving the run characterization.

**Step 2: finite improvement.** In an improving exchange the three edges on the four-vertex path initially join opposite colors, and afterward only the central edge does. The outside colors and all other edges are unchanged. Hence the number \(b(x)\) of bichromatic edges falls by exactly two. In every mixed coloring of a simple cycle, \(b(x)\) is an even integer of at least two, so there can be no more than \((b(x)-2)/2\) improving exchanges. This implies both the global bound and termination at the equilibrium described in Step 1. In \(C_3\), no such exchange exists and the assertion remains valid.

**Step 3: exact weighted enumeration.** Form a directed transition graph on the ordered three-bit states \(\mathcal S\). A transition \(abc\to bcd\) is permitted precisely when \(abcd\) is not one of the two forbidden alternating patterns, and contributes weight \(z^d\). Every closed directed walk of length \(n\) corresponds bijectively to a length-\(n\), vertex-indexed cyclic binary coloring avoiding those words, including periodic colorings; its weight is \(z^{\sum_i x_i}\). The trace therefore equals the claimed polynomial. Expanding the determinant of this explicit eight-state matrix gives
\[
 \det(I-tT(z))=(1+zt^2)(1-(1+z)t+z^2t^4).
\]
The determinant expansion is also independently executable in `verify.py`, which constructs the matrix from the rule rather than inserting an assumed characteristic polynomial. At \(z=1\), the denominator becomes \((1+t^2)(1-t)(1-t-t^2-t^3)\). Accordingly the nonzero eigenvalues are \(i,-i,1\) and the three roots of \(\lambda^3-\lambda^2-\lambda-1=0\); the other two eigenvalues are zero. Their power sums give \(E_n(1)=U_n+1+2\cos(n\pi/2)\) for \(n\ge3\). The cubic has one real root \(\tau>1\), and its other two conjugate roots have modulus \(\tau^{-1/2}<1\), by the product-of-roots identity. The remaining eigenvalues have modulus at most one, so \(E_n(1)=\tau^n+O(1)\). Dividing by \(2^n\) proves the last probability statement.

## Verification
Run `python verify.py` with Python 3 and SymPy installed. It reconstructs \(T(z)\) from the forbidden-transition definition, checks the determinant and characteristic polynomial as **exact symbolic identities**, and independently enumerates all labeled binary colorings for \(3\le n\le14\). For each coloring it checks all opposite-color agent pairs by directly recomputing both agents' utilities before and after an exchange. It compares that verdict with the forbidden-word criterion, and checks every coefficient of the resulting color-count polynomial against \(\operatorname{tr}(T(z)^n)\). It finally compares the total with the tribonacci recurrence and mod-four correction. All tests passed.

The first twelve total counts, for \(n=3,\ldots,14\), are \(8,14,22,38,72,134,242,442,816,1502,2758,5070\). These finite checks are supportive only: the all-size conclusions follow from Steps 1–3.

## Relationship to prior work
Bilò, Bilò, Lenzner and Molitor (2022) rigorously study **closed-neighborhood** single-peaked swap Schelling games; an agent counts itself, so on a cycle the relevant same-type fractions are \(1/3,2/3,1\). Their equilibrium-existence and price-of-anarchy statements do not yield this **open-neighborhood**, peak-at-one-of-two-neighbors classification or its producer-by-population-type counting polynomial. The two equilibrium notions are not equivalent: the coloring \(111000\) is stable here but is not stable under the closed-neighborhood peak-\(1/2\) model, whereas \(010101\) is stable under that closed-neighborhood model but is unstable here. The previously established closed-neighborhood cycle equilibrium distribution therefore does not imply the present count.

Bilò, Bilò, Lenzner and Molitor (2022, *Topological influence and locality in swap Schelling games*) analyze an **open-neighborhood but monotone same-type utility** and give efficiency bounds on cycles. Their utility is not peaked at one same-type neighbor, and their cycle results do not imply the local-alternation condition. Classical finite-state forbidden-word enumeration is used as a proof technique here; no priority is claimed for the underlying transfer-matrix method or for tribonacci numbers as an abstract combinatorial sequence. The claim of mathematical contribution concerns its exact game-theoretic interpretation, global improvement locality and full equilibrium-by-color count.

## Limitations
The theorem does not apply to closed-neighborhood utilities, monotone utilities, heterogeneous preferences, more than two types, empty vertices, general graphs, or swapping rules that accept weak improvements. The count is for type colorings, not distinct-agent assignments. The result gives worst-case convergence steps, not the distribution of convergence times or terminal equilibrium under randomly selected profitable swaps. The possibility of an older, equivalent model-specific statement in unindexed literature is not eliminated by the searches reported here.

## References
1. D. Bilò, V. Bilò, P. Lenzner and L. Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games*, arXiv:2204.12599, first submitted April 26, 2022. https://arxiv.org/abs/2204.12599
2. D. Bilò, V. Bilò, P. Lenzner and L. Molitor, *Topological influence and locality in swap schelling games*, Autonomous Agents and Multi-Agent Systems 36 (2022), article 47. https://doi.org/10.1007/s10458-022-09573-7
3. A. Agarwal, E. Elkind, J. Gan, A. Igarashi, W. Suksompong and A. A. Voudouris, *Schelling games on graphs*, Artificial Intelligence 301 (2021), 103576. https://doi.org/10.1016/j.artint.2021.103576
