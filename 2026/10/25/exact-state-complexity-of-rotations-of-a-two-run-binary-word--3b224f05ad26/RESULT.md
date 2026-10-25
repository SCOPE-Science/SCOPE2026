# Exact state complexity of rotations of a two-run binary word

## Finding
For integers \(a,b\geq1\), let \(n=a+b\) and let \(L_{a,b}\) consist of all cyclic rotations of the binary word \(0^a1^b\). The minimal **complete** deterministic finite automaton for \(L_{a,b}\) has exactly
\[
\operatorname{sc}(L_{a,b})=2ab+3
\]
states. More precisely, among the live Myhill–Nerode quotients reached after \(d\) symbols, the number is
\[
q_d=\begin{cases}1,&d=0\text{ or }d=n,\\2\min\{a,b,d,n-d\},&1\leq d<n.\end{cases}
\]
There is exactly one further quotient, the empty (dead) quotient. For fixed \(n\geq2\), the largest value in this family is \(\lfloor n^2/2\rfloor+3\), attained precisely by \(|a-b|\leq1\). Thus cyclic closure of a singleton language of state complexity \(n+2\) can require quadratically many states even for words with only two runs.

## Assumptions and scope
The alphabet is precisely \(\{0,1\}\); \(a,b\) are positive integers and all rotations have length \(n\). Every position of the original word supplies one rotation, and the two-run word is primitive, so there are exactly \(n\) distinct rotations. The state complexity uses a total transition function, including the rejecting sink. State counts are for this restricted singleton family, not worst-case bounds for arbitrary regular languages.

## Proof
Let \(\ell=n-d\). For every prefix \(p\) of length \(d\) of some rotation, write \(R(p)=\{s:ps\in L_{a,b}\}\). Each \(R(p)\) consists of words of length \(\ell\). Thus nonempty quotients reached at different depths cannot coincide, while all non-prefix inputs lead to the same empty quotient.

Fix \(1\leq d<n\). Call a binary word *pure* if all its letters are equal, and *mixed* otherwise. Every mixed proper contiguous circular factor of \(0^a1^b\) uniquely determines its starting position on the original circle: its first change of symbol locates one of the two run boundaries, and the distance to that change identifies the starting position. In particular, every mixed prefix \(p\) arises from exactly one rotation and has a singleton residual \(R(p)=\{s\}\). Likewise every mixed suffix \(s\) arises from exactly one rotation. Consequently the number of distinct singleton residuals arising from rotations with both mixed prefix and mixed suffix equals the number of such rotations.

Put \(P_c(d)=\max\{c-d+1,0\}\) for \(c\in\{a,b\}\). Exactly \(P_a(d)+P_b(d)\) rotations have a pure prefix of length \(d\): the starting point must lie sufficiently early in one of the two circular runs. Similarly, exactly \(P_a(\ell)+P_b(\ell)\) rotations have a pure suffix of length \(\ell\). A rotation has *both* a pure prefix and a pure suffix precisely when the cut lies at one of the two run boundaries; the number of these is \(B=\mathbf 1_{d=a}+\mathbf 1_{d=b}\). By inclusion–exclusion, the number of rotations with both parts mixed is
\[
M=n-P_a(d)-P_b(d)-P_a(\ell)-P_b(\ell)+B.
\]
Each such rotation contributes a distinct singleton residual, because its mixed suffix identifies its position.

Now examine the remaining quotients. Whenever \(d\leq c\) for a run length \(c\in\{a,b\}\), there is one pure prefix of the corresponding symbol; it contributes exactly one residual set. The two pure-prefix sets are distinct because their completion words have different counts of ones. If a pure-prefix set is a singleton, its unique completion is pure and occurs only at a run-boundary rotation; it cannot duplicate a mixed-prefix residual. Thus the number of pure-prefix residual sets is \(\mathbf1_{d\leq a}+\mathbf1_{d\leq b}\).

Whenever \(\ell\leq c\), the pure suffix of the corresponding symbol occurs. It contributes one singleton residual from a *mixed* prefix, except when the entire word is the boundary rotation comprising one pure prefix and one pure suffix. Such exceptions occur exactly \(B\) times. Different pure suffixes yield different singleton residuals, and none equals a singleton with mixed suffix. Therefore the number of additional quotients is
\[
\mathbf1_{\ell\leq a}+\mathbf1_{\ell\leq b}-B.
\]
Adding these three disjoint contributions gives
\[
\begin{aligned}
q_d&=n-\sum_{c\in\{a,b\}}\bigl(P_c(d)+P_c(\ell)\bigr)
+\sum_{c\in\{a,b\}}\bigl(\mathbf1_{d\leq c}+\mathbf1_{\ell\leq c}\bigr)\\
&=n-\sum_{c\in\{a,b\}}\bigl((c-d)_++(c-\ell)_+\bigr)\\
&=2\min\{a,b,d,\ell\},
\end{aligned}
\]
where \((x)_+=\max\{x,0\}\). For the final equality, assume by symmetry \(a\leq b\), and consider the three ranges \(d\leq a\), \(a\leq d\leq b\), and \(d\geq b\); the displayed quantity is respectively \(2d\), \(2a\), and \(2(n-d)\). These are exactly the distinct nonempty right languages at depth \(d\), so this is a Myhill–Nerode classification, not merely an upper bound.

At depths \(0\) and \(n\), the sole nonempty quotients are \(L_{a,b}\) and \(\{\varepsilon\}\), respectively. The empty quotient also occurs, for instance after reading any word longer than \(n\). Finally, for \(a\leq b\),
\[
\sum_{d=1}^{n-1}\min\{a,b,d,n-d\}=ab,
\]
as is seen from the rising sequence \(1,\ldots,a\), the central plateau, and the reversed sequence. Consequently the number of states is \(1+1+1+2ab=2ab+3\). The extremum for fixed \(n\) follows from \(ab\leq\lfloor n^2/4\rfloor\), with equality precisely for the closest possible pair of positive integers.

## Verification
The included standalone script `verify.py` generates every rotation of every word \(0^a1^b\) for \(1\leq a,b\leq24\), constructs all distinct residual languages directly, and checks both the depth-by-depth quotient formula and the total \(2ab+3\). It reports `VERIFY_OK pairs=576 lengths=2..48 all_depth_residuals=checked`. This bounded test is independent confirmation of the finite instances; the preceding argument proves the result for all positive integers.

Run from the same directory using `python3 verify.py` with Python 3 standard library only.

## Relationship to prior work
Jirásková and Okhotin (2008, first circulated earlier) developed general state-complexity results for the cyclic-shift operation, including exponential/superexponential worst-case phenomena and NFA bounds. That general operation and its constructions are prior work; no claim of discovering cyclic shift is made here. Their inspected discussion, automaton construction, and computational sections do not give the stated exact Myhill–Nerode profile for a two-run singleton. DiMuro (2019) studied rotationally closed fixed-length languages and greedy universal cycles; his paper concerns universal-cycle constructions rather than recognizing such a language with a minimal DFA. This result concerns the precise quotient profile of one natural rotationally closed family. It is not implied by the published general worst-case bounds without additional analysis.

## Limitations
The result treats exactly two nonempty constant runs over a binary alphabet, not words with more runs or languages containing several independent necklaces. The originality assessment is literature-relative; an equivalent statement may appear in less-indexed work, course notes, or implicit special-case computations. Independent validation has not been performed.

## References
1. G. Jirásková and A. Okhotin, *State Complexity of Cyclic Shift*, RAIRO-Theoretical Informatics and Applications 42 (2008), 335–360. DOI: 10.1051/ita:2007038. Full text: https://www.numdam.org/article/ITA_2008__42_2_335_0.pdf
2. J. DiMuro, *Classifying Rotationally-Closed Languages Having Greedy Universal Cycles*, Electronic Journal of Combinatorics 26(1) (2019), P1.35. DOI: 10.37236/7932. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i1p35/pdf/
