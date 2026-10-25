# The characteristic-eleven Hasse divisor on the dihedral genus-three hyperelliptic pencil

## Finding
Over any algebraically closed field \(k\) of characteristic \(11\), the smooth one-parameter family
\[
C_a:\quad y^2=x^8+a x^4+1,\qquad a\in k,\quad a^2\ne4,
\]
contains exactly seven geometric nonordinary parameter values. The \(11\)-rank of the Jacobian is \(1\) at \(a^2=5\) (two values), \(2\) at \(a=0\), \(a^2=3\), or \(a^2=-1\) (five values), and \(3\) everywhere else. The corresponding \(a\)-numbers are \(2,1,0\), respectively; in particular no member has \(11\)-rank zero and none is superspecial.

In the natural relative differential basis, the pullback of the Hasse (nonordinary) divisor has local equation
\[
- (5-a^2)^2\,a(a^2-3)(a^2+1)=0.
\]
Consequently it consists of two points of multiplicity \(2\) and five points of multiplicity \(1\), a divisor of length \(9\) on the smooth affine parameter line. The doubled points are precisely those where the \(11\)-rank falls by two. These assertions concern the indicated parameter line, not multiplicity on an unspecified coarse moduli compactification.

## Assumptions and scope
The field is algebraically closed of characteristic \(11\). For every \(a\in k\) with \(a^2\ne4\), the polynomial \(x^8+a x^4+1\) is squarefree: a repeated root must satisfy \(x^4=-a/2\), which makes the polynomial vanish only when \(a^2=4\). Thus its smooth projective double cover of \(\mathbb P^1\) has genus \(3\). The parameter excludes exactly the two singular fibers. The automorphisms induced by \(x\mapsto\zeta_4x\) and \(x\mapsto1/x\) (with \(y\mapsto y/x^4\) for inversion) explain why this is a natural dihedral-symmetric subfamily. The invariant \(w=a^2\) appears in the genus-three dihedral-invariant normal form of Gutierrez and Shaska.

The \(p\)-rank is the dimension over \(\mathbb F_p\) of the \(p\)-torsion points of the Jacobian, and the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_p,\operatorname{Jac}(C_a)[p])\). The Hasse divisor here is the zero scheme of the determinant of Frobenius on first cohomology, evaluated in the displayed smooth family. Its vanishing orders are independent of regular changes of the Hodge frame.

## Proof
Write \(F_a(x)=x^8+a x^4+1\), let \(z=x^4\), and set \(G_a(z)=z^2+az+1\). The standard hyperelliptic Hasse--Witt formula, relative to the classes dual to the differentials \(x^{j-1}dx/y\), gives the matrix whose \((i,j)\)-entry is the coefficient of \(x^{11i-j}\) in \(F_a(x)^5\), for \(1\le i,j\le3\). All powers occurring in \(F_a^5=G_a(x^4)^5\) are multiples of four. For \(1\le i,j\le3\), the congruence \(11i-j\equiv0\pmod4\) holds exactly at \((i,j)=(1,3),(2,2),(3,1)\). Expanding just the corresponding coefficients yields, in characteristic eleven,
\[
[z^2]G_a(z)^5=[z^8]G_a(z)^5=5+10a^2=5-a^2,
\]
\[
[z^5]G_a(z)^5=a^5+20a^3+30a=a(a^2-3)(a^2+1).
\]
Hence the complete Hasse--Witt matrix is
\[
H(a)=\begin{pmatrix}
0&0&u\\
0&v&0\\
u&0&0
\end{pmatrix},\qquad
u=5-a^2,\quad v=a(a^2-3)(a^2+1).
\]
Its determinant equals \(-u^2v\). Because the base field is perfect, raising every nonzero entry to the \(11\)-th power preserves the zero pattern. Any semilinear iterate of \(H\), taken sufficiently many times to calculate the stable Frobenius rank, has image supported on precisely those coordinate directions corresponding to nonzero \(u\) or \(v\). Therefore the stable Frobenius rank equals its ordinary matrix rank: \(2\) if \(u\ne0,v=0\), \(1\) if \(u=0,v\ne0\), and \(3\) if both are nonzero. The simultaneous equations \(u=v=0\) have no solutions: substituting \(a^2=5\) gives \(v=12a=a\ne0\). Thus \(11\)-rank zero never occurs. The Cartier operator has rank equal to the Hasse--Witt matrix rank, hence the \(a\)-number is three minus that rank.

Finally, \(u=0\) has two distinct roots \(a^2=5\), and \(v=0\) has five distinct roots \(a=0\), \(a^2=3\), and \(a^2=-1\). All seven are disjoint from \(a^2=4\). Each root of \(u\) is simple and contributes order \(2\) to \(\det H\); all roots of \(v\) are simple and contribute order \(1\). The divisor consequently has total length \(2\cdot2+5=9\), with precisely the asserted ranks and multiplicities.

## Verification
Run `python3 verify_p11.py` with a standard Python 3 interpreter. The script independently expands \((z^2+az+1)^5\) over \(\mathbb F_{11}[a,z]\), reconstructs the relevant Hasse--Witt entries, checks the factorization and pairwise coprimality of \(u,v\) and their formal derivatives, and reports `VERIFY_OK`. Its finite residue evaluations are checks, not a substitute for the symbolic proof and the passage to algebraic closure. The absolute normalization of the Hasse matrix is relative to the indicated monomial differential basis; multiplying the determinant by a unit does not change its divisor.

## Relationship to prior work
Gutierrez--Shaska (2005) establish the normal form for hyperelliptic curves with extra involutions and explicitly identify \(w=a^2\) on the dihedral genus-three subfamily. Harvey--Sutherland (2014) give the general Hasse--Witt coefficient formula and computational theory. Paulhus (2008) studies Jacobian isogeny decompositions of genus-three curves with extra automorphisms; Achter--Pries (2011) study global hyperelliptic \(p\)-rank strata. These results make the computation possible and provide its context, but the inspected relevant passages do not give the characteristic-eleven parameter-by-parameter \(p\)-rank and \(a\)-number classification nor the two tangencies to the Hasse divisor. This is a specific family calculation; it is not a new general Hasse--Witt algorithm or a classification of all genus-three curves in characteristic eleven.

## Limitations
The claim concerns the smooth affine family \(a^2\ne4\) and its indicated trivialized Hodge frame. No assertions are made about compactification, other characteristics, Newton polygons beyond their slope-zero multiplicity, or the full Ekedahl--Oort type. Although targeted searches and comparisons found no identical published calculation, equivalent treatment under alternate modular coordinates remains possible. The result has been checked by symbolic computation and a self-review only; no independent scientific audit has been performed.

## References
1. J. Gutierrez and T. Shaska, *Hyperelliptic Curves with Extra Involutions*, LMS J. Comput. Math. **8** (2005), 102--115. DOI: 10.1112/S1461157000000917. Publicly published 7 April 2005; see normal form (2) and Example 3.3.
2. D. Harvey and A. V. Sutherland, *Computing Hasse--Witt Matrices of Hyperelliptic Curves in Average Polynomial Time*, arXiv:1402.3246v1 (13 February 2014), especially introductory Hasse--Witt coefficient formula.
3. J. Paulhus, *Decomposing Jacobians of Curves with Extra Automorphisms*, Acta Arith. **132** (2008), 231--244, §§3.1--3.2.
4. J. D. Achter and R. Pries, *The p-rank strata of the moduli space of hyperelliptic curves*, Adv. Math. **227** (2011), 1846--1875, §2.2.
