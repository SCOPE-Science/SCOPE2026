# Exact observational-quotient census and sharp saturation law for finite S5 Heyting-valued models

## Finding

**Theorem.** Let \(L\) be a finite Heyting algebra with \(q\geq 2\) elements, and fix \(k\geq 1\) propositional variables. Put \(C=L^k\) and \(m=|C|=q^k\). On the labelled carrier \([n]\), choose a single-agent \(\mathsf{S5}\) equivalence relation \(R\) and an arbitrary atomic profile \(c:[n]\to C\). Interpret all Heyting connectives, all exact truth-value tests \(T_\ell\), and \(\Box\) as the meet over accessible worlds. Let \(Q\) be the number of equivalence classes of worlds under equality of *every* formula's exact \(L\)-value.

The complete distribution of \(Q\) over these labelled models has the bivariate exponential generating function
\[
\boxed{\mathcal F_m(z,u)=\sum_{n\geq0}\frac{z^n}{n!}\sum_{(R,c)\text{ on }[n]}u^{Q(R,c)}=\prod_{s=1}^{m}\left[1+u^s\left(\exp\big((e^z-1)^s\big)-1\right)\right]^{\binom ms}.}
\]
The empty-carrier term is a counting convention; the logical models under consideration are nonempty. In particular, \(\mathcal F_m(z,1)=\exp(e^{mz}-1)\), so the total number of models is \(m^n B_n\), where \(B_n\) is the Bell number. The exact maximal quotient size is \(M_m=m2^{m-1}\).

A nonempty family \(\mathcal A\subseteq 2^C\setminus\{\varnothing\}\) specifies one quotient isomorphism type by taking, for each \(S\in\mathcal A\), the \(|S|\) states \((S,c)\) for \(c\in S\), with all states of that \(S\) mutually accessible. This quotient type occurs on a labelled carrier of size \(n\) **if and only if** \(\sum_{S\in\mathcal A}|S|\leq n\). Hence the number of quotient isomorphism types occurring on \([n]\) is
\[
\boxed{U_{m,n}=\sum_{j=1}^{n}[t^j]\prod_{s=1}^{m}(1+t^s)^{\binom ms}.}
\]
For \(n\geq m2^{m-1}\), this stabilizes at \(2^{2^m-1}-1\).

Finally, fix \(m\geq2\), choose \((R,c)\) uniformly among the \(m^nB_n\) labelled models, and let \(w_n>0\) solve \(w_ne^{w_n}=n\) (the principal Lambert \(W\)-function). Then, as \(n\to\infty\),
\[
\boxed{\Pr\{Q<M_m\}\sim m\exp\!\left(-\frac{\mathbf1_{\{m=2\}}}{8}\right)\exp\!\left(1-\left(\frac{n}{w_n}\right)^{1/m}\right).}
\]
The factor \(e^{-1/8}\) at \(m=2\) is a necessary saddle-displacement correction; it is not present for \(m\geq3\). Thus almost every such model realizes the universal maximum quotient size, but the failure probability has an explicit stretched-exponential asymptotic.

## Assumptions and scope

An exact test \(T_\ell\varphi\) has value \(1_L\) exactly where \(\varphi\) has value \(\ell\), and \(0_L\) elsewhere. The modal operator \(\Box\) takes \(\bigwedge_{y\,R\,x}\llbracket\varphi\rrbracket(y)\). There is only **one** agent, \(R\) is **reflexive, symmetric and transitive**, and valuations of the \(k\) variables are independent unrestricted functions into \(L\). Frame multiplicities matter to the labelled census, although not to the quotient. Neither arbitrary Kripke frames nor multi-agent structures are claimed to satisfy these formulas.

For every \(R\)-class \(B\), write \(S_B=\{c_x:x\in B\}\), a nonempty subset of \(C\). The set of distinct supports \(\mathcal A=\{S_B:B\text{ an }R\text{-class}\}\) ignores repeated identical supports. All \(n\) worlds are counted as labelled, and two different equivalence relations or valuations are different models even when their quotients agree.

## Proof

**1. Exact semantic separation.** We first show
\[
x\equiv y\quad\Longleftrightarrow\quad (c_x,S_{[x]_R})=(c_y,S_{[y]_R}).\]
If the right-hand side agrees, induction over formulas shows equality of all exact values. Atoms agree by hypothesis; the Heyting operations and tests preserve agreement pointwise. For the modal step, every state of an \(R\)-class with support \(S\) has successor evaluations indexed by exactly the atomic profiles in \(S\); multiplicities do not affect their meet. The induction therefore depends only on \((S,c_x)\).

Conversely the atomic variables distinguish different profiles. For each \(d=(d_1,\dots,d_k)\in C\), the Boolean-valued formula \(\chi_d=\bigwedge_{i=1}^k T_{d_i}(p_i)\) is true precisely at worlds of profile \(d\). The derived Boolean possibility test \(\Diamond_1\chi_d=T_0\bigl(\Box T_0(T_1\chi_d)\bigr)\) has value \(1_L\) precisely when a successor of profile \(d\) exists. These tests recover each support \(S\). Consequently the quotient has exactly the states \((S,d)\) for every realized support \(S\) and \(d\in S\), and its accessibility classes are indexed by distinct \(S\).

**2. The bivariate labelled census.** Fix a particular support \(S\subseteq C\) with cardinality \(s\). One nonempty equivalence block whose colour map has image exactly \(S\) is a nonempty labelled set with an onto \(S\)-colouring. By inclusion-exclusion its exponential generating function is \((e^z-1)^s\): each of the \(s\) colours receives a nonempty labelled set. An arbitrary *set* of such disjoint blocks therefore has EGF \(\exp((e^z-1)^s)\). If no block has support \(S\), its contribution is \(1\); otherwise its contribution is marked by \(u^s\), regardless of the number of repeated support-\(S\) blocks. Thus the local factor is \(1+u^s(\exp((e^z-1)^s)-1)\). Multiplying over all \(\binom ms\) distinct supports of size \(s\) proves the EGF. At \(u=1\), the identity \(\sum_{s=1}^{m}\binom ms(e^z-1)^s=e^{mz}-1\) yields the Bell-number total.

**3. Possible quotient types.** Every realized support \(S\) requires at least one world of each colour \(d\in S\), so \(\sum_{S\in\mathcal A}|S|\leq n\) is necessary. Conversely, take one labelled class with exactly those \(|S|\) profiles for each \(S\in\mathcal A\), then duplicate an arbitrary world until there are \(n\) worlds. The quotient is unchanged. The product \(\prod_s(1+t^s)^{\binom ms}\) counts all families by their total support size; its empty-family term is excluded. Every possible support occurs when \(n\geq\sum_{\varnothing\ne S\subseteq C}|S|=m2^{m-1}\), yielding the maximum quotient and the stabilized type count.

**4. Sharp asymptotic saturation.** Fix a colour \(a\in C\). Let \(E_a\) mean that no equivalence block has exact support \(\{a\}\). For all models the EGF is \(F(z)=\exp(e^{mz}-1)\). Excluding blocks with singleton support \(\{a\}\), whose EGF is \(g(z)=e^z-1\), gives \(F_a(z)=\exp(e^{mz}-1-g(z))\). Put \(r=w_n/m\). The positive saddle for \([z^n]F\) satisfies \(n=mr e^{mr}\), and its quadratic log-saddle curvature is \(K''(r)=n(1+mr)/r^2\), where \(K(z)=e^{mz}-1-n\log z\). The saddle for \(F_a\) shifts by
\[\delta=\frac{r^2e^r}{n(1+mr)}(1+o(1)).\]
A second-order expansion at the shifted saddle and standard small-arc Gaussian estimates for the two entire positive-coefficient EGFs give
\[\log\frac{[z^n]F_a}{[z^n]F}=-g(r)-\frac{r^2e^{2r}}{2n(1+mr)}+o(1).\]
For clarity on error control: \(r\to\infty\), \(\delta\to0\), the cubic Taylor remainder and the change in the Gaussian prefactor are \(o(1)\); outside a shrinking Gaussian arc the characteristic function of the associated labelled-set exponential construction decays, and the term \(e^{mz}\) dominates the lower-growth subtraction \(e^z\). In particular, the positive block weights of \(F_a\) are \(m^j-1\) in degree \(j\ge1\), ensuring the same aperiodic saddle regime. Since \(e^r=(n/w_n)^{1/m}\), the correction \(r^2e^{2r}/(2n(1+mr))\) tends to \(1/8\) for \(m=2\) and to \(0\) for \(m\ge3\). Hence
\[\Pr(E_a)\sim e^{-\mathbf1_{\{m=2\}}/8}\exp\!\left(1-(n/w_n)^{1/m}\right).\]

For any prescribed support \(S\) of size \(s\ge2\), excluding all blocks of that support yields \(F_S(z)=F(z)\exp(-(e^z-1)^s)\), an EGF with nonnegative coefficients. Cauchy's coefficient bound at \(r\), divided by the standard saddle estimate for \([z^n]F\), gives
\[\Pr(E_S)\leq(1+o(1))\sqrt{2\pi n(1+w_n)}\exp(-(e^r-1)^s)=o(\Pr(E_a)).\]
Likewise, excluding two distinct singleton supports bounds their joint absence by the same polynomial prefactor times \(\exp(-2(e^r-1))\), also \(o(\Pr(E_a))\). There are only finitely many supports for fixed \(m\). Thus inclusion-exclusion gives \(\Pr\{Q<M_m\}\sim\sum_{a\in C}\Pr(E_a)=m\Pr(E_a)\), as stated.

## Verification

The standalone Python 3 script `checker.py` directly enumerates all set partitions and all \(m\)-colour assignments for \(m=2\) through \(n=5\), and \(m=3\) through \(n=5\), and compares the resulting quotient-size histograms against the species convolution. It also checks the Bell totals. For the first two finite Heyting chains it independently closes the set of formula evaluations under meets, joins, implication, all exact tests and the box operation, verifying the claimed semantic equivalence for \(q=2,n\le4\) and \(q=3,n\le3\). A separate integer recurrence tests the exceptional missing-singleton coefficient calculation through \(n=350\). All checks completed with `ALL_CHECKS_OK`.

For example, the exact quotient-size distribution at \((m,n)=(2,4)\) is \(Q=1:30, Q=2:90, Q=3:96, Q=4:24\), total \(240=2^4B_4\). The finite computations corroborate the formulas but do **not** replace the all-size combinatorial proof or the saddle-point estimates.

## Relationship to prior work

Das, Ray and Mali (2026), Sections 2 and 4, give the exact-truth-value semantics and a general finite observational quotient; their theorem is credited and is not presented here as new. Das (2026), Section 2.1, gives the exact tests and the derived existential modality used in the separation argument. Ciardelli and Otto (2023 preprint, Section 3.3.1) explicitly note that, for one-agent epistemic components, propositional support types determine bisimulation type and multiplicities do not matter. Thus the support lemma is a known or immediately related semantic principle. The present result specializes these semantics to S5 and supplies the *exact size-marked labelled distribution*, *all finite quotient types*, and especially the *sharp rarity asymptotic with its exceptional correction*. These statements are not asserted in the inspected passages of the cited works. The exponential formula and saddle analysis rely on standard analytic-combinatorics methods rather than claiming those methods as innovations.

## Limitations

The formula-equivalence quotient uses all exact-value formulas over a fixed finite vocabulary. The census weights every equivalence relation and every valuation on the labelled carrier equally; it is not a distribution for a uniformly chosen *quotient type* or uniformly chosen frame followed by a nonuniform valuation. The asymptotic holds for fixed \(m\) as \(n\to\infty\), not for \(m\) growing with \(n\). Exact tests are essential to the converse separation; without them, weaker languages may induce coarser quotients. The proof does not address multiple agents or arbitrary directed accessibility, and it does not establish historical uniqueness of the enumerative identities.

## References

1. Litan Kumar Das, Kumar Sankar Ray and Prakash Chandra Mali, *A Bitopological Approach to Finite Reduction and Bounded Exact-Value Certificates for Fitting's Finite Heyting-valued Modal Logic*, arXiv:2608.05550 (first posted 2026-08-06), Sections 2.1 and 4. https://arxiv.org/abs/2608.05550
2. Litan Kumar Das, *Lindström Maximality for Fitting's Finite Heyting-Valued Modal Logic with Exact Truth Tests*, arXiv:2608.08755 (first posted 2026-08-09), Section 2.1. https://arxiv.org/abs/2608.08755
3. Ivano Ciardelli and Martin Otto, *On the Expressive Power of Inquisitive Epistemic Logic*, arXiv:2312.14573 (first posted 2023-12-22), Section 3.3.1. https://arxiv.org/abs/2312.14573
4. Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, chapters II and VIII (exponential formula and saddle-point methods).
