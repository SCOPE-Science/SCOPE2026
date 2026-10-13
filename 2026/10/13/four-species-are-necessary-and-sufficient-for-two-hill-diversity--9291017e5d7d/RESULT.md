# Four species are necessary and sufficient for two Hill-diversity profile reversals

## Finding

Let \(s\geq 2\). Two communities each having exactly \(s\) positive species proportions and different multisets of proportions have **at most \(s-2\) distinct ties** between their Hill-diversity profiles at finite sensitivity orders \(q>0\), with the continuous Shannon-order definition at \(q=1\). In particular, no pair of two- or three-species communities can reverse relative Hill-diversity ranking twice as \(q\) varies.

Four species suffice for two actual reversals. The positive integer abundance vectors
\[
P=(994,2014,2989,4003),\qquad Q=(1000,2000,3000,4000)
\]
share total abundance \(10{,}000\). Their Hill profiles intersect **exactly twice** on \(q>0\), once in \((2,3)\) and once in \((3,4)\); each intersection changes the relative ordering. Appending the same positive-abundance species to both vectors preserves these two reversals at all larger species counts.

## Assumptions and scope

A community has strictly positive proportions \(p_1,\ldots,p_s\), with \(\sum_i p_i=1\). Its classical Hill diversity is
\[
D_q(p)=\left(\sum_{i=1}^s p_i^q\right)^{1/(1-q)}\quad (q>0,\ q\neq1),
\qquad D_1(p)=\exp\left(-\sum_{i=1}^s p_i\log p_i\right).
\]
Only finite positive sensitivity orders are considered; \(q=0\) and \(q=\infty\) are excluded. The theorem concerns classical abundance-only diversity, not similarity-weighted or phylogenetic diversity. A tie is a value where \(D_q(p)=D_q(r)\). Profiles identical under permutation of entries are excluded from the finite tie-count theorem.

## Proof

**1. A variation bound for sorted abundance vectors.** Permute both vectors into nondecreasing order \(p_1\le\cdots\le p_s\) and \(r_1\le\cdots\le r_s\). Define
\[
h(t)=\sum_{i=1}^s\bigl({\bf1}_{p_i>t}-{\bf1}_{r_i>t}\bigr),\qquad t>0.
\]
The \(i\)-th summand is zero or is constant \(+1\) on the interval between \(r_i\) and \(p_i\) when \(p_i>r_i\), or constant \(-1\) on the interval between \(p_i\) and \(r_i\) when \(p_i<r_i\). If two summands of opposite signs have indices \(i<j\), their supporting intervals are disjoint and the first lies weakly to the left of the second: in the positive-then-negative case use \(p_i\le p_j\), and in the negative-then-positive case use \(r_i\le r_j\). Therefore the nonzero sign regions of \(h\), viewed left to right, alternate at most \(s-1\) times. Indeed, representatives from successive alternating regions require distinct strictly increasing supporting indices. Since all entries are positive, \(h\) has compact support bounded away from zero.

**2. Mellin-transform zero lemma.** Suppose \(h\) is a nonzero integrable compactly supported real function on \((0,\infty)\), supported away from zero, with at most \(m\) sign changes. Then
\[
M(z)=\int_0^\infty t^z h(t)\,dt
\]
has at most \(m\) real zeros, counted with multiplicity. For clarity, here is a proof. Assume at least \(m+1\) zeros including multiplicities, and select \(m+1\) corresponding functions \(t^{\lambda}(\log t)^j\), taking \(j=0,\ldots,d-1\) at a root of multiplicity \(d\). Their integrals against \(h\) all vanish. On writing \(y=\log t\), these \(m+1\) functions become exponential polynomials \(e^{\lambda y}y^j\) with real, ordered exponents. Every nonzero linear combination of \(N\) such confluent exponentials has at most \(N-1\) real zeros counted with multiplicity: induction on \(N\) divides by the exponential with smallest exponent and differentiates, reducing the dimension by one; Rolle's theorem completes the induction. Choose a nonzero linear combination \(g\) vanishing at the \(m\) boundaries between successive nonzero sign regions of \(h\). Such a combination exists because there are \(m+1\) basis functions. The zero bound makes these its only zeros, all simple; thus, after changing its overall sign, \(g(t)h(t)>0\) on the nonzero intervals of \(h\), contradicting \(\int gh=0\). When \(h\) has fewer than \(m\) sign changes, use its actual number in the same argument.

**3. The compulsory normalization zero.** Put
\[
F(q)=\sum_{i=1}^s p_i^q-\sum_{i=1}^s r_i^q.
\]
Integration of \(u^q=q\int_0^u t^{q-1}dt\) for \(q>0\) gives \(F(q)=qM(q-1)\). The normalization \(\sum p_i=\sum r_i=1\) yields \(M(0)=0\). Step 1 and the zero lemma give at most \(s-1\) real zeros of \(M\), counting multiplicity. If \(M\equiv0\), then the finite exponential sum \(F\) is identically zero, forcing equal multisets of entries by successive dominance of the largest distinct entry; this case was excluded.

**4. Translation to Hill ties, including Shannon order.** For \(q\ne1\), \(D_q(p)=D_q(r)\) if and only if \(F(q)=0\), hence if and only if \(M(q-1)=0\). At \(q=1\), the equality of Shannon Hill diversities is equivalent to \(F'(1)=0\), which is \(M'(0)=0\) because \(F(q)=qM(q-1)\) and \(M(0)=0\). Thus every tie with \(q\ne1\) costs an additional zero of \(M\) besides the compulsory zero at zero; a tie at \(q=1\) costs a further unit of multiplicity at the compulsory zero. Hence there are at most \(s-2\) distinct ties with \(q>0\). In particular, this also bounds strict changes of ranking, as each requires a tie by continuity.

**5. A sharp four-species witness.** Let \(P,Q\) be the displayed integer abundance vectors and divide each coordinate by \(10{,}000\). Direct exact integer arithmetic gives
\[
\begin{aligned}
\sum P_i^2-\sum Q_i^2&=2362>0,\\
\sum P_i^3-\sum Q_i^3&=-517776<0,\\
\sum P_i^4-\sum Q_i^4&=16323602434>0.
\end{aligned}
\]
For \(q>1\), the Hill-number order reverses the order of the corresponding power sums, because \(1/(1-q)<0\). Thus \(D_2(P)<D_2(Q)\), \(D_3(P)>D_3(Q)\), and \(D_4(P)<D_4(Q)\), where the notation denotes the normalized frequencies. Continuity forces two distinct roots between these successive integer orders. The \(s-2=2\) upper bound proves that these are the **only** positive-order roots. The multiplicity bound moreover forces both roots to be simple and therefore genuine sign reversals. Appending the same fixed positive abundance to both integer lists, before common renormalization, adds equal terms to both power sums and preserves the zero and sign pattern for every \(q>0\). This establishes the minimum of four species for two reversals and its persistence at larger species counts.

## Verification

The accompanying `verify_hill_crossings.py` requires only Python 3 and standard-library modules. Run `python3 verify_hill_crossings.py`; the expected terminal line begins with `VERIFY_OK`. It checks the exact witness power-sum differences, its count-function sign profile, the common-padding identity, and a nontrivial finite sweep over small positive integer abundance profiles. The finite sweep illustrates, but does **not** prove, the universal zero bound, which rests on the preceding analytic argument.

## Relationship to prior work

Hill (1973) introduced the continuous effective-number family and its Shannon limit. Patil and Taillie (1982), especially their Sections 6–7, developed partial orders and a crossing-point analysis for controlled community perturbations; that crossing theorem is not a general bound on the number of Hill-profile intersections for any fixed species count. Leinster and Cobbold (2012), Section 5 and Figure 2(iii), explicitly discuss examples with two profile crossings and the absence of a species-independent upper bound; their paper does not establish a sharp four-species minimum or the \(s-2\) bound. Aw and Rosenberg (2018) and Gress and Rosenberg (2024) derive extremal Rényi/Hill bounds conditional on maximum abundance, rather than intersection-count bounds for two arbitrary communities. The present result quantifies the **minimum species support for double ranking reversal** and gives the explicit support-dependent finite bound.

## Limitations

The bound requires equal, fixed finite species counts and strictly positive proportions. It does not apply without modification to two communities of different support sizes, similarity-weighted Hill numbers, uncertainty in observed frequencies, or the limiting order \(q=\infty\). Although the analytic bound is exact, sharpness of \(s-2\) for every \(s>4\) is not asserted. An indexed or unindexed stronger general entropy-order theorem could subsume the result; existing searches cannot rule this out. No independent mathematical audit has been performed.

## References

1. Hill, M. O. (1973), *Diversity and Evenness: A Unifying Notation and Its Consequences*, Ecology **54**, 427–432. DOI 10.2307/1934352; publicly dated 1973-03-01. https://doi.org/10.2307/1934352
2. Patil, G. P. and Taillie, C. (1982), *Diversity as a Concept and its Measurement*, Journal of the American Statistical Association **77**, 548–561. DOI 10.1080/01621459.1982.10477845. https://ricottalab.com/wp-content/uploads/2015/10/patil-taillie-1982.pdf
3. Leinster, T. and Cobbold, C. A. (2012), *Measuring diversity: the importance of species similarity*, Ecology **93**, 477–489. DOI 10.1890/10-2402.1. Author manuscript: https://www.maths.gla.ac.uk/~cc/pdf/Leinster2011.pdf
4. Gress, T. D. and Rosenberg, N. A. (2024), *Mathematical constraints on a family of biodiversity measures via connections with Rényi entropy*, BioSystems **237**, 105153. DOI 10.1016/j.biosystems.2024.105153. https://web.stanford.edu/group/rosenberglab/papers/GressRosenberg2024-BioSystems.pdf
5. Tóthmérész, B. (1995), *Comparison of different methods for diversity ordering*, Journal of Vegetation Science **6**, 283–290. DOI 10.2307/3236223. https://doi.org/10.2307/3236223

6. Aw, A. J. and Rosenberg, N. A. (2018), *Bounding measures of genetic similarity and diversity using majorization*, Journal of Mathematical Biology **77**, 711–737. DOI 10.1007/s00285-018-1226-x. https://rosenberglab.stanford.edu/papers/AwRosenberg2018-JMathBiol.pdf
