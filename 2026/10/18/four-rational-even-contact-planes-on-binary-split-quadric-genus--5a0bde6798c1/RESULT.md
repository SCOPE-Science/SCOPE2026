# Four rational even-contact planes on binary split-quadric genus-four curves

## Finding
Let \(Q=\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\subset\mathbf P^3_{\mathbf F_2}\) be the split Segre quadric. For a nonzero bidegree-\((3,3)\) form \(F\), suppose \(C_F\subset Q\) is geometrically smooth. Let \(e(F)\) be the number of \(\mathbf F_2\)-rational planes \(H\subset\mathbf P^3\) such that the geometric intersection divisor \(H|_{C_F}\) equals \(2D\) for some effective geometric divisor \(D\) of degree three, **without requiring \(D\) reduced**. Then
\[e(F)\le4.\]
Exactly **60** of the \(65,535\) nonzero coefficient vectors have \(e(F)=4\) and are geometrically smooth. They form three orbits under \(\operatorname{Aut}_{\mathbf F_2}(Q)\cong(\operatorname{PGL}_2(\mathbf F_2)^2)\rtimes C_2\), of order \(72\):

| Representative hexadecimal mask | Orbit size | Stabilizer order | Divisor contact partitions among the four planes |
|---|---:|---:|---|
| `0x29e3` | 18 | 4 | three \((2,2,2)\); one \((6)\) |
| `0x2de6` | 36 | 2 | two \((2,2,2)\); one \((4,2)\); one \((6)\) |
| `0x7889` | 6 | 12 | one \((2,2,2)\); three \((6)\) |

In particular, a smooth embedded genus-four curve over \(\mathbf F_2\) can have three distinct rational planes with sextuple contact; the six coefficient vectors realizing this configuration comprise one orbit.

## Assumptions and scope
Use homogeneous coordinates \(([s:t],[r:w])\) and encode the coefficient of \(s^i t^{3-i}r^j w^{3-j}\), for \(0\le i,j\le3\), in bit \(4i+j\) of a 16-bit integer. There is only one nonzero scalar in \(\mathbf F_2\), so the nonzero masks enumerate all projective equations exactly once. Smooth means geometrically smooth over the algebraic closure; it is not merely smooth at rational points. For smooth \((3,3)\) divisors the adjunction formula gives genus \((3-1)(3-1)=4\), and \(\mathcal O_Q(1,1)\) restricts to the canonical embedding. The intersection \(H|_C\) has degree six.

The definition counts **all even-contact planes**, including contact partitions \((4,2)\) and \((6)\); a *proper* tritangent would require partition \((2,2,2)\). The claim is for the indicated split-quadric canonical models only, not for nonsplit quadrics, quadric cones, hyperelliptic genus-four curves, or arbitrary finite fields.

## Proof
Every rational plane intersects \(Q\) in the zero divisor of a nonzero bidegree-\((1,1)\) form. A coefficient matrix has rank two for six planes and rank one for the other nine.

For a rank-two matrix \(M=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\operatorname{GL}_2(\mathbf F_2)\), the smooth section is parametrized by \(([s:t],[bs+dt:as+ct])\). Substitution into \(F\) gives a homogeneous binary sextic \(h_M(s,t)\). The plane is even-contact exactly when \(h_M\) is a square of a homogeneous cubic, equivalently to the vanishing of the coefficients of \(s^5t\), \(s^3t^3\) and \(st^5\). This is a system of three linear equations on the 16 coefficients of \(F\). The equivalence holds geometrically because a binary form with even zero multiplicities is a square over an algebraically closed field; its coefficients here descend to \(\mathbf F_2\), which is perfect.

For a rank-one matrix, the section is the union of a vertical and a horizontal ruling fibre meeting at the rational point \(P=(P_x,P_y)\). Because a smooth \((3,3)\) curve cannot contain either fibre, the degree-three restrictions must both contain \(P\), and the residual intersection divisors away from \(P\) must be even. Equivalently, on the two fibres the restrictions must have the forms \(\ell_{P_y}q_y^2\) and \(\ell_{P_x}q_x^2\), respectively, where the linear factors \(\ell\) vanish at the specified rational points. These impose four explicit homogeneous linear equations on \(F\) (one is redundant). Their satisfaction is exactly the condition that the divisor of the product of the two fibre equations on \(C\) is even.

Enumerating all \(2^{16}-1=65,535\) coefficient vectors against these 15 systems gives counts \(5,824,23,280,21,840,5,180,8,400,560,210,240,1\) for respectively \(e=0,1,2,3,4,6,7,8,15\), with no other values. There are thus precisely \(1,011\) masks with \(e>4\). Independent direct evaluation of \(F\) and its two local partial derivatives on four affine charts locates geometric singularities for all of them: \(1,009\) have a singular point over \(\mathbf F_2\), and the remaining two have one over \(\mathbf F_4\). Consequently no geometrically smooth curve has more than four even-contact planes.

Among the \(8,400\) masks with exactly four even-contact planes, \(8,280\) already have a singular point over \(\mathbf F_2\), and a further \(60\) have a singular point over \(\mathbf F_4\). For each of the remaining \(60\), the Gröbner basis of \((f,\partial f/\partial u,\partial f/\partial v)\) is the unit ideal on **each** of the four affine charts. This exact algebraic test rules out singularities over every extension field. Thus precisely these 60 curves are geometrically smooth. Applying the 72 substitution automorphisms of \(Q\) to their 16-bit coefficients gives three orbits of sizes \(18,36,6\) with listed representatives.

To distinguish contacts, on a smooth \((1,1)\) plane section take the square root \(g\) of \(h_M\). Three simple geometric roots of \(g\) give \((2,2,2)\), a repeated double root gives \((4,2)\), and a triple root gives \((6)\). For a reducible section, the two residual linear factors \(q_x,q_y\) determine whether the crossing point appears twice or four times. These exact tests give the partitions displayed in the table; the group action preserves them.

As an explicit witness, mask `0x7889` encodes
\[F=t^3w^3+t^3r^3+st^2r^3+s^2tr^3+s^3w^3+s^3rw^2+s^3r^2w.\]
Its four even-contact rank-two planes have square-root cubic restrictions, respectively, \(t^3\), \(st(s+t)\), \(s^3\), and \((s+t)^3\) under the six graph parametrizations specified in the verification code. The three sextuple contacts occur at the three distinct rational points \(([1:0],[1:0])\), \(([0:1],[1:1])\) and \(([1:1],[0:1])\), and the remaining plane has contact divisor twice their sum.

## Verification
The complete reproducible certificate is in `code/census_genus4_tritangents.py`, `code/verify_even_contact.py`, and `code/contact_profiles.py`. From the package root, execute `python code/verify_even_contact.py` and `python code/contact_profiles.py` with a Python environment supporting SymPy. The former enumerates all 65,535 masks, gives independently evaluated explicit \(\mathbf F_2\)/\(\mathbf F_4\) singular witnesses for every excluded extremal candidate, performs four-chart exact Gröbner tests on all 60 survivors, and checks the full automorphism orbit partition. The latter checks all four contact partitions on each orbit representative. `data/verify_even_contact_output.json` and `data/contact_profiles_output.txt` contain the reproduced expected results. These are finite exhaustive calculations, not statistical samples; the unit-ideal test is over the algebraic closure.

## Relationship to prior work
Xarles, *A census of all genus 4 curves over the field with 2 elements* (2020, arXiv:2007.07822), classifies the underlying genus-four curves and tabulates point counts and Weil polynomials, rather than this even-contact extremal stratification. Kulkarni, Ren, Sayyary Namin and Sturmfels, *Real Space Sextics and their Tritangents* (2017, arXiv:1712.06274), study characteristic-zero real tritangents, and do not give this characteristic-two arithmetic bound. Previous finite counts restricted to **proper** rational tritangents with three distinct geometric contact points do not determine the extra \((4,2)\) and \((6)\) planes; in particular the present four-plane extremum requires nonreduced contact.

## Limitations
This is a complete classification of **embedded coefficient vectors** attaining the four-plane extremum, modulo automorphisms of the split quadric. It is not a classification of every possible theta characteristic in characteristic two, and the term even-contact must not be silently replaced by proper tritangent. The proof relies on explicit finite computations with included source rather than a uniform theorem over arbitrary fields. An earlier unindexed computation of the same contact statistic cannot be excluded by literature searches, and an independent audit has not been performed.

## References
- X. Xarles, *A census of all genus 4 curves over the field with 2 elements*, arXiv:2007.07822 (first public version 2020-07-15), https://arxiv.org/pdf/2007.07822.
- A. Kulkarni, Y. Ren, M. Sayyary Namin, B. Sturmfels, *Real Space Sextics and their Tritangents*, arXiv:1712.06274 (first public version 2017-12-18), https://arxiv.org/pdf/1712.06274.
- C. Harris, Y. Len, *Tritangent planes to space sextics: the algebraic and tropical stories*, arXiv:1701.02353 (2017), https://arxiv.org/abs/1701.02353.
