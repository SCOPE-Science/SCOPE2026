# Sharp four-step loss of occupation-time universality in a sign-persistent walk

## Finding
Let \(\eta_1,\eta_2,\ldots\) be independent, identically distributed, strictly positive, non-atomic random variables. Independently, let \(\sigma_1\) be fair in \(\{-1,+1\}\), and construct a sign process with \(\Pr(\sigma_{j+1}=\sigma_j)=q\), independently across sign transitions, for \(0\le q\le1\). Put \(S_0=0\), \(S_j=\sum_{i=1}^j\sigma_i\eta_i\), and \(K_n=\sum_{j=1}^n\mathbf1_{\{S_j>0\}}\). Define the single magnitude-law parameter
\[
 v=\Pr(\eta_1>\eta_2+\eta_3),\qquad 0\le v<\frac13.
\]
For \(n\le3\), the distribution of \(K_n\) is independent of the magnitude law. At the first potentially sensitive horizon \(n=4\), define
\[
 a(q)=\frac{5q^3-3q^2+3q+3}{16},\qquad
 b(q,v)=\frac{(1-q)(3-4q+5q^2)}8+v(1-q)^2(2q-1).
\]
Then its **complete** law is
\[
 \bigl(\Pr(K_4=k)\bigr)_{k=0}^4
 =\left(a,\frac{1-2a-b}{2},b,\frac{1-2a-b}{2},a\right).
\]
The dependence on the magnitude law is absent at horizon four precisely for \(q=1/2\) and \(q=1\). For every other persistence parameter, already the probability \(\Pr(K_4=2)\) depends nontrivially on the magnitude distribution. For each fixed \(q\), the sharp range of this probability is the interval between \(b(q,0)\) (attained) and \(b(q,1/3)\) (not attained): if \(q<1/2\), the former is the maximum, while if \(1/2<q<1\), it is the minimum. At \(q=1/2\) or \(q=1\) the range is a singleton.

## Assumptions and scope
All jumps are strictly positive in magnitude, iid and non-atomic; neither density nor moments are required. For fixed \(n\), every nonempty signed sum of the independent magnitudes has probability zero of equaling zero, so the strict positive-occupation convention is unambiguous. The sign chain and magnitudes are independent. Initial sign is fair; subsequent signs are retained with probability \(q\) independently between times. The result concerns discrete sampling times \(1,\ldots,n\), not continuous-time residence.

## Proof
**Step 1: reflection.** Replacing all signs by their negatives preserves the walk law and complements every partial-sum sign. Thus \(\Pr(K_n=k)=\Pr(K_n=n-k)\). For \(n=1\) the law is \((1/2,1/2)\); direct inspection of the first two or three signs gives, respectively,
\[
 \Pr(K_2=0)=\Pr(K_2=2)=\frac{1+q}{4},\quad
 \Pr(K_2=1)=\frac{1-q}{2},
\]
\[
 \Pr(K_3=0)=\Pr(K_3=3)=\frac{1+q^2}{4},\quad
 \Pr(K_3=1)=\Pr(K_3=2)=\frac{1-q^2}{4}.
\]
For example, conditional on first sign positive, the four three-step sign words \(+++,++-,+-+,+--\) make every partial sum positive with respective probabilities \(1,1-v,1/2,v\), where \(v=\Pr(\eta_1>\eta_2+\eta_3)\); the two \(v\) terms have the same sign-transition weight and cancel.

**Step 2: universal difference-pair identities.** Write \(A,B,C,D\) for four iid positive non-atomic magnitudes and set \(u=\Pr(A>B+C+D)\), \(v=\Pr(A>B+C)\). The differences \(U=A-B\) and \(V=C-D\) are iid, continuous and symmetric about zero. Therefore, by four equally likely sign quadrants and equal chance of either larger absolute value on the mixed quadrants,
\[
 \Pr(U>0,U+V>0)=\frac38,\quad
 \Pr(0<U<V)=\Pr(V<U<0)=\frac18.
\]
Writing instead \(W=B-A\) and \(V=C-D\), the same symmetry gives \(\Pr(W>0,V<W)=3/8\). Subtract the event \(W>0,C\le W\) (for which \(V<W\) holds automatically since \(D>0\)). This yields the identity
\[
 \Pr(A<B<A+C<B+D)=\frac38-v.
\]
All event boundaries have probability zero.

**Step 3: eight sign words.** Condition on the first sign being positive; reversal of all signs sends \(K_4\) to \(4-K_4\), so its two-positive-time probability is the same under either initial sign. For the eight sign words in the order
\[
 ++++,\quad +++-,\quad ++-+,\quad ++--,\quad +-++,\quad +-+-,\quad +--+,\quad +---,
\]
the conditional probabilities that \(K_4=2\) are, in that order,
\[
 0,\quad0,\quad u,\quad v,\quad v-u,\quad 3/8-v,\quad1/4,\quad1/2-v.
\]
For \(+-+ -\), the sixth entry is the difference-pair identity above. For \(+--+\), the seventh is the disjoint union \(\{0<U<V\}\cup\{V<U<0\}\), hence probability \(1/4\). The other entries follow by monotonicity during successive same-sign steps and exchangeability of magnitudes. Weighting a sign word by \(q^e(1-q)^{3-e}\), with \(e\) equal to its number of adjacent equal-sign pairs, gives
\[
 \Pr(K_4=2)=\frac12 q^2(1-q)+(v+1/4)q(1-q)^2+(3/8-v)(1-q)^3=b(q,v).
\]
The conditional probabilities that all four partial sums are positive for the same eight words are
\[
 1,\quad1-u,\quad1-v,\quad1/2,\quad1/2,\quad3/8,\quad v,\quad u.
\]
Only a positive initial sign contributes to \(K_4=4\), with probability \(1/2\), and the weighted sum gives
\[
 \Pr(K_4=4)=\frac12\left[q^3+\frac32q^2(1-q)+\frac32q(1-q)^2+\frac38(1-q)^3\right]=a(q).
\]
Reflection and total probability now determine the remaining three probabilities, proving the full law.

**Step 4: exact universality boundary and sharp range.** The coefficient of \(v\) in \(b(q,v)\) is \((1-q)^2(2q-1)\), zero precisely at \(q=1/2\) or \(q=1\) within \([0,1]\). There are absolutely continuous magnitude laws with \(v=0\), e.g. uniform on \((1,3/2)\), and with \(v=1/4\), e.g. exponential of rate one (by \(\mathbb E[e^{-(B+C)}]=(1/2)^2\)). Therefore all other \(q\) genuinely distinguish magnitude laws at \(n=4\). The three disjoint events \(A>B+C\), \(B>A+C\), and \(C>A+B\) imply \(3v\le1\); strictness follows because three iid positive magnitudes have positive probability of lying in a small common interval on which the triangle inequalities all hold. Finally, for \(\eta=\exp(LU)\) with \(U\) uniform on \((0,1)\), \(v=0\) for all sufficiently small \(L>0\), and \(v\to1/3\) as \(L\to\infty\): the largest of three independent exponentials of these uniforms eventually exceeds the sum of the other two with probability tending to one. The probability \(v\) depends continuously on \(L>0\); the intermediate-value theorem therefore realizes every \(v\in[0,1/3)\) by a non-atomic magnitude law. Substitution into the affine function \(b\) yields the sharp intervals and endpoint attainability.

## Verification
Run `python3 verify.py` using Python's standard library. Its 686 exact-rational checks independently aggregate the eight conditional probability entries for multiple persistence probabilities and admissible auxiliary event parameters, verify the polynomial reductions, probability normalization/nonnegativity, both contrasting law values and the universal special points, and verify the two- and three-step formulas. These computations check algebraic consistency; the event classification and the all-law range are established by the preceding proof, not by finite tests.

## Relationship to prior work
Lacroix-A-Chez-Toine and Mori (arXiv:2007.10969, first public July 21, 2020) define this sign-persistent walk, establish universality for survival and maximum-time statistics, and in their Section 6 state that positive-side occupation time is non-universal on numerical evidence; they do not provide this exact four-step law, the sharp first affected horizon, the one-dimensional triangle-probability dependence, or the sharp probability range in the inspected text. Singh and Kundu (arXiv:1906.09442) give a continuous-time run-and-tumble occupation law with a different sampling and speed model, not the finite discrete sign-persistent walk above. Fang and colleagues (DOI:10.1017/jpr.2021.14) study arcsine laws for a different walk derived from random permutations. The present result makes precise a specifically identified gap, without claiming first discovery of the broad nonuniversality phenomenon.

## Limitations
The formulas classify only horizons through four. They assume iid non-atomic positive magnitudes and a fair independent initial sign; distributions with atoms and tied partial sums require convention-dependent corrections. The full infinite-horizon occupation law and the uniqueness of any related families are not resolved. Literature priority remains subject to independent review, especially for potentially unindexed discrete occupation calculations.

## References
1. B. Lacroix-A-Chez-Toine and F. Mori, *Universal survival probability for a correlated random walk and applications to records*, arXiv:2007.10969 (first public July 21, 2020), https://arxiv.org/abs/2007.10969.
2. P. Singh and A. Kundu, *Generalised 'Arcsine' laws for run-and-tumble particle in one dimension*, arXiv:1906.09442, https://arxiv.org/abs/1906.09442.
3. X. Fang, H. L. Gan, S. Holmes, H. Huang, E. Peköz, A. Röllin and W. Tang, *Arcsine laws for random walks generated from random permutations with applications to genomics*, *J. Appl. Probab.* 58 (2021), DOI:10.1017/jpr.2021.14.
