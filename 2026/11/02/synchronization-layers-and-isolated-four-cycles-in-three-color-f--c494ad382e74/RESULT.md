# Synchronization layers and isolated four-cycles in three-color firefly dynamics on complete bipartite graphs

## Finding

Consider the standard synchronous three-color inhibitory firefly cellular automaton on the **labelled** complete bipartite graph \(K_{a,b}\), for arbitrary integers \(a,b\ge2\). Define \(T\in\{0,1,\ldots,6,\infty\}\) to be the first update at which *every vertex has the same color*, or \(\infty\) if no such update exists. Put
\[
x=2^a-2,\qquad y=2^b-2,\qquad u=3^a-3\cdot2^a+3,\qquad v=3^b-3\cdot2^b+3.
\]
The exact number of initially labelled colorings with each first synchronization time is

| \(T\) | Exact number of initial colorings |
|---|---|
| \(0\) | \(3\) |
| \(1\) | \(2+x+y+xy\) |
| \(2\) | \(2+x+y+3xy+xv+uy+uv\) |
| \(3\) | \(2+x+y+xy\) |
| \(4\) | \(x+y\) |
| \(5\) | \(3(x+y)+u+v+2xy+xv+uy\) |
| \(6\) | \(2(x+y)+u+v+xv+uy\) |
| \(\infty\) | \(u+v+2xy\) |

The eight numbers sum to \(3^{a+b}\). **Every nonsynchronizing initial configuration is already periodic:** there are exactly \(u+v\) such states of least period three, and exactly \(2xy\) such states of least period four. Apart from the single three-cycle of synchronized states, there are no other recurrent periods or periodic states. Thus the numbers of nonsynchronized primitive orbits are \((u+v)/3\) of least period three and \(xy/2\) of least period four.

Every synchronizing trajectory synchronizes within six updates, and six updates are necessary for some initial state for **every** \(a,b\ge2\). For independent uniformly distributed initial colors,
\[
\Pr(T=\infty)=\frac{u+v+2xy}{3^{a+b}},\qquad
\Pr(T=2)\longrightarrow1\quad\text{as }\min(a,b)\to\infty.
\]
For balanced shores \(a=b=n\to\infty\), the nonsynchronization probability obeys the sharp asymptotic
\[
\Pr(T=\infty)\sim 2\left(\frac49\right)^n.
\]

## Assumptions and scope

All vertices are distinct and labelled. Each carries exactly one state in \(\{0,1,2\}\) at each nonnegative integer time. State \(1\) is the blinking state. A vertex in state \(0\) becomes \(1\), a vertex in state \(1\) becomes \(2\), and a vertex in state \(2\) becomes \(0\) **unless** at least one of its neighbors is in state \(1\), in which case it stays in state \(2\). Every vertex updates simultaneously from the previous configuration. The two shores have no internal edges; every vertex on one shore is adjacent to every vertex on the other. No stochastic perturbation or asynchronous updating is used. \(T=\infty\) means that no fully uniform coloring is ever reached. A least-period-\(p\) orbit contains exactly \(p\) distinct states; labelled periodic states are counted individually, while primitive orbits are counted up to time-translation. The theorem asserts novelty for thick bicliques \(a,b\ge2\), not for the star specialization \(a=1\) or \(b=1\).

## Proof

**1. Exact support quotient.** For a coloring, let \(A\) and \(B\) be the nonempty sets of colors currently represented on the left and right shores. Every vertex on a given shore sees the same information concerning the presence of blinking color \(1\) on the opposite shore. Let
\[
q_0(0)=1,\quad q_0(1)=2,\quad q_0(2)=0,\qquad
q_1(0)=1,\quad q_1(1)=2,\quad q_1(2)=2.
\]
The subscript indicates whether the opposite shore contains color \(1\). Therefore the support pair evolves autonomously by
\[
\Phi(A,B)=\bigl(q_{\mathbf1_{\{1\in B\}}}(A),\;q_{\mathbf1_{\{1\in A\}}}(B)\bigr),
\]
where \(q_i(S)=\{q_i(s):s\in S\}\). This is an **exact quotient**, not a mean-field approximation: the support of a shore after applying the vertexwise map is precisely its image set. There are \(7^2=49\) ordered nonempty support pairs.

**2. Exhaustive finite transition certificate.** Encode each nonempty support \(S\subseteq\{0,1,2\}\) by its bitmask \(m(S)=\sum_{c\in S}2^c\in\{1,\ldots,7\}\). In the following table, a two-digit symbol \(ij\) denotes the ordered pair \((m(A),m(B))=(i,j)\). Iterating the two explicitly specified maps above gives this complete partition of the 49 ordered pairs, grouped by their first entry time \(\tau\) into a recurrent **support** class and by the corresponding full-coloring least period \(p\):

| \(\tau\) | \(p\) | All corresponding ordered support-mask pairs |
|---|---|---|
| \(0\) | \(3\) | 11, 22, 44, 47, 74 |
| \(0\) | \(4\) | 56, 65 |
| \(1\) | \(3\) | 24, 26, 42, 62, 66 |
| \(2\) | \(3\) | 12, 13, 21, 31, 33, 35, 37, 53, 73, 77 |
| \(3\) | \(3\) | 14, 41, 45, 54, 55 |
| \(4\) | \(3\) | 46, 64 |
| \(5\) | \(3\) | 23, 25, 27, 32, 34, 36, 43, 52, 63, 67, 72, 76 |
| \(6\) | \(3\) | 15, 16, 17, 51, 57, 61, 71, 75 |

Each row can be checked by repeated substitution into \(\Phi\); the table covers all 49 pairs without duplication. In particular the **only** recurrent support classes are (i) the three-cycle \(11\to22\to44\to11\), (ii) the fixed support pairs \(47\) and \(74\), and (iii) the two-cycle \(56\leftrightarrow65\). Every support pair outside these seven recurrent pairs enters class (i) within at most six steps. The full 49-entry reproduction table is included as `artifacts/support_pairs.csv`, and a standalone exact checker is included as `artifacts/verify.py`.

**3. Lifting support recurrence to actual recurrence.** On the three singleton support pairs, the full coloring is necessarily globally monochromatic, and the three states rotate with least period three. On \(47\), the left shore is constantly \(2\), while the right shore uses all three colors and evolves by a cyclic permutation of them, yielding least period three; \(74\) behaves symmetrically. The two-step support loop \(56\leftrightarrow65\leftrightarrow56\) induce a transposition of the two represented colors on **each** shore after two full updates. Since both colors actually occur on each shore, no such coloring can have period two, but every one returns after four updates: least period four. Thus each update along any recurrent support class acts as a bijection between the represented color sets on each shore; hence a labelled coloring is periodic as soon as its support first enters a recurrent class. Conversely, a periodic labelled coloring must have periodic support. Consequently the first periodic-entry time of every labelled coloring is exactly \(\tau\) in the table, and all nonperiodic inputs reach the synchronized three-cycle rather than an asynchronous periodic orbit. This establishes both the claimed absence of transient basins of asynchronous cycles and the universal six-update bound.

**4. Exact lifting of the 49 classes.** If a labelled shore of size \(m\) has exactly a specified \(j\)-color support, the number of assignments realizing that support is the number of surjections from its vertex set onto those \(j\) colors:
\[
U_1(m)=1,\quad U_2(m)=2^m-2,\quad U_3(m)=3^m-3\cdot2^m+3.
\]
Hence an ordered pair of specified supports of sizes \(i\) and \(j\) represents exactly \(U_i(a)U_j(b)\) labelled colorings. Weight the 49 support pairs in the table by these products. The recurrent row \(\tau=0\) contributes \(3+u+v+2xy\): exactly three synchronized states and \(u+v+2xy\) asynchronous periodic states. The other seven rows \(\tau\in\{1,\ldots,6\}\) contribute, respectively,
\[
\begin{aligned}
H_1&=2+x+y+xy,\\
H_2&=2+x+y+3xy+xv+uy+uv,\\
H_3&=2+x+y+xy,\\
H_4&=x+y,\\
H_5&=3(x+y)+u+v+2xy+xv+uy,\\
H_6&=2(x+y)+u+v+xv+uy.
\end{aligned}
\]
As every transient support orbit enters synchronized support class (i), \(H_t\) is exactly the number first synchronizing at time \(t\) for \(t\ge1\). The three monochromatic states yield the \(T=0\) row. Algebraically the total is
\[
3+\sum_{t=1}^6 H_t+(u+v+2xy)=(3+3x+u)(3+3y+v)=3^{a+b}.
\]
The orbit counts follow by dividing periodic **state** counts by their proven least periods. Since \(a,b\ge2\), we have \(x,y\ge2\), so \(H_6>0\): the six-step cutoff is attained for every allowed parameter pair.

**5. Limiting probabilities.** An initial configuration whose two shores both represent all three colors belongs to support pair \(77\), which enters synchronization exactly at time two. Its probability is \(U_3(a)U_3(b)/3^{a+b}\), tending to one when \(\min(a,b)\to\infty\), establishing \(\Pr(T=2)\to1\). The exact nonsynchronization probability is the \(T=\infty\) count divided by \(3^{a+b}\). For \(a=b=n\), the term \(2(2^n-2)^2\) dominates \(2(3^n-3\cdot2^n+3)\), giving \(\Pr(T=\infty)\sim2(4/9)^n\).

## Verification

The included standalone Python script `artifacts/verify.py` is executable with `python3 artifacts/verify.py` using only the standard library. It reconstructs and checks every one of the 49 support states, compares the closed layer formulas against surjection-weighted support counts for 64 parameter pairs, and directly simulates **174,051 labelled initial colorings** over 25 biclique sizes to compare first periodic-entry times and least periods. The direct simulation computes the first repeated full labelled state, rather than trusting a support label. In particular the direct checks include thick bicliques with both shores of size at least two; additional thin-shore checks serve as boundary controls. The recorded deterministic output in `artifacts/verification_output.txt` terminates with `FIREFLY_BICLIQUE_EXACT_VERIFY_OK`. The CSV certificate lists all support transitions' eventual classes. The mathematical proof of all sizes is the exact support reduction plus the finite, fully disclosed 49-state transition table; finite brute-force checks alone are not substituted for the infinite-family proof.

## Relationship to prior work

Hanbaek Lyu's *Synchronization of finite-state pulse-coupled oscillators* (first public arXiv version dated July 4, 2014) **defines the exact inhibitory firefly rule** and proves qualitative synchronization criteria for paths and trees, including the degree restriction. His 2016 tree paper develops further necessary-and-sufficient synchronization criteria and time bounds for trees. Neither inspected text supplies the 49-class two-shore reduction, the six-layer biclique synchronization distribution, or the exact isolated three- and four-cycle census for \(a,b\ge2\). These earlier criteria are not rebranded as discoveries here. A separate earlier exact star-only census concerns the excluded one-shore-singleton case; the thick-biclique phase diagram is not obtained by substituting parameters into the star result. General cyclic cellular automaton and Greenberg–Hastings rules on bicliques are **different transition maps**, so their recurrent-state formulas cannot be transferred without new proof. Indexed exact-orbit studies of binary parity automata likewise use linear XOR updates rather than this nonlinear inhibitor rule. This is a bounded literature comparison, not proof of historical uniqueness.

## Limitations

Only the three-color deterministic inhibitory firefly rule and thick complete bipartite graphs are covered. The formulas count labelled initial states, not color-unlabelled or graph-automorphism classes. No analogous formula for four or more colors, partial biclique edge deletions, or randomized/asynchronous updates is established. No claim is made about a new synchronization rule or general tree theorem. Relevant primary texts were checked in accessible rendered full-text form; literature indexing may miss an equivalent formulation, and no independent mathematical audit has been performed. The thin-shore star case is deliberately excluded from asserted novelty.

## References

1. Hanbaek Lyu, *Synchronization of finite-state pulse-coupled oscillators*, arXiv:1407.1103 (first public version July 4, 2014), https://arxiv.org/abs/1407.1103. Definition 1, Theorems 2–4, and concluding discussion.
2. Hanbaek Lyu, *Time complexity of Synchronization of discrete pulse-coupled oscillators on trees* (also presented under the title *Phase Transition in Firefly Cellular Automata on Finite Trees*), arXiv:1610.00837 (first public version October 4, 2016), https://arxiv.org/abs/1610.00837. Model definition and tree-specific synchronization and complexity results.
