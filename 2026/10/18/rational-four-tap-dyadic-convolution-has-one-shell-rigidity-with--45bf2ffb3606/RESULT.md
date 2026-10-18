# Rational four-tap dyadic convolution has one-shell rigidity, with irrational two-shell resonances

## Finding
Let \(N=2^k\) with \(k\ge3\). Let \(x_1,x_2,x_3,x_4\) be distinct residues in \(\mathbb Z/N\mathbb Z\), and let \(a_1,a_2,a_3,a_4\in\mathbb Q_{>0}\). On complex functions define the convolution operator
\[
(Tf)(y)=\sum_{i=1}^4 a_i f(y-x_i).
\]
For \(1\le r\le k\), write \(h_r=2^{r-1}\) and
\[
M_r(t)=\sum_{x_i\equiv t\pmod {2^r}}a_i,\qquad 0\le t<2^r.
\]
Then the complete nullity formula is
\[
\dim_{\mathbb C}\ker T
=\sum_{r=1}^k 2^{r-1}\mathbf1\{M_r(t)=M_r(t+h_r)\text{ for every }0\le t<h_r\}.
\]
Every nonzero Fourier zero occurs in an entire conductor shell. If the four coefficients are not all equal, **at most one shell can vanish**. Consequently the nullity is zero or one of \(1,2,4,\ldots,N/2\), and the bound \(N/2\) is sharp. Equality \(\dim\ker T=N/2\) holds exactly when the four sites form two antipodal pairs \(\{u,u+N/2\},\{v,v+N/2\}\), with equal coefficients within each pair and unequal coefficients between the pairs.

If the coefficients are all equal, at most two shells vanish, the sharp maximum is \(3N/4\), and equality holds exactly when the sites form a coset of the unique order-four subgroup of \(\mathbb Z/N\mathbb Z\). Each value \(0,1,2,4,\ldots,N/2\) occurs for some choice of unequal positive rational coefficients and four sites.

The rationality restriction marks a genuine boundary: for each \(N\) divisible by eight, the four sites \(\{0,N/8,N/4,3N/8\}\), equipped in this order with positive real weights \((1,1+\sqrt2,1+\sqrt2,1)\), have exactly \(3N/8\) Fourier zeros, located at frequencies \(j\equiv3,4,5\pmod8\). They lie in **two distinct conductor orders** \(N\) and \(N/4\), while the weights are not all equal. In particular, rational shell rigidity is not a general positive-real statement.

## Assumptions and scope
All computations take place over \(\mathbb C\), with unnormalized cyclic Fourier characters \(\chi_j(x)=\exp(2\pi i jx/N)\). For the rigidity and nullity-classification assertions, weights are strictly positive rationals; no integrality or normalization is assumed. The irrational construction deliberately replaces rationality by positivity over \(\mathbb R\). Sites are pairwise distinct modulo \(N\); translated sites and common rescaling do not affect nullity. The theorem does not assert a classification of arbitrary positive-real four-tap filters.

## Proof
**Cyclotomic shell lemma.** For a frequency \(j\ne0\), write its additive-character order as \(Q=N/\gcd(N,j)=2^r\). Then \(j/(N/Q)\) is odd. The corresponding eigenvalue is \(\sum_t M_r(t)\zeta_Q^{ut}\), with \(u\) odd and \(\zeta_Q=\exp(2\pi i/Q)\). Over \(\mathbb Q\), the minimal polynomial of \(\zeta_Q^u\) is \(\Phi_Q(z)=z^{Q/2}+1\). Reducing \(\sum_{0\le t<Q}M_r(t)z^t\) modulo this polynomial gives the unique remainder
\[
\sum_{0\le t<h_r}\bigl(M_r(t)-M_r(t+h_r)\bigr)z^t.
\]
It vanishes at one primitive \(Q\)-th root if and only if the remainder polynomial is identically zero. Thus either every frequency of order \(Q\) vanishes or none does. There are \(\varphi(Q)=2^{r-1}\) such frequencies. At \(j=0\) the eigenvalue is \(\sum_i a_i>0\), proving the displayed nullity formula.

**Two-shell rigidity.** Suppose shells of orders \(2^r\) and \(2^s\) vanish with \(s<r\). Positivity and the mass-matching condition at level \(r\) imply that the four sites occupy either one or two opposite residue pairs modulo \(2^r\): every occupied pair must contain at least one site in each half, and there are four sites total. If just one opposite pair is occupied, all four residues coincide modulo \(2^s\) because \(2^{r-1}\) is divisible by \(2^s\). Their total positive mass cannot cancel at order \(2^s\). Thus two distinct opposite pairs are occupied, each by exactly two sites, one at each endpoint. The level-\(r\) condition forces the two weights in the first pair to equal some \(\alpha>0\) and those in the second to equal \(\beta>0\).

At level \(s\), the two points in each level-\(r\) opposite pair coincide. Hence the level-\(s\) Fourier eigenvalue has the form \(2\alpha\zeta_{2^s}^{ua}+2\beta\zeta_{2^s}^{ub}\). Its vanishing implies \(\alpha=\beta\) from absolute values. Therefore all four original weights agree. Moreover, when they agree, the only possible lower shell requires \(\zeta_{2^s}^{u(a-b)}=-1\), equivalently \(v_2(a-b)=s-1\) for the two different residue classes modulo \(2^r\). Here \(a,b\) denote representatives of the two opposite pairs, considered modulo \(2^{r-1}\); their difference has a well-defined valuation below \(r-1\). Hence there is at most one lower shell, establishing the two-shell maximum.

**Extremizers and attainability.** A single conductor shell contributes at most \(2^{k-1}=N/2\). When unequal weights reach this value, the sole vanishing shell must be of order \(N\). Since all four sites are distinct modulo \(N\), its mass-matching consists of two distinct antipodal pairs, and the paired weights agree separately. Conversely, such pairs with different respective weights have the full primitive shell and no other shell by the rigidity just proved.

With equal weights, two shells together contribute at most \(2^{k-1}+2^{k-2}=3N/4\). Equality forces orders \(N\) and \(N/2\). The upper-order antipodal pairs must have their representatives separated by \(N/4\) modulo \(N/2\), so their union is exactly \(u+\{0,N/4,N/2,3N/4\}\). Conversely this four-point subgroup coset annihilates precisely those characters that are nontrivial on its order-four subgroup, giving \(3N/4\) zeros.

For every \(1\le r\le k\), put \(h=2^{r-1}\), take sites \(\{0,h,t,t+h\}\) with \(t=2^r\) for \(r<k\) and \(t=1\) for \(r=k\), and assign coefficients \(\alpha,\alpha,\beta,\beta\) to the corresponding listed sites, with distinct positive rationals \(\alpha,\beta\). The shell of order \(2^r\) vanishes; rigidity rules out all other shells. This yields nullity \(2^{r-1}\). The weight tuple \((1,2,4,8)\) has no nonempty equal-sum partition, hence no matching opposite-pair masses at any conductor, giving nullity zero on any distinct four sites.

**Irrational boundary.** Writing \(q=N/8\), the Fourier multiplier at frequency \(j\) is the cubic polynomial
\[
P(z)=1+(1+\sqrt2)z+(1+\sqrt2)z^2+z^3
=(z+1)(z^2+\sqrt2 z+1),\quad z=e^{2\pi i j/8}.
\]
Among the eighth roots of unity the roots are exactly \(-1,e^{3\pi i/4},e^{5\pi i/4}\). Thus precisely the residue classes \(j\equiv4,3,5\pmod8\) vanish, each represented \(N/8\) times. The two odd classes have conductor \(N\) and the class \(4\) has conductor \(N/4\), proving the stated \(3N/8\) nullity and the failure of rational full-shell rigidity.

## Verification
The accompanying `dyadic_weighted_check.py` performs exact rational cyclotomic remainder reduction for every four-point support at \(N=8,16,32\) with five representative weight patterns, checks the predicted sharp maxima and equality supports, and cross-checks randomly selected cases against independently evaluated complex Fourier sums and direct per-frequency exact reduction. It also checks the irrational polynomial factorization symbolically and verifies the three residue classes for \(N=8,16,32,64\). All checks completed successfully. The unrestricted statements rest on the algebraic proof above; finite tests are corroboration, not an infinite certificate.

## Relationship to prior work
The cyclotomic-remainder step is a direct specialization of the classical dyadic kernel structure developed by Lam and Leung (1995, Theorem 3.3; see also the earlier Rédei–de Bruijn–Schoenberg theorem). That established theory already covers positive rational root-of-unity cancellation. A published classification of zero shells for **unweighted four-point indicators** covers the equal-weight component. The distinction here is the support-four consequence for arbitrary **positive rational** coefficients, its sharp weighted nullity and equality boundary, and the explicit positive irrational family with simultaneous zeros in distinct conductor orders and an incomplete primitive shell. General Fourier uncertainty estimates, including those surveyed by Krahmer, Pfander, and Rashkov, concern support bounds but do not provide this rational-versus-irrational conductor classification. The 2002 study of four-regular undirected circulant graphs concerns symmetric unweighted generating sets, not arbitrary positive four-tap convolutions.

## Limitations
The result assumes four distinct taps and positivity. The rational coefficient case is strongly informed by classical cyclotomic group-ring structure rather than introducing a new cyclotomic kernel lemma. An equivalent application to rational weighted four-tap circulants or the positive irrational example may exist in older filter or circulant literature; no publication-priority claim is made. The example demonstrates failure of conductor-shell rigidity over positive reals, not failure of the same numerical \(N/2\) upper bound for all positive-real weights. No statement is made for arbitrary real coefficient choices or other prime-power moduli.

## References
1. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209v1, publicly posted November 13, 1995; *Journal of Algebra* 224 (2000), 91–109; especially Theorem 3.3 (preprint p. 7). https://arxiv.org/pdf/math/9511209
2. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1, posted November 16, 2006; Sections 2–3. https://arxiv.org/abs/math/0611493
3. *Dyadic shell classification of Fourier zeros for four-point indicators*, published mathematical record, October 2026, identifier `68cf8ce2dd05` (equal-weight case); its accessible summary was compared, while the full text was unavailable.
4. *4-Circulant Graphs*, *Journal of Combinatorial Mathematics and Combinatorial Computing* 65 (2002), 97–110; see the symmetric four-regular graph scope. https://combinatorialpress.com/ars-articles/volume-065-ars-articles/4-circulant-graphs/
