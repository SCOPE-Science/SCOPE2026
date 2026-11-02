# The characteristic-five Maschke quartic: sixteen rational nodes and a maximal quadratic-extension K3 resolution

## Finding

Let \(X\subset\mathbb P^3_{\mathbb F_5}\) be the reduction of the classical Maschke form
\[
F(x_0,x_1,x_2,x_3)=\sum_{i=0}^{3}x_i^4-6\sum_{0\le i<j\le3}x_i^2x_j^2.
\]
Thus in characteristic five the coefficient \(-6\) is \(-1\). Then \(X\) is an irreducible normal quartic surface whose geometric singular locus consists of exactly sixteen ordinary double points, all rational over \(\mathbb F_5\): for each choice of one zero coordinate, the three remaining coordinates are independently \(\pm1\), modulo simultaneous sign. Its minimal resolution \(\pi:Y\to X\) is a K3 surface. For every integer \(m\ge1\), putting \(q=5^m\),
\[
\#X(\mathbb F_q)=q^2+1+2q+4(-5)^m
=\begin{cases}(q-1)^2,&m\text{ odd},\\q^2+6q+1,&m\text{ even},\end{cases}
\]
and
\[
\#Y(\mathbb F_q)=q^2+1+18q+4(-5)^m.
\]
In particular \(\#X(\mathbb F_5)=16\), \(\#X(\mathbb F_{25})=776\), \(\#Y(\mathbb F_5)=96\), and \(\#Y(\mathbb F_{25})=1176=25^2+22\cdot25+1\): the resolution attains the upper Weil bound for K3 surfaces over \(\mathbb F_{25}\). The geometric Frobenius eigenvalues on \(H^2_{\acute et}(Y_{\overline{\mathbb F}_5},\mathbb Q_\ell)\), for every \(\ell\ne5\), are \(+5\) with multiplicity eighteen and \(-5\) with multiplicity four. The zeta functions are
\[
Z(Y/\mathbb F_5,T)=\frac1{(1-T)(1-25T)(1-5T)^{18}(1+5T)^4}
\]
and
\[
Z(X/\mathbb F_5,T)=\frac1{(1-T)(1-25T)(1-5T)^2(1+5T)^4}.
\]

## Assumptions and scope

The base is exactly \(\mathbb F_5\); geometric assertions are over its algebraic closure, and point-count formulas hold over every finite extension. The object \(X\) is the specified integral Maschke equation reduced modulo five, not an arbitrary model of a complex quartic. The exceptional divisors of the minimal resolution are geometrically sixteen disjoint rational \((-2)\)-curves. No assertion about a characteristic-zero model's good reduction is needed.

## Proof

**Singular points.** Set \(S=\sum_i x_i^2\). Reduction modulo five yields
\[
F=\sum_i x_i^4-\sum_{i<j}x_i^2x_j^2,
\qquad\frac{\partial F}{\partial x_i}=x_i(x_i^2-2S).
\]
Suppose all partials vanish at a projective geometric point. If \(S=0\), every coordinate is zero, impossible. Otherwise every nonzero coordinate has square \(2S\). If exactly \(r\) coordinates are nonzero, then \(S=2rS\), so \(2r=1\) in \(\mathbb F_5\); because \(1\le r\le4\), necessarily \(r=3\). Scaling by a square root of \(2S\), the point has one zero coordinate and three \(\pm1\) coordinates. Conversely each of the resulting \(4\cdot2^3/2=16\) distinct projective points satisfies \(F=0\) and its partials vanish. Every such point is \(\mathbb F_5\)-rational.

**Ordinary nodes and the resolution.** Coordinate permutations and sign changes act transitively on these singular points. In the affine chart \(x_0=1\), at \([1:1:1:0]\) the Hessian in local variables \((x_1,x_2,x_3)\), reduced modulo five, is
\[
H=\begin{pmatrix}3&1&0\\1&3&0\\0&0&4\end{pmatrix},\qquad\det(H)=2\ne0.
\]
Because the characteristic is odd, the local quadratic tangent cone is nondegenerate: every singularity is an \(A_1\) point. A reducible projective quartic in \(\mathbb P^3\) would have a positive-dimensional intersection of its components, hence a nonisolated singular locus, so \(X\) is irreducible. As a hypersurface with isolated singularities, \(X\) is normal by Serre's criterion. The minimal resolution \(Y\) of a normal quartic with only rational double points has trivial canonical bundle and \(H^1(Y,\mathcal O_Y)=0\); thus it is a K3 surface. Each exceptional curve is a smooth conic defined over \(\mathbb F_5\) (its quadratic tangent cone), and every smooth conic over a finite field has a rational point, hence has \(q+1\) points over \(\mathbb F_q\). Since the contracted node contributes one point, each exceptional curve changes the count by \(q\):
\[
\#Y(\mathbb F_q)=\#X(\mathbb F_q)+16q.
\]

**Two exact field counts.** The accompanying `verify.py` implements exhaustive enumeration in the disjoint normalized affine charts
\[
[a:b:c:1],\quad[a:b:1:0],\quad[a:1:0:0],\quad[1:0:0:0].
\]
It checks \(F\) both from the displayed quartic and from the independent polynomial identity \(F=4\sum_i x_i^4+2S^2\) modulo five. For \(\mathbb F_5\), the chart counts are \((12,4,0,0)\); for \(\mathbb F_{25}=\mathbb F_5[\theta]/(\theta^2-3)\), they are \((728,44,4,0)\). Thus the exact totals are \(16\) and \(776\), giving \(\#Y(\mathbb F_5)=96\) and \(\#Y(\mathbb F_{25})=1176\). These are complete finite enumerations (respectively \(156\) and \(16276\) normalized projective points), not statistical tests.

**All extensions and zeta functions.** For a smooth projective K3 surface over \(\mathbb F_5\), \(H^1\) and \(H^3\) vanish, while \(H^2\) has dimension \(22\), and all geometric Frobenius eigenvalues \(\alpha_j\) have complex absolute value \(5\). The Lefschetz trace formula gives
\[
\sum_j\alpha_j=96-1-25=70,
\qquad
\sum_j\alpha_j^2=1176-1-625=550=22\cdot25.
\]
Every \(\alpha_j^2\) has absolute value \(25\), so equality in the triangle inequality forces \(\alpha_j^2=25\) for every \(j\). Hence each \(\alpha_j\in\{+5,-5\}\). From their sum, the multiplicities are respectively eighteen and four. The Lefschetz formula now gives the asserted \(\#Y(\mathbb F_{5^m})\) for every \(m\), and removing the sixteen exceptional \(\mathbb P^1\) contributions gives \(\#X(\mathbb F_{5^m})\). Exponentiating the point-count series yields both displayed zeta functions. No finite-range extrapolation is used in this last step.

## Verification

Execute `python verify.py` using Python's standard library. The verifier enumerates the normalized projective charts over \(\mathbb F_5\) and the quadratic extension defined by \(\theta^2=3\), confirms equality of two polynomial expressions at every point, checks all sixteen singular points and the Hessian determinant, and tests the arithmetic identities. Expected terminal line: `VERIFY_OK`. The infinite-geometric singular-locus argument and the cohomological eigenvalue argument are proved above rather than delegated to the script.

## Relationship to prior work

Edge's 1945 work supplies the original characteristic-zero Maschke quartic form. Edge's 1949 work studies a larger family of Maschke quartics and the general Kummer locus; its published mathematical review gives the Segre-cubic parameter criterion. Hence the presence of a Kummer degeneration should **not** be claimed as a newly discovered general phenomenon. Dolgachev--Lehavi (first posted 7 October 2007) supply background on sixteen-node Kummer quartics and their resolution. The additional arithmetic statement here is the explicit complete \(\mathbb F_5\)-Frobenius spectrum, maximum point count after the quadratic extension, and closed counts/zeta functions for the specified integral reduction; these do not follow merely from a geometric Kummer-locus criterion. No checked material gives these characteristic-five arithmetic statements.

## Limitations

The 1949 Edge original was not available for full-text inspection; its detailed contemporary mathematical review was read. Consequently an unpublished or unindexed exact characteristic-five computation could precede the arithmetic result. The theorem does not classify every integral model of a Maschke surface, nor the polarization or Artin invariant of the K3 resolution. The algebraic spectral argument uses standard Weil purity and the K3 cohomology dimensions, not an independent formal proof assistant. The exact arXiv date in the metadata is a verified public date for the modern background source; the substantially older Edge publications have no independently verified precise publication day in the accessed record.

## References

1. W. L. Edge, *The geometrical construction of Maschke's quartic surfaces*, Proc. Edinburgh Math. Soc. 7(2) (April 1945), 93--103, DOI 10.1017/S0013091500024378, original paper, https://webhomes.maths.ed.ac.uk/cheltsov/edge2021/pdf/1945a.pdf .
2. W. L. Edge, *The Kummer quartic and the tetrahedroids based on the Maschke forms*, Proc. Cambridge Philos. Soc. 45 (1949), 519--535, DOI 10.1017/S0305004100025226 (original not inspected; scientific summary reviewed via the contemporary Math Reviews review MR0033562 at https://webhomes.maths.ed.ac.uk/cheltsov/edge2016/pdf/msn.pdf , page 39 of the digital scan).
3. I. Dolgachev and D. Lehavi, *On isogenous principally polarized abelian surfaces*, arXiv:0710.1298 (first public version 2007-10-07), https://arxiv.org/html/0710.1298v3 .
