# Above the conjugate exponent, WMP and SMP coincide on \(\ell_p\) domains
## Finding
Let \(1<p<\infty\), let \(p^*=p/(p-1)\), and let \(Y\) be any Banach space. For every finite \(r\ge p^*\), the pair \((\ell_p,Y)\) has the weakly \(r\)-singular maximizing property if and only if it has the weak maximizing property. Hence, whenever \((\ell_p,Y)\) has the weak maximizing property, it has the \(r\)-convergent perturbation property for every finite \(r\ge p^*\). If, in addition, \((\ell_p,Y)\) has the weak maximizing property and \(Y\) contains a closed subspace linearly isometric to \(\ell_p\), then for every \(1\le r<\infty\) the following are equivalent: \((\ell_p,Y)\) has the weakly \(r\)-singular maximizing property; \((\ell_p,Y)\) has the \(r\)-convergent perturbation property; and \(r\ge p^*\).

This identifies \(p^*=p/(p-1)\) as a codomain-independent transfer exponent for the domain \(\ell_p\): above that exponent the weakly singular maximizing hierarchy collapses exactly to the ordinary weak maximizing property. When the codomain contains an isometric copy of \(\ell_p\), the same exponent is also the exact threshold for the corresponding convergent-perturbation property, provided the pair has the weak maximizing property.

## Assumptions and scope
All spaces are over the same real or complex scalar field. Fix \(1<p<\infty\), put \(p^*=p/(p-1)\), and let \(Y\) be a Banach space. A pair \((X,Y)\) has WMP when every operator \(T:X\to Y\) with a non-weakly-null maximizing sequence attains its norm. It has \(\mathrm{SMP}_r\) when every operator with a maximizing sequence containing no weakly \(r\)-summable subsequence attains its norm. It has the \(r\)-convergent perturbation property when \(T+K\) attains its norm whenever \(K\) is \(r\)-convergent and \(\|T\|<\|T+K\|\).

The first equivalence is asserted for every Banach codomain \(Y\) and every finite \(r\ge p^*\). The exact-threshold conclusion for the perturbation property additionally assumes that \((\ell_p,Y)\) has WMP and that \(Y\) contains a closed subspace linearly isometric to \(\ell_p\). No assertion is made for \(r=\infty\), where the perturbation convention changes to compact perturbations.

## Proof
Assume first that \((\ell_p,Y)\) has WMP and fix finite \(r\ge p^*\). Let \(T:\ell_p\to Y\) admit a weakly \(r\)-singular maximizing sequence \((x_n)\subset S_{\ell_p}\). Suppose for contradiction that \((x_n)\) is weakly null. The Bessaga--Pełczyński selection principle yields a subsequence \((x_{n_k})\) equivalent to a block basic sequence of the canonical basis of \(\ell_p\). Every normalized block basic sequence of the canonical basis is isometric to that basis; after harmless normalization of the comparison block sequence, \((x_{n_k})\) is therefore equivalent to the canonical basis \((e_k)\).

For \(r\ge p^*\), \((e_k)\) is weakly \(r\)-summable. Indeed, for each \(a=(a_k)\in(\ell_p)^*=\ell_{p^*}\), the scalar sequence \((a(e_k))=(a_k)\) belongs to \(\ell_r\) because \(\ell_{p^*}\subseteq\ell_r\). Weak \(r\)-summability is preserved under equivalence of basic sequences, so \((x_{n_k})\) is weakly \(r\)-summable, contradicting weak \(r\)-singularity. Thus \((x_n)\) is not weakly null, and WMP forces \(T\) to attain its norm. Hence \((\ell_p,Y)\) has \(\mathrm{SMP}_r\).

Conversely, Blanco Ardila and Miranda prove for arbitrary pairs that \(\mathrm{SMP}_r\) implies WMP. Therefore, for every finite \(r\ge p^*\),
\[
(\ell_p,Y)\text{ has WMP}\quad\Longleftrightarrow\quad(\ell_p,Y)\text{ has }\mathrm{SMP}_r.
\]
Their Proposition 4.1 also proves that \(\mathrm{SMP}_r\) implies the \(r\)-convergent perturbation property, giving the stated positive perturbation conclusion.

Now suppose in addition that \((\ell_p,Y)\) has WMP and that \(Y\) contains a closed subspace \(F\) linearly isometric to \(\ell_p\). The preceding argument gives both \(\mathrm{SMP}_r\) and the \(r\)-convergent perturbation property for every \(r\ge p^*\). If \(r<p^*\) and \((\ell_p,Y)\) had \(\mathrm{SMP}_r\), inheritance to closed codomain subspaces would give \((\ell_p,F)\) the same property, hence \((\ell_p,\ell_p)\) would have \(\mathrm{SMP}_r\), contradicting Theorem 2.2 of the focal source. Likewise, if \((\ell_p,Y)\) had the \(r\)-convergent perturbation property, Proposition 4.1(3) would pass it to \((\ell_p,F)\), contradicting the exact \((\ell_p,\ell_p)\) threshold in Examples 4.2(1). This proves the three-way equivalence under the additional hypotheses.

## Verification
The critical domain fact is the exact exponent at which the canonical basis becomes weakly summable: \((e_k)\subset\ell_p\) is weakly \(r\)-summable exactly when \(r\ge p^*\). The forward implication uses only the standard selection principle plus WMP and does not use any structure of the codomain. The reverse implication, subspace inheritance, \(\mathrm{SMP}_r\Rightarrow r\)-convergent perturbation, and the sharp negative model \((\ell_p,\ell_p)\) were checked against arXiv:2609.03988v1, specifically Proposition 2.1, Theorem 2.2, Corollary 2.3, Theorem 2.4, Proposition 4.1, and Examples 4.2.

Boundary checks: the proof requires \(1<p<\infty\) so that \(p^*<\infty\) and the classical basis/dual description applies. The threshold includes equality \(r=p^*\). The exact perturbation threshold uses isometric, not merely isomorphic, containment because the inherited subspace is compared directly with the source's \((\ell_p,\ell_p)\) model.

## Relationship to prior work
Blanco Ardila and Miranda introduce \(\mathrm{SMP}_r\), prove \(\mathrm{SMP}_r\Rightarrow\mathrm{WMP}\), characterize \((\ell_p,\ell_q)\) and \((\ell_p,c_0)\), and prove \(\mathrm{SMP}_r\Rightarrow r\)-convergent perturbation. Their positive proofs for \((\ell_p,L_p[0,1])\) and \((\ell_p,c_0)\) use the same block-basis mechanism, but the paper does not state the codomain-independent equivalence
\[
\mathrm{WMP}(\ell_p,Y)\Longleftrightarrow\mathrm{SMP}_r(\ell_p,Y)\qquad(r\ge p^*)
\]
for arbitrary \(Y\), nor the resulting exact \(r\)-convergent perturbation threshold for WMP codomains containing an isometric \(\ell_p\).

The older WMP literature establishes the underlying weak maximizing property and gives sufficient criteria for particular pairs, but predates the \(\mathrm{SMP}_r\) and \(r\)-convergent perturbation notions. Targeted searches for arbitrary-codomain formulations, equivalent threshold statements, and perturbation versions did not locate a published statement covering the theorem above.

## Limitations
The result does not classify \(\mathrm{SMP}_r\) below \(p^*\) for arbitrary codomains: below the threshold, behavior genuinely depends on \(Y\). The exact negative perturbation conclusion assumes an isometric copy of \(\ell_p\) in \(Y\); no claim is made for merely isomorphic copies. The theorem also does not assert a converse from the \(r\)-convergent perturbation property to WMP without the additional containment hypothesis.

The main originality risk is that the arbitrary-codomain implication is a short abstraction of the block-basis argument used in two examples of the focal preprint, so an equivalent observation may exist as an unindexed remark or in a later version.

## References
1. O. I. Blanco Ardila and V. C. C. Miranda, *A \(p\)-summability approach to the weak maximizing property*, arXiv:2609.03988v1, 3 September 2026.
2. R. M. Aron, D. García, D. Pellegrino and E. V. Teixeira, *Reflexivity and nonweakly null maximizing sequences*, Proc. Amer. Math. Soc. 148 (2020), 741--750.
3. F. Albiac and N. J. Kalton, *Topics in Banach Space Theory*, 2nd ed., Springer, 2016, for the Bessaga--Pełczyński selection principle and standard \(\ell_p\) basis facts.
