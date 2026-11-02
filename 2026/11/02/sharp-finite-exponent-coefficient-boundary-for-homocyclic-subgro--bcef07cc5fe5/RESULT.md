# Sharp finite-exponent coefficient boundary for homocyclic subgroup polynomials

## Finding

For integers \(r\ge 2\) and \(a\ge1\), let \(P_{r,a}(p)\in\mathbb Z[p]\) be the polynomial whose value at each prime \(p\) equals the total number of subgroups of the homocyclic abelian group \((C_{p^a})^r\). Define its degree and reversed polynomial by
\[
D_{r,a}=a\left\lfloor\frac{r^2}{4}\right\rfloor,
\qquad F_{r,a}(t)=t^{D_{r,a}}P_{r,a}(t^{-1}).
\]
For \(s\ge1\), define the formal series
\[
\Xi_{2s}(t)=\begin{bmatrix}2s\\s\end{bmatrix}_t
\prod_{j=1}^{s}\frac1{(1-t^j)^2}
=\frac{\prod_{j=1}^{2s}(1-t^j)}{\bigl(\prod_{j=1}^{s}(1-t^j)\bigr)^4}.
\]
Here the bracket is the Gaussian binomial polynomial. The following statements form one coefficient-rigidity theorem.

**Even rank, with sharp boundary.** For every \(s,a\ge1\),
\[
\Xi_{2s}(t)-F_{2s,a}(t)
=(2a+3)t^{a+1}+t^{a+2}R_{s,a}(t),
\qquad R_{s,a}(t)\in\mathbb Z_{\ge0}[[t]].
\]
Consequently all coefficients of codegree at most \(a\) agree *exactly* with the published limiting series, and the first unequal coefficient is at codegree \(a+1\), where the shortfall is \(2a+3\), independently of \(s\).

**Odd rank, with eventual affine behavior.** For every \(s\ge1\) and fixed integer \(k\ge0\), the coefficient \([t^k]F_{2s+1,a}(t)\) is an affine function of the exponent \(a\) for all \(a\ge k+2\). The first two coefficients, valid for every \(a\ge1\), are
\[
[t^0]F_{2s+1,a}=a+1,\qquad [t^1]F_{2s+1,a}=2a.
\]
In even rank the corresponding coefficients are \([t^0]F_{2s,a}=1\) and \([t^1]F_{2s,a}=3\). The leading coefficients and limiting series themselves are previously known; the precise finite boundary, universal defect, and odd finite-exponent affine law are the claims here.

## Assumptions and scope

All polynomial identities are identities with integer coefficients, hence hold simultaneously for every prime \(p\); no restriction to odd primes is made. The variable \(t\) is formal. For a polynomial of degree \(D\), its *codegree-\(k\) coefficient* is the coefficient of \(p^{D-k}\), equivalently \([t^k]\) of the reversed polynomial (zero if \(k>D\)). The theorem concerns homocyclic groups of rank at least two; the cyclic case has constant subgroup polynomial \(a+1\).

Let \(\begin{bmatrix}n\\m\end{bmatrix}_t\) denote the Gaussian polynomial (zero outside \(0\le m\le n\)); it has constant coefficient one in its valid range and is reciprocal of degree \(m(n-m)\). Put \(h_{a+1}=0\) for all height chains below.

## Proof

**1. Normalized Delsarte formula.** A subgroup type of \((C_{p^a})^r\) has conjugate column heights \(r\ge h_1\ge\cdots\ge h_a\ge0\). Delsarte's subgroup-type formula gives
\[
P_{r,a}(p)=\sum_{h_1\ge\cdots\ge h_a}
\prod_{i=1}^{a}p^{h_{i+1}(r-h_i)}
\begin{bmatrix}r-h_{i+1}\\h_i-h_{i+1}\end{bmatrix}_p.
\]
Each summand has degree \(\sum_i h_i(r-h_i)\), so the full degree is \(D_{r,a}\). Reciprocity of Gaussian polynomials yields the *exact* reversed expression
\[
F_{r,a}(t)=\sum_{h_1\ge\cdots\ge h_a}
 t^{\sum_{i=1}^{a}\delta_r(h_i)}
\prod_{i=1}^{a}\begin{bmatrix}r-h_{i+1}\\h_i-h_{i+1}\end{bmatrix}_t,
\quad \delta_r(h)=\left\lfloor\frac{r^2}{4}\right\rfloor-h(r-h).
\tag{1}
\]
For \(r=2s\) the defect is \((h-s)^2\); for \(r=2s+1\) it is \((h-s)(h-s-1)\). All factors in (1) have nonnegative integer coefficients.

**2. Even-rank insertion and the limiting series.** Fix \(r=2s\). Every height chain consists of a possibly empty prefix of entries strictly above \(s\), a (possibly empty) middle run of \(s\), and a suffix strictly below \(s\). Delete the middle run. The remaining *noncentral pattern* is specified uniquely by its two monotone lists of lengths \(u,v\), of total length \(L=u+v\). Its defect is at least \(L\).

If a central entry is present, the product of Gaussian factors in (1) does not depend on the number of repeated central entries: adding an adjacent entry equal to \(s\) introduces only a Gaussian factor with lower index zero. Thus for \(L\le a-1\), precisely one length-\(a\) chain represents each noncentral pattern and its polynomial contribution is a fixed quantity \(E(P,Q;t)\). For \(L=a\), the unique chain has no central entry; denote its contribution by \(N(P,Q;t)\).

The standard bounded Durfee-square identity, applied separately to the upper and lower lists, gives the exact **formal** identity
\[
\sum_{\text{all finite noncentral patterns }(P,Q)}E(P,Q;t)
=\begin{bmatrix}2s\\s\end{bmatrix}_t
\left(\prod_{j=1}^{s}(1-t^j)^{-1}\right)^2
=\Xi_{2s}(t).
\tag{2}
\]
Equivalently, for either side one uses \(\sum_{s\ge u_1\ge\cdots\ge u_m\ge1}t^{\sum u_i^2}D_s(u) =\prod_{j=1}^s(1-t^j)^{-1}\), where \(D_s(u)\) is the Gaussian chain product. Here \(D_s(u)=(t;t)_s/((t;t)_{s-u_1}\prod_i(t;t)_{u_i-u_{i+1}})\) for \(u_{m+1}=0\), with the empty list assigned \(D_s(\varnothing)=1\), and \((t;t)_j=\prod_{e=1}^{j}(1-t^e)\). This identity, including its interpretation as the homocyclic limiting factor, is established in the prior literature cited below and is **not** claimed as new.

Inserting one central entry into a no-central chain splits the unique jump across level \(s\). If the jump has positive upper and lower lengths \(\rho,\sigma\), the Gaussian product changes by exactly
\[
\frac{E(P,Q;t)}{N(P,Q;t)}
=\begin{bmatrix}\rho+\sigma\\\rho\end{bmatrix}_t.
\tag{3}
\]
The jump may occur at an endpoint, but both lengths remain positive because a central value is missing. Formula (3) follows directly from the factorial form of the Gaussian product: the denominator factor \((t;t)_{\rho+\sigma}\) is replaced by \((t;t)_\rho(t;t)_\sigma\). Hence \(E-N\) has nonnegative coefficients and zero constant term. We therefore have a coefficientwise-nonnegative decomposition
\[
\Xi_{2s}-F_{2s,a}
=\sum_{L=a}(E-N)+\sum_{L\ge a+1}E,
\tag{4}
\]
where the first sum is over patterns of length exactly \(a\) and the second over patterns of lengths at least \(a+1\). The first sum begins at degree \(a+1\), and the second at degree \(a+1\). This proves equality through codegree \(a\) and coefficientwise positivity of the difference.

To obtain the sharp coefficient, only patterns of minimal possible defect matter. At length \(a\), defect \(a\) forces every noncentral entry to be either \(s+1\) or \(s-1\); monotonicity admits exactly \(a+1\) such patterns. For each, the split jump in (3) has at least one side of length one, so its Gaussian polynomial has linear coefficient exactly one. Their contribution to \([t^{a+1}](\Xi-F)\) is \(a+1\). At length \(a+1\), defect \(a+1\) again requires all deviations to be one, and there are exactly \(a+2\) patterns, each with constant Gaussian coefficient one. All other patterns have larger defect. Thus the first nonzero difference coefficient is \((a+1)+(a+2)=2a+3\), as asserted.

**3. Odd-rank affine law.** Now let \(r=2s+1\), so \(\delta_r(h)=(h-s)(h-s-1)\). Its zeros are precisely \(h=s,s+1\). Every other height has defect at least two. In a term contributing to codegree \(k\), the number of noncentral entries is at most \(\lfloor k/2\rfloor\). They form an initial prefix with heights \(\ge s+2\) and a terminal suffix with heights \(\le s-1\). For a fixed pair of such prefix/suffix lists, the central run has length \(L=a-u-v\ge2\) once \(a\ge k+2\). Its entries are an initial run of \(s+1\), followed by \(s\).

There are two boundary choices (all \(s+1\), or all \(s\)), and \(L-1\) interior switch choices. In (1), each boundary choice has a Gaussian product independent of \(L\); all interior switch choices have the **same** Gaussian product, also independent of \(L\), because repeated equal heights contribute factors one. Therefore, for each fixed prefix/suffix pattern, the codegree-\(k\) contribution is a constant plus \((L-1)\) times another constant, i.e. an affine function of \(a\). Only finitely many prefix/suffix patterns can have defect at most \(k\). Summing establishes the claimed affine behavior for all \(a\ge k+2\).

Finally, in odd rank the zero-defect height chains are precisely the \(a+1\) possible switch positions, each contributing constant coefficient one. Noncentral heights have defect at least two. In the linear coefficient, each of those \(a+1\) central chains contributes one from its terminal Gaussian polynomial, and each of the \(a-1\) interior-switch chains contributes one more from its single \(s+1\)-to-\(s\) Gaussian factor. Therefore \([t]F_{2s+1,a}=2a\). In even rank, the all-central chain supplies one linear term and the two single-unit endpoint deviations supply one each, giving \([t]F_{2s,a}=3\). This completes the proof.

## Verification

The standalone `verify.py` implements (i) the full Delsarte sum by enumerating all nonincreasing height chains and (ii) a separate transfer-state calculation directly from (1). Their *entire integer polynomials* agree for ranks \(2\) through \(8\) and exponents \(1\) through \(7\), in 49 exact tests. For even ranks \(2,4,6,8\) and exponents \(1\) through \(7\), it independently expands the published Gaussian-product series and verifies both equality through degree \(a\) and the first difference coefficient \(2a+3\), in 28 more exact tests. It tests the odd affine law and both first-coefficient formulas. Running `python3 verify.py` prints `VERIFY_OK` on success. The proof above, not these finite tests, establishes the universal quantifiers.

## Relationship to prior work

Delsarte's subgroup-type formula (1948) is the starting enumeration. Aivazidis, *Subgroup bounds for abelian p-groups with applications* (arXiv:2606.03320v1, publicly posted June 2, 2026), proves the exact leading coefficient and the product bound \(\Xi_{2s}\), together with the analytic limit of the normalized homocyclic subgroup count as the exponent grows. In particular, \(\Xi_{2s}\), the central-height method, the insertion identity, and the limiting evaluation are established background, not new claims. The present result asks a different **finite-exponent, coefficientwise** question and obtains a sharp first unequal coefficient, an all-codegree congruence with an effective cutoff, and an odd-rank eventual affine law.

Chew, Chin and Lim (2020) give an explicit rank-four subgroup formula; such special-rank formulas may recover individual cases, but do not state the all-rank sharp cutoff and affine rule. Their abstract was accessible, but a full-text overlap inspection was not possible; this is a residual historical-priority risk. Delsarte's exact formula by itself also makes the results derivable, but the stated coefficient rigidity requires the separate defect-and-insertion analysis.

## Limitations

No independent mathematical audit or historical-priority certification has been performed. Aivazidis's analytic limiting constants are not newly established here, and no result is asserted for general nonhomocyclic abelian groups. The affine coefficients in odd rank are not given in a single closed form for arbitrary codegree; the result establishes their exact eventual degree and an explicit sufficient cutoff. All series are formal at \(t=0\); no uniform numerical asymptotic in simultaneous growing rank and exponent is claimed.

## References

1. S. Aivazidis, *Subgroup bounds for abelian p-groups with applications*, arXiv:2606.03320v1, first posted 2026-06-02, especially Sections 2–4 and 9, https://arxiv.org/abs/2606.03320 .
2. S. Delsarte, *Fonctions de Möbius sur les groupes abéliens finis*, Ann. of Math. (2) 49 (1948); subgroup-type formula as quoted and used in reference 1.
3. C. Y. Chew, A. Y. M. Chin, and C. S. Lim, *The number of subgroups of finite abelian p-groups of rank 4 and higher*, Communications in Algebra 48 (2020), 1538–1547, https://doi.org/10.1080/00927872.2019.1691571 .
