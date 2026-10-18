# Scientific review

**Correctness — PASS.** The primitive-root count \(\varphi(p-1)\) and exact \(p^2\)-lift count yield \(r_p=p^2-1-p\varphi(p-1)\). The Möbius squarefree sieve and Chinese remainder theorem prove an explicit absolute error \(O(Q(y)^2\sqrt N)\) uniformly; the prime number theorem gives the relative asymptotic up to the stated cutoff. The Euler product is strictly positive because the deviations from one are bounded by a convergent \(\sum_p O(p^{-2})\). Independent modular enumeration and finite-product checks pass. There is no unproved analytic hypothesis.

**Originality — PASS, with stated risk.** Johnston–Naik Section 4 counts residues avoiding primitive-root tests without a squarefree restriction, and Fan–Pollack's sampling law likewise averages over unrestricted bases; neither supplies the local squarefree factor \(p\varphi(p-1)/(p^2-1)\), the growing-cutoff squarefree count, or the nontrivial limiting bias \(K\). Their bounds for *individual squarefree bases* are different statements and do not imply this conditional sampling law. Targeted result-record searches and available prior claim comparisons did not reveal covering work. A general squarefree-sieve theorem could imply this result without mentioning the exact application, so completeness of prior coverage remains a residual risk.

**Mathematical value — PASS.** Squarefree integers are a singled-out arithmetic class in the least-Artin-prime literature. The result identifies a concrete, enduring selection bias for the natural least-prime cutoff rather than just a fixed-prime probability. Its explicit cutoff range turns the local phenomenon into a nontrivial global limit, and the product constant is quantitatively reproducible.

**Closest literature and limits.** Johnston–Naik (arXiv:2610.08569v1, Theorem 1.3 and Section 4); Fan–Pollack (arXiv:2505.05601v1, Introduction and Section 4). The result does not improve the full worst-case Artin-prime bound, prove individual infinitude, or claim the cutoff coefficient \(1/4\) is optimal.

Self-review: passed. Independent audit: not yet performed.
