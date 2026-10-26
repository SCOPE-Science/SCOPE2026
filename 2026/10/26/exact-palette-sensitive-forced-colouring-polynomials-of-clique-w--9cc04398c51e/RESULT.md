# Exact palette-sensitive forced-colouring polynomials of clique windmills

## Finding

Let \(r\geq 3\) and \(m\geq 2\) be integers, and let
\[
W_{r,m}=K_1\vee\bigl(mK_{r-1}\bigr),\qquad N=1+m(r-1).
\]
Thus \(W_{r,m}\) consists of \(m\) cliques of order \(r\) sharing just one hub. Let \(q\) be a positive integer and use \(q\) **named** available colours. An initially coloured vertex remains fixed. At each local forcing step, an uncoloured vertex whose coloured neighbours display exactly \(q-1\) distinct colours receives the unique missing colour. A partial assignment succeeds when these steps can complete a proper \(q\)-colouring. The complete domain-size enumerator is
\[
F_{r,m;q}(z)=\sum_{f\text{ succeeds}}z^{|\operatorname{dom}f|}.
\]
Put \(H_r(z)=(r-1)z^{r-2}+z^{r-1}\) and, for \(q>r\),
\[
U_{r,m}(q)=\sum_{j=0}^{q-1}(-1)^j\binom{q-1}{j}\bigl((q-1-j)_{r-1}\bigr)^m,
\]
where \((t)_s=t(t-1)\cdots(t-s+1)\) is the falling factorial (equal to zero when the nonnegative integer \(t<s\)). Then the **full all-palette formula** is
\[
\boxed{
F_{r,m;q}(z)=
\begin{cases}
0,&q<r,\\[3pt]
r((r-1)!)^m\bigl((1+z)H_r(z)^m-(r-1)z^{m(r-2)}\bigr),&q=r,\\[3pt]
q\bigl((q-1)_{r-1}\bigr)^m z^N+qU_{r,m}(q)z^{N-1},&q>r.
\end{cases}}
\]
In particular, the smallest cardinality \(s_{r,m;q}\) of a successful initial domain satisfies
\[
\boxed{
s_{r,m;q}=\begin{cases}
\text{infeasible},&q<r,\\
m(r-2),&q=r,\\
N-1,&r<q\leq N,\\
N,&q>N.
\end{cases}}
\]
For \(q=r\), the number of minimum domains **with their forced colours** is
\[
\boxed{r((r-1)!)^m\bigl((r-1)^m-(r-1)\bigr).}
\]
For \(r<q\leq N\), the number of minimum successful partial assignments is \(qU_{r,m}(q)\). The jump from \(m(r-2)\) to \(m(r-1)\) seeds when the palette grows from \(r\) to \(r+1\) is exactly \(m\): one additional initially coloured vertex is needed per blade.

The corresponding probability polynomial in Farr's independent random-assignment model is, for \(0\leq p\leq 1/q\),
\[
\boxed{\operatorname{FC}_q(W_{r,m};p)
=\sum_{k=0}^N[z^k]F_{r,m;q}(z)\,p^k(1-qp)^{N-k}.}
\]
This expression includes both endpoints by direct polynomial evaluation. It counts **local iterative forcing**, not just uniqueness of a proper extension.

## Assumptions and scope

All graphs are finite, simple and labelled. The hub and the \(m\) vertex-disjoint blades are distinguished by their actual vertices; colour names are also distinguished. A blade is the \((r-1)\)-clique formed by the non-hub vertices of one of the \(r\)-cliques. There are no edges between different blades. The results hold for all integers \(r\geq3\), \(m\geq2\), and \(q\geq1\), with no asymptotic assumptions. A successful initial assignment must be a proper partial colouring, because forcing cannot erase an initially monochromatic edge. A total proper assignment succeeds without taking any steps.

## Proof

**1. Proper completions and the chromatic boundary.** Each hub-plus-blade subgraph is a clique of size \(r\). Hence \(\chi(W_{r,m})=r\), and \(q<r\) permits no successful assignment. For \(q=r\), every proper completed colouring chooses the hub colour in \(r\) ways and uses all remaining \(r-1\) colours exactly once in each blade, independently. Thus there are
\[
r((r-1)!)^m
\]
completed proper colourings. The forcing procedure determines a unique completed colouring from every successful seed assignment: each step has a unique permitted colour. We may therefore count initial subsets separately for each completed colouring, without duplication.

**2. Chromatic-palette forcing when the hub is initially coloured.** Assume \(q=r\) and the hub is initially coloured. If two vertices of a blade are initially uncoloured, neither can be the first vertex forced in that blade: each sees the hub and at most \(r-3\) coloured blade neighbours, thus at most \(r-2\) distinct colours rather than the required \(r-1\). Forcing in other blades cannot increase its coloured neighbourhood, which lies wholly within its own blade and the hub. Hence such a blade prevents completion. Conversely, when each blade has at least \(r-2\) initially coloured vertices, any unique uncoloured vertex in a blade sees all \(r-1\) other clique colours and is forced immediately. Relative to a fixed completed colouring, a blade therefore contributes either \(r-2\) of its \(r-1\) vertices or all \(r-1\), with weight
\[
H_r(z)=(r-1)z^{r-2}+z^{r-1}.
\]
The hub-coloured contribution is \(zH_r(z)^m\).

**3. Chromatic-palette forcing when the hub is initially uncoloured.** No blade vertex can be forced before the hub: an uncoloured blade vertex has the uncoloured hub as a neighbour, and hence sees at most \(r-2\) coloured blade neighbours. Thus the first forcing step, if any, must colour the hub. To complete every blade after that step, each blade must initially contain at least \(r-2\) coloured vertices by the argument in step 2. The hub is initially forceable exactly when all \(r-1\) leaf colours appear somewhere on the coloured blades.

For a fixed completed colouring, the weighted total of blade seed choices meeting the blade lower bound is \(H_r(z)^m\). A leaf colour fails to appear precisely when every blade omits its unique vertex of that colour. Such a failure has weight \(z^{m(r-2)}\), and there are \(r-1\) mutually exclusive choices of the missing colour. (They are mutually exclusive because a single blade omits at most one vertex.) Subtracting these gives
\[
H_r(z)^m-(r-1)z^{m(r-2)}.
\]
If all leaf colours appear, the hub is forced at the first step and any remaining leaf in each blade is forced after it. Combining steps 2 and 3 and multiplying by the number of completed proper colourings proves the middle case of the formula. Its lowest nonzero coefficient is
\[
r((r-1)!)^m\bigl((r-1)^m-(r-1)\bigr)>0
\]
when \(r\geq3,m\geq2\), proving both the minimum-seed size and its multiplicity for \(q=r\).

**4. Larger palettes: only the hub can be forced.** Suppose \(q>r\). Every blade vertex has degree \(r-1<q-1\); it can never see enough distinct neighbour colours for a forcing step. Consequently every blade vertex must be coloured initially. If the hub is coloured initially too, the assignment is any proper total \(q\)-colouring. There are
\[
q\bigl((q-1)_{r-1}\bigr)^m
\]
such assignments, because the hub has \(q\) choices and each blade uses \(r-1\) distinct colours other than the hub colour.

If the hub is uncoloured initially, all \(N-1\) blade vertices are coloured, and the hub is forced exactly when they use \(q-1\) distinct colours. First choose the missing hub colour (\(q\) choices), then assign all remaining \(q-1\) named colours across the \(m\) blade cliques, injectively within each blade and **surjectively** over their union. Inclusion-exclusion on unused leaf colours gives exactly
\[
U_{r,m}(q)=\sum_{j=0}^{q-1}(-1)^j\binom{q-1}{j}\bigl((q-1-j)_{r-1}\bigr)^m.
\]
These hub-uncoloured assignments have exactly \(N-1\) seeds; together with the total assignments, this proves the last case of the polynomial.

**5. Exact palette threshold.** Each blade requires \(r-1\) distinct colours, so a surjective leaf assignment onto \(q-1\) colours is impossible if \(q-1<r-1\) or \(q-1>m(r-1)\). In the present \(q>r\) case the first obstruction is absent. Every integer number of distinct leaf colours between \(r-1\) and \(m(r-1)\) is attainable: start with one blade using \(r-1\) distinct colours, then introduce additional previously unused colours in the remaining blades, one vertex at a time, while completing each blade with other available colours. No blade repeats a colour. Therefore \(U_{r,m}(q)>0\) precisely for \(r<q\leq N\). The minimum-seed classification follows: a successful incomplete assignment has size \(N-1\) exactly in that range, while for \(q>N\) all successful assignments are total.

**6. Probability transform.** In Farr's random model, each specific initial colour has probability \(p\) and a blank has probability \(1-qp\), independently for all vertices. Every successful assignment with \(k\) seeds has weight \(p^k(1-qp)^{N-k}\). Summing by \(k\) yields the stated probability polynomial directly; no analytic continuation assumption is needed.

## Verification

The standalone stdlib-only program `verify_windmill.py` constructs the graph and enumerates every one of its \((q+1)^N\) initial states in 12 small instances. It tests properness, repeatedly applies the explicit local rule, and compares the observed count in **each seed cardinality** with a separately implemented formula. Its completed run reports `VERIFY_OK cases=12 complete_assignments=489479`.

Representative exact coefficient vectors, ordered from degree zero, are:

- \(W_{3,2}\), \(q=3\): \((0,0,24,96,60,12)\).
- \(W_{3,2}\), \(q=4\): \((0,0,0,0,96,144)\).
- \(W_{4,2}\), \(q=4\): \((0,0,0,0,864,2160,1008,144)\).
- \(W_{3,3}\), \(q=3\): \((0,0,0,144,480,432,168,24)\).

These finite checks test boundary behaviour and implementation independently, but the theorem for unbounded \(r,m,q\) follows from the structural arguments in steps 1–6, not from extrapolation.

## Relationship to prior work

G. E. Farr's *The forced colouring function of a graph* (arXiv:2609.17108v1, 15 September 2026) defines this precise iterative local forcing rule, its probability polynomial, and general identities. It gives the complete-graph formula, corresponding to the **excluded** one-blade boundary \(m=1\), but the inspected sections do not supply the multi-blade windmill formula or the palette-threshold theorem. Farr and Morgan (arXiv:2406.15746v1) introduced the polynomial framework earlier and gave general reductions; those reductions require resolving the instances and do not imply the displayed closed all-palette formula without further analysis.

The published results *Forced colourings of complete multipartite graphs at the chromatic palette size* and *Forced three-colouring polynomial of complete bipartite graphs* handle different graph families. For \(r\ge3,m\ge2\), the windmill is **not** complete multipartite: two vertices in one blade are adjacent although both are nonadjacent to a vertex in another blade, contradicting the transitivity of nonadjacency in a complete multipartite graph. Those results therefore do not specialize to this family.

The published *Zero forcing polynomial of friendship graphs* counts binary blue/white propagation under a different local rule. Even for the friendship subfamily \(r=3\), its seed-size polynomial and its minimum exponent differ from this colour-specific iterative forcing invariant. Harary, Slany and Verbitsky's older *forcing chromatic number* concerns **unique extension** of a partial chromatic colouring, not the requirement that all vertices be generated by Farr's local steps. Neither is a statement implying the displayed full coefficient polynomial.

## Limitations

The graphs are uniform clique windmills with at least two blades, and the colours are named. The theorem does not give a closed polynomial for arbitrary block graphs, mixed blade sizes, or general chordal graphs. It addresses success under exactly the local forcing rule above, not arbitrary unique extendability, ordinary zero forcing, or other propagation rules. No claim of global historical uniqueness is made; older results under other terminology may exist.

## References

1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1 (15 September 2026), https://arxiv.org/abs/2609.17108v1 .
2. G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746v1 (22 June 2024), https://arxiv.org/abs/2406.15746v1 .
3. *Forced colourings of complete multipartite graphs at the chromatic palette size*, publicly available mathematical finding, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-forced-colourings-of-complete-multipartite-graphs-at-the-chromat--ab08eebc2655 .
4. *Forced three-colouring polynomial of complete bipartite graphs*, publicly available mathematical finding, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-forced-three-colouring-polynomial-of-complete-bipartite-graphs--3fb93c858f69 .
5. *Zero forcing polynomial of friendship graphs*, publicly available mathematical finding, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-zero-forcing-polynomial-of-friendship-graphs--b77605779c1b .
6. F. Harary, W. Slany, O. Verbitsky, *On the Computational Complexity of the Forcing Chromatic Number*, arXiv:cs/0406044 (2004), https://arxiv.org/abs/cs/0406044 .
