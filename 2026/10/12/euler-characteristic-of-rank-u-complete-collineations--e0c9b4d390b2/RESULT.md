# Euler characteristic of rank-\(u\) complete collineations
## Finding
Let \(V,W\) be complex vector spaces with
\[
\dim V=v,
\qquad
\dim W=w,
\]
and let
\[
1\le u\le \min(v,w).
\]
Let
\[
\mathcal C_u(V,W)
\]
be the projective variety of rank-\(u\) complete collineations in the sense of Vainsencher--Thaddeus.

Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\mathcal C_u(V,W)\right)
=
\binom vu\binom wu (u!)^2
=
\frac{v!\,w!}{(v-u)!(w-u)!}.
}
\]

In particular, for the square full-rank compactification
\[
\mathcal C_n(\mathbb C^n,\mathbb C^n)
\]
of \(\operatorname{PGL}_n\),
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\mathcal C_n(\mathbb C^n,\mathbb C^n)\right)
=
(n!)^2.
}
\]

Thus the Euler characteristic factors into the two Grassmannian cell counts and the square of the Weyl-group order of type \(A_{u-1}\).

## Assumptions and scope
The base field is \(\mathbb C\).

Thaddeus defines the rank-\(u\) complete-collineation space as the closure of the exterior-power map over
\[
\operatorname{Gr}_u(V),
\]
and recalls Vainsencher's construction by successive blow-ups of the proper transforms of the lower-rank determinantal loci in
\[
\mathbb P\operatorname{Hom}(S_V,W).
\]

All varieties in the blow-up construction are smooth at the stage where they are blown up. Ordinary and compactly supported Euler characteristics agree because the final complete-collineation space is projective.

## Proof
First treat the square full-rank space
\[
C_n
=
\mathcal C_n(\mathbb C^n,\mathbb C^n).
\]
Vainsencher's construction starts from
\[
\mathbb P\operatorname{Hom}(\mathbb C^n,\mathbb C^n)
\cong
\mathbb P^{n^2-1},
\]
whose Euler characteristic is
\[
n^2.
\]

For
\[
1\le r<n,
\]
the proper transform of the rank-at-most-\(r\) determinantal locus is the compactified rank-\(r\) center. A rank-\(r\) map determines its kernel, its image, and an invertible map between the corresponding \(r\)-dimensional quotient and image. After the lower-rank blow-ups, the last datum is compactified by \(C_r\). Consequently the center is a locally trivial bundle over
\[
\operatorname{Gr}_{n-r}(\mathbb C^n)
\times
\operatorname{Gr}_{r}(\mathbb C^n)
\]
with fiber \(C_r\), hence has Euler characteristic
\[
\binom nr^2\chi_{\mathrm{top}}(C_r).
\]

Its codimension remains
\[
(n-r)^2.
\]
For a blow-up of a smooth variety along a smooth center of codimension \(c\),
\[
\chi_{\mathrm{top}}(\operatorname{Bl}_Z X)
=
\chi_{\mathrm{top}}(X)+(c-1)\chi_{\mathrm{top}}(Z),
\]
because the exceptional divisor is a \(\mathbb P^{c-1}\)-bundle over \(Z\).

Therefore
\[
\chi_{\mathrm{top}}(C_n)
=
n^2+
\sum_{r=1}^{n-1}
\left((n-r)^2-1\right)
\binom nr^2
\chi_{\mathrm{top}}(C_r).
\]

Inductively assume
\[
\chi_{\mathrm{top}}(C_r)=(r!)^2
\qquad
(r<n).
\]
Set
\[
j=n-r.
\]
Then
\[
\binom nr^2(r!)^2
=
\frac{(n!)^2}{(j!)^2},
\]
and
\[
\frac{j^2-1}{(j!)^2}
=
\frac{1}{((j-1)!)^2}
-
\frac{1}{(j!)^2}.
\]
Hence
\[
\frac{\chi_{\mathrm{top}}(C_n)}{(n!)^2}
=
\frac{n^2}{(n!)^2}
+
\sum_{j=1}^{n-1}
\frac{j^2-1}{(j!)^2}.
\]
The sum telescopes:
\[
\sum_{j=1}^{n-1}
\frac{j^2-1}{(j!)^2}
=
1-\frac{1}{((n-1)!)^2},
\]
while
\[
\frac{n^2}{(n!)^2}
=
\frac{1}{((n-1)!)^2}.
\]
Thus
\[
\chi_{\mathrm{top}}(C_n)=(n!)^2.
\]

Now return to arbitrary \(V,W,u\). Vainsencher's construction starts from the projective bundle
\[
\mathbb P\operatorname{Hom}(S_V,W)
\longrightarrow
\operatorname{Gr}_u(V),
\]
whose Euler characteristic is
\[
\binom vu\,uw.
\]

For
\[
1\le r<u,
\]
the rank-\(r\) center records:
an \(u\)-plane in \(V\); an \((u-r)\)-plane kernel inside it; an \(r\)-plane image in \(W\); and a square complete collineation of rank \(r\) between the quotient and the image. Its Euler characteristic is therefore
\[
\binom vu\binom ur\binom wr(r!)^2.
\]
The determinantal codimension is
\[
(u-r)(w-r).
\]

The blow-up formula gives
\[
\chi_{\mathrm{top}}\!\left(\mathcal C_u(V,W)\right)
=
\binom vu
\left[
uw+
\sum_{r=1}^{u-1}
\left((u-r)(w-r)-1\right)
\binom ur\binom wr(r!)^2
\right].
\]

Put
\[
q=w-u,
\qquad
j=u-r.
\]
Using
\[
\binom ur\binom wr(r!)^2
=
\frac{u!\,w!}{j!(q+j)!},
\]
one has
\[
\frac{j(q+j)-1}{j!(q+j)!}
=
\frac{1}{(j-1)!(q+j-1)!}
-
\frac{1}{j!(q+j)!}.
\]
Again the sum telescopes, while the initial term \(uw\) supplies exactly the terminal correction. The bracket becomes
\[
\frac{u!\,w!}{(w-u)!}.
\]
Thus
\[
\chi_{\mathrm{top}}\!\left(\mathcal C_u(V,W)\right)
=
\binom vu\frac{u!\,w!}{(w-u)!}
=
\binom vu\binom wu(u!)^2.
\]
This proves the formula.

## Verification
The bundled checker evaluates the blow-up recurrence exactly for
\[
1\le u\le \min(v,w),
\qquad
1\le v,w\le 14,
\]
and compares it with
\[
\binom vu\binom wu(u!)^2.
\]

It separately verifies the square recurrence
\[
\chi_{\mathrm{top}}(C_n)
=
n^2+
\sum_{r=1}^{n-1}
\left((n-r)^2-1\right)
\binom nr^2
\chi_{\mathrm{top}}(C_r)
\]
through \(n=30\), as well as both telescoping identities used in the symbolic proof.

These finite computations are regression evidence only. The theorem for all dimensions follows from the blow-up geometry and the two exact telescoping identities.

## Relationship to prior work
Thaddeus recalls Vainsencher's construction of rank-\(u\) complete collineations by iterated blow-ups of lower-rank loci and identifies the resulting projective variety with several quotient constructions. That provides the geometric input used here.

Later work on spaces of complete collineations and complete singular collineations studies their wonderful structure, divisor cones, Cox rings, Mori chamber decompositions, and related moduli spaces. Targeted searches for Euler characteristics, Poincaré polynomials, factorial formulas, and torus-fixed-point counts did not locate the closed formula above.

The formula is not a determinantal-rank-locus Euler characteristic: the complete-collineation space is the iterated resolution/compactification, and every exceptional divisor contributes through the blow-up recurrence.

## Limitations
The result determines only the ordinary Euler characteristic. It does not give the full Poincaré polynomial, Chow ring, intersection cohomology of the original determinantal loci, or multiplicative structure in cohomology.

The proof uses the standard Vainsencher compactification. It does not assert that an arbitrary compactification of the same open rank-\(u\) locus has the same Euler characteristic.

Because the recurrence collapses by an elementary telescoping identity, an older unindexed computation remains a residual novelty risk.

## References
Michael Thaddeus, *Complete collineations revisited*, arXiv:math/9808114, first submitted 27 August 1998; *Mathematische Annalen* 315 (1999), 469--495, DOI 10.1007/s002080050324.

Alex Casarotti, Elsa Corniani, and Alex Massarenti, *Complete singular collineations and quadrics*, arXiv:2111.02940, first submitted 4 November 2021.
