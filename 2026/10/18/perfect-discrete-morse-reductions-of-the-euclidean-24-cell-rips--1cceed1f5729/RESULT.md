# Perfect discrete Morse reductions of the Euclidean 24-cell Rips filtration

## Finding

Let \(V\subset\mathbb R^4\) be the twenty-four vertices of the root-system 24-cell,
\[
V=\{s_i e_i+s_j e_j:1\le i<j\le4,\ s_i,s_j\in\{-1,1\}\}.
\]
For \(r\ge0\), let \(K_r\) denote the inclusive Euclidean Vietoris–Rips complex: a nonempty \(F\subseteq V\) is a face exactly when every distance between points of \(F\) is at most \(r\).

**Perfect-Morse theorem.** The complexes \(K_{\sqrt2}\) and \(K_2\) admit acyclic discrete-Morse matchings with respective critical-cell vectors
\[
(c_0,c_1,c_2)=(1,0,23),\qquad
(c_0,c_1,c_2,c_3,c_4,c_5)=(1,0,0,1,0,0).
\]
These are perfect over the integers: the critical-cell counts meet the integral Betti-number bounds. A complete finite witness comprises exactly \(96\) free-face pairs at the first scale and \(791\) at the second. Therefore the **complete homotopy filtration** is
\[
K_r\simeq
\begin{cases}
\bigsqcup^{24}\mathrm{pt},&0\le r<\sqrt2,\\
\bigvee^{23}S^2,&\sqrt2\le r<2,\\
S^3,&2\le r<\sqrt6,\\
S^{11},&\sqrt6\le r<2\sqrt2,\\
\mathrm{pt},&r\ge2\sqrt2.
\end{cases}
\]
Here equivalence describes each individual homotopy type, not a claim that unspecified choices of equivalences commute with inclusions.

## Assumptions and scope

The ambient metric is **Euclidean distance** on the specified twenty-four points; it is not shortest-path distance on the 24-cell's edge graph. Equalities at the four distance thresholds are included. The theorem concerns this single finite point set in \(\mathbb R^4\), with the fixed root-vector normalization above. No assertion is made about other regular four-polytopes or their generalizations.

## Proof

**1. Exact distance levels.** For distinct points in \(V\), squared Euclidean distances belong to \(\{2,4,6,8\}\). Exhausting unordered pairs gives respective multiplicities \(96,72,96,12\). There is one squared-distance-eight partner of each vertex, namely its negative. Consequently the filtration changes only at \(\sqrt2,2,\sqrt6,2\sqrt2\).

**2. Exhaustive finite simplicial models.** The recursive clique enumeration implemented in `verify_24cell.py` visits each increasing vertex sequence once, recursing only on common future neighbors in the integer squared-distance graph. It enumerates all nonempty simplices, not merely maximal cliques. At squared thresholds \(2\) and \(4\), respectively, the resulting face vectors (in dimensions increasing from zero) are
\[
(24,96,96),\qquad(24,168,480,600,288,24).
\]
Thus these complexes have \(216\) and \(1584\) nonempty simplices.

**3. Elementary-pair certificates.** Number the vertices \(0,\ldots,23\) in lexicographic coordinate-pair and sign order as defined in `verify_24cell.py`. Encode a face \(F\) by its exact nonnegative integer bitmask \(m(F)=\sum_{j\in F}2^j\). The complete ordered certificates reside in `24cell_certificate.json`. A two-element operation `[a,b]` removes the face with mask `a` and its unique codimension-one coface with mask `b`; at that moment the latter is maximal in the remaining complex. A singleton operation `[a]` records the removal of a maximal critical simplex.

The checker reconstructs the full current face poset, and for each operation verifies that the designated faces remain present and that every removal satisfies precisely the preceding conditions. It then updates every affected immediate-coface set. At the end it verifies that every original simplex was consumed exactly once and that the only critical cells have the asserted dimensions. Reversal of this sequence of elementary collapses and maximal critical-cell deletions is an acyclic discrete-Morse matching: directed cycles are impossible because each matched removal precedes every remaining cell that could participate in such a cycle.

The first certificate removes \(96\) face pairs and has exactly one critical vertex and \(23\) critical triangles. The second removes \(791\) pairs and has exactly one critical vertex and one critical tetrahedron. Forman's discrete-Morse theorem produces CW models with those respective cell vectors. Every attaching map in positive dimension must be constant because there are no positive-dimensional cells below the top critical dimension. The two homotopy types are therefore exactly \(\bigvee^{23}S^2\) and \(S^3\).

**4. Final two thresholds.** At squared threshold \(6\), every pair is an edge except for the twelve antipodal pairs. A clique contains at most one vertex from each pair, so the entire complex is the join of twelve two-point complexes, \((S^0)^{*12}\cong S^{11}\). At squared threshold \(8\), the complex is the full simplex and is contractible. Below \(\sqrt2\), it consists of twenty-four isolated vertices. This proves all stages.

## Verification

The two standalone files are `verify_24cell.py` and `24cell_certificate.json`. From their common directory, execute:

```text
python verify_24cell.py 24cell_certificate.json
```

Only the Python standard library and exact integer arithmetic are used. The verifier checks the squared-distance histogram, independently reconstructs every face by exhaustive clique generation, checks the exact face vectors, and replays all \(887\) free-face pairs and \(26\) critical-cell removals individually. Expected terminal line: `CERTIFICATE VERIFIED`. The resulting Morse models prove full integral homotopy types, not merely mod-prime Betti numbers.

## Relationship to prior work

Attali–Lieutier–Salinas (2011) develop collapses and homotopy reconstruction for Euclidean Vietoris–Rips complexes under general geometric hypotheses; no perfect matching or explicit 24-cell calculation is asserted here as belonging to that paper. Saleh's 2023 dissertation, Section 4.2, reports the **already known** integral homology ranks \(23\) in degree two, \(1\) in degree three, and \(1\) in degree eleven for the respective three nontrivial scales. Its open-questions section calls for homotopy classifications of four-polytopes. Those known homology values are acknowledged and are not the novelty claimed here. The present stronger datum is the complete, replayable **perfect discrete-Morse matching** at both finite intermediate scales, yielding a direct homotopy classification. Existing published calculations of other graphs or polytopes do not directly supply these two certificates.

## Limitations

The homology ranks at the three scales were reported previously; the new assertion is the perfect-Morse structure and resulting constructive homotopy equivalences. Perfectness is established by the supplied finite witnesses, not by a dimension-free symbolic matching rule. The result does not identify symmetry-equivariant Morse functions, naturality of the chosen homotopy equivalences along the filtration, or matching constructions for all regular four-polytopes. Bibliographic completeness beyond inspected/indexed sources is not guaranteed.

## References

1. D. Attali, A. Lieutier, D. Salinas, *Vietoris-Rips complexes also provide topologically correct reconstructions of sampled shapes*, SoCG 2011, pp. 491–500, https://doi.org/10.1145/1998196.1998276 (public proceedings date 2011-06-13).
2. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, dissertation, September 2023, §4.2, p. 73, and open questions, p. 75, https://d-nb.info/1375949942/34.
3. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris-Rips complexes of Platonic solids*, https://arxiv.org/abs/2302.14388 (three-dimensional Platonic solids, not the regular four-dimensional 24-cell).
4. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145, https://doi.org/10.1006/aima.1997.1650.
