# Sharp output-sphere bound and rigidity for nonbinary permutation bursts of arbitrary length

## Finding

**Theorem.** Fix integers \(q\ge k\ge4\) and \(n\ge k\), and an alphabet \(\Sigma_q\) of \(q\) symbols. An admissible received word arises from an input \(x\in\Sigma_q^n\) by choosing exactly one *non-wrapping* consecutive length-\(k\) block and permuting its entries arbitrarily, including the identity permutation. Let \(B_k(x)\) be the set of distinct admissible words, rather than the number of choices of a block and permutation. For \(2\le m\le k\), put

\[
c_m=m!-2(m-1)!+(m-2)!.
\]

Then the **sharp** radius-one output-volume bound, valid for all finite \(n\), is

\[
\boxed{\max_{x\in\Sigma_q^n}|B_k(x)|=1+\sum_{m=2}^{k}(n-m+1)c_m.}
\]

Equality holds **if and only if** every consecutive length-\(k\) block of \(x\) consists of \(k\) distinct symbols. The exact number of distinct labeled maximizing centers equals

\[
\boxed{\frac{q!}{(q-k)!}(q-k+1)^{n-k}.}
\]

In particular, on a four-letter alphabet for \(k=4\), the exact maximum is \(18n-48\), and exactly \(24\) distinct centers attain it at every \(n\ge4\). For \(q=k=5\), the maximum is \(96n-360\), attained by \(120\) centers. These are output-sphere statements, not optimal-code-size or decoder guarantees.

## Assumptions and scope

The alphabet consists of distinguishable symbols. Windows have exactly \(k\) positions, lie entirely inside the word, and may be chosen at any of the \(n-k+1\) starting positions. They do not wrap around. An operation permits any permutation of the selected block; possible output multiplicities from different permutations or windows are discarded. The hypotheses \(q\ge k\ge4\), \(n\ge k\) are necessary for the proposed extremizer class to be nonempty; the support-count lemma below also applies with \(q<k\) and \(k\ge2\), but does not assert the same sharp upper bound there.

For a length-\(m\) word \(u\), let \(r_a\) count occurrences of letter \(a\) in \(u\), and write \(T(u)=m!/\prod_a r_a!\) for its distinct anagrams. Let \(H(u)\) denote the number of distinct anagrams \(v\) satisfying \(v_1\ne u_1\) and \(v_m\ne u_m\). With \(a=u_1\) and \(b=u_m\), the exact local number is

\[
H(u)=T(u)\left(1-\frac{r_a+r_b}{m}+\frac{r_a(r_b-\mathbf 1_{a=b})}{m(m-1)}\right).
\]

This rational-looking expression is a nonnegative integer because it enumerates finite anagrams.

## Proof

**1. Disjoint decomposition by changed support.** Fix \(x\) and one nonidentity output \(y\in B_k(x)\). Let \(i\) and \(j\) be its first and last positions differing from \(x\). This interval \([i,j]\) is unique; write \(m=j-i+1\). The unchanged sites outside \([i,j]\) imply that \(x_i\cdots x_j\) and \(y_i\cdots y_j\) have the same letter multiplicities: the operation permutes one larger length-\(k\) block and cancels equal symbols at both ends. Necessarily \(2\le m\le k\), and the two endpoint letters differ from their counterparts in \(x\).

Conversely, select any interval \([i,j]\) of length \(2\le m\le k\) and any anagram of \(x_i\cdots x_j\) that changes both endpoints. Since \(n\ge k\), there exists a length-\(k\) consecutive window containing this interval: choose its start between \(\max(1,j-k+1)\) and \(\min(i,n-k+1)\), a nonempty integer range. Fix all other symbols inside that larger window and use the chosen anagram. This produces exactly the specified output. Two distinct intervals or distinct anagrams cannot produce the same output because its first and last changed positions uniquely recover the interval. Hence, with \(x_{i:i+m-1}\) denoting the actual consecutive block,

\[
\boxed{|B_k(x)|=1+\sum_{m=2}^{k}\sum_{i=1}^{n-m+1}H(x_{i:i+m-1}).}\tag{1}
\]

**2. Anagram endpoint exclusion.** An arbitrary distinct anagram of \(u\) fixes its first original symbol with probability \(r_a/m\), fixes its last original symbol with probability \(r_b/m\), and fixes both with probability \(r_a(r_b-\mathbf1_{a=b})/[m(m-1)]\), under a uniform choice from its \(T(u)\) distinct anagrams. Inclusion-exclusion gives the displayed exact formula for \(H(u)\).

If all \(m\) letters of \(u\) are different, \(T(u)=m!\), \(r_a=r_b=1\), and \(a\ne b\). Therefore

\[
H(u)=m!-2(m-1)!+(m-2)!=c_m.
\]

If \(u\) repeats any letter, then \(T(u)\le m!/2\), hence \(H(u)\le m!/2\). For every \(m\ge4\),

\[
c_m/m!=1-\frac{2}{m}+\frac1{m(m-1)}>\frac12,
\]

so equality is impossible for a repeated-letter block. At \(m=2\), a repeated-letter block has \(H=0<1=c_2\). At \(m=3\), repeated-letter patterns have at most \(H=1<3=c_3\), by direct inspection of the patterns with two equal symbols (all-equal blocks have \(H=0\)). Thus for every \(m\ge2\) one has \(H(u)\le c_m\), with equality if and only if all letters of \(u\) are different.

**3. Sharpness and rigidity.** Apply the local upper bound term by term to (1). This yields the asserted universal upper bound. It is attained by any input with pairwise distinct symbols throughout each length-\(k\) block; then every shorter consecutive block also has distinct letters and each summand is maximal. Conversely, if any length-\(k\) block repeats a symbol, its \(m=k\) summand is strictly smaller than \(c_k\), and no other summand can exceed its respective \(c_m\). Thus the global upper bound is strictly missed. The equality characterization is exact, not merely sufficient.

**4. Number of maximizers.** The first \(k\) symbols must all be different and may be chosen in \(q(q-1)\cdots(q-k+1)=q!/(q-k)!\) ways. At every subsequent site its symbol must avoid exactly the previous \(k-1\) distinct letters, leaving \(q-k+1\) choices. The construction is reversible and does not overcount words, giving the population formula. For \(k=4\), \((c_2,c_3,c_4)=(1,3,14)\), giving \(1+(n-1)+3(n-2)+14(n-3)=18n-48\). For \(k=5\), \(c_5=78\) and the formula simplifies to \(96n-360\). This completes the proof.

## Verification

The accompanying `verify.py` constructs every possible output directly for a finite input by enumerating distinct permutations of every admissible length-\(k\) window, then **independently** computes the local anagram formula and the theorem's proposed bound. It exhaustively checked 100,978 input words over 43 parameter triples, with alphabet sizes from 2 through 5, including cases with \(q<k\) to test the local identity outside the sharp-extremizer hypothesis. The output recorded in `verification_output.txt` ends with `VERIFY_OK`. The mathematical proof above, not this finite testing, establishes the unbounded-parameter statement.

Reproduce with a standard Python 3 interpreter: `python verify.py`. No external libraries, network access, files, or user-supplied input are required. The finite enumerator establishes direct consistency in the checked ranges only.

## Relationship to prior work

Chen and Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1 (11 October 2026), define this exact-window permutation-burst model in Definition 1 and analyze binary sphere sizes, redundancy, and coding constructions. Their introduction explicitly confines their analysis to binary alphabets and defers the extension to larger alphabets. The present theorem is a sharp **nonbinary** sphere maximum and equality census for **every** block length \(k\ge4\); it does not claim the error model, the binary probabilistic bounds, or coding constructions as new.

A previously derived exact all-alphabet output-sphere spectrum for \(k=3\) already determines the specialized maximum \(4n-6\) and its extremal population. The \(k=3\) case is not claimed as new here. The novelty is the unrestricted factorial-length theorem and complete rigidity for arbitrary \(k\ge4\), not an increment of an existing small-block numerical table. Other nearby models, including limited permutation error covers, deletion/insertion bursts, and cyclic-only shifts, have different allowed output sets.

## Limitations

The result assumes \(q\ge k\); it does not provide sharp maxima when \(q<k\), determine the entire output-ball distribution for \(k\ge4\), improve optimal-code sizes or rates, or address multiple permutation bursts. The unique-support decomposition does apply to arbitrary alphabet sizes but yields a different extremal optimization question in the repeated-letter regime. A prior equivalent nonbinary all-\(k\) extremal theorem in unindexed literature cannot be ruled out; the accessible primary paper and checked mathematical records did not reveal such coverage. The four-symbol instance is a mathematical channel idealization and does not by itself predict empirical nanopore error frequencies.

## References

1. Yuan-Pon Chen and Olgica Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1, first submitted 2026-10-11, https://arxiv.org/html/2610.15701v1 ; https://arxiv.org/abs/2610.15701 .
2. Prior exact finite-alphabet length-three substring-permutation output-sphere calculation, 2026; the specialized \(k=3\) case is used only to delineate the contribution, not as an assumption in this proof.
