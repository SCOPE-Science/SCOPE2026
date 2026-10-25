# A parity reversal in complete-graph monomer–dimer precision

## Finding
For every integer \(n\geq4\) and activity \(t>0\), give each matching \(M\) of the complete graph \(K_n\) probability proportional to \(t^{|M|}\). Let \(X_e\) indicate the presence of edge \(e\), let \(\Sigma=\operatorname{Cov}((X_e)_e)\), and set \(Q=\Sigma^{-1}\). For any vertex-disjoint edges \(e,f\), the number \(q_n(t)=Q_{ef}\) is independent of their choice. The covariance matrix is positive definite, and
\[
\lim_{t\downarrow0}\frac{q_n(t)}{t^2}=-2,\qquad
\lim_{t\to\infty}\frac{q_n(t)}t=
\begin{cases}-2/(n-2),&n\text{ even},\\ 6/(n-1),&n\text{ odd}.\end{cases}
\]
In particular, for every odd \(n\geq5\), at least one finite positive activity changes the sign of the full-order linear partial correlation of two vertex-disjoint edge indicators: it is positive at low activity and negative at high activity. No uniqueness of the crossing is asserted. For even \(n\), that partial correlation is positive at sufficiently small and sufficiently large activity, without a claim about intermediate activities.

## Assumptions and scope
A matching is a set of pairwise vertex-disjoint unoriented edges, including the empty set. The exact partition polynomial is
\[
Z_n(t)=\sum_{k=0}^{\lfloor n/2\rfloor}\frac{n!}{(n-2k)!\,2^k k!}t^k,
\quad Z_0=Z_1=1,
\quad Z_n=Z_{n-1}+(n-1)tZ_{n-2}.
\]
Here all limits in activity hold with \(n\) fixed, and \(t>0\). A full-order *linear* partial correlation means \(-Q_{ef}/\sqrt{Q_{ee}Q_{ff}}\), not a nonlinear conditional correlation or conditional independence. Let
\[
p=\frac{tZ_{n-2}}{Z_n},\quad s=\frac{t^2Z_{n-4}}{Z_n},\quad H=\binom n2,\quad D=\binom{n-2}2.
\]
The first quantity is a single-edge occupancy probability, and the second is a probability for two disjoint specified edges.

## Proof
**1. Exact covariance and invariant spaces.** Two distinct incident edges cannot both occur; two disjoint edges occur together with probability \(s\). Let \(A_1\) be the adjacency matrix of the line graph of \(K_n\), and \(J\) the all-ones matrix on its \(H\) edges. Directly,
\[
\Sigma=(p-s)I-sA_1+(s-p^2)J.
\]
The edge space is the orthogonal sum of constants, the \((n-1)\)-dimensional vertex-star difference space, and the \(H-n\)-dimensional space orthogonal to all vertex stars. The respective eigenvalues of \(A_1\) are \(2(n-2)\), \(n-4\), and \(-2\); those of \(J\) are \(H,0,0\). Consequently, the three covariance eigenvalues are
\[
L_0=p-Hp^2+Ds,\qquad L_1=p-(n-3)s,\qquad L_2=p+s.
\]
They have multiplicities \(1,n-1,H-n\). All are strictly positive: the empty matching and each single-edge matching have positive mass, so a linear statistic with nonzero edge coefficients cannot be almost surely constant. Thus \(\Sigma\) is positive definite.

**2. Exact inverse for disjoint edges.** Write \(P_0,P_1,P_2\) for the orthogonal projectors onto those three spaces. For distinct disjoint edges, their entries are, respectively,
\[
(P_0)_{ef}=\frac2{n(n-1)},\qquad
(P_1)_{ef}=-\frac4{n(n-2)},\qquad
(P_2)_{ef}=\frac2{(n-1)(n-2)}.
\]
For example, on edge vectors, the vertex-incidence Gram matrix has eigenvalue \(2(n-1)\) on constants and \(n-2\) on star differences, giving the displayed \(P_1\) entry; \(P_2=I-P_0-P_1\). Inverting the three eigenvalues yields the exact formula
\[
\boxed{\ q_n(t)=\frac2{n(n-1)L_0}-\frac4{n(n-2)L_1}+\frac2{(n-1)(n-2)L_2}.\ }
\]

**3. The low-activity limit.** Expand the finite polynomials \(Z_n\), \(Z_{n-2}\), \(Z_{n-4}\) at zero in the exact formula. The resulting reciprocal-eigenvalue series (valid for each fixed \(n\geq4\)) through degree two are
\[
\begin{aligned}
L_0^{-1}&=t^{-1}+2(2n-3)+(n^2+3n-9)t-16(n-3)(n-2)t^2+O(t^3),\\
L_1^{-1}&=t^{-1}+3(n-2)+3(n-3)t+(n-8)(n-4)(n-3)t^2+O(t^3),\\
L_2^{-1}&=t^{-1}+2(n-2)+(-n^2+5n-9)t+(2n^3-17n^2+57n-74)t^2+O(t^3).
\end{aligned}
\]
These coefficients can be obtained by formal division of polynomials whose coefficients count the size-zero through size-four matchings; absent sizes have zero coefficients. Substitution into the boxed identity cancels degrees \(-1,0,1\) and gives \(q_n(t)=-2t^2+O(t^3)\).

**4. The high-activity limit.** Put \(K=|M|\). Since the all-ones vector is an eigenvector, \(L_0=\operatorname{Var}(K)/H\). For \(n=2m+1\) odd, the ratio of the numbers of size-\((m-1)\) and size-\(m\) matchings is \(m/3\). Hence \(\operatorname{Var}(K)=m/(3t)+O(t^{-2})\), so \(L_0=1/(3nt)+O(t^{-2})\). In this case \(p\to1/n\) and \(s\to1/[n(n-2)]\), whence \(L_1\to1/[n(n-2)]\) and \(L_2\to(n-1)/[n(n-2)]\). Only the \(L_0^{-1}\) contribution in the boxed expression grows linearly, giving \(q_n(t)/t\to6/(n-1)\).

For \(n=2m\) even, the ratio of the numbers of size-\((m-1)\) to size-\(m\) matchings is \(m\). Thus \(L_0=1/[(n-1)t]+O(t^{-2})\). Let \(Y_v\) indicate an unmatched vertex. With probability \(m/t+O(t^{-2})\), exactly two unmatched vertices occur; conditional on this event, their pair is uniform among all vertex pairs. For distinct vertices \(u,v\), therefore,
\[
\operatorname{Var}(Y_u-Y_v)=\frac{2(n-2)}{(n-1)t}+O(t^{-2}).
\]
The star-difference edge score at \(u,v\) equals \(-(Y_u-Y_v)\) and its coefficient vector has squared norm \(2(n-2)\). Consequently \(L_1=1/[(n-1)t]+O(t^{-2})\). Meanwhile \(p\to1/(n-1)\), \(s\to1/[(n-1)(n-3)]\), so \(L_2\) tends to a positive limit. Inserting these three estimates into the boxed formula gives
\[
\frac{q_n(t)}t\longrightarrow \frac2n-\frac{4(n-1)}{n(n-2)}=-\frac2{n-2}.
\]
Finally \(q_n\) is continuous on \((0,\infty)\); its endpoint signs and the positive diagonal entries of \(Q\) prove the asserted parity-dependent linear partial-correlation conclusions.

## Verification
The accompanying standard-library `check.py` enumerates finite matchings independently of the partition recurrence, checks one- and two-edge probabilities, checks exact covariance matrices against their three-mode formula, and verifies the exact inverse by matrix multiplication with rational arithmetic. It additionally checks activity expansions against exact rational evaluations and samples high-activity limits; the analytic expansions and limits above, not these finite checks, establish all-\(n\) claims. The program reports 5039 exact rational assertions passing.

## Relationship to prior work
Monomer–dimer correlation decay and dimer–dimer covariances have been studied by Quitmann (arXiv:2309.13632; first public 2023-09-24) for lattice graphs. Alberici–Contucci–Mingione (arXiv:1409.6192) study mean-field monomer–dimer models on complete graphs and thermodynamic observables. Chen–Liu–Vigoda (DOI:10.1137/21M1443340) establish broad Glauber-mixing and spectral-independence theory, including related Gibbs matching models. Their inspected statements address pair correlations, limiting density, or influence/mixing rather than the exact finite complete-graph *inverse-covariance* sign reversal. Standard matching enumeration and Johnson-scheme eigenspaces are used as tools and not presented as novel. Priority beyond the inspected literature is not certified.

## Limitations
The theorem assumes the homogeneous complete graph with edge activity \(t>0\), no spatial structure, and fixed \(n\) in activity limits. It does not determine how many sign changes occur, the sign at intermediate activity for even \(n\), nonlinear conditional dependence, or growing-\(n\) scaling. Exhaustive finite checks do not prove general statements. Independent validation and historical-priority determination remain outstanding.

## References
1. Alexandra Quitmann, *Decay of correlations in the monomer-dimer model*, arXiv:2309.13632 (first public September 24, 2023), https://arxiv.org/abs/2309.13632.
2. Diego Alberici, Pierluigi Contucci, Emanuele Mingione, *A mean-field monomer-dimer model with random monomer activities: Exact solution and rigorous results*, arXiv:1409.6192 (2014), https://arxiv.org/abs/1409.6192.
3. Zongchen Chen, Kuikui Liu, Eric Vigoda, *Optimal Mixing of Glauber Dynamics: Entropy Factorization via High-Dimensional Expansion*, https://doi.org/10.1137/21M1443340.
