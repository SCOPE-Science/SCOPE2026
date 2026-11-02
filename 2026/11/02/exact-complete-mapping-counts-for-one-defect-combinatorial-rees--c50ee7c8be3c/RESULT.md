# Exact complete-mapping counts for one-defect combinatorial Rees zero-matrix semigroups

## Finding
For integers \(m,n\ge 2\), let \(I\) and \(\Lambda\) have cardinalities \(m\) and \(n\), and let \(P\) be an \(n\times m\) zero-one matrix whose entries are all one except one zero. Let \(S=M^0(\{1\},I,\Lambda,P)\). The number \(C_{m,n}\) of bijections \(\alpha:S\to S\) for which \(x\mapsto x\alpha(x)\) is bijective is exactly
\[
C_{m,n}=(n!)^m(m!)^n\sum_{r=0}^{\min(m,n)}\frac{(-1)^r(m)_r(n)_r}{r!(mn)^r},
\]
where \((k)_r=k(k-1)\cdots(k-r+1)\), with \((k)_0=1\). The count depends only on \(m,n\), not on the location of the zero. For the corresponding all-one sandwich matrix the count is \((n!)^m(m!)^n\).

Consequently the ratio of the one-defect count to the full-support count tends to \(e^{-1}\) as \(m,n\to\infty\) jointly. Holding \(m\) fixed and sending \(n\to\infty\) gives \((1-1/m)^m\); holding \(n\) fixed and sending \(m\to\infty\) gives \((1-1/n)^n\). Thus deleting a single one from the sandwich matrix eliminates an asymptotically positive proportion \(1-e^{-1}\) of the complete mappings when both index sets grow.

## Assumptions and scope
The multiplication on \(S=\{0\}\cup(I\times\Lambda)\) is defined, for \(i,j\in I\) and \(\lambda,\mu\in\Lambda\), by
\[
(i,\lambda)(j,\mu)=\begin{cases}(i,\mu),&P_{\lambda j}=1,\\0,&P_{\lambda j}=0,\end{cases}
\]
with absorbing zero. The unique zero entry is \(P_{\lambda_0j_0}=0\). A complete mapping means a bijection \(\alpha:S\to S\) such that the product map \(\theta(x)=x\alpha(x)\) is also a bijection. The index sets are labelled; the count is of actual bijections, not conjugacy classes. Since \(m,n\ge2\), no row or column of \(P\) vanishes.

## Proof
First consider the all-one sandwich matrix. Since \(\theta(0)=0\) and \(\theta\) is bijective, no nonzero element can map under \(\theta\) to zero. Likewise \(\alpha(0)=0\): the unique preimage of zero under \(\alpha\) cannot be nonzero, since its product with zero would force a second zero value of \(\theta\). Thus \(\alpha\) permutes the nonzero elements.

For each fixed \(i\in I\), the first coordinate of \(\theta(i,\lambda)\) is always \(i\). As \(\theta\) is a bijection, its second coordinate for fixed \(i\) is \(\pi_i(\lambda)\) for a permutation \(\pi_i\in\operatorname{Sym}(\Lambda)\). Write
\[
\alpha(i,\lambda)=\bigl(\sigma_{\pi_i(\lambda)}(i),\pi_i(\lambda)\bigr).
\]
For each \(\mu\in\Lambda\), the values of the first coordinate of \(\alpha\) over the \(m\) source elements having \(\pi_i(\lambda)=\mu\) must be distinct. Hence \(\sigma_\mu\in\operatorname{Sym}(I)\). Conversely any \(m\) choices of \(\pi_i\) and \(n\) choices of \(\sigma_\mu\) produce a bijection \(\alpha\) with bijective \(\theta\) for the all-one matrix. The number of such permutation systems is therefore \((n!)^m(m!)^n\).

For the one-defect matrix the same parametrization is necessary, because the product \(\theta\) must avoid zero on all nonzero elements; and it is sufficient provided
\[
\sigma_{\pi_i(\lambda_0)}(i)\ne j_0\qquad(i\in I).
\]
Select the full-support permutation systems uniformly. For each \(i\in I\) let \(E_i\) be the failure event \(\sigma_{\pi_i(\lambda_0)}(i)=j_0\). If \(T\subseteq I\) has \(r\) elements, simultaneous occurrence of all events \(E_i\) for \(i\in T\) requires the \(r\) independent values \(\pi_i(\lambda_0)\) to be distinct; otherwise a single permutation \(\sigma_\mu\) would map two different inputs to \(j_0\). The probability of distinctness is \((n)_r/n^r\), interpreted as zero when \(r>n\). Conditional on distinctness, the corresponding \(r\) independent permutations \(\sigma_\mu\) hit the prescribed target independently, each with probability \(1/m\). Thus
\[
\Pr\!\left(\bigcap_{i\in T}E_i\right)=\frac{(n)_r}{(mn)^r}.
\]
Inclusion-exclusion over the \(m\) events gives the asserted ratio
\[
\Pr\!\left(\bigcap_{i\in I}E_i^c\right)
=\sum_{r=0}^{\min(m,n)}(-1)^r\binom mr\frac{(n)_r}{(mn)^r}
=\sum_{r=0}^{\min(m,n)}\frac{(-1)^r(m)_r(n)_r}{r!(mn)^r}.
\]
Multiplication by the full-support count proves the exact enumeration. Relabelling \(I\) and \(\Lambda\) moves any unique zero to any other position.

For joint growth, every unsigned summand is bounded by \(1/r!\), and for each fixed \(r\), \((m)_r(n)_r/(mn)^r\to1\). Extending summands by zero beyond \(\min(m,n)\), dominated convergence for the series yields \(\sum_{r\ge0}(-1)^r/r!=e^{-1}\). When \(m\) is fixed, the limit is the binomial sum \(\sum_{r=0}^{m}(-1)^r\binom mr m^{-r}=(1-1/m)^m\); the other fixed-parameter limit is symmetric. This completes the proof.

## Verification
The standalone script `verify_complete_maps_missing_edge.py` exhaustively enumerates every permutation of the nonzero elements and directly computes the product map for \((m,n)=(2,2),(2,3),(3,2),(3,3)\). Observed defect-one counts are, respectively, \(2,48,48,9984\), matching the formula. It independently checks the all-one counts \(16,288,288,46656\). The script uses only Python's standard library and reports `VERIFY_OK`. These finite tests corroborate but do not replace the all-parameter argument.

## Relationship to prior work
Araújo, Bentz, Cameron, Hendrey, and Kinyon (2026) introduce and study complete mappings of finite semigroups. Their Theorem 6.2 gives an existence criterion for combinatorial Rees zero-matrix semigroups in terms of balanced support; their Proposition 6.5 enumerates mappings of Brandt semigroups using Latin squares. The present all-one-minus-one support pattern is neither the Brandt diagonal pattern nor an existence-only claim; it supplies a closed cardinality formula and a nontrivial joint-size survival limit. The counting uses standard inclusion-exclusion after a permutation parametrization.

## Limitations
The formula is restricted to trivial maximal subgroup and exactly one missing sandwich-matrix entry, with \(m,n\ge2\). It does not enumerate complete mappings for arbitrary zero-one support patterns, nontrivial groups, or conjugacy classes. The source comparison does not establish absolute historical novelty: an earlier combinatorial enumeration under transversal, rook-theoretic, or matching terminology could imply this special case. The proof is elementary and does not claim any classification of all Rees zero-matrix semigroups.

## References
Araújo, João; Bentz, Wolfram; Cameron, Peter J.; Hendrey, Kevin; Kinyon, Michael. *Complete Mappings of Semigroups*, arXiv:2608.25092v1, first public 2026-08-25, https://arxiv.org/abs/2608.25092 (especially §1, Theorem 6.2, and Proposition 6.5).
