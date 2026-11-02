# Six affine conjugacy classes of Rota–Baxter operators on the canonical Heisenberg Lie affgebra

## Finding

Let \(k\) be an arbitrary field and \(H=kx\oplus ky\oplus kz\) the three-dimensional Heisenberg Lie algebra with \([x,y]=z\) and central \(z\). Give the underlying affine space the canonical Lie affgebra bracket \(\{u,v\}=[u,v]+v\). An affine map \(P\) is called a Rota–Baxter operator here when, for all \(u,v\in H\),
\[
\{P(u),P(v)\}=P\bigl(\{P(u),v\}-\{u,v\}+\{u,P(v)\}\bigr).
\]
The affine combination on the right is defined in the underlying vector space. Under conjugation by *automorphisms of this fixed canonical Lie affgebra*, there are exactly six such operators, represented, for \(h=ax+by+cz\), by
\[
P_0(h)=0,\quad P_1(h)=x,\quad P_2(h)=ax,\quad
P_3(h)=ax+cz,\quad P_4(h)=ax+cz+y,\quad P_5(h)=h.
\]
Here \(a,b,c\in k\). These representatives are pairwise inequivalent over **every field**, including characteristic two.

If \(k=\mathbb F_q\), the exact number of affine Rota–Baxter operators is
\[
\boxed{2q^4+3q^3+1}.
\]
The six corresponding conjugacy-orbit sizes in the displayed order are
\[
\boxed{q,\ q^3-q,\ q^3(q+1),\ q^2(q+1),\ q^2(q^2-1),\ 1}.
\]
For linear-part rank \(0,1,2,3\), respectively, the numbers of operators are \(q^3,q^3(q+1),q^3(q+1),1\).

## Assumptions and scope

The field is arbitrary; \(H\) has basis \(x,y,z\) and brackets \([x,y]=z\), \([x,z]=[y,z]=0\). The affine bracket and Rota–Baxter identity are exactly those displayed, not the purely linear Rota–Baxter identity on a Lie algebra. Two operators \(P,Q\) are equivalent precisely when \(Q=fPf^{-1}\) for an affine automorphism \(f\) satisfying \(f(\{u,v\})=\{f(u),f(v)\}\) on this *same* bracket. In particular, transformations that change the underlying Lie-affgebra bracket are excluded.

## Proof

**1. Projection reduction.** Every affine map has unique form \(P(h)=Rh+p\) with \(R\) linear. Expanding the displayed identity by degree in \(u,v\) shows that it is equivalent to
\[
R^2=R,\qquad Rp=0,\qquad R\operatorname{ad}_p=\operatorname{ad}_pR,
\]
\[
[R u,R v]=R\bigl([R u,v]+[u,R v]-[u,v]\bigr).
\]
These equations follow directly by comparing the constant, the two linear coefficients, and the bilinear term; the same expansion proves their sufficiency. Put \(U=\operatorname{im}R\) and \(W=\ker R\). The last identity holds for the projection \(R\) exactly when both \(U,W\) are Lie subalgebras: test inputs in each factor for necessity; for sufficiency write \(u=u_U+u_W\), \(v=v_U+v_W\), so the argument inside \(R\) becomes \([u_U,v_U]-[u_W,v_W]\). The other identities say \(p\in W\) and \([p,U]\subseteq U\), since \(W\) is already a Lie subalgebra. Thus the classification problem becomes: choose an ordered complementary pair of Lie subalgebras \(H=U\oplus W\), and a vector \(p\in W\) normalizing \(U\). This reduction is also the general canonical-affgebra theorem of Han--Khudoyberdiyev--Xie--Zhang (Theorem 4.4); it is used as an acknowledged antecedent, not claimed as new.

**2. Subalgebra geometry.** Every line in \(H\) is a Lie subalgebra. A two-dimensional subspace \(E\) is a Lie subalgebra *if and only if* \(z\in E\). Indeed, a plane avoiding \(z\) maps isomorphically to \(H/kz\); a basis of its image has nonzero alternating determinant, so the bracket of its lifts is a nonzero multiple of \(z\), outside \(E\). A plane containing \(z\) is automatically closed. Consequently, a nontrivial splitting has either \(\dim U=1,\dim W=2\) or \(\dim U=2,\dim W=1\); exactly the planar factor contains the center.

For \(\dim U=1\), \(W\) is a plane containing \(z\) and \(U\) is a noncentral complementary line. Since \([p,U]\subseteq kz\) whereas \(U\cap kz=0\), normalizing \(U\) means \([p,U]=0\); within \(W\) this forces \(p\in kz\). For \(\dim U=2\), \(U\) is a plane containing \(z\) and \(W\) is a noncentral line. All \(p\in W\) normalize \(U\), because \([H,U]\subseteq kz\subseteq U\). For \(R=0\), \(p\) is arbitrary; for \(R=I\), \(p=0\).

**3. Automorphism orbits.** Every Lie automorphism is uniquely given by \(A\in\mathrm{GL}_2(k)\), \(\ell\in\operatorname{Hom}_k(k^2,k)\), acting on \(v+cz\), \(v\in k^2\), as
\[
\phi(v+cz)=Av+\bigl(\ell(v)+(\det A)c\bigr)z.
\]
The canonical Lie-affgebra automorphisms are exactly \(f(h)=\phi(h)+tz\), \(t\in k\): compatibility of affine translation with the canonical bracket requires and suffices that the translation be central. On \(P=R+p\), conjugacy acts by
\[
R'=\phi R\phi^{-1},\qquad p'=\phi(p)+(I-R')tz.
\]
The natural \(\mathrm{GL}_2(k)\) action is transitive on ordered pairs of independent lines in \(H/kz\); the arbitrary functional \(\ell\) adjusts the central slope of complementary lines. Hence all rank-one splittings form one orbit. Their \(p\in kz\) can be removed using the translation \(tz\), since their projection kills \(z\). All rank-two splittings form one orbit before considering \(p\). For these, \(Rz=z\) and central translations cannot change \(p\); the stabilizer of a split pair acts transitively on the nonzero elements of its one-dimensional kernel. It follows that rank two has exactly two orbits, \(p=0\) and \(p\ne0\). Constant maps have exactly two orbits, according as their value belongs to \(kz\) or not: central translations act transitively on \(kz\), and \(\mathrm{GL}_2(k)\) together with \(\ell\) acts transitively on noncentral vectors. The identity is the final orbit. Rank, centrality of a constant value, and vanishing of the rank-two translation distinguish the six representatives.

**4. Exact finite-field counts.** There are \(q+1\) planes containing \(z\), and each such plane has \(q^2\) complementary lines (there are \(q^2+q+1\) lines in \(H\) and \(q+1\) inside the plane). The rank-one count is therefore \((q+1)q^2\cdot q=q^3(q+1)\); its orbit is single. Rank two has the same count, split into \((q+1)q^2=q^2(q+1)\) operators with \(p=0\), and \((q+1)q^2(q-1)=q^2(q^2-1)\) with \(p\ne0\). The \(q^3\) constant maps split into \(q\) central and \(q^3-q\) noncentral values; there is one identity. Summing gives \(2q^4+3q^3+1\), and all orbit sizes follow.

## Verification

The included standalone Python program `check_affine_heisenberg.py` enumerates idempotent linear parts, tests every defining affine Rota–Baxter identity on every ordered pair over \(\mathbb F_2\) and \(\mathbb F_3\), constructs the full affine Lie automorphism groups, and independently determines the conjugacy orbits. For \(\mathbb F_2\), it also compares with an exhaustive search over **every affine map**. The exact checks give 57 operators and six orbits over \(\mathbb F_2\), and 244 operators and six orbits over \(\mathbb F_3\), with orbit sizes as in the formula. The verified output is embedded as `verification_output.txt`. Finite tests support, but do not replace, the field-independent proof above. Run with `python3 check_affine_heisenberg.py`.

## Relationship to prior work

Han, Khudoyberdiyev, Xie and Zhang (arXiv:2610.14838, first posted October 10, 2026), Theorem 4.4, already give the general factorization-and-translation description of *all* affine Rota–Baxter operators on a canonical Lie affgebra, and Proposition 4.5 gives the conjugacy criterion. They classify operators up to automorphism on abelian Lie algebras and on Lie algebras of dimension at most two (Section 4.3); their scope is explicitly characteristic zero. The new contribution here is the **complete six-orbit conjugacy classification and exact finite-field operator/orbit counts for the first nonabelian nilpotent Lie algebra in dimension three**, including positive characteristics, rather than a new general operator parameterization. This conclusion is not explicitly stated by that paper, but its structural results make the reduction in Step 1 available.

Brzeziński (arXiv:2610.33573, first posted October 24, 2026), Proposition 4.5, shows affine translations can be gauged to zero under isomorphisms that may *change the Lie-affgebra bracket*. This does not identify the two rank-two orbits above, which are distinguished under automorphisms of a fixed canonical bracket. Earlier linear Heisenberg Lie Rota–Baxter classifications, for example Ji--Hua (2018) and Rathee (2024), do not classify these canonical affine operators or their finite-field orbits.

## Limitations

The result is specific to the canonical bracket on the three-dimensional Heisenberg algebra; it does not classify general Lie affgebra brackets, higher-dimensional Heisenberg algebras, or non-idempotent ordinary Lie Rota–Baxter operators. The general projection/factorization criterion is prior work. Earlier implicit deductions from this criterion or from historical Heisenberg linear-operator classifications cannot be ruled out absolutely; the novelty assessment compares exact statements and inspected material but is not a guarantee of historical priority. Computational checks are exhaustive only for the stated small fields, not a proof for all fields. No independent mathematical audit is claimed.

## References

1. J. Han, A. Khudoyberdiyev, Y. Xie, Y. Zhang, *Rota-Baxter operators and factorization of Lie affgebras*, arXiv:2610.14838 (2026), https://arxiv.org/abs/2610.14838. Sections 4.2--4.3, Theorem 4.4 and Proposition 4.5.
2. T. Brzeziński, *A note on Rota-Baxter affgebras*, arXiv:2610.33573 (2026), https://arxiv.org/abs/2610.33573, Proposition 4.5.
3. R. Rathee, *Rota–Baxter operators and skew left brace structures over Heisenberg group*, arXiv:2402.15428 (2024), https://arxiv.org/abs/2402.15428.
4. J. Ji, N. Hua, *Rota-Baxter operators of 3-dimensional Heisenberg Lie algebra*, Korean Journal of Mathematics 26 (2018), 53--60, https://doi.org/10.11568/kjm.2018.26.1.53.
