# Exact prime-support fibers of periodic Dedekind-psi dynamics

## Finding
Let \(\psi(n)=n\prod_{p\mid n}(1+1/p)\) be the Dedekind psi function, and let \(T(n)=\psi(n)-n\). Fix any integer \(r\geq1\) and any ordered word \(\boldsymbol S=(S_0,\ldots,S_{r-1})\) of nonempty finite sets of rational primes. Define the *rooted fiber*
\[
\mathcal F(\boldsymbol S)=\{n\geq2:T^r(n)=n,\ \operatorname{supp}(T^i(n))=S_i\ (0\leq i<r)\},
\]
where \(\operatorname{supp}(m)\) is the set of prime divisors of \(m\). The following gives a finite, exact criterion for nonemptiness, every member when nonempty, its exact dynamical period, and the fiber's counting asymptotic.

Put \(U=\bigcup_i S_i\), \(K=\bigcap_i S_i\), and
\[
D_i=\prod_{p\in S_i}p,\qquad A_i=\prod_{p\in S_i}(p+1)-D_i>0.
\]
First require the integer identity \(\prod_{i=0}^{r-1}A_i=\prod_{i=0}^{r-1}D_i\). If it fails, the fiber is empty. If it holds, for each \(p\in U\) set
\[
h_{0,p}=0,\quad h_{i,p}=\sum_{j=0}^{i-1}\bigl(\nu_p(A_j)-\mathbf1_{p\in S_j}\bigr)\quad(1\leq i\leq r).
\]
For each \(p\in U\setminus K\), choose an index \(j_p\) with \(p\notin S_{j_p}\), and put \(b_p=-h_{j_p,p}\). Check the finite conditions
\[
b_p+h_{i,p}=0\quad(p\notin S_i),\qquad
b_p+h_{i,p}\geq1\quad(p\in S_i)
\]
for every \(p\in U\setminus K\) and every \(0\leq i<r\). If any condition fails, the fiber is empty. Otherwise define \(b_p=\max_{0\leq i<r}(1-h_{i,p})\) for \(p\in K\), and \(n_*=\prod_{p\in U}p^{b_p}\). Then
\[
\boxed{\mathcal F(\boldsymbol S)=\left\{n_*\prod_{p\in K}p^{t_p}:t_p\in\mathbb Z_{\geq0}\right\}.}
\]
In particular, the root is unique when \(K\) is empty; otherwise the fiber is a free prime-power lattice of rank \(d=|K|\). Every member has exact dynamical period equal to the least cyclic period of the support word \(\boldsymbol S\) (not necessarily \(r\)). This periodic-word assertion includes the case of a repeated shorter word.

For \(X\geq n_*\), let \(N_{\boldsymbol S}(X)=|\mathcal F(\boldsymbol S)\cap[1,X]|\). If \(d=0\), then \(N_{\boldsymbol S}(X)=1\); for \(d\geq1\), writing \(Y=\log(X/n_*)\),
\[
\boxed{N_{\boldsymbol S}(X)=\frac{Y^d}{d!\prod_{p\in K}\log p}
+O_{\boldsymbol S}\bigl((1+Y)^{d-1}\bigr).}
\]
If \(X<n_*\), the count is zero. Thus any nonempty fiber with at least one persistent prime has an explicit polylogarithmic growth law.

## Assumptions and scope
The theorem applies to every finite length \(r\geq1\) and every specified word of **nonempty finite prime sets**, with no bound on the primes, word length, or prime exponents. Its fibers count starting integers with the specified *ordered* itinerary, not cyclically unrooted orbits. The map is considered on positive integers; \(T(1)=0\), so an orbit containing \(1\) is not a positive periodic orbit. The symbols \(\nu_p\), \(\operatorname{supp}\), and \(\mathbf1\) mean the usual prime valuation, prime-divisor support, and indicator respectively. All tests use finite integer products, factorizations, and comparisons. The result does not classify which prime-set words arise when the word itself is unrestricted.

## Proof
**Step 1: the local transition.** Whenever \(\operatorname{supp}(m)=S_i\), the defining product for \(\psi\) gives the exact rational identity
\[
T(m)=m\frac{A_i}{D_i}.
\]
Consequently a positive periodic orbit with the proposed word must satisfy \(\prod_i A_i/D_i=1\). Under this product identity, no prime outside \(U\) divides any \(A_i\): such a prime would divide the left integer product but not the right. Moreover, for any \(p\in U\) the successive prime valuations of the prescribed formal orbit are \(\nu_p(m)+h_{i,p}\). The product identity also gives \(h_{r,p}=0\).

**Step 2: necessity and uniqueness of the exponent constraints.** If \(p\in U\setminus K\), there is an index \(j_p\) at which \(p\) is absent. The valuation there must be exactly zero; therefore the initial valuation is forced to be \(-h_{j_p,p}=b_p\). At every other index it must be zero for an absent prime and at least one for a present prime, giving precisely the stated checks. If \(p\in K\), the prime occurs at every index and the necessary inequalities are \(\nu_p(m)\geq1-h_{i,p}\) for every \(i\), equivalently \(\nu_p(m)\geq b_p\). These are all valuation restrictions: primes outside \(U\) are forbidden and no other primes can appear during the orbit.

**Step 3: sufficiency.** If the integer product condition and finite valuation checks hold, \(b_p\) is nonnegative for \(p\in U\setminus K\) (its index-zero valuation is either zero or at least one), and \(b_p\geq1\) for \(p\in K\). Hence \(n_*\) is a positive integer supported on exactly \(S_0\). For arbitrary nonnegative \(t_p\) on \(K\), define
\[
m_i=n_*\left(\prod_{p\in K}p^{t_p}\right)\prod_{j=0}^{i-1}\frac{A_j}{D_j},\qquad 0\leq i\leq r.
\]
For every prime in \(U\), the valuation at step \(i\) equals the chosen initial exponent plus \(h_{i,p}\), and has exactly the zero/positive pattern required by \(S_i\). For every prime outside \(U\) the valuation is zero by Step 1. Each \(m_i\) is therefore an integer with precisely the desired support, and the local transition identity proves \(m_{i+1}=T(m_i)\). Product balance yields \(m_r=m_0\). Steps 2 and 3 establish both the exact fiber and its canonical root.

**Step 4: exact period.** Let \(s\mid r\) be the least period of the cyclic support word. Then \(A_i/D_i\) repeats with period \(s\). Put \(c=\prod_{i=0}^{s-1}A_i/D_i>0\). Since the full product is one, \(c^{r/s}=1\), whence \(c=1\) and \(T^s(m_0)=m_0\). Conversely any shorter dynamical period would force that same shorter period on the support word. Therefore the two least periods coincide.

**Step 5: the count.** The fiber formula gives a bijection between rooted points \(n\leq X\) and lattice points \((t_p)_{p\in K}\in\mathbb Z_{\geq0}^{d}\) satisfying \(\sum_{p\in K}t_p\log p\leq Y\). For \(d\geq1\), surrounding each lattice point with its unit half-open cube sandwiches the count between the volumes of the simplices of weighted radii \(Y\) and \(Y+\sum_{p\in K}\log p\). Their volumes are \(Y^d/(d!\prod\log p)\) and \((Y+O_{\boldsymbol S}(1))^d/(d!\prod\log p)\), respectively; their difference gives the claimed error. The zero-dimensional case is immediate.

**Explicit genuine two-cycle.** For \(S_0=\{2,5,7,19\}\) and \(S_1=\{2,5,31\}\), the successive ratios are \(155/133\) and \(133/155\), the canonical root is \(1330\), and \(K=\{2,5\}\). Therefore every starting point with this ordered support word is exactly \(1330\cdot2^a5^b\), \(a,b\geq0\), with second point \(1550\cdot2^a5^b\). The pair has exact period two and its rooted counting function is asymptotic to \((\log X)^2/(2\log2\log5)\).

**A necessary obstruction beyond product balance.** The word \((\{2,7\},\{2,3,5\})\) passes product balance, because its transition ratios are \(5/7\) and \(7/5\), but its fiber is empty: prime \(3\) is absent initially and cannot appear after multiplication by \(5/7\). This demonstrates why the valuation checks are essential, rather than a restatement of product balance.

## Verification
The standalone standard-library program `verify.py` factors integers by trial division and implements the criterion using exact integer arithmetic. It independently enumerates all positive two-step periodic points with initial value at most \(25000\), groups them by ordered prime-support word, and compares every resulting fiber count with the criterion. It also checks the fixed-point family, the explicit two-cycle, absent-word rejection, and twenty-five higher-exponent scalings of the two-cycle. Run `python3 verify.py`; the recorded result is in `verify_output.txt`. The tests corroborate, but do not replace, the general argument in Steps 1–5.

## Relationship to prior work
Guo [1] proves that positive periodic points of \(T\) of each prescribed fixed period have asymptotic density zero, using almost-all prime-divisor persistence; that theorem does not supply an exact criterion for a specified finite support itinerary or its free-lattice fiber and polylogarithmic counting law. Dimitrov [2] studies \(\psi\)-amicable numbers (two-cycles), proves density zero, lists examples, and presents a separate multiplicative construction for a different notion of \(\psi\)-amicable tuples. OEIS A323329 [3] already tabulates the familiar pair \((1330,1550)\), and OEIS A033845 [4] already gives the entire fixed-point family. Those examples and the fixed-point classification are **not** claimed to be new. The result here is the all-length necessary-and-sufficient prime-support-word test, canonical fiber, exact least-period relation, and counting law. A failed literature search is not a proof of uniqueness, and possible unindexed equivalent formulations remain a limitation.

## Limitations
The test fixes the support itinerary as input; it does **not** decide whether there exist cycles of any given new length without specifying prime sets, and it does not improve Guo's global counting estimate for the union of all support words. The individual fiber asymptotics cannot be summed over infinitely many words without uniform error control. The elementary character of the transition identity means alternative presentations may already exist. No independent mathematical audit or external certification has been performed.

## References
[1] A. Guo, *Normal Behavior and Periodic Points of a Pseudo-Aliquot Map Associated with the Dedekind Psi Function*, arXiv:2609.06332v1 (first posted 2026-09-06), https://arxiv.org/html/2609.06332v1.

[2] S. I. Dimitrov, *On \(\psi\)-amicable numbers and their generalizations*, arXiv:2508.02318v2 (first posted 2025-08-04), https://arxiv.org/html/2508.02318v2.

[3] OEIS A323329, pseudo-aliquot amicable pair starters, https://oeis.org/A323329.

[4] OEIS A033845, Dedekind-psi perfect numbers, https://oeis.org/A033845.
