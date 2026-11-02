# A sharp degree-seven bound for bitangent fields, realized by a Klein-quartic twist

## Finding

Let \(C\) be a smooth plane quartic over any finite field \(\mathbb F_q\) of odd characteristic. Define \(d(C)\) to be the least positive integer \(d\) for which \(C\) has a geometrically bitangent line defined over \(\mathbb F_{q^d}\); hyperflex lines are included. Then
\[
d(C)\in\{1,2,3,4,7\}.
\]
In particular \(d(C)\le7\), and the bound is sharp. Indeed the explicit smooth plane quartic
\[
D:\quad X^3Y+2Y^3Z+Z^3X=0\quad\text{over }\mathbb F_{29}
\]
has four Frobenius orbits of length seven on its 28 geometric bitangents. Therefore \(d(D)=7\), and no bitangent of \(D\) is defined over \(\mathbb F_{29^m}\) for \(1\le m\le6\).

For the full abstract symplectic action on the 28 odd theta characteristics, there are exactly 25 distinct cycle spectra. The least-cycle-length multiplicities among its 1,451,520 elements are respectively 984,852, 71,820, 96,768, 90,720, and 207,360 for the five values \(1,2,3,4,7\). This full group enumeration supplies the universal restriction; it does **not** assert that every spectrum is realized by a quartic over every finite field.

## Assumptions and scope

A bitangent is an \(\overline{\mathbb F}_q\)-line whose scheme-theoretic intersection with the smooth quartic is an even effective divisor (including a hyperflex, whose intersection is quadruple at one point). Its field of definition refers to the line, not necessarily to its individual contact points. In odd characteristic, the 28 geometric bitangents form the 28-point finite étale scheme corresponding to the odd theta characteristics of the canonical genus-three curve. The stated universal theorem includes every odd characteristic, but the explicit sharp example has characteristic 29.

The least degree \(d(C)\) is the minimum **orbit length** of Frobenius on the 28 lines. The statement is not that a fixed seventh-degree extension works for every quartic: the least degrees 2, 3, or 4 need not divide 7.

## Proof

**1. Reduction to the finite symplectic action.** The Jacobian's two-torsion \(V=J(C)[2](\overline{\mathbb F}_q)\) is a six-dimensional symplectic vector space over \(\mathbb F_2\). Theta characteristics identify Frobenius-equivariantly with quadratic refinements of the Weil pairing; the 28 odd refinements are characterized by Arf invariant one. Hence Frobenius acts on the 28 bitangents through an element of \(\operatorname{Sp}_6(\mathbb F_2)\). Under a symplectic basis, write
\[
q_0(u_1,u_2,u_3,v_1,v_2,v_3)=u_1v_1+u_2v_2+u_3v_3,
\quad q_c(x)=q_0(x)+\langle c,x\rangle.
\]
The odd subset consists of the 28 vectors \(c\) with \(q_0(c)=1\). A transvection \(t_w(x)=x+\langle x,w\rangle w\) acts on refinements by a permutation computed exactly from this formula.

**2. Exhaustive, independently reproduced finite classification.** The 18 explicit nonzero transvection vectors in `theta_generators.txt` generate a subgroup of order 1,451,520 in the 28-point permutation action. Since
\[
|\operatorname{Sp}_6(\mathbb F_2)|=2^9(2^2-1)(2^4-1)(2^6-1)=1,451,520,
\]
they generate the full group. `verify_theta_permutations.cpp` exhaustively composes those permutations, while `verify_symplectic_matrices.cpp` independently exhaustively constructs the six-by-six binary symplectic matrices and computes their actions on odd refinements. Both programs yield exactly the same 25 cycle partitions and multiplicities (see `group_cycle_spectra.csv` and the two execution outputs). The only minima are \(1,2,3,4,7\), with counts stated above, and each element having minimum 7 has partition \((7,7,7,7)\). This proves the universal restriction; it is a finite *exhaustive* certificate, not an experimental sample.

**3. Rational bitangents on the untwisted quartic.** Put \(K:X^3Y+Y^3Z+Z^3X=0\) over \(\mathbb F_{29}\). The partial-derivative equations imply that a singular point would satisfy \(a=b=c=0\) for \(a=X^3Y\), \(b=Y^3Z\), and \(c=Z^3X\), because the determinant of the associated coefficient matrix is 28, invertible modulo 29. No projective nonzero coordinate triple with all three monomials zero is singular; thus \(K\) is smooth.

Enumerate the 871 lines of \(\mathbb P^{2\vee}(\mathbb F_{29})\) and the 871 projective square classes of binary quadratic forms. Exactly 28 line sections of \(K\) are scalar multiples of squares of quadratic forms; they are the 28 distinct lines \(aX+bY+Z=0\) listed in `bitangents_F29.csv`. For \(Z=-aX-bY\), the section is
\[
-a^3X^4+(1-3a^2b)X^3Y-3ab^2X^2Y^2-(a+b^3)XY^3-bY^4.
\]
For each listed pair \((a,b)\), setting \(\lambda=-a^3\), \(u=(1-3a^2b)/(2\lambda)\), and \(v=[-3ab^2/\lambda-u^2]/2\) gives precisely \(\lambda(X^2+uXY+vY^2)^2\) in \(\mathbb F_{29}[X,Y]\). The independent coefficient checks are in `verify_f29.py`. A smooth plane quartic has exactly 28 geometric bitangents; thus *all* bitangents of \(K\) are rational over \(\mathbb F_{29}\). None of the coordinate lines is bitangent, since its section consists of a triple and a simple intersection.

**4. Kummer twist giving sharpness.** The element 2 is not a seventh power in \(\mathbb F_{29}\), since \(2^4=16\ne1\). Choose \(\beta\) with \(\beta^7=2\) in \(\mathbb F_{29^7}\). The projective change of variables
\[
(X,Y,Z)\longmapsto(\beta X,\beta^4Y,\beta^2Z)
\]
takes the equation of \(D\) to twice the equation of \(K\). The arithmetic Frobenius obeys \(\beta^{29}=16\beta\); \(\zeta=16\in\mathbb F_{29}\) has exact order seven. On the 28 split bitangents of \(K\), twisted Frobenius is therefore, up to inverse, induced by
\[
g=\operatorname{diag}(\zeta,\zeta^4,\zeta^2)\in\operatorname{PGL}_3(\mathbb F_{29}).
\]
For each \(1\le j\le6\), the eigenvalues of \(g^j\) are distinct; its only invariant lines in the dual plane are the three coordinate lines. As none of these is bitangent to \(K\), no proper positive power \(g^j\) with \(j<7\) fixes any bitangent. Since \(g^7=1\), the 28 lines decompose into exactly four orbits of length seven. The geometric equivalence to smooth \(K\) proves the smoothness of \(D\) as well. This proves sharpness and the exact field-of-definition claim.

## Verification

Run with Python 3 and a C++17 compiler from the directory containing all accompanying files:

```sh
python3 verify_f29.py
c++ -std=c++17 -O2 verify_theta_permutations.cpp -o verify_theta
c++ -std=c++17 -O2 verify_symplectic_matrices.cpp -o verify_matrices
./verify_theta > result_theta.txt
./verify_matrices > result_matrices.txt
python3 verify_consistency.py
```

The finite-field check independently enumerates 871 rational lines, verifies 28 explicit square identities, and checks the seventh-root Frobenius multiplier. The two symplectic enumerators independently produce 1,451,520 elements and identical 25-cycle spectra. The consistency script checks these against the exact multiplicities above. These computations establish the finite group lemma and the explicit finite-field certificate; the theorem also uses the classical, rigorous theta-characteristic correspondence and the written Kummer descent argument.

## Relationship to prior work

The bitangent/odd-theta correspondence, the symplectic action, and the existence of 28 bitangents are classical. Dalla Piazza–Fiorentino–Salvati Manni (2014) explicitly develop the matrix of bitangents and the symplectic action; the ATLAS lists the 28-point permutation representation of \(\operatorname{Sp}_6(\mathbb F_2)\). Meagher–Top (preprint dated 2010-03-10, §8) classify twists of the Klein quartic and Frobenius traces of their Jacobians, including order-seven automorphisms; they do not evaluate the uniform least bitangent-field degree or the 28-bitangent orbit decomposition of the particular twist displayed here.

These inputs are not claimed as new. The point proved here is their *combined sharp arithmetic implication*: the complete universal least-degree restriction and an explicitly certified plane quartic over \(\mathbb F_{29}\) with no bitangent below degree seven. An earlier computation of the untwisted Klein quartic's split 28-bitangent configuration over \(\mathbb F_{29}\), or an arithmetic classification involving only the number of first-field rational bitangents, does not itself give this twist's four degree-seven orbits. The group computation and twist construction are explicitly presented for comparison against known representation tables and existing twist literature.

## Limitations

The finite symplectic enumeration gives restrictions on possible Frobenius orbit structures, not a realization theorem for every abstract class over every finite field. The bound concerns *some* bitangent and the minimal extension degree, not the common field of definition of all 28. No claim is made about characteristic two, whose classical bitangent theory differs, or about contact points being rational over the same field as their bitangent lines. Historical priority for the combined minimal-degree statement remains subject to older permutation and twist literature, including classical group tables; an inaccessible full historical dissertation was not used as negative evidence.

## References

- S. Meagher and J. Top, *Twists of genus three curves over finite fields*, publicly dated preprint March 10, 2010; *Finite Fields and Their Applications* **16** (2010), 347–368, doi:10.1016/j.ffa.2010.06.001. Open author manuscript: https://home.mathematik.uni-freiburg.de/arithgeom/TwistsGenThreeCurve.pdf (especially §8).
- F. Dalla Piazza, A. Fiorentino and R. Salvati Manni, *Plane quartics: the matrix of bitangents*, arXiv:1409.5032, first version September 17, 2014; https://arxiv.org/abs/1409.5032.
- ATLAS of Finite Group Representations, *\(S_6(2)\): permutation representation on 28 points*; https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/S62G1-p28B0.
- S. Meagher, *Twists of genus three curves and their Jacobians*, doctoral dissertation (2008), University of Groningen research portal; complete PDF access not obtained in this review.
