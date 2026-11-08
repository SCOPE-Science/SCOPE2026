# A complete absorption law for random-majority opinion dynamics on triangular books

## Finding

**Theorem.** Let \(m=2r\ge 2\) be even. Let \(B_m=K_2\vee\overline K_m\) be the *triangular book*: two adjacent hubs are each connected to the same \(m\) pairwise nonadjacent leaves. In synchronous random-majority dynamics, each vertex adopts the strict majority of its neighbors' binary opinions, and independently chooses a fair binary opinion when its neighbors tie. Write the initial state as \((u,v,k)\), where \(u,v\in\{0,1\}\) are the hub opinions and \(k\in\{0,\ldots,m\}\) is the number of opinion-one leaves.

The process almost surely enters exactly one of three terminal communicating classes: unanimous zero \(C_0\), unanimous one \(C_1\), or the deterministic two-cycle \(C_{\mathrm{osc}}\) alternating between the states with both hubs zero/all leaves one and both hubs one/all leaves zero. Put
\[
c_m=2^{-m}\binom{m}{m/2},\qquad
q_m=\frac{1+c_m}{2},\qquad d_m=2^{1-m}.
\]
If the hubs initially disagree, the probabilities of eventual entry into \((C_0,C_1,C_{\mathrm{osc}})\), respectively, are exactly
\[
\begin{cases}
(q_m,0,1-q_m),&k<r,\\
(q_m/2,q_m/2,1-q_m),&k=r,\\
(0,q_m,1-q_m),&k>r.
\end{cases}
\]
In particular, the eventual probability of **persistent oscillation** is \((1-c_m)/2\), independent of every initial leaf opinion whenever the hubs disagree.

If the hubs initially agree at opinion \(b\), the outcome is deterministic: for \(b=0\) it is \(C_0\) when \(k\le r\) and \(C_{\mathrm{osc}}\) otherwise; for \(b=1\) it is \(C_1\) when \(k\ge r\) and \(C_{\mathrm{osc}}\) otherwise.

Let \(\tau\) be the first time at which the chain enters one of these terminal classes, including time zero for an initially terminal state. For initially disagreeing hubs and \(k\ne r\),
\[
\mathbb E[z^{\tau}]=d_m z+(1-d_m)z^2.
\]
For initially disagreeing hubs and \(k=r\),
\[
\mathbb E[z^{\tau}]=\frac{(1-c_m)z}{1-c_mz}\bigl(d_m z+(1-d_m)z^2\bigr).
\]
Thus for disagreeing hubs
\[
\mathbb E\tau=2-d_m+\frac{\mathbf 1_{\{k=r\}}}{1-c_m},\qquad
\operatorname{Var}(\tau)=d_m(1-d_m)+\frac{\mathbf 1_{\{k=r\}}c_m}{(1-c_m)^2}.
\]
For initially agreeing hubs, \(\tau=0\) if \(k\in\{0,m\}\), and \(\tau=1\) otherwise.

For independently and uniformly initialized opinions at **all** vertices, the probabilities of \((C_0,C_1,C_{\mathrm{osc}})\) are \(((1+c_m)/4,(1+c_m)/4,(1-c_m)/2)\). Since \(c_m\sim\sqrt{2/(\pi m)}\), the probability of persistent two-cycle polarization approaches \(1/2\), despite every graph \(B_m\) containing triangles.

## Assumptions and scope

All graphs are finite, simple, undirected, and unlabeled except for the two distinguished hubs. The two hubs have degree \(m+1\), which is odd, while each leaf has degree two. Updates are simultaneous at integer times, and all leaf tie-breaking coins are mutually independent across vertices and times. Binary opinions are labeled zero and one. The theorem treats every deterministic initial configuration, summarized without loss by \((u,v,k)\). The exactly even number of leaves is essential to the stated formulas; the odd case is not claimed.

The three terminal classes are the two monochromatic singleton classes \(\{(0,0,0)\}\), \(\{(1,1,m)\}\), and the communicating two-state class \(\{(0,0,m),(1,1,0)\}\). Here the triple records both hub opinions and the number of one-leaves, not an ordering of leaves.

## Proof

**Step 1 (one-step transition).** If the hubs agree at \(b\in\{0,1\}\), every leaf sees two opinions \(b\) and becomes \(b\) at the next step. Each hub sees the other hub and all \(m\) leaves. Because its degree is \(m+1=2r+1\), its next opinion is one exactly when \(k+b\ge r+1\). Consequently the hubs remain equal. If their next opinion is \(b\), the next state is unanimous \(b\); otherwise the next state is one of the two alternating states of \(C_{\mathrm{osc}}\). This also proves the deterministic cases and the time-zero exceptions.

If the hubs disagree, each leaf has one neighbor of each opinion, hence independently becomes one with probability \(1/2\). The new count \(Y\) is therefore \(\operatorname{Bin}(m,1/2)\), independently of the previous leaf configuration. The hubs' outputs are both zero if \(k<r\), both one if \(k>r\), and are opposite (interchanged) if \(k=r\). These statements follow directly from the same strict-majority threshold \(r+1\), since the two hubs see counts \(k\) and \(k+1\) of opinion-one neighbors.

**Step 2 (exit and class selection).** When disagreeing hubs have \(k\ne r\), the next state has equal hubs at opinion \(b=\mathbf 1_{\{k>r\}}\) and independent \(Y\sim\operatorname{Bin}(m,1/2)\) leaves. By binomial symmetry,
\[
\mathbb P(Y<r)=\mathbb P(Y>r)=\frac{1-c_m}{2},\quad
\mathbb P(Y\le r)=\mathbb P(Y\ge r)=q_m.
\]
Applying Step 1 to the state with equal hubs gives consensus at \(b\) with probability \(q_m\), and the two-cycle with probability \(1-q_m\).

When initially disagreeing hubs have \(k=r\), they remain opposed after one update and regenerate an independent binomial leaf count. Each round continues this opposed stage with probability \(c_m\) and exits with probability \(1-c_m\). The number \(G\) of rounds until the first unequal-to-\(r\) leaf count is geometric on \(\{1,2,\ldots\}\) with parameter \(1-c_m\). At that exit, the count lies above or below \(r\) with equal conditional probability by binomial symmetry. The same class selection as in the unbalanced case applies, yielding the claimed half-and-half split of consensus colors and the unchanged oscillation probability. Since \(0<c_m<1\), exit occurs almost surely.

**Step 3 (exact entrance time).** From opposed hubs with \(k\ne r\), after one round the hubs agree at \(b\), and the new leaves have binomial count \(Y\). The state is *already* in a terminal class if and only if \(Y\in\{0,m\}\). This event has probability \(d_m=2^{1-m}\). Otherwise exactly one further update is needed by Step 1. Hence the terminal-class entrance time \(H\) has values one and two with probabilities \(d_m\) and \(1-d_m\), proving the first generating function.

For the balanced opposed state, the geometric exit time \(G\) is independent of the fresh leaf coins used after the exit. Thus \(\tau=G+H\) with independent summands. Multiplying their generating functions proves the second formula. Differentiating or using elementary geometric and Bernoulli moments gives the stated expectation and variance.

**Step 4 (unbiased initial profile).** With independent fair initialization, the two hubs disagree with probability \(1/2\); conditional on this event the oscillation probability is \((1-c_m)/2\). When both hubs start zero or both start one (each with probability \(1/4\)), oscillation occurs when the leaf count is on the opposite side of \(r\), each with probability \((1-c_m)/2\). Adding gives total probability \((1-c_m)/2\); color symmetry divides the remaining probability equally between the two consensus classes. Stirling's formula gives the asserted limit.

The transition cases exhaust every possible state, and every path reaches a listed terminal class almost surely; no additional recurrent class exists.

## Verification

Run `python verify.py` using Python 3.9 or newer. The standard-library-only checker independently constructs the exact macrostate transition matrix, solves absorbing-chain linear equations using rational Gauss–Jordan elimination, and compares all three class probabilities, the expected first entrance time, and its second moment with the theorem for every macrostate at \(m=2,4,6,8\). All 480 comparisons pass. These finite checks confirm the formulas for those cases and do not replace the all-even-size proof above.

## Relationship to prior work

Zehmakan (2023) defines synchronous RMM with independent uniform tie-breaking, proves general examples with exponential stabilization time and large recurrent components, and classifies cycle-graph recurrent behavior and final outcomes. Its published results do not give an exact absorption law for the triangular-book family. The present finding is a model-specific, explicitly solvable nonbipartite family with all initial conditions and exact hitting-time distributions. The deterministic tie-preserving majority models of Out and Zehmakan (2021) and Benjamini et al. (2016) use a different tie rule and do not imply the stochastic class-selection formula.

## Limitations

This result does not describe odd leaf counts, arbitrary book-like graph perturbations, asynchronous updates, correlated tie decisions, or other majority rules. Exact absorption formulas do not certify originality over every unpublished or unindexed source. Persistent two-cycle oscillation here is deterministic once entered; the randomness affects which terminal class is selected and when.

## References

- A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes* (2023), arXiv:2302.06760v1, first posted 2023-02-14. https://arxiv.org/html/2302.06760v1
- C. Out and A. N. Zehmakan, *Majority Vote in Social Networks: Make Random Friends or Be Stubborn to Overpower Elites* (2021), arXiv:2109.14265. https://arxiv.org/abs/2109.14265
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs* (2016), arXiv:1405.2486. https://arxiv.org/abs/1405.2486
