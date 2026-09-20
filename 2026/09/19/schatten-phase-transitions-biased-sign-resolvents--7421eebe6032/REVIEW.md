# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The diagonal formula is immediate from Acuaviva's Proposition 3.2 and the Walsh orthonormal basis: the singular values on \(L_2\) are exactly \((1+t\lambda_F)^{-1}\). The Mellin product identity follows from Tonelli and the finite-subset product expansion, so it remains valid with value \(+\infty\).

The representability implication was checked independently of the later asymptotics. Finite \(S_p\)-membership forces summability of the singleton eigenvalues, hence \(\sum_j e^{-2u\lambda_j}<\infty\) for every \(u>0\). Kakutani's biased-product criterion therefore gives \(\mu_u\ll m\); when every \(\lambda_j>0\), this improves to equivalence. Averaging these measures with the positive resolvent density yields \(\nu_t\ll m\), and Costé's criterion gives representability of convolution by \(\nu_t\). This is compatible with Acuaviva's Schur example: his common Haar-null carrier makes every \(\nu_t\) singular, so those compact resolvents cannot lie in any finite Schatten class. A direct level-counting proof gives the same conclusion.

For \(\lambda_j=e^{cj^\gamma}\), the proof uses the exact multiplicity \(2^{N-1}\) of Walsh characters with \(\max F=N\). The lower and upper bounds use only \(\lambda_N\le\lambda_F\le\sum_{j\le N}\lambda_j\), so no independence or genericity of subset sums is assumed. At \(\gamma=1\), every level has eigenvalues comparable to \(a^{-N}\) and cumulative multiplicity comparable to \(2^N\), which gives both the sharp threshold \(p>\log_a2\) and \(s_k\asymp k^{-1/d}\) at the endpoint.

The spectral-zeta residue was checked by grouping by the maximal index, reversing the lower binary digits, and applying the Abel limit to \(q(s)=2a^{-s}\). The dyadic case provides an exact check: subset sums of \(2^j\), \(j\ge1\), are the even nonnegative integers, giving a Hurwitz zeta function whose residue agrees with the general formula.

No complementability or inheritance assertion beyond results already proved in the source paper is used. The new exponentially growing choices are not asserted to preserve the source paper's singularity or Schur-space conclusions.

## Originality

Acuaviva's current v1 defines the resolvent family for arbitrary nonnegative \((\lambda_j)\) and records the Walsh eigenvalue formula, but its compactness analysis is qualitative and specialized to the Schur construction; the paper contains no Schatten, trace-class, Hilbert--Schmidt, weak-Schatten, or spectral-zeta analysis.

Schachermayer's 1986 paper was inspected because it is the closest prior art. It explicitly constructs a singular biased-product convolution whose multiplicative Walsh eigenvalues put the operator in \(S_p\) for every \(p>2\). That result is not claimed as new. The present observation concerns Acuaviva's resolvent spectrum, where eigenvalues depend on reciprocal additive subset sums. In this setting finite Schatten membership forces absolute continuity of the positive-time product measures and therefore representability of the resolvent convolution, producing the opposite singularity/Schatten boundary.

Targeted searches using Acuaviva's title and identifier, biased-coin and biased-sign resolvents, Walsh multipliers, Schatten and weak-Schatten classes, subset-sum spectra, and spectral-zeta formulations did not locate the phase diagram, the incompatibility theorem, or the geometric-weight residue formula. The principal residual prior-art risk is older work on diagonal semigroups, product-measure generators, or spectral triples on Cantor groups, where a comparable counting argument might appear under different terminology. The classical ingredients themselves are excluded from the novelty claim. Originality is asserted only to the best of our knowledge.

## Value

The result upgrades a qualitative compactness mechanism into a sharp ideal-theoretic classification. It explains why Acuaviva's singular compact resolvents are exceptionally far from trace ideals, realizes every positive weak-Schatten critical exponent in a simple geometric family, and supplies an explicit zeta residue at the phase boundary. The comparison with Schachermayer also isolates a structural difference between direct biased-product convolution and resolvent averaging.

## Limitations

The full Schatten behavior for arbitrary \((\lambda_j)\) is not classified. Absolute continuity or representability of \(\nu_t\) is not claimed to imply finite Schatten membership. The exponentially growing families are spectral examples inside the general resolvent construction and are not asserted to yield the same complemented-space geometry as the source paper's Schur example. No claim is made about optimal Lorentz refinements away from the geometric critical line or about Dixmier traces.
