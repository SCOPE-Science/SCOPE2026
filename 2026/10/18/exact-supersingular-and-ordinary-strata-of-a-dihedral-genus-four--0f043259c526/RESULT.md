# Exact supersingular and ordinary strata of a dihedral genus-four family in characteristic \(11\)

## Finding
Let \(k=\overline{\mathbf F}_{11}\). For every \(a\in k\) satisfying \(a^2\ne4\), the genus-four curve
\[
C_a:\qquad y^2=x^9+a x^5+x
\]
is geometrically smooth. Its Jacobian invariants are exactly
\[
(\operatorname{rank}_{11}J(C_a),\,a(J(C_a)))=
\begin{cases}
(0,2),&a(a^4-5a^2+2)=0,\\
(4,0),&a(a^4-5a^2+2)\ne0.
\end{cases}
\]
All five exceptional parameters give supersingular but non-superspecial Jacobians. The five are \(a=0\) and the four simple roots of \(a^4-5a^2+2\). The quartic is irreducible over \(\mathbf F_{11}\), so these other four parameters belong to \(\mathbf F_{11^4}\setminus\mathbf F_{11^2}\). The five parameters describe precisely three geometric isomorphism classes (one for \(a=0\), one for each root of \(z^2-5z+2\), with the two square roots identified).

## Assumptions and scope
The ground field is algebraically closed of characteristic \(11\). The \(11\)-rank denotes the stable rank of geometric Frobenius on the first coherent cohomology, equivalently the dimension of the \(\mathbf F_{11}\)-vector space of geometric \(11\)-torsion points of the Jacobian. The \(a\)-number denotes \(\dim_k\operatorname{Hom}(\alpha_{11},J(C_a))\), equivalently the dimension of the kernel of Cartier on regular differentials. Supersingular means all Newton slopes are \(1/2\); superspecial is stronger and would require \(a\)-number \(4\).

Write \(f_a(x)=x(x^8+a x^4+1)\). Outside \(x=0\), put \(u=x^4\). Repeated roots of \(u^2+a u+1\) occur exactly when \(a^2=4\); the root \(x=0\) is simple. Thus \(a^2\ne4\) is necessary and sufficient for smoothness of the genus-four hyperelliptic model.

## Proof
A basis of regular differentials is \(\{dx/y,x\,dx/y,x^2\,dx/y,x^3\,dx/y\}\). Let \(c_n\) be the coefficient of \(x^n\) in \(f_a(x)^5\) over \(\mathbf F_{11}[a]\). With rows and columns indexed from \(1\) to \(4\), the Frobenius-semilinear Hasse–Witt coefficient matrix \(H=(c_{11i-j})\) is
\[
H(a)=\begin{pmatrix}
0&5a&0&0\\
5a^4-3a^2-1&0&0&0\\
0&0&0&5a^4-3a^2-1\\
0&0&5a&0
\end{pmatrix}.
\]
This follows by direct coefficient extraction from \(x^5(x^8+a x^4+1)^5\), with every other indicated coefficient zero. Set \(A=5a\) and \(B=5(a^4-5a^2+2)=5a^4-3a^2-1\) in characteristic \(11\). Then \(\det H=(AB)^2\). If \(AB\ne0\), Frobenius is invertible, so the \(11\)-rank is \(4\) and the \(a\)-number is \(0\).

If \(AB=0\), the two polynomials never vanish together because \(A=0\) forces \(a=0\), whereas \(B(0)=-1\). Therefore \(\operatorname{rank}H=2\), so the \(a\)-number is \(2\). The zero/nonzero pattern further gives \(H(a)H(a)^{(11)}=0\) whenever \(AB=0\), where the superscript applies the eleventh power to coefficients. Thus the semilinear Frobenius has square zero and stable rank \(0\), proving \(11\)-rank zero.

To establish *supersingularity* rather than merely \(11\)-rank zero, consider the two commuting involutions on \(C_a\):
\[
\sigma(x,y)=(x^{-1},y/x^5),\qquad
\tau(x,y)=(x^{-1},-y/x^5).
\]
They extend to the smooth projective model since \(f_a(x^{-1})=f_a(x)/x^{10}\), and their product is the hyperelliptic involution. For \(a^2\ne4\), \(\sigma\) fixes exactly the two points above \(x=1\), while \(\tau\) fixes exactly the two points above \(x=-1\). Riemann–Hurwitz yields quotient genus \(2\) in both cases. The invariant and anti-invariant parts of first cohomology under either involution give an isogeny
\[
J(C_a)\sim J(C_a/\langle\sigma\rangle)\times J(C_a/\langle\tau\rangle)
\]
(the identification is separable of degree a power of \(2\)). Since \(J(C_a)\) has \(11\)-rank zero at an exceptional parameter, both genus-two quotient Jacobians have \(11\)-rank zero. For an abelian surface the only Newton polygon of \(11\)-rank zero has all slopes \(1/2\). The isogeny therefore forces all eight slopes of \(J(C_a)\) to be \(1/2\). The previously computed \(a\)-number \(2\) excludes superspeciality.

For the exact parameter count, let \(z=a^2\). The nonzero exceptional parameters satisfy \(z^2-5z+2=0\). Its discriminant is \(17\equiv6\pmod{11}\), a nonsquare, so the two values of \(z\) lie in \(\mathbf F_{11^2}\setminus\mathbf F_{11}\). Each has norm \(2\), also a nonsquare in \(\mathbf F_{11}\); hence neither is a square in \(\mathbf F_{11^2}\). Each has two distinct square roots in \(\mathbf F_{11^4}\setminus\mathbf F_{11^2}\). These roots and \(a=0\) are smooth, since \(a^4-5a^2+2\) evaluates to \(-2\ne0\) at \(a=\pm2\). They give five distinct parameters in total.

Finally, the established geometric isomorphism criterion for this hyperelliptic normal form identifies \(C_{a_1}\cong C_{a_2}\) exactly when \(a_1^2=a_2^2\): Ohashi–Kudo, Proposition 3.2.4 and Remark 3.2.2, using \(\lambda+\lambda^{-1}=a^2-2\). The exceptional values therefore represent three geometric isomorphism classes. At \(a=0\) the automorphism group is larger; at the other four roots it is dihedral of order \(16\).

## Verification
Execute \(\texttt{python3 verification/check_p11.py}\) from the directory containing this document. The dependency-free program recomputes all sixteen Hasse–Witt coefficients symbolically in \(\mathbf F_{11}[a]\), checks their polynomial formulas, confirms the nonsquare discriminant and norm, tests the smooth rational parameter cases, and reproduces two finite-field point-count sanity checks. The isogeny, Newton-polygon implication, and isomorphism classification are proved mathematically above rather than inferred from finite experiments.

## Relationship to prior work
Ohashi and Kudo introduced the displayed dihedral genus-four normal form, its isomorphism criterion, and sparse Cartier matrices in the superspecial setting [1]. Their superspecial criterion and enumeration do not state the full characteristic-eleven ordinary/supersingular dichotomy or its three exceptional geometric isomorphism classes; their computations of superspecial curves begin at larger characteristics. Cavalieri and Pries studied a cyclic-cover presentation of this dihedral family and obtained a weighted formula for its nonordinary locus [2, §8], but explicitly left its \(a\)-number uncomputed in general. Their weighted count alone does not determine the present individual parameters, Newton polygons, and three isomorphism classes. Kudo–Harashita–Senda established supersingular genus-four existence in arbitrary characteristic using Howe curves [3], a different existence assertion not classifying the present locus. The odd-abelian-cover results of Lin–Mantovan–Singhal [4] impose an odd-order covering group, unlike this dihedral family with cyclic order \(8\).

## Limitations
This theorem describes only this one-parameter family in characteristic \(11\), not the entire supersingular locus of genus-four curves. The parameter count differs from a count of geometric isomorphism classes. The five roots are geometric points; a field of definition for the displayed coefficient is not a claim about minimal fields of moduli or descent for abstract curves. The theorem's proof invokes the published normal-form isomorphism criterion and the standard isogeny decomposition for two commuting involutions. No independently certified formal proof is claimed. An equivalent, unindexed arithmetic classification remains a possible bibliographic priority risk.

## References
[1] R. Ohashi and M. Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858 (first public 2023-12-28), §§2.2 and 3.2, https://arxiv.org/abs/2312.16858 .

[2] R. Cavalieri and R. Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891 (first public 2023-08-28), §8, https://arxiv.org/html/2308.14891v3 .

[3] M. Kudo, S. Harashita and H. Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic*, arXiv:1903.08095 (first public 2019-03-19), https://arxiv.org/abs/1903.08095 .

[4] Y. Lin, E. Mantovan and A. Singhal, *Non-p-ordinary smooth abelian covers of the projective line*, arXiv:2406.09632 (first public 2024-06-13), https://arxiv.org/html/2406.09632v2 .
