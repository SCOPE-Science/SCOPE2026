# Normal-crossings nonordinary locus and exact rank counts for characteristic-three Ciani quartics

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\). For \((r,s,t)\in k^3\), set
\[
C_{r,s,t}: X^4+Y^4+Z^4+rX^2Y^2+sY^2Z^2+tZ^2X^2=0.
\]
Write \(\Delta=r^2+s^2+t^2-rst-1\) and restrict to the smooth parameter space
\[
U=\{(r,s,t): (r^2-1)(s^2-1)(t^2-1)\Delta\ne0\}.
\]
Define \(h_X=s+rt\), \(h_Y=t+rs\), and \(h_Z=r+st\). For every geometric parameter in \(U\), the curve is a smooth nonhyperelliptic curve of genus \(3\), with Jacobian \(3\)-rank and \(a\)-number
\[
f_3(C_{r,s,t})=\mathbf 1_{h_X\ne0}+\mathbf 1_{h_Y\ne0}+\mathbf 1_{h_Z\ne0},\qquad
 a(C_{r,s,t})=3-f_3(C_{r,s,t}).
\]
The reduced nonordinary divisor \(D=V(h_Xh_Yh_Z)\cap U\) has **simple normal crossings**. Its three components are smooth geometrically irreducible rational surfaces; their pairwise intersections are precisely the three coordinate axes inside \(U\), and their only triple intersection is the origin. In particular, the unique smooth coefficient-marked superspecial parameter is \((r,s,t)=(0,0,0)\), while rank-one parameters are exactly the three punctured axes with their \(\pm1\) points deleted.

For every finite field \(\mathbb F_q\) with \(q=3^m\), \(m\ge1\), the exact number \(N_j(q)\) of smooth **ordered coefficient triples** defined over \(\mathbb F_q\) with geometric Jacobian \(3\)-rank \(j\) is
\[
\begin{aligned}
N_0(q)&=1,\\
N_1(q)&=3(q-3),\\
N_2(q)&=3(q-3)(q-5),\\
N_3(q)&=(q-3)(q^2-7q+18).
\end{aligned}
\]
Their sum is \((q-2)^3-(q-3)^2\). These formulas count **equations in the fixed standard coordinates**, not isomorphism classes of curves.

## Assumptions and scope

Throughout, characteristic is exactly \(3\). Geometric rank refers to the \(p\)-rank of the Jacobian over an algebraic closure; it agrees with the stable semilinear Hasse--Witt rank. All geometric divisor claims are on \(U\), not on the ambient affine space including singular curves. The three Hasse surfaces are indexed by the fixed coordinate system and must not be interpreted as distinct moduli divisors after quotienting by coordinate changes.

## Proof

**1. Smoothness criterion.** Let \(F\) be the homogeneous quartic in the statement. In characteristic \(3\), its gradient is
\[
(F_X,F_Y,F_Z)=\bigl(X(X^2-rY^2-tZ^2),\;Y(Y^2-rX^2-sZ^2),\;Z(Z^2-sY^2-tX^2)\bigr).
\]
No point of \(C\) with two vanishing homogeneous coordinates exists. On a coordinate line the simultaneous derivative equations have a nonzero solution exactly when the matching parameter square is \(1\). When all three coordinates are nonzero, the gradient equations become a homogeneous linear system in \((X^2,Y^2,Z^2)\) with determinant \(-\Delta\). If no parameter square is \(1\), any kernel vector of this system has all three entries nonzero; over \(k\) each can be realized by coordinate squares. Euler's identity \(4F=XF_X+YF_Y+ZF_Z\), with \(4=1\) in characteristic \(3\), then guarantees the point lies on the curve. This proves the claimed smoothness criterion (equivalently, Ohashi's Lemma 2.1 specialized to characteristic \(3\)). A smooth plane quartic has genus \(3\).

**2. Cartier--Manin diagonalization.** For a smooth plane quartic in characteristic \(p=3\), use the canonical basis represented by \(X,Y,Z\). The Hasse--Witt coefficient matrix is obtained from the monomial coefficients of \(F^{p-1}=F^2\); its \((i,j)\) entry is the coefficient whose exponent vector is \((p-1,p-1,p-1)+p e_i-e_j\), where \(e_i\) is the corresponding unit vector. All monomials of \(F^2\) have even exponents, so the off-diagonal entries vanish. Direct multiplication gives
\[
H=\operatorname{diag}\bigl(2(s+rt),\;2(t+rs),\;2(r+st)\bigr).
\]
Transpose or Frobenius-twist conventions do not change the ranks. Every Frobenius iterate remains diagonal and an entry stays nonzero under every positive Frobenius power. Therefore the stable Hasse--Witt rank is the number of nonzero displayed entries; the Cartier rank is the same, and the stated formulas for \(f_3\) and \(a\) follow.

**3. Intersection geometry.** Each \(V(h_i)\) is a graph isomorphic to an affine plane; for example \(h_X=0\) means \(s=-rt\). On this graph, \(\Delta=-(r^2-1)(t^2-1)\), so its intersection with \(U\) is the complement of the curves \(r=\pm1\), \(t=\pm1\), and \(rt=\pm1\), hence is smooth and geometrically irreducible. On \(V(h_X,h_Y)\), substitution gives \(t(1-r^2)=0\), and on \(U\) therefore \(s=t=0\). Cyclic permutations show that the three pairwise intersections are the corresponding coordinate axes with the \(\pm1\) points removed. The triple intersection is exactly the origin. Along the \(r\)-axis the gradients of \(h_X,h_Y\) are \((0,1,r)\) and \((0,r,1)\); their independent normal directions have determinant \(1-r^2\ne0\) on \(U\). The other axes are symmetric. At the origin, the gradients of all three equations form a permutation matrix. Thus \(D\) has simple normal crossings at every point of \(U\).

**4. Universal finite-field census.** Let \(q=3^m\) and \(T=\mathbb F_q\setminus\{\pm1\}\). For \(r,s\in T\), the equation \(\Delta=0\) is quadratic in \(t\), with discriminant \((r^2-1)(s^2-1)\ne0\). Let \(\chi\) be the quadratic character, extended by \(\chi(0)=0\). The classical elementary identity \(\sum_{u\in\mathbb F_q}\chi(u^2-1)=-1\) follows by counting pairs satisfying \(u^2-v^2=1\) via \((u-v)(u+v)=1\). Therefore the number of triples with \(r,s\in T\), \(t\in\mathbb F_q\), and \(\Delta=0\) is
\[
(q-2)^2+\Bigl(\sum_{u\in T}\chi(u^2-1)\Bigr)^2=(q-2)^2+1.
\]
At \(t=1\), \(\Delta=(r+s)^2\); at \(t=-1\), \(\Delta=(r-s)^2\). Exactly \(q-2\) solutions are removed at each excluded value of \(t\). Hence the singular discriminant surface contains exactly \((q-3)^2\) triples in \(T^3\), and the smooth family has \((q-2)^3-(q-3)^2\) rational parameter triples.

On \(V(h_X)\), the variables \((r,t)\) range through \(T^2\), except that \(rt=\pm1\) is forbidden. Each of the \(q-3\) nonzero \(r\in T\) has exactly two forbidden values of \(t\), so this Hasse component has \((q-2)^2-2(q-3)=q^2-6q+10\) rational points. Within it, the union of the two pairwise intersection axes has \(2(q-2)-1=2q-5\) points. Thus the number of rank-two parameters, on precisely one Hasse component, is \(3(q^2-8q+15)=3(q-3)(q-5)\). The pairwise intersections away from the origin give \(3(q-3)\) rank-one parameters, and the origin contributes the sole rank-zero parameter. Subtracting these from the smooth total yields the stated formula for \(N_3(q)\).

## Verification

Run `python3 verify_symbolic.py` with SymPy installed. It expands the quartic coefficient formula in characteristic \(3\), verifies all relevant discriminant identities and the triple-intersection Jacobian determinant, and checks the polynomial count identities. Run `python3 verify_fields.py` using only the Python standard library. It independently enumerates all ordered coefficients in explicit polynomial-basis models of \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\), testing smoothness and all Hasse values directly. Results:

| \(q\) | Smooth triples | Rank \(0\) | Rank \(1\) | Rank \(2\) | Rank \(3\) |
|---:|---:|---:|---:|---:|---:|
| 3 | 1 | 1 | 0 | 0 | 0 |
| 9 | 307 | 1 | 18 | 72 | 216 |
| 27 | 15,049 | 1 | 72 | 1,584 | 13,392 |

The infinite-field assertions and all-extension count formulas are proved algebraically; the three finite censuses alone would not establish them.

## Relationship to prior work

Ohashi (arXiv:2201.12996, January 31, 2022) studies this **same standard Ciani family**, proves the smoothness criterion in Lemma 2.1, describes its elliptic quotients and prime-to-characteristic isogeny in Section 3, and proves arithmetic properties of superspecial members. All those facts are established prior work and are not claimed here. The specific new conclusion assessed here is the **full characteristic-three coefficient-space normal-crossings geometry, its rank-stratum decomposition, and the four uniform polynomials counting every rank over all finite extensions**. This requires additional characteristic-three coefficient identities and a discriminant-conic character-sum count; it is not asserted to be a new general decomposition theorem.

Ohashi--Kudo--Harashita (arXiv:2111.09777) treat a different cyclic-automorphism family with characteristic expressly different from \(3\), and recall that Ciani Jacobians already admit a three-elliptic decomposition. Bouw and collaborators (arXiv:2003.07633 and arXiv:2310.10416) examine stable-reduction and conductor questions for Ciani families. Their abstracts indicate related but different invariants; their full contents were not established to be disjoint from every counting formula. A previously available characteristic-seven Ciani rank-stratification calculation concerns the same polynomial family over a different characteristic and does not imply these characteristic-three counts. No source inspected here explicitly states the normal-crossings and uniform coefficient-count theorem, but this is a best-knowledge priority assessment rather than an exhaustive literature certification.

## Limitations

The strata live in the chosen **coefficient space**, not a fine moduli space of isomorphism classes. The formulas count ordered coefficient triples, so parameter symmetries are not quotiented out. The theorem does not determine zeta functions of individual curves, Ekedahl--Oort types beyond the \(a\)-number, or stable reduction at the excluded singular parameters. General elliptic-quotient results already give a route to the rank classification; the assessed structural contribution is the detailed normal-crossings incidence and all-extension count polynomial. Unindexed equivalent earlier calculations cannot be ruled out, and no independent external mathematical audit has been performed.

## References

1. R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996 (first public January 31, 2022); journal title *Maximality of Ciani curves over finite fields*, *Finite Fields and Their Applications* 83 (2022), 102089. https://arxiv.org/abs/2201.12996
2. R. Ohashi, M. Kudo and S. Harashita, *The \(a\)-numbers of non-hyperelliptic curves of genus 3 with cyclic automorphism group of order 6*, arXiv:2111.09777 (first public November 18, 2021). https://arxiv.org/abs/2111.09777
3. I. Bouw, N. Coppola, P. Kılıçer, S. Kunzweiler, E. Lorenzo García and A. Somoza, *Reduction type of genus-3 curves in a special stratum of their moduli space*, arXiv:2003.07633 (first public March 17, 2020). https://arxiv.org/abs/2003.07633
4. I. Bouw, N. Coppola, E. Lorenzo García and A. Somoza, *On the conductor of Ciani plane quartics*, arXiv:2310.10416 (first public October 16, 2023). https://arxiv.org/abs/2310.10416
