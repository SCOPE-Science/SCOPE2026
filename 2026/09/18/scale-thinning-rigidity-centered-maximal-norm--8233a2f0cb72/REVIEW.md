# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The lower bound is reduced to two finite constructions and all limiting steps are monotone or approximation steps with explicit error control.

First, the finite product martingale is explicit. For \(q=1-1/B\) and terminal value \(F=q^{-T/p}\), where \(T\) is the first-zero time capped at \(n\), direct conditioning gives
\[
F_k=q^{-k/p}\left((1-q)\sum_{s=0}^{n-k-1}q^{s/p'}+q^{(n-k)/p'}\right)
\]
on the event that the first \(k\) digits are nonzero. Also
\(\mathbb EF^p=n(1-q)+1\). Summing the martingale maximum only over first-zero times at least \(L\) steps from the terminal level gives the displayed lower bound in RESULT.md. Sending \(n\to\infty\), then \(L\to\infty\), then \(B\to\infty\) produces the sharp constant \(p'\).

Second, the spatial realization uses only a prescribed finite chain of radii. The inequalities
\[
\rho_j/\rho_{j-1}\le\delta^2/B^2
\]
guarantee that each interval
\[
\left[1+\log_B\frac{S}{\delta\rho_{j-1}},\ \log_B\frac{\delta S}{\rho_j}\right]
\]
has length at least one, so suitable integer digit positions exist. The upper digit-position bound makes the selected averaging interval avoid past-digit jumps outside a set of relative measure at most \(2\delta\) per level. The lower bound makes each future-digit period at most \(\delta\) times the selected radius. The periodic-average error is therefore at most \(2\|F\|_\infty\delta\). Uniform distribution of the selected base-\(B\) digits over one spatial period gives exactly the original product probability measure.

Potential failure modes were checked explicitly: an unbounded-above radius set supplies the required separated chain by choosing radii successively upward and reversing their order; an infimum-zero set supplies it directly downward. The grid for the finest past digit contains all coarser past-digit jump points. The suffix pattern has the stated common period and has conditional mean exactly \(F_k\). Cutoff boundary losses vanish after repetition over many periods. Smooth approximation is stable because
\(|M_{\mathcal R}f-M_{\mathcal R}h|\le M_c(f-h)\) and the unrestricted operator has norm \(p'\).

The upper bound is exactly Madrid's 2026 theorem for the unrestricted centered maximal operator.

## Originality

**PASS, to the best of our knowledge.**

Madrid's arXiv abstract was checked and establishes the exact unrestricted norm \(p'\). A detailed public review of that paper reports an additional dyadic-radii theorem. Because the full source text of arXiv:2609.12440 was not directly retrievable in this review, that reported dyadic statement is treated conservatively as prior art and is excluded from the originality claim.

Wei--Nie--Wu--Yan (2016) were inspected in accessible HTML. Their Theorem 1.1 proves equality of the full and upper-truncated centered maximal norms for the continuous radius interval \(0<r<\gamma\). Thus continuous truncation is also prior art.

Searches for exact and synonymous formulations combining “restricted radii”, “set of radii”, “lacunary”, “superlacunary”, “centered Hardy--Littlewood maximal”, “exact norm”, “arbitrary prescribed radii”, and “p/(p-1)” did not locate a theorem saying that every radius set with \(\inf\mathcal R=0\) or \(\sup\mathcal R=\infty\) has the full sharp norm. Searches around arXiv:2609.12440 likewise located the dyadic special case but not the arbitrary irregular-radius statement. Current SCOPE records were searched by the source identifier, Hardy--Littlewood terminology, restricted-radii terminology, and equivalent scale-thinning language; no overlapping record was found.

The originality claim is therefore limited to the arbitrary-scale rigidity theorem and its finite-subfamily/smooth-near-extremizer strengthening. The martingale principle, base-digit encoding, the unrestricted sharp norm, continuous truncation, and the dyadic special case are not claimed as original.

The principal residual risk is the recency of arXiv:2609.12440 and the lack of direct full-text inspection: the source may contain a more general radius-set statement not reflected in its abstract or the detailed public review. No other inaccessible paper was found whose title or abstract specifically suggests this exact arbitrary-radius theorem.

## Value

**PASS.**

The result identifies a sharp rigidity phenomenon that is not visible from the unrestricted norm alone. Scale sparsification can be arbitrarily severe: geometric spacing, regularity, or any lower density of radii is unnecessary. Even a superlacunary or irregular set retains the full constant whenever its logarithmic scale range is unbounded. The finite-subfamily strengthening shows that the obstruction is already witnessed by finitely many prescribed scales for each requested accuracy, rather than by an essentially infinite supremum.

This cleanly separates the centered interval-average problem from many lacunary maximal settings where thinning the scale set improves boundedness. It also gives a reusable prescribed-scale realization lemma for finite martingales.

## Scope and limitations

No claim is made for radius sets confined to a compact annulus, for the weak \((1,1)\) constant, or for higher-dimensional exact norms. The result does not claim that unbounded logarithmic diameter is necessary for norm \(p'\); it is a sharp sufficient structural condition established here. The dyadic-radii conclusion is explicitly treated as prior coverage.

No independent validation is asserted.
