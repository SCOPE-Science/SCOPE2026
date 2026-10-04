# A coordinate counterexample to the local relay-dual theorem
## Finding
Hong and Li define a local relay dual by choosing, for each relay space \(K_i\), a frame operator \(S_i\), setting \(\widetilde V_{{ij}}=S_i^{{-1}}V_{{ij}}\), and setting \(\widetilde\Lambda_i=S_i^{{-1}}\tau_{{V_{{ij}}}}\Lambda_i\). Their Theorem 3.10 asserts that this construction takes every relay fusion frame to another relay fusion frame. The assertion fails when the local frame operators are not uniformly controlled.

Take \(H=\ell^2(\mathbb N)\) with standard orthonormal basis \(\{e_i\}_{{i\ge 1}}\). For every \(i\), set \(J_i=\{{1\}}\), \(W_i=\operatorname{{span}}\{{e_i\}}\), \(K_i=V_{{i1}}=\mathbb C\), \(v_{{i1}}=1\), and
\[
\Lambda_i f=\langle f,e_i\rangle.
\]
Then
\[
\sum_{{i=1}}^\infty \|\tau_{{V_{{i1}}}}\Lambda_i\pi_{{W_i}}f\|^2
=\sum_{{i=1}}^\infty |\langle f,e_i\rangle|^2
=\|f\|^2,
\]
so the original family is a Parseval relay fusion frame.

For each one-dimensional local relay space choose the one-vector frame \(\{\sqrt{i}\}\). Its frame operator is \(S_i=iI_{{\mathbb C}}\). The source construction therefore gives
\[
\widetilde V_{{i1}}=S_i^{{-1}}V_{{i1}}=\mathbb C,
\qquad
\widetilde\Lambda_i=S_i^{{-1}}\Lambda_i=\frac1i\Lambda_i.
\]
Consequently
\[
\sum_{{i=1}}^\infty \|\widetilde\Lambda_i\pi_{{W_i}}f\|^2
=\sum_{{i=1}}^\infty \frac{|\langle f,e_i\rangle|^2}{i^2}.
\]
At \(f=e_n\) this quantity is \(1/n^2\), so no positive lower relay-fusion-frame bound exists. Thus the claimed local relay dual need not be a relay fusion frame.

## Assumptions and scope
The counterexample uses the literal Hilbert-space definition of relay fusion frame in the source, a countable index set, singleton second-level index sets, and one-dimensional relay spaces. It therefore avoids the notational issue that \(\widetilde\Lambda_i\) is written with no \(j\)-index although its displayed definition contains \(V_{{ij}}\). Each \(S_i\) is genuinely the frame operator of a frame for \(K_i\), exactly as required in the local relay-dual construction.

The motivating source was publicly published on 27 August 2019 and lists MSC 42C15 first. The result concerns Theorem 3.10 and Remark 3.11 of that source.

## Proof
Let the original relay fusion frame have bounds \(\alpha,\beta\), and suppose instead that its selected local frame operators satisfy
\[
M:=\sup_i\|S_i\|<\infty,
\qquad
N:=\sup_i\|S_i^{{-1}}\|<\infty.
\]
For \(y\in V_{{ij}}\), one has \(S_i^{{-1}}y\in S_i^{{-1}}V_{{ij}}\), hence the projection onto \(S_i^{{-1}}V_{{ij}}\) leaves \(S_i^{{-1}}y\) unchanged. Moreover,
\[
\frac1{\|S_i\|}\|y\|
\le \|S_i^{{-1}}y\|
\le \|S_i^{{-1}}\|\,\|y\|.
\]
Applying this pointwise to \(y=\tau_{{V_{{ij}}}}\Lambda_i\pi_{{W_i}}f\) and summing gives
\[
\frac{\alpha}{M^2}\|f\|^2
\le
\sum_{{i,j}}v_{{ij}}^2\|S_i^{{-1}}\tau_{{V_{{ij}}}}\Lambda_i\pi_{{W_i}}f\|^2
\le
\beta N^2\|f\|^2.
\]
Thus uniform bounds on both \(S_i\) and \(S_i^{{-1}}\) repair the theorem, with explicit relay-fusion-frame bounds.

For the scalar coordinate family above, replacing \(S_i=iI\) by arbitrary positive scalars \(S_i=s_iI\) produces coefficient weights \(s_i^{{-1}}\). The transformed family is a relay fusion frame exactly when
\[
0<\inf_i s_i^{{-1}}\le \sup_i s_i^{{-1}}<\infty,
\]
which is equivalent to uniform boundedness of both \(s_i\) and \(s_i^{{-1}}\). Hence the missing uniformity is not an artifact of the proof in this natural coordinate model.

## Verification
The defining relay-fusion-frame identity, the local frame operators \(S_i=iI\), and the transformed energy were checked symbolically. No numerical approximation or finite truncation is used. The counterexample is already Bessel after transformation; only the positive lower bound fails, so the obstruction targets precisely the frame conclusion.

The source proof itself estimates the upper bound using a displayed \(\max_i\{\|S_i^{{-1}}\|^2\beta\}\) and the lower bound using a displayed \(\min_i\{\alpha/\|S_i\|^2\}\), but the theorem assumes only that each \(S_i\) is a frame operator, not that these extrema are uniformly finite and positive. Remark 3.11 emphasizes that many choices of frames on the local relay spaces are allowed.

## Relationship to prior work
Hong and Li, *Relay fusion frames for Hilbert spaces*, Journal of Inequalities and Applications 2019:226, introduces the local relay dual and states Theorem 3.10. The same article separately introduces relay fusion frame systems with common local frame bounds, showing that a uniform-bounds concept is available elsewhere in the framework but is absent from Theorem 3.10.

Hong and Li, *Relay fusion frames and bridging results for fusion frames*, Journal of Mathematical Analysis and Applications 489 (2020), 124124, develops the relay-fusion-frame framework and again defines common frame bounds for relay-local frame systems. It does not state the counterexample or the repaired local-dual theorem above.

Hong and Li, *Relay fusion frames in Banach spaces*, Open Mathematics 21 (2023), 20220554, uses explicit uniform boundedness assumptions for families of nested g-frames in an analogous Banach-space construction. That later hypothesis is consistent with the uniformity mechanism here but does not imply the Hilbert-space counterexample or repair.

## Limitations
The finding is scoped to the local relay-dual assertion of Theorem 3.10. It does not challenge the global relay-dual theorem, where a single global frame operator automatically has finite operator norm and bounded inverse. The two-sided uniform condition above is a sufficient repair in general and is exact for the scalar coordinate model; no claim is made that it is the weakest possible hypothesis for every fixed relay fusion frame.

A residual originality risk is an unindexed erratum, thesis, or informal note that may already observe the missing uniformity. No such source was located in the checked literature or semantic database searches.

## References
1. G. Hong and P. Li, *Relay fusion frames for Hilbert spaces*, Journal of Inequalities and Applications 2019, article 226 (2019), DOI: 10.1186/s13660-019-2181-9.
2. G. Hong and P. Li, *Relay fusion frames and bridging results for fusion frames*, Journal of Mathematical Analysis and Applications 489 (2020), 124124, DOI: 10.1016/j.jmaa.2020.124124.
3. G. Hong and P. Li, *Relay fusion frames in Banach spaces*, Open Mathematics 21 (2023), 20220554, DOI: 10.1515/math-2022-0554.
