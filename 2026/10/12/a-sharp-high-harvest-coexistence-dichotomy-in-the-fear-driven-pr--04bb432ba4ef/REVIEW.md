# Self-review

## Correctness

PASS. The proof uses the exact positive-equilibrium equations of the harvested model. For \(r>m\), the predator nullcline defines a unique positive \(v=V_q(u)\), uniformly tends to zero on a fixed prey interval, and forces a prey-residual sign change between \(K/2\) and \(K\). This gives a positive high-\(q\) branch, its limit \(u_q\to K\), and the asymptotic law
\[
qv_q^{r-m}\to eK^p.
\]
The exact Jacobian signs then give negative trace and positive determinant for sufficiently large \(q\). For \(r=m\), the predator equilibrium equation gives both the necessary cutoff and a continuous sign-change proof of sufficiency.

## Originality

PASS. Nonlinear harvesting and equilibrium bifurcation theory are established prior art. The accepted result is restricted to the motivating model's exponent balance: the stable high-\(q\) branch and its power law for \(r>m\), together with the exact finite coexistence threshold at \(r=m\). The motivating source gives numerical high-harvest behavior and leaves a full analysis for future work. Source-specific, exponent-alias, correction, broader-harvesting, and published-finding searches did not locate the same theorem.

## Value

PASS. The source explicitly asks how harvesting changes finite-time extinction, conjectures harvesting-induced recovery, and discusses whether predators survive under very high effort. The result supplies a sharp structural answer at the equilibrium level: the exponent relation \(r-m\) determines whether stable coexistence persists to arbitrarily large finite harvesting or ends at a finite cutoff, with an explicit decay law in the persistent case.

## Closest literature and limitations

A primary nonlinear-harvesting paper by Caraballo, Colucci, and Guerrini proves persistence and equilibrium bifurcation results for a different delayed Holling-type harvesting law. It establishes the general methodology as prior art but does not contain the target \(qv^r\) versus \(v^m\) exponent competition.

The theorem is local at the high-harvest coexistence branch and does not prove global persistence from every initial condition. It does not classify \(r<m\).

Self-review: passed. Independent audit: not yet performed.
