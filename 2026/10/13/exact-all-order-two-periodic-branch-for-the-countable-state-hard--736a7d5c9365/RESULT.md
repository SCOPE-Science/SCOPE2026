# Exact all-order two-periodic branch for the countable-state hard-core tree model

## Finding

For the countable-state hard-core model on a Cayley tree of order \(k\ge2\), write
\[
\Lambda=\sum_{j\ne0}\lambda_j
\]
for the total nonzero activity. The published two-periodic boundary-law reduction gives positive totals \(A,B\) satisfying
\[
A(1+B)^k=B(1+A)^k=\Lambda.
\]
Every nontranslation-invariant solution is described, up to interchanging the two parity classes, by one and only one parameter \(r>1\). With
\[
S_m(r)=1+r+\cdots+r^{m-1},
\]
the branch is
\[
A(r)=\frac{r^{k-1}}{S_{k-1}(r)},\qquad
B(r)=\frac{1}{rS_{k-1}(r)},\qquad
\Lambda(r)=\frac{S_k(r)^k}{rS_{k-1}(r)^{k+1}}.
\]
The activity is strictly increasing with \(r\), from
\[
\Lambda_{\rm cr}=\frac{k^k}{(k-1)^{k+1}}
\]
to infinity. More precisely,
\[
\frac{d}{dr}\log\Lambda(r)
=\frac{(r-1)Q_k(r)}{rS_k(r)S_{k-1}(r)},
\]
where
\[
Q_k(r)=\sum_{j=0}^{2k-4}
\binom{\min\{j,2k-4-j\}+3}{3}r^j.
\]
All coefficients of \(Q_k\) are positive.

For the normalized parity order parameter
\[
\Delta=\frac{A-B}{A+B},
\]
the symmetry-broken branch has the sharp onset
\[
\lim_{\Lambda\downarrow\Lambda_{\rm cr}}
\frac{\Delta(\Lambda)}
{\sqrt{\Lambda/\Lambda_{\rm cr}-1}}
=\sqrt{\frac{6k}{k+1}}.
\]

## Assumptions and scope

The tree order is an integer \(k\ge2\). The activities are those of the countable-state hard-core model in Khakimov, Makhammadaliev and Rozikov, with finite positive total activity \(\Lambda\). The statement concerns the scalar totals of two-periodic boundary laws after the reduction established in that source. It classifies the nontranslation-invariant positive solutions of that reduced system; it does not classify arbitrary nonperiodic boundary laws or all Gibbs measures.

The branch is oriented by \(A>B\). Interchanging the parity classes sends \(r\) to \(1/r\) and swaps \(A\) with \(B\).

## Proof

Suppose \(A>B>0\) satisfies the published two-periodic equations. Dividing the two equal expressions for \(\Lambda\) gives
\[
\frac{A}{B}
=\left(\frac{1+A}{1+B}\right)^k.
\]
Set
\[
r=\left(\frac{A}{B}\right)^{1/k}
=\frac{1+A}{1+B}>1.
\]
Then \(A=r^kB\) and \(1+A=r(1+B)\). Eliminating \(A\) gives
\[
B=\frac{1}{rS_{k-1}(r)},\qquad
A=\frac{r^{k-1}}{S_{k-1}(r)}.
\]
Since
\[
rS_{k-1}(r)+1=S_k(r),
\]
substitution into \(\Lambda=A(1+B)^k\) yields
\[
\Lambda(r)=\frac{S_k(r)^k}{rS_{k-1}(r)^{k+1}}.
\]
Conversely, these formulas satisfy both source equations directly, so no positive nontrivial branch is omitted.

Differentiate the last display. After multiplication by the positive denominator \(rS_k(r)S_{k-1}(r)\) and coefficient collection,
\[
rS_k(r)S_{k-1}(r)\frac{d}{dr}\log\Lambda(r)
=(r-1)Q_k(r),
\]
where
\[
Q_k(r)=\sum_{j=0}^{2k-4}
\binom{\min\{j,2k-4-j\}+3}{3}r^j.
\]
The coefficient identity follows by expanding the two finite geometric sums and taking first differences of their cumulative coefficient counts. Every displayed binomial coefficient is positive. Hence \(\Lambda'(r)>0\) for \(r>1\). Also,
\[
\lim_{r\downarrow1}\Lambda(r)
=\frac{k^k}{(k-1)^{k+1}},
\qquad
\lim_{r\to\infty}\Lambda(r)=\infty.
\]
Thus \(r>1\) parameterizes the whole symmetry-broken activity range bijectively.

For the critical asymptotic, put \(r=e^s\). The geometric-sum identity
\[
S_m(e^s)
=e^{(m-1)s/2}\frac{\sinh(ms/2)}{\sinh(s/2)}
\]
and
\[
\log\!\left(\frac{\sinh z}{z}\right)
=\frac{z^2}{6}+O(z^4)
\]
give
\[
\log\frac{\Lambda(e^s)}{\Lambda_{\rm cr}}
=\frac{k(k+1)}{24}s^2+O(s^4).
\]
Meanwhile
\[
\Delta(e^s)=\frac{e^{ks}-1}{e^{ks}+1}
=\tanh\!\left(\frac{ks}{2}\right)
=\frac{k}{2}s+O(s^3).
\]
Combining these expansions proves
\[
\Delta
=\sqrt{\frac{6k}{k+1}}\,
\sqrt{\frac{\Lambda}{\Lambda_{\rm cr}}-1}
+o\!\left(\sqrt{\frac{\Lambda}{\Lambda_{\rm cr}}-1}\right).
\]

## Verification

The accompanying verifier checks the branch equations exactly over rational test parameters for several tree orders, verifies the finite-polynomial derivative identity coefficient-by-coefficient through a range of orders, and numerically checks the critical amplitude from the stable hyperbolic-sine representation. These finite calculations corroborate the algebra but are not used as a proof of the all-\(k\) statement.

## Relationship to prior work

Khakimov, Makhammadaliev and Rozikov reduce two-periodic boundary laws to \(A(1+B)^k=B(1+A)^k=\Lambda\), prove the threshold \(\Lambda_{\rm cr}=k^k/(k-1)^{k+1}\), and establish the number of positive solutions using an S-shaped fixed-point argument. Their explicit closed formulas are specialized to \(k=2\). The geometric-sum parameterization above instead gives the entire nontranslation-invariant branch for every \(k\ge2\), together with a positive-coefficient derivative certificate and the exact order-parameter onset amplitude.

Rozikov and Haydarov subsequently analyze convergence of the associated scalar iteration and recover the same threshold, but do not provide this all-order branch parameterization. Earlier regular-tree hard-core work, including Galvin, Martinelli, Ramanan and Tetali, develops the scalar fixed-point and phase-transition framework but does not supply the displayed geometric-sum branch formula.

## Limitations

The result is confined to the two-periodic scalar boundary-law sector. It does not prove uniqueness or completeness among arbitrary Gibbs measures, and it does not address models with a different compatibility graph. The originality comparison cannot exclude weakly indexed material using substantially different variables; the closest accessible primary and predecessor sources were checked for the same equations, branch structure, and critical behavior.

## References

1. R. M. Khakimov, M. T. Makhammadaliev, U. A. Rozikov, “Gibbs measures for HC-model with a countable set of spin values on a Cayley tree,” arXiv:2205.02025, first public 2022-05-04; later published in *Mathematical Physics, Analysis and Geometry*, DOI:10.1007/s11040-023-09453-w.
2. U. A. Rozikov, F. H. Haydarov, “A HC model with countable set of spin values: uncountable set of Gibbs measures,” arXiv:2206.06333.
3. D. Galvin, F. Martinelli, K. Ramanan, P. Tetali, “The multi-state hard core model on a regular tree,” arXiv:1007.4806.
