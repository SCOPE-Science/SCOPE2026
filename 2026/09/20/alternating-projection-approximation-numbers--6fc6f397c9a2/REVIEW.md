# Review: exact approximation-number power law for two-subspace alternating projections

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

Let
\[
E_n=(PQ)^n-R,\qquad R=P_{M\cap N}.
\]
The intersection projection satisfies \(PQR=RPQ=R\), so \(E_n=(PQ-R)^n\).

On the four elementary reducing summands of the two-subspace decomposition, \(E_n=0\). On the generic summand \(K\oplus K\),
\[
P=
\begin{pmatrix}I&0\\0&0\end{pmatrix},
\qquad
Q=
\begin{pmatrix}C^2&CS\\CS&S^2\end{pmatrix},
\qquad C^2+S^2=I,
\]
with \(C,S\) commuting positive contractions. Direct multiplication gives
\[
(PQ)^n=
\begin{pmatrix}
C^{2n}&C^{2n-1}S\\
0&0
\end{pmatrix}
\]
and hence
\[
(PQ)^n((PQ)^n)^*
=
\begin{pmatrix}
C^{4n-2}&0\\0&0
\end{pmatrix}.
\]
Therefore the generalized singular-value data are those of \(C^{2n-1}\oplus0\). The Hilbert-space spectral min-max formula for a positive operator gives
\[
a_k(C^{2n-1})=a_k(C)^{2n-1}.
\]
This proves the main identity.

The essential-norm consequence follows from \(\lim_k a_k(T)=\|T\|_{\mathrm e}\). Compactness and rank follow because the power map preserves zero and convergence to zero. In the compact case approximation numbers are singular values, and summing their \(p\)-powers gives the stated Schatten equivalence and exact norm identity.

The proof was also stress-tested in finite-dimensional random projection examples: the singular values of the iterates matched the predicted odd powers to floating-point precision. This computation is supporting evidence only and is not used in the proof.

## Originality and literature

The following ingredients are established prior work and are not part of the novelty claim:

- Halmos' canonical two-subspace decomposition;
- principal-angle and singular-value descriptions of products of two orthogonal projections;
- the Kayalar-Weinert formula for the operator norm of the alternating-projection error;
- singular-value decompositions of compact or Schmidt-decomposable products of projections.

The full text of Andruchow and Corach's paper on Schmidt-decomposable products was inspected for the terms and concepts most likely to cover the result. It characterizes singular-value decompositions of \(PQ\) and records the algebraic identity \(T^2=TT^*T\) for products of projections, but no treatment of powers, alternating iterates, Schatten transfer, or approximation-number power laws was located. Their work on essentially orthogonal subspaces covers compact-product singular-value geometry but no iterate formula was located in the inspected text.

Targeted searches also covered:
“product of two orthogonal projections” with “powers”, “singular values”, and “approximation numbers”; “alternating projections” with “Schatten”, “essential norm”, and “singular values”; and principal/Friedrichs-angle formulations. These searches recovered the classical norm-rate and canonical-angle literature, but not the all-\(k\) identity
\[
a_k((PQ)^n-R)=a_k(PQ-R)^{2n-1}.
\]

Originality therefore passes **to the best of our knowledge** for the all-\(k\) statement and the exact ideal consequences, with a residual risk noted below.

## Value

The result gives more than an alternative proof of the known norm rate. One equality simultaneously determines:

- every optimal rank-\((k-1)\) approximation error of every iterate;
- the Calkin norm of every iterate;
- whether any iterate is compact or finite rank;
- the complete singular-value sequence in the compact case;
- exact Schatten membership and norm transfer.

The compactness converse is structurally useful: for arbitrary bounded operators a power may become compact without the operator itself being compact, whereas this cannot happen for two-subspace alternating-projection errors.

The diagonal model \(c_j\asymp j^{-\alpha}\) shows that the Schatten threshold can be tuned and that iteration multiplies the singular-value decay exponent by \(2n-1\).

## Scientific limitations

The theorem is restricted to two orthogonal projections on a Hilbert space. It does not establish an analogous law for cyclic products of three or more projections, oblique projections, or Banach-space projections.

The 2010 Böttcher-Spitkovsky survey was not exhaustively inspected in full. Because that survey covers a large portion of two-projection theory, an equivalent all-\(k\) formula could conceivably occur there or in older canonical-angle language. No such statement was located in the searches performed. This is the main residual originality risk.

## Sources checked

- Halmos, “Two subspaces,” *Trans. Amer. Math. Soc.* 144 (1969), 381–389.
- Kayalar and Weinert, “Error bounds for the method of alternating projections,” *Math. Control Signals Systems* 1 (1988), 43–59.
- Böttcher and Spitkovsky, “A gentle guide to the basics of two projections theory,” *Linear Algebra Appl.* 432 (2010), 1412–1459.
- Corach and Maestripieri, “Products of orthogonal projections and polar decompositions,” *Linear Algebra Appl.* 434 (2011), 1594–1609.
- Klaja, “The numerical range and the spectrum of a product of two orthogonal projections,” *J. Math. Anal. Appl.* 411 (2014), 177–195.
- Andruchow and Corach, “Schmidt decomposable products of projections,” *Integral Equations Operator Theory* 89 (2017), 485–503.
- Andruchow and Corach, “Essentially orthogonal subspaces,” *J. Operator Theory* 79 (2018), 79–100.
