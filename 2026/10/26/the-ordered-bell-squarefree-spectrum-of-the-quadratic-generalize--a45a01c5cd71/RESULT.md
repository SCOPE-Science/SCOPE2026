# The ordered-Bell squarefree spectrum of the quadratic generalized Möbius recurrence

## Finding

Define \(s(1)=1\) and, for each integer \(n\ge2\),
\[
s(n)=1-n-\sum_{d=2}^{n-1}s(d)\left\lfloor\frac nd\right\rfloor^2.
\]
Let \(F_j=\sum_{k=0}^{j}k!\left\{\begin{smallmatrix}j\\k\end{smallmatrix}\right\}\) be the ordered Bell (Fubini) numbers, with \(F_0=1\). Let \(e_j\) denote the elementary symmetric polynomial of degree \(j\), with \(e_0=1\). For every squarefree integer \(n=p_1\cdots p_r>1\), putting \(x_i=p_i-1\),
\[
\boxed{s(n)=(-1)^r\left(1+2\sum_{j=1}^{r-1}F_j e_j(x_1,\ldots,x_r)\right).}
\]
For every nonsquarefree integer \(n\ge2\), \(s(n)\equiv0\pmod2\). Consequently, for every integer \(n\ge2\), \(s(n)=-1\) if and only if \(n\) is prime. On squarefree integers, the sign is precisely \((-1)^r\); if \(r\ge2\), the absolute value is strictly greater than one. The exact formula, not merely the primality consequence, is the central finding.

## Assumptions and scope

The recurrence is the quadratic specialization \(f(m)=m^2\) (including \(f(1)=1\)) of the generalized Möbius construction in Andrews–Kauffman–Sahoo (2026). All variables are ordinary positive integers; \(p_1,\ldots,p_r\) are distinct primes and \(r\ge1\). The ordered Bell numbers count ordered set partitions and are integers; their exponential generating function is \(\sum_{j\ge0}F_j z^j/j!=(2-e^z)^{-1}\). Values on nonsquarefree integers are only asserted to be even, not otherwise classified. No analytic continuation, asymptotic assertion, or unverified infinite computation is required.

## Proof

**Divisor convolution.** Write \(g(m)=2m-1\) for \(m\ge1\), let \(u(m)=1\), and let \(\delta\) be the identity for Dirichlet convolution. Subtract the defining recurrence at consecutive indices \(n\) and \(n-1\). The difference of the floors \(\lfloor n/d\rfloor-\lfloor(n-1)/d\rfloor\) is one exactly when \(d\mid n\), and zero otherwise. Equivalently (including \(n=2\) directly),
\[
s(n)=-1-\sum_{\substack{d\mid n\\1<d<n}}s(d)g(n/d),\qquad n\ge2.
\]
Since \(s(1)=g(1)=1\), this is the convolution identity
\[
s*g=g-u+\delta.
\]
Reducing modulo two gives \(g\equiv u\pmod2\) and hence \(s*u\equiv\delta\pmod2\). Convolution with the classical Möbius function \(\mu=u^{-1}\) proves \(s(n)\equiv\mu(n)\pmod2\) for every \(n\ge1\). Therefore every nonsquarefree integer has even \(s(n)\).

**Restriction to the Boolean lattice.** Fix squarefree \(n=p_1\cdots p_r\). Work in the finite ring
\[
\mathcal R=\mathbb Z[z_1,\ldots,z_r]/(z_1^2,\ldots,z_r^2).
\]
For a subset \(A\subseteq[r]\), write \(z_A=\prod_{i\in A}z_i\), \(p_A=\prod_{i\in A}p_i\), and \(p_\varnothing=1\). Define
\[
S=\sum_{A\subseteq[r]}s(p_A)z_A,\quad E=\prod_{i=1}^r(1+z_i),\quad H=\prod_{i=1}^r(1+p_i z_i),\quad G=2H-E.
\]
Products in \(\mathcal R\) implement divisor convolution on subsets. Since the coefficient of \(z_A\) in \(G\) is \(2p_A-1=g(p_A)\), the convolution identity yields \(SG=G-E+1\). The constant terms of \(G\) and \(E\) are one, so both are invertible in \(\mathcal R\), and
\[
S=1-\frac{E-1}{G}=1-\frac{1-E^{-1}}{2HE^{-1}-1}.
\]
Writing \(x_i=p_i-1\), the nilpotence \(z_i^2=0\) gives
\[
R=E^{-1}=\prod_{i=1}^r(1-z_i),\qquad T=HE^{-1}=\prod_{i=1}^r(1+x_i z_i),\qquad S=1-(1-R)(2T-1)^{-1}.
\]

**Ordered-Bell coefficient identity.** Let \(Q=(2T-1)^{-1}\). Its constant coefficient is one. For every nonempty subset \(A\subseteq[r]\) with \(|A|=j\), the coefficient of \(z_A\) in \((T-1)^k\) is \(x_A k!\left\{\begin{smallmatrix}j\\k\end{smallmatrix}\right\}\), where \(x_A=\prod_{i\in A}x_i\): partition the \(j\) distinct selected variables into \(k\) ordered nonempty blocks. Therefore the coefficient of \(z_A\) in \(Q=\sum_{k\ge0}(-2)^k(T-1)^k\) is \(x_A t_j\), with
\[
t_j=\sum_{k=1}^{j}(-2)^k k!\left\{\begin{smallmatrix}j\\k\end{smallmatrix}\right\}\quad(j\ge1),\qquad t_0=1.
\]
By the exponential generating function for Stirling numbers,
\[
\sum_{j\ge0}t_j\frac{z^j}{j!}=\frac{1}{1+2(e^z-1)}=\frac1{2e^z-1}=2\frac1{2-e^{-z}}-1.
\]
Indeed, multiplying by \(e^{-z}\) gives the exact identity
\[
\frac{1}{2e^z-1}=\frac{e^{-z}}{2-e^{-z}}=2\frac1{2-e^{-z}}-1.
\]
Thus \(t_0=1\) and for each \(j\ge1\), \(t_j=2(-1)^jF_j\).

**Top coefficient and sharpness.** For \(r\ge1\), the coefficient of \(z_{[r]}\) in \(1-(1-R)Q\) receives contributions from proper subsets \(A\subsetneq[r]\) of the \(Q\)-variables; using \([z_B](1-R)=(-1)^{|B|+1}\) for nonempty \(B\) gives
\[
s(n)=(-1)^r\left(1+2\sum_{\varnothing\ne A\subsetneq[r]}F_{|A|}x_A\right)=(-1)^r\left(1+2\sum_{j=1}^{r-1}F_j e_j(x_1,\ldots,x_r)\right).
\]
For \(r=1\), the sum is empty and \(s(p)=-1\). For \(r\ge2\), the degree-one part \(2F_1e_1\) is strictly positive, proving \(|s(n)|>1\). Every nonsquarefree \(s(n)\) is even and cannot equal \(-1\). These cases exhaust all \(n\ge2\), completing the proof.

## Verification

The attached standalone Python file `verify_quadratic.py` computes the original floor recurrence through \(n=600\), compares it to the exact divisor recurrence, then computes the latter through \(n=40000\). It independently factors each index and constructs ordered Bell numbers using the Stirling recursion; it confirms the full squarefree formula for 24,309 squarefree indices, parity for 15,690 nonsquarefree indices, and the prime-indicator equivalence over the tested range. Execution output: `VERIFY_OK 40000 600 24309 15690`. This finite check supplements the universal algebraic proof.

For orientation, \(s(4)=2\), \(s(6)=7\), and \(s(30)=-99\).

## Relationship to prior work

Andrews, Kauffman and Sahoo introduce the generalized recurrence and a universal formal-primality assertion. The published argument shows a nonzero polynomial obstruction under independent function-value parameters; it does not supply the present pointwise, quadratic, squarefree coefficient formula. Its literal all-functions primality statement is not valid for constant \(f\), so that assertion cannot substitute for the independent proof above. An earlier constant-function counterexample illustrates this limitation. Prior fixed-affine specializations \(f(m)=1+c(m-1)\) yield a different structure that depends only on the number of prime factors; the quadratic specialization depends on the individual factors \(p_i-1\). Classical Fubini numbers furnish the new exact coefficients here. No claim of uniqueness or complete literature coverage is inferred from unsuccessful searches.

## Limitations

The explicit magnitude formula is proved for squarefree integers only. Nonsquarefree values satisfy a parity law, but their full spectrum is not classified. The prime test is a theoretical characterization by the recursively defined integer sequence, not a claim of computational advantage over classical primality algorithms. A broader, not-yet-located identity may encode this squarefree formula implicitly. Independent validation has not been performed.

## References

Andrews, G. E., Kauffman, L. H., and Sahoo, D., *A surprising generalization of the Möbius function*, arXiv:2609.25628v1 (first public submission September 22, 2026), https://arxiv.org/html/2609.25628.

The ordered Bell/Fubini numbers and Stirling set-partition identity are classical combinatorial objects; the precise coefficient computation is supplied in the proof above.
