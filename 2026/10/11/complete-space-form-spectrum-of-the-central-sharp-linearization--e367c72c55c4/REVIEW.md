# Same-model review

## Correctness

PASS. The primary source gives
\[
\Gamma_{1,1}(R_\kappa)
=
\kappa\sum_{a<b}D_L(E_{ab})D_R(E_{ab})
\]
and
\[
d\mathcal Q_{R_\kappa}=-2\Gamma_{1,1}(R_\kappa).
\]
For diagonal curvature weights \(w_{ij}\), direct use of the derivation action gives
\[
(\Gamma S)_{ij}
=
\kappa\sum_{k\ne i,j}(w_{ik}+w_{jk}).
\]
The scalar choice \(w_{ij}=1\), a traceless-Ricci choice \(w_{ij}=s_i+s_j\) with \(\sum_i s_i=0\), and a nonzero diagonal Weyl choice with zero row sums give respectively
\[
2(n-2)\kappa,\qquad
(n-4)\kappa,\qquad
-2\kappa.
\]
The central channel is \(O(n)\)-equivariant and the source's Ricci decomposition consists of irreducible \(O(n)\)-summands, so these are the eigenvalues on the full pieces. The bundled checker reconstructs all \(D(E_{ab})\) matrices and replays the calculation in dimensions four through nine.

## Originality

PASS. The motivating preprint identifies the central channel with the sharp product, proves the sharp-quadratic linearization formula, and separately recovers the orthogonal scalar/traceless-Ricci/Weyl decomposition. Its inspected text contains no eigenvalue or spectrum statement; direct full-text searches for those terms and for the factor \(n-4\) found none. Targeted searches of the classical sharp-product literature and published records did not locate the normalized three-eigenvalue formula.

The main residual risk is normalization-dependent prior art: the sharp product is classical, and an equivalent older calculation may use curvature-operator notation and different factors.

## Value

PASS. This is the complete spectral answer for the most symmetric background of the new central linearization. It isolates a dimension-four cancellation in the traceless-Ricci channel and a dimension-independent Weyl response. Those features are directly relevant to understanding how the new Clifford channel sits inside curvature dynamics and provide exact benchmarks for later comparisons with the full reaction operator.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is A. Belkhirat, arXiv:2610.04428v1. Böhm--Wilking supply the classical curvature-operator sharp-product dynamics, and Labbi supplies the double-form sharp-product framework.

The spectrum computed here belongs only to
\[
\mathcal Q(R)=-\frac14R\#R.
\]
It is not the spectrum of the complete Ricci-flow linearization, which contains additional algebraic and differential terms.
