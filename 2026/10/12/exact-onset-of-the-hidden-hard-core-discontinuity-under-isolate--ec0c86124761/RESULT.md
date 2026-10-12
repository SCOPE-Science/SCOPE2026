# Exact onset of the hidden hard-core discontinuity under isolate removal on regular trees
## Finding
Let \(T\) remove every occupied site whose neighbors are all empty, and let \(\mu'_p=\mu_p\circ T^{-1}\) be the image of the Bernoulli field on the Cayley tree of order \(d\ge2\). Put
\[
\lambda=\frac{p}{1-p},\qquad
\lambda_{\mathrm{hc}}(d)=\frac{d^d}{(d-1)^{d+1}},\qquad
p_{\mathrm{hc}}(d)=\frac{d^d}{d^d+(d-1)^{d+1}}.
\]
For every \(p>p_{\mathrm{hc}}(d)\), the image measure \(\mu'_p\) is not quasilocally Gibbs. At and below \(p_{\mathrm{hc}}(d)\), the specific all-zero hidden-hard-core parity witness used here has no phase split. Thus \(p_{\mathrm{hc}}(d)\) is the exact onset of this witness, not asserted to be the full Gibbs/non-Gibbs boundary. For the binary tree, \(p_{\mathrm{hc}}(2)=4/5\).

## Assumptions and scope
The tree is the regular Cayley tree of order \(d\ge2\), meaning that a directed edge sees \(d\) forward descendants. Away from the distinguished root every vertex has degree \(d+1\). The starting law \(\mu_p\) is i.i.d. Bernoulli occupation with \(0<p<1\). The conclusion concerns the quasilocal Gibbs property of the transformed measure and the all-zero second-layer conditioning. It does not address whether other bad configurations can create non-Gibbsianness at smaller \(p\).

## Proof
Under all-zero second-layer conditioning, every occupied first-layer site must be isolated from all other occupied sites. Therefore the allowed first-layer configurations are exactly independent sets. Their Bernoulli weights are proportional to \(\lambda^{N_1}\), where \(N_1\) is the number of occupied sites and \(\lambda=p/(1-p)\). This is the standard hard-core gas.

For a finite directed branch, let \(Z_0\) and \(Z_1\) be its partition functions with the top vertex fixed empty or occupied, and set \(r=Z_1/Z_0\). A top vertex has \(d\) forward children, so one layer of recursion gives
\[
f(r)=\frac{\lambda}{(1+r)^d}.
\]
The unique fixed point \(r_*\) satisfies \(\lambda=r_*(1+r_*)^d\). At a loss of stability,
\[
|f'(r_*)|=\frac{d r_*}{1+r_*}=1,
\]
so \(r_*=1/(d-1)\) and
\[
\lambda_{\mathrm{hc}}(d)=\frac{d^d}{(d-1)^{d+1}}.
\]
The exact hard-core tree recursion has one limiting cavity ratio for \(\lambda\le\lambda_{\mathrm{hc}}(d)\), while for \(\lambda>\lambda_{\mathrm{hc}}(d)\) the iteration from the boundary alternates between two limits \(r_-<r_+\). This is the standard regular-tree uniqueness transition.

The boundary condition in the source fixes the exterior occupied. The outermost interior layer is therefore forced empty, so its inward cavity iteration starts at \(r_0=0\). Consider the source cylinder in which the observation root is empty and all of its \(q=d+1\) neighbors are occupied. The hard-core constraint then automatically forces every distance-two vertex empty, so this is precisely the alternating \(B_2\)-pattern used in the source. If the incoming neighbor message is \(r\), its probability is
\[
P_q(r)=\frac{r^q}{(1+r)^q+\lambda}.
\]
Indeed, the root-empty partition contribution is \((1+r)^q\), the root-occupied contribution is \(\lambda\), and the specified root-empty/all-neighbors-occupied contribution is \(r^q\). Moreover
\[
P_q'(r)=\frac{q r^{q-1}\bigl((1+r)^{q-1}+\lambda\bigr)}{\bigl((1+r)^q+\lambda\bigr)^2}>0.
\]
Hence \(P_q(r_-)\ne P_q(r_+)\) whenever \(\lambda>\lambda_{\mathrm{hc}}(d)\).

Lemma 1 of the primary source expresses a ratio of two second-layer conditional cylinder probabilities as \(\lambda\) times the corresponding first-layer alternating-cylinder probability. Its quasilocality argument shows that, if a compatible quasilocal specification existed, even- and odd-radius versions of the relevant local ratio would have to agree asymptotically. Remark 2 gives an \(R\)-independent positive lower bound on the denominator for every fixed \(p\in(0,1)\). The strict parity gap \(P_q(r_+)\ne P_q(r_-)\) therefore gives the same contradiction for every \(\lambda>\lambda_{\mathrm{hc}}(d)\), rather than only for the sufficiently large activities controlled by the source's cutset estimate. Converting \(\lambda=p/(1-p)\) gives the stated \(p_{\mathrm{hc}}(d)\).

At equality, \(r_-=r_+=1/(d-1)\); below equality the regular-tree hard-core recursion has a single limit. Thus the parity witness itself turns on exactly at the displayed threshold.

## Verification
The critical activity follows by exact substitution of \(r_*=1/(d-1)\) into \(\lambda=r_*(1+r_*)^d\). The transfer from the hidden hard-core split to the transformed measure uses the primary source's Lemma 1 and Remark 2 directly. The standalone `verify.py` checks the exact threshold identities for several integer orders and numerically replays the alternating cavity limits and strict local-cylinder separation above threshold. Those finite checks are corroborative only; the infinite-volume conclusion rests on the analytic recursion and the standard exact hard-core uniqueness theorem.

## Relationship to prior work
Henning, Külske, and Schubert prove non-quasilocality on bounded-degree trees for sufficiently large \(p\), explicitly include regular trees, identify the all-zero conditioned first layer as a hard-core gas, and use its hidden phase transition to create the second-layer discontinuity. Their quantitative tree argument controls that transition only as \(p\uparrow1\), and Theorem 1 therefore leaves an unspecified upper threshold \(p_2(d_{\max})\). The standard hard-core literature gives the exact uniqueness activity \(d^d/(d-1)^{d+1}\) on the infinite \(d\)-ary tree, but does not state the isolate-removal non-Gibbs consequence. Combining the source's exact two-layer transfer with the regular-tree cavity transition yields the explicit threshold above.

Targeted searches by the source identifier, isolate-removal terminology, hard-core aliases, the exact activity, and the converted Bernoulli threshold found no statement with the same implication. The closest companion work treats \(\mathbb Z^d\), not regular trees.

## Limitations
The result proves a sharp onset only for the all-zero hidden-hard-core discontinuity witness. It does not prove quasilocal Gibbsianness for the entire interval \(p\le p_{\mathrm{hc}}(d)\), does not exclude other bad second-layer configurations there, and does not address the one-dimensional case. The standard hard-core uniqueness threshold is used as an established theorem; the included finite replay is not a substitute for that infinite-volume result. An equivalent observation may exist in weakly indexed notes or unpublished calculations.

## References
1. F. Henning, C. Külske, N. Schubert, *Gibbs Properties of the Bernoulli Field on Inhomogeneous Trees under the Removal of Isolated Sites*, arXiv:2304.03102; Markov Processes and Related Fields 29(5), 641--659.
2. A. Sinclair, P. Srivastava, Y. Yin, *Spatial mixing and approximation algorithms for graphs with bounded connective constant*, arXiv:1308.1762.
3. B. Jahnel, C. Külske, *Gibbsianness and non-Gibbsianness for Bernoulli lattice fields under removal of isolated sites*, arXiv:2109.13997; Bernoulli 29(4), 3013--3032.
