# Sharp exponential obstruction width for disjunctions of constancy atoms

## Finding

For every integer \(m\geq1\), let \(x_1,\ldots,x_m\) be distinct variables and let
\[
\Phi_m=\operatorname{dep}(x_1)\vee\cdots\vee\operatorname{dep}(x_m)
\]
be their iterated **team-splitting** disjunction of constancy atoms. An assignment team \(T\) fails \(\Phi_m\) precisely when it cannot be covered by one constant-value coordinate slice in each of the \(m\) directions.

**Theorem (sharp obstruction width).** On every nonempty universe, finite or infinite, every team \(T\) failing \(\Phi_m\) contains a failing subteam of cardinality at most \(2^m\). The bound is best possible simultaneously for every \(m\): on the two-element universe the entire Boolean cube is a failing team of size \(2^m\), whereas all of its proper subteams satisfy \(\Phi_m\). Equivalently, the largest possible size of a finite inclusion-minimal failing team is exactly \(2^m\).

Thus satisfaction of \(\Phi_m\) on an arbitrary team is determined by its subteams of size *at most* \(2^m\), independent of the universe's cardinality. The exact widths begin \(2,4,8,16,\ldots\). The case \(m=2\), of width \(4\), was already established in the primary literature; the all-\(m\), all-universe sharp classification is the contribution assessed here.

## Assumptions and scope

Use standard lax dependence-logic team semantics: a constancy atom \(\operatorname{dep}(x)\) holds when all assignments in a team give \(x\) the same value; disjunction holds when the team is the union of satisfying subteams. The nonempty universe \(A\) is arbitrary and may be infinite. A team is a set of assignments from a variable domain containing the displayed distinct variables to \(A\); unrelated extra variables are allowed. The empty team satisfies the formula. There are no restrictions on additional relations of the structure.

For \(\mathbf a=(a_1,\ldots,a_m)\in A^m\), set
\[
C(\mathbf a)=\{s:\text{for some }i\in\{1,\ldots,m\},\ s(x_i)=a_i\}.
\]
By the splitting semantics and downward closure, \(T\models\Phi_m\) if and only if there is \(\mathbf a\in A^m\) with \(T\subseteq C(\mathbf a)\). Indeed the selected constancy slices cover \(T\); conversely the values of the satisfying split pieces provide such a tuple, with arbitrary filler values for empty pieces.

"Obstruction width" here means the *maximum cardinality of an inclusion-minimal failing team*, equivalently the smallest \(b\) such that all failures have a failing subteam of size at most \(b\). It is the unambiguous **at-most-\(b\)** local-testing invariant. For a definition using literally only subteams of cardinality exactly \(b\), teams smaller than \(b\) must be treated separately; no literal exact-cardinality equivalence is asserted for those teams.

## Proof

**1. Every failure has a finite witness.** Proceed by induction on \(m\). For \(m=1\), failure means two assignments with different \(x_1\)-values, giving a two-assignment witness. Suppose \(m\geq2\) and the assertion holds for \(m-1\). Fix \(s_0\in T\) when \(T\not\models\Phi_m\). For each \(i\), define
\[
T_i=\{s\in T:s(x_i)\ne s_0(x_i)\}.
\]
If \(T_i\) could be covered by constant-value slices in the other \(m-1\) coordinates, then those slices together with \(s(x_i)=s_0(x_i)\) would cover all of \(T\), a contradiction. Thus every \(T_i\), viewed on the other coordinates, fails the corresponding \(m-1\) formula. Inductively choose a finite failing subset \(U_i\subseteq T_i\). Then
\[
U=\{s_0\}\cup\bigcup_{i=1}^mU_i
\]
is a finite failing subset: any proposed \(m\)-slice cover of \(U\) must cover \(s_0\) by at least one coordinate \(i\), so it chooses that coordinate's value \(s_0(x_i)\); this coordinate covers none of \(U_i\), and the remaining slices cannot cover \(U_i\). This completes finite reduction even when \(T\) and \(A\) are infinite.

**2. A polynomial interpolation bound for inclusion-minimal failures.** Inside a finite failing team choose a subset \(U=\{s_1,\ldots,s_n\}\) minimal under inclusion. For each \(r\), the subteam \(U\setminus\{s_r\}\) is coverable. Choose a tuple \(\mathbf a^{(r)}\in A^m\) whose coordinate slices cover it. Since \(U\) fails, \(s_r\) is not covered by this tuple, which means
\[
a_i^{(r)}\ne s_r(x_i)\qquad(1\leq i\leq m).
\]
Only finitely many elements of \(A\) appear in these assignments and tuples. Assign them distinct rational labels by an injection \(\lambda\) into \(\mathbb Q\). Form the \(n\)-by-\(n\) matrix
\[
H_{sr}=\prod_{i=1}^m\bigl(\lambda(a_i^{(r)})-\lambda(s_s(x_i))\bigr).
\]
If \(s\ne r\), the coverage of \(s_s\) by the witness tuple \(\mathbf a^{(r)}\) gives at least one zero factor, hence \(H_{sr}=0\). If \(s=r\), all factors are nonzero by the displayed inequality. Thus \(H\) is diagonal with nonzero diagonal and has rank \(n\) over \(\mathbb Q\).

On the other hand, each column of \(H\) is the evaluation, on \(s_1,\ldots,s_n\), of a polynomial of degree at most one in each of the \(m\) formal variables \(z_1,\ldots,z_m\):
\[
P_r(\mathbf z)=\prod_{i=1}^m\bigl(\lambda(a_i^{(r)})-z_i\bigr).
\]
All these polynomials lie in the \(2^m\)-dimensional span of square-free monomials \(\prod_{i\in J}z_i\), \(J\subseteq\{1,\ldots,m\}\). Therefore \(\operatorname{rank}H\leq2^m\), forcing \(n\leq2^m\). Together with Step 1, every arbitrary failing team has a failing subteam of size at most \(2^m\).

**3. Sharpness.** Let \(A=\{0,1\}\) and take as team the full cube \(Q_m=A^m\), with one assignment for every coordinate vector. Any choice of constants \(a_i\in A\) leaves the unique complement vector \((1-a_1,\ldots,1-a_m)\) uncovered. Hence \(Q_m\not\models\Phi_m\). Conversely, given any deleted vector \(t\), choose \(a_i=1-t_i\). Every vector \(s\ne t\) differs from \(t\) in at least one coordinate \(i\) and therefore satisfies \(s(x_i)=a_i\); these slices cover \(Q_m\setminus\{t\}\). Every proper subteam is contained in one such deleted-point team and therefore satisfies \(\Phi_m\) by downward closure. So the bound \(2^m\) cannot be lowered.

## Verification

The standalone standard-library program `checker.py` directly tests covers by coordinate slices. It enumerates every subteam over binary alphabets for \(m=1,2,3,4\), every subteam over the ternary alphabet for \(m=1,2\), verifies each inclusion-minimal bad team's size against the proved bound, and checks all complement-cube diagonal interpolation witnesses through \(m=6\). Running `python checker.py` returns `ALL_CHECKS_OK`.

The exact finite outcomes include ternary \(m=2\) minimal failing subteams of sizes \(3\) and \(4\); this is why the theorem deliberately states an at-most-cardinality obstruction invariant rather than a literal exact-cardinality assertion for small teams. Finite checks are not the proof for unbounded universes; that follows from the induction and rank argument.

## Relationship to prior work

Fröhlich, Kolaitis, and Meier prove the \(m=2\) constancy-disjunction coherence level \(4\) in Corollary 23 of *Disjunctions of Two Dependence Atoms* (arXiv:2508.16146; CSL 2026). Their Section 4 and its appendix treat disjunctions of two dependence or constancy atoms, not an arbitrary number of distinct constancy atoms. The special case \(m=2\) is **not** claimed as new here.

Barlag et al., *Aspects of Coherence in Dependence Logic* (arXiv:2605.31269), establish a general relation between first-order rewritability and existence of some finite coherence bound. Their Theorems 27–28 explicitly use formulas containing disjunctions of several constancy atoms to establish undecidability; their argument shows some bounds are insufficient but does not give a uniform sharp \(2^m\) bound for this class over arbitrary universes. Their propositional-logic section observes a trivial \(2^m\) size limit for binary teams on \(m\) variables, but that does not bound minimal failing teams over unbounded alphabets. The present proof supplies the non-Boolean, cardinality-independent uniform bound and proves it optimal.

The interpolation method is a standard multilinear algebra idea; no claim of inventing that general technique is made. Searches for an existing equivalent axis-parallel covering or product-Helly theorem did not settle historical priority; see the review for residual risk.

## Limitations

The sharp formula concerns disjunctions of **distinct unary constancy atoms** only. It does not assert corresponding finite coherence levels for disjunctions of arbitrary functional dependence atoms, many of which are known to be incoherent. The proof assumes a nonempty universe, although the empty-universe case is vacuous. The size \(2^m\) is a worst-case local-test size, not a minimum size for every failing team, nor a computational lower bound for model checking. The result has undergone the documented self-review only; no independent audit or priority certification has been performed.

## References

1. N. Fröhlich, P. G. Kolaitis, and A. Meier, *Disjunctions of Two Dependence Atoms*, first posted 2025-08-22, arXiv:2508.16146, https://arxiv.org/abs/2508.16146; complete CSL 2026 article, https://drops.dagstuhl.de/storage/00lipics/lipics-vol363-csl2026/html/LIPIcs.CSL.2026.10/LIPIcs.CSL.2026.10.html (especially Section 4, Corollary 23 and the appendix).
2. T. Barlag, N. Fröhlich, M. Hannula, P. G. Kolaitis, J. Kontinen, A. Meier, and J. Väänänen, *Aspects of Coherence in Dependence Logic*, first posted 2026-05-29, arXiv:2605.31269, https://arxiv.org/html/2605.31269v1 (especially Sections 3 and 5, Theorems 27–28).
3. J. Väänänen, *Dependence Logic: A New Approach to Independence Friendly Logic*, Cambridge University Press, 2007 (background on constancy atoms and team-splitting semantics; no general sharp-width claim attributed).
