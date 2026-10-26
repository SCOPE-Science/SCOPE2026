# Review

## Correctness

**PASS.** The code definition matches the primary source's two boundary TRL cases. The NMDS membership test implements its necessary-and-sufficient criteria, and the Euclidean hull identity \(\dim\operatorname{Hull}(C)=5-\operatorname{rank}(GG^{\mathsf T})\) follows from the kernel of the Gram matrix. The checker enumerates all \(1296\) nonzero parameter pairs for each twist position and uses exact arithmetic modulo 37. It reproduces the counts and exception lists and returns `VERIFY_OK`.

## Originality

**PASS, with a stated residual risk.** The primary paper gives the general NMDS criteria and two examples, but not this complete Euclidean-hull census. Focused searches for the exact TRL parameters, Euclidean hull, LCD status, Gram rank, and the listed parameter pairs returned no exact matching result. Generalized Roth–Lempel hull papers are related, but the accessible abstracts do not establish this exact finite census. One relevant full text remained inaccessible, so global novelty is not claimed beyond the stated scope.

## Value

**PASS.** The census distinguishes LCD and one-dimensional-hull members among two explicit NMDS families with identical \([13,5,8]_{37}\) parameters. The exact parameter lists are useful for selecting a code with the desired Euclidean-hull behavior; the distinction is not implied by NMDS status alone.

## Closest literature and limitations

- Lei–Gu–Zhang–Zhou, *On Twisted Roth-Lempel Codes*, arXiv:2609.17304v1, §§2 and 4, Example 4.4: provides the code family and NMDS criteria, but not the hull census.
- Liu–Wu–Zhou, arXiv:2604.11350v2: related generalized Roth–Lempel work on Hermitian self-orthogonality; only the abstract was available.
- Wu–Liu–Chen–Zhou, arXiv:2609.20453v1: related Galois-hull constructions for generalized Roth–Lempel codes; only the abstract was available, so a residual overlap risk remains.

Self-review: passed. Independent audit: not yet performed.
