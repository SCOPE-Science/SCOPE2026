# Generic automorphism rigidity and asymptotic orbit counts for perfect evolution algebras over fixed finite fields

## Finding
Fix a prime power \(q\ge3\). For every integer \(n\ge2\), choose \(A\) uniformly in \(\operatorname{GL}_n(\mathbb F_q)\), and define the perfect evolution algebra \(E(A)\) by a natural basis \(e_1,\ldots,e_n\) and products
\[
e_i e_j=0\quad(i\ne j),\qquad e_j^2=\sum_{i=1}^{n}a_{ij}e_i.
\]
Write \(S(A)=|\operatorname{Aut}_{\mathbb F_q}(E(A))|\), let \(N_{n,q}\) be the number of isomorphism classes of such algebras, and define the positive Euler product and explicit error bound
\[
\gamma_q=\prod_{j=1}^{\infty}(1-q^{-j}),\qquad
\eta_{n,q}=\frac{1}{\gamma_q}\left[\frac{(q-1)^n-1}{q^n}+(q-1)^n\sum_{k=2}^{n}n^k q^{-k(2n-k)/2}\right].
\]
Then, for every \(n\ge2\),
\[
0\le\mathbb E[S(A)-1]\le\eta_{n,q},\qquad
\Pr(S(A)>1)\le\eta_{n,q}.
\]
Moreover,
\[
N_{n,q}=\frac{|\operatorname{GL}_n(\mathbb F_q)|}{n!(q-1)^n}(1+\delta_{n,q}),
\qquad 0\le\delta_{n,q}\le\eta_{n,q}.
\]
Among isomorphism classes sampled uniformly (rather than matrices), the fraction with nontrivial automorphism group is at most \(2\eta_{n,q}\). For each **fixed** prime power \(q\ge3\),
\[
\eta_{n,q}=O_q\!\left((1-q^{-1})^n+n^2q^{-n/2}\right)\longrightarrow0
\quad(n\to\infty).
\]
Thus almost every labeled perfect evolution algebra and almost every isomorphism class is automorphism-rigid in the fixed-field, growing-dimension limit. The displayed asymptotic gives the leading number of high-dimensional isomorphism classes with a quantitative relative error.

## Assumptions and scope
All automorphisms are \(\mathbb F_q\)-linear algebra automorphisms. The sampling is uniform on the invertible **structure matrices** in a fixed natural basis. This is not initially a uniform distribution on isomorphism classes, although the theorem obtains a separate conclusion for that distribution. The coefficient field is fixed when taking \(n\to\infty\). The theorem is stated for \(q\ge3\); it does not claim the earlier, sharper binary-field asymptotic as new. The complete classification of all evolution algebras, including those with singular structure matrices, is not asserted.

## Proof
**1. Every automorphism is monomial.** If a linear algebra automorphism has matrix \(P=(p_{ij})\), then for distinct \(i,j\) the relation \(e_ie_j=0\) gives \(\sum_h p_{hi}p_{hj}e_h^2=0\). Since \(A\) is invertible, the vectors \(e_h^2\) are linearly independent. Hence each row of \(P\) has at most one nonzero entry. Invertibility of \(P\) forces exactly one nonzero entry in each row and column. Consequently every automorphism uniquely has the form \(e_j\mapsto t_j e_{\sigma(j)}\), for \(\sigma\in S_n\) and \(t_j\in\mathbb F_q^\times\). There are \(n!(q-1)^n\) possible monomial maps. Comparing the coefficient of \(e_{\sigma(i)}\) in the images of \(e_j^2\) gives the necessary and sufficient equation
\[
t_i a_{ij}=t_j^2 a_{\sigma(i),\sigma(j)}
\quad (1\le i,j\le n). \tag{1}
\]

**2. The diagonal case forces many zero entries.** Suppose \(\sigma\) is the identity but \(t\ne(1,\ldots,1)\). Choose \(i\) with \(t_i\ne1\). For every column \(j\), if \(t_j\ne1\) then equation (1) at \((j,j)\) forces \(a_{jj}=0\); otherwise equation (1) at \((i,j)\) forces \(a_{ij}=0\). These are \(n\) distinct matrix entries. Thus at most \(q^{n^2-n}\) matrices (invertible or not) satisfy the equation for each nonidentity diagonal map.

**3. A moved permutation loses at least half its moved matrix coordinates.** Suppose \(\sigma\) moves exactly \(k\) indices, with \(2\le k\le n\). The map \((i,j)\mapsto(\sigma(i),\sigma(j))\) fixes exactly \((n-k)^2\) ordered pairs. Its other \(k(2n-k)\) pairs lie in orbits of length at least two. Along each such orbit, equation (1) relates all entries by nonzero multipliers and allows at most one freely chosen field value (some cycles may force zero). Hence the solution space in all \(n\)-by-\(n\) matrices has cardinality at most
\[
q^{\,n^2-k(2n-k)/2}.
\]
There are at most \(n^k\) permutations moving exactly \(k\) indices and exactly \((q-1)^n\) scalar tuples for each permutation.

**4. Condition on invertibility and sum stabilizers.** The proportion of invertible matrices among all matrices is
\[
\frac{|\operatorname{GL}_n(\mathbb F_q)|}{q^{n^2}}
=\prod_{j=1}^{n}(1-q^{-j})\ge\gamma_q>0.
\]
Consequently the probability that a particular nontrivial monomial map fixes uniform \(A\in\operatorname{GL}_n(\mathbb F_q)\) is bounded by \(\gamma_q^{-1}q^{-n}\) in the diagonal case and by \(\gamma_q^{-1}q^{-k(2n-k)/2}\) in the support-\(k\) permutation case. Summing over all nonidentity monomial maps gives the claimed \(\eta_{n,q}\) bound for \(\mathbb E[S(A)-1]\). Since \(S(A)\) is a positive integer, \(\Pr(S(A)>1)\le\mathbb E[S(A)-1]\).

**5. Count isomorphism classes.** The monomial group acts on the invertible structure matrices, with orbits corresponding to algebra isomorphism classes and stabilizers to automorphism groups. Burnside's lemma gives
\[
N_{n,q}=\frac{1}{n!(q-1)^n}\sum_{A\in\operatorname{GL}_n(\mathbb F_q)}S(A).
\]
Therefore \(\delta_{n,q}=\mathbb E[S(A)-1]\). If \(B\) is the set of matrices with \(S(A)>1\), the fraction of *isomorphism classes* represented by \(B\) equals
\[
\frac{\mathbb E[S(A)\mathbf1_B]}{\mathbb E[S(A)]}
\le\frac{2\mathbb E[S(A)-1]}{\mathbb E[S(A)]}\le 2\eta_{n,q},
\]
because for every integer \(s\ge2\), \(s\le2(s-1)\).

**6. The error vanishes.** For \(2\le k\le n/2\), \(k(2n-k)/2\ge3kn/4\). Set \(z_n=nq^{-3n/4}\). For sufficiently large \(n\), \(z_n\le1/2\), and the corresponding part of the permutation sum is at most \(q^nz_n^2/(1-z_n)\le2n^2q^{-n/2}\). For \(n/2<k\le n\), \(k(2n-k)/2\ge3n^2/8\), so the remaining part is bounded by \(n^{n+1}q^{n-3n^2/8}\), which is superexponentially small for fixed \(q\). The diagonal term equals \(((q-1)^n-1)q^{-n}\le(1-q^{-1})^n\). These estimates prove the displayed \(O_q\) bound, the limit, and all stated asymptotics.

## Verification
The file `verify_generic.py` independently enumerates all matrices over small prime fields, tests invertibility by Gaussian elimination, checks each monomial candidate against the defining multiplication, and separately verifies the coordinate fixed-point equations. It computes full stabilizer histograms and the Burnside orbit counts, verifying \(N_{2,2}=4\), \(N_{3,2}=33\), \(N_{2,3}=7\), \(N_{3,3}=249\), \(N_{2,5}=17\), and \(N_{4,2}=908\). The last value agrees with the published four-dimensional binary count; the binary examples are checks rather than part of the claimed new domain. The verifier also checks exact rational finite-size bounds for the mean extra stabilizer size and the nonrigid proportion. Execution of the packaged program returned `VERIFY_OK`.

## Relationship to prior work
Wei and Zou (2023) identify isomorphism classes with monomial-group orbits, derive a general Burnside expression, and compute exact class numbers in dimensions at most four. Their result provides the group action used in this proof; the fixed-\(q\), growing-\(n\) probability estimates and asymptotic class count are not among their stated results. Sriwongsa and Zou (2022) describe automorphism groups and specific high-symmetry classes, not a uniform large-dimensional fixed-field law. A 2026 survey lists counting asymptotics and random automorphism probabilities as broader directions; the theorem here addresses only the perfect, matrix-uniform dense finite-field regime. Previously considered binary-field and fixed-dimension, growing-field rarity regimes are distinct from the \(q\ge3\), fixed-field theorem.

## Limitations
No sharp leading asymptotic is claimed for \(\Pr(S(A)>1)\), only a rigorous vanishing upper bound. The dependence is not uniform when \(q\) grows with \(n\). The theorem concerns \(E^2=E\); it does not settle the broader random singular-matrix model or the total number of all evolution algebras. The computational verifier uses prime fields, not all prime-power representations; the proof is field-general. Literature comparisons do not certify publication priority.

## References
1. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1 (public 2023-10-18), especially Theorem 1.1, Section 2, equation (3.1), and Theorem 6.1. https://arxiv.org/pdf/2310.12368
2. S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333 (2022), especially Theorem 2.1 and Sections 3–4. https://arxiv.org/pdf/2202.01333
3. I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (public 2026-10-15), especially Sections 1.3.4, 1.6.1 and Questions 21–22. https://arxiv.org/pdf/2610.22248
