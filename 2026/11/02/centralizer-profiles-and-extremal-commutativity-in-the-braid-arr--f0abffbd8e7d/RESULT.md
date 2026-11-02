# Centralizer profiles and extremal commutativity in the braid-arrangement face monoid

## Finding

For every integer \(n\ge1\), let \(\mathcal F_n\) be the face monoid of the type-\(A\) braid arrangement, identified with all ordered partitions of \([n]\). For \(\alpha=(A_1,\ldots,A_k)\), write \(m_i=|A_i|\). Let \(F_m=\sum_{j=1}^{m}j!\,\left\{\begin{smallmatrix}m\\j\end{smallmatrix}\right\}\) be the ordered Bell number; \(F_0=1\).

**Centralizer theorem.** The number of elements commuting with \(\alpha\) is
\[
|\operatorname{Cent}_{\mathcal F_n}(\alpha)|=2^{k-1}\prod_{i=1}^k F_{m_i}.
\]
This determines the entire centralizer-size multiset: for every positive composition \((m_1,\ldots,m_k)\) of \(n\), the displayed size occurs with the composition's multiplicity \(n!/\prod_i m_i!\), with multiplicities added whenever sizes coincide.

**Extremal centralizers.** Among elements with exactly \(k\) blocks, the maximum is \(2^{k-1}F_{n-k+1}\), attained precisely by block-size compositions with at most one size above one. Writing \(n=ak+r\) with \(0\le r<k\), the minimum is \(2^{k-1}F_a^{k-r}F_{a+1}^r\), attained precisely when all block sizes differ by at most one. These characterizations include the boundary \(k=1\) and \(k=n\).

**Global commutativity.** The count \(C_n\) of ordered pairs \((\alpha,\beta)\) with \(\alpha\beta=\beta\alpha\) is
\[
C_n=\sum_{j=1}^{n}3^{j-1}j!\left\{\begin{smallmatrix}n\\j\end{smallmatrix}\right\},\qquad
\sum_{n\ge0}C_n\frac{z^n}{n!}=\frac{3-2e^z}{4-3e^z},\quad C_0=1.
\]
The numerical sequence \(1,1,7,73,1015,17641,\ldots\) and its generating function were already tabulated as OEIS A050352 for another class of objects; no numerical-sequence priority is claimed. The assertion here is the complete semigroup centralizer profile, its extremizers, and its commutativity interpretation.

For independent uniformly chosen elements of \(\mathcal F_n\), as \(n\to\infty\),
\[
\Pr(\alpha\beta=\beta\alpha)\sim\frac{1}{3n!}
\left(\frac{(\log 2)^2}{\log(4/3)}\right)^{n+1}.
\]

## Assumptions and scope

All statements concern the finite combinatorial monoid \(\mathcal F_n\) for **every** positive integer \(n\), without a field or characteristic assumption. An ordered partition is a sequence of disjoint nonempty subsets whose union is \([n]\). Multiplication is defined by listing all nonempty intersections \(A_i\cap B_j\) in lexicographic \((i,j)\) order. For convenience the empty ground set has the unique empty ordered partition, which is the identity of \(\mathcal F_0\). The numbers \(F_m\) count ordered partitions of an \(m\)-element labeled set.

## Proof

**Step 1: a necessary and sufficient commutation criterion.** Write \(\alpha=(A_1,\ldots,A_k)\), \(\beta=(B_1,\ldots,B_\ell)\). In \(\alpha\beta\), the nonempty cells \(A_i\cap B_j\) are ordered by \((i,j)\); in \(\beta\alpha\), exactly the same cells are ordered by \((j,i)\). These orders agree if and only if there do not exist nonempty cells \(A_i\cap B_j\) and \(A_{i'}\cap B_{j'}\) with \(i<i'\) but \(j>j'\). Equivalently, for all \(x\in A_i\), \(y\in A_{i'}\) and \(i<i'\), the \(\beta\)-block index of \(x\) is at most that of \(y\). This criterion includes ties.

**Step 2: centralizer bijection.** Fix \(\alpha\). Every commuting \(\beta\) restricts to an arbitrary ordered partition of each \(A_i\). By Step 1 the restrictions occur in consecutive order. At each of the \(k-1\) interfaces, the last restricted block of \(A_i\) and the first restricted block of \(A_{i+1}\) may either belong to the same \(\beta\)-block or be separated; no other mixing is possible. Conversely, independently making either choice at every interface, then merging the specified adjacent blocks transitively, yields a unique \(\beta\) satisfying Step 1. Even if several consecutive interfaces are merged, all such chains are uniquely reconstructed from \(\beta\) and the fixed \(\alpha\). This is a bijection with \(\prod_i \operatorname{OP}(A_i)\times\{0,1\}^{k-1}\) and proves the centralizer formula. An ordered block-size composition \((m_i)\) has exactly \(n!/\prod_i m_i!\) labeled realizations; therefore the asserted complete distribution follows.

**Step 3: strict extremal rule.** The ordered Bell numbers admit the positive moment representation
\[
F_m=\frac12\sum_{r=0}^{\infty}\frac{r^m}{2^r}\qquad(m\ge0),
\]
with \(0^0=1\). By strict Cauchy--Schwarz, \(F_m^2<F_{m-1}F_{m+1}\) for every \(m\ge1\). Hence the successive ratios \(F_{m+1}/F_m\) increase strictly with \(m\). For positive \(x\ge y+2\), replacing sizes \((x,y)\) by \((x-1,y+1)\) strictly decreases the product. Iterating proves that the unique minimizing multiset is balanced. Conversely, transferring one unit from a smaller positive size greater than one to a larger size strictly increases the product until at most one size exceeds one; this is the unique maximizing multiset. The factor \(2^{k-1}\) is common to both. The cases \(k=1\) and \(k=n\) are immediate.

**Step 4: total count.** The exponential generating function of nonempty ordered partitions is
\[
T(z)=\sum_{m\ge1}F_m\frac{z^m}{m!}=\frac{e^z-1}{2-e^z}.
\]
For fixed \(k\), summing \(n!/\prod_i m_i!\) times \(2^{k-1}\prod_iF_{m_i}\) over all positive compositions yields the exponential series \(2^{k-1}T(z)^k\). Therefore
\[
\sum_{n\ge0}C_n\frac{z^n}{n!}
=1+\sum_{k\ge1}2^{k-1}T(z)^k
=1+\frac{T(z)}{1-2T(z)}
=\frac{3-2e^z}{4-3e^z}.
\]
Expanding \(1+\frac{e^z-1}{1-3(e^z-1)}\) in powers of \(e^z-1\) and using the standard Stirling expansion yields the sum for \(C_n\). The resulting numbers coincide with the already-known A050352 values.

**Step 5: probability.** The dominant singularity of \(T(z)\)'s ordered-Bell generating function \(1/(2-e^z)\) is the simple pole at \(\sigma=\log 2\), implying \(F_n\sim n!/(2\sigma^{n+1})\). The dominant singularity of the commuting-pair generating function is the simple pole at \(\rho=\log(4/3)\), with residue \(-1/12\), implying \(C_n\sim n!/(12\rho^{n+1})\). All other poles of the respective functions have strictly greater modulus. Dividing by \(F_n^2\) proves the displayed commutativity asymptotic.

## Verification

The included `face_band_verify.py` builds every ordered partition as a surjective block-index word, calculates the two products directly from their intersection cells, and tests **every ordered pair** through \(n=5\). Every individual centralizer agrees with \(2^{k-1}\prod_iF_{m_i}\), and the total commuting-pair counts are \(1,1,7,73,1015,17641\). It also checks independent sample noncommutation. Run `python3 face_band_verify.py`; the expected final line is `VERIFY_OK`. This is exhaustive only for the indicated finite sizes, while the proof above is unrestricted.

## Relationship to prior work

Commins, *Invariant theory for the face algebra of the braid arrangement*, arXiv:2404.00536v1 (31 March 2024), §2.1, defines precisely this face monoid and product and develops the symmetric-group and descent-algebra representation theory. Steinberg, *Topology and monoid representations II: left regular bands of groups and Hsiao's monoid of ordered G-partitions*, arXiv:2404.03475v1 (4 April 2024), studies extensions, resolutions and representation theory for the broader left regular-band framework. Their inspected results do not assert centralizer-cardinality profiles or the semigroup commuting-pair theorem.

**Numerical prior coverage:** OEIS A050352, originally authored in 1999, records the same integer sequence, exponential generating function, Stirling expansion and first-order asymptotic under a 4-level labeled-tree interpretation. Those formulas are acknowledged rather than asserted as independently new; only the semigroup-specific structural classification and extremal centralizer consequences are proposed as a new finding.

## Limitations

The claim concerns finite braid-arrangement face monoids, not arbitrary arrangements or general left regular bands. Exact priority remains provisional: an earlier general theory of Tits products could implicitly specialize to the stated centralizer parametrization. No claim is made that the numerical sequence or its generating function was undiscovered, nor that numerical checks prove the all-\(n\) theorem. There has been no independent mathematical audit.

## References

1. P. Commins, *Invariant theory for the face algebra of the braid arrangement*, arXiv:2404.00536v1, 31 March 2024; https://arxiv.org/abs/2404.00536 .
2. B. Steinberg, *Topology and monoid representations II: left regular bands of groups and Hsiao's monoid of ordered G-partitions*, arXiv:2404.03475v1, 4 April 2024; https://arxiv.org/abs/2404.03475 .
3. OEIS Foundation, *A050352: Number of 4-level labeled linear rooted trees with n leaves*, https://oeis.org/A050352 , original entry 1999; contains the pre-existing sequence and its generating function.
