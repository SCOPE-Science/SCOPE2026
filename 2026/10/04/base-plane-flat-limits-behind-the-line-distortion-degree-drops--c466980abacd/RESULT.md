# Base-plane flat limits behind the line-distortion degree drops
\
## Finding
For the distortion vector \(u=(1,2,3)\), write the coordinates of the ambient scroll as
\[
(a_0,a_1\mid b_0,b_1,b_2\mid c_0,c_1,c_2,c_3).
\]
For a line \(L_{{\alpha,\beta,\gamma}}=V(\alpha a+\beta b+\gamma c)\subset\mathbb P^2\), its distortion surface is a linearly embedded smooth rational normal scroll
\[
S(2,3),\quad S(1,3),\quad S(1,2)
\]
according as \(\alpha\ne0\), \(\alpha=0,\beta\ne0\), or \(\alpha=\beta=0\). These have degrees \(5,4,3\), respectively.

The sharper statement concerns the degree jumps. Let
\[
B=V(a_0,b_0,b_1,c_0,c_1,c_2)\cong\mathbb P^2,
\]
the base-locus plane of the rational map from the ambient scroll to \(\mathbb P^2\). Along the path \(V(t a+b)\), the scheme-theoretic flat limit at \(t=0\) is
\[
S(1,3)\cup B,
\]
whereas the actual special distortion surface is only \(S(1,3)\). Along the path \(V(t b+c)\), the flat limit is
\[
S(1,2)\cup B,
\]
whereas the actual special distortion surface is only \(S(1,2)\). In both limits the two components meet along a ruling line. Hence each adjacent degree drop loses exactly one reduced degree-one component, namely the same base-locus plane \(B\).

## Assumptions and scope
Work over a field of characteristic zero. The statement concerns Example 2.1 of Kileel--Kukelova--Pajdla--Sturmfels for the one-parameter distortion vector \(u=(1,2,3)\). The notation \(S(p,q)\) denotes the standard two-dimensional rational normal scroll obtained from blocks of lengths \(p+1\) and \(q+1\). The flat limits are taken after closing the punctured one-parameter families over the local parameter line and removing \(t\)-torsion, equivalently by \(t\)-saturation.

## Proof
The ambient rational normal scroll \(S_u\subset\mathbb P^8\) has prime ideal given by the \(2\times2\) minors of
\[
H=\begin{{pmatrix}}
a_0&b_0&b_1&c_0&c_1&c_2\\
a_1&b_1&b_2&c_1&c_2&c_3
\end{{pmatrix}}.
\]
Its dense parametrization is
\[
(a,a\tau\mid b,b\tau,b\tau^2\mid c,c\tau,c\tau^2,c\tau^3).
\]
If \(\alpha\ne0\), solve \(a=-(\beta/\alpha)b-(\gamma/\alpha)c\). Then \(a_0,a_1\) are linear combinations of the first two coordinates of the \(b\)- and \(c\)-blocks, and the remaining coordinates are exactly the standard parametrization of \(S(2,3)\). If \(\alpha=0\) and \(\beta\ne0\), solve \(b=-(\gamma/\beta)c\); the remaining independent blocks have lengths \(2\) and \(4\), giving \(S(1,3)\). If \(\alpha=\beta=0\), then \(c=0\), leaving the blocks of lengths \(2\) and \(3\), hence \(S(1,2)\). Standard rational normal scrolls with positive block lengths are smooth, and their degrees are the sums of the two scroll parameters, giving \(5,4,3\).

For the first boundary path, the closure of the punctured family \(V(t a+b)_{[u]}\) is defined by
\[
\mathcal I_1=I_2(H)+(t a_0+b_0,\ t a_1+b_1).
\]
Exact Gröbner elimination verifies \(\mathcal I_1:t^\infty=\mathcal I_1\), so its special fiber is the Hilbert flat limit. Setting \(t=0\) gives
\[
J_1=I_2(H)+(b_0,b_1).
\]
Let
\[
K_{{13}}=(b_0,b_1,b_2)+I_2\begin{{pmatrix}}a_0&c_0&c_1&c_2\\a_1&c_1&c_2&c_3\end{{pmatrix}}
\]
be the ideal of the actual special surface \(S(1,3)\), and let \(P_B=(a_0,b_0,b_1,c_0,c_1,c_2)\). Direct ideal calculation gives
\[
J_1=K_{{13}}\cap P_B.
\]
Moreover, \(K_{{13}}+P_B=(a_0,b_0,b_1,b_2,c_0,c_1,c_2)\), so the intersection has free homogeneous coordinates \([a_1:c_3]\) and is a line, namely the limiting ruling over \(\tau=\infty\).

For the second boundary path,
\[
\mathcal I_2=I_2(H)+(t b_0+c_0,\ t b_1+c_1,\ t b_2+c_2)
\]
is likewise \(t\)-saturated. Its special fiber is
\[
J_2=I_2(H)+(c_0,c_1,c_2).
\]
With
\[
K_{{12}}=(c_0,c_1,c_2,c_3)+I_2\begin{{pmatrix}}a_0&b_0&b_1\\a_1&b_1&b_2\end{{pmatrix}},
\]
exact ideal arithmetic gives \(J_2=K_{{12}}\cap P_B\). Here \(K_{{12}}+P_B=(a_0,b_0,b_1,c_0,c_1,c_2,c_3)\), leaving the line with homogeneous coordinates \([a_1:b_2]\). Thus both adjacent flat limits acquire exactly the same reduced plane \(B\), accounting scheme-theoretically for the missing unit of degree.

## Verification
The bundled script `verify_distortion_line_scrolls.py` uses exact symbolic arithmetic. It checks that restricting the ambient determinantal ideal gives the ideals of \(S(2,3)\), \(S(1,3)\), and \(S(1,2)\); verifies both family ideals are unchanged by \(t\)-saturation; computes the two special-fiber ideal intersections with \(B\); and verifies that the component intersections are projective lines. A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Kileel--Kukelova--Pajdla--Sturmfels define the ambient smooth rational normal scroll, identify its base-locus plane, and in Example 2.1 record that line-distortion surfaces have degrees \(5,4,3\) on the three coefficient strata. The inspected paper does not identify the three surfaces as the scrolls above, and more importantly does not analyze the coefficient-boundary family in the Hilbert scheme or identify the base-locus plane as the extra component in the flat limits. Targeted searches for the exact scroll types and for a base-plane flat-limit description did not locate an equivalent statement.

## Limitations
The result treats the specific distortion vector \(u=(1,2,3)\) and the two adjacent coordinate-boundary paths. It does not classify flat limits for arbitrary paths in the dual projective plane, arbitrary distortion vectors, or higher-dimensional source varieties. The calculation is scheme-theoretic over characteristic zero; behavior in small positive characteristic was not analyzed.

## References
1. J. Kileel, Z. Kukelova, T. Pajdla, B. Sturmfels, *Distortion Varieties*, arXiv:1610.01860v1, 6 October 2016; *Foundations of Computational Mathematics* 18 (2018), 1043--1071, DOI 10.1007/s10208-017-9361-0.
2. D. Eisenbud, J. Harris, *On varieties of minimal degree (a centennial account)*, in *Algebraic Geometry, Bowdoin 1985*, Proc. Sympos. Pure Math. 46 (1987), 3--13.
