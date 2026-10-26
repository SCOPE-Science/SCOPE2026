# A fixed-point pinning law for records of uniform random permutations

## Finding

Let \(\Pi\) be uniformly distributed on permutations of \(\{1,\ldots,n\}\), \(n\ge2\). Let \(R_n\) be its number of left-to-right **upper records**: position \(j\) is a record when \(\Pi(j)>\max_{k<j}\Pi(k)\), with the first position always a record. Let \(F_{n,i}=\mathbf1\{\Pi(i)=i\}\) be the fixed-point indicator at label \(i\). For a nonnegative integer \(k\), set \(t^{\overline k}=\prod_{j=0}^{k-1}(t+j)\), with \(t^{\overline0}=1\).

For every \(n\ge2\), every \(1\le i\le n\), and all complex \(t\), the complete conditional probability-generating polynomial is
\[
\boxed{\mathbb E[t^{R_n}\mid F_{n,i}=1]=\frac{t^{\overline{n-1}}+(t-1)t^{\overline{i-1}}t^{\overline{n-i}}}{(n-1)!}.}
\]

In particular the conditional distribution is invariant under reflecting the *conditioned fixed-point label*: \(R_n\mid\{\Pi(i)=i\}\) and \(R_n\mid\{\Pi(n+1-i)=n+1-i\}\) have identical laws. This symmetry is nonobvious for a one-directional record statistic.

Differentiating at \(t=1\) yields
\[
\mathbb E[R_n\mid F_{n,i}=1]=H_{n-1}+\binom{n-1}{i-1}^{-1},\qquad
\boxed{\operatorname{Cov}(F_{n,i},R_n)=\frac1{n\binom{n-1}{i-1}}-\frac1{n^2}.}
\]
Here \(H_k=\sum_{j=1}^k 1/j\). For **every** \(n\ge5\), the covariance is strictly positive at exactly the four labels \(i\in\{1,2,n-1,n\}\), and strictly negative for every \(3\le i\le n-2\). It is never zero for \(n\ge5\).

For total fixed-point count \(F_n=\sum_{i=1}^n F_{n,i}\), the many negative interior correlations do not determine the aggregate sign:
\[
\boxed{\operatorname{Cov}(F_n,R_n)=\frac1n\left(\sum_{k=0}^{n-1}\frac1{\binom{n-1}{k}}-1\right)>0,\qquad n\operatorname{Cov}(F_n,R_n)\longrightarrow1.}
\]

## Assumptions and scope

The permutation is uniform on all \(n!\) one-line permutations. Records refer to entries increasing past every earlier entry, not peaks, descents, lower records, or maxima in cycle notation. Fixing the label \(i\) means conditioning on the **event** \(\Pi(i)=i\); it does not mean conditioning on the total number of fixed points or on a cycle type. All expectations are finite. The generating-function identity is a polynomial identity over \(\mathbb C\), including \(t=0\) and \(t=1\). The sign partition is asserted only for \(n\ge5\); the displayed covariance and generating-function formulas remain valid for \(n=2,3,4\).

## Proof

**1. Pinned-point deletion.** Fix \(i\), set \(N=n-1\), \(m=i-1\), and condition on \(\Pi(i)=i\). Delete the entry at location \(i\), then standardize the remaining \(n-1\) entries to obtain a uniform \(\sigma\in S_N\). Let \(E\) be the event that the first \(m\) values of \(\sigma\) are precisely \(\{1,\ldots,m\}\). For \(m=0\) or \(m=N\), this is the certain event. In general, \(\Pr(E)=\binom Nm^{-1}\).

Insertion of value \(i\) in location \(i\) preserves each pre-existing record of \(\sigma\). Indeed, earlier than the insertion point, comparisons of the relative orders do not change. After insertion, the value \(i\) cannot suppress a later record: if any preceding value exceeds \(i\), the insertion is immaterial; otherwise all preceding nonfixed values are smaller than \(i\), forcing every nonfixed value available from the next location onward to exceed \(i\). The insertion itself is an upper record precisely on \(E\). Consequently, exactly, \(R_n=R_N(\sigma)+\mathbf1_E\).

**2. Joint generating polynomial.** A uniform permutation of \(k\) positions has independent upper-record indicators with respective probabilities \(1,1/2,\ldots,1/k\); thus its record-count probability generating polynomial is \(G_k(t)=t^{\overline k}/k!\), with \(G_0(t)=1\). Conditional on \(E\), the first \(m\) values and the remaining \(N-m\) values are independently uniformly permuted within their two separated value blocks, and every record of the second block is a record of the entire \(\sigma\). Therefore
\[
\mathbb E[t^{R_N}\mathbf1_E]=\binom Nm^{-1}G_m(t)G_{N-m}(t).
\]
Using \(t^{R_N+\mathbf1_E}=t^{R_N}+(t-1)t^{R_N}\mathbf1_E\), we obtain
\[
\mathbb E[t^{R_n}\mid F_{n,i}=1]=G_N(t)+(t-1)\binom Nm^{-1}G_m(t)G_{N-m}(t).
\]
The factorial identity \(\binom Nm^{-1}/(m!(N-m)!)=1/N!\) proves the displayed closed polynomial formula. Its product is symmetric in \(m\) and \(N-m\), establishing reflection of the pinned label at the level of the complete conditional law.

**3. Means and local covariance.** The derivative of \(G_N\) at \(1\) equals \(H_N\), and the correction contributes exactly \(\binom Nm^{-1}\), because the coefficient of \(t-1\) is a normalized generating polynomial with value \(1\) at \(t=1\). Independently \(\mathbb E R_n=H_n\), \(\Pr(F_{n,i}=1)=1/n\), so
\[
\operatorname{Cov}(F_{n,i},R_n)=\frac1n\left(H_{n-1}+\binom{n-1}{i-1}^{-1}-H_n\right)=\frac1{n\binom{n-1}{i-1}}-\frac1{n^2}.
\]

**4. Sharp four-label sign classification.** The covariance sign is the sign of \(n-\binom{n-1}{i-1}\). For \(n\ge5\), the two endpoint binomial coefficients equal \(1<n\), and the next-to-endpoint coefficients equal \(n-1<n\). For every interior index \(2\le i-1\le n-3\), binomial unimodality gives \(\binom{n-1}{i-1}\ge\binom{n-1}{2}=(n-1)(n-2)/2>n\). This proves strict signs and excludes zeros throughout the claimed domain.

**5. Aggregate sign and asymptotics.** Covariance is linear in its first argument. Summing the local formula over \(i\) gives the displayed expression for \(\operatorname{Cov}(F_n,R_n)\). The reciprocal-binomial sum exceeds \(2\) because its endpoint terms are both \(1\); hence the covariance is positive. Moreover, the two endpoint terms sum to \(2\); the next two terms sum to \(2/(n-1)\), and the remaining terms total \(O(n^{-1})\): each of the at most \(n-4\) remaining reciprocals is at most \(1/\binom{n-1}{2}=O(n^{-2})\). Hence the entire reciprocal-binomial sum tends to \(2\), and \(n\operatorname{Cov}(F_n,R_n)\to1\).

## Verification

The standalone standard-library Python verifier `verify.py` directly enumerates all \(n!\) permutations for every \(2\le n\le9\), obtains the distribution of record counts conditional on each individual fixed-point event without relying on the deletion proof, and compares every probability as an exact rational number with the generating-function formula. It separately checks means, reflection symmetry, and covariance; it also checks all sign classifications and the exact aggregate identity through \(n=400\). The replay of the verifier produced **161,280 passing assertions**. These finite checks supplement, and do not replace, the analytic argument for arbitrarily large \(n\).

Reproduce from this package with `python verify.py` using Python 3.9 or later; no nonstandard dependencies are required.

## Relationship to prior work

The classical independent record-indicator law establishes \(G_n(t)=t^{\overline n}/n!\) but not the conditional distribution at a prescribed permutation fixed point. Gnedin (2006) and Gnedin--Gorin (2012) investigate coherent record-dependent random permutations; their inspected constructions and classification concern record-driven laws rather than conditioning the uniform law on a fixed point at a specified position. Brändén--Claesson (2011) represent both left-to-right maxima and fixed points as mesh-pattern statistics, but their separate expansions do not give the pinned conditional generating polynomial or its exact four-label covariance sign split. Dubach (2024) investigates upper records in conjugacy-invariant permutations, including dependence on the **total** fixed-point count; the inspected asymptotic results are not an exact finite conditional law for a fixed-point **position**. None of the inspected material states or plainly subsumes the exact formula in this report. This is a literature-comparison assessment, not a proof of priority across all historical sources.

## Limitations

The result concerns one fixed-point event at a time and a uniform permutation. It does not claim independence of records and fixed points, describe simultaneous conditioning on several pinned points, or cover nonuniform random permutations. The sign classification is for \(n\ge5\). Historical priority remains subject to wider literature review, particularly older work on joint record/fixed-point enumeration and permutation pattern statistics.

## References

- A. Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538, first posted 2006-11-17. Full text examined for record-biased constructions and introductory results.
- P. Brändén and A. Claesson, *Mesh patterns and the expansion of permutation statistics as sums of permutation patterns*, arXiv:1102.4226, first posted 2011-02-21. Full text examined, including separate examples for left-to-right maxima and fixed points.
- A. Gnedin and V. Gorin, *Record-dependent measures on the symmetric groups*, arXiv:1202.3680, first posted 2012-02-16. Full text examined for record-dependent classification statements.
- V. Dubach, *A geometric approach to conjugation-invariant random permutations*, arXiv:2402.10116, first posted 2024-02-15. Open full HTML examined for record behavior under total fixed-point constraints; used as later supporting literature only.
