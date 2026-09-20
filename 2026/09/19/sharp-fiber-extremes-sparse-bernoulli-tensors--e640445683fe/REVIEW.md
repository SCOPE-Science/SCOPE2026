# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The result was checked at the fiber reduction, binomial large-deviation, discrete-extreme, second-order, and sublogarithmic steps.

For a fiber containing \(D\) ones, the centered squared norm is exactly
\[
D(1-p)^2+(n-D)p^2=(1-2p)D+np^2.
\]
Fixing all other tensor arguments at coordinate vectors proves that the injective norm dominates every fiber norm. In any fixed mode the \(n^{k-1}\) fibers partition the tensor entries and therefore have independent \(\operatorname{Bin}(n,p)\) degrees. The full collection has only a fixed factor \(k\) more fibers, so one-mode lower bounds and all-mode union upper bounds have the same logarithmic exponent.

At \(d\sim c\log n\), a one-mass Stirling lower bound and Chernoff upper bound both give
\[
\log\Pr\{D\ge xd\}=-d h(x)+o(d)
\]
for fixed \(x>1\). This yields both the threshold equation \(c h(x)=k-1\) and, above threshold, the exact polynomial exponent \(k-1-c h(x)\).

The second-order calculation was checked separately. Since \(m=O(\log n)\) and \(p=c\log n/n\), the binomial mass is relatively asymptotic to the Poisson mass. Summing upper-tail mass ratios gives the prefactor
\[
\frac{\sqrt{x}}{(x-1)\sqrt{2\pi d}}.
\]
Taylor expansion at the critical solution then forces the correction
\[
-\frac{\log\log n}{2\log x_*}.
\]
The one-mode lattice CDF follows from independence. For the all-mode maximum, the same center is tight by combining that one-mode lower bound with a \(k\)-mode union upper bound; no unjustified cross-mode independence is used.

The sublogarithmic statement uses only exponential-rate separation at \((1\pm\varepsilon)x_n\). Since \(h(x)\sim x\log x\), the two rates straddle \((k-1)\log n\) by fixed proportional factors, which is enough for convergence of the maximum after normalization.

The deterministic verification artifact independently evaluates exact binomial tails. For \(k=3,c=2\), where \(x_*=e\), its one-mode CDF values approach the predicted lattice profile; it also reproduces the \(r=2\) barrier \(x_r=3.591121476668\ldots\).

## Originality

**PASS, to the best of our knowledge, with a deliberately narrow claim.**

Zhou and Zhu (arXiv:2609.20520v1) was inspected at its main theorem, optimality discussion, and maximum-fiber-degree lemma. It proves the log-free \(O(\sqrt d)\) upper bound for \(d\ge c\log n\), notes that the injective norm dominates every fiber norm, uses a fixed-fiber lower bound to show scale optimality, and states only qualitative divergence of the maximum fiber norm when \(1\le d=o(\log n)\). Its Lemma 4.3 uses the same Chernoff rate \(h(\kappa)\) to choose a sufficient bounded-degree constant with slack. It does not state the sharp critical equation \(c h(x)=k-1\), the second-order fiber localization, the exact polynomial failure exponent, or the resulting necessary lower bound on \(C_{k,r,c}\).

The scalar discrete-extreme mechanism is classical and is not claimed as new. Anderson, Coles and Hüsler (1997) explicitly study maxima of Poisson-like triangular arrays; Bollobás (1982) studies degree extremes in random graphs in the logarithmic regime; fixed-mean Poisson maxima have still older literature. These sources make it plausible that the scalar maximum-degree asymptotics, including refined lattice behavior, are covered in more general language. No novelty claim is made for that scalar theory or for the \(k=2\) row/column-degree specialization.

The claim is instead restricted to the tensor-specific consequences for the new independent-entry sparse-tensor concentration theorem: the explicit \(k,c\) fiber lower constant, the second-order localization of the tensor's maximum fiber, the exact polynomial-tail obstruction, the necessary
\[
C\ge\sqrt{h^{-1}((k-1+r)/c)}
\]
dependence for \(n^{-r}\) spectral-norm tails, and the quantitative sublogarithmic refinement.

Searches by the source title and identifier, maximum fiber degree, fiber norm, logarithmic sparsity, the rate \(x\log x-x+1\), and equivalent spectral-norm formulations did not locate these tensor-specific statements. Repository overlap searches also found no matching SCOPE record.

The complete 1997 Anderson--Coles--Hüsler article was not directly inspected; its abstract and bibliographic record were inspected. That is the most concrete residual originality risk for the scalar triangular-array extreme formulas. It does not by itself establish prior coverage of the tensor-norm application, so originality is reported only “to the best of our knowledge.”

## Value

**PASS.** The source theorem establishes the optimal \(\sqrt d\) order but leaves its constants opaque. The present result identifies an unavoidable constant inflation at the exact logarithmic sparsity boundary and quantifies how the required constant grows with tensor order \(k\), tail exponent \(r\), and sparsity coefficient \(c\). The second-order \(\log\log n\) correction also identifies the actual fiber-extreme location rather than only its order. Below logarithmic sparsity, the Lambert-\(W\) formula turns the qualitative divergence into an explicit rate.

These statements are directly useful when interpreting or attempting to sharpen constants in sparse tensor spectral-norm concentration, and they separate a compulsory degree-extreme contribution from the genuinely multilinear part of the tensor norm.

## Limitations

- Homogeneous independent Bernoulli entries only.
- The exact second-order center is stated for \(d=c\log n\); smaller perturbations of \(d\) can affect the \(O(\log\log n)\) term.
- The exact lattice limit is for one fixed mode. Across all modes, overlapping fibers prevent the same independence argument, so only \(O_{\mathbb P}(1)\) localization is claimed.
- The result gives a lower obstruction, not the full limiting law or exact leading constant of the tensor injective norm.
- Classical discrete-extreme theory may subsume the scalar maximum calculation; no priority claim is made for that component.
- The full Anderson--Coles--Hüsler (1997) text was not directly inspected.
