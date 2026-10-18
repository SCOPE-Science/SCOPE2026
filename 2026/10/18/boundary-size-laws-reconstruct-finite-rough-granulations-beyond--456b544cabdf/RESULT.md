# Boundary-size laws reconstruct finite rough granulations beyond their rough-set lattices

## Finding
Let \(E\) be an equivalence relation on a finite set \(X\), with blocks \(C_1,\ldots,C_r\) of positive sizes \(b_i=|C_i|\). Select each point independently with the same known probability \(p\in(0,1)\) to obtain a random subset \(S\subseteq X\). With Pawlak lower and upper approximations \(L_E\) and \(U_E\), define its boundary \(\partial_E S=U_E(S)\setminus L_E(S)\) and its exact size distribution polynomial \(F_{E,p}(z)=\mathbb E[z^{|\partial_E S|}]\).

**Theorem (exact law and inverse granulation classification).** For every finite equivalence partition,
\[
F_{E,p}(z)=\prod_{i=1}^r \left(q_{b_i}+(1-q_{b_i})z^{b_i}\right),\qquad q_b=p^b+(1-p)^b.
\]
For a fixed known \(p\in(0,1)\), two finite equivalence partitions (even on sets of different cardinalities) have the same boundary-cardinality distribution if and only if they have the same multiset of block sizes at least two. If the cardinality of the universe is also known, their complete multisets of block sizes, hence their partitions up to isomorphism, are determined.

In particular, a single histogram of boundary sizes retains granule sizes not recoverable from the abstract lattice of all rough sets. The coefficients up to degree \(K\) of the normalized polynomial \(F_{E,p}(z)/F_{E,p}(0)\) determine precisely the multiplicities of blocks of each size \(2,\ldots,K\). This is a sharp uniform cutoff even when the total number of points and classes are known: for unbiased sampling and any \(K\ge2\), partitions with sizes \((K+1,K+3)\) and \((K+2,K+2)\) share the coefficients of the **unnormalized** probability law through degree \(K\), yet have different full laws.

## Assumptions and scope
The set \(X\) is finite (possibly empty), \(E\) is an equivalence relation, the sampling law independently selects each point with **known** common parameter \(0<p<1\), and the full probability distribution of the boundary cardinality is available as exact data. The boundary counts points, not equivalence classes. No claim is made for dependent sampling, unknown sampling parameter, or observations limited to a single expectation or finite noisy samples.

## Proof
**(1) Block factorization.** On any block of size \(b\), the boundary includes that entire block if and only if \(S\) intersects it without containing it. The only two ways for the block to contribute zero boundary points are \(S\cap C=\varnothing\) and \(S\cap C=C\), having total probability \(q_b=(1-p)^b+p^b\). Otherwise it contributes exactly \(b\) points. Independence across disjoint blocks proves the displayed product. Note that \(q_1=1\), while for \(b\ge2\) one has \(0<q_b<1\).

**(2) Constructive inversion and uniqueness.** Write \(m_b\) for the number of blocks of size \(b\ge2\) and set \(\rho_b=(1-q_b)/q_b>0\). Since \(F_{E,p}(0)>0\), the normalized polynomial is
\[
R(z)=\frac{F_{E,p}(z)}{F_{E,p}(0)}=\prod_{b\ge2}(1+\rho_b z^b)^{m_b}.
\]
Work in formal power series over the real numbers (or exact rational arithmetic for rational \(p\)). Assume the multiplicities below \(b\) already have been recovered, and divide their corresponding factors out of \(R\) to obtain \(R_b(z)=\prod_{j\ge b}(1+\rho_j z^j)^{m_j}\). Its coefficient of \(z^b\) equals exactly \(m_b\rho_b\), since products of higher-degree terms contribute no such coefficient. Therefore
\[
m_b=[z^b]R_b(z)/\rho_b.
\]
Starting at \(b=2\), the algorithm determines every multiplicity and terminates at the degree of \(F\); division is exact. Conversely, equality of all non-singleton multiplicities implies equality of the product, because singleton factors equal \(1\). If \(|X|\) is known, \(m_1=|X|-\sum_{b\ge2}b m_b\), completing the isomorphism classification. This also proves the asserted coefficient-local recovery for sizes at most \(K\).

**(3) Sharp cutoff at fixed total size and block count.** Take unbiased sampling \(p=1/2\), where \(q_b=2^{1-b}\). For \(K\ge2\), let the two block-size lists be \((K+1,K+3)\) and \((K+2,K+2)\). Both have \(2K+4\) points and two blocks, each larger than \(K\). Both therefore have no nonconstant terms of degree at most \(K\), and the constant products are equal:
\[
2^{1-(K+1)}2^{1-(K+3)}=2^{1-(K+2)}2^{1-(K+2)}=2^{-2K-2}.
\]
Their full laws differ by the inversion theorem, since their non-singleton multisets differ.

**(4) Additional information over the rough-set lattice.** For a singleton class \(C\), the possible pairs \((L_E(S)\cap C,U_E(S)\cap C)\) are \((\varnothing,\varnothing)\) and \((C,C)\), forming a two-element chain. For a block of size at least two, the additional pair \((\varnothing,C)\) is attainable, yielding a three-element chain. Thus the rough-set lattice ordered coordinatewise is \(\mathbf2^{m_1}\times\mathbf3^{\sum_{b\ge2}m_b}\), which remembers no individual non-singleton block sizes. On six points, partitions \((2,4)\) and \((3,3)\) have isomorphic rough-set lattices \(\mathbf3\times\mathbf3\), but at \(p=1/2\) their boundary laws are respectively
\[
\frac{(1+z^2)(1+7z^4)}{16}\qquad\text{and}\qquad\frac{(1+3z^3)^2}{16}.
\]
They are unequal, finishing the structural contrast.

## Verification
A standalone standard-library Python program, `verify_boundary.py`, independently enumerates selected subsets for every integer partition of an \(n\)-point universe for \(0\le n\le9\) and three exact biases \(p=1/2,1/3,2/5\). It compares direct boundary computations with the product polynomial, executes formal-series multiplicity recovery, checks fixed-universe injectivity, and tests the truncated-law collision construction for \(K=2,\ldots,11\). Successful execution prints the actual finite test counts. Enumeration is independent confirmation of finite instances, **not** a substitute for the general proof above.

## Relationship to prior work
Järvinen and Radeleczki (2020) develop approximation operators and the lattice structure of rough sets, including the theory of multigranular systems. Al-shami (2022) discusses topological and rough approximation models, including pointwise boundary/accuracy concepts. Neither inspected source establishes the quantitative inverse theorem for the **full distribution of boundary cardinalities under independently sampled subsets**, or the explicit cutoff construction here. The product-of-independent-blocks method is elementary and no general novelty is claimed for independence, generating functions, or the abstract product-lattice description. The new mathematical statement is the exact inverse classification together with its sharp information-loss boundary and the lattice/distribution separation.

## Limitations
The theorem assumes exact probability values and a known common sampling rate \(p\in(0,1)\); it supplies mathematical identifiability, not a sample-complexity or numerically stable estimation bound. Singleton classes remain invisible without separately knowing universe size. Related identifiability theorems may exist under terminology such as granule-size distributions or rough-set uncertainty polynomials; the accessible literature inspected does not exclude every such formulation. These claims have not undergone an independent external audit.

## References
1. Jouni Järvinen and Sándor Radeleczki, *The structure of multigranular rough sets*, publicly posted February 12, 2020, arXiv:2002.05238, https://arxiv.org/abs/2002.05238 .
2. Tareq M. Al-shami, *Topological approach to generate new rough set models*, published March 14, 2022, DOI:10.1007/s40747-022-00704-x, https://doi.org/10.1007/s40747-022-00704-x .
