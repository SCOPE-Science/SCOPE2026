# One-step orbit laws and opinion amplification on leaf-dominated networks

## Finding

**Theorem (complete recurrent-class and initial-distribution law).** Let \(H=(V,E)\) be any finite simple graph with \(k=|V|\ge1\). For each \(v\in V\), attach \(t_v\) private leaves, with integer \(t_v>d_H(v)\), and denote the resulting graph by \(G\). In synchronous binary random-majority dynamics, each vertex adopts its neighbors' strict majority, independently choosing either color with probability \(1/2\) at a tie. Neither self-color nor inertia contributes to the vote.

Every initial coloring enters a closed deterministic period-one or period-two class after **at most one update**, regardless of tie outcomes. There are exactly \(2^k\) fixed states and \((4^k-2^k)/2\) distinct two-cycles, or \((4^k+2^k)/2\) recurrent classes in total. These counts are independent of all core edges and leaf multiplicities satisfying the stated dominance inequality.

For any initial coloring with each vertex blue independently with probability \(p\in[0,1]\), all individual recurrent-class probabilities have the explicit finite product form below, and the expected long-run time-average number of blue vertices is

\[
\mathbb E[\overline B]=\frac12\sum_{v\in V}(t_v+1)\bigl[p+M_{t_v+d_H(v)}(p)\bigr],
\]

where

\[
M_s(p)=\Pr\{\operatorname{Bin}(s,p)>s/2\}+\tfrac12\Pr\{\operatorname{Bin}(s,p)=s/2\}.
\]

If every core vertex has at least one core neighbor, then \(\mathbb E[\overline B]>p|V(G)|\) for \(1/2<p<1\), with the reverse strict inequality for \(0<p<1/2\). Thus, even though individual trajectories may blink forever, the *expected time-averaged* blue fraction strictly amplifies a biased independent initial majority. No almost-sure consensus claim is made.

In particular, for any \(k\ge2\), choosing \(H=P_k\) and \(t_v=d_H(v)+1\) produces a tree on exactly \(4k-2\) vertices, of maximum degree at most \(5\), with \((4^k+2^k)/2\) distinct recurrent classes and one-update entrance into some such class.

## Assumptions and scope

A color is encoded as \(0\) or \(1\). The leaves attached to core vertex \(v\) form a nonempty indexed set \(L_v\) of cardinality \(t_v\); the sets are disjoint. A state is *coherent* if all leaves in each \(L_v\) have the same color. In a coherent state write \((a,b)\) for core-color vector \(a\in\{0,1\}^k\) and common leaf-color vector \(b\in\{0,1\}^k\). The symbols \((a,b)\) are phase coordinates, not claims of independence.

For \(a\in\{0,1\}^k\), put \(c_v(a)=\sum_{u\in N_H(v)}a_u\), \(s_v=t_v+d_H(v)\), and define

\[
q_v(a,p)=\sum_{j=0}^{t_v}\binom{t_v}{j}p^j(1-p)^{t_v-j}\begin{cases}
1,&2(j+c_v(a))>s_v,\\
\tfrac12,&2(j+c_v(a))=s_v,\\
0,&2(j+c_v(a))<s_v.
\end{cases}
\]

Define the nonnegative weight

\[
w_p(a,b)=p^{\sum_v a_v}(1-p)^{k-\sum_v a_v}
\prod_{v\in V}q_v(a,p)^{b_v}\bigl(1-q_v(a,p)\bigr)^{1-b_v}.
\]

Endpoint powers are interpreted by the usual probability-product convention, with zero-power factors equal to one. The probability of the fixed class \((a,a)\) is exactly \(w_p(a,a)\). For any \(a\ne b\), the probability of the two-cycle consisting of \((a,b)\) and \((b,a)\) is exactly \(w_p(a,b)+w_p(b,a)\), with each unordered pair counted once. All formulas hold for arbitrary real \(p\in[0,1]\), including ties at core vertices.

## Proof

**Step 1 (one-update coherence).** Every pendant leaf has exactly one neighbor, its core vertex. Therefore all leaves of \(L_v\) update to that vertex's *previous* color, regardless of their own colors and all coin tosses. Consequently every one-step outcome is coherent.

**Step 2 (deterministic involution).** In a coherent state \((a,b)\), a core vertex \(v\) sees \(t_v\) leaf neighbors of color \(b_v\) and only \(d_H(v)<t_v\) other neighbors. Its unique strict neighborhood majority is therefore \(b_v\). Each attached leaf sees only the core color \(a_v\). The update sends

\[
T(a,b)=(b,a),\qquad T^2(a,b)=(a,b).
\]

There are \(4^k\) coherent states. Exactly the \(2^k\) states satisfying \(a=b\) are fixed; the remaining \(4^k-2^k\) coherent states form disjoint pairs. Since the coherent set is closed and reached after at most one step, no other recurrent states or classes exist. Every pair is realizable at time zero by a coherent starting configuration, so the count is exact rather than an upper bound. This proves the dynamical classification.

**Step 3 (exact absorption probabilities).** Under independent \(p\)-random initial coloring, the initial core vector \(a\) has mass \(p^{\sum a_v}(1-p)^{k-\sum a_v}\). Conditional on \(a\), the initial pendant colors of different \(L_v\) are independent. The new core color at \(v\) depends only on the \(t_v\) independent initial pendant colors, the fixed value \(c_v(a)\), and an independent fair coin if necessary. Hence the new core vector \(b\) has independent conditional Bernoulli coordinates of success probabilities \(q_v(a,p)\). The new leaf vector is the initial core vector \(a\), giving the time-one phase \((b,a)\). Thus its unordered eventual orbit has mass \(w_p(a,b)\). Summing the two possible phase orientations proves the fixed and two-cycle probabilities; the weights sum to one because they are the joint law of the initial and new core vectors.

**Step 4 (time-average and majority bias).** A two-cycle with phase vectors \(a,b\) has, over two successive rounds, a total of \((t_v+1)(a_v+b_v)\) blue vertex-rounds in the block containing \(v\). This is also true when the class is fixed. Consequently, for every trajectory, the asymptotic time-averaged blue count is \(\frac12\sum_v(t_v+1)(a_v+b_v)\). The original \(a_v\) has mean \(p\). The new \(b_v\) is the fair-tie majority of \(s_v\) *independent* initial Bernoulli colors (its neighbors' initial colors), so it has mean \(M_{s_v}(p)\). Linearity proves the expectation formula, without requiring independence of the different \(b_v\).

For \(r\ge1\), direct binomial conditioning gives

\[
M_{2r}(p)=M_{2r-1}(p),\qquad
M_{2r+1}(p)-M_{2r-1}(p)
=\binom{2r-1}{r-1}p^r(1-p)^r(2p-1).
\]

To verify the second identity, start with \(2r-1\) votes and add two. Only an initial count \(r-1\) (which wins after two added blue votes) or \(r\) (which loses after two added white votes) can change the strict-majority event; their probabilities differ by the displayed expression. The first identity follows by adding one vote and assigning half the mass to an even tie. Since \(M_1(p)=p\), these identities imply \(M_s(p)>p\) for every \(s\ge3\) and \(1/2<p<1\), with the opposite inequality for \(0<p<1/2\). If \(d_H(v)\ge1\) then the strict dominance assumption gives \(s_v=t_v+d_H(v)\ge3\). Summing the positive weighted gaps yields strict majority amplification.

**Step 5 (bounded-degree tree family).** For core \(P_k\), \(\sum_vd_H(v)=2(k-1)\) and choosing \(t_v=d_H(v)+1\) gives \(|V(G)|=k+2(k-1)+k=4k-2\). Internal core degrees are at most \(2d_H(v)+1\le5\); leaves have degree one. Attaching leaves to a path preserves acyclicity and connectedness, so this is a tree. Step 2 gives the asserted exponential class count for all \(k\ge2\).

## Verification

The included standalone `verification/check.py` requires only Python 3 and runs exact rational arithmetic. It independently enumerates all starting colorings for six finite instances, including a case with a fair-tie branch, checks coherent one-step entry and deterministic two-step return, computes all absorbing-orbit probabilities both by exhaustive state transitions and by the binomial product formula for \(p=1/3\) and \(p=2/3\), verifies the time-average expectation, and checks the binomial recurrences. It produces 16,412 exact checks across graph sizes up to 12 vertices. The exhaustive finite cases are **not** offered as a substitute for Steps 1–5, which quantify over every finite eligible graph and every real initial bias.

To reproduce: `python3 verification/check.py` from the directory containing the extracted package. No random seeds, external libraries, data downloads, or remote services are needed.

## Relationship to prior work

Zehmakan's 2023 analysis introduced the independent-tie Random Majority Model, studied general absorbing components and stabilization, and derived final blue-count laws specifically for cycles. The present result uses that model but imposes a different, leaf-dominated core architecture and gives a full absorbing-orbit probability distribution rather than only a cycle-graph expectation. Turau's 2022 and 2023 work characterizes deterministic synchronous majority fixed points and (pure) 2-cycles on trees. That pre-existing general tree structure is acknowledged; neither a general length-at-most-two conclusion nor the ability to count tree fixed points alone is asserted to be new here. The substantive additional assertion is the exact one-step random-tie absorbing-class law with a complete \(p\)-dependent joint probability formula and a strict expected opinion-amplification identity on an arbitrary core with private leaf clusters, including bounded-degree trees.

## Limitations

The theorem requires \(t_v>d_H(v)\) at **every** core vertex; it makes no claim for equality or leaf-sparse cores. The recurrence holds for synchronous, loopless neighborhood majority with independent fair ties, not asynchronous updates or self-inclusive majority. The signed amplification statement assumes all core degrees are positive and is in **expectation of a long-run time average**, not eventual consensus or almost-sure amplification. It is an analytic specialization to a structured graph family, and the general tree characterization in the references may already imply portions of the recurrent-state enumeration. Unindexed publications may contain an equivalent full stochastic absorbing-class formula; its priority has not been independently certified.

## References

- A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1, 14 February 2023. https://arxiv.org/html/2302.06760v1
- V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580v1, 3 February 2022. https://arxiv.org/abs/2202.01580
- V. Turau, *Counting Problems in Trees, with Applications to Fixed Points of Cellular Automata*, arXiv:2312.13769v1, 21 December 2023. https://arxiv.org/html/2312.13769v1
