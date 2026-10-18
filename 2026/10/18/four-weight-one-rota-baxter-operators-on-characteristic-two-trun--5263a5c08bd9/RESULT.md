# Four weight-one Rota–Baxter operators on characteristic-two truncated polynomial chains

## Finding

Let \(K\) be **any field of characteristic \(2\)**, let \(n\ge 2\) be an integer, and set
\[
A_n=K[t]/(t^n),\qquad \mathfrak m=(t),\qquad
\pi\!\left(\sum_{i=0}^{n-1}a_it^i\right)=a_0.
\]
A weight-one Rota–Baxter operator is a \(K\)-linear map \(P:A_n\to A_n\) satisfying
\[
P(a)P(b)=P\bigl(P(a)b+aP(b)+ab\bigr)
\qquad(a,b\in A_n).
\]
Then the **complete** set of such operators is
\[
\boxed{\{0,\ \operatorname{id},\ \pi,\ \operatorname{id}-\pi\}.}
\]
In particular, there are exactly four operators over every finite field \(\mathbb F_{2^f}\), independent of \(f\) and \(n\); their ranks, counted with multiplicity, are \(0,1,n-1,n\). The classification remains valid for infinite characteristic-two fields. All four are fixed under conjugation by algebra automorphisms of \(A_n\).

## Assumptions and scope

The algebra is associative, unital, commutative, finite-dimensional, and a one-generator split local \(K\)-algebra. There is no finiteness assumption on the field itself. The operator is required to be \(K\)-linear and its weight is one. The integer \(n\) is at least two; for \(n=1\) the constants and identity maps coincide and the distinct-operator count is two.

## Proof

**Step 1: characteristic two forces an idempotent linear operator.** Write \(u=P(1)\). Substituting \(a=b=1\) in the Rota–Baxter identity, and using \(2=0\), gives
\[
u^2=P\bigl(2u+1\bigr)=P(1)=u.
\]
The only multiplicative idempotents in a local ring are \(0\) and \(1\); thus \(P(1)\in\{0,1\}\). Substituting \(a=1\) and an arbitrary \(b\) gives
\[
u P(b)=P\bigl(P(b)+ub+b\bigr).
\]
If \(u=0\), this reads \(0=P^2(b)+P(b)\), hence \(P^2=P\) in characteristic two. If \(u=1\), it reads \(P(b)=P^2(b)\). In both cases \(P\) is an idempotent \(K\)-linear map.

**Step 2: splitting characterization.** For any idempotent linear map \(P\) in characteristic two, the weight-one Rota–Baxter identity is equivalent to both \(B=\operatorname{im}P\) and \(C=\ker P\) being subalgebras (not necessarily unital). In the forward direction, substituting elements of \(B\) and using \(P|_B=\operatorname{id}\) shows \(P(b_1b_2)=b_1b_2\). Substituting elements of \(C\) shows \(P(c_1c_2)=0\). Conversely, for \(a=b_1+c_1\), \(b=b_2+c_2\), direct expansion cancels both mixed products in characteristic two, leaving
\[
P(a)b+aP(b)+ab=b_1b_2+c_1c_2.
\]
Applying \(P\) yields \(b_1b_2=P(a)P(b)\). Thus the characterization is an equivalence, with \(A_n=B\oplus C\) as vector spaces.

**Step 3: two elementary subalgebra facts.** First, if a subalgebra \(S\subseteq A_n\) contains an element \(v\) with nonzero constant term \(c\), then \(1\in S\). Indeed, \((v-c)^n=0\); expanding this identity and rearranging its nonzero constant term expresses \(1\) as a \(K\)-linear combination of the positive powers \(v,v^2,\ldots,v^n\), all in \(S\). Consequently a subalgebra not containing \(1\) is contained in \(\mathfrak m\).

Second, if a subalgebra \(S\) contains \(w=a_1t+\cdots+a_{n-1}t^{n-1}\), with \(a_1\ne0\), then \(\mathfrak m\subseteq S\). The \(n-1\) powers \(w,w^2,\ldots,w^{n-1}\) are triangular relative to \(t,t^2,\ldots,t^{n-1}\), with nonzero diagonal entries \(a_1,a_1^2,\ldots,a_1^{n-1}\). Thus these powers form a basis of \(\mathfrak m\).

**Step 4: classify the splittings.** First suppose \(P(1)=0\). Then \(1\in C\), whereas \(1\notin B\); by Step 3, \(B\subseteq\mathfrak m\). If \(C\) contains an element whose coefficient of \(t\) is nonzero, subtracting its scalar part (which lies in \(C\)) and applying Step 3 gives \(\mathfrak m\subseteq C\). Therefore \(C=A_n\), \(B=0\), and \(P=0\).

Otherwise every element of \(C\) has zero coefficient of \(t\). Since \(A_n=B\oplus C\), decomposing \(t\) shows that \(B\) contains an element with nonzero \(t\)-coefficient. The second subalgebra fact then gives \(\mathfrak m\subseteq B\), so \(B=\mathfrak m\) and dimension forces \(C=K1\). Hence \(P=\operatorname{id}-\pi\).

Finally suppose \(P(1)=1\). The complementary projection \(Q=\operatorname{id}-P\) has \(Q(1)=0\) and interchanges the two complementary subalgebras. By Step 2 it is also a weight-one Rota–Baxter operator. Therefore \(Q=0\) or \(Q=\operatorname{id}-\pi\), giving \(P=\operatorname{id}\) or \(P=\pi\). These four maps are distinct for \(n\ge2\), and each has image and kernel among \(0,K1,\mathfrak m,A_n\), all subalgebras, so all four satisfy the identity. This proves both necessity and sufficiency.

Every \(K\)-algebra automorphism of \(A_n\) fixes \(1\) and preserves the unique maximal ideal \(\mathfrak m\), hence commutes with \(\pi\) and all four listed operators. Their ranks follow immediately.

## Verification

The standalone standard-library program `verify.py` exhaustively enumerates **every** linear operator and checks the defining identity on all unordered pairs of monomial basis elements, which suffices by bilinearity. It reproduces exactly four operators for \((q,n)=(2,2),(2,3),(2,4),(4,2),(4,3),(8,2),(16,2)\). The respective exhaustive map-space sizes are \(16,512,65536,256,262144,4096,65536\). The checks are finite confirmations only; the proof above establishes the arbitrary-field and arbitrary-length statement.

## Relationship to prior work

Farooq, *Rota–Baxter Operators on Truncated Polynomial Algebras* (arXiv:2605.15670v1, first posted 15 May 2026), classifies weights zero and one on the **square-zero** multivariate algebra \(K[x_1,\ldots,x_s]/(x_1,\ldots,x_s)^2\) over characteristic-zero fields. Its weight-one solutions are parametrized by idempotent matrices. The present statement instead treats every nilpotency length of the **one-variable** algebra over characteristic two and proves no additional operators arise when higher powers survive. The distinction is in both the field characteristic and the length of the nilpotent filtration. The splitting-projection mechanism itself is standard and is not claimed as new.

Zheng, Guo and Rosenkranz (2019) classify **weight-zero** Rota–Baxter operators on certain semigroup algebras of orders two and three, using a different underlying family and weight. Related cutoff constructions on generalized power-series algebras furnish examples of splitting operators but do not, from the material inspected, establish exhaustiveness in the current class.

## Limitations

No statement is made about weight-zero maps, nonzero weights other than the immediate scalar rescaling, arbitrary multivariate truncations, coefficient rings that are not fields, or infinite-length power-series algebras. The exhaustive computations cover finitely many fields and dimensions, not all possibilities. Exhaustiveness of published-literature searching cannot be guaranteed; a broader unindexed theorem about characteristic-two chain algebras could subsume this conclusion. No independent audit has been performed.

## References

1. A. Farooq, *Rota–Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1 (15 May 2026), https://arxiv.org/html/2605.15670v1 ; full text inspected, especially Sections 1–4.
2. S. Zheng, L. Guo, and M. Rosenkranz, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, Communications in Algebra 47 (2019), DOI:10.1080/00927872.2018.1552278 ; abstract, setup, and concluding scope inspected.
3. S. Zheng, L. Guo, and M. Rosenkranz, *Rota–Baxter operators on the polynomial algebra, integration and averaging operators*, Pacific Journal of Mathematics 275 (2015), 481–507, arXiv:1407.5306 ; background on polynomial algebras rather than truncated finite local rings.
