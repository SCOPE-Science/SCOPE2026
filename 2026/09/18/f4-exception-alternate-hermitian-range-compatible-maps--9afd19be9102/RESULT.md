# The missing F4 exception for alternate-Hermitian range-compatible maps

Let \(\mathbb D=\mathbb F_4\) carry its nonidentity involution \(x^\star=x^2\), let \(\mathbb F=\mathbb F_2\), and put \(n=2\). Then
\[
\mathcal{AH}_2(\mathbb F_4)=\mathcal H_2(\mathbb F_4).
\]
Consequently the exceptional range-compatible map
\[
\Phi_0:\begin{bmatrix}a&x^\star\\x&b\end{bmatrix}
\longmapsto
\begin{bmatrix}x\\x^\star\end{bmatrix}
\]
from Theorem 1.6 of arXiv:2609.20363v1 is also a nonlocal range-compatible \(\mathbb F_2\)-linear map on the alternate-Hermitian space. This gives a direct counterexample to Theorem 1.7(a) of that version, which states without exception that every range-compatible \(\mathbb F\)-linear map on \(\mathcal{AH}_n(\mathbb D)\) is local.

## Corrected statement

Under the hypotheses of Theorem 1.7 of arXiv:2609.20363v1, part (a) can be replaced by:

> Every range-compatible \(\mathbb F\)-linear mapping on \(\mathcal{AH}_n(\mathbb D)\) is local, except when \(\mathbb D=\mathbb F_4\), the involution is nonidentity, \(\mathbb F=\mathbb F_2\), and \(n=2\). In that exceptional case all such mappings are
> \[
> M\longmapsto MX+\Phi_0(M)\alpha,
> \qquad X\in\mathbb F_4^2,\ \alpha\in\mathbb F_4.
> \]

The exceptional case is unique: Theorem 1.3 of the same paper already proves locality on alternate-Hermitian matrices outside \(n=2,|\mathbb D|=4\); if \(|\mathbb D|=4\) and the involution is nonidentity, then \(\mathbb D=\mathbb F_4\), its fixed field is \(\mathbb F_2\), and an admissible scalar field \(\mathbb F\) fixed pointwise by the involution is therefore \(\mathbb F_2\).

## Proof of the exceptional identification

In characteristic two, an alternate-Hermitian element has the form \(y-y^\star=y+y^\star\), hence is Hermitian. Conversely, the paper observes that for an involution of the second kind in characteristic two every Hermitian scalar is alternate-Hermitian. Thus the scalar subgroups \(H\) and \(A\) coincide. The off-diagonal defining conditions for Hermitian and alternate-Hermitian matrices also coincide because \(-1=1\). Therefore
\[
\mathcal{AH}_2(\mathbb F_4)=\mathcal H_2(\mathbb F_4).
\]

Theorem 1.6 of arXiv:2609.20363v1 states that every range-compatible group homomorphism on \(\mathcal H_2(\mathbb F_4)\) is a sum of a local map and a scalar multiple of \(\Phi_0\), and the preceding discussion proves that \(\Phi_0\) is range-compatible and nonlocal. Every additive map between \(\mathbb F_2\)-vector spaces is \(\mathbb F_2\)-linear, so this classification applies verbatim to the alternate-Hermitian \(\mathbb F_2\)-linear problem.

## Exact size of the exceptional space

There is a direct-sum decomposition of right \(\mathbb F_4\)-vector spaces
\[
\operatorname{RC}_{\mathbb F_2}(\mathcal{AH}_2(\mathbb F_4),\mathbb F_4^2)
=
\operatorname{Loc}\oplus \Phi_0\mathbb F_4
\cong \mathbb F_4^3.
\]
Indeed, local maps are parametrized by \(X\in\mathbb F_4^2\). If a nonzero scalar multiple \(\Phi_0\alpha\) were local, multiplication by \(\alpha^{-1}\) would make \(\Phi_0\) local, contradicting the explicit nonlocality proof in the source paper. Hence the intersection is zero.

It follows that there are exactly
\[
4^3=64
\]
range-compatible \(\mathbb F_2\)-linear maps in the exceptional case. Of these, \(4^2=16\) are local and
\[
64-16=48
\]
are nonlocal.

## Finite exhaustive verification

The accompanying script `artifacts/verify_f4_exception.py` represents \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\), enumerates all 16 matrices in \(\mathcal{AH}_2(\mathbb F_4)=\mathcal H_2(\mathbb F_4)\), all \(2^{16}=65536\) \(\mathbb F_2\)-linear maps from this four-dimensional \(\mathbb F_2\)-space to \(\mathbb F_4^2\), and tests range compatibility exactly by finite-field arithmetic. It returns 64 range-compatible maps, 16 local maps, and 48 nonlocal maps, and verifies that every range-compatible map is of the displayed classified form. This finite computation supports the classification; the proof above does not depend on enumeration.

## Scope and limitations

The exceptional map and the Hermitian classification are results of arXiv:2609.20363v1 and are not claimed here as new. The contribution recorded here is the identification of the resulting contradiction with Theorem 1.7(a), the corrected alternate-Hermitian statement, and the exact direct-sum/counting consequence with exhaustive verification. The source is a very recent first version and may be revised independently. No public erratum or revised arXiv version addressing this point was located at publication time.

## References

1. C. de Seguins Pazzis, *Range-compatible homomorphisms on Hermitian matrices*, arXiv:2609.20363v1 (2026).
2. C. de Seguins Pazzis, *Range-compatible homomorphisms on spaces of symmetric or alternating matrices*, Linear Algebra Appl. 507 (2016), 331–360; arXiv:1506.07203.
