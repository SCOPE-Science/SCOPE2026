# Sharp generic rigidity and orbit asymptotics for perfect evolution algebras over nonbinary finite fields

## Finding

Fix a prime power \(q\ge3\). For each \(n\ge1\), independently choose a uniform invertible matrix \(A=(a_{ij})\in\operatorname{GL}_n(\mathbb F_q)\), and form the perfect evolution algebra \(E_A\) with natural basis \(e_1,\ldots,e_n\), cross-products \(e_i e_j=0\) for \(i\ne j\), and squares \(e_i^2=\sum_j a_{ij}e_j\). All limits below hold with \(q\) fixed and \(n\to\infty\).

Put
\[
\beta_{n,q}=\binom n2(q-1)^2q^{1-2n}.
\]
Then
\[
\Pr\bigl(\operatorname{Aut}_{\mathbb F_q}(E_A)\ne1\bigr)
=\beta_{n,q}(1+o_q(1)),
\]
and, conditional on a nontrivial automorphism group,
\[
\Pr\bigl(\operatorname{Aut}_{\mathbb F_q}(E_A)\cong C_2\mid
\operatorname{Aut}_{\mathbb F_q}(E_A)\ne1\bigr)\longrightarrow1.
\]
More precisely, the unique nonidentity automorphism of a typical exceptional algebra interchanges exactly two natural-basis lines, with reciprocal nonzero scalings, and fixes all other basis elements.

Let \(\mathcal N_{n,q}\) be the number of isomorphism classes of \(n\)-dimensional perfect evolution algebras over \(\mathbb F_q\). Then
\[
\boxed{\mathcal N_{n,q}=
\frac{|\operatorname{GL}_n(\mathbb F_q)|}{n!(q-1)^n}
\left(1+\beta_{n,q}+o_q(\beta_{n,q})\right).}
\]
The same symmetry correction satisfies
\[
\mathbb E\,|\operatorname{Aut}_{\mathbb F_q}(E_A)|
=1+\beta_{n,q}+o_q(\beta_{n,q}).
\]
Thus rigidity holds not only for uniformly sampled structure matrices but also for a proportion tending to one of isomorphism classes. These statements concern ordinary automorphism groups over the stated finite field, not automorphism group schemes or all (possibly singular) evolution algebras.

## Assumptions and scope

A finite evolution algebra is called *perfect* when its square spans the algebra, equivalently when its structure matrix in a natural basis is nonsingular. The sample space for the probability is the set of \(|\operatorname{GL}_n(\mathbb F_q)|=q^{n^2}\prod_{j=1}^n(1-q^{-j})\) invertible matrices, each equally likely; it is not uniform over isomorphism classes. The orbit-count conclusion concerns unlabeled isomorphism classes. The field order \(q\ge3\) is fixed during the dimension limit. We do not assert a uniform error as \(q\) grows with \(n\).

An invertible evolution-algebra automorphism sends each natural basis vector to a nonzero scalar multiple of another basis vector. Indeed, the squares of the natural basis vectors are linearly independent, and the products of two distinct images must vanish; hence their coordinate supports are disjoint, and an invertible transformation of \(n\) nonzero disjoint supports on \(n\) coordinates must be monomial. Explicitly, with \(\varphi(e_i)=t_i e_{\sigma(i)}\), the automorphism condition is
\[
t_j a_{ij}=t_i^2 a_{\sigma(i),\sigma(j)}
\quad(1\le i,j\le n).
\tag{1}
\]
This also determines the natural monomial group action on structure matrices; the acting group has order \(n!(q-1)^n\).

## Proof

**1. Stabilizers and the scalar fixed-point sum.** Take an auxiliary matrix with all \(n^2\) entries independent uniform over \(\mathbb F_q\), without yet conditioning on nonsingularity. For a scalar tuple \(t=(t_1,\ldots,t_r)\in(\mathbb F_q^\times)^r\), define
\[
E_r(t)=\#\{(i,j):t_j\ne t_i^2\},\qquad
Z_r(q)=\sum_{t\in(\mathbb F_q^\times)^r}q^{-E_r(t)},
\quad Z_0(q)=1.
\]
Let \(N_v\) count the occurrences of scalar \(v\) in \(t\), and let \(L=\max_vN_v\). Every row has at most \(L\) permitted column positions under (1), hence \(E_r(t)\ge r(r-L)\). If all entries equal \(v\ne1\), the number of forbidden positions is \(r^2\), since \(v^2=v\) in the multiplicative group only for \(v=1\). If \(L>r/2\) and \(a=r-L\ge1\), there are at most \((q-1)\binom ra(q-2)^a\) scalar tuples of this majority type. If \(L\le r/2\), all have \(E_r(t)\ge r^2/2\). Consequently
\[
0\le Z_r(q)-1\le (q-2)q^{-r^2}
+(q-1)\sum_{a=1}^{\lfloor(r-1)/2\rfloor}
\binom ra(q-2)^a q^{-ra}
+(q-1)^r q^{-r^2/2}
=O_q(rq^{-r}).\tag{2}
\]
The implied constant depends only on the fixed field.

For a permutation moving exactly \(s\) indices, there are \(r=n-s\) fixed indices and exactly \(2sn-s^2\) moved ordered matrix positions. Under (1), each moved-position orbit of length \(d\ge2\) has at most one free matrix entry, hence contributes a probability at most \(q^{-(d-1)}\). The entire moved portion therefore contributes at most \(q^{-\lceil(2sn-s^2)/2\rceil}\). Summing the \((q-1)^s\) scalars on moved indices and all scalars on fixed indices gives
\[
\sum_{t\in(\mathbb F_q^\times)^n}
\Pr(\text{the monomial }(\sigma,t)\text{ fixes }A)
\le(q-1)^s Z_{n-s}(q)
q^{-\lceil(2sn-s^2)/2\rceil}.\tag{3}
\]
The probability that a uniform matrix is nonsingular is bounded below by the positive constant \(\Phi_q=\prod_{j\ge1}(1-q^{-j})\), so restricting to invertible matrices costs at most the multiplicative factor \(\Phi_q^{-1}\).

**2. Permutations moving at least three indices.** There are at most \(n^s\) permutations with support \(s\). For \(3\le s\le n/2\), equation (2) makes \(Z_{n-s}(q)\le2\) for sufficiently large \(n\), and \(\lceil(2sn-s^2)/2\rceil\ge3sn/4\). Summation of (3) gives \(O_q(n^3q^{-9n/4})\). For \(s>n/2\), the crude bound \(Z_{n-s}(q)\le(q-1)^{n-s}\) and the rank loss \(\ge3n^2/8\) give a superexponentially small remainder. Thus the expected number of all stabilizer elements whose permutation moves at least three indices is
\[
o_q(n^2q^{-2n}).\tag{4}
\]

**3. Purely diagonal automorphisms.** Suppose \(\sigma=1\), the matrix is invertible, and a nonidentity tuple \(t\) satisfies (1). A row with scalar \(v\) can have nonzero entries only in columns whose scalar is \(v^2\). Invertibility forces the multiplicity vector \((N_v)\) to be stationary under the deterministic squaring map: for every scalar \(w\), \(N_w=\sum_{v^2=w}N_v\). Thus every scalar occurring in \(t\) lies on a periodic squaring orbit and occurs with the same multiplicity as the other elements of that orbit. The sole fixed point of squaring in \(\mathbb F_q^\times\) is \(1\); every other periodic orbit has length at least two.

Let \(h\) be the number of coordinates with \(t_i\ne1\). Then \(h\ge2\). Because no nonidentity periodic scalar squares to \(1\), every matrix entry crossing between the \(h\) exceptional coordinates and the \(n-h\) identity coordinates is zero. For \(2\le h\le n/2\), the probability of these \(2h(n-h)\) zeros is at most \(q^{-2h(n-h)}\). There are at most \(\binom nh(q-2)^h\) tuples with \(h\) exceptions, so their total contribution is \(O_q(n^3q^{-3n})\) (with the \(h=2\) term even smaller). For \(h>n/2\), no scalar occurs more than \(n/2\) times: the identity scalar occurs \(n-h<n/2\) times and each nonidentity scalar at most \(h/2\) times. Hence \(E_n(t)\ge n^2/2\), yielding a superexponentially small sum. After conditioning on invertibility, all nonidentity diagonal automorphisms contribute
\[
o_q(n^2q^{-2n}).\tag{5}
\]

**4. Exact leading contribution of transpositions.** Fix a transposition \(\sigma=(1\ 2)\), and assume all scalars on its other \(n-2\) fixed indices equal \(1\). Write \(u=t_1\), \(v=t_2\). If \(uv\ne1\), the automorphism equations force every entry in columns \(1,2\) to vanish: the equations for the two swapped columns in every fixed row force those entries to zero, while the four entries in the leading \(2\times2\) block also vanish. Such a matrix cannot be invertible. If \(uv=1\), there are exactly \(q-1\) choices, and each resulting scaled transposition is diagonally conjugate in the monomial group to the unscaled transposition. Hence each has precisely \(|C_{\operatorname{GL}_n(q)}(P_\sigma)|\) invertible fixed matrices.

For odd characteristic, the permutation matrix has eigenspace dimensions \(n-1\) and \(1\), so its centralizer has size \(|\operatorname{GL}_{n-1}(q)|(q-1)\). For even characteristic, its Jordan type is \((2,1^{n-2})\); the centralizer units form a group of size \(q^{2n-3}(q-1)|\operatorname{GL}_{n-2}(q)|\). In either case, with \(n\ge2\),
\[
\frac{|C_{\operatorname{GL}_n(q)}(P_\sigma)|}{|\operatorname{GL}_n(q)|}
=(q-1)q^{1-2n}(1+O_q(q^{-n+1})).\tag{6}
\]
If one of the \(n-2\) fixed-index scalars is not \(1\), (2) and (3) bound the total expected contribution across every transposition by \(O_q(n^3q^{-3n})\). Therefore, the expected number of nonidentity automorphisms is
\[
\binom n2(q-1)
\frac{|C_{\operatorname{GL}_n(q)}(P_\sigma)|}{|\operatorname{GL}_n(q)|}
+o_q(n^2q^{-2n})
=\beta_{n,q}(1+o_q(1)).\tag{7}
\]

**5. From expectation to probability and orbit count.** Let \(T\) count the automorphisms of the canonical scaled-transposition kind in step 4, over all transpositions. If \(T\ge2\), multiplying two distinct such automorphisms produces either a nonidentity diagonal automorphism (same transposition, different scalings) or an automorphism whose underlying permutation moves three or four indices (different transpositions). By (4) and (5), this exceptional event is exponentially smaller than \(\beta_{n,q}\), even after multiplying its probability by the deterministic bound \(T\le\binom n2(q-1)\). Therefore \(\Pr(T\ge1)=\mathbb E T+o_q(\beta_{n,q})\). All automorphisms outside this canonical kind have total expected count \(o_q(\beta_{n,q})\), proving the probability and conditional \(C_2\) assertions.

Burnside's lemma gives
\[
\mathcal N_{n,q}=\frac{|\operatorname{GL}_n(q)|}{n!(q-1)^n}
\mathbb E|\operatorname{Aut}_{\mathbb F_q}(E_A)|,
\]
which, with (7), proves the orbit-count asymptotic. A nonrigid isomorphism class contributes at least one extra stabilizer element per matrix, so the proportion of nonrigid classes is \(O_q(\beta_{n,q})\), establishing the unlabeled rigidity assertion.

## Verification

The accompanying `verify_random_evolution.py` uses exhaustive prime-field matrix enumeration and, separately, a direct \(\mathbb F_4\) polynomial-basis implementation. It constructs all nonsingular structure matrices, explicitly checks every monomial algebra automorphism using (1), and independently counts the action's orbits. Tested cases are \((q,n)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(5,1),(5,2),(4,2)\); the binary cases are regression comparisons, not part of the novel domain. It independently checks the pure-transposition centralizer counts and 16 finite scalar sums. The verifier reports `VERIFY_OK`.

For instance, over \(\mathbb F_3\) in dimension \(3\), there are \(11232\) nonsingular matrices, \(576\) with nontrivial automorphism group, and \(249\) isomorphism classes. Over \(\mathbb F_4\) in dimension \(2\), the corresponding figures are \(180\), \(36\), and \(13\). These are finite checks only; the proof above supplies the infinite-dimension asymptotics.

## Relationship to prior work

Sriwongsa and Zou (2022) classify certain possible automorphism groups and maximal diagonal groups for perfect evolution algebras. Wei and Zou (2023) establish the monomial orbit framework and exact Burnside formula, with explicit enumerations in dimensions at most four. Costoya, Mayorga, and Viruel (2024) study representability of particular permutation actions. The theorem uses the established monomial description and orbit framework but establishes a new large-dimension, fixed-field probability law with an exact leading coefficient and corresponding asymptotic orbit count; the inspected primary texts do not state this result.

Kaygorodov, Martín González, and Viruel (2026) explicitly identify random evolution-algebra automorphism probabilities as an open research direction (Question 22). The present theorem addresses the dense, fixed-field, **perfect-algebra conditional subcase**, not the unrestricted singular or sparse cases. The binary-field \(q=2\) case has separate prior coverage and is excluded from the new claim, which starts at \(q\ge3\). The 2026 source motivates the value but does not set the first-public-source date for the older primary algebra direction.

## Limitations

The asymptotic fixes \(q\ge3\) and lets \(n\) grow. It is not uniform in the field order and does not settle automorphism probabilities for singular evolution algebras or for sparse random structures. The assertion concerns finite rational automorphism groups, not nonreduced automorphism group schemes. The finite enumerations are checks of boundary cases, not proof of asymptotics. Priority is a best-knowledge literature assessment, not an independent mathematical or bibliographic certification; an equivalent asymptotic under a broader monomial-matrix orbit theorem may exist.

## References

1. S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333, first publicly available 2022-02-02; https://arxiv.org/abs/2202.01333.
2. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, first publicly available 2023-10-18; https://arxiv.org/abs/2310.12368.
3. C. Costoya, P. Mayorga, and A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, arXiv:2401.05924, first publicly available 2024-01-11; https://arxiv.org/abs/2401.05924.
4. I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution Algebras: A Survey of Results and a List of Open Problems*, arXiv:2610.22248, first publicly available 2026-10-15; https://arxiv.org/abs/2610.22248, especially Question 22.
