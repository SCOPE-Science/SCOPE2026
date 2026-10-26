# Arithmetic lattice phases in the boundary sensitivity of quadratic discrete least squares

## Finding

The worst-case amplification at either observed endpoint of **unweighted quadratic least-squares regression on an equispaced grid** is exactly computable for every sample count. More unusually, its normalized second-order sampling error oscillates with a dense irrational lattice phase and has distinct sharp limit inferior and superior.

For an integer \(m\ge3\), fit a real or complex polynomial of degree at most two by ordinary least squares to data \(y=(y_0,\ldots,y_{m-1})\) at \(x_j=-1+2j/(m-1)\). Let \(P_m\) denote the fitted values at the sample nodes, and put
\[
E_m=\sup_{\|y\|_\infty\le1}|(P_my)_0|.
\]
Define
\[
D_m=6m^2-6m-11,\quad r_\pm=\frac{6m-3\pm\sqrt{D_m}}{10},\quad L_m=r_+-r_-,
\]
\[
\delta_-=\lceil r_-\rceil-r_-,\qquad \delta_+=r_+-\lfloor r_+\rfloor,
\]
where the fractional offsets lie in \([0,1)\), and \(B_2(u)=u^2-u+1/6\), \(B_3(u)=u^3-3u^2/2+u/2\). Then **exactly**
\[
\boxed{E_m=1+\frac{10L_m^3-30L_m[B_2(\delta_-)+B_2(\delta_+)]+20[B_3(\delta_-)+B_3(\delta_+)]}{m(m+1)(m+2)}.}
\]
In particular,
\[
E_m=1+\frac{12\sqrt6}{25}-\frac{54\sqrt6}{25m}+O(m^{-2}).
\]
The residual \(R_m=m^2[E_m-1-12\sqrt6/25+54\sqrt6/(25m)]\) does **not** converge:
\[
\boxed{\liminf_{m\to\infty}R_m=\frac{119\sqrt6}{50},\qquad \limsup_{m\to\infty}R_m=\frac{269\sqrt6}{50}.}
\]
Thus the leading boundary sensitivity is universal, but the next correction cannot be represented by a single fixed coefficient of \(m^{-2}\).

## Assumptions and scope

The observations have equal positive least-squares weights, and both the input and endpoint output have the absolute-value/supremum norm. The fitted polynomial is evaluated **at one of the sample endpoints**. Reflection gives the same sharp value at the opposite endpoint. No assertion is made that an endpoint maximizes the absolute row sums over all output nodes, or that the displayed number is the global operator norm of the matrix. The fitted polynomial space has dimension three, so \(m\ge3\) is necessary. The extremal input takes the sign (or unit complex phase) of the endpoint projection row; the finite-dimensional norm is attained.

## Proof

**1. Orthogonal regression kernel.** Index the observations by \(j=0,\ldots,m-1\), and set \(t_j=j-(m-1)/2\) and \(q_j=t_j^2-(m^2-1)/12\). The mutually orthogonal sampled polynomials \(1,t,q\) have squared Euclidean norms
\[
\|1\|_2^2=m,\quad \|t\|_2^2=\frac{m(m^2-1)}{12},\quad \|q\|_2^2=\frac{m(m^2-1)(m^2-4)}{180}.
\]
Their reproducing-kernel row at \(j=0\) is therefore
\[
h_{m,j}=\frac1m+\frac{t_0t_j}{\|t\|_2^2}+\frac{q_0q_j}{\|q\|_2^2}
=\frac{3[10j^2+(6-12m)j+3m^2-3m+2]}{m(m+1)(m+2)}.
\]
Since the projector reproduces constants, \(\sum_jh_{m,j}=1\). Since it is a scalar linear functional, \(E_m=\sum_j|h_{m,j}|\).

**2. Exactly two sign boundaries.** The two real roots of the numerator quadratic are \(r_-\) and \(r_+\). They obey \(0<r_-<r_+\le m-1\) for \(m\ge3\), with equality at the upper bound only when \(m=3\). Consequently,
\[
h_{m,j}=\frac{30(j-r_-)(j-r_+)}{m(m+1)(m+2)},\quad
E_m=1-\frac{60}{m(m+1)(m+2)}\sum_{r_-<j<r_+}(j-r_-)(j-r_+).
\]
The sum is over integers; roots which happen to be integers contribute zero.

**3. Exact lattice summation.** For any real \(a<b\), put \(L=b-a\), \(\delta_a=\lceil a\rceil-a\), \(\delta_b=b-\lfloor b\rfloor\). Direct integration of the quadratic \(p(x)=(x-a)(x-b)\), with the trapezoidal endpoint correction and the exact quadratic Euler–Maclaurin term, gives
\[
\sum_{a<j<b}(j-a)(j-b)
=-\frac{L^3}{6}+\frac{L}{2}[B_2(\delta_a)+B_2(\delta_b)]
-\frac13[B_3(\delta_a)+B_3(\delta_b)].
\]
The formula remains valid when a root is an integer because its summand vanishes and \(B_2(0)=1/6\), \(B_3(0)=0\). Substitution proves the exact expression for \(E_m\).

**4. Uniform asymptotic expansion.** We have \(L_m=\sqrt{D_m}/5\), so the integral term is
\[
1+\frac{2D_m^{3/2}}{25m(m+1)(m+2)}
=1+\frac{12\sqrt6}{25}-\frac{54\sqrt6}{25m}+
\frac{219\sqrt6}{50m^2}+O(m^{-3}).
\]
Since \(B_2\) and \(B_3\) are bounded on \([0,1]\), the exact remainder gives, uniformly in the lattice offsets,
\[
R_m=\sqrt6\left[\frac{219}{50}-6\big(B_2(\delta_-)+B_2(\delta_+)\big)\right]+O(m^{-1}).
\]
The bounds \(-1/12\le B_2(u)\le1/6\) imply \(-1/6\le B_2(\delta_-)+B_2(\delta_+)\le1/3\), hence the stated universal lower and upper cluster bounds.

**5. Both limits are attained along subsequences.** The root sum is \(r_-+r_+=(6m-3)/5\). On the subsequence \(m\equiv3\pmod5\) this is an integer. Writing \(\theta_m=\{r_-\}\), the symmetry \(B_2(u)=B_2(1-u)\) gives
\[
B_2(\delta_-)+B_2(\delta_+)=2B_2(\theta_m).
\]
Also \(r_-=\alpha m+c+O(m^{-1})\), with irrational \(\alpha=(6-\sqrt6)/10\) and a fixed \(c\). Restricted to \(m=5k+3\), \(\theta_m\) is therefore an irrational rotation modulo one plus a vanishing perturbation and is equidistributed in \([0,1)\) (Weyl's criterion). The values \(B_2(1/2)=-1/12\) and \(B_2(0)=1/6\) can both be approached, so the two universal bounds are the actual liminf and limsup. This completes the proof.

## Verification

The standalone Python checker `quadratic_boundary_verify.py` reconstructs the projection row from independent rational Gram-matrix inversion, compares its entries with the closed polynomial kernel for all \(3\le m\le50\), and compares the exact rational absolute row sums with the Bernoulli formula at 70-digit precision for all \(3\le m\le250\). The checker also prints the predicted sharp asymptotic cluster values. These finite tests do not prove the equidistribution assertion or the infinite asymptotic limits; those follow from the algebraic and analytic steps above.

## Relationship to prior work

Cohen, Davenport and Leviatan study stability of polynomial least-squares reconstruction, including deterministic samples equispaced for relevant measures (arXiv:1111.4422, first publicly submitted 18 November 2011). Zhou, Narayan and Xu develop deterministic multivariate discrete least-squares schemes using different point sets (arXiv:1401.0894, 5 January 2014). Their inspected statements concern stable reconstruction, approximation rates, and sampling design, rather than exact quadratic endpoint \(\ell^\infty\) sensitivity or its second-order arithmetic oscillations. Goertz's dissertation on equidistant discrete least squares (2018) is the closest same-grid treatment inspected; its chapter-level results concern representation by Hahn polynomials, convergence, and estimates, not an identified matching endpoint second-order theorem. The latter comparison is not an exhaustive claim about every line of the dissertation.

## Limitations

Only endpoint evaluation on the observed grid is evaluated exactly; the norm of the full projection or evaluation at unsampled points is not determined. The result assumes uniform weights and quadratic degree and does not establish corresponding formulas for higher degrees or nonuniform designs. Prior unindexed treatments or an unexamined passage in the large same-grid dissertation could contain equivalent calculations; absence from the searched sources is not a proof of priority. No independent mathematical audit has been performed.

## References

1. A. Cohen, M. A. Davenport, D. Leviatan, *On the stability and accuracy of least squares approximations*, arXiv:1111.4422 (first version 18 November 2011), https://arxiv.org/abs/1111.4422.
2. T. Zhou, A. Narayan, Z. Xu, *Multivariate discrete least-squares approximations with a new type of collocation grid*, arXiv:1401.0894 (5 January 2014), https://arxiv.org/abs/1401.0894.
3. R. Goertz, *Zur Konvergenz diskreter Least-Squares Methoden auf äquidistanten Stützstellen*, dissertation, Cuvillier Verlag (2018), https://cuvillier.de/get/ebook/5433/9783736987432.pdf.
