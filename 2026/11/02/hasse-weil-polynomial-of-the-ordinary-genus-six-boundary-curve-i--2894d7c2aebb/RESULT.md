# Hasse–Weil polynomial of the ordinary genus-six boundary curve in characteristic three

## Finding
Let \(X/\mathbb F_3\) be the unique smooth projective curve with function field
\[
\mathbb F_3(x,y),\qquad y^3-y=x+\frac{1}{x^3-x}.
\]
Then its genus is \(6\), and its exact Hasse–Weil numerator is
\[
\boxed{L_X(T)=1+16T^3+118T^6+432T^9+729T^{12}}
\]
with the integral factorization
\[
L_X(T)=(1-T+3T^2)^2(1+T-2T^2+3T^3+9T^4)^2.
\]
In particular, \(\#\operatorname{Jac}(X)(\mathbb F_3)=L_X(1)=1296\). If \(E/\mathbb F_3\) is an elliptic curve of trace \(1\), and \(A/\mathbb F_3\) is the simple ordinary abelian surface with Frobenius characteristic polynomial
\[
z^4+z^3-2z^2+3z+9,
\]
then
\[
\operatorname{Jac}(X)\sim_{\mathbb F_3}E^2\times A^2.
\]
Furthermore, for *every* positive integer \(n\) not divisible by \(3\),
\[
\boxed{\#X(\mathbb F_{3^n})=3^n+1.}
\]
This is one coherent arithmetic determination of the distinguished prime-field member of the ordinary genus-six equality family introduced in [1, Proposition 8.7].

## Assumptions and scope
The base field is exactly \(\mathbb F_3\), and the curve denotes the **smooth projective normalization** of the displayed Artin–Schreier equation. Its function field has a degree-three separable Artin–Schreier extension of \(\mathbb F_3(x)\). The three finite poles of \(x+1/(x^3-x)\) are \(x=0,1,-1\); the fourth is \(x=\infty\). All four poles are simple and rational. The statements about the Jacobian are over \(\mathbb F_3\), not only over an algebraic closure. The source's more general parameters \(c\in\overline{\mathbb F}_3^*\) are **not** covered by this zeta calculation; the two nonzero values \(c\in\mathbb F_3\) are isomorphic over \(\mathbb F_3\) by \(y\mapsto-y\).

## Proof
**1. Ramification and genus.** The polynomial \(x^3-x\) has simple roots in \(\mathbb F_3\), because its derivative is \(-1\). At each finite root, \(1/(x^3-x)\) has a simple pole. At infinity, \(x+1/(x^3-x)\) has a simple pole. No other poles occur. For an Artin–Schreier cover of degree \(p=3\), each simple pole is totally ramified with different exponent \((p-1)(1+1)=4\). The Riemann–Hurwitz formula gives
\[
2g(X)-2=3(-2)+4\cdot4=10,
\]
so \(g(X)=6\). Each pole has exactly one point above it, rational over every \(\mathbb F_{3^n}\), contributing **four** points in all extension counts.

**2. Trace count and orbit identity.** For \(q=3^n\) and \(x\in\mathbb F_q\setminus\mathbb F_3\), put \(f(x)=x+1/(x^3-x)\). The equation \(y^3-y=f(x)\) has exactly three solutions in \(\mathbb F_q\) when \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_3}(f(x))=0\), and none otherwise. The translation identity
\[
f(x+t)=f(x)+t\qquad(t\in\mathbb F_3)
\]
follows from \((x+t)^3-(x+t)=x^3-x\). Therefore, along an orbit \(\{x,x+1,x-1\}\) of size three in \(\mathbb F_q\setminus\mathbb F_3\), the trace values differ by \(n t\) in \(\mathbb F_3\). When \(3\nmid n\), exactly one member has trace zero and contributes three points; the orbit contributes three in total. There are \((3^n-3)/3\) such orbits, giving \(4+(3^n-3)=3^n+1\). This proves the last displayed formula for **all** eligible \(n\), not merely those tested.

**3. Exhaustive counts needed for the numerator.** Exact arithmetic in \(\mathbb F_{3^n}\), with explicitly tested irreducible defining polynomials, gives the following point counts for \(n=1,\dots,9\):
\[
(N_1,N_2,N_3,N_4,N_5,N_6,N_7,N_8,N_9)
=(4,10,76,82,244,670,2188,6562,18868).
\]
The polynomial-time point-count algorithm in `verify.py` iterates over **all** elements of each relevant finite field, adds the four totally ramified points, and compares two independent counts for each \(x\): the number of solutions of \(y^3-y=f(x)\) from its complete image table, and the zero-trace criterion. For degrees three and six it additionally repeats the calculation in a different irreducible field presentation. Thus the values for \(n\le6\) are exhaustive exact finite computations, not sampled experiments.

Write \(N_n=3^n+1-S_n\), where \(S_n=\sum_{i=1}^{12}\alpha_i^n\) for the reciprocal roots of the Weil numerator. The values for \(n\le6\) above yield
\[
(S_1,S_2,S_3,S_4,S_5,S_6)=(0,0,-48,0,0,60).
\]
The integral Newton identities \(k c_k=-\sum_{j=1}^k c_{k-j}S_j\), with \(c_0=1\), give
\[
(c_0,c_1,\dots,c_6)=(1,0,0,16,0,0,118).
\]
The Weil functional equation of a genus-six curve over \(\mathbb F_3\) implies
\[
c_{12-k}=3^{6-k}c_k\quad(0\le k\le6),
\]
which forces the claimed complete degree-twelve polynomial. The independent counts for degrees seven through nine satisfy the resulting Newton recurrences.

**4. Isogeny decomposition.** Direct integer polynomial multiplication verifies the claimed factorization. The quadratic factor is a Frobenius polynomial of an ordinary elliptic curve of trace \(1\). The quartic reciprocal factor corresponds to the monic Frobenius polynomial \(h(z)=z^4+z^3-2z^2+3z+9\). The four roots of \(h\) have complex absolute value \(\sqrt3\), since \(h\) divides the characteristic polynomial of Frobenius of \(X\). If \(h\) factored over \(\mathbb Q\), Gauss's lemma and the absence of linear factors (no integer root can have absolute value \(\sqrt3\)) would give monic integer quadratics \((z^2+az+b)(z^2+cz+d)\). Each factor's constant term has absolute value \(3\), hence \(b,d\in\{\pm3\}\). Matching coefficients requires
\[
a+c=1,\quad bd=9,\quad ac+b+d=-2,\quad ad+bc=3.
\]
The condition \(bd=9\) forces \((b,d)=(3,3)\) or \((-3,-3)\). The first case requires \(ac=-8\), impossible for integers \(a+c=1\) (discriminant \(33\)); the second requires \(ac=4\) (discriminant \(-15\)). Thus \(h\) is irreducible over \(\mathbb Q\). By the finite-field isogeny classification, its factor defines a simple abelian surface \(A\). Its middle coefficient \(-2\) is not divisible by \(3\), proving ordinarity. Uniqueness of the isogeny class associated with a Weil polynomial establishes \(\operatorname{Jac}(X)\sim E^2\times A^2\). Substitution at \(T=1\) yields \(L_X(1)=(3\cdot12)^2=1296\).

## Verification
Run the entirely self-contained exact verifier with `python3 verify.py`. It uses only the Python standard library, tests irreducibility of every finite-field modulus by exhaustive trial division, enumerates all field elements for degrees \(1\) through \(9\), independently checks traces and solution-image tables, confirms alternate models in degrees \(3\) and \(6\), reconstructs the Weil numerator from the first six counts, checks the factorization and the value at \(1\), and checks further Newton identities. Its observed final output line is `VERIFY_OK`. The infinite extension-count identity is proved separately in Step 2; finite tests do not establish that infinite assertion.

## Relationship to prior work
Tafazolian [1, Proposition 8.7] introduces precisely the characteristic-three ordinary genus-six boundary family, giving its genus and automorphism structure; Proposition 8.8 gives its full geometric automorphism group and isomorphism criterion. The inspected full primary article does not supply the Hasse–Weil numerator or the arithmetic isogeny decomposition of its \(\mathbb F_3\)-member. Giulietti–Korchmáros [2] analyzes large \(p\)-group actions and a separate genus-\(p-1\) Kloosterman family, not this genus-six curve's zeta polynomial. Finite-field point counting, Newton identities, the Weil functional equation, and isogeny classification are classical tools. The specific polynomial, simple-factor pattern, and uniform extension-count identity for this named curve are the assessed additions; no novelty is claimed for those general tools or for the original construction.

## Limitations
The exact arithmetic assertions apply to the specified \(\mathbb F_3\)-form and its \(\mathbb F_3\)-isomorphic coefficient \(-1\) counterpart. This does not classify twists, all non-prime-field parameters \(c\), polarizations, integral endomorphism rings, explicit isogeny maps, or all automorphisms over \(\mathbb F_3\). Although the inspected literature and research records did not show this exact result, historical priority cannot be proved by search alone; other curve models and unindexed arithmetic tables remain possible overlap risks. 

## References
[1] S. Tafazolian, *Sharp bounds and gap phenomena for large \(p\)-subgroups of automorphism groups of curves*, arXiv:2610.05539 (first submitted 2026-10-04), especially Propositions 8.7–8.8. https://arxiv.org/abs/2610.05539

[2] M. Giulietti and G. Korchmáros, *Large \(p\)-groups of automorphisms of algebraic curves in characteristic \(p\)*, arXiv:1507.03737 (2015). https://arxiv.org/abs/1507.03737
