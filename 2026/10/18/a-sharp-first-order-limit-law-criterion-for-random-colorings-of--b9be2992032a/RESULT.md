# A sharp first-order limit-law criterion for random colorings of equal-block equivalence structures

## Finding

Let \(s_n\) and \(c_n\) be arbitrary sequences of positive integers tending to infinity. On a set of \(c_ns_n\) elements, fix an equivalence relation \(E\) with exactly \(c_n\) equivalence classes, each of size \(s_n\). Form a random expansion \(\mathcal M_n=(E,P)\) by independently placing each element in the unary predicate \(P\) with probability \(1/2\). There are no other symbols in the signature.

For every fixed integer \(j\geq0\), define
\[
\lambda_{n,j}=c_n2^{-s_n}\binom{s_n}{j},
\]
with the binomial coefficient interpreted as zero if \(j>s_n\). The following conditions are equivalent:

1. For every first-order sentence \(\varphi\) in the signature \(\{E,P\}\), the probability \(\Pr(\mathcal M_n\models\varphi)\) converges.
2. For every fixed \(j\geq0\), the sequence \(\lambda_{n,j}\) converges in the extended nonnegative real interval \([0,+\infty]\).

When the conditions hold, write \(\lambda_j=\lim_n\lambda_{n,j}\). For any finite collection of indices \(j\) with \(\lambda_j<\infty\), the counts of equivalence classes containing exactly \(j\) elements of \(P\), and separately exactly \(j\) elements outside \(P\), converge **jointly** to independent Poisson random variables of respective means \(\lambda_j\) (zero means give deterministic zeros). Categories with \(\lambda_j=+\infty\) contain arbitrarily many classes with probability tending to one. The same holds for classes containing at least \(q\) elements of each color, for each fixed \(q\).

Moreover, the resulting first-order limit law is a **zero-one law exactly when every** \(\lambda_j\) **is either** \(0\) **or** \(+\infty\). At most one index can have a finite positive limit.

## Assumptions and scope

Both the equivalence-class size \(s_n\) and the number of classes \(c_n\) tend to infinity. The equivalence relation is deterministic; randomness is only the independent fair unary coloring. All convergence is as \(n\to\infty\), every index \(j\) and every sentence being fixed independently of \(n\). The signature consists solely of equality, \(E\), and \(P\). There are no parameters or auxiliary orders. The result classifies convergence of **all first-order sentence probabilities**, not convergence of arbitrary infinitary logical properties.

## Proof

**1. Distinguishing sentences force convergence of the thresholds.** For every fixed \(j\geq0\), there is a first-order sentence \(\theta_j\) asserting that some \(E\)-class has exactly \(j\) elements satisfying \(P\). For \(j=0\), one can use \(\exists x\,\forall z(E(x,z)\to\neg P(z))\). For positive \(j\), existentially choose \(j\) pairwise different \(P\)-elements equivalent to \(x\), then universally assert that every \(P\)-element equivalent to \(x\) is one of those witnesses. Within one class the number of \(P\)-elements is \(\operatorname{Bin}(s_n,1/2)\). Consequently, with \(p_{n,j}=2^{-s_n}\binom{s_n}{j}\),
\[
\Pr(\mathcal M_n\models\theta_j)=1-(1-p_{n,j})^{c_n}.
\]
For each fixed \(j\), \(p_{n,j}\to0\). Uniformly in positive integers \(c_n\), the difference between \((1-p_{n,j})^{c_n}\) and \(\exp(-c_np_{n,j})\) tends to zero: for example, sandwich the former between \(\exp(-c_np_{n,j}/(1-p_{n,j}))\) and \(\exp(-c_np_{n,j})\), and maximize their difference over nonnegative \(c_np_{n,j}\) to obtain a bound tending to zero. Thus the sentence probability converges if and only if \(\lambda_{n,j}\) has a limit in \([0,+\infty]\), because \(t\mapsto1-e^{-t}\) is a homeomorphism of the extended interval onto \([0,1]\). This proves necessity.

**2. A finite-rank semantic normal form.** Fix an integer \(q\ge1\). To each equivalence class \(C\), assign the profile
\[
\pi_q(C)=\bigl(\min(q,|C\cap P|),\ \min(q,|C\setminus P|)\bigr).
\]
For each possible profile \(\pi\), count its classes, truncating that count at \(q\). Two finite colored equivalence structures with the same resulting data satisfy exactly the same first-order sentences of quantifier rank at most \(q\). Indeed, the duplicator wins the \(q\)-round Ehrenfeucht--Fraïssé game: previously visited classes are paired with their color profiles preserved, and there are fewer than \(q\) previously selected elements, hence fewer than \(q\) occupied classes. A new class of a given profile has a fresh partner because the number of such classes is either equal below \(q\), or at least \(q\) on both sides. Within paired classes, a requested unused element of a given color can be matched because either both available populations have the same size below \(q\), or each has at least \(q\) elements and fewer than \(q\) have been used. Equality, \(E\), and \(P\) are preserved after every move. This proves the claimed sufficiency of the finite data for rank \(q\).

**3. Limit of the finite-rank data.** Once \(s_n\ge2q\), the only possible class profiles are \((j,q)\) and \((q,j)\) for \(0\le j<q\), and \((q,q)\). Each rare category has probability exactly \(p_{n,j}\), and the categories are pairwise disjoint inside a class. Since \(s_n\to\infty\), the typical category \((q,q)\) has probability tending to one. Because classes are independently colored, all category counts have a multinomial distribution with \(c_n\) trials. For the finitely many categories with \(\lambda_j<\infty\), the joint probability generating function (or multinomial factorial moments) converges to that of independent Poisson variables with corresponding means. Any category whose expected count \(\lambda_{n,j}\to\infty\) has variance at most its expectation; Chebyshev's inequality shows that its count tends to infinity in probability. The typical class count also tends to infinity in probability because its expectation is asymptotic to \(c_n\). Consequently, the finite vector of doubly truncated class-profile counts converges in distribution. By step 2, the probability of each sentence of quantifier rank \(q\) converges. Every first-order sentence has finite quantifier rank, proving sufficiency.

**4. Exact zero-one boundary.** If every \(\lambda_j\) equals zero or infinity, the finite-rank count vector tends in probability to a deterministic value for each \(q\), so every sentence probability tends to zero or one. If any \(0<\lambda_j<\infty\), the sentence \(\theta_j\) has limit \(1-e^{-\lambda_j}\), strictly between zero and one. Finally,
\[
\frac{\lambda_{n,j+1}}{\lambda_{n,j}}=\frac{s_n-j}{j+1}\longrightarrow+\infty
\]
for each fixed \(j\) and all sufficiently large \(n\). Two distinct indices cannot both have finite positive limiting means. This completes the proof.

**5. Distinct regimes with the same uncolored limit.** For fixed \(j\ge0\) and \(\alpha>0\), set \(s_n=n\) and \(c_n=\lfloor \alpha\,2^n/\binom n j\rfloor\) whenever \(n>j\) (assign arbitrary positive values for the finitely many earlier indices). Then \(\lambda_j=\alpha\); earlier thresholds vanish and later thresholds diverge. If \(s_n=n\) and \(c_n=n\), all thresholds vanish. If \(s_n=n\) and \(c_n=2^{2n}\), all diverge. If \(s_n=n\) and \(c_n=2^n\) for even \(n\) but \(c_n=2^{n+1}\) for odd \(n\), \(\theta_0\) has two different subsequential limiting probabilities and no first-order convergence law exists. Nonetheless, in all four constructions the uncolored \(E\)-reducts have the same eventual first-order theory: infinitely many infinite equivalence classes. This follows by the uncolored version of the finite-rank game in step 2.

## Verification

An independent exact finite enumerator for class sizes and numbers of classes up to nine underlying elements confirms the probability identity for every possible exact color count, and the full multinomial profile distribution. A separate calculation confirms the adjacent-mean identity and the critical one-sided limiting probability numerically. Run \(\texttt{python3 verify.py}\) to reproduce the check with only the Python standard library; expected output: \(\texttt{EQUIVALENCE_COLOR_LIMIT_LAW_VERIFY_OK}\). The general limit-law equivalence is proved by the game argument and probability limits above, not by finite enumeration.

## Relationship to prior work

Koponen's 2026 work studies structural criteria enabling logical convergence for random expansions of finite base structures, including Example 2.12 and Remark 2.15. It does not derive the specific full first-order convergence criterion for independently two-colored equal-size equivalence classes. Kruckman's results on generic theories of equivalence relations and pseudofiniteness address different structural limit questions. The Ehrenfeucht--Fraïssé method, multinomial-to-Poisson limit and first-order zero-one laws are established techniques; the claimed new contribution is their **exact necessary-and-sufficient synthesis**, including the critical threshold and explicit nonconvergent expansions on a fixed limiting base theory.

## Limitations

The theorem requires growing class size, growing class count, identical deterministic block sizes, and fair independent element colors. No claim is made for dependent colorings, biased probabilities, heterogeneous blocks, extra binary relations, infinitary logic, or arbitrary prescribed finite structures. Historical priority is not certified: an older theorem on random colored partitions or generalized unary-expansion limit laws might imply this special classification. The program only checks finite computations; it does not cover the all-size proof.

## References

1. Vera Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1, initially public 12 October 2026. https://arxiv.org/html/2610.16163v1 . Relevant material: Introduction, Example 2.12, Remark 2.15, Theorem 3.1.
2. Alexander Kruckman, *Disjoint \(n\)-amalgamation and pseudofinite countably categorical theories*, arXiv:1510.03539 (2015). https://arxiv.org/abs/1510.03539 . Background on generic equivalence theories, not a statement of the present random-color threshold theorem.
3. Alexander Kruckman, *Infinitary Limits of Finite Structures*, PhD thesis (2015), Chapter 5.4, https://escholarship.org/uc/item/2057n08h . Context on generic theories of equivalence relations; full section not independently checked here.
