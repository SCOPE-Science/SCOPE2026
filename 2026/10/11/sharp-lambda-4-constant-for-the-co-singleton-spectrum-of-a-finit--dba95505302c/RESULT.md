# Sharp \(\Lambda(4)\) constant for the co-singleton spectrum of a finite abelian group
## Finding
Let \(G\) be a finite abelian group of order \(N\ge4\), with normalized counting measure, and put \(\Lambda=\widehat G\setminus\{1\}\). The sharp inequality
\[
\left\|\sum_{\chi\in\Lambda}a_\chi\chi\right\|_4
\le K_4(\Lambda)\left(\sum_{\chi\in\Lambda}|a_\chi|^2\right)^{1/2}
\]
has
\[
K_4(\Lambda)^4=N-2+\frac1{N-1}.
\]
Every nonzero extremizer is exactly
\[
a_\chi=c\,\overline{\chi(x_0)}\qquad(\chi\ne1)
\]
for some \(c\ne0\) and \(x_0\in G\). Equivalently,
\[
f(x)=c\bigl(N\mathbf 1_{\{x_0\}}(x)-1\bigr).
\]

## Assumptions and scope
The group is finite abelian and \(N\ge4\). Haar measure is normalized counting measure. The theorem concerns the full co-singleton character set, not arbitrary dense subsets. The restriction \(N\ge4\) is used for the stated rigidity of all extremizers.

## Proof
A Fourier polynomial supported on \(\Lambda\) is exactly a mean-zero function on \(G\). Parseval therefore reduces the problem to the following finite-dimensional statement. For complex numbers \(z_1,\ldots,z_N\) satisfying \(\sum_i z_i=0\), write
\[
S_2=\sum_i|z_i|^2,\qquad S_4=\sum_i|z_i|^4.
\]
We prove
\[
\frac{S_4}{S_2^2}\le \frac{N^2-3N+3}{N(N-1)}.
\]

Normalize \(S_2=1\) and order the magnitudes so that \(x_1=|z_1|\) is maximal. The zero-sum condition implies the polygon inequality \(x_1\le\sum_{i>1}x_i\). Hold the ratios among \(x_2,\ldots,x_N\) fixed and increase \(x_1\) until equality in that polygon inequality. If \(u=x_1^2\), \(A_2=\sum_{i>1}x_i^2\), and \(A_4=\sum_{i>1}x_i^4\), then before renormalization the fourth-to-second-moment quotient is
\[
Q(u)=\frac{u^2+A_4}{(u+A_2)^2},
\qquad
Q'(u)=\frac{2(uA_2-A_4)}{(u+A_2)^3}\ge0,
\]
because \(u\) is at least every \(x_i^2\), hence at least the weighted average \(A_4/A_2\). Thus a maximizer lies on the boundary \(x_1=\sum_{i>1}x_i\).

On that boundary put \(y_i=x_i/x_1\) for \(i>1\). Then \(y_i\ge0\), \(\sum_{i>1}y_i=1\), and
\[
Q=\frac{1+\sum_{i>1}y_i^4}{(1+\sum_{i>1}y_i^2)^2}.
\]
Pairwise averaging increases this quantity. Indeed, for a pair with sum \(s\), squared difference \(v\), and with \(A_0\) and \(B_0\) the sums of the squares and fourth powers of the remaining coordinates, the derivative with respect to \(v\) has the sign of an affine function whose maximum on \(0\le v\le s^2\) is
\[
s^2(1+A_0)-1-B_0.
\]
Since \(A_0\le(1-s)^2\),
\[
s^2(1+A_0)\le s^2\bigl(1+(1-s)^2\bigr)\le1\le1+B_0.
\]
Hence reducing the squared difference cannot decrease \(Q\), and for \(N\ge4\) equality throughout forces all \(N-1\) values \(y_i\) to be equal. Therefore \(y_i=1/(N-1)\), and
\[
\max Q=\frac{1+(N-1)^-3}{(1+(N-1)^-1)^2}
=\frac{N^2-3N+3}{N(N-1)}.
\]
Normalized counting measure multiplies this unnormalized quotient by \(N\), giving
\[
K_4(\Lambda)^4=N-2+\frac1{N-1}.
\]

For equality, the polygon inequality is sharp, so the \(N-1\) smaller values have one common phase and the largest value has the opposite phase. Pairwise averaging rigidity gives equal smaller magnitudes. Thus, after permutation and a nonzero scalar, the value vector is
\[
(N-1,-1,\ldots,-1).
\]
For any \(x_0\in G\), character orthogonality gives
\[
N\mathbf 1_{\{x_0\}}-1
=\sum_{\chi\ne1}\overline{\chi(x_0)}\,\chi,
\]
which proves both attainment and the complete coefficient classification.

## Verification
The accompanying `artifacts/verify.py` checks the exact rational identity for every \(4\le N\le100\), verifies the equality witness exactly, tests deterministic complex mean-zero vectors against the sharp bound, and checks the pair-smoothing inequality on deterministic simplex samples. These computations support the algebra but are not substitutes for the proof above.

## Relationship to prior work
Michels gives the standard \(\Lambda(p)\) framework and studies infinite character sets through operator-ideal structure; the inspected preprint does not state the finite co-singleton \(\Lambda(4)\) constant or its equality cases. Hajela's earlier work constructs infinite thin \(\Lambda(4)\) sets with sharp exponent behavior, a different problem from the dense finite co-singleton spectrum considered here. Searches also compared the claim with finite cyclic projection norms, phase-only fourth moments, finite-field extension inequalities, and a distinct extremal-measure classification on four characters of \(\mathbb Z_5\); none implies this unrestricted co-singleton \(L^4/L^2\) theorem.

## Limitations
The theorem is not asserted for nonabelian groups or for general character subsets. The equality classification is stated only for \(N\ge4\). A residual bibliographic risk remains that the same zero-sum hyperplane norm may appear in older finite-dimensional Banach-space terminology rather than \(\Lambda(p)\)-set language.

## References
1. C. Michels, *Λ(p)-sets and the limit order of operator ideals*, arXiv:math/9904176v1, first public 1999-04-30.
2. D. J. Hajela, *Construction techniques for some thin sets in duals of compact abelian groups*, Ann. Inst. Fourier 36 (1986), 137–166, DOI 10.5802/aif.1063.
