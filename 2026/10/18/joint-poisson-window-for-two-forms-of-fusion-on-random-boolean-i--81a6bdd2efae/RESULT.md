# Joint Poisson window for two forms of fusion on random Boolean information frames

## Finding
Let \(X\) be a finite set with \(|X|=k\geq 0\), and regard \(\mathcal P(X)\) as a join-semilattice with join \(u\vee v=u\cup v\). Give two propositional letters \(a,b\) independent random truth sets: for each world \(u\subseteq X\), the indicators \(\mathbf1_{u\models a}\) and \(\mathbf1_{u\models b}\) are all mutually independent, each Bernoulli with parameter \(p\in[0,1]\). The *fusion* clause is
\[
 x\models\langle\operatorname{sup}\rangle(\varphi,\psi)
 \iff (\exists u,v\subseteq X)\bigl[u\cup v=x,\ u\models\varphi,\ v\models\psi\bigr].
\]
At the top world \(X\), let \(M_k\) count **ordered** witnesses \((u,v)\) for \(\langle\operatorname{sup}\rangle(a,b)\); let \(S_k\) count **unordered distinct** pairs \(\{u,v\}\) with \(u\cup v=X\) and both endpoints satisfying \(a\). Thus \(S_k>0\) witnesses \(\langle\operatorname{sup}\rangle(a,a)\), while the diagonal witness \((X,X)\) is represented separately by the event \(X\models a\).

**Exact finite moment theorem.** Writing \(A=3^k\), \(B=5^k\), and \(C=2^k\), for all \(k\geq0\) and \(p\in[0,1]\):
\[
\begin{aligned}
\mathbb EM_k&=Ap^2,& \mathbb ES_k&=\frac{A-1}{2}p^2,\\
\operatorname{Var}(M_k)&=Ap^2(1-p^2)+2(B-A)p^3(1-p),\\
\operatorname{Var}(S_k)&=\frac{A-1}{2}p^2(1-p^2)
 +(B-A-2C+2)p^3(1-p),\\
\operatorname{Cov}(S_k,M_k)&=(B-C)p^3(1-p).
\end{aligned}
\]
Let \(\Pi_s,\Pi_m\) be independent Poisson random variables with means \((A-1)p^2/2\) and \(Ap^2\), respectively. Their joint law obeys the explicit bound
\[
 d_{\rm TV}\bigl(\mathcal L(S_k,M_k),\mathcal L(\Pi_s,\Pi_m)\bigr)
 \leq 20\,5^k(p^3+p^4).
\]
In particular, for fixed \(t>0\) and \(p_k=t\,3^{-k/2}\) (for sufficiently large \(k\), so \(p_k\leq1\)),
\[
 (S_k,M_k)\xrightarrow{\rm TV}
 \operatorname{Poi}(t^2/2)\otimes\operatorname{Poi}(t^2),
\]
with error bounded by
\[
 20t^3\left(\frac{5}{3\sqrt3}\right)^k
 +20t^4\left(\frac59\right)^k+\frac{t^2}{2\,3^k}.
\]
Thus the two (logically related but not identical) fusion formulas have limiting truth probabilities \(1-e^{-t^2/2}\) and \(1-e^{-t^2}\), and their truth indicators converge jointly to **independent** Bernoulli variables with these success probabilities despite sharing the valuation of \(a\). The additional diagonal of self-fusion changes the first probability by at most \(p_k\), hence does not affect the limit.

**Sharp threshold.** More generally, for any sequence \(p_k\in[0,1]\), if \(3^k p_k^2\to0\), both fusion formulas are false at the top with probability tending to one; if \(3^k p_k^2\to\infty\), both are true there with probability tending to one. The critical scale is therefore \(p_k\asymp3^{-k/2}\). Every assertion also holds at any world \(x\) of a larger Boolean information frame after replacing \(k\) by \(|x|\), because every join witness for \(x\) lies below \(x\).

## Assumptions and scope
The valuations are **arbitrary classical random propositional valuations**, not monotone or persistent valuations. The frame is the full finite Boolean inclusion order, and fusion means *least upper bound* (set union), not arbitrary common upper bound. The repeated letter \(a\) uses the **same** truth set in both argument positions; \(a,b\) use independent truth sets. In \(d_{\rm TV}\), distance means \(\sup_E|\Pr(U\in E)-\Pr(V\in E)|\). The theorem concerns one fixed evaluation world at a time, not the total number of worlds satisfying a modal formula.

## Proof
**1. Incidence geometry of joins.** At the top \(X\), an ordered pair \((u,v)\) has \(u\cup v=X\) precisely when each coordinate has membership pattern \((1,0),(0,1)\), or \((1,1)\). There are exactly \(3^k\) ordered pairs. Swapping has the single fixed point \((X,X)\), so the number of distinct unordered pairs is \((3^k-1)/2\). For a fixed \(u\subseteq X\), the number of ordered partners \(v\) is \(2^{|u|}\), and the number of **distinct** self-fusion partners is \(d_s(u)=2^{|u|}-\mathbf1_{u=X}\). The sums \(\sum_{u\subseteq X}2^{|u|}=3^k\) and \(\sum_{u\subseteq X}4^{|u|}=5^k\) follow by the binomial theorem.

**2. Exact moments.** Every mixed or distinct self witness requires exactly two independent Bernoulli bits, so each indicator has mean \(p^2\) and variance \(p^2(1-p^2)\). Two *different* witness indicators are independent unless they share an underlying bit. A pair sharing exactly one bit has covariance \(p^3-p^4=p^3(1-p)\). Mixed ordered witnesses share either one \(a\)-bit or one \(b\)-bit. The number of **ordered distinct pairs of mixed witnesses** sharing an underlying bit is \(2\sum_u2^{|u|}(2^{|u|}-1)=2(5^k-3^k)\). For distinct self witnesses, the corresponding count is
\[
\sum_{u}d_s(u)(d_s(u)-1)=5^k-3^k-2^{k+1}+2.
\]
A self witness \(\{u,v\}\) and a mixed witness \((w,z)\) share a bit exactly when \(w=u\) or \(w=v\), yielding \(\sum_ud_s(u)2^{|u|}=5^k-2^k\) cross-type pairs. Summing diagonal variances and these covariance contributions gives every displayed finite moment identity.

**3. Joint Poisson bound.** Index the indicators by the disjoint union of the mixed ordered and distinct self witness sets. Each depends on two independent basic bits, either \(a_u,a_v\) with \(u\neq v\), or \(a_u,b_v\). Connect two indices when they share a basic bit, and include each index in its own dependency neighborhood. Outside its neighborhood, an indicator is independent of all the other indicators jointly; hence the local-dependence term \(b_3\) of the Arratia–Goldstein–Gordon theorem vanishes. An \(a\)-bit at \(u\) occurs in at most \(2^{|u|+1}\) witness indicators, while a \(b\)-bit at \(v\) occurs in \(2^{|v|}\). Therefore the sum of the squares of all bit degrees is at most
\[
\sum_u(2^{|u|+1})^2+\sum_v(2^{|v|})^2
 =5\cdot5^k.
\]
Every neighboring *distinct* pair of witness indicators shares exactly one bit; two indicators with identical pairs of basic bits cannot occur because unordered self witnesses are counted once. Thus the standard dependency sums satisfy \(b_1\leq5\cdot5^kp^4\) and \(b_2\leq5\cdot5^kp^3\). Apply the **multivariate** Poisson approximation (Arratia, Goldstein and Gordon, 1989, Theorem 2, partitioning the index set by witness type): the total-variation distance to the product of the two Poisson distributions having the exact means is at most \(4(b_1+b_2)\). This is the stated \(20\cdot5^k(p^3+p^4)\) bound.

**4. Critical law and truth.** Under \(p_k=t3^{-k/2}\), the exact means tend to \((t^2/2,t^2)\). Substitution into the total-variation bound gives the two exponential terms; changing the first Poisson mean by \(t^2/(2\cdot3^k)\) costs no more than that quantity in total variation. The key strict inequality is \(5<3\sqrt3\). Self-fusion is true iff \(S_k>0\) or \(a_X=1\), and the difference between these truth events is at most \(\Pr(a_X=1)=p_k\). Taking coordinatewise positivity of independent Poisson limits proves the two truth probabilities and their asymptotic independence.

**5. Off-critical regimes.** If \(3^kp_k^2\to0\), Markov's inequality gives \(M_k=S_k=0\) with high probability; also \(p_k\to0\) excludes the diagonal self witness. If \(3^kp_k^2\to\infty\), both witness-count expectations diverge. Their exact variance formulas imply, separately for the two counts,
\[
\frac{\operatorname{Var}(W_k)}{(\mathbb EW_k)^2}
 =O\!\left(\frac1{3^kp_k^2}+\frac{(5/9)^k}{p_k}\right)=o(1).
\]
Indeed \(p_k/3^{-k/2}\to\infty\) and \(5/(3\sqrt3)<1\). Chebyshev's inequality then makes both counts positive with high probability, proving the claimed threshold.

## Verification
An independent brute-force implementation in `verify.py` enumerates *every* pair of valuation sets for \(k=0,1,2,3\), for each of the rational probabilities \(p=1/2\) and \(p=1/3\), and compares exact rational first moments, variances and covariance to the five closed formulas. It separately enumerates witness dependency neighborhoods and cross-type overlaps for those four values of \(k\), and checks the distinct-pair/diagonal characterization of self-fusion. The program reports `VERIFY_OK 8 exact enumerations and 4 dependency-graph checks`. Finite checks do not certify an asymptotic Poisson law; that law follows from Steps 3–5 and the cited multivariate approximation theorem.

## Relationship to prior work
Knudstorp's 2022 thesis *Modal Information Logics* (especially the introduction and Chapter 6) establishes the logical framework for the binary supremum modality on join-semilattices and gives axiomatization results, but neither random valuations nor witness-count distribution or the two-form critical comparison. The related 2023 journal paper treats axiomatization and decidability for preorders and posets. Arratia, Goldstein and Gordon's 1989 multivariate Chen–Stein theorem supplies the general Poisson approximation machinery; it does not supply the Boolean-join incidence counts \(3^k,5^k\), exact bivariate moments, the two different critical intensities, or the shared-valuation joint limit without the present application-specific verification. Goldstein and Reinert (2006) consider Poisson approximation for intersection sizes of fixed-cardinality random subsets, a different probability space and different statistic. No claim of originality is made for the general Poisson approximation theorem or the semantics of fusion itself.

## Limitations
The random valuations are independent across all worlds and letters; models with persistent valuations, biased by world-rank, or correlated letters need different calculations. The convergence is for a fixed Boolean evaluation world of growing rank and does not yield simultaneous truth estimates for all worlds. The proof uses a published approximation theorem, not a new general Poisson theorem. Source comparisons cannot exclude an equivalent Boolean-join random-family result under alternate terminology; independent literature certification has not been performed.

## References
1. S. B. Knudstorp, *Modal Information Logics*, Master of Logic thesis, University of Amsterdam, 2022; public repository deposit 2022-10-31. https://eprints.illc.uva.nl/id/eprint/2226/1/MoL-2022-24.text.pdf
2. S. B. Knudstorp, *Modal Information Logics: Axiomatizations and Decidability*, *Journal of Philosophical Logic* **52** (2023), 1723–1766. https://doi.org/10.1007/s10992-023-09724-5
3. R. Arratia, L. Goldstein, L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen–Stein Method*, *Annals of Probability* **17** (1989), 9–25, especially Theorem 2. https://dornsife.usc.edu/larry-goldstein/wp-content/uploads/sites/221/2023/06/AGG-1.pdf
4. L. Goldstein, G. Reinert, *Total variation distance for Poisson subset numbers*, *Annals of Combinatorics* **10** (2006), 333–341. https://doi.org/10.1007/s00026-006-0291-9
