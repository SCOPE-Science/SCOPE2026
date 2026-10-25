# Minimal absent subsequences of alternating binary words: an exact bivariate generating function

## Finding
For every integer \(m\geq1\), set \(w_m=(01)^m\). A **minimal absent subsequence** of \(w_m\) is a binary word that is not a scattered subsequence of \(w_m\), while each word obtained by deleting one character is a scattered subsequence. Let \(P_m(z)=\sum_{v\in\operatorname{MAS}(w_m)}z^{|v|}\). Then the complete length-refined enumeration is

\[
\boxed{\sum_{m\geq1}P_m(z)u^m
=\frac{uz^2\left(3+(z^2-2z)u+2z^3u^2\right)}{(1-zu)^2-z^4u^3}.}
\]

In particular, \(P_1(z)=3z^2\), \(P_2(z)=4z^3+z^4\), \(P_3(z)=5z^4+4z^5\), and for every \(m\geq4\),
\[
P_m(z)=2zP_{m-1}(z)-z^2P_{m-2}(z)+z^4P_{m-3}(z).
\]
The total counts, beginning at \(m=1\), are \(3,5,9,16,28,49,86,151,265,465,816,1432,\ldots\). The shortest absent subsequences have length \(m+1\), and exactly \(m+2\) minimal absents attain this length. Their total number grows exponentially: \(P_m(1)\sim c\lambda^m\), where \(\lambda\approx1.75487766624669\) is the unique positive real root of \(\lambda^3-2\lambda^2+\lambda-1=0\), and \(c\approx1.67873560259\).

There is also a complete intrinsic membership criterion. For any nonempty binary word \(v=v_1\cdots v_\ell\), put
\[
F(v)=\ell+\mathbf1_{\{v_1=1\}}+\#\{i\in\{1,\ldots,\ell-1\}:v_i=v_{i+1}\}.
\]
A word \(v\) is in \(\operatorname{MAS}(w_m)\) if and only if all of the following hold: \(\ell\geq2\); \(v\) does not begin with `01`; \(v\) has neither `010` nor `101` as a contiguous factor; and either \(F(v)=2m+1\), or \(F(v)=2m+2\) and the last two symbols of \(v\) are equal.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). Scattered subsequences preserve order but need not be contiguous. The words \(w_m\) are linear, not cyclic. Every occurrence of a minimal absent word is counted once as a *distinct word*, not once per embedding. Here \(m\) is any positive integer and \(z,u\) are formal variables. The two-variable identity is an identity in formal power series, so no convergence hypothesis is needed.

## Proof
**1. Greedy embedding.** Embed \(v\) greedily from left to right in the infinite alternating sequence \(010101\cdots\), indexed from position \(1\). If the first letter is \(0\), its first occurrence is at position \(1\); if it is \(1\), at position \(2\). Given one embedded letter, the next required letter is one position later if the letters differ, and two positions later if they agree. The final greedy position is therefore exactly \(F(v)\), and hence
\[
v\preceq w_m\quad\Longleftrightarrow\quad F(v)\leq2m.
\]

**2. Effects of one deletion.** For \(\ell\geq2\), deleting the first letter reduces \(F\) by \(0\) precisely when \(v\) begins with `01`, and by \(2\) otherwise. Deleting an interior letter reduces \(F\) by \(0\) precisely when the surrounding triple is `010` or `101`, and by \(2\) otherwise. Deleting the final letter reduces \(F\) by \(1\) when the final two symbols differ and by \(2\) when they agree. These identities follow by evaluating the initial indicator and the adjacent-equality terms in the displayed definition of \(F\). In particular, any single deletion reduces \(F\) by at most \(2\). A minimal absent word has \(F(v)>2m\) and all deletions have \(F\leq2m\), so \(F(v)\) can only be \(2m+1\) or \(2m+2\). The zero-decrease restrictions and the last-letter condition now yield precisely the membership criterion stated above, in both directions. No word of length one is absent from \(w_m\).

**3. Enumeration by runs.** Let \(t\) mark the weight \(F(v)\) and \(z\) mark length. A run of \(a\) identical letters contributes \(z^a t^{2a-1}\). Put
\[
X=zt,\qquad Y=\sum_{a\geq2}z^at^{2a-1}=\frac{z^2t^3}{1-zt^2}.
\]
The initial symbol \(1\) contributes one further factor \(t\). The conditions excluding an initial `01` and interior alternating triples mean that the initial run must have length at least two when it begins in \(0\), every *strictly interior* run must have length at least two, and the final run may be a singleton. A single-run word is required to have length at least two. Therefore the generating series \(C(t,z)\) for all such candidate words, without yet imposing a threshold on \(F\), is
\[
C=(1+t)Y+\frac{[Y+t(X+Y)](X+Y)}{1-Y}
=\frac{t^3z^2(t^2z+tz+t+2)}{1-zt^2-z^2t^3}.
\]
Among the same candidates, those whose final two letters agree have generating series
\[
E=(1+t)Y+\frac{[Y+t(X+Y)]Y}{1-Y}
=\frac{t^3z^2(t^2z+t+1)}{1-zt^2-z^2t^3}.
\]
Each candidate word has a unique decomposition into runs, so no word is counted twice. By step 2, the number of minimal absent words for \(w_m\) of each length is the coefficient of \(t^{2m+1}\) in \(C\) plus the coefficient of \(t^{2m+2}\) in \(E\).

**4. Extract odd and even weights.** Writing \(C_{\rm odd}(t,z)=[C(t,z)-C(-t,z)]/2\) and \(E_{\rm even}(t,z)=[E(t,z)+E(-t,z)]/2\), the previous paragraph yields
\[
t^2\sum_{m\geq1}P_m(z)t^{2m}
=tC_{\rm odd}(t,z)+E_{\rm even}(t,z).
\]
Substitution of the explicit rational expressions and collection of terms gives
\[
tC_{\rm odd}+E_{\rm even}=
\frac{t^4z^2\left(3+(z^2-2z)t^2+2z^3t^4\right)}{(1-zt^2)^2-z^4t^6}.
\]
Dividing by \(t^2\) and setting \(u=t^2\) proves the boxed bivariate identity. The recurrence follows by multiplying by its denominator and equating powers of \(u\).

**5. Shortest and asymptotic consequences.** Since \(w_m\) is a concatenation of \(m\) complete binary arches, it contains every word of length \(m\) as a subsequence; thus minimal absent words have length at least \(m+1\). The length-\(m+1\) absent words are exactly the \(m+2\) nonincreasing words \(1^a0^{m+1-a}\), for \(0\leq a\leq m+1\): they are absent by the greedy-position criterion, whereas any length-\(m+1\) binary word containing an adjacent `01` has greedy position at most \(2m\). Every such shortest absent word is minimal. Finally, setting \(z=1\) produces
\[
\sum_{m\geq1}P_m(1)u^m=\frac{3u-u^2+2u^3}{1-2u+u^2-u^3}.
\]
The denominator has one simple positive root \(\rho\approx0.569840290998053\), and its other two roots have larger absolute value. The numerator is nonzero at \(\rho\), so the unique dominant simple pole gives \(P_m(1)\sim c\rho^{-m}\), where \(c=-N(\rho)/(\rho Q'(\rho))\approx1.67873560259\), with \(N(u)=3u-u^2+2u^3\) and \(Q(u)=1-2u+u^2-u^3\).

## Verification
Run `python3 verify_mas.py` with Python 3 and no external dependencies. The script independently enumerates every binary candidate up to the maximum possible absent-word length for \(m=1,\ldots,8\), compares the direct subsequence definition with the closed structural criterion, and checks each length-refined coefficient against the rational-generating-function recurrence. It also separately verifies the greedy-position identity for \(m\leq6\) and the scalar totals through \(m=12\). The expected final line is `VERIFY_OK`. These finite checks test examples and boundary cases; the proof above, not the computations, establishes the result for all positive integers \(m\).

## Relationship to prior work
Kosche, Koß, Manea, and Siemer [1], especially Section 3 and Proposition 3.8, introduce a general minimal-absent-subsequence characterization and consider the repeated increasing-alphabet-block words \(B_k\), which specialize to alternating binary words when the alphabet has two letters. Their quantitative proposition assumes a larger even alphabet and supplies a broad asymptotic separation, not an exact binary length-refined enumeration. Manea, Ringleb, Siemer, and Winkler [2] develop optimal general enumeration algorithms, rather than a symbolic generating function for this periodic binary family. Adamson and collaborators [3] establish bounds for the number of *all absent subsequences of fixed length* as universality varies; that statistic is distinct from the minimal absent-subsequence distribution for a fixed word. The new claim is the stated explicit binary run criterion and bivariate identity, not the definition of minimality, the standard greedy matching algorithm, or the general existence of exponential growth.

## Limitations
The formulas are restricted to the fixed linear alternating binary family; they do not count minimal absent subsequences for arbitrary words or larger alphabets. The comparison with published literature cannot exclude equivalent work in unindexed sources or differently presented generating functions. The reproduction script verifies finite instances only; the rational identity is proved symbolically above. No independent scientific audit has been performed.

## References
[1] M. Kosche, T. Koß, F. Manea, and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first public 2021-08-31), https://arxiv.org/html/2108.13968v6.

[2] F. Manea, T. Ringleb, S. Siemer, and M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (first public 2025-04-30), https://arxiv.org/html/2504.21471v1.

[3] D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, and M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (first public 2024-07-26), https://arxiv.org/html/2407.18599v2.
