# Uniform \(5/16\) subsequence-universality density in the Rudin–Shapiro word

## Finding
Let \(r=r_0r_1r_2\cdots\) be the binary Rudin–Shapiro word, where \(r_n\) is the number of (possibly overlapping) occurrences of `11` in the base-two expansion of \(n\), reduced modulo two. For a finite binary word \(v\), let \(\iota(v)\) be the largest nonnegative integer \(k\) such that **every** length-\(k\) word over the fixed alphabet \(\{0,1\}\) occurs as a scattered subsequence of \(v\).

**Uniform factor theorem.** For all integers \(i\geq0\) and \(N\geq1\), writing \(v=r_ir_{i+1}\cdots r_{i+N-1}\),
\[
\boxed{\left|\iota(v)-\frac{5N}{16}\right|\leq 2\lfloor\log_2N\rfloor+2.}
\]
In particular, \(\iota(v)/N\to5/16\) uniformly over all starting positions \(i\) as \(N\to\infty\).

**Exact dyadic prefixes.** For each integer \(m\geq4\),
\[
\boxed{\iota(r_0\cdots r_{2^m-1})=5\cdot2^{m-4}-\mathbf 1_{\{m\ \mathrm{even}\}}.}
\]
The first values for \(m=4,5,6,7,8,9\) are \(4,10,19,40,79,160\).

## Assumptions and scope
The alphabet is always the full fixed binary alphabet \(\{0,1\}\), including for very short factors that might contain only one symbol. Indices begin at zero; a subsequence need not consist of consecutive positions. Factors are contiguous. The first formula holds for **every** finite factor of the indicated infinite word, without a bounded starting-position assumption. No claim about other automatic sequences or about optimality of the logarithmic error is made.

## Proof
**1. Four-letter morphic presentation.** Write \(a=(0,0)\), \(b=(0,1)\), \(c=(1,1)\), and \(d=(1,0)\), encoding the pair \((r_n,n\bmod2)\). Counting occurrences of adjacent ones in binary gives
\[
r_{2n}=r_n,\qquad r_{2n+1}=r_n\oplus(n\bmod2).
\]
Consequently, the pair at index \(n\) has the two successors at indices \(2n\) and \(2n+1\) given by the uniform substitution
\[
\tau(a)=ab,\quad\tau(b)=ac,\quad\tau(c)=db,\quad\tau(d)=dc.
\]
Let \(\pi(a)=\pi(b)=0\) and \(\pi(c)=\pi(d)=1\). The infinite word is \(r=\pi(\tau^\omega(a))\). In particular, at every position divisible by \(2^m\), an aligned block of length \(2^m\) has the form \(\pi(\tau^m(s))\) for some \(s\in\{a,b,c,d\}\).

**2. Arch-counting transducer.** Read a binary word from left to right with state \(\bot\) (no symbol yet in the current arch) or state \(0\) or \(1\) (the one symbol already seen). Reading a bit in state \(\bot\) sets that bit as state; reading the same bit in a nonempty state leaves the state unchanged; reading the other bit increases the count by one and resets to \(\bot\). Thus the count is precisely the number of complete greedy arches, each the shortest next factor containing both letters.

That count equals \(\iota(v)\): any target of length equal to the count embeds by choosing the corresponding target symbol in each arch. Conversely, append to the sequence of arch-closing letters a symbol absent from the unfinished final remainder. Since each arch-closing letter is its **first** occurrence after the preceding arch, the indicated target of length one greater cannot embed. This also proves the equality when the count is zero.

Write \(F_{m,s}(u)\) for (number of completed arches, final state) when \(\pi(\tau^m(s))\) is read starting in state \(u\in\{\bot,0,1\}\). Under concatenation, the count adds and the final state of the left factor becomes the starting state of the right factor.

**3. Explicit block induction.** Put \(q=5\cdot2^{m-4}\) and \(e=m\bmod2\). For every \(m\geq4\), the complete transfer table is as follows. The `base count` is the count from initial state \(\bot\); the two `extra` columns give the number to add to the base count for initial states \(0\) and \(1\), respectively. The final bit is independent of the initial state.

| Block | Base count | Extra from 0 | Extra from 1 | Final bit |
| --- | ---: | ---: | ---: | ---: |
| \(\pi(\tau^m(a))\) | \(q-1+e\) | 0 | 1 | \(1-e\) |
| \(\pi(\tau^m(b))\) | \(q-e\) | 0 | 1 | \(e\) |
| \(\pi(\tau^m(c))\) | \(q-e\) | 1 | 0 | \(1-e\) |
| \(\pi(\tau^m(d))\) | \(q-1+e\) | 1 | 0 | \(e\) |

For \(m=4\), direct reading of the four length-16 blocks gives base counts \((4,5,5,4)\), final bits \((1,0,1,0)\), and extras as displayed. This is the induction base.

For the step \(m\to m+1\), the four blocks concatenate, in order, as \(ab,ac,db,dc\) at level \(m\). From initial state \(\bot\), the new base counts for \(a,d\) are both \(2q-e\), while those for \(b,c\) are both \(2q-1+e\). To see the first identity, for example, concatenate level-\(m\) blocks \(a\) and \(b\): the counts are \((q-1+e)+(q-e)\), plus \(1-e\) from entering the second block with the first block's ending bit. The other three concatenations are identical substitutions into the table. With \(q'=2q\) and \(e'=1-e\), these are exactly \(q'-1+e'\) and \(q'-e'\). The right-hand blocks \(b,c,b,c\) give the required final bits. The initial-state extras remain as shown, since \(a,b\) begin with a level-\(m\) block of type \(a\), while \(c,d\) begin with type \(d\). The table follows for all \(m\geq4\).

For \(m=0,1,2,3\), direct evaluation of the same four transfers suffices. Together with the table it implies the **uniform block estimate**, for every level \(m\geq0\), letter \(s\), and input state \(u\),
\[
\left|\#\mathrm{arches}(\pi(\tau^m(s));u)-\frac5{16}2^m\right|\leq1.
\]
Here the count means arches completed **during that block**, so the input state may reflect earlier text.

**4. Every factor.** Cover the interval of positions \([i,i+N)\) by maximal aligned dyadic intervals. There are at most two intervals of any fixed power-of-two length, hence at most \(2(\lfloor\log_2N\rfloor+1)\) intervals altogether. Each corresponds to a substitution block from Step 1. Reading the intervals in order, the completed-arch count adds, and Step 3 bounds each interval's deviation from five sixteenths of its length by one, for **any** state inherited from earlier intervals. The triangle inequality gives
\[
\left|\iota(v)-5N/16\right|\leq2(\lfloor\log_2N\rfloor+1).
\]
Dividing by \(N\) yields the asserted uniform limit.

**5. Dyadic prefixes.** The prefix of length \(2^m\) is exactly \(\pi(\tau^m(a))\). Starting from \(\bot\), the level-\(m\) table gives count \(q-1+e\), which is \(q-1\) when \(m\) is even and \(q\) when \(m\) is odd. This proves the second formula. \(\square\)

## Verification
Run `python3 verify.py` with a standard Python 3 installation. It constructs all three-state transfers by repeated substitution through level 22 and checks the symbolic formula for every letter and starting state; separately checks the four-letter coding against the binary-digit definition of the Rudin–Shapiro sequence for dyadic prefixes through length 32768; checks direct exhaustive subsequence inclusion against arch counting on short factors; and tests the all-factor discrepancy on 22,890 factor instances. Output on successful completion is `RS_UNIFORM_UNIVERSALITY_PASS transfers=23 dyadic=16 brute=19x14 factors=22890`. The infinite statements follow from the proof, not from the finite tests.

## Relationship to prior work
Barker et al. establish scattered-factor universality and its greedy arch-factorization computation. Schnoebelen and Veron analyze compositional signatures and algorithms for arch factorizations and compressed words. Meleshko et al. describe the Rudin–Shapiro sequence while studying a different invariant, pseudoperiods. Those works supply the conceptual framework, but the source material inspected does not give the stated specific \(5/16\) density, the exact dyadic-prefix formula, or an all-factors logarithmic discrepancy bound. The latter depend on the explicit four-letter weighted-transfer calculation above.

## Limitations
The logarithmic error bound is a proven uniform upper estimate but is not asserted to have optimal order or optimal constant. The theorem concerns only the classical binary Rudin–Shapiro coding. Computations are finite corroborations of the inductive proof and cannot themselves establish its infinite quantifiers. Unindexed or inaccessible equivalent treatments remain a literature risk.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629 (initial public version 2020-03-10), especially Section 4.
2. J. Meleshko, P. Ochem, J. Shallit, S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171 (initial public version 2022-07-20), Section 4.4.
3. P. Schnoebelen, J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932 (initial public version 2023-04-24), Sections 3 and 5.
