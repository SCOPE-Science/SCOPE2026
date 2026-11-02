# Exact fluctuations of two-deletion output counts over finite alphabets

## Finding

For every integer alphabet size \(q\ge 2\), every length \(n\ge 2\), and a uniformly random word \(W\in\{0,\ldots,q-1\}^{n}\), let \(B_2(W)\) count its **distinct** length-\(n-2\) subsequences obtained by deleting exactly two indexed symbols. Put \(m=n-1\), \(p=(q-1)/q\), and \(a=1/(q-1)\). Then

\[
\mathbb E B_2(W)=1+(m-1)p+\binom m2p^2,
\]
\[
\boxed{\operatorname{Var}(B_2(W))
= m(m-1)^2p^3(1-p)
+(m-1)\left(\frac{m-2}{2}+a^2\right)p^2(1-p)^2
+(m-1)a(1-a)p^2.}
\]
Equivalently the variance is
\[
\frac{(m-1)(q-1)}{2q^4}
\left[2m^2(q-1)^2-m(q-1)(2q-3)+2q(q-2)\right].
\]
In particular, for fixed \(q\), the variance is asymptotic to \((q-1)^3n^3/q^4\) as \(n\to\infty\). This includes the previously available binary formula \((n-1)(n-2)(2n-3)/32\), but the new result also determines the exact nonbinary fluctuations.

There is a stronger **conditional distribution law**. Define the adjacent-change indicators \(X_i={\bf1}_{\{W_i\ne W_{i+1}\}}\) for \(1\le i\le m\); set \(S=\sum_iX_i\), \(Q=\sum_{i=1}^{m-1}X_iX_{i+1}\), \(E=X_1+X_m\), and \(T=\sum_{i=1}^{m-1}{\bf1}_{\{W_i=W_{i+2}\ne W_{i+1}\}}\). Almost surely,
\[
B_2(W)=\binom{S+2}{2}-E-Q-T.
\]
Conditionally on the **entire** vector \((X_1,\ldots,X_m)\),
\[
\boxed{T\mid(X_1,\ldots,X_m)\ \sim\ \operatorname{Binomial}\left(Q,\frac1{q-1}\right).}
\]
This law is exact, not an asymptotic approximation; for \(q=2\), the binomial variable is deterministic.

## Assumptions and scope

The input letters are independent and uniformly distributed on an alphabet of arbitrary fixed cardinality \(q\ge2\); no field structure is required. All subsequences are indexed in their original linear order, but repeated deletion outputs are counted **once**. Deletions are performed at two distinct input positions, never in consecutive blocks by requirement. The formulas include \(n=2\), where there is one empty output and zero variance; the second-moment calculation and conditional law apply unchanged. No claim is made for nonuniform or dependent sources, more than two deletions, or Levenshtein balls involving insertions.

## Proof

**Step 1. A deterministic run identity.** Write an arbitrary nonempty word as \(r\) maximal constant-symbol runs. Let \(k\) be the number of runs of length at least two, and let \(t\) count interior singleton runs whose two neighboring runs carry the same symbol (an \(ABA\) configuration). We first show for every word of length at least two, over **every** finite alphabet,
\[
B_2(w)=\binom r2+k-t.\tag{1}
\]
This follows by induction using the exact disjoint-output decomposition with an intersection:
\[
D_2(wa)=\{ua:u\in D_2(w)\}\cup D_1(w),
\]
where \(D_j(w)\) is the set of distinct words from exactly \(j\) deletions. A word with \(r\) runs has \(|D_1(w)|=r\). Let \(b\) be the final letter of \(w\). If the appended \(a=b\), the intersection has size \(r-1\) when the last old run is a singleton, and \(r\) otherwise: its elements are precisely the one-deletion outputs of the prefix without its last symbol, followed by \(b\). Thus adding \(b\) increases \(B_2\) by one exactly when the last old run was a singleton. The run count stays fixed, \(k\) increases in exactly that case, and \(t\) is unchanged, establishing (1) inductively. If \(a\ne b\), the intersection consists of the single prefix \(w\) without its final symbol exactly when \(w\)'s penultimate symbol equals \(a\), and is empty otherwise. Hence \(B_2(wa)-B_2(w)=r-\mathbf1_{\{w_{|w|-1}=a\}}\). On the right of (1), appending \(a\) increases \(r\) by one, leaves \(k\) fixed and creates a new interior singleton \(ABA\) precisely under that same condition; the change matches. The base case \(|w|=2\) gives one deletion output of length zero. This proves (1), including overlapping chains of singleton runs rather than assuming their effects are disjoint.

Now \(r=S+1\). Counting non-singleton runs from the changes gives
\[
k=1-X_1+S-X_m-Q,
\]
and the above interior singleton \(ABA\) count is precisely \(t=T\). Substitution into (1) yields the claimed deterministic formula for \(B_2\).

**Step 2. Independent edge changes and the exact conditional binomial law.** Temporarily identify the symbols bijectively with the additive cyclic group \(\mathbb Z/q\mathbb Z\). The initial letter \(W_1\) and increments \(\Delta_i=W_{i+1}-W_i\) form independent uniform coordinates, because this change of variables is bijective. Consequently the indicators \(X_i=\mathbf1_{\{\Delta_i\ne0\}}\) are independent Bernoulli \(p\) variables. Conditional on their entire vector, the nonzero increments remain independent uniform elements of the \(q-1\) possible nonzero residues. Each counted \(ABA\) event at position \(i\) is exactly \(\Delta_i+\Delta_{i+1}=0\) with both increments nonzero.

The eligible pairs of increments form a subgraph of the path with vertices \(1,\ldots,m\) and edges \((i,i+1)\) precisely when \(X_i=X_{i+1}=1\). Every subset of these \(Q\) edges is a forest. On any chosen \(h\)-edge subset, satisfying all \(h\) inverse-increment constraints leaves exactly one free nonzero increment per tree component, hence has conditional probability \((q-1)^{-h}=a^h\). Since **every** subset of indicators has its expected product \(a^h\), the eligible \(ABA\) indicators are mutually independent conditional on the full transition vector, each with success probability \(a\). Thus \(T\mid X\sim\operatorname{Binomial}(Q,a)\), including the degenerate \(q=2\) case.

**Step 3. Moments and orthogonal expansion.** Conditional on \(X\), the mean and variance of \(B_2\) are
\[
\mu(X)=\binom{S+2}{2}-E-(1+a)Q,\qquad
v(X)=a(1-a)Q.
\]
The mean follows from \(\mathbb E S=mp\), \(\mathbb E Q=(m-1)p^2\), \(\mathbb E E=2p\), and the relation \(ap=1-p\).

For variance, write \(Z_i=X_i-p\), \(\sigma^2=p(1-p)\). Expanding \(\mu\) in independent centered variables and using \(ap=1-p\) gives the exact orthogonal decomposition
\[
\mu-\mathbb E\mu
= p(m-1)\sum_{i=1}^{m}Z_i
+\sum_{\substack{1\le i<j\le m\\j-i\ge2}}Z_iZ_j
-a\sum_{i=1}^{m-1}Z_iZ_{i+1}.
\]
Products of two different squarefree monomials above have zero expectation, since at least one centered independent factor appears only once. Consequently,
\[
\operatorname{Var}(\mu)
=m p^2(m-1)^2\sigma^2
+\left[\binom m2-(m-1)+(m-1)a^2\right]\sigma^4.
\]
The conditional variance adds \(\mathbb Ev(X)=a(1-a)(m-1)p^2\). Substitution of \(\sigma^2=p(1-p)\) proves both equivalent variance formulas for all parameters. No limiting approximations enter the argument.

## Verification

The accompanying standalone `verify.py` reproduces the formulas using Python's standard library. It directly generates every q-ary word for \(q=2\), \(2\le n\le10\); \(q=3\), \(2\le n\le8\); and \(q=4\), \(2\le n\le6\), checks its two-deletion output set, the independent run formula, exact rational first and second moments, and the full conditional binomial distribution for every transition vector. It also enumerates independent Bernoulli transition vectors using exact fractions for \(q\in\{2,3,4,5,7,11\}\) and \(1\le m\le12\). On execution it prints `VERIFY_OK` with the measured case counts. These finite checks are corroboration, not proofs of the infinite statements; Steps 1--3 are the proof.

## Relationship to prior work

Swart and Ferreira's 2003 run-based enumeration of **binary** two-deletion subsequences and Liron and Langberg's 2012 binary deletion characterization supply the direct structural antecedents. Their binary per-input enumeration is not claimed novel here. Bar-Lev, Etzion and Yaakobi (public preprint 2 March 2021) study the cardinalities and averages of **fixed-length Levenshtein radius-one balls**—a different insertion-and-deletion observation set. Wang and Wang subsequently study concentration of those radius-one balls. Abbasian, Mirmohseni and Nasiri Kenari (2024) analyze larger *mixed-error* balls, specifically channels with one deletion and two substitutions or insertions, and another with one insertion and one substitution; these are not pure two-deletion outputs. The published *Exact variance of binary two-deletion sphere size* establishes the \(q=2\) specialization of the displayed variance; that case is expressly **excluded from the novelty claim**. The new target is the nonbinary exact variance and the conditional \(ABA\)-return law for arbitrary alphabet size, which the inspected primary sources do not state. A per-word two-deletion formula by itself does not supply these moments or the conditional independence structure.

## Limitations

The claim assumes a uniform independent source, with \(q\) fixed but arbitrary, and makes no claims for variable-rate deletions or higher radii. The leading cubic variance coefficient is exact asymptotically but does not by itself imply a central limit theorem or sharp tail bounds. The result is a same-source mathematical derivation plus executable finite tests, not an independently certified theorem. As with any literature comparison, equivalent unindexed formulations cannot be ruled out conclusively, especially in sources treating higher deletion moments or general alphabet run statistics.

## References

- T. G. Swart and H. C. Ferreira, *A note on double insertion/deletion correcting codes*, IEEE Transactions on Information Theory **49** (2003), 269–273. DOI: https://doi.org/10.1109/TIT.2002.806155 . Full mathematical discussion of binary two-deletion cardinalities in Proposition 3.1.
- Y. Liron and M. Langberg, *A characterization of the number of subsequences obtained via the deletion channel*, arXiv:1202.1644 (2012), https://arxiv.org/abs/1202.1644 .
- D. Bar-Lev, T. Etzion and E. Yaakobi, *On Levenshtein Balls with Radius One*, arXiv:2103.01681v1, first public 2021-03-02, https://arxiv.org/abs/2103.01681 .
- G. Wang and Q. Wang, *On the size distribution of Levenshtein balls with radius one*, arXiv:2204.02201 (2022), https://arxiv.org/abs/2204.02201 .
- A. Abbasian, M. Mirmohseni and M. Nasiri Kenari, *On the Size of Error Ball in DNA Storage Channels*, arXiv:2410.15290 (2024), https://arxiv.org/abs/2410.15290 .
- *Exact variance of binary two-deletion sphere size*, published research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-variance-of-binary-two-deletion-sphere-size--6c9fe70986cc .
