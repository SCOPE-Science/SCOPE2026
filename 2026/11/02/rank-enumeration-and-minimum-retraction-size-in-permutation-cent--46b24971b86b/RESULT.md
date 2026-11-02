# Rank enumeration and minimum retraction size in permutation-centralizer monoids

## Finding
Fix \(n\ge1\), \(\sigma\in S_n\), and a permutation cycle profile \((m_d)_{d\ge1}\), where \(m_d\) denotes the number of cycles of length \(d\) and \(\sum_d d m_d=n\). Write \(T_n\) for all transformations of the \(n\)-point set and
\[
C(\sigma)=\{f\in T_n:f\sigma=\sigma f\},\qquad
F_\sigma(z)=\sum_{\substack{f\in C(\sigma)\\f^2=f}}z^{|\operatorname{im}f|}.
\]
The complete idempotent image-rank enumerator is
\[
\boxed{F_\sigma(z)=\sum_{0\le k_d\le m_d} z^{\sum_d d k_d}
 \prod_e \binom{m_e}{k_e}\left(\sum_{d\mid e}d k_d\right)^{m_e-k_e}.}\tag{1}
\]
Only finitely many lengths are supported. Set \(0^0=1\); products range over supported lengths \(e\).

Let \(M\) be the set of **divisibility-minimal supported lengths**: \(d\in M\) exactly when \(m_d>0\) and no supported \(e\ne d\) properly divides \(d\). Then the minimum idempotent rank and the exact number at that rank are, respectively,
\[
\boxed{R_{\min}(\sigma)=\sum_{d\in M}d,}\qquad
\boxed{N_{\min}(\sigma)=\prod_{d\in M}m_d d^{m_d-1}\prod_{\substack{e\notin M\\ m_e>0}}
 \left(\sum_{\substack{d\in M\\d\mid e}}d\right)^{m_e}.}\tag{2}
\]
A second, global identity relates this semigroup rank distribution to integer partitions:
\[
\boxed{\frac1{n!}\sum_{\sigma\in S_n}F_\sigma(z)=\sum_{\lambda\vdash n}z^{\ell(\lambda)}.}\tag{3}
\]
Thus the expected number of idempotents in the transformation centralizer of a uniform permutation is the integer partition number \(p(n)\), and the expected number at rank \(r\) equals the number of partitions of \(n\) into exactly \(r\) parts. Equivalently, writing \(z_\lambda=\prod_d d^{m_d}m_d!\), the weighted identity \(\sum_{\lambda\vdash n}F_\lambda(z)/z_\lambda=\sum_{\lambda\vdash n}z^{\ell(\lambda)}\) holds.

## Assumptions and scope
The transformations are **total maps** of a labeled finite set. Composition is ordinary function composition; \(f^2=f\) means idempotence and hence \(f\) fixes every image point. The permutation \(\sigma\) need not act transitively, and its cycle lengths may repeat or be pairwise incomparable by divisibility. The zero-length case is not included. The identity (3) averages over the uniform distribution on labeled permutations, *not* uniformly over conjugacy classes. Formula (2) concerns the minimum nonzero image rank: a total transformation on a nonempty set cannot have empty image.

## Proof
**Cycle mapping.** Let \(O=(x_0,\dots,x_{e-1})\) be a cycle of \(\sigma\). If \(f\sigma=\sigma f\), the image of \(O\) is one entire target cycle \(O'=(y_0,\dots,y_{d-1})\) with \(d\mid e\). After choosing \(f(x_0)=y_j\), equivariance forces \(f(x_i)=y_{i+j\bmod d}\) for every \(i\); this is well-defined precisely when \(d\mid e\). For each prescribed target \(d\)-cycle there are exactly \(d\) choices for the phase \(j\). This basic cycle-divisibility characterization appears in Konieczny [1, Theorem 1].

**Idempotence.** If \(f^2=f\), every point in \(\operatorname{im}f\) is fixed by \(f\). The image is \(\sigma\)-invariant because \(f\) commutes with \(\sigma\). Hence the image is a union of whole \(\sigma\)-cycles, and each selected image cycle is fixed pointwise. Conversely, select any union of cycles, impose the identity on them, and map each unselected source cycle equivariantly into a selected cycle of length dividing its length; the resulting map fixes its image and is idempotent.

**Enumeration.** Suppose exactly \(k_d\) of the \(m_d\) cycles of length \(d\) are selected. There are \(\binom{m_d}{k_d}\) such selections. The image size is \(\sum_d d k_d\). Each of the \(m_e-k_e\) unselected source cycles of length \(e\) may be sent to any selected \(d\)-cycle with \(d\mid e\), with exactly \(d\) phases. There are \(\sum_{d\mid e} d k_d\) allowed maps per unselected \(e\)-cycle, independently across source cycles. Multiplication and summation over selections give (1), including the all-unselected term, which vanishes for \(n\ge1\).

**Minimum rank.** For each supported \(e\) some selected target length \(d\mid e\) must exist; otherwise the source \(e\)-cycles have nowhere to map. In particular, a divisibility-minimal length \(d\in M\) can map only to another \(d\)-cycle, so at least one such cycle must be selected. Every supported \(e\) has a divisibility-minimal supported divisor, so selecting exactly one cycle of each \(d\in M\) yields a valid retraction and attains rank \(\sum_{d\in M}d\). These are the **only** selections of that rank: any additional retained cycle adds a strictly positive length. There are \(m_d\) ways to choose the one fixed \(d\)-cycle; its other \(m_d-1\) cycles each have \(d\) phase choices. Every supported \(e\notin M\) maps to any minimal retained divisor cycle in \(\sum_{d\in M,d\mid e}d\) ways, independently for its \(m_e\) cycles. This proves (2).

**Partition average.** The symmetric group acts on idempotents in \(T_n\) by conjugation. For a given \(\sigma\), its fixed points under this action are precisely the idempotents in \(C(\sigma)\); a fixed idempotent contributes \(z^{\operatorname{rank}(f)}\). A rank-\(r\) idempotent is a partition of the underlying labeled set into exactly \(r\) nonempty fibers, each equipped with one fixed distinguished point (its image point). Two idempotents are conjugate if and only if the multisets of their fiber sizes coincide: a bijection matching blocks of equal size and their distinguished points induces the conjugacy. Hence the conjugacy orbits at rank \(r\) are exactly integer partitions of \(n\) with \(r\) parts. Applying the orbit-counting lemma rank by rank yields (3).

## Verification
A standalone, standard-library Python script `verify.py` independently enumerates all idempotent set maps and tests commutation directly for each permutation cycle type of \(1\le n\le8\), and compares each rank count to (1), the minimum-rank count to (2), and the weighted average to (3). There are 66 cycle-type instances across these dimensions. Its successful terminal output ended with `ALL_VERIFY_OK`; for \(n=8\), the algorithm enumerated 41,393 idempotents for each relevant type. No finite experiment is used as a proof for arbitrary \(n\); the preceding arguments supply that proof.

As an illustrative case, for cycle type \((1,1,2)\) formula (1) yields \(F_\sigma(z)=2z+2z^2+2z^3+z^4\); here \(R_{\min}=1\) and \(N_{\min}=2\).

## Relationship to prior work
Konieczny [1] proves the decisive cycle-divisibility characterization of commuting transformations and studies regular, inverse, and completely regular centralizers, including idempotent examples. The present result assumes that characterization as known; its quantified output is the all-cycle-type rank polynomial, the divisibility-minimal retraction count, and the rank-refined conjugacy/Burnside partition identity, none of which is stated as such in the material inspected in [1]. Araújo and Konieczny [2] study centralizers of arbitrary finite transformations and structural questions, without giving this rank-refined idempotent enumeration in the inspected passages. Mir and Alali [3] study automorphisms of centralizers of restricted-range **idempotents**; their fixed element and their enumeration question are different. This newer semigroup-centralizer perspective motivates the present quantitative study, but does not supply its formula.

## Limitations
This is a self-review, not an independent peer review. An equivalent formula may be implicit in earlier work on morphisms of finite cyclic sets, equivariant retracts, or transformation-semigroup centralizers, and some sources could not be inspected in entirety. The 2024 paper is the date-bounded literature motivation; the cycle-mapping lemma is explicitly credited to older literature. The result concerns a single permutation's commuting transformations; it does not classify the complete semigroup structure of every centralizer or count all nonidempotent elements by rank.

## References
[1] J. Konieczny, *Regular, inverse, and completely regular centralizers of permutations*, Mathematica Bohemica 128 (2003), 179–186. DOI: 10.21136/MB.2003.134038.

[2] J. Araújo and J. Konieczny, *Centralizers in the Full Transformation Semigroup* (2013), full text available at https://repositorioaberto.uab.pt/server/api/core/bitstreams/e1505ef6-df71-4791-a964-cd83058b4fc9/content.

[3] D. J. Mir and A. S. Alali, *On Centralizers of Idempotents with Restricted Range*, Symmetry 16(6), 769 (published 19 June 2024). DOI: 10.3390/sym16060769.
