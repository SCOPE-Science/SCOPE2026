# A single symmetry jump in the \(E_\lambda\) evolution-algebra family
## Finding
Let \(K\) be a field, let \(\lambda\in K^\times\), and let \(E_\lambda\) be the three-dimensional evolution algebra with natural basis \(e_1,e_2,e_3\) and
\[
e_1^2=-e_1-e_3,\qquad
e_2^2=-2e_1+\lambda e_2+(\lambda-2)e_3,\qquad
e_3^2=e_1+e_3,
\]
with \(e_i e_j=0\) for \(i\ne j\). Then
\[
\operatorname{Aut}_K(E_\lambda)\cong
\begin{cases}
\{1\},&\lambda\ne4,\\
K^\times,&\lambda=4.
\end{cases}
\]
For \(\lambda=4\), writing \(u=e_1+e_3\), \(v=e_2+e_3\), and \(w=e_3\), every automorphism is uniquely
\[
\phi_\beta(u)=(1+2\beta)u,\qquad
\phi_\beta(v)=v+\beta u,\qquad
\phi_\beta(w)=w+\beta u,
\]
where \(\beta\in K\) and \(1+2\beta\ne0\); under \(t=1+2\beta\), composition becomes multiplication in \(K^\times\). Thus the pairwise non-isomorphic family has exactly one automorphism-symmetry jump, at \(\lambda=4\).

In particular, over a finite field \(\mathbb F_q\), every \(E_\lambda\) has one automorphism unless \(\lambda=4\). When \(\lambda=4\) is admissible, necessarily \(\operatorname{char}\mathbb F_q\ne2\), and
\[
|\operatorname{Aut}_{\mathbb F_q}(E_4)|=q-1.
\]

The symmetry jump occurs at a different parameter from the idempotent-free exceptional member \(\lambda=2\) emphasized in the motivating family, so the automorphism phenomenon is not merely a reformulation of the idempotent calculation.

## Assumptions and scope
The field \(K\) is arbitrary and \(\lambda\) is required only to be nonzero. The statement concerns ordinary \(K\)-linear algebra automorphisms. It does not identify the full automorphism group scheme after extension of scalars.

Put
\[
u=e_1+e_3,\qquad v=e_2+e_3,\qquad w=e_3.
\]
Then \(E_\lambda^2=S=\operatorname{span}_K\{u,v\}\), and direct multiplication gives
\[
u^2=0,\qquad uv=u,\qquad v^2=-u+\lambda v,
\]
together with
\[
uw=u,\qquad vw=u,\qquad w^2=u.
\]
These formulas remain valid in every characteristic with the usual interpretation of the coefficients.

## Proof
Because \(S=E_\lambda^2\) is characteristic, every \(\phi\in\operatorname{Aut}_K(E_\lambda)\) preserves \(S\). For \(x=au+bv\in S\),
\[
x^2=(2ab-b^2)u+\lambda b^2v.
\]
Since \(\lambda\ne0\), the square-zero elements of \(S\) are exactly the line \(Ku\). Hence
\[
\phi(u)=\alpha u
\]
for some \(\alpha\in K^\times\). Write
\[
\phi(v)=\beta u+\gamma v.
\]
Applying \(\phi\) to \(uv=u\) gives \(\alpha\gamma u=\alpha u\), so \(\gamma=1\). Applying \(\phi\) to \(v^2=-u+\lambda v\) and comparing the \(u\)-coefficient gives
\[
\alpha=1+(\lambda-2)\beta.
\]

Now write
\[
\phi(w)=pu+qv+cw.
\]
From \(uw=u\) we get \(q+c=1\). From \(vw=u\), comparison of the \(v\)-coefficient gives \(\lambda q=0\), hence \(q=0\) and \(c=1\). The remaining \(u\)-coefficient then gives
\[
p=\alpha-\beta-1.
\]
Finally, applying \(\phi\) to \(w^2=u\) yields
\[
2p+1=\alpha.
\]
Combining the last two identities with \(\alpha=1+(\lambda-2)\beta\) gives
\[
(4-\lambda)\beta=0.
\]

If \(\lambda\ne4\), then \(\beta=0\), hence \(\alpha=1\) and \(p=0\); therefore \(\phi\) is the identity.

If \(\lambda=4\), then \(\alpha=1+2\beta\) and \(p=\beta\). The map is invertible exactly when \(1+2\beta\ne0\), and substitution into the six displayed multiplication identities shows that every such map is an automorphism. Since \(\lambda=4\in K^\times\), this case cannot occur in characteristic \(2\). Thus \(2\) is invertible, and
\[
t=1+2\beta
\]
is a bijection from the admissible parameters to \(K^\times\). Direct composition gives
\[
1+2(\beta+\gamma+2\beta\gamma)=(1+2\beta)(1+2\gamma),
\]
so this bijection is a group isomorphism \(\operatorname{Aut}_K(E_4)\cong K^\times\).

## Verification
The proof uses only the multiplication table and preservation of the characteristic subspace \(E_\lambda^2\). Each coefficient comparison occurs in the basis \(u,v,w\), so no classification theorem or finite enumeration is needed.

The characteristic-\(2\) boundary is explicit: there \(4=0\), and because \(\lambda\in K^\times\), the exceptional equation \(\lambda=4\) is impossible. Hence the rigidity branch applies to every member in characteristic \(2\).

For \(\lambda=4\), the matrix of \(\phi_\beta\) in the ordered basis \(u,v,w\) is triangular with determinant \(1+2\beta\), exactly the stated invertibility condition.

## Relationship to prior work
Hu and Wen introduce the family \(E_\lambda\), determine its stable square \(E_\lambda^2\), its idempotents, and the pairwise isomorphism distinction among parameters. The inspected paper does not state the automorphism-group classification above.

Elduque and Labra describe automorphisms for evolution algebras satisfying \(E^2=E\). Here \(\dim E_\lambda^2=2<3=\dim E_\lambda\), so that coverage does not apply. Costoya, Mayorga, and Viruel study automorphism realizations for idempotent evolution algebras, a different structural setting.

The earlier three-dimensional classification of Cabrera Casado, Siles Molina, and Velasco is directly relevant background because the complex isomorphism class of the exceptional member already occurs there. Its accessible classification overview does not by itself settle the full self-isomorphism stabilizer used here; this remains the principal literature-overlap risk.

## Limitations
No claim is made about automorphism group schemes, semilinear automorphisms, or arbitrary three-dimensional evolution algebras. The result is specific to the displayed \(E_\lambda\) family.

An older case-by-case classification could encode the same stabilizer after a non-obvious change of basis even if it does not advertise an automorphism theorem. No such equivalent statement was located in the inspected sources or indexed scientific comparisons.

## References
1. X.-Y. Hu and R. Wen, *Idempotent-free non-solvable evolution algebras over \(\mathbb C\)*, arXiv:2609.25023v1, 2026.
2. A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191.
3. C. Costoya, P. Mayorga, and A. Viruel, *Permutation representations and automorphisms of evolution algebras*, arXiv:2401.05924.
4. Y. Cabrera Casado, M. Siles Molina, and M. V. Velasco, *Classification of three-dimensional evolution algebras*, Linear Algebra and its Applications 524 (2017), 68–108; arXiv:1701.07219.
