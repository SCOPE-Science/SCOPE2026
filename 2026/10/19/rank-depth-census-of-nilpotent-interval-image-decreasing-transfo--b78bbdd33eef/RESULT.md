# Rank–depth census of nilpotent interval-image decreasing transformations

## Finding
For each integer \(n\ge2\), let \(M_n\) be the monoid of order-preserving maps \(f:\{1,\ldots,n\}\to\{1,\ldots,n\}\) with interval image and \(f(i)\le i\). Its zero \(z_n\) is the constant map with value \(1\). Write \(\mathcal N_n=\{f\in M_n:f^h=z_n\text{ for some }h\ge1\}\), and let \(\tau(f)\) be the least such positive \(h\). Define \(a_{n,k,h}\) to count elements of \(\mathcal N_n\) of image rank \(k+1\) and depth \(h\).

The complete rank–depth census is determined by the following exact, terminating integer recurrence (with out-of-domain entries and invalid binomial coefficients equal to zero):
\[
 a_{n,0,h}=\begin{cases}1,&h=1,\\0,&h\ne1,\end{cases}\qquad
 a_{n,k,h}=\sum_{j=0}^{k-1}\binom{n-k-1}{k-j}\,a_{k+1,j,h-1}
 \quad (1\le k\le n-2).
\]
Its nonzero support is characterized sharply: a rank \(r\in\{1,\ldots,n-1\}\) and depth \(h\ge1\) occur together if and only if
\[
 \boxed{\ \left\lceil\frac{n-1}{n-r}\right\rceil\le h\le r.\ }
\]
For \(r\ge2\), the number of maps attaining their largest possible depth \(h=r\) is precisely \(n-r\). At rank \(1\) there is just the zero map, of depth \(1\).

At the first nontrivial depth cutoff, the number of rank-\(r\) maps with depth at most \(2\) is
\[
 \binom{n-r}{r-1},\quad 1\le r\le n-1.
\]
Consequently their bivariate generating function is
\[
 \boxed{\ \sum_{n\ge2}x^n\sum_{\substack{f\in\mathcal N_n\\\tau(f)\le2}}u^{|\operatorname{im}f|}
 =\frac{u x^2(1+u x)}{1-x-u x^2}.\ }
\]
In particular, there are \(F_n\) such maps, where \(F_1=F_2=1\) are Fibonacci numbers; among all \(2^{n-2}\) nilpotent maps their proportion decays at exponential rate \((\varphi/2)^n\), where \(\varphi=(1+\sqrt5)/2\). These statements include all small-size boundary cases \(n\ge2\).

## Assumptions and scope
All maps act on the labeled chain \([n]=\{1,\ldots,n\}\). Composition is ordinary function composition, and \(f^h\) means \(h\) iterations of the same map. The rank here is **image cardinality**, not the minimum size of a monoid generating set. An interval image means every intermediate value between attained values is attained. As \(f\) is monotone, interval image is equivalent to every consecutive value difference being \(0\) or \(1\). The identity \(n=1\) has a degenerate zero-power convention and is excluded. The theorem concerns **full** order-decreasing interval-image maps, not partial transformations, and does not equate semigroup-element nilpotency depth with nilpotency class of the whole subsemigroup.

## Proof
**1. Zero-root normal form.** Every element \(f\in M_n\) has \(f(1)=1\), and monotonicity plus interval image imply
\[
 f(i+1)-f(i)\in\{0,1\}\quad(1\le i<n).
\]
Conversely any sequence beginning with \(f(1)=1\) and having those increments is a map in \(M_n\): the difference condition gives an interval image, monotonicity, and \(f(i)\le i\). There are therefore \(2^{n-1}\) elements. If \(f(2)=2\), then \(2\) is a fixed point and no power equals \(z_n\). If \(f(2)=1\), then \(f(i)\le i-1\) for every \(i\ge2\); repeated application strictly lowers every non-root state and eventually yields \(z_n\). Thus \(f\in\mathcal N_n\) exactly when the first increment is zero, leaving \(n-2\) independent binary increments and \(|\mathcal N_n|=2^{n-2}\).

The image of every \(f\in\mathcal N_n\) is \([r]\) for \(r=f(n)\), with \(r\le n-1\). As every iterate of a monotone map is monotone, the largest value at the \(t\)-th iteration is \(f^t(n)\). Therefore the least zero power equals the length of the strictly descending orbit
\[
 n=x_0>x_1=f(n)>\cdots>x_h=1.
\]

**2. Exact recurrence.** Put \(k=r-1\), the number of unit increments among the \(n-2\) free increments. When \(k=0\), the map is \(z_n\) and has depth one. For \(k\ge1\), restriction to the initial segment \([k+1]\) is again a zero-root map because every image lies in \([k+1]\). Let \(j\) be its number of unit increments, so \(0\le j\le k-1\), and let its depth be \(h-1\). Since \(f(n)=k+1\), the original depth is exactly one greater. Conversely, a chosen restricted map, with \(j\) unit increments, extends to an original map of rank \(k+1\) precisely by placing \(k-j\) unit increments among the \(n-k-1\) remaining positions. There are \(\binom{n-k-1}{k-j}\) choices. Summing disjointly over \(j\) proves the recurrence and its uniqueness by induction on \(n\). It also proves \(\sum_h a_{n,k,h}=\binom{n-2}{k}\), as independently follows from the binary normal form.

**3. The sharp attainable rank–depth region.** Let \(r=f(n)\), and define the defect \(\delta(i)=i-f(i)\). Its increments satisfy \(\delta(i+1)-\delta(i)\in\{0,1\}\), so \(\delta\) is nondecreasing, \(\delta(1)=0\), and \(\delta(n)=m=n-r\). Along the descending orbit in Step 1, put \(d_j=x_j-x_{j+1}=\delta(x_j)\). Then
\[
 m=d_0\ge d_1\ge\cdots\ge d_{h-1}\ge1,
 \qquad \sum_{j=0}^{h-1}d_j=n-1.
\]
The upper bound on each difference gives \(n-1\le hm\), while positivity after the first gives \(n-1\ge m+h-1\); these are the claimed bounds on \(h\).

For sufficiency suppose the displayed bounds hold. If \(h=1\), necessarily \(r=1\) and take \(z_n\). Otherwise distribute the integer \(r-1\) among \(h-1\) positive integers not exceeding \(m\), then arrange these in descending order \(d_1\ge\cdots\ge d_{h-1}\); this is possible precisely because \(h-1\le r-1\le(h-1)m\). Set \(d_0=m\) and \(x_0=n\), \(x_{j+1}=x_j-d_j\), so \(x_h=1\). Prescribe \(\delta(x_j)=d_j\) for \(0\le j<h\) and \(\delta(1)=0\). Between adjacent anchors, the required increase in \(\delta\) is nonnegative and no greater than the number of intervening unit steps: for \(j<h-1\) this says \(0\le d_j-d_{j+1}\le d_j\), and on the final segment it says \(d_{h-1}\le x_{h-1}-1=d_{h-1}\). Fill the remaining values with steps \(0\) or \(1\). The resulting \(f(i)=i-\delta(i)\) is in \(\mathcal N_n\), has rank \(r\), and maps each \(x_j\) to \(x_{j+1}\), giving depth \(h\). This establishes both necessity and attainability without a finite-experiment inference.

**4. The extreme depth stratum.** For rank \(r\ge2\), depth \(r\) means that after the first jump from \(n\) to \(r\), all further jumps are by exactly one. Thus \(f(t)=t-1\) for every \(2\le t\le r\). The first binary increment is zero and the next \(r-2\) increments are one. Since there are \(r-1\) unit increments in total, precisely one must lie in the \(n-r\) subsequent increment positions, giving \(n-r\) choices. At rank one only \(z_n\) occurs.

**5. Fibonacci shallow-depth boundary.** For \(r=k+1\ge2\), depth two occurs exactly when the restriction to \([k+1]\) in Step 2 is constant one, so \(j=0\). Its count is \(\binom{n-k-1}{k}=\binom{n-r}{r-1}\); the same binomial equals one for the rank-one zero when \(r=1\). Summing over ranks and then over \(n\), using \(\sum_{s\ge0}\binom{k+s}{k}x^s=(1-x)^{-k-1}\), yields
\[
 \sum_{n\ge2}x^n\sum_{r\ge1}u^r\binom{n-r}{r-1}
 = \frac{ux}{1-x-ux^2}-ux
 = \frac{u x^2(1+u x)}{1-x-u x^2}.
\]
Putting \(u=1\) gives \(x^2(1+x)/(1-x-x^2)=\sum_{n\ge2}F_nx^n\). The Binet formula and \(|\mathcal N_n|=2^{n-2}\) give the stated exponential rate.

## Verification
The bundled standalone \(checker.py\) uses exact integer arithmetic. It independently enumerates all monotone candidate maps on chains of sizes \(2\) through \(8\), checks the unique-zero-root characterization against the binary normal form, directly generates every zero-root map through size \(16\), and evaluates its powers by repeated composition. These coefficients agree with independently computed recurrence coefficients. The checker also verifies the complete attainable rank–depth region, the extreme-depth multiplicities, the Fibonacci cutoff, and the total nilpotent count through size \(32\); it returns `ALL_EXACT_CHECKS_PASSED`. Its exhaustive finite checks corroborate but do not replace the uniform proof above.

The total depth histograms at sizes \(5\), \(8\), and \(12\) are respectively \((1,4,2,1)\), \((1,20,23,12,5,2,1)\), and \((1,143,360,269,139,64,28,12,5,2,1)\), indexed by depths starting at one.

## Relationship to prior work
Fernandes (arXiv:2407.05084, first posted 6 July 2024; later Semigroup Forum 109) identifies \(M_n\) as the order-decreasing interval-image monoid and establishes its size, monoid rank, and presentation. Fernandes and Paulista (arXiv:2112.13427) identify the encompassing interval-image monoid with weak endomorphisms of a directed path and determine its size, regular elements, idempotents and generating rank. These structural descriptions are used as context, not claimed as new.

Koppitz and Worawiset (2022) consider the larger semigroup of all order-preserving full maps with a unique fixed point, focusing on generating rank and presentation. Ayık, Fernandes, and Korkmaz (arXiv:2503.19459, 2025) count nilpotents of a different, partial-map monoid with the empty partial map as zero. Neither result inspected supplies the exact zero-root rank–depth coefficients, their sharp attainable region, or the Fibonacci rank-refined cutoff for the full interval-image decreasing monoid. The scalar Fibonacci sequence is classical: no novelty is claimed for the number sequence independently of this monoid interpretation.

## Limitations
This theorem is restricted to full maps with interval image and order-decreasing condition. It does not classify the nilpotency depths of all order-preserving maps or partial maps. The recurrence is an exact finite computation for any \(n\), not a closed elementary formula for every individual depth stratum. Search and document inspection do not guarantee absence of an equivalent treatment under different terminology; in particular older transformation-semigroup literature may contain a stronger power-distribution theorem not found here. Independent audit has not been performed.

## References
1. V. H. Fernandes, *On the monoid of order-preserving transformations of a finite chain whose ranges are intervals*, arXiv:2407.05084 (first posted 2024-07-06), https://arxiv.org/abs/2407.05084; Semigroup Forum 109 (2024), 336–346, https://doi.org/10.1007/s00233-024-10466-2.
2. V. H. Fernandes and T. Paulista, *On the Rank of Monoids of Endomorphisms of a Finite Directed Path*, arXiv:2112.13427 (first posted 2021-12-26), https://arxiv.org/abs/2112.13427.
3. J. Koppitz and S. Worawiset, *Ranks and presentations for order-preserving transformations with one fixed point*, Turkish Journal of Mathematics 46 (2022), 3408–3418, https://doi.org/10.55730/1300-0098.3341.
4. H. Ayık, V. H. Fernandes, and E. Korkmaz, *On the monoid of partial order-preserving transformations of a finite chain whose domains and ranges are intervals*, arXiv:2503.19459 (2025), https://arxiv.org/pdf/2503.19459.
