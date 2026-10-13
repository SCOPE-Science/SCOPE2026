# Sharp power stop-loss transition for the unit Shiha distribution

## Finding
Fix \(\omega>0\), \(0<\eta_1<\eta_2\), and \(r>0\). Let \(X_i\) have the unit Shiha law \(\operatorname{USh}(\omega,\eta_i)\) defined below, and let \(Z_i=X_i^r\). Then the **complete increasing-convex (stop-loss) ordering phase diagram** is
\[
Z_2\le_{\mathrm{icx}}Z_1\quad\Longleftrightarrow\quad r\ge 2\omega.
\]
For \(0<r<2\omega\), the two laws are incomparable in increasing-convex order: their stop-loss premiums reverse their ordering at exactly one *positive deductible* \(d_{\omega,r}\in(0,u_*^{r/\omega})\). This deductible is independent of both \(\eta_1\) and \(\eta_2\). For \(r\ge2\omega\) the stop-loss comparison is strict for every deductible in \((0,1)\).

At the sharp boundary \(r=2\omega\), the two transformed laws have equal mean and a strict convex ordering:
\[
Z_2\le_{\mathrm{cx}}Z_1,\qquad
\mathbb E Z_i=\frac13,\qquad
\operatorname{Var}(Z_i)=\frac{4+10q_i}{45(1+3q_i)},\quad q_i=\frac{\eta_i}{\omega}.
\]
In particular the sharp variance envelope over \(\eta>0\) is \((2/27,4/45)\); the endpoint ratio is \(5/6\). Neither endpoint is attained for finite strictly positive \(\eta\).

For all these comparisons, the original cumulative distributions cross exactly once, at \(x_*=u_*^{1/\omega}\), where \(u_*=0.5768340041423086893\ldots\) is the unique interior root of
\[
u(3-4\log u)=3.
\]
The associated **parameter-independent quantile rank** is \(p_*=u_*\): every \(\operatorname{USh}(\omega,\eta)\) distribution has \(p_*\)-quantile \(x_*\). For the powered laws the cumulative-distribution crossing is \(u_*^{r/\omega}\).

## Assumptions and scope
All variables take values in \((0,1)\). For \(\omega>0\) and \(\eta>0\), the unit Shiha CDF is the one in Shiha (2026, equation (2.6)):
\[
F_{\omega,\eta}(x)=\frac{\omega x^\omega+\eta x^{2\omega}(3-4\omega\log x)}{\omega+3\eta},\qquad0<x<1.
\]
Write \(q=\eta/\omega\) and \(U=X^\omega\). Its CDF and density are
\[
H_q(u)=\frac{u+q u^2(3-4\log u)}{1+3q},\qquad
h_q(u)=\frac{1+q u(2-8\log u)}{1+3q},\quad0<u<1.
\]
The density is positive, integrates to one, and the source parameter range ensures \(q>0\). The formulas extend continuously to \(q=0\) and to the weak limit \(q\to\infty\); only finite positive parameters enter the stated order theorem. The notation \(A\le_{\mathrm{icx}}B\) means \(\mathbb E\varphi(A)\le\mathbb E\varphi(B)\) for every finite increasing convex function on the unit interval; \(\le_{\mathrm{cx}}\) removes the increasing requirement.

## Proof
**1. Universal single crossing.** For \(q_2>q_1\), set \(k=(q_2-q_1)/[(1+3q_1)(1+3q_2)]>0\). Direct subtraction gives
\[
H_{q_2}(u)-H_{q_1}(u)=k u\,[u(3-4\log u)-3].
\]
For \(g(u)=u(3-4\log u)-3\), we have \(g'(u)=-1-4\log u\), \(g''(u)=-4/u<0\), \(g(0+)=-3\), \(g(e^{-1/4})=4e^{-1/4}-3>0\), and \(g(1)=0\). Therefore \(g\) has exactly one zero \(u_*\) in \((0,e^{-1/4})\), with negative sign below and positive sign above it. The other zero at \(u=1\) is the endpoint. At \(u_*\), the defining identity gives \(H_q(u_*)=u_*\) for every \(q\), yielding both the exact quantile pivot and the powered CDF crossing.

**2. All positive power moments.** For \(s>0\), put \(z=s/\omega>0\). Integrating \(u^z h_q(u)\) gives
\[
\mathbb E[X^s]=\frac{1}{1+3q}\left[\frac1{z+1}+q\left(\frac2{z+2}+\frac8{(z+2)^2}\right)\right].
\]
Consequently
\[
\mathbb E[X_2^s]-\mathbb E[X_1^s]
=k\frac{z(2-z)}{(1+z)(2+z)^2}.
\]
This is positive when \(s<2\omega\), zero exactly when \(s=2\omega\), and negative when \(s>2\omega\). In particular the mean difference of \(Z_2\) and \(Z_1\) has the sign of \(2\omega-r\).

**3. Exact stop-loss sign classification.** For a bounded nonnegative variable \(Z\), \(\mathbb E(Z-d)_+=\int_d^1[1-F_Z(t)]\,dt\) for \(0\le d\le1\). Set \(a=\omega/r\), \(\xi=u_*^{r/\omega}\), and
\[
B(d)=\mathbb E(Z_2-d)_+-\mathbb E(Z_1-d)_+.
\]
Using the difference from Step 1,
\[
B(d)=-k\!\int_d^1\!\left[t^{2a}(3-4a\log t)-3t^a\right]dt=-kJ_a(d),
\]
where, for \(0<d<1\), the exact elementary antiderivative is
\[
J_a(d)=\left(\frac3{2a+1}+\frac{4a}{(2a+1)^2}\right)(1-d^{2a+1})
+\frac{4a}{2a+1}d^{2a+1}\log d
-\frac3{a+1}(1-d^{a+1}).
\]
The limiting formula defines \(J_a(0)\). From Step 1, \(B'(d)<0\) on \((0,\xi)\), and \(B'(d)>0\) on \((\xi,1)\). Moreover \(B(\xi)<0\), \(B(1)=0\), and \(B(0)\) has the sign of \(2\omega-r\) by Step 2.

If \(r\ge2\omega\), then \(B(0)\le0\), hence \(B(d)<0\) for every \(0<d<1\). For \(d<0\) the stop-loss difference equals the mean difference, and for \(d\ge1\) it is zero. The stop-loss characterization of increasing-convex order proves \(Z_2\le_{\mathrm{icx}}Z_1\). If \(0<r<2\omega\), then \(B(0)>0>B(\xi)\). Strict decrease on \((0,\xi)\) gives exactly one root \(d_{\omega,r}\in(0,\xi)\), with \(B(d)>0\) below this root and \(B(d)<0\) above it up to one. Since \(k\) is a positive multiplicative factor, this root is independent of \(q_1,q_2\); equivalently it is the unique root of \(J_{\omega/r}(d)=0\) in that interval. Neither direction of increasing-convex comparison can then hold. The reverse increasing-convex order is also impossible in the supercritical case because \(B(d)<0\) near one.

**4. Exact convex-order boundary and variance.** Convex-order comparability requires equality of means. Step 2 shows this occurs only at \(r=2\omega\), when Step 3 supplies the required stop-loss inequalities. At this power, the first two moments are
\[
\mathbb E[X^{2\omega}]=\frac13,\qquad
\mathbb E[X^{4\omega}]=\frac{1/5+5q/9}{1+3q}.
\]
Subtracting the squared mean yields \(\operatorname{Var}(X^{2\omega})=(4+10q)/[45(1+3q)]\). It decreases strictly with \(q>0\) and has the endpoint limits stated above. This completes the classification. \(\square\)

## Verification
The standalone file `check_unit_shiha_order.py` runs with the Python standard library. In the recorded run it passed 1,850 checks, including exact rational power-moment identities, the common quantile-pivot identity, independent Simpson quadrature against the stop-loss antiderivative, numerical deductible sign tests across several power regimes, and exact rational variance identities. For illustration, \(\omega=r=1\) gives \(d_{\omega,r}=0.315037545734950\ldots\), strictly below the CDF pivot \(0.576834004142308\ldots\). The analytic proof, rather than these finite tests, establishes all parameter and deductible quantifiers.

## Relationship to prior work
Shiha's unit-distribution paper (arXiv:2602.04400v1, 4 February 2026; journal version DOI:10.1155/ijmm/4454027) supplies the exact CDF, raw moments, and stress-strength reliability of the model. Its quantile table and discussion already observe a reversal near rank \(0.57\) as \(\eta\) increases. Its earlier positive-lifetime antecedent (arXiv:2602.02875v1, 2 February 2026) similarly describes a qualitative quantile reversal near rank \(0.43\) for the lifetime variable. These source formulas and qualitative reversals are not new contributions here. The distinct result proved here is the full necessary-and-sufficient increasing-convex ordering classification under arbitrary positive power transformations, the unique universal stop-loss reversal below its sharp boundary, and the strict convex-order chain at that boundary. General stop-loss characterizations are classical and are not claimed as new.

## Limitations
The comparison holds at **fixed** \(\omega\) while \(\eta\) varies; it does not classify joint changes in both parameters, arbitrary monotone transformations, or multivariate dependence. The zero- and infinite-\(\eta\) cases are limiting envelopes, not members of the strictly positive finite-parameter family. The source literature provides the distribution formulas and empirical qualitative hints; a previously unindexed equivalent order theorem cannot be excluded by searches alone.

## References
1. F. A. Shiha, *Unit Shiha Distribution and its Applications to Engineering and Medical Data*, arXiv:2602.04400v1 (first public posting 2026-02-04), https://arxiv.org/abs/2602.04400.
2. F. A. Shiha, *Shiha Distribution: Statistical Properties and Applications to Reliability Engineering and Environmental Data*, arXiv:2602.02875v1 (first public posting 2026-02-02), https://arxiv.org/abs/2602.02875.
3. F. A. Shiha, *Unit Shiha Distribution and Its Applications to Engineering and Medical Data*, International Journal of Mathematics and Mathematical Sciences (2026), DOI:10.1155/ijmm/4454027 (later journal version; not the earliest public date).
4. M. Shaked and J. G. Shanthikumar, *Stochastic Orders*, Springer, 2007, DOI:10.1007/978-0-387-34675-5 (general stop-loss and convex-order theory).
