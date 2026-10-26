# Equilibrium multiplicity concentrates near maximal provision in complete public-goods networks

## Finding

Fix an integer capacity \(k\ge1\), and let \(n>k\) players occupy the loopless complete directed graph. Each player either abstains or buys a unit-value public good at cost \(c\in(0,1)\) and nominates exactly \(k\) distinct out-neighbours. A nominated player can use the good without buying. Let \(Q_n\) be the number of nonbuyers in a pure Nash equilibrium sampled uniformly from all labelled pure-equilibrium strategy profiles.

For \(k\le q\le\lfloor kn/(k+1)\rfloor\), the exact number of profiles with \(q\) nonbuyers is
\[
N_{n,k}(q)=\binom{n}{q}\sum_{j=0}^{q}(-1)^j\binom{q}{j}\binom{q-j}{k}^{n-q},
\]
and it is zero outside this range. For fixed \(k\),
\[
\frac{Q_n\log n}{n}\xrightarrow[n\to\infty]{\mathsf P}1.
\]
Thus a uniformly sampled equilibrium has \(n-o(n)\) buyers with probability tending to one. Since the largest equilibrium buyer count is \(n-k\) and the efficient buyer count is \(\lceil n/(k+1)\rceil\), the ratio of its cost to the worst equilibrium cost tends to \(1\), while its ratio to efficient cost tends to \(k+1\). Here \(\log\) is the natural logarithm and the probability is only over the uniform measure on labelled pure-equilibrium profiles.

## Assumptions and scope

The graph has every directed arc between distinct vertices and no loops. A buyer pays \(c\), obtains value \(1\) for the good, and chooses exactly \(k\) distinct other vertices to share it with; an abstainer pays nothing and has access if and only if at least one buyer nominates that player. The strict inequalities \(0<c<1\) remove indifference at both best-response boundaries. Capacity \(k\) is fixed as \(n\to\infty\), and \(n>k\). Strategy profiles are labelled, and different nomination sets count as different pure strategies. No behavioural equilibrium-selection assumption is made.

## Proof

Write \(m=n-q\) for the number of buyers. In equilibrium no buyer can be nominated: a nominated buyer could abstain, retain access, and save \(c>0\). Every nonbuyer must be nominated, since an unserved abstainer could buy and improve its payoff by \(1-c>0\). Consequently every buyer nominates only nonbuyers, so \(q\ge k\), and the \(mk\) nominations must cover all \(q\) nonbuyers, so \(mk\ge q\). Equivalently, \(k\le q\le\lfloor kn/(k+1)\rfloor\).

These two inequalities are sufficient as well. Label the nonbuyers by residues modulo \(q\). In a cyclic construction, buyer \(i\) nominates the \(k\) residues \(ik,ik+1,\ldots,ik+k-1\pmod q\). Because \(q\ge k\), each buyer's nominations are distinct; because \(mk\ge q\), the first \(mk\) residues include every nonbuyer. Thus each feasible \(q\) occurs in an equilibrium.

For a fixed nonbuyer set of size \(q\), count the ordered lists of \(m\) nominated \(k\)-subsets whose union is all of that set. Inclusion-exclusion over the nonbuyers omitted by every buyer gives
\[
A_{m,q,k}=\sum_{j=0}^{q}(-1)^j\binom{q}{j}\binom{q-j}{k}^{m}.
\]
Choosing the nonbuyer set in \(\binom nq\) ways proves the formula for \(N_{n,k}(q)\).

For the asymptotic statement, put \(q_0=\lfloor n/\log n\rfloor\) and \(m_0=n-q_0\). For all sufficiently large \(n\), this is feasible. If each buyer independently chooses a uniformly random \(k\)-subset of the \(q_0\) nonbuyers, a fixed nonbuyer is missed with probability \((1-k/q_0)^{m_0}\). The union bound therefore gives
\[
A_{m_0,q_0,k}\ge\binom{q_0}{k}^{m_0}\bigl(1-q_0(1-k/q_0)^{m_0}\bigr),
\]
where the factor in parentheses tends to \(1\), since \(q_0e^{-km_0/q_0}=O(n^{1-k}/\log n)\to0\). Hence
\[
\log N_{n,k}(q_0)=kn\log n-kn\log\log n-n\log(k!)-kn+o(n).
\]

For every feasible \(q\), inclusion-exclusion is bounded above by the number of all nomination lists, so
\[
\log N_{n,k}(q)\le g_n(q):=q\log(en/q)+(n-q)(k\log q-\log(k!)).
\]
A direct differentiation yields \(g_n''(q)=-(k+1)/q-kn/q^2<0\). For each fixed \(a>0\),
\[
g_n'\!\left(\frac{an}{\log n}\right)=k\log n\left(\frac1a-1\right)+O(\log\log n).
\]
Thus the unique maximizer of \(g_n\) lies at \(q\log n/n\to1\). Moreover, for every fixed \(\varepsilon\in(0,1)\), strict concavity and the displayed expansion imply that outside \([(1-\varepsilon)n/\log n,(1+\varepsilon)n/\log n]\), \(g_n\) is smaller than \(\log N_{n,k}(q_0)\) by at least \(\delta n\) for some \(\delta=\delta(k,\varepsilon)>0\) and all sufficiently large \(n\). There are at most \(n\) possible values of \(q\), so the total number of profiles outside this interval divided by \(N_{n,k}(q_0)\) is at most \(n\exp(-\delta n+o(n))\to0\). This proves convergence in probability.

Every equilibrium covers all players, so its social cost is \(c(n-Q_n)\). The extremal buyer counts follow from the same feasibility inequalities: the worst equilibrium has \(n-k\) buyers, and a minimum-cost covering outcome has \(\lceil n/(k+1)\rceil\) buyers. Since \(Q_n/n\to0\) in probability, the two stated cost-ratio limits follow.

## Verification

The exact profile formula was checked against direct enumeration of every pure strategy profile for all \(2\le n\le5\) and all \(1\le k<n\), using the included standard-library Python script. This finite check tests the counting formula and best-response characterization only; it is not used as a proof of the asymptotic limit. The asymptotic result follows from the analytic upper and lower bounds in the proof. The uniform profile measure and fixed-capacity limit are explicit parts of the claim.

## Relationship to prior work

Deligkas, Gutin, Jones, Neary, and Yeo study the same capacity-constrained directed best-shot game and prove that the pure price of anarchy is \(k+1\); their complete-digraph example includes an equilibrium with \(n-k\) buyers. Their paper studies existence, computational complexity, and efficiency bounds, but does not state the exact number of labelled pure-equilibrium strategy profiles or their uniform-profile asymptotic distribution. Papadimitriou and Peng study public-goods games on directed graphs with buy/abstain actions and no nomination-capacity choices, so their complexity results do not determine this profile count. Bramoullé and Kranton study undirected networks with continuous effort and characterize specialized equilibria through maximal independent sets; that is a different strategy space and payoff model.

## Limitations

The asymptotic is for fixed \(k\) and uniform sampling over labelled pure-equilibrium strategy profiles. It does not assert that actual agents select equilibria uniformly, does not cover \(k\) growing with \(n\), and does not extend automatically to incomplete or arbitrary directed graphs. The count treats nomination choices as distinct strategies, as required by the model.

## References

1. A. Deligkas, G. Gutin, M. Jones, P. R. Neary, and A. Yeo, “Public Goods Games in Directed Networks with Constraints on Sharing,” arXiv:2511.11475 (first public version 2025-11-14). https://arxiv.org/abs/2511.11475
2. C. Papadimitriou and B. Peng, “Public Goods Games in Directed Networks,” arXiv:2106.00718 (2021). https://arxiv.org/abs/2106.00718
3. Y. Bramoullé and R. Kranton, “Public goods in networks,” Journal of Economic Theory 135 (2007), 478–494. https://doi.org/10.1016/j.jet.2006.06.006
