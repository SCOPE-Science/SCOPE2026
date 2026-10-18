# Sharp eventual injectivity thresholds for one- and two-pass tortoise sorting of period-doubling factors

## Finding

Let \(\mu(0)=01\), \(\mu(1)=00\), and let \(\mathbf p=\mu^\omega(0)\) denote the infinite period-doubling fixed point beginning with zero. For a finite binary word, the **tortoise operation** \(\tau\) moves its first \(1\) to the right end; if there is no \(1\), it fixes the word. For \(k\in\{1,2\}\), put

\[
\rho_k(n)=\bigl|\{\tau^k(u):u\in F_{\mathbf p}(n)\}\bigr|,
\]

where \(F_{\mathbf p}(n)\) denotes all distinct contiguous length-\(n\) factors. The two exact eventual-injectivity thresholds are

\[
\rho_1(n)=|F_{\mathbf p}(n)|\quad(n\ge10),\qquad
\rho_2(n)=|F_{\mathbf p}(n)|\quad(n\ge18).
\]

Both are sharp: the first-pass map is noninjective at length \(9\) and the second-pass map is noninjective at length \(17\). In particular, the following is the **complete complexity profile for all the exceptional lengths and boundary lengths**:

| \(n\) | \(|F_{\mathbf p}(n)|\) | \(\rho_1(n)\) | \(\rho_2(n)\) |
|---:|---:|---:|---:|
|1|2|2|2|
|2|3|2|2|
|3|5|3|3|
|4|6|3|2|
|5|8|5|3|
|6|10|7|4|
|7|11|9|5|
|8|12|10|5|
|9|14|13|7|
|10|16|16|9|
|11|18|18|13|
|12|20|20|16|
|13|21|21|18|
|14|22|22|20|
|15|23|23|21|
|16|24|24|22|
|17|26|26|25|
|18|28|28|28|

## Assumptions and scope

Factors are contiguous and distinct, not occurrence-counted. Lengths are positive integers; the alphabet order is \(0<1\). Here \(\tau^2\) means *two successive applications* of the stated map, not a two-letter block sort or the hare map. The number of passes remains fixed at one or two as the factor length varies. Equality with ordinary factor complexity is equivalent to injectivity of the corresponding image map on the factor set. The theorem covers **every** factor length above the displayed thresholds, not merely factors within a finite prefix.

## Proof

**1. A local-to-global lemma.** Let \(x\) be any infinite binary word, and choose integers \(m\ge k\ge1\). Assume every factor of \(x\) of length \(m\) contains at least \(k\) copies of \(1\), and assume \(\tau^k\) is injective on \(F_x(m)\). Then it is injective on \(F_x(n)\) for every \(n\ge m\).

Indeed, for an eligible word \(u\), \(\tau^k(u)\) deletes its first \(k\) ones (preserving the order of all other symbols), then appends \(k\) ones at the end. Let \(u,v\in F_x(n)\) have equal \(\tau^k\) images. Equality of their first \(m-k\) image symbols means that the length-\(m\) prefixes of \(u,v\), after deleting their first \(k\) ones, yield the same word of length \(m-k\). Adding \(k\) terminal ones proves equality of the \(\tau^k\) images of those two length-\(m\) prefixes. Injectivity at \(m\) makes the prefixes identical. Thus the removed \(k\) ones occupy the same original positions in \(u,v\); equality of the remaining image prefixes and suffixes then gives \(u=v\). This proves the lemma.

**2. An exact finite factor certificate for the entire infinite word.** Let \(W=\mu^7(0)\), which has length \(128\), and define \(E\) to consist of its distinct length-\(18\) windows. There are exactly \(28\) such windows, listed below. A finite direct check proves

\[
\bigcup_{v\in E} F_{\mu(v)}(18)=E.
\]

Every length-\(18\) window of \(\mu(U)\), for a finite input word \(U\) of length at least \(18\), is contained in \(\mu(v)\) for some length-\(18\) window \(v\) of \(U\): its output interval crosses at most ten input symbols and can always be extended to eighteen input symbols. Hence substitution-closure and induction show that every length-\(18\) factor of \(\mu^j(0)\), for \(j\ge7\), lies in \(E\). Conversely \(E\) occurs already in \(W\) and hence in \(\mathbf p\). Therefore \(E=F_{\mathbf p}(18)\) **exactly**, without inferring infinite coverage from a long sampled prefix. Truncating its members gives the complete factor sets for all \(1\le n\le18\).

**3. The finite witnesses and injection checks.** Every member of \(F_{\mathbf p}(10)\) contains at least one \(1\); this set has \(16\) members and its \(16\) \(\tau\)-images are distinct. Every member of \(E\) contains at least two ones; the \(28\) \(\tau^2\)-images of \(E\) are distinct. These four finite assertions follow by exhaustive evaluation of the explicit set \(E\). Apply Step 1 with \((k,m)=(1,10)\) and \((k,m)=(2,18)\) to obtain the claimed assertions for **all** longer factors.

To prove sharpness, both indicated pairs occur among prefixes of \(E\) and have the same image:

```
length 9:  000101010  !=  010001010
           tau(000101010) = tau(010001010) = 000010101
length 17: 00010101000100010  !=  01010001000100010
           tau^2 of each = 00000100010001011
```

The small-length table is computed by taking all length-\(n\) prefixes of \(E\) and counting the distinct \(\tau^k\)-images for \(k=1,2\); equality with the entire infinite factor sets was established in Step 2. This completes the proof.

For completeness, the exact \(28\)-element set \(E\) is:

```
000100010001010100
000100010101000100
000100010101000101
000101010001000100
000101010001010100
001000100010101000
001000101010001000
001000101010001010
001010100010001000
001010100010101000
010001000100010101
010001000101010001
010001010100010001
010001010100010101
010100010001000101
010100010101000100
010100010101000101
010101000100010001
010101000101010001
100010001000101010
100010001010100010
100010101000100010
100010101000101010
101000100010001010
101000101010001000
101000101010001010
101010001000100010
101010001010100010
```

## Verification

The standalone `check.py` constructs \(W\), forms \(E\), checks both inclusions of substitution-closure by explicit set equality, verifies all factor counts and output-image counts, and prints the complete table and collision witnesses. It also computes the period-doubling sequence independently using the digit recurrence \(p(2j)=0\) and \(p(2j+1)=1-p(j)\), comparing its first \(8192\) symbols against the morphic fixed point and its factors against those obtained from \(E\). All checks passed. Run `python3 check.py` in a directory containing the standalone program; the exact output is recorded in `check_output.txt`. The computation certifies the finite premises in Steps 2 and 3; Step 1 and the inductive argument establish the infinite assertion.

## Relationship to prior work

Campbell and Rampersad introduced tortoise-image factor complexity and its iterates, focusing on the paperfolding and Thue–Morse words. Their 2026 full text treats neither the one-pass nor the two-pass tortoise complexity of the period-doubling fixed point. The ordinary factor complexity of the period-doubling sequence is classically studied and does not by itself imply image-map injectivity. The present result applies the same natural invariant to a different classical automatic word, with sharp all-length thresholds for two distinct numbers of passes. General symbolic-dynamics facts about factor languages do not determine the two thresholds; the specific local substitution certificate is essential.

## Limitations

Nothing is claimed about \(\tau^k\) for \(k\ge3\), about other substitutions, or about the classification of all finite words with injective tortoise images. The priority assessment is necessarily limited to the examined primary literature and available research records; an equivalent result under different terminology could exist. Finite computation alone is not an infinite proof; the argument uses exact closure and the proved local-to-global lemma. No independent scientific audit has been performed.

## References

1. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811 (first posted April 28, 2026), https://arxiv.org/abs/2604.25811 ; freely accessible full text at https://arxiv.org/html/2604.25811v2 .
2. M. Poláková, *Complexity and invariant measure of the period-doubling subshift*, arXiv:1902.08387 (2019), https://arxiv.org/abs/1902.08387 .
