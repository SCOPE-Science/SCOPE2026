# Exact dyadic residue multiplicities of derangement numbers

## Finding
Let \(D_n\) be the number of fixed-point-free permutations of an \(n\)-element set, normalized by \(D_0=1\). Equivalently, for each integer \(n\ge1\),
\[
D_n=nD_{n-1}+(-1)^n.
\]
For each integer \(k\ge3\), define the complete fiber multiplicity
\[
M_k(y)=\#\{n:0\le n<2^k,\quad D_n\equiv y\pmod{2^k}\}.
\]
Then, for every residue class \(y\in\mathbb Z/2^k\mathbb Z\),
\[
\boxed{M_k(y)=\begin{cases}
1&y\equiv0\pmod2,\\
4&y\equiv1\pmod8,\\
0&\text{otherwise}.
\end{cases}}
\]
The least positive index period of \(D_n\) modulo \(2^k\) is \(2^k\). The precise image size is \(5\cdot2^{k-3}\); the normalized additive Haar measure of the closure of the derangement values in \(\mathbb Z_2\) equals \(5/8\), and that closure is exactly \(2\mathbb Z_2\cup(1+8\mathbb Z_2)\). For \(k=1\), the residues \(0,1\) occur once each. For \(k=2\), the counts of residues \(0,1,2,3\) are respectively \(1,2,1,0\). The exact index periods for these two cases are \(2\) and \(4\).

## Assumptions and scope
All assertions concern the classical integer derangement numbers, each complete period starting with index \(0\), and all positive powers of two. For \(z\in\mathbb Z_2\), write \(v_2(z)\) for its 2-adic valuation with \(v_2(0)=\infty\). The result concerns natural index periods and the *additive* normalized Haar measure of the 2-adic range; it does not assert equidistribution among all residues.

## Proof
**1. A uniformly differentiable 2-adic interpolation.** Define the falling-factorial polynomials \(P_0(X)=1\) and \(P_j(X)=\prod_{h=0}^{j-1}(X-h)\) for \(j\ge1\). Define
\[
H(x)=\sum_{j=0}^{\infty}(-1)^jP_j(x),\qquad x\in\mathbb Z_2.
\]
The sum converges uniformly because \(P_j(x)=j!\binom{x}{j}\in j!\mathbb Z_2\) for every \(x\in\mathbb Z_2\). (The binomial polynomial is integral on \(\mathbb Z_2\) by density of nonnegative integers and continuity.) In particular, each \(P_j\) is 1-Lipschitz and so is \(H\). For any nonnegative integer \(n\), truncation at \(j=n\) and inclusion–exclusion yield \(H(n)=(-1)^n D_n\).

For \(j\ge1\), set
\[
Q_j(X,Y)=\frac{P_j(X)-P_j(Y)}{X-Y}
=\sum_{i=0}^{j-1}\Big(\prod_{h=0}^{i-1}(X-h)\Big)
\Big(\prod_{h=i+1}^{j-1}(Y-h)\Big).
\]
In each summand, the two consecutive-factor products lie respectively in \(i!\mathbb Z_2\) and \((j-1-i)!\mathbb Z_2\). Thus each summand lies in \(2^{v_2(\lfloor(j-1)/2\rfloor!)}\mathbb Z_2\). Hence \(\sum_{j\ge1}(-1)^jQ_j(x,y)\) converges uniformly on \(\mathbb Z_2^2\). Let its limit be \(Q(x,y)\); it satisfies \(H(x)-H(y)=(x-y)Q(x,y)\). On the diagonal,
\[
Q(x,x)=H'(x):=\sum_{j\ge1}(-1)^jP_j'(x),
\]
where the derivative series also converges uniformly. Since each polynomial \(Q_j\) has integer coefficients, whenever \(x\equiv y\pmod{2^r}\) we have
\[
Q(x,y)\equiv H'(x)\pmod{2^r}.
\]

**2. Two exact local valuation laws.** For odd \(x\), the first three derivative terms \((-1)^jP'_j(x)\), with \(j=1,2,3\), are each odd; for \(j\ge4\), the derivative is even because four consecutive factors contain two even factors and deletion of one still leaves an even factor. Therefore
\[
H'(x)\equiv1\pmod2\qquad(x\text{ odd}).
\]
For even \(x\), the derivative contributions through \(j=4\) give
\[
-P'_1(x)+P'_2(x)-P'_3(x)+P'_4(x)\equiv2\pmod4.
\]
For \(j\ge5\), the derivative \(P_j'(x)\) is divisible by four: five consecutive factors starting at even \(x\) have three even factors, so removing any one leaves two even factors. Consequently
\[
H'(x)\equiv2\pmod4\qquad(x\text{ even}).
\]
Now take different odd \(x,y\). Since \(x\equiv y\pmod2\), the congruence for \(Q\) and the odd derivative give \(Q(x,y)\) odd. Thus
\[
\boxed{v_2(H(x)-H(y))=v_2(x-y)}\quad(x,y\text{ odd},\ x\ne y).
\]
If instead \(x,y\) are different even integers of \(\mathbb Z_2\) with \(x\equiv y\pmod4\), then \(Q(x,y)\equiv2\pmod4\), so
\[
\boxed{v_2(H(x)-H(y))=v_2(x-y)+1}
\quad(x\equiv y\equiv0\text{ or }2\pmod4,\ x\ne y).
\]

**3. Three surjective isometric branches.** Because \(H(1)=0\) and \(H(0)=H(2)=1\), these exact valuation laws show that the maps
\[
F_{\mathrm{odd}}(u)=-\frac{H(1+2u)}2,
\quad F_0(u)=\frac{H(4u)-1}{8},
\quad F_2(u)=\frac{H(2+4u)-1}{8}
\]
are all well-defined maps \(\mathbb Z_2\to\mathbb Z_2\) satisfying
\[
v_2(F(u)-F(v))=v_2(u-v)\qquad(u,v\in\mathbb Z_2).
\]
An isometry of \(\mathbb Z_2\) to itself induces an injection on every finite quotient modulo \(2^r\), hence a bijection on that quotient. Compatibility and completeness therefore make each of the three maps a bijection of \(\mathbb Z_2\).

For odd integer \(n=1+2u\), \(D_n=-H(n)=2F_{\mathrm{odd}}(u)\): the \(2^{k-1}\) odd indices modulo \(2^k\) map bijectively to the \(2^{k-1}\) even residues. For even integer \(n\), \(D_n=H(n)\). Its two classes modulo four satisfy \(D_{4u}=1+8F_0(u)\) and \(D_{2+4u}=1+8F_2(u)\). For \(k\ge3\), each of these classes contains \(2^{k-2}\) indices modulo \(2^k\), mapping onto the \(2^{k-3}\) residues congruent to one modulo eight with multiplicity two. Combining the two classes gives multiplicity four. No odd residues outside the latter class occur. This establishes the formula, and direct reduction gives the two small-level tables.

**4. Least period, closure, and measure.** Since \(H\) is 1-Lipschitz, the sign relation \(D_n=(-1)^nH(n)\) implies \(D_{n+2^k}\equiv D_n\pmod{2^k}\) for every \(k\ge1\). An index period must be even because the parity of \(D_n\) alternates. For any even period \(T\) modulo \(2^k\), compare two odd indices \(n\) and \(n+T\) using the first valuation law: \(2^k\mid D_{n+T}-D_n\) implies \(2^k\mid T\), proving minimality. Finally each integer-index class is dense in the corresponding 2-adic index coset, and the three bijections show that the exact range closure is \(2\mathbb Z_2\cup(1+8\mathbb Z_2)\). Their disjoint additive Haar measures are \(1/2\) and \(1/8\), totaling \(5/8\).

## Verification
Run `python3 verify.py` using the embedded standalone verifier. It checks inclusion–exclusion against the recurrence for indices through \(120\), derivative congruences at 32 test arguments, and every residue fiber for each exponent from \(1\) through \(15\), comprising 65,534 tested target fibers. The successful run reports `VERIFY_OK exhaustive_fibers=65534 levels=1..15 derivative_mod4_test_points=32 exact_formula_n=0..120`. This finite calculation is independent corroboration; the argument above proves the theorem for every exponent.

## Relationship to prior work
The classical derangement congruences in Sun–Wu–Zhuang (2010) provide the archival number-theory starting point, but not the exact multiplicities of all residue classes modulo every power of two. Aebi–Cairns (2013) prove a modular subfactorial analogue of Wilson's theorem. Wang–Miska–Mező (2018) study prime-adic valuations and Hensel-type lifting of generalized derangements, while O'Desky–Richman (2020) develop prime-adic interpolation and continuity of derangement-type functions. These are relevant tools and comparisons, but the inspected statements do not supply the three exact isometric branches or the all-residue fiber formula. Exact least periods of the classical sequence also follow from previously available weighted-derangement period results; minimality is included here to specify the full cycle, **not** asserted as the new contribution. The new claim is the explicit entire dyadic residue distribution and its 2-adic support geometry. Absence of a detected exact prior theorem does not establish historical uniqueness.

## Limitations
Only the classical derangement numbers and powers of two are classified. The result does not provide the corresponding residue-fiber distributions for odd prime powers, for generalized derangements, or for weighted polynomials. It establishes value-set Haar measure, not uniform distribution across the image. Historical priority remains subject to specialist comparison, and no independent mathematical audit has been conducted.

## References
1. Y. Sun, X. Wu, J. Zhuang, *Congruences on the Bell polynomials and the derangement polynomials*, arXiv:1009.2929v1, posted 2010-09-15, https://arxiv.org/abs/1009.2929.
2. C. Aebi, G. Cairns, *Wilson Theorems for Double-, Hyper-, Sub- and Super-factorials*, arXiv:1302.3676, posted 2013-02-15, https://arxiv.org/abs/1302.3676.
3. C. Wang, P. Miska, I. Mező, *The r-derangement numbers*, arXiv:1803.04529v1, posted 2018-03-12, https://arxiv.org/abs/1803.04529.
4. A. O'Desky, D. H. Richman, *Derangements and the p-adic incomplete gamma function*, arXiv:2012.04615, posted 2020-12-08, https://arxiv.org/abs/2012.04615.
