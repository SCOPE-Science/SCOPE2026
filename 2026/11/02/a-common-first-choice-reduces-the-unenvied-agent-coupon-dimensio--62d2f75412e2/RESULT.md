# A common first choice reduces the unenvied-agent coupon dimension by one

## Finding

Let \(n\ge 2\), and consider a square market with \(n\) students and \(n\) unit-capacity schools. Fix a school \(s\) and a set of \(r\) students, \(0\le r\le n\). Each designated student ranks \(s\) first and independently ranks the other \(n-1\) schools in a uniformly random strict order. Every undesignated student has an independent uniformly random strict ranking of all \(n\) schools. Run random serial dictatorship (RSD), independently choosing a uniformly random student priority order. Let \(X_{n,r}\) be the number of students whom **no other student envies**, where student \(j\) envies student \(i\) exactly when \(j\) strictly prefers \(i\)'s assigned school to their own. Let \(S_m\) be the number of singleton coupon types among independent uniform draws on \(m\) labels, stopped at the **first** draw by which every type has appeared.

**Theorem (common-favorite distributional reduction).** For all integers \(n\ge2\) and \(0\le r\le n\),
\[
X_{n,r}\ \overset{d}{=}\ \begin{cases}
S_n,&r\in\{0,1\},\\
S_{n-1},&2\le r\le n.
\end{cases}
\]
In particular, with \(H_m=\sum_{k=1}^{m}1/k\),
\[
\mathbb E[X_{n,r}]=\begin{cases}H_n,&r\in\{0,1\},\\H_{n-1}=H_n-1/n,&2\le r\le n.\end{cases}
\]
The entire law, not merely its mean, is independent of \(r\) once two students share the designated first choice. For \(m=n\) or \(m=n-1\), the exact mass function is the known coupon-singleton formula
\[
\Pr(S_m=j)=j\binom mj\int_0^\infty t^{j-1}(e^t-1-t)^{m-j}e^{-mt}\,dt,
\qquad 1\le j\le m.
\]
The integral formula and the identity \(\mathbb E[S_m]=H_m\) are due to Myers and Wilf; the contribution here is the complete correlated-RSD distributional reduction.

## Assumptions and scope

All rankings are complete and strict. Conditional on the designated set, student rankings are independent; the correlation refers to their shared deterministic top school. No school has a capacity exceeding one. The designated set and \(s\) are fixed ex ante and independent of the student priority. The result in fact holds conditional on any fixed priority order and any fixed assignment of the \(r\) designated students to positions in that priority, so the random-priority convention is not needed for its validity. Envy refers to students' own school preferences, not schools' priorities or justified envy. The statement makes no assertion about other preference-correlation laws, deferred acceptance under this modified model, or many-to-one admissions.

## Proof

**1. Realize rankings by raw draws.** Fix any student priority and write students in priority order. Give an undesignated student an independent infinite sequence of uniform school labels. Their strict ranking is the order of first occurrences in that sequence. Give a designated student the first raw draw \(s\), followed by an independent infinite sequence of uniform draws on the other \(n-1\) school labels; again retain first occurrences to construct the ranking. These constructions generate exactly the assumed independent ranking distributions. To implement RSD, when a student moves, inspect raw draws from their stream only until the **first** label not previously allocated, and assign that label. Repeats of already-allocated labels are read and ignored. No student's stream is read after they obtain a school.

**2. Unenvied schools are exactly raw singletons.** Concatenate every raw draw actually inspected during the RSD execution. The first occurrence of each school \(g\) is when \(g\) is allocated: until then \(g\) is available, so the first student encountering it immediately takes it. In the ranking of a later student, an earlier-allocated school \(g\) appears ahead of their assigned school if and only if it occurs among that student's inspected raw draws before their first available draw. The same statement holds for designated students, including their mandatory first draw of \(s\). Earlier students cannot envy later students, because they chose their own schools while the later students' eventual schools were still available. Therefore the recipient of \(g\) is unenvied if and only if \(g\) appears **exactly once** in the concatenated raw stream.

**3. No or one designated student.** For \(r=0\), all inspected raw draws are independent uniform labels on \(n\) schools, and RSD stops exactly on the first discovery of all labels. Step 2 identifies \(X_{n,0}\) with \(S_n\) pathwise. For \(r=1\), start with the \(r=0\) experiment and condition the designated student's first-ranked school to be \(s\). By invariance under simultaneous permutations of school names, the distribution of the number of unenvied students conditional on any possible top school is the same as its unconditional distribution. Conditional on that top school, the remaining order is uniform and independent of other students. Thus \(X_{n,1}\overset d=S_n\).

**4. At least two designated students.** For \(r\ge2\), the school \(s\) is allocated **no later than** the first designated student's mandatory draw of \(s\): an undesignated earlier student may have obtained it already. Every designated student inspects a mandatory first raw draw of \(s\), even if \(s\) was previously allocated. Hence \(s\) appears at least twice in the concatenated raw draws and is not a singleton. There is another designated student later than the first designated student, so at least one student remains to choose after \(s\) has been allocated. Consequently the last school allocated is not \(s\).

Delete every draw of \(s\) from the concatenated raw stream. The remaining labels, in order, are independent and uniform on the other \(n-1\) schools until the first appearance of every one of them. To see this precisely, expose the adaptive raw-draw process one draw at a time. After arbitrary revealed history, an undesignated student's next raw draw is uniform among all \(n\) labels; conditional on its being different from \(s\), it is uniform among the other labels. A designated student's draws after the mandatory \(s\) are directly uniform among the other labels. Independently generated fresh draws remain independent of all previously revealed identities. Thus the next observed **non-\(s\)** label, even when its source student is selected by preceding allocation history and intervening discarded draws of \(s\), is conditionally uniform on the \(n-1\) labels. Induction gives an independent uniform sequence of non-\(s\) labels.

Because \(s\) has already been allocated before the final selection, RSD terminates precisely when the final non-\(s\) label is first observed, with no additional raw draws. Deleting \(s\)-draws therefore yields the ordinary \((n-1)\)-type coupon process stopped upon its first full collection. All non-\(s\) multiplicities are preserved by deletion, and \(s\) was already non-singleton. By Step 2 the unenvied count consequently equals the singleton count of this reduced coupon process, proving \(X_{n,r}\overset d=S_{n-1}\).

**5. Distribution and expectation.** Apply the exact coupon-singleton distribution and harmonic-mean identity established by Myers and Wilf to the corresponding number of coupon types. The expected-value reduction from any \(r\ge2\), relative to \(r\le1\), is exactly \(1/n\); the full-law equality is stronger than this difference of means. This concludes the proof.

## Verification

The standalone `verify.py` performs an independent exact-rational check: for every \(n\in\{2,3,4\}\), every possible \(r\), every choice of the designated positions in a fixed student order, and every admissible tuple of complete strict rankings, it explicitly constructs RSD, counts unenvied students from pairwise ranking comparisons, and compares the resulting entire probability mass function with an independently computed absorbing-state coupon-singleton distribution. It verifies **810,521** complete profile/designation cases. No randomness or floating-point arithmetic enters this check. Reproduce with `python3 verify.py`; captured output is included in `verify_output.txt`.

For example, with \(n=4\) and at least two designated students, the probabilities for exactly \(1,2,3\) unenvied students are, respectively, \(7/18,7/18,2/9\), regardless of the number designated. With zero or one designated student, the corresponding \(n=4\) probabilities for \(1,2,3,4\) unenvied students are \(97/288,97/288,67/288,3/32\). These finite checks corroborate but do not replace the proof for all \(n\).

## Relationship to prior work

Ortega, Ziegler, Arribillaga and Zhao (2026), Proposition 3, show that under **independently uniform rankings** the expected number of students unenvied by anyone under RSD is \(H_n\), and explicitly ask about correlated preferences in their Discussion. Their Sections 2–4 do not provide the exact correlated common-favorite law here. An existing full-distribution coupon representation for completely independent uniform rankings also covers \(r=0\) but does not apply to \(r\ge2\), which violates its input assumptions. Myers and Wilf (2003/2006) established the singleton coupon mass function and expectation for a classical coupon stream, not the reduction from a correlated school-choice experiment to a smaller stream. Wang (2026) studies correlated Mallows rankings and two-sided stable matchings, not the ex-post envy count under RSD with a forced shared first choice. The new component is the coupling that removes a necessarily repeated shared school and leaves a pristine, stopped coupon stream of one lower dimension.

## Limitations

The result applies only to one fixed school shared as the certain top choice by a designated subset, with all remaining preferences independently uniform in the stated manner. It does not imply that any general correlated ranking model gives this law, nor that equivalent statements cannot appear in as-yet unindexed literature. The exact coupon integral and harmonic identity are established prior results rather than independently new formulas. The included finite enumeration checks only markets with at most four students; the unlimited theorem is established by the proof above. No independent external review has been conducted.

## References

1. Josué Ortega, Gabriel Ziegler, R. Pablo Arribillaga, and Geng Zhao, *The Distribution of Envy in Matching Markets*, arXiv:2603.23385v1, first posted 2026-03-24, https://arxiv.org/html/2603.23385v1 . In particular, Sections 2–4 and Proposition 3.
2. Amy N. Myers and Herbert S. Wilf, *Some New Aspects of the Coupon-Collector’s Problem*, arXiv:math/0304229v1, first posted 2003-04-16; later SIAM Review 48 (2006), 549–565. Section 4, formula (49) and the following harmonic-mean identity. https://arxiv.org/html/math/0304229v1 .
3. Bill Wang, *Random Matching Markets with Correlated Preferences*, arXiv:2603.24526v1, first posted 2026-03-25, https://arxiv.org/html/2603.24526v1 .
