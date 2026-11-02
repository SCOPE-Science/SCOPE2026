# Two contiguous chip-energy bands and an exact three-cycle census on connected graphs

## Finding

For every finite connected simple graph \(G=(V,E)\) with \(n=|V|\ge2\) and \(m=|E|\), the standard synchronous parallel chip-firing map admits the exact polynomial below, whose coefficient of \(z^k\) counts **primitive temporal period-three orbits**, each counted once, at conserved chip total \(k\).

For a phase assignment \(s:V\to\mathbb Z/3\mathbb Z\), put
\[
a_v(s)=|\{w\sim v:s(w)=s(v)-1\pmod3\}|,\quad
h(s)=|\{\{v,w\}\in E:s(v)=s(w)\}|.
\]
Let \([a]_z=1+z+\cdots+z^{a-1}\) for positive integral \(a\), and \([0]_z=0\). Then
\[
P_{G,3}(z)=\frac13\sum_{s:V\to\mathbb Z/3\mathbb Z}
\left(z^{m+h(s)}\prod_{v\in V}[a_v(s)]_z+
 z^{3m-n-h(s)}\prod_{v\in V}[a_v(s)]_{z^{-1}}\right).
\tag{1}
\]
The displayed Laurent-looking summands simplify to a polynomial with nonnegative integer coefficients, despite the division by three.

Let \(\mathcal A(G)=\{s:a_v(s)\ge1\text{ for all }v\}\), and, when this set is nonempty, let \(h_* =\min_{s\in\mathcal A(G)}h(s)\). Then a primitive three-cycle exists **if and only if** \(G\) contains a simple cycle whose length is divisible by three. In that case, the **exact set** of conserved chip totals supporting primitive three-cycles is the disjoint union of two complete integer intervals:
\[
\boxed{\{m+h_*,m+h_*+1,\ldots,2m-n\}\ \cup\
\{2m,2m+1,\ldots,3m-n-h_*\}.}\tag{2}
\]
Every integer in each interval is attained, and none in the gap. The count at the two inner endpoints \(2m-n\) and \(2m\) is \(|\mathcal A(G)|/3\); the count at the outer endpoints \(m+h_*\) and \(3m-n-h_*\) is \(|\{s\in\mathcal A(G):h(s)=h_*\}|/3\). Moreover,
\[P_{G,3}(z)=z^{4m-n}P_{G,3}(z^{-1}).\tag{3}\]

For every connected unicyclic simple graph with \(n=m\) and unique cycle length \(\ell\), the polynomial is exactly \(2z^n+2z^{2n}\) when \(3\mid\ell\), and zero otherwise. For the labelled clique \(K_4\), it is \(12(z^7+z^8+z^{12}+z^{13})\). In the labelled book graph \(B_r=K_2\vee\overline K_r\), consisting of two adjacent core vertices and \(r\ge1\) shared degree-two neighbors, the *low-energy* orbit polynomial is
\[
P^{(1)}_{B_r,3}(z)=2z^{2r+1}\frac{(1+z)^r-(2z)^r}{1-z}
=2\sum_{k=0}^{r-1}\!\left(\sum_{j=0}^{k}\binom rj\right)z^{2r+1+k}.
\tag{4}
\]
Its high-energy counterpart is obtained by \(z^k\mapsto z^{7r+2-k}\). Thus its previously known unweighted three-cycle total \(r2^{r+1}\) is refined by *binomial cumulative coefficients at every conserved energy*. The unicyclic formula is a consequence, rather than an assertion that cyclic period-three existence is new.

## Assumptions and scope

States are functions \(x:V\to\mathbb Z_{\ge0}\). Write \(d_v\) for vertex degree and \(f_v(x)=\mathbf1_{x_v\ge d_v}\). A *parallel* update is
\[
F(x)_v=x_v-d_v f_v(x)+\sum_{w\sim v}f_w(x).
\]
Every vertex fires at most once per update, simultaneously. An orbit of *primitive period three* has three distinct states \(x,F(x),F^2(x)\) and satisfies \(F^3(x)=x\). The orbit-counting polynomial records conserved \(\sum_vx_v\) and identifies temporal rotations only: graph automorphisms do not identify distinct orbits. There are no sinks, loops, multiple edges, dissipation, or random steps. The theorem does not classify non-period-three dynamics.

## Proof

**1. Uniform activity.** Consider any period-three state with firing indicator \(f_{v,t}\in\{0,1\}\) for times \(t=0,1,2\) modulo three. Summing three update equations gives
\[
0=-d_v q_v+\sum_{w\sim v}q_w,
\qquad q_v=\sum_{t=0}^2 f_{v,t}.
\]
Thus \(q\) is harmonic on connected \(G\), hence constant. If \(q=0\) or \(q=3\), all vertices always wait or always fire, respectively; these give fixed states, not primitive three-cycles. Therefore primitive three-cycles have either \(q=1\) at every vertex or \(q=2\) at every vertex.

**2. Exact states with activity one-third.** Let \(q=1\), so each vertex fires at a unique phase \(s(v)\in\mathbb Z/3\mathbb Z\). Let \(b_{v,j}=|\{w\sim v:s(w)=j\}|\), and \(a_v=b_{v,s(v)-1}\). At vertex \(v\), let \(d_v+u_v\) be the chip count at its firing time. At its two subsequent update times, the counts are, in order,
\[
 u_v+b_{v,s(v)},\qquad
 u_v+b_{v,s(v)}+b_{v,s(v)+1}=d_v+u_v-a_v.
\]
The first and second counts must be strictly below \(d_v\), which is equivalent to \(0\le u_v<a_v\); the second bound implies the first. Conversely, for every phase assignment with \(a_v\ge1\) at all vertices and every integral choice \(0\le u_v<a_v\), the three displayed counts are nonnegative and satisfy exactly their stated firing inequalities. Updating them reproduces their values cyclically, so this construction is necessary and sufficient and produces no fixed state.

At time zero the chip count at vertex \(v\) is
\[
x_v=\begin{cases}
d_v+u_v,&s(v)=0,\\
d_v-a_v+u_v,&s(v)=1,\\
b_{v,2}+u_v,&s(v)=2.
\end{cases}
\]
Summing the constant parts edge-by-edge, a same-phase edge contributes two chips and a different-phase edge contributes one. The total is therefore exactly \(m+h(s)+\sum_vu_v\). Each primitive orbit contributes three distinct phase-relabelled states, so the generating polynomial for activity one-third is
\[
P^{(1)}_{G,3}(z)=\frac13\sum_s z^{m+h(s)}\prod_v[a_v(s)]_z.
\tag{5}
\]
No two distinct assignments with their \(u_v\) choices produce the same state: a state's deterministic three firing patterns recover \(s\), and the firing-time height recovers each \(u_v\).

**3. Activity two-thirds.** Every vertex of a non-fixed periodic state has at least one waiting step. It then has at most \(d_v-1\) chips at that step and at most \(2d_v-1\) at any other step (one update gains at most \(d_v\)). The involution
\[J(x)_v=2d_v-1-x_v\]
therefore maps such periodic states to nonnegative states and swaps firing with waiting. Its update intertwining identity is \(F(Jx)=J(Fx)\), because \(\sum_{w\sim v}1=d_v\). It maps activity one-third bijectively to activity two-thirds. Since \(\sum_v(2d_v-1)=4m-n\), a state of chip total \(k\) maps to one of total \(4m-n-k\). Reversing the exponents in (5) yields the second term of (1) and (3).

**4. Every energy in exactly two bands.** For any phase assignment with positive \(a_v\), every edge with different endpoint phases contributes exactly one to \(\sum_va_v\), while every same-phase edge contributes zero. Thus
\[\sum_va_v=m-h(s).\]
For this phase assignment, the independent choice intervals for \(u_v\) realize **every** integer from \(\sum_vu_v=0\) through \(\sum_v(a_v-1)=m-h(s)-n\). Their chip-total interval is consequently \([m+h(s),2m-n]\), independent of the phase assignment at its upper end. The phase assignments attaining \(h_*\) supply the full first interval of (2); other assignments contribute only subsets of it. Complementation supplies the full second interval, starting at \(2m\). Their separation is strict since \(n\ge2\). The endpoint counts follow from the uniqueness of all-zero and all-maximal height choices at the respective extremal endpoints, and division by three.

**5. Graph-theoretic existence criterion.** If every vertex has a predecessor-phase neighbor, orient one such incident edge from each vertex towards its chosen predecessor. The finite functional digraph has a directed cycle. Its colors decrease by one modulo three on each edge, so this simple directed cycle has length divisible by three; the underlying simple graph contains such a cycle. Conversely, start from any simple cycle of length divisible by three, assign phases consecutively around it, and extend to a spanning forest of the remaining vertices rooted on that cycle by setting each child's phase one greater than its parent's. Every vertex then has a predecessor neighbor, so the preceding construction gives a primitive three-cycle.

**6. Exact book-graph energy law.** For the two core vertices of \(B_r\), positive predecessor counts force distinct phases. There are six assignments of these ordered distinct core phases. After fixing one, each degree-two neighbor may occupy either of two permitted phases; if \(b\) neighbors use the phase required by the otherwise unsupplied core predecessor, then \(1\le b\le r\), with multiplicity \(\binom rb\). The only variable height belongs to that core and ranges through \(0,\ldots,b-1\); the number of monochromatic edges is \(r-b\). Dividing the six choices by the three phase rotations gives
\[
2\sum_{b=1}^r\binom rb z^{3r+1-b}[b]_z
=\frac{2z^{3r+1}}{1-z}\left[(1+z^{-1})^r-2^r\right],
\]
which reduces to the polynomial and binomial cumulative coefficients in (4). The companion activity class follows from complementation. Summing the low- and high-energy coefficients yields \(r2^{r+1}\), consistently recovering the known unweighted book-graph count.

**7. Unicyclic rigidity.** If \(G\) is unicyclic, \(m=n\). A positive-admissibility assignment satisfies \(n\le\sum_va_v=m-h(s)\le m=n\). Thus \(h(s)=0\) and \(a_v=1\) for every vertex, leaving no height choices. Every edge is oriented by its distinct phase, and every vertex has exactly one predecessor neighbor; the directed unique cycle is the graph's underlying cycle, and it must have length divisible by three. For each of the two cycle orientations there are exactly three global phase rotations, and the phases of every branch vertex are forced by its parent. Thus each activity class has exactly two temporal orbits and a single total chip number, respectively \(n\) and \(2n\). This proves the stated unicyclic formula.

## Verification

The accompanying standalone `verification_code.py` computes the phase polynomial by convolution, independently generates all bounded microscopic chip states, tests the exact period-three return condition, and compares their orbit-count polynomials. It examines all connected labelled simple graphs on two, three and four vertices, plus all connected five-vertex graphs with at most six edges: 595 graph cases and 578,628 bounded configurations. It checks the two uninterrupted mass bands and reciprocity for every graph with a three-cycle, checks 48 unicyclic graph constructions, checks eight book-graph energy distributions, and reconstructs 1,380 additional phase-height states on complete graphs. Output: `PERIOD3_WEIGHTED_COLORING_CHECKS_PASSED`. Execute `python3 verification_code.py` using only the Python standard library. The proof above, not finite enumeration, establishes the claim for all finite connected simple graphs.

## Relationship to prior work

The uniform per-vertex firing count and chip-complement symmetry are established general features of periodic chip-firing; they are **not** presented here as new. Prisner's 1994 Lemma 6.7 gives a general constructive phase-partition method for activity \(1/p\), and Proposition 6.8 proves period realizability from cycle-length divisibility; the existence criterion above specializes and rederives that known mechanism. Jiang (2010) gives an independent general discussion of uniform activity and complement. Dall'Asta (2006) treats the one-dimensional ring and period/energy orbit structure, so the simple-cycle specialization is already in established territory. Work on periodic firing sequences and motorized trees likewise covers important aspects of the underlying local phase constraints.

The specific claim here is the **arbitrary-graph conserved-chip-total generating polynomial**, the two *gap-free* period-three energy intervals, and their exact endpoint multiplicities, not the known basic phase-partition construction. The previously available complete period-two edge-cut enumerator is a distinct statistic, with different local constraints; it does not give the period-three coefficients. An earlier book-graph computation gives the unweighted primitive three-cycle total \(r2^{r+1}\); the binomial cumulative energy distribution (4) refines, rather than repeats, that count. These relationships substantially qualify novelty and should be reviewed independently against historical literature.

## Limitations

The formula sums over all \(3^n\) phase assignments and is not claimed to be a polynomial-time algorithm. It counts primitive three-cycles only, not attraction basins, transient lengths, or all other primitive periods. The unicyclic statement is a checkable corollary and is not claimed as an independent breakthrough. The 1992 Bitar–Goles original article was available only at abstract level; its full text was not inspected. Prisner's text was examined in an accessible transcription, whose formulas have imperfect character extraction; this raises residual literature-equivalence risk. No independent mathematical audit or certification has been performed.

## References

- J. Bitar and E. Goles, *Parallel chip firing games on graphs*, Theoretical Computer Science 92 (1992), 291–300. DOI: 10.1016/0304-3975(92)90316-8. Abstract-level inspection only.
- E. Prisner, *Parallel Chip Firing on Digraphs*, Complex Systems 8 (1994), 367–383, particularly Corollary 6.6, Lemma 6.7 and Proposition 6.8.
- L. Dall'Asta, *Exact solution of the one-dimensional deterministic Fixed-Energy Sandpile*, arXiv:cond-mat/0601267 (initial public posting 2006-01-12); full five-page preprint inspected.
- T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (initial public posting 2010-03-04), especially Section 2.
- T.-Y. Jiang, Z. Scully and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786 (2012); related complete phase-sequence restrictions.
- Z. Scully, T.-Y. Jiang and Y. Zhang, *Firing Patterns in the Parallel Chip-Firing Game*, DMTCS Proc. AT (2014), DOI: 10.46298/dmtcs.2421.
