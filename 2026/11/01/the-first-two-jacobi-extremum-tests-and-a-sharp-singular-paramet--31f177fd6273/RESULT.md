# The first two Jacobi-extremum tests and a sharp singular-parameter frontier

## Finding

For real parameters \(a,b>-1\), put
\[
p_n(x)=\frac{P_n^{(a,b)}(x)}{P_n^{(a,b)}(1)},\qquad
P_n^{(a,b)}(1)=\frac{(a+1)_n}{n!},
\]
where \(P_n^{(a,b)}\) is the classical Jacobi polynomial. Let \(x_{1,n}\) be its first extremum after the right endpoint: for \(n\ge2\) this is the largest interior zero of \((P_n^{(a,b)})'\), and for \(n=1\) put \(x_{1,1}=-1\). Write \(M_n(a,b)=|p_n(x_{1,n})|\).

**Exact finite-degree classification.** Define
\[
R(a,b)=\sqrt{\frac{(a+3)(b+3)}{a+b+5}}.
\]
Then, throughout \(a,b>-1\),
\[
\begin{aligned}
M_1&=\frac{b+1}{a+1},\\
M_2&=\frac{b+2}{(a+1)(a+b+4)},\\
M_3&=\frac{2(b+3)[a-b+(a+b+4)R(a,b)]}{(a+1)(a+2)(a+b+6)^2}.
\end{aligned}
\]
Consequently, the first first-extremum monotonicity test holds strictly, \(M_2<M_1\), **if and only if**
\[
(b+1)(a+b+4)>b+2.
\]
The next test, \(M_3<M_2\), holds strictly **if and only if**
\[
2(b+3)(a+b+4)[a-b+(a+b+4)R(a,b)]
<(a+2)(b+2)(a+b+6)^2.
\]
Equality in either displayed test gives equality of the corresponding two extrema; reversing the relevant inequality reverses the monotonicity. These equations determine the exact two-parameter degree-one and degree-two test boundaries.

**Sharp singular-parameter frontier.** Let
\[
 b_1=\frac{\sqrt5-3}{2}=-0.3819660112\ldots,
\]
and let \(b_c=-0.341032918083006\ldots\) be the unique zero on \((-1,\infty)\) of
\[
 C(b)=b^3+7b^2+14b+4.
\]
As \(a\downarrow-1\), the first two test differences have sharp sign transitions:
\[
\lim_{a\downarrow-1}(a+1)(M_2-M_1)<0
\quad\Longleftrightarrow\quad b>b_1,
\]
and
\[
\lim_{a\downarrow-1}(a+1)(M_3-M_2)>0
\quad\Longleftrightarrow\quad -1<b<b_c.
\]
In particular, for **every** \(b\in(b_1,b_c)\), there is \(\varepsilon_b>0\) such that whenever \(-1<a<-1+\varepsilon_b\),
\[
\boxed{M_2(a,b)<M_1(a,b)\quad\text{but}\quad M_3(a,b)>M_2(a,b).}
\]
Thus passing the first nontrivial normalized Jacobi relative-extremum comparison does **not** suffice to pass the next one, even in an open set of genuine admissible Jacobi parameters.

An exact rational example is \(a=-19/20\), \(b=-3/8\):
\[
M_1=\frac{25}{2},\qquad M_2=\frac{1300}{107}<\frac{25}{2},
\qquad M_3>M_2.
\]
The strict last inequality follows from the rational certificate given below.

## Assumptions and scope

Every parameter is real and satisfies \(a,b>-1\). Jacobi normalization is at \(x=1\), not a monic or orthonormal normalization. The index \(1\) counts extrema from the right endpoint, and the degree-one comparison uses the opposite endpoint as its first extremum. The singular parameter \(a=-1\) is never included in the theorem; only the limits after multiplying by \(a+1\) are asserted. Neither an all-degree monotonicity theorem nor a claim that degree three is the first failure for arbitrary parameters is made.

## Proof

The classical Jacobi derivative formula is
\[
\frac{d}{dx}P_n^{(a,b)}(x)
=\frac{n+a+b+1}{2}P_{n-1}^{(a+1,b+1)}(x).
\]
For degree one the normalized value at \(-1\) has modulus \((b+1)/(a+1)\). For degree two, direct expansion gives the unique interior critical point
\[
x_{1,2}=\frac{b-a}{a+b+4}
\]
and its unnormalized polynomial value
\[
P_2^{(a,b)}(x_{1,2})=-\frac{(a+2)(b+2)}{2(a+b+4)}.
\]
Division by \(P_2^{(a,b)}(1)=(a+1)(a+2)/2\) yields the asserted \(M_2\).

For degree three the derivative has two distinct roots; the larger is
\[
x_{1,3}=\frac{b-a+2R(a,b)}{a+b+6}.
\]
Exact polynomial division by its derivative gives
\[
P_3^{(a,b)}(x)\equiv
-\frac{(a+3)(b+3)}{6(a+b+6)}
[(a+b+4)x+a-b]
\pmod{(P_3^{(a,b)})'}.
\]
This polynomial value at the largest critical point is negative because it is the first local minimum after \(P_3^{(a,b)}(1)>0\), and the standard interlacing of Jacobi zeros places this extremum between the largest two zeros. Substitute \(x_{1,3}\) and divide by
\[
P_3^{(a,b)}(1)=\frac{(a+1)(a+2)(a+3)}6
\]
to obtain the \(M_3\) formula, including the strictly positive bracket. All factors used when cross-multiplying the two test inequalities are strictly positive on \(a,b>-1\), proving the exact classifications and their equality cases.

At the singular boundary, multiplication by \(a+1\) and passage to \(a\downarrow-1\) give
\[
\begin{aligned}
L_1(b)&=b+1,\\
L_2(b)&=\frac{b+2}{b+3},\\
L_3(b)&=\frac{2(b+3)}{(b+5)^2}
\left[(b+3)\sqrt{\frac{2(b+3)}{b+4}}-(b+1)\right].
\end{aligned}
\]
Here \(L_j(b)=\lim_{a\downarrow-1}(a+1)M_j(a,b)\). Direct subtraction yields
\[
L_2-L_1=-\frac{b^2+3b+1}{b+3},
\]
whose sign changes in \((-1,\infty)\) precisely at \(b_1\). To determine the other difference without relying on numerical roots, set
\[
\begin{aligned}
U(b)&=2(b+3)^3\sqrt{2(b+3)(b+4)},\\
V(b)&=(b+4)[2(b+1)(b+3)^2+(b+2)(b+5)^2].
\end{aligned}
\]
Both \(U,V\) are positive for \(b>-1\), and exact algebra gives
\[
L_3-L_2=\frac{U-V}{(b+3)(b+4)(b+5)^2},
\]
\[
U^2-V^2=-(b+2)(b+4)(b+5)^3C(b).
\]
Thus \(\operatorname{sgn}(L_3-L_2)=-\operatorname{sgn}C(b)\). Furthermore,
\[
C'(-1)=3>0,\qquad C''(b)=6b+14>0\quad (b>-1),
\]
so \(C\) is strictly increasing there, with \(C(-1)=-4\), \(C(0)=4\). Its unique root \(b_c\) satisfies \(b_c>b_1\), since \(C(b_1)=b_1<0\). Continuity in \(a\) yields the asserted open interval of strict two-test reversals for each fixed \(b\in(b_1,b_c)\).

For the exact rational witness, the formulas give \(M_1=25/2\), \(M_2=1300/107\), and \(R^2=41/28\). The second comparison reduces to
\[
 R>\frac{553037}{457960}.
\]
Both sides are positive, while
\[
\frac{41}{28}-\left(\frac{553037}{457960}\right)^2
=\frac{8755992817}{1468091531200}>0.
\]
Hence \(M_3>M_2\), completing the rational proof.

## Verification

A standalone symbolic checker, `verify.py`, constructs the Jacobi polynomials directly, validates the critical-point identities and the polynomial remainder formula, checks the exact factorization governing the cubic boundary, and checks the fully rational witness. It also tests a separate set of finite parameter samples. The universal claims above rely on the exact polynomial identities and sign arguments, not on sample enumeration or numerical root finding. The checker requires Python and SymPy, and prints `PASS` on success.

## Relationship to prior work

Castillo proved the normalized same-index relative-extremum monotonicity conjecture for all degrees in the region \(a,b>-1/2\) (arXiv:2608.01404v1, first public version August 2, 2026). The preprint describes the complete Jacobi-range boundary as undetermined and gives a reversal outside the proved parameter sector. The present finite-degree formulas and singular cusp distinguish two consecutive tests in the remaining region, without strengthening or re-proving the covered all-degree case.

Wong and Zhang's 1994 work treats relative extrema at the special boundary parameters \((a,b)=(0,-1)\), whereas their separate asymptotic analysis concerns eventual degree comparisons; neither statement determines the open two-parameter first/second-test reversal established here. Castillo and Hang's 2026 Jacobi–Radau theorem concerns the weighted family \((1+x)^{b+1}P_{m-1}^{(0,b+1)}(x)\), a genuinely different object, and its one-parameter threshold has no implication for these normalized ordinary Jacobi polynomials. A comparison by objects, normalizations, parameter domains, and conclusions is essential; matching a polynomial degree or using the phrase “Jacobi extrema” alone does not establish coverage.

## Limitations

The result completely classifies only the first-index degree-one and degree-two tests. It does not identify the maximal region where **all** relative-extremum inequalities hold, nor characterize every higher-index or higher-degree failure. The singular cubic boundary is a limit as \(a\downarrow-1\), not a theorem at the excluded value \(a=-1\). The 2026 primary preprint's abstract and theorem statement, its introductory discussion of the open parameter boundary, and available mathematical literature were checked; possible equivalent older finite-degree calculations remain a residual originality risk. The mathematical assessment here is not an independent audit.

## References

1. K. Castillo, *A Proof of the Szegő Conjecture on Jacobi Extrema*, arXiv:2608.01404v1, first submitted August 2, 2026. https://arxiv.org/abs/2608.01404
2. R. Wong and J.-M. Zhang, *On the Relative Extrema of the Jacobi Polynomials \(P_n^{(0,-1)}(x)\)*, SIAM Journal on Mathematical Analysis 25 (1994), 776–811, doi:10.1137/S0036141091223893.
3. R. Wong and J.-M. Zhang, *Asymptotic Monotonicity of the Relative Extrema of Jacobi Polynomials*, Canadian Journal of Mathematics 46 (1994), 1318–1337, doi:10.4153/CJM-1994-075-1.
4. K. Castillo and P.-C. Hang, *Equal-Phase Monotonicity for Weighted Jacobi–Radau Functions and Jacobi Lebesgue Constants*, arXiv:2609.13030v1, 2026. https://arxiv.org/abs/2609.13030
