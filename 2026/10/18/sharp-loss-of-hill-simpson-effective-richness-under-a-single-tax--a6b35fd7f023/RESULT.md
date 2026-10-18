# Sharp loss of Hill–Simpson effective richness under a single taxonomic merger

## Finding

For each integer \(n\ge3\), take an ecological assemblage with \(n\) strictly positive relative species abundances \(p_1,\ldots,p_n\), normalized by \(\sum_{i=1}^{n}p_i=1\). Its order-two Hill diversity (inverse Simpson concentration) is
\[
D_2(p)=\left(\sum_{i=1}^{n}p_i^2\right)^{-1}.
\]
Combine exactly two species labels into one taxonomic category, adding their abundances and leaving the others unchanged. Let \(\Delta_n(p)\) be the resulting decrease in \(D_2\). Write \(q=n-2\), and let \(z_q\in(0,2/3)\) be the **unique** positive solution of
\[
q^2z_q^4+4qz_q^3+12z_q=8.
\]
Then the sharp, attained bound is
\[
\boxed{\max_{p_i>0,\,\sum p_i=1}\Delta_n(p)
=M_n:=\frac{2(2+qz_q)^2}{(2+qz_q^2)(4+qz_q^2)}.}
\]
Up to interchanging the merged labels and permuting the other labels, the **unique** maximizer is
\[
\boxed{p_1=p_2=\frac{1}{2+qz_q},\qquad
p_3=\cdots=p_n=\frac{z_q}{2+qz_q}.}
\]
In particular, each of the two merged species is individually more abundant than each remaining species. The maximum absolute loss has the sharp asymptotic law
\[
\boxed{\lim_{n\to\infty}\frac{M_n}{n-2}=3-2\sqrt2\approx0.1715728752538.}
\]
Nevertheless, for every positive abundance profile, the **relative** diversity loss is strictly below one half; the bound one half is sharp as a supremum. An equal-abundance community instead loses only \(2n/(n+2)\) effective species under one merger, a quantity bounded by two. Thus a single taxonomic merger can eliminate an asymptotically linear number of *effective* species in an optimally heterogeneous community even though recorded species richness falls by exactly one.

## Assumptions and scope

The \(n\) categories are known species with real, strictly positive relative abundances. The operation replaces two categories of abundances \(a,b\) by one category of abundance \(a+b\), without altering the underlying assemblage, total mass, or any other abundance. There are no stochastic sampling errors, environmental changes, taxonomic splitting, or repeated mergers. A relabeling of the original categories does not change the problem, so the merged pair may be taken as categories one and two. The bound is a maximum, not merely a supremum, for every fixed finite \(n\ge3\).

## Proof

**Exact merger identity.** Put \(a=p_1\), \(b=p_2\), \(R=\sum_{i=3}^n p_i^2\), \(u=a+b\), and \(S=a^2+b^2+R=u^2-2ab+R\). After merging, Simpson concentration is \(S+2ab=u^2+R\). Therefore
\[
\Delta_n(p)=\frac1S-\frac1{S+2ab}
=\frac{2ab}{S(S+2ab)}.
\]
This also proves that every genuine merger strictly decreases order-two Hill diversity.

**Reduction to two abundance levels.** Fix \(0<u<1\). With \(u\) and \(R\) fixed, the difference \(1/(u^2-2ab+R)-1/(u^2+R)\) is strictly increasing in \(ab\). The elementary inequality \(ab\le u^2/4\) is an equality exactly when \(a=b=u/2\). With \(u\) and \(ab>0\) fixed, the derivative of the same difference with respect to \(R\) is
\[
-\frac1{(u^2-2ab+R)^2}+\frac1{(u^2+R)^2}<0.
\]
By Cauchy–Schwarz, \(R\ge(1-u)^2/q\), with equality exactly when all \(q\) untouched abundances coincide. Both symmetrizations are therefore strictly improving unless already satisfied. Consequently, every global maximizer must have the form \((t,t,s,\ldots,s)\) for positive \(t,s\) with \(2t+qs=1\).

**Unique global optimum.** Let \(z=s/t>0\). The normalization gives \(t=(2+qz)^{-1}\) and \(s=z/(2+qz)\), and direct substitution yields
\[
F_q(z):=\Delta_n(t,t,s,\ldots,s)
=\frac{2(2+qz)^2}{(2+qz^2)(4+qz^2)}.
\]
Its derivative factors *exactly* as
\[
F_q'(z)=
\frac{-4q(2+qz)\big(q^2z^4+4qz^3+12z-8\big)}
{(2+qz^2)^2(4+qz^2)^2}.
\]
The polynomial \(P_q(z)=q^2z^4+4qz^3+12z-8\) has derivative \(4q^2z^3+12qz^2+12>0\) for every \(z\ge0\), satisfies \(P_q(0)=-8\), and is positive at \(z=2/3\). It therefore has exactly one positive zero \(z_q\in(0,2/3)\). The derivative of \(F_q\) is strictly positive before this zero and strictly negative after it. As \(F_q(0)=1\) by continuity and \(F_q(z)\to0\) as \(z\to\infty\), this unique interior critical point is the unique global maximum. The strict equality conditions in the preceding reduction prove uniqueness up to the allowed relabelings, and the formula for \(M_n\) follows.

**Large-\(n\) asymptotics.** The zero equation implies \(0<q^2z_q^4\le8\), hence \(z_q=O(q^{-1/2})\). It follows that \(qz_q^3\to0\) and \(z_q\to0\). Passing to the limit in the zero equation gives \(q^2z_q^4\to8\), or \(qz_q^2\to2\sqrt2\). Therefore
\[
\frac{M_n}{q}=
\frac{2(2+qz_q)^2/q}{(2+qz_q^2)(4+qz_q^2)}
\longrightarrow\frac{4\sqrt2}{(2+2\sqrt2)(4+2\sqrt2)}
=3-2\sqrt2.
\]
There is no claim that the normalized extremizers converge to a fixed finite-species community.

**Relative bound and evenness comparison.** The fraction of diversity lost equals \(2ab/(S+2ab)\). Since \(S\ge a^2+b^2\ge2ab\), it is at most \(1/2\), strictly less when \(n\ge3\) and all species are present. Letting the other abundances tend to zero and \(a,b\) tend to \(1/2\) shows sharpness of the supremum. At \(p_i=1/n\), Simpson concentration increases from \(1/n\) to \((n+2)/n^2\), so the exact effective-richness loss is \(n-n^2/(n+2)=2n/(n+2)\). Finally, \(M_3\approx1.314056108733>1\), so the loss from merging just two taxa can already exceed one effective species in a three-species community.

## Verification

The standalone `check_hill_merge.py` uses only Python's standard library. It checks the rational-polynomial derivative factorization for eight integer values of \(q\), evaluates the unique quartic root by 260 steps of 70-digit decimal bisection, compares the claimed optimum against 59,776 strictly positive rational abundance profiles (including exhaustive small grids), checks the one-half relative bound for those profiles, and tests the large-\(n\) asymptotic coefficient numerically. Its run prints `PASS`. These finite computations are corroboration only: the strict symmetrization, uniqueness, sharpness and all-\(n\) limit are analytic and do not depend on a numerical root finder or random search. Reproduce with `python3 check_hill_merge.py`.

## Relationship to prior work

Hill's original diversity-number paper (1973) defines the inverse-Simpson effective number and studies what happens when *every* species is duplicated or paired into a coarser collection. It does not state the global worst-case loss from combining **one** pair while allowing all remaining abundances to vary. Bozzuto and Blanckenhorn (published online 2016) study taxonomic resolution and biodiversity effects under fixed taxonomic structures and mortality scenarios, including order-two Hill diversity; their reported analyses are not an extremal all-abundance, all-dimension theorem for one arbitrary pair. Ricotta and Feoli (2024) discuss the interpretation and nonlinearity of Hill numbers, not this coarsening extremum. The well-known Herfindahl concentration merger identity \(\Delta H=2ab\) supplies the initial algebraic identity but not the maximizing abundance profile, its unique quartic characterization, or the linear worst-case asymptotic for reciprocal concentration. The result should not be confused with bounds on *pairwise niche overlap*, with comparisons of different Hill orders between two communities, or with sensitivity of sampled richness to rarefaction.

## Limitations

This theorem quantifies a measurement artifact under perfectly known positive abundances, not actual extinction or an ecological causal effect. It assumes exactly one additive two-taxon merger, equal status of all other taxa, and the order-two Hill diversity; it does not characterize simultaneous multiple mergers, other Hill orders, uncertainty in abundance estimates, or biologically permitted taxonomic hierarchies. The extremizing real proportions need not be exactly representable as counts in a prescribed finite integer census. The bibliographic comparison is literature-based and not independent certification of novelty; an unlocated equivalent optimization under reciprocal Herfindahl concentration terminology remains a residual risk.

## References

- Hill, M. O. (1973). *Diversity and evenness: A unifying notation and its consequences*. Ecology **54**(2), 427–432. DOI: `10.2307/1934352`. Public full text: `https://ricottalab.com/wp-content/uploads/2015/10/hill-1973.pdf`.
- Bozzuto, C., and Blanckenhorn, W. U. (2017; first online 2016-12-11). *Taxonomic resolution and treatment effects – alone and combined – can mask significant biodiversity reductions*. International Journal of Biodiversity Science, Ecosystem Services & Management **13**, 86–99. DOI: `10.1080/21513732.2016.1260638`.
- Ricotta, C., and Feoli, E. (2024). *Hill numbers everywhere. Does it make ecological sense?* Ecological Indicators **161**, 111971. DOI: `10.1016/j.ecolind.2024.111971`.
- Federal Trade Commission / Department of Justice (2010). *Horizontal Merger Guidelines*, §5.3, concentration-index change. Public source: `https://www.ftc.gov/sites/default/files/documents/public_events/horizontal-merger-guidelines-review-project/100420hmg_3.pdf`.
