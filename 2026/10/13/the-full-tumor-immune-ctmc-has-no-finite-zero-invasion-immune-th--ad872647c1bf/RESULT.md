# The full tumor–immune CTMC has no finite zero-invasion immune threshold
## Finding
Jang and Yen define a continuous-time Markov chain for tumor cells, effector immune cells, and IL-4 molecules on
\[
\{0,1,\ldots,K\}\times\mathbb N_0\times\mathbb N_0.
\]
For this exact CTMC, every finite state with
\[
1\le x\le K
\]
has strictly positive probability of reaching the invasion threshold \(x=K\) before tumor extinction, regardless of the finite immune count.

This remains true on every fixed positive time horizon. For every
\[
T>0,
\]
\[
\mathbb P_{x,y,z}\!\left(\tau_K<\tau_0\wedge T\right)>0.
\]

Therefore the source's frozen-environment critical immune level
\[
\bar y_c=\frac{r(m+1)}{\delta}
\]
is not an impossibility threshold for the fully coupled CTMC. Crossing that level can make invasion very unlikely, but it cannot make the exact CTMC invasion probability equal to zero.

The source reports \(10^4\) simulated paths in its reduced-scale experiment with no observed invasion and interprets later crossing of the immune threshold as making extinction certain. The transition graph itself rules out that exact interpretation. Zero observations establish a rare-event bound, not a mathematical zero.

## Assumptions and scope
The source's CTMC has integer tumor carrying capacity
\[
K\in\mathbb N
\]
and state
\[
(x,y,z)\in\{0,1,\ldots,K\}\times\mathbb N_0\times\mathbb N_0.
\]
The relevant transition rates are
\[
r_1(x,y,z)=r x\left(1-\frac{x}{K}\right)
\]
for a tumor birth,
\[
r_2(x,y,z)=\frac{\delta xy}{m+x}
\]
for immune-mediated tumor death,
\[
r_3(x,y,z)=\frac{\beta xy}{k+x}+byz
\]
for immune-cell birth,
\[
r_4(x,y,z)=ay+cy^2
\]
for immune-cell death,
\[
r_5(x,y,z)=\frac{\alpha xy}{h+x}
\]
for cytokine production, and
\[
r_6(x,y,z)=\mu z
\]
for cytokine decay.

The theorem assumes the source's positive parameters, in particular
\[
r>0,\qquad a>0.
\]
It concerns the exact CTMC defined by these rates. The article uses a numerical tau-leaping implementation for its Monte Carlo study; no claim is made here that every discretization artifact of that simulator has the same rare-event probability as the exact CTMC.

The invasion event is the source's event of reaching
\[
x=K
\]
before reaching
\[
x=0.
\]
The finding concerns strict positivity, not a practically useful lower bound.

## Proof
Fix a finite initial state
\[
(x_0,y_0,z_0)
\]
with
\[
1\le x_0\le K.
\]
If \(x_0=K\), invasion has already occurred. Assume
\[
x_0<K.
\]

First consider the finite event sequence consisting of \(y_0\) consecutive immune-death jumps. At a state
\[
(x_0,j,z_0),\qquad j\ge1,
\]
the desired jump rate is
\[
r_4(x_0,j,z_0)=aj+cj^2>0.
\]
Every other rate at that finite state is finite, hence the total leaving rate
\[
R(x_0,j,z_0)=\sum_{i=1}^6 r_i(x_0,j,z_0)
\]
is finite and positive. Conditional on a jump occurring, the probability that the next jump is the immune-death jump equals
\[
\frac{r_4(x_0,j,z_0)}{R(x_0,j,z_0)}>0.
\]
The product of these finitely many positive conditional probabilities is positive. Therefore the process can reach
\[
(x_0,0,z_0)
\]
without changing the tumor or cytokine counts with positive probability.

On the face
\[
y=0,
\]
the rates satisfy
\[
r_2=r_3=r_4=r_5=0.
\]
Thus tumor-death jumps are unavailable, immune cells cannot be regenerated, and cytokines cannot be produced. For every
\[
1\le x<K,
\]
the tumor-birth rate is
\[
r_1(x,0,z)=r x\left(1-\frac{x}{K}\right)>0.
\]
The only possible competitor is cytokine decay, with rate
\[
r_6(x,0,z)=\mu z.
\]
At each state with \(x<K\), choosing a tumor birth as the next event therefore has strictly positive conditional probability. The product of the \(K-x_0\) such positive probabilities is positive, so the path reaches
\[
x=K
\]
before tumor extinction.

This proves
\[
\mathbb P_{x_0,y_0,z_0}(\tau_K<\tau_0)>0.
\]

For the finite-horizon statement, the constructed path contains finitely many jumps. At every intermediate state its total rate is finite and positive. An exponential holding time with positive finite rate has positive probability of being smaller than any prescribed positive number. If the path has \(N\) jumps, require each holding time to be less than
\[
\frac{T}{N}.
\]
The intersection of these finitely many positive-probability jump-type and holding-time events has positive probability. Hence
\[
\mathbb P_{x_0,y_0,z_0}\!\left(\tau_K<\tau_0\wedge T\right)>0
\]
for every
\[
T>0.
\]

The source's branching threshold is derived after freezing the immune environment. It is therefore compatible with zero branching-process invasion probability while the fully coupled CTMC retains the rare path above.

Finally, if \(n=10^4\) independent Bernoulli simulations produce zero invasions, the one-sided 95% Clopper–Pearson upper endpoint \(p_{0.95}\) solves
\[
(1-p_{0.95})^{10000}=0.05,
\]
giving
\[
p_{0.95}=1-0.05^{1/10000}
=0.0002995283597766\ldots.
\]
Thus a zero Monte Carlo count cannot distinguish exact zero from a sufficiently rare positive event.

## Verification
The bundled script `verification/verify.py` checks three pieces independently of the prose proof.

First, with exact rational source-like positive parameters, it evaluates every rate along the constructed immune-death path and confirms that each selected jump has positive rate and positive conditional probability.

Second, after the path reaches \(y=0\), it checks that
\[
r_2=r_3=r_4=r_5=0
\]
while
\[
r_1>0
\]
for every tumor count below \(K\), and it computes a strictly positive product for the finite sequence of tumor-birth selections.

Third, it evaluates the exact zero-success Clopper–Pearson endpoint numerically at high precision and reproduces
\[
0.0002995283597766\ldots.
\]

The finite computations replay a representative path. The general theorem follows from positivity and finiteness of the symbolic rates, not from the numerical example.

## Relationship to prior work
The motivating article itself distinguishes the frozen branching approximation from the fully coupled CTMC and correctly emphasizes that immune feedback can dramatically reduce invasion probability. Its numerical section goes further, however, by interpreting threshold crossing as making extinction certain and invasion no longer possible in the full stochastic system. The CTMC transition graph does not support that exact zero-probability conclusion.

Classical tumor-extinction work already emphasizes that branching approximations are local low-population tools. Merrill studies branching and density-dependent jump-process approximations for tumor elimination by cytotoxic cells. Liu, Li, and Pan develop a different tumor–immune chemotherapy CTMC and use it to estimate tumor-extinction probabilities. Yang, Tan, and Cheke derive extinction and persistence thresholds for a stochastic tumor–immune model with pulsed treatment.

These sources establish the broader stochastic tumor–immune context. The present claim is narrower and source-specific: the exact event graph printed by Jang and Yen contains a finite positive-probability route from every nonzero tumor state to \(x=K\), so no finite immune count can be a zero-invasion threshold for that CTMC.

## Limitations
The theorem provides strict positivity but not a useful numerical lower bound. The constructed event sequence may have an astronomically small probability under strongly suppressive parameter regimes.

The article's reported simulations use a tau-leaping approximation. The statistical zero-count statement applies to the sampled law under independent runs, while the exact reachability theorem applies to the continuous-time Markov chain specified by the transition rates. Quantifying the discretization error between those laws is outside this finding.

The result does not invalidate the source's central qualitative observation that dynamic immune–cytokine feedback can reduce invasion probability far below a frozen branching estimate. It corrects only the stronger interpretation that threshold crossing makes full-CTMC invasion mathematically impossible.

## References
1. S. R.-J. Jang, J.-Y. Yen, “Stochastic Invasion and Immune Feedback in a Tumor–Immune–IL-4 Model,” Mathematics 14 (2026), 2352. DOI: 10.3390/math14132352.
2. S. J. Merrill, “Stochastic models of tumor growth and the probability of elimination by cytotoxic cells,” Journal of Mathematical Biology 20 (1984), 305–320. DOI: 10.1007/BF00275990.
3. X. Liu, Q. Li, J. Pan, “A deterministic and stochastic model for the system dynamics of tumor-immune responses to chemotherapy,” Physica A 500 (2018), 162–176. DOI: 10.1016/j.physa.2018.02.118.
4. J. Yang, Y. Tan, R. A. Cheke, “Thresholds for extinction and proliferation in a stochastic tumour-immune model with pulsed comprehensive therapy,” Communications in Nonlinear Science and Numerical Simulation 73 (2019), 363–378. DOI: 10.1016/j.cnsns.2019.02.025.
