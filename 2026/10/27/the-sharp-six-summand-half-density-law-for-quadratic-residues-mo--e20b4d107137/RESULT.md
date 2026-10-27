# The sharp six-summand half-density law for quadratic residues modulo prime powers

## Finding
For every prime \(p\ge7\), every integer \(a\ge1\), and every subset \(A\) of the invertible quadratic residues modulo \(p^a\), more than half of the available residue classes suffice to represent **every** class as a sum of six members of \(A\):
\[
|A|>\tfrac12|Q(p^a)|\quad\Longrightarrow\quad 6A=\mathbb Z/p^a\mathbb Z.
\]
The number six is sharp uniformly over all such prime powers, already at \(p=7\).

## Assumptions and scope
Here \(p\ge7\) is prime, \(a\ge1\) is an arbitrary integer, \(G=\mathbb Z/p^a\mathbb Z\) is an additive cyclic group, \(Q(p^a)=\{u^2\bmod p^a:p\nmid u\}\), and \(sA\) denotes the set of sums of exactly \(s\) elements of \(A\), with repetition permitted. Since squaring is a two-to-one homomorphism on the units of an odd prime-power ring,
\[
|Q(p^a)|=\frac{(p-1)p^{a-1}}2.
\]
The density hypothesis is strict; no assertion is made at equality. This is a local prime-power theorem, not a claim for general composite moduli, weighted sets, or sums of actual prime squares.

## Proof
Suppose for contradiction that \(6A\ne G\). Let \(H=\{h\in G:h+6A=6A\}\) be its stabilizer, and write \(h=|H|\). Kneser's sumset theorem, applied to six equal summands, gives
\[
|6A|\ge6|A+H|-5h.
\]
Since \(6A\) is a proper union of \(H\)-cosets, \(|6A|\le p^a-h\). Hence
\[
6|A+H|\le p^a+4h.
\]
The cardinality of \(A\) satisfies
\[
|A|>\frac{p-1}{4}p^{a-1},
\]
so, using \(|A+H|\ge|A|\), we deduce
\[
\frac{p-3}{2}p^{a-1}<4h. \tag{1}
\]
Because \(H\) is proper, it is a subgroup of the cyclic prime-power group \(G\) with \(h\le p^{a-1}\). For \(p\ge11\), inequality (1) implies \(h>p^{a-1}\), a contradiction.

It remains to consider \(p=7\). Inequality (1) gives \(h>\tfrac12 7^{a-1}\). The order of any subgroup is a power of seven, so the only possible proper stabilizer has \(h=7^{a-1}\). Thus \(H\) is the kernel of reduction \(G\to\mathbb F_7\). As \(|A|>\tfrac32 7^{a-1}\), its reduction \(\bar A\) contains at least two distinct classes \(r,s\). But sums of six elements drawn from \(\{r,s\}\) give
\[
6r+j(s-r),\qquad j=0,1,\ldots,6,
\]
which are all seven elements of \(\mathbb F_7\). Therefore \(6\bar A=\mathbb F_7\). Since \(6A\) is \(H\)-periodic, it follows that \(6A=G\), another contradiction. This proves the covering statement for all \(p,a,A\).

For sharpness, take \(p=7\), \(a=1\), and \(A=\{1,2\}\subset Q(7)=\{1,2,4\}\). The strict majority condition holds because \(|A|=2>3/2\). However,
\[
5A=\{5,6,0,1,2,3\}\ne\mathbb F_7,
\]
while six copies of the two-element set give all seven residues. Hence no uniform bound below six is possible. \(\square\)

## Verification
The proof is valid for every exponent and does not rest on computation. The included standalone `verify.py` exhaustively checks all smallest qualifying subsets for \(p=7,11,13,17,19\), samples qualifying subsets for moduli \(7^2,7^3,11^2,13^2\) using a fixed seed, and tests the sharpness witness at modulus seven. Run `python3 verify.py`. These finite checks supplement but do not establish the infinite assertion.

## Relationship to prior work
Lacey, Mousavi, Rahimi and Vempati [1, Theorem 1.7] prove a general half-density covering theorem for reduced squares with **ten** summands when the modulus is coprime to thirty. Their more precise Section 4, Lemmas 4.2 and 4.6, permits six summands only at the stronger density threshold \(5/6\), not the half-density threshold considered here. The sharp bound above treats every prime power with \(p\ge7\), including the small prime \(p=7\), by a direct stabilizer argument. Lim [2, Theorem 1.1] proves sharp covering bounds over cyclic groups whose prime divisors are all sufficiently large (depending on the density and summand count), and thus does not supply the uniform small-prime boundary. The two results are different in hypotheses and quantifiers, not simply terminology.

## Limitations
The optimal value is **uniform** in the prime and exponent, not a claim that the minimal order for each individual prime power equals six. In particular, many larger primes permit fewer than six summands. The theorem does not cover moduli divisible by two, three, or five, nor products of distinct primes, nor weighted or mixed summand sets. Novelty has been checked against the named sources and relevant indexed statements but unrecognized older coverage is possible. Independent mathematical review has not been performed.

## References
[1] M. T. Lacey, H. Mousavi, Y. Rahimi and M. N. Vempati, *Density Bounds in Hua’s Theorem for Prime Squares*, arXiv:2610.22747v1, first public 2026-10-15, Sections 1 and 4. https://arxiv.org/html/2610.22747v1

[2] Z. L. Lim, *On the density version of quadratic Waring's problem and the quadratic Waring–Goldbach problem*, arXiv:2508.14939v1, first public 2025-08-20, Theorem 1.1. https://arxiv.org/abs/2508.14939

[3] M. Kneser, the classical sumset-stabilizer theorem for finite abelian groups (six-fold form applied in the proof).
