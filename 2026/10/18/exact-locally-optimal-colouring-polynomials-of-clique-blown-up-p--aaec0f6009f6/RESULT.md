# Exact locally-optimal colouring polynomials of clique-blown-up paths and cycles

## Finding

Let \(q\ge1\) and \(s\ge2\) be integers. A *locally-optimal \(q\)-colouring* of a graph is an assignment from \(q\) named colours in which the colour of **each** vertex occurs strictly more often in its open neighbourhood than **every other individual colour**. Let \(L_G(q)\) count these colourings. A *strict gridlock colouring* is a locally-optimal colouring that is not constant; on the graphs here its count is \(L_G(q)-q\).

For a graph \(H\), write \(H[K_s]\) for the graph obtained by replacing each vertex with a clique of size \(s\), and replacing each edge with all edges between the corresponding cliques. The following statements hold.

**Clique-fibre reduction.** For every finite simple \(H\), all locally-optimal colourings of \(H[K_s]\) are monochromatic on each replacement clique. They correspond bijectively to colourings \(c:V(H)\to[q]\) satisfying the *weak plurality* condition
\[
|\{u\in N_H(v):c(u)=c(v)\}|\ \ge\ |\{u\in N_H(v):c(u)=d\}|
\quad\text{for every }v\in V(H)\text{ and }d\in[q].
\]
This count is independent of \(s\), for every integer \(s\ge2\).

**Exact path and cycle formulas.** For \(n\ge2\),
\[
\boxed{L_{P_n[K_s]}(q)=\sum_{r=1}^{\lfloor n/2\rfloor}
\binom{n-r-1}{r-1}\,q(q-1)^{r-1}.}
\]
For the single-vertex path \(P_1\), \(L_{P_1[K_s]}(q)=q\). For every \(n\ge3\),
\[
\boxed{L_{C_n[K_s]}(q)=q+\sum_{r=2}^{\lfloor n/2\rfloor}
\frac nr\binom{n-r-1}{r-1}
\left((q-1)^r+(-1)^r(q-1)\right).}
\]
An empty sum is zero. In particular, the degree in \(q\) is \(\lfloor n/2\rfloor\) for paths of order \(n\ge2\) and cycles of order \(n\ge3\). The leading coefficient for paths is \(1\) when \(n\) is even and \(\lfloor n/2\rfloor\) when \(n\ge3\) is odd. For cycles, it is \(2\) when \(n\ge4\) is even, \(n\) when \(n\ge5\) is odd, and \(1\) for \(C_3\).

If \(H\) has maximum degree at most two, it is a disjoint union of paths and cycles. Multiplying the displayed polynomials across components therefore gives \(L_{H[K_s]}(q)\) for **every** such \(H\). In particular, the entire strict-gridlock polynomial is explicit for this family at unbounded graph degree.

## Assumptions and scope

All graphs are finite, simple, undirected. The integers \(q\ge1\) and \(s\ge2\) are arbitrary, and colours are named, so exchanging two colours generally changes a counted colouring. The locally-optimal rule demands a *unique* plurality in the open neighbourhood, not merely a tie for first, and not a strict numerical majority over all other colours combined. The base path \(P_n\) has \(n\) vertices and the base cycle \(C_n\) has \(n\ge3\) vertices. There are no restrictions on the number of connected components of \(H\).

## Proof

**1. True-twin rigidity.** Suppose vertices \(x,y\) are adjacent and have identical neighbours outside \(\{x,y\}\). Let their colours be distinct, say \(a\) and \(b\). Let \(A\) and \(B\) be the numbers of vertices coloured \(a\) and \(b\) among their common external neighbours. At \(x\), the plurality rule requires \(A>B+1\), because \(y\) contributes a \(b\)-neighbour. At \(y\), it requires \(B>A+1\), because \(x\) contributes an \(a\)-neighbour. This is impossible. Thus adjacent true twins must share a colour. Every pair in a replacement clique of \(H[K_s]\) is adjacent true twins, so each such clique is monochromatic.

**2. The strict-to-weak plurality equivalence.** Let \(c(v)\) be the common colour of the replacement clique at \(v\in V(H)\). For each colour \(d\), write \(t_d(v)=|\{u\in N_H(v):c(u)=d\}|\). A vertex in the replacement clique at \(v\) sees \(s-1+s\,t_{c(v)}(v)\) neighbours of its own colour, whereas it sees \(s\,t_d(v)\) neighbours of any other colour \(d\). Since the quantities \(t_d(v)\) are integers and \(s\ge2\),
\[
s-1+s\,t_{c(v)}(v)>s\,t_d(v)
\quad\Longleftrightarrow\quad t_{c(v)}(v)\ge t_d(v).
\]
These equivalences hold simultaneously for every vertex and competing colour, establishing a bijection with weak-plurality colourings of \(H\), and showing invariance with respect to \(s\).

**3. Weak plurality on paths and cycles.** At a degree-one base vertex, its colour must equal the colour of its only neighbour. At a degree-two base vertex, if both neighbours agree, its colour must be theirs; if they disagree, its colour must equal one of theirs. Hence at each base vertex of positive degree there must be a same-coloured neighbour. On a path with at least two vertices, this means every maximal monochromatic run has length at least two. On a cycle, it means the same for every cyclic run, including wraparound. Conversely every colouring with no singleton run satisfies the weak-plurality condition. The constant colouring is always allowed.

**4. Path enumeration.** A colouring of \(P_n\) with exactly \(r\) maximal monochromatic runs has an ordered composition of \(n\) into \(r\) parts, each at least two, and \(q(q-1)^{r-1}\) successive colour assignments. Subtracting two from every part and distributing the remaining vertices gives \(\binom{n-r-1}{r-1}\) compositions for \(n\ge2\). Summing for \(1\le r\le\lfloor n/2\rfloor\) gives the path expression. The isolated base vertex \(P_1\) yields \(K_s\), which has exactly \(q\) constant locally-optimal colourings.

**5. Cycle enumeration.** A nonconstant cyclic colouring has \(r\ge2\) maximal monochromatic runs, all of length at least two, with \(r\le\lfloor n/2\rfloor\). Marking one of the \(r\) run starts and its vertex location, then choosing the ordered run lengths, counts \(n\binom{n-r-1}{r-1}\) marked configurations. Each unmarked cyclic run partition is counted \(r\) times, so the number of partitions is \(\frac nr\binom{n-r-1}{r-1}\), which is an integer. The \(r\) successive runs must have different colours across each boundary, including the last-to-first boundary. For \(r\ge3\), their colour assignments are the standard cycle chromatic polynomial \((q-1)^r+(-1)^r(q-1)\); for \(r=2\) the same expression equals \(q(q-1)\), the correct count of two differently coloured runs. Add the \(q\) constant colourings to obtain the cycle formula.

**6. Components and leading terms.** Neighbourhood constraints are componentwise, so counts multiply over the connected components of \(H[K_s]\). The largest permissible run number is \(\lfloor n/2\rfloor\), and its coefficient is positive. For even paths the only longest-run composition has all run lengths two; for odd paths there are \(\lfloor n/2\rfloor\) possible positions of the unique run of length three. For cycles, the analogous run partitions number two when \(n\) is even and \(n\) when \(n\ge5\) is odd. The claimed degrees and leading coefficients follow from the monicity of the proper cyclic run-colouring factor.

## Verification

The accompanying `verify.py` builds the labelled graph from its adjacency relation, enumerates **every** assignment of named colours in each finite test case, and independently tests the unique-neighbourhood-plurality predicate vertex by vertex. It then compares the resulting integer with the binomial formulas. The complete run checked 34 parameter cases and 1,969,502 vertex colourings, including base paths of orders one through eight, base cycles of orders three through eight, clique sizes two and three, and palettes of two and three colours. All 34 exact comparisons passed. Run `python3 verify.py` to reproduce these finite checks. The general statements are proved above independently of the finite computation.

## Relationship to prior work

Jones and Winkeler introduced locally-optimal and strict-gridlock colouring and gave a general recurrence and a partition expansion in *Counting Strict Gridlock on Graphs* (arXiv:2603.18289v1, 2026). Their Theorems 1 and 15 establish general polynomiality and give a universal partition sum. Their Section 4 and Appendix A analyze particular five-clique networks with sparse, differently arranged inter-clique edges; these are **not** the full-join clique blowups \(P_n[K_s]\) or \(C_n[K_s]\). The new result here is the explicit true-twin reduction and complete closed evaluation on the full maximum-degree-two base family, including the surprising invariance under clique size.

The standard lexicographic-product colouring literature also treats nonrepetitive, proper, and other types of colourings; these use predicates different from strict neighbourhood plurality and do not imply this counting theorem. No stronger covering formula was located in the searched literature; absence of a search result does not establish bibliographic priority.

## Limitations

The closed binomial formulas apply to uniform replacement cliques of size at least two, and to base graphs with maximum degree at most two. The general true-twin reduction applies to arbitrary base graphs but does not itself provide a closed enumerator for those bases. Nonuniform clique sizes lead instead to weighted neighbourhood comparisons, and are not counted by the displayed formulas. Proof correctness is subject to independent review; the finite tests do not independently verify the infinite claims, and bibliographic priority is not certified.

## References

- Matthew I. Jones and Zachary Winkeler, *Counting Strict Gridlock on Graphs*, arXiv:2603.18289v1, publicly posted 2026-03-18. https://arxiv.org/abs/2603.18289
- B. Keszegh et al., *Nonrepetitive colorings of lexicographic product of graphs*, arXiv:1210.5607. Cited only as background on a different colouring objective. https://arxiv.org/abs/1210.5607
