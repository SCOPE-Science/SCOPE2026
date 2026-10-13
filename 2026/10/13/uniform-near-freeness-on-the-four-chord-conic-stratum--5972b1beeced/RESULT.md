# Uniform near freeness on the four-chord conic stratum
## Finding
Over \(\mathbb C\), let \(\mathcal A\subset\mathbb P^2\) be a reduced arrangement of one smooth conic and four distinct lines. Assume that every singularity of \(\mathcal A\) is a node or an ordinary triple point and that there are exactly two nodes and four ordinary triple points. Then \(\mathcal A\) is nearly free with exponents \((2,4)\).

In fact, after relabelling the four lines and applying a projective transformation, every such arrangement is
\[
F_\lambda=(xz-y^2)y(x-y)\bigl(x-(1+\lambda)y+\lambda z\bigr)(y-\lambda z)=0,
\qquad \lambda\in\mathbb C\setminus\{0,1\}.
\]
For every admissible parameter,
\[
\operatorname{mdr}(F_\lambda)=2,\qquad \tau(F_\lambda)=18,
\]
so the degree-six nearly-free criterion gives exponents \((2,4)\).

This is a positive-dimensional projective family. The four ordinary triple points lie on the conic, and their unordered cross-ratio is detected by
\[
J(\lambda)=256\frac{(1-\lambda+\lambda^2)^3}{\lambda^2(1-\lambda)^2},
\]
which is nonconstant. Hence infinitely many projectively inequivalent realizations share the same weak combinatorics and are all nearly free.

In the conic-first convention the weak combinatorics are \((k,\ell;n_2,t,n_3)=(1,4;2,0,4)\); in the line-first convention used in the lead source they are \((d,k;n_2,t,n_3)=(4,1;2,0,4)\).

## Assumptions and scope
The ground field is \(\mathbb C\). The conic is smooth, the four lines are distinct, and the arrangement is reduced. The only singularities allowed are ordinary nodes and ordinary triple points; in particular, there are no tangencies, tacnodes, higher-multiplicity points, or nonordinary triple points. The claim is about all realizations with exactly two nodes and four ordinary triple points, not merely about the displayed symmetric example in the literature.

The projective-equivalence statement permits relabelling the line components. The parameter \(\lambda\) is therefore not itself a fine-moduli coordinate: the usual anharmonic transformations of \(\lambda\) can give the same unordered four-point set. The invariant \(J(\lambda)\) is used only to prove that the quotient family is nonconstant and hence positive-dimensional.

## Proof
Write \(C\) for the conic. An ordinary triple point is either the intersection of three lines or the intersection of \(C\) with two lines. Let \(a\) be the number of line-only triple points and \(b\) the number of conic-line-line triple points. Then \(a+b=4\). Let \(c\) be the number of line-line nodes. Counting the six unordered pairs of lines gives
\[
6=3a+b+c=3a+(4-a)+c,
\]
so
\[
c=2-2a.
\]
Thus \(a\in\{0,1\}\). If \(a=1\), three lines are concurrent and \(b=3\). Since \(c=0\), the fourth line meets each of those three lines at one of the three conic-line-line triple points. These three intersections are distinct, because otherwise all four lines would be concurrent and produce a forbidden quadruple point. Hence the fourth line would meet the smooth conic in three distinct points, contradicting Bézout. Therefore \(a=0\), \(b=4\), and \(c=2\).

The two nodes are consequently the intersections of the two pairs of opposite lines, and there are no conic-line nodes. Each of the four lines passes through exactly two of the four triple points on \(C\). Thus the graph whose vertices are the lines and whose edges are the conic-line-line triple points is a simple two-regular graph on four vertices, hence a four-cycle.

Identify the smooth conic with \(\mathbb P^1\). Projective automorphisms of \(\mathbb P^1\) extend through the quadratic Veronese embedding to projective automorphisms of the conic in \(\mathbb P^2\). After relabelling the cycle, send its four vertices to
\[
\infty,\quad 0,\quad 1,\quad \lambda,
\qquad \lambda\ne0,1.
\]
Using the Veronese model \([s:t]\mapsto[s^2:st:t^2]\), the conic is \(xz-y^2=0\), and the four chord lines of the cycle become
\[
y=0,\qquad x-y=0,\qquad x-(1+\lambda)y+\lambda z=0,\qquad y-\lambda z=0.
\]
This proves the normal form.

For this normal form, put \(F=F_\lambda\). The following quadratic triple is a Jacobian syzygy:
\[
\begin{aligned}
A&=-x^2+2(\lambda+1)xy-\lambda xz-2\lambda y^2,\\
B&=xy-\lambda yz,\\
C&=xz+2y^2-2(\lambda+1)yz+\lambda z^2.
\end{aligned}
\]
Exact expansion gives
\[
A F_x+B F_y+C F_z=0,
\]
so \(\operatorname{mdr}(F)\le2\).

To exclude a linear Jacobian syzygy, write a general linear triple with nine scalar coefficients and equate coefficients in \(aF_x+bF_y+cF_z\). The coefficient matrix has a \(9\times9\) minor equal to
\[
108\lambda^2.
\]
Because \(\lambda\ne0\), no nonzero linear syzygy exists. A degree-zero syzygy would yield a degree-one syzygy after multiplication by a coordinate, so
\[
\operatorname{mdr}(F_\lambda)=2.
\]

Each ordinary node has Tjurina number \(1\), and each ordinary triple point has Tjurina number \(4\). Hence
\[
\tau(F_\lambda)=2+4\cdot4=18.
\]
For degree \(m=6\) and \(r=2\), the numerical characterization of near freeness gives
\[
r^2-r(m-1)+(m-1)^2=2^2-2\cdot5+5^2=19=\tau(F_\lambda)+1.
\]
Therefore every member is nearly free. Since the first exponent equals \(\operatorname{mdr}(F_\lambda)=2\) and the exponents of a nearly free degree-six curve sum to \(6\), the exponents are \((2,4)\).

Finally, a projective equivalence between two members preserves the unique degree-two component and hence induces an automorphism of the conic carrying the unordered set of four triple points to the other. The classical unordered cross-ratio invariant is
\[
J(\lambda)=256\frac{(1-\lambda+\lambda^2)^3}{\lambda^2(1-\lambda)^2}.
\]
It is nonconstant, so the projective-equivalence quotient is positive-dimensional.

## Verification
The accompanying `artifacts/verify.py` uses exact symbolic arithmetic. It reconstructs \(F_\lambda\), verifies the displayed quadratic Jacobian syzygy, computes the stated \(9\times9\) linear-syzygy minor as \(108\lambda^2\), checks the four conic-line-line triple points and the two opposite-line nodes, verifies the chord intersections with the conic, and checks the degree-six nearly-free numerical identity. Running it prints `VERIFY_OK`.

The incidence reduction from arbitrary realizations to the four-cycle normal form is a proof by pair counting and Bézout, not an experimental enumeration. The verifier therefore supplements, rather than replaces, that argument.

## Relationship to prior work
Gałecka studies nearly free conic-line arrangements with nodes, tacnodes, and ordinary triple points and explicitly asks for a classification of weak combinatorics admitting nearly free realizations. Her degree-six example is the symmetric arrangement
\[
(x^2+y^2-16z^2)(y-x+4z)(y+x-4z)(y-x-4z)(y+x+4z)=0,
\]
with two nodes, four ordinary triple points, total Tjurina number \(18\), and minimal Jacobian-relation degree \(2\). The source proves that this particular arrangement is nearly free. It does not state that every realization of the same weak combinatorics is nearly free, nor does it give the one-parameter normal form or its cross-ratio moduli.

Dimca and Pokora give the complete classification of *free* conic-line arrangements with these singularity types and prove the corresponding numerical Terao statement for freeness. Their result is relevant because it shows how strongly weak combinatorics can control freeness in this class, but it does not imply the uniform near-freeness statement above.

A 2026 preprint by Bromboszcz records a database of selected conic-line arrangements of degree at most six. Its appendix includes a nearly free representative with weak combinatorics \((1,4;2,0,4)\) and syzygy degrees beginning \(2,4,4\). The paper explicitly describes the appendix as a database of selected arrangements used as a finite source of examples and studies Ziegler pairs within that database. It does not assert that all realizations of \((1,4;2,0,4)\) are nearly free or identify the positive-dimensional projective family. Thus that later table corroborates another representative but does not cover the uniform theorem.

Targeted statement-level searches for the weak-combinatorics vector, the four-chord normal form, cross-ratio formulations, and the assertion that every such realization is nearly free found no covering result. The closest indexed result concerns a different degree-eight nearly free conic-line arrangement and does not imply this degree-six classification.

## Limitations
The theorem is restricted to one smooth conic and four lines with exactly the stated simple singularities. It does not classify other degree-six weak-combinatorics cells, arrangements with tacnodes, or arrangements containing more than one conic. The parameter \(\lambda\) is redundant under the finite anharmonic action, so it is not claimed to be a fine-moduli coordinate.

The originality assessment is based on the lead source, the complete free-classification source, the 2026 low-degree database preprint, targeted database searches, and the available prior ledger claims. An unindexed or differently phrased source could still contain an equivalent uniform statement.

## References
1. A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969v1, first public 29 April 2022.
2. A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2111.12349v1; *Journal of Algebraic Combinatorics* 56 (2022), 403–424.
3. A. Bromboszcz, *On homological properties of conic-line arrangements with simple singularities*, arXiv:2606.31452v1, first public 30 June 2026.
