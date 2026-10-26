# Sharp Engel-fiber stabilization in split metacyclic groups

## Finding
For every split metacyclic group \(G=C_m\rtimes_u C_h\), the entire value-frequency distribution of **every** iterated right Engel word is an explicit divisor sum. More strongly, the distributions reach a permanent plateau at a *sharp, computed length* controlled by the prime-power lifts of the complement action. Their eventual profile depends only on the action orders modulo the individual primes, not on those lifts.

For \(m\ge2\), let \(h\ge1\) and \(u\in(\mathbb Z/m\mathbb Z)^\times\) with \(u^h=1\). Define, for \(0\le i,j<h\) and \(k\ge1\),
\[
d_{i,j,k}=\gcd\left(m,(u^j-1)^k,(u^j-1)^{k-1}(u^i-1)\right).
\]
The exponent-zero factor is \(1\), even when \(u^j-1=0\). Every value lies in \(C_m\), and the number of pairs with value \(c\in C_m\) is exactly
\[
N_k(c)=m\sum_{i,j=0}^{h-1}d_{i,j,k}\,{\bf1}_{\{d_{i,j,k}\mid c\}}.
\]
The image of the word map is exactly \((u-1)^k C_m\).

For each \(p^{a_p}\Vert m\), put \(t_p=\operatorname{ord}_{p}(u)\) and \(s_p=\min(a_p,v_p(u^{t_p}-1))\), where \(v_p(0)=\infty\). The first length from which **all** fiber counts stay fixed is
\[
\boxed{K=\max_{p\mid m}\left(\left\lceil\frac{a_p}{s_p}\right\rceil+{\bf1}_{\{t_p>1\}}\right).}
\]
In particular, \(K\le1+\max_{p\mid m}a_p\), and this uniform bound is sharp for arbitrary exponents. For \(k\ge K\), set
\[
d_j=\prod_{\substack{p^{a_p}\Vert m\\t_p\mid j}}p^{a_p}.
\]
Then
\[
N_k(c)=mh\sum_{j=0}^{h-1}d_j\,{\bf1}_{\{d_j\mid c\}},\qquad
\Pr(e_k=1)=\frac{1}{mh}\sum_{j=0}^{h-1}d_j.
\]
Equivalently, if \(\mathcal P\) is the set of prime divisors of \(m\),
\[
\boxed{\Pr(e_k=1)=\frac1m\sum_{S\subseteq\mathcal P}\frac{\prod_{p\in S}(p^{a_p}-1)}{\operatorname{lcm}_{p\in S}(t_p)}\quad(k\ge K).}
\]
The empty-set product and least common multiple are both \(1\).

## Assumptions and scope
Write elements of \(G\) as \((a,i)\), with \(a\in\mathbb Z/m\mathbb Z\), \(i\in\mathbb Z/h\mathbb Z\), and multiplication
\[
(a,i)(b,j)=(a+u^i b,i+j).
\]
Here \(h\) need not equal the order of \(u\); a nonfaithful cyclic complement is allowed. The commutator convention is \([x,y]=x^{-1}y^{-1}xy\). The left-normed Engel words are \(e_1(x,y)=[x,y]\) and \(e_{k+1}(x,y)=[e_k(x,y),y]\). Frequencies count *ordered* pairs in \(G^2\). The integer representative of \(u\) is arbitrary: all truncated valuations and divisibility conditions are independent of this choice.

## Proof
**1. Linearization on every complement-index pair.** A direct multiplication gives
\[
[(a,i),(b,j)]=\bigl(u^{-i-j}((1-u^j)a+(u^i-1)b),0\bigr).
\]
For a rotation \((c,0)\), the next commutator with \((b,j)\) is \(((u^{-j}-1)c,0)\). Therefore \(e_k((a,i),(b,j))\) is a linear function of \((a,b)\in C_m^2\), whose two coefficients differ by units and signs from \((u^j-1)^k\) and \((u^j-1)^{k-1}(u^i-1)\). Its image is precisely \(d_{i,j,k}C_m\). Every point of that image has \(|C_m|^2/|d_{i,j,k}C_m|=m d_{i,j,k}\) preimages. Summation over the \(h^2\) complement-index pairs proves the fiber formula. As \(u^j-1\) is divisible by \(u-1\), every word value is in \((u-1)^k C_m\). Setting \(i=0,j=1\) realizes this whole subgroup (if \(h=1\), the group is abelian and both sides are zero).

**2. Prime-by-prime stabilization.** Fix \(p^{a}\Vert m\), put \(t=\operatorname{ord}_p(u)\), and \(s=\min(a,v_p(u^t-1))\). If \(t\nmid j\), then \(u^j-1\) is a \(p\)-adic unit and \(v_p(d_{i,j,k})=0\) for every \(k\). If \(t\mid j\), then \(u^j-1\) is divisible by \(p^s\) (with \(j=0\) interpreted as an infinite valuation). For \(k\ge2\) the two coefficients have valuations at least \(ks\) and \((k-1)s+v_p(u^i-1)\), respectively. Thus every such \(d_{i,j,k}\) has full \(p^a\)-part by \(k=\lceil a/s\rceil\) when \(t=1\), since then \(v_p(u^i-1)\ge s\) for all \(i\); and by \(k=1+\lceil a/s\rceil\) when \(t>1\). The same conclusions for \(k=1\) are immediate when the bound equals \(1\).

These thresholds are necessary. If \(t=1\) and \(s<a\), the choice \(i=j=1\) has \(p\)-part \(p^{\min(a,ks)}\). If \(t>1\) and \(s<a\), then \(h>t\) (because \(u^h=1\) modulo \(p^a\)); the choice \(i=1,j=t\) has \(p\)-part \(p^{\min(a,(k-1)s)}\). If \(t>1\) and \(s=a\), the pair \(i=1,j=0\) has a deficient \(p\)-part at \(k=1\), but none at \(k=2\). If \(t=1,s=a\), the \(p\)-part is already full at \(k=1\). Hence the displayed maximum \(K\) is exactly the first length at which **all** the image divisors stabilize. Since each divisor \(d_{i,j,k}\) grows by divisibility with \(k\), the identity fiber \(N_k(0)=m\sum d_{i,j,k}\) is strictly below its terminal value for every \(k<K\). This proves that \(K\) is also the least stabilization length for the actual frequency distribution, rather than merely a sufficient bound.

**3. Terminal distribution.** The preceding argument gives \(v_p(d_{i,j,k})=a_p\) exactly when \(t_p\mid j\), and \(0\) otherwise, once \(k\ge K\). Thus \(d_{i,j,k}=d_j\), independent of \(i\). This proves the terminal fiber formula. Expanding
\[
d_j=\prod_{p^{a_p}\Vert m}\left(1+(p^{a_p}-1){\bf1}_{\{t_p\mid j\}}\right)
\]
and averaging over \(j\) modulo \(h\) gives the subset/lcm expression, since every \(t_p\) divides \(h\). In particular the terminal distribution depends on \(m,h\) and the orders \(t_p\), but the sharp cutoff also depends on the valuations \(s_p\).

**4. Sharpness of the general bound.** Since \(s_p\ge1\), we have \(K\le1+\max a_p\). For each odd prime \(p\) and \(a\ge2\), choose a unit \(u\) that generates \((\mathbb Z/p^a\mathbb Z)^\times\) and set \(m=p^a\), \(h=p^{a-1}(p-1)\). Then \(t_p=p-1>1\) and \(v_p(u^{p-1}-1)=1\), so the least cutoff is exactly \(K=a+1\). This yields sharpness at arbitrarily large exponents.

## Verification
Run `python3 verify_engel_word.py`. The standalone checker verifies group commutators directly and compares every word-value fiber with the divisor formula in 32 exhaustive finite-group/depth combinations. It separately tests the exact cutoff and normalization for 1,965 units across moduli from \(2\) through \(80\), and checks the nonfaithful-complement lift comparison. Its successful output begins with `VERIFY_OK`. These finite computations are cross-checks; the proof covers all \(m,h,u,k\) in the stated domain.

For example, the two actions \(u=2\) and \(u=8\) on \(C_{27}\), both with complement \(C_{18}\), have the same reduction order \(t_3=2\) and terminal identity probability \(14/27\). Their valuations are respectively \(s_3=1\) and \(s_3=2\), hence their exact terminal lengths are \(4\) and \(3\).

## Relationship to prior work
Putignano and Vannacci study comparisons of general word probabilities, including the \(2\)-Engel word, and give lower bounds rather than the exact split-metacyclic fiber/cutoff profile [1]. De las Heras, Toti, and Vannacci study Engel-word fibers for regular cyclic wreath products of \(p\)-groups; their base groups are not cyclic and they give other types of estimates [2]. Camina, Cocke, and Thillaisundaram develop word-fiber tools for metacyclic \(p\)-groups; in particular their coset-wise homomorphism mechanism is a relevant precursor to the first step here [3]. The separate published Engel-digraph classification for Frobenius groups with an abelian kernel and cyclic complement supplies an overlapping fixed-point-free special case, which is **not** claimed as new [4].

The contribution assessed here is the simultaneous exact distribution at all lengths, the **least** universal stabilization length, and the arithmetic terminal profile for arbitrary split cyclic-by-cyclic groups, including non-Frobenius and mixed-prime actions. Broad word-map methods may provide another derivation of the linearization; novelty of the final sharp arithmetic statement has not been independently verified.

## Limitations
Only split extensions with a cyclic normal subgroup and cyclic complement are covered. The result does not address arbitrary nonsplit metacyclic groups or wreath products with noncyclic base group. The proof is exact but has not undergone independent mathematical audit. Earlier literature may contain an equivalent statement formulated through module endomorphisms or generalized word-fiber calculus.

## References
[1] L. Putignano and M. Vannacci, *Comparing word probabilities in finite groups*, arXiv:2610.23100, first posted 16 October 2026. https://arxiv.org/abs/2610.23100

[2] I. de las Heras, T. Toti, and M. Vannacci, *Engel probability in wreath products of p-groups*, arXiv:2607.11605, 2026. https://arxiv.org/abs/2607.11605

[3] R. D. Camina, W. L. Cocke, and A. Thillaisundaram, *The Amit–Ashurst conjecture for finite metacyclic p-groups*, European Journal of Mathematics 9 (2023), article 46. https://doi.org/10.1007/s40879-023-00644-x

[4] *Engel digraphs of abelian-kernel cyclic Frobenius groups*, mathematical research record, October 2026. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-engel-digraphs-of-abelian-kernel-cyclic-frobenius-groups--1e7e2c91abea
