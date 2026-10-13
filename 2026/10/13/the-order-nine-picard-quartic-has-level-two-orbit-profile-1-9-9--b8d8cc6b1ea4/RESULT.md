# The order-nine Picard quartic has level-two orbit profile \(1+9+9+9,\ 9^4,\ 9^7\)
## Finding
Let
\[
C:\quad y^3z=x(x^3-z^3)\subset\mathbf P^2_{\mathbf C}.
\]
Liang proves that \(\operatorname{Aut}(C)\cong C_9\) and gives a generator
\[
g[x:y:z]=[\zeta_3x:\zeta_9y:z].
\]
The complete orbit structure of the classical level-two data under this full automorphism group is as follows.

The 28 bitangents have orbit decomposition
\[
28=1+9+9+9.
\]
The fixed bitangent is the hyperflex \(z=0\). For every other bitangent, normalized as
\[
ax+by+z=0,
\]
the quantity \(u=a^3\) is constant on its \(C_9\)-orbit. The three free bitangent orbits are exactly the three fibers over the roots of
\[
u^3-96u^2+48u+64=0.
\]
These three orbit labels generate the real cubic subfield of the ninth cyclotomic field. More precisely, if
\[
t^3-3t+1=0,
\]
so that \(\mathbf Q(t)=\mathbf Q(\zeta_9+\zeta_9^{-1})\), then
\[
u=-36t^2-12t+104,
\qquad
t=-\frac{u^2}{48}+2u-\frac23.
\]
Thus the three bitangent \(9\)-orbits are Galois conjugate through the cyclic cubic field naturally attached to order nine.

On \(\operatorname{Jac}(C)[2]\), the generator has characteristic polynomial
\[
\Phi_9(T)=T^6+T^3+1,
\]
which is irreducible over \(\mathbf F_2\). Hence all 63 nonzero two-torsion points lie in free \(9\)-orbits:
\[
63=7\cdot9.
\]
Using the fixed odd theta characteristic determined by \(z=0\) as the origin of the affine theta-characteristic torsor, the 64 theta characteristics therefore have one fixed point and seven free \(9\)-orbits. Parity is preserved, so
\[
\#\Theta^-=28=1+3\cdot9,
\qquad
\#\Theta^+=36=4\cdot9.
\]
Equivalently, the 36 Cayley octads form four free \(9\)-orbits and the 63 Steiner complexes form seven free \(9\)-orbits.

## Assumptions and scope
The base field is \(\mathbf C\). The quartic is exactly the order-nine curve \(C_9\) in Liang's classification, not a varying Picard-family member. A bitangent includes a hyperflex line, as usual for smooth plane quartics. Orbit statements refer to the full projective automorphism group \(\operatorname{Aut}(C)\cong C_9\).

The Cayley-octad and Steiner-complex identifications use the standard genus-three correspondences: even theta characteristics correspond to the 36 Cayley octads, and nonzero points of \(\operatorname{Jac}(C)[2]\) correspond to the 63 Steiner complexes.

## Proof
Liang gives \(z=0\) as the unique undulation line and gives all other 27 bitangents in the affine-dual normalization \(ax+by+z=0\). He also gives
\[
a^9-96a^6+48a^3+64=0
\]
and observes that the automorphism sends the coefficient pair to
\[
(a,b)\longmapsto(\zeta_3a,\zeta_9b).
\]
Thus \(u=a^3\) is orbit-invariant and satisfies the displayed cubic.

It remains to prove that no non-hyperflex bitangent has a nontrivial stabilizer. The only proper nontrivial subgroup of \(C_9\) is \(\langle g^3\rangle\cong C_3\). Since
\[
g^3[x:y:z]=[x:\zeta_3y:z],
\]
a line fixed by \(g^3\) is either \(y=0\) or has equation \(ax+cz=0\). The line \(y=0\) cuts out
\[
-x(x^3-z^3),
\]
which has four simple zeros. After scaling a second type of line to \(ax+z=0\), substitution \(z=-ax\) gives
\[
-x\bigl(ay^3+(1+a^3)x^3\bigr).
\]
For \(a\ne0\) and \(1+a^3\ne0\), this again has four simple zeros. If \(1+a^3=0\), the multiplicities are \(1+3\), so the line is not bitangent. The exceptional value \(a=0\) gives precisely \(z=0\), whose intersection is \(-x^4\). Hence \(z=0\) is the only bitangent fixed by any nonidentity subgroup of \(C_9\). The other 27 bitangents are therefore three free \(9\)-orbits.

The cubic in \(u\) has three distinct roots. Because each \(9\)-orbit preserves \(u\), the three free orbits must be its three fibers. The arithmetic identification is exact: reducing
\[
(-36t^2-12t+104)^3-96(-36t^2-12t+104)^2+48(-36t^2-12t+104)+64
\]
modulo \(t^3-3t+1\) gives zero, and the inverse formula for \(t\) similarly reduces \(t^3-3t+1\) to zero modulo the cubic in \(u\). Both cubics are irreducible over \(\mathbf Q\), so they define the same cubic field. The polynomial \(t^3-3t+1\) is the minimal polynomial of \(2\cos(2\pi/9)=\zeta_9+\zeta_9^{-1}\).

For the two-torsion action, on the affine model \(y^3=x^4-x\) a basis of holomorphic differentials is
\[
\omega_1=\frac{dx}{y^2},\qquad
\omega_2=\frac{x\,dx}{y^2},\qquad
\omega_3=\frac{dx}{y}.
\]
Regularity at finite branch points follows from using \(y\) as a local parameter. At the unique point at infinity, with \(x\sim s^{-3}\) and \(y\sim s^{-4}\), their orders are respectively \(4,1,0\), so all three are holomorphic. Pullback by \(g\) gives eigenvalues
\[
\zeta_9,\qquad \zeta_9^4,\qquad \zeta_9^2.
\]
Together with the conjugate eigenvalues on antiholomorphic cohomology, the six eigenvalues are all primitive ninth roots. Therefore the integral characteristic polynomial on first homology, and hence its reduction on \(\operatorname{Jac}(C)[2]\), is
\[
\Phi_9(T)=T^6+T^3+1.
\]
The order of \(2\) modulo \(9\) is \(6\), so \(\Phi_9\) is irreducible over \(\mathbf F_2\). No nonidentity power of \(g\) fixes a nonzero vector of \(\operatorname{Jac}(C)[2]\), and the 63 nonzero vectors consequently form seven free \(9\)-orbits.

Finally, bitangents are the odd theta characteristics. The fixed hyperflex supplies a fixed odd theta characteristic \(\theta_0\), and translation by \(\theta_0\) identifies the 64 theta characteristics equivariantly with the affine torsor \(\theta_0+\operatorname{Jac}(C)[2]\). Thus there is one fixed theta characteristic and seven free \(9\)-orbits. Since automorphisms preserve parity, the remaining 27 odd characteristics are three of those orbits and the 36 even characteristics are the other four. Bergvall's standard correspondences then give the Cayley-octad and Steiner-complex statements.

## Verification
The attached `verification.py` performs exact symbolic checks. It verifies the two polynomial transformations between the \(u\)-cubic and \(t^3-3t+1\), irreducibility of both cubics over \(\mathbf Q\), the nonzero discriminant of the \(u\)-cubic, irreducibility of \(\Phi_9\) over \(\mathbf F_2\), and
\[
\gcd(\Phi_9(T),T^k-1)=1\quad(1\le k\le8)
\]
over \(\mathbf F_2\). It also checks the numerical orbit totals. These computations support, but do not replace, the exhaustive stabilizer and differential arguments above.

## Relationship to prior work
Liang's Theorem 4.3 gives the 28 bitangents, the equations for \(a\) and \(b\), and explicitly observes that \(C_9\) acts on the bitangent configuration. The inspected paper does not state the orbit sizes, does not identify the three \(u=a^3\) fibers as the three free orbits, and does not discuss Cayley octads or Steiner complexes. Its only occurrence of theta-characteristic language is background for asyzygetic sets.

Bergvall gives the general level-two dictionary: 28 bitangents are odd theta characteristics, 36 even theta characteristics correspond to Cayley octads, and the 63 nonzero two-torsion points correspond to Steiner complexes. That work does not specialize these structures to the order-nine Picard quartic.

General \(\operatorname{Sp}(6,2)\) data can encode cycle structures after the relevant conjugacy class is identified, so such tables are a residual source of an equivalent unlabeled orbit count. The present statement additionally identifies the three nonfixed bitangent orbits with the explicit elimination invariant \(u=a^3\) and its real cyclotomic cubic field.

## Limitations
The result concerns the action on bitangents, theta characteristics, Cayley octads, and Steiner complexes only; it does not classify orbit structures of every other classical quartic configuration. It does not give explicit coordinates for all Cayley octads. The originality search cannot exclude an older classical treatment that encodes the same cycle structure or the same cubic-field labeling under different terminology.

## References
1. Dun Liang, *Invariants, Bitangents and Matrix Representations of Plane Quartics with 3-Cyclic Automorphisms*, New York J. Math. 26 (2020), 636–655; arXiv:1902.02914; DOI 10.48550/arXiv.1902.02914.
2. Olof Bergvall, *Arithmetic and topology of classical structures associated with plane quartics*, European J. Math. 9 (2023), Article 117; DOI 10.1007/s40879-023-00711-3.
3. LMFDB, abstract group 1451520.a, \(\operatorname{Sp}(6,2)\), consulted for broader group-theoretic comparison.
