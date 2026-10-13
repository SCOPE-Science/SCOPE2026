# A sharp cubic renewal minorant disproves four-step maximality

## Finding

Let \(X_1,X_2,\ldots\) be independent, identically distributed variables taking values in \(\{1,2,3,4\}\) with respective probabilities \(a,b,c,d\geq0\), where \(a+b+c+d=1\). Set \(S_0=0\), \(S_j=X_1+\cdots+X_j\), and define the renewal masses \(u_n=\Pr(n\in\{S_j:j\geq0\})\). For all choices of these probabilities,

\[
\min_{n\geq1}u_n
\;\geq\;
P(a,b,c,d):=a(a+b)(a+b+c)+2abd.
\]

Write \(Q_4=a(a+b)(a+b+c)\) for the polynomial minorant of Nikolov and Savov. The new cubic polynomial \(P=Q_4+2abd\) dominates \(Q_4\) on the entire probability simplex and strictly dominates it exactly where \(abd>0\). After substituting \(d=1-a-b-c\), \(P\) has total degree at most three in the three free coordinates. It lies in both polynomial classes \(\mathcal A_4\) and \(\widehat{\mathcal A}_4\) of Nikolov–Savov, so their Conjecture 3.7 is false in **both** its maximality and restricted-largest clauses, already at the first case beyond their proved \(k=3\) result.

The coefficient \(2\) is sharp within the one-parameter improvement family: for each \(\lambda\geq0\), the polynomial \(Q_4+\lambda abd\) is a global lower minorant of the renewal masses if and only if \(\lambda\leq2\).

## Assumptions and scope

All probability vectors, including boundary vectors with zero entries, are permitted. Every \(u_n\) is a probability, and \(u_0=1\). The domain is the closed simplex \(\Delta_4=\{(a,b,c,d):a,b,c,d\geq0,\ a+b+c+d=1\}\).

Here \(\mathcal A_4\) denotes the polynomials in \((a,b,c)\) of total degree at most three which do not exceed the minimum renewal mass for any point of \(\Delta_4\), with \(d=1-a-b-c\). For the source's restricted class \(\widehat{\mathcal A}_4\), introduce cumulative coordinates \(x=a\), \(y=a+b\), \(z=a+b+c\), so that \(0\leq x\leq y\leq z\leq1\). In addition to belonging to \(\mathcal A_4\), a polynomial in \(\widehat{\mathcal A}_4\) must have degrees at most one, two, and three upon the successive restrictions \(y=z=1\), \(z=1\), and no restriction, respectively.

## Proof

**Minimum reduction.** The renewal recursion is
\[
 u_n=\sum_{j=1}^{\min\{n,4\}}p_j u_{n-j},\qquad
 (p_1,p_2,p_3,p_4)=(a,b,c,d),\qquad u_0=1.
\]
It gives \(u_1=a\), \(u_2=a^2+b\), and \(u_3=a^3+2ab+c\). Set \(m=\min\{u_1,u_2,u_3\}\leq1\). For every \(n\geq4\), \(u_n\) is a convex combination of its previous four values. Since \(u_0,u_1,u_2,u_3\geq m\), induction yields \(u_n\geq m\) for all \(n\), hence
\[
\min_{n\geq1}u_n=\min\{a,\ a^2+b,\ a^3+2ab+c\}.
\]
This argument also handles reducible and periodic boundary distributions.

**Global cubic lower bound.** With \(P=a(a+b)(a+b+c)+2abd\), direct use of \(a+b+c+d=1\) gives the three polynomial identities
\[
\begin{aligned}
 u_1-P&=a\bigl[(c+d)^2+bc+a(c+2d)\bigr],\\
 u_2-P&=a^2d+b\bigl[(b+c+d)^2+a(b+c)\bigr],\\
 u_3-P&=ab^2+c\bigl[(b+c+d)^2+a(3b+2c+2d)\bigr].
\end{aligned}
\]
Every term on the right is nonnegative throughout \(\Delta_4\). Therefore \(P\leq\min\{u_1,u_2,u_3\}=\min_{n\geq1}u_n\). The improvement \(P-Q_4=2abd\) is positive whenever \(abd>0\).

**Restricted-class membership and the conjecture.** In cumulative coordinates,
\[
 \widehat P(x,y,z)=xyz+2x(y-x)(1-z).
\]
It has total degree three; its restrictions are \(\widehat P(x,y,1)=xy\) (degree two) and \(\widehat P(x,1,1)=x\) (degree one). Hence \(P\in\widehat{\mathcal A}_4\subseteq\mathcal A_4\). As \(P\geq Q_4\) everywhere with strict inequality on a nonempty open set, \(Q_4\) cannot be maximal in \(\mathcal A_4\) or largest in \(\widehat{\mathcal A}_4\).

**Sharp coefficient.** Since the bound holds for \(\lambda=2\), and \(Q_4\leq P\) already, it holds for \(0\leq\lambda\leq2\). Conversely, on the face \(c=0\),
\[
 u_3-[Q_4+\lambda abd]=ab\bigl[b+(2-\lambda)d\bigr].
\]
For any \(\lambda>2\), choose \(d=1/2\), \(0<b<\min\{1/2,(\lambda-2)/2\}\), and \(a=1/2-b\). Then \(u_3<Q_4+\lambda abd\), ruling out such a coefficient. This proves sharpness without an optimization algorithm.

## Verification

Run `python3 verify.py` using Python's standard library. The checker constructs exact multivariate rational-coefficient polynomials and verifies each of the three displayed residual identities coefficient by coefficient; all resulting certificate coefficients are nonnegative. It separately checks 20,474 rational simplex points with denominators at most 24, an interior strict witness, and the sharp-coefficient obstruction. Exact polynomial identities, not the finite grid, establish the global inequalities.

For example, at \((a,b,c,d)=(1/4,1/4,1/4,1/4)\), one has \(P-Q_4=1/32>0\). The proof gives the result for the full continuous simplex, not merely this example or the checked grid.

## Relationship to prior work

Nikolov and Savov, *Properties and Conjectures Regarding Discrete Renewal Sequences*, arXiv:2307.00545 (first posted 2023-07-02; published in *Mathematics and Informatics* 67 (2024), 111–118), introduce the polynomial \(Q_k\), establish it as a lower minorant (Proposition 3.5), and conjecture that it is maximal in \(\mathcal A_k\) and largest in \(\widehat{\mathcal A}_k\) for every \(k\geq3\) (Conjecture 3.7). Their Proposition 3.8 proves that assertion for \(k=3\). Their published text and preprint do not state the above \(k=4\) counterexample. The present finding supplies a dominating admissible polynomial in both of their exact comparison classes. The standard renewal equation and the earlier lower bound for \(Q_k\) are not claimed as new.

## Limitations

This result disproves the two universal clauses of Conjecture 3.7 but does not classify maximal lower minorants at \(k=4\), find a largest element of the restricted class, or decide analogous properties for \(k\geq5\). Sharpness of \(2\) applies only to the explicitly stated one-parameter family \(Q_4+\lambda abd\), not to all degree-three polynomial improvements. Bibliographic priority outside the inspected sources is not independently certified.

## References

1. N. Nikolov and M. Savov, *Properties and conjectures regarding discrete renewal sequences*, arXiv:2307.00545, first publicly posted 2023-07-02, https://arxiv.org/abs/2307.00545.
2. N. Nikolov and M. Savov, *Properties and Conjectures Regarding Discrete Renewal Sequences*, *Mathematics and Informatics* **67** (2024), 111–118, DOI:10.53656/math2024-2-1-pro, https://journals.azbuki.bg/mathinfo/properties-and-conjectures-regarding-discrete-renewal-sequences/view.
