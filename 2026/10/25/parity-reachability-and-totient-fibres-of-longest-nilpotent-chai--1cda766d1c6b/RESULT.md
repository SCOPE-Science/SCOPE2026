# Parity reachability and totient fibres of longest nilpotent chains in orientation-preserving partial permutation monoids

## Finding

For every integer \(n\ge3\), let \(\mathcal{POPI}_n\) denote the monoid of all injective orientation-preserving partial maps of the chain \([n]=\{1,\ldots,n\}\). For a nilpotent map \(f\), let \(\nu(f)\) be the smallest positive integer with \(f^{\nu(f)}=0\). Consider precisely those maps of rank \(n-1\) with \(\nu(f)=n\), the maximal possible nilpotency index.

Write \(a\) for the unique missing domain point and \(b\) for the unique missing image point; these are respectively the terminal and initial points of the directed chain. Write \(d\) for the representative of \(b-a\pmod n\) in \(\{0,\ldots,n-1\}\).

**Theorem.** A maximal-index nilpotent map with endpoint pair \((a,b)\) exists exactly when \(a\ne b\) and either \(n\) is odd or \(d\) is odd. The number of attainable ordered pairs is \(n(n-1)\) for odd \(n\) and \(n^2/2\) for even \(n\). When \(b\) is either cyclic neighbor of \(a\), exactly \(\varphi(n-1)\) such maps realize that pair. Hence exactly \(2n\varphi(n-1)\) have neighboring endpoints.

## Assumptions and scope

An injective partial map \(f\) on \([n]\) is orientation-preserving if, listing its domain increasingly, the resulting injective image word has at most one *cyclic descent*, including the comparison from its last letter back to its first. For nonempty words of length at least two, this is equivalent to being a cyclic shift of the increasing image list. The empty map is zero. All endpoint arithmetic is modulo \(n\); the circular order is the standard order on \([n]\) with its ends joined. We may replace labels by residues \(0,\ldots,n-1\) without affecting the assertions.

An injective partial map of rank \(n-1\) has \(n-1\) arrows, a unique missing source position \(a\), and a unique missing target position \(b\). It is nilpotent if and only if it has no directed cycle. A directed graph with indegree and outdegree at most one, \(n-1\) arrows, and no cycles is exactly one directed path through all \(n\) points. Its index is \(n\). In particular \(a\ne b\) is necessary.

## Proof

**Normal form.** Circular shifts of all point labels preserve the definition of orientation and the graph of the map. Rotate so the missing domain point is \(a=n-1\) in residue notation, and let \(m=n-1\). For \(b\in\{0,\ldots,n-2\}\), every orientation-preserving bijection from \(D=\{0,\ldots,n-2\}\) onto \(I=\{0,\ldots,n-1\}\setminus\{b\}\) is uniquely obtained by an index shift \(t\in\{0,\ldots,m-1\}\) between the increasing lists. Extend it to a permutation \(\pi_t\) of all \(n\) points by assigning \(\pi_t(n-1)=b\). Its partial restriction has a spanning directed chain exactly when \(\pi_t\) is an \(n\)-cycle.

Let \(C=(0\ 1\ \cdots\ n-2)\), fixing \(n-1\). With the convention that rightmost permutations act first, we have
\[
\pi_t=\pi_0 C^t,\qquad \pi_0=(b\ b+1\ \cdots\ n-1),
\]
where \(\pi_0\) fixes every point smaller than \(b\).

**Parity obstruction.** If \(n\) is even, \(C\) is even, whereas \(\operatorname{sgn}(\pi_0)=(-1)^{n-b-1}=(-1)^{b+1}\). An \(n\)-cycle has sign \(-1\), so we need \(b\) even. Since after rotation \(d=b+1\), this is precisely odd \(d\). There is no parity obstruction when \(n\) is odd.

**Sharpness.** Whenever \(b\) and \(n\) have the same parity, choose \(t=1\). For \(b\ge1\), the orbit of \(0\) under \(\pi_1\) is explicitly
\[
0,1,\ldots,b-1,b+1,b+3,\ldots,n-1,b,b+2,\ldots,n-2,0.
\]
Each displayed progression is interpreted with step two; their union is all points and there are no repetitions before returning to zero. This is an \(n\)-cycle. If \(b=0\), the required equal parity forces \(n\) even and the orbit is
\[
0,2,4,\ldots,n-2,1,3,5,\ldots,n-1,0,
\]
again an \(n\)-cycle. For even \(n\), odd \(d\) gives even \(b\), so these constructions cover every permitted pair. For odd \(n\), they cover all *even* nonzero \(d\). Reflect the common domain-and-image circle, reversing the order of labels: conjugation by this reflection preserves orientation-preservation (both circular orders reverse), preserves the chain property, and sends offset \(d\) to \(n-d\). When \(n\) is odd, this sends any odd \(d\) to an even one, completing all pairs.

**Exact neighboring-endpoint fibre.** By circular rotation it is enough to take \(a=n-1\) and \(b=0\), so \(\pi_0=(0\ 1\ \cdots\ n-1)\). The relation \(\pi_t=\pi_0 C^t\) implies that \(n-1\mapsto0\), while every other vertex maps into \(\{1,\ldots,n-1\}\). Contract the arrow entering and leaving vertex \(0\) in \(\pi_t\). The resulting permutation of \(\{1,\ldots,m\}\) is precisely the cyclic translation by \(t+1\) modulo \(m\). Contracting a vertex of a permutation preserves the number of disjoint cycles; thus \(\pi_t\) is an \(n\)-cycle precisely if \(\gcd(t+1,m)=1\). There are exactly \(\varphi(m)=\varphi(n-1)\) permitted values of \(t\). Reflection gives the same fibre for the other cyclic neighbor. Since \(n\ge3\), the two neighbors of every point are distinct. There are \(2n\) such ordered pairs, proving the last count.

Counting the admissible offsets gives \(n(n-1)\) pairs when \(n\) is odd; when \(n\) is even, each of the \(n\) choices of \(a\) has \(n/2\) allowed odd offsets, giving \(n^2/2\). This proves the theorem.

## Verification

The reproducible program `verify.py` independently generates all directed Hamiltonian paths for every \(3\le n\le9\), filters them by cyclic-order preservation, verifies all endpoint-existence conditions and the exact neighboring-pair \(\varphi(n-1)\) fibres. It separately implements and checks constructive maps for every \(3\le n\le35\), and tests the permitted but nonprimitive offset \(d=3\) at \(n=6\). The expected final line is `VERIFY_OK`. Finite tests corroborate, but do not replace, the general permutation proof.

## Relationship to prior work

Fernandes, Jesus and Singha give foundational structure and the standard cyclic-image-word definition for orientation-preserving partial permutations. Li and Fernandes characterize endomorphisms of oriented transformation semigroups, including this monoid. Their inspected full texts treat respectively structural/Green relations and endomorphism classifications, rather than the boundary-parity classification of spanning nilpotent chains and adjacent-endpoint fibres. Li and Fernandes also study restricted-range submonoids, a different restriction from prescribing the two omitted endpoints.

There is a narrower cyclic inverse monoid consisting of restrictions of whole-set rotations. Its longest-chain maps require a primitive global rotation step, hence the boundary offset must be coprime to \(n\); the present result permits all odd offsets when \(n\) is even, including the nonprimitive offset \(3\) when \(n=6\). Thus the stated endpoint theorem is not a corollary of that narrower family. The existing maximal-index count for that family is not claimed here.

## Limitations

This result classifies *attainability* of all ordered endpoint pairs but provides exact fibre sizes only for neighboring endpoint pairs; the other attainable fibres are not enumerated. The theorem concerns injective orientation-preserving partial transformations, not the larger noninjective monoid or orientation-reversing maps. An earlier relevant article on orientation-preserving partial one-to-one transformations could only be evaluated from publicly accessible bibliographic/abstract material, leaving a residual originality risk. The literature comparison does not certify exhaustive priority. No independent audit has been performed.

## References

1. V. H. Fernandes, M. M. Jesus, B. Singha, *On orientation-preserving transformations of a chain*, arXiv:1806.08440 (initial submission 21 June 2018), especially definitions and results on partial injections; https://arxiv.org/html/1806.08440v2.
2. D. B. Li, V. H. Fernandes, *Endomorphisms of semigroups of oriented transformations*, arXiv:2207.12823v1 (26 July 2022); https://arxiv.org/html/2207.12823v1.
3. D. B. Li, V. H. Fernandes, *On semigroups of orientation-preserving partial permutations with restricted range*, arXiv:2401.02185v1 (4 January 2024); https://arxiv.org/html/2401.02185v1.
4. V. H. Fernandes, *On the monoid of all orientation-preserving partial one-to-one transformations on a finite chain*, Communications in Algebra, DOI:10.1080/00927870008827033 (bibliographic/abstract material accessible; full text not verified).
