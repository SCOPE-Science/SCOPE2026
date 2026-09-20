# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof has two independent directions.

For sufficiency, after a threshold \(t\), the small-weight coordinates are recovered
from the first ambient component and the large-weight coordinates from the second.
The only nontrivial boundedness condition is the diagonal multiplier
\[
(\lambda_n^{-1})_{\{|\lambda_n|>t\}}:
(\oplus E_n)_q\longrightarrow(\oplus E_n)_p.
\]
For \(p<q\), its norm is exactly the \(\ell_r\)-norm of the scalar block norms,
where \(1/r=1/p-1/q\). This gives the explicit threshold projection and the upper
bound \(2^{1/p}\Theta(\lambda)\).

For necessity, an arbitrary projection onto the graph can be averaged over
simultaneous coordinate signs. On finitely supported vectors the averages stabilize
and kill all off-diagonal blocks; density then gives a block-diagonal projection
with no larger norm. On the \(n\)-th block it has coefficients \(A_n,B_n\) satisfying
\[
A_n+\lambda_nB_n=I.
\]
If the projection norm is \(K\), then
\[
|\lambda_n|\|A_n\|\le K,\qquad
\|(\|B_n\|)\|_{\ell_r}\le K.
\]
For \(|\lambda_n|>2K\), this forces
\[
\|B_n\|\ge\frac1{2|\lambda_n|},
\]
hence \(L_\lambda(2K)\le2K\). This proves the lower estimate
\(\pi_Z(G_\lambda)\ge\Theta(\lambda)/2\).

The maximal multiplication operator is closed: convergence in the two ambient
direct-sum spaces implies coordinatewise convergence, so the limiting coordinates
still satisfy \(y_n=\lambda_nx_n\). Finite-support vectors are dense in the domain
with its graph norm. The \(q=\infty\) endpoint is handled with \(c_0(E_n)\);
finite supports give the lower half of the multiplier-norm identity.

For power weights \(n^\alpha\), the phase diagram follows from elementary integral
comparison. When \(0<\alpha<\delta\), the threshold functional balances
\(m^\alpha\) against the tail size \(N^{\delta-\alpha}\), giving the exponent
\(\min\{\alpha,\delta-\alpha\}\). At \(\alpha=\delta\), the reciprocal series is
harmonic and produces \((\log(N+1))^\delta\). The regimes \(\alpha\le0\) and
\(\alpha>\delta\) have uniformly bounded threshold functional.

## Originality

The qualitative structure of complemented unconditional subspaces of
\(\ell_p\oplus\ell_q\) is classical. In particular, the following older papers are
directly adjacent and are not part of the novelty claim:

- P. Wojtaszczyk, *On complemented subspaces and unconditional bases in
  \(l_p+l_q\)*, Studia Mathematica 47 (1973), 197--206.
- I. Edelstein and P. Wojtaszczyk, *On projections and unconditional bases in
  direct sums of Banach spaces*, Studia Mathematica 56 (1976), 263--276.
- P. Wojtaszczyk, *On projections and unconditional bases in direct sums of
  Banach spaces II*, Studia Mathematica 62 (1978), 193--201.

A modern source, Albiac--Ansorena (2021), classifies unconditional bases in finite
direct sums of \(\ell_p\) spaces and explicitly invokes the
Edelstein--Wojtaszczyk theorem in the locally convex case. Its accessible text
discusses complemented and well-complemented block sequences, but targeted
full-text searches found no occurrences of “projection constant”, “weighted”, or
“operator graph”.

Additional searches used the terms diagonal graph, graph of a diagonal operator,
closed-operator graph, block-diagonal graph, weighted complemented subspace,
projection constant, reciprocal tail, and power weights. No located source stated
the quantitative two-sided threshold formula
\[
\pi_Z(G_\lambda)\asymp_{p}
\inf_t\max\{1,t,L_\lambda(t)\},
\]
for arbitrary Banach blocks, nor the sharp finite-section rates for
\(\lambda_n=n^\alpha\).

The 1973, 1976, and 1978 Studia Mathematica articles were not all inspected in
full, so an equivalent scalar or qualitative statement under older terminology
remains a significant residual risk. Classical sequence-space monographs and the
projection-constant literature were not exhaustively checked. Accordingly,
originality is asserted only to the best of our knowledge, and the scalar
qualitative splitting phenomenon is not isolated as new.

## Value

The result gives a quantitative localization principle: complementing a diagonal
graph amounts, within universal constants, to choosing where to switch from using
the domain coordinate to using the range coordinate. The norm contribution of that switch is
exactly the competition between the weight threshold and the reciprocal
\(\ell_r\)-tail.

The arbitrary-block formulation shows that this projection geometry depends only
on the outer exponents and weights, not on dimensions or internal Banach geometry.
The power family \(n^\alpha\) then exhibits a simple but nonmonotone phase:
bounded weights are complemented, slowly growing unbounded weights are not, and
fast growth becomes complemented again. The finite-dimensional projection
constants quantify the approach to both phase boundaries.

## Sources checked

- P. Wojtaszczyk, Studia Mathematica 47 (1973), 197--206,
  DOI 10.4064/sm-47-3-197-206.
- I. Edelstein and P. Wojtaszczyk, Studia Mathematica 56 (1976), 263--276,
  DOI 10.4064/sm-56-3-263-276.
- P. Wojtaszczyk, Studia Mathematica 62 (1978), 193--201,
  DOI 10.4064/sm-62-2-193-201.
- F. Albiac and J. L. Ansorena, Mathematische Nachrichten 294 (2021),
  2052--2062, arXiv:1909.06829, DOI 10.1002/mana.201900537.
