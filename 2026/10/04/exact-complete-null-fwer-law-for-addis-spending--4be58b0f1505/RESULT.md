# Exact complete-null FWER law for ADDIS-Spending

## Finding
Consider the ADDIS-Spending rule of Tian and Ramdas with a fixed target level \(\alpha\in(0,1)\), fixed thresholds \(0<\lambda<\tau\le 1\), \(q=\tau-\lambda\), and a nonnegative sequence \((\gamma_j)_{j\ge1}\) satisfying \(\sum_{j\ge1}\gamma_j=1\). Under the complete null, suppose \(P_1,P_2,\ldots\) are independent \(\mathrm{Uniform}(0,1)\), and use
\[
\alpha_i=\alpha q\,\gamma_{t(i)},\qquad
t(i)=1+\sum_{k<i}\left(\mathbf 1\{P_k\le\tau\}-\mathbf 1\{P_k\le\lambda\}\right).
\]
Assume \(\alpha q\gamma_j\le\lambda\) for every \(j\), so every rejection region lies inside the candidate region. Then the familywise error rate over the infinite stream is exactly
\[
\operatorname{FWER}
=1-\prod_{j=1}^\infty \frac1{1+\alpha\gamma_j}.
\]
In particular, the exact complete-null FWER is independent of \(\lambda\) and \(\tau\) once the above containment condition holds.

Among all nonnegative spending sequences with total mass one,
\[
\frac{\alpha}{1+\alpha}
\le \operatorname{FWER}
<1-e^{-\alpha},
\]
where the lower endpoint is attained exactly by concentrating all spending on one index, while \(1-e^{-\alpha}\) is the unattained supremum approached by increasingly diffuse spending. Hence ADDIS-Spending is strictly conservative under independent exact-uniform complete nulls.

For the normalized inverse-square schedule \(\gamma_j=6/(\pi^2j^2)\), used in published ADDIS comparisons, Euler's product for \(\sinh\) gives the closed form
\[
\operatorname{FWER}
=1-\frac{\sqrt{6\alpha}}{\sinh(\sqrt{6\alpha})}.
\]
At \(\alpha=0.2\), this equals \(0.17515476014878684\), leaving an exact gap of \(0.02484523985121316\) below the nominal level.

## Assumptions and scope
The statement concerns the original ADDIS-Spending construction under the complete null with independent exact-uniform p-values. The thresholds \(\lambda\) and \(\tau\) are fixed, and the containment requirement \(\alpha(\tau-\lambda)\gamma_j\le\lambda\) is essential to the two-event state reduction used below. The result does not assert the same formula for conservative-but-nonuniform nulls, dependent p-values, ADDIS-Graph, exhaustive ADDIS, or streams containing false nulls.

The primary source defines ADDIS-Spending by the same state index \(t(i)\) and level \(\alpha_i=\alpha(\tau-\lambda)\gamma_{t(i)}\), and proves PFER/FWER control under independent uniformly conservative nulls. The later exhaustive-ADDIS paper explicitly observes that ordinary ADDIS procedures are conservative and constructs a uniform improvement, which motivates quantifying the unused complete-null error budget exactly.

## Proof
Fix a state \(j\). While \(t(i)=j\), the test level is the constant
\[
a_j=\alpha q\gamma_j.
\]
Because \(a_j\le\lambda\), a fresh uniform p-value has four disjoint effects:
\[
\begin{array}{ll}
P_i\le a_j &: \text{reject and stop},\\
a_j<P_i\le\lambda &: \text{no rejection and remain in state }j,\\
\lambda<P_i\le\tau &: \text{advance to state }j+1,\\
P_i>\tau &: \text{no rejection and remain in state }j.
\end{array}
\]
The only events that end the current state are rejection, with probability \(a_j\), and advancement, with probability \(q\). Since \(q>0\), one of those two events occurs almost surely after finitely many draws. Conditioning on the first draw that lies in their union,
\[
\Pr(\text{reject in state }j\mid\text{state }j\text{ reached})
=\frac{a_j}{a_j+q}
=\frac{\alpha\gamma_j}{1+\alpha\gamma_j},
\]
and
\[
\Pr(\text{advance past state }j\mid\text{state }j\text{ reached})
=\frac{q}{a_j+q}
=\frac1{1+\alpha\gamma_j}.
\]
Therefore the probability of surviving the first \(m\) states without any rejection is
\[
\prod_{j=1}^m\frac1{1+\alpha\gamma_j}.
\]
These events decrease to the event of no false rejection anywhere in the infinite stream, so continuity from above yields
\[
\Pr(\text{no rejection ever})
=\prod_{j=1}^\infty\frac1{1+\alpha\gamma_j},
\]
which proves the exact FWER formula. The product converges to a strictly positive number because
\[
\sum_j\log(1+\alpha\gamma_j)\le\alpha\sum_j\gamma_j=\alpha.
\]

For the sharp envelope, expanding the positive product gives
\[
\prod_j(1+\alpha\gamma_j)\ge 1+\alpha\sum_j\gamma_j=1+\alpha,
\]
with equality exactly when at most one \(\gamma_j\) is positive. This yields
\[
\operatorname{FWER}\ge\frac{\alpha}{1+\alpha}.
\]
On the other hand, \(\log(1+x)<x\) for every \(x>0\), so
\[
\sum_j\log(1+\alpha\gamma_j)<\alpha,
\]
and hence \(\operatorname{FWER}<1-e^{-\alpha}\). For the uniform-on-\(N\) schedule \(\gamma_j=1/N\) for \(1\le j\le N\),
\[
\operatorname{FWER}_N=1-(1+\alpha/N)^{-N}\longrightarrow 1-e^{-\alpha},
\]
showing that the upper bound is the exact supremum.

Finally, for \(\gamma_j=6/(\pi^2j^2)\), Euler's identity
\[
\frac{\sinh x}x=\prod_{j=1}^\infty\left(1+\frac{x^2}{\pi^2j^2}\right)
\]
with \(x=\sqrt{6\alpha}\) gives the displayed closed form.

## Verification
The accompanying checker evaluates the finite-state recursion, verifies convergence of the inverse-square product to the \(\sinh\) expression, checks the sharp envelope on deterministic test schedules, and reproduces the stated numerical value at \(\alpha=0.2\). These computations support the algebra but are not substitutes for the infinite-product proof above.

## Relationship to prior work
Tian and Ramdas introduce ADDIS-Spending, give the state-index formula used here, and prove FWER/PFER control for independent uniformly conservative null p-values. Their analysis focuses on validity and power, not an exact complete-null FWER evaluation for a general spending sequence.

Fischer's later exhaustive-ADDIS paper is especially relevant: it states that the original ADDIS principle is conservative because it is based on a Bonferroni inequality, explains why a direct Sidak factorization is unavailable for history-dependent ADDIS rejection events, and derives a uniformly stronger exhaustive procedure that can exactly exhaust the target level under the global null. The present finding is complementary rather than competing: it evaluates the original ADDIS-Spending error probability exactly and shows how its conservatism depends only on \((\gamma_j)\) in the exact-uniform complete-null regime.

A targeted search for exact ADDIS-Spending complete-null formulas, product representations, and the \(\sinh\) specialization did not locate a source stating this result. The closest inspected literature gives qualitative conservatism and uniform improvements, but not the displayed gamma-dependent equality or its sharp envelope.

## Limitations
The formula is not claimed outside the exact-uniform independent complete-null model. If some rejection threshold exceeds \(\lambda\), the rejection and advancement regions overlap and the state calculation changes. The result also does not compare power under alternatives; it quantifies type-I-error expenditure only. A residual literature risk remains that an equivalent exact product identity appears in supplementary material or unpublished notes not found in the inspected sources.

## References
1. J. Tian and A. Ramdas, "Online control of the familywise error rate," arXiv:1910.04900, first public 2019-10-10; later published in *Statistical Methods in Medical Research* 30(4), 2021, DOI:10.1177/0962280220983381.
2. L. Fischer, "An exhaustive ADDIS principle for online FWER control," *Biometrical Journal*, DOI:10.1002/bimj.202300237.
3. Euler's classical product identity for \(\sinh\), used only to simplify the normalized inverse-square spending schedule.
