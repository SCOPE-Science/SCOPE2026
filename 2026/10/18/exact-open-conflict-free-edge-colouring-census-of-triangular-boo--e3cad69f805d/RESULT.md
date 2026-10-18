# Exact open conflict-free edge-colouring census of triangular books

## Finding

Let \(T_n=K_2\vee\overline{K_n}\) be the **triangular-book graph** with two distinguished spine vertices \(u,v\), their common edge \(uv\), and \(n\) indexed page vertices \(w_1,\ldots,w_n\). Thus every page is a triangle \(uvw_i\), and the pages share exactly the spine edge. The vertex names distinguish individual edges. An **open conflict-free edge-colouring** assigns a colour to every edge so that, for every edge, at least one colour appears exactly once among its *other* incident edges (the open neighbourhood in the line graph). Properness is not required.

**Theorem.** For every integer \(n\ge3\), the open conflict-free chromatic index of \(T_n\) is exactly \(3\). With three *named* colours, including all edge assignments and keeping the vertices indexed, the number \(C_n(3)\) of such colourings is

\[
 C_n(3)=\begin{cases}
 198,&n=3,\\
 1080,&n=4,\\
 18n(2n-1),&n\ge5.
 \end{cases}
\]

For \(n\ge5\), each optimal colouring uses all three colours and differs from a constant page-pair colouring on at most two pages. More precisely, after fixing the colour of \(uv\) as \(0\) and calling the others \(1,2\), each page has an ordered spoke-colour pair \((a,b)\), where \(a\) is on \(uw_i\) and \(b\) on \(vw_i\). Every valid colouring has one of the following 18 patterns (all page indices distinct when two exceptions are listed):

| Uniform pair on ordinary pages | One exceptional pair | Two exceptional pairs (four choices) |
| --- | --- | --- |
| \((0,0)\) | \((1,2)\) or \((2,1)\) | \(\{(1,1),(2,0)\}\); \(\{(1,0),(2,2)\}\); \(\{(0,2),(1,1)\}\); \(\{(0,1),(2,2)\}\) |
| \((1,1)\) | \((1,2)\) or \((2,1)\) | \(\{(2,0),(2,2)\}\); \(\{(1,0),(2,2)\}\); \(\{(0,2),(2,2)\}\); \(\{(0,1),(2,2)\}\) |
| \((2,2)\) | \((1,2)\) or \((2,1)\) | \(\{(1,1),(2,0)\}\); \(\{(1,1),(1,0)\}\); \(\{(1,1),(0,2)\}\); \(\{(1,1),(0,1)\}\) |

For a row's single-exception entry there are \(n-1\) ordinary pages; for a double-exception entry there are \(n-2\) ordinary pages. The pair sets are unordered only as *types*: their two page positions remain distinguished by the ordered edge endpoints.

## Assumptions and scope

All graphs are finite, undirected and simple. The join symbol in \(K_2\vee\overline{K_n}\) means that both spine vertices are adjacent to all page vertices, and there are no edges between distinct page vertices. This triangular-book convention is not the quadrilateral book \(K_{1,n}\square K_2\). The open edge neighbourhood of \(e=xy\) consists of the edges incident with either endpoint other than \(e\) itself. This is **not** the closed conflict-free model and not a proper edge-colouring requirement. An edge with a nonempty open neighbourhood is satisfied precisely when that neighbourhood contains a colour of multiplicity one. The theorem concerns the fixed graph with indexed page vertices and a named palette of size exactly three; colours need not appear by definition, but the theorem forces all three for \(n\ge3\).

## Proof

**1. Local necessary-and-sufficient conditions.** Give the spine the colour \(0\). Write \((a_i,b_i)\) for the colours of the spokes \(uw_i,vw_i\). Define the nine nonnegative integers \(m_{ab}=|\{i:(a_i,b_i)=(a,b)\}|\), for \(a,b\in\{0,1,2\}\), and the side counts \(R_k=\sum_b m_{kb}\), \(S_k=\sum_a m_{ak}\). Write \([P]\) for \(1\) if statement \(P\) is true and \(0\) otherwise.

The spine is satisfied precisely when

\[
 \text{for some }k\in\{0,1,2\},\quad R_k+S_k=1.
\]

For every occupied type \((a,b)\), the spoke at \(u\) is satisfied precisely when

\[
 \text{for some }k,\quad R_k-[a=k]+[b=k]+[k=0]=1,
\]

and the spoke at \(v\) is satisfied precisely when

\[
 \text{for some }k,\quad S_k-[b=k]+[a=k]+[k=0]=1.
\]

These statements are exact: an edge's other incident edges consist of the common edge, its same-side spokes except itself, and its opposite spoke on the same page. Therefore these three tests characterize all feasible colourings, without omitted edges or assumptions of properness.

**2. Infinite-to-finite reduction.** Replace every \(m_{ab}\) by \(\widehat m_{ab}=\min\{m_{ab},3\}\). This preserves all three tests. Indeed, a colour's count in a spoke neighbourhood is its side total altered by a value between \(-1\) and \(2\), but the *negative* alteration is at most one. Once a side total reaches three, no alteration can make it equal one; clipping any component at three cannot change an equality-to-one test. For the spine, a total at least three also cannot equal one. Thus the feasible status of the original nine-vector equals that of its clipped vector in \(\{0,1,2,3\}^9\).

For clarity, the finite lemma used here is:

* Among the \(4^9=262144\) clipped vectors, exactly 18 feasible vectors have some entry equal to three. All 18 have exactly one such entry, equal to three, and one or two other nonzero entries, each equal to one; their types are precisely the 18 patterns displayed in the table.
* No feasible clipped vector with all entries at most two has coordinate sum at least five.

The standalone `VERIFY.py` computes the local tests as printed above for every one of the \(262144\) vectors and checks both conclusions against an independently hard-coded transcription of the 18 rows. This is an exhaustive *finite* lemma, not an extrapolation from bounded values of \(n\); it has only nine entries, each with four possibilities, regardless of \(n\). The relevant code has no external dependencies.

If \(n\ge5\), the clipped vector either has an entry equal to three or has unchanged sum \(n\ge5\). The second alternative is excluded by the lemma. The 18 remaining clipped patterns have one component equal to three, one or two other components equal to one, and no further components. Restoring the true total \(n\) uniquely makes the dominant component equal to \(n-1\) or \(n-2\). Conversely, each resulting count vector passes the exact local conditions because its clipping passes them. This proves the structural classification for **every** \(n\ge5\).

**3. Enumerating page positions.** With the spine's colour fixed, the table has six single-exception patterns, each giving \(n\) assignments, and twelve double-exception patterns, each giving \(n(n-1)\) assignments because the two exceptional types are different. There are three choices of the spine's named colour. Hence

\[
 C_n(3)=3\bigl(6n+12n(n-1)\bigr)=18n(2n-1),\quad n\ge5.
\]

For \(n=3,4\), finite exhaustive edge-level tests over respectively \(3^7\) and \(3^9\) assignments yield \(198\) and \(1080\), with the graph-edge open-neighbourhood predicate implemented directly rather than through the side totals. These small cases are finite assertions and are also cross-checked against the nine-type orbit enumerator in `VERIFY.py`.

**4. Exactly three colours are necessary and sufficient.** Suppose a colouring uses only two colours \(A,B\) and \(n\ge3\). The spine has \(2n\) other incident edges; to see a singleton colour, exactly one spoke has colour \(A\), while all other spokes have colour \(B\), after possibly exchanging the colour names. By symmetry let the exceptional spoke meet \(u\). Every spoke at \(v\) is \(B\). If the spine has colour \(B\), then an ordinary spoke at \(v\) sees only \(B\) on its other incident edges and is not satisfied. Thus the spine must have colour \(A\). But then any ordinary spoke at \(u\) sees exactly two \(A\)-coloured edges (the exceptional spoke and the spine) and \(n-1\ge2\) \(B\)-coloured edges. Neither colour is unique, a contradiction. One colour is clearly impossible as the spine has more than one neighbour. On the other hand, for every \(n\ge3\), colouring the spine \(0\), one page \((1,2)\), and all other pages \((0,0)\) satisfies every edge by the local tests (also directly for the small cases). Thus the minimum palette is exactly three.

## Verification

Run `python3 VERIFY.py` from the directory containing this document. The program tests the exact nine-type local predicates on all \(4^9\) clipped vectors, checks the complete 18-family classification, and separately evaluates original graph-edge neighbourhoods for every named three-colouring when \(n=3,4,5\). It also checks two-colour impossibility by direct enumeration for these sizes and compares an exact orbit count with the closed formula for \(5\le n\le12\). The expected output is recorded in `VERIFY_OUTPUT.txt`. The proof for unbounded \(n\) is the clipping reduction followed by the exact finite lemma, not the small-graph test range.

## Relationship to prior work

Kamyczura and Przybyło (January 25, 2026, arXiv:2601.17827) study open conflict-free edge-colouring systematically and give asymptotically sharp general bounds for nearly regular graphs. Their full-text definitions match the open-neighbourhood convention used here. Their results do not state this exact triangular-book census. Kamyczura and Przybyło (April 24, 2026, arXiv:2604.22357) extend asymptotically sharp bounds to general graphs and derive deterministic upper bounds via chromatic number; their discussion of simple graph classes does not contain a three-colour triangular-book enumeration. Those general upper bounds do not imply the exact named-colouring count.

Open conflict-free edge-colouring is equivalent to open-neighbourhood conflict-free vertex-colouring of the line graph, but this correspondence alone supplies no formula for this particular line-graph family. Ordinary proper, closed-neighbourhood, and strong-majority colourings are distinct problems. Searches for triangular books, books with triangles sharing a spine, line-graph formulations and three-colour exact counts found no covering source. Publication priority is not claimed established by failure to locate one.

## Limitations

The result is for the precisely defined triangular books and counts optimal colourings from a named three-colour palette; it does not give the full polynomial in arbitrary palette size. The 18-family claim for unbounded size has a transparent nine-variable reduction but relies on a small, fully specified exhaustive finite lemma, which should be rerun when reproducing the result. The bibliographic comparison cannot certify absolute priority; alternative graph names and unindexed sources remain a risk. No independent mathematical audit is represented by these computations or the present review.

## References

1. M. Kamyczura and J. Przybyło, *On asymptotically tight bounds for the open conflict-free chromatic indexes of nearly regular graphs*, arXiv:2601.17827, first posted 2026-01-25. https://arxiv.org/abs/2601.17827
2. M. Kamyczura and J. Przybyło, *Asymptotically Tight Bound for the Conflict-Free Chromatic Index*, arXiv:2604.22357, first posted 2026-04-24. https://arxiv.org/html/2604.22357v1
