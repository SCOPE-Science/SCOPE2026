# The commuting-clique polynomial of corank-two Jones idempotents

## Finding
For every integer \(n\ge2\), consider the Jones (Temperley–Lieb diagram) monoid \(J_n\) of planar pairings on \(n\) upper and \(n\) lower points, with loop-erasing concatenation. Let \(E_n\) be its idempotents with exactly \(n-2\) propagating strings. A *commuting clique* is a subset of \(E_n\) whose distinct elements commute pairwise; the empty subset is included. Set \(m=n-1\) and
\[
P_m(z)=\sum_{A\subseteq E_n\,\text{pairwise commuting}} z^{|A|}.
\]
Then the complete clique polynomial is given by
\[
P_0(z)=1,\qquad P_1(z)=1+z,\qquad P_2(z)=1+4z,
\quad P_m(z)=P_{m-1}(z)+zP_{m-2}(z)+2zP_{m-3}(z)\quad(m\ge3).
\]
Equivalently,
\[
\sum_{m\ge0}P_m(z)u^m=\frac{1+zu+2zu^2}{1-u-zu^2-2zu^3}.
\]
The number of *ordered* commuting pairs, including equality, is
\[
K_n=\begin{cases}1,&n=2,\\4,&n=3,\\9n^2-66n+129,&n\ge4.\end{cases}
\]
The largest commuting clique has size \(\lfloor n/2\rfloor\). Its multiplicity is \(1\) for even \(n\) and \((3n-1)/2\) for odd \(n\).

## Assumptions and scope
A Jones diagram is a nonintersecting perfect matching on two opposite horizontal rows of \(n\) boundary vertices. Composition stacks diagrams and erases closed middle loops. Rank counts arcs joining the upper to lower boundary. A rank-\(n-2\) diagram is uniquely specified by the adjacent upper cup at positions \(i,i+1\) and adjacent lower cap at positions \(j,j+1\), with the remaining \(n-2\) monotone propagating arcs. Denote it by \(d_{ij}\), where \(1\le i,j\le n-1\). Write \(\tau_i=d_{ii}\). The elementary diagram relations used below are \(\tau_i^2=\tau_i\), \(\tau_i\tau_{i\pm1}\tau_i=\tau_i\), and \(\tau_i\tau_j=\tau_j\tau_i\) whenever \(|i-j|\ge2\).

## Proof
**1. Rank and idempotents.** Concatenating \(d_{ij}\) with \(d_{k\ell}\) causes its rank to remain \(n-2\) exactly when their intermediate cap and cup meet, that is, \(|j-k|\le1\); otherwise it drops to \(n-4\). Every rank-\(n-2\) product retains the top cup of its first factor and the bottom cap of its second. Their indices determine the whole diagram. Thus \(d_{ij}^2=d_{ij}\) exactly when \(|i-j|\le1\). These \(3n-5\) idempotents are precisely
\[
\tau_i\quad(1\le i\le n-1),\qquad
\tau_i\tau_{i+1},\ \tau_{i+1}\tau_i\quad(1\le i\le n-2).
\]
This classification of the individual idempotents is an established result (East--Gray, Lemma 9.8); it is recalled as input, not claimed as novel.

**2. Exact commutation criterion.** For an idempotent \(d_{ij}\), define its generator support \(S(d_{ij})=\{i,j\}\), a singleton when \(i=j\). Two *distinct* such idempotents \(d_{ij}\) and \(d_{k\ell}\) commute if and only if
\[
|a-b|\ge2\quad\text{for every }a\in\{i,j\},\ b\in\{k,\ell\}.\tag{1}
\]
Indeed, if their two products are equal and have rank \(n-2\), equality of the retained upper cups and lower caps forces \(i=k\) and \(j=\ell\), contrary to distinctness. Hence both products must have rank \(n-4\), giving \(|j-k|\ge2\) and \(|\ell-i|\ge2\). Moreover, the common product retains both original upper cups (one from each multiplication order). Two distinct adjacent cups cannot share a boundary vertex, so \(|i-k|\ge2\): equality \(i=k\) would imply \(|\ell-i|\le1\), since \(d_{k\ell}\) is idempotent, which is already excluded. Analogously the common product retains both original lower caps, so \(|j-\ell|\ge2\). These are all four distances in (1). Conversely, under (1) all elementary generators in the words \(\tau_i\tau_j\) and \(\tau_k\tau_\ell\) commute, so the idempotents commute.

**3. All clique sizes.** A singleton support \(\{i\}\) has one idempotent orientation, and an adjacent double support \(\{i,i+1\}\) has two orientations. Criterion (1) says that chosen supports must be separated by at least one unused index. Encode these as interval tiles of length one (weight \(z\)) or length two (weight \(2z\)) on \(m\) sites, separated by at least one empty site. Split by whether site one is unused, carries a singleton tile, or starts a double tile. Their contributions are respectively \(P_{m-1}\), \(zP_{m-2}\), and \(2zP_{m-3}\). The first three cases are obtained by direct enumeration, and the stated rational generating function follows from the recurrence.

**4. Ordered pairs and maxima.** Write \(c_{m,2}=[z^2]P_m(z)\). For \(m\ge3\), the number of unordered compatible pairs of singleton supports is \((m-1)(m-2)/2\); singleton--double pairs contribute \(2(m-3)(m-2)\) (two double orientations); and double--double pairs contribute \(2(m-3)(m-4)\). Thus
\[
c_{m,2}=\frac{9m^2-51m+74}{2}\quad(m\ge3),\qquad
K_n=(3n-5)+2c_{n-1,2},
\]
which yields the formula in the finding, with \(n=2,3\) checked separately. With \(m\) sites, \(r\) selected support intervals require at least \(2r-1\) sites, hence \(r\le\lfloor(m+1)/2\rfloor=\lfloor n/2\rfloor\); this bound is attained by alternating singletons. When \(m=2k+1\), the unique packing of \(k+1\) intervals is the alternating singleton configuration. When \(m=2k\), maximum packings of \(k\) intervals consist either of \(k\) singleton supports (\(k+1\) position choices), or of exactly one double support and \(k-1\) singleton supports (\(k\) position choices, each with two orientations). Their total is \(3k+1=(3n-1)/2\). This includes the smallest cases.

## Verification
A standalone Python 3 program, `verify.py`, constructs pairings as literal matchings, computes concatenation by union--find without using the diagram monoid's generator presentation, checks all rank-\(n-2\) diagrams for \(2\le n\le12\), and independently enumerates every commuting clique from the computed commutation graph. For \(2\le n\le8\) it also enumerates *all* noncrossing matchings to verify that the chosen diagrams exhaust the rank stratum. All tests passed (`VERIFY_OK_JONES_CORANK_TWO`). They independently corroborate, but do not constitute, the arbitrary-\(n\) proof above.

## Relationship to prior work
East--Gray (2014), Lemma 9.8, already identifies every rank-\(n-2\) idempotent and establishes their number \(3n-5\). The same paper examines the rank and number of minimal generating sets of ideals of diagram monoids; those results are different from requiring elements to commute pairwise. Dolinka and collaborators (2015) classify and enumerate *individual* idempotents throughout planar diagram monoids, and their earlier paper (2014) counts idempotents in several other diagram monoids. The present assertion is the entire commuting-clique polynomial of this specifically defined Jones stratum and its pair and extremal specializations, **not** the already-known individual-idempotent classification. Equivalent formulations involve independent interval packings with two orientations for length-two tiles. The overlap search has not excluded every possible prior result under these aliases.

## Limitations
Only the idempotents in the first nonidentity rank stratum \(n-2\) are classified by commutation; neither arbitrary ranks nor the number of distinct subsemigroups generated by these cliques is determined. The recurrence is for subsets, not ordered tuples. Literature priority remains subject to an equivalent previously published compatibility/independence-polynomial result.

## References
1. J. East and R. D. Gray, *Diagram monoids and Graham--Houghton graphs: Idempotents and generating sets of ideals*, arXiv:1404.2359 (first posted 2014-04-09), especially Lemma 9.8 and Section 9.4, https://arxiv.org/abs/1404.2359.
2. I. Dolinka et al., *Enumeration of idempotents in planar diagram monoids*, arXiv:1507.04838 (first posted 2015-07-17), https://arxiv.org/abs/1507.04838.
3. I. Dolinka et al., *Enumeration of idempotents in diagram semigroups and algebras*, arXiv:1408.2021 (first posted 2014-08-09), https://arxiv.org/abs/1408.2021.
4. OEIS A225798, *Number of idempotents in the Jones monoid*, https://oeis.org/A225798, a count of all idempotents, not a commuting-clique polynomial.
