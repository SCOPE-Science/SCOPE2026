# Poisson and compound-Poisson violation laws for random poly-dependence

## Finding

The elementary cross-team dependence atom has an exact finite probability generating function under independent Bernoulli relation sampling. Two natural critical sparse regimes with **the same limiting expected number of violations** have different limiting violation distributions: ordinary Poisson and a nontrivial compound Poisson law. In particular, their integrity-satisfaction probabilities have different limits. This distinction quantifies the clustering created by a sparse relation that encounters multiple rows of a denser relation.

For an integer \(q\geq 1\) and \(p,r\in[0,1]\), let \(X,Y\subseteq[q]\times[q]\) be independent random relations; include each pair in \(X\) with probability \(p\) and independently each pair in \(Y\) with probability \(r\). Define the **cross-team violation count**
\[
W_q=\sum_{a,b,c=1}^q {\bf1}\{(a,b)\in X\}{\bf1}\{(a,c)\in Y\}{\bf1}\{b\ne c\}.
\]
Here the poly-dependence atom says that whenever the two teams have the same first-coordinate value, their second-coordinate values must agree; equivalently, \(W_q=0\).

**Exact finite law.** For \(0\le t\le1\),
\[
\boxed{\mathbb E[t^{W_q}]=G_q(t;p,r)^q},\qquad
G_q(t;p,r)=\sum_{m=0}^{q}\binom qm p^m(1-p)^{q-m}
(1-r+rt^{m-1})^m(1-r+rt^m)^{q-m}.
\]
At \(m=0\), define the first factor to be \(1\), including at \(t=0\). For arbitrary \(p,r\) this has the exact satisfaction-probability specialization
\[
\boxed{\Pr(W_q=0)=\left[(1-p)^q+(1-r)^q-(1-p)^q(1-r)^q+
qpr(1-p)^{q-1}(1-r)^{q-1}\right]^q.}
\]
The endpoint convention \(0^0=1\) applies to the factors in this finite identity. For \(p=r=1/2\), exactly \(\bigl(2^{q+1}-1+q\bigr)^q\) of the \(2^{2q^2}\) ordered pairs of relations satisfy the atom.

**Distinct critical laws.** Fix real \(a,b>0\), and permit \(p=p_q,r=r_q\) to vary with \(q\). If
\[
q^{3/2}p_q\longrightarrow a,\qquad q^{3/2}r_q\longrightarrow b,
\]
then
\[
W_q\ \xrightarrow{d}\ \operatorname{Poisson}(ab),\qquad
\Pr(W_q=0)\longrightarrow e^{-ab}.
\]
If instead
\[
qp_q\longrightarrow a,\qquad q^2r_q\longrightarrow b,
\]
then
\[
W_q\ \xrightarrow{d}\ \sum_{i=1}^{N}J_i,
\quad N\sim\operatorname{Poisson}(b),\quad
J_i\stackrel{\rm iid}{\sim}\operatorname{Poisson}(a),
\]
where all variables on the right are independent, and consequently
\[
\boxed{\Pr(W_q=0)\longrightarrow \exp\{-b(1-e^{-a})\}.}
\]
The latter distribution has mean \(ab\) and variance \(ab(1+a)\), whereas ordinary \(\operatorname{Poisson}(ab)\) has variance \(ab\). Both sampling regimes have \(\mathbb E W_q\to ab\); moreover \(e^{-b(1-e^{-a})}>e^{-ab}\) for \(a,b>0\). Exchanging the two relations gives the symmetric asymmetric regime.

## Assumptions and scope

We use **set-valued**, not bag-valued, teams: a pair is either present or absent. Relations are independent, and all individual facts are mutually independent; the inclusion probability is constant within each relation, not necessarily between relations. The key and value alphabets both have \(q\) elements. The variables of the two teams are different sorts but take values in a common alphabet, as in the semantics of poly-dependence in Hannula–Kontinen–Virtema. No assumption of internal functional dependence within either relation is made. Violation counts are ordered by their roles \(X\) and \(Y\) and count all mismatching cross-table pairs, including coinciding keys. Weak convergence assertions take \(q\to\infty\); \(a,b\) are fixed positive constants. The finite generating-function and satisfaction formulas also cover \(q=1\) and endpoint inclusion probabilities with the stated conventions.

## Proof

**1. Conditional per-key generating function.** Fix a key \(u\in[q]\), and let \(A_u=\{v:(u,v)\in X\}\) and \(B_u=\{v:(u,v)\in Y\}\). Conditional on \(|A_u|=m\), a present \(Y\)-value in \(A_u\) generates exactly \(m-1\) violations and one outside \(A_u\) generates exactly \(m\) violations. The \(Y\)-facts are independent Bernoulli variables. Therefore the conditional generating function is
\[
(1-r+rt^{m-1})^m(1-r+rt^m)^{q-m}.
\]
Since \(|A_u|\sim\operatorname{Binomial}(q,p)\), its expectation is \(G_q(t;p,r)\). Different keys use disjoint independent facts, so the full generating function is its \(q\)-th power. When \(m=0\), there are no violations and the first factor equals one.

**2. Exact satisfaction criterion.** At one fixed key, zero violations occur exactly when \(A_u=\varnothing\), or \(B_u=\varnothing\), or both are the identical singleton. Inclusion–exclusion for the first two events, followed by the disjoint singleton event, gives
\[
(1-p)^q+(1-r)^q-(1-p)^q(1-r)^q+qpr(1-p)^{q-1}(1-r)^{q-1}.
\]
Independence across keys proves the stated finite formula. For \(p=r=1/2\), multiply by \(2^{2q^2}\), obtaining the integer enumeration displayed above.

**3. Balanced sparse regime.** Let \(p_q\sim a q^{-3/2}\) and \(r_q\sim b q^{-3/2}\). For one key, the probability that \(A_u\) and \(B_u\) are both nonempty is
\[
(1-(1-p_q)^q)(1-(1-r_q)^q)=ab/q+o(q^{-1}).
\]
The chance that either \(|A_u|\ge2\) with \(B_u\ne\varnothing\), or \(|B_u|\ge2\) with \(A_u\ne\varnothing\), is \(O(q^{-3/2})=o(q^{-1})\): use the second factorial moments of the binomial sizes and independence. The joint singleton case has equal values with conditional probability exactly \(1/q\). Thus the key-wise violation count is one with probability \(ab/q+o(q^{-1})\), zero otherwise apart from probability \(o(q^{-1})\). For fixed \(0\le t\le1\), \(G_q(t;p_q,r_q)=1+ab(t-1)/q+o(q^{-1})\). Taking the \(q\)-th power yields \(\exp\{ab(t-1)\}\), the PGF of a Poisson law. In particular, setting \(t=0\) proves the satisfaction limit.

**4. Asymmetric sparse regime.** Let \(p_q\sim a/q\), \(r_q\sim b/q^2\). At one key \(|B_u|\sim\operatorname{Binomial}(q,r_q)\): the probabilities of zero, one, or at least two \(Y\)-facts are respectively \(1-b/q+o(q^{-1})\), \(b/q+o(q^{-1})\), and \(O(q^{-2})\). Given precisely one \(Y\)-fact with value \(c\), the violation count is \(|A_u\setminus\{c\}|\sim\operatorname{Binomial}(q-1,p_q)\), whose PGF converges to \(e^{a(t-1)}\). Hence
\[
G_q(t;p_q,r_q)=1+\frac bq(e^{a(t-1)}-1)+o(q^{-1}),
\]
for every fixed \(0\le t\le1\). Taking the \(q\)-th power yields \(\exp\{b(e^{a(t-1)}-1)\}\). This is precisely the PGF of \(\sum_{i=1}^N J_i\) with the stated independent Poisson variables. The limiting PGF is continuous at one, so PGF convergence yields convergence in distribution. At zero it gives \(\exp\{-b(1-e^{-a})\}\). Its mean and variance are \(b\mathbb E J_1=ab\) and \(b\mathbb E[J_1^2]=ab(1+a)\).

**5. Same first moment.** The expectation of the explicit violation sum is, for every \(q\),
\[
\mathbb E W_q=q^2(q-1)pr.
\]
Substitution shows it tends to \(ab\) under both scalings. Since \(1-e^{-a}<a\), the two zero-violation limits are strictly different for positive \(a,b\). This completes the comparison.

## Verification

A standalone Python 3 checker, `verify_polydependence.py`, enumerates **all** pairs of subset relations for \(q=1,2,3\), compares their entire violation-count distributions against independent key-wise convolutions, and independently confirms the zero-count formula and the expected violation count. It additionally checks the exact Bernoulli satisfaction identity in 56 numerical parameter cases and evaluates convergence at three larger alphabet sizes. Invoke `python3 verify_polydependence.py`. The final output terminates with `VERIFY_OK`.

Those finite tests corroborate the finite formulas and sample convergence, but cannot by themselves certify the asymptotic limits; the proof above supplies the required general probability argument.

## Relationship to prior work

Hannula, Kontinen and Virtema [1, §2.2] defined the precise cross-team dependence atom and studied its implication and expressive power; their result does not supply an independent-Bernoulli satisfaction polynomial or these two critical laws. Demetrovics, Katona, Miklós, Seleznjev and Thalheim [2, §2, Theorem 1] established an asymptotic \(e^{-\lambda}\) law for traditional functional dependencies in a single database with a fixed number of independent random tuples. Their single-table sampling law does not imply the present asymmetric compound-Poisson result for independently sampled *two-table* relations. Amarilli and Kimelfeld [3] studied the complexity of reliability for Boolean self-join-free conjunctive queries under tuple-independent probability models; reliability/model counting as a general framework is antecedent, but their theorems do not state this exact cross-team violation PGF or the contrasting infinite-law limits. In particular, a general model-counting formulation is not claimed as new.

## Limitations

Only independent Bernoulli presence/absence sampling, one unary key and one unary value per relation, and the two stated critical scaling regimes are treated. Neither arbitrary correlations nor tuples with duplicate multiplicity are covered. No quantitative total-variation error estimate or intermediate scaling phase diagram is established. Earlier literature on compound-Poisson subgraph or conjunctive-query counts may contain equivalent results under different terminology; the mathematical comparison is not an assertion of exhaustive historical novelty.

## References

[1] M. Hannula, J. Kontinen, J. Virtema, “Polyteam Semantics,” arXiv:1704.02158 (first posted 2017-04-07), §2.2, https://arxiv.org/abs/1704.02158 .

[2] J. Demetrovics, G. O. H. Katona, D. Miklós, O. Seleznjev, B. Thalheim, “Asymptotic properties of keys and functional dependencies in random databases,” *Theoretical Computer Science* **190** (1998), 151–166, §2, https://www.renyi.hu/~ohkatona/paper_87.pdf .

[3] A. Amarilli, B. Kimelfeld, “Uniform Reliability of Self-Join-Free Conjunctive Queries,” *Logical Methods in Computer Science* **18** (2022), no. 4; arXiv:1908.07093, https://arxiv.org/abs/1908.07093 .
