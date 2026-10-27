# A sharp rarity law for non-upward bilateral team meanings

## Finding

Fix an integer \(q\ge 1\), let \(V\) be the set of all classical valuations of \(q\) propositional letters, and put \(N=|V|=2^q\). Count formulas of propositional bilateral state-based logic (BSL) **up to support-equivalence**: two formulas are identified precisely when their *supporting teams* agree for every team \(T\subseteq V\). No identification of their anti-supporting teams is asserted.

Let \(M_k\) be the \(k\)-th Dedekind number, i.e. the number of upward-closed families of subsets of a labelled \(k\)-element set, **including** the empty family. Write \(W_N\) for the number of BSL support-equivalence classes, and \(E_N\) for the number whose support is *not* upward closed on all teams \(T\subseteq V\). Then

\[
 W_N=1+\sum_{k=0}^{N}\binom Nk(M_k-1),\qquad
 E_N=\sum_{k=0}^{N-1}\binom Nk(M_k-1).
\]

As \(q\to\infty\), hence \(N=2^q\to\infty\), the exceptional classes obey the **sharp first-order equivalent**

\[
 E_N\sim N M_{N-1},\qquad W_N\sim M_N,
 \qquad \frac{E_N}{W_N}\sim\frac{N M_{N-1}}{M_N}.
\]

More explicitly, with \(B_N=\binom N{N/2}\) (\(N\) is even),

\[
 \log_2\frac{E_N}{W_N}=-\bigl(\tfrac12+o(1)\bigr)B_N.
\]

Thus a uniformly selected *support-equivalence class* is upward closed with probability tending to one, despite the logic admitting non-upward-closed support. Moreover, conditioned on being exceptional, with probability tending to one its largest supporting team has exactly \(N-1\) valuations: its deviation from full upward closure is concentrated in a single omitted valuation.

For the first three nonempty languages, \(q=1,2,3\), the exact triples \((W_N,M_N,E_N)\) are

\[
 (11,6,5),\quad(283,168,115),\quad
 (56130437248005233867039,56130437228687557907788,19317675959251).
\]

## Assumptions and scope

A *team* is any subset of the fixed finite valuation set \(V\), including the empty team. A *support meaning* is a collection \(\mathcal F\subseteq\mathcal P(V)\). Call it a *weak ideal* when (i) \(A,B\in\mathcal F\) implies \(A\cup B\in\mathcal F\), and (ii) \(A,C\in\mathcal F\) and \(A\subseteq B\subseteq C\) implies \(B\in\mathcal F\). The empty collection is allowed; union closure requires only binary/nonempty unions. Upward closure refers to inclusion among **teams**, not inclusion among valuations. The previously established expressiveness theorem for BSL identifies its possible support meanings with these weak ideals (Anttila--Knudstorp, 2025; restated by Aloni et al., 2026). This expressiveness theorem is an input, not a new result here.

All counts are for labelled valuations, not under permutation of propositional letters, and for support alone, not for the ordered pair of support and anti-support meanings. A ``uniformly selected class'' is a uniform selection among this finite collection of inequivalent support meanings, not among formulas of bounded length.

## Proof

**1. Normal form.** Take a nonempty weak ideal \(\mathcal F\). Since \(V\) is finite, \(\mathcal F\) is finite, so binary-union closure gives the unique maximum \(U=\bigcup\mathcal F\in\mathcal F\). Convexity now gives

\[
 \mathcal F=\{T\subseteq U:\exists S\in\mathcal F\ (S\subseteq T)\}.
\]

The right-hand side is a nonempty upward-closed family inside \(\mathcal P(U)\). Conversely, every nonempty upset of \(\mathcal P(U)\), considered as a family of subsets of \(V\), is closed under binary unions and is inclusion-convex. Its union is exactly \(U\), because every nonempty upset contains its maximum \(U\). Therefore the choice of \(U\) is unique. The empty weak ideal is an additional case.

**2. Exact count.** For fixed \(U\) of size \(k\), the number of nonempty upsets of \(\mathcal P(U)\) is \(M_k-1\), and there are \(\binom Nk\) choices of \(U\). Summing and adding the empty weak ideal proves the expression for \(W_N\). A weak ideal is globally upward closed if and only if it is empty or its maximum is \(V\): nonempty globally upward-closed families must contain \(V\), and the normal form with \(U=V\) is globally upward closed. There are exactly \(M_N\) such families, hence the stated expression for \(E_N=W_N-M_N\). The BSL expressiveness theorem transfers these family counts bijectively to support-equivalence classes.

**3. Dominant exceptional layer.** The contribution to \(E_N\) from maxima \(U\) omitting one valuation is \(N(M_{N-1}-1)\). The remaining contribution \(R_N\), for \(N\ge2\), satisfies

\[
 0\le R_N=\sum_{k=0}^{N-2}\binom Nk(M_k-1)
 \le 2^N M_{N-2}.
\]

The classical Dedekind estimate (Kleitman--Markowsky; also reviewed by Jenssen--Malekshahian--Park, 2026) states

\[
 \log_2 M_m=(1+o(1))\binom m{\lfloor m/2\rfloor}\quad(m\to\infty).
\]

The middle binomial coefficient at \(m-1\) is asymptotically one-half that at \(m\), so

\[
 \log_2 M_{N-1}-\log_2 M_{N-2}
  =(\tfrac12+o(1))\binom{N-1}{\lfloor(N-1)/2\rfloor}\gg N.
\]

It follows that \(2^N M_{N-2}=o(N M_{N-1})\), establishing \(E_N\sim N M_{N-1}\). Likewise \(N M_{N-1}/M_N\to0\), hence \(W_N=M_N+E_N\sim M_N\). The same binomial-ratio estimate gives

\[
 \log_2 E_N=(\tfrac12+o(1))B_N,
 \qquad \log_2 W_N=(1+o(1))B_N,
\]

and subtraction proves the logarithmic law. Finally, the probability that an exceptional family omits exactly one valuation is exactly \(N(M_{N-1}-1)/E_N\to1\).

**4. Explicit finite values.** Insert the established Dedekind numbers \(M_0,\ldots,M_8=(2,3,6,20,168,7581,7828354,2414682040998,56130437228687557907788)\) into the exact formulas. No new claim is made about the computation or discovery of those Dedekind numbers.

## Verification

Run `python3 check_weak_ideals.py` with Python 3.10 or later. The standalone checker independently tests every possible family of teams when \(0\le |V|\le4\), without using the derived normal form as its test for weak-ideal membership. It verifies binary unions, all intermediate teams for convexity, and the proposed unique-maximum/upset equivalence. It separately counts globally upward-closed families and checks the exact binomial formula. It evaluates the formula for \(N=2,4,8\) using independently published Dedekind numbers. Representative output:

```
DIRECT_FAMILY_CLASSIFICATION_OK n=4 weak=283 global_upset=168 by_top=[1, 8, 30, 76, 167]
BSL_SUPPORT_SPECTRUM_OK q=3 N=8 total=56130437248005233867039 upward=56130437228687557907788 exceptional=19317675959251
WEAK_IDEAL_SPECTRUM_AND_CONCENTRATION_CHECK_OK
```

The finite exhaustive checks do not constitute a proof of the asymptotics. The latter follows from the cited Dedekind estimate and the explicit comparison bounds in the proof.

## Relationship to prior work

Anttila and Knudstorp (2025), *Convex Team Logics*, prove expressive completeness for convex union-closed team properties; their Section 3.1, especially Lemma 3.2 and Theorem 3.5, already contains the basic union-of-members representation underlying Step 1. Aloni, Baltag, van Benthem, Bezhanishvili, and Knudstorp (2026), *Teams, Truthmakers, Translations*, Section 3.1, explicitly formulate BSL denotations as weak ideals and credit that expressive-completeness result. These are substantial antecedents, not independent findings of this note.

The remaining input is the known Dedekind enumeration and its classical logarithmic asymptotics, reviewed and sharpened in Jenssen, Malekshahian, and Park (2026). The claim here is their **quantitative synthesis in BSL support-equivalence semantics**: the exact class spectrum, dominant one-valuation defect layer, and limiting rarity exponent. We do not claim a novel proof of Dedekind asymptotics, a new expressive-completeness theorem, or a count of bilateral semantics retaining anti-support.

## Limitations

The result counts support-equivalence classes on the complete classical valuation domain only. It does not count finite syntax trees, semantic pairs of support and anti-support, modal extensions on arbitrary Kripke structures, or formulas up to syntactic equivalence. The numerical values for \(N=8\) inherit the established exact Dedekind values; the standalone check does not independently enumerate all such upsets. The asymptotic result uses the previously proved Dedekind estimate. Although searches did not identify the stated BSL concentration law in the inspected literature, an older general counting result for convex union-closed families could subsume it; historical priority is not certified.

## References

1. A. Anttila and S. B. Knudstorp, *Convex Team Logics*, arXiv:2503.21850, first public version 27 March 2025; Section 3.1 (Lemma 3.2 and Theorem 3.5); https://arxiv.org/abs/2503.21850.
2. M. Aloni, A. Baltag, J. van Benthem, N. Bezhanishvili, and S. B. Knudstorp, *Teams, Truthmakers, Translations*, arXiv:2610.15680v1, first public version 11 October 2026; Section 3.1; https://arxiv.org/abs/2610.15680.
3. M. Jenssen, A. Malekshahian, and J. Park, *On Dedekind's problem, a sparse version of Sperner's theorem, and antichains of a given size in the Boolean lattice*, J. Lond. Math. Soc. 114 (2026), e70624, DOI:10.1112/jlms.70624; Introduction, pp. 1--2, for the classical Kleitman--Markowsky bound and background on exact values.
4. The Dedekind Project, independent published tabulation of \(M_0,\ldots,M_9\); https://github.com/VonTum/Dedekind.
