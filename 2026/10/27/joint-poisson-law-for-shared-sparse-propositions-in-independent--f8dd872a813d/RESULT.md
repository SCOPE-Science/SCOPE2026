# Joint Poisson law for shared sparse propositions in independent finite S5 frames

## Finding
Let \(r\ge 2\) be fixed. On \([n]\), choose independently and uniformly \(r\) equivalence relations \(E_1,\ldots,E_r\). Independently choose one **shared** unary predicate \(P\subseteq[n]\). Write \(B_n\) for the \(n\)-th Bell number, \(B_0=1\), and \(b_n=B_{n-1}/B_n\). For \(1\le a\le r\) and \(j\ge1\), let \(Y_{a,j}\) count the \(E_a\)-classes of size \(j\) that lie wholly inside \(P\).

**Theorem.** Suppose either (i) \(P\) is uniform among subsets of deterministic size \(m_n\), where \(m_n b_n\to c\in(0,\infty)\), or (ii) vertices are marked independently with probability \(p_n\), where \(n p_n b_n\to c\in(0,\infty)\). Then the full count array \((Y_{a,j})_{1\le a\le r,\,j\ge1}\), regarded as an element of the countable discrete space of finitely supported arrays, converges **in total variation** to mutually independent Poisson variables \((Z_{a,j})\) with \(\mathbb E Z_{a,j}=c^j/j!\). In case (i), the \(r\) agent-wise count processes are in fact independent for **every finite** \(n\), not merely asymptotically.

Thus the first-order witness sentences
\[
\varphi_a:=\exists x\,\bigl(P(x)\wedge\forall y\,[E_a(x,y)\Rightarrow P(y)]\bigr)
\]
are asymptotically independent, with
\[
\lim_{n\to\infty}\Pr\bigl(\bigwedge_{a=1}^r\varphi_a\bigr)
=\bigl(1-\exp(1-e^c)\bigr)^r.
\]
Moreover, if \(n p_n b_n\to0\), the probability of any \(\varphi_a\) tends to zero, while if \(n p_n b_n\to\infty\), the probability of every \(\varphi_a\) tends to one (the analogous statements hold for fixed-size marking with \(m_n b_n\)). Since \(n b_n\sim W(n)\), the critical independent-vertex marking scale is \(p_n\asymp1/W(n)\), where \(W\) is the positive Lambert function.

## Assumptions and scope
Equivalence relations are selected uniformly from the \(B_n\) partitions of the labeled domain; distinct relations are mutually independent. In both marking models the *same* predicate \(P\) is used for every relation. A fully marked class is a class whose every vertex belongs to \(P\), not merely a nonempty induced class in the restriction to \(P\). The number of relations \(r\) is fixed as \(n\to\infty\). All cardinalities and indices are positive integers, and for the total-variation statement the limiting sequence of counts is almost surely finitely supported because \(\sum_{j\ge1}c^j/j!=e^c-1<\infty\). 

The source motivating the logical perspective is Koponen's October 2026 work on finite base structures and random first-order expansions. The result here concerns a different, explicit sparse-parameter random expansion and is not asserted as a consequence of that paper.

## Proof
**1. An exact factorial-moment identity.** Fix a marked set \(M\) of size \(m\) and one independently uniform partition \(E\). For a finite sequence of nonnegative integers \((k_j)_{1\le j\le J}\), set \(s=\sum_{j=1}^J j k_j\), and write \((t)_s=t(t-1)\cdots(t-s+1)\) with \((t)_0=1\). Then
\[
\mathbb E\Bigl[\prod_{j=1}^J (Y_j)_{k_j}\,\Bigm|\,P=M\Bigr]
=\frac{(m)_s B_{n-s}}{B_n}\prod_{j=1}^J\frac{1}{(j!)^{k_j}}
\qquad(0\le s\le n),
\]
and the left-hand side is zero when \(s>m\). To prove the identity, count ordered selections of \(k_j\) distinct \(j\)-element blocks inside \(M\). Their disjoint vertex sets have \((m)_s\prod_j(j!)^{-k_j}\) possibilities, and each prescribed family extends to exactly \(B_{n-s}\) partitions of the remaining elements. This counts the factorial moment with no independence assumption among blocks.

**2. A Bell-number uniform bound.** Define \(a_n=B_n/n!\) and \(\lambda_n=a_{n-1}/a_n=nB_{n-1}/B_n=nb_n\). Log-concavity of \(a_n\), as proved by Asai, Kubo and Kuo, implies \(\lambda_n\) is nondecreasing. Consequently,
\[
\frac{(n)_s B_{n-s}}{B_n}
=\frac{a_{n-s}}{a_n}=\prod_{t=0}^{s-1}\lambda_{n-t}\le\lambda_n^s.
\]
As \((m)_s/(n)_s\le(m/n)^s\) for \(m\le n\), the factorial moment in step 1 is at most \((mb_n)^s\prod_j(j!)^{-k_j}\). In particular,
\[
\mathbb E\bigl[Y_j\mid |P|=m\bigr]\le\frac{(mb_n)^j}{j!},
\qquad
\Pr(\exists j>J:Y_j>0\mid |P|=m)
\le\sum_{j>J}\frac{(mb_n)^j}{j!}.
\]
These bounds hold uniformly in \(n,m\).

**3. The one-relation Poisson vector.** Standard Bell-number asymptotics give \(\lambda_n\sim W(n)\), in particular \(b_n\to0\) and \(\lambda_{n-t}/\lambda_n\to1\) for every fixed nonnegative \(t\). If \(mb_n\to c\in(0,\infty)\), then \(m\to\infty\), and for each fixed \(s\)
\[
\frac{(m)_sB_{n-s}}{B_n}
=\frac{(m)_s}{(n)_s}\prod_{t=0}^{s-1}\lambda_{n-t}\longrightarrow c^s.
\]
Thus the mixed factorial moments in step 1 converge to \(\prod_j(c^j/j!)^{k_j}\), those of independent Poisson variables. The bound of step 2 dominates the corresponding multivariate factorial-moment power series in a neighborhood of any fixed finite argument; therefore the finite-coordinate probability generating functions converge to \(\exp(\sum_{j=1}^J(c^j/j!)(z_j-1))\). Convergence on each fixed count vector is thus total variation on finite coordinates. The last inequality of step 2 makes the unobserved size tail uniformly negligible as \(J\to\infty\). The limiting Poisson array also has a negligible tail, since its total expected count above \(J\) is \(\sum_{j>J}c^j/j!\). Truncation yields total-variation convergence of the full array.

**4. The joint multi-relation law.** Conditional on \(P=M\), the partitions are independent, so the count processes for different \(a\) are independent. Permutation invariance ensures that each process's conditional distribution depends only on \(|M|=m\), not on the identity of \(M\). Consequently, *when \(|P|=m\) deterministically*, integrating over the uniform choice of \(M\) preserves exact independence of the \(r\) processes: their joint distribution is exactly a product for every \(n\). By step 3 each factor tends in total variation to its indicated independent-Poisson array, and the finite product does too.

For independent-vertex marking, put \(M_n=|P|\sim\mathrm{Bin}(n,p_n)\). From \(np_nb_n\to c\) and \(\mathrm{Var}(M_nb_n)=np_n(1-p_n)b_n^2\le (np_nb_n)b_n\to0\), we obtain \(M_nb_n\to c\) in probability. Conditional on \(M_n=m\), the distribution is the fixed-size product just analyzed. The convergence in step 3 holds along **every deterministic sequence** satisfying \(mb_n\to c\); a standard subsequence argument, followed by bounded convergence for total variation (bounded above by one), therefore gives the same limit for the binomial mixture. This also proves that any dependence introduced by the shared random total mark count vanishes.

**5. Logical probabilities and extreme regimes.** The sentence \(\varphi_a\) holds exactly when \(\sum_{j\ge1}Y_{a,j}>0\). Because a sum of independent Poisson variables is Poisson with parameter \(\sum_{j\ge1}c^j/j!=e^c-1\), the asserted limit follows by total-variation convergence. When \(mb_n\to0\), step 2 gives \(\Pr(\varphi_a)\le e^{mb_n}-1\to0\), and the same is true for Bernoulli marks by direct expected-count bounds \(\mathbb E Y_j=\binom njp_n^j B_{n-j}/B_n\le (np_nb_n)^j/j!\). When \(mb_n\to\infty\), let \(T_a=Y_{a,1}\). The identities
\[
\mathbb E T_a=mb_n,\qquad
\mathbb E(T_a)_2=m(m-1)\frac{B_{n-2}}{B_n}
\]
show \(\mathrm{Var}(T_a)/(\mathbb E T_a)^2\to0\), since \(B_nB_{n-2}/B_{n-1}^2\to1\) and \(m\to\infty\). Thus \(\Pr(T_a=0)\to0\); a union bound over the fixed \(r\) gives simultaneous truth. Under Bernoulli marking, replace \(m\) by \(np_n\) in the first moment and use \(n(n-1)p_n^2 B_{n-2}/B_n\) in the second factorial moment to obtain the same conclusion. This proves the claimed sharp zero-to-one transition.

## Verification
The standalone `checker.py` enumerates every labeled set partition for \(n=1,\ldots,7\), every deterministic marked-set size \(0\le m\le n\), and all factorial-moment multiindices \((k_1,k_2,k_3)\in\{0,1,2\}^3\) with \(\sum_j j k_j\le n\). It compares exact rational values from direct enumeration against step 1's formula; **406 equalities passed**. It also checks the initial Bell numbers. The checker is deliberately finite; it cannot by itself establish the asymptotic limit, which follows from steps 2–5 and the cited Bell inequalities/asymptotics.

## Relationship to prior work
Arratia and Tavaré's 1994 theory of independent-process approximations encompasses the classical *unmarked, one-partition* Poisson component-count limit and its variants; no novelty is claimed for those underlying facts. The present claim is about **one shared sparse proposition in several independently random equivalence relations**, the exact finite-size decorrelation of the complete marked-block processes, their infinite-array joint total-variation limit, and the resulting simultaneous first-order sentence probability. Those objects are not supplied by the inspected single-assembly component-count results without a new conditional-coloring and product-mixture argument. Koponen's 2026 results concern conditions for finite-model properties and convergence in expansions of finite structures rather than this specific moving marking-density regime. Asai, Kubo, and Kuo provide the Bell-number log-concavity used for global tail bounds, not the asserted multiagent logical probability law.

## Limitations
The number of relations must be fixed; no rate is proved when the number of agents grows. The proposition is sampled independently of the equivalence relations, and the equivalence relations themselves are independent. Arbitrary dependence across agents, non-uniform partitions, or strongly nonexchangeable colors are not covered. The limiting law is **annealed** over random finite frames and labels, not a quenched statement for each frame. The general random-assembly literature may contain equivalent marked-component formulations not isolated in the inspected material, so historical priority needs broader specialist review. No independent validation was performed.

## References
1. Vera Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1, first posted 12 October 2026. https://arxiv.org/html/2610.16163v1 .
2. Richard Arratia and Simon Tavaré, *Independent Process Approximations for Random Combinatorial Structures*, *Advances in Mathematics* **104** (1994), 90–154; open arXiv reproduction: https://arxiv.org/abs/1308.3279 . Especially the general independent-component process and section on set partitions.
3. Nobuhiro Asai, Izumi Kubo, and Hui-Hsiung Kuo, *Bell numbers, log-concavity, and log-convexity*, *Acta Applicandae Mathematicae* **63** (2000), 79–87; https://arxiv.org/abs/math/0104137 .
