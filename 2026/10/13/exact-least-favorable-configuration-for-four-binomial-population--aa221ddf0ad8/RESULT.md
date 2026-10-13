# Exact least-favorable configuration for four binomial populations with two trials

## Finding

Consider four independent Bernoulli populations, each sampled twice. The two populations with the largest observed success counts are selected, with ties broken uniformly at random. For any fixed \(0<\delta<1\), suppose the ordered success probabilities satisfy \(0\le\theta_{[1]}\le\theta_{[2]}<\theta_{[3]}\le\theta_{[4]}\le1\) and \(\theta_{[3]}-\theta_{[2]}\ge\delta\). If \(\operatorname{PCS}(\theta)\) denotes the probability of selecting exactly the two populations with larger parameters, then

\[
\min_{\theta:\,\theta_{[3]}-\theta_{[2]}\ge\delta}\operatorname{PCS}(\theta)
=\frac{(1+\delta)^4(\delta^3-4\delta^2-7\delta+16)}{96}.
\]

The **only minimizing ordered parameter vector** is
\[
\left(\frac{1-\delta}{2},\frac{1-\delta}{2},
\frac{1+\delta}{2},\frac{1+\delta}{2}\right).
\]
For labeled populations the sole freedom is to permute labels within or across the two distinguished groups; the unordered parameter multiset is unique. Thus the first balanced four-population, two-trial case of the even-sample centering conjecture has a sharp solution for the entire gap range, not merely at a specified numerical gap.

## Assumptions and scope

Exactly four independent binomial counts are observed, each distributed as \(\operatorname{Bin}(2,\theta_i)\). Ties are independently resolved by continuous uniform auxiliary ranks, equivalent to choosing uniformly among the tied admissible selections. The desired selection is the pair corresponding to the strictly larger two underlying success probabilities. The gap is in the open interval \(\delta\in(0,1)\); no limits in sample size or in the number of populations are asserted.

## Proof

**Step 1: full-space reduction.** Write the ordered parameters \(\theta_{[1]}\le\theta_{[2]}\le\theta_{[3]}\le\theta_{[4]}\), put \(p=\theta_{[3]}-\delta\in[0,1-\delta]\), and let \(q=p+\delta\). Proposition 2.1 of Wu--Chen [1], proved by monotone Bernoulli coupling, states that the correct-selection probability is at least the one for the two-level vector \((p,p,q,q)\). Its strict equality clause states that when \(p\in(0,1-\delta)\), equality holds exactly for this two-level vector. Denote the two-level success probability by \(P_\delta(p)\). It suffices to minimize this scalar polynomial, then invoke the strict equality clause.

**Step 2: exact tie-weighted polynomial.** Set \(p_c=(1-\delta)/2\) and \(h=p-p_c\). The allowed scalar domain is \(|h|\le(1-\delta)/2\). Let \(g_1,g_2\in\{0,1,2\}\) be the observed high-population counts, and \(l_1,l_2\in\{0,1,2\}\) the low-population counts. The mass for a count \(j\) at success parameter \(x\) is \(b_j(x)=\binom2j x^j(1-x)^{2-j}\). If \(a(g_1,g_2,l_1,l_2)\) is the fraction of the \(24\) equally likely strict auxiliary rank orders for which both highs are selected, then

\[
P_\delta(p)=\sum_{g_1,g_2,l_1,l_2=0}^2
 a(g_1,g_2,l_1,l_2)b_{g_1}(q)b_{g_2}(q)b_{l_1}(p)b_{l_2}(p).
\]

Expanding this explicitly finite sum in the indeterminates \(\delta\) and \(h\) gives the following **exact identity**:

\[
\begin{aligned}
P_\delta(p_c+h)-P_\delta(p_c)
=\frac{\delta h^2}{24}\big[&29+64\delta+38\delta^2-3\delta^4\\
&-(84-12\delta^2)h^2-16h^4\big],
\end{aligned}
\]

with

\[
P_\delta(p_c)=\frac{(1+\delta)^4(\delta^3-4\delta^2-7\delta+16)}{96}.
\]

Both identities can be reproduced from independent enumeration of the \(3^4=81\) count vectors and \(4!=24\) auxiliary orders, using exact rational arithmetic in the accompanying `check_exact.py`. Its polynomial coefficient comparison—not its finite numerical spot checks—verifies all possible values of the formal variables.

**Step 3: global strict inequality.** Put \(z=h^2\) and \(z_{\max}=(1-\delta)^2/4\). The square bracket is \(F_\delta(z)=29+64\delta+38\delta^2-3\delta^4-(84-12\delta^2)z-16z^2\). For \(\delta\in(0,1)\), \(84-12\delta^2>0\), so \(F_\delta(z)\) is strictly decreasing on \(0\le z\le z_{\max}\). Substitution at the largest allowed \(z\) gives

\[
F_\delta(z_{\max})=7+110\delta+14\delta^2-2\delta^3-\delta^4
\ge7+110\delta+11\delta^2>0,
\]

where the inequality uses \(\delta^3\le\delta^2\) and \(\delta^4\le\delta^2\). Because \(\delta>0\), the exact difference identity implies \(P_\delta(p)>P_\delta(p_c)\) at every admissible \(p\ne p_c\). Thus the unique scalar minimizer is \(p_c\), an interior point. Wu--Chen's strict coupling clause now yields the claimed unique full-space minimizer and the displayed sharp value. \(\square\)

## Verification

The standalone `check_exact.py` requires only Python 3 standard library and uses `fractions.Fraction`; invoke `python3 check_exact.py` in a directory containing that file. It explicitly constructs both binomial laws, enumerates all \(81\) score quadruples and \(24\) strict rank orders, and compares every coefficient of the resulting bivariate polynomial against the closed expression. The package checker completed successfully. The strict analytic bound in Step 3 and the cited full-space coupling, rather than finite numerical tests, provide the universal assertions.

## Relationship to prior work

Wu and Chen [1] formulated the general binomial top-\(t\) selection model and proved their full-space slippage reduction (Proposition 2.1), reflection identity (Proposition 2.2), asymptotic eventual uniqueness in the balanced case (Theorem 2.3), and exact centering for the two-population problem (Corollary 2.4). Section 6 conjectures exact unique centering for **every even sample size** in **every balanced problem**, but does not prove the four-population two-trial case for all gap values. Their Table 2 supplies numerical evidence at one gap. The present theorem gives a complete finite-sample, all-gap proof, together with the sharp probability and full-space equality characterization. The source's known reduction is used rather than rediscovered.

## Limitations

Only the first nontrivial balanced case (four populations, two samples per population, selection of two) is proved. The general even-sample balanced conjecture, including four populations with more than two trials or larger balanced groups, remains outside scope. The formal polynomial certificate uses exact enumeration but is not an independent human review. Priority is limited by possible differently indexed equivalent results in earlier ranking-and-selection literature. No independent scientific audit is claimed.

## References

[1] Y. Wu and P. Chen, *Least-Favorable Location for Binomial Top-t Selection*, arXiv:2609.03466v1 (first publicly posted 3 September 2026), Proposition 2.1, Theorem 2.3, Table 2, Section 6, Appendix A. https://arxiv.org/pdf/2609.03466
