# Exact odd-ring and twice-odd bijectivity for quadratic five-site cellular automata

## Finding
Consider a binary one-dimensional cellular automaton with five formal input sites and a local Boolean polynomial of **exact algebraic-normal-form degree two**. Among all \(2^{16}-2^6=65{,}472\) such rules, exactly **32** induce bijections on **every odd cyclic ring of size \(N\ge3\)**, and exactly **8** induce bijections on **every cyclic ring of size \(N\equiv2\pmod4\), \(N\ge6\)**. These classes admit the following explicit structural classification, not merely a numerical count.

Let \(\mathcal R=\{45,75,89,101,154,166,180,210\}\) denote elementary cellular automaton (ECA) rules in the standard Wolfram bit convention. Every one of the 32 odd-ring rules is an ECA rule from \(\mathcal R\), evaluated at exactly one of the four three-site arithmetic progressions
\[
 (i-2,i-1,i),\quad (i-1,i,i+1),\quad (i,i+1,i+2),\quad (i-2,i,i+2).
\]
Conversely, all 32 of these distinct five-input expressions are bijective on every odd ring. Of these, precisely the eight rules supported on \((i-2,i,i+2)\) are bijective on every ring of size \(N\equiv2\pmod4\). In particular, no genuinely five-variable quadratic rule and no other quadratic three-/four-site rule has either universal bijectivity property.

## Assumptions and scope
The state alphabet is \(\mathbb F_2\). A cyclic configuration \(x\in\mathbb F_2^N\) evolves synchronously according to
\[
(F_Nx)_i=f(x_{i-2},x_{i-1},x_i,x_{i+1},x_{i+2}),\qquad i\in\mathbb Z/N\mathbb Z.
\]
Here \(f:\mathbb F_2^5\to\mathbb F_2\) is specified by its unique algebraic-normal form, with at least one quadratic coefficient nonzero and all coefficients of degree at least three equal to zero. Thus \(f\) has one constant, five linear, and ten quadratic free coefficients, with the all-zero quadratic coefficient choice excluded. Ring indices are interpreted modulo \(N\); formal input sites may coincide on small rings, and the proof accommodates that.

For an ECA rule indexed \(r\in\{0,\ldots,255\}\), its output at three bits \((u,v,w)\) is the bit of \(r\) at position \(4u+2v+w\). The statement concerns bijectivity of a finite-ring map, not injectivity of the map on the full infinite shift. It makes no assertion that all rules not listed are non-bijective at every odd or twice-odd ring length.

## Proof
**1. An exact equal-output graph.** For each rule \(f\), introduce a directed graph with 256 vertices, each vertex an ordered pair \((u,v)\) of four-bit words. Append independently one bit to each word and retain the directed transition exactly when the corresponding five-bit words produce the same value of \(f\). Its destination is the ordered pair of length-four suffixes. Mark a vertex *off diagonal* when \(u\ne v\).

An ordered pair of distinct cyclic configurations of size \(N\) having the same image under \(F_N\) determines a length-\(N\) closed walk in this graph visiting an off-diagonal vertex. Conversely, every such walk reconstructs the two cyclic configurations by overlapping the four-bit windows. Consequently, \(F_N\) is noninjective if and only if there is a length-\(N\) closed walk through an off-diagonal vertex. Since the configuration set is finite, injectivity and bijectivity are equivalent.

**2. Cyclic-length criterion.** Decompose the graph into strongly connected components (SCCs). An off-diagonal vertex belonging to no directed cycle is irrelevant. For any cyclic SCC, let \(g\) be the greatest common divisor of the lengths of all its directed cycles, its graph period. Standard finite directed-graph path concatenation implies: from each vertex of a cyclic SCC, all sufficiently large positive multiples of \(g\) occur as lengths of closed walks, while every such length is divisible by \(g\). In particular, a cyclic off-diagonal SCC admits an odd closed-walk length exactly when \(g\) is odd. It admits a length \(N\equiv2\pmod4\) exactly when \(4\nmid g\): if \(g\) is odd take a sufficiently large multiplier congruent to two modulo four, and if \(g\equiv2\pmod4\) take a sufficiently large odd multiple. Therefore all odd rings are bijective precisely when **every cyclic off-diagonal SCC has even period**; all twice-odd rings are bijective precisely when **every cyclic off-diagonal SCC has period divisible by four**. The restriction \(N\ge3\) or \(N\ge6\) is automatic: the construction yields arbitrarily large admissible collision lengths when any forbidden SCC is present.

**3. Exhaustive finite classification.** Number the input variables \(a,b,c,d,e\), from leftmost to rightmost. Encode an algebraic-normal form by its 16-bit coefficient mask in the monomial order
\[
1,\ a,b,c,d,e,\ ab,ac,ad,ae,bc,bd,be,cd,ce,de.
\]
The additional standalone file `verify.c` exhaustively iterates every one of the 65,472 masks with a nonzero quadratic part. For each it constructs all allowed equal-output graph edges using the 32-bit truth table, computes SCCs, and checks the period-divisibility conditions from step 2 by two separately implemented exact integer procedures: Tarjan SCCs with modular edge-potential constraints, and Kosaraju SCCs with gcds of spanning-depth edge discrepancies. They agree for every rule, with 32 and 8 survivors respectively. Direct independent enumeration of entire cyclic state maps also gives 42 bijective quadratic rules for \(N=9\), 8 for \(N=10\), and 32 for \(N=15\), consistent with (but not used in place of) the universal SCC certification.

The exact coefficient masks for the 32 universal odd-ring rules are
\[
\begin{gathered}
74,75,76,77,162,163,168,169,1030,1031,1034,1035,\\
1044,1045,1048,1049,8204,8205,8212,8213,8232,8233,8240,8241,\\
16394,16395,16418,16419,32792,32793,32808,32809.
\end{gathered}
\]
The eight masks for all \(N\equiv2\pmod4\) are \(162,163,168,169,16394,16395,16418,16419\). Each mask is recognized by the verifier, which rejects any extra or missing mask. Direct truth-table substitution identifies these exactly with the four stated arithmetic-progression placements of the eight ECA rules, with the eight twice-odd survivors using only the spread-two progression.

**4. Independent conceptual verification of the positive class.** Nobe and Yura (2004) prove that all eight ECA rules in \(\mathcal R\) are bijective on odd cyclic rings; the eight-rule classification is prior knowledge. Any spatial shift in the three input arguments preserves bijectivity. On an odd ring, the change of spatial coordinate \(i\mapsto2i\) permutes sites, so applying any of those ECA rules at \((i-2,i,i+2)\) is a spatially relabeled copy of an odd-ring ECA rule. When \(N\equiv2\pmod4\), even- and odd-indexed sites form two independent cycles under steps of two, each of odd length \(N/2\), giving two disjoint copies of the known bijective ECA dynamics. Hence all displayed rules have the asserted property. Step 3 proves there are no others.

## Verification
Compile and execute the accompanying standard C11 file using `cc -std=c11 -O2 -Wall -Wextra -pedantic verify.c -o verify && ./verify`. Expected output:

`VERIFY_OK: 65472 exact-degree-two rules; odd=32; 2mod4=8; finite counts n9=42 n10=8 n15=32; two independent graph methods agree.`

The code builds each local truth table from the monomial mask rather than relying on precomputed truth tables. Both SCC methods construct their own SCC decomposition. The direct cyclic-state test uses an independent evaluator of the five-neighbor rule. This is exhaustive finite-state computation combined with a proved reduction from arbitrary cyclic sizes to SCC periods, not finite-length extrapolation. All integer operations are exact; the verification uses no external datasets or proprietary libraries.

## Relationship to prior work
Houqiao Fu, *Finite-ring obstructions for quadratic binary radius-two cellular automata* (first publicly posted September 28, 2026; arXiv:2609.35921), studies precisely this five-input degree-two family and proves noninjectivity on all rings of size divisible by four from size eight upward. That result does not determine which rules are bijective on every odd or every twice-odd ring; this theorem addresses the complementary infinite congruence families. Only the source abstract, not its full manuscript, was accessible for the priority comparison.

Nobe and Yura (2004) already give the eight odd-ring reversible elementary rules and a de Bruijn-graph approach. Their established three-neighbor classification provides the positive examples here, but not the necessity of their generating all universal odd-ring and twice-odd-ring reversible five-input quadratic rules. Bhattacharjee and Das (2019) develop finite-cell reversibility and reachability methods and discuss the familiar elementary examples. Haugland and Omland (2026) classify **proper liftings**, meaning invertible maps for all sufficiently large ring lengths, and report the absence of degree-two proper liftings through diameter seven; their all-length property is strictly different from odd-ring or twice-odd-ring invertibility, and does not imply the classification here.

## Limitations
The result is conditional on exact quadratic algebraic normal form, binary states, synchronous spatially uniform local rules and cyclic boundary conditions. In particular, it is not a census of higher-degree five-site functions, asynchronous networks, open-boundary systems or all possible ring-length subsets. The exhaustive finite certificate can be independently replayed, but has not received independent scientific audit. The full text of the motivating September 2026 paper was not accessible for comparison and may contain additional results bearing on priority; the novelty assessment is consequently provisional. Older results on elementary automata and graph-period algorithms are explicitly acknowledged.

## References
- H. Fu, *Finite-ring obstructions for quadratic binary radius-two cellular automata*, arXiv:2609.35921, initial public version dated September 28, 2026, https://arxiv.org/abs/2609.35921.
- A. Nobe and F. Yura, *On reversibility of cellular automata with periodic boundary conditions*, Journal of Physics A 37 (2004), 5789–5804, DOI:10.1088/0305-4470/37/22/006.
- K. Bhattacharjee and S. Das, *On Finite 1-Dimensional Cellular Automata: Reversibility and Semi-reversibility*, arXiv:1903.06011 (2019), https://arxiv.org/abs/1903.06011.
- J. K. Haugland and T. Omland, *New classes of reversible cellular automata*, Designs, Codes and Cryptography 94 (2026), article 131, DOI:10.1007/s10623-026-01869-z.
