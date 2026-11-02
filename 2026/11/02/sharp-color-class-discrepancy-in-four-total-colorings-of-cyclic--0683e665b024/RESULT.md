# Sharp color-class discrepancy in four-total colorings of cyclic prisms

## Finding

Let \(G_m=C_m\square K_2\) be the simple circular ladder with \(m\ge3\) rungs. A proper four-total coloring assigns one of four named colors to each vertex and edge, giving distinct colors to every pair of adjacent or incident elements. If \(c_j\) is the number of vertices **and** edges of color \(j\), define its discrepancy by
\[
\Delta(c)=\max_{j\in\{0,1,2,3\}}c_j-\min_{j\in\{0,1,2,3\}}c_j.
\]

**Theorem.** Write \(m=3k+r\), where \(k\ge1\) and \(0\le r\le2\). There is no proper four-total coloring when \(m=5\). For every other \(m\ge3\), the exact maximum discrepancy is
\[
\boxed{\max_c\Delta(c)=k-r=\left\lfloor\frac m3\right\rfloor-(m\bmod3).}
\]
In particular, a non-equitable four-total coloring of \(G_m\) exists exactly for \(m\in\{6,9,10\}\cup\{12,13,14,\ldots\}\). For \(m=3\), \(4\), \(7\), \(8\), or \(11\), every four-total coloring is equitable. A four-total coloring of \(G_5\) does not exist.

## Assumptions and scope

All graphs are finite, simple and undirected. The Cartesian product \(C_m\square K_2\) has top vertices \(u_i\), bottom vertices \(v_i\), edges \(u_iu_{i+1}\), \(v_iv_{i+1}\), and \(u_iv_i\), with indices modulo \(m\). Its order is \(2m\), its size is \(3m\), and every vertex has degree three. The four colors are named \(0,1,2,3\), although permuting their names does not change discrepancy. A four-total coloring need not use all four colors by convention, but at each cubic vertex it necessarily uses all four on that vertex and its incident edges. Equitability means discrepancy at most one.

## Proof

**A universal bound.** Fix a four-total coloring. For a color \(j\), let \(s_j\) and \(e_j\) be its numbers of vertices and edges. Since the vertex and its three incident edges exhaust the four colors, counting appearances of color \(j\) at all vertices yields
\[
s_j+2e_j=2m,\qquad c_j=s_j+e_j=m+\frac{s_j}{2}.
\]
Thus every \(s_j\) is even. The vertices of color \(j\) form an independent set \(S_j\); the edges of color \(j\) form a perfect matching of the induced graph \(G_m-S_j\).

An independent set meets each rung in at most one vertex. Write a one on a rung if it meets \(S_j\), and a zero otherwise. **Three consecutive ones are impossible.** Indeed, independence forces the selected vertices on three consecutive rungs to alternate between rows. The unselected vertex on the middle rung then has all three of its neighbors in \(S_j\), so is isolated in \(G_m-S_j\), contradicting the perfect matching.

There are \(m\) cyclic windows of three successive rungs, and each contains at most two ones. Counting each occupied rung three times gives \(3s_j\le2m\). Since \(s_j\) is even,
\[
s_j\le 2\left\lfloor\frac m3\right\rfloor=2k.
\]
The four vertex color classes partition the \(2m\) vertices, so \(\sum_j s_j=2m=6k+2r\). Hence every \(s_j\ge2r\), since the other three classes have size at most \(2k\). Therefore
\[
\Delta(c)=\frac{\max_j s_j-\min_j s_j}{2}\le k-r.
\]
For \(m=5\), this inequality gives a negative upper bound for a nonnegative quantity, proving nonexistence.

**Sharp constructions.** For each rung \(i\), encode the colors by a five-digit word \(a_i b_i r_i t_i w_i\): respectively the top vertex, bottom vertex, rung edge, forward top edge \(u_iu_{i+1}\), and forward bottom edge \(v_iv_{i+1}\). The following cyclic words are proper four-total colorings, as checked by comparing at every rung the four colors on each vertex and its incident edges and checking adjacent vertex colors:

```text
P3 = 30102 23130 02123
P4 = 30102 21310 03231 12023
P7 = 30102 23130 01213 32021 10302 23130 02123
P8 = 30102 23130 01213 30201 12320 01312 23031 12023
```

Every word begins with `30102`, and the final state of each word can be followed legally by `30102`. Consequently, concatenating these blocks yields a proper coloring of the longer cyclic prism. A direct check of adjacent vertex colors and of the four mutually different colors at each cubic vertex certifies each block and its junctions.

The vertex color class sizes for `P3`, `P4`, `P7`, and `P8` respectively are
\[
(2,0,2,2),\quad (2,2,2,2),\quad (4,2,4,4),\quad(4,4,4,4).
\]
When \(m=3k\), take \(k\) copies of `P3`. When \(m=3k+1\ge7\), take `P7` and \(k-2\) copies of `P3`. When \(m=3k+2\ge8\), take `P8` and \(k-2\) copies of `P3`. In each case the vertex sizes are exactly
\[
(s_0,s_1,s_2,s_3)=(2k,2r,2k,2k),
\]
and the total color class sizes therefore are
\[
(c_0,c_1,c_2,c_3)=(m+k,m+r,m+k,m+k).
\]
Their discrepancy is \(k-r\), meeting the universal bound. The blocks `P3` and `P4` also supply the two smallest cases. This proves the theorem.

## Verification

The standalone script `verify.py` reconstructs the original labelled prism's total-coloring constraints directly, verifies all four displayed blocks, and checks their concatenations for every \(6\le m\le90\). Independently it constructs all 96 locally admissible five-digit states, its 168 directed transitions, and performs an exact maximum-weight closed-walk enumeration for \(3\le m\le24\), obtaining the stated discrepancy and the absence of four-total colorings at \(m=5\). Run with `python3 verify.py`. These finite checks corroborate the explicit construction and small cases; the universal and infinite statements follow from the proof above.

## Relationship to prior work

The 2026 preprint by Adauto, de Figueiredo, Sasaki and Schneider disproves Stemock's equitability conjecture using the 12-vertex circular ladder and characterizes small-order color class configurations. An accessible 2022 dissertation by Adauto presents the older Chetwynd--Hilton cyclic-prism pasting constructions and explicitly observes that the resulting colorings become non-equitable as the prism grows; it also records the non-equitable 12- and 18-vertex examples. The existence of such examples, basic four-total-colorability, and the general cubic color-class/matching identity are **prior work**, not new claims here. The contribution assessed here is the *sharp maximum attainable discrepancy for every order*, with an independent no-three-occupied-rungs upper bound matching explicit constructions. The inspected accessible dissertation does not state that all-order optimal bound. The full text of the 2026 preprint was unavailable for inspection; its abstract reports only fixed small-order configurations, not this all-order extremal function. Comprehensive historical priority remains provisional.

## Limitations

The theorem concerns named-color proper four-total colorings on simple two-row cyclic prisms only; it does not classify all intermediate attainable class-size vectors or extend the sharp bound to arbitrary cubic graphs, open ladders, or more than four colors. It does not claim that the non-equitable-coloring construction or the general matching identity was first discovered here. The accessible 2022 dissertation was inspected in detail, while the full texts of the 1988 original pasting paper and 2026 preprint were not available; an equivalent extremal statement in those sources remains a historical-priority risk. This research has not undergone independent mathematical validation.

## References

1. M. Adauto, C. de Figueiredo, D. Sasaki and R. Schneider, *Order 14 is the largest order for which every 4-total coloring of every cubic graph is equitable*, arXiv:2609.05259, first posted 2026-09-04, https://arxiv.org/abs/2609.05259.
2. M. N. Adauto, *Equitable Total Coloring of Small Cubic Graphs*, master's dissertation, Federal University of Rio de Janeiro, February 2022, https://pesc.coppe.ufrj.br/uploadfile/publicacao/3032.pdf; in particular Sections 3.2 and 4.2--4.3.
3. A. G. Chetwynd and A. J. W. Hilton, *Some refinements of the total chromatic number conjecture*, Congressus Numerantium 66 (1988), 195--216, as cited in Reference 2; original full text not inspected.
4. S. Dantas et al., *On the equitable total chromatic number of cubic graphs*, Discrete Applied Mathematics 209 (2016), 84--91, DOI:10.1016/j.dam.2015.10.013; abstract and bibliographic record consulted.
