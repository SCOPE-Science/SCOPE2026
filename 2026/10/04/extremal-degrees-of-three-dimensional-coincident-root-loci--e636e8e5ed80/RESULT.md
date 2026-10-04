# Extremal degrees of three-dimensional coincident root loci
## Finding
Let \(d\ge 3\). For a partition \(\lambda=(a,b,c)\) with \(1\le a\le b\le c\) and \(a+b+c=d\), let \(\Delta_\lambda\subset\mathbb P(\operatorname{{Sym}}^d\mathbb C^2)\) be the coincident root locus of binary degree-\(d\) forms having three distinct roots with multiplicities \(a,b,c\), after taking Zariski closure. Its projective dimension is three.

For \(d\ge6\), there is a unique partition maximizing \(\deg\Delta_\lambda\). Write \(d=3q+r\), where \(r\in\{{0,1,2\}}\). The maximizer and its degree are
\[
\begin{{array}}{{c|c|c}}
r&\lambda_{{\max}}&\deg\Delta_{{\lambda_{{\max}}}}\\ \hline
0&(q-1,q,q+1)&6q(q^2-1)\\
1&(q-1,q,q+2)&6q(q-1)(q+2)\\
2&(q-1,q+1,q+2)&6(q-1)(q+1)(q+2).
\end{{array}}
\]
Thus the largest three-dimensional stratum is never the equal-multiplicity stratum once the distinct triple exists: the symmetry factor in Hilbert's formula pushes the maximum to the nearest possible triple of distinct multiplicities.

For \(d\ge7\), the unique degree-minimizing partition is
\[
\lambda_{{\min}}=(1,1,d-2),\qquad \deg\Delta_{{\lambda_{{\min}}}}=3(d-2).
\]
The small cases are \(d=3\): degree \(1\) at \((1,1,1)\); \(d=4\): degree \(6\) at \((1,1,2)\); \(d=5\): minimum \(9\) at \((1,1,3)\), maximum \(12\) at \((1,2,2)\); and \(d=6\): minimum \(8\) at \((2,2,2)\), maximum \(36\) at \((1,2,3)\).

## Assumptions and scope
The ground field is \(\mathbb C\). A three-part partition means exactly three positive parts, unordered but written increasingly. The locus \(\Delta_\lambda\) is the usual coincident-root locus in projective binary-form space; its dimension is the number of parts, hence three. The statement concerns projective degree, equivalently the number of members of a generic complementary-dimensional linear family having root-multiplicity pattern \(\lambda\), counted with intersection multiplicity.

## Proof
Write \(e_j\) for the number of parts of \(\lambda\) equal to \(j\). Hilbert's formula, as recorded by Fehér--Némethi--Rimányi, is
\[
\deg\Delta_\lambda=\frac{3!}{\prod_j e_j!}\prod_j j^{{e_j}}=\frac{6abc}{\prod_j e_j!}.
\]
Therefore a distinct triple has degree \(6abc\), a triple with exactly two equal parts has degree \(3abc\), and an equal triple has degree \(abc\).

First consider maxima. Any partition with a repeated part has degree at most
\[
3abc\le 3\left(\frac d3\right)^3=\frac{{d^3}}9.
\]
For \(d\ge6\), the displayed candidate distinct triple has degree strictly larger than \(d^3/9\). For \(d=3q\), the difference is \(3q(q^2-2)>0\). For \(d=3q+1\), nine times the difference is \(27q^3+27q^2-117q-1\), which is positive at \(q=2\) and strictly increasing thereafter. For \(d=3q+2\), nine times the difference is \(27q^3+54q^2-90q-116\), again positive at \(q=2\) and strictly increasing thereafter. Hence every maximizer for \(d\ge6\) has three distinct parts.

Now suppose \(a<b<c\). If \(b-a\ge3\), replacing \((a,b,c)\) by \((a+1,b-1,c)\) preserves strict inequalities and changes the product by
\[
c\bigl((a+1)(b-1)-ab\bigr)=c(b-a-1)>0.
\]
If \(c-b\ge3\), replacing \((a,b,c)\) by \((a,b+1,c-1)\) increases the product by \(a(c-b-1)>0\). Finally, if both gaps equal two, replacing \((a,b,c)\) by \((a+1,b,c-1)\) increases the product by \(b(c-a-1)=3b>0\). Thus at a maximum the two positive gaps are each at most two and cannot both be two. Their pattern is therefore uniquely forced by \(d\bmod3\), giving exactly the three triples stated above. Substitution in \(6abc\) gives the maximum-degree formulas.

For minima with \(d\ge7\), the partition \((1,1,d-2)\) has degree \(3(d-2)\). If \(a=a<c\) with \(a\ge2\), then \(3a^2c>3(d-2)\); the case \(a=1\) is exactly \((1,1,d-2)\). If \(a<b=b\), then
\[
ab^2-(a+2b-2)=a(b^2-1)-2b+2\ge(b-1)^2>0,
\]
so its degree is larger than \(3(d-2)\). If the parts are distinct, then for \(a=1\) the product \(bc\) is minimized at \(b=2\), while for \(a\ge2\) one has \(b\ge3\) and \(c\ge d/3\); in either case \(abc\ge2(d-3)\). Hence \(6abc\ge12(d-3)>3(d-2)\). If all three parts are equal, then \(d=3a\) with \(a\ge3\), and \(a^3>9a-6=3(d-2)\). This proves the unique minimum. The four small degrees are checked directly from their three-part partitions.

## Verification
The standalone checker `verify_coincident_extrema.py` enumerates every three-part partition for \(3\le d\le500\), evaluates Hilbert's formula using exact integer arithmetic, and verifies the complete maximizing and minimizing classification, including uniqueness and all small exceptions. It also separately checks the residue-class maximum formulas. This finite replay is regression evidence; the proof above is uniform in \(d\).

## Relationship to prior work
Fehér--Némethi--Rimányi define coincident root loci, record that their dimension is the number of parts, and give Hilbert's general degree formula. They also interpret the degree as the intersection count with a generic complementary-dimensional family. Their work supplies the pointwise degree input, not the fixed-dimension extremal ordering proved here. Brambilla--Staglianò later use the same family of loci in the geometry of real-rank boundaries and recall Hilbert's degree formula, but their statements concern duals, polar degrees, and rank boundaries rather than maximizing or minimizing the ordinary degree over all three-part partitions.

Searches for the equivalent terminology “multiple root locus”, “coincident root stratum”, fixed three-part partitions, and extremal degree did not locate a published statement of this classification. A residual risk remains that the elementary partition optimization may have appeared outside the checked sources.

## Limitations
The theorem is only for coincident root loci of dimension three, i.e. partitions with exactly three parts. In higher dimension, repeated multiplicities can compete more subtly with distinct near-balanced partitions, so the proof does not extend verbatim. No assertion is made about degrees of dual varieties, polar degrees, defining equations, singular-locus degrees, or real-rank boundaries.

## References
L. M. Fehér, A. Némethi, R. Rimányi, “Coincident root loci of binary forms,” arXiv:math/0311312, first public version 18 November 2003; later Michigan Math. J. 54 (2006), 375–392.

M. C. Brambilla, G. Staglianò, “Algebraic boundaries among typical ranks for real binary forms of arbitrary degree,” arXiv:1911.01958, 2019; Found. Comput. Math. 21 (2021), 1003–1022.
