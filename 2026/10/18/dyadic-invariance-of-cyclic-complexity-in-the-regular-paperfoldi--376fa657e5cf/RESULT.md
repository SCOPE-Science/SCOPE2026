# Dyadic invariance of cyclic complexity in the regular paperfolding word

## Finding

Let \(f=f_1f_2\cdots\) be the regular binary paperfolding word, with \(f_i=1\) if the odd part of \(i\) is congruent to \(1\) modulo \(4\), and \(f_i=0\) otherwise. Let \(c_f(n)\) be the number of conjugacy classes (cyclic-rotation orbits, not reversal orbits) represented among the length-\(n\) contiguous factors of \(f\).

**Theorem.** For every positive integer \(n\) satisfying \(n\ge 8\) and \(4\mid n\),
\[
  c_f(2n)=c_f(n).
\]
More precisely, deleting the uniquely alternating parity track of a length-\(2n\) factor yields a well-defined **bijection** between conjugacy classes of factors of lengths \(2n\) and \(n\). For all odd \(r\ge3\) and \(k\ge2\), \(c_f(2^k r)=c_f(4r)\); the corresponding power-of-two ray satisfies \(c_f(2^k)=4\) for \(k\ge3\). The lower boundary is sharp: \(c_f(4)=3\) whereas \(c_f(8)=4\).

In particular, for all integers \(j\ge0\), \(c_f(12\cdot2^j)=16\), \(c_f(20\cdot2^j)=28\), and \(c_f(28\cdot2^j)=40\). The initial counts are exhaustive by the known paperfolding factor count and the standalone verifier; the infinite propagation is proved below.

## Assumptions and scope

Words are indexed from position \(1\). A factor is a consecutive word of a finite length appearing anywhere in the one-sided infinite sequence. Conjugacy means equality under a cyclic rotation, whether or not that rotation is itself a factor. A parity track of an even-length word is the subsequence in odd or even word positions. An *alternating track* is a track in which consecutive bits differ. Rotations do not identify reversal or bit complementation.

The theorem is for the **regular** paperfolding word, not an arbitrary nonstationary generalized folding-instruction sequence; the latter's even-index decimation need not reproduce the same word.

## Proof

**Step 1: the parity-decimation law.** By the displayed digit definition, for each \(t\ge1\), \(f_{2t}=f_t\). For each \(t\ge0\), \(f_{2t+1}=1\) exactly when \(t\) is even. Thus the bits on odd global positions form a perfectly alternating sequence. The sequence \(f\) has no alternating factor of length four: any four consecutive positions include two consecutive odd global positions, separated by two in the word, which carry different bits; in an alternating four-letter word the symbols two apart agree.

**Step 2: unique track and phase.** Fix an even factor length \(\ell\ge8\). If a factor begins at an odd global position, its odd-position track is alternating; if it begins at an even global position, its even-position track is alternating. The other track is a contiguous factor of \(f\) of length \(\ell/2\ge4\), by \(f_{2t}=f_t\), and hence is not alternating by Step 1. Thus exactly one track alternates, and the parity of any occurrence's global starting position is uniquely determined by the factor. Write \(\varepsilon(w)\) for this global starting-position parity for any length-\(n\) factor \(w\), \(n\ge8\).

Now assume \(4\mid n\). Each parity track of a length-\(n\) word has even length \(n/2\). Cyclic rotation of the full word by \(r\) positions cyclically rotates the two tracks and exchanges them precisely if \(r\) is odd. An alternating track of even length stays alternating under cyclic rotation, while a nonalternating track stays nonalternating. Consequently, whenever \(w'=\operatorname{rot}_r(w)\) is also a factor, \(\varepsilon(w')\equiv\varepsilon(w)+r\pmod2\).

**Step 3: construct a lift of each factor.** Write an occurrence \(w=w_0\cdots w_{n-1}=f_t\cdots f_{t+n-1}\). Define \(a_j(t)=f_{2(t+j)+1}\); it is alternating in \(j\) and depends only on \(t\bmod2\). Define the interleaved word
\[
L_t(w)=w_0a_0(t)w_1a_1(t)\cdots w_{n-1}a_{n-1}(t).
\]
This is the actual factor of \(f\) of length \(2n\) beginning at global position \(2t\). The length-\(2n\) factor beginning at position \(2t-1\) is the one-position right cyclic rotation of \(L_t(w)\): its initial odd-index bit agrees with \(a_{n-1}(t)\), because the two odd indices differ by \(2n\), divisible by \(4\); every other bit agrees directly.

**Step 4: a well-defined bijection on conjugacy classes.** Every length-\(2n\) factor begins either at position \(2t\) or at position \(2t-1\) for some \(t\ge1\), so Step 3 shows that it is conjugate to a lift \(L_t(w)\) of a length-\(n\) factor \(w\). If \(w'=\operatorname{rot}_r(w)\) is another factor, Step 2 says that the starting-index parities of its occurrences differ by \(r\pmod2\). Consequently its alternating interleaving sequence agrees with that of \(L_t(w)\) after shifting by \(r\), so \(L_{t'}(w')\) is the rotation of \(L_t(w)\) by \(2r\). Thus the lift depends only on the conjugacy class of \(w\), and every conjugacy class of length-\(2n\) factors arises from one of length \(n\).

Conversely, suppose two lifts are cyclic rotations of one another. Each lift has its nonalternating track in the same parity positions: this track is the factor \(w\), which has length \(n\ge8\) and cannot be alternating. The other track is alternating. Hence a conjugating rotation cannot shift by an odd number of positions, which would exchange the tracks. It shifts by \(2r\) positions and therefore makes the nonalternating length-\(n\) tracks cyclic rotations of one another. The two source factors are conjugate. The lift map is injective, and hence bijective, proving \(c_f(2n)=c_f(n)\).

Iteration gives the stated dyadic rays. Exact initial values \(c_f(8)=4\), \(c_f(12)=16\), \(c_f(20)=28\), \(c_f(28)=40\) are obtained by exhaustive finite factor enumeration, certified complete by the previously proved factor-count formula \(p_f(\ell)=4\ell\) for \(\ell\ge7\). The exception \(c_f(4)=3\) follows by enumerating the twelve length-four factors.

## Verification

Run `python3 verify_paperfolding_cyclic.py` with Python \(3\). It independently generates the first \(32768\) symbols via odd-part residues and via the recursion \(f_{2t}=f_t\), checks the absence of alternating four-factors, computes factor sets at twenty lengths divisible by four between \(8\) and \(128\) and their doubles, and checks all twenty paired cyclic-complexity counts. It verifies the known factor count at every tested length to certify that the finite prefix contains **all** possible factors at those lengths, and cross-checks the minimum-rotation routine by naive rotation at small lengths.

The expected terminal marker is `VERIFY_OK independent_paperfolding_recursion_32768_positions factor_exhaustiveness_via_4n 20_doubling_pairs_n_8_to_128 sharp_n4_exception counts_n12_16_n20_28_n28_40`. No finite test substitutes for the all-length proof above.

## Relationship to prior work

Cassaigne, Fici, Sciortino, and Zamboni introduced cyclic complexity and proved, in their section on paperfolding words (Proposition 12), \(c_f(4\cdot2^j)=4\) for \(j\ge1\); this special dyadic ray and the known base value are **not new claims** here. The new theorem establishes **class-by-class doubling invariance for every multiple of four at least eight**, including all odd multipliers and a canonical bijection explaining why the scale invariance occurs. Their proof treats the one power-of-two ray, not the arbitrary-multiplier assertion.

Allouche's factor-complexity theorem gives \(p_f(\ell)=4\ell\) for \(\ell\ge7\) and a parity-of-occurrence separation lemma. These are distinct from cyclic complexity and are used only to certify the finite counts; the present bijection has an independent proof using the explicit regular folding recursion.

## Limitations

The assertion concerns contiguous factors of one specific infinite word, and equality of orbit **counts**, not equality of actual factor sets. The numerical examples require exhaustive finite factor sets, which the checker validates using a previously proved factor-complexity theorem. No claim is made for lengths outside \(4\mid n\) in the doubling theorem, for arbitrary generalized paperfolding words, or for equality of individual factors as strings. The case \(n=4\) fails, while other unproved extensions may exist. Priority beyond the inspected sources and mathematical-record search remains subject to external literature review.

## References

1. J. Cassaigne, G. Fici, M. Sciortino, and L. Q. Zamboni, *Cyclic Complexity of Words*, first arXiv version dated 2014-02-24, arXiv:1402.5843, Section 5.2 and Proposition 12, https://arxiv.org/abs/1402.5843.
2. J.-P. Allouche, *The Number of Factors in a Paperfolding Sequence*, Bulletin of the Australian Mathematical Society **46** (1992), 23–32, especially Lemma 2 and the Section 5 theorem, https://doi.org/10.1017/S0004972700011655.
