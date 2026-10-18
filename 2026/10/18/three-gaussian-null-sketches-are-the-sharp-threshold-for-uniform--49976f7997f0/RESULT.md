# Three Gaussian null-sketches are the sharp threshold for uniformly integrable near-null residuals

## Finding

For any integer \(n\ge2\), consider a real matrix with singular values \(a,\ldots,a,b\), where \(a>b>0\) and \(\kappa=a/b>1\). Independently draw \(K\ge1\) standard real Gaussian sketches having \(n-1\) rows, extract the unit null vector of each sketched matrix, evaluate its **unsketched** squared residual, and retain the smallest. Write the squared residual divided by the optimal squared residual \(b^2\) as \(R_{\kappa,K}\).

**Sharp replication threshold.** For every fixed \(n\ge2\) and every real \(q>0\),
\[
\sup_{\kappa>1}\mathbb E[R_{\kappa,K}^{q}]<\infty
\quad\Longleftrightarrow\quad K>2q.
\]
In particular, exactly **three** independent one-row-short sketches are necessary and sufficient for a condition-number-uniform bound on the expected *relative squared residual*. One or two trials cannot provide that bound, even though every individual selected unit vector converges in angle to the exact smallest right singular vector as \(\kappa\to\infty\).

Let \(B_n=B(\tfrac12,\tfrac{n-1}{2})\), with \(B\) denoting Euler's beta function. The first two trial counts have the precise divergent rates
\[
\mathbb E R_{\kappa,1}\sim\frac{\pi}{B_n}\,\kappa,
\qquad
\mathbb E R_{\kappa,2}\sim\frac{8}{B_n^2}\log\kappa.
\]
For \(K\ge3\), the expectation increases to the finite exact constant \(\mathbb E[W^{-1}]\) described below.

In the three-dimensional model \(n=3\), this constant is explicitly
\[
\sup_{\kappa>1}\mathbb E R_{\kappa,K}=\frac{K}{K-2}\qquad(K\ge3).
\]
Consequently, three trials give the sharp dimension-three bound \(\mathbb E\|Av_*\|_2^2\le3b^2\), uniformly over every \(a>b>0\). Two trials have no condition-number-uniform expected guarantee.

## Assumptions and scope

Fix real integers \(n\ge2\), \(K\ge1\) and reals \(0<b<a\). First set \(A=\operatorname{diag}(a,\ldots,a,b)\in\mathbb R^{n\times n}\). Let \(G_j\in\mathbb R^{(n-1)\times n}\) for \(1\le j\le K\) be independent matrices with i.i.d. real standard-normal entries. Almost surely, each \(G_jA\) has a one-dimensional kernel. Choose any unit \(v_j\) spanning it, and let \(v_*\) be a minimizer of \(\|Av_j\|_2^2\) over these \(K\) vectors. Ties are immaterial. Set \(R_{\kappa,K}=\|Av_*\|_2^2/b^2\), where \(\kappa=a/b\).

The same result applies to any tall real \(m\times n\) matrix, \(m\ge n\), with those singular values, when the left sketch is standard Gaussian of size \((n-1)\times m\): left/right orthogonal invariance reduces it to the diagonal model. All statements concern exact arithmetic and selection by an exact evaluation of the original (unsketched) residual.

## Proof

**1. The random null line.** Since each \(G_j\) is rotationally invariant and has rank \(n-1\) almost surely, its one-dimensional kernel is a uniform unoriented line. Select a unit representative \(u_j\) of that line. Then
\[
 v_j=\frac{A^{-1}u_j}{\|A^{-1}u_j\|_2}
 \quad\text{up to sign}.
\]
The scalar \(T_j=(u_j)_n^2\) has the beta law \(\operatorname{Beta}(\tfrac12,\tfrac{n-1}{2})\). The variables \(T_j\) are independent. A direct division by \(b^2\) gives
\[
 \frac{\|Av_j\|_2^2}{b^2}
 =\frac{\kappa^2}{1+(\kappa^2-1)T_j}.
\]
Let \(W=\max_{1\le j\le K}T_j\). Since this expression is decreasing in \(T_j\), selection by the original residual yields the **exact law**
\[
 \boxed{R_{\kappa,K}=\frac{\kappa^2}{1+(\kappa^2-1)W}}.
\]
In particular, writing \(F_n\) for the beta distribution function,
\[
 \Pr\{R_{\kappa,K}>r\}
 =\left[F_n\!\left(\frac{\kappa^2/r-1}{\kappa^2-1}\right)\right]^K,
 \qquad 1\le r\le\kappa^2.
\]
The strict comparison endpoints are immaterial because the law is continuous.

**2. Sharp moment threshold.** On the same probability space, \(R_{\kappa,K}\) is increasing in \(\kappa\) and tends almost surely to \(W^{-1}\) as \(\kappa\to\infty\). The beta density and cumulative distribution have the exact near-zero equivalents
\[
 f_n(t)\sim B_n^{-1}t^{-1/2},
 \qquad F_n(t)\sim\frac{2}{B_n}\sqrt{t}.
\]
Thus the density of \(W\), namely \(K F_n(t)^{K-1}f_n(t)\), satisfies
\[
 f_W(t)\sim\frac K2\left(\frac2{B_n}\right)^K t^{K/2-1}
 \qquad(t\downarrow0).
\]
It follows by integrating near zero that \(\mathbb E W^{-q}<\infty\) precisely when \(K>2q\). Monotone convergence proves the stated necessary-and-sufficient condition for \(\sup_{\kappa}\mathbb E R_{\kappa,K}^q\). This proves the **sharp cutoff** \(K=3\) for the first moment.

**3. Rates at one and two trials.** Using the density \(f_n\) and substituting \(t=\kappa^{-2}z\) in the expectation for \(K=1\), the dominant boundary layer gives
\[
 \lim_{\kappa\to\infty}\kappa^{-1}\mathbb E R_{\kappa,1}
 =\frac1{B_n}\int_0^\infty\frac{z^{-1/2}}{1+z}\,dz
 =\frac\pi{B_n}.
\]
For \(K=2\), the maximum density satisfies \(f_W(t)\to 4/B_n^2\) as \(t\downarrow0\). Integration of \((t+\kappa^{-2})^{-1}\) near zero then gives
\[
 \lim_{\kappa\to\infty}
 \frac{\mathbb E R_{\kappa,2}}{\log\kappa}
 =\frac8{B_n^2}.
\]
To make these steps rigorous, split each integral at an arbitrary fixed \(\delta\in(0,1)\). On \((0,\delta)\), the beta density ratios approach their displayed leading terms uniformly as \(\delta\downarrow0\); on \((\delta,1)\) the integrals are uniformly bounded, and their normalized contributions vanish. The single-trial scaled kernel has integrable limit \(z^{-1/2}/(1+z)\), justifying the substitution limit.

**4. Closed dimension-three family.** For \(n=3\), \(T_j\sim\operatorname{Beta}(\tfrac12,1)\), so \(U_j=\sqrt{T_j}\) is exactly uniform on \((0,1)\). The maximum \(M=\max_jU_j\) has density \(K u^{K-1}\). Hence
\[
 \mathbb E R_{\kappa,K}
 =K\kappa^2\int_0^1\frac{u^{K-1}}{1+(\kappa^2-1)u^2}\,du.
\]
For \(K>2\), monotone convergence yields
\[
 \sup_{\kappa>1}\mathbb E R_{\kappa,K}
 =K\int_0^1u^{K-3}\,du=\frac K{K-2}.
\]
This constant is optimal because it is approached as \(\kappa\to\infty\). Writing \(d=\kappa^2-1>0\), the first three exact finite-contrast expectations are
\[
 \begin{aligned}
 \mathbb E R_{\kappa,1}&=\frac{\kappa^2}{\sqrt d}\arctan\sqrt d,\\
 \mathbb E R_{\kappa,2}&=\frac{\kappa^2}{d}\log(1+d),\\
 \mathbb E R_{\kappa,3}&=\frac{3\kappa^2}{d}
       \left(1-\frac{\arctan\sqrt d}{\sqrt d}\right).
 \end{aligned}
\]
They exhibit respectively linear growth, logarithmic growth, and convergence to \(3\).

**5. The angle/residual distinction.** If \(u_{j,n}\ne0\), the first \(n-1\) components of \(v_j\) relative to its last component have size proportional to \(\kappa^{-1}\), so \(v_j\) converges projectively to the unique smallest right singular direction as \(\kappa\to\infty\). Yet its normalized squared residual converges to \(1/T_j\), not to \(1\); for a finite best-of-\(K\) pool it converges to \(1/W\), whose first moment diverges for \(K=1,2\). This completes the proof.

## Verification

Run the standalone standard-library script `python3 verify.py`. It checks an exact rational three-dimensional null-vector example, reproduces the three integral formulas through deterministic numerical quadrature at five contrasts each, checks the limiting moment identities, and independently forms 105,000 Gaussian row sketches via cross products. The recorded output is:

```
VERIFY_OK exact_fraction_witness=1 exact_n3_formula_quadratures= 15 limit_checks=3 threshold_integrals=4 random_matrix_sketches=105000 mc_mean= 2.1289949 theory= 2.1109245
```

The Gaussian experiment confirms the **direct matrix construction**, rather than simulating only the beta-transformed variable. Its Monte Carlo tolerance is deliberately loose because it is a finite random check. No numerical experiment substitutes for the integral proof above.

## Relationship to prior work

Epperly, Park, and Nakatsukasa (arXiv:2602.16797v1, February 18, 2026), Sect. 2 and 3, analyze minimum singular vectors using sketches that preserve an entire full-column-rank trial space, in particular their Definition 1, Theorem 2, and Facts 5–6. Their algorithm requires an invertible sketch-derived preconditioner; it **does not use** a one-row-short rank-deficient sketch. The present theorem instead analyzes the exact null vector available just below this rank threshold, combined with best-of-replicates selection using original residual evaluations.

Park and Nakatsukasa (2023), Sect. 2–3 and Theorems 2.3 and 3.1, analyze sketch-and-solve approximate nullspaces under \(s\ge n\) and full-rank embedding hypotheses; those statements likewise cannot be applied to a sketch with \(n-1\) rows. Their work and the first paper are the relevant motivating benchmark, not targets of a purported refutation.

The proof deliberately uses classical spherical-coordinate beta and order-statistic identities. Neither their discovery nor the general fact that beta variables can have divergent inverse moments is claimed as new. The proposed contribution is their exact combination for an actionable undersketched singular-vector selection rule, yielding the sharp **three-trial** boundary and the exact dimension-three expected-quality constants. An equivalent treatment in older probabilistic numerical linear algebra could exist; that residual originality risk remains for independent assessment.

## Limitations

The singular spectrum has one simple smallest singular value and all remaining singular values equal; sketches are **real Gaussian**, independent, and have exactly one fewer row than columns. Selection evaluates the true unsketched residual, so this is not a complexity or wall-clock improvement guarantee, nor a theorem about the implementation of RLOBPCG or the 2023 sketch-and-solve method. The constants for \(n>3\) depend on dimension. The result provides no guarantee for finite-precision nullspace extraction, arbitrary spectra, dependent trials, complex sketches, or downstream eigensolver convergence. All novelty conclusions are based on inspected published sources, not a proof of uniqueness across all literature.

## References

1. E. N. Epperly, T. Park, Y. Nakatsukasa, *Fast, high-accuracy, randomized nullspace computations for tall matrices*, arXiv:2602.16797v1 (first public February 18, 2026), https://arxiv.org/html/2602.16797.
2. T. Park, Y. Nakatsukasa, *A fast randomized algorithm for computing an approximate null space*, BIT Numerical Mathematics **63**, article 36 (2023), https://doi.org/10.1007/s10543-023-00979-7, freely accessible at https://link.springer.com/article/10.1007/s10543-023-00979-7.
3. N. Halko, P. G. Martinsson, J. A. Tropp, *Finding structure with randomness: probabilistic algorithms for constructing approximate matrix decompositions*, SIAM Review **53** (2011), 217–288, https://doi.org/10.1137/090771806. This general survey is background; full-text exclusion of an implicit related consequence is not claimed.
