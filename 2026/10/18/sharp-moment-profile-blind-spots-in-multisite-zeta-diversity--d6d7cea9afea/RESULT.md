# Sharp Moment-Profile Blind Spots in Multisite Zeta Diversity

## Finding
Consider \(N\ge1\) labeled sampling sites and \(S\ge1\) species, each present at least once. Choose a uniform \(k\)-subset \(W\) of sites and count \(Z_k\), the species present in *all* sites of \(W\). Set \(Z_0=S\). For every \(1\le r\le S\), define \(H_r(t)\) as the number of unordered \(r\)-species groups whose occupied-site sets have intersection of size \(t\), for \(0\le t\le N\).

**Complete moment-spectrum reconstruction.** For every \(0\le t\le N\),
\[
H_r(t)=\sum_{k=t}^{N}(-1)^{k-t}\binom{k}{t}\binom{N}{k}\,\mathbb E\!\left[\binom{Z_k}{r}\right].
\]
Consequently, the entire mean profile \(\mathbb EZ_k\) reconstructs the histogram of individual range sizes, and the entire mean-and-variance profiles reconstruct the histogram of *pairwise species range-intersection sizes*. More generally, the factorial-moment profiles through order \(r\) determine exactly all aggregate intersection-size histograms for groups of up to \(r\) species. These are aggregate, not species-labeled, histograms.

**Two sharp limits to second-moment identification.** Equal mean and variance of \(Z_k\) for *every* sample depth do not always determine the distribution of \(Z_k\). Such an ambiguity is impossible with fewer than three sites, regardless of the number of species, and impossible with fewer than three species, regardless of the number of sites. At three sites it is impossible with at most four species, but occurs with five. At three species it occurs with four sites. In particular the smallest possible combined number of sites and species is **seven**, attained by four sites and three species. These are separate sharp coordinatewise boundaries; no assertion is made that every larger parameter pair admits ambiguity.

For three sites and five species \(a,b,c,d,e\), compare the site assemblages
\[
(\varnothing,\{a,b,c\},\{a,d,e\})\quad\text{and}\quad(\{a\},\{a\},\{b,c,d,e\}).
\]
For \(k=1\), the respective \(Z_1\) lists are \((0,3,3)\) and \((1,1,4)\); for \(k=2\), both lists are permutations of \((1,0,0)\); and for \(k=3\), both are zero. Thus the full mean-and-variance profiles coincide, but
\[
\mathbb E\binom{Z_1}{3}=\frac23\quad\text{versus}\quad\frac43.
\]
For three species and four sites, compare
\[
(\{a,b,c\},\{a\},\{b\},\{c\})\quad\text{and}\quad(\{a,c\},\{a,b\},\{b,c\},\varnothing).
\]
At one site their shared-species lists are \((3,1,1,1)\) and \((2,2,2,0)\); at two sites both have three ones and three zeros; at larger samples they vanish. Their full mean-and-variance profiles agree, but their third binomial moments at one site are \(1/4\) and \(0\), respectively.

## Assumptions and scope
The community is a fixed binary species-by-site incidence matrix with \(N\) columns, \(S\) rows, and no all-zero row. Empty sites are permitted. Each \(k\)-subset is equally probable; sampling is without replacement, observations are perfect, and \(N,S\) are known. \(Z_k\) is common-species (intersection) richness, not pooled (union) richness. We use \(\binom{u}{r}=0\) for integers \(u<r\). All expectations are over the random subset of sites, not ecological dynamics.

## Proof
For species \(i\), let \(A_i\subseteq\{1,\ldots,N\}\) be its incidence set. Expanding the binomial coefficient of the number of species present on every selected site yields the identity
\[
\binom{Z_k}{r}=\sum_{I\subseteq\{1,\ldots,S\},\,|I|=r}\mathbf1\!\left\{W\subseteq\bigcap_{i\in I}A_i\right\}.
\]
For a fixed \(r\)-species set with intersection size \(t\), exactly \(\binom tk\) of the \(\binom Nk\) possible samples are contained in that intersection. Multiplying expectations by \(\binom Nk\) therefore gives the upper-triangular binomial transform
\[
F_r(k):=\binom Nk\mathbb E\binom{Z_k}{r}=\sum_{t=k}^N\binom tk H_r(t),\qquad 0\le k\le N.
\]
Its inverse follows from
\[
\sum_{k=t}^{u}(-1)^{k-t}\binom kt\binom uk=\mathbf1_{\{u=t\}},
\]
proved by \(\binom uk\binom kt=\binom ut\binom{u-t}{k-t}\) and the binomial theorem. This establishes the reconstruction formula, including \(t=0\) because \(Z_0=S\). The second factorial moment is available from mean and variance through
\[
\mathbb E\binom{Z_k}{2}=\frac{\operatorname{Var}(Z_k)+(\mathbb EZ_k)^2-\mathbb EZ_k}{2}.
\]
No higher histogram can be inferred *solely by this inversion* from moment orders below its own order; the two displayed witnesses prove concrete failure already at third order.

For the three-site witness, direct enumeration of all three single-site samples gives \((0,3,3)\) and \((1,1,4)\). Their raw means are both \(2\), their second raw moments both \(6\), and their third binomial moments are \(2/3\) and \(4/3\). Among the three two-site samples, each model has exactly one sample with a shared species; three-site intersections are empty. The four-site witness is checked analogously by listing its four singleton-site samples and six two-site samples. Thus both witnesses give distinct distributions with identical full mean-and-variance profiles.

For minimality, if \(S\le2\), every \(Z_k\) is supported on \(\{0,1,2\}\); its normalization, mean and second raw moment uniquely determine the three masses. If \(N\le2\), \(Z_1\) takes two equally weighted site-richness values, whose unordered pair is determined by its mean and variance; \(Z_2\) is deterministic. Now suppose \(N=3\) and \(S\le4\). For each sample order \(k=1,2\), the distribution of \(Z_k\) consists of three equally weighted integers between zero and four. Among the \(35\) unordered triples in \(\{0,1,2,3,4\}\), the *only* distinct triples with equal sums and equal sums of squares are \((0,3,3)\) and \((1,1,4)\); this is an exhaustive finite check also implemented in `verify.py`. For \(Z_2\), the triple \((0,3,3)\) cannot occur: two pairs of sites sharing three of at most four species force the third pair to share at least two. For \(Z_1\), if its triple is \((0,3,3)\), there are exactly four occurring species, and the two richness-three sites share exactly two species, giving \(Z_2\)-values \((2,0,0)\). If its triple instead is \((1,1,4)\), the two singleton sites either name the same species or different species, giving \(Z_2\)-values \((1,1,1)\) or \((1,1,0)\). Neither shares both first two moments with \((2,0,0)\). Hence identical complete first-two-moment profiles cannot conceal differing distributions with three sites and at most four species. Together the witnesses prove the claimed sharp boundaries. Every case with \(N+S\le6\) falls under \(N\le2\), \(S\le2\), or \(N=3,\ S\le3\), and hence is identifiable; the four-site three-species example achieves \(N+S=7\).

## Verification
`verify.py` is standalone Python standard-library code. Run `python verify.py` and compare its exact JSON stdout byte-for-byte with `certificate.json`. It enumerates all three-site binary incidence matrices with one through five nonempty species rows, checking \(94{,}773\) binomial-transform identities for the full range of moment orders and overlap sizes. It independently checks all \(2{,}800\) valid three-site incidence matrices with up to four species for absence of any first-two-moment ambiguity in the full law, checks the \(35\) possible bounded triples and both witnesses, and uses exact integers or rational arithmetic only. These finite tests support, but do not replace, the stated analytical inverse-transform proof and arbitrary-size minimality arguments.

## Relationship to prior work
Hui and McGeoch (2014) established the incidence-based zeta-diversity framework and formulas connecting its **mean** decline to occupancy-frequency profiles. The present result extends the identifiability question to factorial-moment curves of the **random** number of commonly occurring species. One can view the binomial inversion here as applying classical occupancy inversion to intersections of \(r\)-tuples; that elementary mechanism is acknowledged rather than portrayed as an entirely new transform. The additional substantive boundary is that even complete first-and-second moment curves can hide different shared-species distributions, at the proved smallest site and species thresholds.

Trejo-Barocio and Arita (2013) studied covariance of species and sites and variance-ratio summaries in neutral models. Arita (2015) developed multispecies overlap and co-diversity indices, including pairwise co-occurrence aggregation. Their inspected texts do not give the all-depth moment-to-intersection-histogram inverse together with the two sharp third-order information-loss witnesses. Prior work on co-detection covariance addresses pairs of named species rather than identification of the unlabeled histogram of all species-tuple intersections. These distinctions are about theorem implications, not titles.

## Limitations
Full sampling-depth curves are assumed known exactly, not estimated from sparse samples. Binomial inversion can amplify sampling noise, and there is no statistical error bound or numerical stability guarantee here. The recovered histograms are unlabeled aggregates, not full incidence-matrix reconstructions. Empty sites must be retained if included in the sampling frame. All sharpness witnesses are finite combinatorial communities, not field data; no mechanism of association or ecological causation follows. The novelty assessment remains subject to independent bibliographic review, especially because standard binomial inversion may have appeared in alternate combinatorial or ecological terminology.

## References
1. Hui, C., and McGeoch, M. A. (2014). *Zeta diversity as a concept and metric that unifies incidence-based biodiversity patterns*. The American Naturalist 184, 684–694. DOI: 10.1086/678125. First publicly available online 2014-09-24.
2. Trejo-Barocio, P., and Arita, H. T. (2013). *The co-occurrence of species and the co-diversity of sites in neutral models of biodiversity*. PLOS ONE 8, e79918. DOI: 10.1371/journal.pone.0079918.
3. Arita, H. T. (2015 online). *Multisite and multispecies measures of overlap, co-occurrence, and co-diversity*. Ecography 40, 709–718. DOI: 10.1111/ecog.01942. First published online 2015-11-19; journal issue 2017.
