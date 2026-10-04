# Interior divisor degrees are never unique for two-prime φ-practical numbers
## Finding
Let \(a\ge 1\). For \(n=2^a\), and more generally for
\[
n=2^a p^b,
\]
where \(p\) is an odd prime, \(b\ge 1\), and \(p\le 2^a+1\), define \(N_n(d)\) to be the number of monic divisors of \(X^n-1\) in \(\mathbb Z[X]\) having degree \(d\). Then
\[
N_n(0)=N_n(n)=1,
\]
and
\[
N_n(d)\ge 2\qquad(1\le d\le n-1).
\]
In fact \(N_n(1)=N_n(n-1)=2\), so the minimum multiplicity among all interior degrees is exactly \(2\).

For \(b\ge1\), Thompson's extension criterion shows that the displayed bound \(p\le2^a+1\) is exactly the condition for \(2^a p^b\) to be \(\varphi\)-practical. Thus, on the complete even two-prime-support family, existence of a divisor in every degree automatically strengthens to nonuniqueness in every nontrivial degree.

## Assumptions and scope
All divisors are monic divisors in \(\mathbb Z[X]\). The factorization
\[
X^n-1=\prod_{m\mid n}\Phi_m(X)
\]
is squarefree over \(\mathbb Q[X]\), and the cyclotomic factors are distinct monic irreducibles in \(\mathbb Z[X]\). Therefore every monic divisor corresponds uniquely to a subset of the cyclotomic factors, and its degree is the sum of the corresponding values \(\varphi(m)\).

The theorem covers \(n=2^a\) and every \(n=2^a p^b\) in the \(\varphi\)-practical range. It makes no assertion for \(p>2^a+1\), where some degrees need not occur at all.

## Proof
Put \(A=2^a\). First group the cyclotomic factors according to the exponent of \(p\) in their index. For the pure power-of-two layer, set
\[
H_A(z)=\prod_{i=0}^a\left(1+z^{\varphi(2^i)}\right).
\]
Since the multiset of the exponents \(\varphi(2^i)\) is \(1,1,2,4,\ldots,A/2\),
\[
H_A(z)=(1+z)^2\prod_{r=1}^{a-1}(1+z^{2^r})
       =(1+z)\frac{1-z^A}{1-z}.
\]
Consequently the coefficient \(h_A(x)=[z^x]H_A(z)\) is
\[
h_A(x)=\begin{cases}1,&x=0\text{ or }x=A,\\2,&1\le x\le A-1.\end{cases}
\]

For \(j\ge1\), write
\[
c_j=(p-1)p^{j-1}.
\]
The factors whose indices have exact \(p\)-adic exponent \(j\) contribute \(H_A(z^{c_j})\). Hence the degree-counting polynomial is
\[
F_n(z)=\sum_{d=0}^nN_n(d)z^d
      =H_A(z)\prod_{j=1}^bH_A(z^{c_j}).
\]
Equivalently, every contribution to \(N_n(d)\) comes from a digit vector \(x_0,\ldots,x_b\) with \(0\le x_j\le A\) satisfying
\[
d=x_0+\sum_{j=1}^bc_jx_j,
\]
and that vector contributes the positive weight \(\prod_{j=0}^b h_A(x_j)\).

When \(b=0\), the formula for \(H_A\) already proves the theorem. Assume \(b\ge1\). Thompson's extension lemma applied to \(M=A\) implies that \(p\le A+1\) is precisely the \(\varphi\)-practical range here, so at least one digit vector exists for every \(0\le d\le n\).

Fix \(0<d<n\) and choose a digit vector for \(d\). If one coordinate lies strictly between \(0\) and \(A\), then its contribution has weight at least \(2\), and therefore \(N_n(d)\ge2\). It remains only to treat an endpoint vector \(x_j=A\varepsilon_j\), where each \(\varepsilon_j\) is \(0\) or \(1\). Since \(d\) is interior, this binary vector is neither all zero nor all one. The coefficient sequence of \(F_n\) is symmetric, because taking the complementary subset of cyclotomic factors sends degree \(d\) to degree \(n-d\). We may therefore replace \(d\) by \(n-d\) if necessary and assume \(\varepsilon_0=1\).

Let \(r<b\) be the last index in the initial run
\[
\varepsilon_0=\cdots=\varepsilon_r=1,\qquad \varepsilon_{r+1}=0.
\]
There are two cases.

If \(p\le A-1\), then for \(r=0\) the identity
\[
A=(A-p+1)+(p-1)
\]
replaces the pair \((x_0,x_1)=(A,0)\) by \((A-p+1,1)\). Both new entries are interior. If \(r\ge1\), then \(c_{r+1}=pc_r\) and
\[
Ac_r=(A-p)c_r+c_{r+1},
\]
so \((x_r,x_{r+1})=(A,0)\) may be replaced by \((A-p,1)\), again with interior entries. In either subcase the same degree has a representation whose weight is at least \(2\).

The only remaining possibility is \(p=A+1\). Here \(p-1=A\), and the total degree of all layers from \(0\) through \(r\) is
\[
\sum_{m\mid Ap^r}\varphi(m)=Ap^r=c_{r+1}.
\]
Thus the full initial block \((x_0,\ldots,x_r,x_{r+1})=(A,\ldots,A,0)\) can be replaced by \((0,\ldots,0,1)\). The last coordinate is interior, so this representation again contributes at least \(2\).

Therefore \(N_n(d)\ge2\) for every interior degree. The empty and full subsets are the unique divisors of degrees \(0\) and \(n\). Finally, degree \(1\) can arise only from \(\Phi_1\) or \(\Phi_2\), so \(N_n(1)=2\); complementing gives \(N_n(n-1)=2\). This proves the exact interior minimum.

## Verification
A standalone checker included with this result constructs the cyclotomic-degree subset-sum generating function directly for a finite grid of admissible parameters and verifies that the endpoint coefficients are \(1\), every interior coefficient is at least \(2\), and the coefficients at degrees \(1\) and \(n-1\) equal \(2\). This finite replay is a consistency check only; the proof above is uniform in all parameters.

## Relationship to prior work
Thompson introduced \(\varphi\)-practical numbers through the requirement that \(X^n-1\) possess a divisor of every degree and proved the prime-extension criterion used here. In particular, her Lemma 4.1 gives the complete \(2^a p^b\) existence range. The present statement asks a different, multiplicity-sensitive question: how many divisors can realize a given degree? It shows that throughout this complete two-prime-support range, no interior degree is unique and determines the exact minimum multiplicity.

Targeted searches for phrases involving \(\varphi\)-practical multiplicity, degree-counting coefficients, and numbers of monic divisors of \(X^n-1\) by degree did not locate an equivalent or stronger statement. Related literature found in those searches concerns existence of all degrees or distribution of \(\varphi\)-practical integers, rather than multiplicity within each degree.

## Limitations
The result is restricted to the complete even family with at most one odd prime factor. It does not classify degree multiplicities for general \(\varphi\)-practical integers with three or more distinct prime factors, nor does it give the full coefficient sequence \(N_n(d)\). The literature search cannot exclude an obscure formulation of the same multiplicity statement outside the terminology used here.

## References
1. L. Thompson, “Polynomials with divisors of every degree,” arXiv:1111.5401v1, 23 November 2011; Journal of Number Theory 132 (2012), 1038–1053.
2. OEIS A260653, “Phi-practical numbers,” for the standard sequence terminology and references to later distribution results.
