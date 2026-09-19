# Exact power-avoiding factorization for finite nilpotent groups

## Result

For a finite group \(G\) and an integer \(k\ge 2\), let
\[
s_k(G)=\max\{|X|: X\subseteq G,\ \{g,g^k\}\not\subseteq X\text{ for every }g\in G\}.
\]
Equivalently, \(s_k(G)\) is the independence number of the directed functional graph
\[
D_k(G):\qquad g\longmapsto g^k,
\]
where a loop forbids its vertex from an independent set.

Let \(G\) be finite nilpotent. Let \(\pi\) be the set of prime divisors of \(k\), and write
\[
G=P\times H,
\]
where \(P\) is the Hall \(\pi\)-subgroup and \(H\) is the Hall \(\pi'\)-subgroup. In the functional graph \(D_k(P)\), every vertex eventually reaches \(1\). Delete the loop at \(1\) and regard the resulting graph as a rooted tree \(T\) with root \(1\). Put
\[
A=\alpha(T-\{1\}),\qquad
\varepsilon=\alpha(T)-\alpha(T-\{1\})\in\{0,1\}.
\]

Then
\[
\boxed{s_k(G)=|H|A+\varepsilon\,s_k(H).}
\]

Since \(\gcd(k,\exp H)=1\), the map \(h\mapsto h^k\) is a permutation of \(H\). If
\[
n_d(H)=|\{h\in H:|h|=d\}|,\qquad
r_d=\operatorname{ord}_d(k)
\]
for \(d\mid \exp H\) (with \(r_1=1\)), then
\[
\boxed{
s_k(H)=
\sum_{d\mid \exp H}
\frac{n_d(H)}{r_d}\left\lfloor\frac{r_d}{2}\right\rfloor
}
\]
and therefore
\[
\boxed{
s_k(G)=|H|A+
\varepsilon
\sum_{d\mid \exp H}
\frac{n_d(H)}{\operatorname{ord}_d(k)}
\left\lfloor\frac{\operatorname{ord}_d(k)}2\right\rfloor .
}
\]

Thus, for finite nilpotent groups, the power-avoiding optimization splits into one statistic of the \(k\)-primary rooted tree and an explicit order-spectrum contribution from the coprime Hall factor.

## Proof of the factorization

Every element of \(P\) has order supported on primes dividing \(k\). Hence for every \(p\in P\), some iterate \(p^{k^N}\) equals \(1\), so \(D_k(P)\) has the unique directed cycle \(1\to1\), and deleting that loop gives the rooted tree \(T\).

On the other hand, \(\gcd(k,\exp H)=1\). Choose \(u\) with
\[
ku\equiv 1\pmod{\exp H}.
\]
Then \(h\mapsto h^u\) is the inverse of \(h\mapsto h^k\), so the latter map is a permutation of \(H\). Hence every vertex of \(D_k(H)\) is periodic.

Fix a directed cycle
\[
h_0\longmapsto h_1\longmapsto\cdots\longmapsto h_{r-1}\longmapsto h_0
\]
in \(D_k(H)\). For \(p\in P\), let \(\delta(p)\) be the least nonnegative integer such that \(p^{k^{\delta(p)}}=1\). The vertices attached to the cycle vertex \((1,h_i)\) are naturally identified with \(T\) by
\[
p\longmapsto (p,h_{i-\delta(p)}),
\]
with indices modulo \(r\). Indeed, applying the \(k\)-th power decreases \(\delta(p)\) by one until the root is reached and advances the \(H\)-coordinate by one. Consequently every cycle vertex carries a copy of the same rooted tree \(T\).

If the root of one attached copy is excluded, at most \(A\) vertices can be chosen from that copy. If the root is allowed, the optimum is \(\alpha(T)=A+\varepsilon\). Since adjoining one vertex to an independent set of \(T-\{1\}\) can improve its size by at most one, \(\varepsilon\in\{0,1\}\).

For a cycle of length \(r\), taking a root-excluding optimum in every copy gives \(rA\) vertices. If \(\varepsilon=0\), no choice of roots improves this. If \(\varepsilon=1\), every selected root contributes one additional vertex, while selected roots themselves must form an independent set on the directed cycle. A cycle of length \(r\ge2\) has independence number \(\lfloor r/2\rfloor\), while a loop (\(r=1\)) contributes zero. Thus the component contributes
\[
rA+\varepsilon\left\lfloor\frac r2\right\rfloor.
\]

Summing over all cycles of \(D_k(H)\) gives
\[
s_k(G)=|H|A+\varepsilon s_k(H).
\]

Finally, if \(h\in H\) has order \(d\), then its cycle length is the least \(r>0\) such that
\[
h^{k^r}=h,
\]
equivalently \(k^r\equiv1\pmod d\). Hence every element of order \(d\) lies on a cycle of length \(r_d=\operatorname{ord}_d(k)\), and there are \(n_d(H)/r_d\) such cycles. Summing their independence numbers proves the order-spectrum formula.

## Coprime case and parity defect

If \(\gcd(k,\exp G)=1\), then \(P=1\), so \(A=0\) and \(\varepsilon=1\). Hence
\[
\boxed{
s_k(G)=
\sum_{d\mid\exp G}
\frac{n_d(G)}{\operatorname{ord}_d(k)}
\left\lfloor\frac{\operatorname{ord}_d(k)}2\right\rfloor.
}
\]

Equivalently,
\[
\boxed{
2s_k(G)=
|G|-
\sum_{\substack{d\mid\exp G\\ \operatorname{ord}_d(k)\ {\rm odd}}}
\frac{n_d(G)}{\operatorname{ord}_d(k)}.
}
\]
Thus the deficit from \(|G|/2\) is exactly the number of odd cycles, counted one per cycle.

## Closed formula for cyclic groups under prime powering

Let \(p\) be prime and write
\[
n=p^a m,\qquad \gcd(p,m)=1.
\]
For \(G=C_n\), the primary factor is \(P=C_{p^a}\). In \(T=D_p(C_{p^a})\) with the root loop removed, the vertices at depth \(j\) are exactly the elements of order \(p^j\), so level \(j\) has size
\[
\varphi(p^j)\qquad (1\le j\le a).
\]

Let
\[
A_p(a)=
\sum_{\substack{1\le j\le a\\j\equiv a\pmod2}}\varphi(p^j).
\]
The union of these alternating levels is independent in \(T-\{1\}\). It is maximum: match every vertex on the other parity of levels to one of its children on the next level; distinct parents have disjoint sets of children. This saturates the complementary parity class, so König's theorem gives maximality of the displayed independent set. Therefore
\[
A_p(a)=
\begin{cases}
\dfrac{p(p^a-1)}{p+1},&a\text{ even},\\[6pt]
\dfrac{p^{a+1}-1}{p+1},&a\text{ odd}.
\end{cases}
\]
The even formula includes \(a=0\), giving \(A_p(0)=0\).

The same matching argument on the full rooted tree \(T\) shows
\[
\alpha(T)-\alpha(T-\{1\})=
\begin{cases}
1,&a\text{ even},\\
0,&a\text{ odd}.
\end{cases}
\]
Indeed, for even \(a\) the even levels, including the root, form a maximum independent set; for odd \(a\) the odd levels form one.

Since \(H=C_m\) has exactly \(\varphi(d)\) elements of order \(d\), the general factorization becomes
\[
\boxed{
s_p(C_{p^a m})=
mA_p(a)+
\mathbf 1_{2\mid a}
\sum_{d\mid m}
\frac{\varphi(d)}{\operatorname{ord}_d(p)}
\left\lfloor\frac{\operatorname{ord}_d(p)}2\right\rfloor.
}
\]

For example, \(20=2^2\cdot5\). Here \(A_2(2)=2\), and the coprime \(C_5\) term is \(2\). Hence
\[
s_2(C_{20})=5\cdot2+2=12,
\]
agreeing with the example displayed in Blackburn--Hart--McVeagh.

## Relation to prior literature

Blackburn, Hart and McVeagh introduced the parameter \(s_k(G)\) and identify it with the independence number of \(D_k(G)\). Their structural analysis of the functional graph shows that every component has a unique directed cycle and that the rooted trees attached to cycle vertices satisfy strong symmetry properties.

The structure of power-map functional graphs predates that paper. Qureshi and Reis give explicit decompositions for finite abelian groups, including cyclic groups. Fernandes and Reis study power-map digraphs over finite nilpotent groups. Those graph-structure results are prior art and are not claimed here.

The contribution here is the exact independent-set optimization on the nilpotent decomposition, the order-spectrum formula for the coprime factor, and the resulting closed formula for \(s_p(C_n)\) for every cyclic group and every prime \(p\).

## Reproducibility

The accompanying script `artifacts/verify_cyclic_prime.py` independently computes the independence number of the functional graph \(x\mapsto px\) on \(C_n\) by exact cycle/tree dynamic programming and compares it with the closed formula above. The recorded check covers every prime
\[
p\in\{2,3,5,7,11\}
\]
and every \(1\le n\le120\), for 600 cases, with no discrepancy. This finite verification supports the formula but is not used in place of the proof.

## Limitations

For a general nonabelian Hall \(\pi\)-subgroup \(P\), the theorem isolates the primary contribution in the rooted-tree statistic \(A\) and the bit \(\varepsilon\), but does not give a closed group-theoretic formula for those two quantities.

Originality is claimed only to the best of our knowledge. The full text of Fernandes--Reis, *Digraphs of power maps over finite nilpotent groups*, Discrete Mathematics 347 (2024), 114000, was not independently inspected; it is the most relevant prior structural source and could contain an equivalent optimization statement in different language. McVeagh's 2026 thesis, *Square-free Sets in Groups and Groups with Many Roots*, cited by Blackburn--Hart--McVeagh for related \(k=2\) results and power-digraph symmetry, was also not independently inspected in full. No claim is made that the structural decomposition of the functional graph is new.

## References

1. S. R. Blackburn, S. B. Hart, D. McVeagh, *Finite groups with large power-avoiding subsets*, arXiv:2609.18513v1 (2026).
2. C. Qureshi, L. Reis, *On the functional graph of the power map over finite groups*, arXiv:2107.00584v2; Discrete Applied Mathematics 319 (2022), 115--125.
3. A. Fernandes, L. Reis, *Digraphs of power maps over finite nilpotent groups*, Discrete Mathematics 347 (2024), 114000, doi:10.1016/j.disc.2024.114000.
4. A. Fernandes, C. Qureshi, L. Reis, S. Ribas, *On a class of combinatorial group invariants*, arXiv:2609.20516 (2026).
5. D. McVeagh, *Square-free Sets in Groups and Groups with Many Roots*, PhD thesis, Birkbeck University of London (2026).
