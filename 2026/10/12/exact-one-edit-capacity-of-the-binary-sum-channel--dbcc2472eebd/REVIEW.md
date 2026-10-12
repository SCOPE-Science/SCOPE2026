# Scientific review

## Correctness — PASS

For each fixed prefix of \(n-1\) input columns, the possible remaining columns form a binary distance-at-least-three code: changes in one or two positions alter exactly two bits of the augmented sum matrix, which makes the corresponding one-substitution balls intersect. This independently establishes an upper bound of \(2^{\ell(n-1)}A_2(\ell,3)\) for **all**, including nonlinear, codes. The matching row-parity-seed construction corrects substitutions via row-syndrome decoding and length-changing edits via unmodified rows. Its cardinality has been counted without approximation. Independent exhaustive tests of three small constructions and a length-eight nonlinear seed succeed; no finite computation is used as an infinite proof.

## Originality — PASS, with identified residual risk

Abboud–Yaakobi [1, Section V] proves the lower-bound construction with an arbitrary distance-three seed but stops at a coarser sphere-packing upper bound, giving a one-bit gap for arbitrary row counts. The present claim establishes a sharper upper bound and an exact identity for the same channel. The established binary-code-size tables [2,3] contain the classical invariant and the twenty-word example but not this channel identity. Searches over relevant published mathematical records did not identify an equivalent statement, although a general Cayley-graph/Cartesian-product independence theorem or an unindexed subsequent paper could offer another route to the same conclusion; absence from search is not a proof of uniqueness.

## Value — PASS

The result determines the exact maximum cardinality at all allowed frame lengths for the one-edit and one-substitution versions of a newly studied distributed-storage channel, reducing a previously open gap to the well-studied classical invariant \(A_2(\ell,3)\). It also identifies an explicit improvement obtained from a known nonlinear distance-three seed. It makes no new claim about unknown values of the classical invariant and does not assert a fixed-length message-bit improvement at non-power-of-two cardinalities.

## Closest work and limitations

[1] L. Abboud and E. Yaakobi, *Error-Correcting Codes for the Sum Channel*, arXiv:2601.10256v2, https://arxiv.org/html/2601.10256v2 (Section V-B, Construction 4, Theorem 4, and Theorem 5).

[2] Classical table of binary code bounds, https://aeb.win.tue.nl/codes/binary-1.html ; [3] P. R. J. Östergård, T. Baicheva, and E. Kolev, binary \((8,20,3)\) code examples, https://users.aalto.fi/~pat/opt/20.txt .

Self-review: passed. Independent audit: not yet performed.
