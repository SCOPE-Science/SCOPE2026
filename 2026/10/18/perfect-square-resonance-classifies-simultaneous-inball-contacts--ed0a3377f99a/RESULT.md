# Perfect-square resonance classifies simultaneous inball contacts of integral parking-function polytopes

## Finding

Let \(n\ge 2\), let \(\mathbf b=(b_1,\dots,b_n)\in\mathbb Z_{>0}^n\) with \(b_1\ge2\), and let \(P(\mathbf b)\) be the convex hull in the standard Euclidean space \(\mathbb R^n\) of the \(\mathbf b\)-parking functions. These are positive integer vectors whose increasingly sorted coordinates \(\beta'_j\) obey \(\beta'_j\le S_j=\sum_{i=1}^j b_i\). Put
\[
 A_k=\sum_{j=n-k+1}^{n}(S_j-1),\qquad f_k=k+\sqrt{k},\qquad
 \mathcal T(\mathbf b)=\operatorname{argmin}_{1\le k\le n}\frac{A_k}{f_k}.
\]
The set \(\mathcal T(\mathbf b)\) consists exactly of the cardinalities of upper subset-facet orbits touching the unique maximum-radius Euclidean inball. The new classification of **all attainable simultaneous contact patterns** is:

**Theorem.** For fixed \(n\ge2\), a nonempty set \(T\subseteq\{1,\ldots,n\}\) occurs as \(\mathcal T(\mathbf b)\) for some positive *integral* parameter vector with \(b_1\ge2\) **if and only if** either \(|T|=1\), or every member of \(T\) is a perfect square. Every permitted pattern admits an explicit integer construction.

Consequently the maximum possible number of facets tangent to the unique largest inball is exactly
\[
 \boxed{n+\sum_{1\le j\le\lfloor\sqrt n\rfloor}\binom{n}{j^2}},
\]
attained by a positive integral parameter vector. For any specific \(T\), the exact tangent-facet count is
\[
 n+\sum_{k\in T}\binom{n}{k}.
\]
This establishes an arithmetic selection rule for *simultaneous* Euclidean contact orbits, in contrast to the previously known realization of each individual contact cardinality.

## Assumptions and scope

All distances, facet normals, and balls refer to the *unlifted*, standard-coordinate Euclidean realization of \(P(\mathbf b)\subset\mathbb R^n\). The integral hypothesis is essential for the obstruction: allowing arbitrary positive real parameters permits other tie phenomena. The condition \(b_1\ge2\) ensures that every upper subset inequality is a true facet (rather than a redundant hyperplane). The theorem classifies the complete upper-contact cardinality set, including ties, not the combinatorial types of the polytopes. It makes no assertion about maximum-volume inscribed ellipsoids.

## Proof

**1. Facets, background inball formula, and exact contact orbit.** By Bayer et al., Theorem 2.3(c), the facet system for \(b_1\ge2\) is
\[
 x_i\ge1\quad (1\le i\le n),\qquad
 \sum_{i\in I}x_i\le \sum_{j=n-|I|+1}^nS_j
 \quad(\varnothing\ne I\subseteq[n]).
\]
The outward Euclidean normal of an upper subset facet of cardinality \(k\) has length \(\sqrt k\). If a ball of radius \(r\) is contained in \(P(\mathbf b)\) with center \(z\), each lower facet forces \(z_i\ge1+r\); summing any \(k\) of these and comparing with the corresponding upper facet yields
\[
 r\le\frac{\sum_{j=n-k+1}^n S_j-k}{k+\sqrt k}=\frac{A_k}{f_k}.
\]
Conversely, take \(r=\min_k A_k/f_k\) and \(z=(1+r)\mathbf1\). The lower facet inequalities hold at distance exactly \(r\); the upper inequalities all hold at distance at least \(r\). Thus this \(r\) is the exact Euclidean inradius. If a different center attained it, for any minimizing \(k\) all \(k\)-subsets would satisfy \(\sum_{i\in I}z_i\le k(1+r)\) while every coordinate obeys \(z_i\ge1+r\). Each coordinate belongs to one such subset, hence equality forces \(z=(1+r)\mathbf1\). At that center, an upper facet is tangent precisely when its cardinality minimizes \(A_k/f_k\); all \(n\) lower facets are tangent. This preliminary metric formula and individual-cardinality attainability are background; **the new assertion is the entire attainable family of sets** \(\mathcal T\).

**2. Integer square-root obstruction.** The numbers \(A_k\) are positive integers. If distinct \(k,\ell\) both minimize, then \(f_k/f_\ell=A_k/A_\ell\) is a positive rational \(q\). Therefore
\[
 \sqrt k=q\sqrt\ell+(q\ell-k).
\]
If \(\ell\) is not a perfect square, squaring this equality and comparing its rational and irrational parts gives \(q\ell-k=0\). It follows that \(k=q\ell=q^2\ell\), hence \(q=1\) and \(k=\ell\), a contradiction. Thus \(\ell\) is a square, and \(f_k=qf_\ell\) is rational, so \(k\) is also a square. Every set with more than one active cardinality therefore contains only square indices.

**3. Universal explicit realizability.** Write \(f(j)=j+\sqrt j\) for integers \(j\ge0\), taking \(f(0)=0\), and fix the positive integer \(M=100n^4\). Let \(A_0=0\). To realize any nonempty subset \(T\) of the square indices, define, for \(1\le j\le n\),
\[
 A_j=\begin{cases}
 M(j+\sqrt j),&j\in T,\\
 Mj+\lfloor M\sqrt j\rfloor+1,&j\notin T.
 \end{cases}
\]
These are integers; \(\frac{A_j}{M f(j)}=1\) if \(j\in T\), and \(A_j/Mf(j)>1\) otherwise. Hence the desired minimum pattern is exactly \(T\), provided the integer sequence \(A_j\) corresponds to a positive parameter vector. It does, by the following general verification.

For a singleton \(T=\{t\}\) with nonsquare \(t\), instead put
\[
 A_j=Mj+\lfloor M\sqrt j\rfloor+\begin{cases}1,&j=t,\\n+4,&j\ne t.\end{cases}
\]
Writing \(A_j=Mf(j)+\delta_j\), we have \(0<\delta_t<1\), while \(n+3<\delta_j\le n+4\) for \(j\ne t\). Since \(f(j)\le n+\sqrt n\le2n\) and \(f(t)\ge2\),
\[
 \frac{\delta_j}{f(j)}>\frac{n+3}{2n}>\frac12\ge\frac{\delta_t}{f(t)}.
\]
Thus only \(t\) minimizes \(A_j/f(j)\). (Singleton square indices are already covered by the first construction.)

In both constructions \(0\le\delta_j\le n+4\). For \(1\le j\le n-1\), direct square-root differences give
\[
 2\sqrt j-\sqrt{j-1}-\sqrt{j+1}
 \ge\frac1{4(j+1)^{3/2}}\ge\frac1{4n^{3/2}}.
\]
Since \(M/(4n^{3/2})=25n^{5/2}>2(n+4)\), the integer sequence \((A_0,\ldots,A_n)\) is **strictly discretely concave**: \(A_{j+1}-2A_j+A_{j-1}<0\). It is also strictly increasing, since its baseline successive differences exceed \(M\) and perturbations change by at most \(n+4\). Define
\[
 y_i=A_{n-i+1}-A_{n-i}\quad(1\le i\le n),\qquad
 b_1=1+y_1,\quad b_i=y_i-y_{i-1}\ (2\le i\le n).
\]
The \(y_i\) are positive, strictly increasing integers, so every \(b_i\) is a positive integer and \(b_1\ge2\). Their cumulative sums are \(S_i=1+y_i\), and telescoping gives
\[
 \sum_{j=n-k+1}^n(S_j-1)=\sum_{j=n-k+1}^ny_j=A_k.
\]
Thus these vectors realize exactly the prescribed \(T\). This proves the converse and completes the classification.

**4. Maximum contacts and a small witness.** For any possible active set \(T\), the contact count is \(n+\sum_{k\in T}\binom nk\). Every binomial coefficient is positive. By the classification, the largest count is obtained by choosing all square indices, giving the boxed maximum formula. For example, \(n=4\) and \(\mathbf b=(5,5,2,1)\) give \(A_1=12,A_2=23,A_3=32,A_4=36\). The minimum \(A_k/(k+\sqrt k)=6\) occurs exactly at \(k=1,4\), yielding \(4+4+1=9\) tangent facets. The construction above works in every dimension, including simultaneous sets with three or more square cardinalities.

## Verification

Run `python3 check_contact_resonance.py` with the Python standard library. The checker uses integer square roots and exact rational upper/lower bounds of \(\sqrt k\) rather than floating-point comparison to certify its constructed minima. It verified 431 prescribed patterns in dimensions 2 through 24, comprising 9,605 exact normalized distance comparisons; it also checked telescoping parameter reconstruction and strict concavity. A separate exact check confirms the small \(n=4\) tie witness. These finite calculations corroborate the explicit construction; the proof above establishes the infinite statement.

## Relationship to prior work

Bayer, Borgwardt, Chambers, Daugherty, Dawkins, Deligeorgaki, Liao, McAllister, Morrison, Nelson, and Vindas-Meléndez determine the underlying facet system and polymatroid structure of general \(\mathbf b\)-parking-function polytopes. Behrend and collaborators study partial permutohedra, whose classical parking-function instance is obtained by translation and whose polyhedral classification supplies related geometric context. Hanada, Lentfer, and Vindas-Meléndez study the earlier two-parameter specialization. A prior exact-inradius analysis already established the scalar minimum formula and that each individual upper cardinality can be uniquely active; neither assertion is presented as new here. The contribution here is the **complete, exact integer-arithmetic feasibility classification for simultaneous upper-cardinality contacts** and its sharp maximum facet-contact count. The two-parameter inball phase theorem is a strict subfamily and does not supply this general multi-orbit classification.

## Limitations

The classification applies only to integer parameters with \(b_1\ge2\) and standard-coordinate Euclidean balls. The case \(b_1=1\) has redundant upper inequalities and is not included in the realizability theorem. Inexact floating-point comparisons are insufficient to certify a tie; the proof uses exact algebraic identities. Prior-equivalent results under other terminology remain a bibliographic possibility. The verification is computational corroboration, not independent mathematical validation or a formal proof assistant certificate.

## References

1. M. M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, first public arXiv version 2024-03-12, arXiv:2403.07387, Theorem 2.3(c). https://arxiv.org/abs/2403.07387.
2. M. Hanada, J. Lentfer and A. R. Vindas-Meléndez, *Generalized parking function polytopes*, first public arXiv version 2022-12-13, arXiv:2212.06885. https://arxiv.org/abs/2212.06885.
3. R. E. Behrend et al., *Partial permutohedra*, first public arXiv version 2022-07-28, arXiv:2207.14253, with primary MSC2020 52B05. https://arxiv.org/abs/2207.14253.
