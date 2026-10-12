# Binary-carry thresholds for maximal abelian ideals in modular null-filiform Zinbiel algebras

## Finding

Fix any field \(K\) of characteristic \(2\), and any integer \(n\ge2\). Let \(N_n(K)\) be the \(n\)-dimensional Zinbiel algebra with basis \(e_1,\ldots,e_n\) and multiplication
\[
e_i\circ e_j=
\begin{cases}
\binom{i+j-1}{j}e_{i+j},&i+j\le n,\\
0,&i+j>n,
\end{cases}
\]
where the binomial coefficient is computed over the integers and reduced in \(K\). This is the characteristic-two instance of the standard null-filiform multiplication in Ceballos–Towers, Proposition 4.2.

For \(1\le j\le n\), put
\[
A_j=\operatorname{span}_K\{e_j,e_{j+1},\ldots,e_n\},
\qquad A_{n+1}=0,
\]
and let \(t(j)\) be the least power of \(2\) greater than or equal to \(j\).

**Exact abelian-ideal cutoff.** Every two-sided ideal is precisely one \(A_j\), and
\[
\boxed{A_j\circ A_j=0\quad\Longleftrightarrow\quad j+t(j)>n.}
\]
More precisely, before truncation the least total degree of a nonzero product of basis elements in \(A_j\) is exactly \(j+t(j)\). Hence the smallest index of an abelian tail is
\[
\boxed{j_*=\max\{2^{r-1}+1,\;n-2^r+1\},\qquad r=\lfloor\log_2 n\rfloor.}
\]
The **unique** largest abelian ideal is \(A_{j_*}\), and its dimension is
\[
\boxed{\beta(N_n(K))=\min\{2^r,\;n-2^{r-1}\}.}
\]
This formula is field-independent within characteristic \(2\).

Ceballos–Towers prove over \(\mathbb C\) that the same integral multiplication has
\[
\beta(N_n(\mathbb C))=n-\lfloor n/2\rfloor=\lceil n/2\rceil.
\]
For every integer \(r\ge2\), choosing \(n=3\cdot2^{r-1}\) yields
\[
\beta(N_n(K))=2^r,
\qquad
\beta(N_n(\mathbb C))=3\cdot2^{r-2}.
\]
Thus the characteristic-two excess is exactly \(2^{r-2}\), and grows without bound.

## Assumptions and scope

The result concerns the explicitly defined, canonical one-generated null-filiform family \(N_n(K)\) in arbitrary characteristic-two fields. It does **not** claim an invariant for every Zinbiel algebra, nor for other characteristics. The formula counts maximal-dimensional **abelian two-sided ideals**, not all abelian subalgebras.

The multiplication is valid as a Zinbiel product over any field: its structure constants satisfy the integer Zinbiel identity and may be reduced modulo \(2\). Moreover \(e_1\circ e_i=e_{i+1}\) for \(i<n\); hence the chain of powers is \(N_n(K)^j=A_j\), making the family null-filiform.

The primary inspiration is Ceballos–Towers, whose Proposition 4.2 establishes the complex-field cutoff and uniqueness of the largest abelian ideal. The extension here keeps the same integral multiplication but analyzes modular vanishing of its binomial coefficients.

## Proof

**1. The product and all ideals.** For basis elements with total degree at most \(n\), the Zinbiel identity
\[
(x\circ y)\circ z=x\circ(y\circ z)+x\circ(z\circ y)
\]
reduces to the integer binomial identity
\[
\binom{i+j-1}{j}\binom{i+j+k-1}{k}
=
\left(\binom{j+k-1}{k}+\binom{j+k-1}{j}\right)
\binom{i+j+k-1}{j+k}.
\]
It follows directly from the factorial formulas or from Pascal's identity. If a total degree exceeds \(n\), both sides vanish by truncation. Thus the product defines a Zinbiel algebra in characteristic \(2\).

The equality \(e_1\circ e_i=e_{i+1}\) for \(i<n\) shows that left multiplication \(L_{e_1}\) is a single nilpotent Jordan block. Every two-sided ideal is invariant under \(L_{e_1}\). The invariant subspaces of a single Jordan block are exactly its tail spans \(A_j\), one in each dimension. Conversely, every \(A_j\) is a two-sided ideal because multiplying a basis vector of index at least \(j\) by any positive-index basis vector can only increase its index. Consequently the complete ideal lattice is
\[
N_n(K)=A_1\supset A_2\supset\cdots\supset A_n\supset A_{n+1}=0.
\]

**2. The binary-carry cutoff.** By the parity form of Lucas's theorem,
\[
\binom{i+k-1}{k}\not\equiv0\pmod2
\quad\Longleftrightarrow\quad
(i-1)\ \mathbin{\&}\ k=0,
\]
where \(\mathbin{\&}\) denotes bitwise intersection of binary digits. This condition is equivalent to carry-free addition of \(i-1\) and \(k\).

Fix \(j\ge1\), and let \(t=t(j)\). Since \(0\le j-1<t\), the binary digits of \(j-1\) and \(t\) are disjoint. Hence
\[
\binom{j+t-1}{t}\equiv1\pmod2
\]
and the product \(e_j\circ e_t\) is nonzero whenever \(j+t\le n\).

Conversely, suppose \(i,k\ge j\) and \(i+k<j+t\). Then \(i<t\) and \(k<t\). If \(j=t\), the inequalities are impossible. Otherwise \(t\) is a power of two satisfying \(t/2<j<t\). Therefore
\[
t/2\le i-1<t,
\qquad t/2<k<t,
\]
so the binary digit \(t/2\) appears in both \(i-1\) and \(k\). Their bitwise intersection is nonzero, the binomial coefficient is even, and \(e_i\circ e_k=0\). Thus no product of elements in \(A_j\) has a nonzero term before total degree \(j+t(j)\). This proves
\[
A_j\circ A_j=0\quad\Longleftrightarrow\quad n<j+t(j).
\]

**3. The largest abelian ideal.** Let \(r=\lfloor\log_2 n\rfloor\), so \(2^r\le n<2^{r+1}\). If \(j\le2^{r-1}\), then \(j+t(j)\le2^r\le n\), so \(A_j\) is not abelian. For indices
\[
2^{r-1}<j\le2^r,
\]
we have \(t(j)=2^r\), and the cutoff becomes \(j>n-2^r\). Because \(n<2^{r+1}\), some index in that range satisfies the inequality. The first such index is
\[
j_*=\max\{2^{r-1}+1,n-2^r+1\}.
\]
The chain of all ideals proves uniqueness. Finally,
\[
\dim A_{j_*}=n-j_*+1
=\min\{n-2^{r-1},2^r\}.
\]

**4. Unbounded characteristic gap.** At \(n=3\cdot2^{r-1}\), for \(r\ge2\), the formula gives \(2^r\), while the complex formula is \(3\cdot2^{r-2}\). Their difference \(2^{r-2}\) is unbounded.

## Verification

The executable `artifacts/verify.py` uses only Python's standard library. It checks the integral binomial Zinbiel identity for all basis triples with indices from \(1\) through \(25\), verifies the Lucas parity criterion through indices \(256\), and independently reconstructs the least nonzero product degree among **both** product orientations for all \(j\le512\) using a search through indices at most \(1024\).

It checks the closed maximal-ideal dimension formula at every integer \(n\) from \(2\) through \(512\). It also exhaustively constructs all linear subspaces of \(\mathbf F_2^n\) for \(2\le n\le6\), checks the two-sided ideal property directly, and finds precisely the \(n+1\) tail ideals and exactly one abelian ideal of maximum dimension. Finally it checks the explicit unbounded-gap instances \(2\le r\le9\).

The checker prints `VERIFY_OK`. These finite checks are independent replay evidence, **not** a proof for all \(n\) or infinite fields; the proof above is uniform.

## Relationship to prior work

Ceballos–Towers, Proposition 4.2, proves the complex-field formula \(\beta=n-\lfloor n/2\rfloor\) and uniqueness for the same binomial multiplication. Their proof relies on the relevant self-product coefficient remaining nonzero and does not extend unchanged to characteristic \(2\), where binomial coefficients vanish according to binary carries. The modular dimension formula here differs already at \(n=6\) (dimension \(4\) rather than \(3\)), with an arbitrarily large discrepancy in higher dimensions.

Camacho–Fernández Ouaridi–Kaygorodov–Navarro, *Zinbiel superalgebras* (2023), recalls a canonical null-filiform multiplication as Theorem 1.4, including an arbitrary-field formulation. That structural classification does not state a maximal abelian-ideal dimension formula in characteristic \(2\). It is compatible with, rather than dominating, the present invariant calculation.

Searches for characteristic-two maximal abelian ideals of null-filiform Zinbiel algebras, modular binomial carry conditions, the exact power-of-two dimension formula, and equivalent square-zero tail cutoffs did not locate a published statement implying this formula.

## Limitations

The exact formula is for the canonical binomial null-filiform family; it is not a statement about all arbitrary Zinbiel algebra families, and it does not determine the maximal abelian **subalgebra** dimension \(\alpha\).

The binary formula uses characteristic \(2\) essentially; different primes require a separate base-prime carry analysis and are not classified here.

Although the two most directly relevant full-text sources were inspected in their pertinent sections, equivalent results might be phrased using nilpotent shift filtrations or modular shuffle algebras. The literature search does not establish absolute historical novelty.

## References

1. M. Ceballos and D. A. Towers, “Abelian subalgebras and ideals of maximal dimension in Zinbiel algebras,” arXiv:2202.03214 (first public 7 February 2022), later *Communications in Algebra* 51 (2023), 1323–1333, DOI `10.1080/00927872.2022.2134409`, especially Proposition 4.2.
2. L. M. Camacho, A. Fernández Ouaridi, I. Kaygorodov, and R. Navarro, “Zinbiel superalgebras,” *New York Journal of Mathematics* 29 (2023), 1341–1362, arXiv:2304.00273, especially Theorem 1.4.
3. É. Lucas, “Théorie des Fonctions Numériques Simplement Périodiques,” *American Journal of Mathematics* 1 (1878), 184–196, 197–240, 289–321 (binomial congruence theorem).
