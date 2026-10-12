# Household matching can lower outbreak probability while strictly raising the household reproduction number

## Finding
Consider the two-type stochastic household SIR epidemic with proportionate global mixing of Ball and Critcher [1]. For every mixing parameter \(b\in[0,1]\), fix equal type frequencies and households of size two, with fraction \((1-b)/2\) of households of type \(AA\), fraction \(b\) of type \(AB\), and fraction \((1-b)/2\) of type \(BB\). Give both types a deterministic infectious period of length one, global infectivity rates \(\beta_A=1\), \(\beta_B=5\), and global susceptibility weights \(\kappa_A=\kappa_B=1\). Let the local probabilities of transmission from an initially infected member to its susceptible partner be
\[
p_{AA}=\frac{19}{20},\quad p_{BB}=\frac{1}{100},\quad
p_{AB}=\frac25,\quad p_{BA}=\frac{1}{100}.
\]
All four local contact rates are strictly positive and finite: \(\lambda_{ij}=-\log(1-p_{ij})\).

Then the household reproduction number satisfies, **for the entire matching interval**,
\[
R_*(b)=\frac72+\frac{101}{200}b>1.
\]
Nevertheless the limiting probability \(\Pi(b)\) of a major outbreak from a single uniformly selected individual is **strictly decreasing** on \([0,1]\). Specifically, the extinction probability \(q_b=1-\Pi(b)\) is the unique nontrivial root of the explicitly given offspring generating function below, and \(0<q_b<1/5\), while \(q_{b'}>q_b\) whenever \(0\le b<b'\le1\). Thus moving continuously from perfectly same-type to fully cross-type pairings makes the household reproduction number larger but makes major outbreaks less likely, with individual type proportions and all biological rates held fixed. Moreover, the strict reversal throughout the matching interval persists under sufficiently small independent perturbations of all six positive biological parameters (the two global rates and four local contact probabilities), keeping the infectious periods and susceptibility weights fixed.

## Assumptions and scope
For each \(b\), consider a sequence of closed, finite populations with the household-category fractions converging to the stated values and total households tending to infinity. Initially exactly one uniformly selected individual is infected. A type-\(i\) infective makes independent global Poisson contacts with each particular individual at rate \(\beta_i/N\), and independent local Poisson contacts with its household partner at rate \(\lambda_{ij}\), during an infectious interval of length one. Contacts with already infected individuals have no effect. The limiting event of a major outbreak is infection of at least \(\log m\) households in a population of \(m\) households, as in [1, Supplement, Theorem 9.1]. The claim concerns this large-population limit, not arbitrary finite-population monotonicity or final epidemic size conditional on takeoff.

## Proof
**1. Household offspring law.** The proportionate global mixing choice \(\kappa_A=\kappa_B=1\) means that each global contact samples the two individual types with probability \(1/2\) each. Given type \(i\), the index case belongs to a same-type household with probability \(1-b\), and a mixed-type household with probability \(b\). A type-\(i\) index with a type-\(j\) partner infects that partner locally with probability \(p_{ij}=1-\exp(-\lambda_{ij})\). Since infectious periods are deterministically one, the number of global contacts produced by the household, conditional on whether the partner becomes infected, is Poisson with mean \(\beta_i\) or \(\beta_i+\beta_j\). Thus for \(u=\exp(s-1)\), \(0\le s\le1\), the four conditional probability generating functions are
\[
G_{AA}(s)=\tfrac1{20}u+\tfrac{19}{20}u^2,\qquad
G_{BB}(s)=\tfrac{99}{100}u^5+\tfrac1{100}u^{10},
\]
\[
G_{AB,A}(s)=\tfrac35u+\tfrac25u^6,\qquad
G_{AB,B}(s)=\tfrac{99}{100}u^5+\tfrac1{100}u^6.
\]
Averaging over the type and household composition of the index case gives \(F_b=(1-b)F_0+bF_1\), where
\[
F_0(s)=\frac1{40}u+\frac{19}{40}u^2+\frac{99}{200}u^5+\frac1{200}u^{10},
\]
\[
F_1(s)=\frac3{10}u+\frac{99}{200}u^5+\frac{41}{200}u^6.
\]
Here the descendant households have exactly the same law as the initial household, because the global contact target is selected independently and uniformly and \(\kappa_A=\kappa_B=1\). Hence \(F_b\) is the single-type Galton–Watson household offspring generating function of [1, Sections 4.1 and 4.4], including its ancestor.

**2. Strictly increasing reproduction number.** Differentiating at \(s=1\), or taking the mean of each Poisson mixture, gives
\[
F_0'(1)=\frac72,\qquad F_1'(1)=\frac{801}{200},
\qquad F_b'(1)=\frac72+\frac{101}{200}b.
\]
The process is uniformly supercritical. As \(F_b(0)>0\), its extinction probability is the unique solution \(q_b\in(0,1)\) distinct from the trivial solution \(1\) of \(F_b(s)=s\).

**3. Uniform rational enclosure of all extinction roots.** For \(0\le s\le1/5\),
\[
u=\exp(s-1)\le \exp(-4/5)<1/2.
\]
The last inequality follows, without numerical approximations, from \(\exp(4/5)>1+4/5+(4/5)^2/2=53/25>2\). The coefficient polynomials have nonnegative terms, so at \(s=1/5\)
\[
F_0(1/5)<\frac{30049}{204800}<\frac15,
\qquad F_1(1/5)<\frac{2159}{12800}<\frac15.
\]
Consequently \(F_b(1/5)<1/5\) for every \(b\in[0,1]\), whereas \(F_b(0)>0\); the nontrivial fixed point satisfies \(0<q_b<1/5\).

**4. Strict reversal over the complete matching interval.** An exact subtraction yields
\[
F_1(s)-F_0(s)=\frac{u}{200}\bigl(55-95u+41u^5-u^9\bigr).
\]
For \(0\le s\le1/5\), the bracket is bounded below by
\[
55-\frac{95}{2}-\frac1{512}=\frac{3839}{512}>0.
\]
Thus \(F_{b'}(s)>F_b(s)\) for all \(s\in[0,1/5]\) whenever \(b'>b\). At \(s=q_b\), this yields \(F_{b'}(q_b)>q_b\), whereas \(F_{b'}(1/5)<1/5\). By continuity and uniqueness of the nontrivial fixed point, \(q_{b'}\in(q_b,1/5)\). Therefore \(q_b\) is strictly increasing and \(\Pi(b)=1-q_b\) is strictly decreasing. The large-population outbreak interpretation follows from [1, Supplement, Theorem 9.1]. Since the inequality \(F_1(s)-F_0(s)>0\) holds uniformly on the compact interval \([0,1/5]\), the mean-slope difference is strictly positive, and both upper root brackets have strictly positive margins, continuity in all six rate/probability parameters proves persistence of the entire ordering under sufficiently small simultaneous perturbations. Positive, finite contact rates remain positive and finite in such a neighborhood.

## Verification
The accompanying standalone Python script `verify.py` uses exact rational arithmetic to reconstruct the household mixture coefficients, the offspring means, the two rational upper bounds at \(u=1/2\), the uniform positive lower bound on the difference polynomial, and the elementary exponential lower bound. It also prints illustrative (non-certifying) numerical extinction roots for three parameter values. Run with `python3 verify.py` in the same directory; the exact checks print `VERIFY_OK`. No simulation is used to infer the infinite-population assertion.

## Relationship to prior work
Ball and Critcher [1] establish the household branching-process reduction and the reproduction-number and extinction-probability formulas for general proportionately mixed multitype households. Their main text and supplementary proof support the large-population interpretation. They do **not** give the above fixed-marginal, three-composition pairing family, exact offspring polynomials, or all-parameter strict reverse ordering. The qualitative warning that a household reproduction number may mis-rank epidemics is already explicit in [1], citing Ball, Sirl and Trapman [2]. A later book discussion of [2, Figure 7] records a network-clustering example in which takeoff probability falls while the household reproduction number initially rises; that qualitative phenomenon is not new here. The distinct contribution is an exact strict reversal for **every** household-pair matching parameter under a fixed individual-type composition, within the explicitly proportionate-global-mixing two-type model and with finite local rates. Nishiura, Cook and Cowling [3] examine extinction under preferred *global type mixing*, rather than fixed-proportion household matching. Ball, Britton and Neal [4] prove takeoff monotonicity when local contacts are replaced by global contacts in a single-type model; that perturbation is different from the household-composition perturbation here.

## Limitations
This is a specific parameter family and a strictly asymptotic takeoff-probability comparison, not a universal theorem for arbitrary local transmission matrices or a comparison of the conditional final size. The existence and monotonicity of \(q_b\) use standard branching-process results from [1]. The qualitative separation between reproduction-number ranking and outbreak risk predates this finding; only the exact fixed-marginal all-matching-parameter claim is put forward here. The full text of [2] was not obtained during this comparison; its Figure 7 is described in [1] and in a secondary mathematical-epidemiology text, and any unexamined special case remains a literature-overlap risk. No independent assessment has been performed.

## References
[1] F. Ball and L. Critcher, *Multitype SIR epidemics among a population partitioned into households with proportionate global mixing*, Journal of Mathematical Biology 92 (2026), 77, doi:10.1007/s00285-026-02359-5. Full text: https://link.springer.com/article/10.1007/s00285-026-02359-5; electronic supplement: https://media.springernature.com/original/springer-static/esm/art:10.1007%2Fs00285-026-02359-5/MediaObjects/285_2026_2359_MOESM1_ESM.pdf.

[2] F. Ball, D. Sirl and P. Trapman, *Analysis of a stochastic SIR epidemic on a random network incorporating household structure*, Mathematical Biosciences 224 (2010), 53–73, doi:10.1016/j.mbs.2009.12.003.

[3] H. Nishiura, A. R. Cook and B. J. Cowling, *Assortativity and the Probability of Epidemic Extinction: A Case Study of Pandemic Influenza A (H1N1-2009)*, Interdisciplinary Perspectives on Infectious Diseases 2011, 194507, doi:10.1155/2011/194507; https://onlinelibrary.wiley.com/doi/10.1155/2011/194507.

[4] F. Ball, T. Britton and P. Neal, *Household epidemic models revisited*, arXiv:2505.17890v1, 2025; https://arxiv.org/pdf/2505.17890.

[5] T. Britton and E. Pardoux (eds.), *Stochastic Epidemic Models with Inference*, Lecture Notes in Mathematics 2255, Springer (2019), doi:10.1007/978-3-030-30900-8. Its discussion of [2, Fig. 7] explicitly distinguishes reproduction-number ranking from takeoff probability under network clustering.
