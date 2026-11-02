# Sharp line covers for cyclic even-order plane cubics via Skolem sequences

## Finding

Let \(E\subset\mathbb P^2_{\mathbb F_q}\) be a smooth plane cubic admitting a rational flex \(O\). Write \(\operatorname{cov}_{\mathbb F_q}(E)\) for the smallest number of \(\mathbb F_q\)-rational projective lines whose union contains every point of \(E(\mathbb F_q)\).

**Theorem.** Suppose \(E(\mathbb F_q)\) is cyclic of order \(6m\), with an integer \(m\ge1\) satisfying \(m\equiv0\) or \(1\pmod4\). Then
\[
\operatorname{cov}_{\mathbb F_q}(E)=2m+1=\frac{\#E(\mathbb F_q)}3+1.
\]
An optimal family of lines is constructive from any Skolem sequence of order \(m\).

**Arithmetic specialization.** For every prime \(p\equiv5\) or \(23\pmod{24}\), the smooth projective curve \(E_p:y^2=x^3+1\) over \(\mathbb F_p\) satisfies
\[
\operatorname{cov}_{\mathbb F_p}(E_p)=\frac{p+1}{3}+1.
\]
There are infinitely many such primes, by Dirichlet's theorem.

## Assumptions and scope

A rational flex is needed to identify a hyperplane section with \(3O\). Under that embedding, three *distinct* rational points are collinear exactly when their elliptic-group sum is \(O\). The theorem assumes **cyclicity** of the full rational group, not merely its cardinality. It is valid for all finite fields, with no restriction on the characteristic beyond smoothness. The congruence on \(m\) is used solely to invoke classical Skolem-sequence existence; no assertion for the other congruence classes is made.

A **Skolem sequence of order \(m\)** is a word of length \(2m\) containing each integer \(j=1,\ldots,m\) twice, at positions \(a_j<b_j\) separated by \(b_j-a_j=j\). Such sequences exist for every \(m\equiv0,1\pmod4\) (the classical Skolem theorem; cited below).

## Proof

**Lower bound.** Identify \(E(\mathbb F_q)\) with \(\mathbb Z/(6m)\mathbb Z\), sending \(O\) to zero. By Bézout, each line meets the cubic in at most three distinct rational points. A covering by \(2m\) lines would therefore partition its \(6m\) rational points into \(2m\) disjoint triples, each summing to zero. But the sum of all members of the even cyclic group is its unique element of order two, namely \(3m\ne0\). Summing the disjoint triples gives zero, a contradiction. Hence at least \(2m+1\) lines are necessary.

**Skolem partition.** Fix a Skolem sequence. For \(1\le j\le m\), define the integer triple
\[
T_j=(j,\ m+a_j,\ m+b_j).
\]
These are disjoint, together partition \(\{1,\ldots,3m\}\), and satisfy \(j+(m+a_j)=m+b_j\). There is precisely one triple with largest entry \(3m\); denote it \((a,b,3m)\), so that \(a\ne b\), \(1\le a,b<3m\), and \(a+b=3m\). (In fact this triple comes from the pair whose second position is \(2m\).)

**Covering all residues.** Put \(h=3m\) in \(\mathbb Z/(6m)\mathbb Z\). For each \(T_j=(u,v,w)\ne(a,b,h)\), take two zero-sum triples of group elements:
\[
(u,v,-w),\qquad(-u,-v,w).
\]
They each have three distinct residues, because \(u,v,w\) are distinct integers between \(1\) and \(h-1\), and their signs lie in opposite halves of the residue system. Across all retained Skolem triples these \(2(m-1)\) triples cover exactly the positive and negative copies of every member of \(\{1,\ldots,h-1\}\setminus\{a,b\}\), once each.

Add the following three zero-sum triples:
\[
(h,a,b),\qquad(h,-a,-b),\qquad(0,a,-a).
\]
They have pairwise distinct entries within each triple (the residues \(a,b\) are distinct and neither is \(0\) or \(h\)). The first two are zero-sum because \(a+b=h=-h\pmod{6m}\); the third is immediate. Together they cover the remaining \(\{0,h,\pm a,\pm b\}\). Thus the \(2m+1\) zero-sum triples cover every element of the cyclic group.

Every zero-sum triple of distinct rational elliptic-curve points corresponds to a line defined over \(\mathbb F_q\): the divisor \(P+Q+R\) is linearly equivalent to \(3O\), the complete linear system embedding the plane cubic, and the unique line through \(P,Q\) contains \(R\). Using these lines gives a covering of size \(2m+1\), matching the lower bound.

**Infinite arithmetic family.** Let \(p\equiv5\) or \(23\pmod{24}\). Then \(p\equiv2\pmod3\), and \(u\mapsto u^3\) permutes \(\mathbb F_p\). With \(\chi\) the quadratic character, the curve \(y^2=x^3+1\) has
\[
\#E_p(\mathbb F_p)=p+1+\sum_{x\in\mathbb F_p}\chi(x^3+1)=p+1.
\]
The sum vanishes by the cube permutation and \(\sum_{u\in\mathbb F_p}\chi(u+1)=0\). The rational two-torsion has only one nonzero point, since \(x^3+1\) has exactly one root in \(\mathbb F_p\). By the finite-field elliptic-group structure theorem, \(E_p(\mathbb F_p)\simeq\mathbb Z/d\oplus\mathbb Z/e\), with \(d\mid e\), \(d\mid(p-1)\), and \(de=p+1\). Hence \(d\mid\gcd(p-1,p+1)=2\). The possibility \(d=2\) would give four rational two-torsion points when \(d\mid e\), contrary to uniqueness. Therefore \(d=1\) and the group is cyclic.

For \(p\equiv5\pmod{24}\), \(m=(p+1)/6\equiv1\pmod4\); for \(p\equiv23\pmod{24}\), \(m\equiv0\pmod4\). The theorem applies. Both congruence classes are prime to \(24\), so Dirichlet's theorem supplies infinitely many primes in each.

## Verification

The standalone `verify.py` reconstructs Skolem-sequence position pairs for \(m=1,4,5\), verifies the Schur triples partition \(\{1,\ldots,3m\}\), constructs all \(2m+1\) covering triples, checks their sums and distinctness, and checks exact coverage of the cyclic group. It also counts points of the specified elliptic curve over several small primes. Execute `python verify.py` with Python 3; the observed result is `VERIFY_OK`. These finite computations are supplementary; the universal statement follows from the complete proof above and the cited Skolem existence theorem.

## Relationship to prior work

Asgarli–Dassarma–Ghioca–MacLean–Stokdyk (arXiv:2610.13042v1, 2026) prove a general asymptotic line-covering bound for plane curves and discuss elliptic-group triple partitions with odd point counts. Their asymptotic estimate alone does not imply the **exact additive constant** here; a partition into \(2m\) triples is obstructed by even cyclic parity, and the Skolem construction attains the next integer bound. Skolem's classical existence theorem supplies the combinatorial ingredient, but does not itself formulate a line-covering result for elliptic curves. The present theorem combines these with an explicit repair of the unique-involution obstruction.

## Limitations

The argument applies only when the rational group is cyclic of order \(6m\) and \(m\equiv0,1\pmod4\). It does not classify all even-order elliptic groups, the other two residue classes of \(m\), or every optimal covering. No independence, formal proof certification, or comprehensive historical-priority guarantee is asserted. A possible earlier formulation under cyclic Steiner/zero-sum covering terminology remains a literature risk.

## References

1. S. Asgarli, S. Dassarma, D. Ghioca, S. MacLean, E. Stokdyk, *Covering plane curves over finite fields with lines*, arXiv:2610.13042v1 (submitted 2026-10-09), https://arxiv.org/abs/2610.13042v1.
2. T. Skolem, *On certain distributions of integers in pairs with given differences*, Mathematica Scandinavica **5** (1957), 57–68 (Skolem sequence existence).
3. G. K. Bennett, M. J. Grannell, T. S. Griggs, *Exponential lower bounds for the numbers of Skolem-type sequences* (preprint; discusses exact existence criterion), https://studylib.net/doc/7984788/exponential-lower-bounds-for-the-numbers-of-skolem.
4. L. C. Washington, *Elliptic Curves: Number Theory and Cryptography*, standard finite-field rational-group structure theorem.
