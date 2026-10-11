# Exact weight optimization for geometric cyclic shifts and the dimension-three gain

## Finding

For integers \(n\ge2\), real \(a>1\) and \(r\ge1\), let the invertible weighted cyclic shift on \(\mathbb C^n\) be
\[
T_{n,a}e_j=a^j e_{j-1\pmod n},\qquad j=0,1,\ldots,n-1.
\]
Write \(w(S)=\max_{\|x\|=1}|\langle Sx,x\rangle|\) for the numerical radius. For \(\theta\in[0,1]\), consider the weighted upper-bound functional introduced in [1],
\[
\Phi_{n,a,r}(\theta)=\frac14\big\||T_{n,a}|^{4r\theta}+|T_{n,a}^*|^{4r(1-\theta)}\big\|
 +\frac12 w\!\left(|T_{n,a}|^{2r\theta}|T_{n,a}^*|^{2r(1-\theta)}\right).
\]
Its established operator inequality is \(w(T_{n,a})^{2r}\le\Phi_{n,a,r}(\theta)\). This finding determines the *unique optimizing weight*, uniformly for all dimensions, geometric ratios and exponents. It optimizes this upper-bound functional, **not** the numerical radius itself.

Define five positive scalar functions on \([0,1]\):
\[
\begin{aligned}
U(\theta)&=a^{4r(n-2)\theta},&
V(\theta)&=a^{4r(n-1)(1-\theta)},\\
Z(\theta)&=a^{4r(n-1)\theta},&
P(\theta)&=a^{2r(n-1-\theta)},&
Q(\theta)&=a^{2r(n-1)\theta}.
\end{aligned}
\]
The exact functional is
\[
\boxed{\Phi_{n,a,r}(\theta)=\tfrac14\max\{U(\theta)+V(\theta),Z(\theta)+1\}
+\tfrac12\max\{P(\theta),Q(\theta)\}.}
\]
For \(n=2\), its unique minimizer is \(\theta_*=1/2\), and the minimum is \((1+a^r)^2/4\). For \(n\ge3\), let \(\tau\) be the unique solution in \((1/2,(n-1)/n)\) of
\[
U(\tau)+V(\tau)=Z(\tau)+1,
\]
and let \(G(\theta)=(n-2)U(\theta)-(n-1)V(\theta)-P(\theta)\). The global optimizer has the exact classification
\[
\boxed{\theta_*=
\begin{cases}
\tau,&G(\tau)\le0,\\
\text{the unique root of }G(\theta)=0\text{ in }(1/2,\tau),&G(\tau)>0.
\end{cases}}
\]
In both cases \(1/2<\theta_*<(n-1)/n\) and \(\Phi_{n,a,r}(\theta_*)<\Phi_{n,a,r}(1/2)\). Thus dimension three is the exact onset of a strict gain over the symmetric parameter in this natural class.

Both regimes in the formula genuinely occur: for every \(a>1\), \(r\ge1\), the three-dimensional minimizer is the nonsmooth crossing \(\tau\); for \(n=10\), \(a=6/5\), \(r=1\), the minimizer is the smooth root of \(G\). For \(n=3\), the number \(h=a^{4r\tau}>1\) is the unique positive root of
\[
 h^4-h^3+h^2-a^{8r}=0,
\]
and the sharp optimized *upper bound* is
\[
\boxed{\min_{0\le\theta\le1}\Phi_{3,a,r}(\theta)=\frac{1+h^2}{4}+\frac{a^{4r}}{2\sqrt h}.}
\]
For \(a=2,r=1\), this is approximately \(8.571894478999\), strictly below the symmetric value \(9\). The optimal parameter is approximately \(0.518032178392\).

## Assumptions and scope

All Hilbert spaces and matrices here are complex and finite dimensional. The shift uses the orthonormal basis \(e_0,\ldots,e_{n-1}\), with indices reduced modulo \(n\). The coefficient \(a\) is strictly greater than one, so the shift and both positive moduli are invertible. The exponent \(r\) is any real number at least one, as required for the bound in [1]. Only \(\theta\in[0,1]\) is optimized. The theorem does not claim that the optimized expression equals the numerical radius.

## Proof

**Step 1: exact diagonal reduction.** Because \(T_{n,a}\) is monomial, direct multiplication gives
\[
 |T_{n,a}|e_j=a^je_j,\qquad |T_{n,a}^*|e_j=a^{j+1\pmod n}e_j.
\]
The two moduli commute. Consequently the positive diagonal-sum norm equals the largest diagonal entry and the numerical radius of their positive diagonal product equals its largest diagonal entry. For \(0\le j\le n-2\), these entries are respectively
\[
 a^{4rj\theta}+a^{4r(j+1)(1-\theta)},\qquad
 a^{2r(j+1-\theta)}.
\]
Each sequence is nondecreasing in \(j\), strictly unless a boundary exponent vanishes. The remaining wraparound entry at \(j=n-1\) is
\[
 a^{4r(n-1)\theta}+1,\qquad a^{2r(n-1)\theta}.
\]
Taking the two maxima proves the claimed exact formula, with no approximation.

**Step 2: the two-dimensional boundary.** For \(n=2\), the formula simplifies to
\[
\Phi_{2,a,r}(\theta)=\frac{1+a^{4r m}}4+\frac{a^{2r m}}2,
\quad m=\max\{\theta,1-\theta\}.
\]
It is strictly increasing with \(m\), which is uniquely minimized at \(\theta=1/2\); substitution gives \((1+a^r)^2/4\).

**Step 3: unique crossing for higher dimensions.** Suppose \(n\ge3\). Put
\[
 F(\theta)=U(\theta)+V(\theta)-Z(\theta)-1,
\qquad k=4r\log a>0.
\]
Then
\[
 F'(\theta)=k\big((n-2)U(\theta)-(n-1)V(\theta)-(n-1)Z(\theta)\big)<0.
\]
Indeed \(Z\ge U\) on \([0,1]\) and \(V>0\). At \(\theta=1/2\),
\[
F(1/2)=a^{2r(n-2)}-1>0.
\]
At \(\theta=(n-1)/n\), set \(b=a^{4r(n-1)/n}>1\); then
\[
F((n-1)/n)=b^{n-2}+b-b^{n-1}-1=-(b-1)(b^{n-2}-1)<0.
\]
Hence exactly one crossing \(\tau\in(1/2,(n-1)/n)\) exists.

**Step 4: optimization on both sides of the crossing.** The inequality \(P(\theta)\ge Q(\theta)\) is equivalent to \(\theta\le(n-1)/n\). Thus on \([0,\tau]\), the exact formula reduces to \(\Phi=(U+V)/4+P/2\), and
\[
\Phi'(\theta)=\frac{k}{4}G(\theta),\qquad
G'(\theta)=k\left((n-2)^2U(\theta)+(n-1)^2V(\theta)+\tfrac12P(\theta)\right)>0.
\]
Also \(G(1/2)<0\), because \(U(1/2)<V(1/2)\). It follows that the restriction to \([0,\tau]\) is either strictly decreasing, with minimum \(\tau\) when \(G(\tau)\le0\), or decreases then increases across the unique interior zero of \(G\) when \(G(\tau)>0\).

For \(\tau\le\theta\le(n-1)/n\), the active branches are \(Z+1\) and \(P\). Their sum has derivative
\[
\Phi'(\theta)=\frac{k}{4}\big((n-1)Z(\theta)-P(\theta)\big)>0,
\]
since \(Z(\theta)>P(\theta)\) whenever \(\theta\ge1/2\): their base-\(a\) exponents differ by \(2r((2n-1)\theta-(n-1))>0\). For \(\theta\ge(n-1)/n\), both active terms \(Z+1\) and \(Q\) increase strictly. Thus no later point can minimize. We have proved the global classification and uniqueness. Because \(G(1/2)<0\) and \(\tau>1/2\), a small increase above \(1/2\) strictly lowers \(\Phi\). This proves the strict dimension-three onset for all \(n\ge3\), all \(a>1\), and all \(r\ge1\).

**Step 5: both regimes, including an exact nontrivial smooth example.** When \(n=3\), the crossing satisfies \(\tau<2/3\), and \(V(\tau)>U(\tau)\), because \(2(1-\tau)>\tau\). Therefore \(G(\tau)=U(\tau)-2V(\tau)-P(\tau)<0\), forcing the crossing optimizer. With \(h=a^{4r\tau}\), the crossing identity becomes \(h+h^{-2}a^{8r}=h^2+1\). Multiplication by \(h^2\) gives the quartic. Its positive root is unique since the derivative of \(h^4-h^3+h^2\) equals \(h(4h^2-3h+2)>0\) for \(h>0\). Evaluating the active expression at \(\tau\) yields the announced formula.

For \(n=10\), \(a=6/5\), \(r=1\), use \(\theta_0=11/20\) and let \(y=(6/5)^{1/10}\). Then
\[
F(\theta_0)=y^{176}+y^{162}-y^{198}-1,
\qquad G(\theta_0)=y^{162}(y^7+1)(8y^7-9).
\]
The exact rational comparisons
\[
\left(\frac{10183}{10000}\right)^{10}<\frac65<\left(\frac{10185}{10000}\right)^{10},\qquad
\left(\frac{10183}{10000}\right)^{176}+\left(\frac{10183}{10000}\right)^{162}-\left(\frac{10185}{10000}\right)^{198}-1>0,
\]
and \((6/5)^7>(9/8)^{10}\) prove \(F(\theta_0)>0\) and \(G(\theta_0)>0\). Since \(F\) decreases and vanishes at \(\tau\), \(\theta_0<\tau\); since \(G\) increases, \(G(\tau)>0\). Hence the smooth-root regime really occurs, and both types in the classification are necessary.

## Verification

A standalone Python standard-library checker in `verify_geometric_cycle.py` reconstructs the diagonal entries from the monomial shift, checks the full scalar reduction at selected dimensions and weights, brackets the crossing and smooth-root cases numerically, and verifies the three rational inequalities in the exact smooth-regime certificate using integer arithmetic. Its finite tests are consistency checks only. The global dimension and parameter assertions are proved analytically above; no finite sample is used as an infinite proof.

## Relationship to prior work

Mondal, Mohapatra and Dewage [1, Theorem 2.1 and Proposition 2.5, also Proposition 5.20] introduced this weighted numerical-radius upper bound and established existence of an optimal weight for invertible operators. Their published general theorem gives no formula for an optimizing weight on positive geometric cyclic monomial matrices, no sharp dimension threshold for improvement over the symmetric bound, and no crossing-versus-smooth optimizer classification. Their Sections 5 and 6 focus on normal operators, triangular and block examples rather than cyclic geometric shifts. The present result solves the concrete optimization problem for all geometric cycles, all dimensions and all allowed exponents; it is not an independent improvement of the parent inequality or a claim about exact numerical radii.

Chang and Wang [2] study which permutations of prescribed weights maximize the **numerical radius itself** of cyclic shifts. Chien and Nakazato [3] study numerical radii of geometric infinite unilateral shifts. These are related in operator type, but their stated objectives are mathematically different from optimizing the new parameter in [1]. Their results are not used in the proof.

## Limitations

This theorem applies only to a positive geometric progression around one invertible finite cyclic shift; it does not classify the optimizer for arbitrary nonnormal matrices or arbitrary positive weight lists. It concerns minimization of a published *upper-bound expression*, not equality in that bound. The smooth/crossing criterion is implicit through uniquely defined roots, although it is globally exact and decidable by monotonic scalar functions. The real parameters are not restricted to machine-representable values. The exact arithmetic checks certify the displayed concrete example but are not needed for the universal analytic proof. No claim is made about journal peer review or independent verification.

## References

[1] S. Mondal, R. N. Mohapatra and K. T. Dewage, *Refined upper bounds for the numerical radius via weighted operator means*, arXiv:2602.04134v1 (first public 4 February 2026), revised v2 (4 September 2026), especially Theorem 2.1, Proposition 2.5, Proposition 5.20 and Sections 5--6. https://arxiv.org/html/2602.04134v2

[2] C.-T. Chang and K.-Z. Wang, *Maximizing numerical radii of weighted shifts under weight permutations*, Journal of Mathematical Analysis and Applications **394** (2012), 592--602. DOI:10.1016/j.jmaa.2012.04.039.

[3] M.-T. Chien and H. Nakazato, *The numerical radius of a weighted shift operator with geometric weights*, Electronic Journal of Linear Algebra **18** (2009), DOI:10.13001/1081-3810.1293.
