# The Hilbert matrix is trace class immediately above the logarithmic Bergman endpoint

## Finding
For every real \(\alpha\), the classical Hilbert matrix, initially acting on analytic polynomials, admits a Schatten trace-class extension
\[
H:A^2_{\log^\alpha}(\mathbb D)\longrightarrow A^2(\mathbb D)
\]
**if and only if \(\alpha>2\)**. At the exact endpoint \(\alpha=2\), this operator extends boundedly but is not compact. When \(\alpha<2\), it has no bounded extension. The positive result is therefore stronger than compactness at *every* parameter above the boundedness endpoint: no further logarithmic damping is needed to obtain nuclearity.

## Assumptions and scope
All spaces comprise holomorphic functions on the unit disk, with normalized area measure \(dA=dx\,dy/\pi\). For \(\alpha\in\mathbb R\), set
\[
\|f\|_{\alpha}^{2}=\int_{\mathbb D}|f(z)|^{2}\left(\log\frac{e}{1-|z|^{2}}\right)^\alpha\,dA(z),
\qquad A^2=A^2_{\log^0}.
\]
On polynomials \(f(z)=\sum_{n\ge0}a_nz^n\), define \(Hf(z)=\sum_{m\ge0}\big(\sum_{n\ge0}a_n/(m+n+1)\big)z^m\). Trace class means membership in the Schatten ideal \(\mathcal S_1\) as an operator between these Hilbert spaces, not a trace of a non-endomorphic map. The conclusion covers all real \(\alpha\), with no positivity restriction on polynomial coefficients.

## Proof
**1. Coefficient model.** Orthogonality of monomials gives
\[
v_n=\|z^n\|_\alpha^2=\int_0^1t^n\left(\log\frac e{1-t}\right)^\alpha dt
\asymp\frac{(\log(n+3))^\alpha}{n+1}.
\]
The asymptotic is valid for every real \(\alpha\), by the dominated-convergence moment lemma in Norrbo [1]; it also follows by writing \(u=(n+1)(1-t)\) and dominating the resulting exponential integral. Orthonormal monomials in the domain and range turn \(H\) into the positive matrix
\[
M_{mn}=\frac{1}{\sqrt{m+1}\sqrt{v_n}\,(m+n+1)}.
\]
We prove \(M\in\mathcal S_1\) whenever \(\beta=\alpha/2>1\), using an explicit absolutely trace-norm convergent decomposition.

**2. Geometric-block estimates.** Discard the finitely many rows and columns with indices below \(2\): they contribute finite-rank bounded operators when \(\alpha>2\), since \(\sum_{n\ge2}v_n^{-1}(n+1)^{-2}<\infty\). Let \(I_k=\{2^k,\ldots,2^{k+1}-1\}\), \(k\ge1\). Uniformly for \(n\in I_k\),
\[
\frac1{\sqrt{v_n}}\asymp\frac{\sqrt{n+1}}{k^\beta}.
\]
If \(k\ge l+2\), expand, absolutely on \(I_l\times I_k\),
\[
\frac1{m+n+1}=\sum_{j\ge0}\frac{(-m)^j}{(n+1)^{j+1}}.
\]
Each term is rank one after multiplication by the two coefficient weights. Its nuclear norm is at most \(C_\beta 2^{j(l+1-k)}k^{-\beta}\), because the squared row and column norms are bounded respectively by \(C2^{2j(l+1)}\) and \(C2^{-2jk}k^{-2\beta}\). For \(j\ge1\), summing first over \(l\le k-2\), then over \(j\) and \(k\), is finite:
\[
\sum_{k\ge3}k^{-\beta}\sum_{j\ge1}\sum_{l=1}^{k-2}2^{j(l+1-k)}<\infty.
\]

For the \(j=0\) terms, let \(u_l\) be the vector \(((m+1)^{-1/2})_{m\in I_l}\), and \(w_k\) the vector \(((v_n)^{-1/2}/(n+1))_{n\in I_k}\). Their norms satisfy \(\|u_l\|\asymp1\) and \(\|w_k\|\asymp k^{-\beta}\). Their supports are mutually orthogonal on both sides. Therefore the sum of these rank-one blocks is unitarily equivalent, up to uniformly bounded diagonal factors, to the discrete upper-triangular matrix
\[
S_{lk}=\mathbf1_{\{k\ge l+2\}}k^{-\beta},\qquad l,k\ge1.
\]
Here is an elementary nuclearity lemma: \(S\in\mathcal S_1\) for \(\beta>1\). Divide its columns into consecutive shells \(2^h\le k<2^{h+1}\). Rows strictly below the shell contribute one rank-one matrix of trace norm \(O(2^{h(1-\beta)})\). Rows in or immediately adjacent to the shell give a triangular array of size \(O(2^h)\), with each column weighted by at most \(2^{-h\beta}\). Let \(U_N\) be the \(N\)-by-\(N\) upper-triangular matrix of ones. Its block decomposition
\[
U_{2N}=\begin{pmatrix}U_N&J_N\\0&U_N\end{pmatrix},
\quad\|J_N\|_{\mathcal S_1}=N
\]
implies \(\|U_{2^h}\|_{\mathcal S_1}\le2^h(1+h)\) by induction; removing two diagonals, transposing, or adding two rows changes this estimate only by a constant multiple of \(2^h\). Each shell therefore has trace norm \(O(2^{h(1-\beta)}(1+h))\), and summing over \(h\ge0\) converges for \(\beta>1\). This proves the lemma, including the nontrivial \(j=0\) part.

If instead \(l\ge k+2\), use the absolutely convergent expansion
\[
\frac1{m+n+1}=\sum_{j\ge0}\frac{(-n)^j}{(m+1)^{j+1}}.
\]
Its rank-one blocks have nuclear norm at most \(C_\beta 2^{(j+1)(k+1-l)}k^{-\beta}\). The sum over all \(j\ge0\), all gaps \(l-k\ge2\), and all \(k\ge1\) is finite.

Finally, on the three neighboring diagonals \(|l-k|\le1\), center the row interval at \(c_l=3\cdot2^{l-1}\). Since \(|m-c_l|\le2^{l-1}\) and \(n+c_l+1\ge2^{l+1}\),
\[
\frac1{m+n+1}=\sum_{j\ge0}\frac{(-1)^j(m-c_l)^j}{(n+c_l+1)^{j+1}}
\]
with ratio at most \(1/4\). The nuclear norm of its \(j\)-th rank-one block is at most \(C_\beta4^{-j}k^{-\beta}\); summing over \(j,k\) and the three neighboring diagonals is finite. Collecting the four regions gives an absolutely trace-norm convergent rank-one expansion of \(M\). Its matrix entries equal the displayed Hilbert coefficients, so the bounded extension is trace class when \(\alpha>2\).

**3. Sharp obstruction at and below the endpoint.** Let \(L\to\infty\), \(N_L=\lceil e^L\rceil\), \(P_L=\lfloor e^{2L}\rfloor\), and choose the positive-coefficient polynomial
\[
f_L(z)=L^{-(\alpha+1)/2}\sum_{n=N_L}^{P_L}z^n.
\]
The moment estimate yields
\[
\|f_L\|_\alpha^2\asymp L^{-(\alpha+1)}\sum_{n=N_L}^{P_L}\frac{(\log(n+3))^\alpha}{n+1}\asymp1,
\]
for every fixed real \(\alpha\); the logarithmic interval has length \(L\). The normalized sequence \(f_L/\|f_L\|_\alpha\) is weakly null because the Taylor supports move to infinity. For integers \(e^{L/2}\le m\le e^L\), positivity and \(m\le n\) give
\[
(Hf_L)_m\ge cL^{-(\alpha+1)/2}\sum_{n=N_L}^{P_L}\frac1n\ge c'L^{(1-\alpha)/2}.
\]
Consequently,
\[
\|Hf_L\|_{A^2}^2\ge c''L^{1-\alpha}\sum_{e^{L/2}\le m\le e^L}\frac1{m+1}\ge C_3L^{2-\alpha}.
\]
For \(\alpha<2\) this contradicts boundedness. At \(\alpha=2\) it contradicts compactness, because the inputs are bounded and weakly null while their images stay separated from zero. Norrbo [1] proves boundedness at \(\alpha=2\), completing the trichotomy.

## Verification
The decomposition uses only geometric series on regions where the ratio is bounded by \(1/2\) or \(1/4\), a triangular-matrix trace-norm recursion, and the exact Bergman coefficient norms. Independent finite rational tests of the two geometric expansions and the triangular recursion are supplied in `checks/check_blocks.py`; executing it prints `CHECK_OK`. Finite tests do not certify the infinite sums, whose convergence is proved above. Every constant may depend on the fixed \(\alpha\) but not on the dyadic indices.

## Relationship to prior work
Norrbo [1] proved the sharp boundedness boundary, including the endpoint \(\alpha=2\), and supplied the requisite logarithmic moment lemma. Karapetrović [2] established earlier logarithmic-domain mapping estimates for supercritical parameters. Published research results on compactness above the endpoint and the essential norm at the endpoint do not imply trace-class membership above it: compactness is strictly weaker than nuclearity. The present statement is the exact trace-class classification, with an explicit nuclear decomposition; it makes no new priority claim for the earlier boundedness/compactness conclusions.

## Limitations
The result establishes trace-class membership, not explicit singular values, trace norms, or the Schatten-quasinorm scale below \(p=1\). The available source comparison does not rule out an implicit equivalent in older operator-ideal literature. No independent audit has been performed.

## References
[1] D. Norrbo, *The Hilbert matrix operator into the Bergman space*, arXiv:2610.00252v1 (first publicly available 2026-09-23), https://arxiv.org/html/2610.00252v1.

[2] B. Karapetrović, *Libera and Hilbert matrix operator on logarithmically weighted Bergman, Bloch and Hardy-Bloch spaces*, Czechoslovak Mathematical Journal (2018), DOI:10.21136/CMJ.2018.0555-16.
