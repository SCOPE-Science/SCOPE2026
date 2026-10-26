# Prescribed Diophantine densities for two covering sets of upper density one

## Finding

Let \(\delta(T)\) be the restricted-approximation Diophantine density defined below. **For every pair \((\alpha,\beta)\in[0,1]^2\), there exist explicit subsets \(A_\alpha,B_\beta\subseteq\mathbb N\) such that**

\[
A_\alpha\cup B_\beta=\mathbb N,\qquad
\delta(A_\alpha)=\alpha,\qquad
\delta(B_\beta)=\beta,
\]

and both sets have upper ordinary asymptotic density equal to \(1\). Thus the set of possible ordered Diophantine-density pairs for two sets covering \(\mathbb N\) is exactly \([0,1]^2\). At \(\alpha=\beta=0\), the two covering sets are disjoint and both have Diophantine density zero, while their union has density one. In particular, this Diophantine density is not subadditive; the discrepancy is the largest possible.

## Assumptions and scope

Write \(\mathbb N=\{1,2,\ldots\}\), let \(\|x\|\) denote distance to the closest integer, and set \(T(Q)=\#\{v\in T:1\le v<Q\}\). For nonempty \(T\subseteq\mathbb N\), define \(\delta(T)\) as the supremum of all \(s\ge0\) for which there exist \(C>0\) and \(q_0\ge2\) such that, for every integer \(q\ge q_0\) and every integer \(p\) coprime to \(q\), some \(v\in T\) with \(1\le v<q\) satisfies

\[
\left\|\frac{vp}{q}\right\|\le Cq^{-s}.
\]

Set \(\delta(\varnothing)=0\). The normalization implies \(0\le\delta(T)\le1\), \(\delta(\mathbb N)=1\), and monotonicity under set inclusion. The set at each real parameter is mathematically explicit through integer floors; no claim of effective computation from an uncomputable real parameter is made.

## Proof

**Step 1: the cardinality obstruction.** For every nonempty \(T\),

\[
\delta(T)\le\liminf_{Q\to\infty}\frac{\log T(Q)}{\log Q}.
\tag{1}
\]

To reconstruct this bound directly, fix \(0<s<\delta(T)\). The defining approximation holds with an exponent \(s\) and a fixed constant \(C\). If \(q\) is a sufficiently large prime, then for each fixed \(v\in T\) with \(v<q\), multiplication by \(v\) permutes the nonzero residues modulo \(q\). Hence at most \(2Cq^{1-s}\) of the \(q-1\) possible numerator classes \(p\) satisfy the required inequality with this \(v\). All \(q-1\) classes must be covered, so

\[
q-1\le 2Cq^{1-s}T(q),\qquad T(q)\ge \frac{1}{4C}q^s.
\]

Bertrand's postulate supplies a prime between \(Q/2\) and \(Q\); monotonicity of \(T(Q)\) therefore extends \(T(Q)\gg_s Q^s\) to all sufficiently large integers \(Q\). Taking lower logarithmic growth and then \(s\uparrow\delta(T)\) proves (1); the case \(\delta(T)=0\) is immediate. This reproduces the relevant upper-bound argument independently.

**Step 2: small cores with exactly prescribed density.** For \(0<t<1\), put

\[
n_{t,k}=\lfloor 2^{tk}\rfloor,\qquad
d_{t,k}=\left\lfloor\frac{2^k}{n_{t,k}}\right\rfloor,\qquad
S_t=\bigcup_{k\ge0}\{md_{t,k}:1\le m\le n_{t,k}\}.
\]

For any \(q\ge2\), choose \(k\) with \(2^k<q\le2^{k+1}\). Dirichlet's pigeonhole lemma applied to \(d_{t,k}p/q\) yields an integer \(1\le m\le n_{t,k}\) for which \(v=md_{t,k}\le2^k<q\) and

\[
\left\|\frac{vp}{q}\right\|\le\frac1{n_{t,k}+1}<2^{-tk}\le 2^t q^{-t}.
\]

Thus \(\delta(S_t)\ge t\). To count members below \(Q\), split the union into \(k\le L=\lfloor\log_2Q\rfloor\) and \(k>L\). The first part contributes at most \(\sum_{k\le L}2^{tk}=O_t(Q^t)\). Since \(d_{t,k}\ge2^{(1-t)k-1}\), the second contributes at most \(2Q\sum_{k>L}2^{-(1-t)k}=O_t(Q^t)\). Therefore \(S_t(Q)=O_t(Q^t)\), and (1) gives \(\delta(S_t)=t\). At endpoints, set \(S_0=\varnothing\) and \(S_1=\mathbb N\), which have densities \(0\) and \(1\), respectively.

**Step 3: alternating superexponential blocks.** Let \(b_0=2\), \(b_{j+1}=2^{b_j}\), and define

\[
E=\bigcup_{j\ge0}\bigl([b_{2j},b_{2j+1})\cap\mathbb N\bigr),
\qquad O=\mathbb N\setminus E.
\]

For \(j\ge1\) and \(Q=b_{2j}\), there are no elements of \(E\) between \(b_{2j-1}\) and \(Q\); in particular, \(E(Q)\le b_{2j-1}\). Similarly, for \(Q=b_{2j+1}\), \(O(Q)\le b_{2j}\). Both subsequences are unbounded, and

\[
\frac{\log b_{j-1}}{\log b_j}
=\frac{b_{j-2}}{b_{j-1}}\longrightarrow0
\qquad (j\to\infty).
\tag{2}
\]

Consequently, both \(E\) and \(O\) have lower logarithmic counting exponent zero; by (1), \(\delta(E)=\delta(O)=0\). They cover \(\mathbb N\) disjointly. Both also have upper ordinary asymptotic density one, because their respective full blocks occupy fractions \(1-b_j/b_{j+1}\to1\) of initial intervals ending at suitable \(b_{j+1}\).

**Step 4: interpolation without disturbing the opposite sparse scales.** Define

\[
A_\alpha=E\cup S_\alpha,\qquad B_\beta=O\cup S_\beta.
\]

Their union is \(\mathbb N\). Monotonicity gives \(\delta(A_\alpha)\ge\alpha\) and \(\delta(B_\beta)\ge\beta\). If \(0<\alpha<1\), at \(Q=b_{2j}\),

\[
A_\alpha(Q)\le C_\alpha Q^\alpha+b_{2j-1}
=Q^{\alpha+o(1)},
\]

where (2) makes the second term \(Q^{o(1)}\). For \(\alpha=0\), the corresponding bound is \(A_0(Q)\le b_{2j-1}=Q^{o(1)}\); for \(\alpha=1\), use \(\delta(A_1)\le1\). Applying (1) gives \(\delta(A_\alpha)\le\alpha\) in every case. Using \(Q=b_{2j+1}\) gives the identical conclusion \(\delta(B_\beta)\le\beta\). Thus both equalities hold. Their inclusions of \(E\) and \(O\) guarantee upper ordinary asymptotic density one. Since all Diophantine densities lie in \([0,1]\), this construction realizes the entire possible ordered-pair region and proves the theorem.

## Verification

A standalone exact-integer Python verifier accompanies the result. For five rational parameters it checks Dirichlet-stage witnesses over all coprime numerator classes with \(3\le q<260\), and checks the block partition through the first \(65{,}536\) positive integers. It also tests finite core-membership counts at several thresholds, using integer-root floors without floating-point approximations. Execution returned `VERIFY_OK rational_dirichlet_checks=102510 integer_partition_checks=65536 exact_fraction_floor_checks=PASS all_finite`. These finite tests do not certify the infinite estimates, which are established above.

## Relationship to prior work

Chance Sanford introduced the restricted-approximation density condition in *A Note on Diophantine Approximation with Restricted Denominators* (first public May 28, 2026). In his *On a Notion of Density Related to Restricted Diophantine Approximation* (first public October 20, 2026), the normalized supremum definition, the upper counting bound, and the prescribed-density cores are explicit (Theorems 5 and 6); Section 7, Question 2 asks whether a union may have strictly greater Diophantine density than either constituent and considers failure of subadditivity. These named ingredients and question are not claimed as new. The proof above reconstructs their relevant ingredients and combines them with scale-separated blocks to settle the question and classify all prescribed covering pairs.

Di Nasso and Jin, *Abstract densities and ideals of sets*, Proposition 1.3 (2017), already exhibit alternating-block witnesses to non-subadditivity of **lower ordinary asymptotic density**. The use of alternating blocks alone is therefore not new. That work does not establish the corresponding claim for Sanford's restricted rational-approximation density or the all-pairs interpolation. This finding is the application and quantified synthesis, not a claim to a novel block technique or an independent rediscovery of the foundational lemmas.

## Limitations

The construction is existential and explicit via real-parameter floors; uniform efficient computability for arbitrary noncomputable parameters is not asserted. It classifies covering pairs, not disjoint partitions at every prescribed pair. Ordinary asymptotic densities generally fail to exist for the examples, although their upper ordinary densities are both one. The finding is an elementary synthesis of existing ingredients rather than a general theorem about all abstract densities. Potential subsumption by other sources or unpublished priority remains for independent verification.

## References

1. Chance Sanford, *A Note on Diophantine Approximation with Restricted Denominators*, arXiv:2606.02620v1 (2026-05-28), https://arxiv.org/abs/2606.02620.
2. Chance Sanford, *On a Notion of Density Related to Restricted Diophantine Approximation*, arXiv:2610.27497v1 (2026-10-20), Sections 2–4 and 7, https://arxiv.org/html/2610.27497v1.
3. Mauro Di Nasso and Renling Jin, *Abstract densities and ideals of sets*, arXiv:1709.03097 (2017), Proposition 1.3, https://arxiv.org/abs/1709.03097.
