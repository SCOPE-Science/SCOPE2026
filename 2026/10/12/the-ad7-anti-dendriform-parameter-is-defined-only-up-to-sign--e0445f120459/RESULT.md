# The AD7 anti-dendriform parameter is defined only up to sign

## Finding

Let \(A_\lambda=AD_3^7(\lambda)\) denote the family in Theorem 4.1 of Abdurasulov--Adashev--Normatov--Solijonova. In the displayed basis \(\{e_1,e_2,e_3\}\), its nonzero \(\triangleright\)-products are
\[
e_1\triangleright e_1=e_3,\qquad
e_1\triangleright e_2=\lambda e_3,\qquad
e_2\triangleright e_2=e_3,
\]
and the corresponding \(\triangleleft\)-products are their negatives.

Then
\[
\boxed{A_\lambda\cong A_\mu\iff \mu=\pm\lambda.}
\]
Consequently the source's statement that the displayed \(AD_3^7(\lambda)\) family is pairwise non-isomorphic for all \(\lambda\in\mathbb C\) has a sign redundancy. For every \(\lambda\),
\[
A_\lambda\cong A_{-\lambda}
\]
via
\[
e_1\mapsto e_1,\qquad e_2\mapsto-e_2,\qquad e_3\mapsto e_3.
\]
The corrected moduli parameter is therefore
\[
\boxed{t=\lambda^2.}
\]

## Assumptions and scope

The statement is over \(\mathbb C\), exactly the field used in Theorem 4.1.

All products not displayed in the source table are zero. Since \(\triangleleft=-\triangleright\) on this family, an isomorphism is determined by preservation of the single bilinear product \(\triangleright\).

The claim concerns only the parameter identification inside the \(AD_3^7(\lambda)\) family. The other models in Theorem 4.1 have different product ranks or asymmetry type and are not asserted to merge with this family.

## Proof

For \(x,y\in W=\operatorname{span}\{e_1,e_2\}\), write
\[
x\triangleright y=(x^{\mathsf T}B_\lambda y)e_3,
\qquad
B_\lambda=
\begin{pmatrix}
1&\lambda\\
0&1
\end{pmatrix}.
\]
The product space is
\[
A_\lambda^2=\mathbb C e_3.
\]
Hence any algebra isomorphism \(F:A_\lambda\to A_\mu\) sends \(e_3\) to \(c e_3\) for some \(c\ne0\), and induces some \(P\in\operatorname{GL}_2(\mathbb C)\) on \(A_\lambda/A_\lambda^2\). Central shifts by multiples of \(e_3\) do not affect any product. The isomorphism condition is therefore
\[
P^{\mathsf T}B_\mu P=cB_\lambda.
\tag{1}
\]

For an invertible bilinear-form matrix \(B\), define its asymmetry
\[
S(B)=B^{-1}B^{\mathsf T}.
\]
Multiplying \(B\) by a nonzero scalar does not change \(S(B)\), and replacing \(B\) by \(P^{\mathsf T}BP\) conjugates \(S(B)\) by \(P\). Thus equation (1) implies that \(S(B_\lambda)\) and \(S(B_\mu)\) are similar.

A direct computation gives
\[
S(B_\lambda)=
\begin{pmatrix}
1-\lambda^2&-\lambda\\
\lambda&1
\end{pmatrix},
\qquad
\operatorname{tr}S(B_\lambda)=2-\lambda^2.
\]
Similarity therefore forces
\[
2-\lambda^2=2-\mu^2,
\]
so
\[
\mu^2=\lambda^2.
\]
Over \(\mathbb C\), this means
\[
\mu=\pm\lambda.
\]

Conversely, \(\mu=\lambda\) is trivial. If \(\mu=-\lambda\), put
\[
D=\operatorname{diag}(1,-1).
\]
Then
\[
D^{\mathsf T}B_{-\lambda}D=B_\lambda,
\]
which is exactly the change of basis
\[
e_1\mapsto e_1,\qquad e_2\mapsto-e_2,\qquad e_3\mapsto e_3.
\]
This proves the classification inside the family.

For completeness, the other nontrivial forms displayed in Theorem 4.1 do not create an additional identification with \(AD_3^7(\lambda)\): the \(\triangleright\)-forms for \(AD_3^5\) and \(AD_3^6\) have rank one, whereas \(B_\lambda\) has rank two. The \(AD_3^4\) form is nondegenerate alternating, whose asymmetry is \(-I\); for \(\lambda=\pm2\), where the characteristic polynomial of \(S(B_\lambda)\) becomes \((z+1)^2\), the matrix \(S(B_\lambda)\) is nevertheless non-scalar, so it is not similar to \(-I\).

## Verification

The included checker `artifacts/verify.py` symbolically verifies:

- the formula for \(B_\lambda^{-1}B_\lambda^{\mathsf T}\);
- the trace invariant \(2-\lambda^2\);
- the exact sign-change congruence \(D^{\mathsf T}B_{-\lambda}D=B_\lambda\);
- the rank separation from \(AD_3^5\) and \(AD_3^6\);
- the scalar-versus-Jordan separation from the alternating \(AD_3^4\) form at \(\lambda=\pm2\).

The checker returns `VERIFY_OK`.

## Relationship to prior work

Theorem 4.1 of the 2024 preprint states that every three-dimensional complex anti-dendriform algebra associated to the zero associative algebra is isomorphic to one of several "pairwise non-isomorphic" displayed models and includes the full family \(AD_3^7(\lambda)\) with \(\lambda\in\mathbb C\).

The same paper explicitly records a parameter identification for a different family in Theorem 4.2, namely \(AD_3^8(\alpha,\beta)\cong AD_3^8(-\beta,-\alpha)\). No analogous sign identification is stated for \(AD_3^7(\lambda)\).

Targeted searches for the exact family name, sign change, projective congruence, and corrections to the classification did not locate a published statement of \(AD_3^7(\lambda)\cong AD_3^7(-\lambda)\). The later journal article has the same title and authors; its publicly accessible metadata confirms the classification paper, but the full journal text was not accessible during this check. That remains a bibliographic risk rather than a mathematical one.

## Limitations

This is a correction to one parameter family, not a reclassification of every three-dimensional anti-dendriform algebra.

The proof establishes the exact equivalence relation inside \(AD_3^7(\lambda)\). It does not claim any change to the paper's existence or completeness arguments for the other families.

A correction may exist in inaccessible or unindexed later literature.

Failed searches do not prove novelty.

## References

1. K. Abdurasulov, J. Adashev, Z. Normatov, and Sh. Solijonova, “Classification of three-dimensional anti-dendriform algebras,” arXiv:2404.00981v1, first public version 1 April 2024. MSC 2020: 16P10, 17A30.
2. K. Abdurasulova, J. Adashev, Z. Normatov, and Sh. Solijonova, “Classification of three dimensional anti-dendriform algebras,” *Communications in Algebra* 53 (2025), 1887–1903, DOI 10.1080/00927872.2024.2426037.
