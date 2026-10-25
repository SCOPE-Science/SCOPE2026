# Asymptotic isomorphism enumeration and corank distribution of finite-field evolution algebras

## Finding
Fix a prime power \(q\geq2\). Let \(I_{n,q}^{(r)}\) be the number of \(\mathbb F_q\)-algebra isomorphism classes of \(n\)-dimensional evolution algebras with \(\dim(E/E^2)=r\), for integers \(0\leq r\leq n\). Define \(P_m(q)=\prod_{j=1}^{m}(1-q^{-j})\) (with \(P_0(q)=1\)), and \(\rho_q=1-q^{-1}\). Uniformly in all such \(r\), as \(n\to\infty\) with \(q\) fixed,
\[
\frac{I_{n,q}^{(r)} n!(q-1)^n}{q^{n^2}}
=q^{-r^2}\frac{\prod_{j=r+1}^{n}(1-q^{-j})^2}{P_{n-r}(q)}
+O_q\bigl(n^2\rho_q^n\bigr).
\tag{1}
\]
In particular, for every fixed \(r\geq0\), putting \(P_\infty(q)=\prod_{j\geq1}(1-q^{-j})>0\),
\[
I_{n,q}^{(r)}\sim \frac{q^{n^2}}{n!(q-1)^n}\,\frac{q^{-r^2}P_\infty(q)}{P_r(q)^2}.
\tag{2}
\]
Summing over all coranks gives the asymptotic count of **all** evolution algebras, not merely perfect ones:
\[
\sum_{r=0}^n I_{n,q}^{(r)}
=\frac{q^{n^2}}{n!(q-1)^n}\bigl(1+O_q(n^2\rho_q^n)\bigr).
\tag{3}
\]
Among these isomorphism classes the asymptotic fraction of nonperfect algebras is \(1-P_\infty(q)\), strictly between zero and one; the perfect fraction is \(P_\infty(q)\). Equations (1)–(3) are the single corank-resolved enumeration result.

## Assumptions and scope
An evolution algebra is a finite-dimensional commutative, generally nonassociative algebra with a **natural basis** \(e_1,\ldots,e_n\) such that \(e_i e_j=0\) whenever \(i\ne j\). Its structure matrix \(M=(m_{ij})\in\mathbb F_q^{n\times n}\) is defined by \(e_i^2=\sum_jm_{ij}e_j\). Thus \(\dim E^2=\operatorname{rank}(M)\), so its corank is the intrinsic integer \(r=n-\operatorname{rank}(M)\). An isomorphism is any invertible linear algebra homomorphism, **not** just a prescribed change of natural basis. The finite field \(\mathbb F_q\) can have arbitrary characteristic or extension degree; only \(q\) is held fixed in the asymptotics. Empty products are one. The \(O_q\) constant is independent of \(r\) and \(n\) (for all sufficiently large \(n\)). The statements are not uniform in growing \(q\), and the fixed-\(r\) equivalence in (2) is not claimed when \(r\) grows with \(n\).

## Proof
**1. Most matrices have a rigid natural-basis type.** Call a structure matrix *2LI* when all its rows are nonzero and every pair of distinct rows is linearly independent. If \(M\) is uniform on \(\mathbb F_q^{n\times n}\), then a row is zero with probability \(q^{-n}\), while two fixed nonzero rows are proportional with probability at most \((q-1)q^{-n}\). A union bound gives
\[
\frac{|\mathrm{Bad}_{n,q}|}{q^{n^2}}
\leq \bigl[n+\tbinom n2(q-1)\bigr]q^{-n}.
\tag{4}
\]
For any natural-basis element \(u\), the multiplication map \(L_u:v\mapsto uv\) has rank at most one, since the other natural-basis elements annihilate \(u\). If \(u=\sum_i a_i e_i\), then \(\operatorname{im}L_u=\operatorname{span}\{e_i^2:a_i\ne0\}\). For a 2LI matrix, rank at most one forces the support of \(u\) in the original basis to be a singleton. Therefore **every** natural basis is a scaled permutation of the given one. This elementary proof is the known 2LI natural-basis rigidity criterion [2, 3], used here, not claimed as new.

**2. The monomial matrix action.** The group \(G_n=(\mathbb F_q^\times)^n\rtimes S_n\) has order \(H_n=(q-1)^n n!\). A change of natural basis \(f_i=d_i e_{\sigma(i)}\) sends \(M\) to the matrix
\[
M'_{ij}=d_i^2d_j^{-1}M_{\sigma(i),\sigma(j)}.
\tag{5}
\]
This defines a group action on all structure matrices, preserving matrix rank. Every isomorphism between two 2LI evolution algebras lies in this action, by Step 1. For arbitrary matrices, a monomial orbit is only a subset of an algebra-isomorphism class.

**3. A uniform Burnside estimate.** Write
\[
R_{n,q}=q^{-n^2}\sum_{g\in G_n\setminus\{1\}}|\operatorname{Fix}(g)|.
\tag{6}
\]
For a permutation \(\sigma\ne1\) moving exactly \(s\geq2\) indices, its simultaneous action on ordered pairs \((i,j)\) has at most \(\frac12(n^2+(n-s)^2)\) orbits: exactly \((n-s)^2\) ordered pairs are fixed, and all other orbits have size at least two. In the fixed-point equations from (5), each orbit determines at most one free field element, irrespective of the scaling factors. Hence
\[
\frac{|\operatorname{Fix}(\sigma,d)|}{q^{n^2}}
\leq q^{-sn+s^2/2}\leq q^{-sn/2}.
\tag{7}
\]
There are at most \(n^s\) permutations of support \(s\) and \((q-1)^n\) scalings. For \(t_n=nq^{-n/2}<1\), their total contribution to (6) is at most
\[
(q-1)^n\sum_{s=2}^n(nq^{-n/2})^s
\leq (q-1)^n\frac{t_n^2}{1-t_n}
=O_q\bigl(n^2\rho_q^n\bigr).
\tag{8}
\]
For \(\sigma=1\), write \(d=(d_i)\). A coefficient \(M_{ij}\) can be nonzero in a fixed matrix only if \(d_j=d_i^2\). If \(m\) is the maximum multiplicity among the \(d_i\), there are at most \(nm\) such ordered pairs; hence the fixed fraction is at most \(q^{-n(n-m)}\). For a nonconstant \(d\), set \(s=n-m\geq1\), choose one modal scalar, its \(n-s\) positions, and the other \(s\) entries. The sum over all nonconstant scalings is bounded by
\[
(q-1)\sum_{s=1}^n\binom ns(q-2)^s q^{-ns}
=(q-1)\left[(1+(q-2)q^{-n})^n-1\right].
\tag{9}
\]
Each of the \(q-2\) constant scalings other than the identity fixes only the zero matrix, contributing \((q-2)q^{-n^2}\). Thus the entire diagonal contribution is \(O_q(nq^{-n})\), and combining with (8) gives
\[
R_{n,q}=O_q\bigl(n^2\rho_q^n\bigr).
\tag{10}
\]
This is a **sum of fixed-point fractions**, stronger than an estimate for the probability of having some nontrivial stabilizer.

**4. Squeezing true algebra-isomorphism classes.** Let \(S_{n,q}^{(r)}\) be the rank-\(n-r\) matrices and let \(I_{n,q}^{(r)}\) count their algebra-isomorphism classes. On its 2LI subset, algebra isomorphism coincides with monomial equivalence, so there are at least \((|S_{n,q}^{(r)}|-|\mathrm{Bad}_{n,q}|)/H_n\) distinct algebra-isomorphism classes. Conversely, every algebra-isomorphism class is a union of monomial orbits. Burnside's lemma bounds their number by
\[
I_{n,q}^{(r)}\leq |S_{n,q}^{(r)}/G_n|
\leq \frac{|S_{n,q}^{(r)}|+q^{n^2}R_{n,q}}{H_n}.
\tag{11}
\]
Consequently, uniformly in \(r\),
\[
\frac{H_n I_{n,q}^{(r)}}{q^{n^2}}
=\frac{|S_{n,q}^{(r)}|}{q^{n^2}}
+O_q(n^2\rho_q^n).
\tag{12}
\]
This argument does **not** assume all matrices have unique natural bases; exceptional matrices are controlled by both sides of the squeeze.

**5. Exact matrix corank probability.** The number of \(n\times n\) matrices of rank \(k\), for \(0\leq k\leq n\), is
\[
\frac{\prod_{i=0}^{k-1}(q^n-q^i)^2}{\prod_{i=0}^{k-1}(q^k-q^i)},
\tag{13}
\]
by factoring a rank-\(k\) linear transformation into a full-rank \(n\times k\) and a full-rank \(k\times n\) map, modulo the \(\operatorname{GL}_k(\mathbb F_q)\) ambiguity. With \(k=n-r\), dividing (13) by \(q^{n^2}\) gives exactly the first term on the right side of (1). This proves the uniform corank estimate. For fixed \(r\), \(P_{n-r}(q)\to P_\infty(q)\) and \(\prod_{j=r+1}^n(1-q^{-j})\to P_\infty(q)/P_r(q)\); their limits are nonzero. Therefore (2) follows. Summing over all coranks in Burnside's squeeze (or repeating Step 4 with all matrices) gives (3) without multiplying the error by \(n\). The fraction of perfect matrices is \(P_n(q)\to P_\infty(q)\), and the same squeeze separately for invertible and singular matrices yields the claimed isomorphism-class proportions. \(\square\)

## Verification
The standalone script `verify_small.py` independently enumerates all structure matrices, invertible linear basis changes, and monomial basis changes for \((n,q)=(2,2),(2,3)\), with an extended run for \((3,2)\). It computes **true** isomorphism classes through all permissible invertible natural-basis changes, not just monomial orbits. Recorded checks: for \((2,2)\), 16 matrices, 6 satisfying 2LI, 10 monomial orbits, 9 genuine isomorphism classes, and 4 2LI orbits; for \((2,3)\), 81 matrices, 48 satisfying 2LI, 15 monomial orbits, 13 genuine classes, and 7 2LI orbits. The extended \((3,2)\) run yielded 512 matrices, 210 satisfying 2LI, 104 monomial orbits, 85 genuine classes, and 43 2LI orbits. The script asserts the sandwich in Step 4 and returned `VERIFY_OK`. These finite computations check the interpretation of the action and its exceptional matrices; they cannot prove the asymptotic bound. The proof in Steps 1–5 is uniform over all finite fields.

To reproduce: run `python verify_small.py` with Python 3; add `--extended` for the longer three-dimensional binary test. No external packages are required.

## Relationship to prior work
The 2026 survey of Kaygorodov, Martín González and Viruel [1], first publicly posted on 2026-10-15, asks in **Question 21** for the asymptotic number of **all**, including nonperfect, finite-field evolution algebras. Equations (1)–(3) give that asymptotic and refine it by square-space corank. Wei and Zou [4] already prove a Burnside formula for **perfect** algebras (corank zero), so that known subgroup action and its exact perfect counting are not new. The 2LI natural-basis criterion is due to [2] and also appears in [3]; here it allows comparison between monomial and unrestricted isomorphisms on a density-one subset. The new counting step is the uniform fixed-point Burnside estimate **across every corank**, coupled with a two-sided orbit squeeze for the exceptional nonperfect matrices. In particular, (2) for fixed positive corank and the nonperfect proportion are not immediate restatements of the perfect-algebra enumeration.

## Limitations
The proof counts unlabelled algebra isomorphism types only in the fixed-field, large-dimension regime. It does not give exact finite-dimensional isomorphism counts, uniform relative errors for corank growing with dimension, or a result uniform when \(q\) grows. The uniform error in (1) is **absolute** after normalization, so the term may dominate the principal term for large corank. Source comparisons are bounded to the cited literature and accessible mathematical record; an equivalent treatment in unindexed work is not logically excluded. The result is presently subject to further independent mathematical audit, and small-case tests do not certify an infinite-family theorem.

## References
1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems* (2026), arXiv:2610.22248v1, Question 21 and Section 1.3.4. https://arxiv.org/abs/2610.22248
2. N. Boudi, Y. Cabrera Casado, M. Siles Molina, *Natural families in evolution algebras*, Publ. Mat. 66 (2022), 159–181; arXiv:2006.14460, Corollary 2.7. https://arxiv.org/abs/2006.14460
3. Y. Cabrera Casado et al., *Solenoids in automorphism groups of evolution algebras* (2025), arXiv:2505.14584, Theorem 5.3. https://arxiv.org/abs/2505.14584
4. Y. Wei, Y. M. Zou, *Isomorphism classes of idempotent evolution algebras*, Linear Algebra Appl. 675 (2023), 142–178; arXiv:2310.12368, Theorem 2.1. https://arxiv.org/abs/2310.12368
