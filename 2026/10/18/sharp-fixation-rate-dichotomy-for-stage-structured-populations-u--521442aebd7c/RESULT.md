# Sharp fixation-rate dichotomy for stage-structured populations under periodic selection pulses

## Finding

Periodic genotype-dependent mortality in an irreducible stage-structured population has two sharply different asymptotic resistance-fixation laws. With some selective pressure against heterozygotes, the residual susceptible-allele frequency decreases at an exact exponential rate determined by a ratio of Perron roots. When heterozygotes are as pulse-resistant as resistant homozygotes at every stage where selection occurs, fixation is algebraic with a universal, explicitly weighted coefficient:

\[
\lim_{k\to\infty} k\,[1-y_i(k\tau^+)]=\left(\sum_{j=1}^{n}s_j\pi_j\right)^{-1},\qquad \pi_j=\frac{w_jv_j}{w^\top v}.
\]

Here \(v,w\) are the positive right and left Perron eigenvectors of the fully resistant pulse matrix, and the same limit holds for every stage \(i\). The coefficient is independent of initial allele frequencies and of whether total population density grows or decays.

## Assumptions and scope

Fix an integer \(n\ge2\), an irreducible Metzler matrix \(A\in\mathbb R^{n\times n}\), a period \(\tau>0\), and set \(E=e^{\tau A}\); every entry of \(E\) is strictly positive. At each pulse, genotype survival probabilities at stage \(i\) are

\[
\delta_i^{22}=d_i,\qquad \delta_i^{12}=d_i(1-s_ih_i),\qquad
\delta_i^{11}=d_i(1-s_i),
\]

where \(0<d_i\le1\), \(0\le s_i,h_i\le1\), \(1-s_ih_i>0\), and at least one \(s_i>0\). Between pulses, stage densities satisfy the same linear equation \(\dot x=Ax\) for all alleles and their frequencies evolve by demographic inflow, as in the source's Hardy–Weinberg pulse model. Stage-dependent parameters include the source's common-dominance subfamily. Assume strictly positive initial stage densities and that both allele types occur in at least one stage initially. Write \(y_i(k\tau^+)\) for the resistant-allele frequency immediately after the \(k\)-th pulse, with the initial postpulse state indexed by \(k=0\).

Define \(P=\operatorname{diag}(d_i)E\), \(Q=\operatorname{diag}(d_i(1-s_ih_i))E\), and let \(\rho\) denote spectral radius. Then the two complementary conclusions are:

**Heterozygote-selective regime.** If \(s_ih_i>0\) for at least one stage, \(0<\rho(Q)<\rho(P)\), and for every stage \(i\),

\[
\lim_{k\to\infty}\frac{1}{k}\log[1-y_i(k\tau^+)]=\log\frac{\rho(Q)}{\rho(P)}<0.
\]

**Fully dominant resistance at selected stages.** If \(s_ih_i=0\) for every stage, let \(Pv=\rho(P)v\), \(w^\top P=\rho(P)w^\top\), with \(v,w>0\) and \(w^\top v=1\). Set \(\sigma=\sum_i s_iw_iv_i>0\). For every stage \(i\),

\[
\lim_{k\to\infty}k\,[1-y_i(k\tau^+)]=\sigma^{-1}.
\]

Both limits apply to any initial condition meeting the stated mixed-allele assumption; these are stroboscopic limits after pulses. The second result does not assume \(\rho(P)>1\).

## Proof

**1. Positive allele-mass coordinates.** Put \(R_i=x_iy_i\), \(S_i=x_i(1-y_i)\). Between pulses, direct differentiation of the demographic allele-frequency equations gives \(\dot R=AR\) and \(\dot S=AS\). At a pulse, Hardy–Weinberg genotype weights give resistant and susceptible allele survival factors, respectively,

\[
 d_i\frac{1+(1-s_ih_i)r_i}{1+r_i},\qquad
 d_i\frac{(1-s_ih_i)+(1-s_i)r_i}{1+r_i},\quad r_i=S_i/R_i.
\]

After the first complete period both allele vectors are strictly positive by \(E>0\) and \(1-s_ih_i>0\). Reindex after that period if necessary; a finite shift does not change either asserted limit.

For positive postpulse ratios \(r_{k,i}=S_{k,i}/R_{k,i}\), define the pre-pulse ratios \(\widehat r_{k,i}=(ES_k)_i/(ER_k)_i\). The exact ratio recurrence is

\[
 \widehat r_{k,i}=\sum_j B^{(k)}_{ij}r_{k,j},\quad
 B^{(k)}_{ij}=\frac{E_{ij}R_{k,j}}{(ER_k)_i},\quad
 r_{k+1,i}=f_i(\widehat r_{k,i}),
\]
\[
 f_i(u)=u\frac{(1-s_ih_i)+(1-s_i)u}{1+(1-s_ih_i)u},\qquad
 u-f_i(u)=\frac{s_iu[h_i+(1-h_i)u]}{1+(1-s_ih_i)u}.
\]

All rows of \(B^{(k)}\) are stochastic and \(0\le f_i(u)\le u\). To obtain *uniform* mixing, observe that the resistant mass satisfies \(R_{k+1,i}=\delta^m_{k,i}(ER_k)_i\), with \(d_i(1-s_ih_i)\le\delta^m_{k,i}\le d_i\). Since all entries of \(E\) are positive, each component \(R_{k+1,i}/\sum_jR_{k+1,j}\) is bounded below by a positive constant depending only on the fixed matrices. Consequently there is a \(\beta>0\) such that \(B^{(k)}_{ij}\ge\beta\) for all sufficiently large \(k\) and every \(i,j\).

**2. Uniform fixation.** Let \(M_k=\max_i r_{k,i}\), nonincreasing by the recurrence. Suppose \(M_k\to L>0\). Choose any stage \(a\) with \(s_a>0\). Every sufficiently late \(\widehat r_{k,a}\) is at least \(\beta M_k\ge\beta L/2\). The displayed strict-drop identity then supplies \(\varepsilon>0\) with \(r_{k+1,a}\le M_k-\varepsilon\). In the next mixing step, every stage puts weight at least \(\beta\) on stage \(a\), and hence \(M_{k+2}\le M_k-\beta\varepsilon\), contradicting convergence of \(M_k\). Thus \(M_k\to0\), and therefore \(y_i(k\tau^+)\to1\) at all stages.

**3. Exact exponential exponent.** When \(s_ah_a>0\) for some \(a\), the exact allele-mass recurrences of Step 1 read \(R_{k+1}=D^m_kER_k\) and \(S_{k+1}=D^s_kES_k\), with \(D^m_k\to\operatorname{diag}(d_i)\), \(D^s_k\to\operatorname{diag}(d_i(1-s_ih_i))\) entrywise by Step 2. For each \(\epsilon>0\), eventually

\[
 (1-\epsilon)PR_k\le R_{k+1}\le(1+\epsilon)PR_k,\qquad
 (1-\epsilon)QS_k\le S_{k+1}\le(1+\epsilon)QS_k
\]

componentwise. Comparison with powers of the strictly positive matrices \(P,Q\), followed by the Perron–Frobenius theorem and \(\epsilon\downarrow0\), gives \(k^{-1}\log R_{k,i}\to\log\rho(P)\) and \(k^{-1}\log S_{k,i}\to\log\rho(Q)\). Strict comparison \(Q\le P\) with at least one strict row yields \(\rho(Q)<\rho(P)\). Since \(1-y_i=r_i/(1+r_i)\), the logarithmic conclusion follows.

**4. Exact quadratic defect under dominant resistance.** Suppose \(s_ih_i=0\) for all \(i\). Resistant mass then follows the *exact linear recurrence* \(R_{k+1}=PR_k\). Susceptible mass follows

\[
 S_{k+1,i}=(PS_k)_i- s_i\frac{(PS_k)_i^2}{(PR_k)_i+(PS_k)_i}.
\]

The Perron theorem implies \(R_k/\rho(P)^k\to c_Rv\), with \(c_R>0\), exponentially in projective coordinates. Let \(w^\top v=1\), and define

\[
 c_k=\frac{w^\top S_k}{w^\top R_k},\qquad
 \omega_{k,i}=\frac{w_i(PR_k)_i}{w^\top PR_k},\qquad
 \pi_i=w_iv_i.
\]

Then \(\sum_i\omega_{k,i}=\sum_i\pi_i=1\), \(\omega_{k,i}\to\pi_i>0\), \(c_k\in[\min_i r_{k,i},\max_i r_{k,i}]\), and the preceding recurrence gives the *exact* identity

\[
 c_k-c_{k+1}=\sum_i\omega_{k,i}s_i\frac{\widehat r_{k,i}^{\,2}}{1+\widehat r_{k,i}}.
\]

With \(m_k=\min_i r_{k,i}\), the ratio map in this case gives \(m_{k+1}\ge m_k/(1+m_k)\), so \(m_k\ge(k+C)^{-1}\) for a finite \(C>0\). Conversely, because all mixing weights are at least \(\beta\), every \(\widehat r_{k,i}\ge\beta M_k\), where \(M_k=\max_jr_{k,j}\ge c_k\). At a selected stage with positive limiting \(\omega_{k,i}\), the drift identity therefore gives \(c_k-c_{k+1}\ge\kappa c_k^2\) eventually, for some \(\kappa>0\). It follows that \(c_k=O(k^{-1})\).

For an upper bound on all stage ratios, note that \(f_i(u)=u-s_iu^2/(1+u)\ge u/(1+M_0)\) for \(0\le u\le M_0\). Consequently all \(r_{k+1,i}\ge\beta M_k/(1+M_0)\), so \(M_k\le C'c_{k+1}\le C'c_k=O(k^{-1})\).

Each \(B^{(k)}\) has every entry at least \(\beta\), so its oscillation contraction factor is at most \(\theta=1-n\beta<1\). The nonnegative pulse defects \(u-f_i(u)\le u^2\) give

\[
 M_{k+1}-m_{k+1}\le\theta(M_k-m_k)+M_k^2.
\]

Since \(M_k=O(k^{-1})\), iteration yields \(M_k-m_k=O(k^{-2})\). Thus \(r_{k,i}=c_k+O(k^{-2})\) and \(\widehat r_{k,i}=c_k+O(k^{-2})\), uniformly in \(i\). Using \(c_k\ge m_k\ge(k+C)^{-1}\) in the exact drift identity proves

\[
 \frac{c_k-c_{k+1}}{c_k^2}\longrightarrow\sum_i\pi_i s_i=\sigma>0.
\]

Hence \(c_{k+1}/c_k\to1\) and \((1/c_{k+1})-(1/c_k)\to\sigma\); averaging gives \(k c_k\to\sigma^{-1}\). Since \(r_{k,i}-c_k=O(k^{-2})\) and \(1-y_i=r_{k,i}/(1+r_{k,i})\), the asserted stagewise inverse-pulse limit follows.

## Verification

The standalone `verify.py` uses symbolic algebra to check the marginal-genotype survival transformations and the exact quadratic susceptible-mass update. It integrates a positive three-stage example with either full dominance or partial dominance, compares the observed algebraic and logarithmic limits with independently computed Perron eigenvectors and roots, and reports the reproductive-value weights for the source's rounded four-stage fly parameters. Run `python verify.py` with the libraries in `requirements.txt`.

In the three-stage dominant example, \(\sigma^{-1}=2.5096562247\ldots\) and the computed \(k(1-y_i)\) after 20,000 pulses lies between \(2.5109\) and \(2.5113\). Under heterozygote selection, the theoretical logarithmic rate is \(-0.1729922594\ldots\); numerical estimates after 1,000 pulses agree within \(0.0002\). For the source's four-stage Spinosad **susceptible-genotype** survivals \(\delta^{11}=(0.172,0.241,0.003,0.052)\), choose fully dominant resistance with \(s=1/2\) at exactly one stage and zero selection at other stages. Consistently impose \(\delta_i^{22}=\delta_i^{11}/(1-s_i)\). The predicted \(\sigma^{-1}\) values for selecting egg, larva, pupa, and adult respectively are approximately \(8.063,2.937,122.226,3.995\). These are new full-dominance examples using the source’s rounded empirical inputs, **not** its heterozygote-selection simulation (which sets \(h=1/2\)). Stage-specific pulse survival changes \(P\) and thus its reproductive-value weights: larval selection has the quickest asymptotic fixation of these four treatments, whereas pupal selection is slowest. These are diagnostics; Steps 1–4, not finite simulation, establish the asymptotic theorem.

## Relationship to prior work

D'Ovidio Long, Adjei and Patel (2026, arXiv:2609.10581v1) provide the hybrid stage-structured genotype-dependent pulse model, prove qualitative resistant-allele fixation in Theorem 5, and numerically investigate how selecting different life stages changes resistance buildup (Section 4, Figure 3). The present theorem retains their model structure and derives *sharp rates and coefficients* that their qualitative theorem and simulations do not determine. In particular, the full-dominance boundary changes the exponential scaling to a computable inverse-pulse law.

Patel and De Leenheer (2023/2024, arXiv:2310.07616v1) analyze Perron radii of fixed periodic ecological pulse matrices. That matrix theory supplies background but does not give an allele-frequency nonlinear ratio equation or the dominant-case coefficient. Reproductive-value weighting is a classical theme in class-structured allele dynamics (Taylor, 1990), and scalar slow fixation of fully dominant beneficial alleles is likewise classical. Neither general principle alone identifies the pulse-stage coefficient \(\sum_i s_iw_iv_i\) in this hybrid system. A related 2025 stage-structured anthelmintic-resistance paper was inspected only through its abstract and supporting-data descriptions; its full derivations were not accessible for direct comparison. Therefore complete historical priority is not claimed.

## Limitations

The analysis assumes deterministic, density-independent stage mixing, strict positivity of genotype-heterozygote survival factors, no genotype-dependent inter-pulse fitness costs, a fixed pulse period, at least one selected stage, and presence of both alleles initially. It gives postpulse asymptotics, not finite-time errors or establishment probabilities in stochastic populations. The theorem does not cover zero heterozygote survival at a stage, mutation, immigration, density feedback, changing pulse controls, or fixation starting from an absent resistant allele. The exact law is a rate of deterministic allele fixation, not a guarantee of ecological population persistence. The external 2025 resistance paper's incomplete full-text inspection remains a historical-priority risk.

## References

1. A. D'Ovidio Long, A. Adjei and S. Patel, *On the formulation and analysis of a stage-structured eco-evolutionary model with pulsed disturbances*, arXiv:2609.10581v1 (first public version 2026-09-05), https://arxiv.org/abs/2609.10581; especially equations (2), (7)–(10), Theorem 5 and Section 4.
2. S. Patel and P. De Leenheer, *On spectral radius properties of a key matrix in periodic impulse control*, arXiv:2310.07616v1 (2023), https://arxiv.org/abs/2310.07616.
3. P. D. Taylor, *Allele-Frequency Change in a Class-Structured Population* (1990), a foundational source for reproductive-value frequency weights (abstract inspected).
4. S. Patel, M. Lyberger, C. Vegvari and H. Gulbudak, *Eco-evolutionary dynamics of anthelmintic resistance in soil-transmitted helminths*, *Theoretical Population Biology* (2025), https://doi.org/10.1016/j.tpb.2025.03.006 (abstract and supporting-data descriptions inspected; full text not inspected).
