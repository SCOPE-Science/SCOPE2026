# Globally minimal defensive alliances of balanced complete multipartite graphs

## Finding
Let \(r\ge3\) and \(n\ge2\) be integers, and let \(G=K_{n,\ldots,n}\) be the complete \(r\)-partite graph with \(r\) parts of size \(n\). A defensive alliance is a nonempty vertex set \(S\) for which every \(v\in S\) has at least as many neighbors **including itself** in \(S\) as neighbors outside \(S\). Such an alliance is *globally minimal* if none of its nonempty proper subsets is a defensive alliance. Put
\[
 t=\left\lfloor\frac{(r-1)n}{2}\right\rfloor,\qquad s_i=|S\cap V_i|,\qquad s=|S|.
\]
Then the following three conclusions hold together.

**Exact classification.** The set \(S\) is a globally minimal defensive alliance if and only if, for the integer \(a=s-t\),
\[
 1\le a\le n,\qquad 0\le s_i\le a\ \text{for every }i,\qquad
 |\{i:s_i=a\}|\ge2.
\]
In particular, on these graphs global minimality coincides with one-vertex-deletion (local) minimality, although the two notions differ on general graphs.

**Sharp upper alliance number.** Writing \(A(G)\) for the largest size of an inclusion-minimal ordinary defensive alliance,
\[
 \boxed{A(G)=n+\left\lfloor\frac{(r-1)n}{2}\right\rfloor.}
\]
The bound is attained for every \(r\ge3,n\ge2\).

**Full globally minimal enumerator.** Put
\[
 B_a(z)=\sum_{j=0}^{a}\binom nj z^j,\qquad
 \mathcal M_{r,n}(x)=\sum_{S\text{ globally minimal}}x^{|S|}.
\]
Then
\[
 \boxed{\mathcal M_{r,n}(x)=\sum_{a=1}^{n}N_a x^{t+a},\quad
 N_a=\sum_{k=2}^{r}(-1)^{k-2}(k-1)\binom rk\binom na^{k}
 [z^{\,t-(k-1)a}] B_a(z)^{r-k}.}
\]
Coefficients of negative degrees, or degrees exceeding the polynomial degree, are zero. In particular, the **exact number of maximum-size globally minimal alliances** equals
\[
 \boxed{N_n=\sum_{k=2}^{r}(-1)^{k-2}(k-1)\binom rk
 \binom{(r-k)n}{t-(k-1)n},}
\]
with out-of-range binomial coefficients taken as zero.

## Assumptions and scope
The graphs are finite, simple and undirected, and all \(r\) parts are nonempty and labeled only for counting. The term *ordinary defensive alliance* uses the closed neighborhood in the internal count; replacing it by the open neighborhood changes the threshold and is not the theorem here. The phrase *globally minimal* means inclusion-minimal against **every** proper nonempty subset, not merely against deleting a single vertex. The upper alliance number is a **maximum among inclusion-minimal sets**, not a maximum among all defensive alliances or the usual minimum alliance number. This theorem is restricted to \(r\ge3,n\ge2\), with no claim about unequal parts or the bipartite case.

## Proof
Write \(d=(r-1)n\) for the common vertex degree. Every vertex \(v\in S\cap V_i\) has exactly \(s-s_i\) neighbors in \(S\), so the defensive inequality is
\[
 (s-s_i)+1\ge d-(s-s_i)
 \quad\Longleftrightarrow\quad s-s_i\ge\left\lceil\frac{d-1}{2}\right\rceil=t.
\]
Therefore, since \(t\ge2\), an alliance uses at least two different parts. For \(a=s-t\), feasibility is equivalent to every occupied part satisfying \(s_i\le a\). The omitted parts satisfy this automatically, and because \(S\ne\varnothing\), necessarily \(a\ge1\).

Call an occupied part *tight* if \(s-s_i=t\), equivalently if \(s_i=a\). When a vertex from an occupied part \(V_j\) is deleted, the support \(s-s_i\) for any surviving vertex of \(V_i\) decreases by one when \(i\ne j\), and is unchanged when \(i=j\). Thus if there are no tight parts, every single-vertex deletion leaves an alliance; if there is exactly one tight part, deleting a vertex of that part leaves an alliance (all the other occupied parts have positive slack). Conversely, if at least two distinct parts are tight, every single-vertex deletion violates the inequality for a surviving vertex in a different tight part. This proves the characterization of *local* minimality.

It remains to establish the stronger global assertion. Suppose \(V_i,V_j\) are different tight parts and \(T\subseteq S\) is any nonempty defensive alliance. If \(T\) contains any vertex of the tight part \(V_i\), the support of that vertex in \(S\) equals exactly \(t\); since supports cannot increase on restricting to \(T\), all \(t\) vertices of \(S\setminus V_i\) must belong to \(T\). In particular, \(T\) contains the nonempty tight part \(V_j\). Applying the same argument to a vertex in \(V_j\) forces every vertex of \(S\setminus V_j\) to lie in \(T\), whence \(T=S\). If, on the other hand, \(T\) avoids both tight parts, then
\[
 |T|\le s-s_i-s_j=(t+a)-2a=t-a<t+1.
\]
Yet every nonempty alliance \(T\) must contain at least \(t+1\) vertices, since \(|T|-|T\cap V_h|\ge t\) for any occupied part \(V_h\). This is a contradiction. Hence \(S\) is globally minimal. Since globally minimal implies locally minimal, the classification follows. At least two tight parts imply \(a\le n\), completing the range.

The range yields \(|S|=t+a\le t+n\). Because \(r\ge3\),
\[
 0\le t-n\le (r-2)n.
\]
Consequently select two full parts, of size \(n\) each, and distribute exactly \(t-n\) vertices among the remaining \(r-2\) parts. This set has total size \(t+n\), and at least two parts of occupancy \(n\), hence it is globally minimal. This proves the sharp upper alliance number.

For the enumerator fix \(a\in\{1,\ldots,n\}\). Every part may contribute \(j\) vertices for \(0\le j\le a\), with multiplicity \(\binom nj\), and the total selected size must be \(t+a\). Require at least two parts to achieve the cap \(a\). For each set \(I\) of \(k\) prescribed tight parts, fixing their \(a\) selected vertices gives \(\binom na^k\), while the remaining \(r-k\) parts contribute coefficient
\[
 [z^{t+a-ka}]B_a(z)^{r-k}=[z^{t-(k-1)a}]B_a(z)^{r-k}.
\]
If exactly \(h\) parts are tight, the inclusion-exclusion weight over prescribed tight subsets of sizes \(k\ge2\) is
\[
 \sum_{k=2}^{h}(-1)^{k-2}(k-1)\binom hk=1
 \quad(h\ge2),
\]
and this sum is zero when \(h<2\). To verify the identity, differentiate \((1-u)^h\) at \(u=1\) and combine the binomial sums for \(k\binom hk\) and \(\binom hk\). Thus summing over \(k\) counts each eligible set exactly once and gives the displayed formula for \(N_a\). At \(a=n\), \(B_n(z)=(1+z)^n\), which reduces it to the stated binomial formula for \(N_n\).

For instance, at \(r=3,n=3\), the formula gives \(\mathcal M_{3,3}(x)=81x^5+3x^6\); at \(r=4,n=3\), it gives \(\mathcal M_{4,3}(x)=594x^6+36x^7\).

## Verification
The included standalone `verify.py` runs on standard Python 3 with no third-party dependencies. It builds each finite graph as literal bitset adjacency, checks the defensive inequality for every nonempty subset, and determines **global** minimality by examining proper subsets via a dynamic submask predicate. Separately it constructs the enumerator by part-occupancy vectors, and then independently by the alternating coefficient-extraction formula above. These checks agreed for ten graph sizes with 145,206 direct candidate subsets, plus ten larger parameter profiles beyond the direct-subset range. The script also verifies the upper number and maximum-size multiplicity against the two independent enumerators. Its full captured output is in `verify_output.txt`. Finite tests support, but do not replace, the proof for all integers \(r,n\) in scope.

## Relationship to prior work
Bazgan, Fernau and Tuza (2018 online; journal 2019) introduced and investigated upper defensive alliance parameters and carefully distinguished local from global inclusion-minimality. Gaikwad and Maity (2022) studied parameterized computation of the maximum globally minimal alliance, including a general neighborhood-diversity algorithm, but not this sharp equal-part formula. Feng, Fernau and Mann (2023) investigated enumeration of minimal defensive alliances and its general complexity; the result here instead provides explicit closed enumerators for a particular natural family. An earlier publicly available complete-multipartite result, *Strong alliance polynomial of complete multipartite graphs* (2026), proves a cap inequality and a tight-part criterion for **strong** defensive alliances, a different condition that excludes the selected vertex itself from the internal support and enumerates **all strong alliances**. Its proof technique is a substantial antecedent. When the common degree \( (r-1)n \) is even, the strong and ordinary feasibility inequalities coincide, so the minimal-set **classification** in that parity is already implicit in the prior strong result. When the degree is odd (equivalently, \(r\) is even and \(n\) is odd), the inequalities differ by exactly one cross-part supporter; the present proof establishes the ordinary global-minimality statement and the stated uniform **counting and upper-size formulas** across both parities. No novelty is claimed for the shared even-degree tightness observation or the generic capacity reduction.

## Limitations
The equal-size assumption makes the defensive threshold independent of the occupied part. The given upper formula and one-variable enumerator are not asserted for arbitrary unequal complete multipartite graphs. The inclusion-exclusion formula is exact but may exhibit cancellation and is not claimed optimal for every parameter. This is a same-model mathematical analysis, not an independently audited theorem. Exact novelty cannot be guaranteed from literature/database searches; an equivalent presentation under critical defensive alliances, satisfactory sets or different notation may exist, especially because the strong-alliance counterpart is close. The finite verifier does not certify the infinite claim on its own. In even-degree instances, ordinary and strong alliance predicates coincide, and the earlier strong tightness result already covers the underlying inclusion-minimal classification; the present full enumerator and upper extremal count are the additional claimed outputs, with genuinely different ordinary predicates only in odd degree.

## References
1. C. Bazgan, H. Fernau and Z. Tuza, *Aspects of upper defensive alliances*, Discrete Applied Mathematics **266** (2019), 111–120; first available online 2018-06-30. DOI: 10.1016/j.dam.2018.05.061. Author manuscript: https://real.mtak.hu/105500/1/Bazgan-Fernau-Tuza-Aspects_of_Upper_Defensive_Alliances.pdf.
2. A. Gaikwad and S. Maity, *Globally Minimal Defensive Alliances: A Parameterized Perspective*, arXiv:2202.02010v1, 2022-02-04. https://arxiv.org/abs/2202.02010.
3. Z. Feng, H. Fernau and K. Mann, *Enumerating Minimal Defensive Alliances*, arXiv:2312.11963v1, 2023-12-19. https://arxiv.org/abs/2312.11963.
4. *Strong alliance polynomial of complete multipartite graphs*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-strong-alliance-polynomial-of-complete-multipartite-graphs--cf4980ea579a.
