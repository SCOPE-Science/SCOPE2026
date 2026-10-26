# Sharp five-step extinction for threshold-two excitation on wheel graphs

## Finding
For every integer \(n\ge3\), write \(W_n=K_1\vee C_n\), with one hub and a simple cyclic rim of \(n\) vertices. Let \(F_n\) be the deterministic synchronous three-state Greenberg–Hastings map with excitation threshold two, as defined below. The exact worst-case first hitting time of the all-rest state is
\[
T_n=\begin{cases}3&n=3,\\4&4\le n\le7,\\5&n\ge8.\end{cases}
\]
In particular, \(F_n^5\) sends **every** initial configuration to the all-rest state, regardless of circumference. Consequently the all-rest state is the sole recurrent state and there are no nontrivial periodic orbits.

## Assumptions and scope
The wheel has hub \(h\) and cyclically ordered rim vertices \(v_0,\ldots,v_{n-1}\), with edges \(hv_i\) and \(v_iv_{i+1\pmod n}\). No loops or multiple edges occur; \(n\ge3\). Every vertex has a state in \(\{0,1,2\}\), representing rest, excitation and refractory. Updates are simultaneous:
- \(1\mapsto2\) and \(2\mapsto0\) unconditionally;
- a vertex in state \(0\) changes to \(1\) if and only if **at least two distinct neighbours** are in state \(1\); otherwise it remains \(0\).
There is no external stimulus, no probabilistic update and no self-neighbourhood contribution. At time \(t\), let \(H_t\) be the hub state and let \(R_t\) denote the subset of excited rim vertices.

## Proof
**Two-step rim exclusion lemma.** If \(t\ge1\) and \(H_{t-1}\ne1\), then \(R_{t+1}=\varnothing\). Indeed, each rim vertex excited at time \(t\) was resting at time \(t-1\) and needed two excited neighbours. Since the hub was not excited, **both** of its rim neighbours were excited at time \(t-1\), hence are refractory at time \(t\). Thus no resting rim vertex at time \(t\) can have even one excited rim neighbour. Whether the hub at time \(t\) is excited or not, a resting rim vertex cannot meet threshold two. This proves the lemma, including the small rim \(C_3\).

**Global uniform bound.** Split according to the initial hub state.

If \(H_0=1\), then \(H_1=2\) and \(H_2=0\). Applying the lemma at \(t=2\) and \(t=3\) gives \(R_3=R_4=\varnothing\). As \(R_3=\varnothing\), the hub cannot be newly excited at time \(4\): either \(H_3=1\) and \(H_4=2\), or \(H_3=0\) and \(H_4=0\). At time \(5\) the hub is resting. Moreover, \(R_4=\varnothing\) prevents excitation of rim sites at time \(5\), while residual refractory rim sites return to rest. Hence the entire graph is at rest by time \(5\).

If \(H_0=2\), then \(H_1=0\). The lemma at \(t=1,2\) yields \(R_2=R_3=\varnothing\). Because the hub cannot be excited in two consecutive updates, and \(R_2=R_3=\varnothing\), it is resting by time \(4\). The rim is also resting by time \(4\); indeed, no excitation can occur at time \(4\) without any excited rim vertices at time \(3\), and all refractory sites have recovered.

If \(H_0=0\), the lemma at \(t=1\) yields \(R_2=\varnothing\). Without any excited rim at time \(2\), no rim site can be newly excited at time \(3\); hence \(R_3=\varnothing\). The hub at time \(2\) is either \(0,1\) or \(2\); the only potential excitation at time \(3\) would require two excited rim neighbours at time \(2\), which is impossible. Thus \(H_3\in\{0,2\}\). All vertices are therefore at rest by time \(4\). This proves \(F_n^5\equiv0\) for every \(n\ge3\).

**Exact sharp cutoff.** For \(n=3,4,5,6,7\), an exhaustive finite check of respectively \(3^4,3^5,3^6,3^7,3^8\) distinct labelled initial configurations, using the exact update rule, gives maximum hitting times \(3,4,4,4,4\). The complete reproducible enumerator and its output are provided in `verify.py` and `verify_output.txt`, and finite enumeration is used *only* for these five fixed circumferences.

For every \(n\ge8\), set the initial hub state to \(1\), all unspecified rim states to \(0\), and the rim states at positions \(0,4\) to \(1\); additionally set position \(8\) to \(1\) when \(n\ge9\). At time \(1\), positions \(1,3,5,7\) are excited, the hub is refractory, and positions \(2,6\) are resting. At time \(2\), positions \(2,6\) are excited (they each have both rim neighbours excited at time \(1\)), and the hub is resting. At time \(3\), the hub becomes excited from these two inputs. It must then be refractory at time \(4\) and resting at time \(5\), so the whole configuration is not all-rest at time \(4\). This proves sharpness at every \(n\ge8\). For \(4\le n\le7\), the enumerator also supplies actual time-four witnesses; see its exhaustive depth histograms.

## Verification
Run `python3 verify.py` with standard Python 3 in the directory containing that file. It exhausts all configurations for each \(3\le n\le8\), checks extinction by five updates, computes the complete first-hitting-time histogram, and directly checks explicit sharp witnesses for each \(4\le n\le80\). The recorded run ends `VERIFY_OK`; the universal assertion does not depend on this finite experiment, but on the exclusion lemma and the three hub cases above.

## Relationship to prior work
Fisch, Gravner and Griffeath (1991) introduce threshold-dependent Greenberg–Hastings systems and investigate periodic-wave and extinction regimes primarily on planar lattices, not the exact deterministic wheel cutoff proved here. Wu, Xu and Wang (arXiv:cond-mat/0701248v1, publicly submitted 2007-01-11) study stochastic excitation on scale-free networks, not the deterministic threshold-two wheel. A prior complete result for **threshold-one** excitation on wheels permits many primitive three-cycles, while a threshold-at-least-two result on **complete bipartite graphs** permits three- and four-cycles at sufficiently large part sizes. Neither implies universal extinction on wheels at threshold two. The different update rule and graph geometry are essential.

## Limitations
This theorem is specific to the deterministic three-state rule, distinct-neighbour threshold two, and a single-hub wheel. It does not establish the same cutoff for general graphs, extra refractory states, external stimulation or other thresholds. Novelty comparisons are bounded by inspected primary sources and indexed results; a relevant unindexed equivalent may exist. The small-size sharp cutoffs use exhaustive finite enumeration, but the circumference-uniform bound and the infinite family of time-five witnesses have mathematical proofs.

## References
- R. Fisch, J. Gravner, D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing **1** (1991), 23–39; accessible full text at https://www.stat.cmu.edu/~cshalizi/462/readings/fgg.pdf.
- A.-C. Wu, X.-J. Xu, Y.-H. Wang, *Excitable Greenberg–Hastings cellular automaton model on scale-free networks*, arXiv:cond-mat/0701248v1, submitted 2007-01-11, https://arxiv.org/abs/cond-mat/0701248.
