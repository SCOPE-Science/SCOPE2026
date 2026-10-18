# Two-regime normal form and exact enumeration of finite-chain modal Kleene operators

## Finding
For every integer \(n\ge1\), let \(K_n=\{0,1,\ldots,n-1\}\), ordered as a chain with \(x\wedge y=\min(x,y)\), \(x\vee y=\max(x,y)\), and involution \(\sim x=n-1-x\). Let \(T_n\) be the number of unary operations \(f:K_n\to K_n\) satisfying all three displayed modal Kleene conditions (M), (Pos), and (Con) below. Put \(c=\lfloor(n-1)/2\rfloor\), \(p=\lfloor n/2\rfloor\). Such an operation satisfies these conditions **if and only if** it is nondecreasing, \(f(p)\ge p\), and either \(f(c)\le c\) or \(f\) is constant on \(\{0,\ldots,c\}\). These alternatives are disjoint except that the constant-prefix requirement is redundant in the first one; in the enumeration we partition instead by \(f(c)\le c\) versus \(f(c)>c\).

The resulting exact counts are, for \(h\ge1\),
\[
T_{2h}=\binom{2h-1}{h}^{\!2}+\binom{2h}{h+1},\qquad
T_{2h+1}=\binom{2h}{h}^{\!2}+\binom{2h}{h+1},
\]
with \(T_1=1\). The count \(U_n\) of those operations that also satisfy \(f(n-1)=n-1\) is \(U_1=1\) and
\[
U_{2h}=\binom{2h-1}{h}\binom{2h-2}{h-1}+\binom{2h-1}{h},\quad
U_{2h+1}=\binom{2h}{h}\binom{2h-1}{h-1}+\binom{2h-1}{h}.
\]
As \(n\to\infty\),
\[
T_n\sim\frac{4^n}{2\pi n},\qquad U_n\sim\frac{4^n}{4\pi n},\qquad
\frac{T_n}{\binom{2n-1}{n}}\sim\frac{1}{\sqrt{\pi n}}.
\]
Thus the modal conditions select a proportion asymptotic to \(1/\sqrt{\pi n}\) of all meet-preserving unary self-maps of the chain, while asymptotically half of the admissible maps preserve the greatest element.

## Assumptions and scope
The algebra \(K_n\) is the unique \(n\)-element Kleene chain, and its involution is fixed. The primitive modal operation is \(f\), also written \(\Box\). The **exact axioms** used, for all \(x,y,z\in K_n\), are
\[
\begin{aligned}
\mathrm{(M)}\quad&f(x\wedge y)=f(x)\wedge f(y),\\
\mathrm{(Pos)}\quad&\sim f(z\vee\sim z)\le f(z\vee\sim z),\\
\mathrm{(Con)}\quad&f(x\vee(z\wedge\sim z))\le f(x)\vee\sim f(x\vee(z\wedge\sim z)).
\end{aligned}
\]
Preservation of the greatest element is **not** part of these three axioms; \(U_n\) counts it as a separately imposed property. “Meet preservation” here means preservation of the displayed binary meet, without an implicit nullary condition. Counts refer to operations on the fixed chain; since a finite chain has no nonidentity order automorphism, they also count expansions up to isomorphism of ordered involutive carriers.

## Proof
Write \(c=\lfloor(n-1)/2\rfloor\) and \(p=\lceil(n-1)/2\rceil=\lfloor n/2\rfloor\). Note that \(c+p=n-1\). Because \(K_n\) is totally ordered, (M) is equivalent to the order-preserving property: if \(x\le y\), meet preservation gives \(f(x)=\min(f(x),f(y))\), and the converse is immediate.

For every \(z\), \(z\vee\sim z\ge p\), and every integer in \([p,n-1]\) occurs as such a join. Similarly \(z\wedge\sim z\) ranges over \([0,c]\). For an output \(v\), \(\sim v\le v\) is equivalent to \(v\ge p\). Consequently, for nondecreasing \(f\), (Pos) holds if and only if \(f(p)\ge p\).

For (Con), put \(t=z\wedge\sim z\), \(a=f(\max(x,t))\), and \(b=f(x)\). Monotonicity gives \(a\ge b\). The inequality \(a\le\max(b,n-1-a)\) holds precisely when either \(a=b\) or \(a\le c\). If \(f(c)\le c\), then every strict increment caused by replacing \(x\) by \(\max(x,t)\) occurs at an input at most \(c\), hence at an output at most \(c\), so (Con) holds. Conversely, if \(f(c)>c\), choose \(z\) with \(z\wedge\sim z=c\). Taking each \(x\le c\) forces \(f(x)=f(c)\). If the prefix is constant then (Con) holds: for \(x\le c\) there is no increment, and for \(x>c\) one has \(\max(x,t)=x\). This proves the normal form, including the one-element case.

For \(n=2h\), the small-output regime \(f(h-1)\le h-1\), together with (Pos), consists of an arbitrary weakly increasing \(h\)-tuple in \(\{0,\ldots,h-1\}\) and an independent weakly increasing \(h\)-tuple in \(\{h,\ldots,2h-1\}\). Each contributes \(\binom{2h-1}{h}\) choices. In the large-output regime, \(f(0)=\cdots=f(h-1)=r\) with \(h\le r\le2h-1\), and the remaining \(h\) outputs are weakly increasing from \(r\) to at most \(2h-1\). Stars and bars gives \(\binom{3h-r-1}{h}\) choices for each \(r\); summing over \(r\) gives \(\binom{2h}{h+1}\).

For \(n=2h+1\), the small-output regime forces \(f(h)=h\); its two independent tails are weakly increasing \(h\)-tuples with values in \(\{0,\ldots,h\}\) and \(\{h,\ldots,2h\}\), respectively. Hence it contributes \(\binom{2h}{h}^{2}\). In the large-output regime \(f(0)=\cdots=f(h)=r\) with \(h+1\le r\le2h\), and the remaining \(h\) outputs give \(\binom{3h-r}{h}\) choices; their sum is again \(\binom{2h}{h+1}\).

Imposing \(f(n-1)=n-1\) fixes the last output in each weakly increasing upper tuple, reducing that tuple's length by one. In the even small regime this gives \(\binom{2h-1}{h}\binom{2h-2}{h-1}\), and in the odd small regime \(\binom{2h}{h}\binom{2h-1}{h-1}\). In either large regime, summing the shortened upper tuples by the hockey-stick identity gives \(\binom{2h-1}{h}\). This proves both formulas for \(U_n\).

Finally, the central-binomial estimate and Stirling's formula yield, uniformly over the two parities, \(\binom{n-1}{\lfloor n/2\rfloor}^{2}\sim4^n/(2\pi n)\). The additional \(\binom{2h}{h+1}\) term grows only on the order of \(2^n/\sqrt n\) and is exponentially smaller. The small-regime contribution to \(U_n\) is asymptotically one-half of that to \(T_n\), while its large-regime contribution is negligible. There are exactly \(\binom{2n-1}{n}\sim 4^n/(2\sqrt{\pi n})\) nondecreasing maps from an \(n\)-chain to itself. Substitution proves the three asymptotics.

## Verification
The standalone `checker.py` implements (M), (Pos), and (Con) directly from their quantified definitions without assuming the normal form; it separately implements the claimed normal form and the closed formulas. Run `python3 checker.py` with Python 3 standard library. All \(n^n\) maps are checked for \(1\le n\le6\); for \(7\le n\le10\) the checker exhausts all nondecreasing maps (all possible candidates after (M)), including checks of the greatest-element-preserving count. Its output ends in `EXHAUSTIVE_CHECK_OK`. The counts for \(n=1,\ldots,10\) are \(1,2,5,13,40,115,415,1281,4956,16086\), and the greatest-element-preserving counts are \(1,2,3,9,21,70,210,735,2485,8946\). These finite checks corroborate, but do not establish, the arbitrary-size theorem; the proof above supplies the infinite quantifiers.

## Relationship to prior work
The 2026 preprint of Celani, Menchón and Miguelez introduces modal Kleene algebras and their categorical representation by modal triples and twist products [1]. This finding uses the displayed unary axioms on the canonical finite Kleene chains to give a direct exact classification and enumeration, including the top-preserving subclass and asymptotic frequencies; it does not assert a new categorical equivalence. Chajda, Länger and Paseka [2] characterize constructions of Kleene lattices and represent every finite Kleene chain as an underlying lattice but do not count unary modal expansions. Celani and Rivieccio [3] study nuclei on Heyting-style structures, with different modal requirements (in particular closure conditions), not the three conditions here.

## Limitations
No assertion concerns non-chain carriers, extra axioms such as idempotence or extensivity, or equivalence to a particular Kripke logic. This is not a formal proof in a proof assistant. The motivating 2026 preprint's abstract and a detailed third-party overview were accessible, but its full original text could not be retrieved during the literature comparison. Consequently the originality assessment carries the residual risk that a matching finite-chain enumeration already appears in its inaccessible sections or in unindexed literature. The result is independently stated and proved from the explicit axioms above and does not depend on the overview for correctness.

## References
[1] S. Celani, P. Menchón, V. Miguelez, *A Modal Expansion of Kleene Algebras via Twist Structures*, arXiv:2608.10937, first version 2026-08-11. https://arxiv.org/abs/2608.10937

[2] I. Chajda, H. Länger, J. Paseka, *Constructions of Kleene lattices*, arXiv:2111.00455, 2021. https://arxiv.org/abs/2111.00455

[3] S. A. Celani, U. Rivieccio, *Intuitionistic Modal Algebras*, *Studia Logica* **112** (2024), 611–660, initially published 2023. https://doi.org/10.1007/s11225-023-10065-2
