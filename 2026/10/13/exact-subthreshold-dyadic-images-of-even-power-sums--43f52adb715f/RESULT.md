# Exact subthreshold dyadic images of even-power sums

## Finding
For each even integer \(k\ge 6\), put \(s=\nu_2(k)\), \(h=s+2\), and \(q=2^h\). For every integer \(1\le t<q\) and every \(a\ge1\), define
\[
A_{k,t}(a)=\left\{\sum_{i=1}^{t}x_i^k\bmod 2^a:x_i\in\mathbb Z\right\},\qquad F_{k,t}(a)=|A_{k,t}(a)|.
\]
Zero summands are allowed. Set \(A_{k,t}(0)=\{0\}\) and \(F_{k,t}(0)=1\), interpreting the zero ring as \(\mathbb Z/1\mathbb Z\). For every \(a>h\), there is an exact disjoint decomposition
\[
A_{k,t}(a)=\left(\bigsqcup_{r=1}^{t}\{y\bmod 2^a:y\equiv r\pmod q\}\right)\;\sqcup\; 2^k A_{k,t}(\max(a-k,0)),
\]
where the final term is \(\{0\}\) when \(a\le k\). The cardinality at every modulus is therefore
\[
F_{k,t}(a)=
\begin{cases}
\min(2^a,t+1),&1\le a\le h,\\
t2^{a-h}+1,&h<a\le k,\\
t2^{a-h}+F_{k,t}(a-k),&a>k.
\end{cases}
\]
This provides an exact finite recursive algorithm requiring only elementary integer operations; the recursion descends by \(k\).

There is also a complete description over the \(2\)-adic integers. Set \(\mathcal S_{k,t}=\{\sum_{i=1}^t x_i^k:x_i\in\mathbb Z_2\}\). A nonzero \(y\in\mathbb Z_2\), with \(v=\nu_2(y)\) and \(j=\lfloor v/k\rfloor\), lies in \(\mathcal S_{k,t}\) if and only if
\[
\frac{y}{2^{kj}}\bmod q\ \in\{1,2,\ldots,t\}.
\]
The point \(0\) always belongs. The normalized additive Haar measure, the exact counting discrepancy, and the topological boundary are
\[
\mu(\mathcal S_{k,t})=\lambda_{k,t}:=\frac{t}{q(1-2^{-k})}=\frac{t2^{k-h}}{2^k-1}<1,
\]
\[
F_{k,t}(a+k)-\lambda_{k,t}2^{a+k}=F_{k,t}(a)-\lambda_{k,t}2^a\qquad(a\ge1),
\]
\[
\partial\mathcal S_{k,t}=\{0\}.
\]
Thus the count differs from its limiting density times \(2^a\) by an **exactly \(k\)-periodic bounded discrepancy** (a period dividing \(k\) is not excluded).

For example, the residues representable by 31 eighth powers have limiting \(2\)-adic proportion \(248/255\), so their complementary proportion is \(7/255\). The already-known critical count of 32 eighth powers fills all \(2\)-adic residues; the new formula instead describes every subcritical count exactly.

## Assumptions and scope
The exponent \(k\) is any even integer at least 6, not necessarily a power of two. Its valuation \(s\) is at least 1, and \(k>s+2=h\). The summand count ranges through every integer \(t\) with \(1\le t<2^{s+2}\). The residue modulus is every \(2^a\) for \(a\ge1\). The \(2\)-adic statement uses the usual compact ring \(\mathbb Z_2\), its normalized additive Haar measure, and the ambient topology. No assertion is made for odd exponents, the fourth-power endpoint, the saturated range \(t\ge q\), or odd-prime moduli.

## Proof
**Odd-power image lemma.** For every \(a>h\), the \(k\)-th powers of odd residues modulo \(2^a\) are exactly the subgroup \(1+2^h\mathbb Z/2^a\mathbb Z\). For \(a\le h\), every odd \(k\)-th power is \(1\bmod 2^a\). Indeed, for \(a\ge3\) the odd unit group is \(\{\pm1\}\times\langle5\rangle\), with the order of \(5\) equal to \(2^{a-2}\). As \(k\) is even, its powers of \(\pm1\) are all 1. The standard lifting-the-exponent identity gives \(\nu_2(5^k-1)=\nu_2(k)+2=h\). Consequently \(5^k\) generates the subgroup of odd units congruent to \(1\bmod2^h\) for every \(a>h\); for smaller \(a\), every such power is 1. Passing through the compatible finite quotient groups gives the same surjectivity in \(\mathbb Z_2\).

**Disjoint decomposition.** Every even \(x\) has \(x^k=2^k u^k\) for some integer \(u\). Since \(k>h\), such powers vanish modulo \(q\), whereas every odd \(k\)-th power equals 1 modulo \(q\). In a sum of \(t<q\) powers, let \(r\) be the number of odd summands. Then \(0\le r\le t\) and the sum is congruent to \(r\) modulo \(q\). If \(r=0\), all summands are even, producing exactly the scaled image \(2^kA_{k,t}(\max(a-k,0))\); when \(a\le k\), that scaled image is zero. If \(r\ge1\), the image is contained in the class \(r+q\mathbb Z/2^a\mathbb Z\). Conversely, every member of this class is obtained using \(r-1\) summands equal to 1, a single odd \(k\)-th power varying freely over \(1+q\mathbb Z/2^a\mathbb Z\), and the remaining \(t-r\) summands equal to zero. Distinct values of \(r\) give distinct nonzero classes modulo \(q\), disjoint from the all-even branch. This proves the claimed decomposition for all \(a>h\).

**Exact counts.** For \(a\le h\), every power is either 0 or 1, and all sums of 0 through \(t\) ones occur, giving \(\min(2^a,t+1)\) residues. For \(h<a\le k\), the \(t\) full cosets modulo \(q\) each have \(2^{a-h}\) elements, together with zero. For \(a>k\), the scaling map \(z\mapsto2^kz\bmod2^a\) is injective on \(\mathbb Z/2^{a-k}\mathbb Z\), so the all-even branch contributes exactly \(F_{k,t}(a-k)\) elements. Summing the disjoint sizes proves the three cases.

**The \(2\)-adic set.** Applying the odd-power image lemma in \(\mathbb Z_2\) gives
\[
\mathcal S_{k,t}=\left(\bigsqcup_{r=1}^{t}(r+q\mathbb Z_2)\right)\sqcup 2^k\mathcal S_{k,t}.
\]
Iterating shows that the only point that can remain in the scaled branch indefinitely is 0. Consequently
\[
\mathcal S_{k,t}=\{0\}\cup\bigsqcup_{j\ge0}\bigsqcup_{r=1}^{t}2^{kj}(r+q\mathbb Z_2).
\]
Every nonzero element of the \(j\)-th layer has valuation in \([kj,kj+h-1]\), a range disjoint from all other layers because \(h<k\). Thus \(j=\lfloor\nu_2(y)/k\rfloor\) is forced, proving the stated membership test. The outer cosets have total measure \(t/q\); multiplication by \(2^k\) scales Haar measure by \(2^{-k}\). The disjoint fixed-point equation gives the displayed \(\lambda_{k,t}\). The strict bound follows from \(t\le q-1\) and \(k>h\). Subtracting \(\lambda_{k,t}2^a\) from the cardinality recurrence yields the exact discrepancy identity. The set \(\mathcal S_{k,t}\) is compact, hence closed. Every nonzero point of it lies in one of the displayed open cosets, so it is interior. The missing points \(2^{kj+h}\), for \(j\ge0\), tend to 0 and cannot lie in any displayed layer (their valuation modulo \(k\) equals \(h\)). Hence 0 is in the boundary and no other point is, proving \(\partial\mathcal S_{k,t}=\{0\}\).

## Verification
A standalone Python 3 checker (`verify.py`) directly enumerates the \(k\)-th power residues, constructs their \(t\)-fold modular sumsets, and compares complete sets with the recursively predicted images. It performed 452 exact set and cardinality comparisons for exponents \(6,8,10,12,14,16,20,24,32\), multiple subthreshold summand counts, and moduli from \(2\) through \(2^{12}\). The exact checker output is `verification_output.txt`. The finite tests are not a proof of the statements for unbounded parameters; the group-theoretic and disjoint-union proof above supplies that generality.

## Relationship to prior work
The counting problem is motivated by Arias, Borja, and Anaya's 2023 study of polynomial images modulo prime powers (particularly its Section 7), which gives specific fourth-power sum image counts and general recurrences but not the complete subthreshold formula here for every even \(k\ge6\). Subocz's 1999 Lemma 3.1 identifies the subgroup of odd \(k\)-th powers and his Theorem 3.2 determines the **minimum** number of summands needed for surjectivity at dyadic moduli. Those are important prerequisites and are not claimed as new. The present result instead explicitly classifies **every proper subthreshold image**, its exact cardinality at each power of two, its bounded periodic discrepancy, and its \(2\)-adic topology and measure. General image-counting frameworks of Arias–Borja–Rubio (2019) and lifting bounds for diagonal congruences (Alnaser and collaborators, 2008 and 2020) were also considered.

## Limitations
The theorem does not count how many distinct tuples represent each attainable residue, address other moduli or exponent parities, or improve the already-known dyadic Waring threshold. Much of its structure builds on Subocz's description of odd-power residue groups and existing prime-power image recurrences. A potentially equivalent older formula may be unindexed or implicit in those methods. The checker exercises only finite examples; no independent mathematical audit has been performed.

## References
1. F. Arias, J. Borja, and S. Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences **26** (2023), Article 23.8.1, first published 2023-08-28. https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.pdf
2. J. Subocz, *A Note on Waring's Number Modulo \(2^n\)*, Divulgaciones Matemáticas **7** (1999), 13–18, especially Lemma 3.1 and Theorem 3.2. https://eudml.org/doc/48795
3. F. Arias, J. Borja, and L. Rubio, *Counting Integers Representable as Images of Polynomials Modulo n*, Journal of Integer Sequences **22** (2019), Article 19.6.7. https://cs.uwaterloo.ca/journals/JIS/VOL22/Borja/borja3.pdf
4. A. Alnaser and T. Cochrane, *Waring's Number Mod m*, Journal of Number Theory **128** (2008), 2582–2590. https://www.math.ksu.edu/~cochrane/research/waringmodm.pdf
5. A. Alnaser, T. Cochrane, M. Ostergaard, and C. Spencer, *Waring Numbers for Diagonal Congruences*, Rocky Mountain Journal of Mathematics **50** (2020), 825–838. https://www.math.ksu.edu/~cvs/alnaser_cochrane_ostergaard_spencer-diagonal_cong.pdf
