# Exact fixed-weight capacities for binary short-overlap synchronization codes

## Finding

A binary code \(\mathcal C\subseteq\{0,1\}^n\) is *three-short-overlap-free* when, for every ordered pair \(u,v\in\mathcal C\) (including \(u=v\)) and every \(t\in\{1,2,3\}\), the length-\(t\) prefix of \(u\) differs from the length-\(t\) suffix of \(v\). Write \(M_3(n,w)\) for its maximum cardinality under the additional requirement that every codeword has Hamming weight exactly \(w\).

**Exact fixed-weight optimum.** For every integer \(n\ge6\) and \(0\le w\le n\),

\[
\begin{aligned}
M_3(n,w)=\max\Big\{&\binom{n-4}{w-1},\\
&2\binom{n-5}{w-2}+\binom{n-5}{w-3},\\
&\binom{n-5}{w-2}+2\binom{n-5}{w-3},\\
&\binom{n-4}{w-3}\Big\}.
\end{aligned}
\]

Here \(\binom ab=0\) whenever \(b<0\) or \(b>a\). An optimal code for **each** \((n,w)\) is obtained by intersecting one of only four explicit regular boundary-template codes with the constant-weight layer. The complementary orientation offers no larger value.

**Four asymptotic phases.** If \(0<\alpha<1\) and \(w/n\to\alpha\), then

\[
\lim_{n\to\infty}\frac{M_3(n,w)}{\binom nw}
=\max\big\{\alpha(1-\alpha)^3,\;\alpha^2(1-\alpha)^2(2-\alpha),\;\alpha^2(1-\alpha)^2(1+\alpha),\;\alpha^3(1-\alpha)\big\}.
\]

Away from three transition densities, the uniquely largest template term changes in order from the first to the fourth at

\[
\boxed{\frac{3-\sqrt5}{2},\quad\frac12,\quad\frac{\sqrt5-1}{2}}.
\]

These are transitions of the **optimal boundary-template type**, not assertions about physical thermodynamic transitions or noisy-channel capacity.

## Assumptions and scope

The alphabet is labeled \(\{0,1\}\); words are linear, not circular, and have common length \(n\ge6\). Overlaps of *exactly* lengths \(1,2,3\) are prohibited in either direction, even within the same word. Larger overlaps are permitted. The empty code is admitted, accounting for extreme weights where no admissible word exists. The information-theoretic maximum refers to the zero-error cardinality for precisely this restricted-overlap constraint, with no additional Hamming-distance or biochemical requirements.

For code constructions, concatenation of words is denoted by juxtaposition. Let \(\mathcal T_j(n)\) be the set of **all** words \(pms\) with a prefix \(p\in P_j\), an arbitrary middle \(m\in\{0,1\}^{n-6}\), and a suffix \(s\in S_j\). Define the following four boundary tables:

| Template | \(P_j\) | \(S_j\) | Boundary weight polynomial \(H_j(z)\) |
|---|---|---|---|
| 1 | `000` | `001`, `011`, `101`, `111` | \(z(1+z)^2\) |
| 2 | `000`, `001` | `011`, `101`, `111` | \(z^2(1+z)(2+z)\) |
| 3 | `000`, `001`, `010` | `011`, `111` | \(z^2(1+z)(1+2z)\) |
| 4 | `000`, `001`, `010`, `011` | `111` | \(z^3(1+z)^2\) |

The actual optimal weight-\(w\) code is \(\mathcal T_j(n)\cap\{x:\mathrm{wt}(x)=w\}\), choosing any template maximizing the displayed exact formula.

## Proof

**1. Orient the endpoints.** If \(\mathcal C\) is nonempty, its overlap condition for \(t=1\) forces every codeword to start with the same bit and end with the opposite bit. Indeed, choose a word starting with \(a\). Every word must end in \(1-a\); choosing such an ending forces every beginning to be \(a\). Bit complementation exchanges the two possible orientations. We first assume that all words start with `0` and end with `1`.

**2. Classify all compatible three-bit boundaries.** The possible prefixes in this orientation are \(000,001,010,011\), and the possible suffixes are \(001,011,101,111\). For each prefix \(p\), let \(N(p)\) consist of suffixes \(s\) for which no prefix of \(p\) of length \(1,2,3\) equals the corresponding-length suffix of \(s\). Direct comparisons give

\[
\begin{aligned}
N(000)&=\{001,011,101,111\},\\
N(001)&=\{011,101,111\},\\
N(010)&=\{011,111\},\\
N(011)&=\{111\}.
\end{aligned}
\]

The first boundary bit already differs, so the length-one comparison always passes in this orientation. The length-two comparisons forbid suffixes ending in `01` when the prefix starts `01`. Equality of the entire three-bit blocks additionally forbids `001` paired with `001` and `011` paired with `011`. Thus the four displayed neighborhoods are complete, and crucially are **nested** in the indicated order.

Let \(j\) be the largest index of a prefix appearing in \(\mathcal C\), in the order \(000,001,010,011\). Every occurring prefix is in \(P_j\), and every occurring suffix belongs to \(N(p_j)=S_j\), because the prefix \(p_j\) does occur and must be compatible with every suffix. Consequently

\[
\mathcal C\subseteq\mathcal T_j(n).
\]

Conversely, any pair of boundaries from \(P_j\times S_j\) is compatible: the neighborhoods are nested, so \(S_j\subseteq N(p)\) for each \(p\in P_j\). Since \(n\ge6\), prefix and suffix blocks do not overlap physically; all intervening bits are unrestricted. Hence each \(\mathcal T_j(n)\) is a valid three-short-overlap-free code. This proves that *four universal templates suffice* for optimizing every fixed-weight layer in orientation `0` to `1`.

**3. Count exact weights.** For any boundary pair \((p,s)\), the number of permitted middles of weight \(w-\mathrm{wt}(p)-\mathrm{wt}(s)\) is exactly \(\binom{n-6}{w-\mathrm{wt}(p)-\mathrm{wt}(s)}\). The boundary generating polynomial is

\[
H_j(z)=\sum_{p\in P_j}\sum_{s\in S_j}z^{\mathrm{wt}(p)+\mathrm{wt}(s)},
\]

and the full template weight enumerator is \((1+z)^{n-6}H_j(z)\). Direct multiplication of the four boundary tables gives precisely the four polynomials displayed under “Assumptions and scope”. Their weight-\(w\) coefficients are, respectively,

\[
\binom{n-4}{w-1},\quad
2\binom{n-5}{w-2}+\binom{n-5}{w-3},\quad
\binom{n-5}{w-2}+2\binom{n-5}{w-3},\quad
\binom{n-4}{w-3}.
\]

Every code in the chosen orientation embeds in one of these templates, and every template is attainable. So their maximum is exact. For the opposite orientation, complementing the six boundary bits transforms \(H_j(z)\) into \(z^6H_j(z^{-1})=H_{5-j}(z)\); these are the same four polynomials in reversed order. No extra extremal value occurs. The exact theorem follows, including boundary weights \(w=0,n\) under the out-of-range binomial convention.

**4. Derive the asymptotic transitions.** For fixed integers \(d,r\) and \(w/n\to\alpha\in(0,1)\), elementary factorial cancellation gives

\[
\frac{\binom{n-d}{w-r}}{\binom nw}\longrightarrow
\alpha^r(1-\alpha)^{d-r}
\]

when \(0\le r\le d\). Apply this to each term of the finite exact maximum to obtain the four functions in the statement. The adjacent equality equations simplify to \(\alpha^2-3\alpha+1=0\), \(2\alpha-1=0\), and \(\alpha^2+\alpha-1=0\), respectively. Checking the signs between their roots (and the nonadjacent comparisons) shows that the dominant function progresses from template 1 to 2, 3, and 4 as \(\alpha\) increases. The limits hold for any integer sequence of weights satisfying the asserted ratio, and uniqueness of the leading template is only claimed away from the three thresholds. This finishes the proof.

## Verification

The supplied standalone script `verify.py` independently constructs all length-three boundary compatibility relations and exhaustively checks all \(255\) nonempty three-prefix subsets, including the \(30\) subsets with a nonempty compatible suffix set. It verifies complete coverage by the four templates and compares direct boundary-pair binomial summation with the theorem for every \(n\in\{6,\ldots,30\}\) and every \(0\le w\le n\), totaling \(475\) parameter pairs. It also constructs \(1{,}260\) literal template words across lengths \(6\) through \(11\), checks pairwise nonoverlap and their weight spectra, and runs an independent exhaustive maximum-clique search on literal words in \(24\) weight/length cases up to \(n=8\).

The exact execution reported:

```text
VERIFY_OK exact_prefix_subsets=255 viable_subsets=30 rectangle_parameter_cases=475 literal_template_words=1260 literal_clique_cases=24 n_range=6..30
```

The general theorem does **not** rely on finite experimentation: the nested-neighborhood proof handles every allowed length and weight. The finite program corroborates the boundary list and formulas and is reproducible with a standard Python 3 interpreter, without third-party dependencies.

## Relationship to prior work

Blackburn, Nasr Esfahani, Kreher, and Stinson [1] introduce binary codes forbidding an interval of overlap sizes. Their Theorems 5, 7, and 8 give a boundary-set/independent-set framework and solve the unrestricted-cardinality version for small forbidden-overlap parameters. In particular, their unrestricted \((1,3)\) optimum uses templates having six possible boundary pairs, corresponding to the second and third templates above. **Unrestricted cardinality does not determine the fixed-weight optimum:** for low or high relative weight, the four-pair templates become optimal, and even the asymptotically optimal boundary family changes at nontrivial densities. The exact fixed-weight formula and golden-ratio changeovers require retaining boundary weight distributions rather than their sums.

Wang and Wang [2] analyze generating functions for classical codes forbidding *all* proper overlaps and their variable-length generalizations, which use a different forbidden-overlap set. Blackburn [3] studies the classical all-overlaps case. Stanovnik [4] classifies expandability and gives constructions and bounds for restricted-overlap codes, likewise without a fixed-weight optimum for the binary three-short-overlap setting. Those works do not provide the present four-term fixed-weight optimum or its density-dependent boundary transitions. The possibility that a specialized fixed-composition result elsewhere has an equivalent formulation is not excluded merely by the searches performed.

## Limitations

Only binary codes and forbidden overlap lengths \(1,2,3\) are classified. For length below six, the three-symbol prefix and suffix blocks meet and the product decomposition used here does not apply; no result is claimed for that range. The result is about deterministic synchronization exclusions, not noise correction, thermodynamic phase transitions, or a general four-letter DNA alphabet. The asymptotic template selection is strict only away from the three listed densities; finite-length ties and transition-window behavior are governed by the exact finite formula. The originality comparison does not substitute for a complete external literature review, and independent validation has not been performed.

## References

1. S. R. Blackburn, N. Nasr Esfahani, D. L. Kreher, and D. R. Stinson, “Constructions and bounds for codes with restricted overlaps,” arXiv:2211.10309, first public 2022-11-18. Full public text: https://arxiv.org/html/2211.10309v4 . Especially Sections I, III, IV and VII and Theorems 5, 7, 8.
2. G. Wang and Q. Wang, “Q-ary non-overlapping codes: a generating function approach,” arXiv:2108.06934, first public 2021-08-16. Public text: https://arxiv.org/abs/2108.06934 .
3. S. R. Blackburn, “Non-overlapping codes,” arXiv:1303.1026, first public 2013-03-05. Abstract and references: https://arxiv.org/abs/1303.1026 .
4. L. Stanovnik, “Codes with restricted overlaps: expandability, constructions, and bounds,” *Journal of Applied Mathematics and Computing* 71 (2025), 591–616, published 2025-04-28. Full public text: https://link.springer.com/article/10.1007/s12190-025-02441-z . Particularly Sections 2 and 4.1.
