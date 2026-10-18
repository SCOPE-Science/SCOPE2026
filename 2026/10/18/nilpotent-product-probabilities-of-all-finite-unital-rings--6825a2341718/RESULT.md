# Nilpotent-product probabilities of all finite unital rings

## Finding
Let \(R\) be any **nonzero finite associative ring with identity**. Write \(J=J(R)\) for its Jacobson radical and write its uniquely determined Wedderburn decomposition (up to permutations and finite-field isomorphism) as
\[
R/J\simeq\prod_{i=1}^{s}M_{d_i}(\mathbb F_{q_i}),\qquad s\ge1,\quad d_i\ge1.
\]
For independent uniformly sampled \(X,Y\in M_m(R)\), with any integer \(m\ge1\), the probability of \(XY\) being nilpotent is exactly
\[
\boxed{\Pr(XY\text{ nilpotent})=\prod_{i=1}^{s}\frac{2q_i^{m d_i}-1}{q_i^{2m d_i}}.}
\]
In particular, for every prime power \(q\) and integer \(n\ge1\),
\[
\#\{(A,B)\in M_n(\mathbb F_q)^2:AB\text{ nilpotent}\}
=q^{2n^2-2n}(2q^n-1).
\]
For a **fixed** \(A\in M_n(\mathbb F_q)\) of rank \(r\), exactly \(q^{n^2-r}\) of the \(q^{n^2}\) matrices \(B\) have nilpotent product \(AB\). Hence \(M_n(\mathbb F_q)\) and the field \(\mathbb F_{q^n}\) have the same nilpotent-product probability.

Among all nonzero finite associative unital rings, the sharp upper bound is \(3/4\), with equality **if and only if** \(R/J(R)\simeq\mathbb F_2\); such maximizers need not be commutative.

## Assumptions and scope
An element \(z\) of an associative ring is nilpotent when \(z^h=0\) for some positive integer \(h\). The probability samples ordered pairs independently and uniformly. No commutativity, characteristic restriction, or field-algebra structure is assumed on \(R\). The zero ring is excluded from the sharp-bound statement; \(m\) and all matrix sizes are positive. The finite division rings in the semisimple quotient are finite fields by Wedderburn's little theorem.

## Proof
**1. Nilpotent endomorphisms over a finite field.** Let \(N_k(q)\) be the number of nilpotent endomorphisms of a \(k\)-space over \(\mathbb F_q\), with \(N_0(q)=1\). Every endomorphism \(T\) of a \(k\)-space has a unique Fitting decomposition into a \(T\)-invariant nilpotent summand of dimension \(j\) and a complementary \(T\)-invariant invertible summand of dimension \(k-j\). The number of ordered direct-sum decompositions of those dimensions is \(|\mathrm{GL}_k(q)|/(|\mathrm{GL}_j(q)|\,|\mathrm{GL}_{k-j}(q)|)\). Counting all endomorphisms in this manner and cancelling the invertible-summand count gives
\[
\frac{q^{k^2}}{|\mathrm{GL}_k(q)|}
=\sum_{j=0}^k\frac{N_j(q)}{|\mathrm{GL}_j(q)|}.
\]
Since \(|\mathrm{GL}_k(q)|=q^{k^2}\prod_{h=1}^k(1-q^{-h})\), subtraction of the formulas at \(k\) and \(k-1\) proves
\[
\frac{N_k(q)}{|\mathrm{GL}_k(q)|}=
\frac{q^{-k}}{\prod_{h=1}^k(1-q^{-h})},
\qquad N_k(q)=q^{k^2-k}.
\]
The empty-product convention includes \(k=0\).

**2. Conditional matrix-product fibers.** Fix \(A\in M_n(\mathbb F_q)\) of rank \(r\). Choose invertible \(P,Q\) with \(A=P\operatorname{diag}(I_r,0)Q\). Conjugating \(AB\) by \(P\) shows that it is nilpotent precisely when
\[
\operatorname{diag}(I_r,0)(QBP)
=\begin{pmatrix}C&*\\0&0\end{pmatrix}
\]
is nilpotent, where \(C\) is the upper-left \(r\)-square block of \(QBP\). This block-triangular matrix is nilpotent if and only if \(C\) is nilpotent. As \(B\) runs through all matrices, \(QBP\) does too; \(C\) is arbitrary and each value has exactly \(q^{n^2-r^2}\) lifts. By Step 1 the number of good \(B\)'s is \(q^{r^2-r}q^{n^2-r^2}=q^{n^2-r}\).

**3. Exact matrix-ring average.** A uniform matrix \(A\) therefore satisfies
\[
\Pr_B(AB\text{ nilpotent}\mid A)=q^{-\operatorname{rank}A}
=q^{-n}|\ker A|.
\]
For each nonzero vector \(v\in\mathbb F_q^n\), the probability that a uniform \(A\) kills \(v\) is \(q^{-n}\); the zero vector is always killed. Consequently
\[
\mathbb E_A|\ker A|=1+(q^n-1)q^{-n}=2-q^{-n}.
\]
Thus \(\Pr_{A,B}(AB\text{ nilpotent})=(2q^n-1)/q^{2n}\), and multiplying by the total number \(q^{2n^2}\) of ordered pairs gives the stated integer count.

**4. Nilpotent-ideal and semisimple reduction.** If \(I\) is a nilpotent two-sided ideal of an associative ring \(S\), then \(z\in S\) is nilpotent if and only if its image in \(S/I\) is nilpotent. Indeed, if \((z+I)^h=0\), then \(z^h\in I\), and \(I^t=0\) implies \(z^{ht}=0\). A finite ring has nilpotent Jacobson radical. The quotient homomorphism
\[
M_m(R)\longrightarrow M_m(R/J)
\simeq\prod_{i=1}^s M_{m d_i}(\mathbb F_{q_i})
\]
has nilpotent kernel \(M_m(J)\). Images of independent uniform elements are independent uniform elements of this quotient because every fiber has the same size. Nilpotence in the product ring is coordinatewise. Applying Step 3 to each factor proves the full formula.

**5. Sharp maximum and a noncommutative equality example.** For \(Q\ge2\), the function \(f(Q)=(2Q-1)/Q^2\) is strictly decreasing and \(f(2)=3/4\). Each factor in the formula is at most \(3/4\), so for \(m=1\) their product is \(3/4\) exactly when there is one factor, with \(d_1=1\), \(q_1=2\). This is precisely \(R/J(R)\simeq\mathbb F_2\).

For a concrete noncommutative maximizer, consider the \(16\)-element associative algebra \(\mathbb F_2\langle x,y\rangle/(x^2,y^2,yx)\). It has basis \(1,x,y,xy\), with \(xy\ne yx=0\). Its radical is \((x,y)\), with quotient \(\mathbb F_2\), so its probability is \(3/4\). All products of words of length at least three vanish, so this presentation is finite and the radical is nilpotent.

## Verification
Run `python verify.py` using Python 3. The code exhaustively enumerates nilpotent products in \(M_1(\mathbb F_2)\), \(M_1(\mathbb F_3)\), \(M_2(\mathbb F_2)\), \(M_2(\mathbb F_3)\), \(M_3(\mathbb F_2)\), \(M_2(\mathbb F_2[\varepsilon]/(\varepsilon^2))\), the noncommutative local algebra in Step 5, and \(2\)-square upper triangular matrices over \(\mathbb F_2\). These checks give respectively \(3/4\), \(5/9\), \(112/256\), \(1377/6561\), \(61440/262144\), \(28672/65536\), \(192/256\), and \(36/64\), matching the formula. It also checks the rank-conditioned fiber sizes in the five full-matrix configurations. These finite checks do not replace the proof for all parameters.

## Relationship to prior work
Sarma and Subedi (2026, arXiv:2610.07892v1, first posted October 6, 2026) introduce and investigate nilpotent-product probability, giving bounds, commutative-ring values and formulas for triangular matrix rings; their inspected Sections 1 and 2 do not state the exact formula for arbitrary full matrix rings or all finite unital rings via their Wedderburn quotients. The classical Fine–Herstein enumeration of individual nilpotent matrices gives \(q^{n^2-n}\); Step 1 supplies a self-contained derivation and Steps 2–4 combine it with conditional product fibers and radical reduction. Standard Artin–Wedderburn theory provides the finite semisimple quotient. Neither individual-nilpotent counts nor the list of attainable probability values alone assigns this probability to every finite unital ring.

## Limitations
Only two independently uniform ring elements and nilpotence of their product are counted. The formula does not determine the full distribution of nilpotency indices, the isomorphism class of the ring from the probability, or nonunital-ring probabilities. Equality of probabilities for distinct rings is common. The bibliographic comparison is limited to the stated inspected sources and mathematical-index searches; an equivalent older treatment under a different probabilistic or matrix-enumeration terminology cannot be excluded. No independent mathematical audit has been performed.

## References
1. D. Sarma and T. Subedi, *Nilpotent product probability of finite rings*, arXiv:2610.07892v1 (October 6, 2026), https://arxiv.org/html/2610.07892v1.
2. N. J. Fine and I. N. Herstein, *The probability that a matrix be nilpotent*, Illinois Journal of Mathematics **2** (1958), 499–504.
3. M. Gerstenhaber, *On the number of nilpotent matrices with coefficients in a finite field*, Illinois Journal of Mathematics **5** (1961), 330–333, DOI: 10.1215/ijm/1255629831.
4. S. R. Blackburn and K. R. McLean, *The enumeration of finite rings*, Journal of the London Mathematical Society **106** (2022), 3240–3262, DOI: 10.1112/jlms.12661.
