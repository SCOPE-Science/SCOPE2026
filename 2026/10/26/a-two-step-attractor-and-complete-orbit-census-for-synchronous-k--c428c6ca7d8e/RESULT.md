# A two-step attractor and complete orbit census for synchronous \(k\)-reversible dynamics on bicliques

## Finding
Let \(a,b,k\ge1\) be integers. In the synchronous \(k\)-reversible Boolean dynamics on the labelled biclique \(K_{a,b}\), **every trajectory is periodic by time two**:
\[
F^4=F^2.
\]
The bound two is sharp: it is attained on \(K_{4,4}\) for \(k=2\). Moreover, there is an exact census of every fixed state, primitive two-cycle, transient-depth class, and basin of each uniform attractor, for all parameter triples.

For \(k\le\min(a,b)\), define, for \(d\in\{a,b\}\),
\[
L_d=\sum_{j=0}^{\min(k-1,d-k)}\binom{d}{j},\quad M_d=2^d-2L_d,\quad I_d=\begin{cases}1&d\le 2k-2,\\0&d\ge2k-1.\end{cases}
\]
Here \(L_d\) counts each of the low- and high-weight classes, and \(M_d\) counts the central class. Write \(N_1\) for the number of states of least period one and \(N_2\) for the number of *states* of least period two (so the number of two-cycles is \(N_2/2\)). Then
\[
N_1=2+I_aI_bM_aM_b,\qquad N_2=2+(1-I_aI_b)M_aM_b.
\]
If \(T(x)\) is the least number of updates until the orbit of \(x\) is periodic, the exact counts \(Q_j=|\{x:T(x)=j\}|\) are
\[
Q_0=4+M_aM_b,\quad Q_2=2[(L_a-1)M_b+(L_b-1)M_a],\quad Q_1=2^{a+b}-Q_0-Q_2,
\]
and \(Q_j=0\) for \(j>2\). The attracting all-zero and all-one fixed points have equal basin cardinality
\[
B_0=B_1=L_aL_b+I_bL_aM_b+I_aM_aL_b.
\]
The orbit \((\mathbf 0_a,\mathbf 1_b)\leftrightarrow(\mathbf1_a,\mathbf0_b)\) has basin cardinality
\[
B_{\mathrm{opp}}=2L_aL_b+2(1-I_b)L_aM_b+2(1-I_a)M_aL_b.
\]
The other \(M_aM_b\) configurations are already periodic and form their own disjoint cycles: they are fixed when \(I_aI_b=1\), otherwise they form \(M_aM_b/2\) additional two-cycles.

For \(\min(a,b)<k\le\max(a,b)\), write \(s=\min(a,b)\), \(d=\max(a,b)\), and define \(L_d,M_d,I_d\) by the same expressions (now only for \(d\)). Then
\[
N_1=2L_d+I_d2^sM_d,\qquad N_2=(1-I_d)2^sM_d,\qquad Q_0=N_1+N_2,\quad Q_1=2^{a+b}-Q_0,\quad Q_2=0.
\]
If \(k>\max(a,b)\), \(F\) is the identity on all \(2^{a+b}\) states.

## Assumptions and scope
The graph is the simple labelled complete bipartite graph with two **nonempty** parts \(A\) and \(B\), of orders \(a\) and \(b\). There are no loops; updates are synchronous. A vertex changes its Boolean state if and only if at least \(k\) of its neighbours have the opposite state; equality triggers a flip. All formulas count labelled binary configurations, not vertex-permutation isomorphism classes. The entry time \(T(x)\) is the least \(t\ge0\) for which \(F^t(x)\) lies on a periodic orbit; a period-two *state* count is twice the number of period-two orbits.

## Proof
**Single-part transition lemma.** Suppose a part contains \(d\ge k\) neighbours of every vertex in the other part. If \(j\) of those \(d\) neighbours have state one, the simultaneous update of any opposite-part word \(w\) is:
\[
\Phi_j(w)=\begin{cases}
\mathbf0&0\le j\le\min(k-1,d-k),\\
\mathbf1&\max(k,d-k+1)\le j\le d,\\
w&k> d/2\text{ and }d-k<j<k,\\
\overline w&k\le d/2\text{ and }k\le j\le d-k.
\end{cases}
\]
These are respectively the **low**, **high**, and **middle** neighbour-weight classes; the cases partition all integers \(0\le j\le d\). To check the lemma, a current zero flips exactly when \(j\ge k\) and a current one flips exactly when \(d-j\ge k\). In particular, complementing a middle word stays middle; complementation exchanges low and high.

**Both parts have degree at least \(k\).** Classify the weights of the words on \(A\) and \(B\) as \(L,M,U\). The word pair transition is fully determined by the single-part lemma:

| Initial classes \((A,B)\) | First update | Subsequent dynamics |
|---|---|---|
| \((L,L)\) | \((\mathbf0,\mathbf0)\) | Fixed |
| \((U,U)\) | \((\mathbf1,\mathbf1)\) | Fixed |
| \((L,U)\) or \((U,L)\) | the opposite uniform pair | Uniform two-cycle |
| \((M,M)\) | independently retain or complement each middle word | Fixed when both middle actions retain; otherwise two-cycle |
| Exactly one middle class | the non-middle word is retained/complemented, and the middle word becomes uniform | The *second* update reaches a uniform fixed point or the uniform two-cycle |

The table proves \(F^4=F^2\) pointwise. Each low class has \(L_d\) words, each high class also has \(L_d\), and each middle class has \(M_d\). The middle transformation of the **part opposite to a degree-\(d\) middle input** is identity exactly when \(I_d=1\) and otherwise bitwise complement. In the middle-middle block this produces \(M_aM_b\) periodic configurations; all are fixed if and only if both middle inputs prescribe identity. For a nonempty word, complementation cannot fix it, so otherwise all are period two. Outside that block only two uniform fixed configurations and two uniform opposite-period-two states are periodic. This proves the \(N_1,N_2,Q_0\) formulas.

The only states with entry time **exactly two** have precisely one middle word and a nonuniform low or high word in the other part. Indeed, when the exceptional word is already the relevant uniform word, the first iterate is periodic; when it is nonuniform, the first iterate still has a nonuniform word, while the second is uniform. There are \(2(L_a-1)M_b+2(L_b-1)M_a\) such labelled states. The remaining nonperiodic states enter in one step, giving \(Q_1\). For the basin counts, low-low reaches all-zero, high-high all-one, and low-high/high-low reach the opposite uniform two-cycle. On a low-middle or middle-low pair, the second iterate is all-zero exactly when the middle action retains (the corresponding \(I_d=1\)); if it complements, it enters the opposite uniform two-cycle. The symmetric high cases reach all-one or the same uniform two-cycle. Counting the resulting disjoint classes yields \(B_0,B_1,B_{\mathrm{opp}}\). Every middle-middle orbit has no transient predecessor outside the middle-middle block, as every other initial class first maps to at least one uniform word.

**One degree below \(k\).** If \(s<k\le d\), the \(d\)-vertex part cannot change, because each of its vertices has only \(s<k\) neighbours. Its weight stays fixed, forcing the opposite word either to a constant word, to itself, or to its complement. Hence every state enters a fixed point or two-cycle in at most one update; exactly \(2L_d\) frozen-neighbour words force a uniform target and all \(M_d\) middle words give identity or complementation of each of the \(2^s\) other-part words. This proves the second set of formulas.

**Both degrees below \(k\).** If \(k>\max(a,b)\), no vertex can flip, so every state is fixed.

**Sharpness.** At \((a,b,k)=(4,4,2)\), \(L_4=5\), \(M_4=6\), and \(Q_2=2(4\cdot6+4\cdot6)=96>0\). Thus the universal bound two cannot be replaced by one.

## Verification
The bundled self-contained program `check_biclique.py` independently enumerates all labelled states for **301** parameter triples \(1\le a,b\le7\), \(1\le k\le\max(a,b)+1\). Its direct vertex-by-vertex update agrees with the stated periodic-state, exact entry-time and basin formulas and checks \(F^4=F^2\) on each enumerated state. This is a finite sanity check only; the proof above establishes the claims for every positive parameter triple. For example, \((a,b,k)=(6,6,2)\) yields \((N_1,N_2,Q_0,Q_1,Q_2)=(2,2502,2504,392,1200)\).

## Relationship to prior work
Oliveira, Barbosa and Protti proved that the eventual period of a \(k\)-reversible process on an arbitrary finite graph is at most two and gave general preperiod bounds; that result **does not imply a uniform bound of two updates** for every biclique. Their companion study addresses the computational complexity of finding predecessors, including graph-class-specific algorithms, rather than an all-size biclique orbit census. Subsequent work on dynamic colouring processes characterizes certain tree cases; a biclique with both parts of size at least two has four-cycles and is not covered by tree-only classifications. The present statement supplies the exact all-size transient, orbit and basin counts for this natural dense-graph family.

## Limitations
The result concerns **synchronous**, **uniform-threshold**, **binary** updates on **complete** bipartite graphs. It does not assert the same two-step bound for general bipartite graphs, asynchronous updates, heterogeneous thresholds or multistate processes. Literature comparison is necessarily bounded; an unindexed equivalent could exist. Finite enumeration is not used to justify claims at untested sizes.

## References
1. L. I. L. Oliveira, V. C. Barbosa and F. Protti, *An energy function and its application to the periodic behavior of k-reversible processes*, arXiv:1311.6126v1 (2013), https://arxiv.org/abs/1311.6126.
2. L. I. L. Oliveira, V. C. Barbosa and F. Protti, *The Predecessor-Existence Problem for k-Reversible Processes*, arXiv:1307.7259v1 (2013), https://arxiv.org/abs/1307.7259.
3. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580 (2022), https://arxiv.org/abs/2202.01580.
4. C. A. J. Dourado, L. D. Penso, D. Rautenbach and J. L. Szwarcfiter, *Reversible iterative graph processes*, Theoretical Computer Science (2012), https://doi.org/10.1016/j.tcs.2012.05.042 (abstract inspected; full text not available at review time).
