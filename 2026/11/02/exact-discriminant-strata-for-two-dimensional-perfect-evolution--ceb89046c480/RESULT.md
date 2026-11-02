# Exact discriminant strata for two-dimensional perfect evolution algebras

## Finding
Let \(q\) be a prime power and let \(A=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) run uniformly through \(\mathrm{GL}_2(\mathbb F_q)\). The corresponding perfect evolution algebra has idempotent equations \(A(x^2,y^2)^T=(x,y)^T\). Its geometric scheme of idempotents has length four; the origin is always reduced. Classify the remaining length-three scheme by its geometric root multiplicities. For every odd \(q\), the exact numbers of **labeled invertible structure matrices** in each geometric stratum are

\[
\begin{array}{c|c}
\text{geometric nonzero idempotent multiplicities}&\# A\\\hline
1+1+1&(q^2-1)(q^2-q)-q(q-1)^2\\
2+1&(q-1)^3\\
3&(q-1)^2
\end{array}.
\]

Consequently, for odd \(q\), the probability that the nonzero-idempotent scheme is nonreduced is exactly \(1/(q+1)\); conditional on being nonreduced, the proportions with types \(2+1\) and \(3\) are \((q-1)/q\) and \(1/q\), respectively. In characteristic two every perfect evolution algebra has a reduced idempotent scheme, so the nonreduced probability is zero (this last fact was already recorded in the cited survey). These are matrix-weighted frequencies, not isomorphism-class-weighted frequencies.

## Assumptions and scope
Fix the ordered natural basis, so distinct invertible matrices are counted separately. The multiplication is \(e_1e_2=0\), \(e_1^2=a e_1+c e_2\), \(e_2^2=b e_1+d e_2\). Geometric roots and scheme multiplicities are measured over an algebraic closure, while the counted structure matrices have coefficients in \(\mathbb F_q\). A nonreduced scheme means it has a geometric point of multiplicity at least two.

## Proof

**Reduction to a binary cubic.** For nonzero \((x,y)\), the idempotence equation implies projective proportionality between \(A(x^2,y^2)^T\) and \((x,y)^T\), hence
\[
F_A(X,Y)=cX^3-aX^2Y+dXY^2-bY^3=0.
\]
Conversely, if \([X:Y]\) is a projective zero of \(F_A\), then \(A(X^2,Y^2)^T=\lambda(X,Y)^T\) for a unique nonzero \(\lambda\), since \(A\) is invertible. Scaling to \((\lambda^{-1}X,\lambda^{-1}Y)\) gives a unique nonzero idempotent. Scheme-theoretically, this correspondence respects multiplicities: on a projective chart the radial scale equation has derivative \(1\) at its nonzero solution, so eliminating that parameter preserves the local root multiplicity. The origin is reduced because the Jacobian of \(A(x^2,y^2)^T-(x,y)^T\) at zero is \(-I_2\). The cubic cannot vanish identically for invertible \(A\).

**Coefficient normalization.** If \(F=u_3X^3+u_2X^2Y+u_1XY^2+u_0Y^3\), the corresponding matrix is \(A=\left(\begin{smallmatrix}-u_2&-u_0\\u_3&u_1\end{smallmatrix}\right)\). Thus \(\det A=u_3u_0-u_2u_1\), and each projective cubic with nonzero determinant represents exactly \(q-1\) matrices, one per nonzero scalar multiple.

**Characteristic two.** The partial derivatives of \(F_A\) are \(F_X=cX^2+dY^2\) and \(F_Y=aX^2+bY^2\). A multiple projective root would force \(\left(\begin{smallmatrix}c&d\\a&b\end{smallmatrix}\right)(X^2,Y^2)^T=0\), impossible for a nonzero projective point since its determinant equals \(-\det A\ne0\). (Equivalently, the binary cubic discriminant equals \((\det A)^2\).) Hence every geometric root is simple. This agrees with the characteristic-two Jacobian observation already available in the survey.

**Odd characteristic, triple roots.** Every cubic with one geometric root of multiplicity three is proportional to \((X-rY)^3\) for some \(r\in\mathbb F_q\), or to \(Y^3\). The root lies in \(\mathbb F_q\): Frobenius fixes the unique geometric root. For \((X-rY)^3\), its determinant expression is \(8r^3\); for \(Y^3\), it is zero. Since \(q\) is odd, exactly the \(q-1\) choices \(r\in\mathbb F_q^\times\) are allowable. Multiplying by \(q-1\) nonzero scalars gives exactly \((q-1)^2\) matrices with the type \(3\).

**Odd characteristic, double-plus-simple roots.** A rational binary cubic with a repeated root and a second distinct root has both roots in \(\mathbb P^1(\mathbb F_q)\): the repeated root must be rational by Frobenius and degree three, so the remaining root is rational as well. Write the double root as \(r\) and the simple one as \(t\). If both are finite, normalize \(F=(X-rY)^2(X-tY)\). Its determinant expression is \(2r(r+t)^2\). With \(r\ne t\), nonsingularity requires \(r\ne0\) and \(t\notin\{r,-r\}\), giving \((q-1)(q-2)\) choices. If the simple root is infinity, normalize \(F=Y(X-rY)^2\): its determinant is \(2r\), giving \(q-1\) choices. If the double root is infinity, \(F=Y^2(X-tY)\), whose determinant is zero. Thus there are \((q-1)^2\) admissible projective cubics of type \(2+1\), hence \((q-1)^3\) matrices.

**The remaining stratum.** The group size is \(|\mathrm{GL}_2(\mathbb F_q)|=(q^2-1)(q^2-q)=q(q-1)^2(q+1)\). All other invertible matrices have a cubic with three geometrically distinct roots, whose number is \(|\mathrm{GL}_2|-(q-1)^3-(q-1)^2\). The nonreduced proportion is therefore \(q(q-1)^2/|\mathrm{GL}_2|=1/(q+1)\), and the conditional probabilities follow by division.

## Verification
The accompanying standard-library-only script `verify.py` enumerates all \(2\times2\) invertible structure matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\); it uses exact finite-field multiplication, the binary cubic discriminant, and an independent recognition of the triple-root family. It reproduces the expected counts, respectively \((6;0,0)\), \((36;8,4)\), \((180;0,0)\), \((400;64,16)\), \((1764;216,36)\), where each tuple lists (reduced; double-plus-simple; triple). Enumeration is confirmatory: the above parameter count proves the formula for every finite field.

## Relationship to prior work
Kaygorodov–Martín González–Viruel (2026), Sections 2.1.5, 2.1.10 and Conjecture 2, introduce the idempotent scheme, the universal mean of rational nonzero idempotents under uniform invertible matrices, and the characteristic-two reducedness fact, but do not give the odd-characteristic discriminant-stratum frequencies. The present classification counts singular geometric idempotent schemes, rather than merely the number of rational idempotent points. Earlier classifications of two-dimensional perfect evolution algebras over domains concern isomorphism classes, not this matrix-weighted discriminant count. The finite-field distribution of numbers of rational idempotents alone does not distinguish a triple geometric root from an irreducible/separable cubic with a single rational point. The new numerical contribution here is the odd-characteristic discriminant frequency and double/triple decomposition; the characteristic-two statement is reproduced for completeness and is not claimed as new.

## Limitations
The count uses uniformly chosen labeled invertible matrices, not uniformly chosen algebra isomorphism types. It concerns geometric multiplicity types, not the Frobenius conjugacy classes of the three distinct roots, and does not address dimension three or higher. Older unindexed treatments of the discriminant locus could imply this enumeration; no historical-priority guarantee is made.

## References
1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first public 2026-10-15), Sections 2.1.5, 2.1.10, 2.3.
2. Y. Cabrera Casado, D. Martín Barquero, C. Martín González, *Two-dimensional perfect evolution algebras over domains*, J. Algebraic Combin. 58 (2023), 569–587, DOI 10.1007/s10801-022-01196-1.
