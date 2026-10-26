# Stochastic sign unanimity and deterministic parity cycles in a complete amplification network

## Finding

In the complete-network specialization of the social opinion amplification model, genuine random positive exaggeration has a qualitatively different long-term outcome from fixed exaggeration. For every population size \(n\ge2\), independent uniform exaggeration magnitudes imply **almost-sure finite-time sign unanimity**, with a uniform geometric tail for the waiting time and an exact nonzero escape velocity. By contrast, with the same maximum exaggeration and all magnitudes fixed at that maximum, **mixed-sign two-cycles exist for every \(n\)**. Their admissible initial sign imbalance is at most one individual.

Precisely, let \(0<s\le1/4\), \(4s\le\varepsilon\le1\), and \(|x_i(0)|\le s/2\). Each participant observes every other participant whose previously expressed opinion lies within confidence radius \(\varepsilon\), with the one-step eligibility convention in the source. Everyone amplifies at every step; magnitudes \(A_i(t)\), for \(t\ge1\), are independent \(\operatorname{Unif}[0,s]\). Initial expressions have magnitudes in \([0,s]\). Define \(\operatorname{sgn}_+(z)=1\) for \(z\ge0\), and \(-1\) otherwise. All links remain eligible for every time, and the actual opinion update is
\[
x_i(t)=m(t-1)+\frac{1}{n}\sum_{j\ne i}A_j(t)\operatorname{sgn}_+(x_j(t-1)),\quad m(t)=\frac1n\sum_i x_i(t).
\]

Let \(\tau\) be the first \(t\ge1\) at which either all opinions are strictly positive or all are strictly negative. Then, with
\[
q_n=(4n)^{-12n},
\]
we have the explicit **universal** estimate
\[
\boxed{\Pr\{\tau>1+12k\}\le(1-q_n)^k\quad(k=0,1,2,\ldots).}
\]
In particular, \(\Pr\{\tau<\infty\}=1\). There is a random eventual sign \(S\in\{-1,1\}\) such that simultaneously for every participant
\[
\boxed{\lim_{t\to\infty}\frac{x_i(t)}t=S\frac{(n-1)s}{2n}\quad\text{almost surely}.}
\]
Sign unanimity is not equality of opinions at finite time. The tail constant is explicit but not claimed sharp.

For the deterministic constant-magnitude comparison \(A_i(t)\equiv s\), write \(H\) for the number of positive opinions minus the number of negative opinions at a mixed-sign initial state and \(m\) for its mean. Away from zero-coordinate boundary cases, its subsequent orbit is a mixed-sign two-cycle after at most one transient step exactly when
\[
\boxed{\begin{cases}
H=0,\quad |m|<s/n,&n\ \text{even},\\
H=1,\quad -s(n-1)/n^2<m<0,&n\ \text{odd},\\
H=-1,\quad 0<m<s(n-1)/n^2,&n\ \text{odd}.
\end{cases}}
\]
Outside these strict parameter windows, a generic mixed-sign trajectory becomes sign unanimous and escapes. Thus even versus odd population size changes the location of the deterministic recurrent window, whereas the stochastic conclusion has no parity exception.

## Assumptions and scope

The population consists of \(n\ge2\) agents on the complete graph without self-edges. At time \(t\ge1\), the internally held opinion of agent \(i\) is \(x_i(t)\). Its expression at time \(t\) is \(e_i(t)=x_i(t-1)+A_i(t)\operatorname{sgn}_+(x_i(t-1))\). The listening test at time \(t\) compares \(x_i(t-1)\) to \(e_j(t-1)\), as in equations (3)--(5) of the source, and the update averages the agent's unamplified own opinion with the *current* expressions of its eligible neighbors. For \(t=1\), initialize \(e_j(0)=x_j(0)+A_j(0)\operatorname{sgn}_+(x_j(0))\) with any \(A_j(0)\in[0,s]\). Set every participant's amplification flag and amplification probability to one.

The stochastic theorem uses independent continuous uniform magnitudes at positive integer times. The deterministic comparison uses the different, fixed-magnitude rule \(A_i(t)=s\), and is not asserted to occur with positive probability under a continuous uniform law. Both are legitimate deterministic/stochastic choices of the source's expression mechanism; the stochastic law is precisely the source's uniform-amplitude mechanism at amplification probability one.

The deterministic interval classification excludes equality cases on which an updated opinion is zero, and applies to the induced complete-listening map. For the explicit period-two examples in each parity, initial opinions can be chosen strictly inside \([-s/2,s/2]\), so the complete-listening assumption is automatic under the displayed confidence restriction.

## Proof

**1. Complete listening is invariant.** Assuming all links have passed their tests so far, define \(Z_t=\sum_j A_j(t)\operatorname{sgn}_+(x_j(t-1))\). The update simplifies to
\[
x_i(t)=m(t-1)+\frac{Z_t-A_i(t)\operatorname{sgn}_+(x_i(t-1))}{n}.
\]
It follows exactly that
\[
m(t)-m(t-1)=\frac{n-1}{n^2}Z_t,\qquad
|m(t)-m(t-1)|<s,
\]
and
\[
|x_i(t)-m(t)|\le\frac{2s}{n}\le s\qquad(t\ge1).
\]
At the first update, \(|x_i(0)-e_j(0)|\le2s\). At the second, the maximum test gap is at most \(s+2s/n+s/2+s\le 7s/2\); thereafter it is at most \(s+4s/n+s\le4s\). Hence \(\varepsilon\ge4s\) guarantees every test passes. Induction justifies the full-graph update for all times; this conclusion is not an assumption of the stochastic proof.

**2. Mixed signs force a narrow mean.** If at time \(t\ge1\) there are both positive and negative opinions, then some coordinates lie on either side of zero. Since all coordinates lie within \(2s/n\) of their own average, necessarily
\[
|m(t)|\le2s/n.
\]
Set \(\delta=1/(4n)\). Conditional on the past while signs are mixed, prescribe the following event for the next magnitudes: every currently positive agent draws in \([s(1-\delta),s]\), and every currently negative agent draws in \([0,s\delta]\). This event has conditional probability exactly \(\delta^n\). Since there is at least one positive agent,
\[
Z_{t+1}\ge s\bigl(1-n\delta\bigr)=\frac{3s}{4}.
\]
Thus, provided mixed signs persist, \(m\) grows by at least \(3s(n-1)/(4n^2)\) on each prescribed step. In any 12-step block, twelve such sign-adapted events have probability \(\delta^{12n}=q_n\). If mixed signs survived all twelve steps, the resulting mean increase would be at least \(9s(n-1)/n^2>4s/n\), contradicting its confinement to \([-2s/n,2s/n]\) at both endpoints; the strict inequality holds for all \(n\ge2\). Thus every twelve-step block starting at time \(t\ge1\) while still mixed contains a positive-probability route to unanimous sign. Applying the conditional bound successively gives the geometric tail in the finding. A zero opinion at a positive time has probability zero, because the updated coordinate is a nondegenerate linear combination of independent continuously distributed magnitudes. This validates the strict-sign formulation almost surely.

**3. Unanimity is absorbing and has an exact speed.** If every \(x_i(t)>0\), then every \(x_i(t+1)=m(t)+\sum_{j\ne i}A_j(t+1)/n>0\). The analogous assertion holds for uniformly negative opinions. Once \(\tau<\infty\), the mean therefore satisfies
\[
m(t)-m(t-1)=S\frac{n-1}{n^2}\sum_j A_j(t).
\]
The strong law of large numbers for the underlying independent uniforms yields
\[
\lim_{t\to\infty}\frac{m(t)}t=S\frac{n-1}{n}\mathbb E[A_i(t)]
=S\frac{(n-1)s}{2n}.
\]
The uniform bound \(|x_i(t)-m(t)|\le2s/n\) transfers the limit simultaneously to each agent. The finite random pre-unanimity prefix does not affect the limit.

**4. Deterministic parity comparison.** If \(A_i(t)\equiv s\), fix a mixed-sign state with sign vector \(\sigma\), mean \(m\), and \(H=\sum_i\sigma_i\). The update gives two possible values: old positives become \(m+s(H-1)/n\), and old negatives become \(m+s(H+1)/n\). These values are strictly of mixed signs precisely when
\[
-\frac{s(H+1)}n<m<-\frac{s(H-1)}n.
\]
When this happens, every sign reverses, \(H\) changes to \(-H\), and the mean changes to \(m+sH(n-1)/n^2\). The reverse phase is also mixed precisely when
\[
\frac{s(H-n)}{n^2}<m<\frac{s(H+n)}{n^2}.
\]
Both intervals overlap only if \(|H|<2n/(n+1)\); because \(H\) is an integer of the same parity as \(n\), this forces \(H=0\) for even \(n\), and \(H=\pm1\) for odd \(n\). Intersecting the intervals yields the exact three windows displayed above. Under these conditions the second update returns the original mean and sign pattern, so a third update reproduces the first update. Hence the orbit is period two after the first transient. Outside them, with strict nonzero updated signs, a mixed trajectory cannot survive two further steps: if the first step remains mixed, every sign must reverse; if the next one is not mixed, unanimity is absorbing.

The windows are nonempty with admissible initial opinions: for even \(n\), take equal numbers of \(s/4\) and \(-s/4\). For odd \(n\), take \((n+1)/2\) initial opinions \(s/4-s/(2n)\) and \((n-1)/2\) opinions \(-s/4-s/(2n)\). Their signs have \(H=1\) and their mean is \(-s/(4n)\), inside the odd-population window for every \(n\ge3\). These choices satisfy \(|x_i(0)|<s/2\) and therefore also satisfy the confidence premise proved in step 1.

## Verification

Running `python3 verify.py` uses the Python standard library only. It checks the exact all-listening update and deterministic parity-window equivalence by rational arithmetic for population sizes 2 through 8 over mixed-sign configurations and many means; it then simulates 100 independent uniform-amplitude sample paths at each of the sizes 2, 3, 4, 7, and 15, checking the mean increment and the actual previous-expression confidence gaps. All tested paths reached sign unanimity. The exact infinite-time, all-population, and probability-tail conclusions follow from the mathematical argument above rather than from finite simulations.

## Relationship to prior work

Lim and Bentley's original social opinion amplification model gives equations (3)--(5) for distinct internally held and amplified expressed opinions and numerically examines opinion extremism and possible countermeasures on sampled networks. Its Methods and Results, inspected in full from a lawful university-hosted copy, do not give a full-graph almost-sure sign-absorption theorem, a uniform hitting-time tail, a deterministic parity-window classification, or a post-absorption escape speed. The source's simulations and its finite-time observations of extreme convergence do not logically imply these almost-sure statements.

Standard linear DeGroot averaging theory concerns fixed stochastic averaging matrices without state-dependent signed expressed-opinion offsets; its convergence theorems do not determine this model's sign exit and linear escape. General synchronous majority dynamics can exhibit period-two behavior on graphs, but its binary majority update is not this signed-amplification averaging map. Scalar sign-momentum optimization has two-cycles for unrelated one-dimensional update equations and does not imply the complete-network parity windows or the stochastic sign-absorption theorem.

## Limitations

The theorem uses a complete graph, a common high confidence radius, and initially bounded internal opinions. It sets every agent's amplification probability to one; sparse or directed random networks and intermittent amplification are not covered. The long-term conclusion is sign unanimity and linear growth, **not** convergence to a finite common opinion. The explicit geometric-tail constant is very conservative. The constant-magnitude comparison changes the amplitude distribution and does not describe an event of positive probability in the uniform stochastic model. The model does not impose an upper saturation bound on internal opinions, consistent with the source's definition. The result has not undergone independent mathematical audit. An equivalent proof in a more general random-affine consensus or relay-process framework may exist and is a residual literature risk.

## References

1. S. L. Lim and P. J. Bentley, *Opinion amplification causes extreme polarization in social networks*, Scientific Reports 12, 18131 (2022), first publicly published 2022-10-28, DOI: 10.1038/s41598-022-22856-z. University-hosted open-access PDF: https://discovery.ucl.ac.uk/id/eprint/10158887/1/s41598-022-22856-z.pdf .
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, Stochastic Processes and their Applications 126 (2016), 2719--2733, DOI: 10.1016/j.spa.2016.02.015.
3. M. Brill, *A Survey on Nonstrategic Models of Opinion Dynamics*, Games 11 (2020), 65, DOI: 10.3390/g11040065.
