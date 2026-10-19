# Finite cyclic-factor orbit spectra for dyadic Rudin–Shapiro lengths

## Finding
For the infinite binary Rudin–Shapiro word \(r\), let \(\mathcal F_n(r)\) denote the set of its distinct length-\(n\) contiguous factors. Group those factors by cyclic rotation, counting only distinct factors of \(r\) actually present in each rotation class. For every \(n=2^k\) with integer \(4\le k\le13\), there are exactly \(4n-12\) rotation classes represented by one factor, exactly two represented by two factors, and exactly four represented by all \(n\) rotations. Hence
\[
 |\mathcal F_n(r)|=8n-8,\qquad c_r(n)=4n-6.
\]
These are certified **finite-range identities** for ten substitution-aligned lengths, not a theorem for arbitrary \(k\).

## Assumptions and scope
Take the uniform morphism \(\varphi\) on \(\{0,1,2,3\}\) given by \(\varphi(0)=01\), \(\varphi(1)=02\), \(\varphi(2)=31\), \(\varphi(3)=32\). Its fixed point beginning in state \(0\) is projected by \(\tau(0)=\tau(1)=0\), \(\tau(2)=\tau(3)=1\). This is the binary Rudin–Shapiro sequence, equivalently \(r_i\) is the parity of the number of overlapping occurrences of \(11\) in the binary expansion of \(i\). A cyclic rotation class means conjugacy under \(uv\sim vu\) among finite words; the multiplicity recorded here is the number of *distinct occurring factors* within that ambient necklace, not the number of positional occurrences or the size of its stabilizer.

## Proof
**Factor exhaustivity.** The length-two factors of the four-state fixed point are precisely
\[
 S=\{01,02,10,13,20,23,31,32\}.
\]
Each occurs in \(\varphi^8(0)\). Applying \(\varphi\) to every pair in \(S\) produces only consecutive pairs in \(S\); checking the eight images verifies closure, so there are no other pairs anywhere in the fixed point. For \(n=2^k\), the fixed point is a concatenation of length-\(n\) blocks \(\varphi^k(a)\). Every length-\(n\) factor lies inside one or two consecutive blocks, and every adjacent block pair corresponds to a pair in \(S\). Therefore the exact factor set is
\[
 \mathcal F_n(r)=\bigcup_{ab\in S}\{\operatorname{factor}_n(\tau(\varphi^k(a)\varphi^k(b)),j):0\le j\le n\},
\]
where \(\operatorname{factor}_n(w,j)\) takes \(n\) symbols starting at zero-based offset \(j\). Inclusion both ways holds because all state pairs in \(S\) actually occur.

**Finite exhaustive evaluation.** The accompanying complete source `verify.cpp` constructs each of those eight block concatenations for \(4\le k\le13\), inserts all \(n+1\) windows into an exact string set, and groups the resulting distinct strings by their lexicographically least cyclic rotations (Booth's algorithm). A map stores how many distinct factors belong to each canonical necklace. The verifier asserts for every listed \(n\) that the map's only nonzero multiplicities are \(1,2,n\), occurring respectively \(4n-12,2,4\) times. This proves the ten finite claims by complete enumeration, without inferential extrapolation from smaller lengths.

## Verification
Compile and execute the included source using `c++ -O2 -std=c++17 verify.cpp -o verify && ./verify`; successful execution ends in `VERIFY_OK`. It verifies pair exhaustivity and closure, compares the first \(2^{14}\) projected symbols to the independently defined bit-parity formula, independently extracts direct factors for \(n\le64\), and checks least-rotation canonicalization against a brute-force algorithm for \(n\le32\). All assertions ran successfully. The program prints one row per \(n\): length, factor count, class count, number of singleton classes, number of two-factor classes, and number of full-rotation classes.

## Relationship to prior work
Cassaigne, Fici, Sciortino and Zamboni introduced cyclic factor complexity and investigated Sturmian, Toeplitz/period-doubling and Thue–Morse words [1]. Krawchuk and Rampersad studied Fibonacci and Thue–Morse cyclic complexities [2]. The statements and proofs inspected in these articles do not present the exact Rudin–Shapiro dyadic factor-necklace multiplicity census above. Cyclic-factor equivalence is stronger than equality of symbol-count (abelian) profiles, so an abelian-complexity enumeration does not itself determine this spectrum. A complete factor complexity count also does not determine how factors group into cyclic classes.

## Limitations
The asserted equalities cover only the ten lengths \(16,32,64,128,256,512,1024,2048,4096,8192\). The observed linear formulas are **not** claimed for larger powers of two or arbitrary lengths. Correctness is conditional on ordinary exact string and integer operations and on the correctness of the supplied, reproducible finite enumerator; no external formal proof assistant or independent audit is claimed. The literature comparison cannot rule out an unindexed earlier Rudin–Shapiro cyclic-factor calculation.

## References
1. J. Cassaigne, G. Fici, M. Sciortino, L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843 (first public version 2014-02-24), https://arxiv.org/abs/1402.5843.
2. C. Krawchuk, N. Rampersad, *Cyclic Complexity of Some Infinite Words and Generalizations*, INTEGERS **18A** (2018), A12, https://math.colgate.edu/~integers/sjs12/sjs12.pdf.
