# The smooth irreducible rank-zero divisor in a characteristic-five Picard-curve family

## Finding

Let \(k=\overline{\mathbb F}_5\) and \(U=\{(a,b)\in k^2:ab(a-1)(b-1)(a-b)\ne0\}\). Define smooth genus-three Picard curves
\[
C_{a,b}:\quad y^3=x(x-1)(x-a)(x-b).
\]
Put \(s=a+b\), \(t=ab\), and
\[
H(s,t)=-2t^3-2st^2+(s-1)(s+1)^5(t+s^2-1)\in\mathbb F_5[s,t].
\]
The Jacobian's \(5\)-rank is exactly \(0\) on \(H(a+b,ab)=0\), and exactly \(2\) on its complement in \(U\). Every smooth member has \(a\)-number exactly \(1\). Moreover, \(H(a+b,ab)=0\) defines a **nonempty smooth geometrically irreducible divisor** in \(U\); in particular, there is no intermediate \(5\)-rank-one stratum in this family.

## Assumptions and scope

All curves and parameter loci are over \(k\), characteristic exactly \(5\), and branch values \(0,1,a,b,\infty\) are pairwise distinct. The quintuple branch divisor is not quotiented by coordinate transformations: this is a statement about the ordered parameter surface \(U\). By Riemann--Hurwitz, the degree-three totally ramified cover \(C_{a,b}\to\mathbb P^1\) has genus \(3\). The phrase \(5\)-rank means the rank of the maximal étale subgroup of \(J[5]\), equivalently the stable rank of the Cartier operator on regular differentials. The \(a\)-number is the Cartier-kernel dimension. No statement about the full Newton polygon is claimed.

## Proof

Write \(f=x^4-(s+1)x^3+(t+s)x^2-tx\). A holomorphic differential basis is \(\omega_1=dx/y\), \(\omega_2=dx/y^2\), and \(\omega_3=x\,dx/y^2\). Using \(y^3=f\), the characteristic-five Cartier extraction rule on \(f^3\,dx\), \(f\,dx\), and \(xf\,dx\) gives the following semilinear action:
\[
\begin{aligned}
\mathcal C(\omega_1)&=c_4^{1/5}\omega_2+c_9^{1/5}\omega_3,\\
\mathcal C(\omega_2)&=\omega_1,\\
\mathcal C(\omega_3)&=d^{1/5}\omega_1,
\end{aligned}
\qquad
\begin{aligned}
c_4&=[x^4]f^3=-2t^2(t+s),\\
c_9&=[x^9]f^3=-(s-1)(s^2+t-1),\\
d&=-(s+1).
\end{aligned}
\]
Here \(\mathcal C\) is \(5\)-th-root linear. The second iterate sends \(\omega_1\) to \((c_4+c_9d^5)^{1/25}\omega_1=H(s,t)^{1/25}\omega_1\). The other two basis vectors enter the same alternating two-step cycle. Thus the stable Cartier rank is \(2\) when \(H\ne0\), and \(0\) when \(H=0\) (the cube of the Cartier operator vanishes in the latter case). At every point of \(U\), \((c_4,c_9)\ne(0,0)\): since \(t\ne0\), \(c_4=0\) forces \(t=-s\); then \(c_9=0\) forces \(s=1\) (giving repeated roots) or \(s=3\) (giving a root equal to \(1\)). Thus \(\mathcal C\) has ordinary matrix rank \(2\) everywhere and the \(a\)-number is \(1\).

To prove the divisor smooth, take partial derivatives of \(H\) in the symmetric coordinates. Exact polynomial division over \(\mathbb F_5\), using lexicographic order \(t>s\), gives the reduced Gröbner basis
\[
\bigl\{t+s^6-s^5+s-1,\quad(s-1)(s+1)^5(s+2)^5\bigr\}
\]
for \((H,\partial_sH,\partial_tH)\). Its affine common zeros are \((s,t)=(1,0),(-1,0),(3,2)\). The first two have \(t=0\); the third has \(1-s+t=0\), so all lie outside the smooth branch-parameter locus. Moreover \((a,b)\mapsto(s,t)\) is étale on \(a\ne b\), since its Jacobian is \(a-b\). This proves smoothness in \(U\).

Next prove that the cubic \(H(s,t)\) is absolutely irreducible. Work over \(\overline{\mathbb F}_5(s)\). A rational root in \(t\) would be integral over \(\overline{\mathbb F}_5[s]\) because the \(t^3\) coefficient is a unit, hence must be a polynomial \(t=T(s)\). Comparing top degrees shows \(\deg T\) is \(2\) or \(3\). In degree two, leading balance gives \(T=-s^2+Bs+C\); the \(s^7\) and \(s^6\) coefficients then force \(B=0,C=-1\), but the \(s^4\) coefficient is \(1\), a contradiction. In degree three, write \(T=us^3+vs^2+ws+z\). The \(s^9,s^8,s^7,s^6\) coefficients successively give \(u^2=3,\ v=2u-2,\ w=u+2,\ z=u-2\); the \(s^4\) coefficient is again \(1\), a contradiction. A cubic with no root over a field is irreducible. This proves geometric irreducibility of \(H(s,t)\).

Finally, the ordered-parameter divisor is the quadratic cover of this irreducible symmetric divisor obtained by adjoining a root of \(Z^2-sZ+t\). Its discriminant is \(D=s^2-4t=s^2+t\). On the irreducible curve \(H=0\), set \(r=1/s\) and \(T=r^3t\). The leading equation at \(r=0\) is \(-2T^3+T=0\). At either simple nonzero root \(T=\pm\sqrt3\), the formal implicit-function theorem gives a geometric place where \(s\) has pole order one and \(t\) pole order three. Hence \(D=s^2+t\) has pole order three and cannot be a square in the function field. Therefore the quadratic extension is a field, establishing geometric irreducibility of the ordered divisor. To see nonemptiness, take \(s=-1,t=1\): the roots \(a,b\) of \(Z^2+Z+1\) are distinct and avoid \(0,1\), and \(H(-1,1)=0\).

## Verification

The accompanying `verify.py` regenerates the coefficients of \(f^3\), checks the Cartier cycle polynomial, compares the radical singular-locus Gröbner basis, verifies the excluded boundary points, and checks the coefficient obstructions in the polynomial-root argument. It uses exact symbolic operations over \(\mathbb F_5\) (SymPy) and prints `VERIFY_OK` on success. The valuation argument at infinity and the Cartier-to-\(5\)-rank inference are justified above, not replaced by finite-field sampling.

## Relationship to prior work

The cyclic-three genus-three model, Cartier-operator formalism, and the geometry of the supersingular locus on Picard modular surfaces are established topics. De Shalit and Goren study Picard modular Hasse invariants and supersingular strata abstractly; their cited results do not, in the inspected material, state the explicit rank-zero equation or its smooth irreducibility in this two-parameter ordered branch-coordinate family. Kazemifard and Tafazolian analyze particular finite-field Picard curves, rather than the full present locus. The proposed additional assertion here is the combined explicit equation, complete rank/a-number stratification, and geometric irreducibility in \(U\).

## Limitations

The full Newton polygon and its variation inside the rank-zero locus are not determined. The irreducibility assertion is for the ordered affine parameter locus and does not automatically describe the coarse moduli quotient. A pre-existing equivalent coordinate formulation in older Picard-curve or automorphic-form literature remains possible; novelty is not independently certified. These calculations do not assert supersingularity of every rank-zero Jacobian.

## References

1. E. de Shalit and E. Z. Goren, *A theta operator on Picard modular forms modulo an inert prime*, arXiv:1412.5494 (first posted 2014-12-17), https://arxiv.org/abs/1412.5494.
2. E. de Shalit and E. Z. Goren, *Supersingular curves on Picard modular surfaces modulo an inert prime*, arXiv:1607.04170 (first posted 2016-07-14), https://arxiv.org/abs/1607.04170.
3. A. Kazemifard and F. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields and Their Applications 34 (2015), 107--122, DOI:10.1016/j.ffa.2014.12.002.
