# Sharp restricted two-quintic covering over prime fields

## Finding

For every prime \(p\), put \(H_p=\{x^5:x\in\mathbb F_p^\times\}\) and
\[
2^{\wedge}H_p=\{u+v:u,v\in H_p,\ u\ne v\}.
\]
The two-summand **restricted quintic covering theorem** is the exact equivalence
\[
2^{\wedge}H_p=\mathbb F_p
\quad\Longleftrightarrow\quad
p\ge5\text{ and }p\notin\{11,31,41,61,71,101\}.
\]
Consequently, \(131\) is the *sharp persistent prime threshold*: every prime \(p\ge131\) has the covering property, whereas \(101\) does not. The six exceptional primes have, respectively, \(10,18,16,12,14,20\) missing field residues. Distinctness refers to the **nonzero fifth-power values** \(u\ne v\), not just to the roots producing them.

## Assumptions and scope

The statement concerns prime fields, positive fifth powers of nonzero field elements, and exactly two addends with unequal **values**. There is no assumption that the two fifth-power roots be unique. No conclusion for general prime-power fields, exponents other than five, or more than two addends is asserted. The finite spectrum and the infinite covering theorem form one combined result.

## Proof

**1. Primes with \(5\nmid p-1\).** For every prime \(p\ge5\) with \(p\not\equiv1\pmod5\), the multiplicative group \(\mathbb F_p^\times\) is cyclic and \(x\mapsto x^5\) is bijective; hence \(H_p=\mathbb F_p^\times\). For any \(a\in\mathbb F_p\), choose \(u\) outside the set \(\{0,a,a/2\}\), which is possible because \(p\ge5\). Then \(v=a-u\) is nonzero and distinct from \(u\). This proves the restricted representation for every \(a\). In contrast, for \(p=2\) there are no distinct members of \(H_p\); for \(p=3\), \(H_3=\{1,2\}\) and its restricted two-sum is just \(\{0\}\).

**2. All primes \(p\equiv1\pmod5\), \(p\ge241\).** Fix a nonzero \(a\in\mathbb F_p\). Consider the smooth projective Fermat curve
\[
X^5+Y^5=aZ^5.
\]
It is nonsingular because \(p\ne5\), and has genus \((5-1)(5-2)/2=6\). By the Hasse–Weil bound, the number of \(\mathbb F_p\)-rational projective points is at least
\[
p+1-12\sqrt p.
\]
Call a rational point *inadmissible* if \(Z=0\), or \(X=0\), or \(Y=0\), or \(X^5=Y^5\). The locus \(Z=0\) has at most five points; the loci \(X=0\) and \(Y=0\) have at most five each. Since \(X^5=Y^5\) is the union of five lines over \(\mathbb F_p\), and each line meets this Fermat curve in at most five points, that locus has at most twenty-five rational points. Thus **at most forty** points are inadmissible. For \(p\ge241\),
\[
p+1-12\sqrt p>40,
\]
because \((241-39)^2>144\cdot241\) and \((p-39)^2-144p\) is increasing on \([241,\infty)\). An admissible rational point therefore exists. Normalize \(Z=1\), and take \(u=X^5\), \(v=Y^5\), obtaining nonzero unequal values with sum \(a\). For \(a=0\), choose any \(u\in H_p\); since \(-1=(-1)^5\in H_p\), also \(v=-u\in H_p\), and \(u\ne v\) because \(p\) is odd. Hence the full restricted sumset is \(\mathbb F_p\).

**3. Complete remaining prime census.** Every prime \(p<241\) with \(p\equiv1\pmod5\) is one of
\[
11,31,41,61,71,101,131,151,181,191,211.
\]
For each one, generate precisely the subgroup \(H_p\), form the exact set of unordered distinct-value sums, and complement it in \(\mathbb F_p\). The reproducible integer-only computation gives:

| \(p\) | \(|H_p|\) | \(|\mathbb F_p\setminus 2^{\wedge}H_p|\) |
|---:|---:|---:|
| 11 | 2 | 10 |
| 31 | 6 | 18 |
| 41 | 8 | 16 |
| 61 | 12 | 12 |
| 71 | 14 | 14 |
| 101 | 20 | 20 |
| 131 | 26 | 0 |
| 151 | 30 | 0 |
| 181 | 36 | 0 |
| 191 | 38 | 0 |
| 211 | 42 | 0 |

For full reproducibility, the precise missing-residue sets for the six exceptions are:

- \(p=11\): \(\{1,2,3,4,5,6,7,8,9,10\}\).
- \(p=31\): \(\{2,3,8,9,10,12,13,14,15,16,17,18,19,21,22,23,28,29\}\).
- \(p=41\): \(\{1,3,7,9,14,16,19,20,21,22,25,27,32,34,38,40\}\).
- \(p=61\): \(\{4,5,6,9,17,23,38,44,52,55,56,57\}\).
- \(p=71\): \(\{1,20,23,26,30,32,34,37,39,41,45,48,51,70\}\).
- \(p=101\): \(\{1,6,10,14,17,32,36,39,41,44,57,60,62,65,69,84,87,91,95,100\}\).

The enumerator generates primes by trial division, builds \(H_p\) independently from all fifth powers and from a primitive root, and compares unrestricted pair enumeration subject to unequal values with an independent complement-membership test for each residue. This establishes exhaustive finite coverage—not extrapolation—and completes the proof. \(\square\)

## Verification

Execute `python3 verify_quintic.py` with standard Python 3. The program checks every prime through \(240\), compares two constructions of all fifth-power values and two independently structured restricted-sum tests, and matches the exact six missing-residue arrays. It also checks the integer endpoint inequality for the Hasse–Weil argument. The infinity step is proved mathematically using smoothness, genus, point exclusion and monotonicity; the finite program is not presented as a proof of Hasse–Weil or an infinite search.

## Relationship to prior work

Demiroğlu Karabulut's *Waring's Problem in Finite Rings* (public preprint September 13, 2017, arXiv:1709.04428), Section 3 and its tables, studies ordinary sums of fifth powers, allowing zero and repeated values. In particular, its corrections \(g(5,71)=2\) and \(g(5,101)=2\) do **not** imply restricted covering: the present exceptional data show that both of those prime fields fail when addends must be nonzero and unequal. The author's later work (DOI below) likewise concerns ordinary Waring numbers and a distinct-elements *difference* condition, as described by the accessible abstract; its full text was not accessible in this review.

Wu, Wei and Li (arXiv:2304.11789) study decompositions \(D_k=A+B\) with resultant sumset equal to the *power-residue set*, rather than the restricted doubling \(D_5\dot+ D_5\) being the entire field; these statements do not imply one another. A separately indexed two-sum result for the **graph** \(\{(t,t^5)\}\subset\mathbb F_p^2\) concerns different ambient objects and unrestricted summands, so its reported spectrum does not settle the present distinct nonzero scalar-value condition. The known general Hasse–Weil bound is used rather than presented as a discovery.

## Limitations

The prime-field scope is essential to the small characteristic census; no characterization for all finite extensions is given. The proof does not give the number of admissible representations at each prime greater than \(211\). The exact claim is assessed against accessible literature and record summaries, but earlier unindexed computations or uninspected statements in the later Waring paper could affect publication priority. A separate expert review is not claimed.

## References

1. Y. Demiroğlu Karabulut, *Waring's Problem in Finite Rings*, arXiv:1709.04428 (first public version 2017-09-13), journal DOI:10.1016/j.jpaa.2018.11.003.
2. Y. Demiroğlu Karabulut, *An analogue of Furstenberg–Sárközy's theorem and an alternative solution to Waring's problem over finite fields*, Expositiones Mathematicae (2023), DOI:10.1016/j.exmath.2022.10.003 (abstract inspected; full text inaccessible).
3. H.-L. Wu, N.-L. Wei and Y.-B. Li, *On sumsets involving kth powers of finite fields*, arXiv:2304.11789 (first public version 2023-04-24).
4. Hasse–Weil point bound for smooth projective curves over finite fields, standard theorem; e.g. H. Stichtenoth, *Algebraic Function Fields and Codes*, second ed., Springer (2009).
