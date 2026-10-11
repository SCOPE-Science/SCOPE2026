# Hodge character of the Cartwright–Steger fiber symmetry
## Finding
Let \(F\) be the genus-\(19\) Cartwright–Steger Albanese fiber over the fixed base point and let \(S\) be the order-three automorphism chosen so that its three fixed points on \(F\) have tangent multiplier \(\omega^2\), where \(\omega=e^{2\pi i/3}\). Then the \(S^*\)-eigenspace dimensions on \(H^{1,0}(F)\) for eigenvalues \(1,\omega,\omega^2\) are exactly \(6,6,7\). Consequently the characteristic polynomial of \(S_*\) on \(H_1(F;\mathbb Q)\) is \((t-1)^{12}(t^2+t+1)^{13}\). Equivalently, the nontrivial Prym part of the cyclic triple cover \(F\to F/\langle S\rangle\) has complex dimension \(13\) and Eisenstein Hodge multiplicities \(6\) and \(7\), up to exchanging the two embeddings of \(\mathbb Q(\omega)\).

The conclusion refines the fixed-point and quotient-genus data of Akhmedov–Yeung into the complete rational homology character and the corresponding Hodge multiplicities of the order-three symmetry.

## Assumptions and scope
Let \(X\) be the Cartwright–Steger surface, \(\alpha:X\to E\) its Albanese fibration, and \(F=\alpha^{-1}(O)\) the smooth invariant fiber used by Akhmedov–Yeung. Their normalization chooses the order-three automorphism \(S\) so that \(F\) has genus \(19\), \(S\) has exactly three fixed points on \(F\), the tangent multiplier at each fixed point is \(\omega^2\), and the quotient \(G=F/\langle S\rangle\) has genus \(6\). Here \(\omega=e^{2\pi i/3}\).

No claim is made about an integral direct-sum decomposition of \(H_1(F;\mathbb Z)\), nor about the still-undetermined individual vanishing class or handle monodromy in the source paper.

## Proof
Write \(d_0,d_1,d_2\) for the dimensions of the \(1,\omega,\omega^2\)-eigenspaces of \(S^*\) on \(H^{1,0}(F)\).

First, invariant holomorphic one-forms descend through the finite quotient \(F\to G\), while holomorphic one-forms on \(G\) pull back to invariant forms. Hence
\[
d_0=g(G)=6.
\]
Since \(g(F)=19\),
\[
d_1+d_2=13.
\]

Second, apply the holomorphic Lefschetz fixed-point formula to the structure sheaf of \(F\). The three fixed points are isolated and each tangent multiplier is \(\omega^2\), so
\[
1-\overline{\operatorname{tr}(S^*|H^{1,0}(F))}
 =\frac{3}{1-\omega^2}
 =1-\omega,
\]
where \((1-\omega)(1-\omega^2)=3\). Therefore
\[
\operatorname{tr}(S^*|H^{1,0}(F))=\omega^2.
\]
Thus
\[
6+d_1\omega+d_2\omega^2=\omega^2.
\]
Using \(1+\omega+\omega^2=0\), comparison in the basis \(1,\omega\) gives \(d_2=7\) and \(d_1=6\).

Complex conjugation exchanges the \(\omega\)- and \(\omega^2\)-eigenspaces when passing from \(H^{1,0}\) to \(H^{0,1}\). Therefore on \(H^1(F;\mathbb C)\), and hence on \(H_1(F;\mathbb Q)\), the multiplicities are \(12\) for eigenvalue \(1\) and \(13\) for each primitive cube root. Since \(S^3=1\), the action is semisimple over \(\mathbb Q\), yielding
\[
\det(tI-S_*)=(t-1)^{12}(t^2+t+1)^{13}.
\]
The nontrivial isotypic summand has real homology dimension \(26\), so the connected Prym has complex dimension \(13\); its two nontrivial Hodge multiplicities are \(6\) and \(7\).

## Verification
There are two independent internal consistency checks. The displayed characteristic polynomial has total degree \(12+2\cdot13=38=2g(F)\). Its trace is \(12-13=-1\), exactly the trace obtained in Akhmedov–Yeung from the ordinary Lefschetz number of the three fixed points. Also, Riemann–Hurwitz for a degree-three cover with three totally ramified points gives
\[
2\cdot19-2=3(2\cdot6-2)+3(3-1),
\]
so the genus data used above are mutually consistent.

## Relationship to prior work
Akhmedov–Yeung determine the order-three symmetry, the three fixed points on the invariant genus-\(19\) fiber, their tangent multiplier, the quotient genus \(6\), and the ordinary homological trace \(-1\). They do not state the full characteristic polynomial, the \(H^{1,0}\) eigenspace dimensions, or the Prym Hodge multiplicities. Their paper instead focuses on monodromy relations, vanishing cycles, and spanning of \(H_1(F;\mathbb Q)\).

Cartwright–Koziarz–Yeung establish the genus-\(19\) Albanese fiber and the order-three fixed-point geometry on the surface. The present calculation combines those geometric data, as sharpened in the 2026 monodromy paper, with the holomorphic Lefschetz formula to obtain the exact Hodge character.

## Limitations
The result determines the rational homology representation and complex Hodge multiplicities only. It does not classify the integral \(\mathbb Z[C_3]\)-lattice, the polarization type of the Prym, the vanishing-cycle class, or the unknown handle return map. The originality search found no equivalent statement, but older literature on cyclic covers could contain the same representation-theoretic consequence in a form not indexed by the Cartwright–Steger name.

## References
1. A. Akhmedov and S.-K. Yeung, *A monodromy relation for the Cartwright–Steger fibration*, arXiv:2610.01467v1 (2026).
2. D. I. Cartwright, V. Koziarz, and S.-K. Yeung, *On the Cartwright–Steger surface*, arXiv:1412.4137; J. Algebraic Geom. 26 (2017), 655–689.
3. M. F. Atiyah and R. Bott, *A Lefschetz fixed point formula for elliptic complexes: II. Applications*, Ann. of Math. 88 (1968), 451–491.
