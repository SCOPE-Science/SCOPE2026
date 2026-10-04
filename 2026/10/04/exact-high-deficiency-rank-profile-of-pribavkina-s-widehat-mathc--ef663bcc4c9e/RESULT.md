# Exact high-deficiency rank profile of Pribavkina's \(\widehat{\mathcal F}(k,u)\) automata
## Finding
Let \(A\) be a finite alphabet, let \(k\ge 2\), and let \(u=u_1u_2\cdots u_k\in A^k\) be unbordered. Consider Pribavkina's completed semi-flower automaton \(\widehat{\mathcal F}(k,u)\) on
\[
Q=\{0,1,\ldots,2k-1\}.
\]
Its transitions are
\[
\delta(i,u_i)=i+1,\qquad \delta(i,b)=k+i\quad(b\ne u_i),\qquad 1\le i<k,
\]
\[
\delta(k,u_k)=0,\qquad \delta(k,b)=1\quad(b\ne u_k),
\]
\[
\delta(i,b)=i+1\quad(k+1\le i<2k-1),\qquad \delta(2k-1,b)=1,
\]
for every \(b\in A\), while \(0\) is a sink.

Define
\[
\lambda_{k,u}(s)=\min\{|w|:|Qw|\le 2k-s\}.
\]
Then for every \(k\le s\le 2k-1\),
\[
\boxed{\lambda_{k,u}(s)=k+(s-k)(k+1)}.
\]
Equivalently, for every \(0\le r\le k-1\), the minimum length needed to reach rank at most \(k-r\) is
\[
k+r(k+1).
\]
For every chosen letter \(a\in A\), the word
\[
w_r=u(au)^r
\]
has exactly this length and has image rank exactly \(k-r\).

The endpoint \(r=k-1\) recovers Pribavkina's reset threshold \(k^2+k-1\); the intermediate values are the new rank-compression profile.

## Assumptions and scope
A word is unbordered when no nonempty proper prefix is also a suffix. Word length counts input letters. Transformation rank means image cardinality \(|Qw|\). The result applies to every finite alphabet and every unbordered \(u\); it does not require the additional hypotheses \(k>|A|\) or that every alphabet letter occur in \(u\), which Pribavkina uses only to ensure properness of the automaton.

The claim concerns only the high-deficiency range, from rank \(k\) down to rank \(1\). Shorter-rank thresholds above \(k\) can depend on the letter pattern of \(u\), so no formula is asserted there.

## Proof
Define a phase map on the nonzero states by
\[
\phi(1)=0,
\]
and, for \(1\le j\le k-1\),
\[
\phi(j+1)=\phi(k+j)=j\pmod k.
\]
Every transition that stays outside the sink increases phase by one modulo \(k\). Thus images of states from two different surviving phases can never coincide.

For each phase choose the representative
\[
p_0=1,\qquad p_j=k+j\quad(1\le j\le k-1).
\]
Call phase \(j\) killed by a word \(w\) if every state of that phase is sent to \(0\); in particular \(p_jw=0\). If \(t\) phases survive, their images have distinct phases, so together with the sink,
\[
|Qw|\ge 1+t.
\]
Therefore \(|Qw|\le k-r\) forces at least \(r+1\) killed phases.

Now fix a killed phase \(j\). Starting from \(p_j\), the only way to enter \(0\) is to traverse
\[
1\xrightarrow{u_1}2\xrightarrow{u_2}\cdots\xrightarrow{u_{k-1}}k\xrightarrow{u_k}0.
\]
Hence \(w\) contains a full occurrence of \(u\). If that occurrence starts at position \(s\), the phase rule gives
\[
s-1\equiv -j\pmod k.
\]
Thus distinct killed phases yield occurrences of \(u\) whose starting positions lie in distinct residue classes modulo \(k\).

Because \(u\) is unbordered, two occurrences of \(u\) in the same word cannot overlap: a shift strictly between \(1\) and \(k-1\) would produce a nontrivial border. After sorting occurrences attached to \(r+1\) killed phases, consecutive starts differ by at least \(k\); they cannot differ by exactly \(k\), or by any multiple of \(k\), because their residues modulo \(k\) are distinct. Hence consecutive selected starts differ by at least \(k+1\). A word containing these \(r+1\) occurrences therefore has length at least
\[
k+r(k+1).
\]
This proves the lower bound.

For the upper bound, first read \(u\). State \(1\) reaches the sink. For each \(1\le j\le k-1\), the two states of phase \(j\), namely \(j+1\) and \(k+j\), are merged by \(u\). Indeed, after the first \(k-j\) letters of \(u\), the tail state \(k+j\) reaches state \(1\). Starting from \(j+1\), those same \(k-j\) letters cannot all follow the upper path, since that would make the prefix \(u_1\cdots u_{k-j}\) equal to the suffix \(u_{j+1}\cdots u_k\), a nontrivial border. At the first mismatch the path enters the tail and, after the remaining letters of this prefix, also reaches state \(1\). The remaining \(j\) letters of \(u\) therefore act identically on the pair. Consequently, after the first copy of \(u\) there is at most one nonzero image state in each phase.

In
\[
w_r=u(au)^r,
\]
the displayed \(r+1\) copies of \(u\) start in \(r+1\) distinct residue classes modulo \(k\). They therefore kill at least \(r+1\) distinct phases. Since the first \(u\) has already merged each surviving phase to at most one state, later deterministic actions cannot split a phase. Thus
\[
|Qw_r|\le 1+k-(r+1)=k-r.
\]
The lower bound just proved applies to \(w_r\), whose length is exactly \(k+r(k+1)\); hence its rank is exactly \(k-r\), and equality holds in the threshold formula.

## Verification
The standalone verifier `artifacts/verify_pribavkina_profile.py` reconstructs the automaton directly from the transition definition, computes exact power-automaton distances, and checks the claimed thresholds and witness ranks for every binary unbordered word of lengths \(2\) through \(7\) and every ternary unbordered word of lengths \(2\) through \(5\). It checks \(84\) binary and \(216\) ternary words and ends with `VERIFY_OK`.

These finite computations are stress tests only. The all-parameter statement is proved by the phase and nonoverlap argument above.

## Relationship to prior work
Pribavkina introduced the automata \(\widehat{\mathcal F}(k,u)\) from the incomplete set \(A^k\setminus\{u\}\), proved the equivalence between incompletable words and reset words, and proved that the shortest reset word has length \(k^2+k-1\). Her proof analyzes repeated occurrences of \(u\) through forbidden positions, but the paper states only the rank-one endpoint, not the minimum lengths for the intermediate image ranks \(k,k-1,\ldots,1\).

Volkov's later survey discusses transformation rank in general and cites Pribavkina's series in the section on automata with a zero state, again recording reset-threshold behavior rather than an intermediate-rank profile. Searches under rank compression, transformation rank, incomplete-set automata, semi-flower automata, and incompletable-word terminology did not identify a published formula equivalent to the one above.

The closest related exact results found in the checked research database concern other slowly synchronizing families, especially the exact avoiding profile of the Černý automata and finite slow-reset censuses. Those statements concern different invariants and do not imply this profile.

## Limitations
The theorem gives only the range of target ranks at most \(k\). For ranks above \(k\), the shortest compression length depends on the internal letter pattern of \(u\); exhaustive checks already show different low-deficiency profiles for different unbordered words of the same length.

Originality is stated subject to the residual possibility that an older paper on incomplete sets or transformation rank contains the same intermediate-rank formula under different terminology. No such statement was found in the inspected primary paper, the inspected survey treatment, or the checked research database.

## References
1. E. V. Pribavkina, “Slowly Synchronizing Automata with Zero and Incomplete Sets,” arXiv:0907.4576v1, 27 July 2009; journal version: *Mathematical Notes* 90 (2011), 411–417, DOI 10.1134/S0001434611090094.
2. E. V. Pribavkina, “Slowly Synchronizing Automata with Zero and Uncovering Sets,” *Matematicheskie Zametki* 90 (2011), 422–430, DOI 10.4213/mzm6191.
3. M. V. Volkov, “Synchronization of finite automata,” *Russian Mathematical Surveys* 77 (2022), 819–891, DOI 10.4213/rm10005e.
