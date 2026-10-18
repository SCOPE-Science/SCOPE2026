# The four residue classes of the geometric \(a\)-number of the Chebyshev plane quartic

## Finding
For every odd prime \(p\), let \(C_p\) be the smooth projective plane quartic over \(\overline{\mathbb F}_p\) defined by
\[
y^4=x^4-4x^2+2.
\]
Its Jacobian has the following complete prime-residue classification:

| \(p\bmod8\) | \(a(\operatorname{Jac}(C_p))\) | geometric \(p\)-rank |
|---:|---:|---:|
| \(1\) | \(0\) | \(3\) |
| \(3\) | \(2\) | \(1\) |
| \(5\) | \(1\) | \(2\) |
| \(7\) | \(3\) | \(0\) |

In particular, the Jacobian is ordinary exactly for \(p\equiv1\pmod8\) and superspecial exactly for \(p\equiv7\pmod8\). It is supersingular exactly in the latter case. The statements include \(p=3,5,7\) without excluding small odd characteristics.

## Assumptions and scope
Here \(p\) is any odd rational prime. The \(a\)-number is the dimension over \(\overline{\mathbb F}_p\) of the kernel of the Cartier operator on regular differentials, equivalently \(\dim\operatorname{Hom}(\alpha_p,\operatorname{Jac}(C_p)[p])\). A genus-three Jacobian is superspecial exactly when its \(a\)-number is three. The \(p\)-rank is the dimension of the maximal etale part of its geometric \(p\)-torsion.

The projective equation is \(Y^4=X^4-4X^2Z^2+2Z^4\). On the affine chart \(Z=1\), simultaneous vanishing of the partial derivatives would require \(y=0\) and either \(x=0\) or \(x^2=2\), neither of which lies on the curve because the right side is, respectively, \(2\) or \(-2\). At infinity \(X^4=Y^4\) gives four distinct smooth points. Thus this is a smooth plane quartic of genus three for all odd \(p\).

## Proof
The commuting involutions \(\sigma(x,y)=(-x,y)\) and \(\tau(x,y)=(x,-y)\) generate a Klein four-group. Their three nontrivial quotients are smooth genus-one curves, with explicit rational quotient maps:

1. For \(\sigma\), put \(w=y\) and \(z=x^2-2\). The defining equation becomes \(E_1:z^2=w^4+2\).
2. For \(\tau\), put \(v=y^2\). It becomes \(E_2:v^2=x^4-4x^2+2\).
3. For \(\sigma\tau\), on the dense set \(x\ne0\) put \(r=y/x\) and \(z=2/x^2-2\). Clearing denominators gives \(E_3:z^2=2(r^4+1)\), since \(x^4(z^2-2(r^4+1))=2(x^4-4x^2+2-y^4)\).

All three quotient morphisms have degree two, and each nonsingular quartic model has genus one. Their three pullback lines in \(H^0(C_p,\Omega^1)\) are distinct character eigenspaces under the Klein four-group: for the standard affine plane-quartic differential basis \(dx/y^3,\;x\,dx/y^3,\;dx/y^2\), the three invariant lines belong respectively to \(\sigma\tau,\sigma,\tau\). They span all three dimensions. The sum of the three Jacobian pullbacks therefore gives an isogeny
\[
E_1\times E_2\times E_3\longrightarrow\operatorname{Jac}(C_p)
\]
whose kernel is annihilated by two: the dual norm–pullback composition is multiplication by two on each elliptic factor, and mixed compositions vanish by the distinct character actions. Thus the isogeny has degree a power of two. Because \(p\ne2\), it induces an isomorphism of \(p\)-divisible groups and preserves both the \(a\)-number and \(p\)-rank.

For a genus-one model \(Y^2=aX^4+bX^2+c\), let \(I=12ac+b^2\) and \(J=72abc-2b^3\). The standard binary-quartic formula yields \(j=1728(4I^3)/(4I^3-J^2)\). Consequently,
\[
j(E_1)=1728,\qquad j(E_2)=8000,\qquad j(E_3)=1728.
\]
The corresponding characteristic-zero elliptic curves have complex multiplication by the orders of discriminants \(-4,-8,-4\), respectively. Their smooth models have good reduction at every odd prime. Deuring's CM reduction criterion implies that \(E_1,E_3\) are supersingular precisely for \(p\equiv3\pmod4\), while \(E_2\) is supersingular precisely when \(p\equiv5,7\pmod8\). In each case the complementary primes are ordinary. (This includes the small odd prime \(3\): the CM criterion and direct Cartier computation agree.)

For an elliptic curve, the geometric \(a\)-number is one in the supersingular case and zero in the ordinary case; its \(p\)-rank is respectively zero or one. Summing these three contributions proves every row of the table. The degree-two character decomposition, rather than reduction of an arbitrary isogeny, is essential to the argument in characteristic \(p\).

## Verification
Run \(\texttt{python3 verify_chebyshev_a.py}\). The standalone standard-library script checks the three quartic \(j\)-invariants, the identities of the displayed quotient maps, and Hasse–Witt matrix ranks for fifteen primes \(3\le p\le53\). It computes the Hasse–Witt matrix by extracting the appropriate coefficients from the \((p-1)\)-st power of the defining quartic and performs exact modular elimination. The output ends in \(\texttt{VERIFY\_OK}\). The finite checks corroborate the theorem; they do not replace the Klein-four decomposition and CM reduction proof for all primes.

## Relationship to prior work
Tafazolian and Top (arXiv:2505.01216v1, May 2, 2025) introduce and study the exact Chebyshev plane-curve family and compute its automorphism groups and special maximality phenomena. Their Remark 4.4 explicitly computes \(j=8000\) for the genus-one curve \(y^2=x^4-4x^2+2\), a fact used here, not claimed as original. Dias, Tafazolian and Top (Finite Fields Appl. 101 (2025), 102521) already characterize maximality of Chebyshev plane curves over quadratic finite fields; such maximality data and the known elliptic \(j\)-invariant do not state or imply the four-valued \(a\)-number profile without the three-factor prime-to-characteristic Jacobian decomposition. The general elliptic-factor splitting for Ciani quartics is classical and is likewise not claimed as new. The new exact conclusion is the complete \(p\)-rank and \(a\)-number arithmetic progression for this naturally singled-out plane quartic, including the two nonordinary nonsuperspecial progressions.

## Limitations
This is a geometric statement over the algebraic closure of each prime field, not a determination of the full Ekedahl–Oort types or canonical principal polarizations. It does not classify higher-degree Chebyshev plane curves. A general Ciani-isogeny argument and the CM reduction theorem are established tools; an unindexed treatment may already combine them for this particular curve. The closest earlier maximality paper's full text was not available in the accessed source, leaving specific residual overlap risk despite its abstract focusing on maximality rather than the complete \(a\)-number profile.

## References
- S. Tafazolian and J. Top, *Automorphisms of Plane Curves defined from Chebychev polynomials*, arXiv:2505.01216v1 (first public May 2, 2025), especially Remark 4.4.
- G. Dias, S. Tafazolian and J. Top, *On certain maximal curves related to Chebyshev polynomials*, Finite Fields Appl. **101** (2025), article 102521, doi:10.1016/j.ffa.2024.102521.
- Standard Klein-four/Ciani-quartic Jacobian factorization by elliptic quotients (classical).
- Deuring's criterion for ordinary versus supersingular reduction of CM elliptic curves.
- SageMath, *Elliptic curves over number fields* documentation, \(\operatorname{cm\_discriminant}(8000)=-8\) and \(\operatorname{cm\_discriminant}(1728)=-4\).
