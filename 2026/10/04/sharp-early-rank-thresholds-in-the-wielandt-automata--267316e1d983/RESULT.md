# Sharp early rank thresholds in the Wielandt automata
## Finding
For the labeled \(n\)-state Wielandt automaton \(W_n\) on \(Q=\{0,\ldots,n-1\}\), where \(b(i)=i+1\pmod n\), \(c(0)=c(1)=2\), and \(c(i)=i+1\pmod n\) for \(2\le i<n\), let \(\lambda_n(s)=\min\{|w|:|Qw|\le n-s\}\). For every \(n\ge3\) and \(1\le s\le\lceil n/2\rceil\), \(\lambda_n(s)=2s-1\), and the unique word of that minimum length attaining rank at most \(n-s\) is \(c(bc)^{s-1}\). Moreover, when \(n\ge4\) and \(s_0=\lceil n/2\rceil\), the next threshold is strictly larger than the counting lower bound: \(\lambda_n(s_0+1)>2s_0+1\).

Thus the initial compression profile of this classical slowly synchronizing family is exactly linear through half of the state set, with a unique optimal alternating word at every threshold in that range. The linear regime then fails immediately after \(s_0=\lceil n/2\rceil\) whenever a further rank drop is possible.

## Assumptions and scope
Words act from left to right. The state set is \(Q=\{0,\ldots,n-1\}\). The letter \(b\) is the cyclic permutation \(i\mapsto i+1\pmod n\). The letter \(c\) is given by \(c(0)=c(1)=2\) and \(c(i)=i+1\pmod n\) for \(2\le i<n\). This labeling is a rotation of the standard unique two-letter coloring of the Wielandt digraph. The quantity \(\lambda_n(s)\) asks for the shortest word whose image has cardinality at most \(n-s\); it is an intermediate-rank threshold, not the reset threshold.

## Proof
The letter \(b\) is a permutation, so it never changes image size. The letter \(c\) has exactly one collision, namely \(0c=1c=2\), and therefore decreases the cardinality of any image set by at most one. Moreover, an application of \(c\) decreases cardinality exactly when the current image contains both \(0\) and \(1\). After every application of \(c\), state \(1\) is absent from the image.

Suppose a word decreases the rank by at least \(s\). It must contain at least \(s\) effective occurrences of \(c\). Between two consecutive effective occurrences of \(c\), at least one \(b\) is necessary, because immediately after an effective \(c\) the image omits \(1\), while another \(c\) cannot restore it. Hence every such word has length at least \(s+(s-1)=2s-1\).

Equality forces all of these inequalities to be tight: there are exactly \(s\) occurrences of \(c\), all effective, exactly \(s-1\) occurrences of \(b\), no letter before the first effective \(c\), no letter after the last one, and exactly one \(b\) between successive effective \(c\)'s. Therefore the only possible equality word is
\[
w_s=c(bc)^{s-1}.
\]

It remains to show that \(w_s\) is effective throughout the stated range. Write \(H_s=Q\setminus Qw_s\) for its set of missing states. Since \(Qc\) omits only \(1\),
\[
H_1=\{1\}.
\]
Whenever a set before applying \(c\) contains both \(0\) and \(1\), the missing-state update under \(c\) is
\[
H\longmapsto \{1\}\cup\{h+1\pmod n:h\in H\}.
\]
For \(1\le s<\lfloor n/2\rfloor\), induction gives
\[
H_s=\{1,3,\ldots,2s-1\}.
\]
After the intervening \(b\), these holes become \(\{2,4,\ldots,2s\}\), which omit neither \(0\) nor \(1\); hence the next \(c\) is effective and produces \(H_{s+1}=\{1,3,\ldots,2s+1\}\).

If \(n\) is even, this reaches \(s=n/2\) with all odd states missing. If \(n=2m+1\) is odd, at \(s=m\) the missing set is \(\{1,3,\ldots,n-2\}\); one further \(bc\) changes it to \(\{0,1,3,\ldots,n-2\}\), of size \(m+1=\lceil n/2\rceil\). Thus \(|Qw_s|=n-s\) throughout \(1\le s\le\lceil n/2\rceil\), proving both the upper bound and, together with the counting argument, the exact formula and uniqueness.

Finally let \(s_0=\lceil n/2\rceil\). If \(n\) is even, the image after \(w_{s_0}\) is the set of even states; the following \(b\) yields only odd states, so \(0\) is absent and the next \(c\) is ineffective. If \(n\) is odd, the image after \(w_{s_0}\) is \(\{2,4,\ldots,n-1\}\); the following \(b\) omits \(1\), so again the next \(c\) is ineffective. Since equality at deficiency \(s_0+1\) would force the unique alternating pattern just proved, equality is impossible. Therefore \(\lambda_n(s_0+1)>2s_0+1\) whenever \(n\ge4\).

## Verification
The proof is symbolic and valid for all stated \(n\) and \(s\). The included `verify.py` independently constructs the power automaton for every \(3\le n\le14\), computes exact shortest distances from the full state set, counts all shortest words attaining each target rank, verifies \(\lambda_n(s)=2s-1\) and uniqueness of \(c(bc)^{s-1}\) through \(\lceil n/2\rceil\), and checks the strict boundary inequality. `CHECK.txt` records the replay result.

## Relationship to prior work
Ananichev, Gusev, and Volkov introduced the unique coloring \(W_n\) in this synchronization context and proved its reset threshold \(n^2-3n+3\). Their proof and the later relation to the Černý automata note that a cyclic letter preserves cardinality and the merging letter decreases it by at most one, but they do not state the intermediate-rank profile proved here. Gusev and Pribavkina later generalized Wielandt-type automata and determined reset thresholds for families with two cycle lengths; the published statement concerns reset thresholds rather than these early rank thresholds. Kari, Ryzhikov, and Varonka study shortest words of minimum rank and explicitly revisit the Wielandt automaton when building higher-rank examples, but their Wielandt discussion uses its reset threshold and derived automata of prescribed minimum rank rather than the exact best-target threshold \(\lambda_n(s)\) inside \(W_n\).

## Limitations
The originality check covered the principal Wielandt/reset-threshold sources, a later full-text minimum-rank treatment that explicitly discusses the Wielandt automaton, and targeted searches for equivalent rank/compression formulations. No source inspected states or implies the exact half-range profile with unique optimal words. Because the proof is elementary once the rotated labeling is fixed, an older unindexed note, exercise, or alternate terminology could still contain the same observation. The finite replay is corroboration only; the infinite statement rests on the proof above.

## References
1. D. S. Ananichev, V. V. Gusev, M. V. Volkov, *Slowly Synchronizing Automata and Digraphs*, arXiv:1005.0129v1 (2010), MFCS 2010, pp. 55–65.
2. V. V. Gusev, E. V. Pribavkina, *Reset Thresholds of Automata with Two Cycle Lengths*, arXiv:1403.3992v1 (2014), CIAA 2014.
3. J. Kari, A. Ryzhikov, A. Varonka, *Words of Minimum Rank in Deterministic Finite Automata*, DLT 2019, pp. 74–87, DOI 10.1007/978-3-030-24886-4_5.
