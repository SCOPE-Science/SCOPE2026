# Exact Fourier-support spectrum for four-point affine parallelograms over \(\mathbb F_5^d\)
## Finding
For every integer \(d\ge 2\), let \(f:\mathbb F_5^d\to\mathbb C\) have support exactly an affine parallelogram \(x+\{0,u,v,u+v\}\), where \(u,v\) are linearly independent, and assume all four support values are nonzero. Then the attainable Fourier-support sizes are exactly \[\{16,20,21,22,23,24,25\}5^{d-2}.\] Equivalently, after affine normalization the local bilinear polynomial \(P(X,Y)=a+bX+cY+dXY\) on fifth roots of unity, with \(abcd\ne0\), has exactly \(0,1,2,3,4,5\), or \(9\) zeros, and each of these seven counts occurs. In particular \(17\cdot5^{d-2}\), \(18\cdot5^{d-2}\), and \(19\cdot5^{d-2}\) are impossible Fourier-support sizes for this support geometry.

## Assumptions and scope
The group is \\(G=\\mathbb F_5^d\\) with \\(d\\ge2\\). The Fourier transform is taken with respect to the standard additive characters; its normalization does not affect support. The physical support is exactly \\(x+\\{{0,u,v,u+v\\}}\\), where \\(u\\) and \\(v\\) are linearly independent, and each of the four coefficients is nonzero. The statement classifies only this fixed affine support geometry; it does not classify arbitrary four-point supports in \\(\\mathbb F_5^d\\) or claim an analogous formula for other primes.

## Proof
Translation of the physical support multiplies the Fourier transform by a character, and an invertible linear change of coordinates permutes frequencies. Thus it suffices to use the normalized support \\(\\{{0,e_1,e_2,e_1+e_2\\}}\\). If its four nonzero values are \\(a,b,c,d\\), then on the two-dimensional difference span the Fourier transform is, up to a harmless character factor,
\\[
P(X,Y)=a+bX+cY+dXY,
\\]
where \\(X\\) and \\(Y\\) range over the fifth roots of unity \\(\\mu_5\\). Each local pair \\((X,Y)\\in\\mu_5^2\\) is repeated on exactly \\(5^{d-2}\\) ambient frequencies.

First suppose \\(ad=bc\\). Since all four coefficients are nonzero,
\\[
P(X,Y)=a\\left(1+\\frac ba X\\right)\\left(1+\\frac ca Y\\right).
\\]
Each factor either has no zero on \\(\\mu_5\\) or vanishes on exactly one coordinate value. Hence the local zero count is \\(0\\), \\(5\\), or \\(9\\), the last value being the union of one full row and one full column.

Now suppose \\(ad\\ne bc\\). For each \\(X\\in\\mu_5\\), a zero satisfies
\\[
Y=M(X):=-\\frac{{a+bX}}{{c+dX}}.
\\]
If the denominator vanishes, the numerator cannot vanish as well, because simultaneous vanishing would imply \\(ad=bc\\). Therefore each row contributes at most one zero, so there are at most five. If there were five, the Möbius transformation \\(M\\) would permute all five vertices of the regular pentagon \\(\\mu_5\\). Any Möbius map permuting \\(\\mu_5\\) preserves the unit circle, and its restriction to that circle either preserves or reverses cyclic order. A cyclic-order-preserving permutation of a regular pentagon is a rotation and a cyclic-order-reversing one is a reflection. Thus \\(M(X)=\\eta X\\) or \\(M(X)=\\eta/X\\) for some \\(\\eta\\in\\mu_5\\). Cross-multiplication in the first case forces \\(a=d=0\\); in the second it forces \\(b=c=0\\). Both contradict the nonzero-coefficient hypothesis. Hence the nonfactorable case has at most four zeros.

All permitted zero counts occur. Writing \\(\\zeta=e^{2\\pi i/5}\\), the following coefficient quadruples \\((a,b,c,d)\\) have respectively \\(0,1,2,3,4,5,9\\) local zeros:
\\[
(1,-2,-2,4),
\\quad(-2,-1,1,2),
\\quad(-(1+\\zeta),-(1+\\zeta),-(1+\\zeta),\\zeta^3),
\\]
\\[
(-(1+\\zeta),-1,\\zeta^3,\\zeta^2+\\zeta^3),
\\quad (-(1+\\zeta),\\zeta+\\zeta^3,1+\\zeta^3,-(1+\\zeta)),
\\]
\\[
(1,-1,-2,2),
\\quad(1,-1,-1,1).
\\]
Thus the local support sizes are exactly \\(25,24,23,22,21,20,16\\). Multiplying by the fiber size \\(5^{d-2}\\) proves the asserted spectrum.

## Verification
The bundled exact-arithmetic verifier works in \\(\\mathbb Q(\\zeta_5)\\) using the basis \\(1,\\zeta,\\zeta^2,\\zeta^3\\) and the identity \\(1+\\zeta+\\zeta^2+\\zeta^3+\\zeta^4=0\\). It checks the seven displayed witnesses without floating-point arithmetic. It also exhausts all \\(5!\\) permutations of the pentagon with exact cross-ratio tests, finding exactly the ten dihedral Möbius permutations and confirming that every such permutation is a rotation or reflection. These computations corroborate the two finite local ingredients; the all-dimensional result follows analytically from the proof above.

## Relationship to prior work
Delvaux and Van Barel compute Hamming numbers for Kronecker products of Fourier matrices. Their \\(F_5\\otimes F_5\\) table gives the unrestricted four-sparse minimum Fourier-support size \\(10\\), but Hamming numbers minimize over all supports of a given cardinality and do not give the complete spectrum for a fixed affine parallelogram. Bonami and Ghobber independently give the same global minimum through the uncertainty function on \\(\\mathbb Z_5^2\\), and their equality classification shows that support size \\(10\\) at four physical points is attained only by line-supported extremizers. Hence those results imply that a genuine parallelogram is not globally extremal, but they do not imply its exact minimum \\(16\\), its attainable intermediate sizes, or the forbidden band \\(17,18,19\\).

The present classification is geometry-sensitive: it turns the general rank-deficiency problem into a complete zero-set classification of a bilinear polynomial on the \\(5\\times5\\) root-of-unity grid. The nonfactorable case uses the rigidity of Möbius permutations of a regular pentagon, which is not part of the scalar Hamming-number or equality-case statements.

## Limitations
The theorem is specific to fifth roots of unity and affine parallelogram supports. It does not classify arbitrary four-point supports, coefficients allowed to vanish, or primes other than \\(5\\). The literature comparison found no statement giving this fixed-support complete spectrum, but an equivalent formulation could exist in specialized work on rank-deficient Fourier submatrices, cyclotomic zero sets, or finite-frame spark geometry.

## References
1. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, KU Leuven Report TW 477, 15 November 2006. The report lists primary classification 42A99 and gives the \\(F_5\\otimes F_5\\) Hamming-number table.
2. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060v1, 26 March 2010. Proposition 21 gives the uncertainty function on \\(\\mathbb Z_p^2\\); Theorem 23 classifies equality cases in the relevant range.
