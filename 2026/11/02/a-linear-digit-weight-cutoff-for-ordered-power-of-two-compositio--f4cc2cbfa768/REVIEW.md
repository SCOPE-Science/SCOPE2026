# Self-review

## Correctness — PASS
The unrestricted claim follows from the integral formal-series identity \(S(z)(1-S(z))=z-2T(z)\), the finite geometric expansion modulo \(2^N\), and the fact that an exponent obtained as a sum of \(2r+1\) powers of two has binary weight no greater than \(2r+1\). Addition of \(N-r-1\) proves the advertised bound for every \(n\) and \(N\). Translation into a dyadic counting bound is injective. The verifier independently checks the coefficient identity and many finite valuations. No computation is substituted for the proof.

## Originality — PASS, with residual risk
The closest primary paper is Alkauskas (2010, arXiv:1003.1064v1), whose Theorems 1 and 6 use an exponential-in-precision weight bound on a different shift and whose tables settle small moduli. The complete nine-page text, including its closing improvement, was compared to the linear shifted cutoff, and the statement was not found there. Knopfmacher and Robbins (2003) establish the underlying generating function, recurrence, and parity rather than an all-precision quantitative digital cutoff. Searches for linear digit-weight, equivalent shifted formulations, and the sparsity exponent did not identify stronger published coverage; an unlocated older or newer source remains possible. In particular, existing modulo-four and modulo-eight classifications are not being claimed as new.

## Mathematical value — PASS
For fixed precision \(N\), an exponential digit-weight cutoff implies a potentially much larger polynomial-in-\(\log x\) support envelope. The new all-precision factorization reduces this to \(O_N((\log x)^{2N-1})\), with exponent *linear* rather than exponential in \(N\). It materially sharpens the known rarity phenomenon for this natural ordered-composition sequence. The bound need not be optimal and makes no lower-bound assertion.

## Closest literature and limitations
The 2010 result is the dominant predecessor; the 2003 result supplies its generating-function context. The new statement covers only ordered compositions into powers of two. It does not determine exact residues or the optimal support exponent. Priority has not received independent verification.

Self-review: passed. Independent audit: not yet performed.
