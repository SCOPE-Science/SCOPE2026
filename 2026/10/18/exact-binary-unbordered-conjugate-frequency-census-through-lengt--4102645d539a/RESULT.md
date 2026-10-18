# Exact binary unbordered-conjugate frequency census through length \(28\)

## Finding

For every integer \(1\le n\le28\) and every integer \(0\le j\le n\), the accompanying `histogram_1_to_28.csv` gives the exact integer
\[
H(n,j)=\#\{w\in\{0,1\}^n:\operatorname{nuc}(w)=j\},
\]
where \(\operatorname{nuc}(w)\) counts starting positions whose length-\(n\) cyclic rotation of \(w\) is **unbordered**. An unbordered word has no nonempty proper prefix equal to its suffix. Rotations are counted by starting position, not deduplicated, although all rotations of every primitive word are distinct and nonprimitive words have no unbordered rotations.

In particular, at \(n=28\), the nonzero entries \((j,H(28,j))\) are
\[
\begin{gathered}
(0,16396),\ (2,31444),\ (3,335832),\ (4,3182172),\\
(5,15137360),\ (6,42528920),\ (7,71898064),\\
(8,73564148),\ (9,44033696),\ (10,14906752),\\
(11,2581824),\ (12,213808),\ (13,5040).
\end{gathered}
\]
All omitted entries are zero; in particular \(H(n,1)=0\) for every \(2\le n\le28\) (whereas \(H(1,1)=2\)). For uniformly random \(W\in\{0,1\}^{28}\), the table yields exact mean and variance
\[
\mathbb{E}[\operatorname{nuc}(W)]={62901909\over8388608},\qquad
\operatorname{Var}(\operatorname{nuc}(W))={131772345343303\over70368744177664}.
\]
Every row is fully enumerated, not estimated. The largest observed count at length \(28\) is \(13\), attained by \(5040\) labeled words. These numerical findings do **not** assert an unrestricted-length variance formula or a new maximum theorem.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), with words labeled by their linear start and fixed length \(n\). The conclusion covers all \(2^n\) words separately at every \(1\le n\le28\). The reported histogram rows include zero for out-of-range indices \(j>n\), and the complete CSV lists columns \(h_0,\ldots,h_{28}\). We use the standard finite-word notion of (proper, nonempty) border, and cyclic rotations preserve labels in the enumerative count.

## Proof

The finite claim is certified by an exhaustive, symmetry-reduced integer enumeration with an explicit complete generator and count-preserving orbit weights, supplied as `unbordered_necklaces.cpp`.

First, the binary Fredricksen–Kessler–Maiorana recursion starts with \(a_0=0\), extends a prefix by repeating the entry of period \(p\), and branches to a strictly larger next symbol while setting the new period to the current position. At completed depth \(n\), it emits precisely the binary necklaces when \(p\mid n\), once each, in lexicographically least-rotation order. Each emitted representative has primitive-root length \(p\); the corresponding rotation orbit consists of exactly \(p\) labeled words. This is the usual FKM necklace theorem, with all branch bounds implemented explicitly in `unbordered_necklaces.cpp`.

Second, when \(p<n\), the word is a proper power. Each rotation remains a proper power and hence has a nonempty proper border, so its entire orbit contributes \(p\) to \(H(n,0)\). When \(p=n\), the representative is primitive and has \(n\) distinct rotations. For each start position \(s=0,\ldots,n-1\), check each border length \(b=1,\ldots,\lfloor n/2\rfloor\): a border exists iff the length-\(b\) prefix equals the length-\(b\) suffix of that cyclic rotation. These checks are exhaustive: any border longer than half the word overlaps itself, forcing a strictly shorter positive border. The exact rotation count \(j\) is invariant across an orbit, so that necklace contributes exactly \(n\) to \(H(n,j)\). Because necklace orbits partition \(\{0,1\}^n\), summing these weights is **exactly** \(H(n,j)\). Integer counters do not overflow for \(n\le28\), since the sum of every row is \(2^n\le2^{28}\).

Third, the stated CSV is the verbatim decimal output of the supplied exhaustive necklace program run through \(n=28\), transposed into fixed-width CSV columns. The independent brute-force program `unbordered_allwords.cpp` tests all \(2^n\) labeled words by a separate bit-rotation-and-mask border test and agrees for **every entry** through \(n=25\). The two programs use different enumeration orders and different border implementations. Additional arithmetic identities verify every row through \(n=28\) as recorded below. The mean and variance are obtained from integer sums \(\sum_jjH(28,j)\) and \(\sum_jj^2H(28,j)\), divided by \(2^{28}\), with exact rational reduction.

## Verification

A C++17 compiler is sufficient. From the directory containing the files, run:

```sh
g++ -O3 -std=c++17 unbordered_necklaces.cpp -o necklaces
./necklaces 28 > orbit_table.txt
g++ -O3 -std=c++17 unbordered_allwords.cpp -o allwords
./allwords 25 > direct_table.txt
python3 verify_histogram.py histogram_1_to_28.csv orbit_table.txt direct_table.txt
```

The verifier checks the complete CSV against all \(28\) orbit-enumeration rows, against all \(25\) independent direct-enumeration rows, and against three separate mathematical invariants for all \(28\) rows: \(\sum_jH(n,j)=2^n\); \(H(n,0)\) equals the number of nonprimitive binary words, by Möbius inversion over proper periods; and \(\sum_j jH(n,j)=n u_2(n)\), where \(u_2(n)\) is the number of unbordered binary words. The zero-count identity also follows because every primitive word of length at least two has both a lexicographically least and greatest cyclic conjugate, each unbordered (and the length-one case is direct). The first-moment identity uses the classical recurrence \(u_2(1)=2\), \(u_2(2m+1)=2u_2(2m)\), \(u_2(2m)=2u_2(2m-1)-u_2(m)\). All checks pass with exact integers.

## Relationship to prior work

Clokie, Gabrić and Shallit (2019, arXiv:1904.08187, Sections 3–5) determine attainable unbordered-conjugate counts, their maximum, and the **first moment** \(\mathbb{E}[\operatorname{nuc}]\). Those results constrain the support and the mean of this table but do not supply its full fiber-cardinality distribution or finite variance. Harju and Nowotka (2004, 2008) study the binary border-correlation images and realizability; their image characterization does not count the numbers of labeled words in each image fiber. Holub and Müller (2015, arXiv:1504.02222) classify fully bordered words and pairs of unbordered conjugates, rather than the entire frequency census. Rivals and Wang (2024, arXiv:2405.09393) count self/cross-overlap correlation populations of **pairs** of strings; this is not a distribution of cyclic conjugate border indicators of single words. The present statement is a finite, multivariate refinement of the previously known maximum/mean assertions, not a restatement of either.

## Limitations

The exact exhaustive result stops at \(n=28\). No formula for arbitrary length, higher-order asymptotic, uniqueness assertion about computational discovery, or count above this cutoff is claimed. Direct independent word-by-word enumeration stops at \(n=25\); the remaining three rows have the complete necklace enumeration and independent aggregate identities, but not an independently rerun full word-by-word enumeration. An unlocated published table or a stronger equivalence of a border-correlation result could cover some entries. The 2004 original paper was not fully accessible for comparison; its described objects and the directly readable 2019 and 2008 accounts were compared without treating access difficulty as positive novelty evidence.

## References

1. Trevor Clokie, Daniel Gabrić, Jeffrey Shallit, *Circularly squarefree words and unbordered conjugates: a new approach*, arXiv:1904.08187, first public 2019-04-17. https://arxiv.org/abs/1904.08187
2. Tero Harju and Dirk Nowotka, *Border correlation of binary words*, Journal of Combinatorial Theory, Series A **108** (2004), 331–341, doi:10.1016/j.jcta.2004.07.009.
3. Tero Harju and Dirk Nowotka, *Bordered conjugates of words over large alphabets*, Electronic Journal of Combinatorics **15** (2008), #N41. https://doi.org/10.37236/916
4. Štěpán Holub and Martin Müller, *Fully Bordered Words*, arXiv:1504.02222 (2015). https://arxiv.org/abs/1504.02222
5. Eric Rivals and Pengfei Wang, *Counting overlapping pairs of strings*, arXiv:2405.09393 (2024). https://arxiv.org/abs/2405.09393
6. Frank Ruskey, *Combinatorial Generation*, necklace generation (FKM recursion), manuscript. https://page.math.tu-berlin.de/~felsner/SemWS17-18/Ruskey-Comb-Gen.pdf
