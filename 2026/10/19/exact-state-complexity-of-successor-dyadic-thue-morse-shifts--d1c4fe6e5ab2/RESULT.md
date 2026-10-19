# Exact state complexity of successor-dyadic Thue–Morse shifts

## Finding

Let \(t(n)\) be the parity of the number of ones in the binary expansion of a nonnegative integer. For a positive integer shift \(c\), write \(N(c)\) for the number of states in the smallest deterministic finite automaton with output (DFAO) that, on **every** base-two input word \(w\) read most-significant digit first, returns \(t([w]_2+c)\). Leading zeroes and the empty input are allowed, and an automaton is required to handle them correctly.

**Theorem.** For each integer \(k\ge1\), with \(F_0=0,F_1=1\) and \(F_{m+2}=F_{m+1}+F_m\),

\[
\boxed{N(2^k+1)=2F_{k+4}=N(2^{k+1}).}
\]

Thus the first values for \(k=1,2,3,4,5,6,7,8\) are \(10,16,26,42,68,110,178,288\). This determines an infinite one-above-a-power-of-two family inside the shifted Thue–Morse state-complexity problem.

## Assumptions and scope

Inputs are finite words over \(\{0,1\}\) in most-significant-digit-first order. For a word \(w\), let \([w]_2\) denote its numerical value, with \([\epsilon]_2=0\). The output alphabet is Boolean. No restriction is placed on leading zeroes or on the length of the input. The shift is \(2^k+1\), with \(k\) a positive integer. We make no claim here for arbitrary shifts.

For a positive integer \(c\), define the finite index set

\[
I_c=\{c\}\cup\left\{\left\lfloor\frac{c}{2^\ell}\right\rfloor,\left\lceil\frac{c}{2^\ell}\right\rceil:\ell\ge1\right\}.
\]

Its **residual fingerprint** at prefix value \(n\ge0\) is \(\Phi_c(n)=(t(n+j))_{j\in I_c}\), in fixed increasing order of indices.

## Proof

**Step 1: exact residual characterization.** The output after a prefix of numerical value \(n\), followed by a suffix of length \(\ell\) with value \(u\in\{0,\ldots,2^\ell-1\}\), is

\[
 t(2^\ell n+u+c).
\]

Write \(c=2^\ell q+r\) with \(0\le r<2^\ell\). The binary digit-parity identity

\[
 t(2^\ell a+b)=t(a)\oplus t(b),\qquad 0\le b<2^\ell,
\]

shows that this suffix output is

\[
 t\!\left(n+q+\left\lfloor\frac{u+r}{2^\ell}\right\rfloor\right)
 \oplus t((u+r)\bmod 2^\ell).
\]

As \(u\) varies, the first argument has offset \(q\) and, when \(r>0\), also \(q+1\). Each such bit can be recovered from a particular suffix output by XOR with the known low-digit parity (take \(u=0\) for \(q\), and \(u=2^\ell-r\) for \(q+1\)). At suffix length zero, the output itself is \(t(n+c)\). Thus two prefix values yield the same output after **every** possible continuation if and only if their fingerprints \(\Phi_c\) agree. Every nonnegative prefix value is reachable as a binary word; by deterministic residual minimization,

\[
\boxed{N(c)=\#\{\Phi_c(n):n\ge0\}.}
\]

In particular the minimal DFAO exists because \(I_c\) is finite. Its states can be the reachable fingerprints, with transition \(\Phi_c(n)\mapsto\Phi_c(2n+b)\) on bit \(b\), and output \(t(n+c)\); the equivalence just proved makes these definitions independent of representative \(n\).

**Step 2: exact dyadic benchmark.** For \(r\ge0\), the carry-offset set for \(c=2^r\) is \(I_{2^r}=\{0,1,2,4,\ldots,2^r\}\), with repetitions discarded. Let \(R_j(n)\) be the length of the consecutive run of binary ones starting at the bit of weight \(2^j\) in \(n\), and put \(e_j=R_j(n)\bmod2\). Adding \(2^j\) changes the binary digit-sum parity by \(1\oplus e_j\), hence

\[
 t(n+2^j)=t(n)\oplus1\oplus e_j.
\]

If \(e_j=1\), then \(R_j(n)\) is odd and \(R_{j+1}(n)=R_j(n)-1\) is even; therefore the vector \((e_0,\ldots,e_r)\) has no adjacent ones. Conversely every length-\(r+1\) binary vector with no adjacent ones is realized by choosing those as the binary digits in positions zero through \(r\) and setting the bit in position \(r+1\) to zero. The free bit at position \(r+2\) independently chooses either parity \(t(n)\), without modifying the run parities through index \(r\). Consequently the dyadic fingerprints are in bijection with an arbitrary parity bit and a length-\(r+1\) binary word with no adjacent ones. That word count is \(F_{r+3}\), so

\[
\boxed{N(2^r)=2F_{r+3},\qquad r\ge0.}
\]

This known dyadic state-complexity formula was established by Biswas (2026); the argument here supplies the self-contained count used below.

**Step 3: split the successor-dyadic fingerprints.** For \(k\ge1\), direct division by powers of two gives

\[
 I_{2^k+1}=\{0,1,2^k+1\}\cup
 \bigcup_{j=0}^{k-1}\{2^j,2^j+1\}.
\]

The elementary relations \(t(2m+s)=t(m+\lfloor s/2\rfloor)\oplus(s\bmod2)\) and \(t(2m+1+s)=t(m+\lfloor(s+1)/2\rfloor)\oplus((s+1)\bmod2)\) hold for every nonnegative integer \(s\). Moreover, index-set calculations yield

\[
 \left\{\left\lfloor\frac{s}{2}\right\rfloor:s\in I_{2^k+1}\right\}=I_{2^{k-1}},
 \qquad
 \left\{\left\lfloor\frac{s+1}{2}\right\rfloor:s\in I_{2^k+1}\right\}=I_{2^{k-1}+1}.
\]

The independent, predetermined XOR bits are immaterial to injectivity. Accordingly even prefix values \(n=2m\) contribute exactly \(N(2^{k-1})\) distinct fingerprints, and odd prefix values \(n=2m+1\) contribute exactly \(N(2^{k-1}+1)\).

These two fingerprint families are **disjoint**. Indeed \(\{0,1,2,3\}\subseteq I_{2^k+1}\). For even \(n\), the two pairs of adjacent output bits \((t(n),t(n+1))\) and \((t(n+2),t(n+3))\) each consist of opposite bits. For odd \(n=2m+1\), those two pairs would both have opposite bits only if

\[
 t(m)=t(m+1)=t(m+2).
\]

No three consecutive Thue–Morse bits are constant: every length-three interval contains an even position \(2a\) followed by \(2a+1\), whose bits are opposite. Hence no odd fingerprint can coincide with an even fingerprint. We have proved the exact identity

\[
\boxed{N(2^k+1)=N(2^{k-1})+N(2^{k-1}+1),\quad k\ge1.}
\]

**Step 4: solve the recursion.** Put \(H_k=N(2^k+1)\) for \(k\ge0\), so \(H_0=N(2)\). The dyadic count gives \(H_0=2F_3=6\). Combining the partition with the dyadic benchmark yields, for \(k\ge1\),

\[
 H_k=H_{k-1}+2F_{k+2}.
\]

The Fibonacci summation identity \(\sum_{j=1}^kF_{j+2}=F_{k+4}-F_4\), together with \(F_4=3\), gives \(H_k=6+2(F_{k+4}-3)=2F_{k+4}\). By the dyadic formula, this also equals \(N(2^{k+1})\), completing the proof.

## Verification

The accompanying standalone Python checker uses exact integer arithmetic and no outside packages. It independently constructs each finite residual offset set, exhaustively enumerates all low-order residues together with all four possible adjacent high-order Thue–Morse pairs, and checks the claimed even/odd partition and total cardinality for \(1\le k\le8\). This low/high enumeration exhausts **all possible** fingerprints at each tested shift: for a block size larger than the offset set, every value \(t(n+s)\) depends only on the low residue and one of \(t(h),t(h+1)\), and all four pairs occur among \(h\in\{0,1,2,5\}\).

A separate suffix-output calculation checks the equivalence between residual signatures and fingerprints for forty small shifts on seventy prefix values per shift. The verified output includes the marker `VERIFICATION_OK`. These finite checks corroborate the proof and are not the basis of the all-\(k\) conclusion.

To reproduce from the packaged files: run `python3 checker.py` in the directory containing the included checker. Its expected console output is supplied as `checker_output.txt`.

## Relationship to prior work

Moradi, Rampersad, and Shallit (arXiv:2512.10017, first public version 2025-12-10; reviewed version 2026-04-02), Section 4.2 and Open Problem 2, develop state-complexity bounds for general Thue–Morse shifts and explicitly ask for exact formulas in the shift parameter. Biswas (2026) solves the distinct subfamily of pure dyadic shifts \(c=2^r\), obtaining \(N(2^r)=2F_{r+3}\). The present claim gives a separate complete formula for the **successor-dyadic shifts** \(c=2^k+1\) and an exact even/odd fingerprint decomposition not stated in the inspected material.

OEIS A382296 already lists numerical state complexities for individual shifts, including all finite indices used for comparison. Accordingly we do **not** claim previously unknown individual numerical values or a new formula for pure dyadic shifts. The contribution claimed here is the infinite successor-dyadic law, its exact recurrence, and the proof by parity-disjoint residual classes.

## Limitations

The proof is for every positive integer \(k\), but only shifts exactly one above a power of two. It does not answer the general-shift open problem. Mathematical correctness has been reviewed using the complete proof and reproducible finite checks; no independent external scientific audit has been performed. The literature comparison does not exclude unindexed, unpublished, or differently stated equivalent results.

## References

- D. Moradi, N. Rampersad, and J. Shallit, *Complexity of Linear Subsequences of \(k\)-Automatic Sequences*, arXiv:2512.10017 (first posted 2025-12-10; version 5 dated 2026-04-02), especially Section 4.2 and Open Problem 2. https://arxiv.org/html/2512.10017v5
- R. Biswas, *State Complexity of Thue-Morse Shifts by Powers of Two* (2026), full textual mathematical source and proof. https://github.com/rnbguy/proofs/blob/main/A382296/A382296.typ
- N. J. A. Sloane et al., *The On-Line Encyclopedia of Integer Sequences*, sequence A382296 (state complexity of Thue–Morse translations; individual computed values and pure-dyadic formula). https://oeis.org/A382296/internal
