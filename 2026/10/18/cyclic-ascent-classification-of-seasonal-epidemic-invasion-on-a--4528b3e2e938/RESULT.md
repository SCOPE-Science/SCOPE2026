# Cyclic ascent classification of seasonal epidemic invasion on a directed transmission ring

## Finding

For a periodically switched susceptible–infected–susceptible (SIS) model with \(n\ge2\) host groups, suppose precisely one directed contact link of the ring is active during each of \(n\) consecutive seasons. The \(n\) links appear once per period, in an arbitrary order. Transmission is unidirectional around the ring, and all groups have the same removal rate \(\gamma>0\). Write the dimensionless transmission exposure of link \(i\) as \(a_i=\beta_i\tau_i>0\), and its product as \(P=\prod_{i=0}^{n-1}a_i\). If \(p(i)\) is the position of link \(i\) in the seasonal order, define the cyclic ascent statistic

\[
k=\#\{i\in\{0,\ldots,n-1\}:p(i)<p((i+1)\bmod n)\}.\]

Then \(1\le k\le n-1\), and the infection linearization's undamped period propagator \(Q\) has the **exact characteristic polynomial**

\[
\det(\lambda I-Q)=(\lambda-1)^n-P\lambda^k. \tag{1}
\]

For a period of length \(T=\sum_i\tau_i\), the infection's principal yearly multiplier is \(e^{-\gamma T}\Lambda_k\), where \(\Lambda_k>1\) is the unique real root above one of

\[
(\Lambda_k-1)^n=P\Lambda_k^k.\tag{2}
\]

Consequently the disease-free state is locally exponentially stable precisely when

\[
P<\frac{(e^{\gamma T}-1)^n}{e^{k\gamma T}}, \tag{3}
\]

and linearly unstable for the reverse strict inequality. At equality its principal Floquet multiplier is exactly one and is algebraically simple; nonlinear behavior at equality is not classified. For fixed \(P>0\) and \(\gamma T>0\), the principal multiplier is strictly increasing in \(k\). The chronological link order \((0,1,\ldots,n-1)\) has \(k=n-1\) and is maximally destabilizing; reverse order has \(k=1\) and is maximally stabilizing among permutations. The ratio of their critical exposure products (reverse divided by forward) equals \(e^{(n-2)\gamma T}\). There is no chronological-order effect for \(n=2\), and an order-dependent disease-free stability reversal is possible for every \(n\ge3\).

A sharp three-group witness has \(T=1\), \(\tau_i=1/3\), \(\beta_i=2\), and \(\gamma=\log 2\), hence \(a_i=2/3\) and \(P=8/27\). Chronological order \((0,1,2)\), with \(k=2\), is linearly unstable because \(8/27>1/4\); reverse order \((2,1,0)\), with \(k=1\), is exponentially stable because \(8/27<1/2\). Every frozen-season infection generator is Hurwitz. Their identical time average is also Hurwitz: its spectral abscissa is \(-\log2+2/3<0\). Thus neither each-season stability nor averaged-system stability determines invasion in this noncommuting cyclic-contact setting.

## Assumptions and scope

Fix any integer \(n\ge2\). Each host group has a normalized constant total population, and \(I_i\in[0,1]\) is the infected fraction in group \(i\), with indices understood modulo \(n\). Choose rates \(\beta_i>0\), season lengths \(\tau_i>0\), a common recovery/removal rate \(\gamma>0\), and a permutation \(\pi=(\pi_0,\ldots,\pi_{n-1})\) of the labels \(0,\ldots,n-1\). Repeat these \(n\) seasons periodically. During the season with label \(i\), only the link from infected group \(i\) to susceptible group \(i+1\) transmits, with dynamics

\[
\dot I_j=-\gamma I_j+\mathbf1_{j=(i+1)\bmod n}\,\beta_i(1-I_j)I_i,
\qquad j=0,\ldots,n-1.\tag{4}
\]

The disease-free state \(I=0\) is always a periodic solution. Let \(E_{uv}\) denote the elementary matrix with one at row \(u\), column \(v\). Its variational equation during link \(i\)'s season is \(\dot z=(-\gamma I_n+\beta_i E_{(i+1)\bmod n,i})z\). We analyze the exact linear Floquet multiplier, hence only local invasion/non-invasion of the disease-free state away from the threshold. No stochastic interpretation or nonlinear global persistence claim is made.

## Proof

**Exact propagation.** For every \(n\ge2\), the elementary matrix \(N_i=E_{(i+1)\bmod n,i}\) satisfies \(N_i^2=0\). Because \(-\gamma I_n\) commutes with \(N_i\), propagation through season \(i\) equals

\[
 e^{-\gamma\tau_i}(I_n+a_iN_i),\qquad a_i=\beta_i\tau_i.
\]

Write \(S_i=I_n+a_iN_i\). Thus the whole-period propagator is \(e^{-\gamma T}Q\), with \(Q=S_{\pi_{n-1}}\cdots S_{\pi_0}\). The factors have nonnegative entries and strictly positive diagonal. Expanding their product gives the entrywise inequality \(Q\ge I_n+\sum_i a_iN_i\). Since the right-hand side has a positive self-loop at each vertex and all directed ring edges positive, \(Q\) is primitive. Perron–Frobenius theory therefore gives a unique simple real spectral radius \(\Lambda>1\), strictly dominating the moduli of other eigenvalues.

**The cyclic-ascent polynomial.** Let \(p(i)\) be the chronological index of season \(i\). For an eigenvector \(v\) satisfying \(Qv=\lambda v\), group \(i\)'s abundance changes only when its incoming edge \(i-1\) fires. Immediately before outgoing edge \(i\) fires, its value is therefore \(\lambda v_i\) when \(p(i-1)<p(i)\), and \(v_i\) otherwise. Since the sole increase in group \(i+1\) comes from edge \(i\), we obtain

\[
(\lambda-1)v_{i+1}
=a_i\lambda^{\mathbf1_{p(i-1)<p(i)}}v_i.\tag{5}
\]

The eigenvalue \(\lambda=0\) is impossible because each shear is invertible; if \(\lambda=1\), (5) forces every coordinate of an eigenvector to vanish, also impossible. Therefore any eigenvalue has \(\lambda\ne0,1\), and any nonzero eigenvector has all entries nonzero by this recurrence. Multiplying (5) over all edges gives \((\lambda-1)^n=P\lambda^k\), with \(k=\sum_i\mathbf1_{p(i-1)<p(i)}\); relabeling the sum yields precisely the asserted cyclic-ascent count. Conversely, for every root \(\lambda\) of this polynomial (none can be zero or one because \(P>0\)), choose \(v_0\ne0\) and construct the remaining components by (5). The product identity ensures closure around the cycle. Chronologically applying the edge updates then gives final value \(\lambda v_j\) for each group \(j\), so \(Qv=\lambda v\). Thus the roots of the claimed polynomial coincide with the distinct eigenvalues of \(Q\). For generic positive exposure parameters the displayed polynomial has \(n\) distinct roots, establishing equality with the monic degree-\(n\) characteristic polynomial. Both sides depend continuously (indeed polynomially) on the exposures; approximation by generic positive exposures establishes (1) in the exceptional repeated-root cases as well.

Every permutation has at least one cyclic ascent and at least one cyclic descent, since strict cyclic increase or strict cyclic decrease of the finite position sequence is impossible. Thus \(1\le k\le n-1\). The forward chronological sequence has \(k=n-1\), and its reversal has \(k=1\). No chronology can exceed these extremes.

**Threshold and strict ordering.** For \(\lambda>1\), set \(H_k(\lambda)=(\lambda-1)^n/\lambda^k\). Its logarithmic derivative is

\[
\frac{H_k'(\lambda)}{H_k(\lambda)}
=\frac{n}{\lambda-1}-\frac{k}{\lambda}
=\frac{(n-k)\lambda+k}{\lambda(\lambda-1)}>0.
\]

It increases continuously from zero to infinity, proving uniqueness of \(\Lambda_k>1\) solving (2). Since \(H_{k+1}(\lambda)=H_k(\lambda)/\lambda<H_k(\lambda)\) on this interval, \(\Lambda_{k+1}>\Lambda_k\) for every \(1\le k<n-1\). The multiplier \(e^{-\gamma T}\Lambda_k\) crosses one precisely when \(\Lambda_k=e^{\gamma T}\), giving (3), the reverse inequality and the extreme-threshold ratio. Local exponential stability and linear instability follow from standard Floquet theory for a smooth piecewise-autonomous system. At equality the Perron multiplier is one and simple, so no strict stability statement is inferred.

**Three-season counterexample to averaging.** With \(\tau_i=1/3\), \(\beta_i=2\), and \(\gamma=\log2\), one has \(P=(2/3)^3=8/27\) and \(e^{\gamma T}=2\). For forward chronology, (3)'s right side is \((2-1)^3/2^2=1/4\), below \(8/27\). For reverse chronology it is \((2-1)^3/2=1/2\), above \(8/27\). In each frozen season, \(-\log 2\,I_3+2N_i\) has all eigenvalues \(-\log2\). The averaged generator is \(-\log2\,I_3+(2/3)C\), where \(C=\sum_iN_i\) is the cyclic permutation matrix; its spectral abscissa is \(-\log2+2/3<0\). The strict final inequality follows from \(\log2=2\sum_{m\ge0}(1/3)^{2m+1}/(2m+1)>2/3\). This proves the claimed simultaneous seasonal and averaged stability alongside chronological Floquet invasion.

## Verification

The included standalone standard-library program `check_cycle.py` constructs the time-ordered undamped propagator over all permutations for dimensions \(2\le n\le5\) with unequal positive rational exposures. It computes its exact rational characteristic polynomial by the Faddeev–LeVerrier identities, and compares every coefficient with (1). It checks all \(2!+3!+4!+5!=152\) permutations and independently checks the exact three-group threshold inequalities. Running `python check_cycle.py` prints two `PASS` lines. These finite checks support transcription and example integrity; the preceding analytic proof supplies the unbounded-dimensional theorem.

## Relationship to prior work

Qu and Ashwath (arXiv:2609.13668, first public September 12, 2026) systematically derive reproduction-threshold structures for compartmental epidemic models, including cyclic transmission and next-generation matrices. Their analyzed cyclic mechanism is repeated disease relapse in time-homogeneous compartments rather than a time-permuted single-link transmission ring, and they do not state (1)–(3). The present result is motivated by distinguishing static transmission-path cycles from chronological order effects.

The temporal-network infection-propagator framework of Valdano et al. (arXiv:1406.4815; Physical Review X 2015) already makes epidemic thresholds depend on the spectral radius of a time-dependent contact propagator. The later infection graph diagrams of Valdano and coauthors (Nature Communications 2023, DOI below) explicitly describe time-ordered propagators and when averaging may be justified. Those overarching principles already imply *in principle* that one could compute the threshold by multiplying the season propagators. What is specifically established here is the characteristic polynomial (1) for all ring sizes, its reduction of the entire chronological-permutation dependence to one cyclic-ascent integer, the sharp order ranking and the exact same-average stability reversal. The general time-ordered-propagator principle is not claimed as original. A broader earlier result on products of elementary transvections could potentially subsume the algebraic identity; no such directly covering primary source was identified in the inspected literature.

## Limitations

All theorems concern equal removal rates and exactly one directed transmission edge active per season, with each ring edge appearing once per period. Results need not hold for simultaneous contacts, arbitrary weighted networks, repeated edges, or group-specific removal. The theorem studies local linear stability of the disease-free state only; neither nonlinear critical dynamics at equality nor endemic attractors, stochastic establishment, empirical network realism, or global eradication follow. The word `invasion` means an expanding disease-free linear Floquet mode, not certainty of a macroscopic outbreak. General temporal-propagator methods predate this specialization; unlocated algebraic or epidemiological equivalent statements remain a literature risk.

## References

1. Zhuolin Qu and Abhi Ashwath, *Structures of the Basic Reproduction Number R0 Across Compartmental Disease Models*, arXiv:2609.13668, version first posted September 12, 2026. https://arxiv.org/abs/2609.13668
2. Eugenio Valdano, Luca Ferreri, Chiara Poletto, and Vittoria Colizza, *Analytical Computation of the Epidemic Threshold on Temporal Networks*, Physical Review X **5**, 021005 (2015), preprint arXiv:1406.4815. https://arxiv.org/abs/1406.4815
3. *Epidemic graph diagrams as analytics for epidemic control in the data-rich era*, Nature Communications **14** (2023), DOI:10.1038/s41467-023-43856-1. https://www.nature.com/articles/s41467-023-43856-1
4. *Epidemic Threshold in Continuous-Time Evolving Networks*, arXiv:1706.05968. https://arxiv.org/abs/1706.05968
