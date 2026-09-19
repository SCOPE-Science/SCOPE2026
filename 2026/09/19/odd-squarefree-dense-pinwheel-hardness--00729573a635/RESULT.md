# Dense Pinwheel Packing remains hard with odd squarefree periods

## Statement

Consider **Dense Pinwheel Packing** in the explicit-list model: the input is a list of positive integer periods \(a_1,\ldots,a_k\), equal periods may occur as distinct tasks, the density satisfies
\[
\sum_{i=1}^k \frac1{a_i}=1,
\]
and the question is whether the tasks admit a feasible pinwheel schedule.

**Theorem.** Dense Pinwheel Packing is NP-complete under unary encoding even under the simultaneous restrictions that

1. every period is **odd**;
2. every period is **squarefree**;
3. every period has at most **five distinct prime factors**; and
4. the least common multiple of all periods is itself odd and squarefree; and
5. the greatest common divisor of all periods is an odd prime.

Consequently, the usual binary-encoded problem is strongly NP-complete under the same restrictions.

More precisely, the reduction can be arranged so that there is an odd prime \(p\) and distinct odd marker primes \(r_T>p\) such that every period is of one of the forms
\[
p\prod_{T\ni v}r_T
\quad\text{or}\quad
3p\prod_{T\ni v}r_T,
\]
where each product contains between one and three marker primes. The global least common multiple is exactly
\[
\boxed{M=3p\prod_T r_T},
\]
which is odd and squarefree, while the greatest common divisor of all listed periods is exactly \(p\).

## Context

Kobayashi, Lin, and Swernofsky [1] prove that Dense Pinwheel Packing is NP-complete even when periods are encoded in unary. Their reduction starts from **Sparse Tripartite Triangle Partition**. If the three parts have size \(n\), each graph triangle \(T\) receives a distinct prime marker \(r_T>\max\{3,n\}\), and for each vertex \(v\)
\[
m_v=\prod_{T\ni v}r_T.
\]
Because every source vertex belongs to at least one and at most three graph triangles, \(m_v\) is a product of one, two, or three distinct marker primes. The target contains one task of period \(nm_v\) and \(m_v-3\) tasks of period \(3nm_v\). Their soundness and completeness show that the target is feasible exactly when the source graph has a triangle partition, and their size analysis proves that the full unary output is polynomial.

The only obstruction to making those periods automatically odd and squarefree is therefore the common part-size factor \(n\). A prime-padding step removes that obstruction without changing the source decision problem.

This arithmetic restriction is separate from the classical theory of covering systems with **distinct** moduli. For example, Balister--Bollobás--Morris--Sahasrabudhe--Tiba [3] show that a covering system with distinct squarefree moduli must contain an even modulus. Dense Pinwheel Packing uses an explicit list in which equal periods are allowed as distinct tasks, so there is no contradiction: repetition is essential to the reduction and is allowed by the problem definition.

## Proof

Let \(G=(X\mathbin{\dot\cup}Y\mathbin{\dot\cup}Z,E)\) be an instance of Sparse Tripartite Triangle Partition, with
\[
|X|=|Y|=|Z|=n,
\]
maximum degree at most six, and every vertex contained in between one and three graph triangles.

### 1. Prime padding the source instance

Put \(N=\max\{n,5\}\). By Bertrand's postulate there is a prime \(p\) with
\[
N<p<2N.
\]
Thus \(p>3\) and \(p=O(n+1)\).

Add \(p-n\) disjoint dummy components. Each dummy component consists of one new vertex in each tripartition class and the three edges forming a single tripartite triangle. There are no edges from a dummy component to any other vertex. Call the padded graph \(G'\).

Then every part of \(G'\) has size \(p\). The degree bound is preserved: every dummy vertex has degree two. The triangle-incidence promise is also preserved: every dummy vertex belongs to exactly one triangle.

Moreover,
\[
\boxed{G\text{ has a triangle partition}\iff G'\text{ has a triangle partition}.}
\]
Indeed, in any triangle partition of \(G'\), each dummy component must use its unique triangle, because it has no edges to the rest of the graph. Deleting those forced dummy triangles leaves a triangle partition of \(G\). The forward implication is obtained by adjoining all dummy triangles to any partition of \(G\).

The padding is polynomial-time and increases the source size by only a constant factor.

### 2. Apply the strong-hardness reduction

Apply the reduction of [1] to \(G'\), now with common part size \(p\). Enumerate all graph triangles \(T\) of \(G'\), assign them pairwise distinct primes
\[
r_T>p,
\]
and define
\[
m_v=\prod_{T\ni v}r_T.
\]
For each vertex \(v\), create

- one witness task of period \(pm_v\), and
- \(m_v-3\) cell tasks of period \(3pm_v\).

The reduction in [1] applies verbatim to \(G'\), so the resulting dense instance \(A(G')\) is feasible exactly when \(G'\) has a triangle partition, and hence exactly when \(G\) does.

### 3. Oddness, squarefreeness, and prime support

Every marker \(r_T\) is an odd prime strictly larger than \(p>3\), and all markers are distinct. Since a source vertex belongs to at most three triangles, \(m_v\) is squarefree with
\[
1\le \omega(m_v)\le3,
\]
where \(\omega\) counts distinct prime factors.

The witness period
\[
pm_v
\]
is therefore odd and squarefree, with at most four distinct prime factors.

The cell period
\[
3pm_v
\]
is also odd and squarefree, because \(3\), \(p\), and every marker dividing \(m_v\) are pairwise distinct. It has at most five distinct prime factors. Hence every target period satisfies the promised restrictions.

### 4. The common least common multiple is squarefree

Let \(\mathcal T\) be the complete triangle set of \(G'\). Every target period divides
\[
M=3p\prod_{T\in\mathcal T}r_T.
\]
Conversely, \(p\) divides every period. The prime \(3\) divides every cell period; cell tasks exist because each \(m_v\ge r_T>p>3\), so \(m_v-3>0\). Finally, every marker \(r_T\) divides the witness period of each vertex of \(T\). Hence every prime factor of \(M\) occurs in the least common multiple of the target periods, and
\[
\operatorname{lcm}(A(G'))=M.
\]
All factors of \(M\) are distinct odd primes, so the common least common multiple is odd and squarefree.

Every period is divisible by \(p\). No additional prime divides every period: \(3\) is absent from all witness periods, and a marker \(r_T\) occurs only in periods attached to the three vertices of \(T\), not to every vertex. Hence
\[
\boxed{\gcd(A(G'))=p}.
\]
Thus the common gcd is itself an odd prime.

### 5. Density and polynomial unary size

For each vertex \(v\), its target block contributes
\[
\frac1{pm_v}+(m_v-3)\frac1{3pm_v}
=\frac1{3p}.
\]
There are exactly \(3p\) vertices, so the total density is one.

The size bound of [1] is unchanged up to constants because the padded part size satisfies \(p=O(n+1)\). The number of graph triangles remains linear in \(p\); the marker primes are polynomially bounded; each \(m_v\) contains at most three of them; and both the number of explicitly listed tasks and the largest period are polynomial in the source size. Thus the reduction is polynomial even under unary period encoding.

Dense Pinwheel Packing is in NP by the residue-class certificate of [1]. This proves NP-completeness of the restricted unary problem, and strong NP-completeness under the usual binary representation. \(\square\)

## Equivalent exact-covering formulation

At density one, feasibility is equivalent to choosing one residue class modulo each listed period so that the classes partition \(\mathbb Z\). Because every period divides the odd squarefree integer \(M\), the same certificate can be viewed inside the finite cyclic group \(\mathbb Z/M\mathbb Z\): choose one coset of the subgroup associated with each listed divisor so that the chosen cosets partition the group.

Thus the hardness survives in a divisor lattice with no repeated prime powers at all, while every individual modulus uses at most five prime coordinates of that lattice. This is the structural content beyond mere polynomial boundedness of the periods.

## Reproducibility check

`artifacts/verify_arithmetic.py` checks the arithmetic part of the construction for representative odd common primes and all possible source triangle-incidence counts \(1,2,3\): oddness, squarefreeness, the bounds on \(\omega\), the per-vertex density identity, and the claimed squarefree common-LCM identity. Its recorded output is in `artifacts/verify_output.txt`.

The finite script is a sanity check only. The theorem is proved by the reduction above.

## Limitations

- Equal periods are allowed as distinct tasks, exactly as in the explicit-list Dense Pinwheel Packing model of [1]. The theorem does **not** imply an odd-squarefree covering system with distinct moduli.
- The constant five is not claimed to be optimal. The argument does not establish hardness when every period has at most four prime factors, nor when every period is prime or semiprime.
- The new ingredient is an arithmetic restriction of the recent strong-hardness reduction, not a new hardness source or a new scheduling soundness/completeness mechanism.
- Originality is asserted only to the best of our knowledge. Because [1] is very recent and the prime-padding refinement is short once the reduction is visible, near-simultaneous observation or a subsequent revision remains a material priority risk.

## References

1. Y. Kobayashi, B. Lin, and J. Swernofsky, **Dense Pinwheel Packing Is Strongly NP-Complete**, arXiv:2609.20075, 2026. https://arxiv.org/abs/2609.20075
2. R. Kleinberg and A. Mishra, **NP-Hardness and a PTAS for the Pinwheel Problem**, arXiv:2604.13974, 2026. https://arxiv.org/abs/2604.13974
3. P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe, and M. Tiba, **The Erdős--Selfridge problem with square-free moduli**, Algebra & Number Theory 15 (2021), 609--626; arXiv:1901.11465. https://arxiv.org/abs/1901.11465
