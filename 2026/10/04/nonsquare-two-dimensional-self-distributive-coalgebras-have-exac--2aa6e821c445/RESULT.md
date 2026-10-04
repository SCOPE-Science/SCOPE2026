# Nonsquare two-dimensional self-distributive coalgebras have exactly five compatible products
## Finding
Let \(k\) be a field of characteristic different from \(2\), let \(a\in k^\times\) be nonsquare, and let \(C_a\) be the counital coalgebra with basis \(x,y\), counit \(\varepsilon(x)=1\), \(\varepsilon(y)=0\), and
\[\Delta x=x\otimes x+a\,y\otimes y,\qquad \Delta y=x\otimes y+y\otimes x.\]
There are exactly five bilinear products \(m:C_a\otimes C_a\to C_a\) that are compatible with \(\Delta\) and satisfy the generalized self-distributive identity \((uv)w=(u w_{(1)})(v w_{(2)})\). They are the zero product and the four tables
\[x^2=x,\ xy=y,\ yx=0,\ y^2=0;\qquad x^2=x,\ xy=0,\ yx=y,\ y^2=0;\]
\[x^2=x,\ xy=0,\ yx=-y,\ y^2=0;\qquad x^2=\tfrac12x,\ xy=yx=\tfrac12y,\ y^2=\tfrac1{2a}x.\]
Exactly three of the five also preserve the counit as a multiplication map. If \(a\) is square instead, the split coalgebra has twenty-one such products, so the raw product count has a sharp square-class jump from \(21\) to \(5\).

## Assumptions and scope
The ground field \(k\) has \(\operatorname{char}k\ne2\), and \(a\in k^\times\) is nonsquare. Compatibility means
\[\Delta(m(u,v))=(m\otimes m)(1\otimes\tau\otimes1)(\Delta u\otimes\Delta v),\]
and self-distributivity means
\[m(m(u,v),w)=m(m(u,w_{(1)}),m(v,w_{(2)})).\]
The phrase “counital” refers to the underlying coalgebra, matching the convention of Bardakov–Kozlovskaya–Talalaev. The final sentence about three products uses the stronger condition \(\varepsilon(m(u,v))=\varepsilon(u)\varepsilon(v)\).

## Proof
Put \(K=k(s)\) with \(s^2=a\). Because \(a\) is nonsquare and \(\operatorname{char}k\ne2\), this is a separable quadratic extension. In \(C_a\otimes_k K\), set
\[g_+=x+s y,\qquad g_-=x-s y.\]
A direct calculation gives \(\Delta g_+=g_+\otimes g_+\) and \(\Delta g_-=g_-\otimes g_-\). Thus the scalar extension is the two-point group-like coalgebra.

For a group-like basis, comultiplication compatibility forces every basis product to lie in \(\{0,g_+,g_-}\), and self-distributivity reduces on basis elements to
\[(uv)w=(uw)(vw).\]
Enumerating the \(3^4\) possible tables gives exactly \(21\) solutions, the same raw list as Carter–Crans–Elhamdadi–Saito, Lemma 3.8. The nontrivial Galois automorphism of \(K/k\) swaps \(g_+\) and \(g_-\). A product descends to \(k\) exactly when its table is fixed by this simultaneous input/output swap. Exactly five of the \(21\) tables are fixed:
\[(0,0,0,0),\ (g_+,0,0,g_-),\ (g_+,g_+,g_-,g_-),\ (g_+,g_-,g_+,g_-),\ (g_-,g_-,g_+,g_+),\]
where entries are ordered by \((g_+g_+,g_+g_-,g_-g_+,g_-g_-)\).

Substituting \(x=(g_++g_-)/2\) and \(y=(g_+-g_-)/(2s)\) converts those five fixed tables into exactly the five products stated above; in the symmetric nonzero table the coefficient \(1/(2s^2)\) becomes \(1/(2a)\). Since scalar extension is faithful, these are all compatible self-distributive products over \(k\).

For the stronger counit condition, both group-like basis vectors have counit \(1\), so a table preserves the counit exactly when none of its four entries is zero. Among the five fixed tables this leaves exactly three. If \(a\) is square, \(g_+\) and \(g_-\) already exist over \(k\), so all \(21\) raw tables occur.

## Verification
`verify.py` exhaustively enumerates all \(81\) group-like tables, checks the self-distributive law, obtains \(21\) solutions, applies the Galois swap and obtains exactly \(5\) fixed tables, of which \(3\) preserve the counit. It symbolically transforms the five fixed tables back to the \(x,y\) basis and independently brute-forces all bilinear maps over \(\mathbb F_3\) for the nonsquare parameter \(a=2\), again finding exactly \(5\). The recorded output ends with `CHECK_OK`.

## Relationship to prior work
Bardakov, Kozlovskaya and Talalaev classify two-dimensional counital self-distributive bialgebras over \(\mathbb C\). Their Section 4.2 gives the split group-like classification up to swapping the two basis vectors, while Section 4.4 writes the nonsplit-looking family
\[\Delta x=x\otimes x+a\,y\otimes y,\qquad \Delta y=x\otimes y+y\otimes x\]
and explicitly labels its displayed multiplication list as partial. Their displayed formulas include terms involving \(\sqrt a\), so they do not by themselves classify the nonsquare case over the ground field. Carter, Crans, Elhamdadi and Saito give the underlying \(21\)-table group-like list and, over \(\mathbb C\), the trigonometric case \(a=-1\). The present claim identifies the exact Galois-fixed sublist and yields a field-theoretic square-class transition. Targeted searches for nonsquare, quadratic-extension, finite-field and trigonometric-coalgebra formulations did not locate a published statement of this five-product descent classification.

## Limitations
The theorem excludes characteristic \(2\), the degenerate parameter \(a=0\), and higher-dimensional coalgebras. The originality comparison is strongest against the two directly relevant full texts; older literature under different terminology could contain an equivalent descent statement. The computational check over \(\mathbb F_3\) is corroborative only; the arbitrary-field result rests on the group-like classification and quadratic Galois descent.

## References
1. V. G. Bardakov, T. A. Kozlovskaya, D. V. Talalaev, “Self-distributive algebras and bialgebras,” arXiv:2501.19152; Theoretical and Mathematical Physics 224 (2025), 1103–1118, DOI: 10.1134/S0040577925070013.
2. J. S. Carter, A. S. Crans, M. Elhamdadi, M. Saito, “Cohomology of Categorical Self-Distributivity,” Journal of Homotopy and Related Structures 3 (2008), 13–63, arXiv:math/0607417.
