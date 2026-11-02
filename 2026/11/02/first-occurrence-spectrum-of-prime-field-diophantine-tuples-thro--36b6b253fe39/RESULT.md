# First-occurrence spectrum of prime-field Diophantine tuples through size twelve

## Finding

For an odd prime \(p\), let \(M(p)\) be the greatest cardinality of a subset \(A\subseteq\mathbb F_p^*\) such that \(ab+1\) is a square in \(\mathbb F_p\), **including zero**, for every two distinct \(a,b\in A\). For \(m\ge2\), let \(P(m)\) be the least odd prime \(p\) for which \(M(p)\ge m\).

The **exact first-occurrence spectrum** is

\[
\bigl(P(2),P(3),\ldots,P(12)\bigr)
=(3,7,11,23,37,59,83,131,181,251,353).
\]

In particular, \(353\) is the smallest odd prime admitting a twelve-element Diophantine tuple, and \(M(353)=12\). An explicit twelve-element witness is

\[
\{54,62,69,107,130,178,188,213,280,323,325,347\}\subset\mathbb F_{353}^*.
\]

## Assumptions and scope

The assertion concerns **prime fields**, not general prime-power fields. Each tuple consists of distinct nonzero residues. The value zero is admitted as a square when testing \(ab+1\). The first-occurrence function \(P(m)\) records the *first* prime field containing such a tuple; it does **not** assert that all larger primes admit one. The claim covers exactly \(2\le m\le12\), not arbitrary sizes.

## Proof

For each odd prime \(p\), make a finite simple graph \(G_p\) on vertices \(1,2,\ldots,p-1\). Join distinct vertices \(a,b\) exactly when \((ab+1)\bmod p\) belongs to

\[
R_p=\{x^2\bmod p:0\le x<p\}.
\]

By definition, the desired subsets are precisely cliques of \(G_p\), so \(M(p)=\omega(G_p)\). A standard prime sieve lists **all seventy odd primes** from \(3\) through \(353\) inclusive. The accompanying standalone `verify.py` computes the clique number of each of these seventy graphs by an exact branch-and-bound recursion, with the full seventy-row output `SPECTRUM.csv`. Here is a proof of the recursion's **exhaustiveness**, not an inference from numerical sampling.

At a recursion node, a chosen clique \(C\) is paired with a bitset \(U\) of vertices adjacent to every vertex of \(C\). Greedy coloring repeatedly forms an independent color class from the remaining vertices. Let the resulting order be \(v_1,\ldots,v_t\), with each vertex's associated color-class index \(c_j\). Since each color class is independent, the prefix \(v_1,\ldots,v_j\) has a proper coloring with at most \(c_j\) colors and hence contains no clique larger than \(c_j\). The recursion processes vertices in reverse order. When considering \(v_j\), the remaining candidate pool is precisely that prefix. Its branch chooses \(v_j\) and recurses on vertices in the pool adjacent to \(v_j\), then removes \(v_j\); together the branches partition all possible extensions. A branch is pruned only if \(|C|+c_j\) does not exceed the size of an **already found clique**. This is a valid upper bound and cannot discard an improvement. At each chosen vertex, the best-known clique is updated. Induction on \(|U|\) shows that the returned size is exactly \(\omega(G_p)\), including all boundary cases.

The certificate lists \(M(p)\) for every prime \(p\le353\). Taking the first \(p\) with \(M(p)\ge m\) gives precisely the eleven values displayed above. In particular, all earlier odd prime fields have \(M(p)\le11\), whereas \(M(353)=12\); thus no smaller prime field contains a twelve-tuple, and no thirteen-tuple exists in \(\mathbb F_{353}\). The displayed witness is also verified directly against all sixty-six unordered pairs in `verify.py`.

## Verification

Run `python3 verify.py` from the folder containing `verify.py` and `SPECTRUM.csv` (Python 3 standard library only). It recalculates all seventy exact clique numbers, checks every explicit witness, verifies the claimed first-prime spectrum, and overwrites `SPECTRUM.csv` with its canonical deterministic output. The output is identical to the included table, whose SHA-256 is `16c12abf37901cb41a7515e6c6408f210092250527e0de9e89429139224e4bec`. Ten of the record-size primes were separately checked with maximal-clique enumeration, yielding the same clique numbers; that cross-check is supplementary rather than part of the finite proof.

## Relationship to prior work

Dujella and Kazalicki [2] formulated finite-field Diophantine tuples, enumerated pairs, triples, and quadruples, and gave a general sufficient lower bound on the field size for existence. Hammonds and coauthors [3] generalized to higher-order product conditions and listed small examples of **three-factor** tuples, not the first-prime spectrum of the present **pairwise** condition. Shparlinski [4] improved asymptotic tuple counts. Kim, Yip, and Yoo [1] studied and improved explicit constructions and the growth of the maximum cardinality \(M(q)\). None of the exact values above follows from those asymptotic or one-sided general estimates. The numerical claim is the finite first-occurrence spectrum; it does not assert a new character-sum estimate or a general formula for \(P(m)\).

## Limitations

The proof is an exhaustive finite computation under an elementary, proved search invariant. It is not a noncomputational formula or an infinite-prime theorem, and its exactness depends on faithfully executing the included transparent integer-arithmetic algorithm. The classification is restricted to prime fields and the stated eleven sizes. An unindexed prior list of the same thresholds could exist. The classical first few values are not individually claimed as novel.

## References

1. S. Kim, C. H. Yip, S. Yoo, *Explicit constructions of Diophantine tuples over finite fields*, arXiv:2404.05514v1 (first public 8 April 2024); *Ramanujan Journal* 65 (2024), 163–172, DOI:10.1007/s11139-024-00888-5.
2. A. Dujella, M. Kazalicki, *Diophantine m-tuples in finite fields and modular forms*, arXiv:1609.09356; *Research in Number Theory* 7 (2021), article 3, DOI:10.1007/s40993-020-00232-y.
3. T. Hammonds et al., *k-Diophantine m-tuples in finite fields*, arXiv:2201.06232; *International Journal of Number Theory* 19 (2023), 891–912.
4. I. E. Shparlinski, *On the number of Diophantine m-tuples in finite fields*, arXiv:2301.04063; *Finite Fields and Their Applications* 90 (2023), 102241.
