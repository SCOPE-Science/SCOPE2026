# Pareto branch-exit clock and macroscopic relaxation after rare BCZ roof excursions

## Finding

On the Farey triangle \(\Omega=\{(a,b):0<a,b\le1,\ a+b>1\}\), let
\[
T(a,b)=(b,\kappa(a,b)b-a),\qquad
\kappa(a,b)=\left\lfloor\frac{1+a}{b}\right\rfloor,
\quad R_0(a,b)=\frac1{ab}.
\]
Let \(m=2\,da\,db\) be the known invariant probability measure, and condition the initial state on \(E_R=\{R_0>R\}\), where \(R\to\infty\). For \(d=\min(a,b)\), one has
\[
m(E_R)\sim\frac2{R^2},\qquad
Rd\ \Longrightarrow\ V,\qquad
\Pr(V\le v)=v^2\quad(0\le v\le1).
\]
Thus \(V\) has density \(2v\) on \((0,1)\), and each of the two corners \((0,1)\), \((1,0)\) contributes half the conditioned probability asymptotically.

Put \(j_0=1\) when \(a<b\) and \(j_0=2\) when \(b<a\). For sufficiently large \(R\), define the first post-cusp exit from the branch of index two by
\[
\tau_R=\min\{j\ge j_0:\kappa(T^j(a,b))\ne2\}.
\]
Then the exact asymptotic exit-clock law is
\[
\frac{\tau_R}{R}\ \Longrightarrow\ H=\frac1{2V},\qquad
\Pr(H>t)=\begin{cases}1,&0\le t<1/2,\\1/(4t^2),&t\ge1/2.\end{cases}
\]
In particular the earliest scaled branch exit is \(1/2\), and the exit clock has a Pareto tail of shape two.

For every fixed closed interval \(J=[\eta,\theta]\subset(0,1/2)\), the entire conditioned macroscopic orbit segment obeys
\[
\sup_{t\in J}\left\|T^{\lfloor tR\rfloor}(a,b)
 - (1-tRd,1-tRd)\right\|_\infty\longrightarrow0
\]
uniformly over all initial states in \(E_R\) as \(R\to\infty\). Consequently its law converges, in the uniform metric, to \(t\mapsto(1-tV,1-tV)\); the corresponding roof observable converges uniformly to \(t\mapsto(1-tV)^{-2}\). This is a time window growing linearly with the rare-event threshold, not a fixed-lag cylinder statistic.

## Assumptions and scope

The map is defined on the triangle above; \(T\) preserves \(m\), as established in the cited foundational literature. The roof is \(R_0=1/(ab)\); a large roof observation is an excursion event, not the index \(\kappa\) itself. Thresholds \(R\) are real and tend to infinity. A tie \(a=b\) cannot belong to \(E_R\) once \(R>4\). The assertions hold for the invariant stationary ensemble conditioned on \(E_R\). The path window stays strictly below the critical rescaled time \(1/2\).

## Proof

**1. Conditional corner law.** For \(R>4\), each state of \(E_R\) lies either near \((0,1)\) with \(a<b\) or near \((1,0)\) with \(b<a\). In the first region, \(a<2/R\) and \(1-a<b\le1\), and similarly with coordinates exchanged in the second. Substitute \(z=Ra\) in the first region. The admissible \(b\)-interval is
\[
1-z/R<b\le\min(1,1/z).
\]
For every \(0<z<1\), its width is \(z/R\); for fixed \(z>1\) it is empty eventually. Uniform domination is available because \(0<z<2\) and the rescaled widths are bounded. Thus the first corner has \(R^2\)-scaled Euclidean area \(\int_0^1z\,dz=1/2\), and the other is symmetric. Since \(m=2\,da\,db\), \(R^2m(E_R)\to2\). Replacing the integral endpoint \(1\) by \(v\in[0,1]\) gives \(\Pr(Rd\le v\mid E_R)\to v^2\). The symmetry also gives asymptotically equal corner weights.

**2. Exact escape from the index-two branch.** Take \(R\) large enough that \(d<1/3\). If \(a<b\), the triangle constraint and smallness of \(a\) give \(\kappa(a,b)=1\), hence
\[
T(a,b)=(b,b-a)=(u,u-d),\quad j_0=1,\quad u=b.
\]
If \(b<a\), write \(c=\kappa(a,b)b-a\). The identity \(c=1-b\{(1+a)/b\}\) yields \(1-b<c\le1\); also \(\kappa(b,c)=1\), so
\[
T^2(a,b)=(c,c-b)=(u,u-d),\quad j_0=2,\quad u=c.
\]
In either case \(1-d<u\le1\). At a subsequent state \((s+d,s)\) the branch index equals two precisely when \(s>(1+d)/2\), because
\[
\kappa(s+d,s)=\left\lfloor1+\frac{1+d}{s}\right\rfloor.
\]
Therefore successive index-two iterates have the *exact* form
\[
T^{j_0+\ell}(a,b)=(u-\ell d,u-(\ell+1)d)
\]
for every integer \(0\le\ell<L\), where the first exit index is
\[
L=\max\left\{0,\left\lceil\frac{u-(1+d)/2}{d}\right\rceil-1\right\},\qquad
\tau_R=j_0+L.
\]
The formula includes equality at a branch discontinuity because \(s=(1+d)/2\) already gives index at least three. Since \(1-d<u\le1\), it follows uniformly that
\[
\tau_R=\frac1{2d}+O(1)
\]
with an absolute implied constant. In particular \(\tau_R/R=(2Rd)^{-1}+O(R^{-1})\). Step 1 and the continuous mapping theorem give the Pareto exit law.

**3. Macroscopic relaxation.** For \(J=[\eta,\theta]\subset(0,1/2)\), Step 1's elementary corner bounds give \(Rd\le1+o(1)\) uniformly on \(E_R\): in the small-coordinate region the product condition forces \(Rd<(1-d)^{-1}\). Hence \(\lfloor tR\rfloor<\tau_R\) for all \(t\in J\), uniformly for large \(R\). Substitute \(\ell=\lfloor tR\rfloor-j_0\) into the exact affine orbit formula, use \(u=1+O(d)\), and note \(d=O(R^{-1})\). This proves the asserted uniform deterministic approximation. The conditional convergence of \(Rd\) then gives the limiting diagonal path, and uniform continuity of reciprocal products on the compact positive range \(1-tV\ge1-\theta>1/2\) gives the roof profile.

## Verification

The included standalone Python 3 checker uses exact rational arithmetic to replay the branch identities, the ceiling formula for the *first* non-two index, and the critical \(1/(2d)\) scaling across 120 independent rational cusp configurations. It prints `VERIFY_OK` on success. The measure asymptotic and convergence of conditioned paths are proved analytically above; finite tests are not used as infinite-time or asymptotic certificates.

## Relationship to prior work

The BCZ transformation, invariant area measure, and horocycle roof are established constructions, not new here. Athreya--Cheung's 2012 preprint gives the return-section dynamics and, in Lemma 5.3, credits an earlier result that a sufficiently large index \(\kappa\) forces a long string of index-two iterates. That *lower-bound itinerary statement* neither specifies the exact first exit nor a rare-roof-conditioned distribution for its clock. Augustin--Boca--Cobeli--Zaharescu's classical fixed-length \(h\)-spacing law determines fixed-dimensional joint Farey gap statistics, but it does not supply a limit of observations taken at \(\lfloor tR\rfloor\) iterations as \(R\to\infty\). Artiles--Best--Bordignon's 2026 strong-mixing theorem concerns fixed sets separated by an increasing lag, not the moving rare-event conditioning and proportional-time orbit law above.

## Limitations

This result does not establish an extremal point-process limit, an extremal index, or uniformity in a *finite* Farey order \(Q\). Its explicit path description ends before rescaled time \(1/2\), where a positive fraction of rare-excursion trajectories begin to leave the index-two branch. The original 2001 full texts on Farey \(h\)-spacings and Hall's conjecture were not both materially inspected, so an unrecognized historic reformulation of the proportional-time conditional law remains a bibliographic risk. Independent mathematical and priority review has not been performed.

## References

1. J. S. Athreya and Y. Cheung, *A Poincaré section for horocycle flow on the space of lattices*, arXiv:1206.6597v1 (first public version 28 June 2012), especially Sections 1.2, 1.5, and 5.1.2.
2. V. Augustin, F. P. Boca, C. Cobeli and A. Zaharescu, *The h-spacing distribution between Farey points*, Math. Proc. Cambridge Philos. Soc. 131 (2001), 23–38, doi:10.1017/S0305004101005187.
3. F. P. Boca, C. Cobeli and A. Zaharescu, *A conjecture of R. R. Hall on Farey points*, J. Reine Angew. Math. 535 (2001), 207–236, doi:10.1515/crll.2001.049.
4. A. Artiles, A. Best and M. Bordignon, *Mixing of the BCZ Map*, arXiv:2610.07347v1 (5 October 2026), especially the introduction and Section 2.
