# Exact finite-electorate justified-representation probabilities and their sharp universal failure exponent

## Finding

For every finite number of voters \(n\ge 1\), candidates \(m\ge k\ge 1\), and independent, voter-homogeneous but candidate-heterogeneous Bernoulli approval probabilities \(p_c\in[0,1]\), the probability that a fixed size-\(k\) committee satisfies justified representation (JR) admits an exact one-dimensional binomial-mixture formula. Every committee selecting the \(k\) largest candidate probabilities maximizes this probability **for every finite \(n\)**. For fixed \(m>k\), its worst-case failure probability over the entire probability cube has a sharp universal large-deviation exponent.

For a committee \(W\), put
\[
q_W=\prod_{c\in W}(1-p_c),\quad r=\left\lceil\frac nk\right\rceil,\quad B_u(p)=\Pr\{\operatorname{Bin}(u,p)<r\}.
\]
Then the exact JR probability is
\[
J_n(W)=\sum_{u=0}^{n}\binom nu q_W^u(1-q_W)^{n-u}\prod_{c\notin W} B_u(p_c).
\tag{1}
\]
The empty product is one. The formula can be evaluated exactly in polynomial time for rational input probabilities, including probabilities zero and one. Sorting \(p_c\) and taking any \(k\) largest is an exact algorithm for maximizing \(J_n(W)\) in this model.

Let \(W^\star\) denote such a top-\(k\) committee, and define
\[
a_k=\frac{k^k}{(k+1)^{k+1}},\qquad I_k=D\!\left(\frac1k\middle\|a_k\right),
\]
where the binary relative entropy is \(D(x\|a)=x\log(x/a)+(1-x)\log((1-x)/(1-a))\), with \(0\log0=0\). Then \(I_k>0\), and for every finite \(n,m,k\),
\[
\Pr\{W^\star\text{ fails JR}\}\le (m-k)e^{-nI_k}.
\tag{2}
\]
For each fixed \(m>k\ge1\), this exponential rate is globally sharp:
\[
\lim_{n\to\infty}-\frac1n\log\!\left(
\sup_{\boldsymbol p\in[0,1]^m}\Pr_{\boldsymbol p}\{W^\star\text{ fails JR}\}
\right)=I_k.
\tag{3}
\]
Ties in selecting the largest probabilities can be resolved arbitrarily, consistently within each probability vector.

## Assumptions and scope

The candidate set is \(C=\{1,\ldots,m\}\) and voter set is \(V=\{1,\ldots,n\}\). Every voter \(i\) independently approves each candidate \(c\) with probability \(p_c\), independent across *all* voter-candidate pairs. Candidate probabilities may differ but cannot depend on the voter. Empty approval ballots are allowed.

A size-\(k\) committee \(W\subseteq C\) has JR precisely when every voter group \(S\subseteq V\) with \(\lvert S\rvert\ge n/k\) and a commonly approved candidate contains at least one voter approving some member of \(W\). Equivalently, among voters who approve **no** member of \(W\), no outside candidate is approved by \(r=\lceil n/k\rceil\) or more voters. This equivalence includes all integer-rounding boundary cases.

Statements (1) and the finite-\(n\) maximization hold for \(m=k\) and boundary probabilities. Statement (3) assumes fixed \(m>k\) as \(n\to\infty\). If \(m=k\), JR never fails, and no finite logarithmic failure exponent is asserted. Neither independence across candidates nor voter-homogeneity can be omitted from (1) without further argument.

## Proof

**Conditional reduction.** For every voter, the event of approving no elected candidate has probability \(q_W\), independently of the analogous events for the other voters. Thus the number \(U\) of unrepresented voters has law \(\operatorname{Bin}(n,q_W)\). Conditional on the identity of this unrepresented set, each outside candidate \(c\) has an independent \(\operatorname{Bin}(U,p_c)\) number of approvals within it. Counts of distinct outside candidates remain independent because their approval columns are independent. JR holds precisely when each such count is below \(r\). Multiplication of these conditional probabilities and averaging over \(U\) proves (1), including \(U=0\), \(p_c\in\{0,1\}\), and \(m=k\).

To evaluate (1), calculate each \(B_u(p_c)\) by a binomial sum for all \(u\le n\), using at most \(O(mn^2)\) rational arithmetic operations; products and the outer sum add polynomial work. The numerator and denominator bit lengths remain polynomial in the finite rational input bit lengths and \(m,n\). This supplies an exact, not Monte Carlo, algorithm.

**Global finite-electorate optimum.** In (1), \(J_n(W)\) is nonincreasing as a function of \(q_W\): if \(q\) grows, the binomially distributed number \(U\) of unrepresented voters is stochastically larger, while \(u\mapsto\prod_{c\notin W}B_u(p_c)\) is nonincreasing. The same formula is nonincreasing in each excluded candidate probability \(p_c\), since \(B_u(p_c)\) decreases when \(p_c\) increases. Consider an elected candidate \(b\in W\) and unelected candidate \(a\notin W\) with \(p_a\ge p_b\). Replacing \(b\) by \(a\) weakly decreases the unrepresented probability \(q_W\) and replaces an outside probability \(p_a\) by a weakly smaller outside probability \(p_b\), leaving all other outside probabilities fixed. Both changes weakly increase the probability of JR. Repeated exchanges reach a top-\(k\) committee, proving the finite-\(n\) optimizer, including ties and boundary cases without dividing by \(1-p_b\).

**Uniform tail bound.** For any excluded candidate \(c\notin W^\star\), each voter independently both approves \(c\) and disapproves every elected candidate with probability \(a_c=p_cq_{W^\star}\). Since every elected probability is at least \(p_c\),
\[
a_c\le p_c(1-p_c)^k\le\max_{0\le x\le1}x(1-x)^k
=\frac{k^k}{(k+1)^{k+1}}=a_k<\frac1k.
\]
The maximum is attained at \(x=1/(k+1)\), by differentiation; the final strict inequality holds for every positive integer \(k\). A Bernoulli relative-entropy Chernoff bound gives
\[
\Pr\{\operatorname{Bin}(n,a_c)\ge r\}\le
\exp\left[-nD\!\left(\frac1k\middle\|a_c\right)\right]
\le e^{-nI_k}.
\]
The monotonicity of \(D(1/k\|a)\) for \(0<a<1/k\) gives the last inequality. For \(a_c=0\), the left probability is zero, so continuity handles endpoints. The union bound over the \(m-k\) excluded candidates proves (2).

**Optimality of the exponent.** Fix \(m>k\), and choose \(p_c=1/(k+1)\) for *all* candidates. All top-\(k\) selections are equivalent; for any one excluded candidate, the number of its approvals among unrepresented voters is exactly \(\operatorname{Bin}(n,a_k)\). Hence the full JR-failure probability is bounded **below** by its single-candidate upper-tail probability. The binomial large-deviation limit, obtainable by Stirling's formula applied to the term at \(r=\lceil n/k\rceil\) together with the Chernoff upper bound, is
\[
\lim_{n\to\infty}-\frac1n\log\Pr\{\operatorname{Bin}(n,a_k)\ge r\}=I_k.
\]
For \(k=1\), this reduces exactly to \(\Pr\{\operatorname{Bin}(n,1/4)=n\}=4^{-n}\). Combining this lower bound on worst-case failure with (2) proves (3). No finite computation is used to infer the infinite limit.

## Verification

The accompanying standalone Python program `verification.py` uses only the standard library. It computes (1) in exact rational arithmetic and separately enumerates *all voter-candidate approval profiles*, checking JR directly against **all** cohesive voter subsets. It tests candidate-heterogeneous examples, ties, certain approvals, impossible approvals, and \(k=m\), compares every committee to the top-\(k\) choice, and checks the large-deviation constants numerically without treating finite tests as a proof.

For \(n=4,m=3,k=2\) and candidate probabilities \((3/4,1/2,1/4)\), the top-two committee has \(q=1/8\), sole outsider probability \(1/4\), and failure occurs when \(\operatorname{Bin}(4,1/32)\ge2\). Therefore
\[
\Pr\{\text{JR}\}=\frac{1042685}{1048576},\qquad
\Pr\{\text{JR fails}\}=\frac{5891}{1048576}.
\]
The independent full-profile enumeration gives the same exact result. Running `python verification.py` passes 81 explicit assertions; these assertions verify examples, not the universal quantifiers in the proof.

## Relationship to prior work

Aziz, Kagita, Rastegari and Suzuki study uncertain approval committee voting, prove JR-probability counting hardness for general voter-candidate probabilities, and give a polynomial-time special case when all elected approval decisions are deterministic. Their results do not state the present voter-homogeneous but candidate-heterogeneous stochastic exact mixture or the finite-\(n\) top-probability optimality theorem.

Elkind, Faliszewski, Igarashi, Manurangsi, Schmidt-Kraepelin and Suksompong prove asymptotic JR guarantees for common-\(p\) independent approval culture. In particular, their proof already identifies the maximum \(k^k/(k+1)^{k+1}\) of \(p(1-p)^k\); that maximization and qualitative high-probability JR are **prior art**, not claimed new. The new quantitative conclusion is the exact optimal *relative-entropy exponent* for the entire heterogeneous-parameter cube, together with (1) and finite-\(n\) optimal selection.

Xia's later linear theory proves that top-probability committees satisfy stronger CORE and EJR+ requirements with exponentially high probability in the fixed-parameter i.i.d. model; that qualitative asymptotic coverage is also **prior art**. Neither that asymptotic result nor the cited earlier JR threshold theorem supplies (1), the finite-\(n\) JR optimizer, or equality in the universal worst-case exponential rate (3). No claims about maximizing PJR or EJR probability are made here.

## Limitations

All conclusions use independence across voters and candidates, and probabilities constant across voters for each candidate. The chosen committee is selected from the distribution parameters before the actual ballots are drawn; it is not an observed-profile winner rule. The exponential statement holds for fixed candidate and committee counts as the number of voters grows; no uniformity in a growing number of candidates is asserted. The exponent need not give an exact finite-\(n\) failure probability and the prefactor in (2) need not be sharp. Broader published probability identities could imply part of the formula; publication priority remains subject to independent assessment.

## References

1. H. Aziz, V. R. Kagita, B. Rastegari, M. Suzuki, *Approval-Based Committee Voting under Uncertainty* (2024), arXiv:2407.19391, https://arxiv.org/abs/2407.19391 . Initial public version: 2024-07-28.
2. E. Elkind, P. Faliszewski, A. Igarashi, P. Manurangsi, U. Schmidt-Kraepelin, W. Suksompong, *Justifying Groups in Multiwinner Approval Voting* (2021, revised 2022), arXiv:2108.12949, https://arxiv.org/pdf/2108.12949 .
3. L. Xia, *A Linear Theory of Multi-Winner Voting* (2025), arXiv:2503.03082, https://arxiv.org/pdf/2503.03082 .
4. H. Aziz et al., *Justified Representation in Approval-Based Committee Voting*, Proceedings of AAAI (2015), DOI:10.1609/aaai.v29i1.9324, https://doi.org/10.1609/aaai.v29i1.9324 .
5. R. Bredereck et al., *An Experimental View on Committees Providing Justified Representation* (2019), https://doi.org/10.24963/ijcai.2019/16 .
