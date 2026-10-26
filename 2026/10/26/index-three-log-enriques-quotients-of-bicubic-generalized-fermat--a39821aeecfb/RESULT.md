# Index-three Log Enriques quotients of bicubic generalized Fermat threefolds: singularities and Hodge numbers

## Finding

**Theorem.** Let \(a,b,c\in\mathbb C\setminus\{0,1\}\) be pairwise distinct. In \(\mathbb P^5\) let \(X=X_{a,b,c}\) be defined by
\[
F=x_1^3+x_2^3+x_3^3+x_4^3+x_5^3=0,\qquad
G=ax_1^3+bx_2^3+cx_3^3+x_4^3+x_6^3=0.
\]
Let \(\omega\) be a primitive cube root of unity, and let \(g\) act by
\[
g[x_1:x_2:x_3:x_4:x_5:x_6]=[\omega x_1:\omega x_2:x_3:x_4:x_5:x_6].
\]
Then \(X\) is a smooth Calabi--Yau threefold of generalized Fermat type \((3;3,5)\). Its cyclic quotient \(Y=X/\langle g\rangle\) is a klt, noncanonical, index-three Log Enriques threefold, with a unique irreducible singular curve \(C\), smooth of genus ten. Every transverse singularity is \(\frac13(1,1)\). The projective birational map
\[
f:Z=(\operatorname{Bl}_C X)/\langle g\rangle\longrightarrow Y
\]
is a smooth resolution with irreducible exceptional divisor \(E\cong C\times\mathbb P^1\) and \(K_Z=f^*K_Y-\frac13 E\). Its Hodge invariants and Euler characteristics are independent of \((a,b,c)\) and equal to
\[
(h^{1,1}(Z),h^{2,1}(Z),h^{3,0}(Z))=(2,42,0),\qquad
\chi_{\mathrm{top}}(Y)=-60,\quad\chi_{\mathrm{top}}(Z)=-78.
\]
The resolution is not crepant. The Hodge assertion concerns this smooth ordinary resolution, not an age-shifted or stringy invariant of \(Y\).

## Assumptions and scope

Everything is over \(\mathbb C\); all varieties and quotient spaces are projective. The three coefficients are nonzero, distinct from one another and from one. The canonical class of a normal quotient is a Weil \(\mathbb Q\)-Cartier class; index three means \(3K_Y\sim0\) and \(K_Y\not\sim0\). The notation \(\frac13(1,1)\) denotes the analytic quotient of a transverse smooth two-space by the order-three scalar action. The canonical divisor identity is an equality of \(\mathbb Q\)-linear equivalence classes, or of discrepancies for compatible representatives.

## Proof

**1. Smoothness and the fixed curve.** The columns of the coefficient matrix for \((F,G)\) are \((1,a),(1,b),(1,c),(1,1),(1,0),(0,1)\). Every pair is linearly independent by the coefficient assumptions. At a common zero, at least three projective coordinates are nonzero: two nonzero coordinates would have two independent columns in the relation \(\sum x_i^3 v_i=0\), impossible. The two differential rows have the same columns multiplied by \(3x_i^2\), hence rank two at every point. Thus \(X\) is smooth. Adjunction gives \(K_X\cong\mathcal O_X(3+3-6)\cong\mathcal O_X\), and complete-intersection cohomology gives \(H^1(X,\mathcal O_X)=H^2(X,\mathcal O_X)=0\).

A projective point fixed by \(g\) lies in the ordinary eigenspace \(\{x_1=x_2=0\}\cong\mathbb P^3\) or the \(\omega\)-eigenspace \(\{x_3=x_4=x_5=x_6=0\}\cong\mathbb P^1\). The latter has no points of \(X\) because \(a\ne b\). The former intersection \(C\) is the smooth complete-intersection curve of the two restricted cubics, since its four column pairs are independent. Its degree is nine, and adjunction gives \(2g(C)-2=(3+3-4)\cdot9=18\), hence \(g(C)=10\). Connectedness of the projective complete intersection implies irreducibility. Nonidentity powers of \(g\) have the same fixed locus.

**2. Local quotient, resolution and canonical index.** Along \(C\) the conormal directions are represented by \(x_1,x_2\); since the defining equations have cubic dependence on them, the induced normal action is scalar multiplication by \(\omega\) on a rank-two normal bundle. In fact \(N_{C/X}\cong\mathcal O_C(1)^{\oplus2}\), because \(C\) is cut out in \(X\) by the two coordinate hyperplanes. Finite-order equivariant analytic linearization gives local coordinates \((z,u,v)\) with \(g(z,u,v)=(z,\omega u,\omega v)\). Thus \(Y\) has only the singular curve \(C\), transverse to which the type is \(\frac13(1,1)\). Cyclic quotient singularities are klt, while the age \(2/3<1\) proves noncanonicity.

Let \(B=\operatorname{Bl}_C X\). The scalar action on \(N_{C/X}\) fixes every line in each fiber, so \(E_B=\mathbb P(N_{C/X})\cong C\times\mathbb P^1\) pointwise. In a blowup chart \((u,v)=(t,ts)\), the action sends \((t,s,z)\) to \((\omega t,s,z)\). Therefore \(Z=B/\langle g\rangle\) is smooth; the quotient map \(\rho:B\to Z\) has ramification order three along \(E_B\) and no other ramification, and \(f:Z\to Y\) resolves precisely \(C\). We have \(K_B=\pi^*K_X+E_B\), \(K_B=\rho^*K_Z+2E_B\), and \(\rho^*E=3E_B\). Since \(X\to Y\) is quasi-étale, \(K_X=q^*K_Y\) for compatible rational divisors. These identities give \(K_Z=f^*K_Y-\frac13E\), and the coefficient is nonzero, so \(f\) is not crepant.

The Poincaré residue generator of \(H^0(X,K_X)\) transforms by the determinant of the six-dimensional diagonal lift divided by the characters of the defining invariant equations, hence by \(\omega^2\). The quasi-étale cyclic quotient therefore has \(3K_Y\sim0\) but no invariant canonical generator, so \(K_Y\not\sim0\). Rational singularities and \(H^1(\mathcal O_X)=0\) yield \(q(Y)=0\). By the definition of a Log Enriques variety as a klt \(K\)-torsion variety with zero irregularity, \(Y\) is index-three Log Enriques.

**3. Equivariant middle cohomology.** For a smooth \((3,3)\) complete intersection in \(\mathbb P^5\),
\[
c(T_X)=\frac{(1+H)^6}{(1+3H)^2}=1+6H^2-16H^3,\qquad\int_XH^3=9.
\]
Consequently \(\chi_{\rm top}(X)=-144\). Lefschetz hyperplane theory and Poincaré duality give \(b_0=b_2=b_4=b_6=1\), \(b_1=b_5=0\), and \(b_3(X)=148\). Since the fixed locus of each nontrivial element is \(C\), its topological Lefschetz number is \(\chi(C)=2-2\cdot10=-18\). Contributions from degrees zero, two, four and six total four, hence
\[\operatorname{Tr}(g\mid H^3(X,\mathbb Q))=4-(-18)=22.\]
For an order-three rational representation, the multiplicity of the trivial eigenvalue is \((148+2\cdot22)/3=64\), and each primitive eigenvalue occurs \((148-22)/3=42\) times. The action on the holomorphic volume form is nontrivial, so \(H^{3,0}(X)^{\langle g\rangle}=H^{0,3}(X)^{\langle g\rangle}=0\). Complex conjugation then gives \(h^{2,1}(X)^{\langle g\rangle}=64/2=32\).

**4. Cohomology of the resolution and Euler check.** The blowup formula for Hodge structures says
\[H^j(B,\mathbb Q)\cong H^j(X,\mathbb Q)\oplus H^{j-2}(C,\mathbb Q)(-1).\]
The extra summand is fixed by \(g\), because \(g\) fixes \(C\) and acts trivially on \(\mathbb P(N_{C/X})\). For a finite quotient of a smooth complex projective manifold, rational cohomology of the quotient is the invariant part, compatibly with Hodge structures. Hence
\[h^{1,1}(Z)=h^{1,1}(X)^g+1=2,\quad h^{2,1}(Z)=32+g(C)=42,\quad h^{3,0}(Z)=0.\]
Independently, the orbifold Burnside formula for coarse Euler characteristic gives
\[\chi_{\rm top}(Y)=\tfrac13(\chi(X)+2\chi(C))=(-144-36)/3=-60.\]
The resolution replaces \(C\) by a \(\mathbb P^1\)-bundle over \(C\), adding \(\chi(C)=-18\); thus \(\chi_{\rm top}(Z)=-78\). This agrees with \(2+2h^{1,1}(Z)-2h^{2,1}(Z)=-78\) and proves the theorem.

## Verification

The dependency-free script `verify.py` checks, with exact integer operations, the pairwise coefficient-column determinant test on an admissible example, the Chern-polynomial expansion, the genus formula, the topological Lefschetz character constraints, the invariant and nontrivial eigenspace multiplicities, both Euler formulas, the Hodge consistency equation and the quotient discrepancy number. Running `python verify.py` returns `VERIFY_OK`. The script supports but does not substitute for the proofs of finite-order analytic linearization, cohomological blowup decomposition, quotient transfer, or the invariance over all admissible coefficient triples; those steps are argued mathematically above.

## Relationship to prior work

Billi--Palomino--Sarti, *Quotients of Calabi--Yau Generalized Fermat manifolds and Log Enriques varieties* (arXiv:2610.21752v1, 2026), classify quotients by automorphisms with **empty fixed locus** and explicitly identify removal of that restriction as future work (Introduction, Theorem 1.1). Here the automorphism has a genus-ten fixed curve, and the theorem determines the resulting noncanonical singularity, index-three canonical class, explicit smooth resolution and full basic Hodge profile. Hidalgo--Hughes--Leyton--Álvarez (arXiv:2010.04628) study generalized Fermat automorphisms and fixed loci, so existence of such a fixed curve alone is not claimed as new. Constantin--Gray--Lukas (arXiv:1607.01830) and Braun (arXiv:1003.3235) study **free** quotients of complete-intersection Calabi--Yau manifolds; their free-quotient Hodge tables do not directly classify this ramified nonfree quotient. All standard formulas used in the proof are credited as classical; the specific combined calculation for the nonfree three-dimensional family is the claim.

## Limitations

The smooth threefold \(Z\) is not Calabi--Yau; specifically \(h^{3,0}(Z)=0\). This is an ordinary (noncrepant) resolution and its Hodge numbers must not be mistaken for stringy, orbifold or crepant-resolution Hodge numbers. The theorem makes no classification of all nonfree automorphisms or all coefficient-specialization symmetries. Standard techniques explain individual proof steps; novelty is limited to the explicitly identified family and complete stated invariants. An equivalent earlier calculation not indexed in the consulted sources remains possible.

## References

1. S. Billi, A. J. Palomino and A. Sarti, *Quotients of Calabi--Yau Generalized Fermat manifolds and Log Enriques varieties*, arXiv:2610.21752v1 (public 2026-10-15), especially Introduction, Sections 2--6. https://arxiv.org/html/2610.21752v1
2. R. A. Hidalgo, H. F. Hughes and M. Leyton--Álvarez, *Automorphisms of Generalized Fermat manifolds*, arXiv:2010.04628 (2020; v8 2024). https://arxiv.org/abs/2010.04628
3. A. Constantin, J. Gray and A. Lukas, *Hodge Numbers for All CICY Quotients*, arXiv:1607.01830 (2016). https://arxiv.org/abs/1607.01830
4. V. Braun, *On Free Quotients of Complete Intersection Calabi--Yau Manifolds*, arXiv:1003.3235 (2010). https://arxiv.org/abs/1003.3235
