# Square-zero derivations of binary-characteristic truncated polynomial algebras: exact rank spectra and a uniform limit law

## Finding
Let \(q=2^e\) with \(e\geq1\), let \(M\geq1\), and put
\[
A_M=\mathbb F_q[x]/(x^{2M}),\qquad
\mathcal N_M=\{D\in\operatorname{Der}_{\mathbb F_q}(A_M):D^2=0\}.
\]
Here \(D^2\) means composition as an \(\mathbb F_q\)-linear operator. Every derivation has the unique form \(D_f=f(x)\,d/dx\), with \(f\in A_M\). Set \(L=\lceil M/2\rceil\). The **complete rank enumerator** is
\[
\begin{aligned}
\mathcal R_{M,q}(z)
&=\sum_{D\in\mathcal N_M}z^{\operatorname{rank}_{\mathbb F_q}D}\\
&=1+\sum_{r=1}^{M}(q-1)q^{r-1}z^r\\
&\quad+\sum_{j=L}^{M-1}(q-1)q^{M-j-1}
\left(q^{M-j}z^{M-j}
+\sum_{\alpha=M-j}^{j-1}(q-1)q^{M-\alpha-1}z^{M-\alpha}\right).
\end{aligned}
\]
The last summation is empty if \(M=1\). In particular,
\[
\boxed{\lvert\mathcal N_M\rvert=q^M+\lfloor M/2\rfloor(q-1)q^{M-1}.}
\]
If \(D\) is uniform on \(\mathcal N_M\) and \(R_M=\operatorname{rank}_{\mathbb F_q}D\), then for every fixed \(q\),
\[
\boxed{\frac{R_M}{M}\ \xrightarrow[M\to\infty]{\mathrm d}\
\operatorname{Uniform}\!\left[\tfrac12,1\right].}
\]
In fact the one-dimensional Wasserstein-1 distance between these laws is \(O_q(M^{-1})\).

## Assumptions and scope
All algebras and derivations are unital-algebra derivations over the finite field \(\mathbb F_q\) of characteristic two. The truncation exponent is any **even** positive integer \(2M\), not only a power of two. Rank refers to the underlying \(2M\)-dimensional vector space \(A_M\), not to the rank of an induced map on its maximal ideal. The zero derivation is counted. The limit holds for fixed \(q\) as \(M\to\infty\); no simultaneous growth of the field size is asserted.

For \(a\in B_M=\mathbb F_q[t]/(t^M)\), define \(v(a)\) as its \(t\)-adic order if nonzero and set \(v(0)=M\). A sum whose lower bound exceeds its upper bound is zero.

## Proof
**1. All derivations and the restricted square.** Because \(2M=0\) in \(\mathbb F_q\), the usual formal derivative preserves the relation \(x^{2M}=0\). Conversely, every derivation \(D\) is determined by \(f=D(x)\) and the Leibniz rule gives \(D(x^i)=i x^{i-1}f\). Thus \(D=D_f\). In characteristic two the second formal derivative of every polynomial is zero; applying the product rule twice yields
\[
D_f^2(g)=f f' g',\quad\text{for all }g\in A_M.
\]
In particular \(D_f^2=0\) exactly when \(f f'=0\) in \(A_M\), since evaluation at \(g=x\) gives \(f f'\).

**2. Split even and odd coordinates.** Put \(t=x^2\) and decompose uniquely
\[
f=a(t)+x b(t),\qquad a,b\in B_M.
\]
The derivative of \(f\) is \(f'=b(t)\). Therefore
\[
f f'=a(t)b(t)+x b(t)^2.
\]
The even and odd summands occupy complementary \(\mathbb F_q\)-subspaces. Consequently
\[
D_f^2=0\quad\Longleftrightarrow\quad
ab=0\ \text{and}\ b^2=0\quad\text{in }B_M.
\]
If \(b=0\), \(a\) is unrestricted. If \(b\ne0\) with \(j=v(b)\), the second equation is equivalent to \(2j\geq M\), while the first is equivalent to \(v(a)\geq M-j\). Thus the allowed nonzero \(b\) have \(L\leq j\leq M-1\), with \((q-1)q^{M-j-1}\) possible \(b\)'s at a given \(j\); for each such \(b\), the polynomial \(a\) ranges over an ideal of cardinality \(q^j\).

**3. Rank is the smaller valuation.** Every derivative \(g'\) lies in \(B_M\) and conversely every \(h\in B_M\) equals \((xh)'\). Hence
\[
\operatorname{im}D_f=fB_M,
\]
regarded as a subspace of \(A_M=B_M\oplus xB_M\). Multiplication \(h\mapsto fh\) has kernel \(\{h:ah=bh=0\}\). Writing \(m=\min(v(a),v(b))\), the kernel is the ideal \((t^{M-m})\subset B_M\), of dimension \(m\). It follows that
\[
\boxed{\operatorname{rank}D_f=M-\min(v(a),v(b)).}
\]
This identity also covers both zero coefficients, since \(v(0)=M\).

**4. Exact finite enumeration.** For \(b=0\), \(a=0\) yields rank zero; for \(1\leq r\leq M\), the polynomials \(a\) of order \(M-r\) number \((q-1)q^{r-1}\). This gives the first two terms of \(\mathcal R_{M,q}\).

For nonzero \(b\) of order \(j\), admissible \(a\)'s satisfy \(v(a)\geq M-j\). The \(q^{M-j}\) elements with \(v(a)\geq j\) give rank \(M-j\). For each \(M-j\leq\alpha<j\), the \((q-1)q^{M-\alpha-1}\) choices of \(a\) of order \(\alpha\) give rank \(M-\alpha\). Multiplying by the number \((q-1)q^{M-j-1}\) of such \(b\)'s produces the last double sum, with no overlaps between cases. Summing at \(z=1\) gives \(q^M\) terms with \(b=0\), and for each of the \(\lfloor M/2\rfloor\) possible nonzero orders \(j\), exactly \((q-1)q^{M-1}\) pairs \((a,b)\). This proves the total.

**5. Limiting rank law and a quantitative bound.** For uniform \(D\in\mathcal N_M\), the probability of \(b=0\) is
\[
\varepsilon_M=\left(1+\lfloor M/2\rfloor\frac{q-1}{q}\right)^{-1}=O_q(M^{-1}).
\]
Conditional on \(b\ne0\), the valuation \(J=v(b)\) is *exactly uniform* on the integers \(L,L+1,\ldots,M-1\), because each such valuation supports the same \((q-1)q^{M-1}\) pairs. Conditional on \(J=j\), the coefficient \(a\) is uniform in \(t^{M-j}B_M\). With \(R=M-\min(v(a),j)\), one has \(0\leq j-R\), and for each positive integer \(h\),
\[
\Pr(j-R\geq h\mid J=j)\leq q^{-h}.
\]
Indeed the event, if possible, forces \(a\) to be divisible by \(t^{M-j+h}\) inside the uniform ideal. Summing this tail gives \(\mathbb E(j-R\mid J=j)\leq (q-1)^{-1}\), uniformly in \(j,M\). The discrete uniform law of \(J/M\) is within \(O(M^{-1})\) in Wasserstein-1 distance of the continuous uniform law on \([1/2,1]\). Coupling \(R/M\) to \(J/M\) on \(b\ne0\), and bounding the exceptional \(b=0\) probability by \(\varepsilon_M\), gives the stated \(O_q(M^{-1})\) bound and the weak convergence. \(\square\)

## Verification
The accompanying executable `verify.py` forms every derivation matrix \(D_f\) directly from the Leibniz rule over finite fields, computes \(D_f^2\) by matrix multiplication, and independently computes the matrix rank by Gaussian elimination. It then compares the resulting exact rank histograms with the stated formula for eleven field/truncation configurations: \(q=2\), \(2M=2,4,6,8,10,12\); \(q=4\), \(2M=2,4,6\); and \(q=8\), \(2M=2,4\). It additionally checks 237 symbolic instances of the total formula. The local run returned `VERIFY_OK`.

These finite exhaustive checks are cross-checks rather than an infinite proof. The unrestricted theorem is established by the valuation arguments above. Execute `python verify.py` with Python 3; no third-party packages are required.

## Relationship to prior work
Briggs and Rubio y Degrassi (first posted May 3, 2022) study the restricted Lie structure of derivations of Artin algebras, establishing the mathematical setting for the \(p\)-power operation. Their results do not provide the finite-field cardinality, rank enumerator, or rank-distribution limit for \(\mathbb F_q[x]/(x^{2M})\). Yao and Zhao (2020) treat 2-local derivations on Jacobson–Witt algebras over \(\mathbb F[x_1,\ldots,x_n]/(x_1^p,\ldots,x_n^p)\); their characteristic-two, one-variable specialization has exponent two, but their 2-local classification does not imply these length-\(2M\) rank counts. Premet's work on regular derivations of truncated polynomial rings assumes characteristic strictly greater than two and addresses regularity rather than the square-zero rank spectrum. Cong Chen's Zassenhaus nilpotent-variety result also assumes characteristic greater than three. The derivation and valuation facts used in the proof are elementary; the enumerated spectrum and uniform rank limit are the claims assessed here, not the classical restricted-Lie construction.

## Limitations
The theorem concerns derivations whose **operator square** vanishes, not all nilpotent derivations, not nilpotent matrices on arbitrary vector spaces, and not higher restricted powers. It does not classify automorphism-conjugacy orbits of these derivations or describe the scheme structure of the square-zero locus. The asymptotic rate is for fixed \(q\). No claim of universal publication priority is made; an equivalent enumeration under older Witt-algebra, modular vector-field, or group-scheme terminology cannot be excluded by the literature comparisons performed.

## References
- B. Briggs and L. Rubio y Degrassi, *On the Lie algebra structure of integrable derivations*, arXiv:2205.01660v1 (May 3, 2022), https://arxiv.org/abs/2205.01660 .
- Y. Yao and K. Zhao, *2-local derivations on the Jacobson–Witt algebras in prime characteristic*, arXiv:2007.07746v1 (July 15, 2020), https://arxiv.org/abs/2007.07746 .
- A. Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426v1 (May 10, 2014), https://arxiv.org/abs/1405.2426 .
- C. Chen, *The nilpotent variety of \(W(1;n)_p\) is irreducible*, arXiv:1707.02881v1 (July 10, 2017), https://arxiv.org/abs/1707.02881 .
