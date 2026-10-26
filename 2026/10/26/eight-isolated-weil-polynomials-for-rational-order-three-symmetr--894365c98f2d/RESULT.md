# Eight isolated Weil polynomials for rational order-three symmetry on genus-two curves over \(\mathbf F_3\)

## Finding

Let \(C\) range over geometrically smooth, projective, genus-two curves defined over \(\mathbf F_3\), up to \(\mathbf F_3\)-isomorphism. Write its degree-four Weil polynomial as
\[
W_C(s)=s^4+A_1s^3+A_2s^2+3A_1s+9.
\]
The following conditions are equivalent:

1. The curve admits an \(\mathbf F_3\)-defined automorphism of exact order \(3\).
2. Its Weil coefficient pair \((A_1,A_2)\) is one of
\[
\{(-4,10),(-2,7),(-2,1),(-1,-2),(1,-2),(2,1),(2,7),(4,10)\}.
\]

**Moreover, each of these eight Weil polynomials occurs for exactly one \(\mathbf F_3\)-isomorphism class among *all* genus-two curves over \(\mathbf F_3\).** Thus the Jacobian's unpolarized isogeny class detects this particular rational wild symmetry and determines the curve uniquely on the locus in question. The assertion concerns arithmetic isomorphism and arithmetic order-three automorphisms, not geometric automorphisms after field extension.

Explicit representatives are \(C_{c,a,b}: y^2=c((x^3-x)^2+a(x^3-x)+b)\), with data:

| \((c,a,b)\) | \(\#C(\mathbf F_3)\) | \(\#C(\mathbf F_9)\) | \((A_1,A_2)\) | Frobenius branch partition |
|---|---:|---:|---:|---|
| \((1,0,1)\) | 8 | 14 | \((4,10)\) | \((2,2,2)\) |
| \((1,0,2)\) | 2 | 20 | \((-2,7)\) | \((3,3)\) |
| \((1,1,0)\) | 5 | 5 | \((1,-2)\) | \((1,1,1,3)\) |
| \((1,1,2)\) | 2 | 8 | \((-2,1)\) | \((6)\) |
| \((2,0,1)\) | 0 | 14 | \((-4,10)\) | \((2,2,2)\) |
| \((2,0,2)\) | 6 | 20 | \((2,7)\) | \((3,3)\) |
| \((2,1,0)\) | 3 | 5 | \((-1,-2)\) | \((1,1,1,3)\) |
| \((2,1,2)\) | 6 | 8 | \((2,1)\) | \((6)\) |

All eight curves are ordinary. The separate assertions that there are \(69\) arithmetic genus-two classes in total, \(1296\) squarefree sextic equations, or eight classes with this symmetry are not offered as individually novel: the first two are established arithmetic counts, and a pre-existing full sextic-orbit table already implies the third by filtering stabilizer orders. The differentiated claim is the **isogeny-class detection and uniqueness** statement above, including its complete eight-polynomial list.

## Assumptions and scope

The field is exactly \(k=\mathbf F_3\). Each genus-two curve has its canonical hyperelliptic double cover \(C\to\mathbf P^1\). Its reduced six-point geometric branch divisor is defined over \(k\). A binary sextic \(F(X,Z)=\sum_{i=0}^6 f_i X^i Z^{6-i}\) represents a smooth genus-two curve precisely when it has six distinct geometric roots in \(\mathbf P^1\). In particular, a degree-five dehomogenization is allowed and has one simple branch point at infinity. Two such models are \(k\)-isomorphic if related by a rational change of hyperelliptic coordinate and a rational square rescaling of the right side. Because \((\mathbf F_3^*)^2=\{1\}\), the effective action on nonzero binary sextics is that of \(\operatorname{PGL}_2(\mathbf F_3)\), of order \(24\).

The coefficient \(A_1=\#C(\mathbf F_3)-4\); the second coefficient follows from
\[
A_2=\frac{\#C(\mathbf F_9)-10+A_1^2}{2}.
\]
These two coefficients determine the entire Weil polynomial in genus two. Over finite fields equality of the Weil polynomial is equivalent to isogeny of the Jacobians as abelian varieties, not necessarily as principally polarized abelian varieties.

## Proof

**Structural reduction.** An automorphism of exact order \(3\) descends nontrivially to a rational projective automorphism of the hyperelliptic base, as the kernel of the descent map is the order-two hyperelliptic involution. Every order-three element of \(\operatorname{PGL}_2(\mathbf F_3)\) is rationally conjugate to \(x\mapsto x+1\). Its sole geometric fixed point is infinity. Since the branch divisor has degree six and is invariant, its multiplicity at infinity is congruent to six modulo three; being reduced, that multiplicity must be zero. Thus the branch polynomial has degree exactly six. Its transform under translation is a scalar multiple of itself. Applying translation three times forces that scalar to equal one. The invariant ring is \(\mathbf F_3[x^3-x]\), so after normalizing the leading invariant polynomial coefficient, every such curve admits a model
\[
y^2=c\big(t^2+at+b\big),\qquad t=x^3-x,
\]
with \(c\in\{1,2\}\), \(a,b\in\mathbf F_3\), and \(a^2-b\ne0\). Indeed \(dt/dx=-1\), and the condition \(a^2-b\ne0\) is exactly separability of the quadratic in \(t\) and hence geometric squarefreeness of its six-point pullback. Conversely each model admits the order-three automorphism \((x,y)\mapsto(x+1,y)\). Replacing \(x\) by \(-x\) identifies the models with parameters \(a\) and \(-a\). This leaves the eight displayed model types.

**Weil coefficients for the eight types.** At each rational affine \(x\), \(t=x^3-x=0\). Above rational infinity there are two points if \(c=1\) and none if \(c=2\). For quadratic extension counts, take \(\mathbf F_9=\mathbf F_3[u]/(u^2+1)\). The map \(x\mapsto x^3-x\) takes every value in \(\{0,u,-u\}\) precisely three times, and each nonzero element of \(\mathbf F_3\) is a square in \(\mathbf F_9\); there are two points at infinity in each case. Evaluating \(c(t^2+at+b)\) at these three values gives the two point-count columns above and therefore the eight distinct coefficient pairs. The ordinary property is confirmed directly by the invertible Cartier–Manin matrix \(c\begin{pmatrix}1&-a\\0&1\end{pmatrix}\). The four stated Frobenius partitions follow by factoring \(t^2+at+b\) and studying the Artin–Schreier fibers \(x^3-x=r\).

**Isolation among all genus-two curves.** This last step uses a complete, finite and reproducible enumeration, not a bounded extension-field heuristic. Enumerate the \(3^7-1=2186\) nonzero binary sextics over \(\mathbf F_3\). Exactly \(1296\) are geometrically squarefree, checking a degree-six dehomogenization by derivative gcd, a degree-five one similarly with its simple infinity, and excluding lower degrees with repeated infinity. The \(24\) exact projective substitutions partition these into \(69\) orbits, each a distinct arithmetic isomorphism class. For each representative, count points over \(\mathbf F_3\) and all nine elements of \(\mathbf F_9\), with the appropriate infinity count. This yields exactly \(50\) different coefficient pairs \((A_1,A_2)\). The fiber over **each** of the eight pairs above has size one; the other \(61\) arithmetic classes have none of those eight pairs. The complete loop, all field operations, and all assertions are contained in `artifacts/verify.py`. It also independently confirms exactly \(42\) smooth sextic equations fixed by at least one projective order-three element, forming orbit sizes \(1,1,4,4,8,8,8,8\). This establishes both directions of the Weil-polynomial criterion and the uniqueness assertion.

## Verification

Run `python3 artifacts/verify.py` in a standard Python 3 interpreter. It requires no additional modules. Its complete deterministic stdout must match `artifacts/expected.txt`. The code checks all \(2186\) nonzero binary sextics, including degree-five models, all \(24\) projective substitutions, exact field arithmetic in \(\mathbf F_9\), the \(69\) projective orbits, the \(50\) Weil types and singleton occurrence of all eight specified pairs. It separately verifies the invariant-sextic and rational order-three stabilizer descriptions. Direct outputs and assertions, not external log paths, are the certificates.

## Relationship to prior work

Zobernig's 2021 paper (arXiv:2111.07270v1) studies genus-two curves in small characteristic, especially \(3\)-rank strata and their sizes. Howe–Nart–Ritzenthaler's 2006 preprint (arXiv:math/0607515) characterizes **which** Weil polynomials occur for genus-two curves over finite fields, not the multiplicity of arithmetic curve classes in a given Weil-isogeny class. A separate pre-existing complete enumeration of the \(69\) genus-two classes over \(\mathbf F_3\), with projective stabilizer sizes, already makes the **eight-class symmetry count** a direct consequence and also records branch partitions, \(3\)-rank and rational-point strata. Those counts and tables are prior coverage, not the asserted contribution. The present exact eight-isogeny-type rigidity and the test for a rational order-three symmetry do not follow from the earlier tabulated fields, which omit quadratic-extension point counts or Weil-polynomial multiplicities.

## Limitations

The theorem is restricted to \(\mathbf F_3\); it makes no claim for other finite fields, geometric automorphisms not defined over the ground field, or uniqueness among all polarized abelian surfaces of the indicated isogeny type. The exhaustive calculation is a finite proof only because the entire coefficient space is explicitly exhausted. The cited literature comparisons do not rule out unindexed prior computations or a table that already records precisely these eight singleton Weil types. Independent human audit has not been performed.

## References

1. Lukas Zobernig, *Genus 2 Curves in Small Characteristic*, arXiv:2111.07270v1 (public 2021-11-14), https://arxiv.org/abs/2111.07270 .
2. Everett W. Howe, Enric Nart, Christophe Ritzenthaler, *Jacobians in Isogeny Classes of Abelian Surfaces over Finite Fields*, arXiv:math/0607515 (2006), https://arxiv.org/abs/math/0607515 .
3. Gabriel Cardona, Jordi Quer, *Curves of Genus 2 with Group of Automorphisms Isomorphic to \(D_8\) or \(D_{12}\)*, arXiv:math/0203165 (2002), https://arxiv.org/abs/math/0203165 .
