# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**  The result sharpens a finite sign-vector reduction already proved in Li--Xu--Yan.  Their Lemmas 2.1 and 2.2 reduce eventual equality to \(k\) boundary equations and give unique tail continuation, so counting admissible finite sign vectors is exactly the original counting problem.

The additional finite geometry was checked directly.  Writing \(T=kq+r\), the sets \(P_s\) from the source have union \(\{Q+1,\ldots,T+k-1\}\), hence \(C=\{0,\ldots,Q\}\).  Away from at most one endpoint the coefficient vector is \(1+e_{x\bmod k}\).  This gives the limiting covariance
\[
B=k^{-2}(I+(k+2)J)
\]
with diagonal \((k+3)/k^2\) and off-diagonal \((k+2)/k^2\).  The source's \(M_s=(k-1)T/k^2+O_k(1)\) supplies the common local-limit scale.

The lattice factor in the Rademacher local limit is essential and was checked explicitly:
\[
\Pr(\delta_1+\cdots+\delta_M=h)
\sim \sqrt{2/(\pi M)}e^{-h^2/(2M)}
\]
on the correct parity class.  Parity does not introduce a residue-class oscillation because the source's equation (3.2) makes \(2c_T-S_s\equiv M_s\pmod2\) identically for every boundary sign choice.  Endpoint effects are \(O_k(1)\) in the covariance and in \(M_s\), so they disappear after \(T\)-normalization.

The local-limit insertion can be justified uniformly on \(|S_s|\le T^{5/8}\) by Stirling's formula.  Hoeffding bounds make the complementary event exponentially small, while the maximal point probability of a Rademacher sum is \(O(M^{-1/2})\); hence the discarded contribution is \(o(T^{-k/2})\).  A bounded triangular-array central limit theorem then yields the Gaussian integral.  The determinant and quadratic-form simplifications were checked independently:
\[
\det(I+B/m_0)=\left(\frac{k}{k-1}\right)^k(k+3),
\qquad m_0=\frac{k-1}{k^2},
\]
and the eigenvalue of \(m_0I+B\) along the all-ones vector is \((k+3)/k\).  These identities give exactly the stated constant and Gaussian factor.

The verification artifact compares the reduced dynamic count to direct enumeration of the original boundary equations in small cases, with exact equality, and shows numerical convergence toward the predicted constants in larger cases.  This computation supports but is not used in place of the analytic proof.

## Originality

**PASS, to the best of our knowledge.**  The full text of Li--Xu--Yan arXiv:2609.20385v1 was inspected.  Its Theorem 1.2 proves only
\(N_{k,c}(T)\asymp_{k,c}2^T/T^{k/2}\), and its Corollary 1.3 gives only the corresponding order for \(f_k(t)\).  The proof uses central-binomial comparability and a second-moment bound; it does not state an asymptotic formula, an explicit leading constant, or a \(c_T\asymp\sqrt T\) limit law.

Searches were made for the exact title and arXiv identifier together with “asymptotic formula”, “exact asymptotic”, “local central limit”, the notation \(R_{1,k}\) and \(f_k(t)\), and equivalent weighted-representation terminology.  No source stating the constant
\[
\frac{2^k}{\sqrt{k+3}}\left(\frac{2k}{\pi}\right)^{k/2}
\]
or the Gaussian diffusive factor was located.

Earlier literature in the source's reference chain was also checked for stronger coverage.  Qu (2016) concerns simultaneous weighted representation identities and growth; Li--Shan--Yan (2024) concerns existence/structure for fixed eventual differences; Chen--Ding--Lü--Zhang (2024) concerns the order of the representation values themselves; Yan--Shan (2025) gives exact formulas in small threshold ranges and structural uniqueness statements.  None of the accessible statements found imply the large-threshold leading constant here.

The principal residual risk is recency: arXiv:2609.20385v1 was submitted on 17 September 2026, so a contemporaneous follow-up may not yet be indexed.  No inaccessible paper was found whose title or available metadata specifically indicates the same exact asymptotic or diffusive extension.

## Value

**PASS.**  The result changes an order-of-magnitude theorem into an exact asymptotic with a closed-form constant, sharpens the comparison of different weights to an asymptotic ratio, gives the corresponding exact constant for the Yan--Shan \(g_{k,m}(t)\) family, and identifies the natural \(\sqrt T\)-scale profile of nonzero eventual differences through an explicit Gaussian factor.  The mechanism also explains why the leading constant for fixed \(c\) is independent of \(c\): fixed offsets are negligible on the covariance scale of the boundary random vector.

## Sources checked

- Li--Xu--Yan, arXiv:2609.20385v1: abstract, Theorem 1.2, Corollaries 1.3--1.4, Remark 1.5, Lemmas 2.1--2.6, and the proof of Theorem 1.2 were inspected in full text.
- Yang--Chen (2012) and the subsequent weighted-representation literature cited by the source were searched for equivalent enumeration statements.
- Qu, *Colloq. Math.* 143 (2016), authoritative abstract and bibliographic record.
- Li--Shan--Yan, *Bull. Aust. Math. Soc.* 110 (2024), publisher abstract and bibliographic record.
- Chen--Ding--Lü--Zhang, *C. R. Math.* 362 (2024), publisher full bibliographic page and abstract.
- Yan--Shan, *Ramanujan J.* 67 (2025), bibliographic record and accessible abstract/full-text excerpt describing its exact small-threshold formulas.
- Web searches for exact and synonymous formulations of the asymptotic constant and diffusive extension.
