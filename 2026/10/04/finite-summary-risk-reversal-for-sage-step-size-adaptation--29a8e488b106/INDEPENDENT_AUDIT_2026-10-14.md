# Independent mathematical audit

## correctness

PASS

Let M=(ns barV_s+nt barV_t)/(ns+nt), D=barV_t-barV_s and source scatter S_s. Gaussian covariance gives M independent of (D,S_s), with mean theta and variance sigma^2/(ns+nt). With W=ns S_s/sigma^2 Wishart_r(I,ns-1) and Z=D/(sigma sqrt(1/ns+1/nt)), inverse-Wishart Schur complement yields Q=ns X/Y for independent X~chi2_r and Y~chi2_{ns-r}. For T=(Q/r-1)+ the adaptation residual is (1-r/Q) 1_{Q>r}(1-rho)D. Orthogonal risk decomposition plus independent S=X+Y~chi2_ns and U=X/S~Beta(r/2,(ns-r)/2) yields the displayed exact K beta integral and risk r sigma^2/(ns+nt)+sigma^2 ns K/(nt(ns+nt)). Comparison to source risk r sigma^2/ns yields nt/ns>sqrt(K/r). Independently evaluated K_{4,100}=0.6087790589777287, cutoff 0.3901214743441229, H4=4 exp(-2). ns>=r+1 ensures the covariance inverse a.s. These numbers are only checks, not universal proof. The mapping to the source paper Algorithm 2 could not be independently compared to its full text due access; this is explicitly a limited C provenance risk, whereas the stated estimator and conditional mathematical formula are self-contained and proved.

## originality

PASS

The paper SAGE is known through its primary abstract and source-package step-size transcription to address asymptotic optimality, whereas the new formula isolates finite-dimensional penalty in an explicit Gaussian no-shift setting. Distinct James--Stein external-information estimators have different shrinkage weights and dominance conclusions, so they do not imply the threshold for the exact estimator defined here. No prior Resultary record besides the self-indexed item stated the same risk boundary. Full source paper inaccessible this execution is a bounded remaining equivalence risk.

## value

PASS

An analytically sharp finite-sample failure regime for a proposed distribution-shift adaptive step-size in the no-shift Gaussian benchmark is a motivated counterexample to naively extrapolating asymptotic gains. It quantifies a target/source sample ratio separating improvement from harm and shows how a summary dimension controls the boundary, indicating when a finite-sample safeguard could matter. The statement is limited to the exact estimator defined, not practical SAGE in full generality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
