# Canonical duals of woven \(g\)-frames need not be woven

## Finding
Corollary 2.5 of Li--Leng--Huang--Li states that a woven family of \(g\)-frames remains woven after replacing each constituent \(g\)-frame by its own canonical dual.

This is false even for ordinary finite frames in \(\mathbb R^2\), viewed as scalar-valued \(g\)-frames.

Let
\[
F=(f_1,f_2,f_3)=(e_1,e_1,e_2)
\]
and
\[
G=(g_1,g_2,g_3)=(e_1,e_1+e_2,2e_1+e_2).
\]
For each subset
\[
\sigma\subset\{1,2,3\},
\]
choose \(f_i\) for \(i\in\sigma\) and \(g_i\) otherwise. Since
\[
f_1=g_1=e_1,
\]
the eight partitions give four distinct frame operators:
\[
M_0=
\begin{pmatrix}
6&3\\
3&2
\end{pmatrix},
\qquad
M_1=
\begin{pmatrix}
6&2\\
2&1
\end{pmatrix},
\]
\[
M_2=
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix},
\qquad
M_3=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix}.
\]
Their spectra are
\[
\{4-\sqrt{13},\,4+\sqrt{13}\},
\]
\[
\left\{\frac{7-\sqrt{41}}2,\,\frac{7+\sqrt{41}}2\right\},
\]
\[
\{1,3\},
\qquad
\{1,2\}.
\]
Therefore all weaves are frames, with universal bounds
\[
A=\frac{7-\sqrt{41}}2
\]
and
\[
B=4+\sqrt{13}.
\]

The frame operators of the two original frames are
\[
S_F=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix}
\]
and
\[
S_G=
\begin{pmatrix}
6&3\\
3&2
\end{pmatrix}.
\]
Thus
\[
\widetilde F=
\left(\frac12e_1,\frac12e_1,e_2\right),
\]
while
\[
S_G^{-1}=
\begin{pmatrix}
2/3&-1\\
-1&2
\end{pmatrix}
\]
gives
\[
\widetilde G=
\left(
\frac23e_1-e_2,
-\frac13e_1+e_2,
\frac13e_1
\right).
\]

Now choose the first two vectors from \(\widetilde F\) and the third vector from \(\widetilde G\). The resulting weave is
\[
\left(
\frac12e_1,
\frac12e_1,
\frac13e_1
\right),
\]
which does not span \(\mathbb R^2\). Hence the canonical duals are not woven.

## Assumptions and scope
Ordinary frames are special cases of \(g\)-frames by taking every coefficient space to be one-dimensional and setting
\[
\Lambda_i x=\langle x,f_i\rangle.
\]
Under this identification, the canonical dual \(g\)-frame
\[
\{\Lambda_iS_F^{-1}\}
\]
is induced by the ordinary canonical dual vectors
\[
\{S_F^{-1}f_i\}.
\]
Thus the finite-dimensional example lies exactly inside the scope of Corollary 2.5.

The result refutes the unconditional preservation of wovenness under separately taking canonical duals. It does not say canonical duals can never be woven; later literature gives several sufficient conditions under which they are.

## Proof
For a finite vector family \(V=(v_i)\), its frame operator is
\[
S_V=\sum_i v_iv_i^*.
\]
Direct summation over the possible mixed families gives the four matrices displayed above.

The smallest eigenvalue among them is
\[
\frac{7-\sqrt{41}}2>0,
\]
and the largest is
\[
4+\sqrt{13}.
\]
Hence the original pair \(F,G\) is woven with those universal bounds.

Next,
\[
S_F^{-1}=
\begin{pmatrix}
1/2&0\\
0&1
\end{pmatrix},
\]
so
\[
S_F^{-1}f_1=S_F^{-1}f_2=\frac12e_1,
\qquad
S_F^{-1}f_3=e_2.
\]
Also,
\[
S_G^{-1}=
\begin{pmatrix}
2/3&-1\\
-1&2
\end{pmatrix}.
\]
Multiplication gives
\[
S_G^{-1}g_1=\frac23e_1-e_2,
\]
\[
S_G^{-1}g_2=-\frac13e_1+e_2,
\]
and
\[
S_G^{-1}g_3=\frac13e_1.
\]
The mixed family using the first two canonical-dual vectors from \(F\) and the third from \(G\) lies entirely in the line \(\operatorname{span}\{e_1\}\), so it is not a frame.

For a simple repair, suppose every constituent frame has the same frame operator \(S\). For an original weaving with energy \(E_\sigma(x)\), the corresponding canonical-dual weaving has energy
\[
E_\sigma(S^{-1}x).
\]
If
\[
A\|y\|^2\le E_\sigma(y)\le B\|y\|^2
\]
for every partition and every \(y\), then
\[
\frac{A}{\|S\|^2}\|x\|^2
\le
E_\sigma(S^{-1}x)
\le
B\|S^{-1}\|^2\|x\|^2.
\]
So a common frame operator restores the desired qualitative conclusion.

## Verification
The complete public arXiv version 1 was inspected. It defines canonical dual \(g\)-frames as
\[
\{\Lambda_iS_\Lambda^{-1}\}
\]
and Corollary 2.5 states that separately taking these canonical duals preserves wovenness with bounds \(1/B\) and \(1/A\).

The later arXiv version 3 contains the same Corollary 2.5. The journal version has the same title and authors and was published in 2020, but its full theorem text was not available through the checked public publisher preview; the accepted claim therefore refers directly to the verified public arXiv statement.

All matrix products and spectra in the counterexample are exact.

## Relationship to prior work
The source itself notes on arXiv that part of its argument is wrong, but the notice does not identify this canonical-dual statement.

Subsequent work on weaving and duality treats preservation by canonical duals conditionally. A 2019 preprint on weaving Hilbert-space frames and duality gives sufficient conditions for canonical duals and related dual frames to be woven. A 2021 paper on excess and duality in woven frames likewise gives a norm-closeness condition for canonical duals and separately records that canonical Parseval frames of woven Riesz bases need not be woven.

Those results show that dualization is not automatically compatible with weaving, but the checked material does not contain the present three-vector counterexample or a source-specific correction of Corollary 2.5.

Targeted searches for the exact arXiv identifier, theorem label, canonical-dual formulation, redundant two-dimensional counterexamples, and correction terminology did not locate an indexed source that already gives this correction.

## Limitations
The example disproves the unconditional conclusion of Corollary 2.5 and supplies one simple sufficient repair, namely a common constituent frame operator.

It does not characterize all tuples of frame operators for which canonical dualization preserves wovenness. Quantitative sufficient conditions using closeness of inverse frame operators are available in later literature.

The complete version-of-record theorem text was not publicly inspectable in the checked route, so no claim is made that the published journal copy retained the corollary verbatim.

## References
1. D. Li, J. Leng, T. Huang and X. Li, *On weaving \(g\)-frames for Hilbert spaces*, arXiv:1709.05154v1, 15 September 2017.
2. D. Li, J. Leng, T. Huang and X. Li, *On Weaving \(g\)-Frames for Hilbert Spaces*, Complex Analysis and Operator Theory 14 (2020), article 33, DOI 10.1007/s11785-020-00991-7.
3. F. Arabyani Neyshaburi and A. A. Arefijamaal, *Weaving Hilbert Space Frames and Duality*, arXiv:1909.08835v1, 19 September 2019.
4. E. Agheshteh Moghaddam and A. A. Arefijamaal, *On Excesses and Duality in Woven Frames*, arXiv:2101.00710v1, 3 January 2021; later published in Bulletin of the Malaysian Mathematical Sciences Society, DOI 10.1007/s40840-021-01112-z.
