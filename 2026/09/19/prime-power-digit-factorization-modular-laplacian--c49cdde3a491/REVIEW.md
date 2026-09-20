# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The central statement reduces to a standard but decisive lifting lemma in a commutative integer algebra: if \(A\equiv B\pmod{p^k}\), then \(A^p\equiv B^p\pmod{p^{k+1}}\). Starting from finite-field Frobenius
\[
P^{p^{n-r+1}}\equiv D_{p^{n-r+1}}(P)\pmod p,
\]
iterating the lifting lemma \(r-1\) times yields
\[
P^{p^n}\equiv D_{p^{n-r+1}}(P^{p^{r-1}})\pmod{p^r}.
\]
The arbitrary-time digit factorization follows by writing the time in base \(p\) above the low block \(0\le t_<<p^{r-1}\) and multiplying the special-time identities. The epoch identity follows because all translation-polynomial operators commute.

The theorem applies to Laurent polynomials, so negative lattice shifts cause no difficulty. It applies to every finite mask and finite-support seed, not only the masks used in the source computations.

The standalone verification artifact checks the identities for von Neumann, diagonal-Neumann, and asymmetric masks, for moduli \(4,8,9\), across special and arbitrary times, and for nontrivial finite seeds. It reports all checks passed. The proof, rather than these finite checks, establishes the theorem.

## Originality

**PASS, with a deliberately narrow source-specific novelty claim.**

The source paper arXiv:2609.20416v1 explicitly derives the prime-modulus recurrence from Frobenius but states that prime-power cases such as \(4,8,9\) are computational observations rather than direct algebraic consequences. Its Section 3.2.2 reports binary-like signatures for \(4,8\) and ternary-like signatures for \(9\).

The author's earlier arXiv:2511.17389v1 is important prior coverage: it develops Frobenius revivals for prime moduli and its Table 1 also records empirical replication ladders for powers of two and three, including \(4,8,9,27\). Accordingly, neither the observation of such ladders nor prime-field Frobenius replication is claimed as new here.

The wider algebraic ingredients are also prior art. Additive cellular automata over finite commutative rings have a substantial literature, including Dow (1997). Prime-power congruence structures for Pascal/binomial coefficients have long been studied, including Bés (1997) and later Lucas-type extensions. The lifting lemma itself is elementary p-adic arithmetic.

The novelty claim is restricted to the explicit application to the source model: the exact formula
\[
P^{p^n}\equiv D_{p^{n-r+1}}(P^{p^{r-1}})\pmod{p^r},
\]
its arbitrary-time base-\(p\) digit factorization, and the resulting all-mask/all-seed epoch identity that turns the source paper's prime-power signatures into rigorous algebraic consequences.

Searches by the source identifier, title, modular-Laplacian terminology, prime-power Frobenius terminology, additive/linear cellular automata over \(\mathbb Z/p^r\mathbb Z\), and polynomial congruence formulations did not locate a public source stating this same source-specific package. The current SCOPE repository was checked by source identifier and claim-family terminology and contained no overlap before publication.

Residual originality risk remains nontrivial because older additive-cellular-automaton literature over finite rings is broad, and not every full text was accessible or exhaustively checked. In particular, Dow (1997) was inspected at the abstract level, not line-by-line full text, and Bés (1997) was inspected through bibliographic/abstract material. Either literature family could contain an equivalent general polynomial identity. This risk is why no broad theorem of first discovery for arbitrary additive cellular automata is claimed.

## Value

**PASS.**

The result resolves a concrete gap highlighted by the source paper itself. Prime powers were separated from prime moduli because the finite-field Frobenius map no longer applies directly, leaving the observed mod-4/mod-8/mod-9 recurrence as computational evidence. The exact lifting formula recovers a rigorous renormalization law and explains why the correct recurrent object is a fixed depth kernel \(P^{p^{r-1}}\).

The arbitrary-time digit factorization is stronger than a sparse sequence of special-time snapshots: it decomposes the complete constant-modulus orbit into scaled copies of one depth kernel organized by the base-\(p\) digits of time. The epoch identity likewise applies to every finite seed and preserves residue values, not merely visual support.

## Limitations

The result is confined to constant-modulus linear dynamics. It does not establish analogous factorization for schedules in which the modulus changes with time, and it does not prove density, entropy, or persistence results for the long-lived carpet regimes that motivate the source paper.

Geometric replica statements require separation of translated supports. The operator identity remains exact when replicas overlap, but modular cancellation can then change visible support.

Chinese remainder decomposition gives exact prime-power projected clocks for composite moduli, but no single full-modulus clock is asserted unless the component scales are compatible.

## Sources inspected

- arXiv:2609.20416v1, accessible full HTML, especially the model definition, algebraic Frobenius background, and Sections 3.2.1–3.2.3 on prime, prime-power, and composite moduli.
- arXiv:2511.17389v1, accessible full HTML, especially its prime-modulus Frobenius derivation and Table 1 reporting empirical ladders for \(2,4,8\) and \(9,27\).
- R. A. Dow (1997), *Additive cellular automata and global injectivity*, accessible abstract describing additive cellular automata over finite commutative rings.
- A. Bés (1997), *On Pascal triangles modulo a prime power*, accessible bibliographic record and abstract describing a prime-power generalization of Lucas' theorem.
- R. Meštrović, arXiv:1301.0251, abstract and metadata for Lucas-type congruences modulo prime powers.
- Current SCOPE repository records and recent changes for overlap by source identifier and equivalent terminology.

**Same-model review: passed. Independent audit: not yet performed.**
