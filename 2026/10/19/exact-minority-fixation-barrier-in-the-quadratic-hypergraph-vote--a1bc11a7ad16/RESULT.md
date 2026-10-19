# Exact minority-fixation barrier in the quadratic hypergraph voter model

## Finding

A two-opinion, quadratic social-impact process on the complete \(d\)-hypergraph has an exact finite-population fixation law. For \(N\ge3\) agents and \(2\le d\le N-1\), let \(p_{N,d}(k)\) be the probability of eventually reaching all-positive consensus, starting with \(k\) positive agents. Define
\[
c=\frac{N-1-d}{d-1},\qquad
w_j=\frac{\Gamma(N+c)\Gamma(c+1)}{\Gamma(N+c-j)\Gamma(c+j+1)},
\quad j=0,\ldots,N-1.
\]
Then, exactly,
\[
\boxed{p_{N,d}(k)=\frac{\sum_{j=0}^{k-1}w_j}{\sum_{j=0}^{N-1}w_j}},\qquad 0\le k\le N,
\]
with empty numerator zero. The weights obey \(w_j=w_{N-1-j}\). At each fixed \(N\ge3\), the fixation chance from one positive agent strictly decreases as \(d\) increases; its values range from \(1/N\) at \(d=1\) to \(2^{-(N-1)}\) at \(d=N-1\).

There is a sharp rare-minority asymptotic with a *non-Gaussian* exponential rate. Fix an integer \(d\ge2\) and an integer \(k\ge1\), then let \(N\to\infty\) through \(N\ge d+1,k+1\). Put
\[
a=\frac1{d-1},\quad b=1+2a,\quad
I_d=(1+a)\log(1+a)+a\log a-(1+2a)\log(a+\tfrac12),
\]
\[
C_d=\frac{(1+a)^{b+1/2}a^{b-1/2}}
{\sqrt\pi\,(a+1/2)^{2b+1/2}}.
\]
Then
\[
\boxed{
p_{N,d}(k)=\frac{d^k-1}{d-1}\,C_d N^{-1/2}e^{-NI_d}
\bigl(1+O_{d,k}(N^{-1})\bigr).
}
\]
The rate \(I_d\) grows strictly with \(d\), begins at \(I_2=\log(32/27)\), and tends to \(\log2\) as \(d\to\infty\) *after* the fixed-\(d\), large-\(N\) limit. Moreover,
\[
\boxed{I_d>\frac{d-1}{2(d+1)}}\quad\text{for every finite }d\ge2.
\]
The right-hand side is the exponent obtained by extrapolating the standard Gaussian diffusion exit-probability formula into the one-agent boundary layer; the inequality establishes an exponentially large mismatch there. It does not dispute the accuracy of that Gaussian approximation near the balanced-opinion center.

## Assumptions and scope

There are \(N\ge3\) labeled agents, each carrying \(+\) or \(-\). The complete \(d\)-hypergraph has every possible group of \(d+1\) *distinct* agents. At each independent update, choose one focal agent uniformly and choose uniformly one group containing it, equivalently choosing \(d\) distinct other agents without replacement. If \(J\) of those \(d\) agents disagree with the focal opinion, the focal agent flips with probability \((J/d)^2\). Otherwise the state stays fixed. There are no spontaneous mutations, zealots, external biases, state-dependent group choices, or simultaneous updates. The states with zero or \(N\) positive opinions are absorbing. For \(d=1\), the rule is the ordinary neutral voter rule, treated separately; all formulas involving \(a,b,I_d,C_d\) require \(d\ge2\). This is a finite-population homogeneous mixing result, not a claim about an arbitrary sparse fixed hypergraph.

## Proof

**1. Exact one-step transitions.** Write \(K\) for the number of positive agents. For a negative focal agent at \(K=i\), the number \(J\) of positive agents among \(d\) distinct sampled neighbors has the hypergeometric law with \(i\) positive and \(N-1-i\) negative candidates. Its factorial moments are
\[
\mathbb E J=\frac{di}{N-1},\qquad
\mathbb E[J(J-1)]=\frac{d(d-1)i(i-1)}{(N-1)(N-2)}.
\]
Consequently the unconditional one-step up/down probabilities are
\[
T_i^+=\frac{i(N-i)}{Nd(N-1)}
\left[1+\frac{(d-1)(i-1)}{N-2}\right],
\]
\[
T_i^-=\frac{i(N-i)}{Nd(N-1)}
\left[1+\frac{(d-1)(N-i-1)}{N-2}\right],
\qquad 1\le i\le N-1.
\]
Both are positive. Their quotient simplifies *exactly*, with no binomial approximation, to
\[
\frac{T_i^-}{T_i^+}=\frac{N+c-i}{c+i},
\qquad c=\frac{N-1-d}{d-1}\ge0.
\]
Thus the macrostate is a finite irreducible birth–death chain on its interior, with only the two absorbing endpoints and eventual absorption almost surely.

**2. Exact fixation and finite group-size ordering.** The first-step equation for \(p_i=p_{N,d}(i)\) is
\[
T_i^+(p_{i+1}-p_i)=T_i^-(p_i-p_{i-1}),
\quad p_0=0,\quad p_N=1.
\]
Set \(\Delta_i=p_i-p_{i-1}\). The quotient above gives \(\Delta_{j+1}=w_j\Delta_1\), with \(w_0=1\) and the stated Gamma product. Summing and imposing \(p_N=1\) proves the fixation formula. The product is unchanged by \(j\mapsto N-1-j\), proving the weight symmetry and \(p_{N,d}(N-k)=1-p_{N,d}(k)\).

For fixed \(N\), the parameter \(c\) decreases strictly as integer \(d\) increases. For each \(1\le j\le\lfloor(N-1)/2\rfloor\), every factor \((N+c-i)/(c+i)\) in \(w_j\) has a strictly negative derivative in \(c\), since \(i<N/2\). Thus each interior weight increases strictly with \(d\); symmetry covers the remaining interior weights, while \(w_0=w_{N-1}=1\). Hence \(\sum_jw_j\) increases strictly and \(p_{N,d}(1)=1/\sum_jw_j\) decreases strictly. At \(d=N-1\), \(c=0\) and \(w_j=\binom{N-1}{j}\), yielding \(2^{-(N-1)}\). At \(d=1\), there is no quadratic nonlinear effect because \(J\in\{0,1\}\); the unbiased martingale gives \(p_{N,1}(k)=k/N\).

**3. Fixed-degree asymptotic, including its prefactor.** For fixed \(d\ge2\) write \(a=1/(d-1)\) and \(b=1+2a\). The parameter in the Gamma product is exactly \(c=aN-b\). Define on \([0,1]\)
\[
S(x)=(1+a)\log(1+a)+a\log a
-(1+a-x)\log(1+a-x)-(a+x)\log(a+x),
\]
\[
h(x)=\left(\frac{1+a-x}{1+a}\right)^{b+1/2}
\left(\frac{a+x}{a}\right)^{b-1/2}.
\]
Stirling's expansion applied to the four Gamma factors, uniformly for \(j/N\in[0,1]\) when \(N\) is sufficiently large at fixed \(d\), gives
\[
w_j=h(j/N)e^{NS(j/N)}\bigl(1+O_d(N^{-1})\bigr).
\]
Here \(S'(x)=\log[(1+a-x)/(a+x)]\) and \(S''(x)<0\) throughout \([0,1]\). Therefore \(S\) has a unique maximum at \(x=1/2\), with \(S(1/2)=I_d\) and \(S''(1/2)=-2/(a+1/2)\). The discrete Laplace estimate, with exponentially negligible tails and the ordinary analytic saddle expansion, yields
\[
\sum_{j=0}^{N-1}w_j
=h(1/2)e^{NI_d}\sqrt{\pi N(a+1/2)}\bigl(1+O_d(N^{-1})\bigr).
\]
Since
\[
h(1/2)=\frac{(a+1/2)^{2b}}{(1+a)^{b+1/2}a^{b-1/2}},
\]
the reciprocal leading coefficient is precisely \(C_d\). For each fixed \(j\), the weight ratio approaches \(d\), so \(w_j=d^j(1+O_{d,j}(N^{-1}))\); summing the first \(k\) terms proves the asserted asymptotic for every fixed \(k\ge1\).

**4. Non-Gaussian barrier and its strict separation.** Set \(A=1+2a=(d+1)/(d-1)>1\). Substituting \(z=1-2x\) in \(I_d=\int_0^{1/2}S'(x)\,dx\) gives
\[
I_d=\int_0^1\operatorname{artanh}\!\left(\frac zA\right)\,dz.
\]
The strict inequality \(\operatorname{artanh}(u)>u\) for \(0<u<1\) shows \(I_d>1/(2A)=(d-1)/(2(d+1))\). Increasing \(d\) strictly decreases \(A\), hence strictly increases the integral. Evaluation at \(d=2\) gives \(\log(32/27)\), while monotone convergence as \(A\downarrow1\) gives \(\int_0^1\operatorname{artanh}z\,dz=\log2\).

The earlier Gaussian approximation has kernel proportional to \(\exp[-2N(d-1)(x-1/2)^2/(d+1)]\). For fixed \(k\), integrating this kernel over \(0\le x\le k/N\) and normalizing over \([0,1]\) yields a positive \(d,k\)-dependent constant times \(N^{-1/2}e^{-N(d-1)/(2(d+1))}\). Comparison with the exact asymptotic therefore gives
\[
\lim_{N\to\infty}\frac1N\log\frac{p_{N,d}(k)}{p_{N,d}^{\mathrm{Gauss}}(k)}
=-\left(I_d-\frac{d-1}{2(d+1)}\right)<0.
\]
This comparison is specifically to the *extrapolation* of the Gaussian formula beyond its natural central transition window.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic to enumerate every possible hypergeometric sample at each interior state for \(3\le N\le12\) and \(2\le d\le N-1\), independent of the closed-form rates. It checks the transition-ratio identity, all harmonic first-step equations, boundary symmetry, and strict decrease of one-positive-agent fixation with group size. The run completed 440 exact finite-state checks. It also compared the log-Gamma evaluation of the exact one-positive-agent probability with the Laplace asymptotic at \(N=300,1000\) and \(d=2,3,5,11\), performing 8 supplemental numeric checks; those latter checks are not proofs of the asymptotic statement. The global statements follow from the algebraic and Laplace arguments above.

## Relationship to prior work

Llabrés, Toral, San Miguel, and Vázquez (2026) define the same complete-\(d\)-hypergraph microscopic update law and give the *hypergeometric* single-update rates (their Eq. 24), but focus on microscopic reduction to weighted pairwise dynamics, macroscopic drift, and fixation time rather than a closed finite-\(N\) minority-fixation law. Their mean-field Eq. 33 already gives the quadratic drift factor \(1-1/d\); this is not new here.

Kim, Lee, Min, Porter, San Miguel, and Goh (2025) examine group-driven voter consensus and explicitly derive a Gaussian error-function approximation for the exit probability using a second-order diffusion expansion (their Appendix B and supplemental Eq. S20). This work does not claim to invalidate that central-region result. Its addition is an exact rare-minority law with an independently derived exponential barrier and prefactor, and the proof that the Gaussian extrapolation is exponentially nonuniform at the extreme boundary.

Kim, Lee, and Goh (2026) subsequently emphasize optimal consensus times, not this rare-minority probability. Earlier complete-graph nonlinear voter analysis by Castellano, Muñoz, and Pastor-Satorras (2009) uses a related backward Fokker–Planck approach, but not the finite distinct-neighbor groups and fixed-\(d\) boundary-layer asymptotic here. Doniec and collaborators (2025) consider a biased, unanimity-driven generalized \(q\)-voter model on a complete graph; their finite-state Markov calculations do not state the hypergeometric quadratic-impact barrier above. The general birth–death hitting-probability method and Stirling/Laplace principles are standard and are not claimed as new.

## Limitations

The exact law assumes the complete homogeneous hypergraph and without-replacement sampling; different sparse-network correlations, selection with replacement, other social-impact exponents, external biases, and finite-time consensus statistics are not covered. The large-population expansion is **fixed \(d\)** and fixed initial count \(k\), and is not uniform for \(d\) or \(k\) growing with \(N\). It should not be substituted for the fully connected \(d=N-1\) limit, which has an exact different prefactor. The originality assessment compares the inspected primary works, not every possible WKB or special-function theorem; a prior general birth–death large-deviation result may subsume the asymptotic after specialization.

## References

1. J. Llabrés, R. Toral, M. San Miguel, F. Vázquez, *Reducibility of higher-order to pairwise interactions: Social impact models on hypergraphs*, arXiv:2601.05169 (first posted 2026-01-08), especially Sections IV–V and Appendices D–E. https://arxiv.org/html/2601.05169
2. J. Kim, D.-S. Lee, B. Min, M. A. Porter, M. San Miguel, K.-I. Goh, *Competition between group interactions and nonlinearity in voter dynamics on hypergraphs*, Phys. Rev. E **111**, L052301 (2025), especially Appendix B and supplemental Section S2.B. https://www.math.ucla.edu/~mason/papers/Kim-etal-PRE2025.pdf
3. J. Kim, D.-S. Lee, K.-I. Goh, *Optimality in group-driven social dynamics on hypergraphs*, arXiv:2604.17689 (2026), Sections 1.2 and 3. https://arxiv.org/abs/2604.17689
4. C. Castellano, M. A. Muñoz, R. Pastor-Satorras, *The non-linear q-voter model*, Phys. Rev. E **80**, 041129 (2009), Section III. https://arxiv.org/html/0907.1775v2
5. M. Doniec, P. Mullick, P. Sen, K. Sznajd-Weron, *Modeling biases in binary decision-making within the generalized nonlinear q-voter model*, arXiv:2502.10172 (2025), Section III.D. https://arxiv.org/pdf/2502.10172
