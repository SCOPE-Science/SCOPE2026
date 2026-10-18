# Independent mathematical audit

## correctness

PASS

Direct independent polynomial expansion and even logistic moments (M2=π²/3,M4=7π⁴/15,M6=31π⁶/21,M8=127π⁸/15) reproduce C=c0+c2α², mean −2c2α/C, second moment (2c2+d2α²)/C. The derivative dV/d(α²) has numerator c0(Δ−4c2²)+c2α²(Δ+4c2²), Δ=d2c0−2c2², 0<Δ<4c2². It changes sign once at |α|≈0.16225909; |mean| peaks once at |α|≈0.25018142. Independent SymPy exact identities and direct mpmath integration for α=0,0.5,−2 validated normalizer and signs. At α=+0.5, true mean −3.199071061301 and variance 42.563544077327 versus Table 1 positive mean 2.253, variance 1.478; reflection f_{−α}(−x)=f_α(x) forbids same nonzero mean signs for ±α. Source Figure 3 and displayed moments are mostly consistent; erroneous table and text only.

## originality

PASS

Best-of-knowledge PASS solely as exact correction of the source conflicting numerical table, claims of monotonic growth of mean magnitude and monotonic variance decrease, and exact phase thresholds. Prior source already prints sufficient raw moment formulas, so those expressions are NOT original and cannot be counted as new results by themselves. No separate source-specific published erratum or complete turning-point description was located.

## value

PASS

The source provides applications of a fitted distribution and uses Table 1 to justify shape/dispersion flexibility. Correcting mean sign and order-of-magnitude variance, plus exact one-turning-point variance geometry, changes the statistical interpretation of the model. It is a substantive source-specific numerical/qualitative correction, though no new general moment theorem or refitting is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
