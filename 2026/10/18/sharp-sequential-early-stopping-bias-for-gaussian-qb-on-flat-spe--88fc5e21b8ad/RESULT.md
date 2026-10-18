# Sharp sequential early-stopping bias for Gaussian QB on flat spectra

## Finding

**Theorem.** Fix \(0<\varepsilon<1\). In the unit-block, Gaussian, relative-Frobenius-norm matrix-free QB algorithm described below, run in exact arithmetic on \(A_n=I_n\). Let \(T_n\) be the first inspection that passes the stated random stopping test, and let \(K_n\) be the rank after its optional final-block pruning. For any inspection \(2\le i\le n\) along a hypothetical uninterrupted run, the exact marginal stop-event probability is
\[
\Pr\!\left(\|Y_i\|_2^2<\frac{\varepsilon^2}{i}\sum_{j=1}^i\|\omega_j\|_2^2\right)
= I_{\varepsilon^2/i}\!\left(\frac{n-i+1}{2},\frac{(i-1)(n+1)}{2}\right),
\]
where \(I_z(a,b)\) is the regularized incomplete beta function. This is an unconditional inspection probability, not the conditional hazard given nontermination.

The first stopping inspection and the returned rank have the sharp asymptotic law
\[
\frac{(1-\varepsilon^2)n-T_n}{\sqrt{n\log n}}
\xrightarrow{\mathbb P}\sqrt{2}\,\varepsilon,
\qquad
\frac{(1-\varepsilon^2)n-K_n}{\sqrt{n\log n}}
\xrightarrow{\mathbb P}\sqrt{2}\,\varepsilon.
\]
In particular, the exact returned relative Frobenius error \(e_n=\|I_n-QB\|_F/\sqrt n\) satisfies
\[
\sqrt{\frac{n}{\log n}}\,(e_n-\varepsilon)
\xrightarrow{\mathbb P}\frac1{\sqrt2}.
\]
Thus a repeatedly inspected, fresh, individually unbiased Gaussian residual sketch crosses the requested threshold too early with probability tending to one, even on the identity matrix. The rank shortfall is of order \(\sqrt{n\log n}\), with an explicit constant. All limits are for fixed \(\varepsilon\) as integers \(n\to\infty\).

## Assumptions and scope

At dimension \(n\ge2\), the real input is \(A_n=I_n\), and the unit-block size is exactly one. Independently for each \(1\le i\le n\), draw \(\omega_i\sim N(0,I_n)\). Initially \(Q_0\) has zero columns. Provided inspection \(i\) is reached, form \(Y_i=(I_n-Q_{i-1}Q_{i-1}^{\mathsf T})\omega_i\). Set \(S_i=\sum_{j=1}^i\|\omega_j\|_2^2\); if \(\|Y_i\|_2<\varepsilon\sqrt{S_i/i}\), terminate before adding \(Y_i\) to the basis, optionally deleting the previous block as specified by the source's row-pruning rule. Otherwise append \(Y_i/\|Y_i\|_2\) to \(Q_{i-1}\) and set \(B=Q^{\mathsf T}I_n\). The Gaussian probes make all nonterminal residual directions nonzero almost surely. Define \(T_n=n+1\) and \(K_n=n\) if no inspection passes. Otherwise the source's unit-block pruning retains either \(T_n-2\) or \(T_n-1\) columns. The optimal rank for an exact orthogonal-projection Frobenius error at most \(\varepsilon\sqrt n\) is \(\lceil(1-\varepsilon^2)n\rceil\).

The theorem analyzes this exact specialization of the publicly provided `randQB_MF_Fro.m` and `Prune_Rank_Fro.m`. It is not a theorem about arbitrary matrix-free QB implementations.

## Proof

**1. Independent Gaussian innovation decomposition.** Imagine generating all \(n\) inspections even if the test would have stopped. Gaussian rotational invariance and exact Gram–Schmidt give, at each \(i\),
\[
U_i:=\|Y_i\|_2^2\sim\chi^2_{n-i+1},\qquad
V_i:=\|\omega_i\|_2^2-U_i\sim\chi^2_{i-1}.
\]
The two variables are independent, and all pairs \((U_i,V_i)\) are independent across \(i\): conditioned on all previous vectors, the joint law of squared projections of the fresh isotropic Gaussian vector onto the previous span and its perpendicular complement is the fixed product chi-square law. Their conditional joint law does not depend on the previous vectors. Moreover \(S_i=\sum_{j\le i}(U_j+V_j)\). Thus this construction is an exact joint-law representation of the complete stopping process, not merely a moment identity.

**2. Finite marginal law.** For \(i\ge2\), \(S_i-U_i\) and \(U_i\) are independent, with chi-square degrees of freedom \(in-(n-i+1)=(i-1)(n+1)\) and \(n-i+1\), respectively. Their ratio \(U_i/S_i\) has the beta distribution with the displayed parameters. Squaring the stopping inequality is legitimate because both sides are nonnegative. This proves the exact incomplete-beta probability.

**3. Uniform control of the random denominator.** Set \(i_0=(1-\varepsilon^2)n\). For every fixed \(c>0\), standard chi-square Chernoff bounds and a union bound imply
\[
\sup_{cn\le i\le n}|S_i/i-n|=O_{\mathbb P}(\sqrt{\log n}).
\]
Indeed \(S_i\sim\chi^2_{in}\) and there are only \(n\) inspections. Inspections \(i\le cn\), with \(c<(1-\varepsilon^2)\) chosen sufficiently small, cannot pass with probability tending to one: in that region the residual chi-square mean exceeds \(\varepsilon^2 n\) by a fixed multiple of \(n\), whereas \(S_i/i\) concentrates around \(n\). This early-region exclusion follows from chi-square exponential tail bounds even for small \(i\).

**4. Sharp first-hit location.** Let \(h_n=\sqrt{n\log n}\) and \(c_*=\sqrt2\,\varepsilon\). For \(i=i_0-ch_n+O(\sqrt n)\), with fixed \(c>0\), the innovation \(U_i\) has \(n-i+1=\varepsilon^2 n+ch_n+O(\sqrt n)\) degrees of freedom. Chi-square moderate-deviation estimates at \(\varepsilon^2 n+O(\sqrt{\log n})\) give
\[
\Pr\bigl(U_i\le\varepsilon^2 n+O(\sqrt{\log n})\bigr)
=n^{-c^2/(4\varepsilon^2)+o(1)}.
\]
For completeness, the upper bound follows from exponential Chernoff optimization. For the lower bound, Stirling's formula applied to the chi-square density at \(\varepsilon^2n+O(\sqrt{\log n})\), integrated over a left interval of length \(\sqrt{n/\log n}\), gives the same logarithmic exponent; the density's \(n^{-1/2}\) factor is cancelled by the integration width, with only logarithmic losses. Both bounds are uniform over fixed-width \(O(\sqrt n)\) inspection windows near \(i_0-ch_n\).

If \(c>c_*\), sum the Chernoff tails over all earlier inspections. The effective number with comparable probability is \(O(\sqrt{n/\log n})\): as the residual degrees of freedom grow above \(\varepsilon^2n+ch_n\), the exponent increases quadratically, and the farther region is exponentially negligible. Since \(c^2/(4\varepsilon^2)>1/2\), the union probability tends to zero. Consequently \(T_n\ge i_0-ch_n\) with probability tending to one.

If \(0<c<c_*\), consider \(\lfloor\sqrt n\rfloor\) successive inspections immediately preceding \(i_0-ch_n\). Their innovations \(U_i\) are independent and each has a stop probability at least \(n^{-c^2/(4\varepsilon^2)+o(1)}\) under a deterministic denominator sandwich from Step 3. Because \(1/2-c^2/(4\varepsilon^2)>0\), the chance that every one of these innovations fails the stop test tends to zero. Therefore \(T_n\le i_0-ch_n\) with probability tending to one. Letting \(c\) approach \(c_*\) from both sides proves the first limit, and also \(\Pr(T_n\le n)\to1\).

**5. Returned rank and error.** At a successful inspection the algorithm does not append \(Y_i\), and the unit-block prune can only remove the immediately previous column. Hence \(K_n\in\{T_n-2,T_n-1\}\) on successful termination, so the same normalized rank limit holds. Every retained \(Q\) has orthonormal columns; with \(B=Q^{\mathsf T}\), the exact squared Frobenius error is \(n-K_n\). Thus \(e_n^2-\varepsilon^2=[(1-\varepsilon^2)n-K_n]/n\), and division by \(e_n+\varepsilon\to 2\varepsilon\) yields the final universal constant \(1/\sqrt2\). No simulation or finite inspection count is used to infer an infinite limit.

## Verification

The standalone `CHECK.py` uses independent chi-square innovations to reproduce the exact joint stopping law without forming large dense QR factorizations. It also checks an explicit Gaussian QR experiment, three finite beta-law probabilities, and simulated first-hit shifts at six dimension/tolerance settings, comparing them with the proven constant. Run `python CHECK.py` with NumPy and SciPy installed. The numerical results converge slowly on the displayed normalization, as expected for an extreme-value logarithmic correction; the proof above establishes the limit.

## Relationship to prior work

Smith, Do, and Chen (2026) introduce matrix-free adaptive randomized QB and use a fresh Gaussian residual sketch with a running estimated input norm for the relative-Frobenius stopping criterion. Their companion implementation provides the exact operational definition analyzed here, including final-block pruning. The present finding is a flat-spectrum sequential-first-crossing calculation: a finite incomplete-beta inspection law and the sharp \(\sqrt{n\log n}\) rank underselection scale. The accessible implementation does not state these conclusions. Yu, Gu, and Li (2018) instead analyze a deterministic energy-subtraction Frobenius indicator under exact arithmetic; that indicator has no repeated independent Gaussian noise of the present kind. Classical adaptive Gaussian rangefinders and repeated-testing theory provide background, but no accessed result was shown to imply this complete specialization and constant.

## Limitations

The theorem is about the identity input, unit block size, standard real Gaussian probes, fixed tolerance \(0<\varepsilon<1\), exact arithmetic, and the specified running denominator. It does not quantify finite-precision QR effects or yield a universal finite-dimensional failure probability for other spectra/block sizes. The violation of the requested relative error is asymptotically positive but vanishes in magnitude at rate \(\sqrt{\log n/n}\); the rank shortfall nevertheless diverges. The motivating manuscript itself could not be inspected in full; its publicly available complete algorithm and pruning source were inspected, and any uninspected manuscript discussion of sequential stopping remains a bibliographic risk.

## References

1. A. I. Smith, E. Do, and C. Chen, *Adaptive, Matrix-Free Low-Rank Approximation*, first public July 7, 2026, arXiv:2607.06758. https://arxiv.org/abs/2607.06758
2. Smith, Do, and Chen, `randQB_MF_Fro.m`, publicly released companion implementation, https://github.com/SMART-Algebra/Adaptive-Matfree-Lowrank/blob/main/randQB_MF_Fro.m
3. Smith, Do, and Chen, `Prune_Rank_Fro.m`, companion implementation, https://github.com/SMART-Algebra/Adaptive-Matfree-Lowrank/blob/main/Prune_Rank_Fro.m
4. W. Yu, Y. Gu, and Y. Li, *Efficient Randomized Algorithms for the Fixed-Precision Low-Rank Matrix Approximation*, SIAM Journal on Matrix Analysis and Applications 39 (2018), 1339–1359, DOI:10.1137/17M1141977. https://arxiv.org/abs/1606.09402
5. N. Halko, P.-G. Martinsson, and J. A. Tropp, *Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions*, SIAM Review 53 (2011), 217–288.
