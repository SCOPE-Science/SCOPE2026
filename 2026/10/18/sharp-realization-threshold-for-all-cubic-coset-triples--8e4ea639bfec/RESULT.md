# Sharp realization threshold for all cubic-coset triples

## Finding
For a prime \(p\equiv1\pmod3\), let \(g\) be any primitive root of \(\mathbb F_p^\times\), and define \(c_p(g^a)=a\bmod3\), taking values in \(\{0,1,2\}\). The definition is unambiguous because \(3\mid p-1\). Let
\[
\mathcal W_p=\{(c_p(x),c_p(x+1),c_p(x+2)):1\le x\le p-3\}.
\]
**Theorem.** For every prime \(p\equiv1\pmod3\),
\[
\mathcal W_p=\{0,1,2\}^3\quad\Longleftrightarrow\quad p\ge307.
\]
Equivalently, the only such primes at which one or more cubic-coset words of length three are absent are
\[
7,13,19,31,37,43,61,67,79,127,151,163,283.
\]
At \(p=283\) the only absent word is \((0,0,0)\). At each of \(p=151,163\), the word \((0,0,0)\) occurs but precisely one mixed word is missing. With \(g\) chosen as the least positive primitive root, the missing word is \((2,0,2)\), which becomes \((1,0,1)\) on interchanging the two nonzero coset labels.

## Assumptions and scope
The prime \(p\) ranges over all rational primes congruent to \(1\) modulo \(3\). Each \(x\) is an ordinary integer between \(1\) and \(p-3\), inclusive, so all three entries are nonzero modulo \(p\). The nonzero cubic-residue subgroup is label \(0\); labels \(1\) and \(2\) distinguish its other multiplicative cosets. Changing the primitive root may interchange labels \(1\) and \(2\), but it never alters the assertion that all \(27\) words occur, the number of missing words, or the exceptional-prime set.

## Proof
Fix such a prime \(p\), write \(\zeta=e^{2\pi i/3}\), and take the order-three multiplicative character \(\chi\) satisfying \(\chi(g)=\zeta\); extend nontrivial characters by \(\chi(0)=0\). For a prescribed word \(\mathbf e=(e_0,e_1,e_2)\), let \(N_p(\mathbf e)\) count the corresponding integers \(x\) in the stated range. Character orthogonality gives, on that range,
\[
27 N_p(\mathbf e)=\sum_{x=1}^{p-3}\ \sum_{\mathbf a\in\{0,1,2\}^3}
\zeta^{-\sum_{j=0}^2a_je_j}\prod_{j=0}^2\chi(x+j)^{a_j},
\]
where factors with exponent zero are interpreted as \(1\), including at zero (although zeros do not occur in this range).

The zero exponent vector contributes \(p-3\). For a nonzero exponent vector \(\mathbf a\), put \(t=|\{j:a_j\ne0\}|\) and
\[
P_{\mathbf a}(X)=\prod_{j:a_j\ne0}(X+j)^{a_j}.
\]
This polynomial has exactly \(t\) distinct roots and is not a perfect cube. The standard Weil bound for nontrivial multiplicative character sums therefore gives
\[
\left|\sum_{x\in\mathbb F_p}\chi(P_{\mathbf a}(x))\right|
\le(t-1)\sqrt p
\]
when \(t\ge2\). For \(t=1\), the complete sum is identically \(0\), since \(\chi\) or \(\chi^2\) is nontrivial on \(\mathbb F_p^\times\). Removing the three forbidden arguments \(x=0,-1,-2\) can change a complete sum by at most \(3-t\), since \(t\) of those arguments are roots of \(P_{\mathbf a}\) and yield zero contributions. There are \(\binom3t2^t\) vectors with support of size \(t\). Thus, by the triangle inequality,
\[
27N_p(\mathbf e)\ge p-3-
(12+16)\sqrt p-(6\cdot2+12\cdot1)
=p-28\sqrt p-27.
\]
For every real \(p\ge900\), \(p-28\sqrt p-27\ge33>0\) (the expression increases for \(p>196\)). Hence every word occurs for every admissible prime \(p\ge900\).

The remaining primes are exhausted by `verify.py`: sieve all primes \(p<900\), select those \(p\equiv1\pmod3\), obtain a primitive root by testing its order against every prime divisor of \(p-1\), construct the exact cubic-coset lookup table, and examine all \(x\) from \(1\) through \(p-3\). A second construction independently forms the cubic-residue subgroup and its two cosets, then compares the results modulo interchange of labels \(1,2\). This exhausts \(74\) primes and gives precisely the thirteen exceptional primes listed above. In particular, \(p=283\) lacks \((0,0,0)\), while \(p=307\) has all \(27\) words. The large-prime argument and finite exhaustive certificate together establish the theorem for every eligible prime. \(\square\)

## Verification
Run `python3 verify.py` in the directory containing this document. The program uses only Python standard-library integer arithmetic and reports `VERIFY_OK`, the complete exceptional-prime list, and checks at primes \(151,163,283,307\). The sieve covers every prime below \(900\), the coset arrays cover all nonzero residues, and the tested \(x\)-interval is exhaustive. The infinite portion relies on the standard, explicit Weil bound as stated in the proof; a finite run is not used to extrapolate beyond its cutoff.

## Relationship to prior work
Lehmer, Lehmer, Mills, and Selfridge (1962), Theorem 1(a), already determine the primes with **no three consecutive cubic residues**, that is, the single word \((0,0,0)\). Their exact exceptional set omits \(151\) and \(163\), which are obstructions for *other* words. Their theorem also already places the last all-residue obstruction at \(283\); that earlier single-word result is not claimed as new. Rabung and Jordan (1970) study consecutive entries lying in the **same** power-residue class, not all ordered mixed-class words. Dietzel (first public preprint 28 September 2013) proves a bounded first **pair** of power residues, not the simultaneous realization of all ternary words of length three. Hu and Chen (2020) count cubic-residue conditions on \(a\pm a^{-1}\), not triples \((x,x+1,x+2)\). The new assertion is the complete \(27\)-word support and its exceptional-prime classification. General character-sum machinery is classical and is not claimed to be new.

## Limitations
The theorem proves existence of each class word, not a sharp formula for its number of occurrences or the least starting index. The character-sum cutoff \(900\) is intentionally nonoptimal; the exact prime threshold \(307\) comes from the finite certificate. Emma Lehmer's 1983 *Patterns of power residues* is a highly relevant possible source of overlapping general results; its full text could not be inspected, so equivalence with an unindexed stronger theorem remains a genuine originality risk. No independent scientific audit has been performed.

## References
1. D. H. Lehmer, E. Lehmer, W. H. Mills, J. L. Selfridge, *Machine Proof of a Theorem on Cubic Residues*, Math. Comp. 16 (1962), 407–415, DOI: 10.2307/2003130. Lawful full text: https://www.cs.umd.edu/~gasarch/TOPICS/res/llms.pdf .
2. J. R. Rabung and J. H. Jordan, *Consecutive Power Residues or Nonresidues*, Math. Comp. 24 (1970), 737–741. Lawful full text: https://www.cs.umd.edu/~gasarch/TOPICS/res/resRabungJordan.pdf .
3. Carsten Dietzel, *A generalization of Schur's theorem and its application to consecutive power residues*, arXiv:1309.7506v1, 2013-09-28, https://arxiv.org/pdf/1309.7506 .
4. Hu Jiayuan and Chen Zhuoyu, *On distribution properties of cubic residues*, AIMS Mathematics 5 (2020), 6051–6060, DOI: 10.3934/math.2020388, https://www.aimspress.com/aimspress-data/math/2020/6/PDF/math-05-06-388.pdf .
5. Emma Lehmer, *Patterns of power residues*, J. Number Theory 17 (1983), 37–46, DOI: 10.1016/0022-314X(83)90004-5 (bibliography verified; substantive full-text comparison unavailable).
6. A. Weil, *On some exponential sums*, Proc. Natl. Acad. Sci. USA 34 (1948), 204–207 (classical complete character-sum estimate).
