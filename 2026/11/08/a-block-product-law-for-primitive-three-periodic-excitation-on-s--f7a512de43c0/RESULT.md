# A block-product law for primitive three-periodic excitation on singly resonant cacti

## Finding

Let \(G\) be a finite connected simple cactus: every edge belongs to at most one simple cycle. Suppose that exactly one cycle block, denoted \(C_*\), has length divisible by three, while all other cycle blocks have lengths \(\ell_1,\ldots,\ell_s\geq 3\) not divisible by three. For synchronous threshold-one, three-state Greenberg–Hastings excitation on \(G\), the number of **labelled configurations having least temporal period three from time zero** is exactly
\[
P_3(G)=6\prod_{j=1}^{s}\left(2\left\lfloor\frac{\ell_j}{3}\right\rfloor+1\right).
\]
The empty product is one. These states form exactly \(P_3(G)/3\) distinct temporal three-cycles. The all-resting state is the unique fixed point. Moreover, if a cactus has no cycle of length divisible by three, then \(P_3(G)=0\).

In particular, the count is unchanged by attaching arbitrary trees, moving the attachment points of the nonresonant cycles, or reorganizing the rooted block tree while retaining the nonresonant cycle lengths and the uniqueness of \(C_*\). Attaching each new quadrilateral or pentagon multiplies \(P_3\) by three; attaching a heptagon or octagon multiplies it by five. For a triangle with two attached four-cycles, whether both share core vertices or are nested, \(P_3(G)=54\).

## Assumptions and scope

A cactus is a finite connected undirected loopless simple graph in which every edge is contained in at most one simple cycle. Its blocks are individual bridges and simple cycles. Cycles are **simple graph cycles**, not arbitrary closed walks. A cycle length is resonant when divisible by three. The theorem concerns the exactly-one-resonant-cycle class and separately the zero-resonant-cycle case; it makes no formula claim when two or more cycles are resonant.

A vertex state is \(0\) (resting), \(1\) (excited), or \(2\) (refractory). At each parallel update, \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) precisely when some adjacent vertex currently has state \(1\); otherwise \(0\mapsto0\). Write \(F_G\) for this map and \(P_3(G)=|\{x:F_G^3(x)=x,\ F_G(x)\ne x\}|\). Neither eventual periodicity nor attraction-basin sizes are counted.

## Proof

**1. The local criterion.** Suppose \(F_G^3(x)=x\). Looking at a single vertex through three updates, it either stays at state zero throughout or advances at every update through \(0\to1\to2\to0\); these are the only ways a state can return in three steps. If a permanently resting vertex were adjacent to a rotating vertex, it would encounter an excited neighbor in one of the three phases, contradicting its permanence. Connectivity therefore forces either the all-resting state or every vertex to advance at every time. Consequently a configuration is primitive three-periodic precisely when
\[
\tag{1}\forall v\in V(G)\quad \exists w\sim v:\quad x(w)=x(v)+1\pmod 3.
\]
Indeed, for an advancing configuration this is the needed condition when each vertex reaches state zero. Conversely, (1) ensures every zero vertex is excited, so every vertex advances; shifting all states by one preserves the same modular neighbor condition, and \(F_G^3(x)=x\). Such a configuration is not fixed.

**2. A unique cycle attracts every successor arrow.** For any coloring obeying (1), put a directed arrow \(v\to w\) whenever \(w\sim v\) and \(x(w)=x(v)+1\pmod3\). Each vertex has at least one outgoing arrow. Every directed closed walk of arrows contains a directed simple cycle, and along a directed cycle of length \(h\), colors increase by \(h\pmod3\), so \(3\mid h\). On a singly resonant cactus, every infinite successor-arrow path in the finite graph therefore eventually reaches \(C_*\).

Root the cactus block-cut tree at \(C_*\). If a vertex \(v\) has a successor-arrow neighbor \(w\) strictly in a descendant block, follow arrows starting with \(v\to w\). Any path from that descendant component to \(C_*\) must revisit \(v\). It would then make a directed closed walk wholly outside \(C_*\) with a directed cycle divisible by three, impossible. Thus **no vertex can obtain a successor-arrow from its descendant blocks**. It follows that every vertex of \(C_*\) is supported on \(C_*\); for every other cycle block, all its nonparent vertices must be supported within that cycle; and for a bridge block whose far endpoint is \(u\) and whose parent endpoint is \(v\), support of \(u\) forces \(x(u)=x(v)-1\pmod3\). Conversely these local support conditions make (1) hold globally. All choices in different blocks are independent once their parent articulation color is fixed.

**3. The resonant cycle.** Every vertex on \(C_*\) needs a successor neighbor among its two cycle neighbors. Give a cyclic traversal edge increments \(d_i=x(v_i)-x(v_{i-1})\in\{-1,0,1\}\), interpreted modulo three. The support condition at \(v_i\) is \(d_i=-1\) or \(d_{i+1}=1\). If any increment is not \(-1\), the following increment must be \(+1\); iterating this implication around the entire cycle makes every increment \(+1\). If none differs from \(-1\), every increment is \(-1\). These increments close only if the cycle length is divisible by three. Each orientation has three possible initial phases, giving six core colorings.

**4. A rooted noncore cycle.** Consider a cycle block of length \(\ell\ge3\) with a fixed parent articulation vertex \(v_0\). List the remaining cycle vertices \(v_1,\ldots,v_{\ell-1}\) in cyclic order. The support rule at \(v_i\), for \(1\le i\le\ell-1\), is \(d_i=-1\) or \(d_{i+1}=1\), where the increments also satisfy \(\sum_{i=1}^{\ell}d_i\equiv0\pmod3\). Hence an allowable increment word must be one of
\[
(-1)^a(+1)^{\ell-a}\quad (0\le a\le\ell),
\qquad (-1)^a\,0\,(+1)^{\ell-1-a}\quad (0\le a<\ell).
\]
Here superscripts in this displayed notation denote consecutive repetitions, not powers of numbers. The respective closure constraints are \(\ell-2a\equiv0\pmod3\) and \(\ell-1-2a\equiv0\pmod3\). Writing \(\ell=3k+t\), \(t\in\{0,1,2\}\), the numbers of admissible values of \(a\) in the two families are \((k+1,k)\), \((k,k+1)\), and \((k+1,k)\), respectively. Thus, independently of the fixed color of \(v_0\), exactly
\[
\tag{2} b_\ell=2\lfloor\ell/3\rfloor+1
\]
rooted extensions satisfy all nonroot support requirements. The root itself is already supported by its parent-side blocks, so no root condition is imposed here.

**5. Multiplication.** Each bridge supplies one forced extension, the unique resonant cycle supplies six complete core choices, and each nonresonant cycle supplies the independent factor (2). Multiplying gives the announced formula. If there is no resonant simple cycle, condition (1) would nevertheless provide a directed successor cycle of length divisible by three, a contradiction; the count is zero. The only fixed point is all zero, by the same connectivity argument. Every nonfixed period-three state lies on a three-element orbit, so division by three counts orbits. \(\square\)

## Verification

Run with Python 3 and no external libraries:

```bash
python3 verify_global.py
python3 verify_local.py
```

The first script independently implements the state update and exhaustively compares actual least-period-three counts, modular successor-neighbor colorings, and the theorem on ten labelled cacti: single resonant cycle, nested and nonnested nonresonant cycles, trees, and a no-resonance control. It checks 193,212 labelled configurations. The second script computes rooted-cycle counts using an independent edge-increment dynamic program for all lengths 3 through 200 and separately enumerates full vertex-color assignments for lengths 3 through 10. Both printed outputs are included for reproducibility. These finite tests corroborate but do not replace the preceding arbitrary-size proof.

## Relationship to prior work

Durrett and Griffeath's 1993 work established the context of Greenberg–Hastings excitable cellular automata and periodic waves. Gravner, Lyu, and Sivakoff's public 2016 preprint gives a general finite-graph characterization of synchronization and the asymptotic excitation rate via winding/contour integrals (Theorem 3 and its proof). These results concern long-run behavior, not the **time-zero, primitive-three periodic-state count**. In particular, initial states with nonzero asymptotic activity can have transients and do not all satisfy (1). The present count distinguishes stationary phase support on each cactus block from asymptotic activity and shows exact multiplicative invariance under changing the block tree.

## Limitations

The product expression is not asserted for graphs with two or more resonant cycles, for non-cactus graphs with overlapping cycle edges, for other numbers of excitation states, or for transient and eventual basins. The count may be independently derivable from other enumerative graph-coloring work; historical priority has not been externally certified. Numerical verification covers finite examples only, while the general conclusion follows from the block-cut argument.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first public version 1993-03-22; original text: https://arxiv.org/abs/patt-sol/9303002 ; lawful full text: https://sites.math.duke.edu/~rtd/reprints/paper79.pdf .
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first public version 2016-10-24, especially Theorem 3 and Section 4; https://arxiv.org/pdf/1610.07320 .
