# An ordinary genus-six Frobenius-nonclassical quintic with a cubed abelian-surface Weil factor

## Finding
Let \(a\in\mathbf F_4\) satisfy \(a^2+a+1=0\). The smooth plane quintic \(C/\mathbf F_4\) of Asgarli–Duan–Lai, Example 4.10, has equation
\[
F=X\bigl((a+1)X^4+X^2Y^2+X^2YZ+X^2Z^2+Y^4+Y^2Z^2+Z^4\bigr)+Y^4Z+YZ^4=0.
\]
Its genus is six and its Weil numerator is exactly
\[
L_C(T)=\det(1-T\operatorname{Frob}_4\mid H^1_{\mathrm{\acute et}}(C_{\overline{\mathbf F}_4},\mathbf Q_\ell))
=\bigl(1+3T^2+16T^4\bigr)^3.
\]
Consequently, its Jacobian is ordinary and is \(\mathbf F_4\)-isogenous to \(A^3\), where \(A/\mathbf F_4\) is a simple ordinary abelian surface with Frobenius polynomial \(U^4+3U^2+16\). After base change to \(\mathbf F_{16}\), the Jacobian is isogenous to \(E^6\), where \(E/\mathbf F_{16}\) is an ordinary elliptic curve with Frobenius polynomial \(U^2+3U+16\) (trace \(-3\)). In particular, for every odd positive integer \(n\),
\[
\#C(\mathbf F_{4^n})=4^n+1.
\]
For even \(n=2k\), the count is \(16^k+1-6s_k\), where \(s_0=2\), \(s_1=-3\), and \(s_k=-3s_{k-1}-16s_{k-2}\) for \(k\ge2\).

## Assumptions and scope
The displayed equation is exactly Example 4.10 of the cited preprint, up to the choice of either conjugate root \(a\). It defines a projective curve over \(\mathbf F_4\), not a family over arbitrary coefficient fields. The arithmetic assertions concern its smooth projective model and are unconditional. The value of the L-polynomial and isogeny decomposition, not the existence of this Frobenius-nonclassical curve, is the finding. An isogeny does not assert an isomorphism of principally polarized abelian varieties.

## Proof
Write the partial derivatives in characteristic two:
\[
\begin{aligned}
F_X&=(a+1)X^4+X^2Y^2+X^2YZ+X^2Z^2+Y^4+Y^2Z^2+Z^4,\\
F_Y&=Z(X^3+Z^3),\\
F_Z&=Y(X^3+Y^3).
\end{aligned}
\]
Any common projective zero of these derivatives either has \(Z=0\) and \(Y\ne0\), when \((X/Y)^3=1\), or has \(Z\ne0\), when after scaling \(Z=1\), \(X^3=1\) and \(Y=0\) or \(Y^3=1\). The point \([1:0:0]\) is not a common zero. Since the cube roots of unity lie in \(\mathbf F_4\), the geometric singularity candidates all have representatives among the sixteen explicit projective points checked in `checks/verify.py`; direct substitutions give nonzero derivative triples in each case. As the degree is five, Euler's identity makes simultaneous derivative vanishing the complete singularity criterion. Thus \(C\) is geometrically smooth, and its plane-quintic genus is \((5-1)(5-2)/2=6\).

On the affine chart \(Z=1\), the defining equation is the linearized equation
\[
(X+1)Y^4+(X^3+X)Y^2+(X^3+1)Y+(a+1)X^5+X^3+X=0.
\]
For each \(x\in\mathbf F_{4^n}\), its left side is an \(\mathbf F_2\)-linear function of \(y\) plus a constant. Exact binary elimination therefore counts all its solutions, with nullity giving the number of roots. On \(Z=0\), use \([x:1:0]\) and count roots of \((a+1)x^5+x^3+x=0\); \([1:0:0]\) is not on \(C\). The self-contained finite-field program `checks/count.cpp` enumerates each \(x\) and row-reduces the associated linear map in the extension fields of degrees \(1,2,3,4,5,6,7\) over \(\mathbf F_4\). The independent `checks/direct.cpp` evaluates every affine pair \((x,y)\) and infinity point for degrees \(1\) through \(6\), using polynomial-basis multiplication rather than linear-map ranks. They agree on the exact counts
\[
(N_1,N_2,N_3,N_4,N_5,N_6)=(5,35,65,395,1025,3395).
\]
Consequently the first six power sums of the twelve reciprocal roots of \(L_C(T)\) are \((0,-18,0,-138,0,702)\). Newton identities yield coefficients \(1,0,9,0,75,0,315\) through degree six. The genus-six functional equation, \(c_{12-j}=4^{6-j}c_j\) for \(0\le j\le6\), forces the remaining coefficients. Factoring the resulting integral polynomial gives the displayed \(L_C(T)\); no extrapolation from finitely many point counts is used.

Reduction modulo two gives \(L_C(T)\equiv(1+T^2)^3\), of degree six, so \(C\) has maximal \(2\)-rank six and its Jacobian is ordinary. The quartic \(P(U)=U^4+3U^2+16\) is irreducible over \(\mathbf Q\): a rational factorization into monic quadratics would give either \(b+d=3,\ bd=16\), of negative discriminant \(-55\), or \(b=d\in\{4,-4\}\) and a nonrational solution to \(2b-r^2=3\). Its roots have the correct Weil magnitude; ordinarity ensures that the associated Honda–Tate simple isogeny class has degree-four characteristic polynomial \(P\). Tate's isogeny theorem now gives \(J_C\sim_{\mathbf F_4}A^3\). After quadratic base change the characteristic polynomial is \((U^2+3U+16)^6\); the quadratic factor is the Weil polynomial of an ordinary elliptic curve over \(\mathbf F_{16}\). The same theorem gives \(J_{C,\mathbf F_{16}}\sim E^6\). Finally, the reciprocal roots occur in opposite-sign pairs, proving the odd-degree point formula, and their squares obey the stated quadratic recurrence, proving the even-degree formula.

## Verification
To reproduce, from the directory containing `checks/`, execute `g++ -O2 -std=c++17 checks/count.cpp -o count && ./count`, `g++ -O2 -std=c++17 checks/direct.cpp -o direct && ./direct`, and `python checks/verify.py` (Python with SymPy). The first program additionally verifies \(N_7=16385\), not used to reconstruct the Weil polynomial. `checks/verify.py` verifies geometric smoothness from all algebraically possible derivative-zero candidates, reconstructs the polynomial by Newton identities and the functional equation, checks quartic irreducibility and ordinarity. All programs were run successfully from the packaged source paths.

## Relationship to prior work
Asgarli, Duan and Lai introduced this particular \(\mathbf F_4\) quintic in Example 4.10 of *Frobenius nonclassical hypersurfaces* (arXiv:2207.11981, first public 2022-07-25) to demonstrate the degree-\(q+1\) even-dimensional case and a nonzero Hessian matrix. Their displayed example and proof concern Frobenius nonclassicality and smoothness; they do not state its Weil polynomial or Jacobian decomposition. Hefez–Voloch's rational-point formula, recalled by Borges–Homma, gives the first-extension count \(N_1=5\), but does not determine the degree-twelve numerator or the isogeny factors. The finding specializes standard Tate/Honda–Tate conclusions only **after** establishing a new exact Weil factorization for this specific curve.

## Limitations
The result concerns a single explicitly specified curve; it does not classify all Frobenius-nonclassical plane quintics or their Jacobians. The primary priority risk is an earlier unindexed computation or a published exact zeta table not located by the documented searches. Finite point counts through degree six determine the entire numerator here only because smoothness, genus and the functional equation have independently been established. Isogeny over finite fields does not identify the polarization or geometric automorphism group.

## References
1. Shamil Asgarli, Lian Duan, Kuan-Wen Lai, *Frobenius nonclassical hypersurfaces*, arXiv:2207.11981, Example 4.10 and Theorem 1.6. First public version 2022-07-25. https://arxiv.org/pdf/2207.11981
2. Herivelto Borges, Masaaki Homma, *Points on singular Frobenius nonclassical curves*, arXiv:1511.00339, Theorem 1.2 citing Hefez–Voloch. https://arxiv.org/pdf/1511.00339
3. John Tate, *Endomorphisms of abelian varieties over finite fields*, Inventiones Mathematicae 2 (1966), 134–144; and the Honda–Tate classification of simple isogeny classes.
