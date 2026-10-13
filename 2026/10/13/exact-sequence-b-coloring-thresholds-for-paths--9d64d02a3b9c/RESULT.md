# Exact sequence \(b\)-coloring thresholds for paths
## Finding
Let \(P_n\) be the path on \(n\ge 2\) vertices. Following Jakovac and Lang, a sequence \(b\)-coloring with \(k\) colors realizes a non-increasing sequence \((s_1,\ldots,s_k)\) when every color class \(i\) contains at least \(s_i\) color-dominating vertices (CDVs), where a vertex is a CDV when its closed neighborhood contains every color used by the coloring.

The finite sequences realized by \(P_n\) are exactly these:

1. A two-term sequence \((r,s)\), with \(r\ge s\ge1\), is realized exactly when
\[
r\le \left\lceil\frac n2\right\rceil,
\qquad
s\le \left\lfloor\frac n2\right\rfloor.
\]
2. A three-term sequence \((r,s,t)\), with \(r\ge s\ge t\ge1\), is realized exactly when
\[
n\ge N(r,s,t),
\qquad
N(r,s,t)=
\begin{cases}
3r+2,&r=s=t,\\
2r+s+1,&\text{otherwise.}
\end{cases}
\]
3. No finite sequence of any other length is realized.

Thus, except on the diagonal \(r=s=t\), the minimum path order for a three-term sequence is independent of the smallest requirement \(t\).

## Assumptions and scope
Graphs are finite, simple, and connected, and \(P_n\) has \(n\ge2\) vertices. Color names may be permuted, so for three colors the CDV counts may be sorted as \(a\ge b\ge c\) before comparison with the non-increasing requirement \((r,s,t)\). The result concerns the sequence-realizability definition of Jakovac and Lang, not only the classical \(b\)-chromatic number.

## Proof
A CDV in a coloring with \(k\) colors must have degree at least \(k-1\). Since \(P_n\) has maximum degree two, a realized finite sequence can have length at most three. A one-color proper coloring is impossible for \(n\ge2\), so only lengths two and three remain.

For two colors, the proper coloring of a connected path is its bipartition coloring, unique up to swapping colors. Every vertex sees both colors in its closed neighborhood, hence every vertex is a CDV. The two color classes have sizes \(\lceil n/2\rceil\) and \(\lfloor n/2\rfloor\), which proves the two-term criterion.

Now consider a proper three-coloring and identify the colors with \(\mathbf Z/3\mathbf Z\). Write the successive edge increments as \(\varepsilon_i\in\{+1,-1\}\), so that the color at the next vertex differs from the current color by \(\varepsilon_i\) modulo three. An internal vertex is a CDV exactly when its two neighbors have different colors, equivalently when the two incident increments have the same sign. Therefore the internal non-CDVs are exactly the sign changes in the word \(\varepsilon_1\cdots\varepsilon_{n-1}\).

Let \(q\) be the number of those sign changes. The increment word splits into \(q+1\) constant-sign runs. Within one run, the CDV colors occur cyclically through the three colors, so the numbers contributed to any two colors differ by at most one. Summing over all runs shows that, if the total CDV counts are sorted as \(a\ge b\ge c\), then
\[
a-c\le q+1.
\]
Every internal vertex is either a CDV or a non-CDV, hence
\[
n-2=a+b+c+q.
\]
Combining the two relations gives
\[
n\ge 2a+b+1.
\]
If a coloring realizes \((r,s,t)\), sorting its three CDV counts gives \(a\ge r\), \(b\ge s\), and \(c\ge t\), so
\[
n\ge2r+s+1.
\]
When \(r=s=t\), the total-CDV requirement also gives \(n-2\ge3r\), hence the stronger lower bound \(n\ge3r+2\).

Both bounds are sharp. If \(r=s=t\), the periodic color word
\[
(012)^r01
\]
has length \(3r+2\), every internal vertex is a CDV, and each color has exactly \(r\) CDVs. If \(r=s>t\), then
\[
(012)^r0
\]
has length \(3r+1\) and sorted CDV counts \((r,r,r-1)\), which dominate \((r,r,t)\).

Finally suppose \(r>s\). Start with \((012)^{s+1}\), whose CDV counts are \((s,s+1,s)\), with color \(1\) being the middle entry. Its endpoint is color \(2\). Repeatedly append a pair \(1x\), where \(x\in\{0,2\}\) alternates and differs from the preceding endpoint. Each appended pair turns the old endpoint into a non-CDV and creates exactly one new CDV of color \(1\), without changing the CDV counts of colors \(0\) and \(2\). After \(r-s-1\) such pairs, the length is
\[
3(s+1)+2(r-s-1)=2r+s+1
\]
and the sorted CDV counts are \((r,s,s)\), which dominate \((r,s,t)\). Appending further vertices with colors different from the current endpoint preserves all previously guaranteed CDVs, so every larger path also realizes the sequence.

## Verification
A standalone verifier accompanies this result. It exhaustively enumerates proper three-colorings up to path order twelve and confirms the exact minimal order for every tested requirement whose predicted minimum is at most twelve. It also exhaustively checks the sign-run imbalance lemma through order fourteen, checks the explicit three-color constructions for all \(1\le t\le s\le r\le80\), and checks the two-color branch through order two hundred.

The verifier reports:

`ALL CHECKS PASSED; construction_cases=88560; minimality_cases=17; proper_word_checks=4094; lower_bound_words=16380; two_color_cases=199; exhaustive_order_max=12; lower_bound_order_max=14; construction_r_max=80`

The computation is a finite stress test only; the theorem is proved analytically above for all parameters.

## Relationship to prior work
Jakovac and Lang introduced sequence \(b\)-colorings in 2026. Their paper defines realization by prescribed numbers of CDVs in each color class and gives a complete characterization for cycles, together with results for regular graphs and for sequences requiring one additional CDV. The paper's abstract and organization explicitly single out cycles as the maximum-degree-two family treated in detail; targeted full-text and web searches found no corresponding path classification. The present result supplies that missing canonical family and, unlike the classical \(b\)-chromatic number of a path, determines every finite sequence that a path realizes.

Older work on classical \(b\)-colorings of path-related graphs concerns the maximum number of colors or transformed path families. Those statements do not prescribe multiple CDVs in each color class and therefore do not imply the threshold \(N(r,s,t)\).

## Limitations
The theorem is specific to paths and finite sequences. It does not classify sequence \(b\)-colorings of arbitrary trees or give an enumeration of all realizing colorings. The originality search cannot exclude terminology variants or sources not indexed by the searched literature systems; no such implication-equivalent result was found.

## References
1. M. Jakovac and M. S. Lang, *Sequence b-colorings in graphs*, arXiv:2609.08484v1, 2026. First public 8 September 2026; MSC 2020: 05C15.
2. S. K. Vaidya and R. V. Isaac, *The b-Chromatic Number of Some Path Related Graphs*, International Journal of Mathematics and Scientific Computing 4(1), 2014, 7--12. Classical \(b\)-chromatic-number context only.
