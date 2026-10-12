# Exact all-arity product fibers of rank-one idempotents over finite fields
## Finding
Let \(q\) be any prime power, let \(n\ge2\), and let \(r\ge1\) be integers. Write
\[
\mathcal P_{n,q}=\{P\in M_n(\mathbb F_q):P^2=P,\ \operatorname{rank}P=1\}.
\]
For each prescribed \(B\in M_n(\mathbb F_q)\), let \(\nu_r(B)\) be the number of ordered \(r\)-tuples \((P_1,\ldots,P_r)\in\mathcal P_{n,q}^r\) whose product \(P_1\cdots P_r\) equals \(B\). Set
\[
H=q^{n-1},\quad N=q^n-1,\quad g=q-1,\quad
m=\frac{HN}{g},\quad k=r-1,
\]
\[
a=q^{(2n-2)k},\qquad b=q^{(n-2)k},\qquad c=q^{(n-1)k}.
\]
Then the **complete prescribed-product distribution** is
\[
\boxed{\nu_r(B)=
\begin{cases}
m^r-ma,&B=0,\\[2mm]
\displaystyle\frac{H(a-b)}{N}+\frac{\mathbf1_{\{\operatorname{tr}B\ne0\}}(b-c)}{g}
+\mathbf1_{\{\operatorname{tr}B=1\}}c,&\operatorname{rank}B=1,\\[3mm]
0,&\operatorname{rank}B>1.
\end{cases}}
\]
In particular, the nonzero rank-one fibers depend only on whether the target trace is zero, one, or another nonzero element; the third class is empty when \(q=2\). The count of rank-one idempotents is \(m\). The formula is valid in all characteristics, over nonprime fields, for arbitrarily long products and for \(r=1\), with no asymptotic approximation.

## Assumptions and scope
Factors are **nonzero rank-one idempotents**, not arbitrary idempotents, and tuples are **ordered**. All products are taken in the full matrix algebra over \(\mathbb F_q\); \(\mathbf1_{\{\cdot\}}\) is the indicator of the displayed condition. The quotient expressions are integers because they count finite sets. For \(r=1\), the formula gives one factorization at each rank-one idempotent and zero at all other targets. For every \(r\ge2\), every rank-one target has a positive number of factorizations; products of any length have rank at most one. Positivity at \(r=2\) follows directly from the formula (the smallest fiber is \(q^{n-2}(q^{n-1}-1)>0\)), and inserting a duplicate final idempotent preserves any nonzero product at every greater length.

The formula also determines the exact zero-product probability for uniformly and independently chosen factors:
\[
\Pr(P_1\cdots P_r=0)
=1-\left(\frac{q^{2n-2}}{m}\right)^{r-1}.
\]
Conditioned on a nonzero product, the distribution tends to the uniform distribution on all nonzero rank-one matrices as \(r\to\infty\); its exact deviation is given by the two correction terms in the boxed formula, with exponential eigenvalue ratios \(q^{-n(r-1)}\) and \(q^{-(n-1)(r-1)}\). Thus the all-arity census includes a finite-time nonzero survival law and explicit spectral mixing behavior.

## Proof
1. **Normal form and first factor.** Every nonzero rank-one matrix is \(u\beta\), with \(u\in\mathbb F_q^n\setminus\{0\}\) a column and \(\beta\in(\mathbb F_q^n)^*\setminus\{0\}\) a row form. Its trace is \(\beta(u)\). It is idempotent exactly when \(\beta(u)=1\). For each one-dimensional image \(\langle u\rangle\), fixing a nonzero \(u\) gives exactly \(H=q^{n-1}\) idempotents \(u\alpha\), where \(\alpha(u)=1\). There are \(N/g\) possible images, hence \(|\mathcal P_{n,q}|=m=HN/g\).

2. **A transition-counting lemma.** Fix \(u\ne0\), and take nonzero forms \(\alpha,\beta\). The number of rank-one idempotents \(Q\) satisfying
\[
(u\alpha)Q=u\beta
\]
is exactly the number of vectors \(v\) with \(\alpha(v)=\beta(v)=1\). Indeed, write \(Q=v\delta\), normalize its nonzero column so that \(\alpha(v)=1\) (which is possible whenever the product is nonzero), and the product condition forces \(\delta=\beta\), while idempotency forces \(\beta(v)=1\). Conversely each such \(v\) defines the unique permitted \(Q=v\beta\). The count is therefore \(H\) if \(\alpha=\beta\), zero if they are distinct proportional forms, and \(q^{n-2}\) if linearly independent. This lemma includes characteristic two and \(n=2\).

3. **Diagonalization of the finite transition matrix.** Index rows and columns by the \(N=q^n-1\) nonzero forms, and let \(T_{\alpha\beta}\) be the transition count in step 2. Let \(J\) be the all-ones matrix and \(E\) be the \(0/1\) equivalence matrix for the classes of nonzero proportional forms, each of size \(g=q-1\). Then
\[
T=q^{n-2}(J-E)+H I.
\]
The matrices \(J,E,I\) commute, with \(J^2=NJ\), \(E^2=gE\), and \(JE=gJ\). They give three mutually orthogonal idempotent projections
\[
\Pi_0=J/N,\qquad \Pi_1=E/g-J/N,\qquad \Pi_2=I-E/g.
\]
Direct multiplication shows that \(T\) acts on these spaces with eigenvalues \(q^{2n-2}\), \(q^{n-2}\), and \(q^{n-1}\), respectively. Therefore, for every \(k\ge0\),
\[
T^k=aJ/N+b(E/g-J/N)+c(I-E/g).
\]
For \(q=2\), \(\Pi_2\) is the zero projection, and this identity still holds. The identity for \(k=0\) recovers \(I\).

4. **The rank-one target fiber.** Fix \(B=u\beta\ne0\) and write \(t=\beta(u)=\operatorname{tr}B\). A sequence whose first factor has image \(\langle u\rangle\) is represented uniquely by its first form \(\alpha\), with \(\alpha(u)=1\), and subsequently by \(k=r-1\) transitions ending at \(\beta\). Hence
\[
\nu_r(B)=\sum_{\alpha:\alpha(u)=1}(T^k)_{\alpha\beta}.
\]
The summation set has size \(H\). It meets the proportionality class of \(\beta\) in exactly one element if \(t\ne0\), and in none if \(t=0\). It contains \(\beta\) itself exactly when \(t=1\). Summing the three terms in the preceding formula for \(T^k\) yields
\[
\nu_r(B)=\frac{H(a-b)}{N}
+\frac{\mathbf1_{\{t\ne0\}}(b-c)}{g}
+\mathbf1_{\{t=1\}}c,
\]
as asserted. There are no other possibilities for positive-rank products.

5. **The zero fiber.** Every row of \(T\) sums to \(q^{2n-2}\), either by the eigenvalue on the constants or by counting all next rank-one idempotents giving a nonzero product. For each of the \(m\) first factors, exactly \((q^{2n-2})^{r-1}=a\) ordered choices of later factors maintain nonzero product. Hence exactly \(ma\) ordered words have nonzero product. Subtraction from the \(m^r\) total words gives \(\nu_r(0)=m^r-ma\). Rank at least two is impossible because every factor has rank one. This exhausts the codomain and proves the theorem.

## Verification
The accompanying `verify_rank_one_products.py` is self-contained and uses exact finite-field arithmetic. It enumerates every rank-one idempotent, accumulates the distribution of their ordered products, and checks **each possible matrix target**, including targets of rank greater than one, against the formula. The executable checked 18 combinations: \(n=2\), \(q\in\{2,3,4,5\}\), with lengths up to four; \(n=3\), \(q\in\{2,3\}\), with lengths up to four; and \(n=4\), \(q=2\), with lengths two and three. For \(q=4\) it implements the irreducible-polynomial field \(\mathbb F_2[z]/(z^2+z+1)\). The recorded execution ends with `VERIFY_OK`; all eighteen checks passed. A finite check is corroboration, not a substitute for the proof for all prime powers, dimensions, and lengths.

As separate consistency checks, the sum of all prescribed fibers equals \(m^r\) by step 5, and the \(r=1\) identity reduces to the characteristic function of rank-one idempotents. For \(n=2,q=2,r=2\), there are six rank-one idempotents, twenty-four ordered pairs with nonzero product, and twelve ordered pairs with zero product.

## Relationship to prior work
Alahmadi, Jain, Leroy, and Sathaye (2015, primary MSC 15A23) study products of idempotents over rings and give, in their Section 4, existence criteria and bounds for **nonnegative real rank-one matrices** factored into nonnegative idempotents; their Theorems 4.2–4.3 do not enumerate ordered fibers over finite fields or all lengths. Earlier work of Erdős (1967) establishes existence of products of idempotents for singular matrices over fields, not the multiplicities of prescribed products of rank-one factors.

Ayyer, Schilling, Steinberg, and Thiéry (arXiv:1401.4250) develop spectra for random walks on \(\mathscr R\)-trivial monoids. Their stated hypothesis does not apply directly here: distinct rank-one idempotents with the same image satisfy \(PQ=Q\) and \(QP=P\), hence share a nontrivial Green \(\mathscr R\)-class. The explicit prescribed-target transition matrix and all-length fiber formula above are not corollaries of that restricted hypothesis.

Published finite-field notes on two-factor idempotent–nilpotent and nilpotent–involution factorizations treat different factor classes; an all-arity enumeration of **only rank-one idempotent products** does not follow from their statements. In a distinct problem, enumeration of tuples that **generate** the whole matrix algebra as a unital algebra constrains simultaneous invariance, not a prescribed product. Searches for equivalent formulations, general finite-monoid random walks, and finite-field matrix-product enumerations revealed no identified statement covering all target fibers here. This is a comparison with the inspected results, not a claim of exhaustive bibliographic priority.

## Limitations
Only rank-one idempotent factors are counted; the formula does not enumerate words allowing higher-rank idempotents or mixed nilpotent factors. The spectral diagonalization describes this specific fixed-image transition system, not arbitrary random walks on matrix monoids. The available published literature and searched corpus cannot exclude equivalently formulated work in unindexed or inaccessible sources, notably the complete treatment in Barnes, Cerrito, and Levi (1998), whose abstract, but not full original text, was accessible. No independent audit of the theorem has been conducted.

## References
1. A. Alahmadi, S. K. Jain, A. Leroy, and A. Sathaye, *Decompositions into Products of Idempotents*, Electronic Journal of Linear Algebra **29** (2015), 74–88. DOI: 10.13001/1081-3810.2948. Author-posted public full text dated 19 June 2015; journal publication 20 September 2015. Primary MSC 15A23.
2. J. A. Erdős, *On Products of Idempotent Matrices*, Glasgow Mathematical Journal **8** (1967), 118–122. DOI: 10.1017/S0017089500000173.
3. A. Ayyer, A. Schilling, B. Steinberg, and N. M. Thiéry, *Markov Chains, \(\mathscr R\)-Trivial Monoids and Representation Theory*, arXiv:1401.4250 (2014).
4. A. Barnes, F. Cerrito, and F. W. Levi, *Random Walks on Finite Semigroups*, Journal of Applied Probability (1998), DOI 10.1239/jap/1032438378. Abstract inspected; possible bibliographic coverage remains a stated risk.
