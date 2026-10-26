# The eleven finite spectra of the two-noun cardinality syllogistic

## Finding

Let \(S^\dagger(\mathrm{card})\) be the cardinality-comparison syllogistic with noun complements but no propositional connectives between sentences. Restrict the **raw** noun vocabulary to \(p\) and \(q\). Theory spectra of finite **nonempty** structures in this fragment are precisely
\[
\varnothing;\quad T_k=\{n\in\mathbb N_{>0}:n\ge k\}\quad (1\le k\le7);\qquad
E_k=\{n\in\mathbb N_{>0}: n\ge k,\ n\text{ even}\}\quad(k=2,4,6).
\]
Thus there are exactly eleven distinct spectra. In particular, every satisfiable theory in the fragment has a model of size at most \(7\), and this bound is attained.

The stronger **profile-compression statement** holds: for each nonempty finite structure \(M\), a structure \(M'\) of size at most \(7\) agrees with \(M\) on *all* two-noun syllogistic sentences, not merely a prescribed finite theory.

## Assumptions and scope

A **noun** is one of \(p,\bar p,q,\bar q\); noun complementation is interpreted relative to the nonempty universe. For nouns \(x,y\), allowed sentence forms are \(\mathrm{All}(x,y)\) (inclusion), \(\mathrm{Some}(x,y)\) (nonempty intersection), \(\mathrm{AtLeast}(x,y)\) (\(|x|\ge|y|\)), and \(\mathrm{More}(x,y)\) (\(|x|>|y|\)). A theory is any set of such sentences. No noun intersections/unions are independently available as nouns, and there are no Boolean connectives at the **sentence** level. A spectrum lists positive cardinalities of its finite models.

Write the disjoint Venn-cell sizes as
\[
a=|p\cap q|,\quad b=|p\cap\bar q|,\quad c=|\bar p\cap q|,\quad d=|\bar p\cap\bar q|,
\]
so that \(a,b,c,d\ge0\) and \(n=a+b+c+d>0\). Set \(u=b-c\) and \(v=a-d\).

## Proof

**Lemma (uniform seven-point compression).** Every nonempty four-cell vector \((a,b,c,d)\) has a nonempty representative \((a',b',c',d')\) with sum at most \(7\), such that the zeros of the four cell counts and the four signs
\[
\operatorname{sgn}(u),\quad\operatorname{sgn}(v),\quad
\operatorname{sgn}(u+v),\quad\operatorname{sgn}(v-u)
\]
are preserved.

*Proof.* Normalize the signed differences \(u,v\) as follows. If one is zero, leave that one zero and replace the other nonzero magnitude by \(1\). If both are nonzero and \(|u|=|v|\), replace both magnitudes by \(1\). If \(|u|>|v|>0\), replace their magnitudes by \(2,1\), respectively; for \(|v|>|u|>0\), use \(1,2\), keeping each sign. Denote the resulting values by \(u',v'\). This preserves the four specified signs because they are determined by the signs of \(u,v\) and the comparison of their absolute values. Moreover, \(|u'|+|v'|\le3\).

For a pair of original nonnegative counts \((x,y)\) and target difference \(t\), preserve whether each entry is zero, and realize \(x'-y'=t\) as follows: if both were positive, take \((x',y')=(1+\max(t,0),1+\max(-t,0))\); if only \(x\) was positive, take \((t,0)\); if only \(y\) was positive, take \((0,-t)\); if both vanished, take \((0,0)\). These choices are valid because the normalization preserves the sign of the difference. Apply this construction to \((b,c)\) with target \(u'\), and to \((a,d)\) with target \(v'\). Every pair costs at most \(2+|t|\) points, hence
\[
a'+b'+c'+d'\le4+|u'|+|v'|\le7.
\]
The old and new zero patterns coincide and therefore the new total is positive. This proves the lemma.

**Why it preserves every sentence.** Inclusion and intersection-nonemptiness between any two of \(p,\bar p,q,\bar q\) depend only on whether the relevant Venn cells vanish. Every difference between cardinalities of two of these four nouns is, up to sign, one of
\[
|p|-|q|=u,\quad |p|-|\bar q|=v,\quad
|p|-|\bar p|=u+v,\quad |q|-|\bar q|=v-u,
\]
with the remaining pairwise differences negatives of these. Thus all cardinal comparisons have unchanged truth values. No sentence can distinguish the two structures. In particular, even an infinite satisfiable theory has a model on at most seven points.

**Upper classification.** Jiang's theorem for unrestricted \(S^\dagger(\mathrm{card})\) states that every spectrum is empty, an eventual full tail \(T_k\), or an eventual even tail \(E_k\). By the preceding lemma, a nonempty spectrum here contains an integer at most \(7\). Therefore \(k\le7\) for full tails. For even tails, only minimum even points \(2,4,6\) occur. Tails starting at odd thresholds duplicate the tail whose threshold is the next even integer, so there are at most eleven spectra in total.

**Realizing all eleven spectra.** Abbreviate the four Venn-cell nonemptiness conditions by the theory
\[
\mathcal A=\{\mathrm{Some}(p,q),\mathrm{Some}(p,\bar q),
\mathrm{Some}(\bar p,q),\mathrm{Some}(\bar p,\bar q)\}.
\]
Let \(\mathcal A_j\) consist of its first \(j\) sentences, and put
\[
\mathcal B=\{\mathrm{AtLeast}(p,\bar p),\mathrm{AtLeast}(\bar p,p)\}.
\]
The latter says \(|p|=|\bar p|\). The theory \(\{\mathrm{More}(p,p)\}\) has empty spectrum; the empty theory has spectrum \(T_1\). The theories \(\mathcal A_2,\mathcal A_3,\mathcal A\) give \(T_2,T_3,T_4\), respectively. The theory \(\mathcal A\cup\{\mathrm{More}(p,q)\}\) gives \(T_5\), since the extra condition is \(b>c\). Adding \(\mathrm{More}(p,\bar q)\), meaning \(a>d\), yields \(T_6\). For \(T_7\), instead take
\[
\mathcal A\cup\{\mathrm{More}(p,\bar q),\mathrm{More}(\bar q,q)\}.
\]
These assert \(a>d\) and \(b+d>a+c\), so \(a\ge2\) and \(b\ge c+(a-d)+1\ge3\); the minimum sizes are attained, respectively, by
\[
T_2:(1,1,0,0),\quad T_3:(1,1,1,0),\quad T_4:(1,1,1,1),
\quad T_5:(1,2,1,1),\quad T_6:(2,2,1,1),\quad T_7:(2,3,1,1),
\]
listed as \((a,b,c,d)\). In each case any greater size is obtained by adding points to cell \(b\), which preserves the required nonemptiness and strict inequalities.

Finally, \(\mathcal B\), \(\mathcal B\cup\mathcal A\), and
\(\mathcal B\cup\mathcal A\cup\{\mathrm{More}(p,q)\}\) have spectra \(E_2,E_4,E_6\), respectively. Equality \(|p|=|\bar p|\) forces even size; the last case forces \(b>c\) and hence \(d>a\), requiring the six-point minimum \((1,2,1,2)\). The two smaller even minima occur with counts \((1,0,0,1)\) and \((1,1,1,1)\). Every larger even size is attained by adjoining one point in each of cells \(b\) and \(c\), preserving the comparisons. The eleven spectra are distinct and exhaustive.

## Verification

A standalone `CHECKER.py` enumerates all four-cell models of total size \(1\) through \(35\), checks that the compression retains the zero pattern and comparison-sign profile, and reports a maximum compressed size of \(7\). It also checks all eleven explicit witnesses against the desired spectra at universe sizes \(1\) through \(14\). This finite computation corroborates but does **not** replace the unrestricted symbolic lemma and the global spectrum theorem used above.

## Relationship to prior work

Jiang's 2026 classification gives the unrestricted full-tail/even-tail dichotomy but imposes no two-symbol bound on the raw nouns. The present theorem supplies a sharp quantitative vocabulary bound and a complete list of the surviving spectra when just two raw nouns are permitted. A relevant publicly indexed one-noun analysis identifies only \(\varnothing,T_1,T_2,T_3,E_2\); that classification does not entail the eleven-spectrum two-noun result. The construction explicitly gives the new six additional realizable spectra and demonstrates a qualitatively larger but still bounded threshold.

## Limitations

The result concerns only \(S^\dagger(\mathrm{card})\) with two raw nouns, complement terms, and theories without Boolean sentence connectives. It does not classify three or more noun symbols, allow complex noun intersections as syntactic terms, or address spectra under Boolean combinations of entire sentences. Full-text inspection was not possible for every older foundational syllogistic article; an equivalent earlier vocabulary-bound theorem outside the searched sources remains a residual priority risk. No independent audit or formal proof-assistant verification has been performed.

## References

1. R. Jiang, *Finite Spectra of Syllogistic Logic with Cardinality Comparisons*, arXiv:2609.24902v1, first posted 21 September 2026. https://arxiv.org/abs/2609.24902
2. L. S. Moss, *Syllogistic Logic with Cardinality Comparisons*, in *Logical Aspects of Computational Linguistics*, 2016, DOI:10.1007/978-3-319-29300-4_18.
3. *The one-variable cardinality syllogistic has exactly five finite spectra*, publicly indexed research note, 2026 (relevant one-noun comparison).

