# Sub-Hilbert modified generalized von Neumann–Jordan profile of the regular octagonal plane
## Finding
Let \(X_8=(\mathbb R^2,N)\), where
\[
N(s,t)=\max\!\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For \(p\ge1\), define the modified generalized von Neumann–Jordan constant
\[
\widetilde C_{\mathrm{NJ}}^{(p)}(X)
=\sup_{x,y\in S_X}
\frac{\|x+y\|^p+\|x-y\|^p}{2^p}.
\]
Then, throughout the sub-Hilbert range,
\[
\widetilde C_{\mathrm{NJ}}^{(p)}(X_8)=1+(\sqrt2-1)^p,
\qquad 1\le p\le2.
\]
For \(1<p<2\), Yang and Wang's published unrestricted generalized constant is
\[
C_{\mathrm{NJ}}^{(p)}(X_8)
=2^{2-p}\left(1+(\sqrt2-1)^{p/(p-1)}\right)^{p-1},
\]
and it is strictly larger than the displayed modified value. At \(p=2\), both constants equal \(4-2\sqrt2\). Combining the new sub-Hilbert calculation with Yang and Wang's published \(p\ge2\) formula shows that the equal-radius restriction is binding exactly for \(1<p<2\), and is non-binding for \(p\ge2\).

## Assumptions and scope
The scalar field is real. The unit ball of \(X_8\) is the regular octagon whose vertices are the dihedral orbit of
\[
(1,\sqrt2-1).
\]
The new exact calculation concerns \(1\le p<2\), with \(p=2\) included as the shared endpoint. The statement about \(p\ge2\) is used only to locate the comparison threshold and is already contained in the published unrestricted regular-octagon formula together with the same adjacent-vertex witness.

## Proof
Put \(a=\sqrt2-1\). Fu and Li prove the equivalent ball formulation
\[
\widetilde C_{\mathrm{NJ}}^{(p)}(X)
=\sup_{x,y\in B_X}
\frac{\|x+y\|^p+\|x-y\|^p}{2^p}
\]
for every positive exponent. For \(p\ge1\), the numerator is separately convex in each of \(x\) and \(y\): the norm is convex, and the map \(r\mapsto r^p\) is convex and increasing on \([0,\infty)\). Therefore a maximum over the compact polygon \(B_{X_8}\times B_{X_8}\) is attained at a pair of extreme points.

Up to the dihedral symmetry of the octagon and exchange of the two shifted norms, only the cyclic separation of two vertices matters. Fix \(u=(1,a)\). For a second vertex \(v\), the possible ordered pairs
\[
\bigl(N(u+v),N(u-v)\bigr)
\]
are
\[
(2,0),\qquad (2,2a),\qquad (\sqrt2,\sqrt2),
\]
together with the swapped versions. Hence the normalized objective can take at most
\[
1,\qquad 1+a^p,\qquad 2^{1-p/2}.
\]
The middle value always dominates the last one for \(p\ge1\). Indeed, \(1+a=\sqrt2\), and convexity of \(r\mapsto r^p\) gives
\[
1+a^p\ge 2\left(\frac{1+a}{2}\right)^p
=2^{1-p/2}.
\]
For \(p>1\) the inequality is strict because \(1\ne a\). Thus
\[
\widetilde C_{\mathrm{NJ}}^{(p)}(X_8)=1+a^p
\]
for every \(p\ge1\), and in particular for \(1\le p\le2\). Adjacent octagon vertices attain equality.

It remains to compare the sub-Hilbert branch with the unrestricted constant. For \(1<p<2\), let \(q=p/(p-1)\). Yang and Wang proved
\[
C_{\mathrm{NJ}}^{(p)}(X_8)
=2^{2-p}(1+a^q)^{p-1}.
\]
Taking \(p\)-th roots rewrites this as
\[
\left(C_{\mathrm{NJ}}^{(p)}(X_8)\right)^{1/p}
=2^{1/p-1/q}\,\|(1,a)\|_{\ell_q^2},
\]
whereas
\[
\left(\widetilde C_{\mathrm{NJ}}^{(p)}(X_8)\right)^{1/p}
=\|(1,a)\|_{\ell_p^2}.
\]
Because \(p<q\), the sharp two-coordinate norm comparison gives
\[
\|(1,a)\|_{\ell_p^2}
<2^{1/p-1/q}\,\|(1,a)\|_{\ell_q^2};
\]
the inequality is strict because the two positive coordinates are unequal. This proves strict separation for \(1<p<2\). At \(p=2\), both formulas reduce to \(1+a^2=4-2\sqrt2\). Yang and Wang's published formula \(C_{\mathrm{NJ}}^{(p)}(X_8)=1+a^p\) for \(p\ge2\), together with the adjacent-vertex lower bound for the modified constant and the general inequality \(\widetilde C_{\mathrm{NJ}}^{(p)}\le C_{\mathrm{NJ}}^{(p)}\), yields equality for every \(p\ge2\).

## Verification
The finite geometric reduction was replayed by `verify.py` using exact arithmetic in \(\mathbb Q(\sqrt2)\). It constructs all eight octagon vertices, checks their unit norm, exhausts all sixty-four ordered vertex pairs, and verifies that the only unordered shifted-norm patterns are \((2,0)\), \((2,2(\sqrt2-1))\), and \((\sqrt2,\sqrt2)\). It also checks the endpoint identity \(1+(\sqrt2-1)^2=4-2\sqrt2\). The universal inequalities in \(p\) are proved above by convexity and the sharp finite-dimensional \(\ell_p\)-to-\(\ell_q\) norm comparison; they are not inferred from numerical sampling.

## Relationship to prior work
Yang and Wang introduced the modified generalized von Neumann–Jordan constant in 2017; the official publication record gives 10 May 2017 and primary MSC \(46B20\). Their defining article establishes relations with the unrestricted generalized constant but does not, in the available abstract and metadata, state a regular-octagon profile. Fu and Li's 2022 full text restates the definition, proves the ball formulation used above, develops general structural results, and gives classical \(\ell_r\) and \(L_r\) examples rather than a regular-octagon calculation.

A different 2017 paper by Yang and Wang computes the unrestricted \(C_{\mathrm{NJ}}^{(p)}(X_8)\) exactly. Its full text was inspected: it studies the unrestricted normalization and gives the two exponent branches quoted above. It does not define or compute the modified unit-sphere constant. For \(p\ge2\), its stronger unrestricted value, combined with the same adjacent-vertex witness, already forces equality of the modified and unrestricted constants; that covered implication is not presented here as new. The new content is the exact modified sub-Hilbert branch and the resulting sharp comparison showing that the equal-radius restriction becomes active precisely below \(p=2\).

Targeted indexed-literature searches for the modified exponent profile, regular-octagon aliases, the exact radical formula, and an equal-radius phase transition did not locate a statement covering the sub-Hilbert result. A closely related quadratic unit-sphere profile varies a mixing parameter while fixing exponent two; its statement does not imply the exponent profile proved here.

## Limitations
This is an exact result for one two-dimensional polyhedral Banach space. It does not classify other regular polygons or determine modified constants for \(0<p<1\). The full text of the 2017 defining article was not available from the lawful sources checked; its official abstract and metadata were inspected, and Fu–Li's later full text explicitly records the definition and the scope of the 2017 estimates. This leaves ordinary bibliographic risk, but no inspected source gives the sub-Hilbert regular-octagon formula or the comparison threshold as a theorem.

## References
1. C. S. Yang and F. H. Wang, “An extension of a simply inequality between von Neumann–Jordan and James constants in Banach spaces,” Acta Mathematica Sinica, English Series 33 (2017), 1287–1296. DOI: 10.1007/s10114-017-6211-6. Published 10 May 2017.
2. C. Yang and T. Wang, “Generalized von Neumann-Jordan constant \(C_{\mathrm{NJ}}^{(p)}(X)\) for the regular octagon space,” Mathematical Inequalities & Applications 20 (2017), 483–490. DOI: 10.7153/mia-20-32.
3. Y. Fu and Y. Li, “The relations between the von Neumann–Jordan type constant and some geometric properties of Banach spaces,” Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas 117 (2023), article 25. DOI: 10.1007/s13398-022-01358-7. Published online 24 November 2022.
