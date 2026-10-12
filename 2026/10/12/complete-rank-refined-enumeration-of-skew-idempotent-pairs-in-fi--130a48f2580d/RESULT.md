# Complete rank-refined enumeration of skew idempotent pairs in finite transformation monoids

## Finding

For any integer \(n\geq1\), let \(T_n\) be the monoid of all functions from \(X=\{1,\ldots,n\}\) to itself, with composition \((ab)(x)=a(b(x))\). An **ordered skew pair** is \((e,f)\in T_n^2\) for which \(e^2=e\), \(f^2=f\), \(fe\) is idempotent and \(ef\) is not. This fixes the conventional orientation used in the referenced semigroup literature. Let \(C_n(r,s)\) count such pairs with \(|e(X)|=r\) and \(|f(X)|=s\).

For every \(1\leq r,s\leq n\), the complete exact count is

\[
\begin{aligned}
C_n(r,s)={}&\binom ns
\sum_{t=\max(0,r+s-n)}^{\min(r,s)}
\binom st\binom{n-s}{r-t}(rs)^{n-r-s+t}\\[-1mm]
&\qquad\times\sum_{k=\max(1,t)}^{\min(r,s)}
\binom{s-t}{k-t}\frac{(r-t)!}{(r-k)!}
 k^{r-k}\bigl(r^{s-k}-k^{s-k}\bigr).
\end{aligned}
\]

Consequently the **entire joint-rank enumerator** is \(\mathcal K_n(U,V)=\sum_{r=1}^n\sum_{s=1}^n C_n(r,s)U^rV^s\). No field, representation, random-model, or asymptotic hypothesis is involved; the formula holds for every positive integer \(n\). All factorial arguments are nonnegative over the stated summation ranges.

There are no skew pairs for \(n\leq2\), and there are exactly six for \(n=3\). In the first nontrivial rank slice, for every \(n\geq3\),

\[
C_n(2,2)=\frac{n(n-1)(n-2)(n+1)}4\,4^{n-3}.
\]

For \(n=4\), the complete rank polynomial is

\[
\mathcal K_4(U,V)=120U^2V^2+36U^2V^3+24U^3V^2+24U^3V^3,
\]

so the full transformation monoid on four labeled points has precisely \(204\) ordered skew pairs of idempotents.

## Assumptions and scope

Every transformation is a total function, every count is of **ordered, labeled** pairs, and rank means image cardinality. The condition on the products is asymmetric; reversing the order of the two transformations exchanges the variables \(U,V\) and reverses which product is required to be idempotent. The statement counts all conventional skew pairs together, not their four previously defined semigroup-theoretic subtypes.

## Proof

**1. Image choices and restrictions.** Fix a pair of idempotents \(e,f\) and write \(A=f(X)\), \(B=e(X)\), \(C=A\cap B\), with cardinalities \(|A|=s\), \(|B|=r\), \(|C|=t\). Since an idempotent transformation fixes its image pointwise, \(e\) fixes \(B\) and \(f\) fixes \(A\). Put \(\alpha=f|_B:B\to A\), \(\beta=e|_A:A\to B\); both restrictions fix \(C\) pointwise. Conversely, these two restrictions and arbitrary images for each point outside \(A\cup B\) uniquely specify \(e,f\). The number of choices of image sets \(A,B\) is \(\binom ns\binom st\binom{n-s}{r-t}\), and the number of extensions outside their union is \((rs)^{n-r-s+t}\).

**2. Exact product conditions.** Since the images of \(fe\) and \(ef\) are respectively \(\alpha(B)\) and \(\beta(A)\), and a map is idempotent exactly when it fixes its image, one has the equivalences

\[
(fe)^2=fe\iff\alpha\beta\alpha=\alpha,
\qquad
(ef)^2=ef\iff\beta\alpha\beta=\beta.
\]

These equivalences are both necessary and sufficient for full transformations, because \(e(X)=B\) and \(f(X)=A\) are surjective image maps.

**3. The weighted fiber count.** Let \(Y=\alpha(B)\) and \(|Y|=k\). As \(\alpha\) fixes \(C\), \(C\subseteq Y\), and \(1\leq k\leq\min(r,s)\). The remaining \(k-t\) points of \(Y\) form a set \(D\subseteq A\setminus C\) with \(\binom{s-t}{k-t}\) possibilities. The identity \(\alpha\beta\alpha=\alpha\) forces \(\beta(y)\in\alpha^{-1}(y)\) for \(y\in Y\). For \(y\in C\), the choice is fixed as \(\beta(y)=y\). For each \(y\in D\), choose its representative \(\beta(y)\in B\setminus C\). These representatives are distinct, so there are \((r-t)!/(r-k)!\) choices. The remaining \(r-k\) elements of \(B\setminus C\) may be mapped by \(\alpha\) independently to any of the \(k\) elements of \(Y\), giving \(k^{r-k}\) choices. This counts every pair consisting of a restriction \(\alpha\) and the forced-on-\(Y\) part of \(\beta\) exactly once.

For each of the \(s-k\) points of \(A\setminus Y\), the first product condition permits any of \(r\) values of \(\beta\). The second product condition holds as well if and only if each of these values lies in the set of the \(k\) already selected representatives \(\beta(Y)\): indeed \(\beta\alpha\beta=\beta\) reduces to this fixed-representative condition, and the representatives are distinct. Hence the number of choices making \(fe\) idempotent but \(ef\) non-idempotent is \(r^{s-k}-k^{s-k}\). Multiplying the independent choices and summing over \(t,k\) gives the asserted formula without inclusion-exclusion or overcounting.

**4. Small-rank consequences.** If either transformation has rank one, both products are constant and hence idempotent; those coefficients vanish. The displayed sum for \(r=s=2\) receives contributions only from \(t=0,1\): their sum is

\[
\binom n2\left(\binom{n-2}{2}+2(n-2)\right)4^{n-3}
=\frac{n(n-1)(n-2)(n+1)}4\,4^{n-3}.
\]

For \(n=1,2\) every possible rank pair has a rank-one factor or else both are bijections (hence identity idempotents), so the skew locus is empty. At \(n=3\), the rank-two slice gives six pairs.

## Verification

The accompanying standalone `checker.py` creates every idempotent full transformation by fixing an image set and independently assigning each other point to that image. For each ordered pair it computes both products as full functions, checks their idempotence by direct composition, records ranks, and compares every rank coefficient with the independent summation formula. Exhaustive tests are performed for \(n=1,2,3,4,5,6\); totals are respectively \(0,0,6,204,5900,190410\). The last case checks over one million ordered pairs. A successful run prints `VERIFY_OK`.

The exhaustive finite checks are regression evidence, **not** a substitute for the all-\(n\) combinatorial proof above.

## Relationship to prior work

Blyth and Almeida Santos (2006) introduced and investigated the occurrence and types of skew idempotent pairs in full transformation semigroups. Their accessible abstract emphasizes occurrence of the four types, not labeled pair counting. Their complete article was unavailable for material inspection, leaving a specific bibliographic risk. Luangchaisri and Changphas (first publicly available 21 December 2021) study the four types in **partial** transformation semigroups, including precise existence thresholds; the materially inspected full article's theorems and conclusions do not give an all-\(n\) rank-refined enumeration in the full monoid. Blyth and Almeida Santos' derived Rees-matrix investigation concerns embeddings and existence thresholds of small semigroups rather than this distribution. These studies motivate the present count, and their established results are not claimed as new.

The reported contribution is **only** the exact bivariate joint-rank distribution and its derived rank-two slice, not the existence or classification of skew-pair types. Failed bibliographic searches are not mathematical proof of priority.

## Limitations

The theorem concerns total transformations of finite labeled sets; it does not classify skew pairs up to simultaneous conjugacy, does not split the count by the four recognized skew-pair subtypes, and does not automatically extend to partial transformations or infinite sets. Some older work exists only as abstracts in the accessible sources. No independent mathematical audit has been performed.

## References

1. P. Luangchaisri and T. Changphas, *Skew Pairs of Idempotents in Partial Transformation Semigroups*, Mathematics **10** (2022), article 2. First online 21 December 2021. DOI: `10.3390/math10010002`.
2. T. S. Blyth and M. H. Almeida Santos, *Skew Pairs of Idempotents in Transformation Semigroups*, Acta Mathematica Sinica, English Series **22** (2006), 1705–1714. DOI: `10.1007/s10114-005-0703-5`.
3. T. S. Blyth and M. H. Almeida Santos, *Derived Rees Matrix Semigroups as Semigroups of Transformations*, Semigroup Forum **73** (2006), 219–233. DOI: `10.1007/s00233-006-0605-6`.
