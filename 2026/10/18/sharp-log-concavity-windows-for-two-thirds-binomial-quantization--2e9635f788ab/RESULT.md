# Sharp log-concavity windows for two-thirds binomial quantization

## Finding

Let \(X\sim\operatorname{Bin}(n,p)\), with an integer \(n\ge1\) and \(0<p<1\), and let
\[
Y=\left\lfloor\frac{2X}{3}\right\rfloor.
\]
The probability mass function of \(Y\) is (ordinary) log-concave **if and only if** its parameters fall into one of the following cases:

| Trial count | Exact success-probability region |
| --- | --- |
| \(n=1,2\) | Every \(0<p<1\). |
| \(n=3\) | \(1/7\le p<1\). |
| \(n=4\) | \((9-\sqrt{33})/18\le p\le(9+\sqrt{33})/18\). |
| \(n=5\) | \((13-\sqrt{41})/32\le p\le(13+\sqrt{41})/32\). |
| \(n\ge6\) | No \(0<p<1\). |

In particular, six is the sharp trial-count cutoff at which ordinary log-concavity fails **for every nondegenerate Bernoulli success probability**, despite the original binomial law being ultra-log-concave.

## Assumptions and scope

For a finite mass function \((b_j)\) with interval support, ordinary log-concavity means \(b_j^2\ge b_{j-1}b_{j+1}\) at every interior index. Endpoints satisfy no interior inequality. Throughout, \(n\) is a positive integer and \(p\) is strictly between zero and one. This leaves out the two deterministic endpoint laws, which are trivially log-concave. All occupied values of \(Y\) have positive mass and form an interval, because the integer map \(k\mapsto\lfloor2k/3\rfloor\) hits every integer up to \(\lfloor2n/3\rfloor\).

## Proof

**1. Unnormalized probabilities and the first obstruction.** Set \(t=p/(1-p)>0\). Multiplying every probability by the same positive factor \((1-p)^{-n}\) preserves log-concavity. Let
\[
 b_j(t)=\sum_{\substack{0\le k\le n\\\lfloor2k/3\rfloor=j}}\binom nk t^k.
\]
Use the convention \(\binom nk=0\) when \(k>n\). For \(n\ge3\), the first three masses are
\[
 b_0=1+nt,\qquad b_1=\binom n2t^2,\qquad b_2=\binom n3t^3+\binom n4t^4.
\]
Consequently the first log-concavity gap is
\[
 b_1^2-b_0b_2=t^3F_n(t),\qquad
 F_n(t)=\binom n2^2t-(1+nt)\left(\binom n3+\binom n4t\right).
\tag{1}
\]
The right-hand side has the same sign as the necessary condition at index one.

**2. Trial counts at most five.** For \(n\le2\), the support contains at most two points and there is no interior inequality. Direct substitution in (1) gives
\[
\begin{aligned}
F_3(t)&=6t-1,\\
F_4(t)&=-4t^2+19t-4,\\
F_5(t)&=-5(5t^2-9t+2).
\end{aligned}
\tag{2}
\]
For \(n=3,4\), the mass function has exactly three occupied indices and (1) is the only inequality. For \(n=5\), its four unnormalized masses are
\[
(1+5t,\ 10t^2,\ 10t^3+5t^4,\ t^5).
\]
Its additional gap at index two is identically positive:
\[
(10t^3+5t^4)^2-10t^7=5t^6(5t^2+18t+20)>0.
\tag{3}
\]
Thus in all three cases (2) is both necessary and sufficient. The positive-odds solutions are \(t\ge1/6\) for \(n=3\); \((19-3\sqrt{33})/8\le t\le(19+3\sqrt{33})/8\) for \(n=4\); and \((9-\sqrt{41})/10\le t\le(9+\sqrt{41})/10\) for \(n=5\). Substituting \(p=t/(1+t)\) gives exactly the three regions stated above. The boundary equalities are included.

**3. Six trials.** Substitution into (1) yields
\[
F_6(t)=-10(3t-1)(3t-2).
\tag{4}
\]
The index-one inequality therefore requires \(1/3\le t\le2/3\). But the last three of the five masses
\[
(1+6t,\ 15t^2,\ 20t^3+15t^4,\ 6t^5,\ t^6)
\]
have the index-three gap
\[
(6t^5)^2-(20t^3+15t^4)t^6=t^9(21t-20).
\tag{5}
\]
It requires \(t\ge20/21\), incompatible with \(t\le2/3\). Hence no positive odds yield log-concavity at six trials.

**4. All larger trial counts.** For \(n\ge7\), \(F_n(t)\) in (1) is a quadratic polynomial in \(t\), with negative leading coefficient \(-n\binom n4\) and negative constant coefficient \(-\binom n3\). Its discriminant equals
\[
\Delta_n=-\frac{n^2(n-1)^2}{192}
 (5n^4-42n^3+73n^2-36n-12).
\tag{6}
\]
Write \(m=n-7\ge0\). The final parenthesis becomes
\[
5m^4+98m^3+661m^2+1672m+912>0.
\tag{7}
\]
Thus \(\Delta_n<0\). Together with the negative leading coefficient, this forces \(F_n(t)<0\) for **every real** \(t\). The first log-concavity inequality already fails for all \(n\ge7\), completing the classification. \(\square\)

## Verification

The attached standalone `VERIFY.py` script reconstructs the coefficient map directly, symbolically verifies all identities (1)–(7) needed for the argument, checks the independent gaps (3) and (5), and runs 1,200 exact rational comparisons across thirty trial counts. Execute with Python 3 and SymPy:

```bash
python VERIFY.py
```

Expected output:

```text
SYMBOLIC_IDENTITIES_PASS
EXACT_RATIONAL_GRID_PASS trial_counts=30 odds_grid=40 tests=1200
```

The proof is the four-case analytical argument above, **not** the finite grid. The symbolic computations are reproducibility checks of explicit identities, not an independent infinite-proof certification.

## Relationship to prior work

Tang and Tang [1,2] specifically study rationally scaled Poisson-binomial variables and the quantization \(\lfloor2X/3\rfloor\). Their result that some such laws fail strong-Rayleigh real-rootedness and the Newton (ultra-log-concavity) inequalities does not establish the failure of **ordinary** log-concavity; lack of real-rootedness is weaker information for this purpose. Their published treatment focuses on zeros, Hurwitz stability and transport approximation. The sharp classification of ordinary log-concavity, the two exact algebraic probability windows, and the uniform six-trial obstruction are separate statements.

Known results on \(\lfloor X/k\rfloor\) for integer \(k\) address equal-sized consecutive blocks. Here the block sizes alternate as two, one, two, one, and so on, and those preservation theorems do not imply the displayed classification. Likewise, a nearest-integer rounding of \(2X/3\) has a different allocation of atoms from its floor and does not settle this law. The result is about the homogeneous binomial subclass; no theorem for arbitrary heterogeneous Poisson-binomial parameters is asserted.

## Limitations

The characterization assumes strictly positive interior success probability, ordinary log-concavity rather than ultra-log-concavity, and the precise floor quantizer shown. It does not classify real-rootedness, Hurwitz stability, stronger total-positivity properties, other rational slopes, or heterogeneous independent Bernoulli sums. Published and open literature were compared, but the possibility of an unlocated equivalent formulation or unindexed treatment remains a residual originality risk.

## References

[1] Wenpin Tang and Fengmin Tang, *The Poisson binomial distribution -- Old & New*, arXiv:1908.10024v1, first publicly posted August 27, 2019, Section 4 and Appendix A. https://arxiv.org/pdf/1908.10024

[2] Wenpin Tang and Fengmin Tang, *The Poisson Binomial Distribution—Old & New*, *Statistical Science* **38** (2023), 108–119, DOI: 10.1214/22-STS852, Section 4. https://doi.org/10.1214/22-STS852
