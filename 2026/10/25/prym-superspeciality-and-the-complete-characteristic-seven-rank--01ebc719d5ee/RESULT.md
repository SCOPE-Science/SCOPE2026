# Prym superspeciality and the complete characteristic-seven rank stratification of a genus-five dihedral pencil

## Finding
Over an algebraically closed field \(k\) of characteristic \(7\), consider the smooth genus-five hyperelliptic curve
\[
 C_a:\ y^2=x^{12}+a x^6+1,\qquad a\in k,\quad a^2\ne4.
\]
The involution \(\iota(x,y)=(-x,y)\) gives a genus-two quotient \(Q_a\) and a three-dimensional Prym \(P_a\). The complete table of invariants is:

| Parameter | \(f(J(C_a)),\ a(J(C_a))\) | \(f(J(Q_a)),\ a(J(Q_a))\) | \(f(P_a),\ a(P_a)\) |
| --- | --- | --- | --- |
| \(a=0\) | \((2,3)\) | \((2,0)\) | \((0,3)\) |
| \(a^2=-1\) | \((3,2)\) | \((0,2)\) | \((3,0)\) |
| \(a^2=1\) | \((4,1)\) | \((2,0)\) | \((2,1)\) |
| all remaining smooth parameters | \((5,0)\) | \((2,0)\) | \((3,0)\) |

Here \(f\) means characteristic-seven rank of an abelian variety and \(a\) its a-number. Thus the Prym is superspecial, and the quotient ordinary, at \(a=0\); the quotient is superspecial and the Prym ordinary at \(a^2=-1\). The complete set of Jacobian ranks is \(\{2,3,4,5\}\). Up to geometric isomorphism, the nonordinary curves form precisely three classes represented by parameters \(0,1,\sqrt{-1}\).

## Assumptions and scope
All curves are their smooth projective models over algebraically closed \(k\) of characteristic exactly \(7\). Write \(f_a(x)=x^{12}+ax^6+1\). Since \(f'_a(x)=6x^5(2x^6+a)\) and \(f_a(0)=1\), repeated roots occur exactly when \(a^2=4\). Hence on the stated open parameter set the polynomial is squarefree of even degree \(12\), and \(C_a\) has genus \(5\). Its quotient by \(\iota\) has equation
\[
 Q_a:\ v^2=t^6+a t^3+1,\quad (t,v)=(x^2,y),
\]
and is likewise smooth of genus \(2\). The cover \(C_a\to Q_a\) has degree \(2\), prime to the characteristic, and is branched at the two points over zero and the two over infinity. Its Prym \(P_a\), the identity component of the norm kernel, has dimension \(3\). None of the assertions concern the singular boundary \(a^2=4\), other characteristics, or full Newton polygons.

## Proof
Set \(F_a(x)=f_a(x)^3\) and write \(F_a(x)=\sum_n c_nx^n\). Because \(7\) is odd, the standard hyperelliptic Cartier--Manin coefficient formula for a genus-\(g\) curve \(y^2=f(x)\) gives, in basis \(x^{j-1}dx/y\), the matrix with entries \(c_{7i-j}\) for \(1\le i,j\le g\), with coefficients read up to Frobenius semilinear convention. Expand in \(z=x^6\):
\[
 (1+az+z^2)^3=1+3az+3(a^2+1)z^2+a(a^2+6)z^3+3(a^2+1)z^4+3az^5+z^6.
\]
In characteristic \(7\), \(a(a^2+6)=a(a^2-1)\). All \(c_n\) vanish unless \(6\mid n\). Since \(7i-j\equiv i-j\pmod6\) and \(1\le i,j\le5\), this forces the five-by-five matrix to be diagonal:
\[
 M_C=\operatorname{diag}\bigl(3a,3(a^2+1),a(a^2-1),3(a^2+1),3a\bigr).
\]
Its determinant is \(3^4a^3(a^2+1)^2(a^2-1)=4a^3(a^2+1)^2(a^2-1)\) in \(k\). For a diagonal Frobenius- or Cartier-semilinear operator over a perfect field, its stable rank equals the number of nonzero diagonal entries; its a-number equals the dimension minus the first-iterate rank. Hence the Jacobian invariant pairs are \((2,3)\) at \(a=0\), \((3,2)\) at \(a^2=-1\), \((4,1)\) at \(a^2=1\), and \((5,0)\) otherwise. These loci are pairwise disjoint and disjoint from \(a^2=4\) in characteristic \(7\), so every stated rank occurs on a smooth curve.

For the quotient \(Q_a\), expanding \((1+at^3+t^6)^3\) with the genus-two coefficient formula gives
\[
 M_Q=3(a^2+1)I_2.
\]
Alternatively, the pullback \(t^{j-1}dt/v\) is \(2x^{2j-1}dx/y\), so the quotient differential space is exactly the \(\iota\)-invariant span of the second and fourth basis vectors, on which \(M_C\) has eigenvalues \(3(a^2+1)\). Since the covering degree is \(2\), the norm and pullback induce an isogeny \(J(Q_a)\times P_a\to J(C_a)\) with kernel killed by a power of \(2\). The isogeny therefore induces an isomorphism on characteristic-seven torsion group schemes and preserves the direct-sum decomposition of seven-divisible groups. The complementary \(\iota\)-anti-invariant Cartier block on \(P_a\) is
\[
 M_P=\operatorname{diag}\bigl(3a,a(a^2-1),3a\bigr).
\]
Thus \(Q_a\) is superspecial precisely when \(a^2=-1\) and ordinary otherwise. The Prym is superspecial precisely when \(a=0\); its seven-rank is \(2\) with a-number \(1\) at \(a^2=1\), and it is ordinary elsewhere. Here superspeciality at \(a=0\) follows from the standard characterization that an abelian variety of dimension \(d\) has a-number \(d\) exactly when it is superspecial. This yields the entire table.

Finally, the transformation \((x,y)\mapsto(\lambda x,y)\), for \(\lambda^6=-1\), exchanges the parameters \(a\) and \(-a\), because \(\lambda^{12}=1\). The three nonordinary parameter orbits \(\{0\}\), \(\{1,-1\}\), and \(\{\sqrt{-1},-\sqrt{-1}\}\) are therefore each a single geometric isomorphism class. They cannot be mutually isomorphic, since the corresponding Jacobian ranks are \(2,4,3\), respectively.

## Verification
The standalone \(check.py\), run with Python 3 and no third-party packages, independently computes the cubic of the defining polynomials over \(\mathbb F_7\), constructs the full Cartier coefficient matrices for both genera, and checks the diagonal values for every prime-field parameter. It verifies the quotient/Prym rank splits, the singular boundary, and both roots of \(a^2=-1\) using a direct implementation of \(\mathbb F_{49}=\mathbb F_7[u]/(u^2+1)\). Output ends with `ALL_CHECKS_PASSED`. These finite computations corroborate the identities; the proof for every \(a\in k\) comes from the displayed polynomial identities and the semilinear diagonal argument.

## Relationship to prior work
The genus-\(g\) hyperelliptic normal form with extra involutions and its dihedral symmetry are due to Gutiérrez and Shaska [1]. The hyperelliptic Cartier coefficient formula and the theory of rank strata are standard; the genus-four dihedral superspecial algorithms of Ohashi and Kudo [3] give a strong comparison but are for a *different genus and family*. General hyperelliptic rank-strata existence results [2] are not a classification of this one-dimensional genus-five locus. Suresh [4] constructs hyperelliptic families using curves with the same polynomial shape for arithmetic applications, but his inspected treatment of specialization and isogenies does not specify the characteristic-seven Jacobian/Prym rank table. The contribution claimed here is solely the complete four-stratum arithmetic classification and the complementary quotient/Prym superspeciality phenomenon for the displayed genus-five family.

## Limitations
No assertion is made about uniqueness among all genus-five curves, Newton slopes, characteristic-seven stable reduction at \(a^2=4\), or an independently certified novelty claim. The results rely on the precise coefficientwise family and the indicated involution. Historical studies of genus-five Prym varieties or symmetric hyperelliptic curves may contain equivalent special cases. The provided checks do not constitute independent mathematical validation.

## References
[1] J. Gutiérrez and T. Shaska, *Hyperelliptic curves with extra involutions*, arXiv:math/0601456, first posted 2006-01-18. https://arxiv.org/pdf/math/0601456

[2] J. Achter and R. Pries, *The p-rank strata of the moduli space of hyperelliptic curves*, preprint (2011); general rank stratification of hyperelliptic moduli.

[3] R. Ohashi and M. Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858. https://arxiv.org/pdf/2312.16858

[4] A. Suresh, *Realizing Galois representations in abelian varieties by specialization*, arXiv:2206.09778. https://arxiv.org/pdf/2206.09778
