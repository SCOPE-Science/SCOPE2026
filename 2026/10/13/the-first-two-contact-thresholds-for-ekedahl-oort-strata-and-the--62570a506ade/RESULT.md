# The first two contact thresholds for Ekedahl–Oort strata and the supersingular locus

## Finding
Let \(g\geq 3\), let \(p\) be an odd prime, and put \(k=\lfloor g/2\rfloor\) and \(h=\lceil g/2\rceil\). In the moduli space \(\mathcal A_g\) of principally polarized abelian varieties over an algebraic closure of \(\mathbb F_p\), write \(\mathcal S_g\) for the supersingular locus. Index Ekedahl–Oort (EO) strata \(\mathcal A_{g,\delta}\) by increment vectors \(\delta\in\{0,1\}^g\), and let \(e_j\) be the vector whose only nonzero entry is at position \(j\).

**Sharp first-two-layer classification.** The following hold uniformly for every \(g\geq3\) and every odd \(p\):

1. Every EO stratum of dimension at most \(k\) is contained in \(\mathcal S_g\) (the established containment boundary).
2. Among EO strata of dimension exactly \(k+1\), precisely \(\mathcal A_{g,e_h}\) is disjoint from \(\mathcal S_g\); every other such stratum is contained in \(\mathcal S_g\).
3. Among EO strata of dimension exactly \(k+2\), precisely \(\mathcal A_{g,e_{h-1}}\) is disjoint from \(\mathcal S_g\), precisely \(\mathcal A_{g,e_h+e_g}\) meets but is not contained in \(\mathcal S_g\), and every other such stratum is contained in \(\mathcal S_g\).

In particular, the least dimension of an EO stratum disjoint from the supersingular locus is \(\lfloor g/2\rfloor+1\), while the least dimension of a **mixed** EO stratum—one meeting but not contained in that locus—is \(\lfloor g/2\rfloor+2\). At either first threshold, the indicated exceptional stratum is unique.

## Assumptions and scope
The characteristic is odd; the proof invokes the nonemptiness criterion of Muller, Theorem 1.7 of arXiv:2609.15024v2. The assertion concerns principally polarized abelian varieties, their EO strata, and the supersingular Newton stratum in the Siegel moduli space. It does not assert these statements in characteristic two, for arbitrary PEL type, or for the Torelli locus. Every EO stratum appearing is nonempty. The coordinates of \(\delta\) are indexed from \(1\) to \(g\), and the associated elementary sequence is \(\varphi_i=\sum_{j=1}^{i}\delta_j\).

## Proof
The known EO dimension and containment formulas [1–3] are
\[
\dim\mathcal A_{g,\delta}=\sum_{i=1}^g(g+1-i)\delta_i,
\qquad
\mathcal A_{g,\delta}\subseteq\mathcal S_g
\iff \varphi_h=0.
\]
Thus an EO stratum that is not contained in \(\mathcal S_g\) has a nonzero increment among the first \(h\) positions. The smallest such weight is \(g+1-h=k+1\). Consequently all strata of dimension at most \(k\) are contained in \(\mathcal S_g\). At dimension \(k+1\), the only vector not covered by the containment condition is \(e_h\). At dimension \(k+2\), the only two not covered are \(e_{h-1}\) and \(e_h+e_g\): an earlier index costs at least \(k+3\), while any additional nonzero entry after position \(h\) contributes at least \(1\), with equality only at position \(g\). This is an exhaustive partition of the stated dimension layers.

It remains to decide whether each exceptional stratum meets \(\mathcal S_g\). For an increment vector \(\delta\), put \(P=\{i:\delta_i=1\}\), \(Z=\{i:\delta_i=0\}\), and define the permutation [2]
\[
\pi_\delta(i)=
\begin{cases}
\varphi_i,&i\in P,\\
g+1-i+\varphi_i,&i\in Z.
\end{cases}
\]
Muller's criterion says that an EO stratum meets \(\mathcal S_g\) precisely when every *bad* cycle of \(\pi_\delta\) can be reached from a *good* cycle in the directed cycle graph. A cycle is bad if it contains a member of \(P\), contains an even number of members of \(Z\), and the number of zero positions between each successive pair of one positions (cyclically) is even. A cycle containing no member of \(P\) is good. Arrows into bad cycles require a one position on the source cycle [2, Definitions 1.3–1.5].

For any \(1\leq j\leq h\), the permutation corresponding to \(\delta=e_j\) has the distinguished cycle \(C_1=(1)\) when \(j=1\), and for \(2\leq j\leq h\) it has the cycle
\[
C_j=(1,\,g,\,2,\,g-1,\,\ldots,\,j),
\]
with length \(2j-1\), and all other cycles contain no one positions. The cycle \(C_j\) contains the unique one position \(j\) and exactly \(2j-2\) zero positions. Hence \(C_j\) is bad; all other cycles are good but cannot be sources of an arrow, because none contains a one position. Thus \(C_j\) is unreachable from any good cycle. Applying the criterion shows that \(\mathcal A_{g,e_j}\cap\mathcal S_g=\varnothing\), in particular for \(j=h\) and \(j=h-1\).

For \(\delta=e_h+e_g\), changing the last increment of \(e_h\) from zero to one leaves \(\pi_\delta\) unchanged: both rules send \(g\) to \(2\). Thus its nontrivial cycle is still \(C_h\). It now has two one positions \(h\) and \(g\). Along the cyclic order from \(h\) to \(g\) there is exactly one zero position, namely \(1\); the opposite interval has \(2h-4\) zero positions. Since one interval contains an odd number of zero positions, \(C_h\) is good. Every other cycle contains no one positions and is also good. Therefore no bad cycle exists, and the criterion proves that \(\mathcal A_{g,e_h+e_g}\cap\mathcal S_g\neq\varnothing\). Finally, \(\varphi_h=1\), so the same stratum is **not** contained in \(\mathcal S_g\). This establishes the complete classification and both sharp thresholds. \(\square\)

## Verification
The standalone standard-library program `check_eo_boundary.py` implements the complete cycle-graph reachability condition and exhaustively enumerates all \(2^g\) increment vectors for each \(3\leq g\leq14\). It checks the exhaustive three-layer classification in those genera and reproduces the independent published meeting-stratum counts for those genera. It prints `EO_FIRST_TWO_CONTACT_LAYERS_EXACT_OK`. These finite checks are corroboration only: the proof for every \(g\geq3\) is the symbolic weight and cycle argument above.

## Relationship to prior work
The containment criterion \(\varphi_h=0\) is due to earlier work of Oort and Harashita and appears explicitly in Görtz–Yu [1, Proposition 2.5]. It is **not** a new assertion. Muller [2, Theorem 1.7] and independently Shimada [3, Proposition 3.1] give general tests for nonempty intersection with the supersingular locus. Shimada [3, Section 3.1] explicitly exhibits a disjoint type with its sole nonzero increment in position \(2\); this supplies the first boundary case when \(h=2\), but not the uniform first-two-layer classification. Groen–Lupoian–Parker [4, Table 1 and Corollary 2] classify all intersections in genus \(5\), including the corresponding isolated boundary examples, but make no all-genus assertion. The contribution here is the exact dimension-minimality, uniqueness, and first mixed-contact classification in all genera, derived by a separate uniform analysis of the two first possible dimension layers. The result is **not** a new general intersection criterion.

## Limitations
The threshold results use existing nonemptiness and containment theorems; they do not independently establish those general theorems. The external-literature comparison supports the absence of an explicit all-genus first-two-layer classification in the most relevant examined sources, not exhaustive historical novelty. The finite checker cannot certify the universal proof. No statement is made concerning the geometry or irreducible components of the intersections, or the case \(p=2\).

## References
[1] U. Görtz and C.-F. Yu, *The supersingular locus in Siegel modular varieties with Iwahori level structure*, arXiv:0807.1229v3, Proposition 2.5 (2009 preprint; published in *Mathematische Annalen* 353 (2012), 465–498). https://arxiv.org/abs/0807.1229

[2] J. Muller, *Ekedahl–Oort strata meeting the supersingular locus*, arXiv:2609.15024v2, Definitions 1.3–1.5, Theorem 1.7 and dimension formula (2026). https://arxiv.org/abs/2609.15024

[3] R. Shimada, *The number of Ekedahl–Oort strata intersecting the supersingular locus in the Siegel modular variety*, arXiv:2609.27198v1, Introduction and Proposition 3.1 (2026). https://arxiv.org/abs/2609.27198

[4] S. R. Groen, E. Lupoian and M. Parker, *Intersections of the Ekedahl–Oort and Newton strata of \(\mathcal A_5\)*, arXiv:2509.19878v2, Table 1 and Corollary 2 (2026 revision). https://arxiv.org/abs/2509.19878
