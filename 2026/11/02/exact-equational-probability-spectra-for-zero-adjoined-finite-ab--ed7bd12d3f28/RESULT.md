# Exact equational probability spectra for zero-adjoined finite abelian groups

## Finding

Let \(G\) be any **nontrivial finite abelian group**, written additively, with \(q=|G|\ge 2\) and exponent \(m\). Let \(S=G\sqcup\{\bot\}\) be its multiplicative semigroup, with the group operation as multiplication on \(G\) and with the newly adjoined element \(\bot\) absorbing. Only the multiplication operation belongs to the language; there are **no constants or unary operations**. Define \(s=q/(q+1)\) and
\[
\mathcal C_G=\left\{\frac1{|dG|}:d\mid m\right\},\qquad dG=\{dg:g\in G\}.
\]
Here, as usual, \(mG=\{0_G\}\), so \(1\in\mathcal C_G\). The complete set of probabilities of **all** finite-variable, constant-free equations between nonempty semigroup words is
\[
\boxed{\displaystyle
\operatorname{PSpec}(S)=\left\{
1-s^i-s^j+(1+c)s^u:\ i,j\in\mathbb Z_{\ge1},\quad
\max(i,j)\le u\le i+j,\quad c\in\mathcal C_G
\right\}.}
\]
Every listed parameter choice is attained by an explicit pair of words. Consequently,
\[
\min\operatorname{PSpec}(S)=\frac1{q+1}.
\]
The minimum occurs **exactly** for word equations whose two nonempty supports are disjoint, at least one support is a singleton, and whose exponent-difference homomorphism onto \(G\) is surjective.

Writing \(X'\) for the set of accumulation points of \(X\subset\mathbb R\),
\[
\boxed{\operatorname{PSpec}(S)'=\{1-s^h:h\ge1\}\cup\{1\},\quad
\operatorname{PSpec}(S)''=\{1\},\quad
\operatorname{PSpec}(S)'''=\varnothing.}
\]
Thus the spectrum is a countable non-dense subset of \([0,1]\), and its Cantor--Bendixson rank (the first derivative index giving the empty set) is exactly three.

The spectrum can detect more than group order: for \(G=C_4\) the equation \(x^2\approx x^4\) has probability \(3/5\), while \(3/5\notin\operatorname{PSpec}((C_2\times C_2)^0)\). Both zero-adjoined groups have five elements. This final separation is proved below, not inferred from finite truncation.

## Assumptions and scope

All algebraic terms are nonempty products of variables in the **single binary semigroup signature**, and an equation is evaluated on independent, uniformly sampled variables in \(S\). The term variables may repeat, and two terms may share some variables. The exponent \(m\) is the least common multiple of the orders of elements of \(G\). The notation \(x^2\) denotes multiplication in the semigroup and not multiplication by a scalar in a ring. The class of underlying groups is finite and abelian; it includes arbitrary products of cyclic prime-power groups, but not general nonabelian groups. The case \(G\) trivial is deliberately excluded because the corresponding two-element semilattice spectrum has been studied previously.

## Proof

**1. Normal form for a word pair.** Since \(G\) is abelian and \(\bot\) is absorbing, a semigroup word \(w\) is uniquely evaluated by a nonempty support \(I\) of variables and positive integer exponents \(a_t\) on this support. For an assignment, \(w=\bot\) exactly when at least one variable from \(I\) equals \(\bot\); otherwise \(w\) is the group sum \(\sum_{t\in I}a_tx_t\). Let the other word have support \(J\) and exponents \(b_t\). Put \(i=|I|\), \(j=|J|\), and \(u=|I\cup J|\). Necessarily \(i,j\ge1\) and \(\max(i,j)\le u\le i+j\).

**2. The probability formula.** Each variable is group-valued with probability \(s=q/(q+1)\), independently. The probability that both words evaluate to the absorbing element is
\[
1-s^i-s^j+s^u.
\]
The only other way they can agree is when all \(u\) variables in \(I\cup J\) are in \(G\) and their group sums coincide. Extend the exponent vectors by zero outside their supports; the equality is
\[
\phi((x_t)_{t\in I\cup J})=\sum_{t\in I\cup J}(a_t-b_t)x_t=0_G.
\]
Let \(\delta_t=a_t-b_t\), and set \(d=\gcd(m,(\delta_t)_{t\in I\cup J})\). The image of \(\phi\) equals \(\sum_t\delta_tG=dG\): one inclusion holds because each \(\delta_t\) is divisible by \(d\), while the reverse follows from the integer Bézout identity expressing \(d\) as a combination of \(m\) and the \(\delta_t\), since \(mG=\{0_G\}\). A homomorphism of finite groups has equally sized fibers. Conditional on all variables lying in \(G\), the equation therefore holds with probability \(c=1/|dG|\). Adding the disjoint cases gives
\[
\Pr(w\approx w')=1-s^i-s^j+(1+c)s^u.
\]
In particular, this probability belongs to the displayed family.

**3. Every parameter is realized.** Given positive integers \(i,j\), and \(u\) between their maximum and sum, choose finite nonempty supports \(I,J\) of sizes \(i,j\) and union size \(u\). Fix any divisor \(d\mid m\), and select one variable \(t_0\in I\cup J\). Give every occurrence of a variable a total positive exponent divisible by \(m\) in each word in which it occurs. Then increase the exponent of \(t_0\) by \(d\) on whichever side contains \(t_0\), leaving the other side unchanged. This is possible with positive integer exponents and the prescribed supports. The exponent difference is \(\pm d\) at \(t_0\) and divisible by \(m\) at every other position; hence its image is \(dG\). This produces the desired \(c=1/|dG|\). The displayed formula is therefore both necessary and sufficient, with no hidden restrictions on its integer parameters.

**4. Sharp minimum, including equality.** Because \(|dG|\le q\), we always have \(c\ge1/q\). Since \(0<s<1\) and \(u\le i+j\),
\[
\Pr(w\approx w')\ge
F(i,j):=1-s^i-s^j+\left(1+\frac1q\right)s^{i+j}
=1-s^i-s^j+s^{i+j-1}.
\]
For fixed \(j\ge1\),
\[
F(i+1,j)-F(i,j)=(1-s)s^i(1-s^{j-1})\ge0,
\]
and similarly in the other coordinate. Thus \(F(i,j)\ge F(1,1)=1-s=1/(q+1)\). Equality in \(F\ge F(1,1)\) occurs exactly when \(\min(i,j)=1\) (the increment is strictly positive if both indices exceed one). Equality in the two preceding bounds requires \(c=1/q\) and \(u=i+j\), respectively. These are exactly the stated support and surjectivity conditions, and they are attained, for example, by \(x\approx y\).

**5. All and only the accumulation points.** The set \(\mathcal C_G\) is finite. Consider an infinite sequence of **distinct** spectrum values converging in \([0,1]\). Choose a sequence of representing quadruples \((i,j,u,c)\). If both \(i\) and \(j\) are bounded, then \(u\le i+j\) and \(c\in\mathcal C_G\), so only finitely many values occur, a contradiction. Passing to a subsequence and interchanging the two words if needed, we may arrange either that \(i\to\infty\) and \(j=h\) is a fixed positive integer, or that both \(i,j\to\infty\). In the first situation \(u\ge i\to\infty\), and the limit is \(1-s^h\). In the second, \(u\to\infty\), and the limit is \(1\). Conversely, for every \(h\ge2\) choose \(i\to\infty\), \(j=h\), \(u=i+h\), and \(c=1/q\). The resulting values are \(1-s^h+(s^{h-1}-1)s^i\), pairwise distinct and tending to \(1-s^h\). For \(h=1\), take \(c=1\) instead: the values \(1-s+(2s-1)s^i\) are distinct because \(q\ge2\) implies \(2s-1>0\). Finally take \(i=j\to\infty\), \(u=2i\), and \(c=1/q\) to obtain distinct values converging to \(1\). Thus the first derived set is precisely the displayed countable convergent sequence and its endpoint. The second derived set consists only of \(1\); the third is empty.

**6. A group-structure witness.** For \(C_4^0\), the word equation \(x^2\approx x^4\) holds for the absorbing element, the identity, and the element of order two, but not for either element of order four. Its probability is \(3/5\).

For \((C_2\times C_2)^0\), the only possible conditional group probabilities are \(c=1\) or \(c=1/4\). Suppose that the spectrum formula equals \(3/5\), put \(s=4/5\), and assume \(1\le i\le j\le u\). Multiplying \(1-\Pr=2/5\) by \(5^u\) gives
\[
2\cdot5^{u-1}=4^i5^{u-i}+4^j5^{u-j}-(1+c)4^u.\tag{*}
\]
If \(u=1\), both supports have size one and coincide, giving probability either \(1\) or \(2/5\), not \(3/5\). Assume \(u\ge2\). If \(c=1\), then for \(u>j\) the right-hand side of (*) is congruent to \(-2\cdot4^u\) modulo five, whereas the left-hand side is divisible by five. For \(u=j>i\), the same argument gives \(-4^u\) modulo five. If \(u=j=i\), the probability is \(1\). Thus \(c=1\) cannot occur.

If \(c=1/4\), the last term in (*) is \(-5\cdot4^{u-1}\). When \(j=u\), reducing (*) modulo five gives a nonzero right-hand side (one or two copies of \(4^u\)), impossible. When \(j\le u-2\), necessarily \(u\ge3\); divide (*) by five and reduce modulo five: its right-hand side is \(-4^{u-1}\ne0\) but its left-hand side is divisible by five. The remaining case is \(j=u-1\). Now the term \(4^j5^{u-j}\) cancels \(5\cdot4^{u-1}\), so (*) becomes \(2\cdot5^{i-1}=4^i\). This is impossible for \(i=1\) and, by divisibility by five, for \(i\ge2\). Thus \(3/5\) is absent from the spectrum of \((C_2\times C_2)^0\), completing the separation.

## Verification

The reproducible scripts `verify_general.py` and `verify_elementary.py` perform direct word-evaluation over the zero-adjoined groups and independently evaluate the symbolic formula using exact rational arithmetic. The general script covers cyclic groups of orders three, four, and six; the Klein four group; and products \(C_4\times C_2\), \(C_2^3\), and \(C_2\times C_3\), checking 25,269 pairs of words. The second script checks 8,428 pairs over elementary abelian groups, including an order-four group and a four-variable case, and checks the analytic minimum on six group orders over finite parameter ranges. Both output `VERIFY_OK`; the raw outputs are embedded alongside the scripts. These computations verify finite cases only. Parts 1–6 above provide the infinite-parameter proof; no extrapolation from finite searches is used for the spectrum, its derived sets, or the separation.

## Relationship to prior work

Cardó, *On semigroups and groupoids with minimal probabilistic spectrum* (arXiv:2603.19487, first version March 19, 2026), introduces the spectrum in this setting and classifies finite semigroups whose spectrum consists of only \(1\) and the inverse of their order. It does not give the present explicit nonminimal spectrum for zero-adjoined nontrivial abelian groups. Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras* (arXiv:2604.08446, April 9, 2026), studies limits and density and computes the **two-element semilattice** spectrum in Example 4.1. That known trivial-group boundary is excluded here; no claim is made that a semilattice spectrum was previously unknown. These papers provide conceptual motivation and the probability definition, but neither yields the general power-image formula, sharp equality characterization, Cantor--Bendixson computation, or equal-order group-separation proof as stated.

## Limitations

The finite abelian hypothesis is essential to the linear-image argument. For nonabelian groups, word maps may have nonuniform fibers and the stated formula need not hold. The language has only multiplication; adjoining an explicit absorbing constant or allowing all named constants changes the set of admissible equations. An exact formula for a family is not a classification of all finite semigroups. The finite checkers do not establish historical novelty or provide independent mathematical review. Historical-priority risk remains for older semigroup word-map results under different terminology.

## References

1. Carles Cardó, *On semigroups and groupoids with minimal probabilistic spectrum*, arXiv:2603.19487 (first posted March 19, 2026), https://arxiv.org/abs/2603.19487 . Relevant sections: 2 and 4, Theorem 9.
2. Carles Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, arXiv:2604.08446 (first posted April 9, 2026), https://arxiv.org/abs/2604.08446 . Relevant sections: 2 and 4, especially Example 4.1.
3. Evelyn Nelson, *The lattice of equational classes of semigroups with zero*, Canadian Mathematical Bulletin **14** (1971), 531–534. This concerns equational classes rather than probabilities and is not used as a covering theorem.
