# Exact equilibrium-stability partition for the Muñoz-Pacheco one-parameter flow

## Finding
Consider the one-parameter system
\[
D^q x=yz+x(y-a),\qquad D^q y=1-|x|,\qquad D^q z=-xy-z.
\]
The source introduces this system and states in its mechanism discussion that all four equilibria are unstable when \(a<1/4\). On the ordinary-flow slice \(q=1\), that statement fails on an entire open parameter interval.

For \(a\le 1/4\), put
\[
r_\pm=\frac{1\pm\sqrt{1-4a}}2.
\]
For each root \(r\), there are two equilibria,
\[
(1,r,-r),\qquad (-1,r,r).
\]
Their characteristic polynomial is independent of the sign of the first coordinate and is
\[
p_r(\lambda)=\lambda^3+(1-r^2)\lambda^2+(1-r)\lambda+(1-2r).
\]
The complete ordinary-flow classification is:

- If \(a<0\), the \(r_+\) pair has exactly one eigenvalue in the open right half-plane, while the \(r_-\) pair has exactly two.
- If \(a=0\), the \(r_+\) pair still has exactly one open-right-half-plane eigenvalue, while the \(r_-\) pair has eigenvalues \(-1,\pm i\).
- If \(0<a<1/4\), the \(r_-\) pair is asymptotically stable and the \(r_+\) pair has exactly one open-right-half-plane eigenvalue.
- If \(a=1/4\), the two branch pairs coalesce to two equilibria with eigenvalues \(0,-3/8\pm i\sqrt{23}/8\).
- If \(a>1/4\), there are no real equilibria.

In addition, for every commensurate fractional order \(0<q\le1\), the \(r_-\) pair remains asymptotically stable throughout \(0<a<1/4\). Hence the source's blanket assertion that all four equilibria are unstable for \(a<1/4\) is false on the whole interval \(0<a<1/4\).

## Assumptions and scope
The ordinary-flow statement concerns the classical autonomous ODE obtained by setting the common fractional order to \(q=1\). The vector field is smooth in neighborhoods of all equilibria because their first coordinate is \(\pm1\), away from the nonsmooth surface \(x=0\). The fractional-order corollary uses the source's commensurate Caputo stability criterion \(|\arg\lambda|>q\pi/2\) and is restricted to \(0<q\le1\).

No claim is made here about the existence, basin, hidden/self-excited status, or global continuation of a chaotic attractor for parameters other than those numerically demonstrated in the source. In particular, the presence of two stable equilibria does not by itself classify any other attractor as hidden.

## Proof
At an equilibrium, \(|x|=1\), so write \(x=s\) with \(s\in\{-1,1\}\). From \(z=-xy\), write \(y=r\) and \(z=-sr\). The first equilibrium equation then becomes
\[
-r^2+r-a=0,
\]
so \(a=r-r^2\) and the two possible values are \(r_\pm\) above.

Near \(x=s\), the derivative of \(|x|\) is \(s\). Substituting \(a=r-r^2\), the Jacobian is
\[
J_s(r)=
\begin{pmatrix}
r^2&s(1-r)&r\\
-s&0&0\\
-r&-s&-1
\end{pmatrix}.
\]
Because \(s^2=1\), direct expansion gives
\[
\det(\lambda I-J_s(r))
=\lambda^3+(1-r^2)\lambda^2+(1-r)\lambda+(1-2r),
\]
independent of \(s\).

Write the cubic as \(\lambda^3+A\lambda^2+B\lambda+C\), where
\[
A=1-r^2,\qquad B=1-r,\qquad C=1-2r.
\]
The decisive Routh quantity factors as
\[
AB-C=r(r^2-r+1).
\]
Since \(r^2-r+1=(r-1/2)^2+3/4>0\), its sign is exactly the sign of \(r\).

For \(0<r<1/2\), all of \(A,B,C,AB-C\) are positive, so the cubic Hurwitz criterion gives asymptotic stability. For \(1/2<r<1\), the Routh first column has signs \(+,+,+,-\), hence exactly one open-right-half-plane root. For \(r>1\), its signs are \(+,-,-,-\), again giving exactly one such root. For \(-1<r<0\), the signs are \(+,+,-,+\), giving exactly two; for \(r<-1\), they are \(+,-,+,+\), also giving exactly two. At \(r=-1\),
\[
p_-1(\lambda)=(\lambda+1)(\lambda^2-\lambda+3),
\]
which also has two open-right-half-plane roots.

The parameter ranges follow from the two quadratic roots. If \(a<0\), then \(r_+>1\) and \(r_-<0\). If \(0<a<1/4\), then \(1/2<r_+<1\) and \(0<r_-<1/2\). At \(a=0\), \(r_+=1\) and \(r_-=0\), with
\[
p_1(\lambda)=\lambda^3-1,
\qquad
p_0(\lambda)=(\lambda+1)(\lambda^2+1).
\]
At \(a=1/4\), \(r_+=r_-=1/2\) and
\[
p_0.5(\lambda)=\lambda\left(\lambda^2+\frac34\lambda+\frac12\right),
\]
whose nonzero roots are \(-3/8\pm i\sqrt{23}/8\). For \(a>1/4\), the equilibrium quadratic has no real root.

Finally, on \(0<a<1/4\), every eigenvalue at the \(r_-\) equilibria lies in the open left half-plane. Therefore each has \(|\arg\lambda|>\pi/2\), which is strictly larger than \(q\pi/2\) for \(0<q<1\) and equals the ordinary Hurwitz requirement at \(q=1\). The source's commensurate fractional-order stability theorem therefore makes the same two equilibria asymptotically stable for every \(0<q\le1\).

## Verification
The bundled `verify.py` reconstructs the characteristic determinant for both signs \(s=\pm1\) using exact polynomial arithmetic, verifies the factorization \(AB-C=r(r^2-r+1)\), and checks the special factorizations at \(r=-1,0,1/2,1\). Running

`python3 verify.py`

returns `VERIFY_OK`.

The proof of the interval classification is analytic; no finite numerical sampling is used as a substitute for the Routh sign argument.

## Relationship to prior work
Muñoz-Pacheco et al. give the system, the four symbolic equilibria, the commensurate fractional-order stability criterion, numerical eigenvalues for \(a=-1\), the nonhyperbolic case \(a=1/4\), and the no-equilibrium regime \(a>1/4\). In Section 3.5 they state that all four equilibria are unstable whenever \(a<1/4\). Their Table 1 verifies only the representative negative value \(a=-1\); it does not supply a proof over the full interval.

The exact Routh partition above shows that the statement does not extend through \(0<a<1/4\): two equilibria are sinks there, while the other two retain one unstable direction. Searches by the source title, DOI, defining equations, equilibrium aliases, and the exact stability interval found no published published-finding corpus item or indexed follow-up that states this partition. The closest published-finding corpus findings concern different vector fields such as the Rössler, Lorenz–Stenflo, Halvorsen, and Rucklidge systems and do not imply this branchwise cubic classification.

## Limitations
This result is a local equilibrium classification plus a commensurate fractional-order stability corollary. It does not establish a bifurcation theorem at \(a=0\) or \(a=1/4\), does not prove persistence or disappearance of any chaotic attractor, and does not determine attraction basins. The literature search cannot prove absolute novelty; the principal residual risk is an unindexed later correction or reproduction of the same cubic calculation.

## References
1. J. M. Muñoz-Pacheco, E. Zambrano-Serrano, C. Volos, S. Jafari, J. Kengne, and K. Rajagopal, “A New Fractional-Order Chaotic System with Different Families of Hidden and Self-Excited Attractors,” *Entropy* 20 (2018), 564. DOI: 10.3390/e20080564. Published 2018-07-28.
2. Mathematical Reviews and zbMATH, *MSC2020*, 37C10: Dynamics induced by flows and semiflows.
