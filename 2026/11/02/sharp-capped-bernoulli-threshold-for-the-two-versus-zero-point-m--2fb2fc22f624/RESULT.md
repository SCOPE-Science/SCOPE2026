# Sharp capped-Bernoulli threshold for the two-versus-zero point-mass reversal

## Finding
For a probability cap \(0<p\le1/2\), define the minimum mean required for the event of exactly two successes to be more likely than zero successes among independent Bernoulli trials. The exact answer is a finite staircase in the cap:
\[
T(p)=mp+\frac{1-\binom{m}{2}t^2}{mt+1-\binom{m}{2}t^2},\qquad t=\frac{p}{1-p},\quad m=\min\{j\ge1:\binom{j+1}{2}t^2\ge1\}.
\]
For every finite independent Bernoulli sum with parameters in \([0,p]\),
\[
\Pr(S=2)>\Pr(S=0)\ \Longrightarrow\ \mathbb E S>T(p).
\]
This is optimal. At the boundary, equality of the two point masses forces exactly \(m\) parameters equal to \(p\) and one residual parameter \(q=(1-\binom{m}{2}t^2)/(mt+1-\binom{m}{2}t^2)\), apart from zero parameters and permutation. The threshold decreases to \(1\) at \(p=1/2\), and approaches the Poisson value \(\sqrt2\) as \(p\downarrow0\).

## Assumptions and scope
The cap is fixed in \((0,1/2]\). The number of independent Bernoulli summands is any finite positive integer and may vary in taking the infimum. Boundary parameters zero are permitted. All probabilities are less than one, so odds and the probability of no success are well-defined. The classification concerns equality *at the least mean* \(T(p)\), not all higher-mean ties.

## Proof
Let \(x_i\in[0,p]\) be the success probabilities and \(z_i=x_i/(1-x_i)\) their odds. Expanding the probability generating polynomial yields
\[
\frac{\Pr(S=2)}{\Pr(S=0)}=e_2(z_1,\ldots,z_n)=\sum_{i<j}z_i z_j,
\qquad \Pr(S=0)=\prod_i(1-x_i)>0.
\]
We prove the following *cap-saturation lemma*: if \(e_2\ge1\) and \(0<p\le1/2\), then at fixed total mean we may successively replace pairs of interior probabilities with feasible endpoints, strictly increasing \(e_2\) until at most one interior parameter remains.

Fix two interior probabilities \(x,y\in(0,p)\), and write \(s=x+y\), \(v=xy\); hence \(0<s<2p\le1\). Let \(U\) and \(H\) be the first and second elementary symmetric sums of the odds of the other variables. Since \(x/(1-x)+y/(1-y)=(s-2v)/(1-s+v)\) and \(xy/[(1-x)(1-y)]=v/(1-s+v)\), we have
\[
e_2=H+\frac{Us+(1-2U)v}{1-s+v},\qquad
\frac{\partial e_2}{\partial v}=\frac{1-s-(2-s)U}{(1-s+v)^2}.
\]
If this derivative were nonnegative, then \(U\le(1-s)/(2-s)\). Since \(H\le U^2/2\), and both odds of the pair are at most \(s/(2-s)\) when their sum is \(s\) and their product is greatest at \(x=y=s/2\), it follows that
\[
e_2\le\frac{(1-s)^2/2+2s(1-s)+s^2}{(2-s)^2}<1.
\]
Indeed, one minus the displayed fraction is \((1-s)(7-3s)/(2(2-s)^2)>0\). This contradicts \(e_2\ge1\). Thus the derivative is strictly negative, and decreasing \(v=xy\) along the fixed-sum interval strictly increases \(e_2\). The minimum product is at a feasible endpoint, where one parameter equals zero or \(p\). As the first symmetric sum is continuous and the derivative is negative throughout the deformation, the condition \(e_2\ge1\) persists. Each operation eliminates at least one interior parameter. After finitely many steps, only the vector \((p,\ldots,p,r,0,\ldots,0)\) remains, where \(r=\mu-\lfloor\mu/p\rfloor p\in[0,p)\).

For a saturated vector with \(j\) full-cap coordinates and one residual \(r\), and \(w=r/(1-r)\), direct expansion gives
\[
e_2=\binom j2t^2+jt w.
\]
It is strictly increasing in \(r\) whenever \(j\ge1\), and continuous and strictly increasing from one cap segment to the next after at least two positive coordinates. The first crossing of one is in the segment \(j=m\) defined above: \(\binom m2t^2<1\le\binom{m+1}2t^2\). Solving \(\binom m2t^2+mtq/(1-q)=1\) gives exactly \(q=a/(mt+a)\); the inequality on binomial coefficients gives \(0<q\le p\). No configuration of smaller mean can have \(e_2\ge1\), by saturation. When \(\mu=T(p)\) the saturated configuration is the unique one with \(e_2=1\), because every nontrivial saturation step is *strict*. Hence the equality classification.

For sharpness, increase the residual coordinate slightly if \(q<p\); if \(q=p\), add a small new Bernoulli coordinate. This makes \(e_2>1\) and increases the mean by an arbitrarily small amount. Finally, the minimality condition implies \(m t\to\sqrt2\) as \(t\downarrow0\), and \(0<q\le p\); thus \(T(p)=mp+q\to\sqrt2\). Direct substitution gives \(T(1/2)=1\).

## Verification
The bundled standalone `odds_cap_check.py` performs 13,122 exact-rational checks on six caps and all vectors of length at most six on three-point parameter grids. It also checks the proposed equality families and existence of strict reversal above the threshold. The computer checks are finite corroboration; the preceding cap-saturation argument establishes the result for arbitrary finite lengths and real parameters. Running `python odds_cap_check.py` reproduces the bundled `odds_cap_check.txt` output.

## Relationship to prior work
Kleiner (2026), *Why Distance Two Is Exceptional for Poisson–Binomial Point Probabilities*, proves the unrestricted-parameter reversal threshold for general point-mass gaps. For the pair \(0,2\) the unrestricted threshold is one, and there are many boundary ties when individual parameters are unrestricted. Here a new upper constraint on each Bernoulli parameter makes the sharp threshold greater than one except at cap \(1/2\), and creates an explicit cap-dependent unique extremal probability vector. Kleiner's shifted-binomial extremal reduction does not provide this saturated-cap extremizer. Classical Poisson-binomial generating-function identities are used without novelty claims. The Poisson limiting threshold is familiar; the finite-cap formula, rigidity, and paired-odds mechanism are the assessed contribution.

## Limitations
The result compares only the zero-success and two-success atoms; it does not solve the cap-constrained problem for arbitrary indices. It assumes independence and a cap no greater than one half. No claim is made about independent historical priority beyond the inspected literature and mathematical-record search. The exact formula is sensitive to which side of a discrete cap breakpoint is used.

## References
1. Igor Kleiner, *Why Distance Two Is Exceptional for Poisson–Binomial Point Probabilities*, arXiv:2610.10664v1, first posted 2026-10-07, https://arxiv.org/html/2610.10664v1 (full primary text inspected).
2. Wenpin Tang and Fengmin Tang, *The Poisson Binomial Distribution—Old & New*, Statistical Science 38 (2023), doi:10.1214/22-STS852 (background survey; only bibliographic/overview material consulted).
