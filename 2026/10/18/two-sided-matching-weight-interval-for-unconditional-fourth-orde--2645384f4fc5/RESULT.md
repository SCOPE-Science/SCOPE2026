# Two-sided matching-weight interval for unconditional fourth-order diffusion positivity

## Finding

Let \(n\ge3\), \(a>0\), and \(b\ge0\). Consider two vertex classes \(A=\{A_1,\ldots,A_n\}\) and \(B=\{B_1,\ldots,B_n\}\). Assign conductance \(b\) to the matched edge \(A_iB_i\) and conductance \(a\) to every unmatched edge \(A_iB_j\) with \(i\ne j\). There are no edges inside either class. This connected weighted graph includes the crown graph at \(b=0\) and the uniform complete bipartite graph at \(b=a\).

Let \(L\) be its combinatorial weighted Laplacian. Define the two-stage, fourth-order Gauss–Legendre diffusion step
\[
T(h)=(12I-6hL+h^2L^2)(12I+6hL+h^2L^2)^{-1},\qquad h\ge0.
\]
Set
\[
r=\frac{(n-2)a+2b}{na},\quad r_-=\frac{\sqrt5-1}{2},\quad
r_+(n)=\frac{1+\sqrt{1+4(n-1)^2}}{2(n-1)}.
\]
**The step is entrywise nonnegative for every \(h\ge0\) if and only if**
\[
\boxed{r_-\le r\le r_+(n).}
\]
Equivalently, the exact **closed** conductance window is
\[
\boxed{\max\left\{0,\,1-\frac{n(3-\sqrt5)}4\right\}\ \le\frac ba\le\ 1+\frac n2\bigl(r_+(n)-1\bigr).}
\]
When \(r<r_-\), there is a unique finite positive timestep \(H\) at which **unmatched** cross-part entries vanish; all such entries are negative for \(h>H\), and all other off-diagonal types remain nonnegative. When \(r>r_+(n)\), the same statements hold with **matched** cross-part entries in place of unmatched entries. In either exterior regime the entire entrywise-nonnegativity set is precisely \([0,H]\). At either boundary of the window, every positive timestep is admissible.

For an explicit algebraic specification of \(H\), put \(t=nah\) and define
\[
\begin{aligned}
Y_r(t)={}&288+144(1+r)t+24(1+2r+2r^2)t^2\\
&+12r^2(1+r)t^3+r(1+r)(r^2+r-1)t^4,\\[2pt]
X_{n,r}(t)={}&144(nr-n+2)+72(1+r)(nr-n+2)t\\
&+12(nr^3-n+2+4r+4r^2)t^2\\
&+6r(1+r)(n(1-r)+2r)t^3\\
&+r(1+r)\bigl((n-1)(1-r^2)+r\bigr)t^4.
\end{aligned}
\]
In the first exterior regime \(naH\) is the unique positive zero of \(Y_r\); in the second it is the unique positive zero of \(X_{n,r}\).

A sharp small-to-large graph transition follows at the crown-graph endpoint \(b=0\): **unconditional positivity holds precisely for \(n\ge6\)**. The upper admissible weight ratio tends to \(5/4\) as \(n\to\infty\), so increasing the matching conductance too far eventually destroys unconditional positivity even for arbitrarily large networks.

## Assumptions and scope

The system is finite, undirected and reversible. Edge weights are real, \(a>0\), \(b\ge0\), and \(n\ge3\). The notation \(T(h)\ge0\) is entrywise and refers to the **completed** rational update, not to individual Runge–Kutta stages. The assertion concerns positivity for all nonnegative initial states, not monotonicity or positivity of eigenvalues alone. The eigenvalue \(0\) is simple because unmatched edges form a connected crown graph for \(n\ge3\).

## Proof

Write \(u=na\), \(v=(n-2)a+2b\) and \(w=u+v=2((n-1)a+b)\). Let \(J\) denote the all-ones \(n\times n\) matrix, \(M=I-J/n\), and \(\mathbf1\) the all-ones vector of length \(n\). In the decomposition \(\mathbb R^{2n}=\mathbb R^n\oplus\mathbb R^n\), the four mutually orthogonal spectral projectors are
\[
\Pi_0=\frac1{2n}\begin{bmatrix}J&J\\J&J\end{bmatrix},\qquad
\Pi_u=\frac12\begin{bmatrix}M&M\\M&M\end{bmatrix},\qquad
\Pi_v=\frac12\begin{bmatrix}M&-M\\-M&M\end{bmatrix},\qquad
\Pi_w=\frac1{2n}\begin{bmatrix}J&-J\\-J&J\end{bmatrix}.
\]
Their eigenvalues under \(L\) are respectively \(0,u,v,w\), of multiplicities \(1,n-1,n-1,1\). These projectors sum to \(I\); the eigenvalues follow directly from the constant and zero-sum actions of the cross-class conductance matrix \(aJ+(b-a)I\).

For \(z\ge0\), put
\[
R(z)=\frac{z^2-6z+12}{z^2+6z+12},\qquad F(z)=1-R(z)=\frac{12z}{z^2+6z+12}.
\]
Since \(z^2-6z+12=(z-3)^2+3>0\) and the denominator is positive, all eigenvalues of \(T(h)\) are strictly positive. Hence every diagonal entry of \(T(h)\) is positive. Since \(R(0)=1\), all row sums are one. With \(\alpha=F(uh)\), \(\beta=F(vh)\), \(\gamma=F(wh)\), the three possible off-diagonal entries are
\[
\begin{array}{ll}
\text{same-part, distinct:}&(\alpha+\beta-\gamma)/(2n),\\
\text{cross-part, matched:}&((n-1)(\beta-\alpha)+\gamma)/(2n),\\
\text{cross-part, unmatched:}&(\alpha-\beta+\gamma)/(2n).
\end{array}
\]
The first expression is strictly positive for \(h>0\), because \(F(z)/z=12/(z^2+6z+12)\) strictly decreases and \(w=u+v\): \(F(uh)+F(vh)>F(wh)\).

Set \(t=uh>0\), \(r=v/u\), and
\[
D(t)=(t^2+6t+12)(r^2t^2+6rt+12)((1+r)^2t^2+6(1+r)t+12)>0.
\]
Direct multiplication of the preceding spectral expressions gives the unmatched entry \(6tY_r(t)/(nD(t))\) and the matched entry \(6tX_{n,r}(t)/(nD(t))\), with exactly the polynomials displayed under Finding. The admissible parameter range is \(r\ge r_0=(n-2)/n\).

All coefficients of \(Y_r\) except its leading one are strictly positive. Its leading coefficient has the sign of \(r^2+r-1\). Consequently \(Y_r(t)>0\) for every \(t>0\) exactly when \(r\ge r_-\); when \(r<r_-\), Descartes' sign rule and the negative leading coefficient give exactly one positive root, followed by strict negativity.

For \(X_{n,r}\), the constant and linear coefficients are nonnegative since \(nr-n+2\ge0\). The quadratic coefficient is strictly positive: \(f(r)=nr^3+4r^2+4r+2-n\) is increasing, while \(f((n-2)/n)=4(n-2)(n-1)/n^2>0\). Its leading coefficient has the sign of \((n-1)(1-r^2)+r\), which changes exactly once on \(r>0\), at \(r_+(n)\). If \(r\le r_+(n)\), then \(r< n/(n-2)\), so the cubic coefficient \(6r(1+r)[n-(n-2)r]\) is positive and hence every coefficient is nonnegative. To check the strict inequality, evaluate the decreasing quadratic \((n-1)(1-r^2)+r\) at \(r=n/(n-2)\), where it is negative. If \(r>r_+(n)\), the leading coefficient is negative; the cubic coefficient may have either sign, but the quadratic and lower coefficients remain nonnegative, so the descending coefficient sequence has exactly one sign change. Descartes' rule and the negative large-\(t\) limit again yield exactly one positive root and strict negativity after it.

Because \(r_-<1<r_+(n)\), the two exterior regimes are disjoint, so at most one cross-entry type can fail. Its unique root defines the full positivity interval. Solving the two leading-coefficient inequalities for \(b/a\) proves the boxed conductance window. At \(b=0\), \(r=(n-2)/n\), which exceeds \(r_-\) exactly for integers \(n\ge6\). Finally, \(r_+(n)=1+1/[2(n-1)]+O(n^{-2})\), yielding the limit \(5/4\) for the upper conductance ratio. All quantifiers and boundary cases are covered.

## Verification

Run `python3 verify.py` using Python's standard library. The checker independently constructs the full weighted Laplacian, computes the rational update by exact-fraction Gauss–Jordan inversion, and checks its entries against the projector formulas and against the two sign polynomials for integer \(3\le n\le6\), two positive choices of \(a\), seven choices of \(b\) including zero, and six timesteps including zero. Its output is `VERIFY_OK 26712 exact rational assertions`. This finite replay verifies arithmetic on a specified finite test domain; the proof above establishes the infinite family.

For concrete negative entries, at \((n,a,b,h)=(3,1,0,20)\), the unmatched cross-part entry is \(-1650620/75851629\). At \((n,a,b,h)=(6,1,2,20)\), the matched cross-part entry is \(-78035480/12902240533\). Both are independently obtained by exact full-matrix inversion.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten (2010, 2012) study the general loss of positivity under diagonal Padé discretization, provide sufficient conditions and examples, and motivate exact structure-dependent criteria. Their inspected arguments do not give an optimal matched-bipartite conductance interval. General Padé positivity on unweighted complete multipartite graphs covers the single case \(a=b\), not the complete anisotropic classification or the crown-graph threshold derived here. Standard spectral decomposition of equitable weighted bipartite graphs is used, not claimed as new.

## Limitations

This is a two-conductance, perfectly matched, balanced bipartite family; arbitrary edgewise conductances or unequal part sizes are not covered. The result concerns a specific fourth-order rational integrator, not all A-stable methods. Originality rests on comparison with inspected material and recoverable prior claims rather than a proof of absolute literature uniqueness. Independent mathematical audit has not been performed.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS 2010, publicly deposited 15 October 2010. https://mural.maynoothuniversity.ie/id/eprint/2195/
2. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, preprint (2012), https://mural.maynoothuniversity.ie/id/eprint/3761/
