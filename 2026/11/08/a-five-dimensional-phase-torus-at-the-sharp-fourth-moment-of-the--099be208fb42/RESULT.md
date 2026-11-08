# A five-dimensional phase torus at the sharp fourth moment of the thirteen-point fifth-power Fourier graph

## Finding
Let \(F=\mathbb F_{13}\), let \(\psi(z)=\exp(2\pi iz/13)\), and for each \(g:F\to\mathbb C\) with \(|g(t)|=1\) for all \(t\), put
\[
\mathcal E_g(u,v)=\sum_{t\in F}g(t)\psi(ut+vt^5),\qquad
\mathcal M(g)=\frac1{13^2}\sum_{(u,v)\in F^2}|\mathcal E_g(u,v)|^4.
\]
Then the sharp phase-only fourth-moment inequality is
\[
\boxed{\mathcal M(g)\le565.}
\]
Its complete equality family is a five-dimensional torus. Namely, choose independently five unit complex numbers \(z_0,A,B,C,D\). Set \(g(0)=z_0\). On the multiplicative orbit
\(H=\langle4\rangle=\{1,4,3,12,9,10\}\), prescribe the six successive values along \(1,4,4^2,\ldots,4^5\) to be
\[
\boxed{g(4^j)=z_0\,(A,B,B/A,A^{-1},B^{-1},A/B)_j,\quad 0\le j<6.}
\]
On the other orbit \(2H=\{2,8,6,11,5,7\}\), prescribe, in the order \(2\cdot4^j\),
\[
\boxed{g(2\cdot4^j)=z_0\,(C,D,D/C,C^{-1},D^{-1},C/D)_j,\quad0\le j<6.}
\]
Every maximizer arises uniquely in this way. Modulo an overall scalar phase, the maximizer set is exactly a four-torus, rather than merely the finite family of additive-character phases.

More strongly, the following **exact deficit identity** holds for every unimodular \(g\). Write \(P_t=g(t)g(-t)\), for \(t\in\{1,\ldots,6\}\). Then
\[
\boxed{\begin{aligned}
565-\mathcal M(g)={}&2\sum_{t=1}^{6}|g(0)^2-P_t|^2
+4\sum_{1\le a<b\le6}|P_a-P_b|^2\\
&+4\sum_{s=1}^{12}|g(0)g(s)-g(4s)g(10s)|^2.
\end{aligned}}
\]
The identity gives both the sharp constant and all equality constraints without a numerical optimization.

## Assumptions and scope
All field operations in the displayed algebraic arguments use \(F=\mathbb F_{13}\). The amplitudes are fixed at one, not merely bounded by one or normalized in \(\ell^2\). The synthesis operator is an **unnormalized** character sum; the fourth moment uses normalized probability measure on the ambient group \(F^2\). With the alternative convention \(\frac1{13}\mathcal E_g\) and counting measure on \(F^2\), the sharp fourth moment is \(565/13^2\). Neither the unrestricted \(\ell^2\to L^4\) operator norm nor a statement for every field is asserted.

## Proof
**Step 1: exact orthogonality expansion.** For each \(w=(s,z)\in F^2\), let \(\mathcal P_w\) be the set of *unordered* pairs \(\{a,b\}\) (with repetitions allowed) satisfying
\(a+b=s\) and \(a^5+b^5=z\). Give such a pair weight \(w_{a,b}=1\) if \(a=b\), and \(w_{a,b}=2\) otherwise. By character orthogonality,
\[
\mathcal M(g)=\sum_{(s,z)\in F^2}\left|\sum_{\{a,b\}\in\mathcal P_{(s,z)}}w_{a,b}\,g(a)g(b)\right|^2.
\]
Since every pair product has modulus one, its squared fiber sum is bounded by the square of the total weight. The aggregate upper bound is the ordered additive energy \(\sum_{s,z}(\sum_{\mathcal P_{(s,z)}}w_{a,b})^2\). Equality holds precisely when all pair products in each non-singleton fiber agree in phase.

**Step 2: classify all collisions exactly.** For \(s=0\), oddness of the fifth power forces \(a^5+(-a)^5=0\); thus the only nonempty fiber is \(\mathcal P_{(0,0)}\), containing \(\{0,0\}\) with weight one and the six pairs \(\{t,-t\}\), \(1\le t\le6\), each of weight two.

Fix \(s\ne0\) and write \(x=ab/s^2\). The Newton identity
\[
a^5+b^5=s^5-5s^3ab+5s(ab)^2=s^5(1-5x+5x^2)
\]
shows that distinct pair products \(x\ne y\) yield the same fifth-power sum if and only if \(x+y=1\). For a pair to be realizable over \(F\), its quadratic equation has discriminant \(s^2(1-4x)\), and for its partner \(1-x\) the discriminant is \(s^2(4x-3)\). The quadratic-residue set, including zero, is exactly
\[
\mathcal Q=\{0,1,3,4,9,10,12\}\subset F.
\]
Inspection of the **full thirteen possible values** \(x\in F\) shows
\[
\{x\in F:1-4x\in\mathcal Q,\ 4x-3\in\mathcal Q\}=\{0,1,7\}.
\]
The value \(x=7=1/2\) gives no distinct partner. The remaining values \(0\) and \(1\) correspond respectively to the pairs \(\{0,s\}\) and \(\{4s,10s\}\), because \(4+10=1\) and \(4\cdot10=1\) in \(F\). Their fifth-power sums agree. Thus the only nontrivial fiber for each \(s\ne0\) comprises precisely these two distinct-entry pairs, both of weight two. All other fibers contain a single unordered pair.

**Step 3: exact constant and deficit.** If there were no collisions between distinct unordered pairs, the energy would equal
\(13+4\binom{13}{2}=325\). Merging the seven pairs of the zero fiber changes its contribution from \(1+6\cdot4=25\) to \(13^2=169\), increasing energy by \(144\). The twelve nonzero fibers each merge two weight-two pairs, increasing energy by \((2+2)^2-(2^2+2^2)=8\), altogether \(96\). Hence \(\mathcal M(g)\le325+144+96=565\), attained by constant \(g\).

For any unit complex numbers \(z_1,\ldots,z_k\) and positive real weights \(w_j\),
\[
\left(\sum_jw_j\right)^2-\left|\sum_jw_jz_j\right|^2
=\sum_{i<j}w_iw_j|z_i-z_j|^2.
\]
Apply this identity to the lone zero-sum fiber (one weight-one pair, six weight-two pairs) and to each of the twelve two-pair fibers (both weights two). Singleton fibers give zero deficit. This proves the boxed three-term identity exactly.

**Step 4: solve every equality constraint.** The nonnegative deficit terms vanish precisely when
\[
\boxed{g(t)g(-t)=g(0)^2\ (t\ne0),\qquad
       g(4s)g(10s)=g(0)g(s)\ (s\ne0).}
\]
Normalize \(h(t)=g(t)/g(0)\); then \(h(0)=1\) and the second equation is
\(h(4s)h(4^{-1}s)=h(s)\), since \(10=4^{-1}\) in \(F\). Because \(4\) has exact multiplicative order six, \(F^\times\) consists of two orbits \(H\) and \(2H\). On either orbit, putting \(h_j=h(c4^j)\), the recurrence is \(h_{j+1}=h_j/h_{j-1}\). With arbitrary \(h_0=A\) and \(h_1=B\), its unique solution is the six-cycle
\((A,B,B/A,A^{-1},B^{-1},A/B)\). It automatically satisfies \(h_{j+3}=h_j^{-1}\); as \(4^3=-1\), this gives \(h(-t)=h(t)^{-1}\), hence all the first family of equalities. The two orbits are independent. Thus exactly the five freely chosen unit complex parameters in the statement determine all and only maximizers; no other equality solutions exist.

## Verification
Run \(`python verify_phase13.py`\) with Python 3 and its standard library. It exhaustively constructs every unordered two-sum fiber on the thirteen-point graph and confirms that the only merged fibers are those proved above; its integer arithmetic verifies the energy \(565\), all field quadratic residues, and the complete discriminant filter \(\{0,1,7\}\). It separately checks seventeen different five-phase parameter choices, both families of equality identities, a nonextremal phase vector and the exact deficit identity, and one direct \(13\times13\) complex Fourier sum. The exact finite enumeration is a reproducible check; the foregoing finite-field algebra and recurrence prove the characterization.

## Relationship to prior work
Mockenhaupt and Tao establish finite-field Fourier restriction and even-moment representation-counting methods, notably their Lemma 5.1; these methods explain the moment expansion but do not classify unimodular equality phases on this graph. A published complete two-sum spectrum of the **same fifth-power graph** determines all representation multiplicities and the additive energy in every finite field of odd order. That more general **counting** result includes the numerical value \(565\) at \(F=\mathbb F_{13}\), which is therefore explicitly *not* claimed as new. However, its published theorem and proof do not determine **which indexed pairs must have equal phase products**, the complete five-torus of unimodular maximizers, or the exact nonnegative phase-deficit identity. A multiplicity histogram cannot by itself identify those product constraints: the incidence of the colliding pairs is needed. This finding supplies that missing sharp-equality description in the natural thirteen-point instance.

## Limitations
The theorem applies only to unimodular input phases, only to \(F=\mathbb F_{13}\), and only to the fourth Fourier moment of the graph \(t\mapsto(t,t^5)\). The computed energy and the general orthogonality method are prior knowledge. No unrestricted \(\ell^2\to L^4\) sharp constant, robust inverse theorem for almost-maximizers, or all-field phase classification is claimed. Despite targeted source comparisons, an unindexed or differently phrased older result could contain the same equality classification; no independent audit has been performed.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first publicly submitted 18 April 2002; especially §5, Lemma 5.1. https://arxiv.org/abs/math/0204234
2. *Complete two-sum spectrum of the finite-field fifth-power graph* (2026), published full result and proof: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-two-sum-spectrum-of-the-finite-field-fifth-power-graph--f9410cde2e91
