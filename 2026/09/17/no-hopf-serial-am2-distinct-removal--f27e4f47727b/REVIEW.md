# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

### Claim checked

The proposed result is that the eight-dimensional serial AM2 model of Hmidhi
and Fekih-Salem cannot undergo a local Hopf bifurcation at any equilibrium, and
that the additional negative-trace condition imposed on the second-reactor
coexistence block is redundant once its determinant is positive.

### Structural check

Ordering the variables by the four substrate--biomass pairs makes the Jacobian
block lower triangular. Therefore its eigenvalues are the union of the
eigenvalues of four \(2\times2\) diagonal blocks. This is visible directly from
system (1): the first acidogenic pair drives later pairs but receives no
feedback; the first methanogenic and second acidogenic pairs receive upstream
forcing; the second methanogenic pair is downstream of both.

A zero-biomass diagonal block is triangular, so it has real eigenvalues.

For a positive first-reactor biomass, the biomass equilibrium equation gives
\(\mu=\alpha D_1\). The corresponding block has
\[
\det A_1=k\alpha D_1\mu' x,\qquad
\operatorname{tr}A_1=-D_1-k\mu' x.
\]
Positive determinant forces \(\mu'>0\), hence strictly negative trace.

For a positive second-reactor biomass, let \(x_0\) be its upstream biomass,
\(x\) its local biomass, and \(r=x_0/x\). The equilibrium biomass equation gives
\(\mu=\alpha D_2(1-r)\) with \(0\le r\le1\). With
\(q=-k\mu'x\) and \(\delta=\alpha D_2r\),
\[
\operatorname{tr}A_2=q-D_2-\delta,\qquad
\det A_2=D_2(\delta-\alpha q).
\]
If \(\det A_2>0\), then \(q<D_2r\), so
\[
\operatorname{tr}A_2<-D_2(1-r+\alpha r)<0.
\]
Conversely, at \(\operatorname{tr}A_2=0\),
\[
\det A_2=\alpha D_2^2((1-\alpha)r-1)
\le -\alpha^2D_2^2<0
\]
for the source assumption \(0<\alpha<1\). Thus no positive diagonal block can
have positive determinant and zero trace, and no full-system equilibrium can
have a nonzero purely imaginary eigenvalue pair.

A symbolic algebra simplification confirms the displayed determinant and trace
identities; no numerical approximation is needed for the proof.

### Adversarial checks

- The conclusion does not rely on monotonicity of \(\mu_2\); it remains valid on
  the inhibited branch where \(\mu_2'<0\).
- The case of zero local biomass is separate and triangular, so division by
  biomass is not used there.
- For positive local biomass, nonnegative growth implies \(0\le r\le1\);
  the source model's interior coexistence states have the strict version
  \(r<1\).
- Off-diagonal inter-reactor and inter-species couplings do not change the
  eigenvalue union because the full Jacobian is block lower triangular.
- A Hopf bifurcation is ruled out, but a global periodic orbit is not. The
  public result does not conflate these statements.

Correctness verdict: **PASS**.

## Originality

The primary source, arXiv:2604.18903 (submitted 20 April 2026), states in its
abstract and conclusion that second-bioreactor coexistence stability may depend
on an additional trace condition and that identifying Hopf bifurcations and
limit cycles remains open. In Remark 1 it specifically describes a
positive-determinant regime with apparently undetermined trace.

The earlier serial-AM2 work with equal removal rates, arXiv:2408.04984 /
Bulletin of Mathematical Biology 87 (2025), treats a reducible special case and
provides complete equilibrium stability, but does not state the present
determinant--trace obstruction for the distinct-rate eight-dimensional system.

Searches covered the exact 2026 title and identifier, combinations of AM2,
serial/interconnected chemostats, Hopf bifurcation, limit cycles, Jacobian
trace/determinant, and related distinct-removal-rate chemostat literature. No
correction, comment, later version, or paper stating this source-specific
no-Hopf theorem or trace redundancy was located. The arXiv record remains v1.

Related literature shows that Hopf bifurcations do occur in other chemostat and
anaerobic-digestion architectures, including aggregated-biomass/flocculation
models with distinct removal rates and three-tier microbial food webs. Those
systems introduce feedback structures absent from the serial AM2 cascade and do
not imply the result here.

No highly relevant source was identified whose inaccessible theorem statement
poses a concrete coverage concern. Residual originality risk remains from
older chemostat literature that may contain an equivalent cascade-block lemma
under different notation. The generic linear-algebra ingredients are standard
and are not claimed as original.

Originality verdict: **PASS, to the best of our knowledge**.

## Value

The result closes the Hopf half of an explicit open question in a recent AM2
preprint and removes an unnecessary trace test from the local stability
classification. It also completes the previously trace-indeterminate
multiple-root stability pattern: determinant-positive odd roots are stable in
the relevant block, while determinant-negative even roots remain unstable.

The mechanism is reusable: the equilibrium flux balance bounds the destabilizing
slope term tightly enough that a trace-zero crossing necessarily occurs after
the determinant has become negative. This identifies why genuine Hopf behavior
seen in other chemostat models requires additional feedback structure.

Value verdict: **PASS**.

## Review status

This is a same-model scientific review. It is not independent validation,
formal verification, expert attestation, or journal peer review.
