# A center–abelianization criterion for nonlinear 2-local half-derivations
## Finding
Let \(k\) be a field with \(\operatorname{char}k\ne2\), and let \(L\) be a Lie algebra over \(k\). If
\[
Z(L)\ne0\qquad\text{and}\qquad \dim_k L/[L,L]\ge2,
\]
then \(L\) admits a nonadditive 2-local \(\frac12\)-derivation. More explicitly, choose \(0\ne z\in Z(L)\), choose linearly independent functionals \(\lambda_1,\lambda_2\in(L/[L,L])^*\), and pull them back to \(L\). Define
\[
f(s,t)=\begin{cases}s,&t=0,\\0,&t\ne0,\end{cases}
\qquad
\Delta(x)=x+f(\lambda_1(x),\lambda_2(x))z.
\]
Then \(\Delta\) is a 2-local \(\frac12\)-derivation but is not additive, hence is not a \(\frac12\)-derivation.

The criterion immediately applies to every totally graded filiform Lie algebra in Arzikulov–Shodiev's 2026 classification: the image of \(e_1,e_2\) spans the two-dimensional abelianization, while the top homogeneous vector \(e_n\) is central. Thus the paper's eleven-family construction is an instance of one intrinsic mechanism.
## Assumptions and scope
A \(\frac12\)-derivation is a linear map \(D:L\to L\) satisfying
\[
D([x,y])=\frac12\bigl([D(x),y]+[x,D(y)]\bigr)
\]
for all \(x,y\in L\). A map \(\Delta:L\to L\), not assumed linear, is 2-local if for every pair \(x,y\in L\) there is a \(\frac12\)-derivation \(D_{x,y}\) with \(\Delta(x)=D_{x,y}(x)\) and \(\Delta(y)=D_{x,y}(y)\).

No finite-dimensionality, algebraic-closedness, or nilpotence hypothesis is needed. The characteristic restriction is only the one required to interpret \(\frac12\). The criterion is sufficient, not necessary.
## Proof
Because \(\lambda_1\) and \(\lambda_2\) factor through \(L/[L,L]\), they vanish on \([L,L]\). For \(a,b\in k\), define the linear map
\[
D_{a,b}(u)=u+\bigl(a\lambda_1(u)+b\lambda_2(u)\bigr)z.
\]
Since \(z\) is central,
\[
[D_{a,b}(u),v]=[u,v],\qquad [u,D_{a,b}(v)]=[u,v].
\]
Since the two functionals vanish on every bracket,
\[
D_{a,b}([u,v])=[u,v].
\]
Therefore
\[
D_{a,b}([u,v])=\frac12\bigl([D_{a,b}(u),v]+[u,D_{a,b}(v)]\bigr),
\]
so every \(D_{a,b}\) is a \(\frac12\)-derivation.

The function \(f\) is homogeneous of degree one over every field: \(f(cs,ct)=c f(s,t)\) for every \(c,s,t\in k\). Fix \(x,y\in L\), and put
\[
p=(\lambda_1(x),\lambda_2(x)),\qquad q=(\lambda_1(y),\lambda_2(y)).
\]
We seek \(a,b\in k\) satisfying
\[
a p_1+b p_2=f(p),\qquad a q_1+b q_2=f(q).
\]
If \(p,q\) are linearly independent, the coefficient matrix is invertible. If they are dependent, degree-one homogeneity makes the two equations compatible; if one vector is zero, its equation is \(0=0\), and the remaining equation has a solution unless it is also zero, in which case every \((a,b)\) works. Hence a solution exists for every pair. For this solution, \(D_{a,b}\) agrees with \(\Delta\) at both \(x\) and \(y\), proving that \(\Delta\) is 2-local.

Finally, the map \(L\to k^2\), \(u\mapsto(\lambda_1(u),\lambda_2(u))\), is surjective because \(\lambda_1,\lambda_2\) are independent. Choose \(x,y\) mapping to \((1,0)\) and \((0,1)\). Then
\[
f(1,0)=1,\qquad f(0,1)=0,\qquad f(1,1)=0,
\]
so
\[
\Delta(x+y)-\Delta(x)-\Delta(y)=-z\ne0.
\]
Thus \(\Delta\) is not additive and cannot be a \(\frac12\)-derivation.
## Verification
The proof above is symbolic and does not depend on computation. As a finite sanity check, `verify.py` specializes the construction to the three-dimensional Heisenberg Lie algebra over \(\mathbb F_5\), exhaustively verifies all \(25\) maps \(D_{a,b}\) against the \(\frac12\)-derivation identity on all ordered element pairs, verifies interpolation for all \(15{,}625\) ordered pairs of elements, and confirms nonadditivity. The recorded output ends with `CHECK_OK`.
## Relationship to prior work
Arzikulov and Shodiev prove in Theorem 24 of arXiv:2610.01556v1 that each of eleven totally graded complex filiform families admits a nonlinear 2-local \(\frac12\)-derivation. Their proof uses a degree-one homogeneous function of the first two coordinates and two free entries in the last row of a family-specific \(\frac12\)-derivation matrix. The present criterion isolates the structural content behind that construction: two independent abelianization functionals supply the interpolation coordinates, and any nonzero central vector supplies the target direction. It therefore removes the family-by-family matrix classification from the existence argument and works over every field of characteristic different from \(2\).

Khudoyberdiyev and Yusupov introduced local and 2-local \(\frac12\)-derivations for finite-dimensional Lie algebras and gave classifications for several solvable families. Their general rigidity theorem states that if all \(\frac12\)-derivations are trivial, then no genuinely new local or 2-local \(\frac12\)-derivation occurs. That result does not imply the sufficient center–abelianization criterion above. Related literature on ordinary 2-local derivations and on Leibniz-algebra \(\frac12\)-derivations uses similar two-point homogeneous interpolation in specific examples; the interpolation technique itself is therefore not claimed as new.
## Limitations
The theorem gives only a sufficient condition. It does not classify all 2-local \(\frac12\)-derivations, and it says nothing when \(Z(L)=0\) or \(\dim_kL/[L,L]<2\). It also excludes characteristic \(2\). The originality comparison is strongest against the inspected recent filiform paper and the earlier general Lie-algebra paper; older or weakly indexed literature could contain an equivalent structural formulation.
## References
1. F. Arzikulov and M. Shodiev, “Local and 2 local \(\frac12\)-derivation of \(n\)-dimensional totally graded filiform Lie algebras,” arXiv:2610.01556v1, 2026.
2. A. Khudoyberdiyev and B. Yusupov, “Local and 2-local \(\frac12\)-derivations on finite-dimensional Lie algebras,” arXiv:2402.09818v1, 2024.
