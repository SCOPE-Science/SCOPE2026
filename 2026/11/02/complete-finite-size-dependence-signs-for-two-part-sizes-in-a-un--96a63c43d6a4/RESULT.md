# Complete finite-size dependence signs for two part sizes in a uniform integer partition

## Finding

Let \(\lambda\) be uniform over the \(p(n)\) unrestricted integer partitions of \(n\), and let \(I_r(\lambda)=\mathbf1\{\lambda\text{ contains a part of size }r\}\). For every \(n\ge2\) and pair \(1\le r<s\le n\), the signs of \(\operatorname{Cov}(I_r,I_s)\) are completely classified:

- **Positive:** \(r=1,\ s=n-1\) with \(n\ge3\), together with the eleven triples \((n,r,s)\)
  \[
  \begin{gathered}
  (5,2,3),(6,2,4),(7,2,5),(8,3,5),\\
  (6,1,3),(8,1,3),(10,1,3),(12,1,3),\\
  (12,1,5),(14,1,3),(16,1,3).
  \end{gathered}
  \]
- **Zero:** exactly \((8,2,6),(9,2,7),(7,3,4),(10,1,5),(9,1,2)\).
- **Negative:** every other admissible triple.

In particular, for every \(n\ge17\), **only** the pair of part sizes \(1\) and \(n-1\) is positively correlated; all other distinct sizes have strictly negative occurrence covariance. This is a complete finite-size sign law, not merely an asymptotic approximation.

## Assumptions and scope

An integer partition of \(n\) is an unordered multiset of positive integers summing to \(n\). The sample law is uniform over all unrestricted partitions. Define \(p(m)\) as the exact integer partition number for \(m\ge0\), with \(p(0)=1\). The binary occurrence indicator \(I_r\) is one if and only if at least one part of size \(r\) occurs; it is **not** the multiplicity count. The result holds for every finite integer \(n\ge2\) and all distinct \(1\le r<s\le n\). Only pairwise covariance signs are asserted; no general negative-association property is claimed.

The all-size step uses the independently established strict partition-number log-concavity theorem of DeSalvo and Pak [2],
\[
p(m)^2>p(m-1)p(m+1)\qquad(m\ge26).
\]
No new proof of that published theorem is claimed.

## Proof

**1. Exact probability identity.** Removing one occurrence of a prescribed part size \(r\) gives a bijection from partitions containing \(r\) to partitions of \(n-r\). Removing one each of distinct \(r,s\) gives the analogous joint bijection when \(r+s\le n\). Hence
\[
\Pr(I_r=1)=\frac{p(n-r)}{p(n)},\qquad
\Pr(I_r=I_s=1)=\begin{cases}
\frac{p(n-r-s)}{p(n)},&r+s\le n,\\
0,&r+s>n.
\end{cases}
\]
If \(r+s>n\), the covariance is strictly negative because the two marginal probabilities are positive.

**2. Reduction to one partition-number defect.** If \(r+s\le n\), put \(a=n-r-s\ge0\), and define
\[
F(a,r,s)=p(a+r)p(a+s)-p(a)p(a+r+s).
\]
Then
\[
\operatorname{Cov}(I_r,I_s)=-\frac{F(a,r,s)}{p(n)^2}.
\]
The sign of the covariance is precisely the *opposite* of the sign of \(F\).

**3. Monotonic propagation above the log-concavity threshold.** Set
\[
Q_t(x)=\frac{p(x+t)}{p(x)} \qquad (t\ge1,\ x\ge0).
\]
By [2], \(p(m+1)/p(m)\) strictly decreases for all \(m\ge26\); a product of \(t\) such factors shows \(Q_t(x)\) strictly decreases in integer \(x\ge26\). Moreover,
\[
\frac{F(a,r,s)}{p(a)p(a+s)}=Q_r(a)-Q_r(a+s).
\]
Consequently, for fixed \(a,r\), this normalized defect strictly increases as \(s\) increases beyond any point satisfying \(a+s\ge26\). The analogous assertion holds when the roles of \(r\) and \(s\) are exchanged. For \(a\ge26\), \(Q_r(a)>Q_r(a+s)\), so \(F(a,r,s)>0\) for every \(r,s\ge1\).

For \(0\le a\le25\), put \(R=26-a\). Replace each of \(r,s\) by its cap at \(R\), obtaining \(r_0=\min(r,R)\), \(s_0=\min(s,R)\). Extending either coordinate from \(R\) is strictly favorable to the sign of the normalized defect, by the previous paragraph. If both coordinates cap at \(R\), the finite check below establishes \(F(a,R,R)>0\). If they cap to distinct values, the finite check controls all possible negative and zero cap values. Thus the infinite sign classification reduces to \(0\le a\le25\), \(1\le r\le s\le26-a\), except for the single negative boundary case \(a=0,r=1,s=26\), which is handled analytically next.

**4. Persistent positive-covariance boundary.** For \(a=0,r=1,s\ge2\),
\[
F(0,1,s)=p(s)-p(s+1)<0.
\]
Strict inequality holds because adding a part of size one injects partitions of \(s\) into those of \(s+1\), and the one-part partition \((s+1)\) is never in the image. This gives the persistent positive-covariance pair \((r,s)=(1,n-1)\) for every \(n=s+1\ge3\), including all \(s>26\).

**5. Complete finite certificate and its implication.** Use exact integer arithmetic, the generating-function recurrence \(\prod_{j\ge1}(1-z^j)^{-1}=\sum_{m\ge0}p(m)z^m\), and calculate \(F(a,r,s)\) for all \(0\le a\le25\), \(1\le r<s\le26-a\). There are exactly
\[
\sum_{R=1}^{26}\binom R2=2925
\]
such comparisons. The full signed finite table has \(2884\) positive \(F\) values, \(5\) zeros, and \(36\) negative \(F\) values. Exactly \(25\) of those \(36\) negative values are \(a=0,r=1,2\le s\le26\); the other eleven correspond precisely to the listed positive-covariance triples. The five zero values correspond precisely to the listed zero-covariance triples. The certificate also checks \(F(a,R,R)>0\) for all \(0\le a\le25\), and at the saturated distinct-coordinate boundary \(s=R\) only \(a=0,r=1\) has negative \(F\); no such boundary value is zero. Therefore extending beyond the finite box can create neither an additional negative defect nor an additional zero: the unique negative boundary trajectory was treated in Step 4. Every listed finite positive and zero triple is within the finite box, and no other exceptions exist. Together with Step 1 this proves the classification for all \(n,r,s\). \(\square\)

## Verification

The standalone accompanying `verify.py` regenerates \(p(0),\ldots,p(150)\) using exact integer arithmetic, checks the entire finite rectangle of \(2925\) off-diagonal comparisons, the \(26\) positive diagonal caps and \(325\) saturated-boundary comparisons, and independently tests \(562475\) complete covariance signs for \(2\le n\le150\). It separately enumerates all \(506\) integer partitions for sizes \(2\le n\le14\), testing the underlying joint-probability identity directly from partition objects. The arithmetic script's output records each successful comparison. All infinite-range statements follow analytically from the published log-concavity theorem and the finite boundary argument, not from finite extrapolation. Reproduce with `python3 verify.py`.

## Relationship to prior work

Corteel–Pittel–Savage–Wilf [1] studied the multiplicity of randomly selected part sizes and statistics of distinct part sizes of a uniform integer partition. Their accessible abstract gives asymptotic marginal sampling results, not the explicit two-prescribed-size sign classification, but their full article was not accessible for inspection; priority remains a risk. DeSalvo–Pak [2] proved the crucial strict log-concavity and stronger symmetric partition inequalities; those *do not state* the bivariate occurrence-sign diagram. The finite exceptions and unique persistent positive pair require the exact small-index classification and the propagation argument. Mutafchiev [3] treats the joint size/multiplicity of **one randomly sampled part**, not the two prescribed occurrence events; the paper's introduction, theorems, relevant generating-function statements and conclusion were inspected. Fristedt [4] addresses conditioning methods and asymptotic random partition structure, a possible broader theoretical antecedent. No claim is made that the one-part marginal identity or log-concavity theorem is new.

## Limitations

Only unrestricted uniform integer partitions and pairwise occurrence indicators are covered. The outcome is a sign classification, not a closed distribution for all occurrence vectors, nor a claim of multivariate negative association. Strict log-concavity for the tail is an external established theorem [2], not reproved here. An inaccessible plausible earlier paper [1] and broader classical random-partition literature leave a historical-priority risk; absence of a retrieved matching statement is not proof of worldwide novelty. No independent scientific audit is asserted.

## References

[1] S. Corteel, B. Pittel, C. D. Savage, H. S. Wilf, *On the multiplicity of parts in a random partition*, Random Structures & Algorithms 14 (1999), 185–197. First public date February 5, 1999. DOI: https://doi.org/10.1002/%28SICI%291098-2418%28199903%2914%3A2%3C185%3A%3AAID-RSA4%3E3.0.CO%3B2-F

[2] S. DeSalvo and I. Pak, *Log-Concavity of the Partition Function*, arXiv:1310.7982 (first submitted October 29, 2013), Theorems 1.1 and 5.1. https://arxiv.org/pdf/1310.7982

[3] L. Mutafchiev, *Sampling Parts of Random Integer Partitions: A Probabilistic and Asymptotic Analysis*, arXiv:1407.3639 (July 14, 2014). https://arxiv.org/pdf/1407.3639

[4] B. Fristedt, *The structure of random partitions of large integers*, Transactions of the AMS 337 (1993), 703–735, DOI: https://doi.org/10.1090/S0002-9947-1993-1094553-1
