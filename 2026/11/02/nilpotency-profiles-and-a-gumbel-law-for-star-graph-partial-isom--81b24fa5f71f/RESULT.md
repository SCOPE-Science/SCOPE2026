# Nilpotency profiles and a Gumbel law for star-graph partial isometries

## Finding
Let \(S_{m+1}=K_{1,m}\) be the undirected star with center \(0\), leaves \(1,\ldots,m\), and \(m\ge2\). Let \(D_m\) be the inverse monoid of distance-preserving partial bijections of the vertex set, with the empty map as zero. For a nilpotent \(f\in D_m\), define its index \(\kappa(f)\) by \(f^{\kappa(f)}=0\) and \(f^{\kappa(f)-1}\ne0\). Its rank is its domain size. Write \(C_m(r,k)\) for the number of elements of rank \(r\) and nilpotency index \(k\).

For \(L\ge1\) put
\[
H_{m,L}(u)=m![z^m]\exp\left(\sum_{j=1}^{L}u^{j-1}z^j\right),\qquad H_{m,0}(u)=0.
\]
Then for all integers \(r\ge0\) and \(k\ge1\),
\[
\boxed{C_m(r,k)=[u^r]\bigl(H_{m,k}(u)-H_{m,k-1}(u)\bigr)
       +2m\,\mathbf1_{(r,k)=(1,2)}
       +m(m-1)\,\mathbf1_{(r,k)=(2,3)}.}
\]
In particular, every nilpotent that moves the center belongs to one of exactly two exceptional types: a singleton arrow between center and leaf (index \(2\)), or a three-vertex arrow chain with the center in the middle (index \(3\)). All other nilpotents act exclusively on the leaf set.

Summing over the index yields the complete rank profile
\[
\boxed{\sum_k C_m(r,k)=\binom mr\binom{m-1}r r!
+2m\,\mathbf1_{r=1}+m(m-1)\,\mathbf1_{r=2},}
\]
where the binomial coefficient vanishes outside its standard range. The number of nilpotents and the monoid order are respectively
\[
\boxed{\#\operatorname{Nil}(D_m)=m![z^m]\exp\!\left(\frac z{1-z}\right)+m(m+1),}
\]
\[
\boxed{|D_m|=2m![z^m]\frac{\exp(z/(1-z))}{1-z}+m^2+2m.}
\]
Therefore a uniformly random element of \(D_m\) is nilpotent with probability asymptotic to \(1/(2\sqrt m)\).

A further limit theorem describes a uniformly random **nilpotent** \(F_m\in D_m\). For every fixed real \(x\),
\[
\boxed{\lim_{m\to\infty}\Pr\!\left\{\frac{\kappa(F_m)-\tfrac12\sqrt m\log m}{\sqrt m}\le x\right\}
=\exp(-e^{-x}).}
\]
Thus its nilpotency index has the Gumbel extreme-value limit, at scale \(\sqrt m\) around \(\tfrac12\sqrt m\log m\).

## Assumptions and scope
The monoid uses the **ambient star-graph distance**, not a path metric on an induced subgraph. Composition is the usual composition of partial functions. The star has \(m+1\) distinct labeled vertices, and \(m\ge2\); the limiting statements let \(m\to\infty\). An isolated singleton of the directed path decomposition counts as a component of length \(1\); this makes the empty partial map have index \(1\). All coefficients are ordinary formal power-series coefficients and all factorials are taken over the integers. No statement is made about arbitrary graph partial-isometry monoids or about products of distinct nilpotent elements.

## Proof
**1. Classification by the center.** For any subset of at least three star vertices that contains the center, the center is the unique point at distance \(1\) from all other selected vertices (or, equivalently, the unique point with two distance-one neighbors). Its image under an isometry must also be the center. For a subset contained entirely in the leaves, all nonzero mutual distances are \(2\), and its image must also be leaf-only when its size is at least two. All leaf-to-leaf partial bijections are isometries, with no further restrictions. A one-point partial isometry may move a leaf to the center or vice versa. A two-point partial isometry on a center-leaf pair may either fix the center or exchange its role with the leaf; exactly \(m^2\) such exchanged-role maps exist, indexed by their domain leaf and image leaf. Hence the monoid is the disjoint union of two copies of the symmetric inverse monoid on \(m\) leaves (one center absent, the other center fixed), together with \(2m\) center-moving singletons and \(m^2\) exchanged-role two-point maps. This proves the order formula, using the standard partial-injection EGF established in Step 4.

**2. Which elements are nilpotent?** The center-fixed copy has no nilpotent elements because \(0\) is a fixed point. A center-moving singleton has one arrow and index \(2\). An exchanged-role two-point map sends \(a\mapsto0\mapsto b\). When \(a=b\), it is a two-cycle and not nilpotent. When \(a\ne b\), it is a length-three directed path and has index \(3\), giving \(m(m-1)\) elements. These cases are disjoint. A leaf-only partial injection is nilpotent exactly when its functional digraph has no cycles, in which case it is a disjoint union of directed paths.

**3. Exact index and rank.** A directed path on \(j\) labeled vertices has \(j!\) orientations/linear orders and contributes \(j-1\) arrows to the rank. The exponential formula for an unordered set of labeled directed paths of lengths at most \(L\) gives \(\exp(\sum_{j=1}^L u^{j-1}z^j)\). Its \(m\)-vertex coefficient counts precisely the nilpotent leaf maps of rank marked by \(u\) and index at most \(L\). Taking the difference between successive cutoffs and adding the two center-moving types proves the first formula. For the rank-only formula, a nilpotent leaf map of rank \(r\) has \(m-r\) path components. Order all \(m\) labels, choose \(m-r-1\) of the \(m-1\) inter-label cuts, and divide by \((m-r)!\) to forget the ordering of the components. This gives \(m!\binom{m-1}{r}/(m-r)!=\binom mr\binom{m-1}r r!\). The assertion also holds at \(r=0\). Adding center-moving terms proves the rank formula.

**4. Unmarked generating functions.** Summing the path species over all positive path lengths gives \(A(z)=\exp(z/(1-z))\); its coefficient \(m![z^m]A(z)\) counts all nilpotent leaf maps. A general partial injection decomposes into disjoint directed paths and directed cycles. The directed-cycle component EGF is \(\exp(\sum_{j\ge1}z^j/j)=1/(1-z)\), so the EGF for every partial injection is \(B(z)=A(z)/(1-z)\). This proves both total-count identities.

**5. Local limit estimate.** Write \(\rho=\rho_m\in(0,1)\) for the unique solution of \(\rho/(1-\rho)^2=m\). Let \(Z_j\) be independent Poisson random variables of means \(\rho^j\), and let \(S=\sum_{j\ge1}jZ_j\). Then \(\mathbb ES=m\) and
\[
\operatorname{Var}(S)=\frac{\rho(1+\rho)}{(1-\rho)^3}\sim2m^{3/2},
\qquad 1-\rho\sim m^{-1/2}.
\]
A local central limit estimate, also valid when the sum is restricted to \(j\le L_m\) with \(L_m\sim\tfrac12\sqrt m\log m\), gives a Gaussian mass uniformly at deviations \(o(m^{3/4})\) from the respective mean. For completeness: use Fourier inversion, expand the cumulant generating function for \(|t|\le m^{-3/4}\log m\), and note that the third cumulant is \(O(m^2)\), so the cubic remainder is \(o(1)\). Outside this range, the first \(\lfloor\sqrt m\rfloor\) Poisson terms yield a Fourier-modulus bound \(\exp[-c\min(m^{3/2}t^2,\sqrt m)]\) uniformly for \(|t|\le\pi\). The same initial terms occur in the truncated sum; the omitted variance for the stated cutoff is \(O(m(\log m)^2)=o(m^{3/2})\). Consequently the same local Gaussian approximation applies to both sums.

Under the conditioning \(S=m\), the path multiplicities \((Z_j)\) have exactly the distribution of the component counts of a uniformly random nilpotent leaf partial injection. Fix real \(x\), put \(L_m=\lfloor\sqrt m(\tfrac12\log m+x)\rfloor\), and let \(E_m\) be the event that all \(Z_j\) with \(j>L_m\) are zero. Independence gives
\[
\Pr(E_m)=\exp\left(-\sum_{j>L_m}\rho^j\right)
=\exp\left(-\frac{\rho^{L_m+1}}{1-\rho}\right)\longrightarrow\exp(-e^{-x}).
\]
The omitted expected size is \(O(\sqrt m\log m)=o(m^{3/4})\); the local limit estimate therefore implies \(\Pr(S=m\mid E_m)/\Pr(S=m)\to1\). Thus \(\Pr(E_m\mid S=m)\to\exp(-e^{-x})\), proving the Gumbel limit for leaf-only nilpotents. The \(m(m+1)\) exceptional center-moving nilpotents are negligible because the leaf-only family contains at least \(m!\) directed full paths. Hence the same limit holds for a uniform nilpotent of \(D_m\).

**6. Nilpotent density.** The same local limit estimate gives \([z^m]B(z)/[z^m]A(z)\sim(1-\rho)^{-1}\sim\sqrt m\). One way to see this is to add an independent geometric random variable \(Y\) with \(\Pr(Y=j)=(1-\rho)\rho^j\) to \(S\): the ratio of these coefficients equals \((1-\rho)^{-1}\Pr(S+Y=m)/\Pr(S=m)\). Since \(Y=O_{\Pr}(\sqrt m)\) and \(S\) has fluctuations of order \(m^{3/4}\), the probability ratio tends to one by the local limit estimate. The polynomial center-correction terms are negligible compared with \(m!\), so the displayed exact counts give \(\Pr\{f\in D_m:f\text{ nilpotent}\}\sim1/(2\sqrt m)\).

## Verification
The accompanying `verify_star_nilpotents.py` independently lists every partial injection on a labeled star of \(m+1\) vertices, checks pairwise ambient distances, calculates powers of each admitted map through the finite maximum possible nilpotency index, and tabulates the rank-index profile. For \(m=1,2,3,4,5\) it agrees exactly with the coefficient formula, the rank totals, and the total monoid orders; the verifier prints `VERIFY_OK`. These finite checks are not the proof of the all-\(m\) formulas or of the extreme-value limit. The proof is combinatorial and analytic as given above.

## Relationship to prior work
Fernandes and Paulista, *On the monoid of partial isometries of a finite star graph* (arXiv:2203.05504, first public 2022-03-10), study this monoid's rank, presentation, Green relations and cardinality. Its structural and counting context is prior work, not a claimed discovery here. Dimitrova, Fernandes and Koppitz (arXiv:2401.11741, first public 2024-01-22) address several larger partial-endomorphism monoids of stars. Ganyushkin and Mazorchuk's *Combinatorics and distributions of partial injections* (arXiv:math/0511431, 2005) studies chain and cycle statistics and growth in the unrestricted symmetric inverse semigroup; Laradji and Umar (2004) address its nilpotent counts. The present claim is confined to the exact joint star-isometry rank/index law, the center-forbidden corrections, and the resulting density and extreme-value law; it does not claim the pre-existing partial-injection combinatorics or the general star-monoid normal form as novel.

## Limitations
The statement applies only to star ambient-metric partial isometries, not to arbitrary graph homomorphisms. The high-level abstract and bibliographic material of the particularly relevant 2022 star paper and the 2005 partial-injection study were accessible, but their complete manuscripts could not be inspected during this comparison. Consequently an equivalent full rank-index formula, or a prior extreme-value result in the earlier partial-injection literature, remains a real originality risk. The asymptotic terms are leading-order only; no uniform convergence rate is claimed. Independent external mathematical validation has not been performed.

## References
1. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a finite star graph*, arXiv:2203.05504 (2022); DOI:10.1080/00927872.2022.2121404.
2. I. Dimitrova, V. H. Fernandes and J. Koppitz, *On partial endomorphisms of a star graph*, arXiv:2401.11741 (2024).
3. O. Ganyushkin and V. Mazorchuk, *Combinatorics and distributions of partial injections*, arXiv:math/0511431 (2005), Australasian Journal of Combinatorics 34 (2006), 161–186.
4. A. Laradji and A. Umar, *On the number of nilpotents in the partial symmetric semigroup*, Communications in Algebra 32 (2004), 3017–3023; DOI:10.1081/AGB-120038637.
