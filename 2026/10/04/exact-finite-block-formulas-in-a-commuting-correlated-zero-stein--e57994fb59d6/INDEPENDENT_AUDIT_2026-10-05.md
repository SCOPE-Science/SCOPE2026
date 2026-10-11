# Independent mathematical audit

## correctness

PASS

Commutation makes the target ray an eigenvector of every block state, with block overlap \(g_k=c+(1-c)q^k\). Replacing an \(\omega^{\otimes k}\) block by \(\zeta_k\) strictly increases target overlap, and \(g_{a+b}-g_ag_b=c(1-c)(1-q^a)(1-q^b)\ge0\), so repeated merging proves the single \(n\)-block state is extremal. The entropy and max-entropy identities then follow from the target eigenvalue. For hypothesis testing, the single-block alternative gives the lower bound and \(Q=(1-\varepsilon)\rho^{\otimes n}\) attains it uniformly. For smoothing, trace distance gives target mass at least \(1-\delta/2\), and the explicit mixture \(L_s=(1-s)\rho^{\otimes n}+s\zeta_n\) attains the bound. The bundled verifier independently checks all block compositions and the merge/smoothing identities on bounded grids; it is corroborative rather than the source of the universal proof.

## originality

PASS

Gao--Ji--Liu introduce exactly the correlated family and use \(\zeta_n\ge c\rho^{\otimes n}\) to show a persistent type-II lower bound and zero normalized Stein rate, but they do not impose the commuting eigenvector parameter \(q\), optimize over all partitions at finite \(n\), or state the resulting exact entropy/testing/smoothing profile. The decisive merge identity and full finite-block equality are therefore not implication-level consequences of the source's stated lower bound. Targeted Resultary search found no published record with the same joint profile.

## value

PASS

The source uses this family specifically to exhibit a nontrivial zero-rate obstruction, so determining its exact finite-block behavior on the natural commuting subfamily is mathematically motivated. The result identifies the precise finite cost hidden behind the vanishing normalized rate and simultaneously resolves relative entropy, max-relative entropy, fixed-error testing, and smoothing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
