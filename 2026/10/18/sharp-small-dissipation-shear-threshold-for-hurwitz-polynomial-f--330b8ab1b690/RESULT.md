# Sharp small-dissipation shear threshold for Hurwitz polynomial flows with periodic orbits

## Finding

In the Castañeda–Rebollo-Perdomo polynomial vector-field family, write the angular-shear parameter as \(e=\kappa\mu\), with \(\kappa>0\) and \(\mu>0\). There is a real-analytic critical function \(\kappa_*(\mu)\), defined for sufficiently small \(\mu\geq0\), such that, uniformly for \(\kappa\) in a fixed open interval about \(\kappa_0\), the Jacobian is Hurwitz at **every** point of \(\mathbb R^3\) precisely when \(\kappa>\kappa_*(\mu)\). Its first two terms are
\[
\kappa_*(\mu)=\underbrace{\frac{5000-400\sqrt{62}}{21}}_{\kappa_0=88.1141357331\ldots}
+\underbrace{\left(-\frac{64250000}{13671}+\frac{39430000\sqrt{62}}{60543}\right)}_{\kappa_1=428.3966137550\ldots}\mu+O(\mu^2).
\]
At equality, the Jacobian has a purely imaginary conjugate eigenvalue pair on **exactly one rotational circle**; at all other points it is Hurwitz. For each fixed \(\kappa>\kappa_0\), the Jacobian is everywhere Hurwitz for all sufficiently small positive \(\mu\); for each fixed \(0<\kappa\le\kappa_0\), it is not. The family simultaneously retains its saddle and attracting \(2\pi\)-periodic circles for these small parameter values. Hence the sharp low-dissipation shear boundary for the established periodic-orbit counterexample is computed to first correction order, not merely exhibited at one parameter pair.

## Assumptions and scope

Let \(u=x^2+y^2\geq0\) and
\[
S(u,z)=(u-5)(20/21-u)-400z^2/21,\qquad
\Omega(u,z)=1+e(z+u/10).
\]
On \(\mathbb R^3\), consider
\[
\dot x=\mu xS(u,z)-\Omega(u,z)y,\quad
\dot y=\mu yS(u,z)+\Omega(u,z)x,\quad
\dot z=-z-u/10,
\]
with \(\mu>0\) and \(e=\kappa\mu>0\). A real matrix is *Hurwitz* when all its complex eigenvalues have negative real parts. The requirement is pointwise for the Cartesian Jacobian, over all \((x,y,z)\in\mathbb R^3\), not merely on invariant sets. The smallness bound for \(\mu\) can depend on a fixed compact interval of positive \(\kappa\)'s. The main exact iff holds within one such interval containing \(\kappa_0\); no global-in-parameters diagram is asserted.

## Proof

**1. Exact cubic test.** Rotational equivariance conjugates Jacobians along circular orbits, so put \(y=0\) and retain \(u=x^2\geq0\). Let
\[
\begin{aligned}
f_1&=126u^2-160uz-500u+800z^2+200,\\
f_2&=21u^2-75u+80z^2+20,\\
f_3&=21u^2-125u+400z^2+100,\\
f_4&=21u^2-32uz-75u+80z^2+20,\\
g&=10+e(u+10z),\\
A&=6(u-125/63)^2+(800/21)z^2-18650/1323.
\end{aligned}
\]
Direct differentiation gives the characteristic polynomial \(\lambda^3+c_2\lambda^2+c_1\lambda+c_0\), with
\[
\begin{aligned}
c_2&=1+\mu A,\\
c_1&=g(g+2eu)/100+\mu f_1/21+5\mu^2f_2f_3/441,\\
c_0&=g^2/100+5\mu^2f_3f_4/441.
\end{aligned}
\]
By the cubic Routh–Hurwitz criterion, the necessary and sufficient inequalities are \(c_2>0\), \(c_0>0\), and \(d:=c_2c_1-c_0>0\). Since \(A\geq-18650/1323\), the first holds for all \(0<\mu<1323/18650\). For \(u^2+z^2\) large, both \(f_3\) and \(f_4\) are positive: their quadratic homogeneous parts are \(21u^2+400z^2\) and \(21u^2-32uz+80z^2\), both positive definite. Thus \(c_0>0\) there, for any \(\mu>0\). On the complementary compact set \(g\to10\) uniformly as \(\mu\downarrow0\), with \(\kappa\) bounded, so \(c_0>0\) globally for sufficiently small \(\mu\).

**2. Exact leading shear obstruction.** Substitution \(e=\kappa\mu\) and polynomial collection yield
\[
\frac d\mu=H_{\mu,\kappa}(u,z)=P_1(u,z;\kappa)+\mu P_2(u,z;\kappa)+\mu^2P_3(u,z;\kappa),
\]
where the leading coefficient has the exact completed-square form
\[
P_1=\frac{1600(z-u/20)^2+248(u-u_0)^2}{21}+\frac{(\kappa-\kappa_0)u}{5},\quad
u_0=\frac{10}{\sqrt{62}},\quad\kappa_0=\frac{5000-400\sqrt{62}}{21}.
\]
For \(\kappa=\kappa_0\), this is nonnegative on \(u\geq0\) with one zero \((u_0,z_0)=(10/\sqrt{62},1/(2\sqrt{62}))\), and its Hessian there is positive definite. For fixed \(\kappa>\kappa_0\), \(P_1\) is strictly positive, while for fixed \(\kappa<\kappa_0\), \(P_1(u_0,z_0)<0\).

**3. No minimizing points escape to infinity.** Write \(s=(u^2+z^2)^{1/2}\), \(v=(u,z)/s\), and \(t=\mu s^2\). The leading homogeneous forms of \(P_1,P_2,P_3\) have degrees two, four, and six and are respectively
\[
\begin{aligned}
B_1(u,z)&=\frac{1600(z-u/20)^2+248u^2}{21},\\
B_2(u,z)&=\frac{15876u^4-16800u^3z+201600u^2z^2-64000uz^3+640000z^4}{441},\\
B_3(u,z)&=\frac{10(21u^2+80z^2)(21u^2+400z^2)(63u^2+400z^2)}{9261}.
\end{aligned}
\]
All are strictly positive for \((u,z)\ne(0,0)\). For \(B_2\), the inequalities \(16800|u^3z|\le8400(u^4+u^2z^2)\) and \(64000|uz^3|\le32000(u^2z^2+z^4)\) give
\[
441B_2\ge7476u^4+161200u^2z^2+608000z^4>0.
\]
For \(\kappa\) in any fixed compact interval, the lower-degree polynomial terms yield the *uniform* estimate, over \(t\ge0\),
\[
\frac{H_{\mu,\kappa}(u,z)}{s^2(1+t+t^2)}
=\frac{B_1(v)+tB_2(v)+t^2 B_3(v)}{1+t+t^2}+O(1/s),\qquad s\to\infty.
\]
The first quotient is bounded away from zero on the unit semicircle \(v_u\ge0\), uniformly in \(t\ge0\), by positivity of all three forms. Therefore a fixed large compact cylinder contains all potential zeros/minima of \(H_{\mu,\kappa}\), uniformly for \(\mu>0\) small and \(\kappa\) near \(\kappa_0\).

**4. Sharp analytic boundary and first correction.** On that fixed compact region, the completed square and continuity make \(H\) strictly positive outside a small fixed disk about \((u_0,z_0)\) when \((\mu,\kappa)\) is close to \((0,\kappa_0)\). Inside the disk its Hessian remains positive definite; hence its sole local minimizer \((u(\mu,\kappa),z(\mu,\kappa))\) is analytic by the implicit-function theorem and is also the unique global minimizer. Its value \(m(\mu,\kappa)\) satisfies \(m(0,\kappa_0)=0\) and
\[
\partial_\kappa m(0,\kappa_0)=u_0/5>0.
\]
Another application of the implicit-function theorem yields a unique analytic \(\kappa_*(\mu)\) solving \(m(\mu,\kappa_*(\mu))=0\), with the claimed strict sign on each side. At the minimizing point, the next coefficient evaluates exactly to
\[
P_2(u_0,z_0;\kappa_0)
=-\frac{78860000}{60543}+\frac{64250000\sqrt{62}}{423801}<0.
\]
Therefore
\[
\kappa_*'(0)=-\frac{5P_2(u_0,z_0;\kappa_0)}{u_0}
=-\frac{64250000}{13671}+\frac{39430000\sqrt{62}}{60543}>0.
\]
When \(\kappa=\kappa_*(\mu)\), \(d=0\) precisely on the rotational circle \(u=u(\mu,\kappa_*)\), \(z=z(\mu,\kappa_*)\). The other two Hurwitz coefficients remain positive there. The characteristic polynomial factors as \((\lambda+c_2)(\lambda^2+c_1)\), giving one negative eigenvalue and a nonzero imaginary conjugate pair; hence strict Hurwitz fails exactly on that circle. The fixed-\(\kappa\) statements follow from the leading sign, and the negative \(P_2\) at \(\kappa=\kappa_0\).

**5. Coexisting periodic dynamics.** In \(u>0\), \(\dot u=2\mu uS(u,z)\), \(\dot z=-z-u/10\), and \(\dot\theta=\Omega\). At \((u,z)=(1,-1/10)\) and \((4,-2/5)\), \(S=0\) and \(\Omega=1\), so the circles persist for all positive parameters and have period \(2\pi\). For sufficiently small \(\mu>0\), direct linearization of the \((u,z)\) subsystem gives a saddle at the first and a sink at the second, independently of \(e\). The previously established absence of additional cycles for small \(\mu\) is not needed for the new sharp-Hurwitz claim.

## Verification

The accompanying `VERIFY.py` reconstructs the Cartesian Jacobian and its characteristic polynomial independently from the vector field, proves the coefficient identities symbolically, checks all three leading homogeneous forms, checks the exact completed square, and verifies the first threshold correction in \(\mathbb Q(\sqrt{62})\). These exact symbolic tests support the coefficient algebra. They are not substitutes for the global degree estimates, convexity, or analytic implicit-function arguments given above.

## Relationship to prior work

Castañeda and Rebollo-Perdomo (arXiv:2610.09176v1, October 6, 2026) introduce this precise polynomial family, prove the existence and type of both periodic circles, give the characteristic coefficients and cubic Hurwitz inequalities, and verify one point \((\mu,e)=(1/1000,1/10)\) plus an unspecified open neighborhood. Those constructions and coefficient formulas are not claimed as novel. The finding here is the sharp **asymptotic shear-to-dissipation boundary**, its first correction, and the unique circle of imaginary spectrum at equality. The source does not formulate these thresholds or solve the associated global polynomial minimization as \(\mu\downarrow0\).

## Limitations

The theorem gives a local parameter-boundary germ as \(\mu\downarrow0\), not a complete Hurwitz region at finite \(\mu\). It does not give a numerical uniform \(\mu\)-radius, does not show stability of the flow's origin is global, and does not claim any new periodic orbit or any changed basin structure. Independent external scientific validation and full bibliographic priority checking remain outstanding.

## References

1. Á. Castañeda and S. Rebollo-Perdomo, *A family of Hurwitz polynomial vector fields in \(\mathbb R^3\) having non-constant periodic orbits*, arXiv:2610.09176v1 (first public posting 2026-10-06), https://arxiv.org/html/2610.09176v1.
2. E. Routh and A. Hurwitz, the classical cubic polynomial stability criterion, as used in reference 1, Section 2.
