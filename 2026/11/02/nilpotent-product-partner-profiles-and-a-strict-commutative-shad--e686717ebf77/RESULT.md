# Nilpotent-product partner profiles and a strict commutative-shadow convex-order gap

## Finding
Let \(R\) be any finite, nonzero, associative ring with identity, and let \(J=J(R)\). For a uniformly chosen element \(X\in R\), study the **nilpotent-partner propensity**
\[
\Theta_R(X)=\frac{1}{|R|}\big|\{y\in R: Xy\text{ is nilpotent}\}\big|.
\]
Suppose the uniquely determined Artin–Wedderburn decomposition is
\[
R/J\cong\prod_{i=1}^{s}M_{n_i}(\mathbb F_{q_i}),\qquad n_i\ge1,
\]
where every \(q_i\) is a prime power. Write \(a_i=q_i^{-n_i}\), and for \(0\le r\le n\) define
\[
C_{n,q}(r)=\frac{\prod_{j=0}^{r-1}(q^n-q^j)^2}{\prod_{j=0}^{r-1}(q^r-q^j)},
\]
with empty products equal to one. Then the complete finite law of \(\Theta_R(X)\) is
\[
\Pr\bigl(\Theta_R(X)=t\bigr)
=\sum_{\substack{0\le r_i\le n_i\\\prod_i q_i^{-r_i}=t}}
\prod_{i=1}^{s}\frac{C_{n_i,q_i}(r_i)}{q_i^{n_i^2}}.
\tag{1}
\]
In particular, the probability that two independent uniform elements of \(R\) have nilpotent product is
\[
\Pr(XY\text{ is nilpotent})=\mathbb E\Theta_R(X)
=\prod_{i=1}^{s}(2a_i-a_i^2).
\tag{2}
\]

There is a sharp distributional distinction that the scalar in (2) cannot detect. Define the *commutative shadow*
\[
S=\prod_{i=1}^{s}\mathbb F_{q_i^{n_i}}.
\]
For independent uniform \(U\in S\), the shadow propensity \(\Theta_S(U)\) has the same mean as \(\Theta_R(X)\), but
\[
\boxed{\quad \mathbb E\varphi(\Theta_R(X))\le
\mathbb E\varphi(\Theta_S(U))\quad}
\tag{3}
\]
for **every convex real-valued function** \(\varphi\) on \([0,1]\). Inequality (3) is strict for **every strictly convex** \(\varphi\) if and only if at least one \(n_i\ge2\); equality of the two propensity distributions holds if and only if the semisimple quotient \(R/J\) is commutative. In particular, the variance is strictly smaller on the left precisely when \(R/J\) is noncommutative.

The shadow can be made **equal in order to the semisimple quotient**: replacing each field \(\mathbb F_{q_i^{n_i}}\) by the commutative local ring \(\mathbb F_{q_i^{n_i}}[t]/(t^{n_i})\) does not change its propensity distribution, and the resulting ring has order \(|R/J|\). Thus for semisimple \(R\), the strict convex-order comparison can be realized by a commutative ring of **the same order**.

For every prime power \(q\), the two equal-order rings \(M_2(\mathbb F_q)\) and \(\mathbb F_{q^2}[t]/(t^2)\) both have nilpotent-product probability \((2q^2-1)/q^4\), yet their propensity variances satisfy the exact sharp ratio
\[
\frac{\operatorname{Var}(\Theta_{M_2(\mathbb F_q)})}
{\operatorname{Var}(\Theta_{\mathbb F_{q^2}[t]/(t^2)})}
=\frac{1}{q+1}.
\tag{4}
\]

## Assumptions and scope
All rings are finite, associative, nonzero, and unital. Nilpotent means that some positive power equals zero. No commutativity of \(R\), restriction on its radical, or common characteristic among its semisimple factors is assumed. Each propensity is computed using independent uniform elements. The Artin–Wedderburn factors are unique up to permutation and field isomorphism. Formula (1) sums over all rank tuples yielding the same numerical propensity, so it also handles collisions among distinct prime powers.

## Proof
**1. Radical invariance, including the conditional law.** Every finite ring has nilpotent Jacobson radical \(J\), say \(J^e=0\). An element \(z\) is nilpotent if and only if \(z+J\) is nilpotent in \(R/J\): indeed, \((z+J)^m=0\) implies \(z^m\in J\), hence \(z^{me}=0\). Since reduction modulo \(J\) maps uniform elements to independent uniform elements, for every \(x\in R\),
\[
\Theta_R(x)=\Theta_{R/J}(x+J).
\tag{5}
\]
The law of the propensity is therefore unchanged by adjoining any nilpotent radical. The same holds for any commutative local ring with a fixed finite residue field.

**2. The exact fixed-first-factor lemma.** Let \(V\) be an \(n\)-dimensional vector space over \(\mathbb F_q\), and fix \(A\in\operatorname{End}(V)\) of rank \(r\). Set \(W=\operatorname{im}A\). If \(B\) is uniformly random in \(\operatorname{End}(V)\), then the restricted operator \((AB)|_W\in\operatorname{End}(W)\) is uniformly random: the restriction \(B|_W\) is uniform in \(\operatorname{Hom}(W,V)\), and postcomposition by the surjection \(A:V\to W\) is a surjective linear map of hom spaces. Relative to \(V=W\oplus W'\), the matrix of \(AB\) has block form
\[
\begin{pmatrix}D&E\\0&0\end{pmatrix}.
\]
It is nilpotent exactly when the \(r\)-dimensional endomorphism \(D\) is nilpotent.

Exactly \(q^{r^2-r}\) of the \(q^{r^2}\) endomorphisms of an \(r\)-dimensional vector space are nilpotent (including the single zero-dimensional endomorphism). For completeness, write \(G_m=|\operatorname{GL}_m(\mathbb F_q)|\) and \(N_m\) for the nilpotent count. The canonical Fitting decomposition of any endomorphism into a nilpotent part of dimension \(d\) and an invertible part of dimension \(m-d\) gives
\[
\frac{q^{m^2}}{G_m}=\sum_{d=0}^{m}\frac{N_d}{G_d}.
\]
Subtract the corresponding formula for \(m-1\), use \(G_m/G_{m-1}=q^{m-1}(q^m-1)\), and obtain \(N_m=q^{m(m-1)}\). Therefore
\[
\boxed{\Theta_{M_n(\mathbb F_q)}(A)=q^{-\operatorname{rank}A}.}
\tag{6}
\]

**3. Full distribution and mean.** The number of rank-\(r\) matrices equals \(C_{n,q}(r)\): choose their \(r\)-dimensional image and then a surjection onto it. Apply (5), (6), and independence of the Artin–Wedderburn blocks to obtain (1). If \(A\) is uniform and \(K=|\ker A|=q^{n-\operatorname{rank}A}\), then linearity of expectation gives
\[
\mathbb E K=\sum_{v\in\mathbb F_q^n}\Pr(Av=0)
=1+(q^n-1)q^{-n}=2-q^{-n}.
\]
Consequently, \(\mathbb E q^{-\operatorname{rank}A}=q^{-n}\mathbb E K=2q^{-n}-q^{-2n}\). Multiplying the independent factors proves (2).

**4. Strict convex-order comparison.** Fix one block and write \(a=q^{-n}\), \(Z=q^{-\operatorname{rank}A}\), where \(A\) is uniform in \(M_n(\mathbb F_q)\). Then \(a\le Z\le1\), and by step 3, \(\mathbb E Z=2a-a^2\). Let \(H\) take values \(1\) and \(a\) with probabilities \(a\) and \(1-a\), respectively. It follows that \(\mathbb E H=\mathbb E Z\). For any convex \(\varphi\), the chord bound
\[
\varphi(z)\le\frac{1-z}{1-a}\varphi(a)+\frac{z-a}{1-a}\varphi(1),\qquad a\le z\le1,
\]
implies \(\mathbb E\varphi(Z)\le\mathbb E\varphi(H)\). If \(n\ge2\), rank-one matrices occur with positive probability and give \(a<Z<1\), so the inequality is strict for each strictly convex \(\varphi\). If \(n=1\), \(Z\) has exactly the law of \(H\).

The variable \(H\) is precisely the nilpotent-partner propensity of a uniform element of the field \(\mathbb F_{q^n}\): it is \(1\) at zero and \(q^{-n}\) elsewhere. For independent block variables, replace \(Z_i\) one at a time by the corresponding independent \(H_i\). Conditional on all other positive factors, \(z\mapsto\varphi(cz)\) remains convex, and strictly convex when \(\varphi\) is strictly convex. The replacements prove (3), with the stated strictness. The variance comparison follows by taking \(\varphi(z)=z^2\), since the means agree. Equality holds exactly when all \(n_i=1\), equivalently when \(R/J\) is commutative.

**5. Equal-order shadows and the dimension-two ratio.** The truncated polynomial ring \(\mathbb F_{q^n}[t]/(t^n)\) has \(q^{n^2}\) elements, nilpotent radical \((t)\), and residue field \(\mathbb F_{q^n}\). Step 1 proves the claimed equal-order comparison. In dimension two, the rank counts of \(M_2(\mathbb F_q)\) are
\[
1,\quad (q-1)(q+1)^2,\quad q(q-1)^2(q+1)
\]
for ranks \(0,1,2\). Direct substitution into the second-moment formula yields
\[
\operatorname{Var}(\Theta_{M_2(\mathbb F_q)})
=\frac{(q-1)^3(q+1)^2}{q^8},
\quad
\operatorname{Var}(\Theta_{\mathbb F_{q^2}[t]/(t^2)})
=\frac{(q-1)^3(q+1)^3}{q^8},
\]
which proves (4).

## Verification
The standalone `CHECK.py` enumerates complete multiplication tables and all ordered pairs for \(M_2(\mathbb F_2)\), \(M_2(\mathbb F_3)\), \(\mathbb F_4\), \(\mathbb F_4[t]/(t^2)\), the binary upper-triangular ring, and binary dual numbers. It compares the resulting per-element propensity with the rank or residue-class formula. It also checks the matrix rank enumerator, exact first and second moments, strict variance gaps, and the convex stop-loss inequalities at every support breakpoint for the order-sixteen matrix/commutative pair. The independent multiplication-table checks returned `VERIFY_OK`; `CHECK_OUTPUT.txt` contains their recorded output. These finite tests corroborate but do not replace the proof for all finite rings.

## Relationship to prior work
Sarma and Subedi (2026) formulate the nilpotent-product probability and analyze its scalar values, primarily in commutative settings and upper-triangular matrix subrings. Holmes and Im (2026), building on earlier work on nilpotent pairs, give the two-map/cyclic-quiver nilpotence probability and rank refinements; their formula already covers the **scalar** probability for a full matrix ring. Dolžan (2025) determines individual product-fiber probabilities for full matrix rings and direct products. The matrix nilpotent count used in step 2 is classical (Fine and Herstein, 1958). The scalar formula (2), viewed only for matrix rings, is **not claimed to be new**. The contribution here is the all-finite-ring **conditional partner-propensity law**, its radical invariance at that level, and a strict convex-order comparison, with an equality criterion detecting the commutativity of the semisimple quotient despite equal scalar nilpotent-product probabilities.

## Limitations
The result concerns uniform, independent sampling and finite associative unital rings; it is not a classification of nonunital or infinite rings, or of nonuniform pair distributions. The variance equality characterizes commutativity of \(R/J(R)\), **not** commutativity of \(R\) itself. The polynomial rank-counting formula may coalesce distinct rank tuples when different factors yield the same numerical propensity. The general nilpotent product probability and finite-field rank-count ingredients have strong published antecedents; historical priority for the combined conditional and convex-order statements is not independently certified.

## References
1. D. Sarma and T. Subedi, *Nilpotent Product Probability of Finite Rings*, arXiv:2610.07892v1, submitted 2026-10-06. https://arxiv.org/abs/2610.07892
2. C. Holmes and M. S. Im, *Nilpotent representations over equioriented cyclic quivers*, arXiv:2608.16636v1, submitted 2026-08-17, especially Proposition 3.13. https://arxiv.org/abs/2608.16636
3. D. Dolžan, *The multiplication probability of a finite ring*, arXiv:2504.12886v1, submitted 2025-04-17, especially Theorem 3.2. https://arxiv.org/abs/2504.12886
4. N. J. Fine and I. N. Herstein, *The probability that a matrix be nilpotent*, Illinois J. Math. 2 (1958), 499–504. (The count is also proved directly above.)
