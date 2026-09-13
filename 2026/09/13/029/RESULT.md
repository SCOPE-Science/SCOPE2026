# Universal small-graph forcing cutoff m = 4 for 2-block graphons

## Context

A graphon is finitely forcible if it is determined up to weak isomorphism by
finitely many homomorphism densities. Lovasz-Szegedy and Lovasz-Sos showed
every stepfunction graphon is finitely forcible, but the forcing family is
parameter-dependent and not explicit. The admitted target asked for a uniform
cutoff: is there an integer m <= 6 such that every 2-block step graphon is
determined up to weak isomorphism by connected-graph densities on at most m
vertices? This record resolves the target positively with m = 4 and an
explicit six-graph forcing set.

## Definitions

Fix a split a in (0,1), b = 1-a, and values q11, q12, q22 in [0,1]. The
2-block graphon W has value q11 on [0,a)x[0,a), q22 on [a,1]x[a,1], and q12
on cross blocks. Block degrees are d1 = a q11 + b q12, d2 = a q12 + b q22;
degree moments m_k = a d1^k + b d2^k. Weak isomorphism here is equality up to
the block swap (a,q11,q12,q22) ~ (b,q22,q12,q11) plus the constant-graphon
identification when the graphon is a.e. constant. Graphs used: edge K2,
2-star P3, 3-star S3, 3-edge path P4, triangle K3, diamond (K4 minus an edge),
all connected on at most 4 vertices.

## Result

Every 2-block step graphon is determined up to weak isomorphism by the
homomorphism densities t(F,W) as F ranges over connected simple graphs on at
most 4 vertices. Hence the universal cutoff m = 4 <= 6 works. The disproof
alternative (pairs agreeing on all connected graphs on at most m vertices for
every m <= 6) is false: no such pair exists even for m = 4.

## Proof / evidence

Exact polynomial identities, verified symbolically by exhaustive expansion
over 2^|V| block labellings (verify_identities.py, ALL OK): t(K2)=m1,
t(P3)=m2, t(S3)=m3; t(P4)=m3-ab q12 (d1-d2)^2; variance v=m2-m1^2=ab(d1-d2)^2
and skewness mu3=m3-3m1m2+2m1^3=-ab(a-b)(d1-d2)^3. On the regular slice
d1=d2=:d with c=q12, u=d-c: t(K3)=d^3+u^3 and
t(diamond)=K(c,d)+u^5/(ab) with K(c,d)=4c^5-19c^4d+34c^3d^2-28c^2d^3+10cd^4.

Reconstruction: (1) If v=0 the graphon is regular; if v>0 then
s=mu3^2/v^3=(a-b)^2/(ab) pins ab=1/(s+4), hence {a,b}, then with m1, the gap
(d1-d2)^2=v/(ab), and the sign rule the unordered pair {(a,d1),(b,d2)} is
pinned up to swap. (2) If d1!=d2, the P4 identity gives
q12=(m3-t(P4))/(ab(d1-d2)^2), then q11,q22 from d1,d2. (3) If d1=d2=:d, the
triangle identity pins u via unique real cube root, hence c; if u=0 the
graphon is a.e. constant d; if u!=0 the diamond identity pins ab and hence a
up to swap, then q11=c+u/a, q22=c+u/b. Identities are polynomial, hence valid
on boundary q in {0,1}. Randomized numeric reconstruction checks passed.

## Limitations

Specific to exactly-2-block graphons with the stated parametrization; does
not extend to k>=3 blocks. Uses only the six named connected graphs on at
most 4 vertices. Weak isomorphism is characterized concretely via block swap
rather than the general Lovasz uniqueness theorem.

## Reproducibility

Run output/artifacts/verify_identities.py (sympy) to recheck all eight
identities; rerun random-parameter reconstruction checks described above.

## References

L. Lovasz, B. Szegedy, Finitely forcible graphons (arXiv:0901.0929);
Lovasz-Sos stepwise forcibility; Noel-Kral-Lovasz-Sosnovec (2020), Cooper-
Kral-Martins (2018) on finitely forcible graphons.
