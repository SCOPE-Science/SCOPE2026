# Six vertices are the sharp onset of rewiring-promoted threshold cascades

## Finding

Fix a common strict fractional adoption threshold \(0\leq\theta<1\). On a finite simple undirected graph \(G=(V,E)\) with a nonempty proper seed set \(S\subset V\), initially only \(S\) has adopted. Under irreversible deterministic threshold dynamics, each nonadopter with a strictly greater than \(\theta\) fraction of adopted neighbors adopts, and updates repeat until stable. Write \(C_\theta(G,S)\) for the eventual adopted set.

A *single homophilic escape rewiring* chooses \(a\in S\), \(v,w\notin S\), with \(av\in E\), \(vw\notin E\), and \(v\ne w\); it replaces edge \(av\) by edge \(vw\). The initially nonadopting endpoint \(v\) thus drops an adopter tie and makes a tie to another initially nonadopting individual. The subsequent irreversible cascade occurs on the altered graph \(G'\), with seeds unchanged and no further rewiring.

**Sharp finite-size theorem.** For every *connected* initial \(G\) on at most five vertices, every permissible rewire, every nonempty proper \(S\), and every \(\theta\in[0,1)\),
\[
|C_\theta(G',S)|\leq |C_\theta(G,S)|.
\]
Six is the smallest connected graph order for which the reverse strict inequality can hold, even when both initial and rewired graphs must be trees.

Indeed, on vertices \(\{0,1,2,3,4,5\}\), take
\[
E(G)=\{02,04,05,12,13\},\qquad S=\{2,3\},
\]
and replace the edge \(21\) by \(10\). Both graphs are trees. For *every* \(\theta\in[1/3,1/2)\),
\[
C_\theta(G,S)=\{1,2,3\},\qquad C_\theta(G',S)=V.
\]
The rewire therefore doubles the final adopter count from three to six. Appending arbitrarily many leaves to the permanently adopting seed \(3\) in both graphs preserves this three-person gain, so such a pair of connected trees exists at **every** order \(n\geq6\).

## Assumptions and scope

Graphs are finite, labeled, undirected, simple, and initially connected; no degree-zero vertex occurs initially. All seeds are permanent adopters. Nonseeds with zero current neighbors never adopt under the stipulated strict-fraction rule. The rewire must remove exactly one edge from an initial adopter to a nonadopter and replace it with an absent edge between two nonadopters, preserving simplicity and the number of edges; the altered graph need not be connected for the small-order bound (a stronger scope), although the six-vertex witness is connected. Only **one** rewire occurs before the remaining cascade. The claim does not quantify over every realization of continuing stochastic adaptive rewiring.

Let \(A_0=S\) and define recursively
\[
A_{t+1}=A_t\cup\left\{u\notin A_t:\ |N_G(u)\cap A_t|>\theta\,\deg_G(u)\right\}.
\]
Then \(C_\theta(G,S)=\bigcup_{t\geq0}A_t\). Because adoption is irreversible, this union stabilizes in at most \(|V\setminus S|\) rounds. Strict inequality at a breakpoint, including equality \(\theta=k/d\), is essential.

## Proof

**A one-round obstruction.** Immediately after the allowed rewire, the original adopter \(a\) and all untouched nodes retain their status and adoption fractions, whereas \(v\) loses one adopted neighbor while keeping its degree, and \(w\) gains one initially nonadopting neighbor, increasing its degree without increasing its initial adopted-neighbor count. Therefore the first newly adopting set in the modified graph is a subset of the first newly adopting set in the original graph. A gain can arise only at a later round through the newly created susceptible–susceptible tie. This observation prevents interpreting rewiring as a direct first-round boost.

**Finite-order obstruction.** For order \(n\leq5\), consider every labeled simple graph, retaining only connected graphs; every nonempty proper seed set; and every ordered permissible triple \((a,v,w)\). If \(d\leq n-1\), whether an individual with \(k\) adopted neighbors among \(d\) neighbors qualifies changes only at \(\theta=k/d\). Thus on \([0,1]\) it suffices to evaluate every rational breakpoint
\[
\mathcal B_n=\{k/d:1\leq d\leq n-1,\ 0\leq k\leq d\}
\]
and one rational midpoint of every consecutive pair of breakpoints. All possible integer-neighbor adoption predicates, at every cascade round on either graph, are fixed within each open cell. Hence agreement with the desired inequality on this finite exact-rational test set proves agreement for **every real threshold** in \([0,1)\). Endpoints are evaluated separately, not inferred by continuity.

The accompanying complete verifier enumerates all \(2^{\binom n2}\) labeled simple graphs before connectivity filtering and all \(2^n-2\) candidate nonempty proper seed sets for each connected graph. Its exact-integer comparisons use the equivalent test \(kq>pd\) for \(\theta=p/q\); no floating-point tolerance enters. It enumerates every allowed ordered rewiring without graph-isomorphism shortcuts and checks the final adoption inequality. The exhaustive output, by order \(n=2,3,4,5\), respectively, is \(1,4,38,728\) connected labeled graphs, \(6,120,4788,283920\) (graph, seed, threshold) checks, and \(0,6,1344,212640\) admissible rewiring comparisons requiring a non-full baseline closure. Every comparison passes. The total is \(213990\) such rewire comparisons. There is no eligible rewire for \(n=1\). These counts and the exhaustive finite-loop structure provide a complete computational proof of the lower bound; they are not a statistical or partial sample.

**Six-vertex construction.** In the initial tree the two seeds \(2,3\) both neighbor \(1\), so \(1\) adopts immediately for every \(\theta<1\). Vertex \(0\) initially sees one adopter among its three neighbors. For \(\theta\geq1/3\) it therefore remains unadopted, leaving both leaves \(4,5\) unadopted. Thus the original final set is \(\{1,2,3\}\) on \([1/3,1/2)\). After rewiring \(21\) to \(10\), vertex \(1\) has just two neighbors, \(3\) (adopting) and \(0\) (not yet adopting), so it adopts for \(\theta<1/2\). Then \(0\), which now has neighbors \(1,2,4,5\), sees two adopters among four neighbors, and adopts for \(\theta<1/2\). Its leaves \(4,5\) adopt in the following round. This proves the strict difference at six vertices, including the threshold endpoint \(1/3\).

**All larger sizes.** Attach \(n-6\) new degree-one vertices to seed \(3\) in each graph, leaving all other edges and seed statuses unchanged. Every new leaf adopts after one round because \(\theta<1\). No original nonseed's neighborhood changes, so the original closures restricted to the original six vertices remain exactly as above. The initial and altered graphs remain connected trees and their closure sizes become \(n-3\) and \(n\) respectively. This completes the theorem.

## Verification

Run `python3 verify.py` with Python 3.8 or newer; only the standard library is required. It checks graph connectivity, all admissible rewires for orders two to five, and the six-vertex tree witness. The finite decision procedure also explains why no unsampled real threshold is omitted. The script asserts the desired inequality and the witness properties, prints exact coverage counts, and exits nonzero on a counterexample. Its 213,990 comparisons exclude cases where the original cascade already adopts everybody (these are safe without further calculation); all such baseline-full cases are correctly skipped.

## Relationship to prior work

Min and San Miguel (2023) introduce the coupled network-plasticity and strict-fraction threshold adoption model and report that rewiring can both suppress and, in some parameter regions, increase cascade sizes on large random networks. The present result isolates a *single permitted homophilic rewiring event* and establishes a sharp connected-network finite-size cutoff and tree witness; it does **not** claim the qualitative promotion mechanism was discovered here. The 2023 study analyzes stochastic ongoing rewiring and random graph phase diagrams, whereas this theorem is about deterministic post-intervention closure and every finite connected graph of order at most five.

Eckles, Mossel, Rahimian, and Sen (2018) analyze rewired long ties and diffusion speed in noisy or absolute-neighbor-count threshold processes on growing lattice/random network families; their results do not imply the sharp cutoff for one adopter–nonadopter tie exchanged for one nonadopter–nonadopter tie under a homogeneous **fractional** threshold. General bootstrap and linear threshold closure methods predate both works; the elementary closure algorithm is not claimed as novel.

## Limitations

The smallest-size classification concerns a single rewire executed **before** deterministic closure, rather than the stochastic process with repeated rewiring at each subsequent step. There are positive-probability executions of common randomized rewiring protocols that realize the same sequence, but no statement here compares unconditional expected cascade sizes as a function of rewiring probability. Thresholds are homogeneous, strict, and fractional; directed, weighted, heterogeneous, reversible, or noisy adoption rules are outside the theorem. The sharp lower cutoff depends on the connectedness assumption and on forbidding parallel edges/self-loops. Source-comparison searches reduce but cannot remove publication-priority uncertainty.

## References

1. B. Min and M. San Miguel, *Threshold cascade dynamics on coevolving networks*, arXiv:2305.13965v1, submitted 2023-05-23; *Entropy* **25** (2023), 929, DOI:10.3390/e25060929.
2. D. Eckles, E. Mossel, M. A. Rahimian, and S. Sen, *Long ties accelerate noisy threshold-based contagions*, arXiv:1810.03579v1, submitted 2018-10-08.
3. D. J. Watts, *A simple model of global cascades on random networks*, *Proc. Natl. Acad. Sci.* **99** (2002), 5766–5771. (Background on fractional threshold diffusion.)
