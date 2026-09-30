# Independent Audit — Sharp fiber-extreme barriers for sparse Bernoulli tensor norms

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `c6efa2a0f9a88d5264d359e934c0417eddf65cc6`  
**Audited current source tree:** `c6efa2a0f9a88d5264d359e934c0417eddf65cc6`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence, and the dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. The fiber identity is exact: for a fiber with D ones, ||W_F||_2^2=(1-2p)D+np^2. In any fixed mode the n^(k-1) fibers partition the entries and hence have independent Bin(n,p) degrees, while all k modes only change upper bounds by a fixed factor. At d=c log n, the binomial upper tail has the Poisson/Stirling form sqrt(x)/((x-1)sqrt(2 pi d)) exp(-d h(x)) for m/d->x>1. This yields the threshold c h(x_*)=k-1, the center x_*c log n-(log log n)/(2 log x_*), and the displayed lattice limit. The same one-mode lower bound plus all-mode union bound gives the exact polynomial failure exponent above threshold. In the sublogarithmic regime, h((1±eps)x_n)/h(x_n)->1±eps gives polynomial separation and D_max/(d x_n)->1. The Lambert-W inversion is algebraically correct.

## Originality — PASS

PASS, narrowly scoped. Zhou--Zhu explicitly prove only a log-free O(sqrt(np)) tensor norm upper bound at np>=c log n, note that the norm dominates the largest fiber, state only qualitative divergence of the maximum fiber norm for 1<=np=o(log n), and use a slack Chernoff constant for maximum fiber degree. Classical discrete/Poisson triangular-array extreme theory already covers much of the scalar maximum mechanism, so no novelty is credited there. Targeted searches did not locate the tensor-specific exact critical equation, second-order fiber localization, explicit n^{-r} constant obstruction, or Lambert-W sublogarithmic refinement. The originality claim is therefore limited to these consequences for the new sparse-tensor theorem.

## Scientific value — PASS

PASS. The result turns the source theorem's opaque constant C_{k,r,c} into a necessary explicit barrier, quantifies the compulsory fiber contribution as a function of tensor order, sparsity and requested tail exponent, and identifies the actual log-log location of the fiber extreme. It also makes the sublogarithmic failure rate explicit rather than qualitative. These are useful sharpness diagnostics even though they do not determine the full tensor-norm limiting constant.

## Independent checks

- Read the lawful arXiv HTML of Zhou--Zhu 2609.20520v1. Lines 138--142 state the fiber lower-bound mechanism and only qualitative sublogarithmic divergence; Lemma 4.3 uses the Chernoff rate h(kappa) with a sufficient slack constant.
- Re-derived the centered fiber norm identity and the independence of all fibers in one fixed mode.
- Re-derived the Poisson-relative binomial tail prefactor, the -log log n/(2 log x_*) correction, and the one-mode lattice CDF.
- Checked the polynomial-tail lower/upper sandwich and the necessary C>=sqrt(h^{-1}((k-1+r)/c)) obstruction.
- Checked the sublogarithmic large-deviation separation and Lambert-W inversion.
- Compared with Anderson--Coles--Husler and related discrete-extreme literature; scalar extreme-value priority is explicitly not claimed.
- Verified the current main record tree equals the assigned source-tree SHA and the 2026-09-30 audit markers are absent.

## Limitations

- Homogeneous independent Bernoulli entries only.
- The exact lattice law is proved for one fixed mode; cross-mode dependence is used only through upper/lower bounds.
- Classical Poisson/discrete extreme theory may subsume the scalar second-order calculation, and no priority is claimed for that scalar component.
- The theorem gives a lower obstruction, not the full tensor injective-norm asymptotic.

## Evidence and references

- https://arxiv.org/abs/2609.20520
- https://arxiv.org/html/2609.20520v1
- https://doi.org/10.1214/aoap/1043862420
- https://arxiv.org/abs/1911.09063
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/sharp-fiber-extremes-sparse-bernoulli-tensors--e640445683fe

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
