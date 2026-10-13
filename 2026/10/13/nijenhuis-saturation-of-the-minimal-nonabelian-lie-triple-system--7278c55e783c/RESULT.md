# Nijenhuis saturation of the minimal nonabelian Lie triple system

## Finding

Let \(K\) be a field with \(\operatorname{char}K\ne2\), and let \(T_K\) have basis \(\{e_1,e_2\}\) with
\[
[e_1,e_2,e_2]=e_1,\qquad [e_2,e_1,e_2]=-e_1.
\]
Equivalently,
\[
[x,y,z]=(x_1y_2-x_2y_1)z_2e_1.
\]

For the two-order Nijenhuis identity
\[
\begin{aligned}
[Nx,Ny,Nz]={}&N([x,Ny,Nz]+[Nx,y,Nz]+[Nx,Ny,z])\\
&-N^2([Nx,y,z]+[x,Ny,z]+[x,y,Nz])+N^3[x,y,z],
\end{aligned}
\]
every endomorphism is a solution:
\[
\boxed{\operatorname{Nij}(T_K)=\operatorname{End}(T_K).}
\]

For
\[
N=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
the induced Nijenhuis bracket is
\[
\boxed{[x,y,z]_N=\det(x,y)(cz_1+dz_2)(de_1-ce_2).}
\]
Hence it is zero exactly when \((c,d)=(0,0)\). If \((c,d)\ne(0,0)\), put
\[
\ell(z)=cz_1+dz_2,\qquad w=de_1-ce_2.
\]
Choose \(v\) with \(\ell(v)=1\). Then \(\ell(w)=0\), \(\det(w,v)=1\), and
\[
[w,v,v]_N=w,
\]
so the induced system is isomorphic to \(T_K\).

Over every odd finite field \(\mathbf F_q\),
\[
\boxed{|\operatorname{Nij}(T_{\mathbf F_q})|=q^4.}
\]
Exactly \(q^2\) operators induce the zero bracket and \(q^4-q^2\) induce the nonabelian isomorphism type. The rank profile is
\[
\boxed{\left(1,(q-1)(q+1)^2,q(q-1)^2(q+1)\right)}.
\]
Over \(\mathbf F_{q^m}\) the count is \(q^{4m}\), hence
\[
\boxed{Z(T)=\frac{1}{1-q^4T}.}
\]

## Assumptions and scope

Xiao, Teng, and Long restate the two-order Hom-Lie-triple Nijenhuis identity and its induced bracket in their work on generalized Reynolds operators. Their preprint was posted on 2 January 2024 and lists \(17A30\) first among its Mathematics Subject Classification codes. They attribute the two-order Hom-Nijenhuis notion to earlier work of Chen, Hou, and Ma.

The theorem uses the untwisted case \(\alpha=\mathrm{id}\). Characteristic \(2\) is excluded. The result concerns this single minimal nonabelian two-dimensional Lie triple system.

## Proof

Substitute
\[
[x,y,z]=\det(x,y)z_2e_1
\]
and a symbolic matrix \(N=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\) into the displayed two-order Nijenhuis defect. Every coefficient cancels identically, so the defect is zero for arbitrary \(a,b,c,d\).

For the induced bracket
\[
\begin{aligned}
[x,y,z]_N={}&[x,Ny,Nz]+[Nx,y,Nz]+[Nx,Ny,z]\\
&-N([Nx,y,z]+[x,Ny,z]+[x,y,Nz])+N^2[x,y,z],
\end{aligned}
\]
direct simplification yields
\[
[x,y,z]_N=\det(x,y)(cz_1+dz_2)(de_1-ce_2).
\]
The basis argument with \(w\) and \(v\) above proves the nonzero isomorphism claim.

Over \(\mathbf F_q\), all \(q^4\) matrices occur. Vanishing of the second row gives the \(q^2\) zero deformations. The rank counts are the standard counts of \(2\times2\) matrices:
\[
1,\qquad \frac{(q^2-1)^2}{q-1},\qquad |\mathrm{GL}_2(\mathbf F_q)|.
\]

## Verification

The bundled checker symbolically reconstructs the universal Nijenhuis defect and verifies that it is identically zero. It independently derives the displayed induced bracket.

It exhaustively checks all endomorphisms over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,\quad\mathbf F_{11},
\]
verifying the zero-deformation fiber, the nonzero normalizing basis, and the rank profile. It returns `VERIFY_OK`.

Finite enumeration is replay evidence; the saturation theorem is a symbolic identity.

## Relationship to prior work

The 2024 source supplies the general two-order Nijenhuis identity, not a classification on this two-dimensional object. The earlier Chen–Hou–Ma paper develops product and complex structures on Hom-Lie triple systems and is cited as the origin of this Nijenhuis notion.

Focused searches for the exact multiplication, “every endomorphism” saturation, two-dimensional Nijenhuis classifications, and the induced-bracket formula did not locate a covering result. A separate Reynolds classification on a twisted version of the same ternary product uses a different operator identity and does not imply the present theorem.

## Limitations

The theorem uses the two-order Hom-Lie-triple Nijenhuis convention, not other first-order ternary deformation conventions.

It treats one two-dimensional Lie triple system and excludes characteristic \(2\).

Failed searches do not prove absolute historical novelty.

## References

1. Y. Xiao, W. Teng, and F. Long, “Generalized Reynolds Operators on Hom-Lie Triple Systems,” Preprints.org `202401.0052.v1`, first public 2 January 2024; *Symmetry* 16 (2024), 262, DOI `10.3390/sym16030262`.
2. L. Chen, Y. Hou, and Y. Ma, “Product and complex structures on Hom-Lie triple systems,” *Journal of Shandong University (Natural Science)* 56 (2021), 48–60, DOI `10.6040/j.issn.1671-9352.9.2021.008`.
