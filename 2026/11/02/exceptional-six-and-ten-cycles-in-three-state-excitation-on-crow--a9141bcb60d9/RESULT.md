# Exceptional six- and ten-cycles in three-state excitation on crown graphs

## Finding
Let \(\operatorname{Cr}_n=K_{n,n}\setminus M\) be the labelled crown graph with matched pairs \((L_i,R_i)\), for every integer \(n\ge1\). Its edges are precisely \(L_iR_j\) with \(i\ne j\). Under synchronous three-state Greenberg–Hastings (GH) excitation, the eventual least periods and **sharp** maximal first-periodic-entry times are:

| Shore size | Eventual least periods | Maximal first periodic-entry time |
|---|---|---:|
| \(n=1\) | \(\{1\}\) | 2 |
| \(n=2\) | \(\{1\}\) | 3 |
| \(n=3\) | \(\{1,3,6\}\) | 5 |
| \(n=4\) | \(\{1,3,4\}\) | 5 |
| \(n=5\) | \(\{1,3,4,10\}\) | 6 |
| \(n\ge6\) | \(\{1,3,4\}\) | 6 |

Thus every trajectory on every crown graph is periodic by time six, sharply so for all \(n\ge5\). There are exactly **two** distinct primitive six-cycle orbits at \(n=3\), and exactly **24** distinct primitive ten-cycle orbits at \(n=5\); these exceptional periods occur at no other shore size. At \(n=5\), exactly 720 labelled configurations enter the ten-cycles: 240 already lie on a ten-cycle, 240 first enter after one update, and 240 first enter after two updates. At \(n=3\), the corresponding period-six basin has 300 initial configurations, distributed by first periodic-entry times \(0,1,2,3\) as \((12,84,144,60)\).

A further exact contrast with three-color cyclic cellular automata (CCA) on the **same** graph is that the 720 labelled initial configurations eventually reaching a ten-cycle on \(\operatorname{Cr}_5\) are identical for the two update rules, although all 720 are immediately periodic under CCA whereas only 240 are immediately periodic under GH. The CCA ten-cycle orbit count is 72, versus 24 under GH.

## Assumptions and scope
Each vertex has a state in \(\{0,1,2\}\): an excited vertex \(1\) becomes refractory \(2\), a refractory vertex \(2\) becomes resting \(0\), and a resting vertex \(0\) becomes \(1\) if and only if **some adjacent** vertex is currently \(1\). All updates occur simultaneously. The graph has no self-loops and excludes exactly the fixed perfect matching \(M\). Every initial vertex colouring is permitted. A primitive period is the least positive temporal return time of a recurrent colouring. First periodic-entry time means the least \(t\ge0\) at which the microscopic labelled configuration lies on its eventual cycle. Orbital counts identify temporal shifts, not vertex relabellings.

## Proof
**Paired-type finite reduction.** For a colouring, let \(c_{ab}\) count matched pairs whose left colour is \(a\) and right colour is \(b\), where \(a,b\in\{0,1,2\}\). Put \(u_{ab}=\min(2,c_{ab})\). Define \(B=\min(2,\sum_a u_{a1})\) and \(A=\min(2,\sum_b u_{1b})\). Every matched pair of type \((a,b)\) changes to \((a',b')\), where
\[
a'=\begin{cases}a+1\pmod 3,&a>0,\\\mathbf1\{B>\mathbf1\{b=1\}\},&a=0,\end{cases}
\qquad
b'=\begin{cases}b+1\pmod 3,&b>0,\\\mathbf1\{A>\mathbf1\{a=1\}\},&b=0.\end{cases}
\]
The subtraction of the inner indicator implements the missing matched edge; because that subtraction is at most one, the clipped totals suffice. Each occupied pair type has one determined image, and the next signature is computed by adding the source counts into their image coordinates and again clipping at two. Therefore the finite map on \(\{0,1,2\}^9\) is an **exact factor** for every shore size. All \(3^9=19{,}683\) signatures can be exhausted without bounding \(n\).

**Recovering real periods from clipped signatures.** Pair types never split into distinct types, so the number of occupied types never increases. Along a recurrent signature cycle this number must remain constant; hence each phase induces a bijection of its occupied types onto those of the next phase. Compose these bijections once around a signature cycle of length \(p\), obtaining a permutation \(\sigma\) of the occupied starting types. Each labelled matched pair follows the image of its own original type. Consequently the least microscopic period of a state at this recurrent signature is exactly \(p\operatorname{ord}(\sigma)\). Its first microscopic periodic-entry time equals its first entry time into a recurrent signature, since the dynamics are invertible on the occupied types thereafter. This also handles clipped coordinates representing arbitrarily many matched pairs.

**Exhaustive finite lemma and sharp cutoff.** The self-contained source file `verify_crown_gh3.py` builds the exact nine-trit transition map, finds all its functional-graph cycles, transports every occupied representative type around each cycle, and computes the permutation orders. It finds 4,394 recurrent signature cycles, with counts by (signature cycle length, representative-permutation order, microscopic period):
\[
\begin{array}{c|rrrrrrrr}
(p,\operatorname{ord}\sigma,\text{period}) &(1,1,1)&(1,3,3)&(1,4,4)&(2,2,4)&(2,3,6)&(2,5,10)&(3,1,3)&(4,1,4)\\\hline
\text{cycles}&3&24&1&6&1&1&4344&14.
\end{array}
\]
The maximum signature transient is six. Exactly ten signatures have transient six, and one explicit six-step initial signature is \((0,0,1,2,0,1,0,1,0)\) in lexicographic \((a,b)\) order. It represents five pairs, with one occupied type of clipped multiplicity two; adding any number of extra copies of that type leaves its entire signature trajectory unchanged. Thus the six-step bound is sharp for every \(n\ge5\). The direct microscopic checks provide the exact boundary maxima for \(1\le n\le4\).

**Exceptional period and orbit census.** Exactly 50 signatures lead to microscopic period six, every one having three coordinates equal to one and all other coordinates zero. Their entry-time histogram is \((2,14,24,10)\) at times \((0,1,2,3)\), so such configurations necessarily have \(n=3\). Similarly, exactly six signatures lead to microscopic period ten, each with five distinct singleton occupied types and zero otherwise; two occur at each of first entry times \(0,1,2\), requiring \(n=5\). The numbers of labelled configurations in the respective exceptional basins are consequently \(50\cdot3!=300\) and \(6\cdot5!=720\). The recurrent subsets have \(2\cdot3!=12\) and \(2\cdot5!=240\) states, so their primitive orbit counts are \(12/6=2\) and \(240/10=24\).

**Other shore sizes and the CCA comparison.** The finite enumeration produces the small-shore spectra and explicit recurrent period-three and period-four signatures. Period three can be sustained for arbitrarily large shores by taking at least two matched pairs in each of the three same-colour types \((0,0),(1,1),(2,2)\); then the matched-edge omission never prevents a resting vertex from receiving an excitation. A recurrent period-four signature with a coordinate clipped at two realizes period four for every \(n\ge5\) by padding that coordinate. The separate enumeration of \(1\le n\le6\) verifies the remaining boundary values. For the CCA comparison at \(n=5\), `verify_crown_gh3.py` independently updates all \(3^{10}=59{,}049\) labelled configurations under both rules, exhaustively finds their eventual least periods, and compares membership of their period-ten basins pointwise; the basin-indicator vectors coincide and have exactly 720 positive entries. Since this comparison is at a fixed graph size, the complete finite exhaustion is the proof, not an extrapolation.

## Verification
Run `python3 verify_crown_gh3.py` with Python 3 and the standard library. The program performs the entire nine-trit exhaustive classification, checks all exceptional-signature conditions and preperiod histograms, then independently constructs the vertex-level update maps for every labelled colouring with \(1\le n\le6\). The microscopic cross-check covers \(597{,}870\) colourings in total. It separately checks the equality of the two period-ten attraction-basin indicator arrays for the 59,049 size-five configurations. A successful execution prints `CROWN_GHM3_VERIFY_OK`.  Neither finite observations at small \(n\) alone nor an unattested log is used to prove the graph-size-uniform theorem; the exact finite quotient and its type-transport lemma supply the infinite-family reduction.

## Relationship to prior work
Greenberg and Hastings (1978) introduce the excitable-media model. Gravner, Lyu and Sivakoff (arXiv:1610.07320, first posted 2016-10-24; later published 2018) characterize synchronization and long-run excitation activity for three-color GH and CCA on arbitrary graphs (Theorem 3). That stronger **graph-domain** theorem constrains activity but does not supply the present crown-specific sharp transient and primitive-orbit/basin populations. Earlier results for full complete bipartite and multipartite graphs do not apply unchanged because they include the deleted matched edges.

A previous exact classification of **three-color CCA**, a different update rule on the same crown family, gives 20 primitive six-cycle orbits at \(n=3\), 72 primitive ten-cycle orbits at \(n=5\), and a four-step uniform transient bound. The GH result above has **two**, **24**, and **six**, respectively. The equal period-ten basin sets at \(n=5\) therefore do not imply equal periodic-orbit or transient distributions. The current finite-factor argument uses GH transitions throughout; it is not an application of the CCA census with a renamed rule.

## Limitations
The nonstandard nine-trit lemma is verified by a short, complete computational enumeration, not by a handwritten case partition. Reproducibility requires running and inspecting the supplied source. The exact orbit counts are provided for the exceptional periods six and ten, not all period-three and period-four orbits for arbitrary \(n\). No statement is made about other graph families or more colours. A complete historical full-text search cannot rule out every unindexed prior enumeration; independent mathematical validation has not been performed.

## References
1. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM Journal on Applied Mathematics **34** (1978), 515–523, DOI: 10.1137/0134040.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, arXiv:1610.07320 (first publicly posted 2016-10-24), later *Annals of Applied Probability* **28** (2018), 3324–3357, DOI: 10.1214/17-AAP1350.
3. *An isolated period-ten resonance in three-color cyclic dynamics on crown graphs*, exact finite-census research record, opaque identifier `3b418a05-b72a-4944-8cc5-8186ef8d8030` (comparison concerns the distinct CCA rule).
