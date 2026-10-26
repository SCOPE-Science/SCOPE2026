# A sharp twelve-symbol threshold for second-update image loss in elementary cellular automata

## Finding
Let \(F_r\), \(0\le r\le255\), be the standard elementary binary cellular automaton of Wolfram number \(r\), acting on \(X=\{0,1\}^{\mathbb Z}\). Let \(Y_{r,t}=F_r^t(X)\) for positive integers \(t\). The following assertions hold simultaneously for all 256 rules.

**Complete one-step stability census.** Exactly 72 rules satisfy \(Y_{r,1}=Y_{r,2}\), and hence \(Y_{r,t}=Y_{r,1}\) for every integer \(t\ge1\). The other 184 have \(Y_{r,2}\subsetneq Y_{r,1}\).

**Sharp finite-observation threshold.** For each of those 184 rules, define \(d_r\) as the least positive integer \(n\) for which some binary length-\(n\) word occurs in \(Y_{r,1}\) but not in \(Y_{r,2}\). Then \(d_r\le12\). The distribution of \(d_r\) for lengths 1 through 12 is, in order,
\[
(4,2,16,28,40,46,24,4,8,8,2,2).
\]
Exactly two rules attain \(d_r=12\): Rule 126 has the witness `011101101110`, and Rule 129 has the witness `100010010001`. Their first- and second-image languages coincide for every word length at most 11.

The accompanying `classification.csv` gives \(d_r\), a shortest witness for every shrinking rule, and finite-search data for all 256 rules.

## Assumptions and scope
The alphabet is \(\{0,1\}\), the spatial domain is the **bilateral infinite integer lattice**, and all initial configurations are permitted. Write the three input bits in the order left, centre, right. The local rule is
\[
f_r(a,b,c)=\left\lfloor\frac{r}{2^{4a+2b+c}}\right\rfloor\bmod2.
\]
An output word is *admissible at time* \(t\) if it occurs as a contiguous finite block in some \(F_r^t(x)\), \(x\in X\). The shortest-difference length \(d_r\) refers to the image languages, not to outputs on a particular finite periodic ring, random initial state, or a specific finite-boundary convention. In the stable cases, \(d_r\) is undefined; the catalog stores zero as a machine-readable sentinel.

## Proof
**1. One- and two-step word graphs.** For \(t=1\), form a directed graph whose vertices are the four input words of length 2. Every length-3 input word \(abc\) defines an edge \(ab\to bc\) labeled \(f_r(a,b,c)\). For \(t=2\), use 16 vertices (length-4 input words). An input word \(abcde\) gives an edge \(abcd\to bcde\) with label
\[
g_r(a,b,c,d,e)=f_r\bigl(f_r(a,b,c),f_r(b,c,d),f_r(c,d,e)\bigr).
\]
For every positive integer \(n\), a binary word \(w\) of length \(n\) occurs in \(Y_{r,t}\) precisely when the corresponding graph has a path of \(n\) successive edges carrying \(w\). Indeed, the overlapping graph windows are exactly the consecutive input windows of a finite block of length \(n+2t\). Every such input block extends to a two-sided full-shift configuration. Conversely, every observed block supplies a path. This equivalence is exact for arbitrary \(n\), not a finite-experiment extrapolation.

**2. Subset transitions.** For each graph let \(V_t\) be its entire vertex set. For a state subset \(S\subseteq V_t\) and letter \(b\in\{0,1\}\), define \(T_t(S,b)\) as the union of all endpoints of edges labeled \(b\) whose initial vertices lie in \(S\). Define \(T_t(S,w)\) by composition in the letter order of \(w\). Then
\[
w\in\mathcal L(Y_{r,t})\iff T_t(V_t,w)\ne\varnothing.
\]
Moreover \(Y_{r,2}=F_r(Y_{r,1})\subseteq Y_{r,1}\). Hence any word accepted at time 2 is also accepted at time 1.

**3. Complete finite-state decision.** Start breadth-first search at the subset pair \((V_1,V_2)\), where \(|V_1|=4\) and \(|V_2|=16\). From any pair reachable by a word accepted in the first language, take the two transitions for each letter. Ignore successors whose first component is empty (they and all their extensions cannot distinguish the images). If a successor has nonempty first component and empty second component, return the word leading to it as a discrepancy. Because breadth-first search explores increasing word lengths and stores only the first occurrence of each pair, that word is of **minimum possible positive length**. If the search exhausts the finite reachable-pair graph with no discrepancy, the two languages agree for words of every length. Compactness of \(X\), continuity of \(F_r\), and shift invariance imply that both image sets are closed subshifts determined by their finite languages, so the images are then equal. Equality of first and second images implies equality at every later positive time by applying \(F_r\) again.

**4. Exact exhaustive arithmetic.** `verify.py` implements the two label functions, the graph transitions as integer bitmasks, and this complete breadth-first algorithm, independently for each of the 256 integer codes. Its complete output is `classification.csv`. The 256 rows yield 72 equality cases and the stated histogram of 184 strict cases. Every computed minimum is at most 12; the only rows with minimum 12 are 126 and 129 and they give the two displayed witnesses. The maximum number of **discovered subset pairs before the search terminates** for any rule is 252. No claim is made that the searches for rules with a discrepancy enumerate all subset pairs beyond the first discrepancy; full closure is performed whenever equality is asserted. Since each run either finds a shortest discrepancy or exhausts the reachable state space, no unexamined longer word can contradict either decision.

## Verification
Execute `python3 verify.py` in a directory containing this script; it regenerates `classification.csv` alongside the script and asserts the full 256-rule table, the 72/184 division, the 12-length histogram and both extremizers. An **independent direct input-block enumeration**, separate from the subset-graph transitions, checks all 256 rules at all output lengths 1 through 5, every reported shortest witness, and the 12-letter extremal witnesses using all length-16 initial blocks. No randomized or unbounded search is used. Successful execution prints a `VERIFY_OK` summary; the complete exact computations, rather than that printed line, provide the finite certificate.

## Relationship to prior work
Ballier's *Limit sets of stable Cellular Automata* (arXiv:1301.3790v1, 2013) studies general stable cellular automata and steady factor maps. This contextualizes stabilization, but does not provide this exhaustive elementary-rule first/second-image comparison or a sharp local discrepancy threshold.

De Oliveira, Ruivo, Costa, Miki and Trafaniuc, *Advances in the study of elementary cellular automata regular language complexity* (first online 2015), explicitly construct finite-time process graphs for elementary rules, including first- and second-step graphs for Rule 126 (their Figures 6–7). Those graphs contain applicable finite-state input data, so the individual Rule 126 discrepancy is related to published material and may be derivable from it. Their Tables 1–2 give graph complexities across the rule space, not exact language equality for all rules; their concluding section identifies further difference-set comparisons between time steps as open research directions. The present contribution is the **complete equality/difference classification**, precise least-observation distribution across all 256 rules, and its sharp global maximum. The graph methodology itself is not claimed to be new.

Related investigations of particular rules, including Rule 54, establish special-case image differences; these do not imply the full 256-rule census or its sharp longest-observation extremizers.

## Limitations
All results concern just the first versus second **spatial image** of a nearest-neighbour binary automaton. They do not classify the time of eventual stabilization for the 184 rules failing at time 1, nor do they give dynamics on every subsequent image or entropy changes. The calculation uses exact finite-state proof for this finite family and makes no claim of a uniform 12-letter threshold for wider neighborhoods or larger alphabets. Although the closest primary papers and indexed comparisons were consulted, an unpublished or unindexed earlier exhaustive table could affect historical priority. The result has no independent external mathematical audit.

## References
1. Alexis Ballier, *Limit sets of stable Cellular Automata*, arXiv:1301.3790v1 (public 2013-01-16). https://arxiv.org/abs/1301.3790
2. P. P. B. De Oliveira, E. L. P. Ruivo, W. L. Costa, F. T. Miki, and V. V. Trafaniuc, *Advances in the study of elementary cellular automata regular language complexity*, *Complexity* 21 (2016), 267–279, first public online 2015-05-06. https://doi.org/10.1002/cplx.21686
3. E. L. P. Ruivo and P. P. B. De Oliveira, *Inferring the Limit Behavior of Some Elementary Cellular Automata*, *International Journal of Bifurcation and Chaos* 27 (2017), 1730028. https://doi.org/10.1142/S0218127417300282 (abstract/preview inspected; full text was not available in the material consulted).
