# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Disposition: **PASSED**.

## Final claim

For maximal-distance Kaczmarz on \(m\) row-normalized equations with row coherence \(\mu\), the exact universal one-step normalized-residual amplification factor is \(\Gamma_m(\mu)=\sqrt{(m-1)(1+\mu)^2/m}\) for \(\mu\le1/(m-1)\) and \(\sqrt{1+(m-1)\mu^2}\) otherwise. Hence universal stepwise residual monotonicity holds exactly for \(\mu\le\sqrt{m/(m-1)}-1\); explicit nonsingular systems attain the bound, and a matching \(	heta\)-approximate-selection frontier holds.

## Correctness — PASS

After scaling the selected normalized residual to one, write the remaining residual coordinates as \(s\) and the selected-row correlations as \(c\). One Kaczmarz projection changes the normalized residual ratio to \(\|s-c\|^2/(1+\|s\|^2)\). Coherence gives \(\|s-c\|\le \|s\|+\mu\sqrt d\) with \(d=m-1\), so optimizing \((y+\mu\sqrt d)^2/(1+y^2)\) over \(0\le y\le\sqrt d\) yields exactly the two branches \(d(1+\mu)^2/(d+1)\) for \(\mu\le1/d\) and \(1+d\mu^2\) otherwise. The explicit row family \(a_1=e_1,\ a_j=-\mu e_1+\sqrt{1-\mu^2}e_j\) attains the bounds (as a limit at the tie boundary). Solving \(\Gamma_m(\mu)\le1\) gives the exact monotonicity threshold \(\sqrt{m/(m-1)}-1\). The same constrained optimization with selector tolerance \(	heta\) gives the approximate-selection formula. Independent numerical optimization over several \(m,\mu\) values reproduced the formula to numerical precision.

## Originality — PASS

The maximal-weighted-residual Kaczmarz literature inspected analyzes convergence rates of the iterates and greedy/oblique variants, including sensitivity to correlated rows, but does not state the exact one-step norm amplification factor as a function only of row coherence, the sharp residual-monotonicity threshold, or the matching approximate-selector frontier. Searches of Gauss–Southwell residual/gradient-norm literature and the published-record corpus did not locate an implication covering these formulas.

## Scientific value — PASS

Residual spikes are a concrete stability issue for greedy row-action methods, and coherence is a standard, readily interpretable geometric parameter. An exact sharp frontier, attained by explicit nonsingular systems and extended to approximate selection, gives a useful boundary theorem rather than an implementation anecdote or a small numerical example.

## Residual risks and limits

- Older relaxation/coordinate-relaxation literature could contain an equivalent stepwise norm inequality under different terminology; no decisive equivalent was found.
- Exact-arithmetic one-step analysis only.
- The norm is the scale-invariant normalized residual, equal to the Euclidean residual for unit-row systems.
- Pairwise coherence can be pessimistic for a fixed matrix; no finite-precision or noisy/inconsistent convergence theorem is claimed.

This is a mathematical review, not formal proof-assistant verification or external certification.
