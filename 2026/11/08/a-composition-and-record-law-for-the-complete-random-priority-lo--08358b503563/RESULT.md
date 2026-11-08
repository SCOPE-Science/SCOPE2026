# A composition and record law for the complete random-priority lottery with one preference dissenter

## Finding

Let \(n\ge2\) agents be matched one-to-one with \(n\) objects. Exactly \(n-1\) agents share the strict ranking \(1\succ2\succ\cdots\succ n\), while a distinguished agent \(e\) has any strict ranking \(\pi\). Random serial dictatorship (RSD) draws all \(n!\) agent priority orders uniformly and gives each agent her favorite remaining object. This finding concerns the **probability of each entire labeled matching**, not merely the matrix of agent-object marginals.

For \(0\le k<n\), let \(f(k)\) be \(e\)'s favorite object among \(\{k+1,\ldots,n\}\), and set
\[
 t_x=\left|\{k\in\{0,\ldots,n-1\}:f(k)=x\}\right|\quad(1\le x\le n).
\]
Then for **each** bijective labeled assignment \(M\), with \(M(e)\) the object assigned to the distinguished agent,
\[
 \Pr_{\mathrm{RSD}}(M)=\frac{t_{M(e)}}{n!}.
\]
An assignment is in the support if and only if it is Pareto efficient. More specifically, \(t_x>0\) exactly when the exceptional agent ranks \(x\) above all larger-indexed objects. If \(R=|\{x:t_x>0\}|\), the deterministic-matching support size is \(S=(n-1)!R\).

The positive multiplicities \(t_x\), read at increasing object indices, range over **every ordered composition of \(n\)** as \(\pi\) varies, and only those compositions. Thus exactly \(2^{n-1}\) ordered multiplicity patterns and \(p(n)\) unordered lottery shapes occur, where \(p(n)\) is the integer partition number. Every support size in
\[
 \{(n-1)!,2(n-1)!,\ldots,n!\}
\]
occurs, and no other one does.

If \(\pi\) is additionally drawn uniformly from all \(n!\) strict rankings, then for any ordered composition \(c=(c_1,\ldots,c_r)\) with \(C_0=0\) and \(C_j=\sum_{h=1}^j c_h\), its exact frequency among these rankings is
\[
 \#\{\pi:(t_x)_{t_x>0}=c\}=\frac{n!}{\prod_{j=0}^{r-1}(n-C_j)}.
\]
The number of positive multiplicities has the unsigned Stirling-number law
\[
 \Pr(R=r)=\frac{\left[{n\atop r}\right]}{n!},\qquad
 \mathbb E[S]=(n-1)!H_n,\qquad
 \operatorname{Var}(S)=((n-1)!)^2\left(H_n-H_n^{(2)}\right),
\]
where \(H_n=\sum_{j=1}^n1/j\), \(H_n^{(2)}=\sum_{j=1}^n1/j^2\), and \(\left[{n\atop r}\right]\) is the unsigned Stirling number of the first kind. These statements are simultaneous for every integer \(n\ge2\); no distributional assumption on \(\pi\) is needed for the fixed-profile assertions.

## Assumptions and scope

Objects are distinct and indexed by the **common agents'** strict desirability order. Agents are labeled, have unit demand, and find all objects acceptable. Each matching is a complete bijection. Ties are absent. RSD draws agent orders uniformly. The exceptional agent can report any one of the \(n!\) strict orders, including the common order. The extra random-ranking hypothesis applies only to the composition-frequency, Stirling, and expectation formulas. The lottery is the induced distribution on complete labeled matchings; it need not be recoverable from its matrix of individual marginal probabilities.

## Proof

**Step 1: Count priorities yielding one complete matching.** In any RSD priority list, the common-preference agents acting before \(e\) take objects \(1,2,\ldots,k\) in that order, for some \(k\in\{0,\ldots,n-1\}\). Consequently \(e\) receives \(f(k)\). After \(e\)'s action, the remaining common-preference agents take the remaining objects in increasing index order. Fix a labeled matching \(M\) and an integer \(k\). If \(M(e)=f(k)\), there is exactly **one** priority ordering yielding \(M\) in which \(e\) acts after \(k\) common agents: list, in increasing order of the object they receive in \(M\), the \(k\) agents assigned \(1,\ldots,k\), then \(e\), then all other common agents in increasing assigned-object order. If \(M(e)\ne f(k)\), there is none. Summing over \(k\) gives exactly \(t_{M(e)}\) priorities and establishes the probability formula. It also verifies normalization because \(\sum_x t_x=n\) and, for each \(x\), exactly \((n-1)!\) labeled matchings assign \(x\) to \(e\).

**Step 2: Characterize support and Pareto efficiency.** For fixed \(x\), the condition \(f(k)=x\) for some \(k\) is equivalent to \(e\)'s preference for \(x\) over every object with index larger than \(x\). The forward implication holds because all larger indices remain available whenever \(x\) does; the reverse implication uses \(k=x-1\). Now suppose a matching assigns \(x\) to \(e\), where \(x\) is not such a suffix record. There is an object \(y>x\) preferred by \(e\) to \(x\). Exchanging \(x\) and \(y\) with the common agent holding \(y\) strictly improves both agents, so the matching is not efficient. Conversely assume \(x\) is a suffix record. In any weak Pareto improvement \(M'\), each common agent must receive an object with index no greater than that agent's original index. Summing indices over the common agents yields \(n(n+1)/2-M'(e)\le n(n+1)/2-x\), hence \(M'(e)\ge x\). If strict, \(e\) becomes strictly worse by the suffix-record property. If equality holds, all common agents' indices must also be unchanged, so there is no strict improvement. Thus all supported matchings and only those are Pareto efficient.

**Step 3: Derive compositions and shape counts.** As \(k\) runs from \(0\) to \(n-1\), \(f(k)\) is nondecreasing in object index: the suffix shrinks, so its highest-ranked object either remains or is removed, in which case the new winner has a larger index. It starts at some \(x_1\) and ends at \(n\), with record indices \(x_1<\cdots<x_r=n\). The consecutive run lengths are precisely \(c_1=x_1\), \(c_j=x_j-x_{j-1}\) for \(j\ge2\), a positive-integer composition of \(n\). Conversely choose any composition and cumulative indices \(x_j=C_j\). Rank these indices at the top in the order \(x_1\succ x_2\succ\cdots\succ x_r\), ahead of every remaining index in arbitrary order. Its suffix winners occur with exactly the designated run lengths. Sorting their positive lengths maps ordered compositions to integer partitions bijectively at the level of unordered multiplicity shapes. A part of size \(c_j\) appears \((n-1)!\) times among the nonzero priority multiplicities of complete labeled matchings. This proves both pattern counts and the support-size spectrum.

**Step 4: Count profile frequencies and records.** Under a uniform random strict ranking \(\pi\), the most preferred object among \(\{1,\ldots,n\}\) is uniform, so the probability that its index is \(x_1=C_1\) is \(1/n\). Conditional on that event, the relative order within \(\{x_1+1,\ldots,n\}\) remains uniform. Repeating for the successive suffixes gives probability \(\prod_{j=0}^{r-1}(n-C_j)^{-1}\) for a specified ordered composition. Multiplication by \(n!\) gives its exact count. The events that an index is a right-to-left preference record are independent under a uniformly random permutation: insert the items into a uniformly random ranking in successively growing suffix sets; each item's relative insertion rank is uniform and independent. Thus the record at index \(x\) occurs with probability \(1/(n-x+1)\), independently for each \(x\). Consequently
\[
 \mathbb E[z^R]=\prod_{j=1}^n\left(1-\frac1j+\frac zj\right)
 =\frac{z(z+1)\cdots(z+n-1)}{n!}.
\]
The coefficient of \(z^r\) is the unsigned Stirling number \(\left[{n\atop r}\right]/n!\). Summing independent Bernoulli expectations and variances proves the stated mean and variance of \(S=(n-1)!R\).

## Verification

The standalone `verify.py` uses exact integers and fractions and the standard Python library. It separately enumerates every exceptional strict ranking and every priority order for \(2\le n\le6\), comparing every complete labeled assignment's priority count with the formula, and for \(n\le5\) independently tests Pareto efficiency against all possible improving complete matchings. It checks all possible composition-pattern frequencies for \(2\le n\le7\), their Stirling support-size frequencies and exact expected support sizes; sampled priority-order checks cover \(n=7,8\). The run reported 872 exhaustive profiles, 1,077,736 priority evaluations, 495,781 positive-support matching comparisons and 15,016 independent Pareto checks, plus the exact ordered-composition checks through \(n=7\). These are finite corroboration, not a substitute for the general proof above. Run with `python3 verify.py`.

For example, with four objects and exceptional order \(2\succ4\succ1\succ3\), the two positive values are \(t_2=t_4=2\); precisely twelve complete labeled matchings have probability \(1/12\) each. Across all twenty-four exceptional strict rankings, the distribution of \(R\) is \((1:6,2:11,3:6,4:1)\), and the mean number of supported complete matchings is \(25/2\).

## Relationship to prior work

Shen, Wang, Zhu, Fain, and Munagala (2023) formulate uncertain priorities and compare efficiency and fairness of RSD and alternatives. Brandt, Greger, and Romen (2023) study axiomatizations of RSD and prove a distinct result on a restricted preference domain, which allows agents to move the position of a single object while keeping the ranking of the others. Aziz and Mestre (2014) give a **general polynomial-time algorithm for agent-object marginal probabilities when the number of preference types is fixed**, which applies in particular to this two-type domain; no new generic tractability claim is made here. Their three-agent example with two matching preferences is a finite overlapping instance. The new statement instead supplies the **complete joint matching lottery**, a closed form for its full support and multiplicities for every \(n\), the composition spectrum, and an exact profile-frequency law; these are not implied by the cited general marginal-probability algorithm or axiomatic assertions. Existing small-market deterministic-support censuses cover some fixed small \(n\) cases but do not determine the variable-size composition law.

## Limitations

The conclusion relies on exactly one agent differing arbitrarily from \(n-1\) agents with a common strict order and on uniformly sampled agent priorities. It makes no claim for two or more arbitrary dissenters, nonuniform agent priorities, ties, incomplete preferences, or non-square allocation. The integer-partition classification is for the entire deterministic matching lottery, not the much smaller set of positive **agent-object marginal** entries. The result does not imply full stochastic-dominance efficiency, strategyproof uniqueness, or an algorithm for the unrestricted counting problem. A separate specialist article on near-common preferences was available only in abstract and has not been ruled out as an unindexed priority overlap; independent mathematical review remains unperformed.

## References

- Z. Shen, Z. Wang, X. Zhu, B. Fain, K. Munagala, *Fairness in the Assignment Problem with Uncertain Priorities*, first arXiv posting January 31, 2023, https://arxiv.org/abs/2301.13804.
- F. Brandt, M. Greger, R. Romen, *Towards a Characterization of Random Serial Dictatorship*, first arXiv posting March 21, 2023, https://arxiv.org/abs/2303.11976.
- H. Aziz, J. Mestre, *Parametrized Algorithms for Random Serial Dictatorship*, first arXiv posting March 4, 2014, https://arxiv.org/abs/1403.0974.
- H.-I. Chang, Y. Chun, *Probabilistic assignment of indivisible objects when agents have the same preferences except the ordinal ranking of one object*, *Mathematical Social Sciences* 90 (2017), 80–92, https://doi.org/10.1016/j.mathsocsci.2017.08.001.
- A. Abdulkadiroğlu, T. Sönmez, *Random Serial Dictatorship and the Core from Random Endowments in House Allocation Problems*, *Econometrica* 66 (1998), 689–702.
