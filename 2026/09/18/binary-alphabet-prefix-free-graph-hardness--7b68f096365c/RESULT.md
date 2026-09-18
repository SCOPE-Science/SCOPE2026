# Minimum prefix-free graph construction is NP-complete over a binary alphabet

## Statement

Consider the decision version of minimum prefix-free graph construction (MPFG): given a pangenome over an alphabet, a trigger length `k`, and a threshold `T`, decide whether some set of length-`k` trigger words induces a prefix-free graph of size at most `T`.

**Theorem.** MPFG is NP-complete even when the alphabet is fixed to `{0,1}`. The hardness reduction can be arranged so that the trigger length satisfies `k = O(log N)`, where `N` is the total length of the resulting binary pangenome.

Consequently, over the fixed binary alphabet there is a clean parameter contrast. For every fixed `k`, the exact `O(2^q N)` algorithm of Baláž and Popa is polynomial (indeed linear in `N` up to a constant depending on `k`) because `q <= 2^k`; nevertheless the problem is NP-complete when `k` is allowed to grow only logarithmically with the input length.

## Context

Baláž and Popa introduced the optimization problem and proved three hardness statements: 1-MPFG is NP-hard; k-MPFG is NP-hard for every fixed `k` when the alphabet may grow; and unrestricted MPFG remains NP-hard over an alphabet of size three. Their ternary construction encodes each source symbol as `2 e(a) 2` and uses a third-symbol delimiter to obtain synchronization and a clean guard word.

Their synchronized-code reduction (Lemma 1) is more general. It suffices to give an injective fixed-length code whose codewords occur in concatenations only at aligned positions, together with a guard word `g` such that no codeword occurs in `g t g` for any unaligned non-codeword window `t`, and no such gadget occurs inside an encoded source string. The binary construction below satisfies exactly these hypotheses.

Primary source: A. Baláž and A. Popa, *Towards Optimal Prefix-Free Graph Construction: NP-Hardness and Structural Insights*, arXiv:2609.17353v1, 15 September 2026, especially Section 3.2, Lemma 1, Theorem 3, and Corollary 1.

## Binary synchronized code

Let the source alphabet be `Sigma`, put

\[
\beta=\max\{1,\lceil\log_2 |\Sigma|\rceil\},
\]

and choose an injective map

\[
e:\Sigma\to\{0,1\}^{\beta}.
\]

Define the two-bit map

\[
h(0)=10,\qquad h(1)=11,
\]

extended by concatenation to binary strings. For each source symbol `a`, set

\[
\phi(a)=001\,h(e(a))\,10.
\]

All codewords have the common length

\[
k=2\beta+5.
\]

Use the guard

\[
g=1^k.
\]

### Synchronization

Every codeword starts with the marker `001`. After this initial marker, the substring `h(e(a))10` contains no two consecutive zeroes, because each block `h(b)` starts with `1`, and the final suffix is `10`. Hence `001` cannot start strictly inside a codeword after its first position.

At a codeword boundary, the relevant bits are

\[
\cdots 10\mid 001\cdots .
\]

The two length-three windows that cross the boundary before the next aligned start are `100` and `000`; the next window is the aligned `001`. Therefore, in every concatenation `phi(a)phi(b)`, the marker `001` occurs only at an aligned codeword start. Since every codeword begins with `001`, a codeword can occur only at one of the two aligned positions. Thus the code is synchronized in the sense required by Lemma 1 of Baláž--Popa.

### Guard property

Every codeword begins with `0` and ends with `0`. Let `t` be any non-codeword length-`k` window occurring in a concatenation of two codewords. Consider a hypothetical codeword occurrence inside

\[
gtg=1^k\,t\,1^k.
\]

If the occurrence begins in the left or right guard, its first symbol is `1`, impossible. If it begins at the first symbol of `t`, it is exactly `t`, which is not a codeword. If it begins strictly inside `t`, then its length forces it to extend into the right guard, so its last symbol is `1`, again impossible because every codeword ends in `0`. Hence no codeword occurs in `g t g`.

It remains to show that no penalty gadget can occur in an encoded source string. Such a gadget contains `g=1^k`. In a codeword, the longest possible run of ones occurs when every payload bit is `1`: the final `1` of the prefix `001`, the `2 beta` payload bits, and the first `1` of the suffix `10` form a run of length at most

\[
2\beta+2=k-3<k.
\]

Codeword boundaries contain zeroes, so a run cannot grow across a boundary. Thus `1^k`, and therefore `g t g`, never occurs in an encoded source string.

The hypotheses of the synchronized-code reduction are now satisfied over the binary alphabet. Applying that lemma to the NP-hard 1-MPFG instances of Baláž--Popa gives

\[
\operatorname{OPT}(S')=k\operatorname{OPT}(S)+C
\]

for a computable constant `C`, and hence gives a polynomial-time many-one reduction to binary MPFG.

## NP membership

For the decision problem, a certificate can list the selected trigger words that actually occur in the pangenome. There are at most `N` distinct relevant length-`k` windows. Given this set, one scans the input strings, determines all internal trigger positions, forms the induced segments, deduplicates the segment labels, and sums the dictionary-label lengths and path lengths. All of these operations are polynomial in the input size. Hence binary MPFG is in NP, and the preceding reduction proves NP-completeness.

## Logarithmic trigger length

The construction uses

\[
k=2\max\{1,\lceil\log_2 |\Sigma|\rceil\}+5.
\]

After unused source symbols are discarded, `|Sigma|` is at most the total source pangenome length `N_0`. The synchronized-code reduction contains encoded copies of the source strings, so the resulting total length `N` is at least `N_0`. Therefore

\[
k=O(\log N_0)=O(\log N).
\]

Thus the NP-hard family already lies in the logarithmic-trigger regime.

## Fixed-k contrast

Baláž and Popa give an exact algorithm running in `O(2^q N)`, where `q` is the number of distinct candidate trigger words occurring in the pangenome. Over `{0,1}`, one always has `q <= 2^k`. Hence for each fixed `k`, binary k-MPFG is solvable in

\[
O(2^{2^k}N),
\]

which is linear in `N` with a `k`-dependent constant. The theorem therefore shows that the binary-alphabet problem changes from polynomial for every fixed trigger length to NP-complete already by `k=O(log N)`.

This does not claim that logarithmic growth is a sharp threshold: intermediate regimes remain open.

## Finite verification

`artifacts/verify_binary_code.py` exhaustively checks, for `beta=1,...,6`, all codewords and all length-`k` windows in every pairwise codeword concatenation. It verifies synchronization, the full guard condition for every resulting non-codeword window, and the strict bound on runs of ones. The recorded output is in `artifacts/verification.txt`.

These finite checks are sanity tests only. The theorem is proved by the general argument above.

## Originality and limitations

To the best of our knowledge, the binary-alphabet strengthening is not stated in the existing literature. The motivating preprint explicitly proves hardness for alphabet size three, while its fixed-trigger-length theorem uses an alphabet that grows with the source instance. Searches for binary-alphabet MPFG/prefix-free-graph hardness and equivalent trigger-selection formulations found no prior binary result. The source preprint is extremely recent, so a near-simultaneous observation or a later revision remains a material originality risk.

The binary code itself is an elementary self-synchronizing construction; no novelty is claimed for binary synchronization coding as a general subject. The contribution is its use to satisfy the exact guard hypotheses of the MPFG reduction and thereby close the alphabet-size gap from three to the minimum nontrivial alphabet size two, together with the fixed-k versus logarithmic-k complexity consequence.

The result does not improve the approximation status of MPFG, does not prove hardness for constant `k` over a binary alphabet (which would contradict the finite-candidate exact algorithm unless P=NP), and does not locate the precise growth-rate threshold for `k`.

## References

1. Andrej Baláž and Alexandru Popa, *Towards Optimal Prefix-Free Graph Construction: NP-Hardness and Structural Insights*, arXiv:2609.17353v1 (2026). https://arxiv.org/abs/2609.17353
2. Andrej Baláž and Alessia Petescia, *Prefix-free graphs and suffix array construction in sublinear space*, arXiv:2306.14689 (2023). https://arxiv.org/abs/2306.14689
