# A sharp binary failure of local-to-global invertibility for algebraic reflexive hulls
## Finding
Let \(V=\mathbf F_2^3\), and let
\[
E=\left\{M(a,b,c)=\begin{pmatrix}b&0&0\\ a&b+c&b\\ 0&0&c\end{pmatrix}:a,b,c\in\mathbf F_2\right\}\subseteq\operatorname{End}_{\mathbf F_2}(V).
\]
Then every element of \(E\) is singular, whereas
\[
\operatorname{Ref}_a(E)=E\oplus\mathbf F_2 I_3.
\]
The hull has exactly two invertible elements, \(I_3\) and \(I_3+E_{21}\). Consequently, over \(\mathbf F_2\), an algebraic reflexive hull can contain an invertible operator even when the original linear operator space contains none. Ambient dimension \(3\) is minimal for this phenomenon over \(\mathbf F_2\). The failure persists in every ambient dimension \(n\ge3\) by the block construction described below.

## Assumptions and scope
For a linear subspace \(S\subseteq\operatorname{End}_F(W)\), its algebraic reflexive hull is
\[
\operatorname{Ref}_a(S)=\{T\in\operatorname{End}_F(W):T(w)\in S(w)\text{ for every }w\in W\}.
\]
The claim is specifically about the binary field and ordinary algebraic reflexivity of finite-dimensional operator spaces. It does not assert an odd-characteristic analogue, a classification of all binary counterexamples in dimension \(3\), or a realization of the example as a derivation space.

## Proof
Write a general element of \(E\) as \(M(a,b,c)\). Its determinant is
\[
\det M(a,b,c)=bc(b+c).
\]
Over \(\mathbf F_2\), this vanishes for every \((a,b,c)\): if either \(b\) or \(c\) is zero then \(bc=0\), while if \(b=c=1\) then \(b+c=0\). Hence \(E\) contains no invertible operator.

Now let \(T\in\operatorname{Ref}_a(E)\). Evaluating on the standard basis vectors forces
\[
T=\begin{pmatrix}p&0&0\\ q&r&s\\ 0&0&t\end{pmatrix}
\]
for some \(p,q,r,s,t\in\mathbf F_2\). Evaluating at \(e_2+e_3\) gives the necessary relation
\[
r+s=t.
\]
Conversely, every matrix of the displayed form satisfying \(r+s=t\) lies in \(\operatorname{Ref}_a(E)\). Indeed, for \(v=(x,y,z)^{\mathsf T}\), if \(x=1\) one can choose \(b=p\), choose \(c=t\) when \(z=1\), and then choose \(a\) to match the middle coordinate. If \(x=0,z=1,y=0\), choose \(c=t\) and \(b=s\); if \(x=0,z=1,y=1\), the middle-coordinate condition is exactly \(r+s=t\); and if \(x=z=0\), one only needs to choose \(b+c=r\). Thus
\[
\operatorname{Ref}_a(E)=\left\{\begin{pmatrix}p&0&0\\ q&r&s\\ 0&0&t\end{pmatrix}:r+s=t\right\}.
\]
Putting \(b=s\), \(d=p+s\), and \(c=t+d\) rewrites every such matrix uniquely as \(M(a,b,c)+dI_3\), proving
\[
\operatorname{Ref}_a(E)=E\oplus\mathbf F_2I_3.
\]
An element of this hull is invertible exactly when \(p=r=t=1\). The relation \(r+s=t\) then forces \(s=0\), while \(q\) is free, giving exactly \(I_3\) and \(I_3+E_{21}\).

For sharpness of the ambient dimension over \(\mathbf F_2\), the included verifier enumerates every linear subspace of \(\operatorname{End}(\mathbf F_2^n)\) for \(n=1,2\), computes the reflexive-hull condition directly from its definition, and checks whether the hull contains the identity while the subspace contains no invertible map. There are exactly \(2\) subspaces for \(n=1\) and \(67\) for \(n=2\); none is a counterexample.

Finally, for \(n>3\) define
\[
E_n=\{M\oplus\lambda I_{n-3}:M\in E,\ \lambda\in\mathbf F_2\}.
\]
Every element of \(E_n\) is singular because its \(3\)-dimensional block \(M\) is singular. For every \((v,w)\in\mathbf F_2^3\oplus\mathbf F_2^{n-3}\), choose \(M_v\in E\) with \(M_vv=v\), which is possible because \(I_3\in\operatorname{Ref}_a(E)\), and take \(\lambda=1\) when \(w\ne0\). Hence \(I_n(v,w)\in E_n(v,w)\) for every vector, so \(I_n\in\operatorname{Ref}_a(E_n)\).

## Verification
The standalone verifier `verify.py` uses exact arithmetic over \(\mathbf F_2\). It reconstructs \(E\), checks singularity of all \(8\) elements, computes \(\operatorname{Ref}_a(E)\) directly by testing all \(512\) endomorphisms on all \(8\) vectors, confirms the exact \(16\)-element hull and its two invertible elements, and exhausts all subspaces of \(\operatorname{End}(\mathbf F_2)\) and \(\operatorname{End}(\mathbf F_2^2)\). A clean replay produces `VERIFY_OK` and reports zero smaller-dimensional counterexamples. The infinite family for \(n\ge3\) is proved symbolically and is not inferred from finite sampling.

## Relationship to prior work
Hao and Chen define the same algebraic reflexive hull and prove that, in their infinite-field setting, if \(\operatorname{Ref}_a(E)\) contains an invertible operator then \(E\) contains one. Their proof explicitly invokes infinitude of the field at the determinant-polynomial step. The present example shows that this implication has a sharp finite-field obstruction already over \(\mathbf F_2\) in ambient dimension \(3\).

Bračič studies finite-dimensional algebraic reflexivity over complex Banach spaces and provides general reflexive-cover tools, but this does not cover the finite-field obstruction. Recent finite-field work of Busaman, Tinpun, and Phokaew treats nonsingular three-spaces in \(M_4\) over finite fields; the present example has the opposite rank profile, since every element of \(E\) is singular. A focused comparison with the closest published published-finding corpus record on characteristic-two algebraic reflexive hulls found a result about failure of Lie closure, not about transfer of invertibility, so neither statement implies the other.

## Limitations
The minimality assertion is only over \(\mathbf F_2\). No claim is made about the smallest dimension over odd finite fields or about a complete orbit classification of binary counterexamples in \(M_3(\mathbf F_2)\). The block construction proves persistence in all higher binary dimensions but is not claimed to minimize the dimension of the operator space there. The comparison with the finite-field nonsingular-three-space literature used its public reproducibility record and stated scope; an equivalent all-singular example under different terminology remains a residual literature risk.

## References
1. Hao, Z.; Chen, Y. *Local derivations is a Lie algebra*. arXiv:2609.09198v1, 2026.
2. Bračič, J. *Reflexivity of finite-dimensional sets of operators*. Banach Journal of Mathematical Analysis 17 (2023), DOI 10.1007/s43037-023-00299-6.
3. Busaman, S.; Tinpun, K.; Phokaew, C. *Reproducibility package for: Local-annihilator relation codes and algebraic reflexivity of nonsingular three-spaces in M4 over finite fields*. Zenodo, DOI 10.5281/zenodo.21739707.
