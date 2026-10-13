# A sharp census threshold for Bray–Curtis versus weighted UniFrac rank reversals

## Finding

Consider equal-census ecological communities with strictly positive integer counts in all three species, compared on one fixed rooted ultrametric three-tip phylogeny. The first two species are sisters; their clade branches from the root through a stem of length \(h\), whereas every leaf lies at distance \(H\) from the root, with \(0<h<H\). Put \(t=h/H\).

**Theorem (sharp rank-reversal phase boundary).** For each integer \(N\ge3\), a strict ordering between two Bray–Curtis community dissimilarities can be reversed by normalized weighted UniFrac if and only if

\[
 t(N-3)>1.
\]

The reversal can always be realized **with a common reference community**. Equivalently, the smallest admissible census for reversal at fixed \(0<t<1\) is

\[
 N_{\min}(t)=4+\left\lfloor\frac1t\right\rfloor.
\]

The inequality is strict: at \(t(N-3)=1\) no opposite strict ranks are possible. This is a universal statement about all possible integer abundance profiles, not a simulation-based or stochastic-sampling assertion.

## Assumptions and scope

Each community is a vector \(x=(x_1,x_2,x_3)\in\mathbb Z_{>0}^{3}\) with \(x_1+x_2+x_3=N\). All compared communities have the same \(N\), and all distances use the same fixed phylogenetic tree. The root-to-sister-stem edge has length \(h\); the two sister pendant edges have length \(H-h\); the outgroup edge has length \(H\). All these lengths are strictly positive.

For two such communities, Bray–Curtis dissimilarity is

\[
 B(x,y)=\frac{\sum_{i=1}^{3}|x_i-y_i|}{2N}.
\]

The **normalized weighted UniFrac** in the sense of Lozupone et al. (2007) is

\[
 U_t(x,y)=\frac{\sum_{e\in E(T)}\ell_e\,|p_e(x)-p_e(y)|}{\sum_{e\in E(T)}\ell_e\,[p_e(x)+p_e(y)]},
\]

where \(p_e(x)=N^{-1}\sum_{i\in\operatorname{desc}(e)}x_i\). Because each root-to-tip path has length \(H\), the denominator is exactly \(2H\), independently of the communities. This is not the unweighted, generalized, or absolute-abundance UniFrac normalization. A strict reversal means two comparisons have strictly opposite orders; ties do not count.

## Proof

For an ordered comparison \((x,y)\), set \(\delta_i=x_i-y_i\). Then \(\delta_1+\delta_2+\delta_3=0\). Define the integers

\[
 k=\tfrac12\bigl(|\delta_1|+|\delta_2|+|\delta_3|\bigr),\qquad
 c=\tfrac12\bigl(|\delta_1|+|\delta_2|-|\delta_3|\bigr).
\]

The triangle inequality gives \(c\ge0\). Since \(|\delta_1|+|\delta_2|-|\delta_1+\delta_2|\) is an even nonnegative integer, \(c\) is integral. Also \(0\le c\le k\). Strict positivity of the three counts in both communities implies

\[
 k=N-\sum_{i=1}^{3}\min(x_i,y_i)\le N-3.
\]

The contributions to raw weighted UniFrac come from the sister stem, the two sister pendants, and the outgroup pendant, respectively. Substituting their lengths yields

\[
 \begin{aligned}
 2H U_t(x,y)
 &=\frac1N\bigl[h|\delta_1+\delta_2|+(H-h)(|\delta_1|+|\delta_2|)+H|\delta_3|\bigr]\\
 &=\frac{2H}{N}(k-tc),
 \end{aligned}
\]

using \(|\delta_1+\delta_2|=|\delta_3|\). Therefore

\[
 \boxed{B(x,y)=\frac{k}{N},\qquad U_t(x,y)=\frac{k-tc}{N},\qquad 0\le c\le k\le N-3.}
\]

Suppose two comparisons have integer pairs \((k,c)\) and \((\ell,d)\), with \(B_1>B_2\) but \(U_1<U_2\). Then \(k>\ell\), hence \(k-\ell\ge1\), while the second inequality gives \(k-\ell<t(c-d)\). As \(d\ge0\), \(c\le k\), and \(k\le N-3\), this forces

\[
 1\le k-\ell<t(c-d)\le tc\le tk\le t(N-3).
\]

Thus no strict reversal is possible when \(t(N-3)\le1\), even if the two comparisons involve four entirely different communities.

Conversely, suppose \(t(N-3)>1\) and put \(k=N-3\). This implies \(N\ge5\), so \(k\ge2\). Consider three strictly positive abundance vectors sharing the census \(N\):

\[
 x=(k+1,1,1),\qquad y=(1,k+1,1),\qquad z=(2,1,k).
\]

For \((x,y)\), the integer parameters are \((k,c)=(k,k)\); for \((x,z)\), they are \((k-1,0)\). Consequently

\[
 B(x,y)=\frac{k}{N}>\frac{k-1}{N}=B(x,z),
\]

whereas

\[
 U_t(x,y)=\frac{k(1-t)}{N}<\frac{k-1}{N}=U_t(x,z),
\]

because \(tk>1\). This realizes a strict reversal with common reference \(x\). Finally, for integer \(N\), the condition \(N>3+1/t\) is equivalent to \(N\ge4+\lfloor1/t\rfloor\). Both directions and the equality boundary follow. \(\square\)

## Verification

An independent direct implementation of the four branch contributions was compared against the derived integer reduction. The standalone exact-rational script `verify.py` enumerates all strictly positive abundance triples with totals \(3\le N\le9\), evaluates seven rational values \(t\in\{1/6,1/4,1/3,2/5,1/2,3/4,9/10\}\), and checks existence/nonexistence of all **common-reference** rank reversals against the theorem. It checks **10,584 ordered pair identities** and **218,484 ordered three-community candidate comparisons**. Executing `python verify.py` returned:

```
VERIFY_OK pair identities 10584 ordered comparison checks 218484
```

For the smallest attainable census, take \(N=5\), \(t=3/4\), and the common reference \(x=(3,1,1)\), with \(y=(1,3,1)\) and \(z=(2,1,2)\). Then \(B(x,y)=2/5>B(x,z)=1/5\), while \(U_t(x,y)=1/10<U_t(x,z)=1/5\). The enumeration corroborates the proof over a finite test domain; it is not the basis for the theorem for arbitrary \(N\).

## Relationship to prior work

Bray and Curtis (1957) established the census-overlap similarity underlying the Bray–Curtis distance. Lozupone et al. (2007) introduced weighted UniFrac and its root-distance normalization, and Evans and Matsen (2010 preprint; 2012 journal publication) established its tree-transport interpretation. Their formulas supply the correct starting definitions, **not** this integer-census ordering theorem. Schmidt, Rodrigues and von Mering (2016/2017) compared traditional and phylogenetic diversity indices while developing other indices; their inspected comparison does not give a universal three-tip finite-census ranking criterion. Roldán Ahumada and Avendaño Garrido (2019) studied small-sample metric properties of UniFrac, not Bray–Curtis ordering relative to normalized weighted UniFrac. Pendleton and Schmidt (2026) provide four-taxon simulations comparing Bray–Curtis and various UniFrac versions, but not an all-census sharp threshold on a rooted three-tip ultrametric tree. The novelty proposed here is **only the exact global rank-reversal boundary and matching shared-reference construction**, not weighted UniFrac itself or its known transport formula.

## Limitations

The result is limited to equal integer censuses, presence of all three species in every community, one rooted three-tip **ultrametric** tree with a positive nontrivial sister stem, and normalized relative-abundance weighted UniFrac. It does not quantify statistical sampling variability or guarantee reversal in observed data; it characterizes when reversal is mathematically possible. Four or more species, unequal censuses, absent species, non-ultrametric lengths, and other UniFrac definitions require separate analysis. The published literature search cannot exclude unindexed equivalent results in general transport-metric or order-equivalence theory, and the result has not been independently audited.

## References

1. Bray, J. R., and Curtis, J. T. (1957). “An Ordination of the Upland Forest Communities of Southern Wisconsin.” *Ecological Monographs* 27(4), 325–349. DOI: 10.2307/1942268. First published 1957-10-01.
2. Lozupone, C. A., Hamady, M., Kelley, S. T., and Knight, R. (2007). “Quantitative and Qualitative β Diversity Measures Lead to Different Insights into Factors That Structure Microbial Communities.” *Applied and Environmental Microbiology*. DOI: 10.1128/AEM.01996-06.
3. Evans, S. N., and Matsen, F. A. “The phylogenetic Kantorovich–Rubinstein metric for environmental sequence samples.” arXiv:1005.1699v1 (2010); *JRSS B* 74(3), 569–592 (2012). DOI: 10.1111/j.1467-9868.2011.01018.x.
4. Schmidt, T. S. B., Rodrigues, J. F. M., and von Mering, C. (2017). “A family of interaction-adjusted indices of community similarity.” *The ISME Journal*. DOI: 10.1038/ismej.2016.139. First available 2016-12-09.
5. Roldán Ahumada, J. A., and Avendaño Garrido, M. L. (2019). “A Commentary on Diversity Measures UniFrac in Very Small Sample Size.” *Evolutionary Bioinformatics*. DOI: 10.1177/1176934319843515.
6. Pendleton, A., and Schmidt, M. L. (2026). “Interpreting UniFrac with absolute abundance: a conceptual and practical guide.” *ISME Communications*. DOI: 10.1093/ismeco/ycaf250.
