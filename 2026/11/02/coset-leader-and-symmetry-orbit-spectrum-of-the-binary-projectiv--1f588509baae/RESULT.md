# Coset-leader and symmetry-orbit spectrum of the binary projective-plane code

## Finding

Let \(D=\{0,1,3,9\}\subset\mathbb Z/13\mathbb Z\) be the Singer difference set of the projective plane \(\mathrm{PG}(2,3)\). Index its thirteen points and lines by \(i,j\in\mathbb Z/13\mathbb Z\), with point \(i\) incident with line \(j\) precisely when \(j-i\in D\). Over \(\mathbb F_2\), define the non-incidence matrix
\[
A_{ij}=\begin{cases}0&j-i\in D,\\1&j-i\notin D,\end{cases}
\qquad C=\{(u,uA):u\in\mathbb F_2^{13}\}.
\]
The code \(C\) is the unique self-dual binary \([26,13,6]\) code, up to coordinate permutation, as established in the cited literature. For a coset \(z+C\) let \(d(z+C)=\min_{c\in C}\operatorname{wt}(z+c)\) and let \(m(z+C)\) be the number of codewords attaining that minimum.

**Theorem.** The coset-leader enumerator of \(C\) is
\[
\sum_{z+C} t^{d(z+C)}=1+26t+325t^2+2080t^3+3770t^4+1990t^5.
\]
In particular the covering radius is \(5\). The exact joint distribution of the minimum distance and number of nearest codewords is:

| Coset distance \(d\) | Minimum leaders \(m\) | Number of cosets |
| ---: | ---: | ---: |
| 0 | 1 | 1 |
| 1 | 1 | 26 |
| 2 | 1 | 325 |
| 3 | 1 | 1560 |
| 3 | 2 | 520 |
| 4 | 1 | 468 |
| 4 | 3 | 1404 |
| 4 | 5 | 1898 |
| 5 | 10 | 117 |
| 5 | 18 | 1872 |
| 5 | 26 | 1 |

The induced action of the **full** code automorphism group \(\operatorname{Aut}(C)\cong\operatorname{PGL}(3,3):2\) has exactly \(22\) orbits on the coset space. The numbers of orbits at distances \(0,1,2,3,4,5\) are respectively \(1,1,3,5,7,5\). The five deepest-orbit sizes are \(936,702,234,117,1\); their respective minimum-leader multiplicities are \(18,18,18,10,26\). Every orbit, its size, smallest numerical syndrome representative and minimum-leader multiplicity appear in `ORBIT_TABLE.csv`.

The mean nearest-codeword distance of a uniformly selected ambient binary word is exactly \(15973/4096\). The unique nonzero singleton coset orbit has all-one syndrome and exactly \(26\) minimum leaders of weight \(5\).

## Assumptions and scope

All coordinates, sums, products, and ranks of the code are over \(\mathbb F_2\). The first thirteen coordinates correspond to points \(0,\ldots,12\) and the last thirteen to lines \(0,\ldots,12\). Syndrome integers use little-endian bits in the first thirteen point-index positions: \(s=\sum_{i=0}^{12}s_i2^i\). Orbit representatives are coordinate-label dependent, whereas orbit sizes, coset distances, and leader multiplicities are invariant.

An error of Hamming weight \(d\) is a subset of exactly \(d\) of the \(26\) coordinates. Repeated-coordinate paths are not counted as distinct errors. A coset's distance is the minimum error weight among all its vectors, and its leader multiplicity counts *distinct* minimum-weight errors, equivalently nearest codewords to any vector in that coset.

## Proof

**Code and syndromes.** The difference set \(D\) has four elements and every nonzero cyclic difference occurs precisely once as a difference of two of its elements. Two distinct projective lines therefore meet in one point. Each column of \(A\) has weight \(9\), while distinct columns of \(A\) overlap in exactly \(6\) positions. Consequently \(A^{\mathsf T}A=I\) and, since \(A\) is square, \(AA^{\mathsf T}=I\). Hence \(H=[I_{13}\mid A]\) is both a generator and parity-check matrix for \(C\): its rows are independent, and \(HH^{\mathsf T}=0\). In particular, the syndrome space is precisely \(\mathbb F_2^{13}\), and the \(26\) distinct nonzero one-error syndromes are
\[
\mathcal S=\{e_i:0\le i<13\}\cup\{A_{\cdot j}:0\le j<13\}.
\]
(The code's minimum distance of \(6\) follows from the cited plane-code construction; `verify.py` also independently enumerates the complete \(8192\)-word weight distribution.)

**Shortest error vectors.** Form the Cayley graph on the \(8192\) syndrome states, joining \(s\) to \(s+v\) for each \(v\in\mathcal S\). Starting from \(0\), breadth-first search gives the distance to every state. This is *exactly* the minimum weight of an error having that syndrome, since every error vector is a subset of columns. Define \(p(0)=1\), and at each other state set
\[
p(s)=\sum_{v\in\mathcal S:\,d(s+v)=d(s)-1}p(s+v).
\]
This counts shortest **ordered** paths from \(0\) to \(s\). A shortest path has no repeated coordinate generator, since two occurrences would cancel and yield a shorter path. Therefore every minimum-weight error of weight \(d\) corresponds to exactly \(d!\) shortest paths, and \(m(s)=p(s)/d!\) is an integer. Full exhaustive execution gives the theorem's distance and multiplicity table. As a methodologically independent cross-check, `verify.py` directly enumerates every coordinate subset of sizes \(0,1,2,3,4,5\), xors its corresponding syndrome columns, and confirms all \(8192\) computed distances and multiplicities without using path counts. The maximum enumerated minimum distance is \(5\), establishing the covering radius without extrapolation.

**Full-group orbit decomposition.** Three explicit incidence-preserving point permutations are
\[
T(i)=i+1\pmod{13},\quad U(i)=3i\pmod{13},\quad
P=(0,7,4,10,1,3,6,12,9,8,5,2,11),
\]
where the tuple lists images of \(i=0,\ldots,12\). Each permutes the thirteen columns \(A_{\cdot j}\), as can be checked from the displayed definition of \(A\). Exact closure under composition produces \(5616\) point permutations. Let \(R(e_i)=e_{-i}\) and set \(S(s)=ARs\). Since \(ARA=R\) over \(\mathbb F_2\), this involution exchanges the point and line syndrome columns, specifically \(S(e_i)=A_{\cdot,-i}\) and \(S(A_{\cdot j})=e_{-j}\). It induces a genuine code automorphism exchanging point and line coordinates. The group generated by these permutations and \(S\) has order \(11232\), since it consists of the \(5616\) point-preserving collineations and a disjoint coset interchanging the two coordinate blocks. Höhn's classification gives \(|\operatorname{Aut}(C)|=11232\), so the generated group is the full code automorphism group.

Run orbit closure from each unseen syndrome under these four generators. Every orbit preserves its shortest error distance and leader count, since all generators permute the set \(\mathcal S\). Exactly \(22\) disjoint orbits exhaust the \(8192\) syndromes and have the values in `ORBIT_TABLE.csv`. The row sums reproduce the distance and multiplicity tables, completing the orbit classification.

## Verification

Run `python3 verify.py` with the accompanying `ORBIT_TABLE.csv` in the same directory. Only the Python standard library is needed. The verifier (i) checks the thirteen-line incidence and \(AA^{\mathsf T}=I\) identities, (ii) enumerates all \(8192\) codewords, (iii) calculates syndrome shortest-path distances and path counts, (iv) independently enumerates every error subset of weight at most five, (v) checks the point-permutation closure size \(5616\), the point-line duality, and the \(22\) orbit partition, and (vi) exactly reproduces every cell of the bundled CSV. Successful verification prints `VERIFY_OK` with the enumerated state counts.

This is a finite, exhaustive result for a precisely defined \(8192\)-coset object. No finite experiment is used to infer a claim about an unexamined infinite family. The established unique-code classification transfers all asserted invariants to any equivalent binary self-dual \([26,13,6]\) code.

## Relationship to prior work

Glynn (1991) constructed the plane code and established its complete **codeword weight enumerator** for the order-three plane; that polynomial is independently reproduced here only as a normalization check. Conway, Pless, and Sloane (1992) classified self-dual binary codes through length \(32\). Höhn (June 23, 2026) independently proved uniqueness and the full automorphism group using the projective-plane and odd-Golay descriptions. These sources determine the code and its symmetry group, but the inspected material does not furnish the present exact coset-leader spectrum or the complete \(22\)-orbit syndrome classification.

Conway and Sloane's 1990 orbit/coset study treats the length-\(16\) Reed–Muller/Nordstrom–Robinson/Hamming codes and Golay-related codes of lengths \(22\), \(23\), and \(24\), not this length-\(26\) plane code. In particular, the **length-24** odd-Golay deep-hole cosets appearing in Höhn's construction must not be mistaken for the \(1990\) deep cosets of this **length-26** code. Harada and Munemasa's binary self-dual-code catalogue supplies classifications and generator matrices but not a covering-spectrum table for the distinguished length-\(26\) code. These comparisons identify the added information as the exact nearest-decoding geometry of this specific unique code, rather than any new code construction, uniqueness theorem, or weight enumerator.

## Limitations

The calculation concerns the unique binary self-dual \([26,13,6]\) code. It does not establish a general theorem for all self-dual lengths or a new optimal bound for covering codes. The orbit classification depends on the already-known automorphism-group theorem; the supplied exact checker verifies that the explicit generators realize the same order and computes their action on every syndrome. Published-priority completeness cannot be guaranteed against unindexed or inaccessible prior computations.

## References

1. D. G. Glynn, *The construction of self-dual binary codes from projective planes of odd order*, Australasian Journal of Combinatorics **4** (1991), 277–284. https://ajc.maths.uq.edu.au/pdf/4/ocr-ajc-v4-p277.pdf
2. J. H. Conway, V. Pless and N. J. A. Sloane, *The binary self-dual codes of length up to 32: a revised enumeration*, Journal of Combinatorial Theory, Series A **60** (1992), 183–195. https://neilsloane.com/doc/pless.pdf
3. J. H. Conway and N. J. A. Sloane, *Orbit and coset analysis of the Golay and related codes*, IEEE Transactions on Information Theory **36** (1990), 1038–1050. https://doi.org/10.1109/18.57203
4. G. Höhn, *The unique self-dual binary code of length 26 with minimum weight 6*, arXiv:2606.24573v1, initially posted June 23, 2026. https://arxiv.org/abs/2606.24573
5. M. Harada and A. Munemasa, *Database of Binary Self-Dual Codes*, https://www.math.is.tohoku.ac.jp/~mharada/research/codes/sd2.htm (classification catalogue).
