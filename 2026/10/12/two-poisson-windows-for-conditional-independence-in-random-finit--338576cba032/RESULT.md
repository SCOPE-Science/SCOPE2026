# Two Poisson windows for conditional independence in random finite teams

## Finding
Let \(n\ge 2\). Form an ordinary (unweighted) relational team \(T_n\subseteq[n]^3\) by including each triple independently with probability \(p_n\in[0,1]\). Interpret the relational conditional-independence atom \(x\perp_z y\) using the usual recombination semantics. Put
\[
\Pi_n(p_n)=\Pr(T_n\models x\perp_z y),\qquad
\alpha_n=n^{5/2}p_n,\qquad \beta_n=n^3(1-p_n).
\]
Then the following three regimes give a sharp two-sided probability law:

1. If \(\alpha_n\to a\in[0,\infty)\), then \(\Pi_n(p_n)\to\exp(-a^2/2)\). The number of conditioning fibers violating the atom converges in distribution to \(\operatorname{Poisson}(a^2/2)\).
2. If \(\beta_n\to b\in[0,\infty)\), then \(\Pi_n(p_n)\to\exp(-b)\). The number of violating fibers converges in distribution to \(\operatorname{Poisson}(b)\).
3. If simultaneously \(\alpha_n\to\infty\) and \(\beta_n\to\infty\), then \(\Pi_n(p_n)\to0\).

In particular, this natural non-monotone logical constraint is almost surely satisfied in both an extremely sparse and an almost-complete random team, and almost surely violated throughout the intervening regime. The sparse and dense transition windows have *different powers* of \(n\).

More generally, let the values of \(x,y,z\) range over nonempty finite sets of cardinalities \(r,s,k\), and include each of the \(rsk\) assignments with common probability \(p\). Define
\[
Q_{r,s}(p)=(1-p)^{rs}+\sum_{i=1}^{r}\sum_{j=1}^{s}\binom ri\binom sj p^{ij}(1-p)^{rs-ij}.
\]
The exact finite reliability is
\[
\Pr(T\models x\perp_z y)=Q_{r,s}(p)^k.
\]
The special case \(p=1/2\) yields \(\bigl(1+(2^r-1)(2^s-1)\bigr)^k\) satisfying relational teams out of \(2^{rsk}\); this unweighted enumeration follows directly from the standard rectangular-fiber description and is not asserted to be independently new.

## Assumptions and scope
A team is a **set**, not a multiset or a probability distribution on assignments. Independence means: for every \(u,v\in T\) with \(u(z)=v(z)\), there exists \(w\in T\) with \(w(z)=u(z)\), \(w(x)=u(x)\), and \(w(y)=v(y)\). An empty team or empty conditioning fiber satisfies the atom. All membership decisions in the Bernoulli model are independent; no claim covers correlated membership, probabilistic-team numerical conditional independence, or arbitrary nonconvergent density sequences beyond the three stated regimes.

## Proof
**Rectangular-fiber equivalence.** Fix a value \(c\) of \(z\), and write \(R_c=\{(a,b):(a,b,c)\in T\}\). The recombination clause holds at \(c\) if and only if \(R_c=\pi_x(R_c)\times\pi_y(R_c)\). Indeed, each ordered pair drawn from the two projections can be formed by choosing two witnesses and recombining them. Conversely, every Cartesian product is closed under recombination. Thus a satisfying fiber is either empty or uniquely equal to \(A\times B\) for nonempty subsets \(A,B\) of the respective coordinate sets.

**Finite probability.** For fixed \(A,B\) of sizes \(i,j\), the event \(R_c=A\times B\) has probability \(p^{ij}(1-p)^{rs-ij}\). There are \(\binom ri\binom sj\) such pairs of subsets; empty contributes \((1-p)^{rs}\). Distinct pairs produce distinct nonempty fibers. Multiplying independent probabilities over the \(k\) conditioning values proves the exact formula.

**Sparse window.** On one of the \(n\) square fibers, let \(N\) be its number of included pairs, so \(N\sim\operatorname{Bin}(n^2,p_n)\). When \(\alpha_n\) is bounded, \(n^2p_n=O(n^{-1/2})\), and \(\Pr(N\ge3)\le\binom{n^2}{3}p_n^3=O(n^{-3/2})\). A two-edge fiber fails precisely when its edges have different first and second coordinates. There are exactly \(2\binom n2^2\) such unordered edge pairs. Hence the per-fiber failure probability is
\[
d_n=2\binom n2^2p_n^2(1-p_n)^{n^2-2}+O(n^{-3/2}),
\qquad nd_n\longrightarrow a^2/2.
\]
For \(a=0\), the upper bound \(d_n\le\binom{n^2}{2}p_n^2\) gives the same conclusion. The number of failed fibers is \(\operatorname{Bin}(n,d_n)\), which converges to the stated Poisson law; its zero probability tends to \(\exp(-a^2/2)\).

**Dense window.** Let \(q_n=1-p_n\). A non-full rectangular \(n\times n\) fiber has an entirely empty row or an entirely empty column. The probability that any of the \(n\) fibers is a non-full rectangle is therefore at most \(2n^2q_n^n\). Consequently, when \(p_n\ge1/2\),
\[
p_n^{n^3}\le\Pi_n(p_n)\le p_n^{n^3}+2n^2q_n^n.
\]
If \(\beta_n\to b<\infty\), this squeezes \(\Pi_n\) to \(e^{-b}\). On a single fiber the same estimate shows its failure probability is \(1-p_n^{n^2}+O(2nq_n^n)\), so multiplying by \(n\) yields \(b\), while the single-fiber failure probability tends to zero. The binomial-to-Poisson argument proves the dense count law.

**Exhaustion of the intervening regime.** Suppose \(\alpha_n\to\infty\) and \(\beta_n\to\infty\). If \(p_n\ge1/2\), the preceding upper bound gives \(\Pi_n\le e^{-\beta_n}+2n^2 2^{-n}\to0\). For \(p_n\le1/2\), set \(\lambda_n=n^2p_n\). If \(\lambda_n\le1\), the event consisting of exactly two edges in distinct rows and columns yields \(d_n\ge c\lambda_n^2\) for a universal \(c>0\), since \((1-p_n)^{n^2-2}\) is uniformly bounded below. Therefore \(\Pi_n\le\exp(-cn\lambda_n^2)=\exp(-c\alpha_n^2)\to0\). If \(\lambda_n\ge1\), divide the rows and columns into two nonempty halves. With probability at least \((1-e^{-1/16})^2\), both opposite diagonal blocks contain an edge. Choose the first edge of each block. Their two cross-completion cells lie in the other two blocks and remain independent Bernoulli variables. At least one is absent with conditional probability \(1-p_n^2\ge3/4\). Thus the fiber fails with probability at least the positive constant \(\tfrac34(1-e^{-1/16})^2\). Taking the \(n\)-fold product again gives \(\Pi_n\to0\). These bounds hold uniformly across both subcases and complete the proof.

## Verification
The included standalone Python 3 verifier, `verify_independence.py`, exhaustively lists all \(2^{n^2}\) binary matrices for \(n=2,3,4\) and compares rectangularity with the coefficient formula. It independently evaluates the recombination definition on all \(2^8=256\) ternary teams for \(n=2\), checks three exact rational Bernoulli probabilities, and confirms 100 satisfying teams in that case. Run `python3 verify_independence.py`; the expected last line is `VERIFY_OK rectangle_matrices 66064 ternary_teams 256 rational_probability_tests 3`. These finite tests are corroboration; the limiting laws are proved above rather than inferred from experiments.

## Relationship to prior work
The usual relational independence clause and its relation to database multivalued dependencies are explicit in Hannula, Kontinen, and Virtema, *Polyteam Semantics*, arXiv:1704.02158, Definition 1 in Section 2.1. Hella, Luosto, and Väänänen, *Dimension in team semantics*, arXiv:2304.03354, study dimensions and representation of families satisfying dependence and independence atoms. Their natural unweighted rectangular-family perspective is antecedent to, and not a novelty claim of, the present finite enumeration. Hannula, Hirvonen, Kontinen, Kulikov, and Virtema, *Facets of Distribution Identities in Probabilistic Team Semantics*, arXiv:1812.05873, study *weighted* probabilistic independence semantics; the present Bernoulli sampling of an **unweighted relational team** is a different probabilistic question. The proposed contribution is the explicit two-sided critical-window law and complete intervening regime for that fixed relational atom.

## Limitations
No assertion is made for a universal threshold for every dependency atom, for other domain growth regimes, or for numerical independence of probability distributions. The full accepted-manuscript text of the 2023 dimension paper was not retrievable for a complete comparison; accessible indexed substantive passages include its independence-atom dimension formula. Equivalent asymptotic results may exist under terminology from random databases or complete bipartite subgraph reliability. There is no independent novelty or correctness audit.

## References
1. Miika Hannula, Juha Kontinen, Jonni Virtema, *Polyteam Semantics*, arXiv:1704.02158 (first public version 2017-04-07), https://arxiv.org/html/1704.02158v3 .
2. Miika Hannula, Åsa Hirvonen, Juha Kontinen, Vadim Kulikov, Jonni Virtema, *Facets of Distribution Identities in Probabilistic Team Semantics*, arXiv:1812.05873 (first public version 2018-12-14), https://arxiv.org/html/1812.05873v2 .
3. Lauri Hella, Kerkko Luosto, Jouko Väänänen, *Dimension in team semantics*, arXiv:2304.03354 (first public version 2023-04-06), https://arxiv.org/abs/2304.03354 ; Mathematical Structures in Computer Science 34 (2024), 410–454, DOI:10.1017/S0960129524000021.
