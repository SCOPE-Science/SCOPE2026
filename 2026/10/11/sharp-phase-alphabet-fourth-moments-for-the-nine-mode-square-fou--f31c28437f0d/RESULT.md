# Sharp phase-alphabet fourth moments for the nine-mode square Fourier aperture

## Finding
Let \(\mu_q=\{e^{2\pi i k/q}:0\le k<q\}\), \(q\in\{2,3,4,6\}\), and set
\[
P_c(z,w)=\sum_{i=0}^{2}\sum_{j=0}^{2}c_{ij}z^i w^j,\qquad c_{ij}\in\mu_q.
\]
For normalized Haar measure on \(\mathbb T^2\), let \(M(c)=\int_{\mathbb T^2}|P_c|^4\,dm\). The exact minima and complete counts of ordered arrays attaining them are:

| Phase alphabet | Minimum \(M(c)\) | Normalized optimizers | All optimizers |
| --- | ---: | ---: | ---: |
| \(q=2\) | \(113\) | \(8\) | \(64\) |
| \(q=3\) | \(97\) | \(2\) | \(54\) |
| \(q=4\) | \(105\) | \(16\) | \(1024\) |
| \(q=6\) | \(97\) | \(6\) | \(1296\) |

Here *normalized* means \(c_{00}=c_{01}=c_{10}=1\). In particular, writing \(\omega=e^{2\pi i/3}\), **every ternary minimizer**, and no others, has the form
\[
c_{ij}=\lambda\alpha^i\beta^j\omega^{\sigma ij},\quad
\lambda,\alpha,\beta\in\mu_3,\quad \sigma\in\{-1,1\}.
\]
The ternary minimum is strictly below the quaternary minimum, despite the latter alphabet having more elements. At six phases, four additional normalized equality cases occur besides the two embedded ternary patterns.

## Assumptions and scope
Indices \(i,j\) always range over \(\{0,1,2\}\), coefficients have unit magnitude and belong to the stated **finite** phase alphabet. No assertion is made about coefficients ranging freely over the entire unit circle or about phase alphabets not listed above. Arrays are ordered, not quotiented by row/column permutation or geometric reflection. The common/linear modulations \(c_{ij}\mapsto\lambda\alpha^i\beta^j c_{ij}\) are permitted only with phases from \(\mu_q\).

## Proof
**Autocorrelation identity.** For each displacement \(h=(u,v)\in\{-2,-1,0,1,2\}^2\), define the aperiodic correlation
\[
R_{u,v}(c)=\sum_{\substack{0\le i,j\le2\\0\le i+u,j+v\le2}}
c_{i+u,j+v}\overline{c_{ij}}.
\]
Expanding the Haar integral and using character orthogonality gives the exact identities
\[
M(c)=\sum_{u,v=-2}^{2}|R_{u,v}(c)|^2
=\sum_{a,b=0}^{4}\left|\sum_{\substack{0\le i,j,k,l\le2\\i+k=a,\ j+l=b}}c_{ij}c_{kl}\right|^2.
\]
The first formula groups difference frequencies in \(|P_c|^2\); the second groups sum frequencies in \(P_c^2\). Their terms are computed by independent loops in the attached checker, with exact arithmetic, for every normalized array.

**Normalization and exhaustive finite certificate.** Multiplication by \(\lambda\alpha^i\beta^j\) preserves every \(|R_{u,v}|\) and therefore \(M(c)\). Each \(\mu_q\)-valued array has a **unique** normalized representative, obtained by choosing \(\lambda=c_{00}^{-1}\), \(\beta=c_{00}c_{01}^{-1}\), and \(\alpha=c_{00}c_{10}^{-1}\). Its six free entries are \(c_{02},c_{11},c_{12},c_{20},c_{21},c_{22}\). Therefore exactly \(q^6\) representatives exhaust the domain and each corresponds to exactly \(q^3\) original arrays.

The supplied standard-library program `checker.py` enumerates all \(q^6\) representatives for each stated \(q\), calculates both independent moment expressions in exact quadratic-integer arithmetic, asserts equality term by term, and determines the minimum and every equality case. For \(q=2,4\), the coefficient ring is \(\mathbb Z[i]\); for \(q=3,6\), it is \(\mathbb Z[\omega]\), with norm \(N(a+b\omega)=a^2-ab+b^2\). The output minima and equality counts are precisely those in the table. There are \(64+729+4096+46656=51545\) normalized cases, with no numerical approximations or truncated search.

**An independent analytic ternary bound.** Since \(R_{0,0}=9\), the origin contributes \(81\). For each of the \(16\) mixed displacements \((u,v)\) with \(u,v\ne0\), the correlation has \((3-|u|)(3-|v|)\in\{1,2,4\}\) summands in \(\mu_3\). A sum of three cube-root phases can vanish only if all three phases occur with equal multiplicity (use \(1+\omega+\omega^2=0\) and the rational linear independence of \(1,\omega\)); none of \(1,2,4\) is divisible by three. Thus every mixed correlation is a nonzero Eisenstein integer, so its squared norm is a positive integer, at least \(1\). The axial correlations contribute nonnegative terms. Hence
\[
M(c)\ge81+16=97\qquad(c_{ij}\in\mu_3).
\]
For the Fourier phase matrix \(c_{ij}=\omega^{ij}\), direct geometric-sum evaluation gives vanishing correlations on nonzero axial displacements and squared norm exactly \(1\) on all \(16\) mixed displacements. Hence equality is attained. Conjugation gives the second normalized optimizer; complete uniqueness follows from the exhaustive exact certificate. The checker identifies their normalized free-exponent tuples as \((0,1,2,0,2,1)\) and \((0,2,1,0,1,2)\).

**Six-phase equality profiles.** With primitive sixth root \(\zeta=e^{2\pi i/6}\), the six normalized optimizer free-exponent tuples, in the same positional order, are
\[
(0,2,4,0,4,2),\ (0,4,2,0,2,4),\ (1,2,5,5,3,2),\
(1,4,3,5,1,4),\ (5,2,3,1,5,2),\ (5,4,1,1,3,4).
\]
The exhaustive calculation proves no additional six-phase cases attain \(97\).

## Verification
Run `python3 checker.py` using only the Python standard library. The checker tests all \(51545\) normalized arrays, evaluates the two independent autocorrelation/convolution expressions, and checks each phase-alphabet minimum, normalized count, complete count, and listed equality representatives. Exact integer-pair ring arithmetic prevents floating-point near-equality errors. The separate ternary analytic inequality is a proof valid for every ternary array, not a numerical observation.

## Relationship to prior work
Zhang–Fan–Mesnager (arXiv:2107.11599v1) construct two-dimensional \(q\)-ary **complementary pairs**, whose combined autocorrelations cancel on specified regions; their results do not assert a single-array, full \(3\times3\) fourth-moment minimum or classify these phase-alphabet-specific optimizers. Pai–Chen (arXiv:2102.04043v1) likewise constructs complementary **sets** using generalized Boolean functions. Both motivate the use of two-dimensional aperiodic correlations but neither directly proves this single-array classification. Literature on perfect **periodic** arrays has a different correlation domain. The fourth moment here is an aperiodic Haar moment and no periodic-to-aperiodic equivalence is assumed.

## Limitations
This is a finite phase-alphabet theorem for four specified alphabets, not the minimum over arbitrary unimodular coefficients and not a general classification of all \(q\). Exact enumeration is exhaustive only because the normalized finite spaces have been completely enumerated; no claim about larger grids follows from it. The existence of an equivalent historical classification in polyphase-array catalogs remains a bibliographic risk, and no independent audit has been performed.

## References
- H. Zhang, C. Fan, S. Mesnager, *New constructions of \(q\)-Ary 2-D Z-Complementary Array Pairs*, arXiv:2107.11599v1, first public 24 July 2021. https://arxiv.org/abs/2107.11599
- S. Pai and C. Chen, *Two-Dimensional Golay Complementary Array Sets from Generalized Boolean Functions*, arXiv:2102.04043v1, first public 8 February 2021. https://arxiv.org/abs/2102.04043
- P. Svalbe and A. Tirkel, *Extended families of 2D arrays with near optimal auto and low cross-correlation* (2017); addresses periodic correlation arrays.
