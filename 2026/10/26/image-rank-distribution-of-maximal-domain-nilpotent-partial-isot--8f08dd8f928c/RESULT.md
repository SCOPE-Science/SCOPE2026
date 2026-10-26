# Image-rank distribution of maximal-domain nilpotent partial isotone maps

## Finding

Let \(\mathrm{PO}_n\) be the semigroup of partial weakly order-preserving maps of the chain \([n]=\{1,\dots,n\}\), with the empty map as zero. For every integer \(n\ge2\), the largest possible domain of a nilpotent element has size \(n-1\). Among the nilpotent elements with that domain size, the number whose image has size \(r\) is

\[
N_{n,r}=\frac{2}{n-1}\binom{n}{r+1}\binom{n-1}{r-1}\qquad(1\le r\le n-1).
\]

There are no other image ranks in this stratum. In particular, the total number is the Catalan number

\[
\sum_{r=1}^{n-1}N_{n,r}=\frac1{n+1}\binom{2n}{n},
\]

exactly \(n\) have image rank one, and exactly two have image rank \(n-1\). More finely, if \(m\) is the unique point missing from the domain, the corresponding image-rank polynomial is

\[
\sum_{\substack{f\in\mathrm{PO}_n\text{ nilpotent}\\\operatorname{dom}f=[n]\setminus\{m\}}}t^{|\operatorname{im}f|}
=t\,C_{m-1}(t)C_{n-m}(t),
\]

where \(C_0(t)=1\) and

\[
C_s(t)=\sum_{j=1}^{s}\frac1s\binom{s}{j}\binom{s}{j-1}t^{j-1}\quad(s\ge1)
\]

is the Narayana polynomial with the exponent shifted down by one.

## Assumptions and scope

Composition is the usual composition of partial functions; an element \(f\) is nilpotent when \(f^{\circ k}\) is the empty partial map for some positive integer \(k\). A map is weakly order-preserving when \(i<j\) in its domain implies \(f(i)\le f(j)\). Domain size and image rank are distinct invariants; the theorem fixes domain size at its maximal nilpotent value \(n-1\) and refines by image rank. For \(n=1\), the only nilpotent map is the empty map of domain and image size zero, outside the displayed \(n\ge2\) formula. The theorem does not count nilpotents with smaller domains.

## Proof

**1. Nilpotence and maximal domain.** A partial weakly increasing map of a finite chain has no periodic orbit of length greater than one: on an orbit, the least member cannot move to a larger member and later return while the map is weakly increasing. Consequently a partial isotone map is nilpotent if and only if it has no fixed point: every indefinitely defined forward trajectory in a finite domain would eventually be periodic. Every full weakly increasing self-map of \([n]\) fixes a point, since iteration from \(1\) is weakly increasing and must stabilize. Thus a nilpotent element has domain of size at most \(n-1\). The maps described below show this bound is attained.

**2. The omitted-point normal form.** Fix \(m\in[n]\) and suppose \(\operatorname{dom}f=[n]\setminus\{m\}\). Nilpotence forces, for each \(i<m\),

\[
i<f(i)\le m,
\]

and, for each \(i>m\),

\[
m\le f(i)<i.
\]

Indeed, an orbit starting below \(m\) cannot take a nonincreasing first step and later escape through the unique absent point \(m\): monotonicity would keep subsequent steps nonincreasing until a forbidden fixed point arose. It also cannot take a first step past \(m\), after which monotonicity keeps the trajectory strictly increasing above \(m\). The upper-side argument is symmetric. Conversely, each displayed inequality makes every trajectory move strictly towards the missing point, so the map is nilpotent.

For \(1<m<n\), weak monotonicity across the gap additionally gives

\[
m\le f(m-1)\le f(m+1)\le m,
\]

hence both values equal \(m\). The endpoint cases have the same property on whichever side is nonempty. All left-side images are at most \(m\), all right-side images are at least \(m\), and the two parts meet only in the image value \(m\). Conversely, any two individually weakly increasing sides satisfying the displayed inequalities fit together into a weakly increasing nilpotent partial map, because their boundary values are \(m\).

**3. Two Catalan-side objects.** Set \(a=m-1\) and \(b=n-m\). The left-side sequence, read in reverse and complemented, is

\[
x_j=m+1-f(m-j)\quad(1\le j\le a),
\]

and the right-side sequence, shifted, is

\[
y_j=f(m+j)-m+1\quad(1\le j\le b).
\]

Each nonempty sequence is weakly increasing and satisfies \(1\le x_j\le j\), respectively \(1\le y_j\le j\). Conversely, every pair of sequences of these types reconstructs exactly one nilpotent map with missing point \(m\). Such length-\(s\) sequences are classical Dyck-path encodings; the number with exactly \(j\) distinct entries is the Narayana number \(\frac1s\binom{s}{j}\binom{s}{j-1}\). For example, encode each value's multiplicity as a vertical run in a Dyck path: distinct values correspond to the path's peaks, and the usual ballot restriction is precisely \(x_j\le j\). This gives the polynomial \(C_s(t)\) above.

The common value \(m\) appears on each nonempty side. Distinct values contributed by the two sides are otherwise disjoint. Thus total image rank is one plus the number of distinct side values other than \(m\), proving the missing-point identity \(tC_a(t)C_b(t)\), including the empty-side convention.

**4. Closed coefficients.** Put \(C(z,t)=\sum_{s\ge0}C_s(t)z^s\). The first-return decomposition of the Dyck paths, with peak weight \(t\), yields

\[
C(z,t)=1+zC(z,t)\bigl(1+t(C(z,t)-1)\bigr).
\]

Writing \(u=C-1\), the equivalent functional equation is \(u=z(1+u)(1+tu)\). Summing over \(m\in[n]\) gives

\[
\sum_{r=1}^{n-1}N_{n,r}t^r=t[z^{n-1}]C(z,t)^2.
\]

Lagrange inversion for \(n-1\ge1\) now gives

\[
\begin{aligned}
[z^{n-1}]C(z,t)^2
&=\frac{2}{n-1}[u^{n-2}](1+u)^n(1+tu)^{n-1}\\
&=\frac{2}{n-1}\sum_{r=1}^{n-1}
\binom{n}{r+1}\binom{n-1}{r-1}t^{r-1}.
\end{aligned}
\]

This proves the rank formula. Substituting \(t=1\) gives \(\frac2{n-1}\binom{2n-1}{n-2}=\frac1{n+1}\binom{2n}{n}\). The rank-one and rank-\(n-1\) counts follow by taking the first and last coefficients.

## Verification

The standalone `verify.py` reconstructs each order-preserving partial map of domain size \(n-1\) by independent weakly increasing image sequences. It tests nilpotence by following all trajectories, compares the count at each rank and each omitted point with the Narayana convolution, and checks the closed binomial coefficient formula for every \(2\le n\le9\). It independently confirms equality of fixed-point-freeness and nilpotence on these finite instances. Additional exact integer checks through \(n=150\) compare the closed coefficient formula with the Narayana convolution and Catalan total. The expected terminal marker is `VERIFY_OK_MAXIMAL_DOMAIN_NILPOTENT_RANK_NARAYANA`. The infinite statement rests on the proof, not on the finite checks.

## Relationship to prior work

Garba's study of nilpotents in partial order-preserving semigroups (journal issue 1994; DOI below) concerns structural and nilpotent-generation questions. Laradji and Umar (2004) give order, idempotent and Green-class enumerations for the ambient partial isotone semigroup. Their 2013 preprint (available in complete author-posted text) develops lattice paths primarily for the order-decreasing subsemigroup, rather than the present maximal-domain nilpotent image-rank statistic. Laradji and Umar (2015) enumerate nilpotents of order-preserving **partial injections**, a distinct semigroup. The Narayana numbers and Catalan totals themselves are classical; the asserted contribution is their precise rank-refined identification with the extremal-domain nilpotents of the unrestricted partial isotone monoid, including the omitted-point factorization and universal closed formula.

## Limitations

Only nilpotents with domain exactly \(n-1\) are classified; smaller-domain distributions and nilpotency-index distributions are not determined. The 1994 and 2004 primary papers were not available for complete full-text comparison, so historical-priority uncertainty remains. The numerical sequence and the Narayana polynomials are not claimed to be previously unknown combinatorial objects.

## References

1. G. U. Garba, *Nilpotents in semigroups of partial order-preserving transformations*, Proc. Edinburgh Math. Soc. 37 (1994), 361–377, DOI: 10.1017/S001309150001885X.
2. A. Laradji and A. Umar, *Combinatorial results for semigroups of order-preserving partial transformations*, J. Algebra 278 (2004), 342–359, DOI: 10.1016/j.jalgebra.2003.10.023.
3. A. Laradji and A. Umar, *Lattice Paths and Order-preserving Partial Transformations*, arXiv:1304.7574 (first version 29 April 2013).
4. A. Laradji and A. Umar, *Combinatorial results for semigroups of order-preserving or order-reversing subpermutations*, J. Difference Equations Appl. 21 (2015), 269–283, DOI: 10.1080/10236198.2015.1005080.
5. OEIS A001263, Narayana number triangle, and OEIS A000108, Catalan numbers.
