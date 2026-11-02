# Exact random-majority absorption laws and the sharp universal time bound on complete bipartite networks

## Finding

**Theorem.** In synchronous, independent, unbiased-tie random-majority dynamics on every complete bipartite graph \(K_{a,b}\), \(a,b\geq1\), exactly three closed communicating classes exist: the all-blue fixed point, the all-white fixed point, and the two-state period-two orbit exchanging a uniformly blue part with a uniformly white part. Every initial coloring enters one of these classes almost surely.

Let \(i\) and \(j\) be the initial numbers of blue vertices in the parts of sizes \(a\) and \(b\). Set
\[
 h_d(k)=\begin{cases}1,&2k>d,\\1/2,&2k=d,\\0,&2k<d.\end{cases}
\]
Then the exact probabilities of eventual all-blue agreement, all-white agreement, and the period-two orbit are, respectively,
\[
 h_a(i)h_b(j),\qquad [1-h_a(i)][1-h_b(j)],\qquad
 h_a(i)[1-h_b(j)]+[1-h_a(i)]h_b(j).
\]
In particular, the limiting orientation of each bipartition class at even times is an independent fair resolution of its own initial majority tie; an initial strict local majority is retained at even times.

Write
\[
 q_d=\begin{cases}2^{-d}\binom d{d/2},&d\text{ even},\\0,&d\text{ odd},\end{cases}
 \qquad u_d=2^{1-d},\qquad \Delta=1-q_aq_b.
\]
For the first entrance time \(T\) into any of the three closed classes, the following formulas are exact. If both parts are initially monochromatic, \(\mathbb ET=0\). If neither part is initially tied but at least one is not monochromatic, \(\mathbb ET=1\). If the first part is tied and the second is not, then
\[
 \mathbb ET=X_{a,b}:=\frac{2+q_b-u_b-q_bu_a-q_aq_b}{\Delta}.
\]
If only the second part is tied, then
\[
 \mathbb ET=Y_{a,b}:=\frac{2+q_a-u_a-q_au_b-q_aq_b}{\Delta}.
\]
If both parts are tied, then
\[
 \mathbb ET=Z_{a,b}:=
 \frac{2+q_a+q_b-q_aq_b-q_au_b-q_bu_a-u_au_b}{\Delta}.
\]
These cases also have an **exact first-entrance-time distribution**, through the probability-generating equations in the proof. A sharp global expectation bound holds for all \(a,b\ge1\) and all initial colorings:
\[
 \boxed{\mathbb ET\le\frac{79}{27}.}
\]
Equality holds precisely when the part sizes are \(\{a,b\}=\{2,6\}\) and both parts start equally split between blue and white.

For independent Bernoulli-\(p\) initial colors, set
\[
 H_d(p)=\Pr\bigl(\operatorname{Bin}(d,p)>d/2\bigr)
 +\tfrac12\Pr\bigl(\operatorname{Bin}(d,p)=d/2\bigr).
\]
The three closed-class probabilities are \(H_a(p)H_b(p)\), \([1-H_a(p)][1-H_b(p)]\), and \(H_a(p)[1-H_b(p)]+[1-H_a(p)]H_b(p)\). The expected long-run time-averaged blue proportion is exactly
\[
 \frac{H_a(p)+H_b(p)}2.
\]

## Assumptions and scope

The graph \(K_{a,b}\) is finite, simple, loopless and fully occupied. Every vertex synchronously adopts the strict majority color of its entire open neighborhood. Whenever its neighborhood has equal blue and white counts, that vertex tosses an independent fair coin, independent across vertices and rounds. Initially all colors are prescribed, unless the independent Bernoulli initialization is explicitly invoked. A closed communicating class is a recurrent class of this finite Markov chain; a deterministic two-cycle counts as one such class. The stopping time \(T\) counts complete synchronous updates, and is zero for an initial state already in a closed class. No assertion about the time to *consensus* is made: two-cycle outcomes need not reach unanimity.

## Proof

### 1. The count chain and the two-step sign channel

At round \(t\), let \(I_t\in\{0,\ldots,a\}\) and \(J_t\in\{0,\ldots,b\}\) denote the two blue counts. Conditional on \((I_t,J_t)=(i,j)\), the next counts are independent. Specifically, \(I_{t+1}=a\) if \(2j>b\), \(I_{t+1}=0\) if \(2j<b\), and \(I_{t+1}\sim\operatorname{Bin}(a,1/2)\) if \(2j=b\). The rule for \(J_{t+1}\) interchanges \(a,i\) with \(b,j\).

Encode a part's count by its sign \(s_d(k)\in\{-,0,+\}\), distinguishing a strict white majority, a tie, and a strict blue majority. After two updates, the sign in the first part depends only on the sign in that same part two rounds earlier; analogously for the second part. A strict sign \(+\) or \(-\) is unchanged. For a tied sign, the two-step output is tied with probability \(q_aq_b\), and takes each strict sign with probability \((1-q_aq_b)/2\). This follows by applying the two conditional binomial update rules successively. The noises driving these two-step updates on the two parts are disjoint, since at each intervening round their fresh coin tosses occur on disjoint vertex sets. Thus the two resulting two-step sign chains are independent conditional on the initial coloring.

Since \(q_d\le1/2\) for every positive integer \(d\), a tie survives \(k\) two-step attempts with probability \((q_aq_b)^k\), which tends to zero. The ultimate even-time sign on a part therefore equals its original strict sign if it had one, and otherwise is a symmetric fair sign; the two ultimate signs are independent. Once both signs are strict, the following update makes both parts monochromatic. The process then either remains unanimously blue or white, or exchanges the two opposing monochromatic part colors forever. Conversely, those three classes have no exit, and no other state can be recurrent. The product law in the statement follows.

### 2. First-entry generating functions and expectations

Let \(F_X(z)\), \(F_Y(z)\), and \(F_Z(z)\) be the probability generating functions of \(T\) for the respective cases of a tie only in the first part, a tie only in the second part, and ties in both parts. These depend on the part sizes but not on which strict sign occupies an untied part. A fair-binomial redraw of \(d\) vertices is monochromatic with probability \(u_d\), tied with probability \(q_d\), and non-tied but non-monochromatic with probability \(1-u_d-q_d\). Conditioning on the first update, with \(0\le z\le1\), gives
\[
 F_X(z)=z\bigl[u_b+(1-u_b-q_b)z+q_bF_Y(z)\bigr],
\]
\[
 F_Y(z)=z\bigl[u_a+(1-u_a-q_a)z+q_aF_X(z)\bigr],
\]
\[
 \begin{aligned}
 F_Z(z)=z\bigl[&u_au_b+\bigl((1-q_a)(1-q_b)-u_au_b\bigr)z\\
 &+q_a(1-q_b)F_X(z)+(1-q_a)q_bF_Y(z)+q_aq_bF_Z(z)\bigr].
 \end{aligned}
\]
For example, in the first equation the untied second part makes the first part monochromatic in one update. The second part independently becomes monochromatic, a mixed strict majority, or a tie with probabilities \(u_b\), \(1-u_b-q_b\), and \(q_b\), causing respectively one update, two updates, or one update followed by the \(Y\) case. The last equation similarly enumerates all nine tie/pure/mixed combinations after two simultaneous binomial redraws.

The system has a unique analytic solution near \(z=0\), and \(q_aq_b\le1/4\) ensures its finite expectation. Differentiate at \(z=1\) (or condition directly on the next step). Writing \(X=F'_X(1)\) and analogously, the equations simplify to
\[
 X=2-u_b-q_b+q_bY,\qquad
 Y=2-u_a-q_a+q_aX,
\]
\[
 Z=1+(1-q_a)(1-q_b)-u_au_b+q_a(1-q_b)X+(1-q_a)q_bY+q_aq_bZ.
\]
Solving yields exactly \(X_{a,b}\), \(Y_{a,b}\), and \(Z_{a,b}\) displayed in the theorem. No initially tied part can already be monochromatic. If neither side is tied, the next update renders both parts monochromatic, unless both already were monochromatic at round zero. This proves every remaining case. The rational generating system also specifies all exact finite-time probabilities, not merely their means.

### 3. Sharp universal expectation bound

If at least one part size is odd, simultaneous ties are impossible. When exactly one part is tied, the other part has odd size and its tie probability is zero, so the appropriate expectation is \(2-u_d<2\). All other initial states have expectation at most one.

Now suppose both part sizes are even. Direct subtraction yields
\[
 Z-X=\frac{q_a(1-u_b)+u_b(1-u_a)}{\Delta}>0,
 \qquad
 Z-Y=\frac{q_b(1-u_a)+u_a(1-u_b)}{\Delta}>0.
\]
Thus the largest expectation for each fixed pair of even sizes occurs when both initial parts are tied.

Since the terms involving \(u_a,u_b\) decrease \(Z\), we have
\[
 Z_{a,b}\le G(q_a,q_b):=
 \frac{2+q_a+q_b-q_aq_b}{1-q_aq_b}.
\]
The function \(G\) is strictly increasing in either nonnegative argument: its partial derivative in its first argument is \((1+q_b+q_b^2)/(1-q_aq_b)^2>0\), and symmetrically for its second argument. For even sizes \(d\), the central binomial probabilities decrease strictly, since
\[
 \frac{q_{d+2}}{q_d}=\frac{d+1}{d+2}<1.
\]
After ordering the part sizes, if the smaller is at least four and the larger at least eight, then
\[
 Z_{a,b}\le G(3/8,35/128)<79/27.
\]
If the smaller size is two and the larger at least fourteen, then
\[
 Z_{a,b}\le G(1/2,429/2048)<79/27.
\]
These two inequalities leave exactly nine unordered even-size pairs. Substitution into the already proved formula for \(Z\) gives:

| Part sizes | Exact maximum first-entry expectation |
|---|---|
| \((2,2)\) | \(8/3\) |
| \((2,4)\) | \(38/13\) |
| \((2,6)\) | \(79/27\) |
| \((2,8)\) | \(638/221\) |
| \((2,10)\) | \(1279/449\) |
| \((2,12)\) | \(5119/1817\) |
| \((4,4)\) | \(32/11\) |
| \((4,6)\) | \(322/113\) |
| \((6,6)\) | \(2567/924\) |

Only \((2,6)\) attains \(79/27\). In that case the preceding strict comparisons show that equality requires a tie in *both* parts. This proves the global maximum and its equality conditions without restricting the vertex count.

### 4. Independent random initial colors

If the initial colors are independent Bernoulli-\(p\), the probability that the eventual even-time strict sign of a part of size \(d\) is blue is \(H_d(p)\), by the binomial initial count and fair resolution of a tie. The two part resolutions are independent by Step 1, proving the three product formulas. Unanimity contributes long-run blue proportion zero or one, and the period-two class has long-run time-average blue proportion exactly \(1/2\) regardless of unequal part sizes. Substituting the three outcome probabilities yields \([H_a(p)+H_b(p)]/2\).

## Verification

The standalone file `verify_bipartite_rmm.py` computes the transition probabilities of the full blue-count Markov chain independently of the three-case recurrence and checks the exact Bellman equations for expected first-entry time and all three absorption probabilities. It passed \(144\) part-size pairs \((a,b)\) with \(1\le a,b\le12\), \(7524\) transient count states, and \(18024\) exact-rational individual transitions. It also checked every finite pair left by the infinite-size bounding argument, verified the central-binomial monotonicity in the first forty even-size steps, and reproduced the unique extremal value \(79/27\). Run with `python3 verify_bipartite_rmm.py`. This is corroboration; the infinite theorem is justified by the four mathematical proof steps above rather than finite enumeration.

## Relationship to prior work

Zehmakan (2023; journal 2024) defines exactly the independently fair-tied synchronous Random Majority Model, gives general exponential stabilization-time examples, and proves cycle-specific bounds and terminal statistics. Its even-cycle Corollary 4.3 already determines terminal probabilities for Bernoulli initial colors on \(C_4=K_{2,2}\), a covered boundary case and not an originality claim here. The cited work does not present the complete-biclique all-size entry-time distribution or the sharp size-uniform rational expectation maximum. Mossel, Neeman and Tamuz (2012) and Benjamini and collaborators (2014) analyze majority dynamics with deterministic tie resolution, among other phenomena; their period-two theory and random-network results do not imply the independently fair-tied finite-size formulas stated here. Related deterministic or asynchronous complete-bipartite models are not equivalent to this synchronous independent-tie process.

## Limitations

The formulas require a fully occupied loopless complete bipartite graph, simultaneous updates, an exactly binary opinion space, and independent fair tie coins. They do not extend without further analysis to incomplete bipartite networks, unequal tie biases, asynchronous updating, or more than two opinions. The process may enter a non-consensus period-two class; therefore the bound is for recurrent-class entrance rather than consensus. Literature searches and comparisons provide a best-knowledge originality assessment, not proof of absolute priority or an independent external scientific audit.

## References

- A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1, first submitted 2023-02-14. https://arxiv.org/html/2302.06760v1
- A. N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems (2024). https://doi.org/10.1007/s10458-024-09651-y
- E. Mossel, J. Neeman and O. Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks*, arXiv:1207.0893, 2012. https://arxiv.org/abs/1207.0893
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486, 2014. https://arxiv.org/html/1405.2486v1
