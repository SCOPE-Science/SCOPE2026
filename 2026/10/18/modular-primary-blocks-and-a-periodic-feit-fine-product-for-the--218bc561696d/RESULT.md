# Modular primary blocks and a periodic Feit–Fine product for the Jordan plane

## Finding

Fix a prime \(p\), a prime power \(q=p^f\), and an integer \(n\geq 0\). Let \(J\) be the Jordan-plane algebra with generators \(u,v\) and relation \(uv-vu=v^2\). Its labeled \(n\)-dimensional representations over \(\mathbb F_q\) are the ordered matrix pairs
\[
\mathcal R_n(\mathbb F_q)=\{(X,Y)\in M_n(\mathbb F_q)^2:XY-YX=Y^2\}.
\]
For a matrix \(Y\), examine its Jordan blocks over an algebraic closure of \(\mathbb F_q\). There exists a solution \(X\) if and only if **every block of \(Y\) with a nonzero eigenvalue has length divisible by \(p\)**. Blocks at eigenvalue zero are unrestricted. For every admitted \(Y\), the set of suitable \(X\) is an affine translate of \(\operatorname{Cent}_{M_n}(Y)\).

Put \(N_n(q)=|\mathcal R_n(\mathbb F_q)|\) and \(g_n(q)=|\mathrm{GL}_n(\mathbb F_q)|=\prod_{i=0}^{n-1}(q^n-q^i)\), with \(g_0(q)=1\). Then the **complete labeled-representation enumeration in every matrix size** is the coefficientwise formal identity
\[
\boxed{\sum_{n\geq0}\frac{N_n(q)}{g_n(q)}z^n=
\prod_{j\geq1}\prod_{a\geq0}
\left(1-q^{\mathbf1_{p\mid j}-a}z^j\right)^{-1}.}
\]
Equivalently, for partitions \(\lambda\vdash n\), with \(m_j(\lambda)\) parts of size \(j\),
\[
\boxed{N_n(q)=g_n(q)\sum_{\lambda\vdash n}
\frac{q^{\sum_{p\mid j}m_j(\lambda)}}
{\prod_{j\geq1}\prod_{h=1}^{m_j(\lambda)}(1-q^{-h})}.}
\]
All finite products and sums are exact rational expressions evaluating to integers. A part size divisible by \(p\) contributes one extra factor \(q\) in the partition formula; no other part size does.

For the **geometric reduced support** over an algebraically closed field \(k\) of characteristic \(p\), write \(\mathcal R_n(k)\) for the set defined by the same equation. Its dimension is \(n^2\) for \(0\leq n<p\), but
\[
\boxed{\dim\mathcal R_p(k)=p^2+1.}
\]
In size \(n=p\), the nonnilpotent part consists precisely of \(Y\) similar to \(\lambda I_p+J_p(0)\) with \(\lambda\ne0\). For each finite field of characteristic \(p\), its exact contribution to the representation count is \(q\,g_p(q)\). Thus the first dimension jump is accompanied by an exact arithmetic contribution, not merely by existence of a modular representation.

## Assumptions and scope

All statements concerning point counts use finite fields \(\mathbb F_q\) with \(q=p^f\), \(f\geq1\). The existence criterion itself works over any field of characteristic \(p\) after scalar extension to an algebraic closure; the conclusion descends because it is solvability of a linear system. Every assertion on dimension concerns the underlying reduced algebraic set, not the scheme cut out by all entrywise commutator equations. The Euler products are interpreted as formal power series in \(z\), with coefficients in \(\mathbb Q\) after fixing the integer \(q>1\), so convergence in a complex variable is not required.

## Proof

**1. Trace-pairing criterion.** For \(Y\in M_n(k)\), consider the linear operator \(\operatorname{ad}_Y(X)=XY-YX\) on the matrix space. Under the nondegenerate pairing \(\langle A,B\rangle=\operatorname{tr}(AB)\), the annihilator of \(\operatorname{im}(\operatorname{ad}_Y)\) is exactly \(\ker(\operatorname{ad}_Y)\), since
\[
\operatorname{tr}((XY-YX)C)=\operatorname{tr}(X(YC-CY)).
\]
Therefore \(Y^2\in\operatorname{im}(\operatorname{ad}_Y)\) if and only if \(\operatorname{tr}(CY^2)=0\) for every matrix \(C\) commuting with \(Y\). When solvable, the solution set is an affine translate of the centralizer vector space, of size \(q^{\dim_{\mathbb F_q}\operatorname{Cent}(Y)}\) over \(\mathbb F_q\).

**2. Exact Jordan-block test.** Work over an algebraic closure and put \(Y\) in Jordan form. A diagonal block of a commuting \(C\), restricted to a Jordan block \(B=\lambda I_s+N_s\), lies in \(k[N_s]\); write it \(c_0I_s+c_1N_s+\cdots\). Both \(B^2\) and each positive power of \(N_s\) are upper triangular, and
\[
\operatorname{tr}\bigl(B^2(c_0I_s+c_1N_s+\cdots)\bigr)=s\lambda^2c_0.
\]
The same identity applies to diagonal blocks of a centralizer of a matrix with repeated eigenvalues; off-diagonal block entries do not contribute to the trace. The projector onto any individual Jordan block commutes with block-diagonal \(Y\), so the trace criterion forces \(s\lambda^2=0\) separately on each block. Conversely, if every such scalar vanishes, the displayed formula makes \(\operatorname{tr}(CY^2)=0\) for **every** centralizer element \(C\). Thus the condition is both necessary and sufficient. In characteristic \(p\), for \(\lambda\ne0\) it reads \(p\mid s\), and when \(\lambda=0\) it is automatic. Matrix-rank preservation under field extension proves descent of linear solvability to the original field.

**3. Rational canonical types and affine fibers.** For each monic irreducible polynomial \(f\in\mathbb F_q[t]\), let \(d_f=\deg f\) and let \(\lambda_f\) be the partition indexing the \(f\)-primary elementary divisors of \(Y\). The admissibility condition is unrestricted for \(f=t\) and requires all parts of \(\lambda_f\) to be multiples of \(p\) for \(f\ne t\). Set \(c(\lambda)=\sum_i(\lambda'_i)^2\) and let \(m_j(\lambda)\) denote the multiplicity of the part \(j\). Standard primary-module centralizer calculation gives
\[
\dim_{\mathbb F_q}\operatorname{Cent}(Y)=\sum_f d_f c(\lambda_f),
\quad |\operatorname{Cent}_{\mathrm{GL}_n}(Y)|=
\prod_f q^{d_f c(\lambda_f)}\prod_{j\geq1}\prod_{h=1}^{m_j(\lambda_f)}(1-q^{-d_fh}).
\]
The first formula follows by summing \(d_f\min(r,s)\) over pairs of primary cyclic summands. For the second, the semisimple quotient of the centralizer algebra is \(\prod_{f,j}M_{m_j(\lambda_f)}(\mathbb F_{q^{d_f}})\), and the rest is its nilpotent radical. Combining the class size \(g_n(q)/|\operatorname{Cent}_{\mathrm{GL}_n}(Y)|\) with the affine fiber size cancels the factors \(q^{d_f c(\lambda_f)}\).

**4. Euler product.** The elementary \(q\)-binomial identity
\[
\sum_{m\geq0}\frac{w^m}{\prod_{h=1}^m(1-Q^{-h})}
=\prod_{a\geq0}(1-wQ^{-a})^{-1}
\]
allows independent sums over primary-part multiplicities. The zero polynomial \(f=t\) contributes \(\prod_{j\geq1,a\geq0}(1-z^jq^{-a})^{-1}\). The nonzero monic irreducibles contribute
\[
\prod_{\ell\geq1,a\geq0}\prod_{f\ne t}
(1-(z^{p\ell}q^{-a})^{d_f})^{-1}.
\]
Unique factorization of monic polynomials with nonzero constant term yields
\[
\prod_{f\ne t}(1-w^{d_f})^{-1}=\frac{1-w}{1-qw}.
\]
Its numerator cancels the \(f=t\) Euler factors at indices divisible by \(p\). The remaining factors are exactly \((1-q^{\mathbf1_{p\mid j}-a}z^j)^{-1}\), proving the first boxed identity. Expanding each \(j\)-factor by the same \(q\)-binomial identity gives the second boxed partition formula.

**5. First modular boundary.** If \(n<p\), all admitted \(Y\) are nilpotent. For a fixed nilpotent Jordan type \(\lambda\), the conjugacy orbit of \(Y\) has dimension \(n^2-c(\lambda)\) and the affine space of \(X\)-solutions has dimension \(c(\lambda)\). Hence each such locally closed stratum has dimension \(n^2\); the finite union has dimension \(n^2\). At \(n=p\), nonzero eigenvalues can occur only on a **single block** of size \(p\), with scalar eigenvalue \(\lambda\ne0\). Its \(Y\)-orbit has dimension \(p^2-p\), the parameter \(\lambda\) contributes one dimension, and its affine centralizer fiber contributes \(p\), giving \(p^2+1\). The nilpotent part still has dimension \(p^2\), proving the dimension statement. Over \(\mathbb F_q\) the nonnilpotent contribution is
\[
(q-1)\frac{g_p(q)}{q^p(1-q^{-1})}\,q^p=q\,g_p(q).
\]
No statement about the number of components or their scheme multiplicities is needed.

## Verification

The accompanying standalone `verify.py` enumerates every \(Y\) and solves the resulting linear commutator system by exact finite-field elimination for \((q,n)=(2,1),(2,2),(3,2),(2,3),(3,3),(4,2)\). It compares the resulting labeled pair counts with the partition formula and separately checks the nonnilpotent contribution in the boundary cases. Expected totals are respectively \(2,40,153,2192,95499,1216\). The field of order four uses explicit polynomial-basis arithmetic. These checks provide independent finite-instance corroboration, not a proof of the arbitrary-size identity.

## Relationship to prior work

Iyudu's original Jordan-plane representation-space analysis (arXiv:1209.0746v1, 4 September 2012) treats algebraically closed fields of characteristic zero and proves nilpotence of the second matrix, classification of components, and equidimensionality. Those results are established; the modular block condition and characteristic-periodic all-size counting product above are different claims.

Benkart, Lopes, and Ondrus (arXiv:1212.1404v2) study the Ore-extension family containing the Jordan plane in all characteristics and classify its irreducible modules. In characteristic \(p\), irreducible modules of dimension \(p\) with nonzero eigenvalue are consequently established antecedents. Their irreducible-module classification is not itself an enumeration of **all** labeled representations, including nonsemisimple ones.

The Feit–Fine commuting-pair product, revisited by Fulman and Guralnick (arXiv:1611.05499v1), weights **every** Euler-factor part size with \(q\), whereas nilpotent-second-matrix commuting pairs weight none; the present inhomogeneous Jordan-plane relation selects exactly the part sizes divisible by \(p\). Shirikov's 2007 work studies the Jordan plane in positive characteristic, including prime ideals and its center-related structure; its full paper was not inspected for this comparison. The two-dimensional characteristic-two boundary instance is not claimed as new in isolation.

## Limitations

The result counts labeled pairs, not similarity classes of representations, and gives dimension rather than a full component decomposition at every size. It does not assert reducedness, smoothness, or irreducibility of the defining representation scheme. The existence and counting formulas are mathematically established by the proof, while claims of literature originality remain subject to unidentified prior work, particularly the accessible-abstract but full-text-uninspected Shirikov paper. The finite tests do not certify the infinite family independently.

## References

1. N. K. Iyudu, *Representation spaces of the Jordan plane*, arXiv:1209.0746v1 (4 September 2012), https://arxiv.org/abs/1209.0746.
2. G. Benkart, S. A. Lopes, M. Ondrus, *A Parametric Family of Subalgebras of the Weyl Algebra II: Irreducible Modules*, arXiv:1212.1404v2 (9 April 2013), https://arxiv.org/abs/1212.1404.
3. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499v1 (16 November 2016), https://arxiv.org/abs/1611.05499.
4. E. N. Shirikov, *The Jordan Plane over a Field of Positive Characteristic*, Mat. Zametki 82 (2007), 272–292, https://doi.org/10.4213/mzm3796. Its abstract and bibliographic information, not complete article contents, were available for this comparison.
