# The first entropy gap for Boolean subset-sum covers of finite abelian groups

## Finding
For a finite abelian group \(H\), let \(\lambda(H)\) be the least length of a finite **sequence** \((h_1,\ldots,h_k)\), with repetitions permitted, such that every element of \(H\) is a sum \(\sum_{i=1}^k\epsilon_i h_i\) with each \(\epsilon_i\in\{0,1\}\). The empty sum is included. The counting bound is \(\lambda(H)\ge\lceil\log_2|H|\rceil\).

**Theorem.** Every nontrivial finite abelian group of order at most \(24\) attains this information-theoretic bound. The elementary abelian group \(G=(\mathbb Z/5\mathbb Z)^2\), of order \(25\), is the first exception: \(\lambda(G)=6>\lceil\log_2 25\rceil=5\). The other group of order \(25\), \(\mathbb Z/25\mathbb Z\), attains its bound.

More precisely, the Boolean subsums of any five-term **sequence** in \(G\) contain at most \(24\) distinct elements, and this is sharp. Exactly \(1920\) five-element **subsets** of \(G\) attain \(24\). They form precisely six orbits under \(\operatorname{GL}_2(\mathbb F_5)\), whose sizes, with multiplicity, are \(120,120,240,480,480,480\). Every sequence attaining \(24\) has five distinct elements.

## Assumptions and scope
All groups are finite and written additively. Vectors of \(G\) are coordinate pairs modulo \(5\). Sequence positions remain distinct even when two vectors agree, so the subset-sum definition allows using two equal vectors separately. The theorem's order bound covers every abelian isomorphism type with \(2\le |H|\le25\); the orbit assertion concerns the six linear, not affine, equivalence classes of extremal five-element subsets of \(G\). The result makes no claim about higher orders, about arbitrary moduli of prime-unit groups, or about coverings by distinct primes.

## Proof
Write \(\Sigma(h_1,\ldots,h_k)=\{\sum_{i=1}^k\epsilon_i h_i:\epsilon_i\in\{0,1\}\}\). If \(|H|=n\), then \(|\Sigma|\le 2^k\), proving the lower bound.

For a cyclic factor \(C_d\) with generator \(e\), the \(b=\lceil\log_2d\rceil\) entries \(e,2e,4e,\ldots,2^{b-1}e\) cover every residue: the ordinary binary expansions of \(0,\ldots,d-1\) already occur among the subset sums. Hence for the invariant-factor decomposition \(H\simeq C_{d_1}\times\cdots\times C_{d_r}\), there is a covering sequence of length \(\sum_j\lceil\log_2d_j\rceil\). The executable finite classification below independently enumerates all invariant-factor lists for every \(2\le n\le25\); for the \(38\) resulting group types, it checks that the displayed sum equals \(\lceil\log_2n\rceil\), except exactly for \(n=25\) and factors \((5,5)\), when the two quantities are \(6\) and \(5\). This proves the asserted upper bounds through order \(25\), subject only to determining the latter group's optimal length.

For \(G\), the six vectors \((1,0),(1,0),(2,0),(0,1),(0,1),(0,2)\) have all \(25\) subset sums, since each three-vector coordinate block has subset sums containing the five residues \(0,1,2,3,4\). Consequently \(\lambda(G)\le6\).

For the reverse bound, any five-term sequence whose vectors span a subgroup of rank below two has its subset sums in a subgroup of size at most \(5\). Otherwise, some two entries form an \(\mathbb F_5\)-basis. Since permutations and invertible linear maps preserve Boolean subsum cardinalities, we may put these two entries first and send them to \((1,0)\) and \((0,1)\). The remaining three entries range independently through all \(25\) vectors. Thus **all** five-term sequences, with repeats permitted, are covered by exactly \(25^3=15625\) normalized triples plus the rank-deficient case. The included exact-integer verifier runs this exhaustive search, using the recurrence
\[
S_0=\{(0,0)\},\qquad S_{j+1}=S_j\cup\bigl(S_j+v_{j+1}\bigr),
\]
and reports a maximum of \(24\); exactly \(480\) normalized ordered triples give \(24\), none involving repeated entries. Hence \(\lambda(G)\ge6\) and all five-term extremizers are distinct.

Independently, enumerate all \(\binom{25}{5}=53130\) five-element subsets of \(G\) and apply the same exact recurrence. Precisely \(1920\) have \(24\) subsums. Enumerate the \(480\) invertible \(2\times2\) matrices over \(\mathbb F_5\), apply each to every maximal subset, and partition the \(1920\) maximal subsets into disjoint orbits. The exhaustive exact calculation returns six orbits of sizes \(120,120,240,480,480,480\), all contained in the \(1920\)-set family and totaling \(1920\). Lexicographically least representatives (coordinate pairs reduced to \(0,1,2,3,4\)) are:

| Orbit size | Representative |
|---:|---|
| 480 | \(\{(0,1),(1,0),(1,1),(1,3),(2,3)\}\) |
| 480 | \(\{(0,1),(1,0),(1,1),(1,3),(2,4)\}\) |
| 240 | \(\{(0,1),(1,0),(1,1),(1,3),(3,1)\}\) |
| 480 | \(\{(0,1),(1,0),(1,1),(1,3),(3,2)\}\) |
| 120 | \(\{(0,1),(1,0),(1,1),(2,4),(4,2)\}\) |
| 120 | \(\{(0,1),(1,0),(1,2),(3,3),(4,2)\}\) |

Every reduction and every enumeration loop is finite and explicit in the self-contained verifier, completing the computer-assisted exact proof. The orbit assertion is not an assertion of affine equivalence.

## Verification
Run `python3 verify_binary_cover.py` with Python 3 and no third-party packages. The verifier uses integer residues, Python sets and exhaustive nested loops; it checks the normalized multiset search, an independent complete distinct-subset census, all invertible linear maps, orbit disjointness and completeness, the six-vector cover, and all abelian invariant-factor types through order \(25\). It prints `VERIFY_OK`, maximum \(24\), \(1920\) maximal five-element subsets, orbit-size multiset \([120,120,240,480,480,480]\), and exactly the sole exceptional group type \((25,(5,5))\). These finite enumerations are exact mathematical certificates conditional on running the transparent terminating algorithm; they are not a general theorem for larger group orders.

## Relationship to prior work
Erdős and Rényi, *Probabilistic methods in group theory* (1965), formulate precisely the Boolean subsum covering problem for finite abelian groups and prove an asymptotic probabilistic covering bound; their theorems do not state the exact minimal length or extremal linear-orbit census for the elementary abelian group of order \(25\). Hughes, *Few small primes suffice to cover unit groups* (2026), applies Boolean products to simultaneous covering by small primes, with asymptotic cardinality bounds and a general probabilistic lemma for finite abelian groups. The present theorem isolates a sharp finite obstruction to attaining the elementary counting lower bound; it neither improves Hughes's global theorems nor constructs prime-element covers. Li and Yip's *Generalized additive bases and difference bases for Cartesian product of finite abelian groups* (2025) addresses a different operation, coverage by pairwise sums or differences of a subset, not all \(0\)-\(1\) subset sums. These distinctions are mathematical and not merely terminological.

## Limitations
The key upper bound \(24\) and the orbit counts rely on the complete finite enumeration furnished as executable code. They do not follow from the finite examples alone. The invariant-factor exhaustion concerns only orders at most \(25\). Published literature or unpublished tables may contain an equivalent finite calculation despite the comparisons described; the reported status is an internal mathematical review rather than independent validation.

## References
1. P. Erdős and A. Rényi, *Probabilistic methods in group theory*, Journal d'Analyse Mathématique **14** (1965), 127–138. Open full text: https://users.renyi.hu/~p_erdos/1965-15.pdf.
2. Scott D. Hughes, *Few small primes suffice to cover unit groups*, arXiv:2610.04678v1, initially posted 2026-10-03, https://arxiv.org/abs/2610.04678.
3. Shuxing Li and Chi Hoi Yip, *Generalized additive bases and difference bases for Cartesian product of finite abelian groups*, arXiv:2509.24034v1, initially posted 2025-09-28, https://arxiv.org/abs/2509.24034.
