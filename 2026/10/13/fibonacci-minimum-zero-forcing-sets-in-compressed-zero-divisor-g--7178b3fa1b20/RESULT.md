# Fibonacci minimum zero forcing sets in compressed zero-divisor graphs of finite chain rings

## Finding

Let \(R\) be a finite commutative chain ring with maximal ideal \(\mathfrak m=(\pi)\) and nilpotency length \(\ell\ge2\). In the compressed zero-divisor graph \(\Gamma_E(R)\), annihilator classes are exactly \([\pi],[\pi^2],\ldots,[\pi^{\ell-1}]\), and distinct classes \([\pi^i],[\pi^j]\) are adjacent exactly when \(i+j\ge\ell\). Hence \(\Gamma_E(R)\) is the connected antiregular graph \(A_{\ell-1}\), independently of the residue-field size. If \(\ell=2\), then \(\Gamma_E(R)=K_1\), so \(Z=M=1\), \(\operatorname{mr}=0\), and there is one minimum zero forcing set. For \(\ell\ge3\), \[Z(\Gamma_E(R))=M(\Gamma_E(R))=\left\lfloor\frac{\ell-1}{2}\right\rfloor,\qquad \operatorname{mr}(\Gamma_E(R))=\left\lceil\frac{\ell-1}{2}\right\rceil.\] Writing \(F_0=0,F_1=1\) for the Fibonacci sequence, the number of minimum zero forcing sets is \(F_\ell\) when \(\ell\) is odd and \(2F_{\ell-2}\) when \(\ell\ge4\) is even.

The minimum-set enumeration is independent of the residue field and depends only on the nilpotency length. Its parity split is genuinely Fibonacci.

## Assumptions and scope

Let \(R\) be a finite commutative chain ring. Its ideals form the chain
\[
R\supset \mathfrak m\supset \mathfrak m^2\supset\cdots\supset \mathfrak m^\ell=0,
\]
where
\[
\mathfrak m=(\pi),\qquad \mathfrak m^{\ell-1}\ne0.
\]

For nonzero zero-divisors \(x,y\), Spiroff and Wickham identify
\[
x\sim y
\quad\Longleftrightarrow\quad
\operatorname{ann}(x)=\operatorname{ann}(y),
\]
and define the compressed graph \(\Gamma_E(R)\) on the nontrivial annihilator classes, with distinct classes adjacent when their product is zero.

For a finite simple graph \(G\), \(Z(G)\) denotes its zero forcing number. The real symmetric maximum nullity and minimum rank are denoted by \(M(G)\) and \(\operatorname{mr}(G)\).

## Proof

Every nonzero element of a finite chain ring has a unique form
\[
u\pi^i,
\qquad
u\in U(R),
\qquad
0\le i\le\ell-1.
\]
For \(1\le i\le\ell-1\),
\[
\operatorname{ann}(u\pi^i)=\mathfrak m^{\ell-i}.
\]
Therefore two nonzero zero-divisors have the same annihilator exactly when they have the same valuation. Thus the vertices of \(\Gamma_E(R)\) are
\[
v_i=[\pi^i],
\qquad
1\le i\le\ell-1.
\]
Moreover,
\[
v_i\sim v_j
\quad\Longleftrightarrow\quad
\pi^{i+j}=0
\quad\Longleftrightarrow\quad
i+j\ge\ell.
\tag{1}
\]

Put
\[
m=\ell-1.
\]
The graph on \(v_1,\ldots,v_m\) with adjacency (1) is the connected antiregular graph \(A_m\). Equivalently,
\[
A_{m+2}=K_1\vee(K_1\dot\cup A_m).
\tag{2}
\]
This is the standard recursive description of connected antiregular graphs.

We now determine the minimum zero forcing sets and count them. For \(m\ge2\), call a zero forcing set \(S\subseteq V(A_m)\) **ready** if some blue vertex has no white neighbor initially:
\[
N(v)\subseteq S
\quad\text{for some }v\in S.
\]
Let
\[
k_m=Z(A_m),
\]
let \(a_m\) be the number of zero forcing sets of size \(k_m\), let \(r_m\) be the minimum size of a ready zero forcing set, and let \(b_m\) count ready zero forcing sets of size \(r_m\).

The initial graphs give
\[
A_2=K_2,\qquad A_3=P_3,
\]
hence
\[
k_2=k_3=1,\qquad
r_2=r_3=2,
\]
and
\[
(a_2,b_2)=(2,1),\qquad
(a_3,b_3)=(2,2).
\tag{3}
\]

Assume \(m\ge2\), and construct \(A_{m+2}\) from \(A_m\) as in (2). Denote the new pendant vertex by \(p\) and the new universal vertex by \(u\).

If exactly one of \(p,u\) is initially blue, the old vertices must form a zero forcing set of \(A_m\). Indeed, when \(p\) is blue it first colors \(u\), and when \(u\) is blue while \(p\) is white, \(u\) cannot color an old vertex before the old graph has finished. Conversely, any zero forcing set of \(A_m\), together with exactly one of \(p,u\), forces \(A_{m+2}\).

If neither \(p\) nor \(u\) is initially blue, no old vertex can color another old vertex before \(u\) becomes blue, because the white universal vertex is an additional white neighbor of every old vertex. Thus the first move must be an old blue vertex coloring \(u\), which is possible exactly when the old blue set is ready. Afterward the old set must zero-force \(A_m\).

If both \(p,u\) are initially blue, any force by \(u\) into \(A_m\) can occur only when exactly one old vertex is white. Because \(A_m\) is connected, an old blue neighbor could then make the same final force. Hence the old blue set itself must zero-force \(A_m\).

These observations give, simultaneously,
\[
k_{m+2}=k_m+1,
\qquad
r_{m+2}=k_m+2,
\]
so
\[
r_m=k_m+1
\]
for every \(m\ge2\), and therefore
\[
k_m=\left\lfloor\frac m2\right\rfloor.
\tag{4}
\]

They also count the equality cases. A minimum zero forcing set of \(A_{m+2}\) either contains exactly one of \(p,u\) and a minimum set of \(A_m\), or contains neither and a minimum-size ready set of \(A_m\). Thus
\[
a_{m+2}=2a_m+b_m.
\tag{5}
\]

A minimum-size ready set of \(A_{m+2}\) must contain \(u\). If it also contains \(p\), its old part is a minimum zero forcing set of \(A_m\); if it omits \(p\), its old part must itself be a minimum-size ready zero forcing set. Hence
\[
b_{m+2}=a_m+b_m.
\tag{6}
\]

Solving (5)–(6) from (3), with \(F_0=0,F_1=1\), gives
\[
a_m=
\begin{cases}
F_{m+1},&m\text{ even},\\
2F_{m-1},&m\ge3\text{ odd}.
\end{cases}
\tag{7}
\]
Since \(m=\ell-1\), formula (7) becomes
\[
a_{\ell-1}=
\begin{cases}
F_\ell,&\ell\text{ odd},\\
2F_{\ell-2},&\ell\ge4\text{ even}.
\end{cases}
\]

For minimum rank, antiregular graphs are threshold graphs. Malloy proved that every threshold graph satisfies
\[
M(G)=Z(G)
\]
over the real symmetric graph-pattern model. Hence for \(m\ge2\),
\[
M(A_m)=\left\lfloor\frac m2\right\rfloor
\]
and
\[
\operatorname{mr}(A_m)
=
m-M(A_m)
=
\left\lceil\frac m2\right\rceil.
\]
When \(m=1\), \(A_1=K_1\), so \(Z=M=1\) and \(\operatorname{mr}=0\).

## Verification

The accompanying `verify.py` constructs
\[
A_m:\quad i\sim j\Longleftrightarrow i+j\ge m+1
\]
for \(1\le m\le12\). It exhaustively enumerates every vertex subset, computes the zero forcing number, counts all minimum sets, finds the minimum ready sets, and verifies
\[
a_{m+2}=2a_m+b_m,\qquad b_{m+2}=a_m+b_m.
\]
The Fibonacci formulas are checked exactly in every tested order.

The same program independently constructs the compressed graph of
\[
\mathbb Z/(p^\ell)
\]
for \(p=2,3\) and \(2\le\ell\le6\) by computing annihilators of every nonzero zero-divisor directly. It verifies that the annihilator classes have valuations
\[
1,2,\ldots,\ell-1
\]
and that their graph is exactly \(A_{\ell-1}\).

Exact replay output:

```text
m=1: K1 boundary, Z=1, min_sets=1, mr=0
m=2: Z=1, min_sets=2, ready_min=2, ready_sets=1, mr=1
m=3: Z=1, min_sets=2, ready_min=2, ready_sets=2, mr=2
m=4: Z=2, min_sets=5, ready_min=3, ready_sets=3, mr=2
m=5: Z=2, min_sets=6, ready_min=3, ready_sets=4, mr=3
m=6: Z=3, min_sets=13, ready_min=4, ready_sets=8, mr=3
m=7: Z=3, min_sets=16, ready_min=4, ready_sets=10, mr=4
m=8: Z=4, min_sets=34, ready_min=5, ready_sets=21, mr=4
m=9: Z=4, min_sets=42, ready_min=5, ready_sets=26, mr=5
m=10: Z=5, min_sets=89, ready_min=6, ready_sets=55, mr=5
m=11: Z=5, min_sets=110, ready_min=6, ready_sets=68, mr=6
m=12: Z=6, min_sets=233, ready_min=7, ready_sets=144, mr=6
Z/2^2: classes=1, valuations=[1], anti_regular=A_1
Z/2^3: classes=2, valuations=[1, 2], anti_regular=A_2
Z/2^4: classes=3, valuations=[1, 2, 3], anti_regular=A_3
Z/2^5: classes=4, valuations=[1, 2, 3, 4], anti_regular=A_4
Z/2^6: classes=5, valuations=[1, 2, 3, 4, 5], anti_regular=A_5
Z/3^2: classes=1, valuations=[1], anti_regular=A_1
Z/3^3: classes=2, valuations=[1, 2], anti_regular=A_2
Z/3^4: classes=3, valuations=[1, 2, 3], anti_regular=A_3
Z/3^5: classes=4, valuations=[1, 2, 3, 4], anti_regular=A_4
Z/3^6: classes=5, valuations=[1, 2, 3, 4, 5], anti_regular=A_5
VERIFY_OK
```

The finite computations corroborate but do not replace the symbolic chain-ring and recurrence proofs.

## Relationship to prior work

Spiroff and Wickham introduced the annihilator-equivalence zero-divisor graph and developed its relationship with associated primes. Their public preprint was first posted on 29 December 2007 and lists primary Mathematics Subject Classification \(13A15\). Their paper does not discuss zero forcing.

Levit and Mandrescu study the independence polynomial of antiregular graphs. Their full public text records the recurrence
\[
A_{m+2}=K_1\vee(K_1\dot\cup A_m)
\]
and proves that antiregular graphs are threshold graphs, but contains no occurrence of “zero forcing.”

Malloy proves the broader fact that \(M(G)=Z(G)\) for all threshold graphs. Accordingly, the equality \(M=Z\) is prior structural coverage once the zero forcing number is known. The new content here is the compressed-chain-ring identification together with the exact zero forcing number and Fibonacci enumeration of every minimum set.

Targeted searches under “compressed zero-divisor graph,” “annihilator equivalence,” “finite chain ring,” “antiregular graph,” “zero forcing,” “minimum rank,” and “Fibonacci” did not locate the formulas above.

## Limitations

The theorem assumes that \(R\) is a finite chain ring. General finite local rings can have several incomparable annihilator classes and need not produce an antiregular compressed graph.

The compressed graph depends only on the nilpotency length in this family. It therefore forgets the residue-field order and can identify neither that order nor the isomorphism type of the chain ring.

The minimum-rank conclusion uses the real symmetric graph-pattern model.

The minimum-set count is proved, but the complete zero forcing polynomial of \(A_m\) is not determined here.

## References

1. S. Spiroff and C. Wickham, “A zero divisor graph determined by equivalence classes of zero divisors,” arXiv:0801.0086, first posted 29 December 2007; later published in *Communications in Algebra* 39 (2011), 2338–2348. DOI: 10.1080/00927872.2010.488675.
2. V. E. Levit and E. Mandrescu, “On the independence polynomial of an antiregular graph,” arXiv:1007.0880, first posted 6 July 2010; *Carpathian Journal of Mathematics* 28 (2012), 279–288.
3. N. A. Malloy, “Minimum Rank Problems for Cographs,” M.S. thesis, Brigham Young University, 2013.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
