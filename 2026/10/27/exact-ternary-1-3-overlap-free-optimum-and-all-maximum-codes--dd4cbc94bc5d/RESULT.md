# Exact ternary \((1,3)\)-overlap-free optimum and all maximum codes

## Finding
For every integer \(n\geq 6\), a maximum-size ternary length-\(n\) code with no prefix–suffix overlap of lengths \(1\), \(2\), or \(3\), including a codeword with itself, has exactly
\[
A_3(n;1,3)=72\,3^{n-6}
\]
words. There are exactly **42 distinct labelled maximum codes** on the fixed alphabet \(\{0,1,2\}\) at each such length. Under simultaneous permutation of the three alphabet symbols and reversal of every word, these codes form **four orbits**, of sizes \(6,12,12,12\). Their prefix/suffix three-block cardinality profiles are exactly: \((6,12)\) for six codes, \((8,9)\) for fifteen, \((9,8)\) for fifteen, and \((12,6)\) for six.

## Assumptions and scope
Write \(\Sigma=\{0,1,2\}\). For a word \(w\), write \(\operatorname{pre}_t(w)\) and \(\operatorname{suf}_t(w)\) for its length-\(t\) prefix and suffix. A code \(C\subseteq\Sigma^n\) is \((1,3)\)-overlap-free when
\[
\operatorname{pre}_t(u)\ne\operatorname{suf}_t(v)
\quad\text{for every }u,v\in C\text{ and }t\in\{1,2,3\}.
\]
The quantifier permits \(u=v\). Only overlaps of these three lengths are forbidden; longer prefix–suffix coincidences are permitted. The assertion concerns every \(n\geq6\), with distinct codebooks treated as different subsets of the **labelled** alphabet. A *maximum* code has the largest cardinality, not merely the property that it cannot be enlarged.

For \(p,s\in\Sigma^3\), put \(p\sim s\) when their prefixes and suffixes agree at any of the three forbidden lengths, and define
\[
B(p)=\{s\in\Sigma^3:\exists t\in\{1,2,3\},\ \operatorname{pre}_t(p)=\operatorname{suf}_t(s)\},
\quad S(P)=\Sigma^3\setminus\bigcup_{p\in P}B(p).
\]
For every \(P\subseteq\Sigma^3\), write \(\mathcal C_n(P)=P\,\Sigma^{n-6}\,S(P)\); juxtaposition is word concatenation, and \(\Sigma^0\) consists of the empty word.

## Proof
**Reduction without loss.** For any admissible \(C\), let \(P\) be the set of its length-three prefixes and let \(S\) be the set of its length-three suffixes. Since every pair of codewords must pass the overlap test, \(S\subseteq S(P)\). Each ordered prefix, middle block, suffix triple determines at most one word. Therefore
\[
|C|\le |P|\,|S(P)|\,3^{n-6}.
\]
Conversely, the complete Cartesian-product code \(\mathcal C_n(P)\) is admissible: every comparison of forbidden-length prefixes and suffixes is already excluded by \(S(P)\). Hence
\[
A_3(n;1,3)=3^{n-6}\max_{P\subseteq\Sigma^3}|P|\,|S(P)|.
\]
This reduction is a known general feature of restricted-overlap codes; the exact ternary optimization and classification are the claims here.

**Finite exact optimum and equality cases.** Index the \(27\) triples by \(i=9a+3b+c\) for \(a,b,c\in\{0,1,2\}\). For each index \(i\), encode \(B(p_i)\) as a 27-bit mask \(b_i\). Enumerating every 27-bit selection mask \(m\), compute
\[
f(m)=\operatorname{popcount}(m)\left(27-\operatorname{popcount}\left(\bigvee_{i:\,m_i=1}b_i\right)\right).
\]
The attached standalone C++17 verifier enumerates **all \(2^{27}=134{,}217{,}728\)** masks using an unpruned recursion and independently using a Gray-code sweep with incremental suffix-coverage multiplicities. These methods yield precisely
\[
\max_m f(m)=72,\qquad |\{m:f(m)=72\}|=42.
\]
The 42 equality masks have cardinality profiles \((|P|,|S(P)|)\) occurring with respective multiplicities
\[
(6,12):6,\quad (8,9):15,\quad (9,8):15,\quad (12,6):6.
\]
These counts are finite exact exhaustive computations, not a statistical sample or an inference from bounded word lengths. The complete source code implements the test and supplies an executable enumeration certificate.

To attain \(|C|=72\,3^{n-6}\), the inequalities above must be equalities. Thus \(P\) must be one of the 42 maximizing masks and \(C=\mathcal C_n(P)\): every compatible suffix and every middle word must occur. Different \(P\) give different codes because \(S(P)\) is nonempty and every \(p\in P\) occurs. Therefore the number 42 holds for **all** \(n\geq6\), not only for \(n=6\).

**Orbit classification.** A global alphabet permutation acts on both \(P\) and \(S(P)\) coordinatewise; global word reversal maps \((P,S(P))\) to \((\operatorname{rev}(S(P)),\operatorname{rev}(P))\). These operations preserve the optimum and generate a group of order 12. The verifier explicitly applies its six alphabet permutations and reversal to every maximizing pair and obtains four orbits of sizes \(6,12,12,12\). One representative \((P,S(P))\) from each orbit is given below; three-digit strings denote triples rather than integers:

| Orbit size | \(P\) | \(S(P)\) |
| ---: | --- | --- |
| 12 | `111 112 120 121 122 201 202 211 212 220 221 222` | `000 010 100 110 200 210` |
| 12 | `200 201 202 210 212 220 221 222` | `000 001 010 011 100 101 110 111 211` |
| 12 | `000 001 002 010 011 020 021 022` | `012 111 112 121 122 211 212 221 222` |
| 6 | `200 201 202 210 211 212 220 221 222` | `000 001 010 011 100 101 110 111` |

These four representatives and the stated transformations determine all 42 maximum codes at every permissible length.

**Existence without enumeration.** Choose all nine length-three prefixes beginning with `0` and all eight length-three suffixes with every symbol in `1,2`. The first and last symbols of any such codeword are different, so no forbidden overlap occurs. The resulting size is \(9\cdot8\cdot3^{n-6}=72\,3^{n-6}\), providing a simple independent lower-bound witness. The standalone verifier checks each of the \(72^2\) ordered length-six pairs against all three overlap lengths.

## Verification
In a POSIX shell with a C++17 compiler, save the adjacent file `verify_overlap.cpp` and run:

```sh
c++ -O3 -std=c++17 verify_overlap.cpp -o verify_overlap
./verify_overlap
```

The verified expected success line is:

```text
OVERLAP_Q3_K3_PASS maximum=72 maximum_codes=42 symmetry_orbits=6+12+12+12 exhaustive_prefix_families=134217728 profiles=(6,12):6,(8,9):15,(9,8):15,(12,6):6
```

The checker implements the literal prefix/suffix comparisons, the independent recursion and Gray-code census, the 72-word witness, all maximizing cardinality profiles and symmetry orbits. The all-length statement is deduced mathematically from the prefix–middle–suffix factorization; no infinite claim is inferred from finite data alone.

## Relationship to prior work
Blackburn, Esfahani, Kreher and Stinson introduced or analyzed the restricted-overlap prefix/suffix framework, general cardinality bounds and binary constructions; the reduction to a finite prefix/suffix compatibility problem is not asserted to be novel [1]. Cai, Wang and Feng considered \(q\)-ary \((1,k)\)-overlap-free codes and constructions, with their abstract emphasizing exact maxima for \(k=2\); a complete text comparison could not be made [2]. Stanovnik develops further constructions, expandability and bounds for restricted overlaps [3]. Yang and Ding give \(q\)-ary constructions and tabulate sizes of **their constructed families**, not an unrestricted maximum-code census [4]. In particular, their construction with \(q=3\), \(|I|=2\), \(|J|=1\), and prefix parameter 3 gives a code of size \(72\,3^{n-6}\); **that construction and lower bound are prior work**. The new assertion is that no larger code exists and that the entire set of maximum codebooks consists of exactly 42 members in the four orbits above.

## Limitations
The result is specific to a three-symbol alphabet, the forbidden overlap lengths \(1,2,3\), and \(n\geq6\). It gives no claim for shorter words, larger alphabets, or other forbidden-length intervals. The exact finite extremal calculation depends on complete execution of the supplied standalone checker, rather than a closed-form purely handwritten inequality. The accessible published material does not rule out every unindexed equivalent formulation. The full text of [2] was unavailable during comparison, although its abstract and descriptions in [4] were examined. Independent mathematical audit has not been performed.

## References
[1] S. R. Blackburn, N. Nasr Esfahani, D. L. Kreher and D. R. Stinson, *Constructions and Bounds for Codes with Restricted Overlaps*, arXiv:2211.10309, first posted 2022-11-18, https://arxiv.org/html/2211.10309v4.

[2] Y. Cai, Z. Wang and X. Feng, *Constructions and Bounds for q-Ary (1,k)-Overlap-Free Codes*, IEEE Transactions on Information Theory, DOI:10.1109/TIT.2023.3319010.

[3] N. Stanovnik, *Codes with Restricted Overlaps: Expandability, Constructions, and Bounds*, arXiv:2411.02899, https://link.springer.com/article/10.1007/s12190-025-02441-z.

[4] H. Yang and Y. Ding, *Q-Ary (t1,t2)-Overlap-Free Codes*, IEICE Transactions on Fundamentals, 2026, DOI:10.1587/transfun.2025EAL2050, https://globals.ieice.org/en_transactions/fundamentals/10.1587/transfun.2025EAL2050/_f.
