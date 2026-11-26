# Socle avoidance and conditional dimension in quadratic Artinian Gorenstein algebras

## Finding

Fix an odd prime power \(q\). For each \(d\ge 2\) take a nonsingular symmetric form \(B_d\) on \(V_d=\mathbb F_q^d\), with either Witt type allowed in even dimension. Let \(S_d\) be uniform among the embedded unital \(\mathbb F_q\)-subalgebras of
\[
A_{B_d}=\mathbb F_q1\oplus V_d\oplus\mathbb F_q z,
\qquad vw=B_d(v,w)z,\quad vz=z^2=0.
\]
The line \(\mathbb F_q z\) is the socle, since it annihilates the maximal ideal and \(B_d\) is nonsingular. As \(d\to\infty\), uniformly in the choice of \(B_d\),
\[
\Pr(z\notin S_d)=q^{-d^2/12+d/6+O_q(1)}.
\]
The dimension divided by \(d\) tends in probability to \(1/3\) conditional on \(z\notin S_d\), but tends to \(1/2\) without conditioning. The disparity is between a rare family of graph subalgebras constrained by orthogonality and a dominant family that permits arbitrary linear subspaces. The exact subalgebra enumerator and its Witt detection are inputs, not originality claims here.

For comparison, the unconditioned centered dimension has the same limiting laws as the all-subspaces measure, shifted up by two. For \(d=2m\) the mass at \(\dim S_d=m+2+j\) tends to \(q^{-j^2}/\sum_{\ell\in\mathbb Z}q^{-\ell^2}\); for \(d=2m+1\) it tends to \(q^{j-j^2}/\sum_{\ell\in\mathbb Z}q^{\ell-\ell^2}\), for each fixed integer \(j\).

## Counting inputs

A unital subalgebra has the form \(\mathbb F_q1\oplus W\) with \(W\le V_d\oplus\mathbb F_q z\). If \(z\in W\), then \(W=U\oplus\mathbb F_qz\) for an arbitrary \(U\le V_d\). If \(z\notin W\), then \(W\) is the graph of a unique linear functional \(U\to\mathbb F_q z\), where \(U\) is its projection to \(V_d\). Products of graph elements lie in \(\mathbb F_q z\), so closure is equivalent to \(B_d|_{U\times U}=0\). Writing \({d\brack k}_q\) for the Gaussian binomial and \(I_{d,k}\) for the number of totally isotropic \(k\)-subspaces, the two classes at projection dimension \(k\) therefore have sizes \({d\brack k}_q\) and \(q^k I_{d,k}\), with subalgebra dimensions \(k+2\) and \(k+1\), respectively.

For clarity, the orthogonal-space inputs can be derived as follows. If a quadratic space of dimension \(e\) has \(N_e\) zeros (including zero), adjoining a hyperbolic plane yields \(N_{e+2}=(q-1)q^e+qN_e\): for each old vector, the coordinate product in the new plane has \(q-1\) solutions for nonzero target and \(2q-1\) for zero target. Start with \(N_e=1\) for anisotropic part of dimension \(e=0,1,2\). Subtracting one and dividing by \(q-1\) gives the isotropic-line counts, with \([j]_q=(q^j-1)/(q-1)\),
\[
L_{2r+1}=[2r]_q,\qquad
L^+_{2r}=(q^{r-1}+1)[r]_q,\qquad
L^-_{2r}=(q^r+1)[r-1]_q.
\]
Here \(+\) denotes split and \(-\) nonsplit. An isotropic \(k\)-space has \(L_{d-2k}\) isotropic one-dimensional extensions in its orthogonal quotient, which has the same anisotropic dimension. Counting incident isotropic spaces of dimensions \(k,k+1\) gives \(I_{d,k+1}=I_{d,k}L_{d-2k}/[k+1]_q\). Thus
\[
\begin{aligned}
I_{2m+1,k}&={m\brack k}_q\prod_{i=0}^{k-1}(q^{m-i}+1) &&(0\le k\le m),\\
I^+_{2m,k}&={m\brack k}_q\prod_{i=0}^{k-1}(q^{m-1-i}+1) &&(0\le k\le m),\\
I^-_{2m,k}&={m-1\brack k}_q\prod_{i=0}^{k-1}(q^{m-i}+1) &&(0\le k\le m-1).
\end{aligned}
\]
The count is zero outside the indicated ranges.

## Asymptotic proof

Put \(G_d=\sum_k{d\brack k}_q\), \(H_d=\sum_k q^k I_{d,k}\), and \(C_q=\prod_{j\ge1}(1-q^{-j})^{-1}\). The product formula bounds each Gaussian coefficient between \(q^{k(d-k)}\) and \(C_q q^{k(d-k)}\). Completing the square in \(k(d-k)\) gives \(G_d=q^{d^2/4+O_q(1)}\): a nearest integer to \(d/2\) gives a lower bound within a constant factor and the full discrete-Gaussian sum gives the upper bound. From the three isotropic products, in their respective ranges,
\[
q^k I_{d,k}=q^{kd-3k^2/2+k/2}c_{d,k},\qquad
1\le c_{d,k}\le C_q\prod_{j\ge0}(1+q^{-j}).
\]
The bound comes from the Gaussian coefficient and the remaining distinct nonnegative indices in the \(1+q^{-j}\) factors, so is uniform in \(d,k\) and type. The exponent is
\[
\frac{(d+1/2)^2}{6}-\frac32\left(k-\frac{d+1/2}{3}\right)^2.
\]
For all sufficiently large \(d\), an integer nearest \((d+1/2)/3\) lies within the Witt range for every type. Its contribution gives a constant-factor lower bound and summing the Gaussian envelope gives the matching upper bound \(H_d=q^{d^2/6+d/6+O_q(1)}\). Taking \(H_d/(G_d+H_d)\) proves the rarity with the linear term in the exponent. The same bounds give uniformly summable Gaussian tails for the projection dimensions about their respective centers. After adding one or two and dividing by \(d\), this proves the conditional convergence in probability and, since the containing class dominates, the unconditioned convergence in probability.

For the centered unconditioned law, the normalized Gaussian coefficient \({d\brack m+j}_q/q^{(m+j)(d-m-j)}\) tends to \(C_q\) for each fixed \(j\). This follows from the finite product as both \(m+j\) and \(d-m-j\) grow. The excess exponent relative to \(k=m\) is \(-j^2\) or \(j-j^2\) according to parity, giving summable dominating terms. Dominated convergence under the measure on the containing class gives the two normalizations. The avoiding probability tends to zero, so removing the conditioning on containment gives the same limits.

## Relationship to prior work and scope

*Subalgebra lattices of short bilinear local algebras and a sharp enumerative rigidity theorem* (Resultary, record `fc812afc8d34`, [record](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-subalgebra-lattices-of-short-bilinear-local-algebras-and-a-sharp--fc812afc8d34)) supplies the normal form and exact enumeration in a broader family allowing degenerate forms; its exponent is subalgebra dimension minus one. The orthogonal and Gaussian binomial counts are classical. The contribution here is the two-class asymptotic comparison, including the linear correction in the rarity exponent and the separate limiting dimension scale for the avoiding class. The comparison is for fixed odd \(q\) and nonsingular forms; it does not give uniform asymptotics as \(q\) varies or allow degenerate forms. Strade's *Enumeration Results in Nilpotent Algebras*, Proc. Amer. Math. Soc. 49 (1975), 20–24, doi:10.1090/S0002-9939-1975-0357526-4, is potentially related; its full text was not inspected, and publication priority is not asserted.

## Reproducibility

The companion `verify.py` checks the algebraic counting inputs on finite fields of prime orders 3 and 5 by direct product closure on subspaces. It does not test the limiting laws; those follow from the uniform bounds above. For example, at \(q=3,d=4\) the split and nonsplit dimension profiles are \((1,49,112,130,40,1)\) and \((1,31,40,130,40,1)\).
