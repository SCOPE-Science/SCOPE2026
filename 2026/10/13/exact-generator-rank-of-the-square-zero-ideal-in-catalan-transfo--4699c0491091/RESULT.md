# Exact generator rank of the square-zero ideal in Catalan transformation monoids

## Finding
For every integer \(n\ge3\), let \(\mathcal C_n\) be the monoid of nondecreasing, order-decreasing maps \(f:[n]\to[n]\), with product \(vu=v\circ u\). Write \(\varepsilon(i)=1\) and consider the nilpotent subsemigroup
\[
S_n=\{f\in\mathcal C_n:f^2=\varepsilon\}.
\]
For a nonconstant \(h\in S_n\), define
\[
m(h)=\max\{i:h(i)=1\},\qquad M(h)=h(n),\qquad s(h)=|\operatorname{im}h|-1.
\]
Then the exact membership criterion for the product set \(S_n^2=\{vu:u,v\in S_n\}\) is
\[
\boxed{h\in S_n^2\ \Longleftrightarrow\ m(h)\ge M(h)+s(h).}
\]
The zero element \(\varepsilon\) belongs to \(S_n^2\). The unique inclusion-minimal and cardinality-minimal generating set of \(S_n\) is precisely \(S_n\setminus S_n^2\). If \(b_n=|S_n^2|\) for \(n\ge1\) (including the trivial cases), then
\[
\boxed{\sum_{n\ge1}b_nz^n=\frac{z(1-z)}{1-2z+z^2-z^3},\qquad \operatorname{rank}(S_n)=2^{n-2}-b_n\quad(n\ge3).}
\]
Equivalently \(b_1=b_2=b_3=1\), and \(b_n=2b_{n-1}-b_{n-2}+b_{n-3}\) for \(n\ge4\). The first ranks for \(n=3,4,5,6,7,8,9,10,11\) are \(1,2,4,9,20,43,91,191,398\). In particular the rank for \(n=6\) is \(9\), whereas the earlier general lower bound is \(8\).

## Assumptions and scope
All maps are total maps on the labeled chain \([n]=\{1,\ldots,n\}\). Composition is functional composition with the right factor applied first. The monoid \(\mathcal C_n\) is the Catalan transformation monoid, and \(\varepsilon\) is its absorbing zero. The condition \(f^2=\varepsilon\) means nilpotency degree at most two, not arbitrary nilpotency. The result is stated for every integer \(n\ge3\); the sequence \(b_n\) extends canonically with \(b_1=b_2=1\). The semigroup rank means the minimum cardinality of a semigroup generating set; the zero need not be an explicitly chosen generator.

## Proof
**Square-zero normal form.** Every \(f\in S_n\) has \(f(i)=1\) for \(1\le i\le m\), followed by a nondecreasing suffix with all values in \(\{2,\ldots,m\}\), where \(m=m(f)\) for nonconstant \(f\). Indeed \(f^2=\varepsilon\) forces \(f(j)=1\) for every \(j\in\operatorname{im}f\). Thus every output is in the initial one-fiber, while monotonicity and order decrease show the converse. For each \(m\in\{2,\ldots,n-1\}\), these suffixes number \(\binom{n-2}{n-m}\), by combinations with repetition. Summing, and including \(\varepsilon\), gives \(|S_n|=2^{n-2}\).

**Necessity of the product criterion.** Suppose \(h=v\circ u\) with \(u,v\in S_n\), and \(h\ne\varepsilon\). As \(u^2=\varepsilon\), its image lies in \([m(u)]\). Hence \(h(i)=1\) throughout the first \(m(u)\) positions, so \(m(u)\le m(h)\). Similarly \(M(h)\le m(v)\). Every argument at which \(h\) is nonunit must be sent by \(u\) outside \([m(v)]\). Distinct nonunit values of \(h\) require distinct values of \(u\) in the interval \(\{m(v)+1,\ldots,m(u)\}\), so \(s(h)\le m(u)-m(v)\le m(h)-M(h)\).

**Sufficiency and explicit factorization.** Suppose \(m=m(h)\ge M+s\), where \(M=M(h)\) and \(s=s(h)\). List the nonunit image values \(2\le t_1<\cdots<t_s=M\). Define \(u(i)=1\) for \(h(i)=1\), and \(u(i)=M+j\) for \(h(i)=t_j\). Define \(v(i)=1\) for \(i\le M\), \(v(M+j)=t_j\) for \(1\le j\le s\), and \(v(i)=M\) for \(i>M+s\). All displayed indices are in \([n]\), since \(M+s\le m<n\). Both maps are nondecreasing and order-decreasing. All outputs of \(u\) lie in \([m]\), on which \(u\) equals one, and all outputs of \(v\) lie in \([M]\), on which \(v\) equals one; hence \(u^2=v^2=\varepsilon\). By construction \(v\circ u=h\). The constant map also belongs to \(S_n^2\): for instance \(f=(1,1,2,\ldots,2)\in S_n\) satisfies \(f^2=\varepsilon\).

**Exact count of products.** A nonzero product with initial one-fiber length \(m\), \(s\) distinct nonunit outputs and maximum output \(M\) has \(1\le s\le n-m\) and \(M+s\le m\). For fixed \(m,s\), selecting the \(s\) distinct outputs with maximum \(M\) and summing over admissible \(M\) gives \(\binom{m-s-1}{s}\) choices. Dividing the \(n-m\) suffix positions into \(s\) nonempty constant-value runs gives \(\binom{n-m-1}{s-1}\) choices. Therefore
\[
\boxed{b_n=1+\sum_{m=2}^{n-1}\sum_{s=1}^{\min\{n-m,\lfloor(m-1)/2\rfloor\}}\binom{m-s-1}{s}\binom{n-m-1}{s-1}.}
\]
In formal generating functions, for each \(s\ge1\), the sum over \(m\ge2s+1\) equals \(z^{2s+1}/(1-z)^{s+1}\) and the sum over suffix lengths \(d\ge s\) equals \(z^s/(1-z)^s\). Adding these contributions to the zero map for every \(n\ge1\) gives
\[
\sum_{n\ge1}b_nz^n=\frac z{1-z}+\sum_{s\ge1}\frac{z^{3s+1}}{(1-z)^{2s+1}}=\frac{z(1-z)}{1-2z+z^2-z^3}.
\]
This is the previously catalogued integer sequence OEIS A005251; its appearance here is a new proposed semigroup interpretation, not a claim to have discovered the recurrence as an integer sequence.

**Minimal generating set.** Each nonzero \(f\in S_n\) satisfies \(f(i)<i\) for \(i>1\). Thus a product of \(n-1\) elements of \(S_n\) is \(\varepsilon\); the semigroup is nilpotent. Every generating set must contain every element outside \(S_n^2\). Conversely, every nonzero member of \(S_n^2\) can be expanded into products of elements outside \(S_n^2\): a nonzero product cannot admit arbitrarily long factorizations, by nilpotency, so repeatedly split decomposable factors until all factors are indecomposable. The zero is generated by \(f^2\), where \(f=(1,1,2,\ldots,2)\) is indecomposable (its initial one-fiber has length two, violating the product criterion). Hence \(S_n\setminus S_n^2\) is precisely the unique minimal generating set, and its cardinality is \(2^{n-2}-b_n\).

**Asymptotic size.** The cubic \(x^3-2x^2+x-1\) has unique dominant real root \(\lambda\approx1.754877666\), with both other roots of smaller absolute value. The recurrence yields \(b_n=O(\lambda^n)\), so the generator proportion \(\operatorname{rank}(S_n)/|S_n|\) is \(1-O((\lambda/2)^n)\).

## Verification
A standalone Python 3 checker is included as `checker.py`. It constructs all order-preserving order-decreasing maps independently for \(3\le n\le8\), filters the square-zero maps, composes every ordered pair, and compares the resulting product set with the structural criterion and the closed count. For \(9\le n\le11\), it uses the proved suffix normal form to generate maps and independently checks every pairwise product and the coefficient formula. It verifies \(\operatorname{rank}(S_6)=9\), against the previous lower bound \(8\), and checks the recurrence through thirty terms. Running `python3 checker.py` prints `VERIFY_OK`. These finite checks support but do not replace the all-integers proof.

## Relationship to prior work
Korkmaz and Ayık (2021), Theorem 3.4, establish a general lower bound for the rank of the bounded-potency nilpotent subsemigroups. For the present square-zero case, when \(n\ge4\), their bound is \(2^{n-3}\); their Example 3.6 computes the exact rank \(4\) when \(n=5\), and Example 3.5 constructs an element that cannot split in the square. Their proof does not provide the uniform factorization criterion, exact rank for all \(n\), or this product-set enumeration. The inequality is already strict at \(n=6\), since the exact rank is \(9>8\). Yağcı and Korkmaz (2020) count elements of fixed nilpotency degree and determine the rank of the full nilpotent semigroup, respectively; these are different assertions. The recurrence and integer sequence are already recorded as OEIS A005251. The algebraic interpretation and uniform exact generating rank, not the bare integer sequence, are the contribution evaluated here.

## Limitations
The theorem concerns \(f^2=\varepsilon\) only, not the rank of every bounded-potency ideal \(\{f:f^r=\varepsilon\}\) for \(r\ge3\), nor arbitrary order-preserving maps without the decreasing condition. Prior-work searches cannot certify universal novelty. A 2023 dissertation by Korkmaz on ranks and enumeration could not be inspected in full; its available abstract highlights other classifications. The 2020 paper on the full nilpotent semigroup was accessible only as a publisher preview, although the 2021 full article cites its main rank theorem. These are bibliographic uncertainties, not omitted proof assumptions.

## References
1. M. Yağcı and E. Korkmaz, "On Elements of Finite Semigroups of Order-Preserving and Decreasing Transformations," *Bulletin of the Malaysian Mathematical Sciences Society* 43 (2020), 3863–3870, DOI: 10.1007/s40840-020-00899-7. First online 2020-01-28.
2. M. Yağcı and E. Korkmaz, "On nilpotent subsemigroups of the order-preserving and decreasing transformation semigroups," *Semigroup Forum* 101 (2020), 486–496, DOI: 10.1007/s00233-020-10098-2. First online 2020-03-23.
3. E. Korkmaz and H. Ayık, "Ranks of nilpotent subsemigroups of order-preserving and decreasing transformation semigroups," *Turkish Journal of Mathematics* 45 (2021), 1626–1634, DOI: 10.3906/mat-2008-19. First publicly online 2021-05-07, Theorem 3.4 and Examples 3.5–3.6.
4. OEIS Foundation, Sequence A005251, recurrence and generating function \(z(1-z)/(1-2z+z^2-z^3)\), https://oeis.org/A005251.
