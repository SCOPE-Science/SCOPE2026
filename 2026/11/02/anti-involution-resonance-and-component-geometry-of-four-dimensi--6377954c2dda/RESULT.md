# Anti-involution resonance and component geometry of four-dimensional quantum complete intersections

## Finding
Let \(k\) be any field and \(\lambda\in k^\times\). On the four-dimensional unital associative algebra
\[
 A_\lambda=k\langle x,y\rangle/(x^2,y^2,xy+\lambda yx),
 \qquad z=xy,
\]
consider all **\(k\)-linear anti-involutions**: bijective \(k\)-linear maps \(\sigma\) satisfying \(\sigma(ab)=\sigma(b)\sigma(a)\) and \(\sigma^2=\mathrm{id}\). Every such map fixes \(1\), preserves the radical \(J=(x,y,z)\), and is uniquely determined by its two images of the form
\[
 \sigma(x)=a x+c y+u z,\qquad
 \sigma(y)=b x+d y+v z,
\]
where \(L=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\operatorname{GL}_2(k)\). The complete parameter classification is as follows.

1. **Nonresonant** \(\lambda\notin\{1,-1\}\): exactly
\[
 \sigma(x)=s y+t z,\qquad
 \sigma(y)=s^{-1}x-s^{-1}t z,\qquad \sigma(z)=z,
 \quad s\in k^\times,\ t\in k.
\]
2. **Commutative resonance**, \(\lambda=-1\) and \(\operatorname{char}k\ne2\): the nonresonant-style antidiagonal family above, together with four disjoint diagonal families
\[
 \sigma(x)=\epsilon x+u z,\quad \sigma(y)=\delta y+v z,
 \qquad \epsilon,\delta\in\{1,-1\},
 \quad (1+\delta)u=(1+\epsilon)v=0,
 \quad \sigma(z)=\epsilon\delta z.
\]
3. **Exterior resonance**, \(\lambda=1\) and \(\operatorname{char}k\ne2\): take any \(L\in\operatorname{GL}_2(k)\) with \(L^2=I\), and any row vector \(h=(u,v)\) satisfying \(hL=(\det L)h\); then \(\sigma(z)=-(\det L)z\). Every anti-involution occurs uniquely this way.
4. **Characteristic-two coalescence**, \(\lambda=1=-1\) and \(\operatorname{char}k=2\): take \(L=I+N\), \(N^2=0\), and any row vector \(h=(u,v)\) with \(hN=0\); then \(\sigma(z)=z\). Every anti-involution occurs uniquely this way.

The reduced anti-involution variety over any algebraic closure has, respectively, **\(1,5,3,1\)** geometrically irreducible components in cases 1–4. Their respective dimension lists (with multiplicity) are
\[
 (2),\qquad (2,2,1,1,0),\qquad(3,2,0),\qquad(3).
\]
The first variety is \(\mathbb G_m\times\mathbb A^1\); the last variety is irreducible despite possessing a special closed affine-plane sublocus with \(L=I\).

For \(k=\mathbb F_q\), the **exact numbers of anti-involutions**, in the same four regimes, are
\[
 \boxed{q(q-1),\qquad 2q^2+q+1,\qquad q^3+2q^2+1,\qquad q^3+q^2-q.}
\]
These are actual maps, not conjugacy classes. Their complete fixed-space spectra \(F_j=\#\{\sigma:\dim_k\ker(\sigma-I)=j\}\) are:

| Regime | Nonzero \(F_j\) |
| --- | --- |
| \(\lambda\notin\{1,-1\}\) | \(F_3=q(q-1)\) |
| \(\lambda=-1\), odd characteristic | \(F_2=q^2+2q\), \(F_3=q(q-1)\), \(F_4=1\) |
| \(\lambda=1\), odd characteristic | \(F_1=1\), \(F_3=q^3+2q^2\) |
| \(\lambda=1\), characteristic two | \(F_3=q^3+q^2-q-1\), \(F_4=1\) |

All other fixed-space multiplicities vanish. For example, over \(\mathbb F_5\), parameters \(\lambda=2,-1,1\) give respectively \(20,56,176\) anti-involutions; over \(\mathbb F_4\), parameters \(\lambda\ne1\) give \(12\) and \(\lambda=1\) gives \(76\).

## Assumptions and scope
The algebra is unital, has \(k\)-basis \(1,x,y,z\), and has products \(x^2=y^2=0\), \(xy=z\), \(yx=-\lambda^{-1}z\), and \(Jz=zJ=0\). No restriction on perfection, algebraic closedness, or characteristic is imposed in the structural and geometric statements. Geometric components always refer to the reduced variety after passing to an algebraic closure; nonreduced scheme structure is not claimed. The finite-field formulas apply to every prime power and each permitted nonzero parameter.

## Proof
**Normal form.** Since \(A_\lambda\) is local with radical \(J\), every bijective anti-homomorphism fixes \(1\), preserves \(J\), and induces an invertible linear map on \(J/J^2\). Since \(J^2=kz\) and \(J^3=0\), its action on \(x,y\) has the displayed \(L,h\) form; its value on \(z=xy\) must equal \(\sigma(y)\sigma(x)\). Conversely, an invertible \(L\) and a compatible image pair respecting the reversed defining relations determine a bijective anti-homomorphism because the induced map on \(J/J^2\) is invertible and the coefficient of \(z\) is also nonzero.

**Square-zero and reversed commutation.** For \(w=\alpha x+\beta y+\gamma z\), one has \(w^2=(1-\lambda^{-1})\alpha\beta z\). Hence for \(\lambda\ne1\) each column of \(L\) has at most one nonzero entry, and invertibility makes \(L\) monomial. For a diagonal \(L\), applying the reversed relation gives \(\lambda^2=1\). For an antidiagonal \(L\), the reversed relation holds for every \(\lambda\). Thus the nonresonant linear part is antidiagonal and, when \(\lambda=-1\) in odd characteristic, diagonal parts also occur. With \(\sigma(x)=s y+u z\), \(\sigma(y)=t x+v z\), one has \(\sigma(z)=st z\). Direct substitution into \(\sigma^2=I\) forces \(st=1\) and \(v=-u/s\), giving the first family. In the commuting case \(yx=xy\), a diagonal part with scalars \(\epsilon,\delta\) must have \(\epsilon^2=\delta^2=1\) and the correction constraints shown above; these are also sufficient.

**Exterior resonance.** For \(\lambda=1\), every linear combination of \(x,y\) squares to zero. For any invertible \(L\) the reversed commutation relation holds, and \(\sigma(z)=-(\det L)z\). The two equations \(\sigma^2(x)=x\), \(\sigma^2(y)=y\) are exactly \(L^2=I\) and \(hL=(\det L)h\). In odd characteristic such \(L\) is diagonalizable with eigenvalues \(\pm1\). Its three possibilities are \(I\), \(-I\), or one eigenvalue of each sign. For \(L=I\), \(h\) is arbitrary (dimension two); for \(L=-I\), \(h=0\); in the mixed case \(h\) is a one-dimensional left \(-1\)-eigenspace. The mixed \(L\)'s form the irreducible conjugacy orbit \(\operatorname{GL}_2/(\mathbb G_m)^2\), of dimension two, and their \(h\)'s form a rank-one vector bundle. The \(I\) and \(-I\) fibers are disjoint and closed because the three traces are distinct. This proves three components of dimensions \(2,0,3\).

**Characteristic two.** For \(\lambda=1\), write \(L=I+N\). The condition \(L^2=I\) is \(N^2=0\), hence \(\det L=1\), and \(hL=(\det L)h\) is \(hN=0\). The square-zero cone of \(2\)-by-\(2\) matrices consists of \(N=\left(\begin{smallmatrix}a&b\\c&a\end{smallmatrix}\right)\) with \(a^2+bc=0\); it is irreducible of dimension two. Over its nonzero locus each \(N\) has rank one and the space of rows \(h\) annihilating its image is one-dimensional. Hence the total incidence locus over nonzero \(N\) is irreducible of dimension three. Its closure contains all \((0,h)\): if \(h\ne0\), choose a nonzero square-zero \(N_0\) with image \(\ker h\), and specialize \((tN_0,h)\) as \(t\to0\); the zero row is immediate. Thus the entire reduced variety is irreducible of dimension three.

**Counts and fixed spaces.** Over \(\mathbb F_q\), the nonresonant family has \((q-1)q\) points. In the commuting odd-characteristic case the four diagonal fibers have \(1,q,q,q^2\) points, and the antidiagonal component has \(q(q-1)\), giving \(2q^2+q+1\). In the exterior odd-characteristic case the mixed \(L\) orbit has \(|\operatorname{GL}_2(q)|/(q-1)^2=q(q+1)\) points; each has \(q\) corrections. Together with \(q^2\) corrections over \(L=I\) and one over \(-I\), this gives \(q^3+2q^2+1\). In characteristic two the \(2\)-by-\(2\) square-zero matrices consist of zero and \(q^2-1\) nonzero matrices; the \(h\)-fibers have \(q^2\) and \(q\) points, giving \(q^3+q^2-q\). Finally, computing the rank of \(\sigma-I\) on the four-element basis in each normal-form stratum gives the stated fixed-space histograms. In the antidiagonal family that rank is one; in the odd commuting diagonal branches it is zero only at the identity and otherwise two; in the odd exterior branches it is three only at \(-I\) and otherwise one; in the characteristic-two branch it is zero only at \((N,h)=(0,0)\) and otherwise one. These rank assertions follow directly by the displayed matrices and are verified computationally below.

## Verification
The standalone `check_quantum_anti.py` performs independent enumeration of every invertible linear part \(L\) and every possible radical correction \(h\), using the original four-dimensional multiplication table rather than the normal-form equations. It verifies the reversed defining relations, the full square identity \(\sigma^2=I\) on all four basis elements, and the rank of \(\sigma-I\) by finite-field Gaussian elimination. The tests exhaust nine parameter/field pairs over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\); the \(\mathbb F_4\) implementation uses genuine polynomial-reduced extension-field arithmetic. The exact output is included in `check_quantum_anti.out`. Finite enumeration corroborates, rather than replaces, the arbitrary-field proof.

## Relationship to prior work
Bergh and Erdmann, *\((\mathrm{Co})\)homology of quantum complete intersections* (arXiv:0709.3029, first public 2007-09-19) study the same family of local algebras and determine Hochschild invariants by bimodule resolutions; their text does not classify anti-involutions or their component geometry. Jin and Zhang, *Bi-Frobenius algebra structure on quantum complete intersections* (arXiv:2208.05687), and *Bi-Frobenius quantum complete intersections with permutation antipodes* (arXiv:2309.01485), investigate anti-homomorphisms subject to the additional existence of suitable coalgebra and bi-Frobenius data. Their restricted permutation-antipode constructions and existence conditions do not give the unrestricted unital algebra anti-involution census or the exceptional full-linear and characteristic-two component strata here. Earlier finite-field computations of automorphism spectra and of anti-involutions of different cube-zero algebras likewise do not directly imply these four anti-involution regimes. Standard diagonalizability and finite-field matrix centralizer counts are used as established tools, not claimed as new.

## Limitations
The result concerns only two-generator quantum complete intersections with both generators square-zero, and algebra anti-involutions that are \(k\)-linear and fix the coefficient field elementwise. Semilinear involutions, higher truncations, arbitrary quantum-complete-intersection parameters in more than two generators, and the potentially nonreduced scheme structure are excluded. The exhaustive priority comparison is limited to accessible literature and research records; independent expert mathematical audit has not been performed.

## References
1. P. A. Bergh and K. Erdmann, *\((\mathrm{Co})\)homology of quantum complete intersections*, arXiv:0709.3029 (first public 2007-09-19), https://arxiv.org/abs/0709.3029.
2. H. Jin and P. Zhang, *Bi-Frobenius algebra structure on quantum complete intersections*, arXiv:2208.05687 (2022), https://arxiv.org/abs/2208.05687.
3. H. Jin and P. Zhang, *Bi-Frobenius quantum complete intersections with permutation antipodes*, arXiv:2309.01485 (2023), https://arxiv.org/abs/2309.01485.
