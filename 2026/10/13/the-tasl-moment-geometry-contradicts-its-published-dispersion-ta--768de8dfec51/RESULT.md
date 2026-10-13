# The TASL moment geometry contradicts its published dispersion table
## Finding
The tri-modal alpha-skew logistic (TASL) distribution introduced in the primary source has, for every real \(\alpha\) and \(x\in\mathbb R\), density
\[
f_\alpha(x)=\frac{[(1-\alpha x)^2+1][(x^2-1)^2+2]}{C(\alpha)}\frac{e^{-x}}{(1+e^{-x})^2},
\]
with
\[
C(\alpha)=c_0+c_2\alpha^2,
\quad
c_0=\frac{98\pi^4-140\pi^2+630}{105},
\quad
c_2=\frac{155\pi^6-98\pi^4+105\pi^2}{105}.
\]
Define also
\[
d_2=\frac{889\pi^8-310\pi^6+147\pi^4}{105}.
\]
The exact mean, second raw moment and variance are
\[
\mu(\alpha)=-\frac{2c_2\alpha}{c_0+c_2\alpha^2},
\quad
m_2(\alpha)=\frac{2c_2+d_2\alpha^2}{c_0+c_2\alpha^2},
\quad
V(\alpha)=m_2(\alpha)-\mu(\alpha)^2.
\]
In particular, \(\mu(-\alpha)=-\mu(\alpha)\), \(V(-\alpha)=V(\alpha)\), and \(\mu(\alpha)\) has the sign opposite to \(\alpha\) whenever the parameter is nonzero.

**Exact mean phase.** The magnitude of the mean strictly increases from zero to a single maximum and then strictly decreases back toward zero as \(\lvert\alpha\rvert\) increases. Its unique positive-magnitude maximizer is
\[
a_m=\sqrt{\frac{c_0}{c_2}}=0.250181420197\ldots,
\qquad
\max_{\alpha\in\mathbb R}|\mu(\alpha)|=\sqrt{\frac{c_2}{c_0}}=3.997099381767\ldots.
\]

**Exact variance phase.** Put
\[
\Delta=d_2c_0-2c_2^2.
\]
Then \(0<\Delta<4c_2^2\) and the derivative of variance with respect to \(u=\alpha^2\) is
\[
\frac{dV}{du}=
\frac{c_0(\Delta-4c_2^2)+c_2u(\Delta+4c_2^2)}{(c_0+c_2u)^3}.
\]
Thus variance strictly decreases on \(0\le|\alpha|<a_v\), and strictly increases on \(|\alpha|>a_v\), where
\[
a_v=\sqrt{\frac{c_0(4c_2^2-\Delta)}{c_2(\Delta+4c_2^2)}}
=0.162259089275\ldots,
\quad
V(a_v)=26.350882362830\ldots.
\]
At infinity,
\[
\lim_{|\alpha|\to\infty}V(\alpha)=\frac{d_2}{c_2}=58.0161637186\ldots.
\]
Hence a larger magnitude of the shape parameter *does not* invariably reduce dispersion; beyond the unique turning point it increases it.

**Correction of the source numerical table.** The source's Table 1 prints positive means and variances smaller than \(1.5\) for the eight parameter values below. The density instead yields the following values (twelve decimal places, with numerical integration independently checking the moment formulas):

| \(\alpha\) | Correct mean | Correct variance |
|---:|---:|---:|
| -2 | 0.984593392007 | 56.645203975384 |
| -1 | 1.882192192199 | 52.938329930080 |
| -0.5 | 3.199071061301 | 42.563544077327 |
| 0.5 | -3.199071061301 | 42.563544077327 |
| 1 | -1.882192192199 | 52.938329930080 |
| 2 | -0.984593392007 | 56.645203975384 |
| 3 | -0.662062336273 | 57.397836247981 |
| 5 | -0.399001049115 | 57.791873846003 |

For instance, at \(\alpha=0.5\) the table prints mean \(2.253\) and variance \(1.478\), whereas the correct mean is *negative* and the variance is over \(42\). The source additionally describes the table as showing a mean increasing monotonically with \(|\alpha|\), a decreasing variance, and positive skewness at both parameter signs. The first two statements are disproved by the exact turning-point classifications; the reflection identity also forces any defined skewness coefficient to be odd in the parameter.

The source's own analytical first and second moment expressions on the preceding page, together with its Figure 3, essentially agree with the corrected moment geometry. The discrepancy lies in the numerical table and the explanatory claims that depend on it.

## Assumptions and scope
The density is the unshifted, unscaled TASL model from the source; all \(x\in\mathbb R\) and all \(\alpha\in\mathbb R\) are included. All polynomially weighted logistic moments used below are finite.

The findings concern raw population moments in the source's original units. Scaling the observation variable changes the numerical variance, but cannot repair a table presented for the stated unscaled density. The work neither recomputes the authors' fitted astronomical or biomedical data nor infers the implementation used for simulation.

## Proof
Write the standard logistic density as
\[
\ell(x)=\frac{e^{-x}}{(1+e^{-x})^2},
\]
which is even. Its needed even moments are
\[
M_0=1,\quad M_2=\frac{\pi^2}{3},\quad M_4=\frac{7\pi^4}{15},
\quad M_6=\frac{31\pi^6}{21},\quad M_8=\frac{127\pi^8}{15}.
\]
Expansion of the two polynomial factors yields
\[
[(1-\alpha x)^2+1][(x^2-1)^2+2]
=\alpha^2x^6-2\alpha x^5+(2-2\alpha^2)x^4+4\alpha x^3
+(3\alpha^2-4)x^2-6\alpha x+6.
\]
All odd powers vanish upon integration against \(\ell\). Hence
\[
C(\alpha)=(2M_4-4M_2+6)+\alpha^2(M_6-2M_4+3M_2)=c_0+c_2\alpha^2.
\]
Multiplying the expansion by \(x\) or by \(x^2\), and using parity, gives
\[
E[X_\alpha]=-\frac{2\alpha(M_6-2M_4+3M_2)}{C(\alpha)},
\]
\[
E[X_\alpha^2]=\frac{2(M_6-2M_4+3M_2)+\alpha^2(M_8-2M_6+3M_4)}{C(\alpha)}.
\]
These simplify to the formulas in the finding. They also follow directly from the source's analytic moment formulas.

For \(a=|\alpha|\), the magnitude of the mean is
\[
|\mu(\alpha)|=\frac{2c_2a}{c_0+c_2a^2}.
\]
Its derivative has the sign of \(c_0-c_2a^2\), giving a unique positive maximum at \(a_m\) and the limit zero at infinity.

For the variance, set \(u=a^2\). Differentiating the rational expression gives the stated derivative. To establish the strict inequalities governing its sign, put \(t=\pi^2>9\). Direct factorization gives
\[
\Delta=\frac{32t^2}{3675}(407t^4-980t^3+5558t^2-1820t+735)>0,
\]
\[
4c_2^2-\Delta=\frac{4t^2}{11025}
(14257t^4-6860t^3-91238t^2+23100t-6615)>0.
\]
The first quartic is positive because \(t^3(407t-980)>0\) and \(5558t^2-1820t+735>0\) for \(t>9\). The second is positive because \(t^2(14257t^2-6860t-91238)>0\) and \(23100t-6615>0\) for \(t>9\). Therefore the derivative numerator is strictly increasing in \(u\), begins negative and becomes positive, so has the unique stated positive root. Taking \(a\to\infty\) proves the variance limit.

Finally, replacing \(\alpha\) by \(-\alpha\) and \(x\) by \(-x\) in the density gives \(f_{-\alpha}(-x)=f_\alpha(x)\). Hence odd central moments reverse sign and even central moments are invariant. That is incompatible with interpreting a positive skewness number as valid at both opposite nonzero parameter signs unless the coefficient vanishes.

## Verification
The enclosed standalone Python checker independently constructs logistic moments, verifies the polynomial-normalization and raw-moment identities with symbolic algebra, factors the variance derivative, verifies the two positivity certificates, computes all eight corrected table rows, and uses high-precision direct quadrature of the normalized density at representative shape parameters. Assertions compare quadrature and formulas and check the exact phase transitions. Run \(\texttt{python verify_tasl_moments.py}\) with the ordinary Python packages SymPy and mpmath installed. The proof, not the finite numerical sampling, establishes the global parameter claims.

## Relationship to prior work
The 2026 source's Section 3.1 correctly derives analytical raw moments and gives a figure consistent with their signed-mean and nonmonotone-variance behavior, while its immediately following Table 1 and prose contradict both the density and those formulas. The correction is a source-specific exact reconciliation, not a claim that the preceding moment equations are new.

A 2025 flexible alpha-skew logistic model shares the general polynomially modified logistic approach but uses a different density/parameterization; its moments and tables do not cover the present TASL table. Standard logistic moments are classical inputs and likewise do not themselves contain this article-specific correction. Exact-title, DOI, distribution-alias, mean/variance, turning-point, Table 1 and erratum searches found no published reconciliation of the displayed contradictory TASL values.

## Limitations
The correction is to Table 1 and the attached interpretation, not to the source's preceding correct raw-moment formulas or to its plotted Figure 3. No empirical refitting or revision of source data is undertaken. The dispersion statements compare raw population variances of the fixed-scale density. A later or unindexed correction could exist. This note does not prove which computation generated the erroneous table.

## References
1. R. Elbarougy, J. Das, P. J. Hazarika, G. G. Hamedani, A. Nandi, and M. S. Eliwa, “A novel one-parameter tri-modal alpha-skew logistic distribution: mathematical and reliability theory with applications to distant astronomical galaxies and biomedical data,” AIMS Mathematics 11 (2026), 7436–7467. DOI: 10.3934/math.2026305.
2. J. Das and collaborators, “On the Flexible Alpha Skew-logistic Distribution: Properties and Applications,” Austrian Journal of Statistics (2025). DOI: 10.17713/ajs.v54i2.1902.
