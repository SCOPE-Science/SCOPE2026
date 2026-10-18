# A certified nonconstant log-periodic singularity in a triangular polynomial map

## Finding
Consider the polynomial planar map
\[
T(x,y)=\left(\frac{x(4-xy)}2,\frac{y(1+xy)}3\right).
\]
For every \(x_0>0\) and \(1<x_0y_0<2\), its orbit tends to a finite point \((X,2/X)\) with \(X>0\). Set \(v=x_0y_0-1\in(0,1)\). The normalized limiting coordinate \(L(v)=X/x_0\) has a singular boundary law
\[
\boxed{L(v)=v^{-\alpha}\,\mathcal Q(\log_{7/6}v)\bigl(1+2v+O(v^2)\bigr),\qquad
\alpha=\frac{\log(3/2)}{\log(7/6)}.}
\]
Here \(\mathcal Q:\mathbb R\to(0,\infty)\) is a **real-analytic, nonconstant, period-one function**, defined constructively below. The remainder is uniform as \(v\downarrow0\); the bounded positive function \(\mathcal Q\) is independent of \(x_0\). The nonconstancy, a very small effect of order \(10^{-24}\) in a certified comparison of two phases, is proved by finite interval enclosures with rigorously bounded infinite-product tails.

## Assumptions and scope
All variables and products in the theorem are real. The domain is \(x_0>0\), \(y_0>0\), \(1<x_0y_0<2\). Define
\[
F(v)=\frac{7v-v^3}{6},\quad \lambda=\frac76,\quad p(v)=\frac{3-v}{2},\quad
\alpha=\log_\lambda(3/2).
\]
The restriction of \(F\) to \((0,1)\) is an increasing analytic bijection of \((0,1)\) onto itself, with fixed endpoints \(0\) (repelling) and \(1\) (attracting). Write \(g=F^{-1}\) on \((0,1)\). Define the convergent objects
\[
L(v)=\prod_{k=0}^{\infty}p(F^k(v)),\qquad
B(v)=\prod_{j=1}^{\infty}\left(1-\frac{g^j(v)}3\right),\qquad
h(v)=\lim_{n\to\infty}\lambda^n g^n(v).
\]
The function \(h\) is the increasing repelling Koenigs coordinate with \(h(Fv)=\lambda h(v)\), \(h(v)=v+O(v^3)\) near zero, and range \((0,\infty)\). Define
\[
A(v)=L(v)B(v)h(v)^\alpha,\qquad
\mathcal Q(t)=A\bigl(h^{-1}(\lambda^t)\bigr).
\]
These are explicit infinite products and limits rather than an unsupported existence assertion. They also give an exact formula for \(L\) at every \(v\in(0,1)\).

## Proof
**1. Product reduction and convergence.** Put \(u_n=x_ny_n\), \(v_n=u_n-1\). Direct multiplication of the two planar updates gives
\[
u_{n+1}=\frac{u_n(4-u_n)(1+u_n)}6,
\qquad v_{n+1}=F(v_n).
\]
For \(0<v<1\), \(F(v)-v=v(1-v^2)/6>0\), while \(F(v)<1\). Thus \(v_n\uparrow1\). Moreover
\[
1-F(v)=(1-v)\frac{6-v-v^2}{6},
\]
which contracts geometrically once \(v\) stays in any compact interval bounded away from zero. Hence \(\sum_n(1-v_n)<\infty\), and
\[
\frac{x_n}{x_0}=\prod_{k=0}^{n-1}\left(1+\frac{1-v_k}{2}\right)
\longrightarrow L(v)\in(1,\infty).
\]
Since \(x_ny_n=1+v_n\to2\), necessarily \(y_n\to2/(x_0L(v))\). This proves the stated finite-limit dynamics.

**2. Backward linearization.** The map \(F\) is analytic and strictly increasing on \([0,1]\), with derivative \((7-3v^2)/6>0\). Its inverse \(g\) has \(g(v)<v\) and, near zero,
\[
g(v)=\lambda^{-1}v+O(v^3).
\]
For \(z_n=g^n(v)\), the ratio of the consecutive renormalized iterates is exact:
\[
\frac{\lambda^{n+1}z_{n+1}}{\lambda^n z_n}
=\frac{1}{1-z_{n+1}^2/7}.
\]
The product of these ratios converges locally uniformly and analytically because the inverse iterates decay geometrically. Consequently \(h(v)=\lim_n\lambda^n z_n\) exists, is positive and locally strictly increasing near zero, and satisfies \(h(Fv)=\lambda h(v)\). Strict monotonicity on the whole interval follows by pulling any two distinct points backward into that local neighborhood. Local analytic linearization at the repeller and oddness of \(F\) give \(h(v)=v+O(v^3)\). Continuity follows from local uniform convergence. Finally, since \(g^n(v)\uparrow1\) for fixed \(n\) as \(v\uparrow1\), one has \(h(v)\ge\lambda^n g^n(v)\to\lambda^n\) for each \(n\); hence \(h(v)\to\infty\) as \(v\uparrow1\). Thus \(h\) maps \((0,1)\) bijectively onto \((0,\infty)\).

**3. An exact one-step invariant.** The backward product \(B(v)\) converges locally uniformly and analytically. Applying the definitions,
\[
L(Fv)=\frac{L(v)}{(3/2)(1-v/3)},\qquad
B(Fv)=(1-v/3)B(v),\qquad
h(Fv)=\lambda h(v).
\]
As \(\lambda^\alpha=3/2\), these identities prove \(A(Fv)=A(v)\). The definition of \(\mathcal Q\) then yields \(\mathcal Q(t+1)=\mathcal Q(t)\). All factors are positive and real analytic; thus \(\mathcal Q\) is positive real analytic and has positive minimum and finite maximum on one period. Rearranging the definition gives the **exact identity**
\[
L(v)=\frac{\mathcal Q(\log_\lambda h(v))}{B(v)h(v)^\alpha}.
\]
The inverse Taylor expansion is \(g^j(v)=\lambda^{-j}v+O(\lambda^{-j}v^3)\), uniformly summably in \(j\). Hence
\[
B(v)=1-\frac v3\sum_{j=1}^\infty\lambda^{-j}+O(v^2)
=1-2v+O(v^2).
\]
Since \(h(v)=v+O(v^3)\) and \(\mathcal Q\) is positive \(C^1\)-periodic, a phase displacement of \(O(v^2)\) changes \(\mathcal Q\) by a relative \(O(v^2)\). Substitution into the exact identity proves the claimed uniform two-term log-periodic asymptotic.

**4. Certified nonconstancy.** For \(v\in\{9/20,1/2\}\), compute the first \(N=1000\) factors in \(L\) and \(B\), and \(h_N=\lambda^N g^N(v)\), with outward-rounded interval arithmetic. The following bounds control all omitted factors. With \(w_N=1-F^N(v)\) and \(z_N=g^N(v)\),
\[
L_N\le L\le L_Ne^{5w_N},\quad
B_N(1-3z_N)\le B\le B_N,\quad
h_N\le h\le h_Ne^{z_N^2}.
\]
Indeed \(w_{n+1}/w_n\le0.9\) for the two input values, and \(z_{n+1}/z_n\le0.9\) since \(z_n\le1/2\). For \(h\) use \(-\log(1-t)\le t/(1-t)\), yielding a total remainder smaller than \(z_N^2\). Every inverse-step interval is certified by checking that the two proposed endpoints map under increasing \(F\) to opposite sides of the current input interval; no heuristic root location is accepted.

The resulting conservative enclosing decimal intervals are
\[
0.23236031438400375677835026781327<A(9/20)
<0.23236031438400375677835026781328,
\]
\[
0.23236031438400375677835155841814<A(1/2)
<0.23236031438400375677835155841815.
\]
In particular \(A(1/2)-A(9/20)>1.2\times10^{-24}\), so \(A\), and therefore \(\mathcal Q\), cannot be constant. The accompanying `verify.py` recreates these interval enclosures from the definitions; it does not extrapolate a finite orbit to an infinite claim without the explicit tail inequalities.

## Verification
The standalone script `verify.py` uses arbitrary-precision real interval arithmetic for products, logarithms and exponentials, and brackets each backward cubic inverse by a monotonicity check. It runs \(1000\) forward and inverse steps independently for both rational inputs, incorporates the rigorous tail factors above, asserts disjoint phase-value intervals and returns `VERIFY_OK`. Its exact scope is certifying nonconstancy of \(\mathcal Q\); convergence, uniform asymptotics and all quantified dynamical assertions are proved analytically in Steps 1–3. The script uses `mpmath` and Python 3; no external data files are required.

## Relationship to prior work
Cima, Gasull and Mañosa (first publicly available 2013-07-25, arXiv:1307.6666, Example F and equation (9), Lemma 10 and Proposition 11) introduced and analyzed precisely the polynomial family from which this \(d=1/3\) specialization is taken. Their convergence theorems for attracting fibers motivate the limiting-coordinate problem, but do not compute the singular dependence of the limiting coordinate on initial product near the repelling fiber, the two-term log-periodic law, or a certified nonconstant phase. The general mechanism of log-periodic corrections is classical (Sornette, 1998); its existence in other models does not give the specific cubic conjugacy, amplitude, or certified phase variation here. Only this particular concrete law and its nonconstancy are claimed as the new contribution.

## Limitations
The theorem is restricted to the positive basin strip \(1<xy<2\) and the parameter \(d=1/3\). It describes the singularity as the initial product approaches \(1\) from above, not all initial data or a global basin classification. The phase variation is extremely small and cannot be inferred reliably from ordinary double-precision experiments. Its certificate depends on the outward-rounded `mpmath.iv` implementation; no independent formal proof assistant or third-party audit has been used. The result does not assert absolute historical priority over inaccessible or unindexed studies.

## References
1. A. Cima, A. Gasull and V. Mañosa, *Basin of attraction of triangular maps with applications*, arXiv:1307.6666v1 (2013-07-25), especially Example F, equation (9), Lemma 10 and Proposition 11; Journal of Difference Equations and Applications **20** (2014), 423–437, DOI: 10.1080/10236198.2013.852187. Accessible full-text transcription at https://www.researchgate.net/publication/251876203_Basin_of_attraction_of_triangular_maps_with_applications.
2. D. Sornette, *Discrete-scale invariance and complex dimensions*, Physics Reports **297** (1998), 239–270, DOI: 10.1016/S0370-1573(97)00076-8. General background, not a source for the specific polynomial theorem.
