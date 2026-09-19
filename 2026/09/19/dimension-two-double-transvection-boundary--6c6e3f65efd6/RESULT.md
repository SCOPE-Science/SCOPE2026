# Dimension-two boundary for double transvection commutators

For a field \(F\), write
\[
[g,h]=ghg^{-1}h^{-1}.
\]
A **transvection** in \(GL_2(F)\) is a nonidentity matrix \(I+N\) with \(N^2=0\) and \(\operatorname{rank}N=1\).

Chinyere's arXiv:2609.17006v2 proves that for every nonzero commutative ring \(R\), every \(n\ge 3\), and every \(\sigma\in GL_n(R)\), there are nonidentity transvections \(\tau_1,\tau_2\) such that
\[
[[\sigma,\tau_1],\tau_2]=I_n.
\]
The paper explicitly notes that its functional-annihilator construction breaks down for \(n=2\), without asserting that the conclusion itself fails there.

The dimension-two situation over fields admits an exact classification, and over \(\mathbb R\) it separates the stronger identity conclusion from the original unipotence question.

## Theorem 1: exact identity over an arbitrary field

Let \(F\) be a field, let \(\sigma\in GL_2(F)\), and put \(\Delta=\det\sigma\). There exist nonidentity transvections \(\tau_1,\tau_2\in GL_2(F)\) such that
\[
[[\sigma,\tau_1],\tau_2]=I_2
\]
if and only if the following condition holds:

- if \(\operatorname{char}F=2\), then \(\sigma\) has an eigenline over \(F\);
- if \(\operatorname{char}F\ne2\), then either \(\sigma\) has an eigenline over \(F\), or \(-\Delta\) is a square in \(F\).

Thus the universal identity theorem for \(n\ge3\) has a genuine dimension-two obstruction even over fields.

### Proof

Fix a nonidentity transvection \(\tau_1\). Its image and kernel for \(\tau_1-I\) are the same line \(L\). Choose a basis whose first vector spans \(L\). In that basis,
\[
\tau_1=\begin{pmatrix}1&t\\0&1\end{pmatrix},\qquad t\in F^\times,
\]
and write
\[
\sigma=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad \Delta=ad-bc\ne0.
\]
Set \(A=[\sigma,\tau_1]\). Direct multiplication gives \(\det A=1\) and
\[
\boxed{\operatorname{tr}A=2+\frac{t^2c^2}{\Delta}.}
\tag{1}
\]

We first record the relevant centralizer fact. For \(A\in SL_2(F)\), there is a nonidentity transvection commuting with \(A\) if and only if \(A\) has a repeated eigenvalue in \(F\). Indeed, after adapting a basis to such a transvection, every commuting matrix has the form
\[
\begin{pmatrix}r&s\\0&r\end{pmatrix}.
\]
Since \(\det A=1\), one has \(r^2=1\). Conversely, if the characteristic polynomial of \(A\) is \((X-r)^2\), then either \(A=rI\), in which case every transvection commutes with \(A\), or \(A-rI\) is a nonzero square-zero rank-one matrix and \(I+(A-rI)\) is a commuting transvection.

Consequently, when \(\operatorname{char}F\ne2\), a commuting nonidentity transvection exists exactly when
\[
\operatorname{tr}A=2\quad\text{or}\quad\operatorname{tr}A=-2.
\]
By (1), the first alternative is equivalent to \(c=0\), which says precisely that \(L\) is \(\sigma\)-invariant. The second alternative is equivalent to
\[
\frac{t^2c^2}{\Delta}=-4,
\]
or
\[
\boxed{-\Delta=\left(\frac{tc}{2}\right)^2.}
\]
This proves necessity in odd characteristic.

For sufficiency, if \(\sigma\) has an eigenline, choose \(L\) to be that line; then \(c=0\), so \(A\) has trace \(2\) and commutes with a nonidentity transvection. If \(\sigma\) has no eigenline but \(-\Delta=s^2\), choose any line \(L\). It is not \(\sigma\)-invariant, hence \(c\ne0\); taking \(t=2s/c\) makes \(\operatorname{tr}A=-2\), so again a nonidentity commuting transvection exists.

In characteristic \(2\), the repeated eigenvalue of an element of \(SL_2(F)\) must be \(1\), and the repeated-root condition is \(\operatorname{tr}A=0\). Formula (1) becomes
\[
\operatorname{tr}A=\frac{t^2c^2}{\Delta},
\]
which vanishes exactly when \(c=0\). Hence the identity double commutator exists exactly when \(\sigma\) has an eigenline over \(F\). ∎

## Theorem 2: the real dimension-two unipotence problem

For every \(\sigma\in GL_2(\mathbb R)\), there exist nonidentity transvections \(\tau_1,\tau_2\) such that
\[
\left([[\sigma,\tau_1],\tau_2]-I_2\right)^2=0.
\]
More precisely:

1. the double commutator can be chosen equal to \(I_2\) if and only if \(\sigma\) has a real eigenline, equivalently
   \[
   (\operatorname{tr}\sigma)^2-4\det\sigma\ge0;
   \]
2. if \(\sigma\) is nonscalar, the double commutator can be chosen to be a **nonidentity transvection**;
3. if \(\sigma\) is scalar, every first commutator \([\sigma,\tau_1]\) is \(I_2\), so every resulting double commutator is \(I_2\).

### Proof

The exact-identity statement follows from Theorem 1. Over \(\mathbb R\), if \(-\det\sigma\) is a square then \(\det\sigma<0\), which already forces two real eigenvalues. Hence the two alternatives in Theorem 1 collapse to the existence of a real eigenline.

Now suppose \(\sigma\) is nonscalar. Then not every real line is \(\sigma\)-invariant, so choose a noninvariant line \(L\) and adapt the basis as above. Thus \(c\ne0\). For
\[
A=[\sigma,\tau_1],
\]
formula (1) gives
\[
\operatorname{tr}A=2+\frac{t^2c^2}{\Delta}.
\]
If \(\Delta>0\), every \(t\ne0\) gives \(\operatorname{tr}A>2\). If \(\Delta<0\), choose \(|t|\) sufficiently large so that \(\operatorname{tr}A<-2\). Thus in either case \(A\in SL_2(\mathbb R)\) is hyperbolic with distinct real eigenvalues \(\lambda,\lambda^{-1}\), where \(\lambda^2\ne1\).

In an eigenbasis for \(A\), take
\[
\tau_2=I+sE_{12},\qquad s\ne0.
\]
Then
\[
[A,\tau_2]
=I+s(\lambda^2-1)E_{12},
\]
which is a nonidentity transvection. Hence its difference from the identity has square zero. The scalar case is immediate. ∎

## A sharp real counterexample to the identity conclusion

Let
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Then \(\det J=1\), \(J\) has no real eigenline, and \(-1\) is not a square in \(\mathbb R\). Theorem 1 therefore gives
\[
[[J,\tau_1],\tau_2]\ne I_2
\]
for every pair of nonidentity real transvections. Nevertheless Theorem 2 gives a pair for which the double commutator is itself a nonidentity transvection. Thus dimension two is a true boundary for the stronger identity statement, but not for the original real unipotence statement.

For example, with
\[
\tau_1=I+E_{12},
\]
one obtains
\[
[J,\tau_1]=\begin{pmatrix}1&-1\\-1&2\end{pmatrix},
\]
which has trace \(3\), determinant \(1\), and two distinct real eigenlines; choosing \(\tau_2\) along either eigenline yields a nonidentity transvection as the second commutator.

## Computational check over finite prime fields

A standalone exhaustive verifier enumerates every element of \(GL_2(\mathbb F_p)\), every nonidentity transvection, and compares direct existence of
\[
[[\sigma,\tau_1],\tau_2]=I_2
\]
with Theorem 1. It reports zero mismatches for \(p=2,3,5,7\):

```text
F_2: |GL2|=6, transvections=3, mismatches=0
F_3: |GL2|=48, transvections=8, mismatches=0
F_5: |GL2|=480, transvections=24, mismatches=0
F_7: |GL2|=2016, transvections=48, mismatches=0
```

The verification supports the formula but is not used in the proof.

## Relation to prior literature

Chinyere's current v2 theorem gives the exact identity double commutator for all \(n\ge3\) over every nonzero commutative ring with identity, and Remark 2.8 explicitly records only a failure of the proof mechanism at \(n=2\). The dimension-two classification above supplies the missing sharp boundary over fields and shows that, over \(\mathbb R\), the original unipotence conclusion still holds in dimension two.

Petechuk--Petechuk study commutators with transvections over division rings using residual and fixed submodules, including dimension \(n\ge2\), under additional commutativity or unipotence hypotheses. Their published statements do not give the existence criterion above for two independently chosen transvections.

Dela Rosa--Santos study products of commutators of index-two unipotent matrices and discuss the \(2\times2\) case, a related but different factorization problem.

## Limitations and originality qualification

Originality is asserted only to the best of our knowledge. The most important unresolved literature risk is the work cited by Chinyere as K. Muliarchyk, *A Counterexample to Kourovka Notebook Problem 10.46: Unipotent Commutators over Noncommutative Algebras*. Chinyere states that its Proposition 5.1 handles the field case by a rank-one argument, but the cited work itself was not independently located or inspected and the inspected bibliography supplies no publication identifier. If Proposition 5.1 includes a dimension-two classification, part or all of Theorem 1 could be prior art.

Targeted searches for dimension-two formulations involving \(GL_2\), transvections, nested commutators, eigenlines, and determinant-square obstructions did not locate the criterion above. The current arXiv v2 source and the relevant published Petechuk--Petechuk material were inspected. The real extension is restricted to \(\mathbb R\); no claim is made here that the unipotence conclusion holds over every field in dimension two.

## References

1. I. Chinyere, *Unipotence of a double commutator with transvections*, arXiv:2609.17006v2 (2026). https://arxiv.org/abs/2609.17006v2
2. V. M. Petechuk and Yu. V. Petechuk, *Properties of the commutators of some elements of linear groups over division rings*, Matematychni Studii 54 (2020), 15--22. DOI: 10.30970/ms.54.1.15-22.
3. K. L. Dela Rosa and J. P. C. Santos, *On commutators of unipotent matrices of index 2*, Linear Algebra and its Applications (2025), 385--404. DOI: 10.1016/j.laa.2025.02.003.
