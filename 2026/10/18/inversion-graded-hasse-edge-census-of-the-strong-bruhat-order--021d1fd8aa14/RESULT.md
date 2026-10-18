# Inversion-graded Hasse-edge census of the strong Bruhat order

## Finding
Let \(n\ge2\), let \(\mathfrak S_n\) carry the strong Bruhat order, and let \(\ell(\pi)\) denote inversion number. For every cover \(\pi\lessdot\sigma\), weight the edge by \(q^{\ell(\pi)}\) and record the distance between the two swapped positions. Set \([k]_q=1+q+\cdots+q^{k-1}\) and \([n]_q!=\prod_{k=1}^n[k]_q\). The polynomial enumerating *all* Hasse edges by the inversion rank of their lower endpoint is

\[
E_n(q):=\sum_{\pi\lessdot\sigma}q^{\ell(\pi)}
=[n]_q!\sum_{d=1}^{n-1}(n-d)\frac{d q^{d-1}}{[d]_q[d+1]_q}.
\]

More finely, the sum \(E_{n,d}(q)\) over covers obtained by swapping positions at distance \(d\) is exactly

\[
E_{n,d}(q)=(n-d)d q^{d-1}\frac{[n]_q!}{[d]_q[d+1]_q}
\qquad(1\le d\le n-1).
\]

These rationally displayed expressions are polynomials with nonnegative integer coefficients, since they enumerate edges. They give every rank-by-rank edge count, not just the aggregate number of edges. They are reciprocal of degree \(\binom n2-1\).

For \(q>0\), draw \(\Pi\) from the Mallows inversion-weighted probability law \(\mathbb P_q(\Pi=\pi)=q^{\ell(\pi)}/[n]_q!\). Its expected upward Bruhat degree is the explicit finite sum

\[
\mu_n(q)=\mathbb E_q\,d_+(\Pi)
=\sum_{d=1}^{n-1}(n-d)\frac{d q^{d-1}}{[d]_q[d+1]_q}.
\]

Two qualitative consequences are exact. First, for every \(n\ge4\), at least one global maximizer of \(\mu_n(q)\) over \(q\ge0\), and in fact every global maximizer, lies strictly between zero and one: neither a nearly sorted deterministic permutation nor the uniform law maximizes the expected number of upward covers. Second, for each fixed \(q>0\), \(q\ne1\), one has \(\mu_n(q)=\Theta_q(n)\), whereas at \(q=1\) one has \(\mu_n(1)\sim n\log n\). Thus the uniform parameter is the unique *fixed-parameter* point of superlinear expected degree.

## Assumptions and scope
The group is the full finite symmetric group on \([n]\), with distinct entries, ordinary inversion length, and *strong* (not weak) Bruhat covers. A cover is counted once, directed upward, and its rank weight belongs to the lower element. The position gap is \(d=j-i\), not a difference of entry values. The variable \(q\) is a formal indeterminate for \(E_n(q)\); the Mallows assertions apply to positive real \(q\), extended continuously to \(q=0\) and with limits as \(q\to\infty\). The reciprocal polynomial has degree \(\binom n2-1\), not \(\binom n2\).

## Proof
For a permutation \(\pi=(\pi_1,\ldots,\pi_n)\) and positions \(i<j\), interchanging the entries increases inversion number by precisely
\[
1+2\#\{k:i<k<j,\ \pi_i<\pi_k<\pi_j\}
\]
when \(\pi_i<\pi_j\). Thus \(i,j\) define an upward strong-Bruhat cover exactly when the two endpoint values increase and no intermediate value lies strictly between them. This is the boxed \(12\) criterion.

Fix a gap \(d=j-i\), and restrict attention to the consecutive block of \(d+1\) positions from \(i\) through \(j\). Under Mallows weighting, the standardized relative order inside any consecutive block has Mallows parameter \(q\). To verify this directly, condition on the set of values occupying the block and the ordered outside entries. Since the block positions are consecutive, inversions between block entries and outside entries depend only on that value set and the outside positions, not on the internal arrangement. Therefore the conditional weight of a block pattern is proportional to \(q\) raised to its internal inversion count. Its normalizer is \([d+1]_q!\).

The two block endpoints are in a cover relation precisely when their ranks among those \(d+1\) values are \(a,a+1\), in that order, for some \(1\le a\le d\). All other \(d-1\) ranks can appear in any order in the interior. The contribution of endpoint/interior inversions is \((a-1)+(d-a)=d-1\), independent of \(a\); the internal inversion generating function is \([d-1]_q!\). Summing over the \(d\) choices of \(a\), the weighted fraction of eligible blocks is
\[
p_d(q)=\frac{d q^{d-1}[d-1]_q!}{[d+1]_q!}
=\frac{d q^{d-1}}{[d]_q[d+1]_q}.
\]
There are exactly \(n-d\) position pairs of gap \(d\). Summing their indicator expectations proves the claimed Mallows mean. Multiplying by the Mallows partition function \([n]_q!\) proves both polynomial identities, with no asymptotic step.

The identity \([k]_{1/q}=q^{1-k}[k]_q\) gives \(p_d(1/q)=q p_d(q)\). Therefore \(\mu_n(1/q)=q\mu_n(q)\), and in particular any parameter \(q>1\) has strictly smaller mean than its reciprocal in \((0,1)\). Near \(q=0\), the first three gap regimes give \(p_1(q)=1-q+O(q^2)\), \(p_2(q)=2q+O(q^2)\) and \(p_d(q)=O(q^2)\) for \(d\ge3\), hence
\[
\mu_n(q)=(n-1)+(n-3)q+O_n(q^2).
\]
For \(n\ge4\) the right derivative at zero is positive. At \(q=1\), logarithmic differentiation of each \(p_d\) yields \(p_d'(1)=-p_d(1)/2\), because \([k]_1=k\) and \([k]'_1=k(k-1)/2\). Thus \(\mu_n'(1)=-\mu_n(1)/2<0\). Continuity, compactness after adjoining the endpoints \(0,\infty\), and \(\lim_{q\to\infty}\mu_n(q)=0\) show that every global maximizer for \(n\ge4\) lies in \((0,1)\).

At \(q=1\), \(p_d(1)=1/(d+1)\), so
\[
\mu_n(1)=\sum_{d=1}^{n-1}\frac{n-d}{d+1}
=(n+1)H_n-2n\sim n\log n,
\]
where \(H_n=\sum_{k=1}^n1/k\). For fixed \(q\ne1\), put \(\rho=\min\{q,q^{-1}\}<1\). The formulas above give \(p_d(q)\le C_q d\rho^{d-1}\). Therefore the series \(A(q)=\sum_{d\ge1}p_d(q)>0\) and \(B(q)=\sum_{d\ge1}d p_d(q)\) converge, and
\[
\mu_n(q)=nA(q)-B(q)+O_q(n\rho^n).
\]
This proves the linear fixed-parameter law and the asserted distinction at \(q=1\). Finally, the reciprocal identities for the \(q\)-factorials and \(p_d\) give \(E_{n,d}(q)=q^{\binom n2-1}E_{n,d}(1/q)\), which also agrees with rank-reversing symmetry of the Bruhat order.

## Verification
A standalone standard-library Python verifier independently enumerates all \(\pi\in\mathfrak S_n\) for \(2\le n\le8\), determines upward covers by *actually swapping entries and recomputing the inversion number*, and forms an integer-coefficient polynomial separately for each position gap. It verifies the cross-multiplied polynomial identity
\[
E_{n,d}(q)[d]_q[d+1]_q=(n-d)dq^{d-1}[n]_q!,
\]
coefficient by coefficient, without rational approximation. It also checks reciprocal ranks, the exact uniform mean and the covariance relation implied by rank reciprocity. The executed verifier examined \(1{,}246{,}964\) candidate position-pair incidences across the seven sizes and passed all assertions. The executable and its exact recorded output are included. These finite checks support, but do not replace, the general proof.

## Relationship to prior work
Adin and Roichman, *On Degrees in the Hasse Diagram of the Strong Bruhat Order* (arXiv:math/0505020, first posted 2005), give the strong-cover criterion and the expected degree under the **uniform** distribution, with extremal results. Kitaev, Qiu and Xu, *Coincidences and Growth of Boxed Mesh Patterns* (arXiv:2609.13764, first posted 2026-09-12), identify boxed \(12\) with upward covers and record the same uniform mean, extremal counts, and an insertion identity for the still-open entire degree-distribution polynomial. Johnson, Leader and Long, *Correlation for permutations* (arXiv:1909.03770), establish positive association for Mallows measures on strong-Bruhat up-sets, not a Mallows rank-by-rank cover enumerator. The result here refines uniform total edge counts by **every lower inversion rank and every position span** and supplies the exact nonuniform Mallows response, its internal maximum, and the fixed-parameter scaling distinction. The reciprocal symmetry and the corresponding uniform covariance identity are recognized as consequences of the familiar rank-reversing symmetry, not claimed as independent priority. These comparisons do not establish exhaustive bibliographic uniqueness.

## Limitations
The theorem counts covers of the full symmetric group, not covers inside arbitrary Bruhat intervals or parabolic quotients. It gives the rank-weighted first moment, not the distribution of the entire upward degree or its variance, and it does not prove uniqueness or an explicit formula for a maximizing Mallows parameter. For \(q\) varying with \(n\), additional scaling regimes may occur; the stated asymptotic separates fixed \(q=1\) from fixed \(q\ne1\). Publication priority beyond inspected accessible literature remains subject to external independent checking.

## References
1. S. Kitaev, D. Qiu and C. Xu, *Coincidences and Growth of Boxed Mesh Patterns*, arXiv:2609.13764, first posted 2026-09-12, Section 8. https://arxiv.org/abs/2609.13764
2. R. M. Adin and Y. Roichman, *On Degrees in the Hasse Diagram of the Strong Bruhat Order*, arXiv:math/0505020, first posted 2005-05-02, Sections 1 and 4. https://arxiv.org/abs/math/0505020
3. J. R. Johnson, I. Leader and E. Long, *Correlation for permutations*, arXiv:1909.03770, first posted 2019-09-09. https://arxiv.org/abs/1909.03770
