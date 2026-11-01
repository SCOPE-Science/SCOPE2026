# Exact phase-alphabet fourth moments on a twelve-mode Fourier prism

## Finding
Let \(\mu_q=\{\exp(2\pi i j/q):0\le j<q\}\), and for each \(q\in\{2,3,4,6\}\) consider
\[
P_c(x,y,z)=\sum_{i,j=0}^{1}\sum_{k=0}^{2}c_{ijk}x^iy^jz^k,\qquad c_{ijk}\in\mu_q,
\]
with normalized Haar fourth moment \(\mathcal M(c)=\int_{\mathbb T^3}|P_c|^4\,dm\). The **exact** least fourth moments, second-smallest attained values, and complete minimizer counts are:

| \(q\) | Least \(\mathcal M\) | Next value | Gap | Normalized minimizers | All minimizers | Geometric-conjugate orbits |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 220 | 228 | 8 | 27 | 432 | 6 |
| 3 | 210 | 216 | 6 | 48 | 3888 | 2 |
| 4 | 188 | 196 | 8 | 6 | 1536 | 2 |
| 6 | 196 | 200 | 4 | 36 | 46656 | 5 |

Every minimizer is obtained by scalar and coordinate-character phase modulation from the following normalized representatives, followed optionally by reflections, interchange of the two short axes, and complex conjugation. A *representative string* lists the twelve exponents \(e_{ijk}\) in the lexicographic order \((i,j,k)=(0,0,0),(0,0,1),\ldots,(1,1,2)\), with \(c_{ijk}=\exp(2\pi i e_{ijk}/q)\). Each *orbit size* counts normalized representatives only.

| \(q\) | Representative string | Normalized orbit size |
| --- | --- | ---: |
| 2 | `000001001101` | 4 |
| 2 | `000001010011` | 8 |
| 2 | `000001010110` | 8 |
| 2 | `000001011010` | 4 |
| 2 | `001001001110` | 1 |
| 2 | `001001011100` | 2 |
| 3 | `000001012210` | 32 |
| 3 | `000001021120` | 16 |
| 4 | `002002010232` | 4 |
| 4 | `002010030022` | 2 |
| 6 | `002015045032` | 8 |
| 6 | `002015052342` | 16 |
| 6 | `003003015342` | 4 |
| 6 | `003003021354` | 4 |
| 6 | `003015045522` | 4 |

The four-phase alphabet has a *strictly smaller* optimal fourth moment than the six-phase alphabet on this prism (188 versus 196); merely increasing the alphabet cardinality need not improve the fourth-moment optimum when neither alphabet contains the other.

These conclusions, including the same equality lists and gaps, hold for normalized Fourier averaging over \(\mu_m\times\mu_n\times\mu_\ell\) whenever \(m,n\ge3\) and \(\ell\ge5\).

## Assumptions and scope
The support consists of **every** frequency in \(\{0,1\}\times\{0,1\}\times\{0,1,2\}\) and all twelve coefficients have unit modulus in the stated alphabet. We minimize the fourth moment of a **single** array, equivalently its full aperiodic autocorrelation energy; this is not periodic correlation or a Golay complementary *pair*. The torus and finite grids have probability-normalized Haar measure. The character modulation is
\[
c_{ijk}\mapsto\lambda\alpha^i\beta^j\gamma^kc_{ijk},\qquad \lambda,\alpha,\beta,\gamma\in\mu_q.
\]
The geometric symmetry group consists of independently reversing each coordinate of the support, swapping the two length-two coordinates, and complex conjugation. No claim about unrestricted complex phases, other finite alphabets, or larger support shapes is made.

## Proof
**1. Two exact Fourier identities.** Put \(S=\{0,1\}^2\times\{0,1,2\}\). For \(a\in S+S\), define \(B_a=\sum_{u,v\in S,\ u+v=a}c_uc_v\). For \(h\in S-S\), define \(R_h=\sum_{u,v\in S,\ u-v=h}c_u\overline{c_v}\). Orthogonality on \(\mathbb T^3\), first applied to \(P_c^2\) and then to \(|P_c|^2\), gives
\[
\mathcal M(c)=\sum_{a\in S+S}|B_a|^2=\sum_{h\in S-S}|R_h|^2.\tag{1}
\]
There are \(3\cdot3\cdot5=45\) possible indices in each sum. Both formulas are exact, with ordered coefficient pairs in their inner sums. This also fixes every normalization factor.

**2. A unique phase gauge.** The four freely chosen phases \((\lambda,\alpha,\beta,\gamma)\) uniquely normalize
\[
c_{000}=c_{100}=c_{010}=c_{001}=1.
\]
For each \(q\), the remaining eight entries may take any \(q\)-th root independently. Thus exactly \(q^8\) normalized arrays exhaust all possibilities, and each represents exactly \(q^4\) distinct unnormalized arrays. Scalar/character modulation leaves \(\mathcal M\) invariant because it changes each \(B_a\) by a single unit factor.

**3. Integer-arithmetic exhaustive certificate.** For \(q=2,4\), represent roots in the Gaussian lattice \(\mathbb Z[i]\), with exact norm \(N(a+bi)=a^2+b^2\). For \(q=3,6\), use the primitive sixth root \(\zeta=\exp(\pi i/3)\) and the lattice \(\mathbb Z[\zeta]\), with \(\zeta^2=\zeta-1\) and
\[
N(a+b\zeta)=a^2+ab+b^2.
\]
These are genuine integer norms, not approximations. The supplied standard-library-only `CHECK.py` enumerates **all**
\[
2^8+3^8+4^8+6^8=1{,}751{,}969
\]
normalized arrays, forms the complete 45-term list of sums \(B_a\) for each, and evaluates (1) by exact integer-pair arithmetic. The program checks the exact minimum, the first strictly greater attained value, and the entire set of minimizers, rather than merely sampling or testing proposed candidates. Its independently implemented difference-correlation formula is also checked on every minimizer and on supplementary nonminimizers.

**4. All equality classes.** After collecting **every** normalized minimizer, the checker constructs the orbit of each under all \(2^3\) coordinate reversals, the optional swap of the two short axes, and conjugation; it renormalizes the four anchor phases after each operation. The orbit enumeration checks that every transformed array is a minimizer and that the resulting disjoint orbits exhaust the winner set. The orbit representatives and sizes are exactly those displayed above. Multiplication by the proven \(q^4\) fiber size yields the complete unnormalized counts. Because every nonwinner has fourth moment at least the computed next value, the tabulated gaps are rigorous.

**5. Finite-grid transfer.** In \(P_c^2\) the first two exponents range from \(0\) to \(2\), and the third from \(0\) to \(4\). When \(m,n\ge3\) and \(\ell\ge5\), these 45 characters remain pairwise distinct on the finite product group. Finite character orthogonality therefore gives the same first formula in (1), for **every** array. The exact minima, equality families and gaps carry over unchanged.

## Verification
Run `python3 CHECK.py` from a directory containing the extracted source file, using Python 3 and its standard library only. The completed execution reports `CHECK_OK 1751969 exact normalized arrays`, following separate checks for each alphabet. It verifies the arithmetic roots, both descriptions of the fourth moment, the four exhaustive minima, the next values, full minimizer counts, and every orbit representative and size. A separate floating-point batch implementation of the 45 sum-frequency coefficients was used as a supplementary cross-check, but does not enter the proof. The decisive certificate is the exact, finite, **exhaustive** loop just described; the analytic argument establishes why that loop covers the asserted domain. No computation establishes an optimum for arbitrary continuous phases.

## Relationship to prior work
Wang's 2026 work on two- and four-phase Golay complementary sequences develops complementary **pairs** and construction families, rather than solving this single-array full-aperiodic fourth-moment minimum for a twelve-point three-dimensional prism; the accessible abstract does not state the present table. Svalbe and Tirkel (2017) study primarily periodic perfect-array families and cross-correlations on two-dimensional prime-size grids, not the exact single-prism fourth-moment classification. Published full texts for the six-mode Fourier rectangle, the eight-mode Fourier cube and the nine-mode Fourier square analyze **different** support sets; none of their inequalities or equality classifications implies the values here for the complete \(2\times2\times3\) prism. The cubic case has eight rather than twelve coefficients and the square and rectangular cases are two-dimensional, so adding the remaining frequencies changes the autocorrelation constraint system rather than preserving a minimizing subclass. Prior research could still contain an unindexed equivalent in engineering polyphase-array catalogs.

## Limitations
The exhaustive certificate has precisely the four finite alphabets and stated support geometry as its domain. The result does **not** prove that 188 is the unrestricted continuous-phase minimum, nor any classification for other alphabets. The no-aliasing transfer requires the stated lower bounds on grid orders. An older exact table not found in accessible searches remains a residual originality risk. The 2026 Golay preprint's full text was not accessible during the comparison, though its abstract describes a different pair-construction problem. No independent validation or audit is asserted.

## References
1. Xu Wang, *A construction method for 2-phase and 4-phase Golay Complementary Sequences*, arXiv:2606.17651, first public 16 June 2026, https://arxiv.org/abs/2606.17651 .
2. I. D. Svalbe and A. Z. Tirkel, *Extended families of 2D arrays with near optimal auto and low cross-correlation*, EURASIP Journal on Advances in Signal Processing 2017, article 18, https://doi.org/10.1186/s13634-017-0455-2 .
3. *Exact fourth-moment rigidity of the eight-mode cubic Fourier aperture* (2026), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-fourth-moment-rigidity-of-the-eight-mode-cubic-fourier-ape--486a31ac0a2d/RESULT.md .
4. *Sharp phase-alphabet fourth moments for the nine-mode square Fourier aperture* (2026), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-phase-alphabet-fourth-moments-for-the-nine-mode-square-fou--f31c28437f0d/RESULT.md .
5. *Exact fourth-moment range and all phase orbits of a six-mode Fourier rectangle* (2026), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-fourth-moment-range-and-all-phase-orbits-of-a-six-mode-fou--5147476c65ae/RESULT.md .
