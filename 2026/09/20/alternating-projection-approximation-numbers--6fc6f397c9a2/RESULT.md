# Exact approximation-number power law for two-subspace alternating projections

## Statement

Let \(M,N\) be closed subspaces of a Hilbert space \(H\), let \(P=P_M\) and \(Q=P_N\) be the corresponding orthogonal projections, and let
\[
R=P_{M\cap N}.
\]
For \(n\ge 1\), put
\[
E_n=(PQ)^n-R,
\qquad
E_1=PQ-R.
\]
For a bounded operator \(T\) on \(H\), write
\[
a_k(T)=\inf\{\|T-F\|:\operatorname{rank}F<k\},
\qquad k\ge1,
\]
for its approximation numbers.

Then for every \(n,k\ge1\),
\[
\boxed{a_k(E_n)=a_k(E_1)^{\,2n-1}.}
\]

Thus the classical scalar norm law for alternating projections extends, with the same exponent, to the entire low-rank approximation profile.

Several consequences are immediate.

1. **Essential norm.**
   \[
   \|E_n\|_{\mathrm e}=\|E_1\|_{\mathrm e}^{\,2n-1}.
   \]

2. **Compactness and rank rigidity.** For every \(n\ge1\),
   \[
   E_n\text{ is compact}\iff E_1\text{ is compact},
   \]
   and
   \[
   \operatorname{rank}E_n=\operatorname{rank}E_1
   \]
   with the value \(+\infty\) allowed.

3. **Compact singular-value profile.** If \(E_1\) is compact and its singular values are
   \[
   s_1(E_1)\ge s_2(E_1)\ge\cdots,
   \]
   then
   \[
   s_k(E_n)=s_k(E_1)^{\,2n-1}
   \qquad(k\ge1).
   \]

4. **Exact Schatten transfer.** For every \(0<p<\infty\),
   \[
   E_n\in S_p
   \iff
   E_1\in S_{p(2n-1)},
   \]
   and whenever these conditions hold,
   \[
   \|E_n\|_{S_p}
   =
   \|E_1\|_{S_{p(2n-1)}}^{\,2n-1}.
   \]

In particular, compactness of one nontrivial alternating-projection iterate cannot appear for the first time at a later step: it is already present in the one-step error.

## Proof

First note that \(R\) commutes with \(PQ\) and satisfies
\[
(PQ)R=R(PQ)=R.
\]
Hence
\[
E_n=(PQ)^n-R=(PQ-R)^n.
\]

Use the standard two-subspace decomposition. The four intersection summands
\[
M\cap N,\quad M\cap N^\perp,\quad M^\perp\cap N,\quad
M^\perp\cap N^\perp
\]
reduce both \(P\) and \(Q\). On all four of them, \(E_n\) vanishes. On the generic part one may identify the space with \(K\oplus K\) so that
\[
P=
\begin{pmatrix}
I&0\\
0&0
\end{pmatrix},
\qquad
Q=
\begin{pmatrix}
C^2&CS\\
CS&S^2
\end{pmatrix},
\]
where \(C,S\) are commuting positive contractions on \(K\) satisfying
\[
C^2+S^2=I.
\]

On this generic part,
\[
PQ=
\begin{pmatrix}
C^2&CS\\
0&0
\end{pmatrix}.
\]
A direct induction gives
\[
(PQ)^n=
\begin{pmatrix}
C^{2n}&C^{2n-1}S\\
0&0
\end{pmatrix}.
\]
Therefore
\[
(PQ)^n\big((PQ)^n\big)^*
=
\begin{pmatrix}
C^{4n}+C^{4n-2}S^2&0\\
0&0
\end{pmatrix}
=
\begin{pmatrix}
C^{4n-2}&0\\
0&0
\end{pmatrix}.
\]
Thus the generalized singular-value profile of \(E_n\) is exactly that of
\[
C^{2n-1}\oplus0,
\]
whereas the profile of \(E_1\) is that of
\[
C\oplus0.
\]

For a positive operator \(C\), the Hilbert-space min-max characterization of approximation numbers and the spectral calculus imply
\[
a_k(C^m)=a_k(C)^m
\qquad (m>0,\ k\ge1).
\]
Equivalently, the spectral distribution above each threshold transforms under
\(t\mapsto t^m\). Taking \(m=2n-1\) proves
\[
a_k(E_n)=a_k(E_1)^{2n-1}.
\]

The essential-norm formula follows by letting \(k\to\infty\), since on Hilbert space
\[
\lim_{k\to\infty}a_k(T)=\|T\|_{\mathrm e}.
\]
The compactness and rank assertions follow from the same identity. In the compact case the approximation numbers are the singular values, giving the third assertion. Finally,
\[
\sum_k s_k(E_n)^p
=
\sum_k s_k(E_1)^{p(2n-1)},
\]
which yields the Schatten equivalence and norm identity.

## A concrete profile family

Let \(K=\ell_2\), fix \(\alpha>0\), and set
\[
Ce_j=(j+1)^{-\alpha}e_j,
\qquad
S=(I-C^2)^{1/2}.
\]
Using the two-subspace model above gives a pair of closed subspaces with trivial intersection for which
\[
s_j(PQ)\asymp j^{-\alpha}.
\]
The theorem gives the exact power law
\[
s_j((PQ)^n)\asymp j^{-\alpha(2n-1)}.
\]
Consequently
\[
(PQ)^n\in S_p
\iff
\alpha p(2n-1)>1.
\]
Thus iteration improves the Schatten exponent in a completely prescribed way even though compactness itself is already decided at the first step.

## Relation to known results

The operator-norm rate for two alternating orthogonal projections is classical. In the usual notation, Kayalar and Weinert proved
\[
\|(PQ)^n-R\|=\|PQ-R\|^{2n-1},
\]
equivalently the rate is governed by the Friedrichs cosine.

Halmos' two-subspace theorem supplies the generic block model used above. Later work on products of two projections develops the spectral, numerical-range, polar-decomposition, and singular-value geometry of \(PQ\). In particular, Andruchow and Corach characterize when a product \(PQ\) is Schmidt decomposable and identify its singular values from biorthogonal bases; their earlier work on essentially orthogonal subspaces treats the compact-product case. These classical structural facts are not claimed as new here.

The contribution claimed here is the all-\(k\) identity
\[
a_k((PQ)^n-R)=a_k(PQ-R)^{2n-1}
\]
for arbitrary Hilbert-space pairs, together with the exact essential-norm, compactness/rank, and Schatten-index consequences.

## Originality and limitations

Originality is claimed **to the best of our knowledge** only for the full approximation-number power law and its stated consequences, not for the two-subspace decomposition, the principal-angle/singular-value description of a product of two projections, or the classical \(k=1\) norm formula.

Targeted searches covered products of two orthogonal projections, alternating projections, principal and Friedrichs angles, singular values, approximation numbers, essential norms, Schatten classes, powers and iterates, and synonymous formulations. The inspected 2017 paper on Schmidt-decomposable products explicitly develops singular-value decompositions of \(PQ\), but searches within that full text located no treatment of powers, alternating iterates, Schatten transfer, or approximation-number power laws. The 2018 paper on essentially orthogonal subspaces gives the compact-product singular-value geometry, again without an iterate power law located in the inspected text.

Residual literature risk remains because the broad 2010 survey by Böttcher and Spitkovsky was not exhaustively inspected in full, and an equivalent statement could appear there or in older projection literature as an unstated corollary of canonical-angle formulas. For that reason the originality claim is deliberately limited to the best of our knowledge.

The theorem is specific to two orthogonal projections on Hilbert space. No analogous exact formula is asserted here for three or more projections, oblique projections, or Banach-space projections.

## References

- P. R. Halmos, “Two subspaces,” *Transactions of the American Mathematical Society* 144 (1969), 381–389. https://doi.org/10.1090/S0002-9947-1969-0251519-5
- S. Kayalar and H. L. Weinert, “Error bounds for the method of alternating projections,” *Mathematical Control and Signals Systems* 1 (1988), 43–59. https://doi.org/10.1007/BF02551235
- A. Böttcher and I. M. Spitkovsky, “A gentle guide to the basics of two projections theory,” *Linear Algebra and its Applications* 432 (2010), 1412–1459. https://doi.org/10.1016/j.laa.2009.11.002
- G. Corach and A. Maestripieri, “Products of orthogonal projections and polar decompositions,” *Linear Algebra and its Applications* 434 (2011), 1594–1609. https://doi.org/10.1016/j.laa.2010.11.033
- H. Klaja, “The numerical range and the spectrum of a product of two orthogonal projections,” *Journal of Mathematical Analysis and Applications* 411 (2014), 177–195. https://doi.org/10.1016/j.jmaa.2013.09.024
- E. Andruchow and G. Corach, “Schmidt decomposable products of projections,” *Integral Equations and Operator Theory* 89 (2017), 485–503. https://doi.org/10.1007/s00020-017-2402-x
- E. Andruchow and G. Corach, “Essentially orthogonal subspaces,” *Journal of Operator Theory* 79 (2018), 79–100. https://doi.org/10.7900/jot.2016dec13.2138
