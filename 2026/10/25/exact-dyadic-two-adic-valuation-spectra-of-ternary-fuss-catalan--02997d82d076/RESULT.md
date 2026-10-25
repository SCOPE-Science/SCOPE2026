# Exact dyadic two-adic valuation spectra of ternary Fuss-Catalan numbers

## Finding

For each integer \(n\geq 0\), define the ternary Fuss-Catalan number
\[
C_3(n)=\frac{1}{2n+1}\binom{3n}{n},
\]
which counts rooted ordered full ternary trees with \(n\) internal vertices. Let \(\nu_2\) be the two-adic valuation, and define the dyadic valuation enumerator
\[
H_L(u)=\sum_{n=0}^{2^L-1}u^{\nu_2(C_3(n))},\qquad L\geq0.
\]
The **complete distribution at every dyadic scale** is specified by
\[
\boxed{\sum_{L\geq0}H_L(u)z^L=
\frac{(1+z)(1-uz)}{1-(1+u)z-(1-u+u^2)z^2+(u+u^2)z^3}.}
\tag{1}
\]
In particular, \(H_0(u)=1\), \(H_1(u)=2\), \(H_2(u)=3+u^2\), and \(H_3(u)=5+2u^2+u^3\). Equivalently, for \(L\geq3\),
\[
H_L(u)=(1+u)H_{L-1}(u)+(1-u+u^2)H_{L-2}(u)
-(u+u^2)H_{L-3}(u).
\tag{2}
\]
Consequences, with \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), are
\[
\#\{0\leq n<2^L:\nu_2(C_3(n))=0\}=F_{L+2}\qquad(L\geq0),
\tag{3}
\]
\[
\max_{0\leq n<2^L}\nu_2(C_3(n))=L,\quad
\#\{0\leq n<2^L:\nu_2(C_3(n))=L\}=F_{L-1}
\qquad(L\geq2).
\tag{4}
\]
If \(N_L\) is uniformly distributed on \(\{0,\ldots,2^L-1\}\) and \(V_L=\nu_2(C_3(N_L))\), then
\[
\boxed{\mathbb E[V_L]=\frac L2-\frac23+
\frac{3+(-1)^L}{6\cdot2^L}}\qquad(L\geq0),
\tag{5}
\]
\[
\operatorname{Var}(V_L)=\frac{11}{12}L+O(1),\qquad
\boxed{\frac{V_L-L/2}{\sqrt{11L/12}}\ \xrightarrow{\ d\ }\ \mathcal N(0,1)}.
\tag{6}
\]
Equations (1)--(6) are a single valuation-distribution theorem and its exact/extremal/asymptotic consequences, not independent conjectures.

## Assumptions and scope

The index \(n\) ranges over nonnegative integers; \(L\) is a nonnegative integer; \(u,z\) are commuting formal indeterminates. The valuation is well-defined because every ternary Fuss-Catalan number is a positive integer. Every denominator \(2n+1\) is odd; this is specific to order three and to the prime two. Formula (1) is an identity of formal power series in \(z\) with polynomial coefficients in \(u\). The asymptotic assertion concerns \(L\to\infty\) along *initial* dyadic intervals, not shifted intervals or other primes. The leading variance coefficient is positive.

## Proof

**1. Reduction to multiplication carries.** Let \(s_2(m)\) be the number of ones in the binary representation of \(m\), with \(s_2(0)=0\). Since \(2n+1\) is odd, Legendre's formula gives
\[
\nu_2(C_3(n))=\nu_2\binom{3n}{n}
=s_2(n)+s_2(2n)-s_2(3n)=2s_2(n)-s_2(3n).
\tag{7}
\]
By Kummer's theorem, this equals the number of carry operations when adding \(n\) and \(2n\) in base two, counting a propagated carry at each bit position. This is an equality for every \(n\), not a heuristic.

**2. Four states, including the final carry.** Write \(n=\sum_{j=0}^{L-1}b_j2^j\), padding with leading zero digits when needed. At position \(j\), the column adds \(b_j+b_{j-1}+c_j\), where \(b_{-1}=0\) and \(c_0=0\) is the incoming carry. The outgoing carry is \(c_{j+1}=\lfloor(b_j+b_{j-1}+c_j)/2\rfloor\). The previous-digit/carry state after that column is \((b_j,c_{j+1})\). The transition has weight \(u^{c_{j+1}}\). In the order \((0,0),(1,0),(0,1),(1,1)\), the transfer matrix is
\[
T(u)=\begin{pmatrix}1&1&0&0\\1&0&0&u\\1&0&0&u\\0&0&u&u\end{pmatrix}.
\tag{8}
\]
After the \(L\) input digits, the remaining bit of \(2n\) and the incoming carry can produce **one additional** carry precisely in state \((1,1)\). This is why the terminal weight vector is \(t(u)=(1,1,1,u)^{\mathsf T}\), rather than the all-ones vector. Consequently, including \(L=0\),
\[
H_L(u)=(1,0,0,0)\,T(u)^L\,t(u).
\tag{9}
\]
To check the rational identity without conjectured recurrence fitting, solve the four linear equations for the entries of \((I-zT(u))^{-1}t(u)\), or directly multiply \((I-zT(u))\) by the proposed solution. One obtains
\[
(1,0,0,0)(I-zT(u))^{-1}t(u)=
\frac{(1+z)(1-uz)}{D(z,u)},
\]
where \(D(z,u)=1-(1+u)z-(1-u+u^2)z^2+(u+u^2)z^3\). This proves (1); coefficient comparison proves (2). Both include the terminal carry and all boundary indices.

**3. Zero and maximum valuation.** There are no carries exactly when the binary expansions of \(n\) and \(2n\) have no overlapping ones. Equivalently, the \(L\)-digit binary representation of \(n\) contains no adjacent ones. The count of these strings satisfies the Fibonacci recurrence and equals \(F_{L+2}\), proving (3).

The first bit position cannot emit a carry, and only positions \(1,\ldots,L\) can emit one. Thus the valuation is at most \(L\), and the all-ones word of length \(L\) attains this bound for \(L\geq2\). Attaining the bound forces the two least significant bits to be one and the most significant bit to be one; while a carry is active, subsequent output carries persist exactly when no two successive input bits are zero. Counting these binary words by the usual Fibonacci recurrence gives \(F_{L-1}\), proving (4). This argument treats the trailing bit and excludes spurious terminal solutions.

**4. Exact first moment.** Differentiating (1) formally at \(u=1\) gives
\[
\sum_{L\geq0}\left(\sum_{0\leq n<2^L}\nu_2(C_3(n))\right)z^L
=\frac{z^2(z-2)}{(z-1)(z+1)(2z-1)^2}.
\tag{10}
\]
Its partial fractions are
\[
\frac7{6(2z-1)}+\frac1{2(2z-1)^2}
+\frac1{6(z+1)}-\frac1{2(z-1)}.
\]
Extracting the coefficient of \(z^L\), and dividing by \(2^L\), proves (5) for all \(L\geq0\).

**5. Gaussian limit.** The characteristic polynomial of \(T(u)\) is
\[
\det(\lambda I-T(u))=\lambda\bigl(\lambda^3-(1+u)\lambda^2
-(1-u+u^2)\lambda+u+u^2\bigr).
\tag{11}
\]
At \(u=1\), the eigenvalues are \(2,1,-1,0\); the eigenvalue \(2\) is simple and strictly dominant. Hence for complex \(u\) in a neighborhood of one, the analytic simple eigenvalue \(\lambda(u)\) with \(\lambda(1)=2\) dominates the remaining eigenvalues. The spectral projection in (9) has an analytic coefficient \(A(u)\) with \(A(1)=1\); thus, uniformly in this neighborhood,
\[
\mathbb E[u^{V_L}]=A(u)\left(\frac{\lambda(u)}2\right)^L
+O(\rho^L)
\]
for some \(0<\rho<1\). Implicit differentiation of the cubic in (11) yields \(\lambda'(1)=1\) and \(\lambda''(1)=4/3\). Therefore the first and second derivatives at \(t=0\) of \(\log(\lambda(e^t)/2)\) equal \(1/2\) and \(11/12\), respectively. Differentiating the cumulant-generating function gives the variance asymptotic in (6). Substituting \(t=is/\sqrt{11L/12}\), centering by \(L/2\), and expanding the analytic logarithm to second order gives pointwise convergence of characteristic functions to \(e^{-s^2/2}\). Lévy's continuity theorem proves the Gaussian limit. All limiting steps use a nonzero analytic spectral gap, not numerical eigenvalue extrapolation.

## Verification

The accompanying standalone standard-library program `verify.py` independently computes factorial valuations for every \(n<2^{12}\), checks 120 exact ternary Fuss-Catalan integers against the binomial formula, builds the four-state valuation histograms, verifies the polynomial recurrence through length 26, and tests parity, maximum/multiplicity, and exact first moments at every length through 12. Execute `python3 verify.py` with Python 3. Its expected final line begins `VERIFY_OK`. The exhaustive checks establish only the specified finite tests; formulas (1)--(6) follow from the arguments above.

## Relationship to prior work

The ternary Fuss-Catalan numbers and their ordered-tree interpretation appear in Aval's 2007 preprint and in OEIS A001764. Kummer's 1852 theorem already implies (7), so neither the individual carry identity nor integrality nor the basic ternary-tree sequence is claimed as new. Aval studies combinatorial refinements of the ternary-tree count rather than the two-adic dyadic valuation distribution. Luca and Young (2010) investigate \(p\)-adic congruences for order \(p^q\) Fuss-Catalan numbers at the same prime \(p\); this does not supply the order-three/two-adic spectrum. Da Conceição (2023) studies a different multinomial Catalan quotient and its Lucas analogues, not the present order-three quotient's dyadic valuation histogram. OEIS A001764 lists the object and interpretations rather than (1)--(6). The explicit polynomial denominator, sharp maximal multiplicities, exact block mean, and Gaussian variance are the assessed contribution. General finite-state or digit-sum limit theorems may imply qualitative rationality or asymptotic normality; no claim is made that transfer-matrix methods themselves are new.

## Limitations

No corresponding result is proved for a prime other than two, an order other than three, or shifted intervals. Equation (7) is classical; the new specificity lies in the complete explicit distribution, the constants, and sharp extremal enumerations. A comprehensive literature proof of global novelty is impossible; an equivalent formulation in specialized digital-carry literature may exist. The verification program is finite evidence and does not establish independent validation. The Gaussian limit provides weak convergence, not a quantitative Berry–Esseen or local limit bound.

## References

1. J.-C. Aval, *Multivariate Fuss-Catalan numbers*, arXiv:0711.0906v1, first submitted 2007-11-06, Sections 2--3, https://arxiv.org/abs/0711.0906.
2. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, J. Reine Angew. Math. **44** (1852), 93--146 (classical theorem on prime-power binomial divisibility).
3. F. Luca and P. T. Young, *Some \(p\)-adic congruences for \(p^q\)-Catalan numbers*, manuscript dated 2010-06-14, https://youngp.people.charleston.edu/pq-catalan.pdf.
4. J. Cera Da Conceição, *Multinomial Catalan Numbers and Lucas Analogues*, J. Integer Seq. **26** (2023), Article 23.9.7, https://cs.uwaterloo.ca/journals/JIS/VOL26/Cera/cera4.pdf.
5. OEIS A001764, *Ternary Fuss-Catalan numbers*, https://oeis.org/A001764 (sequence values and interpretations, not the asserted valuation spectrum).
