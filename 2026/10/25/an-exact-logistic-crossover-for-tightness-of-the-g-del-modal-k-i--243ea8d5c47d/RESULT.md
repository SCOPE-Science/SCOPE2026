# An exact logistic crossover for tightness of the Gödel modal K inequality

## Finding

Fix integers \(n\ge1\) and \(k\ge2\). On a complete crisp Kripke frame with \(n\) worlds, assign independently and uniformly to each of two atoms \(p,r\) at every world a truth value from the \(k\)-element Gödel chain. Let \(E_{n,k}\) mean that the two sides of the valid modal K inequality have **equal truth value**:
\[
\Box(p\to r)= (\Box p\to\Box r).
\]
Then the exact tightness probability is
\[
\boxed{\mathbb P(E_{n,k})=
\frac12\left[1-\sum_{j=1}^{k}\left(\left(\frac jk\right)^n-\left(\frac{j-1}{k}\right)^n\right)^2\right]
+\left(\frac{k+1}{2k}\right)^n.}
\]
For every integer sequence \(k=k(n)\ge2\), if \(n/k(n)\to\lambda\in[0,\infty]\), then
\[
\boxed{\lim_{n\to\infty}\mathbb P(E_{n,k(n)})=
\begin{cases}\frac1{1+e^\lambda},&0\le\lambda<\infty,\\0,&\lambda=\infty.\end{cases}}
\]
Here the value at \(\lambda=0\) is \(1/2\). In particular, the orders of the large-world and fine-truth-scale limits do not commute:
\[
\lim_{n\to\infty}\lim_{k\to\infty}\mathbb P(E_{n,k})=\frac12,
\qquad
\lim_{k\to\infty}\lim_{n\to\infty}\mathbb P(E_{n,k})=0.
\]
The exact fixed-chain exponential regimes are
\[
\mathbb P(E_{n,k})\sim
\begin{cases}
(3/4)^n,&k=2,\\
2(2/3)^n,&k=3,\\
((k-1)/k)^n,&k\ge4.
\end{cases}
\]

There is also an exact distribution-free-in-form extension. If both atoms have the same arbitrary probability mass function \(w_0,\ldots,w_{k-1}\) on the chain, still independently over atoms and worlds, define \(T_i=\sum_{j=i}^{k-1}w_j\) for \(0\le i\le k\), with \(T_k=0\). Then
\[
\boxed{\mathbb P(E_{n,w})=
\frac12\left[1-\sum_{i=0}^{k-1}(T_i^n-T_{i+1}^n)^2\right]
+\left(\frac{1+\sum_{i=0}^{k-1}w_i^2}{2}\right)^n.}
\]
This formula includes degenerate distributions and the one-level chain. The logistic crossover is asserted only for the uniform-chain regime above.

## Assumptions and scope

The complete crisp frame is \(W=\{1,\ldots,n\}\) with all arrows present. It is one equivalence class of an S5 frame, though the assertion concerns only this one class. The truth chain is \(L_k=\{0,1/(k-1),\ldots,1\}\). Gödel implication is
\[
a\Rightarrow b=\begin{cases}1,&a\le b,\\b,&a>b.\end{cases}
\]
Necessity evaluates as the minimum over the accessible worlds. We sample valuations of **two different atomic formulas**, independent and identically distributed at each world; this is a probability over valuations, not a random-frame-validity probability. Equality is numerical equality of truth values, not only equality of designated truth statuses. The result is independent of the chosen pointing world because accessibility is complete.

## Proof

Write \(a_i=e(i,p)\), \(b_i=e(i,r)\) and put \(A=\min_i a_i\), \(B=\min_i b_i\), \(L=\min_i(a_i\Rightarrow b_i)\). The two terms compared are \(L\) and \(A\Rightarrow B\).

**Order criterion.** If \(A>B\), select an index \(j\) with \(b_j=B\). Since \(a_j\ge A>B\), its implication value equals \(B\). Every other implication value is either \(1\) or some \(b_i\ge B\). Thus \(L=B=A\Rightarrow B\). If \(A\le B\), then \(A\Rightarrow B=1\), whereas \(L=1\) precisely when \(a_i\le b_i\) for every \(i\). Consequently
\[
E_{n,k}\quad\Longleftrightarrow\quad
(A>B)\ \text{or}\ (a_i\le b_i\ \text{for all }i).
\]
The two events are disjoint: if each \(a_i\le b_i\), taking an index at which \(b_i=B\) gives \(A\le B\). This also proves the general inequality \(L\le A\Rightarrow B\).

**Exact probability for arbitrary chain masses.** The minima \(A\) and \(B\) are independent and identically distributed. Hence
\[
\mathbb P(A>B)=\frac12(1-\mathbb P(A=B)).
\]
For each chain level \(i\), the minimum has probability \(d_i=T_i^n-T_{i+1}^n\), so \(\mathbb P(A=B)=\sum_i d_i^2\). For one pair of independent atom values, symmetry gives
\[
\mathbb P(a_i\le b_i)=\frac12\left(1+\sum_j w_j^2\right).
\]
The pairs at distinct worlds are independent, so the probability of coordinatewise ordering is the \(n\)-th power of this quantity. Adding the disjoint contributions yields the arbitrary-mass formula. For uniform weights, \(T_i=(k-i)/k\), \(\sum_jw_j^2=1/k\), and reindexing by \(j=k-i\) yields the displayed exact uniform formula.

**Growing-chain limit.** Let \(M_{n,k}\) be the integer index of the minimum of \(n\) independent uniform values on \(\{0,\ldots,k-1\}\). Then
\[
\mathbb P(M_{n,k}\ge t)=(1-t/k)^n\quad(0\le t\le k).
\]
If \(n/k\to\lambda\in(0,\infty)\), the minimum index converges to a geometric variable on the nonnegative integers with probability masses \((1-e^{-\lambda})e^{-\lambda t}\). The tails are tight because they are at most \(e^{-tn/k}\). Thus the tie probability of two independent minima converges to
\[
\sum_{t\ge0}(1-e^{-\lambda})^2e^{-2\lambda t}
=\frac{1-e^{-\lambda}}{1+e^{-\lambda}}.
\]
The coordinatewise-ordering probability is bounded by \((3/4)^n\) for every \(k\ge2\), and therefore vanishes. Half of one minus the tie limit is \(1/(1+e^\lambda)\).

If \(n/k\to0\), the largest probability mass of the minimum is at most \(n/k\), by the union bound applied to each candidate minimum value. Therefore the tie probability tends to zero and the equality probability tends to \(1/2\). If \(n/k\to\infty\), both independent minima equal the lowest level with probability tending to one; the tie probability tends to one and the equality probability tends to zero. These prove the endpoint cases as well.

**Fixed-chain regimes and noncommuting limits.** For fixed \(k\ge2\), the leading contribution to \(\mathbb P(A>B)\) is \(((k-1)/k)^n\), from \(A\ge1\) and \(B=0\); the remaining contribution has exponential base at most \((k-2)/k\). The coordinatewise ordering term has base \((k+1)/(2k)\). The latter base is larger when \(k=2\), equal when \(k=3\), and smaller when \(k\ge4\), proving the three stated asymptotics. For fixed \(n\), each minimum atom has probability at most \(n/k\), so \(\mathbb P(A=B)\to0\), while the ordering term tends to \(2^{-n}\). Thus \(\lim_{k\to\infty}\mathbb P(E_{n,k})=1/2+2^{-n}\), giving both iterated limits.

## Verification

The standalone `checker.py` uses exact rational arithmetic and no external packages. Run `python3 checker.py`. It evaluates the actual Gödel implication and both modal sides for every pair of valuations in 20 uniform finite configurations and 9 additional nonuniform configurations: 486,250 valuation pairs altogether. It verifies the order criterion, pointwise K inequality, disjoint-event decomposition, and exact probability formula, and checks several rational benchmarks and numerical crossover cases. The expected output ends in `ALL_CHECKS_OK`.

For example, exact probabilities are \(\mathbb P(E_{2,2})=3/4\), \(\mathbb P(E_{2,3})=59/81\), \(\mathbb P(E_{3,3})=125/243\), and \(\mathbb P(E_{2,4})=93/128\). These finite checks are not a substitute for the proof of the universal formula or limits.

## Relationship to prior work

The chain residuum, fuzzy Kripke semantics and modal operators are standard in Gödel modal logic; see Caicedo and Rodríguez and the accessible 2025–2026 treatments listed below. Bílková, Ferguson and Kozhemiachenko study Gödel epistemic S5-like modalities with involutive negation, construct tableaux and analyze complexity. Vidal and Rodríguez axiomatize logics of finite Gödel–Kripke models and analyze witnessedness. Ferrari, Fiorentini, Giardini and Rodríguez give a calculus and finite-model result for witnessed Gödel modal models. None of the inspected statements in these papers is an exact measure over independently random valuations of the **tightness** of \(\Box(p\to r)\le(\Box p\to\Box r)\), nor a growing-alphabet logistic law.

The publicly available research note *Ordinal regrading classes of finite Gödel Kripke frames* characterizes order-preserving changes to fuzzy accessibility matrices that preserve frame validity. That statement transports all valuations and all formulas on regraded frames. It does not imply the present probability: this work fixes a complete crisp frame, specifies a sampling distribution on atomic valuations, and calculates the mass of an equality event. Generic discrete-minimum tie formulas are standard probabilistic tools; their use here is not claimed as a new order-statistics lemma.

## Limitations

The formula is exact under independence and a common atom-value distribution; correlated atoms, heterogeneous distributions by world, or non-complete frames are not covered. The logistic limit assumes uniform truth-level sampling. This theorem concerns the equality event for a particular pair of modal terms, not a classification of all Gödel modal formulas, all validities, or all random fuzzy frames. The elementary order criterion alone is not claimed as a separate original theorem. The scientific contribution is the combined exact tightness distribution and its complete changing-alphabet phase diagram. Prior work using alternate probabilistic terminology may still contain equivalent formulas; an independent priority review has not been performed.

## References

1. Marta Bílková, Thomas Ferguson, Daniil Kozhemiachenko, *Tableaux for epistemic Gödel logic*, arXiv:2510.04642, first submitted 2025-10-06, especially the semantics and introductory discussion (pp. 2–4).
2. Amanda Vidal and Ricardo O. Rodríguez, *Axiomatizing logics of finite Gödel-Kripke models*, arXiv:2605.15810, first submitted 2026-05-15, especially introduction and preliminaries.
3. Mauro Ferrari, Camillo Fiorentini, Paolo Giardini, Ricardo Oscar Rodriguez, *A Gödel Modal Logic Over Witnessed Models*, arXiv:2606.31906, first submitted 2026-06-30, especially Section 2.
4. Xavier Caicedo and Ricardo O. Rodríguez, *Standard Gödel Modal Logics*, Studia Logica 94 (2010), 189–214, DOI:10.1007/s11225-010-9230-1. Earlier foundational semantics, not the focal recent source.
5. *Ordinal regrading classes of finite Gödel Kripke frames* (2026), publicly available mathematical research note, for the distinct frame-regrading comparison.
