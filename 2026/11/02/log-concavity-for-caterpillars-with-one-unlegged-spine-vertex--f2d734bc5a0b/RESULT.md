# Log-concavity for caterpillars with one unlegged spine vertex

## Finding

**Theorem.** Fix integers \(k\ge3\) and \(2\le j\le k-1\). Let \(a_1,\ldots,a_k\) be integers with \(a_j=0\) and \(a_i\ge1\) for all \(i\ne j\). Construct a caterpillar \(T\) with a path \(v_1v_2\cdots v_k\), attaching \(a_i\) distinct pendant leaves to \(v_i\). Put \(U_t(x)=x(1+x)^t+x^t\) for positive integers \(t\), and set \(a=a_{j-1}\), \(c=a_{j+1}\). Then its ordinary domination polynomial is

\[
D(T;x)=\left((1+x)U_a(x)U_c(x)-x^{a+c}\right)\prod_{i\notin\{j-1,j,j+1\}}U_{a_i}(x).
\]

All its nonzero coefficients form a log-concave sequence; equivalently, if \(d_r(T)\) counts dominating vertex subsets of cardinality \(r\), then

\[
d_r(T)^2\ge d_{r-1}(T)d_{r+1}(T)\qquad (1\le r<|V(T)|).
\]

In particular, the domination polynomial is unimodal for *every* caterpillar having exactly one unlegged interior spine vertex and at least one private pendant leaf on all other spine vertices, regardless of their number or sizes. For a single unlegged vertex, this settles an infinite family of the legless-caterpillar log-concavity question raised in Remark 3.4 of Du–Heilman–Panova (2026).

## Assumptions and scope

All graphs are finite, undirected, simple and labelled for enumeration. A vertex subset \(S\) is *dominating* when every vertex lies in \(S\) or has a neighbor in \(S\). Its generating polynomial is \(D(T;x)=\sum_{S\text{ dominating}}x^{|S|}\), including zero coefficients below the domination number. Log-concavity means the inequalities above and no internal zero between positive coefficients. The spine includes both endpoints; \(a_1,a_k\ge1\) is automatic from the hypotheses. The theorem allows arbitrarily long spines and arbitrarily many private leaves, but only one zero among the \(a_i\).

## Proof

**1. Exact factorization.** Fix a vertex \(v_i\) with \(a_i=t\ge1\). If \(v_i\) is selected, its attached leaves can be selected arbitrarily, contributing \(x(1+x)^t\). If it is absent, every one of its private leaves must be selected, contributing \(x^t\). In either case \(v_i\) is dominated without assistance from its spine neighbors. Consequently all such positive-leaf blocks are independent, apart from their possible role in dominating the one bare vertex \(v_j\). For that vertex, selection contributes \(x\) and absence contributes \(1\); when absent it must be dominated by at least one of \(v_{j-1}\) and \(v_{j+1}\). Thus begin with \((1+x)U_aU_c\), and subtract configurations where \(v_j\) and both adjacent spine vertices are absent. Each absent adjacent vertex forces *all* of its leaves into the set, giving the single disallowed monomial \(x^{a+c}\). The remaining positive-leaf blocks factor freely, proving the displayed formula.

The distinguished factor \(Q_{a,c}(x)=(1+x)U_a(x)U_c(x)-x^{a+c}\) has the manifestly nonnegative decomposition

\[
Q_{a,c}(x)=x^2(1+x)^{a+c+1}+x^{a+1}(1+x)^{c+1}+x^{c+1}(1+x)^{a+1}+x^{a+c+1}.
\]

Hence it has strictly positive coefficients at *every* degree from \(2\) to \(a+c+3\), and zero coefficients elsewhere.

**2. Local block log-concavity.** For \(t\ge1\), the nonzero coefficient list of \(U_t\) consists of \(\binom{t}{0},\binom{t}{1},\ldots,\binom{t}{t-2},\binom{t}{t-1}+1,\binom{t}{t}\), with the natural direct interpretations when \(t=1,2\). Its log-concavity follows from the standard binomial inequalities, with the sole potentially changed inequality controlled (for \(t\ge3\)) by

\[
\binom t2^2-\binom t3(t+1)=\frac{t(t-1)(t^2-t+4)}{12}>0.
\]

Direct inspection covers \(t=1,2\). Multiplying by \(1+x\) and taking products preserve log-concavity for nonnegative, hole-free coefficient sequences (the convolution closure theorem, equivalently the Toeplitz total-positivity-of-order-two argument). Therefore \(P_{a,c}(x)=(1+x)U_a(x)U_c(x)\) is log-concave.

**3. The only endangered inequality.** Let \(s=a+c\) and \(t=ac\). Since \(Q_{a,c}=P_{a,c}-x^s\), decreasing its coefficient at degree \(s\) can only endanger log-concavity *at that same degree*: all other left sides remain unchanged, whereas adjacent right sides become no larger. Write \(q_r=[x^r]Q_{a,c}\). Explicit coefficient extraction from the positive expansion gives

\[
\begin{aligned}
q_s&=\binom{s+1}{3}+\binom{a+1}{2}+\binom{c+1}{2},\\
q_{s-1}&=\binom{s+1}{4}+\binom{a+1}{3}+\binom{c+1}{3},\\
q_{s+1}&=\binom{s+1}{2}+s+3.
\end{aligned}
\]

Here \(\binom nr=0\) if \(r>n\). Exact polynomial expansion, using \(a^2+c^2=s^2-2t\) and \(a^3+c^3=s^3-3st\), yields

\[
\begin{aligned}
144(q_s^2-q_{s-1}q_{s+1})
={}&s^6+9s^5+19s^4+27s^3+52s^2+36s\\
&-12s^3t-36s^2t+120st+144t^2.
\end{aligned}
\]

The elementary bound \(4t\le s^2\) implies that the two potentially negative terms together satisfy

\[-12s^3t-36s^2t\ge-3s^5-9s^4.\]

Consequently

\[
144(q_s^2-q_{s-1}q_{s+1})\ge
s^6+6s^5+10s^4+27s^3+52s^2+36s+120st+144t^2>0,
\]

because \(s\ge2\) and \(t\ge1\). This proves the sole missing coefficient inequality and hence log-concavity of \(Q_{a,c}\).

**4. Global conclusion.** Each other factor \(U_{a_i}\) is nonnegative and log-concave without internal zeros. Their convolution product with \(Q_{a,c}\) remains log-concave and hole-free, proving the theorem for every admissible \(k,j\) and list \((a_i)\). The result also includes the shortest spine \(k=3\), whose two pendant-bearing spine endpoints can have arbitrarily high degree. \(\square\)

## Verification

The independent Python 3 standard-library program `verify.py` constructs the stated graph explicitly. It compares the factorization with exhaustive domination-set enumeration for 192 small parameter tuples, and separately with a three-state rooted-tree dynamic program for 18,045 tuples. It checks every log-concavity inequality in each comparison. Finally, for all 6,400 integer pairs \(1\le a,c\le80\), it checks the exact degree-six margin identity, its positivity and all inequalities of \(Q_{a,c}\). The program prints `EXHAUSTIVE_OK 192`, `TREE_DP_OK 18045`, `MARGIN_OK 6400`, `VERIFY_OK` when successful. Finite verification is supplementary; the four-part proof above covers all positive integer parameters.

## Relationship to prior work

Du, Heilman and Panova, *Trees and Graphs with Non Log-concave Dominating Set Sequence via AI Tools* (arXiv:2605.02193v1, publicly posted May 4, 2026), Theorem 3.3, establish the product formula and log-concavity when **every** spine vertex has at least one leaf. Their Remark 3.4 explicitly proposes that the analogous statement continues to hold when some spine vertices lack leaves. Their theorem does not include the present exactly-one-gap family, for which the independent product formula fails and the local correction requires a new inequality.

Şahin and Şahin (2018) analyze domination polynomials of caterpillars, including bistar and comb formulas, but the inspected full text does not state the log-concavity result for an arbitrary single missing interior leaf-group. Wang (2026) proves log-concavity for spiders whose legs all have length at most three, a different family: here the caterpillar spine and degrees of its two adjacent support vertices are unbounded. Beaton and Schoonhoven (2024) establish unimodality for nearly well-dominated trees under a domination-number-gap restriction, not this all-parameter log-concavity statement. Standard coefficient-convolution closure is used as a known tool, not claimed as novel.

## Limitations

The theorem leaves two or more unlegged spine vertices untreated, including adjacent unlegged vertices; it is therefore not a proof of the full conjecture on all caterpillars. It concerns ordinary closed-neighborhood domination, not total domination, power domination, independent domination, or the domination polynomial for arbitrary trees. The novelty comparison is based on accessible cited primary texts and targeted search; unpublished or differently named equivalent work may exist. No external independent validation has been performed.

## References

1. A. Du, S. Heilman and G. Panova, *Trees and Graphs with Non Log-concave Dominating Set Sequence via AI Tools*, arXiv:2605.02193v1 (2026), Section 3.2, Theorem 3.3 and Remark 3.4. https://arxiv.org/html/2605.02193v1
2. B. Şahin and A. Şahin, *On Domination Polynomials of Caterpillar Graphs*, Turkish Journal of Mathematics and Computer Science **9** (2018), 34–38, Theorems 2.1–2.3. https://dergipark.org.tr/en/pub/tjmcs/article/434101
3. X. Wang, *Log-concavity of domination polynomials for spiders with legs of length at most three* (2026), DOI:10.5281/zenodo.20513066. https://www.researchgate.net/publication/405734171_Log-concavity_of_domination_polynomials_for_spiders_with_legs_of_length_at_most_three
4. I. Beaton and S. Schoonhoven, *On the unimodality of nearly well-dominated trees*, arXiv:2411.02288 (2024). https://arxiv.org/abs/2411.02288
