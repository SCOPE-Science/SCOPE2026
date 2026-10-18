# Fixed-point-rank census for closures on two-row chain lattices

## Finding
Let \(C_r=\{0,\ldots,r-1\}\) carry the usual order, let \(L_n=C_2\times C_n\) carry the coordinatewise order, and let \(n\ge1\). Define \(\mathcal C_n\) to consist of all extensive, order-preserving, idempotent maps \(c:L_n\to L_n\). The fixed-point-rank polynomial is exactly
\[
F_n(t):=\sum_{c\in\mathcal C_n}t^{|\operatorname{Fix}(c)|}
       =(1+t+t^2)^n-(1+t)^{n-1}.
\]
In particular, the coefficient of \(t^k\) gives the number of closures with exactly \(k\) fixed elements, for every \(1\le k\le2n\). Every such rank occurs. The total number is \(F_n(1)=3^n-2^{n-1}\), a previously known, independently obtained unrefined count (see references).

By the saturated-transfer-system/interior-operator correspondence of Bao et al., the *same* polynomial enumerates saturated transfer systems on the subgroup lattice of the cyclic group \(C_{p q^{n-1}}\), for distinct primes \(p,q\), by the number of fixed subgroup-lattice elements of their associated characteristic interior operators. Equivalently, it counts the subgroups \(H\) admitting **no proper incoming transfer** \(K\mathrel{R}H\) with \(K<H\), since the characteristic map sends \(H\) to the least subgroup having a transfer to \(H\). This is a transported rank refinement, not a claim to a new total count or a new correspondence.

For a uniformly chosen closure from \(\mathcal C_n\), if \(R_n\) is its number of fixed points, then
\[
\frac{R_n-n}{\sqrt{2n/3}}\ \xrightarrow[n\to\infty]{\mathcal D}\ N(0,1).
\]
This distributional consequence follows directly from the exact polynomial. The random variable is sampled from *all* closures on the specified finite lattice; no claim concerns general lattices or arbitrary transfer systems.

## Assumptions and scope
The lattice \(L_n\) consists of the \(2n\) ordered pairs \((\epsilon,j)\), with \(\epsilon\in\{0,1\}\) and \(0\le j<n\). Meets are coordinatewise minima. A closure operator is assumed extensive (\(x\le c(x)\)), order-preserving (\(x\le y\Rightarrow c(x)\le c(y)\)), and idempotent (\(c(c(x))=c(x)\)). No preservation of meets or joins by the closure map is assumed. The set of fixed elements is counted with its actual cardinality, not its lattice-theoretic height or rank.

The transfer-system interpretation uses the subgroup lattice of \(C_{p q^{n-1}}\), which is isomorphic to \(L_n\), and the established bijection from saturated transfer systems to interior operators on that lattice. Here an interior operator is monotone, contractive, and idempotent. Because \(L_n\) is self-dual by reversing both coordinates, these have the same fixed-point counts as closure operators. The theorem includes the \(n=1\) boundary case.

## Proof
**Closure systems.** On a finite lattice \(L\), a subset \(F\subseteq L\) is the fixed-point set of a closure operator if and only if it contains the greatest element and is closed under binary meets. For the forward direction, let \(x,y\in F\): monotonicity gives \(c(x\wedge y)\le c(x)\wedge c(y)=x\wedge y\), while extensivity supplies the reverse inequality, hence equality; the top element is fixed by extensivity. Conversely, given such \(F\), define
\[
c_F(x)=\bigwedge\{z\in F:x\le z\}.
\]
The set is nonempty because it contains the top element; finite meet closure places its meet in \(F\). Thus \(c_F\) is extensive, monotone, idempotent and has precisely \(F\) as its fixed set. These constructions are inverse.

**Two-row criterion.** Write
\[
A=\{j:(0,j)\in F\},\qquad B=\{j:(1,j)\in F\}.
\]
The top-element requirement says \(n-1\in B\). Meets within either row are automatically one of the operands. If \(A=\varnothing\), no further restrictions occur. If \(A\ne\varnothing\), write \(m=\max A\). Meet closure between the two rows is *equivalent* to
\[
B\cap\{0,\ldots,m\}\subseteq A. \tag{1}
\]
Necessity follows by taking the meet of \((0,m)\) and \((1,j)\) for any \(j\le m\) in \(B\). For sufficiency, the meet of \((0,i)\) and \((1,j)\) is \((0,\min(i,j))\); if \(j\ge i\), it is the selected lower-row element, and if \(j<i\le m\), then (1) guarantees that its lower-row coordinate belongs to \(A\). This handles every pair of points and all boundary cases.

**Rank enumeration.** Give a selected lattice element weight \(t\). When \(A=\varnothing\), \(B\) is an arbitrary set containing \(n-1\); its contribution is \(t(1+t)^{n-1}\). Otherwise fix \(m=\max A\), where \(0\le m<n\). At each column \(j<m\), criterion (1) allows exactly three states (neither element; the lower element only; both elements), of weights \(1,t,t^2\). At column \(m\), the lower element is compulsory. Above \(m\), the lower elements are absent. The upper element in the final column is compulsory, while all other upper elements at or above \(m\) are optional. Thus the weight contribution for the given \(m\) is exactly
\[
t^2(1+t+t^2)^m(1+t)^{n-1-m}.
\]
This is valid also at \(m=n-1\), where both final-column elements are compulsory. Put \(a=1+t\) and \(b=1+t+t^2\). Since \(b-a=t^2\), summation gives
\[
\begin{aligned}
F_n(t)&=t a^{n-1}+t^2\sum_{m=0}^{n-1}b^m a^{n-1-m}\\
      &=t a^{n-1}+(b^n-a^n)=b^n-a^{n-1},
\end{aligned}
\]
as asserted. At rank \(k\le n\), choose \(A=\varnothing\) and any \(k\)-element \(B\) containing its top. At rank \(k>n\), choose all \(n\) upper-row points and the first \(k-n\) lower-row points. Both constructions satisfy (1), proving that every \(1\le k\le2n\) occurs.

**Transfer-system interpretation.** For distinct primes \(p,q\), the subgroup lattice of \(C_{p q^{n-1}}\) has elements indexed by the two choices of the exponent of \(p\) and the \(n\) choices of the exponent of \(q\); its order is the product order on \(L_n\). Bao et al., Theorem 2.8 and Remark 2.9, give a bijection between saturated transfer systems on a finite lattice and interior operators, via Hill's characteristic map. The map \(\rho(\epsilon,j)=(1-\epsilon,n-1-j)\) is an order-reversing involution of \(L_n\); conjugating an interior operator by \(\rho\) produces a closure operator with the same number of fixed points. By the definition of the characteristic map \(\chi_R(H)=\min\{K:K\mathrel{R}H\}\), its fixed points are exactly the subgroups \(H\) for which no proper subgroup \(K<H\) transfers to \(H\). Thus the polynomial counts saturated transfer systems by the number of such transfer-minimal subgroup targets. Evaluating at \(t=1\) gives the known total from Hafeez et al.'s enumeration, as it must.

**Asymptotic law.** Let \(S_n\) be the sum of \(n\) independent uniform random variables on \(\{0,1,2\}\), and let \(T_{n-1}\) be the sum of \(n-1\) independent fair Bernoulli variables. Write \(D_n=3^n-2^{n-1}\). The generating-function identity yields, for every event \(E\) in the integers,
\[
\Pr(R_n\in E)=\frac{3^n\Pr(S_n\in E)-2^{n-1}\Pr(T_{n-1}\in E)}{D_n}.
\]
Hence the total-variation distance between the laws of \(R_n\) and \(S_n\) is at most \(2^{n-1}/D_n=O((2/3)^n)\). Since a uniform \(\{0,1,2\}\) summand has mean \(1\) and variance \(2/3\), the ordinary central limit theorem for \(S_n\) transfers to \(R_n\), proving the displayed limit.

## Verification
The companion standalone `verify.py` has no external dependencies and is run with `python3 verify.py`. For each \(1\le n\le8\), it enumerates all subsets containing the top, directly tests pairwise meet closure, and compares the complete fixed-point cardinality histogram to the coefficients of the theorem's polynomial. For \(1\le n\le5\), independently of any fixed-point-set representation, it enumerates every extensive endofunction via all possible images and tests idempotence and monotonicity against the original definitions. The two histograms agree exactly. For \(n\le4\) it also constructs the closure map from each meet-closed set and verifies its three defining axioms directly. The verifier reports `VERIFY_OK`.

For \(n=1,2,3,4,5,6\), the total counts are respectively \(2,7,23,73,227,697\). The exact rank histograms for \(n=3\) and \(n=4\), listed in ascending fixed-point count, are respectively \((1,5,7,6,3,1)\) and \((1,7,15,19,16,10,4,1)\). The infinite-family assertion rests on the proof, not on finite computation.

## Relationship to prior work
Glück's 2023 preprint (published in 2024) develops closure systems and enumerates closures on specific orders, including chains and diamond orders; the product-chain fixed-point-rank polynomial above is not among the results in its Sections 7.1–7.2. Hafeez, Marcus, Ormsby and Osorno (2021 preprint) determine the *unrefined* counts of saturated transfer systems on all rectangular subgroup lattices, which already supply \(3^n-2^{n-1}\) on this family. Bao and collaborators (2023 preprint) establish the bijection between saturated transfer systems and interior operators on finite lattices. Both ingredients are indispensable and credited, rather than presented as new. Their combination alone determines the specialization \(t=1\), not the distribution of the number of fixed characteristic-lattice points. OEIS A083313 records the same unrefined integer sequence, not this polynomial rank statistic.

The new assertion is precisely the two-row normal form and full fixed-point-rank refinement together with its direct transfer-system interpretation and asymptotic law; it is not a new enumeration of the total number of closures, nor a new equivalence between transfer systems and operators. Related work might contain an equivalent rank refinement under different terminology, so originality is subject to subsequent independent literature evaluation.

## Limitations
The formula concerns product lattices with a *two-element* chain factor only. There is no claim to an analogous formula for products of three or more nontrivial chains, arbitrary finite posets, non-saturated transfer systems, or general multiplicative norm constraints. Exhaustive verification reaches only the finite sizes described above; the proof, not the checker, establishes the theorem for all \(n\). The transported statistic counts fixed points of the characteristic interior operator, not the number of transfer relations, covering arrows, or connected components. Prior unrefined enumerations are known; an unindexed prior rank-refinement formulation cannot be excluded solely by searches.

## References
1. Roland Glück, *Isolated Suborders and their Application to Counting Closure Operators*, arXiv:2302.13081 (first public version February 25, 2023), *Logical Methods in Computer Science* 20(3), 2024, DOI 10.46298/lmcs-20(3:11)2024. https://arxiv.org/abs/2302.13081
2. Usman Hafeez, Peter Marcus, Kyle Ormsby and Angélica Osorno, *Saturated and linear isometric transfer systems for cyclic groups of order \(p^m q^n\)*, arXiv:2109.08210 (first public version September 16, 2021). https://arxiv.org/abs/2109.08210
3. Linus Bao, Christy Hazel, Tia Karkos, Alice Kessler, Austin Nicolas, Kyle Ormsby, Jeremie Park, Cait Schleff and Scotty Tilton, *Transfer systems for rank two elementary Abelian groups: characteristic functions and matchstick games*, arXiv:2310.13835 (first public version October 20, 2023). https://arxiv.org/abs/2310.13835
4. OEIS A083313, published sequence recording the known unrefined count. https://oeis.org/A083313
