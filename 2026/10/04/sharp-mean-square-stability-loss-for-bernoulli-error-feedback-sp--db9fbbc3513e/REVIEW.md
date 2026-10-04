# Review

## Correctness

PASS. Conditioning on a successful or failed Bernoulli transmission gives two exact \(2\times2\) state matrices. Their branch-averaged action on \((\mathbb E[x^2],\mathbb E[xe],\mathbb E[e^2])\) is the displayed cubic moment operator. The complete Jury test has exactly one binding factor,
\[
ps[2p-(2-p)s],
\]
because the other two nontrivial expressions are strictly positive for every \(s\ge0\), \(0<p\le1\). An independent renewal calculation gives the same boundary from the geometric waiting time between successful transmissions. The no-memory comparison follows from one-step branch averaging.

Risk: mean-square stability is proved for the stated iid Bernoulli compressor; no claim is made for correlated sparsification.

## Originality

PASS. The defining memory paper contains the exact random-coordinate ultra-sparsification mechanism and the same residual update, but its theorem uses scheduled steps and averaging and does not give a constant-step scalar phase diagram. The general error-feedback paper proves broad convergence but does not state this Bernoulli second-moment law. A quadratic ECQ-SGD paper uses a different stochastic quantizer and extra compensation parameters. A random-block sparsification paper motivates a detached alternative because ordinary error feedback can perform poorly, but does not derive this threshold. A recent tight error-feedback analysis assumes deterministic contractive compression in its main exact results and therefore does not imply the iid Bernoulli frontier.

Focused published-record searches over random sparsification, error feedback, scalar quadratics, geometric delays, mean-square stability, and the derived threshold found no covering statement.

## Value

PASS. Random coordinate omission is one of the canonical communication-saving mechanisms for which memory was introduced. The exact scalar calculation exposes a concrete mechanism hidden by broad convergence-rate analyses: residual accumulation converts transmission sparsity into a geometrically distributed bundled stepsize. The resulting threshold quantifies how aggressive compression forces constant steps to shrink, and the no-memory comparison isolates the cost of accumulation itself. This is a natural stability boundary for a standard algorithmic primitive, not an arbitrary parameter slice.

Same-model review: passed. Independent audit: not yet performed.
