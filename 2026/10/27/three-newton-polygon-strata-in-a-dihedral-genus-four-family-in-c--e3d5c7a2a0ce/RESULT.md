# Three Newton-polygon strata in a dihedral genus-four family in characteristic three

## Finding
Let \(k\) be algebraically closed of characteristic \(3\), and let \(C_{a,b}\) be the smooth projective completion of
\[
C_{a,b}:\quad y^2=x^{10}+a x^8+b x^6+b x^4+a x^2+1,\qquad a,b\in k.
\]
The polynomial is separable, and the curve has genus \(4\), **if and only if**
\[
b\ne1,\qquad a+b+1\ne0,\qquad a^2-a+2-b\ne0. \tag{1}
\]
Within this smooth two-parameter locus, the Newton polygons, \(3\)-ranks and \(a\)-numbers are exactly:

| Parameters | \(3\)-rank | \(a\)-number | Newton slopes with multiplicity |
|:---|:---:|:---:|:---|
| \(a\ne0\) | \(4\) | \(0\) | \(0^{[4]},1^{[4]}\) |
| \(a=0,\ b\ne0\) | \(2\) | \(2\) | \(0^{[2]},(1/2)^{[4]},1^{[2]}\) |
| \(a=b=0\) | \(0\) | \(2\) | \((1/2)^{[8]}\) |

In the middle row, smoothness additionally requires \(b\ne\pm1\). The nonordinary locus is the punctured line \(a=0\), \(b\ne\pm1\), containing the unique supersingular parameter \((a,b)=(0,0)\). Thus \(3\)-ranks \(1\) and \(3\), and \(a\)-number \(1\), do not occur in this family.

For **every** \(q=3^m\), \(m\ge1\), the numbers of smooth **ordered parameter pairs** \((a,b)\in\mathbf F_q^2\) are:
\[
N_{4,0}=q^2-4q+5,\qquad N_{2,2}=q-3,\qquad N_{0,2}=1,\qquad N_{\mathrm{smooth}}=q^2-3q+3. \tag{2}
\]
These are counts of the displayed coordinate-marked equations, **not** counts of isomorphism classes.

## Assumptions and scope
The ground field is algebraically closed of characteristic \(3\) for the geometric statements. Point-count statements use the displayed coefficients in finite fields \(\mathbf F_{3^m}\). The hyperelliptic involution is implicit, and the transformations \((x,y)\mapsto(-x,y)\) and \((x,y)\mapsto(1/x,y/x^5)\) exhibit a dihedral subgroup of order \(8\) of the automorphism group. No assertion is made that this is the full automorphism group. The \(3\)-rank is the \(\mathbf F_3\)-dimension of geometric \(3\)-torsion, and the \(a\)-number is \(\dim\operatorname{Hom}(\alpha_3,J(C_{a,b}))\). Newton slopes refer to the \(3\)-divisible group of the Jacobian.

## Proof
**Smoothness.** Set \(t=x^2\), so that \(f(x)=h(t)\), where
\[
h(t)=t^5+a t^4+b t^3+b t^2+a t+1=(t+1)g(t),
\]
\[
g(t)=t^4+(a-1)t^3+(b-a+1)t^2+(a-1)t+1.
\]
Since \(h(0)=1\) and \(2\ne0\), \(f\) is squarefree exactly when \(h\) is. The discriminant over the integers of the displayed quintic factors (up to a sign) as
\[
\operatorname{Disc}_t(h)=-(a+b+1)(3a-b-5)^3(a^2+2a-4b+5)^2.
\]
Modulo \(3\), this is a unit times \((a+b+1)(1-b)^3(a^2-a+2-b)^2\), proving (1). This also follows by setting \(u=t+t^{-1}\) in \(g(t)/t^2=u^2+(a-1)u+(b-a-1)\), and checking its two critical values and discriminant. When (1) holds, \(f\) is squarefree of degree \(10\), so \(C_{a,b}\) has genus \(4\).

**Cartier–Manin and rank.** On the standard differential basis \(x^{j-1}dx/y\), \(1\le j\le4\), the Cartier–Manin coefficient matrix is
\[
H_{ij}=[x^{3i-j}]f(x),\qquad
H=\begin{pmatrix}
a&0&1&0\\
0&b&0&a\\
a&0&b&0\\
0&1&0&a
\end{pmatrix},\qquad \det H=a^2(b-1)^2. \tag{3}
\]
For \(a\ne0\), (1) makes \(H\) invertible; hence the Jacobian is ordinary. For \(a=0\), the matrix has rank \(2\) at every smooth parameter, so the \(a\)-number is \(4-2=2\). If further \(b\ne0\), direct multiplication of the Frobenius twists of \(H\) shows every positive-length Cartier iterate has stable rank \(2\): the two nonzero eigen-directions have nonzero scalar factors involving powers of \(b\). Hence the stable Frobenius rank and \(3\)-rank equal \(2\). The remaining four isocrystal slopes are \(1/2\), by self-duality and the integrality of slope-denominator multiplicities for a principally polarized abelian fourfold. At \(a=b=0\), one has \(H H^{(3)}=0\), so the stable rank is \(0\), and \(a=2\).

**Supersingularity at the isolated point.** Let \(\mathcal H\) be the degree-\(10\) Hermitian curve
\[
U^{10}+V^{10}+W^{10}=0
\]
over \(\mathbf F_{81}\). It is maximal over \(\mathbf F_{81}\). Choose \(\theta\in\mathbf F_{81}\) with \(\theta^2=-1\). The separable degree-\(5\) map
\[
(U:V:W)\longmapsto \bigl(x=U/W,\ y=(V/W)^5/\theta\bigr)
\]
lands on \(C_{0,0}:y^2=x^{10}+1\). The induced injection on first rational \(\ell\)-adic cohomology, for \(\ell\ne3,5\), shows that \(C_{0,0}\) inherits the Hermitian curve's all-\(-9\) Frobenius eigenvalues. Thus \(C_{0,0}\) is maximal over \(\mathbf F_{81}\), with \(81+1+2\cdot4\cdot9=154\) rational points. Its Jacobian is supersingular, and all eight slopes are \(1/2\). Since its \(a\)-number is \(2\), the Jacobian is not superspecial.

**Exact finite-field stratum counts.** For each \(a\in\mathbf F_q\), the forbidden \(b\) values are \(1\), \(-a-1\) and \(a^2-a+2\). They are pairwise distinct unless \(a=0\), \(a=1\), or \(a=-1\), respectively; these three exceptions are distinct in characteristic \(3\), and no triple collision occurs. Thus there are \((q-3)(q-3)+3(q-2)=q^2-3q+3\) smooth pairs in total. On \(a=0\), smoothness removes exactly \(b=\pm1\), leaving \(q-2\) pairs; one is \(b=0\) and \(q-3\) have \(b\ne0\). Subtraction gives \(q^2-4q+5\) ordinary pairs, proving (2).

## Verification
Run the standalone bundled file `verify.py` using standard Python 3. It builds explicit finite-field arithmetic, checks squarefreeness independently by a polynomial gcd, computes \(H\) and Frobenius-stable ranks, and enumerates all \((a,b)\) for \(q\in\{3,9,27,81\}\). It also directly counts \(154\) rational points of \(C_{0,0}\) over \(\mathbf F_{81}\). Recorded strata \((3\text{-rank},a\text{-number})\) are, respectively: \(q=3: (0,2)\mapsto1,(4,0)\mapsto2\); \(q=9: (0,2)\mapsto1,(2,2)\mapsto6,(4,0)\mapsto50\); \(q=27: 1,24,626\); and \(q=81:1,78,6242\). The program prints `VERIFY_OK`. These are finite corroborations; the proof above supplies the all-\(q\) theorem.

## Relationship to prior work
Kudo–Nakagawa–Takagi [1], especially Appendix A and its dihedral normal forms, and Ohashi–Kudo [2] study the corresponding genus-four automorphism family, chiefly for superspecial classifications in characteristic at least \(7\). The exact equation and its automorphisms are **not** claimed as new. Garton–Thunder–Weir [3] give distribution results for \(a\)-numbers in the *full space* of characteristic-three hyperelliptic curves but do not give the complete simultaneous \(3\)-rank/Newton-strata and rational marked-parameter count for this dihedral family. Camacho-Navarro [4] studies genus-four arithmetic primarily in a nonhyperelliptic setting. The present result identifies a complete exceptional line and one supersingular point within the two-parameter dihedral family, with exact counts over all ternary finite fields.

## Limitations
This classification is restricted to characteristic \(3\), to the displayed two-parameter equations, and to geometrically smooth curves. It does not classify geometric isomorphism classes, the full automorphism group at special parameters, or Newton polygons beyond this family. Independent audit has not been performed. A potentially related article on genus-four superelliptic \(a\)-numbers [5] could not be read in full; its coverage of this particular exact stratification is an unresolved literature risk.

## References
[1] M. Kudo, S. Nakagawa, and T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing Z6*, arXiv:2210.14822 (first posted 2022-10-26), https://arxiv.org/abs/2210.14822.

[2] R. Ohashi and M. Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858 (first posted 2023-12-28), https://arxiv.org/abs/2312.16858.

[3] D. Garton, J. Thunder, and B. Weir, *The distribution of a-numbers of hyperelliptic curves in characteristic three*, arXiv:2403.00120 (first posted 2024-02-29), https://arxiv.org/abs/2403.00120.

[4] C. Camacho-Navarro, *The a-number, p-rank and Cartier points of genus 4 curves*, arXiv:2012.08705 (first posted 2020-12-16), https://arxiv.org/abs/2012.08705.

[5] G. Sohn, *The a-number of superelliptic curves of genus four*, 2025, DOI 10.23091/japm.2025.059; full text not accessed.
