# Sharp factorization and positivity rigidity for coprime-tree monomial-pole kernels

## Finding
For every integer \(r\ge1\), define the rational potential
\[
 H_r(x,y)=\frac{xy}{(1-x^r)(1-y^r)},\qquad
 K_r(x,y)=H_r(x,y)-H_r(x,xy)-H_r(xy,y).
\]
Set \(S_r(t)=1+t+\cdots+t^{r-1}\) and \(V_r(t)=t+t^2+\cdots+t^{r-1}\), with \(V_1=0\). Then
\[
 K_r(x,y)=\frac{xy\bigl(1-V_r(x)V_r(y)\bigr)}
 {(1-xy)S_r(x)S_r(y)S_r(xy)}. \tag{1}
\]
The following two conclusions hold simultaneously.

**Exact factorization rigidity.** The rational function \(K_r(x,y)\) is a product \(F(x)G(y)J(xy)\) of three rational functions over \(\mathbb C\) if and only if \(r\in\{1,2\}\). The two positive factorizations are
\[
 K_1(x,y)=\frac{xy}{1-xy},\qquad
 K_2(x,y)=\frac{xy}{(1+x)(1+y)(1+xy)}.
\]

**Sharp positivity boundary.** If \(r\ge3\), there is a unique \(\tau_r\in(0,1)\) satisfying \(V_r(\tau_r)=1\). For real \(0<q<1\), all the terms \(K_r(q^a,q^b)\) with coprime positive \(a,b\) are nonnegative **exactly** when \(q\le\tau_r\). At equality, precisely the root term \((a,b)=(1,1)\) is zero; above that threshold it is negative. The \(\tau_r\) decrease strictly to \(1/2\), with \(\tau_3=(\sqrt5-1)/2\). For \(r=1,2\) all terms are strictly positive throughout \(0<q<1\).

For every \(r\ge1\) and \(|q|<1\), telescoping also yields the absolutely convergent identity
\[
 \sum_{\substack{a,b\ge1\\\gcd(a,b)=1}} K_r(q^a,q^b)=\frac{q^2}{(1-q^r)^2}. \tag{2}
\]
The general telescoping mechanism and the two special instances \(r=1,2\) are already present in the literature; the all-\(r\) rigidity and sharp positivity boundary are the claims here.

## Assumptions and scope
The integer parameter is \(r\ge1\). All rational identities are in \(\mathbb C(x,y)\). Factorization means **exactly** a product of three one-variable rational functions with arguments \(x\), \(y\), and \(xy\); no assertion about arbitrary multivariate factorization or linear combinations is made. Positivity concerns real \(0<q<1\). Ordered coprime pairs are used, so the root \((1,1)\) occurs once.

## Proof
Subtract the three potentials over a common denominator. The numerator after removing its factor \(xy\) is
\[
 1-x-y+xy^r+x^ry-x^ry^r
 =(1-x)(1-y)-(x-x^r)(y-y^r).
\]
Since \(x-x^r=(1-x)V_r(x)\) and \(1-x^r=(1-x)S_r(x)\), cancellation gives (1). In particular \(V_1=0\), while \(V_2(t)=t\) and the factor \(1-xy\) cancels; this proves the two displayed factorizations.

Suppose \(r\ge3\) and put \(N_r(x,y)=1-V_r(x)V_r(y)\). This polynomial is nonconstant and coprime to the factors in the denominator of (1). We show that no irreducible factor of \(N_r\) is of the three forms \(x-c\), \(y-c\), or \(xy-c\), for any \(c\in\mathbb C\). Indeed \(N_r(c,0)=N_r(0,c)=1\), excluding the first two forms and \(xy\). When \(c\ne0\), substitute \(y=c/x\): the Laurent polynomial \(N_r(x,c/x)\) has coefficient \(-c\) at its highest positive power \(x^{r-2}\), contributed uniquely by \(x^{r-1}y\). Thus it cannot vanish identically and \(xy-c\) is not a factor. A product \(F(x)G(y)J(xy)\) of rational functions, when reduced over \(\mathbb C[x,y]\), has irreducible numerator and denominator factors only from these three forms, because univariate polynomials split over \(\mathbb C\). Equation (1) therefore cannot admit such a product factorization when \(r\ge3\). This proves the if-and-only-if claim.

For \(0<x,y<1\), every factor of the denominator of (1) is positive, so the sign of \(K_r\) is the sign of \(1-V_r(x)V_r(y)\). For \(r\ge3\), \(V_r\) is strictly increasing on \((0,1)\), so for \(x=q^a\), \(y=q^b\) one has \(V_r(x)V_r(y)\le V_r(q)^2\), with equality only when \(a=b=1\). For \(r\ge3\), \(V_r(0)=0\) and \(\lim_{t\uparrow1}V_r(t)=r-1>1\), so a unique \(\tau_r\) satisfies \(V_r(\tau_r)=1\). The preceding inequality proves nonnegativity for \(q\le\tau_r\). If \(q>\tau_r\), the \((1,1)\) term is negative; at equality it is zero and all other terms are positive. For \(r=1\), \(V_1=0\), and for \(r=2\), \(V_2(q)=q<1\), proving strict positivity.

For each \(0<t<1\), \(V_{r+1}(t)>V_r(t)\), so the thresholds decrease strictly. Also \(V_r(1/2)<\sum_{j\ge1}2^{-j}=1\), hence \(\tau_r>1/2\). As \(r\to\infty\), \(V_r(t)\to t/(1-t)>1\) for every fixed \(t>1/2\), so \(\tau_r\downarrow1/2\). Solving \(t+t^2=1\) gives \(\tau_3=(\sqrt5-1)/2\).

Finally the directed Calkin--Wilf tree enumerates each ordered positive coprime pair exactly once, with root \((1,1)\) and children \((a,a+b)\), \((a+b,b)\). The identity defining \(K_r\) telescopes over its vertices. For \(|q|=\rho<1\), there is a constant \(C_{r,\rho}\) such that \(|H_r(q^a,q^b)|\le C_{r,\rho}\rho^{a+b}\). Since \(\sum_{a,b\ge1}\rho^{a+b}<\infty\), the total boundary mass on successive disjoint levels tends to zero. The sum is therefore \(H_r(q,q)=q^2/(1-q^r)^2\), establishing (2). Absolute convergence of the \(K_r\) sum follows from its defining three-term expression and the same bound.

## Verification
A separate exact-rational checker (`verify.py`) verifies formula (1) against direct differences of potentials for \(r=1,\ldots,20\) at multiple rational arguments; checks the two stated products and selected signs across the sharp thresholds; and confirms the coefficient obstruction for \(r=3,\ldots,20\). These are finite consistency checks. The proof above, rather than the checks, establishes every assertion for all \(r\).

Run `python3 verify.py` with Python 3 and no third-party packages.

## Relationship to prior work
Kalinin (2026, arXiv:2610.26949), Sections 2 and 4, explicitly gives the \(r=2\) factorized kernel, its primitive-pair evaluation, and the \(r=1\) visible-lattice identity; Sections 1 and 2 identify rational-potential factorization as an open classification direction. Hata (1995), Theorem 6.1, supplies the general Farey-tree telescoping principle. That general principle implies the summed identity (2) once the family of potentials is chosen, so (2) is not presented as a novel evaluation. Neither inspected discussion states the complete rigidity theorem in this monomial-pole family or its exact positivity transition. No assertion of exhaustive priority verification is made.

## Limitations
The factorization classification covers only the specifically defined monomial-pole family, not every rational potential. Nonfactorability is with respect to a **single product** of rational functions of \(x\), \(y\), and \(xy\); it does not exclude sums of such products. Positivity is asserted only for real \(0<q<1\). The source paper's broader classification and dimension problem remain open. Priority risk remains for any unindexed earlier computation of this natural family.

## References
- N. Kalinin, *Lucas recurrences and Lambert series in coprime double sums* (2026), arXiv:2610.26949, first posted 18 October 2026. https://arxiv.org/abs/2610.26949
- M. Hata, *Farey fractions and sums over coprime pairs*, Acta Arith. **70** (1995), 149–159, DOI:10.4064/aa-70-2-149-159.
