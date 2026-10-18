# The finite-field Peirce-incidence obstruction for symmetric Jordan matrices

## Finding
Let \(q\) be any odd prime power, \(K=\mathbb F_q\), and \(J=H_2(K)\) the three-dimensional Jordan algebra of symmetric \(2\times2\) matrices under \(X\circ Y=(XY+YX)/2\). Let \(\mathcal P\) be the set of primitive (rank-one) idempotents of \(J\), and for each \(X\in J\) define the **terminal-idempotent incidence**
\[
\kappa(X)=\#\{P\in\mathcal P:X\in P\circ J\}.
\]
Write \(\epsilon=\chi(-1)\in\{-1,1\}\), where \(\chi\) denotes the quadratic character of \(K\) with \(\chi(0)=0\). Then \(|\mathcal P|=q-\epsilon\), and the complete distribution of \(\kappa\) is as follows:

* If \(\epsilon=-1\), then
\[
\#\{X:\kappa(X)=0\}=\frac{q(q-1)^2}{2},\quad
\#\{X:\kappa(X)=1\}=q^2-1,\quad
\#\{X:\kappa(X)=2\}=\frac{q(q^2-1)}2,\quad
\#\{X:\kappa(X)=q+1\}=1.
\]
* If \(\epsilon=1\), then
\[
\#\{X:\kappa(X)=0\}=\frac{q^3-2q^2+7q-6}{2},\quad
\#\{X:\kappa(X)=1\}=3(q-1)^2,\quad
\#\{X:\kappa(X)=2\}=\frac{(q-1)^2(q-2)}2,\quad
\#\{X:\kappa(X)=q-1\}=1.
\]
All other incidence values occur zero times. The unique matrix having \(\kappa(X)=q-\epsilon\) is \(X=0\).

Every finite left-nested Jordan word in idempotents is either \(I_2\) or belongs to \(P\circ J\) for some \(P\in\mathcal P\). In particular, **every nonscalar matrix with \(\kappa(X)=0\) is not representable as such a word**. The exact numbers of nonscalar matrices excluded by this obstruction are respectively
\[
\frac{(q-1)(q-2)(q+1)}2\quad(\epsilon=-1),\qquad
\frac{q^3-2q^2+5q-4}2\quad(\epsilon=1).
\]
These are proven exclusion counts, not asserted to be the total numbers of nonrepresentable matrices.

## Assumptions and scope
The characteristic is odd; all quantities refer to \(K\)-rational symmetric matrices, not hermitian matrices or the full nonsymmetric matrix algebra. A Jordan word is a nonempty left-nested expression \(((E_1\circ E_2)\circ\cdots)\circ E_m\) with all \(E_i\) idempotent; multiplication by \(I_2\) is allowed. The empty word is not needed. The distribution counts **possible terminal Peirce factors**; it does not count distinct word decompositions or prove that every element with positive \(\kappa\) is a word.

For explicit evaluation on one matrix, write uniquely
\[
X=aI_2+\begin{pmatrix}u&v\\v&-u\end{pmatrix},\qquad Q(u,v)=u^2+v^2,
\]
so \(\det X=a^2-Q(u,v)\). If \((u,v)=(0,0)\), then \(\kappa(X)=q-\epsilon\) for \(a=0\), and \(0\) otherwise. For nonzero \((u,v)\) with \(Q(u,v)\ne0\),
\[
\kappa(X)=1+\chi(-\det X).
\]
For nonzero isotropic \((u,v)\) (which occur only if \(\epsilon=1\)), \(\kappa(X)=1\) if \(a\ne0\), and \(0\) if \(a=0\).

## Proof
**Step 1: idempotents and Peirce images.** Every idempotent in \(J\) has rank \(0,1\), or \(2\), since its minimal polynomial divides the separable polynomial \(t(t-1)\). Rank \(0\) and \(2\) yield \(0\) and \(I_2\). The remaining idempotents have the unique form
\[
P=\frac12I_2+T,\qquad T=\begin{pmatrix}r&s\\s&-r\end{pmatrix},\qquad r^2+s^2=\frac14.
\]
For any such \(P\), the Peirce multiplication map \(L_P:Y\mapsto P\circ Y\) has eigenvalues \(1,1/2,0\), each with one-dimensional eigenspace: \(KP\), the off-diagonal Peirce space, and \(K(I_2-P)\). The trace pairing \(\operatorname{tr}(YZ)\) is nondegenerate on \(J\) (characteristic odd), and \(L_P\) is self-adjoint for it. Consequently
\[
P\circ J=\{X\in J:\operatorname{tr}(X(I_2-P))=0\}.
\]
With \(X=aI_2+U\), \(U=\bigl(\begin{smallmatrix}u&v\\v&-u\end{smallmatrix}\bigr)\), the condition is precisely \(ur+vs=a/2\). Thus \(\kappa(X)\) counts the intersection of the conic \(r^2+s^2=1/4\) with the affine line \(ur+vs=a/2\).

**Step 2: pointwise incidence.** When \((u,v)=(0,0)\), the line equation holds for all conic points exactly when \(a=0\). For \(Q=u^2+v^2\ne0\), the full set of line solutions is
\[
(r,s)=\frac{a}{2Q}(u,v)+t(-v,u),\quad t\in K.
\]
The conic condition becomes
\[
t^2=\frac{Q-a^2}{4Q^2}=\frac{-\det X}{4Q^2},
\]
so the number of solutions is \(1+\chi(-\det X)\). If \((u,v)\ne0\) and \(Q=0\), choose an isotropic vector \(w\) independent of \((u,v)\). The line equation fixes the coefficient of \(w\) at a scalar proportional to \(a\); the quadratic equation fixes the remaining coefficient uniquely when \(a\ne0\), and has no solution when \(a=0\). This proves the pointwise classification.

**Step 3: counting the conic and the incidence classes.** For nonzero \(t\in K\), elementary quadratic-character sums give
\[
\#\{(u,v)\in K^2:u^2+v^2=t\}=q-\epsilon,
\qquad
\#\{(a,b)\in K^2:a^2+b^2=t\}=q-\epsilon.
\]
Indeed \(\sum_{a\in K}\chi(t-a^2)=-\epsilon\). The zero level of \(Q\) contains only \((0,0)\) when \(\epsilon=-1\), and \(2q-1\) points when \(\epsilon=1\). In the nonzero levels, the number of scalars \(a\) with \(t-a^2=0\) is \(1+\chi(t)\); the number with \(t-a^2\) a nonzero square is
\[
\frac{q-\epsilon-1-\chi(t)}2.
\]
Summing over \(t\ne0\), using \(\sum_{t\ne0}\chi(t)=0\), gives, if \(\epsilon=-1\), \(q^2-1\) cases with incidence one and \(q(q^2-1)/2\) cases with incidence two. If \(\epsilon=1\), the nonzero quadratic levels contribute \((q-1)^2\) cases with incidence one and \((q-1)^2(q-2)/2\) with incidence two; the \(2(q-1)\) nonzero isotropic vectors each allow the \(q-1\) nonzero choices of \(a\), adding \(2(q-1)^2\) to incidence one. The zero matrix has incidence \(q-\epsilon\). Subtracting from \(|J|=q^3\) yields the displayed incidence-zero counts. This also proves \(|\mathcal P|=q-\epsilon\), by applying the nonzero-level count to \(1/4\).

**Step 4: obstruction for words.** A Jordan factor \(0\) makes the word zero. Factors \(I_2\) can be deleted without changing its value. If there remains a nontrivial idempotent, the final such factor is rank one, so the word belongs to its Peirce image and has positive incidence. If no such factor remains, the word is either zero or \(I_2\). Exactly \(q-1\) nonzero scalar matrices have incidence zero; removing those from the respective incidence-zero totals gives the asserted counts of nonscalar matrices excluded from representation.

## Verification
The standalone `verify.py` directly enumerates every symmetric matrix, every idempotent, and the Peirce images, and checks both the pointwise classification and the complete incidence distribution over prime fields of sizes \(3,5,7,11,13\) and the nonprime field \(\mathbb F_9\). For \(q=3,5,7,9\), it also exhaustively computes the finite word closure; those tests support but do **not** establish a general converse to the necessary Peirce-incidence condition. The general theorem follows from the proof above, not the finite tests.

## Relationship to prior work
The recent study by Gogić and Tomašević [1] initiated the systematic study of idempotent words in simple finite-dimensional Jordan algebras. Its public abstract expressly limits its symmetric-matrix representability results to quadratically closed fields. The present theorem instead determines a finite-field terminal-factor obstruction and its exact distribution in the first symmetric-matrix case, showing quantitatively how rational quadratic obstructions persist. Standard Peirce decomposition and finite-field quadratic-character counts are classical tools, not claimed as innovations. Existing results on associative idempotent factorizations concern different multiplication and do not imply this Jordan-incidence distribution merely from their stated conclusions.

## Limitations
The result is a one-sided word-representation obstruction: \(\kappa(X)>0\) is not proved sufficient for finite word representation. The verified small-field coincidence between the word set and \(\{I_2\}\cup\{\kappa>0\}\) is experimental only. The conclusions exclude characteristic two. A full-text originality comparison against [1] was not possible through available lawful retrieval routes; its public abstract and accessible reviews were examined, and a hidden finite-field lemma or unindexed equivalent result remains a bibliographic risk.

## References
1. I. Gogić and M. Tomašević, *Idempotent words in finite-dimensional simple Jordan algebras*, arXiv:2609.23581, first publicly submitted 2026-09-20. https://arxiv.org/abs/2609.23581
2. American Mathematical Society, *MSC2020*, classification 17C27 (Idempotents, Peirce decompositions). https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=17Cxx
