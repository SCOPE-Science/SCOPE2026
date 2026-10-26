# Finite-window tomography of fragmented binary habitat sequences

## Finding

**Theorem (exact patch-count inversion and its stationary reduction).** Consider a time-homogeneous binary spatial Markov sequence with strictly positive initial-state and transition probabilities. Label occupied cells by \(1\), vacant cells by \(0\), and let \(R_n\) be the number of maximal contiguous occupied patches among the first \(n\) cells, with both window ends treated as boundaries. Write
\[
A=\Pr(R_3=0),\qquad B=\Pr(R_3=2),\qquad C=\Pr(R_4=0).
\]
Then these three patch-count probabilities determine the initial occupancy probability and both transition probabilities **uniquely**, with a necessary-and-sufficient strict feasibility region and a parameter-free test of stationarity. In the stationary submodel, the distribution of \(R_3\) alone already identifies the entire spatial process; no one- or two-cell patch-count distribution does so. Once calibrated, the model determines all patch-count distributions at every length.

The inverse and feasibility formulas appear below. They concern exact population probabilities from identically distributed windows, not finite-sample estimates or inference under misspecification.

## Assumptions and scope

For all \(i\ge1\), \(X_i\in\{0,1\}\) forms a first-order, time-homogeneous Markov chain with
\[
t=\Pr(X_1=0),\quad a=\Pr(X_{i+1}=1\mid X_i=0),\quad b=\Pr(X_{i+1}=0\mid X_i=1),
\qquad 0<t,a,b<1.
\]
The chain is interpreted spatially along a transect, not as a temporal ecological dynamics model. Windows of lengths three and four have **the same initial law** and transition kernel. The patch count is
\[
R_n=\mathbf1_{\{X_1=1\}}+\sum_{i=2}^n\mathbf1_{\{X_{i-1}=0,\ X_i=1\}}.
\]
No empty or occupied cells outside a window are added to the boundary convention. The parameters are distinguished: \(a\) describes entry into an occupied patch, and \(b\) describes exit from it.

## Proof

**1. Three short-window probabilities.** The only three-cell string with zero occupied patches is \(000\); the only one with two occupied patches is \(101\). Thus the chain multiplication rule gives
\[
A=t(1-a)^2,\qquad B=(1-t)ba,\qquad C=t(1-a)^3.
\tag{1}
\]
Dividing the two empty-window probabilities, and then solving in order, yields the exact inverse
\[
\boxed{t=\frac{A^3}{C^2},\qquad
 a=1-\frac CA,\qquad
 b=\frac{BAC^2}{(C^2-A^3)(A-C)}.}
\tag{2}
\]
Every denominator is strictly positive in the stated model.

**2. Exact image and unique feasibility.** A proposed triple \((A,B,C)\) comes from precisely one such strictly interior Markov law if and only if
\[
\boxed{0<C<A,\qquad A^3<C^2,\qquad
0<B<\frac{(C^2-A^3)(A-C)}{AC^2}.}
\tag{3}
\]
Necessity follows from \(0<a<1\), \(0<t<1\), and \(0<b<1\) in (1)–(2). Conversely, these inequalities make the parameters in (2) lie strictly between zero and one. Substituting into (1) reconstructs exactly \((A,B,C)\). This proves existence, uniqueness, and that there are no unmentioned feasibility constraints.

**3. Stationarity is observable from patch counts.** The initial law is stationary if and only if the opposing probability fluxes agree:
\[
ta=(1-t)b.
\]
Since \(B=(1-t)ba\), this is equivalent, for \(a>0\), to \(B=ta^2\). Substitution from (2) proves the exact necessary-and-sufficient identity
\[
\boxed{BC^2=A(A-C)^2.}
\tag{4}
\]
Equation (4), together with (3), is an exact model-level stationarity diagnostic using only three event frequencies.

**4. A single three-cell distribution in the stationary case.** Under stationarity, set \(q=ta=(1-t)b\). Then \(A=(t-q)^2/t\) and \(B=q^2/t\). Their positive square roots \(u=\sqrt A\) and \(v=\sqrt B\) satisfy \(u=(t-q)/\sqrt t\), \(v=q/\sqrt t\). Therefore
\[
\boxed{t=(u+v)^2,\qquad a=\frac{v}{u+v},\qquad
 b=\frac{v(u+v)}{1-(u+v)^2}.}
\tag{5}
\]
Here \(R_3\) takes only the values \(0,1,2\), so \(A,B\) determine its entire distribution. The exact feasible domain of that distribution is
\[
\boxed{u>0,\quad v>0,\quad (u+v)(u+2v)<1,\qquad
 \Pr(R_3=1)=1-u^2-v^2.}
\tag{6}
\]
Indeed the last strict inequality is exactly \(b<1\); it automatically forces \(t<1\), while \(0<a<1\) follows from positive \(u,v\). Equations (5)–(6) prove both directions, including the boundary exclusions.

**5. Minimality for stationary short-window observations.** For two cells, at most one occupied patch can occur, and \(\Pr(R_2=0)=t(1-a)\) is a single number. The distinct stationary chains
\[
(t,a,b)=\left(\frac13,\frac14,\frac18\right),\qquad
(t,a,b)=\left(\frac25,\frac38,\frac14\right)
\]
both have \(\Pr(R_2=0)=1/4\). A one-cell patch-count law identifies only the initial occupancy probability, not the transitions. Hence three is the sharp single-window length for stationary identifiability, among one-, two-, and three-cell windows.

For an arbitrary (not necessarily stationary) initial law, a three-cell patch-count distribution has at most two independent probabilities and need not identify three parameters. More concretely, any fixed admissible \((A,B)\) defines a local one-parameter family by varying \(C\) within the strict feasibility region (3), so the extra four-cell probability is substantive.

**6. Prediction at every window length.** With formal variable \(z\), the probability generating polynomial of occupied-patch count is
\[
\boxed{\mathbb E[z^{R_n}]=
\begin{pmatrix}t&(1-t)z\end{pmatrix}
\begin{pmatrix}1-a&az\\ b&1-b\end{pmatrix}^{n-1}
\begin{pmatrix}1\\1\end{pmatrix},\qquad n\ge1.}
\tag{7}
\]
The initial factor marks the first occupied cell as a patch. The transition \(0\to1\) adds a factor of \(z\); all other transitions leave the patch count unchanged. This proves (7) by induction and shows that recovered parameters predict all future finite-window patch-count laws.

## Verification

The accompanying standalone `verify_fragmentation.py` uses exact rational arithmetic and explicitly enumerates all binary strings of lengths one through eight. It checks (1), (2), (3), (4), the transition-matrix generating polynomial (7), and two-site nonidentifiability across 1,350 strict-interior parameter triples. It makes 10,800 polynomial-law comparisons, summing probabilities across 688,500 binary strings. Its deterministic output is `verification_certificate.json`.

For instance, the stationary law \((t,a,b)=(2/3,1/4,1/2)\) gives \((A,B,C)=(3/8,1/24,9/32)\), while the nonstationary law \((1/3,1/4,1/2)\) gives \((3/16,1/12,9/64)\). Substitution exactly reproduces both triples. The infinite-length prediction and all parameter-identification claims are algebraic proofs above, not conclusions inferred from finite enumeration.

## Relationship to prior work

He and Hubbell (2003) motivate the ecological importance of occupancy, fragmentation, and the number of occupied patches, using independent-cell percolation approximations rather than an inverse for correlated Markov transects. Antzoulakos and Chadjiconstantinidis (2001) derive generating functions and moment recurrences for counts of success runs in Markov-dependent trials; these are forward-distribution results, not the inverse, exact feasible image, or stationarity identity (2)–(6). Savelyev and Balakin (2004) examine forward joint distributions of the number of ones and one-runs; the full text was inaccessible during this review, so an equivalent inverse corollary cannot be excluded. Corzo and Vergara (2016) compare tests of positive Markovian dependence based on run counts and their power; the inspected methods and conclusions do not state this finite-window inversion from occupied-patch counts alone.

An equivalent result under runs-of-ones, Markov-binomial inverse problems, or ecological occupancy mapping terminology remains possible. In particular, forward formulas can make the inversion short to derive; the claim here is the exact inverse feasibility and minimum observable window, not priority for run-generating functions.

## Limitations

Only the strictly interior, spatially homogeneous, first-order **binary** Markov model is covered. The identity (4) tests stationarity **within that assumed model**, not Markovianness of an arbitrary spatial field. Exact population probabilities are assumed; empirical histogram estimation, detection errors, unknown window alignment, boundary states, higher-order dependence, heterogeneous sites, and multidimensional landscapes are not treated. Parameter recovery can be ill-conditioned near rare empty/alternating windows; the theorem gives no uniform statistical error bound. The comparator by Savelyev and Balakin (2004) could not be inspected in full; this is a substantive residual originality risk.

## References

1. F. He and S. P. Hubbell, *Percolation Theory for the Distribution and Abundance of Species*, Physical Review Letters **91** (2003), 198103, first publicly issued 2003-11-07. DOI: 10.1103/PhysRevLett.91.198103. Author-hosted article: https://sites.ualberta.ca/~fhe/He-publications/He_Hubbell.PRL03.pdf.
2. D. L. Antzoulakos and S. Chadjiconstantinidis, *Distributions of Numbers of Success Runs of Fixed Length in Markov Dependent Trials*, Annals of the Institute of Statistical Mathematics **53** (2001), 599–619. https://www.ism.ac.jp/editsec/aism/pdf/053_3_0599.pdf.
3. L. Ya. Savelyev and S. V. Balakin, *The joint distribution of the number of ones and the number of 1-runs in binary Markov sequences*, Discrete Mathematics and Applications **14** (2004), 353–372. DOI: 10.1163/1569392041938802.
4. J. A. Corzo and M. E. Vergara, *A data driven runs test to identify first order positive Markovian dependence*, Hacettepe Journal of Mathematics and Statistics **45** (2016), 521–540. DOI: 10.15672/HJMS.2015559562. https://dergipark.org.tr/en/download/article-file/644858.
