# Exact extremal inverse neighborhoods in order-preserving transformation monoids

## Finding

Let \(\mathcal O_n\) be the monoid of all weakly increasing maps of the chain \([n]=\{1,\dots,n\}\) to itself, with multiplication by composition. For \(f\in\mathcal O_n\), define its semigroup inverse neighborhood
\[
V(f)=\{g\in\mathcal O_n:f\circ g\circ f=f,\quad g\circ f\circ g=g\}.
\]
Put \(M_n=\max_{f\in\mathcal O_n}|V(f)|\) and let \(E_n\) denote the number of \(f\) attaining this maximum. The following formulas hold exactly:
\[
\begin{array}{c|c|c}
n&M_n&E_n\\\hline
1&1&1\\
2&2&2\\
3&4&2\\
3m\ (m\ge2)&16\cdot3^{2m-3}&\binom{m-1}{2}+m\binom{m+1}{3}\\
3m+1\ (m\ge1)&4\cdot3^{2m-1}&\binom{m+1}{2}\\
3m+2\ (m\ge1)&8\cdot3^{2m-1}&m(m+1)
\end{array}
\]
where \(\binom{m-1}{2}=0\) if \(m=2\). For \(n\ge4\), \(M_{n+3}=9M_n\), and hence \(\lim_{n\to\infty} M_n^{1/n}=9^{1/3}\). Maximizing transformations have rank \(m+1\) when \(n=3m+1\) or \(3m+2\), rank \(m\) or \(m+1\) when \(n=3m\ge9\), rank \(3\) when \(n=6\), and rank \(2\) when \(n=3\). At \(n=2\) the maximizers are the two constant maps.

More precisely, if \(f\) has rank \(r\), consecutive nonempty kernel blocks of lengths \(a_1,\ldots,a_r\), and increasing image \(b_1<\dots<b_r\), then
\[
|V(f)|=\left(\prod_{i=1}^{r}a_i\right)\left(\prod_{i=1}^{r-1}(b_{i+1}-b_i)\right),
\]
with empty products equal to one. In particular, among rank-\(r\) maps the maximum inverse degree is \(n\) when \(r=1\), and otherwise
\[
B(n,r)B(n-1,r-1),\qquad
B(N,k)=\left\lfloor\frac Nk\right\rfloor^{k-s}
\left\lceil\frac Nk\right\rceil^{s},\quad s=N-k\left\lfloor\frac Nk\right\rfloor.
\]
The number of **ordered** mutually inverse pairs \((f,g)\) of common rank \(r\) is exactly
\[
\boxed{\binom{n+r-1}{2r-1}^{2}}.
\]
These are counts of concrete order-preserving transformations, not counts modulo conjugation or automorphisms.

## Assumptions and scope

All integers \(n\ge1\) and ranks \(1\le r\le n\) are included. A semigroup inverse is **not** required to be a two-sided functional inverse, and the identities \(fgf=f\) and \(gfg=g\) are both essential. A rank-\(r\) isotone map is uniquely described by an ordered interval partition of \([n]\) into \(r\) nonempty fibers and an increasing \(r\)-element image. Products and powers in this document have their usual integer meanings; the empty-product convention covers rank one.

## Proof

**1. Exact inverse neighborhoods.** Let the intervals \(A_1<\cdots<A_r\) be the kernel blocks of \(f\), with \(f(A_i)=\{b_i\}\). If \(g\) is a semigroup inverse of \(f\), then \(D=\operatorname{im}(g)\) must be a transversal of these intervals: the equation \(fgf=f\) forces one point of \(D\) in each \(A_i\). Conversely such a transversal makes \(fg\) act as required on the image of \(f\). Likewise, \(gfg=g\) forces each \(b_i\) to lie in the corresponding interval kernel block of \(g\), and this condition is sufficient. In particular, \(g\) has rank \(r\) and is uniquely determined by its kernel and image. The \(r\) choices of a transversal point of \(A_i\) are independent, giving \(\prod_i a_i\) possible images of \(g\). Its kernel cuts \(c_i\) satisfy independently \(b_i\le c_i<b_{i+1}\), providing \(\prod_i(b_{i+1}-b_i)\) kernels. This proves the displayed neighborhood formula for all \(r\), including \(r=1\).

**2. Fixed-rank optimization.** For any positive \(k\)-tuple with sum \(N\), replacing a pair \((u,v)\) with \(u\ge v+2\) by \((u-1,v+1)\) strictly increases the product. Thus the maximal product is \(B(N,k)\), achieved precisely when all parts differ by at most one. For \(r\ge2\), the consecutive image gaps are positive and have sum \(b_r-b_1\le n-1\). Any unused endpoint slack can be added to a gap, strictly improving the product, so a maximizer has \(b_1=1\), \(b_r=n\), and balanced gaps. This proves the fixed-rank maximum. It also shows that its number of attaining maps is
\[
\binom{r}{s}\binom{r-1}{t},\quad
s=n-r\lfloor n/r\rfloor,\quad
t=n-1-(r-1)\lfloor(n-1)/(r-1)\rfloor.
\]
For rank one, all \(n\) constant maps have inverse degree \(n\).

**3. Global optimization.** We use the elementary integer-break fact: the largest product of arbitrary positive integer parts summing to \(N\ge2\) is
\[
J(N)=\begin{cases}
3^h&N=3h,\\
4\cdot3^{h-1}&N=3h+1\ (h\ge1),\\
2\cdot3^h&N=3h+2.
\end{cases}
\]
Indeed no optimal decomposition uses a part one (except \(N=1\)); a part at least five can be improved by splitting off a three; and three twos can be replaced by two threes. The remaining parts are twos and threes, allowing a four in place of two twos. The resulting maximizing part patterns are characterized by these replacements.

For \(n=3m+1\), the rank-dependent product is at most \(J(3m+1)J(3m)=4\cdot3^{2m-1}\). It attains the bound at rank \(m+1\): the kernel lengths are two twos and \(m-1\) threes, and the \(m\) image gaps are all threes. This rank is the only one giving equality, because the second factor \(J(3m)\) requires exactly \(m\) threes. For \(n=3m+2\), the bound is \(J(3m+2)J(3m+1)=8\cdot3^{2m-1}\). It is attained uniquely in rank \(m+1\), by \(m\) threes and one two in the kernel, and \(m-1\) threes and one four among the gaps.

For \(n=3m\) with \(m\ge3\), distinguish ranks \(r\le m\) and \(r\ge m+1\). If \(r\le m\), then the image has \(r-1\le m-1\) gaps. A product of \(3m-1\) positive parts is nondecreasing as its number of parts increases from one to \(m-1\): until that threshold there is a part of size at least four, which can be split into \(2\) and the remainder without decreasing the product. Hence
\[
B(3m-1,r-1)\le B(3m-1,m-1)=16\cdot3^{m-3}.
\]
Together with \(B(3m,r)\le J(3m)=3^m\), this gives the bound \(16\cdot3^{2m-3}\). Equality in the first case occurs only at \(r=m\), with all kernel lengths three and two gaps four (all others three). If \(r\ge m+1\), increasing the number of parts past \(m+1\) cannot increase the maximal product for a sum of \(3m\): at least two parts of size at most two may be merged without decreasing the product. Consequently
\[
B(3m,r)\le B(3m,m+1)=8\cdot3^{m-2}.
\]
The second factor is at most \(J(3m-1)=2\cdot3^{m-1}\), giving the same bound. Equality in this case occurs only at \(r=m+1\), with three kernel lengths two (others three) and one gap two (others three). The cases \(n=3\) and \(n=6\) follow by inspecting the two or three possible small ranks, including rank one.

**4. Count of extremizers.** In each maximizing rank the number of orderings of a fixed multiset of balanced kernel lengths times the number of orderings of its balanced image gaps counts the maximizing maps. When \(n=3m+1\), this is \(\binom{m+1}{2}\). When \(n=3m+2\), it is \((m+1)m\). When \(n=3m\ge9\), the two maximizing ranks contribute respectively \(\binom{m-1}{2}\) and \(m\binom{m+1}{3}\); when \(n=6\) the latter contributes two. Direct small-rank evaluation gives the three initial rows of the theorem. The recurrence and exponential growth constant follow immediately.

**5. Rankwise inverse-pair count.** Sum \(|V(f)|\) over all rank-\(r\) maps, using the independent kernel-length and image-gap factors from step 1. The weighted sum over positive compositions \(a_1+\cdots+a_r=n\) equals the coefficient of \(x^n\) in \((x/(1-x)^2)^r\), namely \(\binom{n+r-1}{2r-1}\). For the image factor, write the initial and terminal unused positions as two nonnegative integers, and the \(r-1\) positive gaps as before. The weighted generating function is \((1-x)^{-2}(x/(1-x)^2)^{r-1}\); its coefficient at \(x^{n-1}\) is the same binomial coefficient. These independent sums multiply to its square. Rank one obeys the same identity by direct counting, since every constant map has \(n\) constant inverses.

## Verification

A standalone script `check_inverse_extremal.py` uses direct composition, not Green's-relation formulas, to test both inverse identities for every pair of isotone maps for \(1\le n\le6\). It separately reconstructs the block-gap formula, rankwise pair counts, global maxima, and numbers of maximizers. It then checks the symbolic rank-bound and maximizer-count formulas for every integer \(2\le n\le500\). The last line is `VERIFY_OK`. Direct exhaustive finite tests do not establish the all-\(n\) theorem; its proof is above.

Observed maxima \(M_n\) for \(n=1,\ldots,6\) are \(1,2,4,12,24,48\). The corresponding numbers \(E_n\) are \(1,2,2,1,2,2\), and the total counts of ordered inverse pairs are \(1,5,26,153,931,5794\).

## Relationship to prior work

Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings* (arXiv:2610.01912v1, publicly submitted 2026-10-01), proves existence of a permutation matching for every \(\mathcal O_n\). Its Section 3 identifies kernel/image parametrizations and the transversal incidence of inverses; Section 2 introduces the crossed-square relation. Those are essential prior structural tools and imply the possibility of deriving local inverse counts, but its statements do not give the global maximum, maximizing-rank congruence law, extremizer census, or rankwise inverse-pair numbers. The present result asks a distinct quantitative question motivated by the nonregular inverse graph that the paper handles using balanced weights.

Higgins (2024), *Finite regular semigroups with permutations that map elements to inverses*, discusses existence and regular inverse-graph matchings, including an earlier open question about \(\mathcal O_n\), not this exact degree optimization. Higgins (2014), *Permutations of a semigroup that map to inverses*, studies matching existence and inverse graphs; neither inspected result supplies the new enumerative formulas. The accessible abstract of Higgins (1993), *Combinatorial results for semigroups of order-preserving mappings*, concerns the same ambient monoid, but the complete article was not available for reliable full-document comparison. Historic overlap through that work or equivalent combinatorial integer-product formulas is a residual risk.

## Limitations

The result concerns semigroup mutual inverses, not group inverse maps, and only full order-preserving transformations on one finite chain. It does not classify all possible individual inverse degrees or count all permutation matchings. Mathematical priority is judged against the accessible literature and mathematical records, not independently established for every historic source. The proof and verification are not an independent mathematical audit.

## References

1. P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1 (2026-10-01), https://arxiv.org/html/2610.01912v1 .
2. P. M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, Semigroup Forum **109** (2024), 141–147, https://doi.org/10.1007/s00233-024-10430-0 .
3. P. M. Higgins, *Permutations of a semigroup that map to inverses*, Semigroup Forum **89** (2014), 169–182; accessible manuscript: https://repository.essex.ac.uk/11534/1/Permutations%20by%20inverses%20final.pdf .
4. P. M. Higgins, *Combinatorial results for semigroups of order-preserving mappings*, Math. Proc. Cambridge Philos. Soc. **113** (1993), 281–296, https://doi.org/10.1017/S0305004100075964 .
