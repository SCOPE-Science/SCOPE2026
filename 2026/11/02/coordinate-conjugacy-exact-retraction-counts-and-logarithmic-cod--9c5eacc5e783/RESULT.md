# Logarithmic codimension of a uniform algebra retraction of an elementary-abelian modular group algebra

## Finding

Let \(p\) be prime, \(q=p^f\) with \(f\ge 1\), and let
\[
R_d=\mathbb F_q[(C_p)^d]\cong\mathbb F_q[x_1,\ldots,x_d]/(x_1^p,\ldots,x_d^p).
\]
Choose uniformly among its idempotent unital \(\mathbb F_q\)-algebra endomorphisms. By the known coordinate classification [1], the image has dimension \(p^{K_d}\) for an integer \(0\le K_d\le d\). Put \(B_d=d-K_d\) and \(b_d=\lfloor\log_p d\rfloor\). For fixed \(p,q\),
\[
\Pr\{ B_d\in\{b_d-1,b_d,b_d+1\}\}\longrightarrow 1\qquad(d\to\infty).
\]
In particular, with probability tending to one the ratio of the image dimension to \(p^d/d\) lies between \(1/p\) and \(p^2\).

## Assumptions and scope

The field and characteristic are fixed; only \(d\) grows. Endomorphisms preserve the identity and fix the coefficient field pointwise. The random choice is uniform on maps \(e\) with \(e^2=e\), not on image subalgebras, conjugacy classes, or all endomorphisms. The image dimension is over \(\mathbb F_q\). The integer \(B_d\) is the codimension on the cotangent space of the maximal ideal, not the additive codimension of the image in \(R_d\).

## Proof

The previously established rank count [1, Finding] is
\[
N_{d,k}={d\brack k}_q q^{k(p^d-p^k-d+k)+(d-k)(p^k-1)}.
\]
Here \({d\brack k}_q\) is the Gaussian binomial coefficient. With \(P=p^d\) and \(b=d-k\), its exponent can be written as \(P h_d(b)-b(d-b+1)\), where
\[
h_d(b)=d-b-(d-2b)p^{-b}.
\]
Uniformly for \(0\le b\le d\),
\[
\log_q N_{d,d-b}=P h_d(b)+O(d^2),
\]
since \(0\le b(d-b+1)\le d(d+1)\), and the Gaussian binomial counts subspaces of dimension \(d-b\), of which there are at most \(q^{d^2}\) by counting ordered bases.

The exact adjacent difference is
\[
h_d(b+1)-h_d(b)=-1+\frac{(p-1)(d-2b)+2}{p^{b+1}}\qquad(0\le b<d).
\]
If \(b\le b_d-2\), then \(p^{b+1}\le d/p\) and \(b=O(\log d)\). Thus the difference is at least \(-1+p(p-1)-o(1)\), hence at least \(1/2\) for all sufficiently large \(d\). If \(b\ge b_d+1\), then \(d<p^{b_d+1}\) and \(p^{b+1}\ge p^{b_d+2}\). Using \(d-2b\le d\), the difference is at most \(-1+(p-1)/p+2p^{-(b_d+2)}\), hence at most \(-1/(2p)\) for sufficiently large \(d\).

Let \(W_d=\{b_d-1,b_d,b_d+1\}\). For large \(d\), summing the adjacent differences toward the nearer endpoint of \(W_d\) shows that each \(b\notin W_d\) has \(h_d(b)\le h_d(a)-1/(2p)\) for some \(a\in W_d\). The total count of idempotent maps is at least \(N_{d,d-a}\) for each such comparison. Therefore
\[
\Pr\{B_d\notin W_d\}\le (d+1)q^{-p^d/(2p)+O(d^2)}\longrightarrow0.
\]
On \(W_d\), the ratio of the image dimension to \(p^d/d\) is \(d p^{-B_d}\), which lies in \([1/p,p^2]\) by \(p^{b_d}\le d<p^{b_d+1}\). This proves the finding.

## Verification

The concentration follows from the displayed exact count, the uniform log-error bound and the two uniform adjacent-difference estimates. Finite rank-count and log-space checks in the original supporting material do not establish the limiting claim.

## Relationship to prior work

The coordinate conjugacy and the exact counts are inputs from [1], not new results here. Its exponent is also \(k(p^d-p^k)+(d-k)(p^k-k-1)\). It studies a fixed-dimension comparison as the field grows; that is different from the uniform probability law when the field is fixed and the number of generators diverges. An earlier characteristic-two count appears in [2]. The contribution here is the fixed-field concentration of the corank in an explicit three-point window. This is not a claim of exhaustive publication priority.

## Limitations

The argument does not determine relative probabilities among the three remaining indices or address growth of \(p\) or \(q\) with \(d\).

## References

1. *Rank-stratified algebra retractions of elementary abelian modular group algebras*, Resultary, 2026-10-26, record `8fd6e2bb2372`, [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-rank-stratified-algebra-retractions-of-elementary-abelian-modula--8fd6e2bb2372/RESULT.md), Finding.
2. *Automorphism orbits and rank counts of characteristic-two square-zero algebras*, Resultary, 2026-10-12, record `256249efd1a0`, [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-automorphism-orbits-and-rank-counts-of-characteristic-two-square--256249efd1a0/RESULT.md), Finding.
