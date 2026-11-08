# Independent mathematical audit

## correctness

PASS

For circular mixed binary w with no cyclic 11 and μ(0)=01, μ(1)=00, the 2|w| cyclic rotations partition strictly by prefixes 000 (even 1), 001 (odd 1), 01 (even 0), 1 (odd 0); preceding characters respectively 1,0,1-w_{i-1},0. In the even-0 block, μ reverses the lexical order of original 0-leading rotations (μ(0)>μ(1)); preceding bits are complemented, giving BWT(μ(w))=1^k 0^k complement(reverse(C(w))) 0^z. Tied rotations (nonprimitive w) contribute identical preceding bits so no ambiguity. All μ iterates avoid 11 cyclic, and C_{m+1}=1^(k_m)0^(k_m) complement(reverse(C_m)), C_1=1, C_2=100. Since the suffix/prefix invariant is 1-start/0-end, each iteration m>=2 adds precisely two runs; terminal zeros merge, yielding r(BWT(W_m))=2m-2 for every m>=2. Direct cyclic-rotation sorting independently confirmed the identity for all 187 mixed no-11 words of lengths 2..9 and every iterate through m=9. The all-length proof is by strict order blocks, not experimental extrapolation.

## originality

PASS

PASS qualified: Frosini et al prove general logarithmic order for purely morphic binary words, whereas the complete transform recursion and exact 2m-2 coefficient are not provided. Fici et al study one-step period-doubling BWT-run sensitivity and exhibit arbitrary words with large increments (Lemma 29, Proposition 31), with different quantifiers. The exact fixed-point iteration result and full BWT under cyclic 11 avoidance are not identified as a consequence of those primary statements.

## value

PASS

The cyclic BWT of the canonical period-doubling automatic word is a natural compression/indexing invariant. Exact entire-transform recursion and exact log-run coefficient sharpen prior generic bounds and allow structural construction without repeatedly sorting exponentially many rotations. The simple four-block lemma also applies beyond the fixed point to a motivated natural class of cyclic 11-avoiding words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
