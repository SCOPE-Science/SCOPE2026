# Independent three-axis audit — 2026-09-24

Reviewer type: separate AI audit. This document records reproducible scientific checks and literature comparison, not a transcript of private reasoning.

## Audited source

- Record: `SCOPE-20260908-064`
- Source path: `2026/09/08/064`
- Inventory source tree: `18bb9710b300ee1e97282422e984dec043417565`
- Audited `RESULT.md` blob: `ccdde6b92971b847ab7b388a41174c16201b2a03`
- Claim audited: exact values of the minimum number `Z_L(N)` of unimodular zeros among reciprocal Littlewood polynomials for even degrees `N=8,10,...,24`, together with minimizer counts and witnesses.

## Correctness — PASS

The table was independently recomputed with exact symbolic arithmetic. For a reciprocal polynomial of degree `N=2m`, the standard substitution `x=cos(theta)` gives

`P(e^{i theta})=e^{im theta}[a_m+2 sum_{k=1}^m a_{m-k}T_k(x)]`.

Since `P(1)` and `P(-1)` are odd integers, neither endpoint is a zero. Fixing `a_0=1` therefore reduces the exhaustive search to `2^m` half-strings. A fresh computation built the Chebyshev polynomial exactly over the rationals, square-free factored it, and used exact Sturm root counts on `(-1,1)`, with multiplicities restored from the square-free factors. Exhausting all 8176 half-strings over the nine degrees reproduced exactly

`Z_L(8,10,12,14,16,18,20,22,24)=2,2,2,6,4,4,6,6,6`

and the stated numbers of minimizers

`2,2,2,22,6,2,12,12,8`.

This also independently confirms the reported non-monotonicity at degrees 14, 16 and 18. The reduction itself proves that all unit-circle roots occur in conjugate pairs and hence the counts are even.

## Originality — PASS relative to the literature checked

The checked literature studies lower bounds and asymptotic growth, but no source found publishes this exact contiguous degree table with minimizer counts. Benjamin Bedert, **On the zeros of reciprocal Littlewood polynomials**, Acta Arithmetica 219 (2025), 297–330, DOI `10.4064/aa231207-20-4`, arXiv `2312.04454`, defines the same quantity `Z_L(N)`, summarizes the earlier finite lower bounds, and proves `Z_L(N) -> infinity`; its introduction records the prior even-degree bound `Z_L(N)>=4` for `N>=14` due to Drungilas, not exact small-degree values. Paulius Drungilas, **Unimodular roots of reciprocal Littlewood polynomials**, J. Korean Math. Soc. 45 (2008), 835–840, likewise proves the lower bound 4 for even degrees at least 14, rather than the nine exact minima audited here.

Checked sources include:
- https://arxiv.org/abs/2312.04454
- https://doi.org/10.4064/aa231207-20-4
- Paulius Drungilas, Journal of the Korean Mathematical Society 45 (2008), 835–840.

Searches included exact `Z_L(14)`, `Z_L(16)`, and table/value queries as well as equivalent phrases for reciprocal Littlewood polynomials and unimodular roots. The originality verdict is therefore relative to the sources checked, not a guarantee of global priority.

## Scientific value — FAIL

The surviving contribution is a correct but very small exhaustive computation: only 8176 canonical polynomials across degrees 8–24. It supplies no new lower-bound mechanism, asymptotic information, structural classification of minimizers, or reusable theorem that advances the open problem studied by Bedert and earlier authors. Several entries merely meet a long-known lower bound, and the finite non-monotonicity does not yield a consequence for the asymptotic question. Under this campaign's value criterion, an arbitrary small exact census and witness list, without a structural result or meaningful new regime, is insufficient for acceptance.

## Repair attempt

A bounded repair was considered by narrowing the record to a benchmark dataset and emphasizing the exact Sturm certificates. That makes the computation reproducible but does not create a structural contribution or a substantive advance on the known theory, so the value failure remains.

## Final disposition

**FAILED** on scientific value; correctness passes and the exact table is original relative to the literature checked. Scientific rejection evidence is published at the source record; archival relocation to the assigned failed-attempt path remains pending and does not affect the scientific verdict.
