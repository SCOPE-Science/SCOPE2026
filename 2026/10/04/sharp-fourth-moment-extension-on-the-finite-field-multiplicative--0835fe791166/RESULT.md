# Sharp fourth-moment extension on the finite-field multiplicative hyperbola
## Finding
Let \(F\) be a finite field of odd order \(q\), and write
\[
H=\{(t,t^{-1}):t\in F^\times\}\subset F^2.
\]
Give \(H\) normalized surface measure \(d\sigma\), give \(F^2\) counting measure, and fix a nontrivial additive character \(e:F\to\mathbb C\). For \(g:F^\times\to\mathbb C\), define
\[
Eg(x,y)=\frac{1}{q-1}\sum_{t\in F^\times}g(t)e(xt+yt^{-1}).
\]
Then
\[
R_H^*(2\to4)^4=\frac{3q^2(q-2)}{(q-1)^3}.
\]
The nonzero extremizers are exactly the functions of constant modulus for which all antipodal products \(g(t)g(-t)\) have one common argument. Equivalently, there are \(r>0\) and \(\phi\in\mathbb R\) such that
\[
|g(t)|=r,\qquad g(-t)=e^{i\phi}\overline{g(t)}\quad(t\in F^\times).
\]
Consequently constant functions are extremizers, and the additive energy of \(H\) is
\[
E(H)=3(q-1)(q-2).
\]

## Assumptions and scope
The field has odd order; characteristic two is excluded because the antipodal pairing used below degenerates. The ambient \(L^4\) norm uses ordinary counting measure on \(F^2\), while the \(L^2\) norm on \(H\) uses normalized surface measure. These are the standard finite-field restriction normalizations of Mockenhaupt--Tao. No asymptotic limit in \(q\) is taken.

## Proof
Put
\[
S=\sum_{t\in F^\times}|g(t)|^2.
\]
Expanding the fourth power and using additive-character orthogonality gives
\[
\|Eg\|_4^4=\frac{q^2}{(q-1)^4}Q(g),
\]
where
\[
Q(g)=\sum_{\substack{a,b,c,d\in F^\times\\
(a,a^{-1})+(b,b^{-1})=(c,c^{-1})+(d,d^{-1})}}
 g(a)g(b)\overline{g(c)g(d)}.
\]
Also
\[
\|g\|_{L^2(H,d\sigma)}^4=\frac{S^2}{(q-1)^2}.
\]

The collision geometry has one exceptional fiber. If \(a+b=c+d=s\ne0\), then equality of inverse sums gives
\[
\frac{s}{ab}=\frac{s}{cd},
\]
so \(ab=cd\); hence \(\{a,b\}=\{c,d\}\). If \(s=0\), every ordered antipodal pair \((a,-a)\) has the same vector sum \((0,0)\). Therefore, with
\[
P_4=\sum_t|g(t)|^4,\qquad
R=\sum_t|g(t)|^2|g(-t)|^2,\qquad
B=\sum_t g(t)g(-t),
\]
one has the exact identity
\[
Q(g)=2S^2-P_4-2R+|B|^2.
\]

Partition \(F^\times\) into its \((q-1)/2\) antipodal pairs. On the \(j\)-th pair set
\[
x_j=|g(t_j)|^2,\quad y_j=|g(-t_j)|^2,\quad s_j=x_j+y_j,\quad p_j=\sqrt{x_jy_j},
\]
and write \(g(t_j)g(-t_j)=p_je^{i\theta_j}\). Then
\[
Q(g)=2S^2-\sum_j s_j^2-2\sum_jp_j^2+4\left|\sum_jp_je^{i\theta_j}\right|^2.
\]
For fixed \((s_j)\), the last two terms are maximized when all phases \(\theta_j\) agree and each \(p_j=s_j/2\). Indeed, after phase alignment the function
\[
-2\sum_jp_j^2+4\left(\sum_jp_j\right)^2
\]
is coordinatewise increasing on \(0\le p_j\le s_j/2\), with strict improvement unless the coordinate is already maximal in every nonzero pair. Thus
\[
Q(g)\le3S^2-\frac32\sum_js_j^2.
\]
There are \((q-1)/2\) pairs, so Cauchy--Schwarz yields
\[
\sum_js_j^2\ge\frac{2S^2}{q-1}.
\]
Hence
\[
Q(g)\le \frac{3(q-2)}{q-1}S^2.
\]
Combining this with the two norm identities gives
\[
\frac{\|Eg\|_4^4}{\|g\|_2^4}
\le \frac{3q^2(q-2)}{(q-1)^3}.
\]

Equality in the triangle inequality requires all nonzero antipodal products to have the same argument; equality in \(p_j\le s_j/2\) requires \(x_j=y_j\); and equality in Cauchy--Schwarz requires all \(s_j\) to be equal. Together these are exactly the stated constant-modulus and common-product-phase conditions. They are plainly attainable, so the constant is sharp and the equality classification is complete. Taking \(g\equiv1\) and reading the collision sum as additive energy gives \(E(H)=3(q-1)(q-2)\).

## Verification
The included script `verify_hyperbola.py` reconstructs the pair-sum fibers for every odd prime through \(101\), checks the exact additive-energy formula, checks that the unique exceptional vector sum has \(q-1\) ordered representations, and verifies sharp weighted collision values for deterministic sign extremizers satisfying the equality conditions. The script is corroborative only; the proof above covers every finite field of odd order.

## Relationship to prior work
Mockenhaupt--Tao introduced the finite-field extension normalization and the \(R^*(p\to r)\) framework, with counting measure on the physical space and normalized surface measure on the frequency surface. Iosevich--Koh proved the uniform \(L^2\to L^4\) extension bound for every nondegenerate quadratic surface; in dimension two their proof bounds the number of representations of each nonzero pair sum by two. For the present hyperbola, that argument gives the correct exponent but does not compute the best finite-\(q\) constant or classify equality.

Iosevich--Murphy--Pakianathan study exactly the hyperbola \(xy=1\) over finite rings and fields through its Fourier coefficients and Kloosterman--Salem behavior. Their invariant is Fourier decay of the surface measure rather than the sharp weighted fourth extension norm. González-Riquelme--Oliveira e Silva initiated sharp finite-field restriction theory for best constants and maximizers, treating the parabola, paraboloids, the hyperbolic paraboloid, and cones; their listed sharp surfaces do not include the planar multiplicative hyperbola. The present result isolates the exceptional zero-sum fiber of that hyperbola and exactly optimizes the resulting weighted energy.

## Limitations
The theorem excludes characteristic two. It does not address other \(L^p\to L^r\) exponents, stability of near-extremizers, or finite rings with zero divisors. The literature comparison found no covering statement for this exact constant and equality class, but differently indexed work on Kloosterman sets or sharp conic inequalities remains a residual originality risk.

## References
G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first submitted 2002-04-18; Duke Math. J. 121 (2004), 35--74.

A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505, first submitted 2008-04-28; Illinois J. Math. 52 (2008), 611--628.

A. Iosevich, B. Murphy, and J. Pakianathan, *The square root law and structure of finite rings*, arXiv:1405.7657, first submitted 2014-05-29.

C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first submitted 2024-05-26.
