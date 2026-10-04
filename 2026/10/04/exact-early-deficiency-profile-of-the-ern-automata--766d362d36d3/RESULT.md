# Exact early deficiency profile of the Černý automata
## Finding
For the standard \(n\)-state Černý automaton \(C_n\) on \(Q=\mathbb Z/n\mathbb Z\), let
\[
 a:i\mapsto i+1\pmod n,
 \qquad
 b:i\mapsto\begin{cases}0,&i=n-1,\\ i,&0\le i\le n-2.\end{cases}
\]
For \(1\le s\le n-1\), define
\[
\lambda_n(s)=\min\{|w|:|Qw|\le n-s\}.
\]
Then, for every \(n\ge3\) and every \(1\le s\le\lceil n/2\rceil\),
\[
\boxed{\lambda_n(s)=3s-2}.
\]
A shortest witness is
\[
w_s=b(a^2b)^{s-1}.
\]
Thus the first half of the rank-collapse profile of the classical Černý family is exactly linear, even though the final reset threshold is quadratic.

## Assumptions and scope
The automaton convention is the displayed one; cyclic relabelings or exchanging the usual conjugate presentation give the same rank-length invariant. A letter \(b\) is called *effective* on a current image set when applying it decreases the image cardinality. The theorem concerns reaching rank at most \(n-s\) from the full state set. It does not claim a formula for \(s>\lceil n/2\rceil\).

## Proof
Only \(b\) can decrease rank, because \(a\) is a permutation. Moreover one occurrence of \(b\) can decrease rank by at most one, since it identifies only the pair \(\{0,n-1\}\). Hence any word with image size at most \(n-s\) contains at least \(s\) effective occurrences of \(b\).

After an effective \(b\), the state \(n-1\) is absent from the current image. Consider the segment before the next effective \(b\). If the segment contains no \(a\), then \(n-1\) remains absent, so no later \(b\) can be effective. If the segment contains exactly one \(a\), then immediately after that \(a\), state \(0\) is absent: the only predecessor of \(0\) under \(a\) is \(n-1\), which was absent. Subsequent \(b\)'s without another \(a\) cannot decrease rank. Indeed, if \(n-1\) is absent they do nothing; if \(n-1\) is present while \(0\) is absent, applying \(b\) replaces \(n-1\) by \(0\), preserving cardinality and again leaving \(n-1\) absent. Therefore at least two occurrences of \(a\) lie between consecutive effective occurrences of \(b\).

A word producing deficiency at least \(s\) consequently has length at least
\[
s+2(s-1)=3s-2.
\]

It remains to attain this bound. Apply \(w_s=b(a^2b)^{s-1}\). After the \(j\)-th effective \(b\), the missing-state set is
\[
M_j=\{1,3,\ldots,2j-3,n-1\},
\]
where the odd progression is empty for \(j=1\). This is proved by induction. From \(M_j\), the following \(a^2\) shifts the missing set to
\[
\{1,3,\ldots,2j-1\}.
\]
For every transition with \(j\le s-1\), the hypothesis \(s\le\lceil n/2\rceil\) gives \(2j-1\le n-2\). Thus neither \(0\) nor \(n-1\) is missing before the next \(b\), so that \(b\) is effective and appends \(n-1\) to the missing set. After \(s\) effective occurrences, exactly \(s\) states are missing, so \(|Qw_s|=n-s\). Since \(|w_s|=3s-2\), the lower and upper bounds agree.

## Verification
The included `artifacts/verify_cerny_deficiency.py` independently performs breadth-first search in the image-subset automaton for every \(3\le n\le12\) and every \(1\le s\le\lceil n/2\rceil\). It checks that the exact finite-case threshold is \(3s-2\), verifies the explicit witness, and verifies the stated missing-set formula. The deterministic output is in `artifacts/verification_output.txt`. These finite computations are checks only; the proof above establishes the theorem for all admissible \(n\) and \(s\).

## Relationship to prior work
Pin's 1977 paper introduced systematic bounds for words of prescribed rank and proved a general quartic-in-deficiency bound. Pin's 1978 work on circular automata proved the then-conjectured square bound in the high-rank regime; those results give general upper bounds rather than the exact deficiency profile of the specific Černý family.

Rystsov's 2025 work proves the rank conjecture for Černý-type transformation monoids and obtains reset-threshold results, but its rank threshold is the length of a map of *minimal* monoid rank rather than the shortest word reaching each intermediate rank.

A 2026 exact result for the same Černý family determines the *maximum*, over prescribed \(k\)-sets, of the shortest avoidance length as \(kn\). The present invariant is complementary: deficiency \(s\) asks to avoid *some* \(s\)-set, hence takes the lower envelope over avoided sets. That prior maximum formula neither states nor implies the exact lower-envelope value \(3s-2\) without an additional argument.

Targeted searches under rank, deficiency, partial synchronization, image size, avoiding sets, and the explicit expression \(3s-2\) did not locate this formula. Historical priority is therefore asserted only to the best of the inspected literature.

## Limitations
The formula is proved only through deficiency \(\lceil n/2\rceil\). Beyond that range the repeated \(a^2b\) construction ceases to be effective and the exact profile becomes more complicated. No claim is made about a closed formula for the remaining ranks. An older equivalent formulation may exist under subset-reachability or deficiency terminology not exposed by the inspected indexes.

## References
1. J.-É. Pin, “Sur la longueur des mots de rang donné d’un automate fini,” *C. R. Acad. Sci. Paris Sér. A-B* 284 (1977), 1233–1235. HAL: hal-00017720. The issue text is dated 16 May 1977.
2. J.-É. Pin, “Sur un cas particulier de la conjecture de Černý,” *Automata, Languages and Programming*, LNCS 62 (1978), 345–352. DOI: 10.1007/3-540-08860-1_25.
3. I. Rystsov, “Cerny type automata and rank conjecture,” arXiv:2501.19166 (2025).
4. “Exact k-avoiding thresholds of the Černý automata,” public research record `2026/9/17/SCOPE-cerny-k-avoiding-thresholds--5cdbaf373a0f` (2026).
