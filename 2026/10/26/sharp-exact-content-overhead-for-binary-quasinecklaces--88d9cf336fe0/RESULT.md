# Sharp exact-content overhead for binary quasinecklaces

## Finding

Let \(Q(z,r)\) be the number of binary quasinecklaces (in the sense of Gabrić--Sawada) with exactly \(z\) zeros and \(r\) ones, and let \(N(z,r)\) be the number of binary necklaces at the same content, represented by their lexicographically least rotations. For all integers \(z,r\geq 1\),

\[
Q(z,r)=\sum_{\ell=1}^{z}[t^{z-\ell}](1+t+\cdots+t^\ell)^{r-1},
\qquad
N(z,r)=\frac{1}{z+r}\sum_{d\mid\gcd(z,r)}\varphi(d)\binom{(z+r)/d}{z/d}.
\]

Every cyclic word contributes to \(Q(z,r)\) exactly as many distinct rotations as there are zero-runs of maximal length in its primitive cyclic period. In particular,

\[
N(z,r)\leq Q(z,r)\leq zN(z,r),\qquad
\lim_{r\to\infty}\frac{Q(z,r)}{N(z,r)}=z
\quad\text{for each fixed }z\geq1.
\]

Consequently the best constant bounding the quasinecklace-to-necklace ratio **uniformly over the positive number of ones**, at a fixed positive number of zeros \(z\), is exactly \(z\). There is no content-independent constant. This concerns the number of candidates in the quasinecklace superset; it does **not** rule out constant-amortized-time algorithms using different candidate sets or direct necklace generation.

## Assumptions and scope

A binary word uses the ordered alphabet \(0<1\). In the original ordered alphabet \(1<2\), subtracting one from each symbol gives the same objects; at fixed word length, specifying the exact symbol-sum weight is equivalent to specifying the number of larger symbols.

A nonempty word is a *quasinecklace* if, writing \(a\) for its least symbol and \(\ell\) for the maximum length of a run of \(a\): (i) it begins with \(a^\ell\); (ii) every later occurrence of \(a^\ell\) with a following symbol is followed by a symbol no smaller than the symbol following its initial \(a^\ell\); and (iii) if the word ends with \(a\), it consists entirely of \(a\)'s. These are Gabrić--Sawada's defining conditions. A *necklace* is the lexicographically smallest distinct rotation in a cyclic rotation class. A primitive cyclic period is the shortest word whose repeated concatenation is the given word. Only the nonmonochromatic case \(z,r\geq1\) is needed for the assertions above; either monochromatic content has one quasinecklace and one necklace.

The notation \([t^j]F(t)\) denotes a polynomial coefficient; \(\varphi\) denotes Euler's totient function.

## Proof

**Binary characterization and exact enumeration.** In a binary word using both symbols, conditions (i) and (iii) force a prefix of \(\ell\) zeros, where \(\ell\) is the longest zero-run, and a final one. The symbol after any maximal zero-run must be one, so condition (ii) holds automatically. Hence the quasinecklaces are precisely the words with the unique decomposition

\[
0^\ell1(0^{e_1}1)\cdots(0^{e_{r-1}}1),
\qquad 1\leq\ell\leq z,\quad
0\leq e_i\leq\ell,\quad
\sum_{i=1}^{r-1}e_i=z-\ell.
\]

Here uniqueness means that \(\ell\) and all gaps \(e_i\) are determined by the word. Conversely, every word in the displayed form obeys all three conditions: its first zero-run is of maximal length and it ends in one. Counting bounded gap compositions proves the formula for \(Q(z,r)\), including \(r=1\), when an empty product contributes only for \(\ell=z\).

**Cyclic multiplicity.** Fix any cyclic binary word containing both symbols. Rotate it so that a longest cyclic zero-run starts first. Such a rotation ends in one and is a quasinecklace, proving at least one representative per cyclic orbit. Conversely, the first zero-run of any quasinecklace representative must be a longest cyclic zero-run; no other rotations qualify. If the given cyclic word is a repetition of its primitive period, repetitions of the same starting run produce identical rotations. Therefore the number of distinct qualifying rotations is exactly the number of longest zero-runs in one primitive period. This number is between one and the number of zeros in that period, hence at most \(z\). Summing over cyclic orbits proves \(N(z,r)\le Q(z,r)\le zN(z,r)\). Standard Burnside counting of binary words with prescribed content proves the displayed formula for \(N(z,r)\).

**Sharpness.** Fix an integer \(z\geq2\) and let \(r\to\infty\). The term \(\ell=1\) in the exact quasinecklace formula is \(\binom{r-1}{z-1}\). For each \(\ell\ge2\), the remaining polynomial coefficient is \(O_z(r^{z-\ell})\), so

\[
Q(z,r)=\frac{r^{z-1}}{(z-1)!}+O_z(r^{z-2}).
\]

In Burnside's formula the identity-rotation term is

\[
\frac{1}{r+z}\binom{r+z}{z}
=\frac{r^{z-1}}{z!}+O_z(r^{z-2}).
\]

Every nonidentity term comes from a divisor \(d\ge2\) of \(z\) and is \(O_z(r^{z/d-1})=O_z(r^{z-2})\); the divisor set is fixed. Thus

\[
N(z,r)=\frac{r^{z-1}}{z!}+O_z(r^{z-2}),
\qquad \frac{Q(z,r)}{N(z,r)}\longrightarrow z.
\]

For \(z=1\) there is exactly one cyclic orbit and one quasinecklace at every \(r\ge1\), so the ratio is identically one. The established upper bound and asymptotic lower approach prove that the optimal constant is \(z\) for every \(z\ge1\). Since \(z\) is unbounded, no absolute constant works simultaneously for all exact contents.

## Verification

The included standalone `verify.py` compares the defining three-condition predicate against the coefficient formula by exhausting all binary words of lengths \(1\) through \(15\), and separately checks the Burnside count by exhaustive rotation testing; this covers \(135\) length/content classes. It also tests the exact maximal-zero-run orbit-multiplicity statement on \(2587\) nonmonochromatic cyclic orbits through length \(14\), and computes large-count ratios for \(z=1,\ldots,7\) with \(r=3000\) using integer arithmetic. Run `python3 verify.py` in the directory containing the supplied script. Its success line is `VERIFY_OK`.

The exhaustive checks cover finitely many parameters and are not the proof of the all-parameter formulas or limits. Those follow from the foregoing decomposition, orbit argument, and coefficient asymptotics.

## Relationship to prior work

Gabrić and Sawada (2026) introduce quasinecklaces, prove an unrefined constant-factor bound relative to necklaces, and establish constant-amortized-time colex generation for a *weight upper bound*. Their Section 4.3 explicitly uses transformations that preserve or **decrease** weight, not necessarily preserve exact weight. Their published length-only recurrence and bounded-weight result do not provide the fixed-content sharp ratio above.

Sawada and Williams (2013; author-hosted preprint dated 2010) already give constant-amortized-time algorithms for **exact-density binary necklaces and pseudonecklaces**. Pseudonecklaces are a distinct, generally smaller auxiliary class than the quasinecklaces studied here. Consequently the result is a sharp structural limit on transferring the particular 2026 quasinecklace candidate-superset analysis to an exact-weight slice; it is not an algorithmic impossibility theorem.

## Limitations

The sharp multiplicative factor is proved for the two-symbol quasinecklace class only. No corresponding classification is asserted for larger alphabets, and no claim is made that an exact-weight colex algorithm must enumerate all quasinecklaces. The enumerator itself is elementary once the binary form of the definition is identified; the substantive distinction is its exact parameter-by-parameter relation to necklaces and the arbitrarily large sharp overhead. Independent historical-priority review has not been performed.

## References

1. D. Gabrić and J. Sawada, *Necklaces and Lyndon words in colexicographic order*, arXiv:2607.05324, initially submitted 2026-07-06; see Definition 3, Theorems 4 and 9, and Section 4.3. https://arxiv.org/abs/2607.05324
2. J. Sawada and A. Williams, *A Gray code for fixed-density necklaces and Lyndon words in constant amortized time*, *Theoretical Computer Science* **502** (2013), 46–54. Author-hosted preprint: https://www.socs.uoguelph.ca/~sawada/papers/bubble4.pdf
