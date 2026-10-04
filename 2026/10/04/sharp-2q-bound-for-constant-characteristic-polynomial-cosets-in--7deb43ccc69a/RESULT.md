# Sharp \(2q\) bound for constant-characteristic-polynomial cosets in \(\mathrm{GL}_2(\mathbb F_q)\)
## Finding
Let \(q\) be an odd prime power, let \(H\leq \mathrm{GL}_2(\mathbb F_q)\), and let \(x\in \mathrm{GL}_2(\mathbb F_q)\). Assume \(\chi_{xh}=\chi_x\) for every \(h\in H\). Then \(H\) is abelian and \(|H|\leq 2q\). More precisely, if \(\operatorname{tr}(x)\neq0\), then \(H\) is conjugate into a one-parameter upper-unitriangular group and \(|H|\leq q\). If \(\operatorname{tr}(x)=0\), then either \(H\subseteq\{\pm I\}\), or there is a nonzero traceless matrix \(y\) such that \(H\) is contained in the determinant-one units of the commutative algebra \(\mathbb F_q I+\mathbb F_q y\); writing \(y^2=\delta I\), that ambient norm-one group has order \(2q\), \(q-1\), or \(q+1\) according as \(\delta=0\), \(\delta\) is a nonzero square, or \(\delta\) is a nonsquare. The bound \(2q\) is sharp. Equality holds exactly, up to simultaneous conjugacy, when \(H=\{\pm\begin{psmallmatrix}1&t\\0&1\end{psmallmatrix}:t\in\mathbb F_q\}\) and \(x=\begin{psmallmatrix}a&b\\0&-a\end{psmallmatrix}\) with \(a\neq0\); every such pair has constant characteristic polynomial on \(xH\).\n\n## Assumptions and scope
The field is \(\mathbb F_q\) with \(q\) odd. The hypothesis is literal equality \(\chi_{{xh}}=\chi_x\) for every \(h\in H\), where \(H\) is an arbitrary subgroup of \(\mathrm{{GL}}_2(\mathbb F_q)\) and \(x\) is invertible. No generation, irreducibility, or closure hypothesis is imposed.

## Proof
Equality of characteristic polynomials gives both \(\det(h)=1\) and \(\operatorname{{tr}}(xh)=\operatorname{{tr}}(x)\) for every \(h\in H\), so \(H\leq\mathrm{{SL}}_2(\mathbb F_q)\). Since \(h^{{-1}}=\operatorname{{tr}}(h)I-h\) in dimension two, applying the trace condition to \(h^{{-1}}\) yields
\[
(\operatorname{{tr}}(h)-2)\operatorname{{tr}}(x)=0.
\]

Suppose first that \(\operatorname{{tr}}(x)\neq0\). Then every \(h\in H\) has trace \(2\), hence is unipotent. Write nonidentity elements as \(I+N\) with \(N^2=0\). If \(I+N,I+M\in H\), then their product also has trace \(2\), so \(\operatorname{{tr}}(NM)=0\). For nonzero rank-one nilpotent \(2\)-by-\(2\) matrices this forces \(M\) to be a scalar multiple of \(N\): writing \(N=u\varphi\) and \(M=v\psi\), nilpotence gives \(\ker\varphi=\mathbb F_q u\) and \(\ker\psi=\mathbb F_q v\), while \(\operatorname{{tr}}(NM)=\varphi(v)\psi(u)=0\). Thus all nilpotent parts lie on one line. After conjugacy, \(H\) lies in \(\{\begin{{psmallmatrix}}1&t\\0&1\end{{psmallmatrix}}:t\in\mathbb F_q\}\), so \(H\) is abelian and \(|H|\leq q\).

Now suppose that \(\operatorname{{tr}}(x)=0\). For \(h\in H\), write \(h=a_hI+y_h\), where \(a_h=\operatorname{{tr}}(h)/2\) and \(y_h\in\mathfrak{{sl}}_2(\mathbb F_q)\). Let
\[
V=\{y\in\mathfrak{{sl}}_2(\mathbb F_q):\operatorname{{tr}}(xy)=0\}.
\]
Then each \(y_h\) lies in \(V\). Because \(x\) is invertible and traceless, \(\operatorname{{tr}}(x^2)=-2\det(x)\neq0\), so \(V\) is two-dimensional. For \(h,k\in H\), expanding \(hk\) and using \(\operatorname{{tr}}(xhk)=0\) gives
\[
\omega(y_h,y_k):=\operatorname{{tr}}(xy_hy_k)=0.
\]
The form \(\omega\) is alternating on \(V\), since every traceless \(2\)-by-\(2\) matrix \(y\) satisfies \(y^2=-\det(y)I\). It is nondegenerate: if \(\omega(y,z)=0\) for all \(z\in V\), then invariance of the trace pairing gives \(\operatorname{{tr}}([x,y]z)=2\omega(y,z)=0\) for all \(z\in V\). Hence \([x,y]\) lies in both \(V\) and its trace-orthogonal complement \(\mathbb F_qx\), so \([x,y]=0\). The centralizer of the nonscalar matrix \(x\) in \(\mathfrak{{sl}}_2\) is \(\mathbb F_qx\), and \(x\notin V\), forcing \(y=0\).

Thus the span of all \(y_h\) is a totally isotropic subspace of the two-dimensional symplectic space \(V\), so it has dimension at most one. Unless all \(y_h=0\), choose a nonzero traceless \(y\) spanning it. Then \(H\subseteq\mathbb F_qI+\mathbb F_qy\), a commutative quadratic algebra. Put \(y^2=\delta I\). For \(a,b\in\mathbb F_q\),
\[
\det(aI+by)=a^2-\delta b^2.
\]
Consequently the determinant-one units in this algebra have exactly \(2q\) elements when \(\delta=0\), exactly \(q-1\) when \(\delta\) is a nonzero square, and exactly \(q+1\) when \(\delta\) is a nonsquare. This proves abelianness and the sharp bound \(|H|\leq2q\).

If equality holds, necessarily \(\delta=0\) and \(H\) is the full determinant-one group of a dual-number algebra. Conjugating its nonzero nilpotent generator to \(N=\begin{{psmallmatrix}}0&1\\0&0\end{{psmallmatrix}}\) gives \(H=\{\pm(I+tN):t\in\mathbb F_q\}\). The two equations \(\operatorname{{tr}}(x)=0\) and \(\operatorname{{tr}}(xN)=0\) force \(x=\begin{{psmallmatrix}}a&b\\0&-a\end{{psmallmatrix}}\), and invertibility forces \(a\neq0\). Conversely these matrices have fixed determinant and zero trace after multiplication by every element of \(H\), proving the equality characterization.

## Verification
A standalone exact checker exhaustively enumerates every subgroup of \(\mathrm{{SL}}_2(\mathbb F_q)\) and every possible invertible left multiplier for \(q=3\) and \(q=5\). It confirms that every qualifying subgroup is abelian, that the maximal orders are respectively \(6\) and \(10\), and that equality occurs. The checker is only a finite regression test; the arbitrary-prime-power statement is established by the proof above.

## Relationship to prior work
Avni and Gelander prove that over an arbitrary field and in arbitrary dimension, constancy of the characteristic polynomial on a coset \(xH\) forces the identity component of the Zariski closure of \(H\) to be solvable. Their Appendix A gives unipotent and toral examples and discusses sharpness over \(\mathbb C\). For a finite subgroup, however, virtual solvability alone imposes no effective restriction, and the inspected paper does not give the odd-finite-field \(2\)-dimensional abelianness classification, the exact three norm-one ambient sizes, or the sharp order bound \(2q\). Semantic and exact-phrase searches for these formulations did not locate a published statement implying them.

## Limitations
The theorem is restricted to odd characteristic. Characteristic two has a degenerate trace-form geometry and is not covered. The result is specific to dimension two and does not claim analogous order bounds in higher dimension. The computational verification covers only \(q=3\) and \(q=5\) and is not used as evidence for the infinite family beyond checking the symbolic argument on small fields. Older low-dimensional finite-linear-group literature could contain an equivalent statement under different terminology; no such source was located in the searches recorded in the review.

## References
1. N. Avni and T. Gelander, *Cosets with constant characteristic polynomial*, arXiv:2609.27204v1 (first public version, 23 September 2026); current inspected version v2, 29 September 2026. Theorem 1.1 and Appendix A.
2. Mathematics Subject Classification 2020, class 20H30: other matrix groups over finite fields.
