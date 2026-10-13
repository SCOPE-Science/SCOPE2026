# Self-review

## Correctness

PASS. The algebraic constraint is
\[
e(p\,x-c)=m>0.
\]
Positive initial effort forces
\[
x(0)>\frac{c}{p}.
\]
A continuous finite trajectory cannot cross
\[
x=\frac{c}{p}
\]
because the algebraic equation would become
\[
0=m.
\]
Therefore a finite classical trajectory on the positive-effort branch keeps
\[
x>\frac{c}{p}
\]
and
\[
e>0.
\]
Exact arithmetic reproduces the source-parameter barrier and the initial-consistency residuals.

## Originality

PASS. Feasibility regions and singularity-induced bifurcations in bioeconomic DAEs are established prior methodology. The surviving source-specific contribution is the exact noncrossing consequence of the Meng-Meng algebraic closure and its direct conflict with Figure 6. Searches by DOI, title, harvesting-effort aliases, singularity wording, and correction terminology found no published source-specific repair.

## Value

PASS. Figure 6 is used to argue that a low prey initial value can drive prey extinction while harvest effort fluctuates strongly. The printed DAE forbids that finite continuous trajectory from the positive-effort branch before the singular manifold is reached. This changes the interpretation of the numerical example and provides a concrete reproducibility condition rather than a cosmetic algebra correction.

## Closest literature and limitations

Meng and Wu study singularity-induced bifurcation in a different delayed predator-prey DAE, and Li, Chen, and Ye study another bioeconomic DAE with nonlinear prey harvesting. Those works establish the broader method but do not state the source-specific Figure 6 barrier.

No simulation code is available. The initial-triple residual calculation assumes the Figure 6 values are ordered as
\[
(x,y,e),
\]
but the hard branch barrier does not depend on that interpretation.

Self-review: passed. Independent audit: not yet performed.
