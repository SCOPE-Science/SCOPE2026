# Congruence profiles and exponential asymptotics for associative quasitrivial operations

## Finding
For every integer \(n\ge1\), consider the labeled associative quasitrivial binary operations \(S\) on \([n]\): \(x*y\in\{x,y\}\) for all \(x,y\). A semigroup congruence is an equivalence relation \(\theta\) respected by multiplication on both sides. Write \(c_S(z)=\sum_{\theta\in\operatorname{Con}(S)}z^{|S/\theta|}\), and denote by \(B_s(z)=\sum_{j=1}^{s}\left\{\begin{smallmatrix}s\\j\end{smallmatrix}\right\}z^j\) the Bell polynomial, for \(s\ge1\).

Every such operation has a unique ordered partition of its underlying set into weak-order levels \(L_1<\cdots<L_m\), with each level a left-zero or right-zero band. A singleton level has only one orientation. **A two-sided congruence consists of a partition of the ordered level sequence into consecutive intervals:** every interval containing at least two levels is collapsed to one congruence class; on any singleton-level interval \(\{i\}\), an arbitrary set partition of \(L_i\) is allowed. In particular,
\[
c_S(z)=\sum_{\mathcal I}\prod_{I\in\mathcal I}w_I(z),\qquad
w_I(z)=\begin{cases}B_{|L_i|}(z),&I=\{i\},\\z,&|I|\ge2,\end{cases}
\]
where \(\mathcal I\) ranges over consecutive-interval partitions of \([m]\).

The following **bivariate exponential generating function**, jointly recording the number of labeled operations and the quotient class count of all their congruences, holds as a formal power series:
\[
\begin{aligned}
H(x,z)&=1+\sum_{n\ge1}\frac{x^n}{n!}\sum_{S}c_S(z)
=\frac{1}{1-U(x,z)-zB(x)^2/(1-B(x))},\\
B(x)&=2e^x-2-x,\\
U(x,z)&=2\exp\!\bigl(z(e^x-1)\bigr)-2-zx.
\end{aligned}
\]
(The constant \(1\) records the empty combinatorial object; no empty semigroup is assumed.) The numbers of pairs \((S,\theta)\), for \(n=1,2,3,4,5,6,7,8,9\), are respectively \(1,8,70,846,12784,232238,4923734,119325224,3253497786\).

There is an explicit sharp asymptotic for the mean number of congruences. Let \(\rho\) be the unique positive root of \(B(\rho)=1\), and let \(\sigma\in(0,\rho)\) be the unique positive root of
\[
J(\sigma)=1,\qquad J(x)=2\exp(e^x-1)-2-x+\frac{B(x)^2}{1-B(x)}.
\]
Then the total number of pairs is asymptotic to \(n!\sigma^{-n}/(\sigma J'(\sigma))\), and the **mean** number of two-sided congruences of a uniformly chosen labeled associative quasitrivial operation satisfies
\[
\frac{\sum_S|\operatorname{Con}(S)|}{\#\{S\}}\sim
\frac{\rho B'(\rho)}{\sigma J'(\sigma)}
\left(\frac{\rho}{\sigma}\right)^n
\approx 0.627900141295\,(1.766516095507)^n.
\]
Numerically \(\rho\approx0.583073876037\) and \(\sigma\approx0.330069948142\).

## Assumptions and scope
Only finite nonempty sets and associative binary operations with the quasitriviality property are considered. Labeled objects are counted without quotienting by isomorphism. Each semigroup congruence is an **equivalence relation on its underlying set**, not a general relation, left congruence, or right congruence. Coefficients of \(z^r\) count quotient sets with exactly \(r\) classes, including the universal and equality congruences. All generating-function and asymptotic assertions are exact for the stated labeled model; the asymptotic takes \(n\to\infty\) through positive integers.

## Proof
**Weak-order normal form.** By the established structural classification of associative quasitrivial operations [1,2], there is a unique total preorder with ordered nonempty equivalence classes \(L_1<\cdots<L_m\). Products across different levels return the element from the higher level. Within \(L_i\), the operation is \(x*y=x\) (left-zero) or \(x*y=y\) (right-zero). Choices agree on singleton levels. Conversely every such orientation-decorated ordered partition gives one associative quasitrivial operation.

**Necessity of the interval rule.** Suppose \(x\in L_i\), \(y\in L_j\), \(i<j\), and \(x\equiv_\theta y\). For every \(t\in L_i\), either \(x*t=x\) (left-zero case) or \(x*t=t\) (right-zero case). In the first case \(t*x=t\), \(t*y=y\) proves \(t\equiv_\theta y\); in the second, \(x*t=t\), \(y*t=y\) proves the same. Thus the entire lower level joins the class. Similarly, for \(t\in L_j\), either \(y*t=y\) or \(t*y=y\); comparing respectively with \(x*t=t\) or \(t*x=t\) proves \(t\equiv_\theta y\). Hence the entire upper level joins. For every intermediate level \(i<k<j\) and \(t\in L_k\), \(x*t=t\), while \(y*t=y\), proving \(t\equiv_\theta y\). Therefore every congruence class meeting two levels includes **all elements of every intervening level**. Classes confined to an individual level may partition that level arbitrarily, because a left-zero or right-zero band admits every equivalence relation as a congruence. Two distinct multislice classes cannot overlap in levels, and they partition the chain into consecutive runs.

**Sufficiency.** Given a chain of consecutive runs, collapse each run of length at least two into one class and choose any partition of each singleton-level run. A product with an external level always selects the higher-level factor and therefore preserves these classes under replacing a factor by another in its class. A product between elements of the same level selects the left or right factor and also preserves every chosen partition. If one factor lies in a multislice run, its products with all elements inside that run remain in that run, and products with elements outside depend only on the order of the runs. These checks establish compatibility on both sides. Thus the construction is bijective and gives \(c_S(z)\).

**Species enumeration.** An oriented nonempty weak-order level of size \(s\) has multiplicity \(w_1=1\) for \(s=1\) and \(w_s=2\) for \(s\ge2\); its EGF is \(B(x)=x+2(e^x-1-x)\). Each singleton-level congruence run carries an arbitrary set partition. The EGF for partitions of a nonempty labeled set with \(z\) per part is \(\exp(z(e^x-1))-1\); correcting the singleton orientation gives \(U(x,z)=2(\exp(z(e^x-1))-1)-zx\). A collapsed multislice run is an **ordered sequence of at least two oriented levels**, of EGF \(z\sum_{\ell\ge2}B(x)^\ell=zB(x)^2/(1-B(x))\). An entire congruence-decorated semigroup is a **sequence of these runs**. The labeled sequence construction proves the expression for \(H\). Its coefficients are finite integer counts since every underlying nonempty block has positive size.

**Exponential asymptotics.** At \(z=1\), the denominator is \(1-J(x)\). The series \(B(x)\) has positive coefficients in every positive degree and is strictly increasing for \(x>0\), so \(\rho\) is unique and positive. The function \(J\) has nonnegative coefficients, positive coefficients in degrees one and two, is increasing on \((0,\rho)\), satisfies \(J(0)=0\), and diverges to infinity as \(x\uparrow\rho\). Hence it has a unique \(\sigma\in(0,\rho)\) with \(J(\sigma)=1\), and \(J'(\sigma)>0\). For \(|x|\le\sigma\), coefficient positivity gives \(|J(x)|\le J(|x|)\le1\), with strict inequality except at \(x=\sigma\): equality on the boundary requires all consecutive positive-degree monomials to have one common argument. Therefore \(1-J\) has a unique simple zero on this circle. Analyticity in a neighborhood of the closed disc, with no other zeros sufficiently near it, gives a simple-pole transfer,
\[
[x^n]\frac1{1-J(x)}\sim\frac{\sigma^{-n}}{\sigma J'(\sigma)}.
\]
The same argument applied to \(1/(1-B(x))\) yields \(\#\{S\}\sim n!\rho^{-n}/(\rho B'(\rho))\); taking the ratio proves the mean formula. This uses analytic properties of the displayed EGFs, not any inference from finite enumerations.

## Verification
Independent executable checks are supplied in `checks/quasitrivial_checker.py`, `checks/quasitrivial_exhaustive.py`, and `checks/quasitrivial_bivariate.py`. The first enumerates all oriented ordered-partition operations for \(1\le n\le4\), determines their congruence partitions by direct multiplication tests, and compares the resulting coefficient profiles with the interval formula. The second exhaustively enumerates **every** labeled quasitrivial operation for \(1\le n\le4\), tests associativity and each congruence directly, independently of the normal form. The third evaluates the bivariate labeled recurrence through degree nine using integer Stirling-number arithmetic and checks the pair counts. They returned `CHECKER_OK`, `EXHAUSTIVE_OK`, and `BIVARIATE_OK`, respectively. Finite verification does not replace the all-degree proof or analytic asymptotics.

## Relationship to prior work
Couceiro–Devillet–Marichal [1] established the unique weak-order representation and the labeled operation generating function; the present work uses these facts rather than claiming them anew. Devillet–Marichal–Teheux [2] further study quasitrivial semigroup classification, counts, and asymptotics **without a compatible two-sided congruence as the second labeled object**. The general algorithmic work of Anagnostopoulou-Merkouri–Cirpons–Mitchell–Tsalakou [3] enumerates finite-index congruences in finitely presented semigroups but does not give this normal form or the bivariate quasitrivial EGF. The finite structural lemma may be recognized as a specialization of more general band-semigroup congruence theory, and the contribution claimed here is the explicit entire congruence-size census and its mean asymptotic. A differently formulated equivalent formula cannot be excluded without a wider literature audit.

## Limitations
The result applies only to finite labeled associative quasitrivial semigroups and to equivalence congruences compatible on both sides. The arithmetic enumerates congruence **relations**, not isomorphism types of quotients or congruence lattices up to isomorphism. The cited literature comparisons support a best-knowledge originality assessment, not a theorem of absolute novelty. The asymptotic is for the uniform labeled-operation distribution and does not describe uniform isomorphism classes. No independent external validation or certification is asserted.

## References
[1] M. Couceiro, J. Devillet, and J.-L. Marichal, *Quasitrivial semigroups: characterizations and enumerations*, arXiv:1709.09162v1 (first public 2017-09-26), https://arxiv.org/abs/1709.09162.

[2] J. Devillet, J.-L. Marichal, and B. Teheux, *Classifications of quasitrivial semigroups*, arXiv:1811.11113v1 (2018), https://arxiv.org/abs/1811.11113.

[3] M. Anagnostopoulou-Merkouri, R. Cirpons, J. D. Mitchell, and M. Tsalakou, *Computing finite index congruences of finitely presented semigroups and monoids*, arXiv:2302.06295v1 (2023), https://arxiv.org/abs/2302.06295.
