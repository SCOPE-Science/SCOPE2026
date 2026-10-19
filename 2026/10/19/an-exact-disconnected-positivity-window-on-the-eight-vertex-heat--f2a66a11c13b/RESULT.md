# An exact disconnected positivity window on the eight-vertex heat path

## Finding

Let \(P_n\) be the unweighted path on \(n\ge1\) vertices, let \(L_n\) be its combinatorial graph Laplacian (unit rate across each edge), and put
\[
\mathcal T_n(h)=
(12I-6hL_n+h^2L_n^2)(12I+6hL_n+h^2L_n^2)^{-1},\qquad h\ge0.
\]
This is the completed two-stage, fourth-order Gauss–Legendre Runge–Kutta step for \(u'=-L_nu\), equivalently the diagonal \([2/2]\) Padé approximation to \(e^{-hL_n}\).

**Theorem (small-step path barrier and first sharp reentry).** Every \(P_n\) with \(1\le n\le7\) has some \(\varepsilon_n>0\) such that \(\mathcal T_n(h)\) is entrywise nonnegative whenever \(0\le h\le\varepsilon_n\). For every \(n\ge8\), \(\mathcal T_n(h)\) has a strictly negative entry for every sufficiently small \(h>0\).

For the first obstructed path, \(n=8\), the **complete** positivity set is exactly
\[
\boxed{\{h\ge0:\mathcal T_8(h)\ge0\text{ entrywise}\}=\{0\}\cup[\alpha,\beta]},
\]
where \(\alpha\) is the unique positive zero of
\[
F(h)=7h^6+126h^5+660h^4+1320h^3+936h^2-144,
\]
and \(\beta\) is the unique positive zero of
\[
\begin{aligned}
G(h)={}&h^{12}+58h^{11}+1172h^{10}+7944h^9+16584h^8\\
&-64224h^7-525456h^6-1665792h^5-3124224h^4\\
&-3732480h^3-2820096h^2-1244160h-248832.
\end{aligned}
\]
In particular, \(3/10<\alpha<1/3\), \(4<\beta<9/2\), and numerically \(\alpha\approx0.317755145825641\), \(\beta\approx4.286367710313382\). For \(0<h<\alpha\) entry \((0,7)\) is negative; for \(h>\beta\) entry \((3,4)\) is negative, with zero-based indexing. At either positive endpoint only the indicated symmetric pair vanishes; all other entries are strictly positive.

## Assumptions and scope

All edge rates are exactly one. At an endpoint the diagonal Laplacian entry is one; at an interior path vertex it is two. Each off-diagonal edge entry is minus one. Thus \(-L_n\) is a conservative symmetric continuous-time Markov generator and \(e^{-hL_n}\) is nonnegative for all \(h\ge0\). Positivity refers only to the **completed rational step**, not internal Runge–Kutta stages. Matrix calculations and polynomial sign assertions use exact rational arithmetic; the decimal root values are informative only.

## Proof

**1. The sharp small-step obstruction for all paths.** For
\[
r(z)=\frac{12+6z+z^2}{12-6z+z^2},
\]
the Maclaurin expansion begins
\[
r(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}
+\frac{z^5}{144}+0z^6-\frac{z^7}{1728}+O(z^8).
\]
Put \(Q_n=-L_n\). If two vertices are a graph distance \(d\) apart, then \((Q_n^j)_{uv}=0\) for \(j<d\) and \((Q_n^d)_{uv}=1\): there is a unique shortest path and no diagonal stay is possible in \(d\) moves. For distances \(1\le d\le5\), the leading off-diagonal term of \(r(hQ_n)\) is positive. For distance \(d=6\), the order-six coefficient vanishes, and
\[
(Q_n^7)_{uv}=-\sum_{v\text{ on the unique six-edge path from }u\text{ to }v}\deg(v)<0.
\]
Indeed a seven-factor product connecting vertices at distance six must traverse all six edges and insert exactly one negative diagonal factor; an all-edge seven-step walk has the wrong parity. Since the order-seven Padé coefficient is negative, the first nonzero contribution at distance six is positive. Every diagonal entry equals \(1+O(h)\). Thus for each fixed \(n\le7\), all matrix entries are nonnegative on a sufficiently small common right-hand interval. For \(n\ge8\), choose vertices at distance seven. Their entry satisfies
\[
[\mathcal T_n(h)]_{uv}=-h^7/1728+O_n(h^8)<0
\]
for all sufficiently small positive \(h\), proving the infinite-family assertion.

**2. Exact eight-vertex rational reduction.** For \(L=L_8\), write
\[
Q(h)=12I+6hL+h^2L^2,\quad M(h)=12I-6hL+h^2L^2.
\]
The matrix \(Q(h)\) is positive definite for \(h\ge0\), since every Laplacian eigenvalue is nonnegative. Define the explicitly positive polynomial
\[
\begin{aligned}
D(h)={}&(h^2+3h+3)(h^4+12h^3+54h^2+72h+36)\\
&\cdot(h^8+48h^7+888h^6+5760h^5+18936h^4\\
&\hspace{3em}+34560h^3+36288h^2+20736h+5184).
\end{aligned}
\]
There is an integer-coefficient polynomial matrix \(P(h)\), with each entry of degree at most fourteen, satisfying the **full matrix identity**
\[
Q(h)P(h)=4D(h)M(h).
\]
The standalone `verify.py` reconstructs every coefficient of \(P\) by exact rational interpolation, checks all 64 polynomial identities coefficient-by-coefficient, and proves the coefficient-sign facts used below. In particular,
\[
P_{0,7}(h)=9h^7F(h),\qquad P_{3,4}(h)=-9hG(h).
\]
Since \(Q\) is invertible and \(D(h)>0\), these identities yield \(\mathcal T_8(h)=P(h)/(4D(h))\). They are checkable finite polynomial identities, not numerical sampling statements.

**3. Exact global sign certificate.** Both \(F\) and \(G\), written in ascending powers of \(h\), have exactly one coefficient-sign change. Their constant terms are negative and leading coefficients positive. By Descartes' rule and continuity, each has exactly one positive zero. Direct exact rational substitutions show
\[
F(3/10)<0<F(1/3),\qquad G(4)<0<G(9/2).
\]
Thus the two controlling entries have the signs specified in the theorem.

To check no other entry imposes a tighter restriction, divide each remaining nonzero numerator \(P_{ij}(h)\) by its maximal initial power \(h^{k_{ij}}\). The exhaustive coefficient certificate yields the following **64-entry partition**, taking symmetric entries separately: four entries are the two controlling symmetric pairs; of the other sixty entries, forty have only nonnegative coefficients and positive constant term after division, whereas twenty have positive constant term, negative leading coefficient, **exactly one** sign variation from positive low-degree coefficients to negative high-degree coefficients, and a strictly positive value at \(h=9/2\). For a polynomial in the last group, Descartes' rule gives at most one positive zero. Since the value is positive both immediately to the right of zero and at \(9/2\), any such zero lies strictly beyond \(9/2\). Consequently, every other entry is positive throughout \(0<h\le9/2\).

It follows that the entire eight-vertex matrix is nonnegative exactly for \(\alpha\le h\le\beta\) among positive \(h\). At \(h=0\) it is \(I\). Below \(\alpha\), the endpoint-to-endpoint entry is negative; above \(\beta\), the middle-edge entry is negative. This proves the claimed if-and-only-if, including endpoints and all positive times outside the window.

## Verification

Run `python3 verify.py` using the Python standard library (no external packages). The script rebuilds the eight-vertex path Laplacian, evaluates the rational step at fifteen integer arguments in exact fractions, interpolates each degree-at-most-fourteen numerator, verifies all 64 polynomial matrix identities, checks the two displayed exceptional numerator factorizations, and verifies all coefficient patterns and rational root brackets. It also independently verifies
\[
[\mathcal T_8(1/4)]_{0,7}=-\frac{2291913}{780953605188301},\quad
[\mathcal T_8(1)]_{0,7}=\frac{747}{17136140},
\]
and
\[
[\mathcal T_8(5)]_{3,4}=-\frac{701357055435}{35412335776468}.
\]
The exact interpolation is not relied upon alone: the polynomial identity \(QP=4DM\), whose two sides have explicitly bounded degrees, is verified coefficient-by-coefficient. The completed proof for arbitrary \(n\) is analytic and is not inferred from finite sample sizes.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten (2012) demonstrate arbitrarily-small-step positivity loss for the same Padé rational map using an eight-state nilpotent one-way shift and a related Hurwitz Metzler system. That directed, nonconservative example does not determine the signs for the symmetric conservative path generator. Lóczi and Ketcheson (2014, Section 2.2.1) establish the zero radius of absolute monotonicity for the fourth-order \([2/2]\) rational class. That general uniform obstruction does not imply the unit-path family threshold or the exact positivity window for \(P_8\).

A public 2026 study, “Eight-state barrier for Markov positivity of the [2/2] Padé map,” proves a sharp dimension-eight obstruction for conservative Markov generators and determines an intermediate positivity interval for an **absorbing directed pure-birth chain**, with a different sixth-degree lower polynomial and upper bound \(2\sqrt3\). That result supplies important overlapping qualitative context, but does not give the reflecting, reversible unit-path family statement or the distinct exact interval proved here. Jin, Lazarov, Thomée and Zhou (2015) show that positivity can reappear above a threshold in different finite-element subdiffusion discretizations, not in this Gauss–Legendre path problem.

## Limitations

The result is an exact mathematical statement for unit-rate, symmetric path generators and the completed \([2/2]\) Padé step. It does not classify the full positivity sets for paths with more than eight vertices, irregular weights, other rational integrators, or internal stages. The positive interval is not a stability interval: A-stability and entrywise nonnegativity are distinct. The priority assessment is a comparison against specified inspected literature rather than a proof of historical uniqueness; independent mathematical validation has not been performed.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, “Essentially Negative News About Positive Systems,” *Linear Algebra and its Applications* 436 (2012), 3425–3442; lawful preprint at https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf and public repository record https://mural.maynoothuniversity.ie/id/eprint/3761/ .
2. L. Lóczi and D. I. Ketcheson, “Rational functions with maximal radius of absolute monotonicity,” *LMS Journal of Computation and Mathematics* 17 (2014), 159–205, https://doi.org/10.1112/S1461157013000326 ; preprint arXiv:1303.6651.
3. B. Jin, R. Lazarov, V. Thomée and Z. Zhou, “On Nonnegativity Preservation in Finite Element Methods for Subdiffusion Equations,” arXiv:1510.02825v1 (9 October 2015), https://arxiv.org/abs/1510.02825 .
4. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab .
