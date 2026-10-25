# Complete vertex spectra and generic face enumerators of cross-polytope hyperplane sections

## Finding
For each integer \(n\ge3\), let \(C_n=\operatorname{conv}\{\pm e_1,\ldots,\pm e_n\}\subset\mathbb R^n\). For any affine hyperplane meeting \(C_n\), including supporting and nongeneric sections, the set of all possible numbers of section vertices is exactly
\[
\mathcal V_n=\{s+r(2n-r-s-1):0\le r,s,\ 1\le r+s\le n\}\;\cup\;\{r(r-1)+2(n-r):1\le r\le n\}.
\]
Every displayed value occurs, and \(\max\mathcal V_n=n(n-1)\). A supporting hyperplane produces at most \(n\) vertices, whereas every hyperplane meeting the interior produces at least \(2n-2\). Thus for \(n\ge4\), none of the integers from \(n+1\) through \(2n-3\) occurs.

If the hyperplane avoids every original vertex, then it intersects the interior. Write \(r\) for the number of original signed vertices in its positive open halfspace after orienting the affine equation so that the offset is nonnegative. Then \(1\le r\le n\), and its *entire* face vector is encoded by
\[
\sum_{k=0}^{n-2} f_k(C_n\cap H)z^{k+2}=(1+2z)^n-(1+z)^r(1+2z)^{n-r}-(1+z)^r+1.
\]
In particular, generic section vertex counts are precisely \(r(2n-r-1)\), for \(1\le r\le n\), and exactly \((n-2)^2\) integers in the closed interval from \(2n-2\) to \(n(n-1)\) are absent from that generic spectrum.

## Assumptions and scope
A hyperplane means a proper affine codimension-one subspace \(H=\{x:\langle a,x\rangle=b\}\) with \(a\ne0\); only nonempty sections are counted. A supporting section need not be full-dimensional in \(H\). For the generic face polynomial, \(H\) must avoid every one of the \(2n\) vertices of \(C_n\). A vertex count is the number of extreme points of the intersection, not the number of crossed edges counted with multiplicity. The coordinate sign symmetries permit taking \(b\ge0\) and \(a_i\ge0\).

## Proof
**1. Counting-section-vertices lemma.** If a hyperplane meets a polytope, every vertex of the section is either a polytope vertex contained in the hyperplane or the unique intersection with the relative interior of an edge whose endpoints lie strictly on opposite sides. Conversely, each such point is a section vertex. Indeed, the smallest face of the polytope containing a point that is extreme in the section must have dimension at most one; an intersection with the relative interior of any face of dimension at least two would contain a nontrivial line segment through the point. Conversely, the hyperplane intersects a straddling edge at a singleton, so the corresponding supporting face restricts to a singleton in the section. Different crossed edges give different vertices because distinct edges have disjoint relative interiors.

**2. Cross-polytope edges.** The edges of \(C_n\) consist of every pair of distinct original vertices except antipodal pairs. A nonempty signed subset of its vertices is a proper simplex face if and only if it contains no antipodal pair.

**3. Positive offset.** Assume \(b>0\). Let \(r\) be the number of coordinates with \(a_i>b\), and \(s\) the number with \(a_i=b\). There are \(r\) original vertices above the hyperplane, \(s\) on it, and \(2n-r-s\) below. Each of the \(r\) upper vertices has one antipode below (never an edge), so the number of strictly crossed edges is \(r(2n-r-s)-r\). Adding the \(s\) vertices already on \(H\) gives
\[
 v(r,s)=s+r(2n-r-s-1).
\]
Nonemptiness requires \(r+s\ge1\), and necessarily \(r+s\le n\). Conversely all these parameter pairs occur with \(b=1\) and coordinate values \(a_i=2\) on \(r\) indices, \(1\) on \(s\), and \(0\) otherwise.

**4. Zero offset.** Suppose \(b=0\) and exactly \(r\) of the \(a_i\) are nonzero. There are \(r\) upper vertices, \(r\) lower vertices, and \(2(n-r)\) on the section. Among the \(r^2\) upper/lower pairs, exactly \(r\) are antipodal nonedges. Therefore
\[
 w(r)=r(r-1)+2(n-r).
\]
All values occur by setting \(a_i=1\) on any \(r\) indices and \(0\) elsewhere. These two cases exhaust every affine hyperplane up to reversing its normal.

**5. Gaps and sharp maximum.** The supporting case has \(r=0\), hence \(v(0,s)=s\le n\). For \(r\ge1\), use \(s\le n-r\) and \(r\ge1\) to obtain
\[
 v(r,s)=r(2n-r-1)-(r-1)s\ge n+(r-1)(n-2)\ge2n-2\quad(r\ge2).
\]
For \(r=1\) the direct identity is \(v(1,s)=2n-2\). The central count is \(w(r)=2n-2+(r-1)(r-2)\ge2n-2\). Moreover \(v(r,s)\le r(2n-r-1)\le n(n-1)\) for \(r\ge1\), and \(w(r)\le n(n-1)\); the upper bound is realized by \(r=n\) (and also \(r=n-1,s=0\)). The asserted forbidden band follows. 

**6. Generic face polynomial.** Suppose \(H\) avoids all vertices. Since each nonempty proper face of \(C_n\) is a simplex with at most one signed vertex from each antipodal pair, each \((j-1)\)-face straddling the hyperplane intersects it in one \((j-2)\)-face; this correspondence is a bijection. For a nonempty section, any such straddling simplex face meets \(H\) in its relative interior, so the intersection has the claimed dimension. Encode a selected vertex by \(z\). All signed simplex faces (and the empty choice) contribute \((1+2z)^n\). Of these, the faces having no positive vertex contribute \((1+z)^r(1+2z)^{n-r}\): on the \(r\) positive-antipodal coordinate pairs, just the negative sign may be chosen. Faces having no negative vertex contribute \((1+z)^r\). Their intersection consists only of the empty choice and contributes one. Inclusion-exclusion gives the stated generating polynomial. For vertex-avoiding sections with \(b>0\), the positive count \(r\) lies in \(1,\ldots,n\); for \(b=0\), absence of section vertices forces all coordinates nonzero and \(r=n\). Choosing \(b=1\) and \(a_i=2\) on exactly \(r\) indices realizes every such generic count. The vertex coefficient is \(r(2n-r-1)\). Its values at \(r=n-1\) and \(r=n\) coincide, and its values for \(r=1,\ldots,n-1\) are strictly increasing. Hence there are \(n-1\) distinct generic counts within \([2n-2,n(n-1)]\), an interval containing \(n(n-1)-(2n-2)+1\) integers; subtraction gives \((n-2)^2\) excluded integers.

## Verification
The bundled `check_cross_sections.py` performs independent exact signed-edge and signed-face enumeration across dimensions two through nine, and separately checks geometric convex-hull vertices for nontrivial representative sections in dimensions three through six. It confirms the displayed formulas and generic face coefficients in its tested range. Execute with `python check_cross_sections.py`; the second test group requires NumPy and SciPy. Finite tests corroborate but do not replace the all-dimensional counting proof above.

## Relationship to prior work
De Loera, Lopez-Campos, and Torres study hyperplane-section vertex-count sequences and their gaps for general polytopes, with explicit emphasis on three-dimensional polytopes and hypercubes; their general section framework supplies motivation. Birkemeyer, Brose, Brandenburg, and Prün develop a broader combinatorial theory of face posets of affine and central slices, including a general face-intersection correspondence. Neither inspected paper explicitly states the above complete dimension-parametrized cross-polytope vertex spectrum or generic face-enumerator formula. The general face-intersection correspondence is an acknowledged ingredient here, rather than a claimed new principle. The conclusion is a specific complete classification for the regular cross-polytope family, not a claim about arbitrary centrally symmetric polytopes.

## Limitations
The generic polynomial requires a hyperplane avoiding all original vertices; it is not asserted for nongeneric sections. The unrestricted vertex-count formula applies even for supporting sections, but it does not classify every face vector of those degenerate sections. The cross-polytope must have its standard antipodal simplex-face structure; arbitrary perturbations do not necessarily share the spectrum. No claim of independent validation or established historical priority is made. A differently indexed equivalent specialization remains possible.

## References
1. Jesús A. De Loera, Gyivan Lopez-Campos, Antonio J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419 (first public 2024-12-17), https://arxiv.org/abs/2412.12419 .
2. Anna Birkemeyer, Anouk E. Brose, Marie-Charlotte Brandenburg, Niklas Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195 (first public 2026-09-14), https://arxiv.org/abs/2609.16195 .
