# Binary generalized packing-covering through redundancy 15

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is qualified to the best of our knowledge.

## Claim

The source run proposes:

**The generalized packing--covering conjecture holds for every binary linear code of redundancy at most 15.**

Essayag and Zabokritskiy, arXiv:2609.19098v1, prove the conjecture for every finite field through redundancy 14 and identify the first binary residual parameter triple beyond their reductions as

`rho=15, t=3, R_3(C)=6`,

with their generic dimension estimate giving `k<=78`.

The source run rules out exactly that residual binary case.

## Order-three line-cap bound

Let `C` be a binary `[n,k]_2` code of redundancy `rho` that would violate the generalized packing--covering conjecture at order `t=3`, and put `r=R_3(C)`.

The source run proves the reusable estimate

`k <= 2^(rho-2r+3) - (rho-2r+3)`.                 (1)

A violation implies `d_3(C)>=2r+3`. With `D=C^perp`, the dual-weight step imported from the parent paper gives a generalized-weight lower bound. Set

`h=rho-2r+3`.

After shortening `D` on `rho-h` independent coordinate functionals and puncturing, the source run obtains an `h`-dimensional binary code `E` of length

`N=k+h`

such that every `(h-2)`-dimensional subcode has at most four zero coordinate positions.

Let `G` be a full-rank `h x N` generator matrix for `E`, and view its columns as a multiset `M` in `F_2^h`. An `(h-2)`-dimensional coefficient subspace has a two-dimensional annihilator, so the preceding support statement is equivalent to:

**every two-dimensional vector subspace of `F_2^h` contains at most four columns of `G`, counted with multiplicity.**

### Line-cap lemma

If a multiset `M` of vectors in `F_2^h`, `h>=2`, has mass at most four in every two-dimensional vector subspace, then

`|M|<=2^h`.

Fix a nonzero vector `x`, let `m_0,m_x` be the multiplicities of `0,x`, and let

`L=2^(h-1)-1`

be the number of two-dimensional subspaces through `x`. Summing their multiset masses gives

`|M|+(L-1)(m_0+m_x) <= 4L`.

If `m_0+m_x>=2` for some occupied `x`, this gives `|M|<=2^h`; otherwise `m_0=0` and every nonzero vector occurs at most once, giving the even stronger `|M|<=2^h-1`.

Since `N=k+h`, inequality (1) follows.

## Closing redundancy 15

For

`rho=15`, `t=3`, `r=6`,

we have `h=6`, so (1) gives

`N=k+6<=64`, hence `k<=58` and `n=k+15<=73`.

The binary generalized sphere-covering inequality in this case would require

`V_8(n,6)=sum_{i=0}^6 C(n,i) 7^i >= 2^45`.

By monotonicity in `n`,

`V_8(n,6) <= V_8(73,6) = 20,282,523,983,828`,

but

`2^45 = 35,184,372,088,832`.

This contradiction eliminates the sole residual binary redundancy-15 parameter triple identified by the parent reductions.

## Reproducibility

`artifacts/verify.py` is the exact-arithmetic script embedded in the source report. It reconstructs the residual parameter reduction, checks the `N<=64` line-cap consequence, evaluates the covering volume, and checks the sharpness example for the line-cap lemma.

## Closest prior work

- Essayag--Zabokritskiy, arXiv:2609.19098v1, is the direct parent source and explicitly isolates the residual binary triple.
- Yu--Schwartz, arXiv:2609.14477v1, prove order-two and other rate/asymptotic results that do not settle this finite high-rate case.

The source run searched the exact residual triple, equivalent generalized packing/covering terminology, and finite-geometric line-cap formulations and found no prior result closing this case.

## Limitations

The result is binary at redundancy 15; it does not claim the all-field redundancy-15 statement. The parent preprint was only about one day old, and an older equivalent finite-geometry lemma or a contemporaneous response could reduce originality. No independent review is claimed.
