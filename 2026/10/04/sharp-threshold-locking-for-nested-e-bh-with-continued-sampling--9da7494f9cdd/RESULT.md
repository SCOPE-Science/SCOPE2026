# Sharp threshold locking for nested e-BH with continued sampling


## Finding

For base e-BH with \(K\) hypotheses at level \(\alpha\), suppose the current rejection set is a nonempty set \(R\) with \(|R|=r\). Its current cutoff is
\[
c_r=\frac{{K}}{{\alpha r}}.
\]
If a later nonnegative evidence vector \(E'\) satisfies \(E'_i\ge c_r\) for every \(i\in R\), then every member of \(R\) is still rejected by e-BH. No restriction is needed on coordinates outside \(R\).

The cutoff is sharp as a coordinatewise persistence floor. For every \(b<c_r\), one can start from \(r\) coordinates equal to \(c_r\) and all others equal to zero, then lower just one old rejected coordinate to \(b\) while keeping the other \(r-1\) old rejected coordinates at \(c_r\) and all outsiders at zero. The next e-BH rejection set is empty.

This yields a data-collection rule that is strictly less restrictive than freezing every rejected stream. At time \(t\), let \(R_t\) be the current nonempty e-BH rejection set, let \(r_t=|R_t|\), and put
\[
c_t=\frac{{K}}{{\alpha r_t}}.
\]
For a rejected stream \(i\in R_t\), continue sampling through a nonnegative one-step e-factor \(X_{{i,t+1}}\) satisfying
\[
\mathbb E[X_{{i,t+1}}\mid\mathcal F_t]\le1
\]
under \(H_i\), and update by
\[
E_{{i,t+1}}=c_t+(E_{{i,t}}-c_t)X_{{i,t+1}}.
\]
Then \(E_{{i,t+1}}\ge c_t\) pathwise, its conditional null expectation is at most \(E_{{i,t}}\), and the e-BH rejection sets remain nested. Thus rejected hypotheses may still be sampled, but only the evidence above the current e-BH cutoff is put at risk.

Among affine lock-and-bet rules whose factor may equal zero and that must guarantee persistence for every configuration of the other coordinates, the lock \(c_t\) is minimal. Hence \(E_{{i,t}}-c_t\) is the largest uniformly safe amount of active capital. When later discoveries increase \(r_t\), the cutoff \(c_t\) decreases, so previously locked capital can be released.

## Assumptions and scope

The deterministic persistence statement concerns the base e-BH rule applied to arbitrary nonnegative vectors. No probabilistic dependence assumptions are needed for that statement.

The sequential corollary assumes a common filtration \((\mathcal F_t)\) and conditionally valid one-step e-factors for every null stream to which the update is applied. Before rejection, any ordinary update used for a stream must likewise preserve its e-process property. Under these global-filtration conditions, the lock-and-bet continuation remains a nonnegative supermartingale under each true null. This is the same type of filtration requirement needed when e-processes are used inside repeatedly monitored e-BH.

The claim is about pathwise non-revocation and coordinatewise worst-case safe capital. It does not optimize power, sampling cost, or FDR under weaker local-filtration assumptions.

## Proof

Write the ordered next e-values as \(E'_[1]\ge\cdots\ge E'_[K]\), and let
\[
k'=\max\left\{{k: E'_[k]\ge\frac{{K}}{{\alpha k}}}\right\},
\]
with \(k'=0\) if the set is empty. Because the \(r\) old rejected coordinates all satisfy \(E'_i\ge c_r\), the \(r\)-th largest next e-value obeys
\[
E'_[r]\ge c_r=\frac{{K}}{{\alpha r}}.
\]
Therefore \(k'\ge r\). The new e-BH cutoff is \(K/(\alpha k')\), which is at most \(c_r\). Hence every old rejected coordinate satisfies
\[
E'_i\ge c_r\ge\frac{{K}}{{\alpha k'}},
\]
so every old rejection remains rejected.

For sharpness, fix any \(b<c_r\). Let the current vector have value \(c_r\) on a chosen \(r\)-element set and zero elsewhere. The condition at rank \(r\) holds with equality, while every rank above \(r\) is zero, so e-BH rejects exactly those \(r\) coordinates. In the next vector, set one of those coordinates to \(b\), keep the other \(r-1\) at \(c_r\), and keep every outsider at zero. Rank \(r\) now fails because \(b<c_r\). Every rank \(k<r\) also fails because
\[
c_r=\frac{{K}}{{\alpha r}}<\frac{{K}}{{\alpha k}}.
\]
Ranks larger than \(r\) have value zero. Thus no rank qualifies and the next rejection set is empty.

For the sequential rule, an old rejected coordinate satisfies \(E_{{i,t}}\ge c_t\), so the coefficient \(E_{{i,t}}-c_t\) is nonnegative and the update is always at least \(c_t\). Under \(H_i\),
\[
\mathbb E[E_{{i,t+1}}\mid\mathcal F_t]
=c_t+(E_{{i,t}}-c_t)\mathbb E[X_{{i,t+1}}\mid\mathcal F_t]
\le E_{{i,t}}.
\]
The deterministic persistence result then gives \(R_t\subseteq R_{{t+1}}\). Because the rejection count cannot decrease, the future cutoff cannot increase.

Finally, consider an affine continuation that locks a level \(L\) and risks the remainder through a factor that is allowed to be zero. An outcome with factor zero leaves exactly \(L\). If \(L<c_t\), the sharpness construction shows a configuration of the other coordinates for which the old rejection is lost. Therefore every uniformly safe such rule needs \(L\ge c_t\); choosing \(L=c_t\) maximizes active capital.

## Verification

The accompanying `verify_lock_and_bet.py` independently evaluates the e-BH rule on a grid of values of \(K\), \(\alpha\), and \(r\), verifies the persistence implication under randomized outsider coordinates, checks the sharp one-coordinate counterexample for every tested rank, and verifies the affine conditional-expectation identity for discrete factor distributions. It prints `VERIFY_OK` when all checks pass.

These computations are supplementary. The theorem is proved by the order-statistic and conditional-expectation arguments above, not by finite enumeration.

## Relationship to prior work

Wang and Ramdas introduced base e-BH and its rank cutoff \(K/(\alpha k)\). Lin, Ma, Ren, and Wei study adaptive data collection with e-processes and e-BH. Their recent e-PS construction obtains nested rejection sets under a sufficient sampling condition that collects new evidence only from hypotheses not already rejected. The result here identifies a weaker prospective condition: rejected streams may continue to be sampled provided their current e-BH cutoff is locked and only excess evidence is exposed to the next factor. The sharpness statement also identifies the maximal uniformly safe excess capital.

Tavyrikov, Goeman, and de Heide study revocation under ongoing e-processes from another direction: they use running suprema and adjusters to obtain carefree multiple-testing guarantees. That changes the evidence fed to e-BH. The present construction instead keeps ordinary current e-values and modifies the continuation dynamics after rejection. Wang, Dandapanthula, and Ramdas emphasize that repeated e-BH requires compatibility with a common/global filtration; the sequential corollary here adopts that requirement explicitly.

The inspected sources did not state the cutoff-locking persistence lemma, its one-coordinate sharpness construction, or the resulting maximal-active-capital continuation rule. A terminologically different equivalent construction in unindexed material remains possible.

## Limitations

The result is criterion-specific. It guarantees pathwise nesting against arbitrary behavior of other coordinates, which is stronger than many stochastic notions of persistence and therefore may lock more capital than necessary in a model-specific design. It does not claim that continued sampling of already rejected streams is sample-optimal, nor that the rule is optimal under objectives such as expected discovery time or power.

The anytime-valid FDR interpretation needs globally valid e-processes with respect to the common filtration. Local e-process validity alone is not sufficient in general. The theorem does not repair violations of that filtration condition.

## References

- Z. Lin, W. Ma, Z. Ren, and Y. Wei, *Sample-Efficient Multiple Testing with Adaptive Data Collection*, arXiv:2609.26651v1, 2026.
- R. Wang and A. Ramdas, *False Discovery Rate Control with E-values*, Journal of the Royal Statistical Society: Series B 84(3), 822–852, 2022. DOI: 10.1111/rssb.12489.
- Y. Tavyrikov, J. J. Goeman, and R. de Heide, *Carefree multiple testing with e-processes*, Electronic Journal of Statistics 20(2), 3178–3189, 2026. DOI: 10.1214/26-EJS2546.
- H. Wang, S. Dandapanthula, and A. Ramdas, *Anytime-valid FDR control with the stopped e-BH procedure*, Statistics & Probability Letters 226, 110512, 2025. DOI: 10.1016/j.spl.2025.110512.
