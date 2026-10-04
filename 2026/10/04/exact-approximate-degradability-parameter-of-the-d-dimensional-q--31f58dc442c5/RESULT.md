# Exact approximate-degradability parameter of the d-dimensional quantum erasure channel

## Finding

For the standard \(d\)-dimensional erasure channel
\[
\mathcal E_{p,d}(\rho)=(1-p)\rho\oplus p\operatorname{Tr}(\rho)|e\rangle\langle e|,
\qquad d\ge2,
\]
the complementary channel is unitarily equivalent to \(\mathcal E_{1-p,d}\).  In the approximate-degradability convention of Sutter, Scholz, Winter, and Renner, define
\[
\varepsilon_{\mathcal E_{p,d}}
=
\inf_{\Xi\ \mathrm{CPTP}}
\left\|\mathcal E^c_{p,d}-\Xi\circ\mathcal E_{p,d}\right\|_\diamond.
\]
Then
\[
\varepsilon_{\mathcal E_{p,d}}
=
\begin{cases}
0,&0\le p\le \tfrac12,\\[3pt]
2(2p-1)(1-d^{-2}),&\tfrac12<p\le1.
\end{cases}
\]
For \(p>1/2\), an optimal degrading map has an elementary operational form.  It sends a surviving receiver state directly to the environment data sector.  On the receiver erasure flag, it outputs the maximally mixed data state \(I_d/d\) with probability
\[
\frac{2p-1}{p}
\]
and the environment erasure flag with probability
\[
\frac{1-p}{p}.
\]
Its defect from the complementary channel is exactly
\[
(2p-1)(\operatorname{id}-\mathcal R),
\qquad
\mathcal R(\rho)=\operatorname{Tr}(\rho)I_d/d,
\]
and
\[
\|\operatorname{id}-\mathcal R\|_\diamond=2(1-d^{-2}).
\]

## Assumptions and scope

The input data space has finite dimension \(d\ge2\).  The erasure flag is orthogonal to the data sector.  The result concerns the smallest diamond-norm defect in the approximate-degradability definition, not distance to the set of degradable channels.  Complementary channels that differ by an environment isometry give the same value.  No capacity formula beyond the standard erasure-channel facts is claimed.

## Proof

For \(p\le1/2\), exact degradability is immediate.  Whenever the receiver gets the unerased data state, the degrading channel forwards that state to the environment data sector with conditional probability \(p/(1-p)\) and otherwise emits the environment erasure flag.  A receiver erasure flag is sent to the environment erasure flag.  The environment therefore receives the input state with total probability \(p\), exactly reproducing \(\mathcal E^c_{p,d}\), so \(\varepsilon_{\mathcal E_{p,d}}=0\).

Now let \(p>1/2\) and put \(\delta=2p-1>0\).  Because the channel and its complement are covariant under \(U(d)\) on the data sector while fixing the erasure flag, any degrading map can be Haar-twirled without increasing the diamond error.  Pinching data versus flag sectors is likewise harmless because both target and channel outputs are block diagonal.  Thus an optimal degrading map may be taken in the covariant form
\[
D_0(\rho)=s\left[a\rho+(1-a)\operatorname{Tr}(\rho)I_d/d\right]
\oplus(1-s)\operatorname{Tr}(\rho)|e\rangle\langle e|,
\]
for a data-sector input, and
\[
D_e(|e\rangle\langle e|)=tI_d/d\oplus(1-t)|e\rangle\langle e|
\]
for the receiver erasure flag.  Here \(0\le s,t\le1\), and complete positivity of the depolarizing block in particular implies \(a\le1\).

The data block of the defect \(\Delta=\mathcal E^c_{p,d}-D\circ\mathcal E_{p,d}\) is
\[
\Delta_0(\rho)=A\rho-B\operatorname{Tr}(\rho)I_d/d,
\]
where
\[
A=p-(1-p)sa,
\qquad
B=(1-p)s(1-a)+pt.
\]
The flag block is \(-(A-B)\operatorname{Tr}(\rho)|e\rangle\langle e|\).  Since \(s\le1\) and \(a\le1\),
\[
A\ge p-(1-p)=\delta.
\]
Testing \(\Delta\) on a normalized maximally entangled input gives the trace-norm lower bound
\[
\|\Delta\|_\diamond
\ge
\left|A-\frac{B}{d^2}\right|
+\frac{d^2-1}{d^2}B
+|A-B|.
\]
Here \(B\ge0\).  With \(q=d^2\) and \(b=B/A\), the right-hand side divided by \(A\) is
\[
f_q(b)=\left|1-\frac bq\right|+\frac{q-1}{q}b+|1-b|.
\]
A direct three-interval calculation on \(0\le b\le1\), \(1\le b\le q\), and \(b\ge q\) gives
\[
\min_{b\ge0}f_q(b)=2\left(1-\frac1q\right),
\]
with the minimum attained at \(b=1\).  Therefore every degrading channel obeys
\[
\|\Delta\|_\diamond
\ge
2\delta(1-d^{-2}).
\]

For the matching upper bound, take \(s=a=1\), and on a receiver erasure flag choose
\[
t=\frac{\delta}{p}=\frac{2p-1}{p}.
\]
The remaining flag probability is \((1-p)/p\), so this is a channel.  It has \(A=B=\delta\), hence
\[
\Delta=\delta(\operatorname{id}-\mathcal R)
\]
on the data output, with no flag defect.

It remains to compute the norm of \(\operatorname{id}-\mathcal R\).  On the normalized maximally entangled state \(|\Phi_d\rangle\),
\[
\left((\operatorname{id}-\mathcal R)\otimes\operatorname{id}\right)
(|\Phi_d\rangle\langle\Phi_d|)
=|\Phi_d\rangle\langle\Phi_d|-I_{d^2}/d^2,
\]
whose trace norm is \(2(1-d^{-2})\).  This gives the lower bound.  For the upper bound, the positive part of the unnormalized Choi matrix
\[
J=|\Omega\rangle\langle\Omega|-I_d\otimes I_d/d
\]
is
\[
J_+=(d-d^{-1})|\Phi_d\rangle\langle\Phi_d|,
\]
and
\[
\operatorname{Tr}_{\mathrm{out}}J_+=(1-d^{-2})I_d.
\]
The standard diamond-norm semidefinite program therefore gives the matching upper bound \(2(1-d^{-2})\).  Combining the two bounds proves the formula.

## Verification

`verify_erasure_degradability.py` checks the scalar minimization lower bound on a dense exact-rational grid for \(2\le d\le12\), verifies the Choi positive-part certificate algebraically, and checks the proposed degrading-channel probabilities for many exact rational erasure probabilities on both sides of \(p=1/2\).  It returns `VERIFY_OK`.  These finite checks are supplementary; the continuum statement is proved analytically above.

## Relationship to prior work

Sutter, Scholz, Winter, and Renner introduced \(\varepsilon\)-degradability and proved that the least admissible \(\varepsilon\) for a finite-dimensional channel can be computed by a semidefinite program.  Their applications treat channels such as the depolarizing channel.  The inspected full text contains no erasure-channel specialization.

A later semidefinite-programming tutorial by Siddhu and Tayur explicitly checks the erasure channel only in the degradable range \(0\le p\le1/2\), where the optimum is \(0\), and notes antidegradability above the threshold.  The formula here supplies the exact nonzero defect throughout the antidegradable half and in arbitrary finite input dimension.

Focused literature and database searches did not locate the displayed closed formula or the explicit optimal degrading map.  The general SDP and the classical degradability threshold are prior work and are not claimed anew.

## Limitations

The proof uses the exact flag/data direct-sum symmetry of the standard erasure channel.  It does not automatically extend to flagged channels whose unerased branch is noisy, to nonorthogonal erasure flags, or to the distinct notion of distance to a degradable channel.  A residual literature risk remains because the symmetry reduction is short and could have appeared in notes, software documentation, or unindexed discussions even though it was not found in the inspected sources.

## References

1. D. Sutter, V. B. Scholz, A. Winter, and R. Renner, “Approximate Degradable Quantum Channels,” arXiv:1412.0980; *IEEE Transactions on Information Theory* 63 (2017), 7832–7844.
2. V. Siddhu and S. Tayur, “Five Starter Pieces: Quantum Information Science via Semidefinite Programs,” *INFORMS Tutorials in Operations Research* (2022), 59–92, DOI: 10.1287/educ.2022.0243.
3. J. Watrous, “Simpler semidefinite programs for completely bounded norms,” *Chicago Journal of Theoretical Computer Science* 2013, Article 8; arXiv:1207.5726.
