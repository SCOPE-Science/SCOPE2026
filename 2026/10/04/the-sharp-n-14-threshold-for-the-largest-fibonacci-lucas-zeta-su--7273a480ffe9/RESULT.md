# The sharp \(N=14\) threshold for the largest Fibonacci–Lucas zeta-sum term
## Finding
Let \(F_j\) and \(L_j\) be the Fibonacci and Lucas sequences, and put \(a_j^F=F_j+F_{2j}\) and \(a_j^L=L_{2j}-L_j\). For \(X\in\{F,L\}\), even \(N\ge 4\), and \(1\le j\le N-2\), define
\[
t_{N,j}^X=N\binom{N-1}{j}a_j^X2^{N-j-1}\zeta(j+1-N).
\]
The smallest even integer \(N_0\) for which \(j=8\) is the unique maximizer of \(\lvert t_{N,j}^X\rvert\), simultaneously for both \(X=F\) and \(X=L\), for every even \(N\ge N_0\), is
\[
N_0=14.
\]
At \(N=12\), the unique maximizer is \(j=10\) for both sequences.

## Assumptions and scope
The normalization and index range are exactly those of equation (27) in Danesh, arXiv:2609.33564v1. The claim concerns even degrees only and the two weight sequences above. Odd-indexed summands vanish because their zeta arguments are negative even integers. No statement is made for other recurrence weights or altered normalizations.

## Proof
For even \(N\) and even \(j\), set \(m=N-j\). Then \(m\ge 2\) is even. From
\[
\zeta(1-m)=-\frac{B_m}{m}
\]
and the definition of \(t_{N,j}^X\), the term magnitude is the exact rational number
\[
\lvert t_{N,j}^X\rvert
=N\binom{N-1}{j}a_j^X2^{m-1}\frac{\lvert B_m\rvert}{m}.
\]
Thus every comparison at a fixed even degree can be made with integer and rational arithmetic alone.

Proposition 7 of arXiv:2609.33564v1 proves that, for both weight sequences, \(j=8\) is the unique largest term index for every even \(N\ge 26\). Its proof identifies \(j=8\) as the unique largest limiting weight, bounds the second weight by the \(j=6\) weight, transfers the strict gap using the total-variation estimate from Theorem 6, and verifies the explicit bound needed at \(N=26\). The source also states explicitly that the threshold \(26\) is sufficient rather than asserted minimal.

It therefore remains only to bridge the six even degrees \(14,16,18,20,22,24\). Exhaustive exact comparison of every even \(j\) in the admissible range gives the following winner, runner-up, and positive gap \(\lvert t_{N,8}^X\rvert-\max_{j\ne8}\lvert t_{N,j}^X\rvert\):

| \(X\) | \(N\) | winner | runner-up | exact gap |
| --- | ---: | ---: | ---: | ---: |
| \(F\) | \(14\) | \(8\) | \(6\) | \(1793792/5\) |
| \(F\) | \(16\) | \(8\) | \(6\) | \(24414208/3\) |
| \(F\) | \(18\) | \(8\) | \(6\) | \(1240702976/5\) |
| \(F\) | \(20\) | \(8\) | \(6\) | \(9515073536\) |
| \(F\) | \(22\) | \(8\) | \(6\) | \(2224780214272/5\) |
| \(F\) | \(24\) | \(8\) | \(6\) | \(373197717635072/15\) |
| \(L\) | \(14\) | \(8\) | \(10\) | \(14055184/15\) |
| \(L\) | \(16\) | \(8\) | \(6\) | \(72550400/3\) |
| \(L\) | \(18\) | \(8\) | \(6\) | \(3703447552/5\) |
| \(L\) | \(20\) | \(8\) | \(6\) | \(199033323520/7\) |
| \(L\) | \(22\) | \(8\) | \(6\) | \(6649987334144/5\) |
| \(L\) | \(24\) | \(8\) | \(6\) | \(223116686262272/3\) |

Every listed gap is strictly positive, so the source theorem and these six exact finite checks prove the assertion for every even \(N\ge14\). At \(N=12\), exact comparison gives \(j=10\) as the unique winner for both sequences, with gaps \(16984\) and \(44968\), respectively, over the runner-up \(j=8\). Hence no smaller even threshold can work, and \(N_0=14\) is sharp.

## Verification
The supplied `verify.py` implements Fibonacci and Lucas recurrences, Bernoulli numbers, and the displayed rational magnitude formula using Python's exact `Fraction` arithmetic. It exhaustively compares all admissible even indices for \(N\in\{12,14,16,18,20,22,24\}\), checks the source's initial weights in equation (46), and checks its explicit numerical inequality (50) exactly. The replay output is stored in `verification_output.txt`, and the decisive finite cases are recorded in `verification_cases.csv`.

The computation is a finite certificate for the bridge and the sharpness witness; it is not being used as an infinite proof. The infinite range \(N\ge26\) is covered by the reconstructed proof of Proposition 7 in the cited source.

## Relationship to prior work
Danesh proves the unique-largest-index statement only for every even \(N\ge26\), expressly saying that \(26\) is sufficient and that no minimal-threshold assertion is made. The same proof notes that \(N=12\) has largest index \(j=10\) for both sequences. The present result closes precisely that finite gap by proving that every intervening even degree from \(14\) through \(24\) already has unique maximum at \(j=8\), thereby determining the exact threshold.

An earlier paper by Danesh establishes the underlying finite Fibonacci–Lucas Bernoulli–zeta identities but does not determine a largest-term threshold. Searches for the exact threshold formulation, its equivalent largest-term statement, and the same objects in a published-result index returned no statement covering \(N_0=14\); the closest Fibonacci records concern different reciprocal-tail invariants.

## Limitations
The result is confined to the exact two weight sequences and finite-sum normalization above. It does not extend the source theorem to arbitrary recurrence-family weights. The novelty search cannot exclude every unpublished or poorly indexed source; it does exclude the directly relevant source, its earlier identity paper, targeted published-result records, and targeted web searches inspected for this claim.

## References
1. Payam Danesh, “Cancellation profiles of Fibonacci-Lucas zeta sums,” arXiv:2609.33564v1, first posted 27 September 2026. https://arxiv.org/abs/2609.33564
2. Payam Danesh, “Bernoulli-Zeta transforms for Fibonacci-type recurrence,” Cambridge Open Engage, Version 1, 12 June 2026, DOI: 10.33774/coe-2026-rxfr3.
