# Six-site threshold for hidden richness risk in cyclic species–area curves

## Finding

Consider a circular transect containing \(N\ge1\) labeled sites, exactly one species per site, and a uniformly chosen *contiguous* cyclic window of \(m\) sites, \(1\le m\le N\). Write \(K_m\) for the number of species represented. Its mean species–area curve is \(\mu(m)=\mathbb E[K_m]\). The species-resolved detection curve of taxon \(i\) is \(p_i(m)=\Pr(i\text{ appears in the window})\).

**Sharp finite identifiability threshold.** On every such transect with \(N\le5\), the entire mean curve \((\mu(1),\ldots,\mu(N))\) determines the entire law of \(K_m\) for every \(m\). At \(N=6\) this fails, even when the full species-resolved curves agree under the same species labels. Explicitly, the circular words `BACAAA` and `BAACAA` have identical \(p_A(m),p_B(m),p_C(m)\) for every \(m\), but at \(m=3\) their richness frequency histograms (out of six equally likely windows) are

\[
\begin{array}{c|ccc}
 &K_3=1&K_3=2&K_3=3\\\hline
\mathrm{BACAAA}&1&4&1\\
\mathrm{BAACAA}&0&6&0
\end{array}
\]

and therefore \(\operatorname{Var}_{\mathrm{BACAAA}}(K_3)=1/3\), while \(\operatorname{Var}_{\mathrm{BAACAA}}(K_3)=0\). Six sites are minimal for either kind of complete-curve ambiguity.

**Unbounded and quantitatively sharp family.** For every \(N\ge6\), place species \(B\) at site zero, species \(C\) at site \(s\), and species \(A\) at all other sites; require \(2\le s\le N-2\). Every such arrangement has exactly the same three species-resolved detection curves at *every* window length, regardless of \(s\). Set \(m=\lfloor N/2\rfloor\). Across this natural family, the *exact* range of richness variances is

\[
\boxed{\max_{2\le s\le N-2}\operatorname{Var}(K_m)-
\min_{2\le s\le N-2}\operatorname{Var}(K_m)
=\frac{2(\lfloor N/2\rfloor-2)}{N}.}
\]

The maximum occurs at \(s=2\) or \(s=N-2\), and the minimum at \(s=m\) or \(s=N-m\). Along even \(N\), this gap equals \(1-4/N\) and tends to one in squared-richness units. For even \(N\) at half-transect scale, the maximally separated singleton sites give *deterministic* richness \(K_m=2\), while nearby singleton sites yield a richness variance tending to one. Thus the ambiguity is not confined to tiny landscapes or vanishingly small fluctuations.

## Assumptions and scope

Sites are distinguishable locations in the cyclic group \(\mathbb Z/N\mathbb Z\), with periodic boundary conditions; each site bears exactly one species label. A window of length \(m\) consists of \(m\) consecutive sites and is sampled by choosing its starting site uniformly from the \(N\) possibilities. Sampling is **not** an unordered uniformly selected \(m\)-subset of sites and is **not** independent sampling with replacement. All probability and variance statements concern the randomness of the window location, with the landscape fixed. The near/far family has one common species \(A\) and two singleton species \(B,C\); there are no empty or multispecies sites.

## Proof

**1. Why a complete mean curve is sufficient through five sites.** Let \(S\) be the number of distinct species in the whole transect; it equals the known endpoint \(\mu(N)\). For \(m=1\) and \(m=N\), richness is deterministic. At \(m=2\), richness belongs to \(\{1,2\}\), hence its mean determines its distribution. At \(m=N-1\), omission of one site can remove at most one species, so \(K_{N-1}\in\{S-1,S\}\), also determined by its mean. These depths exhaust \(N\le4\).

For \(N=5\), only \(m=3\) remains. If \(S\le2\), richness at depth three lies in \(\{1,2\}\); if \(S\ge4\), it lies in \(\{2,3\}\). If \(S=3\), the only possible abundance multisets are \((2,2,1)\) and \((3,1,1)\). For \((2,2,1)\), richness at depth three is again in \(\{2,3\}\). The profiles are distinguished by \(\mu(4)\): the loss of a singleton when one uniformly random site is omitted gives \(\mu(4)=14/5\) for \((2,2,1)\), versus \(13/5\) for \((3,1,1)\). Within \((3,1,1)\), the two singleton sites are either adjacent or nonadjacent on the five-cycle. In the adjacent case precisely three of five length-two windows have different labels, so \(\mu(2)=8/5\); in the nonadjacent case precisely four do, so \(\mu(2)=9/5\). Each case has a single cyclic pattern up to rotation, reflection and exchange of the singleton labels, fixing its full richness law. This proves the claim without extrapolating from an enumeration.

**2. Common species-resolved curves.** In the family of the finding, the two rare sites are nonadjacent, so every contiguous window of length \(m\ge2\) contains an \(A\). Therefore

\[
\begin{aligned}
p_A(1)&=(N-2)/N,&p_A(m)&=1\quad(2\le m\le N),\\
p_B(m)&=m/N,&p_C(m)&=m/N\quad(1\le m\le N).
\end{aligned}
\]

In particular, \(\mu(1)=1\), and \(\mu(m)=1+2m/N\) for every \(2\le m\le N\), independently of the relative positions of \(B\) and \(C\). This is stronger than agreement of the total means.

**3. Exact joint-detection law.** Let \(s\) be the clockwise distance from \(B\) to \(C\). For any \(2\le m\le N\), the number of cyclic length-\(m\) windows containing both rare sites is

\[
J_N(m,s)=(m-s)_++(m-(N-s))_+,
\qquad (x)_+=\max(x,0).
\]

Indeed, such a window contains the oriented \(B\)-to-\(C\) arc, accounting for \((m-s)_+\) starting positions, or the opposite oriented arc, accounting for \((m-(N-s))_+\) positions. These count disjoint positions according to which rare site comes first when the window is read linearly. Put \(p=m/N\), \(q=J_N(m,s)/N\). Since \(K_m=1+I_B+I_C\), the full probability distribution is

\[
\Pr(K_m=1)=1-2p+q,\quad
\Pr(K_m=2)=2p-2q,\quad
\Pr(K_m=3)=q,
\]

and direct indicator covariance gives

\[
\operatorname{Var}(K_m)=2p(1-p)+2(q-p^2).
\]

At \(N=6,m=3\), the distances \(s=2\) and \(s=3\) yield \(J=1\) and \(J=0\) respectively, producing the stated histograms and variances.

**4. Sharp range at half-transect scale.** Put \(m=\lfloor N/2\rfloor\). Since \(2\le s,N-s\le N-2\) and \(2m\le N\), at most one summand in \(J_N(m,s)\) is positive and

\[
0\le J_N(m,s)\le m-2.
\]

The lower endpoint is attained when \(s=m\) or \(s=N-m\); the upper endpoint is attained when \(s=2\) or \(s=N-2\). The variance's dependence on \(s\) is exactly \(2J_N(m,s)/N\), so the difference between extremes is \(2(m-2)/N\). This completes the unrestricted family and its sharp within-family extremality claim.

## Verification

The companion `verify.py` uses only the Python standard library and exact rational arithmetic. Its restricted-growth-word enumeration exhausts *all* species partitions of the labeled site positions for \(1\le N\le5\), with Bell counts \(1,2,5,15,52\), then verifies that a full mean signature never corresponds to two richness-distribution signatures. It independently enumerates all windows in both six-site landscapes and checks their species-wise detection curves and complete histograms.

For \(6\le N\le40\), every eligible singleton separation and every \(2\le m\le N\) is checked against the complete three-point distribution formula and the variance formula, for \(18{,}970\) parameter triples. For \(6\le N\le60\), the exact extremal variance range is also checked. The machine-readable outputs are in `certificate.json`. Exhaustive finite checks corroborate the analytic unrestricted proof, rather than substituting for it.

## Relationship to prior work

Scheiner (2003) distinguished spatially contiguous and other species–area sampling designs. Laurie and Perrier (2007) showed in a multifractal bisection model that spatial variance carries information separate from mean richness, a broad conceptual point not claimed as new here. Tjørve, Kunin, Polce and Calf Tjørve (2008) studied spatially aggregated occupancy and mean species–area curves, including wrapped-around spatial samples, and explicitly identified expected richness as a sum of species-wise detection probabilities. Their demonstrated one- and two-species examples do not entail an exact minimal three-species cyclic identifiability threshold, nor the sharp half-transect variance gap with identical complete species-wise curves. Helmus and Ives (2012) discuss retaining adjacency when constructing spatial diversity–area curves, but do not supply this finite cyclic classification. The new contribution is the exact small-site information threshold and quantitatively macroscopic all-size ambiguity under a completely specified sampling model, not the general observation that mean richness need not determine spatial heterogeneity.

## Limitations

The sharp six-site cutoff applies only to one-species-per-site cyclic transects and to the **entire** mean-versus-window-length curve. It does not claim this cutoff for general multispecies quadrats, open intervals, arbitrary planar windows, random placement models, or information from only one sample size. The formula \(2(\lfloor N/2\rfloor-2)/N\) is the exact range only within the stated three-species, two-nonadjacent-singleton family, not a universal variance gap across all landscapes. No independence, causal ecological mechanism, or field-data inference is asserted. The reviewed literature does not exclude all differently worded prior mathematical formulations; independent literature validation remains outstanding.

## References

- S. M. Scheiner (2003), “Six types of species–area curves,” *Global Ecology and Biogeography* 12, 441–447, DOI: 10.1046/j.1466-822X.2003.00061.x (first public record 2003-10-17).
- H. Laurie and E. Perrier (2007), “A multifractal model for spatial variation in species richness,” arXiv:0710.5886v1 (2007-10-31); later *Ecological Complexity* 7 (2010), 32–35.
- E. Tjørve, W. E. Kunin, C. Polce, and K. M. Calf Tjørve (2008), “Species–area relationship: separating the effects of species abundance and spatial distribution,” *Journal of Ecology* 96, 1141–1151, DOI: 10.1111/j.1365-2745.2008.01433.x (first published 2008-10-15).
- M. R. Helmus and A. R. Ives (2012), “Phylogenetic diversity–area curves,” *Ecology* 93, S31–S43, DOI: 10.1890/11-0435.1.
