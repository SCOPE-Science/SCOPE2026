# A determinant-sign phase law for balanced six-season stage-specific population interventions

## Finding

Consider a strictly positive two-stage annual population projection matrix
\[
L=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad a,b,c,d>0.
\]
Before each projection the population is subjected either to a juvenile-stage treatment, multiplying juveniles by \(u\), or to an adult-stage treatment, multiplying adults by \(v\), with \(0<u,v<1\). Denote the annual matrices by
\[
J=L\operatorname{diag}(u,1),\qquad A=L\operatorname{diag}(1,v).
\]
Exactly three treatments of each kind are scheduled in a six-season period, in any of the \(\binom63=20\) orders. Let \(T_w\) denote the trace and \(G_w\) the sixth root of the spectral radius of the six-season matrix product. The twenty orders fall into at most three distinct growth levels: a blocked value \(G_B\), a mixed value \(G_M\), and an alternating value \(G_T\). They satisfy the **complete and sharp phase law**
\[
\begin{array}{lll}
ad<bc &: &G_T>G_M>G_B,\\[2pt]
ad>bc &: &G_B>G_M>G_T,\\[2pt]
ad=bc &: &G_T=G_M=G_B.
\end{array}
\]
The sign determining the ordering is **independent of both treatment-survival fractions** \(u,v\) inside the stated open parameter range. Thus the ordering changes at the rank-one boundary \(\det L=0\), not at a treatment-intensity threshold.

Write \(T_B,T_M,T_T\) for the corresponding traces. The exact gaps, valid without numerical approximation, are
\[
T_M-T_B=-bc(ad-bc)(d+au)(a+dv)(1-uv)^2,
\]
\[
T_T-T_M=-bc(ad-bc)\bigl(bc(1+uv)+a^2u+d^2v\bigr)(1-uv)^2.
\]
These equations and a common determinant completely determine the ordering of all twenty periodic schedules.

For one biologically interpretable example, take
\[
L=\begin{pmatrix}1/5&5/4\\3/5&1/2\end{pmatrix},\qquad u=1/2,\quad v=2/3.
\]
Here \(a+c=4/5\) and \(d=1/2\) are feasible survival/transition fractions, with adult fecundity \(b=5/4\). The exact blocked, mixed and alternating traces are respectively
\[
\frac{5691779}{6750000},\quad
\frac{6159779}{6750000},\quad
\frac{7895279}{6750000},
\]
while every six-season product has determinant \(4826809/1728000000\). Its positive characteristic polynomial evaluated at one is positive for blocked and mixed schedules and negative for alternating schedules. Hence \(G_B<1\), \(G_M<1\), but \(G_T>1\): **the same number of both stage treatments can yield population decline or growth solely through their seasonal order** in this model.

## Assumptions and scope

A population vector has two nonnegative components (juvenile and adult). The untreated linear projection first counts stage-specific survivors/transitions and reproductive recruitment through \(L\). Each season either juvenile reduction \(\operatorname{diag}(u,1)\) or adult reduction \(\operatorname{diag}(1,v)\) is applied before that season's projection. Exactly three of each treatment are used per period; a season cannot use both. No density dependence, demographic noise, seasonal variation in \(L\), or treatment carryover is assumed. All four entries of \(L\) must be strictly positive, and the fractions satisfy \(0<u,v<1\).

A word \(w\) records the matrices in product order; the chronological matrix product uses its reversal. The trace of a product of two \(2\times2\) matrices with only two letter types equals the trace of its reversal (Greene, Theorem 1.1), and the determinant is unchanged, so the stated spectral classification also applies directly to chronological schedules. The six-season growth factor is \(\rho(M_w)\); the annualized factor is \(G_w=\rho(M_w)^{1/6}\). Periodic repetition of the same word is required for the asymptotic interpretation.

The primary mathematical domain is \(a,b,c,d>0\) without additional life-history feasibility constraints; the worked example separately meets \(a+c\le1\) and \(d\le1\). The statement is not asserted for zero entries, zero/complete treatment survival, unequal intervention counts, arbitrary seasons, or matrices without a common base \(L\).

## Proof

**1. Every schedule belongs to one of four cyclic classes.** Directly selecting which three of six positions are marked \(J\) gives twenty words. Up to cyclic rotation their representatives and orbit sizes are:

| Class | Representative | Number of words |
|---|---|---:|
| Blocked | `JJJAAA` | 6 |
| Mixed I | `JJAJAA` | 6 |
| Mixed II | `JJAAJA` | 6 |
| Alternating | `JAJAJA` | 2 |

These orbit sizes sum to twenty. Trace is invariant under cyclic permutations. Mixed I and Mixed II have the same trace because one representative is cyclically equivalent to the reversal of the other and two-letter products of \(2\times2\) matrices have reversal-invariant trace; see Greene, Theorem 1.1. Thus there are at most three distinct traces.

**2. Product determinants are identical.** Multiplicativity yields
\[
\det J=u(ad-bc),\quad \det A=v(ad-bc),\quad
\Delta=\det M_w=(ad-bc)^6(uv)^3
\]
for every balanced six-season word \(w\).

**3. Exact trace identities.** Starting from the two displayed annual matrices, ordinary \(2\times2\) multiplication gives the explicit matrix-product identities
\[
\begin{aligned}
&\operatorname{tr}(J^2AJA^2)-\operatorname{tr}(J^3A^3)\\
&\hspace{6mm}=-bc(ad-bc)(d+au)(a+dv)(1-uv)^2,
\end{aligned}
\]
\[
\begin{aligned}
&\operatorname{tr}((JA)^3)-\operatorname{tr}(J^2AJA^2)\\
&\hspace{6mm}=-bc(ad-bc)\bigl(bc(1+uv)+a^2u+d^2v\bigr)(1-uv)^2.
\end{aligned}
\]
Both follow by expansion and collecting the terms in the six scalar parameters; they can also be reproduced symbolically by the accompanying `verify.py`, which checks each difference as an identically zero polynomial after subtracting its stated factorization. No numerical sampling is used to prove the identities.

Every factor other than the leading minus sign and \(ad-bc\) is **strictly positive**: this uses exactly the stated assumptions \(a,b,c,d>0\) and \(0<u,v<1\). Consequently the trace ordering is strictly increasing from blocked to mixed to alternating when \(ad<bc\), strictly decreasing when \(ad>bc\), and all traces coincide when \(ad=bc\).

**4. Trace ordering is growth ordering.** Every six-season product is entrywise positive. Its characteristic polynomial is \(\lambda^2-T_w\lambda+\Delta\), with \(\Delta\ge0\). The Perron root is
\[
\rho(M_w)=\frac{T_w+\sqrt{T_w^2-4\Delta}}{2}.
\]
At fixed \(\Delta\), this root is strictly increasing in \(T_w\) for the present entrywise positive matrices. Because all words have the same \(\Delta\), the trace inequalities prove the claimed strict growth inequalities. If \(ad=bc\), all traces and determinants agree, hence all Perron roots agree. This proves all cases for every admissible real parameter tuple, not only the checked rational examples.

**5. Exact growth/decline witness.** For the displayed rational \(L,u,v\), direct multiplication produces the three displayed traces and common \(0<\Delta<1\). The values of \(1-T_w+\Delta\) for blocked, mixed and alternating programs are respectively
\[
\frac{55146277}{345600000},\qquad
\frac{31184677}{345600000},\qquad
-\frac{57672923}{345600000}.
\]
Since \(0<\Delta<1\), a positive \(2\times2\) product has Perron root less than one exactly when this characteristic-polynomial value is positive. The first two schedules therefore decline and the third grows under repeated six-year cycles.

## Verification

Run `python verify.py` with Python 3 and SymPy 1.12 or newer (see `requirements.txt`). It constructs \(J,A\) symbolically and checks the two trace-gap polynomial factorizations, equality of mixed traces, a common determinant, the four cyclic orbit sizes, and membership of all twenty schedules. A separately implemented exact-rational matrix multiplier checks 192 parameter tuples without floating-point arithmetic and verifies a strict decline/growth witness. Observed output:

```
VERIFY_OK: symbolic six-season polynomial identities, 20-word exhaustive partition, 192 independent exact-rational parameter tests, growth/decline witness
```

The symbolic polynomial identities and the finite orbit partition support the universal proof; 192 rational tests alone would not prove it. All checked computations arise from the standalone embedded file, not from external state.

## Relationship to prior work

Mertens, van den Bosch and Heesterbeek (2002) established the ecological importance of seasonal order in crop-rotation matrix models and numerically compared two- through six-year rotations. Their model incorporates seed-depth structure and plowing; the available abstract does not state the exact two-stage shared-matrix determinant-sign theorem here. The most directly overlapping statement—sequence matters—is therefore **prior work**, not claimed as new. Complete text of that study was not accessible during this comparison; a matching result in its full text remains a residual risk.

Greene (2014), Theorem 1.1, establishes reversal invariance for two-letter \(2\times2\) trace products. This covers one ingredient, the equivalence of the two mixed cyclic classes; it does not fix their strict ordering relative to blocked or alternating stages under the shared projection-treatment hypothesis. Schneider (2015) explicitly identifies four six-letter necklace classes and studies broad relative-trace orders for general matrices, but does not give the specialized sharp \(\operatorname{sgn}(ad-bc)\) criterion for the two pre-projection stage interventions.

Alaifari, Cheng, Pierce and Steinerberger (arXiv:1904.05239), Theorem 1, prove a rearrangement bound for the **operator norm** of products of two symmetric positive-semidefinite \(2\times2\) matrices. The present treatment matrices are generally nonsymmetric and not jointly symmetrizable; the result here orders Perron roots and admits the opposite ranking when \(ad<bc\). Their theorem therefore does not subsume this population-growth phase law. The novelty asserted here is solely the complete specialized six-season stage-intervention classification and its exact phase boundary, not matrix periodicity or necklace/reversal invariance generally.

## Limitations

The theorem is restricted to a positive two-stage common-baseline projection with *pre-projection diagonal* intervention matrices and exactly three annual treatments of each type in six seasons. It does not optimize monetary cost, ecological diversity, transient stage distributions, arbitrary multistage models, or demographic stochastic extinction. The precise treatment fractions influence the actual growth factors even though they do not influence the ranking. The original 2002 crop-rotation paper's full text could not be inspected; a stronger unpublished or unindexed result remains possible. No independent mathematical audit has been performed.

## References

1. S. K. Mertens, F. van den Bosch and J. A. P. Heesterbeek, “Weed populations and crop rotations: exploring dynamics of a structured periodic system,” *Ecological Applications* 12 (2002), 1125–1141, DOI: 10.1890/1051-0761(2002)012[1125:WPACRE]2.0.CO;2; first online 2002-08-01.
2. J. Greene, “Traces of Matrix Products,” *Electronic Journal of Linear Algebra* 27 (2014), 716–734, DOI: 10.13001/1081-3810.1999.
3. A. Schneider, *Investigating Traces of Matrix Products*, MS thesis, University of Minnesota Duluth, May 2015, https://www.d.umn.edu/~jgreene/masters_reports/Andrew%20S%20Paper.pdf.
4. R. Alaifari, X. Cheng, L. B. Pierce and S. Steinerberger, “On Matrix Rearrangement Inequalities,” arXiv:1904.05239 (2019), https://arxiv.org/abs/1904.05239.
