# Self-review

## Correctness
PASS. Exact indicator identities give the finite-sample covariance and variance and hence equation (1). The rare-endpoint scaling \(t=c/n\) yields a locally uniform limit \(c^2/(e^c-1)\). The substantive global step is a uniform inequality in \(u=nt\) showing that all candidate optimizers must stay in a compact positive \(u\)-window; this excludes both boundary-escape regimes. The limit profile has a unique maximum at the positive root of \((2-c)e^c=2\). The argument proves the limit and localization of every optimizer, including existence and parameter boundaries. A separate exact-rational finite replay confirms the moment identities but is not used as an infinite proof.

## Originality
PASS with residual bibliographic risk. The 2022 primary text gives the discrete-uniform two-draw case, quotes a universal \(1/n\) extreme-correlation upper bound, and raises nonuniform probability-vector optimization as a distinct direction. Those statements neither imply the sharp constant in the restricted three-state family nor determine the unique rare-mass scale. A related 2021 article concerns optimizing nonlinear transformations of order statistics for fixed discrete parents; its complete full text was not available in the inspected material. Candidate-specific published-record and mathematical database searches did not find the same sharp asymptotic and all-optimizers localization. General older occupancy/dependence theory may still implicitly cover it.

## Value
PASS. The theorem identifies how endpoint masses must shrink to retain optimal order-statistic correlation as the iid sample grows. It sharpens the general \(1/n\) envelope to the exact coefficient within a nontrivial natural family, proves a unique universal scaling law, and demonstrates why fixed equal probabilities become exponentially inferior.

## Closest literature and limitations
Papadatos, arXiv:2205.14360v1 (2022), is the motivating paper; Székely–Móri (1985) gives the universal rectangular-distribution bound; López-Blázquez and Salamanca-Miño (2021), DOI 10.1007/s00180-021-01103-5, treats functional maximal correlation for discrete parents. The conclusion is restricted to ordinary Pearson correlation and symmetric masses on three equally spaced points. The 2021 full text and older terminology-based equivalents remain bibliographic risks.

Self-review: passed. Independent audit: not yet performed.
