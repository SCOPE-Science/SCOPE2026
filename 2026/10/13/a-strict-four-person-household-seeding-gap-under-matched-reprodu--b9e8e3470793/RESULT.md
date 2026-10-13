# A strict four-person household seeding gap under matched reproduction numbers
## Finding

For the four-person standard and Greenwood household transmission rules of Ball, Martin, Neal and Sirl, with deterministic one-day infectious periods, matching the **single-seed household reproduction number** does not match the response to a simultaneous importation pulse.

For every standard-model per-pair local infection probability \(0<p<1\), there is exactly one Greenwood local infection probability \(g(p)\) giving the same expected number infected from one initial infective. Its sharp comparison window is
\[
p<g(p)<2p-p^2.
\]
If \(E^S_k(p)\) and \(E^G_k(g)\) are the expected total household sizes infected by the end of an isolated local outbreak from \(k\) simultaneous seeds, then at the matched parameter
\[
E^S_1(p)=E^G_1(g(p)),\qquad
E^S_2(p)>E^G_2(g(p)),\qquad
E^S_3(p)>E^G_3(g(p)).
\]

Consequently, if each person is independently seeded at the same instant with probability \(0<q<1\), and no additional infections arrive from outside the household, the expected final infected *fraction* under the standard rule is strictly greater:
\[
F_S(q)-F_G(q)
=\frac32 q^2(1-q)^2(E^S_2-E^G_2)
+q^3(1-q)(E^S_3-E^G_3)>0.
\]
All three expectations in the difference are evaluated at their respective matched parameters. The strict comparison holds for the full open parameter square \(0<p,q<1\), not just for a numerical sample.

## Assumptions and scope

The population consists of one closed household of exactly four individuals; no additional infections arrive from outside after the initial instant. Each infective remains infectious for exactly one day and then recovers; an infected susceptible becomes infectious on the following day. Within a day, conditional on current household state, different susceptible persons are infected independently.

Under the standard Reed–Frost rule, with \(i\ge1\) current infectives, each susceptible becomes infected with probability \(1-(1-p)^i\). Under the Greenwood rule, with \(i\ge1\) current infectives, each susceptible becomes infected with probability \(g\), independently of \(i\). These are the \(p_R=1\) cases of Sections 2.1 and 2.3 of the motivating paper, with global infection prevalence subsequently fixed at zero.

For the early-household branching-process comparison only, take the same positive mean global offspring-contact intensity \(\lambda_G\) in both models. With deterministic one-day infectious periods and one infective establishing a new household, the total expected number of global contacts from its local outbreak is \(R_*=\lambda_G E_1\). Accordingly, equality of one-seed expected totals is exactly equality of the corresponding household offspring means. The theorem applies whether the common \(R_*\) falls below or above one.

The one-time multiple-import pulse assumes \(K\sim\operatorname{Bin}(4,q)\), with independent initial statuses across residents. This pulse is distinct from continued global exposure in the full multi-household epidemic; no full-population final-size ordering is asserted.

## Proof

For \(M\in\{S,G\}\), let \(e^M(s,i)\) be the expected final number infected from a local household state with \(s\) susceptibles and \(i\) *currently* infectious persons, where all previously recovered persons are already counted only at the end via the identity below. More precisely, define \(e^M(s,i)\) to count infections among those \(s+i\) people from the current day onward, including all \(i\) already infectious. Set \(e^M(s,0)=0\) and \(e^M(0,i)=i\). If \(a_i^S=1-(1-p)^i\) and \(a_i^G=g\), then the paper's exact binomial transition rules imply
\[
e^M(s,i)=i+\sum_{j=1}^{s}\binom{s}{j}
(a_i^M)^j(1-a_i^M)^{s-j}e^M(s-j,j).
\]
Indeed, today's \(i\) cases are included, the newly infected \(j\) become tomorrow's only infectives, and after a day with \(j=0\) no further transmission occurs. Hence \(E^M_k=e^M(4-k,k)\).

Exact recursion gives the following polynomials (all algebraic identities, not interpolations):
\[
\begin{aligned}
A(x):=E^G_1(x)&=1+3x+6x^2-3x^3-15x^4+18x^5-6x^6,\\
B(x):=E^G_2(x)&=2+2x+2x^2-2x^3,\\
E^G_3(x)&=3+x,\\
E^S_1(p)&=1+3p+6p^2-21p^4+21p^5-6p^6,\\
E^S_2(p)&=2+4p+2p^2-10p^3+8p^4-2p^5,\\
E^S_3(p)&=3+1-(1-p)^3.
\end{aligned}
\]
In particular,
\[
E^S_1(p)-A(p)=3p^3(1-p)^2>0,
\qquad
E^S_2(p)-B(p)=2p(1-p)^2(1+2p-p^2)>0.
\]

We prove that \(A\) increases strictly and that the unique solution of \(A(g)=E^S_1(p)\) lies below \(u=2p-p^2\). Direct differentiation yields
\[
A'(x)=3(1-x)Q_4(x),\quad
Q_4(x)=12x^4-18x^3+2x^2+5x+1.
\]
Its degree-four Bernstein coefficients on \([0,1]\), in increasing index order, are
\[
\left(1,\frac94,\frac{23}6,\frac54,2\right),
\]
all strictly positive. Hence \(A'(x)>0\) for \(0<x<1\). Moreover,
\[
A(2p-p^2)-E^S_1(p)=3p(1-p)^3P_8(p),
\]
where
\[
P_8(x)=2x^8-18x^7+66x^6-126x^5+131x^4-67x^3+5x^2+8x+1.
\]
Its degree-eight Bernstein coefficients are
\[
\left(1,2,\frac{89}{28},\frac{187}{56},\frac{221}{70},
\frac{41}{14},\frac{75}{28},\frac{19}{8},2\right),
\]
again all strictly positive. Since \(A(p)<E^S_1(p)<A(2p-p^2)\), strict monotonicity proves existence, uniqueness, and the stated bounds \(p<g<2p-p^2\).

To compare two-seed responses, write
\[
R(x)=\frac{B'(x)}{A'(x)}
=\frac{2(3x+1)}{3Q_4(x)},
\qquad
H(x)=\frac{2(1+2x-x^2)}{3x^2}.
\]
The function \(H\) decreases strictly on \((0,1)\), because \(H'(x)=-4(1+x)/(3x^3)<0\). A direct rational identity is
\[
H(x)-R(x)=\frac{2(1-x)P_5(x)}{3x^2Q_4(x)},
\]
with
\[
P_5(x)=12x^5-30x^4-4x^3+18x^2+8x+1.
\]
The degree-five Bernstein coefficients of \(P_5\) are
\[
\left(1,\frac{13}5,6,\frac{54}5,\frac{53}5,5\right),
\]
so \(P_5(x)>0\) throughout \([0,1]\), whence \(R(x)<H(x)\) for \(0<x<1\). Since \(g>p\), it follows that
\[
\begin{aligned}
B(g)-B(p)&=\int_p^g R(x)A'(x)\,\mathrm dx\\
&<H(p)[A(g)-A(p)]\\
&=H(p)\,3p^3(1-p)^2\\
&=2p(1-p)^2(1+2p-p^2)\\
&=E^S_2(p)-B(p).
\end{aligned}
\]
Thus \(E^S_2(p)>E^G_2(g)\). For three seeds,
\[
E^S_3(p)-E^G_3(g)=1-(1-p)^3-g
>1-(1-p)^3-(2p-p^2)=p(1-p)^2>0.
\]
Finally, \(E^S_0=E^G_0=0\), \(E^S_4=E^G_4=4\), and \(E^S_1=E^G_1\) by calibration. Averaging \(E^M_K/4\) over \(K\sim\operatorname{Bin}(4,q)\) yields the stated strictly positive final infected-fraction difference, completing the proof.

## Verification

Run `python verification/check.py` in an environment with SymPy installed. The standalone checker derives the complete \(s,i\) recursions independently for both models, confirms all six final-size polynomials, the rational derivative identity, the three positive Bernstein coefficient arrays, and the exact binomial-mixture formula. It also brackets the unique matching Greenwood parameter for \(p=1/2\) between \(525741/10^6\) and \(525742/10^6\), with both two- and three-seed gaps positive at both bracket endpoints. The checker prints `VERIFY_OK` if its algebraic and exact-rational assertions succeed.

The finite parameter witness is not used as an infinite-parameter proof: the exact polynomial identities, monotonicity argument, and positive Bernstein certificates establish the result over all \(p,q\in(0,1)\).

## Relationship to prior work

Ball, Martin, Neal and Sirl give both the standard and Greenwood daily household transition probabilities (Sections 2.1 and 2.3), and the associated single-seed household branching-process reproduction number (Section 3). Their Section 6 compares the population-level final-size behavior of those models numerically, including matched reproduction-number examples, but does not state the four-person one-pulse, multiple-seed response inequality proved here.

Earlier susceptibility-set and collective Reed–Frost theory, including Ball's 2018 contribution, provides exact general final-size machinery for related epidemic processes. The novel assertion here is **not** the existence of exact finite-population recursions. It is the parameter-uniform strict ordering after the nonlinear calibration \(E^S_1(p)=E^G_1(g)\), together with uniqueness and the explicit envelope \(p<g<2p-p^2\), for a natural minimal nontrivial household size.

## Limitations

This theorem concerns one closed four-person household with a one-time simultaneous importation pulse and no later outside introductions. It does **not** imply that the standard model always has a larger final size in a globally coupled epidemic, where arrival timing and continued importations affect both dynamics. The result assumes \(p_R=1\); arbitrary geometric infectious periods require different recursions. No stochastic dominance of the *entire final-size distribution* is claimed: only the expected final infected fraction is strictly ordered. The source's global numerical comparisons are neither refuted nor certified by this theorem.

## References

1. F. Ball, N. Martin, P. Neal and D. Sirl, “Discrete-Time Household Epidemic Models,” *Methodology and Computing in Applied Probability* 28 (2026), article 21. DOI: 10.1007/s11009-026-10253-2.
2. F. Ball, “Susceptibility Sets and the Final Outcome of Collective Reed–Frost Epidemics,” *Methodology and Computing in Applied Probability* 21 (2019), 401–421; first online 2018. DOI: 10.1007/s11009-018-9631-6.
