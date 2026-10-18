# Complete characteristic-seven \(p\)-rank and \(a\)-number strata of a genus-three Howe family

## Finding

Let \(k=\overline{\mathbb F}_7\). Consider the smooth genus-three hyperelliptic curves
\[
 C_{a,b}:\quad y^2=(x^4+a x^2+1)(x^4+b x^2+1),
\]
where \(a,b\in k\), \(a\ne b\), and \(a,b\notin\{2,-2\}\). Set \(s=a+b\) and \(u=ab\), and define, with all coefficients reduced modulo \(7\),
\[
\begin{aligned}
 H_0(s,u)&=(u+3)((u+1)(u+2)-s^2),\\
 H_-(s,u)&=(s-4)(s^2+s-2-u),\\
 H_+(s,u)&=(s+4)(s^2-s-2-u).
\end{aligned}
\]
The exact smoothness condition in this symmetric parameter plane is
\[
 \Delta(s,u):=(s^2-4u)(u^2+u+3s^2+2)\ne0.
\]
For every pair satisfying this condition, put \(r=\#\{H_0,H_-,H_+\text{ that vanish at }(s,u)\}\). Then
\[
 \boxed{\operatorname{rank}_7\operatorname{Jac}(C_{a,b})=3-r,\qquad
 a(\operatorname{Jac}(C_{a,b}))=r.}
\]
Thus the reduced nonordinary divisor in the smooth symmetric parameter plane is the restriction of \(H_0H_-H_+=0\), a union of six distinct geometrically irreducible rational plane curves (two components of each of \(H_0,H_-,H_+\)). The points in this smooth plane with \(r\ge2\) are *exactly* the following seven parameter points, all rational over \(\mathbb F_7\):
\[
\begin{array}{c|c|c}
(s,u)&\operatorname{rank}_7&a\\\hline
(0,5)&0&3\\
(2,4),(4,0),(5,4),(3,0),(4,3),(3,3)&1&2
\end{array}
\]
At every other smooth parameter, the Jacobian is either ordinary \((3,0)\) or has invariants \((2,1)\), according as none or exactly one of the three Hasse factors vanishes. The three Hasse divisors meet transversely at the triple point \((0,5)\), and the two meeting Hasse divisors meet transversely at each of the other six points. These conclusions hold over the full algebraic closure, not just at \(\mathbb F_7\)-rational parameters.

## Assumptions and scope

The base field has characteristic \(7\) and is algebraically closed. The parameters are *ordered* \((a,b)\), but all invariants are symmetric, so the theorem is presented on the symmetric quotient chart with coordinates \((s,u)\). The smoothness condition is equivalent to \(a\ne b\) and \(a,b\ne\pm2\). Statements count parameter points, not necessarily distinct isomorphism classes; no claim is made that these seven points yield seven nonisomorphic curves. The superspecial member is already known in the literature; its recovery is part of the exhaustive stratification, not a new uniqueness result.

## Proof

**Smooth locus and quotient curves.** The eight branch points of the hyperelliptic map are distinct precisely when the two even quartics are separately squarefree and share no roots. Their discriminant conditions are \((a^2-4)(b^2-4)(a-b)^2\ne0\), which in characteristic \(7\) becomes \(\Delta(s,u)\ne0\). For such parameters \(C_{a,b}\) has genus three. The commuting involutions \(\sigma(x,y)=(-x,y)\) and \(\tau(x,y)=(1/x,y/x^4)\) generate a Klein-four subgroup (these rational formulas extend to automorphisms of the complete curve). The quotient of \(\sigma\) has invariant coordinates \(X=x^2\), \(Y=y\); the quotient of \(\tau\) has \(X=x+1/x\), \(Y=y/x^2\); and the quotient of \(\sigma\tau\) has \(X=x-1/x\), \(Y=y/x^2\). These three smooth genus-one quotients are presented birationally as
\[
\begin{aligned}
E_0:&\quad Y^2=(X^2+aX+1)(X^2+bX+1),\\
E_-:&\quad Y^2=(X^2+a-2)(X^2+b-2),\\
E_+:&\quad Y^2=(X^2+a+2)(X^2+b+2).
\end{aligned}
\]
The addition of the three pullback maps gives \(E_0\times E_-\times E_+\to\operatorname{Jac}(C_{a,b})\). Each factor spans a distinct nontrivial character eigenspace of the Klein-four action on the three-dimensional differential space, and the invariant subspace for the full Klein-four group is zero (the residual double quotient of each displayed elliptic curve is rational). Thus their sum is an isogeny. Its kernel is annihilated by a power of two, by the character idempotents \((1\pm\sigma)(1\pm\tau)/4\), so its degree is a power of two. Because its degree is prime to \(7\), it induces an isomorphism on \(7\)-divisible groups; in particular the \(7\)-rank and \(a\)-number add across the three elliptic factors.

**Three explicit Hasse factors.** For an elliptic curve \(Y^2=q(X)\) with a separable quartic \(q\), its Hasse invariant in characteristic seven is the coefficient \([X^6]q(X)^3\), up to a nonzero scalar; it vanishes exactly when that elliptic curve is supersingular. Expanding each of the three displayed quartics and expressing elementary symmetric functions of \(a,b\) as \(s,u\) gives, exactly modulo \(7\), \(H_0,H_-,H_+\) as stated. Thus a supersingular quotient contributes \((\operatorname{rank}_7,a)=(0,1)\), and an ordinary quotient contributes \((1,0)\). Additivity under the prime-to-seven isogeny proves the full rank and \(a\)-number formulas at **every** smooth geometric parameter.

**All exceptional intersections.** In the polynomial ring \(\mathbb F_7[s,u]\), eliminate \(u\) from each pair \((H_0,H_-),(H_0,H_+),(H_-,H_+)\). Apart from nonzero constants, the three elimination resultants factor respectively as
\[
 s(s-2)(s+3)^7,\quad s(s+2)(s-3)^7,\quad s(s+3)(s-3).
\]
At every root \(s\) of these resultants, taking the polynomial greatest common divisor in \(u\), and then imposing \(\Delta\ne0\), gives, respectively,
\[
\begin{aligned}
V(H_0,H_-)\cap\{\Delta\ne0\}&=\{(0,5),(2,4),(4,0)\},\\
V(H_0,H_+)\cap\{\Delta\ne0\}&=\{(0,5),(5,4),(3,0)\},\\
V(H_-,H_+)\cap\{\Delta\ne0\}&=\{(0,5),(4,3),(3,3)\}.
\end{aligned}
\]
The elimination-and-gcd argument takes place in \(k\), not by bounded enumeration of rational points: every resultant root lies in \(\mathbb F_7\), and every corresponding gcd splits linearly over \(\mathbb F_7\). Therefore the sets are geometrically exhaustive. Direct substitution shows that all seven listed points satisfy \(\Delta\ne0\), and that only \((0,5)\) lies on all three Hasse divisors.

**Component geometry and transversality.** The factorization of \(H_0\) gives the distinct line \(u+3=0\) and the smooth affine conic \((u+1)(u+2)=s^2\); the factors of \(H_-\) and \(H_+\) give two further lines and two parabolas. Each is rational and geometrically irreducible. At each listed pairwise intersection, the gradients of the two vanishing Hasse polynomials are linearly independent over \(\mathbb F_7\); at \((0,5)\), their three gradients are pairwise independent. This proves the asserted transversal incidence structure.

## Verification

The standalone program `verify.py` reproduces the quartic Hasse coefficients, an independent determinant identity for the \(3\times3\) Cartier–Manin matrix of the genus-three curve, the three resultants, all specialized univariate gcds, the smoothness exclusions, and the seven exceptional parameters. It also checks direct Cartier-matrix ranks at the 31 smooth symmetric parameters in \(\mathbb F_7^2\), yielding \(12,12,6,1\) parameters with \(a\)-numbers \(0,1,2,3\), respectively. This last finite check is supplementary; the all-geometric-points assertion follows from the symbolic resultants and prime-to-seven isogeny, not from finite-field enumeration. Execute with Python 3 and SymPy using `python3 verify.py`.

## Relationship to prior work

Ohashi, *On the maximality of hyperelliptic Howe curves of genus 3* (first public 2021-12-21), develops the Howe-curve elliptic quotient decomposition and superspecial/maximality questions. Borówka and Shatsila, *Hyperelliptic genus 3 curves with involutions and a Prym map* (2023), give the same positive-sign model and explicit genus-one quotients in characteristic zero. Moriya and Kudo (2022) study superspecial genus-three curves and related enumerations. These antecedents supply the natural family, quotient isogeny and known superspecial context; the present result computes the *complete characteristic-seven intermediate \(7\)-rank/\(a\)-number stratification* in its two-parameter smooth chart, including all six \(a=2\) intersections. The known characteristic-seven superspecial isomorphism classification is not claimed anew.

## Limitations

The result is restricted to characteristic seven and the specified smooth hyperelliptic Howe family. The quotient coordinates do not classify the geometric isomorphism classes of all seven exceptional parameter points. The nonordinary divisor and its incidence structure are computed in the symmetric parameter chart, not in a compactification of the moduli stack. No assertion is made about Newton polygons beyond the stated \(7\)-rank and \(a\)-number, or about higher-genus Howe curves. Although the calculations and primary-text comparisons give strong support, an equivalent formulation may occur in literature not identified here; independent mathematical review has not been performed.

## References

- R. Ohashi, *On the maximality of hyperelliptic Howe curves of genus 3*, arXiv:2112.11152 (v1 publicly available 2021-12-21), especially the equations for elliptic quotients and the quotient-isogeny discussion.
- P. Borówka and A. Shatsila, *Hyperelliptic genus 3 curves with involutions and a Prym map*, arXiv:2308.07038 (2023), especially Proposition 4.3.
- T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926 (2022), superspecial classification context.
