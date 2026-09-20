# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The result combines the universal converse of Cohen--D'Oliveira--Sprintson with
an exact Fourier calculation for the uniform nonzero rank-one shell.

For \(K=uv^\top\) with independent uniform nonzero \(u,v\), every nonzero
rank-one matrix has exactly \(q-1\) factorizations, so \(K\) is uniform on the
shell. For a character indexed by a rank-\(s\) matrix \(H\), direct character
orthogonality gives
\[
\lambda_s=
\frac{q^{2n-s}-2q^n+1}{(q^n-1)^2}.
\]
The sequence is strictly decreasing. Its final value is
\(-1/(q^n-1)\), and for \(n\ge3\) the rank-one value dominates that endpoint in
absolute value. Hence the additive channel has maximal correlation
\[
\lambda_1=
\frac{q^{2n-1}-2q^n+1}{(q^n-1)^2}.
\]
Theorem 5 of arXiv:2609.18876v1 gives exactly this expression as a lower bound
for every input-independent rank-at-most-one mask, even after secret invertible
left and right transformations. The achievability and converse therefore match
exactly.

The complete-view corollary was also checked: independent masked uploads form a
product channel whose largest nonconstant Fourier singular value is the same
single-upload value, and the multiplication result is a deterministic function
of those uploads. Conversely, the source theorem explicitly notes that a server
may ignore extra observations, so its upload lower bound applies to the complete
view.

The verification artifact independently enumerates rank-one shells over
\(\mathbb F_2,\mathbb F_3,\mathbb F_5\) for \(n=3\), checks every character rank,
and verifies the symbolic identities over additional prime powers and dimensions.
All recorded checks pass.

## Originality

The motivating preprint, arXiv:2609.18876v1, states finite-length achievability
\(\rho_{\mathrm m}\le q^{-r}\), a converse within a factor of two, and
asymptotic optimality for fixed \(q\) and \(r=o(n)\). Its rank-one specialization
does not state an exact finite-length optimizer or the nonzero rank-one-shell
construction.

The rank-metric Fourier background is classical. Delsarte's bilinear-forms
association scheme describes the relevant character/eigenvalue structure, so no
novelty is claimed for the existence of fixed-rank Fourier spectra. The new claim
is the privacy optimization statement: the rank-one shell has exactly the
coefficient required to saturate the recent universal masking converse, even
against the larger class with secret invertible transformations, and therefore
also gives the exact complete-view optimum.

Targeted searches for uniform nonzero rank-one masks, exact rank-one maximal
correlation, rank-constrained masking, and equivalent finite-field formulations
found the motivating preprint and classical rank-metric background but no prior
statement of this exact secrecy optimum. Searches of the current SCOPE archive by
the source identifier and the same claim family found no overlap.

The claim is made only to the best of our knowledge. Priority risk is elevated
because arXiv:2609.18876v1 is very recent, so a near-simultaneous observation or
a later source revision could cover the same rank-one specialization. No
inaccessible source was identified as a concrete coverage threat; the Delsarte
article was inspected through its bibliographic record and abstract, and its
role here is background on the bilinear-forms spectrum rather than the recent
privacy optimization problem.

## Value

The result turns a finite-length factor-two guarantee into an exact minimax
formula at the first nontrivial rank constraint. It also identifies a sampler
that is strictly better at every finite \(n\ge3\) than both rank-one samplers
analyzed in the source paper, while retaining the same low-rank computational
cost. The improvement is conceptually useful because it separates the optimal
rank-one distribution from the more convenient rank-ball and unconstrained-factor
samplers.

## Limitations

The proof does not establish exact optimality of fixed-rank shells for
\(r\ge2\). The numerical size of the improvement over \(1/q\) vanishes
exponentially with \(n\), so this is primarily an exact finite-length structural
result. The uniform-input and input-independent-mask assumptions are unchanged
from the converse theorem being saturated. No independent audit has been performed.
