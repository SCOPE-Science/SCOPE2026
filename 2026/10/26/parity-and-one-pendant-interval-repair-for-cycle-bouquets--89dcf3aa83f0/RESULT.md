# Parity and one-pendant interval repair for cycle bouquets

## Finding

Let \(R(\ell_1,\ldots,\ell_k)\) be the simple graph obtained from \(k\ge1\) pairwise vertex-disjoint cycles of lengths \(\ell_i\ge3\) by identifying one vertex from each cycle into a common hub \(h\). Let \(s=|\{i:\ell_i\text{ is odd}\}|\). For ordinary interval edge colorings, and the deficiency, local deficiency, and weak local deficiency defined in the cited literature, the following complete classification holds:

\[
R(\ell_1,\ldots,\ell_k)\text{ admits an interval edge coloring}\iff s\equiv0\pmod2,
\]
\[
\operatorname{def}(R)=\operatorname{def}_{\mathrm{loc}}(R)=\operatorname{def}_{\mathrm{wloc}}(R)=s\bmod2.
\]

If \(s\) is even, an interval coloring with precisely \(2k\) colors exists, which is the minimum possible by the degree of \(h\). If \(s\) is odd, attaching **one pendant edge at the hub and nowhere else** produces an interval-colorable graph with precisely \(2k+1\) colors, again the minimum possible by the hub degree. In particular, at least one pendant edge is necessary for a deficient bouquet, and a single pendant edge at its hub always suffices, independently of the petal lengths.

## Assumptions and scope

Graphs are finite, loopless, and simple. An interval edge coloring is a proper coloring by the consecutive positive integers \(1,\ldots,t\), every one used, such that the colors on edges incident to each vertex form an integer interval. The *deficiency* \(\operatorname{def}(G)\) is the minimum total number of pendant edges whose attachment yields an interval-colorable graph. The *local deficiency* \(\operatorname{def}_{\mathrm{loc}}(G)\) is the minimum, over proper edge colorings, of the maximum number of missing integers inside an incident-color span at a vertex. The *weak local deficiency* \(\operatorname{def}_{\mathrm{wloc}}(G)\) is the analogous minimum of the maximum length of a **consecutive** missing-color gap. We use the convention that a vertex with no missing colors has local and weak local deficiency zero. The standard inequalities are
\[
0\le\operatorname{def}_{\mathrm{wloc}}(G)\le\operatorname{def}_{\mathrm{loc}}(G)\le\operatorname{def}(G).
\]
Only the stated one-vertex wedges of cycles are classified; the theorem does not assert the same criterion for all cacti or all Eulerian graphs.

## Proof

**1. Odd-petal obstruction.** All vertices of \(R\) have even degrees: the hub has degree \(2k\), and every other vertex degree two. In an interval coloring, the incident colors at each even-degree vertex contain equally many odd and even integers. Summing incidences therefore yields equally many odd-colored and even-colored edges, so the total number of edges is even. But
\[
|E(R)|=\sum_{i=1}^{k}\ell_i\equiv s\pmod2.
\]
Thus if \(s\) is odd, an interval coloring of \(R\) is impossible. This is the standard Eulerian parity obstruction, included here to make the proof self-contained.

**2. Local coloring lemma for one petal.** Let an abstract cycle of length \(\ell\ge3\) meet the hub in precisely two incident edges. Suppose those edges must receive colors \(a,b\), where \(a\ge1\) and \(b>a\). For an even cycle, \(b=a+1\) is realized by the sequence of its successive edge colors
\[
a,a+1,a,a+1,\ldots,a+1
\]
(in alternating order, with \(\ell\) entries). For an odd cycle, \(b=a+2\) is realized by
\[
a,a+1,a+2,a+1,a+2,\ldots,a+2.
\]
Every consecutive pair in either sequence differs by one; consequently, the two colors incident to each nonhub degree-two vertex form an interval. The distinct values \(a,b\) occur at the hub. No color smaller than \(a\) or larger than \(b\) appears on this petal. This proves the lemma, including lengths three and four.

**3. Even \(s\): perfect pairing at the hub.** Write \(r=k-s\) for the number of even petals. Reserve colors \(1,\ldots,2r\) for those petals, paired consecutively:
\[
(1,2),(3,4),\ldots,(2r-1,2r).
\]
For the \(s\) odd petals, reserve the remaining colors \(2r+1,\ldots,2k\). Within each of the two parity subsequences of this interval, pair successive values at distance two. Since \(s\) is even, each parity subsequence has an even length, and this creates exactly \(s\) pairs. Assign these pairs bijectively to the odd petals. Each hub color occurs once, and each pair meets the applicable case of the local coloring lemma. The gluing yields a proper interval coloring of the entire graph, with hub spectrum exactly \(\{1,\ldots,2k\}\). In particular all colors occur and its maximum is \(2k\). Since \(\deg(h)=2k\), this color count is optimal.

**4. Odd \(s\): one hub pendant.** Again reserve \(1,\ldots,2r\) for the even petals. Reserve \(2r+1,\ldots,2k+1\) for the odd petals and one new pendant edge. Among the latter \(2s+1\) colors, the odd positions form a list of \(s+1\) elements and the even positions form a list of \(s\) elements. Because \(s\) is odd, pair all successive odd positions at difference two; pair all but the last even position at difference two; assign the final unpaired even integer \(2k\) to the new pendant edge. The pairs number
\[
\frac{s+1}{2}+\frac{s-1}{2}=s.
\]
Apply the local coloring lemma independently to all petals. Every hub incident color is different, and they are exactly \(1,\ldots,2k+1\), so the augmented graph has an interval coloring with \(2k+1\) colors. Its hub degree is \(2k+1\), establishing color-count optimality. Step 1 shows that no augmentation by zero edges works, hence \(\operatorname{def}(R)=1\).

**5. All three deficiencies.** In the even case an interval coloring gives all three values zero. In the odd case absence of an interval coloring forces both local deficiencies to be positive (by their definitions). The known inequalities in the scope section, together with \(\operatorname{def}(R)=1\), force all three quantities to equal one. This completes the proof for every \(k\ge1\) and every \(\ell_i\ge3\).

## Verification

The self-contained `verify.py` generates the specified coloring, builds the entire simple graph, and checks distinct incident edge colors, consecutive spectra at every vertex, presence of every global color, and the prescribed hub degree. It verifies **all 2,800 ordered cycle-length lists with one through four petals and lengths in \(\{3,\ldots,9\}\)**, as well as **3,000 reproducibly seeded larger cases** with up to twenty petals and lengths up to 99. It records `CONSTRUCTIVE_CERTIFICATE_OK` in `verification_output.txt`. These experiments check the construction in finite cases; the argument in the preceding section, not the tests, proves the unrestricted statement.

## Relationship to prior work

Petrosyan (2013) proves the general necessary parity condition for Eulerian interval-colorable graphs; that gives Step 1, not the converse or one-edge repair for arbitrary bouquets. Casselgren–Petrosyan (2026) introduces and studies local and weak local deficiency, giving inequalities and general upper bounds for other graph families. Its reported weak-local upper bound for outerplanar graphs already implies part of the weak-local **upper** bound here, not the exact hub-only ordinary deficiency repair. Sahakyan (2021) studies edge coloring of cactus graphs with given spectra, supplying general algorithmic context; an exact bouquet parity-and-repair classification was not identified in the accessible material. A 2025 doctoral abstract on interval colorability of cactus graphs and cyclic trees concerns related structures and raises a specific literature-coverage risk.

The present assertion is restricted to a constructive closed-form criterion and globally minimal **single hub-edge repair** for arbitrary one-point cycle bouquets, with local and weak-local values recorded as consequences. Neither the Eulerian parity obstruction nor the generic outerplanar weak-local bound is claimed as new.

## Limitations

The classification does not extend without additional proof to cacti in which different pairs of cycles meet at different cut vertices, nor to general Eulerian graphs. Published or otherwise unindexed equivalent results may exist, particularly in work on interval colorings of cactus graphs. No independent audit has been performed. Computational checks are corroboration only.

## References

1. C. J. Casselgren and P. A. Petrosyan, *Local measures of interval edge-uncolorability*, arXiv:2609.15873v1, posted 2026-09-14. https://arxiv.org/abs/2609.15873
2. P. A. Petrosyan, *On Interval Non-Edge-Colorable Eulerian Multigraphs*, arXiv:1311.2210, posted 2013-11-09. https://arxiv.org/abs/1311.2210
3. A. Kh. Sahakyan, *Edge Coloring of Cactus Graphs with Given Spectrums*, International Academy Journal Web of Scholar 2(52) (2021), DOI:10.31435/rsglobal_wos/30062021/7617.
4. L. Sahakyan, *doctoral abstract on interval edge colorings of cactus graphs and cyclic trees* (2025), https://www.ysu.am/sites/default/files/2025-05/Levon_PhD_Abstract_For_Print%20%281%29.pdf (the accessible abstract provides contextual evidence, not a complete primary-text exclusion check).
