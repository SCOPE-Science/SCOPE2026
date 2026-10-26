# A critical sparse-colouring convergence law for uniform random equivalence relations

## Finding

Let \(E_n\) be a uniformly chosen equivalence relation on \([n]\): each of the \(B_n\) set partitions has equal probability. Independently mark each element with a unary predicate \(P_n\), with probability \(p_n\) independently over elements. Let \(r_n>0\) satisfy \(r_ne^{r_n}=n\). Assume \(p_nr_n\to c\) for a fixed \(c\in(0,\infty)\). For \(j\ge1\), let \(N_{j,n}\) be the number of \(E_n\)-classes of size exactly \(j\) all of whose elements satisfy \(P_n\).

**Critical marked-class process and first-order theorem.** The entire vector of counts \((N_{j,n})_{j\ge1}\) converges in distribution, as a finite counting measure on the positive integers, to independent Poisson counts \((Z_j)_{j\ge1}\) with means
\[
\lambda_j(c)=\frac{c^j}{j!}.
\]
In particular, the total \(T_n=\sum_{j\ge1}N_{j,n}\) converges to \(\operatorname{Poisson}(e^c-1)\).

Every first-order sentence \(\varphi\) over \(\{E,P,=\}\) has an effectively computable limiting probability. More explicitly, let \(q\ge1\) be at least the quantifier rank of \(\varphi\). The limit is computed solely from **independent** Poisson variables with means
\[
\lambda_1(c),\ldots,\lambda_{q-1}(c),\qquad
\lambda_{\ge q}(c)=e^c-\sum_{j=0}^{q-1}\frac{c^j}{j!},
\]
by capping all their counts at \(q\) and evaluating \(\varphi\) on the finite canonical representatives described below. Thus the limiting probability is a real-analytic, effectively specified function of \(c>0\).

The unary-marked-class sentence
\[
\psi:=\exists x\,\forall y\,\big(E(x,y)\longrightarrow P(y)\big)
\]
has the nontrivial critical limit
\[
\lim_{n\to\infty}\Pr((E_n,P_n)\models\psi)=1-\exp(1-e^c).
\]
This threshold is sharp: if \(p_nr_n\to0\), that probability tends to zero; if \(p_nr_n\to\infty\), it tends to one.

## Assumptions and scope

Structures are nonempty and finite before taking \(n\to\infty\). The equivalence relation is **uniform across the \(B_n\) set partitions**, not uniform across integer partitions or chosen by assigning independent edges. Marking is independent of the partition and of other vertices. The first-order language has equality, one binary equivalence relation and one unary predicate; there are no extra functions, built-in order, constants or counting quantifiers. The first-order conclusion assumes fixed \(c\in(0,\infty)\), not a uniform limit over moving \(c\). The threshold assertion for \(\psi\) also covers the endpoint regimes.

Write \((t)_s=t(t-1)\cdots(t-s+1)\), with \((t)_0=1\), and let \(S(s,m)\) denote a Stirling number of the second kind. Put \(A_n=B_n/n!\) and \(R_n=A_{n-1}/A_n=nB_{n-1}/B_n\) for \(n\ge1\). Standard Bell asymptotics give \(R_n/r_n\to1\). The established log-concavity of \((A_n)_{n\ge0}\) implies, for every \(0\le s\le n\),
\[
\frac{n!B_{n-s}}{(n-s)!B_n}=\frac{A_{n-s}}{A_n}\le R_n^s.
\]
These two previously known Bell-number properties are inputs, not new lemmas claimed here.

## Proof

**1. Exact coloured-block factorial moments.** Choosing ordered distinct all-marked classes of specified sizes and then partitioning all remaining elements gives, for finitely supported nonnegative integers \(m_j\) and \(s=\sum_j jm_j\le n\),
\[
\mathbb E\prod_j(N_{j,n})_{m_j}
=\frac{n!B_{n-s}}{(n-s)!B_n}\prod_j\left(\frac{p_n^j}{j!}\right)^{m_j}.
\]
For \(s>n\) the moment vanishes. Since for every fixed \(s\), \(A_{n-s}/A_n\sim r_n^s\), each finite vector of fixed-size all-marked-class counts has limiting mixed factorial moments \(\prod_j(c^j/j!)^{m_j}\).

For the total number \(T_n\), ordered selection of \(m\) marked classes and the Stirling exponential identity give the exact formula
\[
\mathbb E(T_n)_m=
\sum_{s=m}^{n}\frac{n!B_{n-s}}{(n-s)!B_n}\frac{m!S(s,m)}{s!}\,p_n^s.
\]
The log-concavity bound controls this by \((e^{p_nR_n}-1)^m\). Each fixed summand converges to its corresponding term with \(c^s\), and these uniformly summable dominating series imply
\[
\mathbb E(T_n)_m\longrightarrow(e^c-1)^m
\]
for every fixed \(m\ge0\). The probability-generating-function expansion \(\mathbb E[t^{T_n}]=\sum_m (t-1)^m\mathbb E(T_n)_m/m!\), dominated locally uniformly by \(\exp(|t-1|(e^{p_nR_n}-1))\), consequently converges to the generating function of \(\operatorname{Poisson}(e^c-1)\). The same argument using finitely many variables yields independent \(\operatorname{Poisson}(c^j/j!)\) limits for every fixed vector \((N_{1,n},\ldots,N_{d,n})\). Finally, the expected count in sizes greater than \(d\) tends to \(e^c-1-\sum_{j=1}^d c^j/j!\), which tends to zero as \(d\to\infty\). This gives tightness of the full size-marked counting measure and identifies its independent Poisson limit, including aggregate tails.

**2. Every class containing an unmarked vertex is abundant at fixed finite profile.** For fixed \(a\ge0\) and \(b\ge1\), let \(M_{a,b,n}\) count classes containing exactly \(a\) marked and \(b\) unmarked vertices. With \(s=a+b\), the exact first moment is
\[
\mathbb EM_{a,b,n}=
\frac{n!B_{n-s}}{(n-s)!B_n}\frac{p_n^a(1-p_n)^b}{a!b!}
\sim\frac{c^a}{a!b!}r_n^b\longrightarrow\infty.
\]
The exact second factorial moment is obtained by choosing two disjoint classes, replacing \(s\) by \(2s\) and squaring the local marking factor. Its ratio to \((\mathbb EM_{a,b,n})^2\) tends to one because both Bell coefficient ratios have their fixed-shift asymptotics. Thus \(M_{a,b,n}/\mathbb EM_{a,b,n}\to1\) in probability, and every such fixed mixed-colour profile occurs in arbitrarily many distinct classes with probability tending to one.

**3. Bounded-rank classification.** For a finite structure in this signature and a class \(C\), record \((\min(q,|C\cap P|),\min(q,|C\setminus P|))\). Record also, truncated at \(q\), the number of classes of each such type. Two equivalence structures with identical records satisfy exactly the same first-order sentences of quantifier rank at most \(q\): in the \(q\)-round Ehrenfeucht–Fraïssé game, Duplicator matches new classes of the same recorded type and, within matched classes, matches elements of the same unary colour. At most \(q\) classes and \(q\) elements per colour can be requested, so these truncations suffice. This is a direct game argument, not a numerical heuristic.

By Step 2, with probability tending to one, every type with at least one unmarked vertex (in its \(q\)-truncated profile) occurs at least \(q\) times: choose its exact representative profile with each positive coordinate in \(\{1,\ldots,q\}\), interpreting the value \(q\) as exactly \(q\). The only random counts remaining at rank \(q\) are the all-marked class types of exact sizes \(1,\ldots,q-1\) and the aggregate all-marked size \(\ge q\). By Step 1 their joint limit consists of the independent Poisson variables listed in the Finding.

For explicit effective evaluation, for each vector \(v=(v_1,\ldots,v_{q-1},v_\star)\in\{0,\ldots,q\}^q\), create a finite structure \(C_q(v)\) with \(q\) classes of every mixed-colour \(q\)-profile (each represented by exactly the recorded numbers of marked and unmarked elements), \(v_j\) all-marked classes of size \(j\) for \(j<q\), and \(v_\star\) all-marked classes of size exactly \(q\). For \(h_q(t,\lambda)=e^{-\lambda}\lambda^t/t!\) when \(0\le t<q\), and \(h_q(q,\lambda)=1-e^{-\lambda}\sum_{t=0}^{q-1}\lambda^t/t!\), the limiting probability is the **finite, computable expression**
\[
\sum_{v\in\{0,\ldots,q\}^{q}}
\mathbf1\{C_q(v)\models\varphi\}
\left[\prod_{j=1}^{q-1}h_q(v_j,c^j/j!)\right]
 h_q\left(v_\star,e^c-\sum_{j=0}^{q-1}c^j/j!\right).
\]
For the tautological quantifier-rank-zero case any \(q\ge1\) may be used. Every term is analytic in \(c\), proving the stated analyticity.

**4. Sharpness of the sparse-marking scale.** The sentence \(\psi\) is equivalent to \(T_n\ge1\), hence its critical limit is \(1-\exp(-(e^c-1))\). If \(p_nR_n\to0\), the same moment bound with \(m=1\) yields \(\mathbb ET_n\le e^{p_nR_n}-1\to0\). If \(p_nR_n\to\infty\), the number \(N_{1,n}\) of marked singleton classes has \(\mathbb EN_{1,n}=p_nR_n\to\infty\). Its exact second factorial moment, together with fixed-shift Bell asymptotics, implies \(\operatorname{Var}(N_{1,n})/(\mathbb EN_{1,n})^2\to0\). Thus \(N_{1,n}>0\) with probability tending to one. Because \(R_n/r_n\to1\), these cases are precisely the three regimes formulated using \(r_n\).

## Verification

`checker.py` (included with the result) enumerates **every set partition and every marked subset** for domain sizes \(0\) through \(7\) at the exact rational marking probability \(2/5\). It compares weighted combinatorial sums with the displayed identities for \(m=1,2,3\), and with size-resolved factorial moments for sizes \(1,2,3\) and multiplicities \(1,2\). The expected output is `SPARSE_EQUIVALENCE_MOMENTS_OK 127203 72`. All rational computations use Python integers; no simulation is involved. The finite computation tests exact counting identities, **not** the infinite-domain limit or originality.

## Relationship to prior work

Koponen (2026, arXiv:2610.16163) discusses criteria relevant to logical convergence of random expansions of finite base structures. That paper investigates finite-model properties and extension/closure hypotheses, not the present explicit sparse-colouring law for uniform Bell partitions. Arratia and Tavaré (1994) establish the general independent-process treatment of uniform set partitions and their component counts; their method and the fixed-size Bell ratio asymptotics are foundational inputs, not claimed as new. Asai, Kubo and Kuo (2001) prove the required log-concavity of \(B_n/n!\). St. John (1997) studies a different sparse-unary first-order limit law over linear orders. The new assertion assessed here is the **combined critical Poisson class-size process plus effective all-sentence first-order limiting semantics on random equivalence relations**, with the sharp Lambert-W marking scale.

## Limitations

The proof does not provide a uniform convergence rate for arbitrary first-order formulas. The first-order law with the displayed canonical Poisson profiles is established only for \(p_nr_n\to c\in(0,\infty)\); outside this window only the threshold for \(\psi\) is asserted. Historical priority is qualified: more general refined assembly limit theorems supply much of the probabilistic machinery, and an unlocated specialized random-colouring logic theorem could supersede the combination. The results have not received independent review.

## References

1. V. Koponen, *A characterization of the finite model property for omega-categorical theories*, arXiv:2610.16163v1, 12 October 2026. https://arxiv.org/html/2610.16163v1
2. R. Arratia and S. Tavaré, *Independent Process Approximations for Random Combinatorial Structures*, Advances in Mathematics 104 (1994), 90–154. https://www.columbia.edu/cu/simontavare/STpapers-pdf/AT94.pdf
3. N. Asai, I. Kubo and H.-H. Kuo, *Bell numbers, log-concavity, and log-convexity*, arXiv:math/0104137 (2001). https://arxiv.org/abs/math/0104137
4. K. St. John, *Limit Probabilities for Random Sparse Bit Strings*, Electronic Journal of Combinatorics 4 (1997), R23. https://doi.org/10.37236/1308
