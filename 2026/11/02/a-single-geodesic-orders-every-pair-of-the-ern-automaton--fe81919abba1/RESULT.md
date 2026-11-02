# A single geodesic orders every pair of the Černý automaton

## Finding

For each integer \(n\ge2\), consider the complete deterministic automaton
\(C_n\) on \(Q_n=\{0,1,\ldots,n-1\}\) with letters
\[
 a(i)=i+1\pmod n,\qquad
 b(i)=\begin{cases}0&i=n-1,\\i&i<n-1.\end{cases}
\]
For an unordered distinct pair \(P=\{i,j\}\), let \(\tau_n(P)\) be the minimum
length of a word that maps both elements of \(P\) to one state. If
\(0\le i<j<n\) and \(d=j-i\), then
\[
\boxed{\tau_n(\{i,j\})=
\begin{cases}
nd-i,&2d<n,\\
(n+1)(n-d)-n-i,&2d\ge n.
\end{cases}}
\]
The \(\binom n2\) lengths are pairwise distinct and comprise precisely
\(1,\ldots,\binom n2\). Every pair has a **unique** shortest merging word,
and these words are the nonempty suffixes of **one** master word
\[
\boxed{W_n=
\begin{cases}
(a^{n-1}b)^{(n-1)/2},&n\text{ odd},\\
a^{n/2-1}b\,(a^{n-1}b)^{n/2-1},&n\text{ even}.
\end{cases}}
\]
In particular, the unique pair attaining the largest merging time
\(\binom n2\) is \(\{0,\lfloor n/2\rfloor\}\). In the pair automaton,
the unique rank-decreasing transitions form a directed Hamiltonian path
through all \(\binom n2\) nonterminal pair states, followed by the sink.

## Assumptions and scope

The convention for the two letters is stated above; it is equivalent by
state relabeling and letter renaming to the usual Černý automaton. All
words act left-to-right. A pair remains merged after any subsequent input.
A shortest merging word is counted as a word over \(\{a,b\}\), not as a
path modulo letter or state symmetry. The result applies for every integer
\(n\ge2\), both parities, and to every distinct pair; it does not assert
uniqueness for shortest *whole-automaton* reset words.

## Proof

Write \(H(i,j)\) for the displayed piecewise integer, and assign rank
\(H=0\) to the merged sink. The proof has three parts.

**Step 1: the sharp potential.** For \(j<n-1\), letter \(a\) shifts both
indices up by one without wraparound; hence \(H(a\{i,j\})=H(i,j)-1\).
Letter \(b\) fixes the pair. If \(j=n-1\), then
\(d=n-1-i\), and letter \(a\) sends the pair to \(\{0,i+1\}\), while
\(b\) sends it to \(\{0,i\}\) (the sink when \(i=0\)). There are two
cases:

* If \(2d<n\), the displayed formula gives
  \(H(i,n-1)=(n+1)d-n+1\) and
  \(H(0,i+1)=(n+1)d-n\). The other successor has strictly larger rank:
  \(H(0,i)-H(i,n-1)=n\) except in the odd-order midpoint
  \(n=2m+1,d=m\), where the difference is \(m>0\).
* If \(2d\ge n\), then \(H(i,n-1)=ni+1\) and
  \(H(0,i)=ni\) for \(i>0\), or \(0\) for \(i=0\). Letter \(b\) therefore
  decreases rank exactly by one. Letter \(a\) raises rank by \(n-1\),
  except when \(n=2m\) and \(d=m\), where it raises rank by \(m-1\)
  (zero for \(n=2\)).

Thus **every transition decreases \(H\) by at most one, and from each
nonterminal pair exactly one of the two letters decreases it by one**.
Choosing that letter repeatedly reaches rank zero, since ranks are
nonnegative integers. Consequently the minimum merging length is exactly
\(H\), and every minimum-length word must choose the unique decreasing
letter at each step. This proves both the formula and unique geodesics.

**Step 2: no repeated or missing ranks.** Put
\(m=\min(d,n-d)\). For each \(1\le m<n/2\), the pairs with
\(d=n-m\) give exactly the \(m\) consecutive ranks
\[
n(m-1)+1,\ldots,n(m-1)+m,
\]
while the pairs with \(d=m\) give the remaining \(n-m\) consecutive
ranks
\[
n(m-1)+m+1,\ldots,nm.
\]
If \(n\) is even, the \(n/2\) antipodal pairs with \(d=n/2\)
give the final ranks from \(n(n-2)/2+1\) through
\(n(n-1)/2\). These intervals partition
\(\{1,\ldots,\binom n2\}\), establishing bijectivity. The unique
maximum belongs to \(\{0,\lfloor n/2\rfloor\}\).

**Step 3: the master geodesic.** Starting at the unique maximal pair and
repeatedly taking the unique rank-decreasing letter visits the pair of
ranks \(\binom n2,\binom n2-1,\ldots,1\) and then the sink. By
Step 2 it visits *every* pair once. For odd \(n=2m+1\), starting from \(\{0,m\}\), each block
\(a^{n-1}b\) sends \(\{0,k\}\) to \(\{0,k-1\}\) for
\(1\le k\le m\), interpreting \(\{0,0\}\) as the sink. Thus the
rank-decreasing word is \((a^{n-1}b)^m\). For even \(n=2m\),
the initial \(a^{m-1}b\) sends the maximal pair \(\{0,m\}\)
to \(\{0,m-1\}\); the remaining \(m-1\) blocks
\(a^{n-1}b\) decrease the second member to zero in turn. In both
cases, every step uses the unique decreasing letter established above.
The resulting master words have lengths
\(\binom n2\). Because the path contains the unique state of each rank,
its final \(h\) letters are the unique shortest word for the rank-\(h\)
pair, for every \(1\le h\le\binom n2\). This completes the proof.

## Verification

Run `python verification/verify.py` from the package root. It tests
all pair ranks and transition differences through \(n=80\), confirms a
complete distinct spectrum, verifies the master path and every suffix,
and uses a separately constructed reverse breadth-first-search distance
algorithm through \(n=35\). The recorded output is in
`verification/verify_output.txt`; the run produced `VERIFY_OK` and
433,740 finite assertions. These computations test the formulas but do
not replace the above infinite-family proof.

## Relationship to prior work

Szykuła's 2026 survey, Sections 2.1 and 2.4, emphasizes shortest
synchronizing words of prescribed subsets and states the established
sharp general upper bound \(n(n-1)/2\) for merging a pair, attained in
the Černý family. Thus **the maximum itself is not claimed as new**.
Gusev's 2014 study, Section 3 and Lemma 1 (including Fig. 3), gives an
explicit equivalent pair automaton for *odd* orders to analyze expected
random-input synchronization times. That known transition description
is a powerful basis from which the odd-order metric can in principle be
derived. Neither inspected source states the present complete
pointwise metric for both parities, the singleton multiplicity of every
possible merging time, the unique-geodesic theorem, or the common
master-suffix characterization. The contribution is this deterministic
metric and its rigidity, not the pair-automaton definition or the
previously known extremal bound.

## Limitations

Only the classical cycle-plus-one-merger family is covered. The
universal upper bound on pair synchronization was known previously.
The odd-order pair graph of Gusev's paper is particularly close prior
art and materially increases the residual originality risk; a priority
claim beyond the inspected sources is not certified. The result says
nothing about all shortest reset words for the complete automaton, or
about generic synchronizing automata. Independent mathematical review
has not been performed.

## References

1. M. Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245v1,
   first public posting 25 August 2026, especially Sections 2.1, 2.4.
   https://arxiv.org/abs/2608.24245
2. V. V. Gusev, *Synchronizing automata with random inputs*,
   arXiv:1404.6731v1 (27 April 2014), Section 3, Lemma 1, Fig. 3,
   Theorems 3 and 4. https://arxiv.org/abs/1404.6731
