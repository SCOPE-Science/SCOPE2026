# Erlang immunization stages induce exact vaccination-depth transitions on complete rooted trees

## Finding

Consider a complete rooted \(b\)-ary tree of height \(H\) with \(b\ge2\), \(H\ge2\), and a single infection source at its root at time zero. Each susceptible child acquires infection independently from its infected parent after an exponential waiting time of rate \(\lambda>0\). Exactly one initially susceptible vertex receives a vaccine at time zero. Vaccine efficacy begins after \(h\ge1\) consecutive independent exponential stages, each at rate \(\mu>0\), independently of infection. A successfully immunized vertex blocks infection of all of its descendants. As in the motivating one-dose objective, the reward counts descendants spared by successful immunization, excluding the vaccinated vertex itself.

Put \(q=\lambda/(\lambda+\mu)\), \(A_j=\binom{h+j-1}{j}\),
\[
 S_d(q)=\sum_{j=0}^{d-1}A_j q^j,\qquad
 N_d=\sum_{i=1}^{H-d}b^i,\qquad
 W_d=N_d(1-q)^h S_d(q)\quad(1\le d\le H-1).
\]
All vertices at a common depth have the same expected reward \(W_d\); the root and leaves have zero reward.

**General classification.** The positive sequence \((W_d)_{1\le d\le H-1}\) is strictly log-concave wherever it has three terms, so an optimal depth is unique or there are exactly two tied, adjacent optimal depths. For each \(1\le d\le H-2\), write \(T_d=N_d/N_{d+1}>1\). An adjacent-depth transition exists at a unique \(q_d\in(0,1)\) precisely when
\[
 T_d<1+\frac{h}{d}.
\]
In that case \(q_d\) is the unique solution of
\[
 \frac{S_{d+1}(q_d)}{S_d(q_d)}=T_d.
\]
The existing transitions form an initial segment \(d=1,\ldots,m\) and obey \(0<q_1<\cdots<q_m<1\). Away from these transition points the unique optimal depth is
\[
 1+\#\{d:1\le d\le m,\ q>q_d\}.
\]
At \(q=q_d\), precisely depths \(d\) and \(d+1\) tie for optimality. Thus progressively slower maturation relative to infection moves the unique optimal vaccination depth outward, one layer at a time.

**Sharp first-stage distinction.** For one exponential stage, \(h=1\), every optimal vertex is at depth one for all \(b,H,\lambda,\mu\). With two stages, \(h=2\), this remains true for \(b\ge3\), and for binary trees \(b=2\) with \(H\le3\). For \(b=2,h=2,H\ge4\), define
\[
 Q_H=\frac{2^{H-2}}{2^{H-1}-2}.
\]
The unique optimal depth is one for \(q<Q_H\), two for \(q>Q_H\), and depths one and two tie for \(q=Q_H\). In particular, two is the smallest maturation-stage count allowing any outward shift, and **within the two-stage class** height four is the smallest binary-tree height allowing it. Two-stage delays cannot shift the optimum outward on trees of branching number at least three.

For \(b=2,H=4,h=2,q=3/4\), the nonzero depth rewards are exactly \(W_1=7/8\), \(W_2=15/16\), \(W_3=67/128\). A depth-two vertex is therefore uniquely optimal. A single exponential maturation stage with the *same mean waiting time* still places the optimum at depth one.

## Assumptions and scope

There is one vaccine and one initially infected root. Infection is an SI process (no recovery); edge transmission times are independent exponential random variables of common rate \(\lambda\). The maturation time is Erlang with integer stage count \(h\) and stage rate \(\mu\), independent of transmission. If a target becomes infected first, it does not confer downstream protection; if immunity takes effect first, no descendant of the target becomes infected. The tree is finite and completely \(b\)-ary, and the target is fixed at time zero. The objective is the expected number of protected strict descendants, matching the single-target reward used in Li–Huang–Lee–Eun. No assumption of an independent incubation clock for different targets is needed because there is only one target. All statements are exact for integer \(b\ge2\), \(H\ge2\), \(h\ge1\), and arbitrary positive rates.

## Proof

**1. Exact race probability.** Infection reaches a vertex at depth \(d\) after the sum of \(d\) independent rate-\(\lambda\) exponential edge times. Its vaccine matures after \(h\) independent rate-\(\mu\) stages. Superpose the two independent Poisson event streams before either required event count is reached. Each event is an infection step with probability \(q\), or a vaccine step with probability \(1-q\). The vaccine's \(h\)-th stage is completed before the infection's \(d\)-th step precisely when the latter has accumulated some \(j\in\{0,\ldots,d-1\}\) steps. There are \(\binom{h+j-1}{j}\) possible orders of these previous events. Thus
\[
 \Pr\{\text{immunity before infection at depth }d\}
 =(1-q)^h\sum_{j=0}^{d-1}\binom{h+j-1}{j}q^j.
\]
A target at depth \(d\) has exactly \(N_d\) strict descendants; multiplying gives \(W_d\). Root vaccination cannot beat the infection already present; leaves have no strict descendants.

**2. Strict log-concavity in depth.** Set \(w_j=A_jq^j>0\). For \(h\ge1\),
\[
 \frac{w_{j+1}}{w_j}=q\frac{h+j}{j+1}
\]
is nonincreasing in \(j\). For \(d\ge2\), this implies \(w_d w_j\le w_{d-1}w_{j+1}\) for each \(0\le j\le d-2\). Summing gives \(w_dS_{d-1}\le w_{d-1}(S_d-w_0)<w_{d-1}S_d\), and hence
\[
 S_d^2-S_{d-1}S_{d+1}=w_{d-1}S_d-w_dS_{d-1}>0.
\]
Also, with \(r=H-d\) and \(C=b/(b-1)\), \(N_d=C(b^r-1)\), so for all interior three-term indices
\[
 N_d^2-N_{d-1}N_{d+1}=C^2b^{r-1}(b-1)^2>0.
\]
Products of positive log-concave sequences are log-concave, and therefore \(W_d^2>W_{d-1}W_{d+1}\). Consequently the ratios \(W_{d+1}/W_d\) strictly decrease with \(d\), and the maximizing set contains only one depth or two adjacent ones.

**3. Adjacent crossings and global optimizer.** We have
\[
 \frac{W_{d+1}}{W_d}=
 \frac{1}{T_d}\left(1+\frac{A_dq^d}{S_d(q)}\right).
\]
The parenthesized term is strictly increasing in \(q\), because
\[
 dS_d(q)-qS'_d(q)=\sum_{j=0}^{d-1}(d-j)A_jq^j>0.
\]
It tends to \(1\) as \(q\downarrow0\). By the hockey-stick identity \(S_d(1)=\binom{h+d-1}{d-1}\), and thus \(S_{d+1}(1)/S_d(1)=1+h/d\). The ratio crosses one at a unique interior parameter exactly under the stated strict inequality. Because the ratios strictly decrease in depth for any \(q\), their upper-endpoint values form an initial segment of values above one, and their crossing parameters are strictly ordered. The optimizer formula and exact adjacent ties follow directly by checking which consecutive ratios exceed one.

**4. Small maturation orders and sharp example.** Since \(N_d=bN_{d+1}+b\), every \(T_d>b\). For \(h=1\), the maximum possible \(S_{d+1}/S_d\) is \(1+1/d\le2\le b<T_d\), so no deeper level wins. With \(h=2\), the maximum is \(1+2/d\). It is strictly below \(T_d\) for \(b\ge3\), and also for \(b=2,d\ge2\). Thus only the first comparison can change for binary trees. When \(H=3\), \(T_1=3\), so the potential equality occurs only at excluded \(q=1\); when \(H=2\), there is no second positive-reward depth. For \(H\ge4\), solving \((1+2q)=N_1/N_2\) gives \(q=Q_H\in(0,1)\); the preceding classifications prove its sharpness.

For the exact witness \((b,H,h,q)=(2,4,2,3/4)\), \(N_1=14,N_2=6,N_3=2\), and \((1-q)^h=1/16\); insertion into the exact formula gives \((7/8,15/16,67/128)\). To match the two-stage mean \(2/\mu\) with a one-stage exponential vaccine, take rate \(\mu/2\). With \(\lambda=3\mu\), the one-stage infection-event probability is \(6/7\), but the universal \(h=1\) theorem still selects depth one.

## Verification

The companion standalone `verify.py` implements both the negative-binomial race formula and an independent event-by-event dynamic recursion using exact rational arithmetic. It checks \(1{,}920\) combinations \(b=2,3,4,5\), \(2\le H\le11\), \(1\le h\le8\), and \(q\in\{1/10,1/3,1/2,2/3,3/4,9/10\}\). Every check passed, including strict log-concavity, the one-stage universal claim, all two-stage small-branching cases, and the exact threshold witness. These finite checks are reproducibility checks; the arbitrary-parameter statements follow from the preceding proof, not from exhaustive numerical sampling. Run with `python3 verify.py` in a Python standard-library environment.

## Relationship to prior work

Li, Huang, Lee, and Eun (2023) establish the tree SI vaccination model, its general expected-descendant-reward formula, submodularity, and a greedy approximation algorithm. Their formula already supplies the individual rewards \(N_d\Pr(\tau<Z_d)\); the present finding does not claim that formula as new. Their full accessible preprint develops numerical experiments on random trees with exponentially distributed maturation time, but does not give this complete \(b\)-ary-tree analytic optimization classification, the Erlang-stage transition thresholds, or the sharp two-stage minimality result. The contribution is the structural log-concavity and ordered depth-switching theorem, including the contrast between one- and two-stage maturation at equal mean time.

DeLegge, Hunzinger, Khatri, and Munir (2015) motivate multistage vaccination within a compartmental epidemic model; this is different from one-node optimal targeting in a finite rooted tree. Nguyen and Carlson (2016) study delayed vaccine deployment in a coupled-city stochastic SIR allocation setting. Related published observations about delay distributions and vaccination success do not imply the ordering of tree-depth reward ratios. The literature comparison is finite rather than a guarantee of first discovery.

## Limitations

The objective deliberately counts protected *strict descendants*, not the vaccinated individual. Including the vaccinated individual in the reward changes the finite tree-height thresholds. The result applies to one initially infected root, one target selected at time zero, homogeneous exponential edge transmission, complete rooted trees, and independent Erlang maturation. It does not establish optimal allocation for multiple vaccines, arbitrary tree shape, cycles, recovery, adverse events, or stage-dependent maturation rates. Physical relevance of a stage-rate parameterization depends on how vaccination delays are modeled. The method gives mathematically exact phases within the specified idealized model and does not itself estimate parameters or real-world effectiveness.

## References

1. S. Li, X. Huang, C.-H. Lee, and D. Y. Eun, *Controlling Epidemic Spread Under Immunization Delay Constraints*, IFIP Networking (presentation scheduled June 14, 2023), DOI: 10.23919/IFIPNetworking57963.2023.10186397; full preprint arXiv:2307.06889 (publicly dated July 13, 2023), https://arxiv.org/abs/2307.06889 .
2. IFIP Networking 2023, official program, Session 8: Resource Management, June 14, 2023, https://networking.ifip.org/2023/index.php/program.html .
3. A. DeLegge, K. Hunzinger, R. Khatri, and K. Munir, *An epidemic model with a multistage vaccine*, Bulletin of Mathematical Biology **77** (2015), 499–513, DOI: 10.1007/s11538-015-0069-5 .
4. C. Nguyen and J. M. Carlson, *Optimizing real time vaccine allocation in a stochastic SIR model*, PLOS ONE **11** (2016), e0152950, DOI: 10.1371/journal.pone.0152950 .
