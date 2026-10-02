# Independent audit — 2026-10-01

**Record:** SCOPE-20260921-332a15a5d36f — Sharp coherence frontier for residual spikes in maximal-distance Kaczmarz

**Disposition:** passed

## Final claim

For maximal-distance Kaczmarz on \(m\) row-normalized equations with row coherence \(\mu\), the exact universal one-step normalized-residual amplification factor is \(\Gamma_m(\mu)=\sqrt{(m-1)(1+\mu)^2/m}\) for \(\mu\le1/(m-1)\) and \(\sqrt{1+(m-1)\mu^2}\) otherwise. Hence universal stepwise residual monotonicity holds exactly for \(\mu\le\sqrt{m/(m-1)}-1\); explicit nonsingular systems attain the bound, and a matching \(	heta\)-approximate-selection frontier holds.

## C — correctness

**PASS**. After scaling the selected normalized residual to one, write the remaining residual coordinates as \(s\) and the selected-row correlations as \(c\). One Kaczmarz projection changes the normalized residual ratio to \(\|s-c\|^2/(1+\|s\|^2)\). Coherence gives \(\|s-c\|\le \|s\|+\mu\sqrt d\) with \(d=m-1\), so optimizing \((y+\mu\sqrt d)^2/(1+y^2)\) over \(0\le y\le\sqrt d\) yields exactly the two branches \(d(1+\mu)^2/(d+1)\) for \(\mu\le1/d\) and \(1+d\mu^2\) otherwise. The explicit row family \(a_1=e_1,\ a_j=-\mu e_1+\sqrt{1-\mu^2}e_j\) attains the bounds (as a limit at the tie boundary). Solving \(\Gamma_m(\mu)\le1\) gives the exact monotonicity threshold \(\sqrt{m/(m-1)}-1\). The same constrained optimization with selector tolerance \(	heta\) gives the approximate-selection formula. Independent numerical optimization over several \(m,\mu\) values reproduced the formula to numerical precision.

## O — originality

**PASS**. The maximal-weighted-residual Kaczmarz literature inspected analyzes convergence rates of the iterates and greedy/oblique variants, including sensitivity to correlated rows, but does not state the exact one-step norm amplification factor as a function only of row coherence, the sharp residual-monotonicity threshold, or the matching approximate-selector frontier. Searches of Gauss–Southwell residual/gradient-norm literature and the published-record corpus did not locate an implication covering these formulas.

### Source inspections

- **A New Theoretical Estimate for the Convergence Rate of the Maximal Weighted Residual Kaczmarz Algorithm** (DOI:10.4208/nmtma.OA-2018-0039): **HIGHLY_RELEVANT_NOT_DECISIVE**. The stated contribution is a computable convergence-rate estimate and numerical comparison, not an exact coherence residual-spike frontier.
- **Greedy Randomized and Maximal Weighted Residual Kaczmarz Methods with Oblique Projection** (arXiv:2106.13606 / DOI:10.3934/era.2022062): **NOT_COVERING_DIFFERENT_UPDATE**. The paper changes the projection direction to an oblique step and studies convergence improvement; it does not state the audited standard-step coherence threshold.

## V — scientific value

**PASS**. Residual spikes are a concrete stability issue for greedy row-action methods, and coherence is a standard, readily interpretable geometric parameter. An exact sharp frontier, attained by explicit nonsingular systems and extended to approximate selection, gives a useful boundary theorem rather than an implementation anecdote or a small numerical example.

## Sources and residual risks

- K. Du, H. Gao, A New Theoretical Estimate for the Convergence Rate of the Maximal Weighted Residual Kaczmarz Algorithm, Numer. Math. Theory Methods Appl. 12 (2019), DOI:10.4208/nmtma.OA-2018-0039.
- F. Wang, W. Li, W. Bao, L. Liu, Greedy Randomized and Maximal Weighted Residual Kaczmarz Methods with Oblique Projection, Electron. Res. Arch. 30 (2022), arXiv:2106.13606, DOI:10.3934/era.2022062.
- J. Nutini et al., Convergence Rates for Greedy Kaczmarz Algorithms, UAI 2016.
- Classical Gauss–Southwell coordinate-descent and Motzkin/maximal-residual row-selection literature.
- Published-record semantic search for Kaczmarz coherence residual amplification and residual-spike thresholds.
- Risk/limit: Older relaxation/coordinate-relaxation literature could contain an equivalent stepwise norm inequality under different terminology; no decisive equivalent was found.
- Risk/limit: Exact-arithmetic one-step analysis only.
- Risk/limit: The norm is the scale-invariant normalized residual, equal to the Euclidean residual for unit-row systems.
- Risk/limit: Pairwise coherence can be pessimistic for a fixed matrix; no finite-precision or noisy/inconsistent convergence theorem is claimed.

