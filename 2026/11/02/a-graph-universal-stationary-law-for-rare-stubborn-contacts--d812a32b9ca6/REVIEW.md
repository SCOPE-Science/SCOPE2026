# Scientific review

## Correctness — PASS
All quantities and limits are defined for fixed finite connected undirected regular-agent graphs with midpoint updating, bounded stubborn opinions and positive total stubborn-contact coefficient. The proof constructs a unique stationary law by a positive-probability strict contraction word, derives the stationary disagreement bound from exact changes in squared deviation and the weighted-Laplacian spectral gap, and couples the mean's stationary law to the contractive scalar affine recursion. The scalar random series and its exact variance follow algebraically. The code in `verify_gossip.py` separately rebuilds exact first and second moment equations and checks 290 rational identities/inequalities; finite computation does not establish the infinite theorem. A simultaneous growing-network/vanishing-contact limit is not claimed.

## Originality — PASS, subject to residual literature priority risk
The full 2022 arXiv:2205.14784 and 2023 arXiv:2304.12495 source formulations address transient concentration and expectations, not the fixed-graph, weak-stubborn-contact *stationary full-law* limit. The 2010/2013 Acemoglu--Como--Fagnani--Ozdaglar work provides a general ergodic model and stationary moment equations, and Xing et al. 2020 characterize stationary expectations, but the inspected material does not give the asserted graph-universal Bernoulli-convolution distribution and Wasserstein error. Relevant mathematical aliases, singular limits, stationary moment formulas, and related indexed results were compared. The existence of an unnoticed equivalent weak-coupling result, including in specialist stochastic approximation literature, cannot be excluded.

## Mathematical value — PASS
The published gossip model explicitly varies regular versus stubborn interaction strength, leaving the long-run weak-stubborn regime structurally important. The theorem resolves its entire one-dimensional stationary law for every fixed connected weighted regular network, not merely the known first moment. It separates fast network synchronization from persistent random population-wide drift and supplies a usable quantitative spectral-gap error. The nonvanishing variance \(1/(4N-1)\) for balanced opposing anchors identifies a counterintuitive order-of-limits phenomenon. This is not a routine plug-in of a previously tabulated answer.

## Limits and sources
Principal sources: https://arxiv.org/abs/2205.14784 ; https://arxiv.org/abs/2304.12495 . Stronger-background comparisons: https://arxiv.org/abs/1009.2653 ; https://arxiv.org/abs/2003.14028 . A prior characterization of an equivalent singular invariant law, if found, would defeat the originality assessment. No full priority certification or independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
