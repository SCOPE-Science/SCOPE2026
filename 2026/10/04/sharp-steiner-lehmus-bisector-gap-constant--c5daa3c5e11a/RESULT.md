# Sharp Steiner–Lehmus bisector-gap constant
## Finding
For every nondegenerate Euclidean triangle \(ABC\), write \(a,b,c\) for the side lengths opposite \(A,B,C\), and write \(y\) and \(z\) for the lengths of the internal angle bisectors from \(B\) and \(C\). If \(c>b\), then
\[
y-z>\kappa(c-b),
\]
where
\[
f(x)=\frac{\sqrt{x+2}(x^2+x+2)}{2(x+1)^2},\qquad
q^3+4q^2+q-10=0,\quad q\in(0,2),\qquad \kappa=f(q).
\]
Numerically, \(q=1.28427753730695\) and \(\kappa=0.856762017555545\). The constant is best possible:
\[
\inf_{c>b}\frac{y-z}{c-b}=\kappa.
\]
The infimum is not attained by a non-isosceles triangle; it is approached when \(c/b\to1\) and \(a/b\to q\). This establishes the sharp constant conjectured in Hajja's 2008 paper.

## Assumptions and scope
The triangle is an ordinary nondegenerate Euclidean triangle. The notation is ordered so that \(c>b\), hence \(C>B\). The result concerns internal angle bisectors only. Interchanging \(B\) and \(C\) gives the symmetric absolute-value form \(|y-z|>\kappa|c-b|\) whenever \(b\ne c\). Equality is impossible for a non-isosceles triangle because the sharp constant is attained only as a limiting isosceles configuration.

## Proof
Put
\[
p=\frac{B+C}2,\qquad \delta=\frac{C-B}2.
\]
Then \(0<\delta<p<\pi/2\) and \(A=\pi-2p\). If \(\rho\) is the circumradius, the sine rule gives
\[
a=2\rho\sin(2p),\quad b=2\rho\sin(p-\delta),\quad c=2\rho\sin(p+\delta).
\]
The standard angle-bisector formula gives
\[
y=\frac{2ac\cos(B/2)}{a+c},\qquad
z=\frac{2ab\cos(C/2)}{a+b}.
\]
After substituting the sine-rule expressions and using sum-to-product identities, define
\[
\gamma=\cos p,\qquad u=\cos\delta.
\]
Because \(0<\delta<p<\pi/2\), one has \(0<\gamma<u<1\). Direct simplification yields the exact dimensionless ratio
\[
Q(\gamma,u):=\frac{y-z}{c-b}
=2(1-\gamma)\sqrt{\frac{1+\gamma}{1+u}}
\frac{u+\gamma+2\gamma^2}{u-4\gamma^3+3\gamma}.
\]
The last denominator is positive because
\[
u-(4\gamma^3-3\gamma)>\gamma-(4\gamma^3-3\gamma)=4\gamma(1-\gamma^2)>0.
\]
For fixed \(\gamma\), logarithmic differentiation gives
\[
\frac{\partial}{\partial u}\log Q(\gamma,u)
=\frac{N_\gamma(u)}{2(1+u)(u+\gamma+2\gamma^2)(u-4\gamma^3+3\gamma)},
\]
where
\[
N_\gamma(u)=8\gamma^5+4\gamma^4-4\gamma^3u-14\gamma^3-6\gamma^2u-7\gamma^2+4\gamma-u^2.
\]
Its derivative is
\[
N_\gamma'(u)=-2u-4\gamma^3-6\gamma^2<0.
\]
Thus, as a function of \(u\in(\gamma,1)\), \(Q\) has at most one stationary point, and if it exists it is a strict maximum. Hence the minimum over the closed endpoint extension is attained at an endpoint. The two endpoint limits are
\[
\lim_{u\downarrow\gamma}Q(\gamma,u)=1,
\]
and
\[
\lim_{u\uparrow1}Q(\gamma,u)
=f(2\gamma),\qquad
f(x)=\frac{\sqrt{x+2}(x^2+x+2)}{2(x+1)^2}.
\]
Therefore every interior configuration satisfies
\[
Q(\gamma,u)>\min\{1,f(2\gamma)\}.
\]
Now
\[
f'(x)=\frac{x^3+4x^2+x-10}{4(x+1)^3\sqrt{x+2}}.
\]
The cubic in the numerator is strictly increasing on \(x>0\), is negative at \(x=0\), and positive at \(x=2\). It therefore has a unique root \(q\in(0,2)\), and \(f\) has its unique minimum there. Set \(\kappa=f(q)\). Since \(\kappa\le f(1)=\sqrt3/2<1\), both endpoint values are at least \(\kappa\), and hence \(Q(\gamma,u)>\kappa\).

For sharpness, choose \(p\) so that \(2\cos p=q\) and let \(\delta\downarrow0\). Then \(c>b\) for every \(\delta>0\), while \(Q(\cos p,\cos\delta)\to f(q)=\kappa\). No larger universal constant can hold.

## Verification
The proof is symbolic and covers the full continuous domain. The accompanying `verify.py` independently evaluates the side/bisector formulas and the reduced \(Q(\gamma,u)\) formula over deterministic random samples, checks the endpoint limits numerically, locates the cubic root by bisection, and stress-tests the sharp inequality. These finite computations are consistency checks only; the infinite statement is proved by the derivative argument above.

## Relationship to prior work
Hajja's 2008 paper asks for the best constant \(\lambda\) in \(y-z\ge\lambda(c-b)\), reports finite integer-side searches near \(0.856762\), derives the isosceles-limit function \(f\), identifies the same cubic root \(q\), and explicitly states the sharp inequality with \(f(q)\) as a conjecture (its equation (13)). The argument above supplies the missing global proof by reducing the full two-parameter problem to an endpoint comparison in \(u=\cos\delta\). A 2013 thesis discussing the conjecture describes it as computationally motivated rather than proved. Later Steiner–Lehmus papers located in the comparison search concern other generalizations and monotonicity configurations; no inspected source states a proof of this best-constant conjecture.

## Limitations
The result is specific to Euclidean internal angle bisectors. It does not address the two other best-constant questions in Hajja's 2008 equations (11), nor hyperbolic or spherical analogues. The literature search cannot establish absolute uniqueness: an equivalent proof could exist in unindexed or differently phrased literature. The 2019 same-theme article was available only at abstract/index level during this check, so possible hidden overlap there remains a residual originality risk; targeted searches for the numerical constant and the conjectured inequality did not surface such a result.

## References
1. M. Hajja, “Stronger Forms of the Steiner-Lehmus Theorem,” Forum Geometricorum 8 (2008), 157–161. Publication date: September 8, 2008.
2. S. R. Gardner, “A Variety of Proofs of the Steiner-Lehmus Theorem,” M.S. thesis, East Tennessee State University, 2013.
3. S. Abu-Saymeh and M. Hajja, “More variations on the Steiner-Lehmus theme,” The Mathematical Gazette 103 (2019), 1–11, DOI 10.1017/mag.2019.1.
4. Q. H. Tran, “A generalisation and proof of the Steiner–Lehmus Theorem,” The Mathematical Gazette 109 (2025), 555–557, DOI 10.1017/mag.2025.10149.
