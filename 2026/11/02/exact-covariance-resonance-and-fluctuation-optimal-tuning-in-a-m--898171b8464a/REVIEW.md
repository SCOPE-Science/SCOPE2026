# Scientific review

## Correctness — PASS

The precise theorem specifies real \(0<t<1\), stationary coordinate observables, and an absolutely continuous invariant distribution. The full Markov orbit \(0\to t\to1\to0\) and each inverse branch were checked. Both branches of the second iterate expand uniformly. The transfer operator preserves the four-dimensional space of intervalwise affine densities, where the characteristic polynomial and covariance generating function follow from explicit rational matrix inversion. The covariance denominator's nontrivial factors have roots strictly inside the unit disk; the third-order pole at the resonance is genuinely uncancelled. Direct symbolic identities establish the positive Green--Kubo variance and unique optimization root. Uniform expansion, primitivity, and bounded-variation spectral theory justify mixing and the central limit theorem. `CHECK.py` was executed successfully for exact identities and rational specializations. No empirical observations substitute for the infinite-time proof.

## Originality — PASS within inspected literature

The motivating 2023 conference and full 2023 journal paper introduce and numerically explore tunable-mean piecewise maps but do not derive the stated exact stationary correlation resolvent or the resonance/variance-optimum comparison. The 2014 Papamarkou--Lawrance full-text treatment of autocovariance assumes every individual branch is fully stretching onto the whole interval, which fails here; its formulas therefore do not directly imply this theorem. Alsedà--Misiurewicz--Pérez (2020), Billings--Bollt (2001) and the classical Ito--Tanaka--Nakada results treat invariant densities or entropy, so no originality is assigned to those ingredients. The 1983 Yoshida--Mori--Shigematsu paper addresses power spectra of standard tent maps at band-splitting points, not the one-parameter asymmetric family. Prior published research abstracts on random expanding maps, symbolic covariances, and related maps were checked for matching parameters, reduction, or dominating results without locating an implication of this precise collection of claims.

Risk: finite-dimensional Markov transfer techniques are well established and might allow the exact expressions to be implicit in earlier unpublished or poorly indexed calculations. The conference proceedings, 1979 paper, and 1983 paper were not inspected in complete full text. Absence from search results is not uniqueness or priority proof.

## Mathematical value — PASS

The parent map was designed for controllable statistical behavior of chaotic sequences; knowing only the stationary mean does not quantify temporal dependence and accumulated fluctuations. A full covariance generating function gives every lag and the exact variance of long-run averages. The noncancelled *triple* eigenvalue resonance yields a sharp \(n^2\)-corrected decay law, while the maximum fluctuation parameter provably differs from the correlation transition and maximum entropy parameter. These are natural, global quantitative distinctions along a parameter slice motivated by the original map, not arbitrary numeric specializations or minor bounds. The density and entropy formulas supply normalization and comparative context only.

## Closest sources and limitations

Moysis et al. (2023), DOI 10.3390/sym15122138, is the direct parent family. Papamarkou--Lawrance (2014), DOI 10.1142/S0218127414500710, is the closest general autocorrelation methodology. Alsedà--Misiurewicz--Pérez (2020), arXiv:2004.01813, addresses the entropy side. The analysis is restricted to the diagonal Markov subfamily; priority verification cannot exclude all earlier general formulas. The exact-rational checker provides reproducibility, not independent validation.

Self-review: passed. Independent audit: not yet performed.
