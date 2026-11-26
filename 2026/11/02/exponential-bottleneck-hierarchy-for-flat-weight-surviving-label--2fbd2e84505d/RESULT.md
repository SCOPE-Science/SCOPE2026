# Joint limits for the low-state residence times of the flat-weight conclave chain

## Finding

There are \(n\ge3\) voters and initially \(n\) active labels. Independently in each round, conditional on the active set, each voter chooses uniformly among that set. Unchosen labels are removed permanently. Let \(K_t\) be the number of labels after round \(t\), with \(K_0=n\). Let \(T_n=\inf\{t:K_t=1\}\) and, for \(2\le k\le n\), set \(H_{n,k}=\#\{t<T_n:K_t=k\}\), with zero residence time at a skipped level.

For every fixed integer \(r\ge2\), as \(n\to\infty\),
\[
\left(\frac{H_{n,k}}{(k/(k-1))^n}\right)_{k=2}^r
 \;\Longrightarrow\;(E_k)_{k=2}^r,
\]
where the \(E_k\) are independent exponentials with rates \(k\). In particular, the convergence is unconditional: the probability that any one of these fixed levels is skipped vanishes. Quantitatively, for \(2\le j\le n\),
\[
\Pr(\text{state }j\text{ is skipped})\le \min\{1,n^j((j-1)/j)^n\}.
\]
This describes the separate time fluctuations within the last several surviving supports, which cannot be read off from an asymptotic law for the total time on its largest scale.

## Assumptions and scope

The number of votes remains \(n\) at each round; the set of labels to choose from does not. The model uses weight one for a positive vote count and zero for a zero count. It is a separately defined endpoint of the power-weight conclave model, not a theorem for a positive reinforcement power or a uniform crossover as that power tends to zero. The joint limit is only asserted for fixed \(r\).

## Proof

The support-size chain is Markov and nonincreasing. For \(1\le j\le k\), its transition probability is \(P_n(k,j)=\binom{k}{j}j!S(n,j)/k^n\), where \(S(n,j)\) is a Stirling number of the second kind: choose the occupied labels and count onto maps. If \(q_{n,k}=1-P_n(k,k)\), then \(q_{n,k}\ge ((k-1)/k)^n>0\) for \(k\ge2\), by missing one specified label. Thus every visited nonabsorbing state is left almost surely, and absorption follows after finitely many strict decreases. For fixed \(k\), inclusion-exclusion gives
\[
q_{n,k}=\sum_{i=1}^k(-1)^{i+1}\binom{k}{i}\left(\frac{k-i}{k}\right)^n
=k\left(\frac{k-1}{k}\right)^n(1+o(1)).
\]

If the chain leaves \(k\ge j+1\) and lands below \(j\), all its votes have landed in some \(j-1\) labels. The probability of such a jump conditional on departure is bounded above by
\[
\frac{\binom{k}{j-1}((j-1)/k)^n}{q_{n,k}}
\le \binom{k}{j-1}\left(\frac{j-1}{k-1}\right)^n.
\]
The same conditional distribution holds at the first departure after any number of self-loops. A skipped level entails such a jump, and there are at most \(n\) departures, with \(\binom{k}{j-1}\le n^{j-1}\) and \(k-1\ge j\) at each candidate jump. A union bound yields the claimed estimate, including the boundary \(j=n\), which is never skipped. For fixed \(r\), all of \(2,\dots,r\) are visited with probability tending to one.

At a visited level \(k\), the number of rounds up to and including departure is geometric on \(\{1,2,\dots\}\) with parameter \(q_{n,k}\), independent of its destination. Indeed, the joint probability of departing at attempt \(m\) for a particular \(j<k\) is \((1-q_{n,k})^{m-1}P_n(k,j)\). Since a level cannot be revisited after departure, sample in advance independent geometric durations \(G_{n,k}\) for all levels and independent departure destinations for all levels, then follow only the selected levels. This realizes \(H_{n,k}=G_{n,k}\) at visited levels. The geometric tail and \(q_{n,k}(k/(k-1))^n\to k\) imply \(G_{n,k}/(k/(k-1))^n\Rightarrow\operatorname{Exp}(k)\). Products of these independent tails give the finite-dimensional joint limit; replacing the auxiliary clocks by the actual residence times changes the vector only on the vanishing event that a fixed level is skipped.

## Relationship to prior work

Benjamini, Cai, Chen, Gong and Li, *The Conclave Process*, [arXiv:2607.22324](https://arxiv.org/abs/2607.22324), treat positive power reinforcement and in Theorem 1.5 obtain an exponential lower bound on the consensus time for a fixed power in \((0,1)\). The transition formula here is the classical single-round occupancy count. Cancrini and Posta, *Mixing time for the Repeated Balls into Bins dynamics*, [arXiv:2001.11246](https://arxiv.org/abs/2001.11246), consider a conservative chain in which empty bins may be refilled.

The indexed finding [*Metastable geometric fixation and an exponential hierarchy at zero reinforcement*](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-metastable-geometric-fixation-and-an-exponential-hierarchy-at-ze--1759e90a3004) describes the same endpoint and overlaps on the consensus-time law and exponential corrections to its expectation. Neither of those total-time findings is claimed here. The indexed summary does not specify the joint limit for the separately rescaled low-state residence times. The assessment of overlap is limited to the accessible statement and does not establish historical priority.

## Verification and limitations

The proof supplies the asymptotic joint law and visitation bound. The optional companion `checker.py` is a finite arithmetic check of the occupancy identities and selected visitation bounds; it cannot certify independence or the infinite-population limit. No result is asserted for a growing range of state labels.
