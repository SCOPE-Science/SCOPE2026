# Exact three-tap convolution nullities on the binary icosahedral group

## Finding

Let \(G=\operatorname{SL}(2,\mathbb F_5)\), the binary icosahedral group of order \(120\). For every three-element subset \(S\subset G\), the complex nullity of its unweighted left convolution operator
\[
(T_S f)(h)=\sum_{s\in S}f(s^{-1}h),\qquad f:G\to\mathbb C,
\]
is determined **solely** by the sorted multiset of orders of the three quotients \(s^{-1}t\) for unordered pairs \(\{s,t\}\subset S\). Every attainable quotient-order signature, its nullity, and its support count are listed below. The list is exhaustive.

| Pairwise quotient orders | Complex nullity | Number of supports |
|---|---:|---:|
| \((2,3,6)\) | 0 | 2,400 |
| \((2,4,4)\) | 0 | 1,800 |
| \((2,5,10)\) | 0 | 2,880 |
| \((3,3,3)\) | 80 | 400 |
| \((3,3,4)\) | 0 | 7,200 |
| \((3,3,6)\) | 10 | 7,200 |
| \((3,3,10)\) | 0 | 7,200 |
| \((3,4,4)\) | 20 | 7,200 |
| \((3,4,5)\) | 0 | 14,400 |
| \((3,4,6)\) | 0 | 14,400 |
| \((3,4,10)\) | 0 | 14,400 |
| \((3,5,5)\) | 4 | 7,200 |
| \((3,5,6)\) | 0 | 14,400 |
| \((3,5,10)\) | 10 | 14,400 |
| \((3,6,6)\) | 40 | 1,200 |
| \((3,10,10)\) | 4 | 7,200 |
| \((4,4,4)\) | 0 | 2,400 |
| \((4,4,5)\) | 0 | 14,400 |
| \((4,4,6)\) | 20 | 7,200 |
| \((4,4,10)\) | 0 | 14,400 |
| \((4,5,5)\) | 5 | 7,200 |
| \((4,5,6)\) | 0 | 14,400 |
| \((4,5,10)\) | 5 | 14,400 |
| \((4,6,6)\) | 0 | 7,200 |
| \((4,6,10)\) | 0 | 14,400 |
| \((4,10,10)\) | 5 | 7,200 |
| \((5,5,5)\) | 0 | 1,440 |
| \((5,5,6)\) | 10 | 7,200 |
| \((5,5,10)\) | 4 | 7,200 |
| \((5,6,10)\) | 4 | 14,400 |
| \((5,10,10)\) | 0 | 4,320 |
| \((6,6,6)\) | 30 | 2,400 |
| \((6,6,10)\) | 0 | 7,200 |
| \((6,10,10)\) | 22 | 7,200 |
| \((10,10,10)\) | 4 | 2,400 |

Aggregated over all \(\binom{120}{3}=280{,}840\) supports, the nullities \(0,4,5,10,20,22,30,40,80\) occur respectively \(159{,}240\), \(38{,}400\), \(28{,}800\), \(28{,}800\), \(14{,}400\), \(7{,}200\), \(2{,}400\), \(1{,}200\), and \(400\) times. Thus exactly \(121{,}600\) supports are singular. The sharp maximum nullity is \(80\), attained precisely for left cosets of cyclic order-three subgroups. In particular, the order signature \((6,10,10)\) has the distinctive nullity \(22\).

## Assumptions and scope

The support is an **unordered set of exactly three distinct group elements**; all three convolution coefficients equal \(1\). Complex functions are considered on the entire finite group, not a proper quotient. The group is represented without rounding as the \(120\) determinant-one matrices over \(\mathbb F_5\). The quotient order is the group-theoretic order; because an element and its inverse have the same order, the sorted three-term signature is well defined. The statement does not concern symmetric or loop-free undirected Cayley graphs exclusively: identity elements in supports and directed sums are allowed.

## Proof

**Finite group and normalization.** Enumerate all quadruples \((a,b,c,d)\in\{0,1,2,3,4\}^4\) for which \(ad-bc\equiv1\pmod5\). With the usual matrix multiplication modulo five they form \(G\), of order \(120\). If \(S=\{u,v,w\}\), then left multiplying all its elements by \(u^{-1}\) replaces it with \(\{1,u^{-1}v,u^{-1}w\}\). Since \(T_{gS}=L_g T_S\), where \(L_g f(h)=f(g^{-1}h)\), this preserves rank. Simultaneous conjugation also preserves rank, since it induces conjugation by a permutation of the regular representation. Consequently all supports reduce to the \(\binom{119}{2}=7{,}021\) unordered normalized pairs \(\{x,y\}\subset G\setminus\{1\}\), modulo simultaneous conjugation and the three choices of normalizing basepoint.

**Orbit reduction.** For each normalized pair, apply each of the three basepoint changes to \(\{1,x,y\}\), then conjugate the two nonidentity elements by every matrix in \(G\). The attached checker constructs these finite orbits explicitly, verifies their disjointness, and verifies that all \(7{,}021\) pairs belong to exactly \(62\) orbits. The quotient-order signature, which is constant on each orbit, assumes exactly \(35\) values. The same checker verifies that every orbit having a fixed signature has the same complex nullity, as proved in the next step.

**Exact rank certificate.** For a normalized support \(\{1,x,y\}\), form its \(120\times120\) integer regular-convolution matrix \(A\), indexed by \(h,k\in G\), with \(A_{h,k}=1\) exactly when \(k=h\), \(k=x^{-1}h\), or \(k=y^{-1}h\), and zero otherwise. These are three distinct positions in each row. The checker computes the row rank of one representative per orbit by finite-field elimination modulo four explicitly verified primes
\[
1{,}000{,}000{,}007,\quad1{,}000{,}000{,}009,\quad998{,}244{,}353,\quad1{,}004{,}535{,}809.
\]
The four resulting ranks agree within each orbit. Let their common rank be \(r\). Every \(k\times k\) minor of \(A\), for \(k\le120\), has absolute determinant at most \(3^{k/2}\le3^{60}\), by Hadamard's inequality, because every row has at most three ones. The product of the four primes is
\[
Q=1{,}002{,}772{,}214{,}764{,}891{,}819{,}703{,}233{,}751{,}393{,}804{,}351
>3^{60}=42{,}391{,}158{,}275{,}216{,}203{,}514{,}294{,}433{,}201.
\]
Every \((r+1)\times(r+1)\) integer minor vanishes modulo all four primes, hence is divisible by \(Q\), so the absolute bound forces it to be zero. Conversely at least one \(r\times r\) minor is nonzero modulo each prime and hence nonzero as an integer. The integer matrix therefore has rank **exactly** \(r\) over \(\mathbb Q\) and \(\mathbb C\). This certifies each orbit nullity without assuming that modular ranks generally equal characteristic-zero ranks.

**Support multiplicities and extremum.** Every original support has exactly three distinguished basepoints, while each normalized support has \(120\) left translates, so an orbit containing \(m\) normalized pairs represents exactly \(40m\) three-element supports. Summing these numbers over the orbit representatives with the same signature produces the table. The enumerated distribution sums to \(280{,}840\). There are exactly \(20\) order-three elements, giving \(10\) order-three subgroups and \(40\) left cosets of each, hence \(400\) order-three cosets. Every such coset has order signature \((3,3,3)\). The table shows that this signature has exactly \(400\) supports, all of nullity \(80\), and no other signature has nullity \(80\), proving the sharp characterization.

## Verification

The standalone \(\texttt{check.cpp}\) included with this result constructs the group, enumerates and checks the \(62\) normalization/conjugacy orbits, performs exact modular Gaussian elimination, proves the modular-to-integer rank transfer via its large-modulus Hadamard bound, and checks all \(35\) signature rows and the complete nullity census. Compile with \(\texttt{g++ -O2 -std=c++17 check.cpp -o check}\) and execute \(\texttt{./check}\). A successful run prints the orbit count, prime-product and determinant bounds, the complete table, and the nine-level nullity distribution. The supplied program was compiled and executed successfully using GNU C++ 14.2.0. Neither floating-point tests nor an assumed modular-rank heuristic enter the proof.

## Relationship to prior work

Dechant's geometric-algebra construction describes the icosian realization of the binary icosahedral group, providing one natural geometric interpretation of the group studied here [1]. Arezoomand and Taeri derive general representation-theoretic spectral decompositions for Cayley digraphs [2], while Siemons and Zalesski study singular Cayley graphs under conjugacy-invariant, inverse-closed connection-set hypotheses [3]. Those general methods do not themselves supply this arbitrary three-point support classification or its exact rank census. The present theorem computes an invariant for all unweighted triples, including nonnormal directed supports, and exhibits the exceptional \(22\)-dimensional nullity stratum. The binary central extension must be treated separately from its rotational quotient: the order-signature law and nine nullity levels are not direct restatements of the quotient's support-rank table.

## Limitations

The theorem makes no assertion about nonunit coefficients, four or more taps, other finite groups, or independently certified publication priority. The calculation is a finite, exhaustive, exact-arithmetic proof for this group; it does not by itself establish a general theorem for arbitrary binary polyhedral groups. Potential implicit earlier classifications in historical group-algebra or Cayley-spectrum tables remain an originality risk. The checker is an explicit computational component of the mathematical proof, not a proof of novelty.

## References

[1] P.-P. Dechant, *Clifford algebra unveils a surprising geometric significance of quaternionic root systems of Coxeter groups*, arXiv:1205.1451 (first version 7 May 2012), especially Definition 3.4. https://arxiv.org/pdf/1205.1451

[2] M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of n-Cayley Digraphs*, Electronic Journal of Combinatorics 20(3), #P57 (2013). https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p57/pdf/

[3] J. Siemons and A. Zalesski, *Remarks on singular Cayley graphs and vanishing elements of simple groups*, arXiv:1804.01204 (first version 4 April 2018); Journal of Algebraic Combinatorics 50 (2019), 379–401. https://arxiv.org/pdf/1804.01204
