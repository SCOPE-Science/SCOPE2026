# Rank spectrum and large-field concentration of retractions of finite Heisenberg Lie algebras

## Finding

Let \(m\ge 2\), let \(q\) be any prime power, and let \(H_m(\mathbb F_q)\) be the \((2m+1)\)-dimensional Heisenberg Lie algebra. An algebra retraction means a \(\mathbb F_q\)-linear Lie endomorphism \(e\) with \(e^2=e\). The **complete linear-rank enumerator** of these retractions is

\[
R_{m,q}(t)=1+t^{2m+1}+\sum_{r=1}^{m} a_{m,r}(q)t^r,\qquad
 a_{m,r}(q)=q^{r(2m-r+1)}\prod_{i=0}^{r-1}\frac{q^{2m-i}-q^i}{q^r-q^i}.
\]

There are no retractions of any other ranks. In particular, every proper nonzero retract is an abelian subalgebra of dimension at most \(m\), while zero and identity are the unique retractions of ranks zero and \(2m+1\), respectively.

For every fixed \(m\ge2\), as prime powers \(q\to\infty\), the rank distribution is controlled by

\[
E_m(r)=\frac{8mr-5r^2+3r}{2},\qquad
 a_{m,r}(q)=q^{E_m(r)}\bigl(1+O_m(q^{-1})\bigr).
\]

Set \(r_\star=\lfloor(4m+4)/5\rfloor\). If \(m\not\equiv 4\pmod5\), then a uniformly selected idempotent Lie endomorphism has rank \(r_\star\) with probability tending to \(1\). If \(m\equiv4\pmod5\), the limiting probabilities of ranks \(r_\star-1\) and \(r_\star\) are each \(1/2\), and all other ranks have limiting probability zero. The first tied case is \(m=4\), with ranks \(3\) and \(4\). Thus the dominant proper retract dimension is asymptotic to four fifths of the symplectic half-dimension as \(m\) increases.

## Assumptions and scope

Fix a finite field \(K=\mathbb F_q\), a \(2m\)-dimensional symplectic vector space \((V,\omega)\), and a central basis vector \(z\). The Lie bracket on \(H=V\oplus Kz\) is \([v+az,w+bz]=\omega(v,w)z\). Here \(\omega\) is nondegenerate and alternating. The argument holds without excluding characteristic two. Rank is the \(K\)-linear dimension of the image. The finite-field hypothesis is used for counting; the structural classification preceding enumeration holds over any field.

## Proof

**1. Parametrize endomorphisms.** Because \([H,H]=Kz\), any Lie endomorphism must have the form

\[
f(v+az)=Av+\bigl(\ell(v)+ca\bigr)z,
\]

for \(A\in\operatorname{End}_K(V)\), \(\ell\in V^*\), and \(c\in K\). Bracket preservation is precisely \(\omega(Av,Aw)=c\omega(v,w)\) for all \(v,w\in V\). The idempotence condition gives \(A^2=A\), \(c^2=c\), and \(\ell A+c\ell=\ell\). As \(K\) is a field, \(c\in\{0,1\}\).

**2. Separate the central scalar.** If \(c=1\), the map \(A\) preserves the nondegenerate form, hence is invertible. Together with \(A^2=A\), this forces \(A=\operatorname{id}_V\), and \(\ell A=0\) then forces \(\ell=0\). Thus this branch consists solely of the identity of \(H\). If \(c=0\), the image \(U=\operatorname{im}A\) is totally isotropic, and \(A\) is a projection onto \(U\). Therefore \(r=\dim U\) satisfies \(0\le r\le m\). The functional condition \(\ell A=\ell\) is equivalent to choosing any functional on \(U\) and composing it with \(A\). This gives exactly \(q^r\) choices. The image of the full endomorphism is the graph of that functional over \(U\), and has rank \(r\). For \(r=0\), only the zero endomorphism occurs.

**3. Count isotropic images and complements.** Ordered independent isotropic vectors spanning an \(r\)-plane can be selected successively in

\[
\prod_{i=0}^{r-1}(q^{2m-i}-q^i)
\]

ways: after an isotropic \(i\)-plane has been chosen, the next vector lies in its symplectic orthogonal complement (size \(q^{2m-i}\)) but not in that plane (size \(q^i\)). Dividing by \(\lvert\operatorname{GL}_r(\mathbb F_q)\rvert=\prod_{i=0}^{r-1}(q^r-q^i)\) gives the number of isotropic \(r\)-planes. For fixed \(U\), choose one complement of dimension \(2m-r\). Every other complement is the graph of a unique linear map from that complement to \(U\); hence exactly \(q^{r(2m-r)}\) projections have image \(U\). Multiplying by \(q^r\) choices of \(\ell\) gives the formula.

**4. Determine large-field concentration.** Every factor in the displayed isotropic-plane count has leading coefficient one. Its degree plus the projection and functional powers is \(E_m(r)=(8mr-5r^2+3r)/2\). Successive degree differences are

\[
E_m(r)-E_m(r-1)=4m-5r+4.
\]

This strictly decreases in \(r\). Its zero lies at an integral \(r\) exactly when \(m\equiv4\pmod5\). Otherwise there is a unique maximizing rank \(r_\star\); in the congruence case there are two consecutive maximizing ranks \(r_\star-1\) and \(r_\star\). Their leading coefficients are both one. As the sum defining \(R_{m,q}(1)\) has finitely many positive terms and both exceptional ranks have constant count one, dividing by the total yields the asserted limiting probabilities. This establishes the result.

## Verification

The standalone `verify_heisenberg.py` computes matrices directly over small prime fields, rather than using isotropic-plane formulas to enumerate candidates. It tests \(A^2=A\), the bilinear bracket-preservation equation and the central-coordinate idempotence equation. Its exhaustive checks give proper rank counts \((1,12)\) for \((m,q)=(1,2)\), \((1,36)\) for \((1,3)\), \((1,150)\) for \((1,5)\), and \((1,240,960)\) for \((2,2)\). For \((m,q)=(2,2)\), adding the identity gives exactly \(1202\) retractions, with rank multiplicities \(1,240,960,1\) at ranks \(0,1,2,5\). The code checks the proposed phase maximizing ranks for \(1\le m\le30\). This finite verification is corroborative; the proof above establishes all fields and dimensions within scope.

## Relationship to prior work

Isotropic subspaces of symplectic spaces are classical objects; their role in symplectic Grassmannians is discussed by Balla and Olarte [1]. Rossmann [2] constructs graph-based finite-field nilpotent Lie algebras and studies conjugacy invariants of the associated groups. Related work on commuting spaces of Heisenberg groups is [3]. Those sources do not state a rank-resolved census of idempotent Lie endomorphisms or its large-field dominant-rank transition. Existing group centralizer, Lie-subalgebra commutativity and automorphism statistics likewise do not imply this retract count: the present count requires individual isotropic images, complements and central-coordinate functionals. General elementary facts about projections, isotropic flag enumeration and their leading-degree estimates are used rather than claimed as discoveries. Literature priority remains conditional on broader terminology and inaccessible sources.

## Limitations

The counted maps must be \(K\)-linear Lie endomorphisms; additive-group endomorphisms or field-semilinear maps are not included. The result concerns Heisenberg Lie algebras, not Heisenberg groups, associative Weyl algebras or all two-step nilpotent Lie algebras. The concentration statement fixes \(m\) and then lets \(q\) grow; no uniform error estimate when both parameters vary is claimed. The rank-one \(m=1\) boundary follows from the proof but is not presented as a novel instance. Numerical checks for finite small cases do not replace the uniform proof. Publication precedence is not claimed from absence of a search match.

## References

[1] George Balla and Jorge Alberto Olarte, *The tropical symplectic Grassmannian*, arXiv:2103.16512v1, first posted 2021-03-30.

[2] Tobias Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564v1 (first posted 2021-07-12), especially the graphical Lie-algebra construction and centralizer invariants.

[3] *Topological components of spaces of commuting elements in connected nilpotent Lie groups*, arXiv:2405.09652v1, first posted 2024-05-15; Heisenberg examples and commuting-space questions.
