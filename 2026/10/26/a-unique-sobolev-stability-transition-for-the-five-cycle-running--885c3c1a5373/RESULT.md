# A unique Sobolev-stability transition for the five-cycle running median

## Finding

On the cyclic five-site sequence space, define the three-point running median by
\[
(Tx)_i=\operatorname{median}(x_{i-1},x_i,x_{i+1}),\qquad i\in\mathbb Z/5\mathbb Z.
\]
For \(g>0\), equip the space with the positive definite discrete Sobolev norm
\[
\|x\|_g^2=\sum_{i=0}^{4}x_i^2+g\sum_{i=0}^{4}(x_{i+1}-x_i)^2.
\]
Let \(L(g)\) be the sharp two-input Lipschitz modulus of \(T\) in this norm. Set
\[
 d(g)=5g^2+5g+1,\qquad R(g)=\frac{10g^2+11g+3}{d(g)}.
\]
Define the cubic
\[
\begin{aligned}
 F(g,z)={}&(25g^4+50g^3+35g^2+10g+1)z^3\\
 &-(125g^4+240g^3+165g^2+48g+5)z^2\\
 &+(160g^4+336g^3+244g^2+74g+8)z\\
 &-(60g^4+140g^3+112g^2+36g+4),
\end{aligned}
\]
and let \(B(g)\) be its largest real zero. Then
\[
 \boxed{L(g)^2=\max\{R(g),B(g)\}.}
\]
More precisely, the polynomial
\[
 H(g)=200g^6+380g^5+259g^4+50g^3-25g^2-14g-2
\]
has exactly one positive zero \(g_*\), approximately \(0.370796344557981\). The first branch strictly dominates for \(0<g<g_*\), the second strictly dominates for \(g>g_*\), and they agree only at \(g_*\). The sharp norm is attained by pairs in a common strict-order chamber for every \(g>0\). The two respective extremizing selection patterns, up to rotations and reflections of the five-cycle, are
\[
 (0,0,3,2,0)\quad\text{and}\quad(0,0,3,4,3),
\]
where a tuple specifies the input coordinate selected for output indices \(0,\ldots,4\). At the transition both types attain the maximum. Finally,
\[
 \lim_{g\downarrow0}L(g)=\sqrt3,
 \qquad \lim_{g\to\infty}L(g)=\sqrt{2+\frac{2\sqrt{10}}5}.
\]

## Assumptions and scope

All inputs and outputs are real five-vectors with periodic indices; the median uses the three distinct nearest-neighbor entries including the center. The same strictly positive parameter \(g\) weights all five undirected cycle edges. The Lipschitz modulus refers to the ratio \(\|T(x)-T(y)\|_g/\|x-y\|_g\) for arbitrary distinct inputs, not the one-input variation of a single filtered signal. The normalized zero-coupling and infinite-coupling statements are limits, not claims of norm equivalence at those endpoints.

## Proof

**Chamber reduction.** For a strict total order of the five coordinates, each local median selects one coordinate, so \(T(x)=P_\sigma x\) for a zero-one matrix having one \(1\) per row. Every such strict chamber is convex. A line segment meets finitely many chamber boundaries; continuity and integration of its piecewise-constant derivative show that the global Lipschitz constant is the maximum of the induced norms of these selection matrices. Conversely, every matrix is realized on a nonempty open order chamber, where a sufficiently small top singular direction gives an actual pair attaining its norm. Writing \(A_g=I+gL_{C_5}\), each squared induced norm is the largest generalized eigenvalue of
\[
 P_\sigma^{\mathsf T}A_gP_\sigma v=\lambda A_gv.
\]

**Finite reduction.** The \(5!=120\) strict orders give precisely \(60\) distinct matrices, forming eight orbits under the dihedral group of the cycle. The canonical selection tuples, with orbit sizes, are

| Canonical tuple | Orbit size |
| --- | ---: |
| `(0,0,1,2,0)` | 10 |
| `(0,0,1,4,0)` | 5 |
| `(0,0,2,2,4)` | 10 |
| `(0,0,2,4,4)` | 5 |
| `(0,0,3,2,0)` | 5 |
| `(0,0,3,2,3)` | 10 |
| `(0,0,3,3,4)` | 5 |
| `(0,0,3,4,3)` | 10 |

The fifth matrix has largest generalized eigenvalue exactly \(R(g)\). The eighth matrix has characteristic determinant \(-z^2F(g,z)\), so its largest generalized eigenvalue is \(B(g)\). The third and fourth matrices have identical characteristic polynomials.

**Exclusion of the remaining six classes.** For each of the first, second, third, and seventh representatives, all five leading principal minors of
\[
 d(g)\bigl(R(g)A_g-P^{\mathsf T}A_gP\bigr)
\]
are nonzero polynomials with nonnegative coefficients. They are strictly positive for \(g>0\), so Sylvester's criterion proves that these four classes have strictly smaller norms than \(R(g)\); equality of the third and fourth characteristic polynomials also excludes the fourth. The included symbolic checker constructs each matrix from the definitions and checks all \(20\) coefficient certificates using exact integer arithmetic, with no numerical sampling of the parameter.

For the sixth representative, the top generalized eigenvalue is
\[
 C(g)=\frac{10g^2+9g+2+\sqrt5\,g(2g+1)}{d(g)}>2.
\]
Direct exact substitution gives
\[
\begin{aligned}
F(g,C(g))=-\frac{2g^3}{d(g)}\bigl[&(50+20\sqrt5)g^3\\
+&(60+24\sqrt5)g^2\\
+&(23+9\sqrt5)g+(3+\sqrt5)\bigr]<0.
\end{aligned}
\]
Since \(F(g,1)=2g^2(3g+1)>0\) and \(F(g,2)=-4g^2(2g+1)(5g+1)<0\), the cubic has one real root below \(1\), one between \(1\) and \(2\), and its largest root above \(2\). Thus \(F(g,C(g))<0\) with \(C(g)>2\) implies \(C(g)<B(g)\). This excludes the sixth representative strictly.

**Unique crossing and limits.** The exact identity
\[
 F(g,R(g))=-\frac{H(g)}{d(g)}
\]
and \(R(g)=2+(g+1)/d(g)>2\) show, by the preceding root ordering, that the sign of \(R(g)-B(g)\) is opposite to the sign of \(H(g)\). The coefficients of \(H\), in descending order, change sign exactly once. Descartes' rule, together with \(H(0)=-2\) and its positive leading coefficient, gives exactly one positive root, counted with multiplicity. It is simple, and the branch crossing is transverse. As \(g\downarrow0\), \(R(g)\to3\) and \(B(g)\to2\). As \(g\to\infty\), the leading cubic factors as \(25(z-1)(z^2-4z+12/5)\), giving the second limit and the claimed strict switching of extremizer families.

## Verification

Run `python checker.py` with SymPy installed. It independently enumerates \(120\) strict input orders, reduces the resulting \(60\) selectors to eight dihedral classes, reconstructs the relevant determinant identities, checks \(20\) exact leading-minor positivity certificates, verifies the algebraic competitor inequality, checks the unique-crossing polynomial, and verifies the large-coupling factorization. Exact symbolic checks, rather than finite parameter samples, verify the parameter-uniform parts of the proof. The final serialized package has been used for the replay.

## Relationship to prior work

Running median filters and their threshold/rank structure are classical. Qiu's functional optimization study establishes a local median cost-minimization property; Arias-Castro and Donoho analyze statistical minimax risks and edge preservation; Pasquini and coauthors derive deterministic restrictions on filtered sequences. Their inspected statements address different invariants from the exact two-input cyclic Sobolev Lipschitz modulus and its parameter-induced extremizer switch. Nearby research on sorting or isotonic projection involves different maps; its conclusions do not algebraically determine this median-filter modulus. No general priority or independence certification is asserted.

## Limitations

The formula is only for five sites, three-point periodic running medians, real signals, and a common positive edge penalty. Sharp formulas for arbitrary cycle length, variable edge weights, or larger median windows are not established. Literature searches cannot eliminate equivalent results in unindexed classical median-filter or nonlinear-operator work; the present scientific assessment is not an independent audit.

## References

1. E. Arias-Castro and D. L. Donoho, *Does median filtering truly preserve edges better than linear filtering?*, arXiv:math/0612422, first posted 2006-12-14; Annals of Statistics 37 (2009), 1172–1206. https://arxiv.org/abs/math/0612422
2. G. Qiu, *Functional Optimization Properties of Median Filtering*, IEEE Signal Processing Letters 1 (1994), 64–65. https://people.cs.nott.ac.uk/pszqiu/webpages/Papers/Functional%20Optimisation%20Properties%20of%20Median%20Filtering.pdf
3. C. Pasquini, G. Boato, N. Alajlan, and F. G. B. De Natale, *A Deterministic Approach to Detect Median Filtering in 1D Data*, IEEE Transactions on Information Forensics and Security (preprint). https://iris.unitn.it/retrieve/handle/11572/161311/110075/median_final.pdf
