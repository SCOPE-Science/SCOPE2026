# Independent mathematical audit

## correctness

PASS

The cubic characteristic polynomial λ³+3λ²+5λ+3−g has Routh–Hurwitz stability for 0≤g<3. Directly recomputing the Lyapunov covariance confirms the rank-one 6/(5(3−g))vvᵀ pole and stated finite B; the slow vector v=(2,1,1) has K_3v=0, the transverse a=(1,−5,3)/2 satisfies aᵀv=0, and H_3v=a with vᵀH_3v=0. Gaussian covariance convergence gives a single slow normal shared across fixed times, independent of the fast Gaussian η; direct matrix calculations recover Rη(0)=5 and Rη′(0+)=-35/4 and fast eigenvalues (-3±i√11)/2. Expanding the torque XᵀHX=2ξ(aᵀX)+bounded transverse term+δy² and applying Slutsky yields the product law, whose variance is 24 and whose lag covariance has the claimed cosine−sine zeros. Independent exact symbolic calculations reproduced the key Lyapunov, Laurent, Wick and oscillator identities; neither finitely many tests nor characteristic-function algebra alone establishes the multi-time limit, which is supplied by the Gaussian argument. At g=3 stationary initialization is undefined; growing time windows are not covered.

## originality

PASS

The exact all-parameter claim was compared by statement and implication against all identified strongly related primary works; known constructions, setup theorems and restricted subclasses are acknowledged as prior. The four structured comparisons and source inspections distinguish unproven priority from a concrete known coverage implication. Under a best-of-knowledge standard the unlocated stronger result is a stated risk, not an invented negative full-text finding.

## value

PASS

A source paper explicitly poses higher-order mechanical fluctuations near this linear stability loss; the stationary mean remains finite while torque variance diverges. A full non-Gaussian normalized law with one common slow factor and a sign-changing two-time memory is a meaningful new fixed-lag observable, not just the known variance divergence. Its exact coefficients are useful calibration benchmarks, but no path-space or long-time scaling limit is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
