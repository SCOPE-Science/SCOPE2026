# A characteristic-sensitive sharp Fourier-projection norm for a cubic fold

## Finding
Let \(F=\mathbb F_q\) be any finite field of odd characteristic \(p\), with \(q=p^m\) and \(m\ge1\). Consider the cubic ruled graph
\[
S_q=\{(x,y,xy^2):x,y\in F\}\subset F^3.
\]
If \(P_{S_q}\) is the ordinary (unweighted) Fourier projection to the characters indexed by \(S_q\), then its **sharp** operator norm, with counting-measure \(\ell^\infty\) on both sides, is
\[
\boxed{\|P_{S_q}\|_{\ell^\infty\to\ell^\infty}
=1+\frac{(q-1)^2}{pq\sin(\pi/(2p))}.}
\]
Its projection kernel has exactly \(1+(q^3-q)/2\) nonzero Fourier coefficients, including the coefficient at the origin. For comparison, the quadratic saddle spectrum \(T_q=\{(x,y,xy):x,y\in F\}\) has sharp projection norm \(q-1+q^{-1}\). Therefore, for each fixed odd characteristic,
\[
\lim_{m\to\infty}\frac{\|P_{S_{p^m}}\|}{\|P_{T_{p^m}}\|}
=\frac{1}{p\sin(\pi/(2p))},
\]
and along prime fields that ratio tends to \(2/\pi\) as \(p\to\infty\).

## Assumptions and scope
The field characteristic \(p\) is an odd prime. The degree \(m\) is arbitrary and positive; thus the theorem includes non-prime finite fields. Let \(\psi:F\to\mathbb C\) be the fixed nontrivial additive character
\[
\psi(t)=\exp(2\pi i\operatorname{Tr}_{F/\mathbb F_p}(t)/p).
\]
For any frequency set \(A\subset F^3\), define the Fourier projection on functions \(g:F^3\to\mathbb C\) by
\[
(P_Ag)(u)=\frac1{q^3}\sum_{\xi\in A}\sum_{v\in F^3}
 g(v)\psi(\langle u-v,\xi\rangle).
\]
There is no averaging in the \(\ell^\infty\)-norm. This normalization makes \(P_A\) an idempotent on the finite-dimensional function space. The theorem concerns the endpoint operator norm, not the optimal \(\ell^2\to\ell^4\) Fourier extension norm.

## Proof
**1. Exact kernel and the fiber trichotomy.** Put
\[
K(a,b,c)=\sum_{x,y\in F}\psi(ax+by+cxy^2).
\]
By additive-character orthogonality in the \(x\)-variable,
\[
K(a,b,c)=q\sum_{y\in F:\ a+cy^2=0}\psi(by).
\]
When \(c=0\), the only nonzero case is \(a=b=0\), with \(K(0,0,0)=q^2\). When \(c\ne0\) and \(a=0\), the unique root \(y=0\) gives \(K=q\) for every \(b\). When \(c\ne0\), \(a\ne0\), and \(-a/c\) is a nonsquare, \(K=0\). Finally, if \(-a/c=r^2\) is a nonzero square, the two roots \(r,-r\) yield
\[
K(a,b,c)=q\bigl(\psi(br)+\psi(-br)\bigr)
=2q\cos\bigl(2\pi\operatorname{Tr}(br)/p\bigr).
\]
Since \(p\) is odd, this cosine never vanishes. There are \((q-1)^2/2\) pairs \((a,c)\) of the final kind, with \(q\) available values of \(b\). Together with the origin and the \(q(q-1)\) one-root values, this proves
\[
|\operatorname{supp}K|=1+q(q-1)+\frac{q(q-1)^2}{2}
=1+\frac{q^3-q}{2}.
\]

**2. Exact absolute-value sum.** For each fixed nonzero \(r\), the map \(b\mapsto\operatorname{Tr}(br)\) is a surjective \(\mathbb F_p\)-linear functional with fibers of size \(q/p\). Write
\[
T_p=\sum_{j=0}^{p-1}|\cos(2\pi j/p)|.
\]
The preceding cases give, without asymptotics,
\[
\sum_{a,b,c\in F}|K(a,b,c)|
=q^2+q^2(q-1)+\frac{q^2(q-1)^2}{p}\,T_p
=q^3+\frac{q^2(q-1)^2}{p}\,T_p.
\]

**3. The elementary trigonometric identity.** The ordinary cosine sum over all residues vanishes. The negative cosine residues constitute one consecutive interval centered at \(p/2\), of length \((p-1)/2\) when \(p\equiv1\pmod4\) and \((p+1)/2\) when \(p\equiv3\pmod4\). Summing that interval as a geometric progression gives
\[
T_p=\frac{2\sin(n\pi/p)}{\sin(\pi/p)}
=\frac{2\cos(\pi/(2p))}{\sin(\pi/p)}
=\frac1{\sin(\pi/(2p))},
\]
where \(n=(p-1)/2\) or \((p+1)/2\), respectively. This includes \(p=3\).

**4. The sharp endpoint norm.** The projection is convolution with the kernel \(q^{-3}K\), up to the harmless sign convention in the Fourier transform. For convolution on a finite group, the \(\ell^\infty\to\ell^\infty\) norm equals the \(\ell^1\)-norm of its kernel: the upper bound is the triangle inequality, and equality at the origin is attained by choosing \(g(v)\) as the conjugate phase of the corresponding kernel coefficient (arbitrarily on zeros). Dividing the sum in Step 2 by \(q^3\) and inserting Step 3 yields the asserted formula.

**5. A nondegenerate benchmark.** For the quadratic saddle, summing first in \(x\) gives \(q\psi(-ab/c)\) whenever \(c\ne0\); at \(c=0\) only the origin contributes \(q^2\). Hence the absolute sum is \(q^2+q^3(q-1)\), whose quotient by \(q^3\) equals \(q-1+q^{-1}\). Dividing the two exact formulas and using \(\sin t\sim t\) proves both ratio limits.

## Verification
Run `python3 CHECK.py` from the same directory. This directly enumerates all Fourier coefficients, without using the simplified kernel as the definition, on prime fields of orders \(3,5,7,11\) and on quadratic extension fields of orders \(9,25\). Its second computation uses quadratic-fiber root counts and independently compares the resulting endpoint norm to the claimed formula, with a stated floating-point tolerance. The tests supplement, but do not replace, the full proof; they are numerical checks, not exact-arithmetic certificates or evidence for arbitrary field sizes.

## Relationship to prior work
Iosevich, Li and Yu (2026) introduce the Fourier algebra norm of an indicator, equivalent to the endpoint norm of its Fourier projection, and evaluate related quantities on hyperplanes and nondegenerate quadratic paraboloids. Their Section 5.1 describes the nondegenerate quadratic Fourier transform; Section 6 addresses composite-modulus Gauss sums. Those statements do not contain the present cubic-fold Fourier coefficient distribution or its characteristic-dependent \(\csc\) formula. The new calculation contrasts two distinct algebraic geometries having equal cardinality \(q^2\), and does not assert a new definition of the norm or the classical convolution identity. Other general Fourier-algebra estimates and finite-field exponential-sum methods are compatible with the result but do not, without additional computations, specify this sharp constant.

## Limitations
The result assumes odd characteristic and only the particular cubic graph shown. It does not classify all cubic surfaces, even characteristic, or arbitrary weights on this frequency set. A literature search and inspection of the most relevant available primary manuscript found no matching theorem, but cannot exclude earlier equivalent calculations under exponential-sum or finite-field idempotent terminology. In particular, the finite-field extension cases are not inferred from numerical experiments.

## References
- A. Iosevich, Z. Li, K. Yu, *Spectral synthesis with the complexity parameter in* \(\mathbb Z_N^d\), arXiv:2609.25404, first public 2026-09-21, especially Sections 2, 5, 6 and 8. https://arxiv.org/abs/2609.25404
