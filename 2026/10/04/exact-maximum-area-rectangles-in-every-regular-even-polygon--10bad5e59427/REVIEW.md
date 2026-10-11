# Independent mathematical audit

## correctness

PASS

The centralization lemma is valid for every rectangle in a centrally symmetric convex body: each centered vertex \(\pm u\pm v\) is the midpoint of an original vertex and the centrally reflected opposite original vertex, so convexity preserves containment and area. For a centered rectangle the half-diagonals have common length \(r\) and area \(2r^2\sin\delta\). In a regular n-gon the radial reach at angular offset \(s\) from a vertex ray is \(\cos\alpha/\cos(\alpha-s)\), \(\alpha=\pi/n\). When \(4\mid n\), \(r\le R\) and \(\sin\delta\le1\) are simultaneously sharp at orthogonal vertex rays. When \(n\equiv2\pmod4\), the largest acute separation of vertex lines is \(\delta_0=\pi/2-\alpha\). For \(\delta=\delta_0+t\), nearest-vertex offsets satisfy \(s_1+s_2\ge t\), so the common radius is at most \(R\cos\alpha/\cos(\alpha-t/2)\); the identity \(\cos^2(\alpha-t/2)-\cos\alpha\cos(\alpha-t)=(1-\cos t)/2\) proves strict loss for every \(t>0\). This reconstructs both formula branches and the centered equality cases.

## originality

PASS

The closest primary literature solves maximum-area rectangles in arbitrary convex or simple polygons algorithmically, including exact cubic-time convex-polygon algorithms. Direct inspection of the most relevant full text found no regular-polygon specialization, modulo-four formula, or equality classification. Fresh exact-expression and regular-polygon searches likewise did not locate a prior all-even-n theorem. The audited result uses symmetry to replace general continuous optimization by a closed formula and equality geometry.

## value

PASS

Regular polygons are a canonical test family for the established maximum-rectangle problem. The theorem completely resolves every even order, explains the modulo-four phase change, and classifies the centered equality geometry. This is a natural infinite-family classification rather than a small numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
