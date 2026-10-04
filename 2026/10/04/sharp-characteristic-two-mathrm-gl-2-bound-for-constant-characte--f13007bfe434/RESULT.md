# Sharp characteristic-two \(\mathrm{GL}_2\) bound for constant-characteristic-polynomial cosets
## Finding
Let \(q=2^e\) with \(e\ge1\), let \(H\le \mathrm{GL}_2(\mathbb F_q)\), and let \(x\in\mathrm{GL}_2(\mathbb F_q)\). Assume \(\chi_{xh}=\chi_x\) for every \(h\in H\). Then \(H\) is abelian and \(|H|\le q+1\). If \(\operatorname{tr}(x)\ne0\), then \(H\) is conjugate to a subgroup of \(\{\begin{pmatrix}1&t\\0&1\end{pmatrix}:t\in\mathbb F_q\}\), so \(|H|\le q\). If \(\operatorname{tr}(x)=0\), then the algebra \(A=\operatorname{span}_{\mathbb F_q}H\) has dimension at most \(2\); when \(\dim A=2\), its determinant-one unit group has order \(q-1\), \(q\), or \(q+1\) according as \(A\cong\mathbb F_q\times\mathbb F_q\), \(\mathbb F_q[\varepsilon]/(\varepsilon^2)\), or \(\mathbb F_{q^2}\). Equality \(|H|=q+1\) occurs exactly when \(A\cong\mathbb F_{q^2}\) and \(H\) is its full norm-one subgroup; the bound is attained by the norm-one torus acting on \(\mathbb F_{q^2}\), with \(x\) equal to the Frobenius map \(z\mapsto z^q\).

## Assumptions and scope
Let \(q=2^e\) with \(e\ge1\). All matrices are \(2\times2\) over \(\mathbb F_q\). For \(A\in M_2(\mathbb F_q)\), \(\chi_A\) denotes its characteristic polynomial. The hypothesis is that a left coset \(xH\) has one characteristic polynomial:
\[
\chi_{xh}=\chi_x\qquad(h\in H),
\]
with \(x\) invertible. No assumption is made that the matrices in the coset are conjugate.

## Proof
Equality of characteristic polynomials gives, for every \(h\in H\),
\[
\det h=1,\qquad \operatorname{tr}(xh)=\operatorname{tr}x.
\]
Hence \(H\le \mathrm{SL}_2(\mathbb F_q)\).

First suppose \(\operatorname{tr}x\ne0\). For \(h\in\mathrm{SL}_2(\mathbb F_q)\), Cayley--Hamilton gives
\[
h+h^{-1}=(\operatorname{tr}h)I.
\]
Applying \(Y\mapsto\operatorname{tr}(xY)\) and using the hypothesis for both \(h\) and \(h^{-1}\) yields
\[
0=2\operatorname{tr}x=(\operatorname{tr}h)(\operatorname{tr}x).
\]
Thus \(\operatorname{tr}h=0\). Since the characteristic is \(2\) and \(\det h=1\), Cayley--Hamilton gives \(h^2=I\). Therefore \(H\) has exponent at most \(2\), so it is abelian. If \(H\ne\{I\}\), choose \(u\ne I\) and write \(N=u-I\). Then \(N\ne0\), \(N^2=0\), and every element of \(H\) centralizes \(N\). The centralizer of a nonzero nilpotent \(2\times2\) matrix is \(\mathbb F_q I+\mathbb F_qN\). Hence every \(h\in H\) has the form \(aI+bN\). The relation \(h^2=I\) gives \(a^2=1\), hence \(a=1\). Consequently
\[
H\le\{I+bN:b\in\mathbb F_q\},
\]
which is conjugate to the upper unitriangular group and has order \(q\).

Now suppose \(\operatorname{tr}x=0\), and set
\[
A=\operatorname{span}_{\mathbb F_q}H\le M_2(\mathbb F_q).
\]
Because \(H\) is a group, \(A\) is a unital subalgebra. The hypothesis gives \(\operatorname{tr}(xa)=0\) for every \(a\in A\). The trace pairing \(\langle Y,Z\rangle=\operatorname{tr}(YZ)\) on \(M_2(\mathbb F_q)\) is nondegenerate, so \(\dim A\ne4\). If \(\dim A=3\), then \(A^\perp\) is one-dimensional and is spanned by \(x\). For any \(a,b\in A\), closure under multiplication gives
\[
\operatorname{tr}((xa)b)=\operatorname{tr}(xab)=0.
\]
Thus \(xa\in A^\perp=\mathbb F_qx\) for every \(a\in A\). Since \(x\) is invertible, this forces every \(a\in A\) to be scalar, contradicting \(\dim A=3\). Therefore \(\dim A\le2\), and \(A\) is commutative.

If \(\dim A=1\), then \(H=\{I\}\). If \(\dim A=2\), choose a nonscalar \(T\in A\). Then \(A=\mathbb F_q[T]\), and the quadratic minimal polynomial of \(T\) is either split with distinct roots, repeated, or irreducible. Accordingly,
\[
A\cong \mathbb F_q\times\mathbb F_q,\qquad
A\cong \mathbb F_q[\varepsilon]/(\varepsilon^2),\qquad
A\cong \mathbb F_{q^2}.
\]
The determinant-one units have orders \(q-1\), \(q\), and \(q+1\), respectively. Indeed, these are respectively the kernel of multiplication in the split algebra, the elements \(1+b\varepsilon\), and the kernel of the field norm \(N_{\mathbb F_{q^2}/\mathbb F_q}\). Since \(H\) lies in this determinant-one group, \(|H|\le q+1\), with equality only in the field-algebra case and only for the full norm-one subgroup.

To see sharpness, let \(E=\mathbb F_{q^2}\), viewed as a two-dimensional \(\mathbb F_q\)-space. Let \(L_a\) denote multiplication by \(a\in E\), let \(\sigma(z)=z^q\), and put
\[
H=\{L_h:N_{E/\mathbb F_q}(h)=1\},\qquad x=\sigma.
\]
Then \(|H|=q+1\). For \(c\ne0\), the semilinear operator \(T_c=L_c\sigma\) satisfies \(T_c^2=N_{E/\mathbb F_q}(c)I\) and is not scalar; Cayley--Hamilton therefore gives
\[
\operatorname{tr}T_c=0,\qquad \det T_c=N_{E/\mathbb F_q}(c).
\]
For \(h\in H\), one has \(xL_h=L_{h^q}\sigma\) and \(N_{E/\mathbb F_q}(h^q)=1\). Thus \(\chi_{xL_h}=\chi_x\) for every \(h\in H\), proving attainability.

## Verification
The proof above is uniform in \(q\). As an independent finite check, `verify_even_gl2.py` enumerates every subgroup of \(\mathrm{SL}_2(\mathbb F_q)\), every \(x\in\mathrm{GL}_2(\mathbb F_q)\), and every admissible pair for \(q=2\) and \(q=4\). It finds maximal subgroup orders \(3=q+1\) and \(5=q+1\), respectively, no nonabelian admissible subgroup, and no violation of the stronger \(q\)-bound when \(\operatorname{tr}x\ne0\). The finite enumeration is supplementary and is not used to infer the theorem for general \(q\).

## Relationship to prior work
Avni and Gelander prove over every field and in every dimension that constant characteristic polynomial on \(xH\) forces the identity component of the Zariski closure of \(H\) to be solvable. For a finite field that conclusion is vacuous at the level of the abstract finite group, because every finite group is virtually solvable. Their inspected statement and examples do not give an exact \(2\times2\) finite-field structure theorem or an order bound. The present result supplies such a sharp characteristic-two specialization: abelianness, the three possible two-dimensional ambient algebras, and the extremal order \(q+1\).

Targeted searches for “constant characteristic polynomial”, “constant spectrum”, “isospectral coset”, \(\mathrm{GL}_2\), finite fields, and characteristic \(2\) did not locate a prior statement implying this theorem. Searches using “isospectral” predominantly concern equality of element-order spectra of finite groups, which is a different notion.

## Limitations
The theorem is specific to dimension \(2\) and to finite fields of characteristic \(2\). It does not classify all admissible pairs \((x,H)\) up to simultaneous conjugacy; it classifies the possible ambient algebra of \(H\), gives the sharp order bound, and characterizes equality. No claim is made here for higher dimensions.

## References
1. N. Avni and T. Gelander, *Cosets with constant characteristic polynomial*, arXiv:2609.27204v1, first submitted 2026-09-23 UTC; Theorem 1.1 gives virtual solvability over arbitrary fields.
2. N. Avni and T. Gelander, *Cosets with constant characteristic polynomial*, arXiv:2609.27204v2, Appendix A; the sharpness examples there are over \(\mathbb C\) and do not state the finite-field \(2\times2\) bound above.
