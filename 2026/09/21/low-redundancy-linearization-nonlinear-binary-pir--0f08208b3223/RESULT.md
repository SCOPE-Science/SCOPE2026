# Low-redundancy linearization of nonlinear binary PIR encoders

## Statement

Let \(t\ge 2\), and let
\[
\varepsilon:\mathbb F_2^k\longrightarrow C\subseteq \mathbb F_2^n
\]
be a binary \(t\)-PIR encoder whose associated code \(C\) is a linear \([n,k]\) code. Write \(r=n-k\).

For each data coordinate \(j\), choose \(t\) pairwise disjoint recovery sets \(I_{j,1},\ldots,I_{j,t}\). After identifying \(C\) linearly with \(\mathbb F_2^k\), the \(j\)-th coordinate of the inverse labeling of \(C\) factors through a linear quotient of dimension at most
\[
\left\lfloor\frac{r}{t-1}\right\rfloor.
\]

Consequently, if
\[
\boxed{r\le 3t-4,}
\]
then every such inverse-labeling coordinate is affine. Hence \(\varepsilon\) itself is an affine relabeling of a linear encoder, and \(C\) admits a linear \(t\)-PIR encoder with exactly the same recovery sets (with the recovery functions changed only by fixed output-bit complements).

Equivalently: in the binary low-redundancy range \(r\le 3t-4\), a nonlinear encoder onto a linear associated code cannot provide a \(t\)-PIR property that no linear encoder onto that code has.

## Proof

Fix a full-rank generator matrix
\[
G=(g_1\;\cdots\;g_n)\in \mathbb F_2^{k\times n}
\]
for \(C\), with columns \(g_i\in V:=\mathbb F_2^k\), and let
\[
\phi:V\to C,\qquad \phi(x)=xG
\]
be the resulting linear isomorphism. Define the permutation
\[
F:=\varepsilon^{-1}\circ\phi:V\to V,
\]
and write \(F=(f_1,\ldots,f_k)\), where each \(f_j:V\to\mathbb F_2\).

Fix a data coordinate \(j\), and abbreviate its disjoint recovery sets by \(I_1,\ldots,I_t\). Put
\[
W_s=\operatorname{span}\{g_i:i\in I_s\}\le V.
\]
The restriction of \(\phi(x)\) to the coordinates in \(I_s\) is determined by the linear map
\[
x\longmapsto (x\cdot g_i)_{i\in I_s},
\]
whose kernel is \(W_s^\perp\). Because \(I_s\) recovers the \(j\)-th data bit, \(f_j\) is constant on every coset of \(W_s^\perp\). Therefore \(f_j\) is invariant under
\[
H_j:=W_1^\perp+\cdots+W_t^\perp.
\]
It follows that \(f_j\) factors through \(V/H_j\). Since
\[
H_j^\perp=W_1\cap\cdots\cap W_t,
\]
the quotient dimension is
\[
d_j:=\dim(V/H_j)=\dim(W_1\cap\cdots\cap W_t).
\]

We now bound \(d_j\) using only redundancy and disjointness. Let
\[
L=W_1\cap\cdots\cap W_t,
\]
so \(\dim L=d_j\). Modulo \(L\),
\[
\dim(W_1+\cdots+W_t)
\le d_j+\sum_{s=1}^t(\dim W_s-d_j)
=\sum_{s=1}^t\dim W_s-(t-1)d_j.
\]
Let \(R=[n]\setminus(I_1\cup\cdots\cup I_t)\). Because the recovery sets are pairwise disjoint and all columns of \(G\) span \(V\),
\[
\begin{aligned}
k
&\le \dim(W_1+\cdots+W_t)+|R|\\
&\le \sum_{s=1}^t|I_s|-(t-1)d_j+n-\sum_{s=1}^t|I_s|\\
&=n-(t-1)d_j.
\end{aligned}
\]
Thus
\[
(t-1)d_j\le n-k=r,
\qquad\text{so}\qquad
\boxed{d_j\le\left\lfloor\frac r{t-1}\right\rfloor.}
\]

Assume now \(r\le3t-4\). Then \(d_j\le2\) for every \(j\). Since \(F\) is a permutation of \(V\), each Boolean coordinate \(f_j\) is balanced. Its induced Boolean function on the \(d_j\)-dimensional quotient is also balanced because all quotient fibers have equal size. A balanced Boolean function on a vector space of dimension at most two is affine: for dimension one this is immediate, while in \(\mathbb F_2^2\) every two-point subset is an affine line, so every balanced truth table is a nonconstant affine function. Hence every \(f_j\) is affine on \(V\).

Therefore
\[
F(x)=Ax+b
\]
for some \(A\in\operatorname{GL}(k,2)\) and \(b\in\mathbb F_2^k\); invertibility of \(A\) follows from bijectivity of \(F\). From \(F=\varepsilon^{-1}\circ\phi\),
\[
\varepsilon(a)=\phi\bigl(A^{-1}(a+b)\bigr).
\]
Define the linear encoder
\[
\varepsilon_{\rm lin}(a)=\phi(A^{-1}a).
\]
Then
\[
\varepsilon_{\rm lin}(a)=\varepsilon(a+b).
\]
Thus any recovery set that recovered the \(j\)-th bit under \(\varepsilon\) recovers \(a_j+b_j\) under \(\varepsilon_{\rm lin}\), and hence also recovers \(a_j\) after a fixed output-bit complement when \(b_j=1\). The same recovery sets therefore make \(\varepsilon_{\rm lin}\) a linear \(t\)-PIR encoder. This proves the theorem.

## Consequence for 3-PIR codes

For \(t=3\), the theorem applies whenever \(r\le5\). A binary linear 3-PIR code of dimension \(k\) and redundancy \(r\) is known to satisfy
\[
\binom r2\ge k.
\]
Hence the same inequality is necessary for any binary 3-PIR encoder whose associated code is linear and whose redundancy is at most five, even if the encoder itself was initially allowed to be nonlinear.

In particular, consider the open parameter pair highlighted by Hollmann and Luhaäär: length \(11\), size \(2^7\). Here \(k=7\) and \(r=4\). If the associated code were linear, the theorem would linearize its 3-PIR encoder, but
\[
\binom42=6<7,
\]
contradicting the linear 3-PIR redundancy bound. Therefore:
\[
\boxed{\text{Any binary 3-PIR code of length 11 and size }2^7\text{ must have a nonlinear associated code.}}
\]
This sharpens the previously stated necessity of being nonlinear as a PIR code: the alternative mechanism of a nonlinear encoder onto a linear code is impossible at these parameters.

## Relation to prior work

Hollmann and Luhaäär explicitly distinguish two ways a PIR code can be nonlinear: its associated code may be nonlinear, or a nonlinear encoder may label a linear associated code. They determine the optimal binary 3-PIR length through combinatorial dimension six, identify length 11 and size \(2^7\) as the next open case, and state that its existence is unknown. They also record the linear 3-PIR redundancy condition \(\binom r2\ge k\).

The present theorem addresses precisely the second source of nonlinearity in a general low-redundancy regime. Searches under PIR code, batch code, nonlinear encoder, nonlinear labeling, linear associated code, recovery sets, affine encoder, and the exact length-11/size-\(2^7\) problem did not locate this linearization statement or its consequence for the open case. Later work located through 2026 continues to develop linear PIR and batch-code variants without supplying this nonlinear-on-linear reduction. Originality is therefore asserted only to the best of our knowledge.

## Limitations

The theorem is binary. Its final affine-forcing step uses the exceptional fact that every balanced Boolean function of at most two variables is affine; analogous statements over larger alphabets need not hold in this form. The threshold \(r\le3t-4\) is sufficient, not claimed necessary. For \(r\ge3t-3\), the quotient dimension may reach three, where balanced nonlinear Boolean functions exist, so this proof no longer forces affine labeling. The length-11, size-\(2^7\) existence problem itself remains open: the result only proves that any solution must use a genuinely nonlinear associated code.

## References

1. H. D. L. Hollmann and U. Luhaäär, “Optimal possibly nonlinear 3-PIR codes of small size,” WAIFI 2022 / LNCS 13638 (2023), arXiv:2208.14552, https://arxiv.org/abs/2208.14552, DOI: 10.1007/978-3-031-22944-2_9.
2. S. Rao and A. Vardy, “Lower Bound on the Redundancy of PIR Codes,” arXiv:1605.01869, https://arxiv.org/abs/1605.01869.
3. S. Kurz and E. Yaakobi, “PIR Codes with Short Block Length,” Designs, Codes and Cryptography 89 (2021), 559–587, DOI: 10.1007/s10623-020-00828-6.
4. H. D. L. Hollmann, M. Puškin, and A.-E. Riet, “PIR Codes, Unequal-Data-Demand Codes, and the Griesmer Bound,” WCC 2024, arXiv:2407.18124, https://arxiv.org/abs/2407.18124.
