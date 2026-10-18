# A unique dispersion crossover in the two-count Poisson range

## Finding
For \(\lambda>0\), let \(X\) and \(Y\) be independent \(\operatorname{Poisson}(\lambda)\) counts. Their sample range is \(R=\max(X,Y)-\min(X,Y)=|X-Y|\). Put
\[
 t=2\lambda,\qquad r(t)=e^{-t}\bigl(I_0(t)+I_1(t)\bigr),\qquad H(t)=r(t)+t\,r(t)^2,
\]
where \(I_k\) is the modified Bessel function of the first kind. **There is a unique positive solution** \(t_*\) of \(H(t_*)=1\), and the exact dispersion classification is
\[
 \begin{aligned}
 \operatorname{Var}(R)&<\mathbb ER&&\text{if }0<\lambda<\lambda_*,\\
 \operatorname{Var}(R)&=\mathbb ER&&\text{if }\lambda=\lambda_*,\\
 \operatorname{Var}(R)&>\mathbb ER&&\text{if }\lambda>\lambda_*,
 \end{aligned}
 \qquad\lambda_*=t_*/2.
\]
The defining equation has the certified rational bracket \(3.4778<t_*<3.4780\), hence \(1.7389<\lambda_*<1.7390\); numerically \(\lambda_*\approx1.7389329672696905\). Thus a natural difference of two Poisson counts crosses from underdispersion to overdispersion exactly once, even though each individual Poisson order statistic is underdispersed [1].

## Assumptions and scope
The two observations are independent, identically distributed, and have a common finite positive intensity. The dispersion comparison is variance versus the **range's own mean**, not variance versus the parent intensity. There are no assertions for unequal rates, for the range of three or more observations, or for alternative count families. The main statement is valid for every real \(\lambda>0\), rather than only the bracket endpoints.

## Proof
**Exact moments.** Write \(D=X-Y\). The symmetric Skellam distribution has \(\Pr(D=k)=e^{-t}I_{|k|}(t)\) for every integer \(k\); therefore \(\mathbb ED^2=\operatorname{Var}(X-Y)=t\). The standard recurrence
\[
 kI_k(t)=\frac t2\bigl(I_{k-1}(t)-I_{k+1}(t)\bigr)\qquad(k\ge1)
\]
allows the absolutely convergent series for \(\mathbb E|D|\) to telescope:
\[
 \mathbb ER=2e^{-t}\sum_{k\ge1}kI_k(t)=t e^{-t}\bigl(I_0(t)+I_1(t)\bigr)=tr(t).
\]
Consequently, using \(R^2=D^2\),
\[
 \operatorname{Var}(R)-\mathbb ER=t-(tr)^2-tr=t\bigl[1-H(t)\bigr].\tag{1}
\]
All of these expectations are finite by the Poisson exponential moments.

**Strict Bessel comparison.** For fixed \(t>0\), set \(u=I_1(t)/I_0(t)\). The integral representation of the positive-order modified Bessel functions gives \(0<u<1\) (strict positivity is immediate from the positive power series; \(I_0>I_1\) follows from integrating \(e^{t\cos\theta}(1-\cos\theta)\) over \(0\le\theta\le\pi\)). The classical strict Turán inequality [2]
\[
 I_k(t)^2>I_{k-1}(t)I_{k+1}(t),\qquad k=1,2,\ldots,
\]
shows the successive ratios \(I_{k+1}(t)/I_k(t)\) decrease strictly with \(k\), so \(I_k(t)<I_0(t)u^k\) for \(k\ge2\), and \(I_1=I_0u\). Hence, by the modified-Bessel generating function,
\[
 e^t=I_0(t)+2\sum_{k\ge1}I_k(t)
 <I_0(t)\frac{1+u}{1-u}.
\]
Rearranging gives the crucial strict inequality
\[
 \boxed{r(t)>1-u(t)}\qquad(t>0).\tag{2}
\]

**All crossings point in one direction.** Differentiate with \(I_0'=I_1\), \(I_1'=I_0-I_1/t\):
\[
 r'(t)=-\frac{e^{-t}I_1(t)}{t}=-\frac{r(t)u(t)}{t(1+u(t))}.
\]
At any positive \(t\) such that \(H(t)=1\), the positivity of \(r\) implies \(r<1\) and \(t=(1-r)/r^2\). Substituting these identities into \(H'=r'+r^2+2trr'\) yields
\[
 H'(t)\big|_{H(t)=1}=\frac{r^2(1-r-u)}{(1-r)(1+u)}<0,\tag{3}
\]
with strict negativity from (2). Thus **every** zero of \(H-1\) is a strict downward crossing.

As \(t\downarrow0\), the power series give \(r(t)=1-t/2+O(t^2)\) and \(H(t)=1+t/2+O(t^2)>1\). As \(t\to\infty\), standard fixed-order modified-Bessel asymptotics give
\[
 r(t)\sim\sqrt{\frac{2}{\pi t}},\qquad H(t)\longrightarrow\frac2\pi<1.
\]
Continuity supplies at least one positive zero. Equation (3) forces any zero to cross from positive to negative; two or more such zeros would require an intervening zero with nonnegative derivative, a contradiction. Therefore the zero is unique and the signs in (1) yield the claimed classification. This is an all-parameter analytical proof; finite tests are not used to infer uniqueness.

## Verification
Run the standalone standard-library checker from the same directory as this document:

```sh
python3 check_dispersion.py
```

The checker bounds \(e^t\), \(I_0(t)\), and \(I_1(t)\) at the **rational** arguments \(t=17389/5000\) and \(t=1739/500\) using positive-term partial sums and a geometric upper bound on the omitted tail. The resulting disjoint enclosures prove \(H(17389/5000)>1\) and \(H(1739/500)<1\). It additionally computes the first absolute moment via an independently truncated double-Poisson sum and verifies agreement with the Bessel series for four finite positive intensities. These latter numerical comparisons are non-exhaustive corroboration, not a substitute for the Bessel inequality and crossing proof. The source file itself supplies every finite computational dependency.

## Relationship to prior work
Badiella, del Castillo, and Puig [1] establish ultra-log-concavity of discrete **individual order-statistic** laws and, consequently, underdispersion of Poisson minima and maxima. The range is the **difference** of two dependent order statistics, and neither ultra-log-concavity nor underdispersion is preserved by that operation as this finding shows. Lu and collaborators [3] use folded Skellam distributions for read-count differences, without classifying their own-mean dispersion transition. Classical Turán inequalities for modified Bessel functions [2] are used as a known lemma; the strict inequality (2) and the all-crossing argument identify the missing global sign structure for this probabilistic question.

## Limitations
The proof assumes a common positive Poisson rate and exactly two observations. The certified rational enclosure applies to this one model, not general folded Skellam mixtures or unequal-rate differences. Classical Bessel Turán inequalities and fixed-order asymptotics are cited, not reproved. No independent audit or absolute priority claim is implied; an unindexed earlier folded-Skellam moment analysis could in principle contain the same classification. One relevant 2023 paper was inspectable through indexed theorem/corollary excerpts but its deposited PDF could not be opened for sequential full-text inspection.

## References
[1] L. Badiella, J. del Castillo, P. Puig, *Ultra log-concavity of discrete order statistics*, *Statistics & Probability Letters* **201** (2023), article 109900. First available online 2023-06-26. DOI: https://doi.org/10.1016/j.spl.2023.109900.

[2] Á. Baricz and S. Ponnusamy, *On Turán type inequalities for modified Bessel functions*, preprint arXiv:1010.3346 (2010), subsequently *Proceedings of the American Mathematical Society*. https://arxiv.org/abs/1010.3346.

[3] R. Lu, R. M. Smith, M. Seweryn et al., *Analyzing allele specific RNA expression using mixture models*, *BMC Genomics* **16** (2015), article 566. DOI: https://doi.org/10.1186/s12864-015-1749-0.

[4] H. Aravinda, A. Marsiglietti, J. Melbourne, *Concentration Inequalities for Ultra Log-Concave Distributions*, arXiv:2104.05054v1 (2021-04-11). https://arxiv.org/abs/2104.05054.
