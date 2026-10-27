# Exact adjacent-pair law and opposite correlation signs in two-species one-shot adsorption

## Finding

In the one-dimensional two-species single-attempt random sequential adsorption model, the entire nearest-neighbor joint law is elementary and, for every nondegenerate species bias and every positive observation time, equal-species occupancy indicators are **strictly positively** correlated across an edge while total-occupancy indicators are **strictly negatively** correlated across that same edge.

Fix \(0<p<1\), write \(q=1-p\), and let \(0<t\le 1\). Independently at each site, a species \(Y_i\in\{A,B\}\) is drawn with \(\Pr(Y_i=A)=p\), and an attempt time \(U_i\) is uniform on \([0,1]\). At time \(U_i\), the species is irreversibly accepted if neither adjacent site already holds the opposite species; otherwise the site remains vacant \(X\). Write \(\eta_i(t)\in\{A,B,X\}\) for its state.

Set \(g=\sqrt{pq}\) and define the two one-sided nonblocking probabilities
\[
 h_A(u)=\cosh(gu)-\frac qg\sinh(gu),\qquad
 h_B(u)=\cosh(gu)-\frac pg\sinh(gu).
\]
Put
\[
 a(t)=p\int_0^t h_A(u)\,du,
 \qquad b(t)=q\int_0^t h_B(u)\,du,
\]
and let \(R_A(t)=p\int_0^t h_A(u)^2\,du\), \(R_B(t)=q\int_0^t h_B(u)^2\,du\). Every integral is elementary. In particular
\[
 a=\frac p g\sinh(gt)-(\cosh(gt)-1),\qquad
 b=\frac q g\sinh(gt)-(\cosh(gt)-1),
\]
\[
 R_A=\frac{(2p-1)t}{2}+\frac{\sinh(2gt)}{4g}-\sinh^2(gt),\qquad
 R_B=\frac{(1-2p)t}{2}+\frac{\sinh(2gt)}{4g}-\sinh^2(gt).
\]

**Exact ordered joint law.** In the row/column order \((A,B,X)\),
\[
 \bigl[\Pr(\eta_0(t)=s,\eta_1(t)=s')\bigr]_{s,s'}
 =\begin{pmatrix}
 a^2 & 0 & R_A-a^2\\
 0 & b^2 & R_B-b^2\\
 R_A-a^2 & R_B-b^2 & (1-a-b)^2
 \end{pmatrix}.
\]
In particular \(R_A+R_B=a+b-ab\), and for every \(0<p<1\), \(0<t\le1\),
\[
 \operatorname{Cov}(\mathbf1_{\{\eta_0=A\}},\mathbf1_{\{\eta_1=A\}})
 =a^2-R_A^2>0,
\]
\[
 \operatorname{Cov}(\mathbf1_{\{\eta_0=B\}},\mathbf1_{\{\eta_1=B\}})
 =b^2-R_B^2>0,
\]
whereas with \(H_i=\mathbf1_{\{\eta_i\ne X\}}\),
\[
 \operatorname{Cov}(H_0,H_1)
 =-ab\bigl[2(1-a)(1-b)-ab\bigr]<0.
\]
The results include the jammed state \(t=1\); the correlations vanish at \(t=0\) or at degenerate species probabilities \(p=0,1\) (interpreted by limits).

## Assumptions and scope

The lattice is the whole of \(\mathbb Z\), with independent site labels, independent continuous one-shot attempt times, initially empty sites, no desorption, and rejection only when an *already accepted opposite* species occupies an adjacent site. Same-species nearest neighbors do not block each other. The observation parameter is \(0\le t\le1\) in the authors' uniform-clock normalization, not an unbounded Poisson exposure time. Correlations concern a single fixed adjacent pair in the infinite-volume dynamics. The stationary/jammed word is used only at \(t=1\); this process is otherwise irreversible and nonstationary.

## Proof

**1. Construction.** To determine acceptance of a site, trace possible blocking backward through neighbors with strictly earlier attempt times. A dependency chain reaching distance \(n\) along either direction requires \(n+1\) independent continuous clocks to be in decreasing order, an event of probability \(1/(n+1)!\) for each direction. The union bound and convergence of \(\sum_n2/(n+1)!\) exclude infinite backward chains almost surely. Thus finite windows eventually stabilize the state of any fixed finite set of sites.

**2. Cavity equations.** Keep a prospective \(A\) site unattempted until time \(u\), and let \(h_A(u)\) be the probability that no accepted \(B\) is present at its left neighbor by that time. Define \(h_B\) analogously, exchanging species. The first opposite-species attempt next to the protected site succeeds at its attempt time only if the other, external neighbor does not already hold the opposite species. Hence
\[
 h_A(u)=1-q\int_0^u h_B(v)\,dv,
 \qquad h_B(u)=1-p\int_0^u h_A(v)\,dv.
\]
(The excluded site's own attempt has not yet occurred.) This Volterra system has the unique solution displayed above, from \(h_A''=pq h_A\), \(h_B''=pq h_B\), and initial derivatives \(h_A'(0)=-q\), \(h_B'(0)=-p\). It also gives \(0<h_A,h_B<1\) at \(0<u\le1\). The two half-lines on either side of the prospective site have independent data. Conditioning on its type and attempt time gives the stated one-site probabilities \(R_A=p\int h_A^2\), \(R_B=q\int h_B^2\). Expanding squares and integrating gives the elementary formulas above, agreeing with the published single-site density law.

**3. Jointly accepted adjacent pair.** If sites \(0\) and \(1\) both have assigned type \(A\), they do not block one another. Their successful deposition events depend, respectively, only on the untouched half-lines \((\ldots,-2,-1)\) and \((2,3,\ldots)\), together with their independent attempt times. They are therefore independent after conditioning on these two prescribed labels. Their joint unconditional probability is \(a^2\). The same reasoning yields \(b^2\) for an adjacent \(BB\) pair. An adjacent \(AB\) or \(BA\) pair of *accepted* particles is impossible: whichever attempted second would have been rejected. Reflection symmetry and the one-site marginals consequently yield all \(AX,XA,BX,XB\) probabilities in the displayed matrix.

**4. The two-vacancy probability.** Differentiating \(a\) and \(b\) and using the cavity equations yields
\[
 a'=p(1-b)=p h_A,\qquad b'=q(1-a)=q h_B.
\]
Therefore
\[
 \frac{d}{dt}(a+b-ab)=a'(1-b)+b'(1-a)=p h_A^2+q h_B^2
 =\frac{d}{dt}(R_A+R_B).
\]
Both sides vanish at \(t=0\), proving \(R_A+R_B=a+b-ab\). Inclusion-exclusion for two vacancies now gives
\[
 \Pr(XX)=1-2(R_A+R_B)+(a^2+b^2)=(1-a-b)^2.
\]
This finishes the entire matrix without making an independence assumption about neighboring vacancies.

**5. Strict signs and boundaries.** Since \(0<h_A,h_B<1\) except at \(u=0\), we have \(0<R_A<a\) and \(0<R_B<b\) for \(0<p<1,t>0\). This proves the two strictly positive equal-species covariances. Put \(R=R_A+R_B=a+b-ab\). Using \(\Pr(H_0=H_1=1)=a^2+b^2\), direct factorization yields
\[
 a^2+b^2-R^2=-ab[2(1-a)(1-b)-ab].
\]
Because \(h_A,h_B\le1\), strictly \(0<a<pt\le p\) and \(0<b<qt\le q\). Consequently \((1-a)(1-b)>pq\) and \(ab<pq\), so the bracket exceeds \(pq>0\). Hence total occupancy is strictly negatively correlated. At \(p=0\) or \(p=1\), every attempted particle is accepted and distinct sites are independent; at \(t=0\), all sites are vacant.

**6. Symmetric jammed check.** At \(p=q=1/2,t=1\),
\[
 a=b=1-e^{-1/2},\quad R_A=R_B=(1-e^{-1})/2,
\]
\[
 \Pr(AA)=\Pr(BB)=(1-e^{-1/2})^2=0.154818121746\ldots,
\]
\[
 \Pr(XX)=(2e^{-1/2}-1)^2=0.045395125835\ldots.
\]
The same-species covariance is \(0.054924021523\ldots>0\), while the total-occupation covariance is \(-0.089940157401\ldots<0\). This checks both signs at a physically natural balanced composition.

## Verification

Run `python3 CHECK.py` with a standard Python installation; no external packages or network access are required. The checker independently simulates the original single-attempt acceptance dynamics on large periodic rings, compares all nine joint probabilities for seven nontrivial parameter pairs, enumerates all species assignments and arrival orders exactly on small rings, and verifies normalization, marginal consistency, positivity, the cavity identity, and the strict covariance signs. Its recorded run passed 147 assertions. Finite-ring enumeration and simulation are diagnostic checks, not proofs of the infinite-volume theorem; the proof above is analytic. Finite rings may have small winding corrections, controlled by the factorial probability of a decreasing causal chain spanning the ring.

## Relationship to prior work

Amaral and dos Santos (arXiv:2306.09786v1, 16 June 2023) introduce exactly this single-attempt antagonistic two-species lattice process and derive the one-point densities \(R_A,R_B\), including their explicit hyperbolic formulas. Their full text (model, event decomposition, density proof, and conclusion) does not state the adjacent-pair matrix or the opposite-sign nearest-neighbor covariance theorem. Those published one-point results are acknowledged as established and are *not* claimed here. The present pair derivation uses a natural two-sided cavity extension of their argument; the method's proximity is a priority risk, but the new claim concerns genuinely two-site observables and universal signed dependence.

Amaral and dos Santos (arXiv:2210.05627v1) give a full pair-correlation calculation for the *different, single-species* nearest-neighbor exclusion RSA model. Its occupancy rule prohibits adjacent occupied sites altogether, unlike the present two-species model. Martins, Dickman, and Ziff (arXiv:2211.04622v1) study antagonistic RSA with *repeated* unsuccessful site attempts, mainly in two dimensions, and discuss one-dimensional three-site approximations. That different acceptance protocol does not furnish this one-shot joint law. General RSA correlation methods could contain an equivalent specialization and cannot be excluded as a priority risk without independent literature assessment.

## Limitations

No claim is made about nonadjacent spatial correlations, cluster-size distributions, repeated-attempt antagonistic adsorption, higher dimensions, or uniform behavior under a scaling of the deposition probabilities with the lattice size. The sign theorem uses \(0<t\le1\) and \(0<p<1\), with exact endpoint behavior specified separately. The calculation is an analytic derivation inside a known stochastic model, not an independent scholarly priority certification. Independent external audit has not been performed.

## References

1. C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site*, arXiv:2306.09786v1, first submitted 2023-06-16. https://arxiv.org/abs/2306.09786
2. C. S. do Amaral and D. C. dos Santos, *Density and correlation in a random sequential adsorption model*, arXiv:2210.05627v1, first submitted 2022-10-11. https://arxiv.org/abs/2210.05627
3. P. H. L. Martins, R. Dickman and R. M. Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions*, arXiv:2211.04622v1, first submitted 2022-11-09. https://arxiv.org/abs/2211.04622
