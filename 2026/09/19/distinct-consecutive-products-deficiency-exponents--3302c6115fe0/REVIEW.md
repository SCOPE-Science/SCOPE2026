# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The new counting step is exact. In the split-product notation \(r=ph\), \(s=qh\), \((p,q)=1\), \(r>s\), the worst component-degree parameter \(p=2\) forces \(q=1\), hence \(r=2s\). The \(X^{1/2}\) integral-point estimate therefore occurs for only \(O(L)\) pairs. Summing this locus gives \(O(X^{1/2}(L^4\log X+L^5))\). All other pairs have \(p\ge3\), so their total is \(O(X^{1/3}(L^5\log X+L^6))\). With \(L=X^{\theta+o(1)}\) and \(\theta<1/6\), the first term dominates, giving \(X^{1/2+5\theta+o(1)}\).

Substitution of that exponent into the source witness-forest formulas gives the raw-root path exponent
\[
E_{\rm raw}(t)=\left(\frac12+5\theta\right)\rho^t+\frac{4\theta(1-\rho^t)}{1-\rho}+\theta\rho^t+\theta,
\qquad \rho=(2-\theta)^{-1}.
\]
For \(0<\theta\le1/20\), its \(\rho^t\)-coefficient is positive, so the maximum is \(E_{\rm raw}(0)=1/2+7\theta\). The long-root exponent from the source remains maximized at its first unequal step and is smaller in the same range. The exact limiting arithmetic at \(\theta=1/24\) was independently recomputed in the published verification script.

Runbo Li's Theorem 1.1 in *Primes in almost all short intervals III* explicitly states the \(1/24+\delta\) short-prime exponent and an exceptional set of size \(O(X(\log X)^{-B})\) for sufficiently large fixed \(B\). This is enough to choose \(\theta\downarrow1/24\), derive the \(17/24+\varepsilon\) and \(19/24+\varepsilon\) exponents, and quantify the long-gap contribution by arbitrary negative powers of \(\log X\).

The conclusion depends on the correctness of the structural construction, split-product proposition, and forest lemmas in arXiv:2609.17543v1. The relevant statements and proofs were inspected. No independent external validation of that preprint's full headline theorem is asserted here.

## Originality

**PASS, to the best of our knowledge.**

The inspected current version of Chojecki's preprint states \(O(X^{4/5+o(1)})\) for short raw rejected gaps and \(O(X^{9/10+o(1)})\) for the total length of short rejected gaps. Its proof applies the \(p=2\) consequence of the component-degree estimate uniformly to all \((r,s)\) before summation. It does not separate the sparse locus \(r=2s\), state the transfer exponents \(1/2+5\eta\) and \(1/2+7\eta\), or use Li's later \(1/24\) result.

Searches using the exact fractions \(17/24\) and \(19/24\), quantitative deficiency terminology, split-product degree-two terminology, and equivalent consecutive-product formulations did not identify the same refinement.

A material residual risk is Ryan Kielhorn's September 2026 Zenodo preprint *Distinct consecutive products in a density-one set via prime-gap deletions* (DOI 10.5281/zenodo.21287064). Its indexed abstract and metadata describe another prime-gap deletion proof and a formalization of the density-one conclusion. The available description does not advertise the \(17/24\), \(19/24\), or sparse degree-two refinement, but the full preprint text was not inspected. This is therefore recorded as unresolved originality risk rather than treated as evidence of non-coverage.

## Value

**PASS.**

The refinement identifies a structural overcount in the quantitative bottleneck of a recent density-one construction. It improves the source's short rejected-length exponent from \(9/10\) to \(19/24+\varepsilon\), improves the raw short-gap exponent to \(17/24+\varepsilon\), and isolates a reusable transfer rule from short-prime exponents to deficiency exponents. The logarithmic exceptional-set strength also yields a super-logarithmic rate of density convergence for the full set.

The result does not change the qualitative resolution of the Erdős--Graham question and does not prove optimal deficiency. Its value is in sharpening and explaining the quantitative structure of the construction.

## Limitations

No lower bound matching \(19/24\) is proved. The power-saving estimate concerns the short rejected portion; the full deficiency remains governed by the exceptional set for long prime gaps and is bounded by arbitrary negative powers of \(\log X\). The related Kielhorn Zenodo preprint remains the principal uninspected source capable of affecting originality.
