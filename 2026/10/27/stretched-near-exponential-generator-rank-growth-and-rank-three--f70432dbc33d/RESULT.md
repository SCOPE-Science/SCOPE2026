# Stretched near-exponential generator-rank growth and rank-three dominance in full transformation endomorphism monoids

## Finding

Let \(\mathcal T_n\) denote the full semigroup of functions on an \(n\)-element set. Write \(m(n)\) for the minimum cardinality of a generating set of the semigroup endomorphism monoid \(\operatorname{End}(\mathcal T_n)\), and \(r_3(n)\) for the number of rank-three endomorphism orbits under right multiplication by automorphisms, equivalently simultaneous conjugacy classes of their permissible pairs (rank refers to the endomorphism's image cardinality). Then, as \(n\to\infty\) through integers \(n\ge5\),
\[
\boxed{\log m(n)=\Theta\!\left(\frac{n}{\sqrt{\log n}}\right),\qquad\frac{m(n)}{r_3(n)}\to1.}
\]
Both statements use natural logarithms. A quantitative version is
\[
\boxed{\frac1{648}\le\liminf_{n\to\infty}\frac{\sqrt{\log n}}{n}\log m(n)
\le\limsup_{n\to\infty}\frac{\sqrt{\log n}}{n}\log m(n)
\le\sqrt{\frac{\zeta(3)}2}.}
\]
In particular, the logarithmic growth has order strictly between the plane-partition scale \(n^{2/3}\) and linear growth. The result supplies an asymptotic growth scale for the minimum generating-set problem explicitly posed in Gould–Grau–Johnson, §8. It does **not** assert that the normalized logarithm converges to a sharp constant.

## Assumptions and scope

Endomorphisms are **semigroup** homomorphisms of \(\mathcal T_n\), and need not fix its identity. The assertions concern all sufficiently large positive integers \(n\), with the structural rank formula applicable for \(n\ge5\). The parameter \(r_3(n)\) counts right-action orbits under postcomposition by automorphisms, which induce simultaneous conjugation of the underlying pairs \((t,e)\); it does not count endomorphism conjugacy under two-sided conjugation or labeled transformations. The singular maps of rank three arise from permissible pairs \((t,e)\) satisfying \(t^3=t\), \(e^2=e\), and \(te=et=e\), with \(t^2\ne t\). Here compositions are transformation products, and \(\zeta\) is the Riemann zeta function.

We use these explicitly defined formal power series:
\[
A(z)=\frac{z}{1-z},\quad P(z)=\prod_{j\ge1}(1-z^j)^{-1},\quad
Q(z)=\prod_{j\ge2}(1-z^j)^{-\lfloor j/2\rfloor},
\]
\[
F(z)=A(z)P(z)Q(z),\qquad F_0(z)=A(z)P(z),\qquad
\mathscr M(H)(z)=\prod_{j\ge1}(1-z^j)^{-[z^j]H(z)}.
\]
Products and formal coefficient extractions are locally finite; evaluation at a real \(0<z<1\) converges absolutely. The exact orbit representation
\[
r_3(n)=[z^n]\left(\mathscr M(F)(z)-\mathscr M(F_0)(z)\right)
\tag{1}
\]
is an already-established exact enumeration; it is derived structurally below solely to make the asymptotic proof self-contained. Gould–Grau–Johnson established
\[
m(n)=3+r_3(n)+r_2(n),\tag{2}
\]
where \(r_2(n)\) counts essential rank-two orbits. The exact Euler-product evaluation of \(r_2(n)\), and equation (1), are not the contributions claimed here.

## Proof

**1. Reconstruction of the rank-three orbit species.** A transformation \(t\) with \(t^3=t\) consists of fixed-point stars and directed two-cycles, each of whose vertices may receive arbitrary additional incoming leaves. The conditions \(te=et=e\) force every \(e\)-fiber to contain exactly one distinguished \(t\)-fixed point, which is the fixed point of \(e\) on that fiber; all other \(t\)-components remain inside that fiber. A fixed-point star with its root distinguished and any number of leaves has ordinary type series \(A(z)\). The unlabelled multiset of remaining fixed-point stars contributes \(\mathscr M(A)=P\).

An unlabelled two-cycle with \(u\) leaves on its first vertex and \(v\) leaves on its second is determined by the unordered pair \(\{u,v\}\), because the two cycle vertices may be exchanged. It therefore has size \(2+u+v\) and type series
\[
B(z)=\frac{z^2}{(1-z)(1-z^2)}=\sum_{j\ge2}\lfloor j/2\rfloor z^j.
\]
The multiset of all such two-cycle components has series \(\mathscr M(B)=Q\). Thus the type series of a single \(e\)-fiber is \(F=APQ\); after excluding two-cycles, it is \(F_0=AP\). An admissible pair \((t,e)\) is a multiset of such fibers. Postcomposition by an automorphism \(\psi_g\) takes \(\phi_{t,e}\) to \(\phi_{g^{-1}tg,g^{-1}eg}\). Thus the requisite right-action orbits coincide with simultaneous relabeling orbits, which are enumerated by \(\mathscr M(F)\), and those with \(t^2=t\) by \(\mathscr M(F_0)\). Subtraction yields (1). In particular every rank-three orbit corresponds to a multiset having at least one two-cycle component.

**2. Upper bound.** Let \(c=\zeta(3)/2\), and take \(t\in(0,1)\). The Euler-product logarithm and the inequalities \(e^x-1\ge x\) and \(\sum_{j\ge1} j e^{-xj}\le x^{-2}\) imply
\[
A(e^{-t})\le t^{-1},\quad
\log P(e^{-t})\le\frac{\zeta(2)}t,\quad
\log Q(e^{-t})\le\frac{c}{t^2}.
\]
Indeed, for \(Q\), expand \(-\log(1-e^{-jt})\) and use \(\lfloor j/2\rfloor\le j/2\); summing the resulting \(\tfrac{1}{2h}(ht)^{-2}\) bounds over \(h\ge1\) gives \(c/t^2\). Consequently
\[
F(e^{-t})\le t^{-1}\exp\!\left(\frac{\zeta(2)}t+\frac{c}{t^2}\right).
\]
Every term of \(F\) has positive degree. Thus \(F(e^{-ht})\le e^{-(h-1)t}F(e^{-t})\) for every integer \(h\ge1\), giving
\[
\log\mathscr M(F)(e^{-t})=\sum_{h\ge1}\frac{F(e^{-ht})}{h}
\le\frac{F(e^{-t})}{1-e^{-t}}
\le\frac{2}{t^2}\exp\!\left(\frac{\zeta(2)}t+\frac{c}{t^2}\right).
\tag{3}
\]
Similarly, \(\log\mathscr M(F_0)(e^{-t})\le2t^{-2}\exp(\zeta(2)/t)\).

Write \(G=\mathscr M(F)\) and \(G_0=\mathscr M(F_0)\). Rank-two permissible pairs have \(t^2=t\), so their right-action orbit count, and hence the essential subcount \(r_2(n)\), is bounded by \([z^n]G_0\). By positivity and equation (2),
\[
m(n)\le3+[z^n]G+[z^n]G_0\le3+2[z^n]G.
\]
Cauchy's coefficient bound \([z^n]G\le e^{nt}G(e^{-t})\) and (3) now apply. For any fixed \(\varepsilon>0\), choose
\[
t=\sqrt{\frac{c+\varepsilon}{\log n}}.
\]
Then \(\log G(e^{-t})=n^{c/(c+\varepsilon)+o(1)}=o(n/\sqrt{\log n})\), and hence
\[
\limsup_{n\to\infty}\frac{\sqrt{\log n}}n\log m(n)\le\sqrt{c+\varepsilon}.
\]
Letting \(\varepsilon\downarrow0\) proves the stated upper constant. Independently, taking \(t=2\zeta(2)/\log n\) for \(G_0\) gives
\[
\log\bigl(1+r_2(n)\bigr)=O\!\left(\frac{n}{\log n}\right).
\tag{4}
\]

**3. Constructive lower bound.** Fix sufficiently large \(n\), and let \(L=\lfloor6\sqrt{\log n}\rfloor\). Consider the unlabelled two-cycle components of every size \(j\in\{L,\ldots,2L\}\). There are
\[
M=\sum_{j=L}^{2L}\lfloor j/2\rfloor\ge L^2/3
\]
distinct component types, and \(M\le2L^2\) for large \(L\). Set \(H=\lfloor M/2\rfloor\). Each \(H\)-element subset of the \(M\) types defines one unlabelled \(e\)-fiber: adjoin one distinguished fixed point (no incoming leaves) to those \(H\) pairwise distinct two-cycle components. The fiber's size lies between \(1+HL\) and \(1+2HL\). By the central binomial bound \(\binom MH\ge2^M/(M+1)\), one size \(s\) is realized by at least
\[
T\ge\frac{2^M}{(M+1)(HL+1)}
\tag{5}
\]
different fiber types, all containing two-cycles. Since \(M\ge L^2/3\) and \(L^2\sim36\log n\), (5) implies \(T\ge n^3\) for all sufficiently large \(n\). Also
\[
s\le1+2LH\le1+2L^3\le648(\log n)^{3/2}
\]
for all sufficiently large \(n\).

Let \(k=\lfloor n/s\rfloor\), and take arbitrary multisets of \(k\) of these \(T\) fiber types. If \(r=n-ks>0\), add one further fiber of size \(r\), consisting of a single fixed-point star and no two-cycle. Because \(r<s\), this padding fiber cannot be confused with any selected size-\(s\) fiber; multiset choices remain pairwise nonisomorphic. Their common transformations \(t\) contain two-cycles, so every such pair determines a rank-three orbit. We obtain
\[
r_3(n)\ge\binom{T+k-1}{k}\ge\left(\frac{T}{k}\right)^k\ge n^{2k}.
\]
For large \(n\), \(k\ge n/(2s)\). Therefore
\[
\log r_3(n)\ge2k\log n\ge\frac{n\log n}{s}\ge\frac{n}{648\sqrt{\log n}}.
\tag{6}
\]
This proves the quantitative lower constant and, together with the upper estimate, the \(\Theta\)-law.

**4. Rank-three dominance.** The essential rank-two orbit bound (4) is \(\exp(O(n/\log n))\), whereas (6) gives \(r_3(n)\ge\exp(n/(648\sqrt{\log n}))\) eventually. Hence \(r_2(n)/r_3(n)\to0\) and \(3/r_3(n)\to0\). Equation (2) completes the proof:
\[
\frac{m(n)}{r_3(n)}=1+\frac{r_2(n)+3}{r_3(n)}\longrightarrow1.
\]

## Verification

The accompanying `checker.py` performs independent integer computations from the ordinary partition, unlabelled two-cycle and multiset transforms, checking the resulting orbit and generator counts for all degrees up to \(40\). It reports a validation table at selected sizes and the marker `VERIFY_OK`. This is a finite coefficient check only. The rigorous asymptotic bounds follow from inequalities (3)–(6), not extrapolation from finite data. To reproduce: run `python3 checker.py` with Python 3 and no additional packages.

## Relationship to prior work

Gould, Grau and Johnson prove the structural rank formula (2) in Proposition 4.2, describe rank-three permissible pairs in §2 and their orbit structure in §4, and explicitly raise the asymptotic growth question in §8. The preprint first appeared July 21, 2023. Earlier exact multiset/Euler-product enumeration already gives equation (1) and the exact finite generator counts; neither that exact count nor the connection with plane partitions is claimed new here. The novel assessed statements are the logarithmic growth scale, the quantitative bounds and the asymptotic dominance of rank-three orbits.

Krattenthaler and Müller analyze labeled solutions to different transformation-semigroup equations, notably commuting *idempotent* pairs, and obtain asymptotics for those labeled solution numbers. Their equations \(X^2=X\), \(Y^2=Y\), \(XY=YX\), and their labeled-count asymptotics do not imply the unlabelled rank-three orbit asymptotics for pairs with \(t^3=t\) and \(te=et=e\): an involutory two-cycle is expressly excluded by their idempotence equation. The comparison was made against the source's full-text introduction and sections on the commuting-idempotent system and its asymptotics.

## Limitations

The leading normalized constant is not identified: the displayed liminf/limsup bounds need not be sharp. The result does not count generators of the identity-preserving *monoid*-endomorphism monoid, nor does it determine the number of all endomorphisms. It concerns generator-set *cardinality* rather than the number of distinct minimal generating sets. Unlocated equivalent asymptotic results under alternative combinatorial-assembly terminology remain a possible originality risk; no exhaustive priority claim is made. The computation checks only small degrees and is not a proof of the infinite assertions.

## References

1. V. Gould, A. Grau and M. Johnson, *The structure of End(\(\mathcal T_n\))* (first preprint July 21, 2023), arXiv:2307.11596v1, especially §§2, 4 and 8. https://arxiv.org/abs/2307.11596
2. C. Krattenthaler and T. Müller, *Equations in finite semigroups: Explicit enumeration and asymptotics of solution numbers* (first preprint March 3, 2003), arXiv:math/0303028, §§1, 5–6. https://arxiv.org/abs/math/0303028
