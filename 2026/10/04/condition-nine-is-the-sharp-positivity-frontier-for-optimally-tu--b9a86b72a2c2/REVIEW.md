# Same-model review

## Correctness
PASS. The first two heavy-ball iterates give the exact matrix identity
\[
x^{(2)}=\alpha[(2+\beta)I-\alpha A]b.
\]
For Stieltjes matrices the off-diagonal signs are automatically favorable, reducing universal second-iterate positivity to diagonal inequalities. Substituting the classical optimal quadratic parameters yields \(\kappa\le9\) exactly. For diagonal systems, the modal error has the exact Chebyshev-\(U\) representation
\[
e_k=q^k[U_k(c)-qU_{k-1}(c)].
\]
When \(q\le1/2\), the standard bound \(|U_k|\le k+1\) proves \(e_k\le1\) for all \(k\), while the \(L\)-mode gives \(e_2=q^2(3+2q)>1\) for \(q>1/2\). The packaged exact-rational checker returns `VERIFY_OK`.

## Originality
PASS with residual literature risk. Heavy-ball construction, optimal quadratic tuning, convergence rates, and qualitative non-monotone transients are prior work and are explicitly excluded. Searches under heavy-ball, Polyak momentum, Stieltjes, positive orthant, diagonal modes, second-iterate positivity, and condition-number-nine aliases did not locate an implication-equivalent result. The inspected full texts analyze convergence, stability, and peak effects rather than the coordinatewise positivity classification proved here. Older monotone-iteration literature remains a residual risk.

## Value
PASS. Heavy-ball is a canonical acceleration method, and Stieltjes systems have nonnegative exact solutions in many discretization and network settings. The result gives a complete sharp early-iterate safety test for arbitrary fixed parameters, identifies the exact loss of that safety under the standard accelerated tuning, and strengthens the conclusion to all iterations on diagonal systems. The threshold \(9\), minimal two-dimensional witness, and exact \(\kappa=16\) counterexample provide concrete diagnostics for positivity-sensitive uses of momentum.

Same-model review: passed. Independent audit: not yet performed.
