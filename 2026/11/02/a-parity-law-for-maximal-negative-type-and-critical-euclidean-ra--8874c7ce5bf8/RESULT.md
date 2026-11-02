# A parity law for maximal negative type and critical Euclidean rank of wheel metrics

## Finding

Let \(n\ge4\) be an integer, and let \(W_n=K_1\vee C_n\) be the wheel with **\(n\) rim vertices and one central vertex**; give each edge unit length and use graph shortest-path distance \(d\). For \(p\ge0\) let \(D_p=(d(u,v)^p)_{u,v\in V(W_n)}\), with diagonal zero, and define the attained normalized spectral negative-type gap
\[
\gamma_n(p)=\inf_{\substack{z\ne0\\\sum_vz_v=0}}\frac{-z^{\mathsf T}D_pz}{\sum_v z_v^2}.
\]
Put \(c_n=1\) if \(n\) is even and \(c_n=\cos(\pi/n)\) if \(n\) is odd. Then for **every** \(p\ge0\), including exponents beyond negative type,
\[
\boxed{\gamma_n(p)=2c_n-(2c_n-1)2^p.}
\]
Consequently, the supremal exponent of negative type (equivalently, maximal generalized roundness) is exactly
\[
\boxed{\wp(W_n)=\log_2\!\left(\frac{2c_n}{2c_n-1}\right).}
\]
Every wheel with an even rim has exponent exactly \(1\). Every wheel with an odd rim has exponent strictly greater than \(1\), decreasing to \(1\) along odd rim lengths, with
\[
\wp(W_n)=1+\frac{\pi^2}{2(\log 2)n^2}+O(n^{-4})\qquad(n\to\infty\text{ through odd integers}).
\]
At the critical exponent \(p=\wp(W_n)\), the squared-distance matrix \(D_p\) has exactly one zero direction on the zero-sum subspace when \(n\) is even, and exactly two when \(n\) is odd. The minimum Euclidean dimension of an isometric realization of the snowflaked metric \(d^{\,p/2}\) at that critical exponent is \(n-1\) for even \(n\) and \(n-2\) for odd \(n\). For \(0\le p<\wp(W_n)\) the dimension is \(n\), while \(p>\wp(W_n)\) admits no isometric Euclidean realization of those powered distances.

## Assumptions and scope

All metrics are finite real metric spaces and all quadratic forms are real. The wheel has exactly \(n+1\) vertices. Distinct rim neighbors have distance \(1\), distinct rim nonneighbors distance \(2\), and every rim vertex has distance \(1\) to the hub. The convention is \(d(v,v)^0=0\); off-diagonal distances to power zero equal \(1\). No normalization by the number of vertex pairs is used in \(\gamma_n(p)\); its denominator is the **Euclidean squared norm of the zero-sum coefficient vector**. This spectral normalization differs from the traditional load-simplex negative-type gap. The statement for \(n=3\) is deliberately excluded: \(W_3=K_4\), a discrete equidistant metric with negative type for all \(p\ge0\).

## Proof

Write \(t=2^p\ge1\). Enumerate the rim cyclically and let \(A\) be the adjacency matrix of \(C_n\). With the hub first, the powered distance matrix is
\[
D_p=\begin{pmatrix}0&\mathbf1^{\mathsf T}\\\mathbf1&t(J-I)+(1-t)A\end{pmatrix}.
\]
The Euclidean zero-sum space \(F=\{z:\sum_v z_v=0\}\) has the orthogonal direct sum
\[
F=F_{\mathrm{rim}}\oplus\operatorname{span}\{(-n,1,\ldots,1)\},
\quad F_{\mathrm{rim}}=\{(0,x):\sum_{j=0}^{n-1}x_j=0\}.
\]
The mixed quadratic pairing of these subspaces under \(D_p\) vanishes: the hub-to-rim row is constant, and every rim row has the same sum because the rim is a cycle. On the normalized hub/rim-constant direction the Rayleigh quotient of \(-D_p\) is
\[
\gamma_{\mathrm{rad}}(t)=\frac{2(n-1)-(n-3)t}{n+1}.
\]
On \(F_{\mathrm{rim}}\), the contribution \(tJ\) vanishes. The cycle Fourier characters with frequency \(k\in\{1,\ldots,n-1\}\) diagonalize the remaining quadratic form and give the eigenvalues
\[
\gamma_k(t)=t+2(t-1)\cos(2\pi k/n).
\]
For \(t\ge1\) their minimum equals \(t-2c_n(t-1)=2c_n-(2c_n-1)t\). The minimum is attained at frequency \(k=n/2\) for even \(n\), or at the conjugate frequencies \(k=(n\pm1)/2\) for odd \(n\). Their **real** multiplicities are \(1\) and \(2\), respectively.

It remains to compare the radial quotient. Subtraction gives
\[
\gamma_{\mathrm{rad}}(t)-\min_k\gamma_k(t)
=(t-1)\left(2c_n-1-\frac{n-3}{n+1}\right).
\]
The bracket is positive for all \(n\ge4\). For even \(n\), this is immediate from \(c_n=1\). For odd \(n\ge5\), \(\cos(\pi/n)>1-\pi^2/(2n^2)>1-2/(n+1)=(n-1)/(n+1)\), where the middle inequality follows from \(\pi^2<10\) and \(10(n+1)<4n^2\) for \(n\ge5\). Thus the cycle Fourier minimum is the **global** minimum on \(F\), proving the gap formula for every \(t\ge1\).

Because \(c_n>1/2\), the global minimum changes sign exactly at \(t=2c_n/(2c_n-1)\). This establishes the exact negative-type cutoff, as well as strict negative type before and failure afterward. At the cutoff the radial eigenvalue is positive, and only the listed Fourier modes vanish. For \(0\le p<\wp(W_n)\) all eigenvalues on \(F\) are strictly positive.

Let \(H=I-\mathbf1\mathbf1^{\mathsf T}/(n+1)\). Schoenberg's centered-Gram criterion states that \(d^{\,p/2}\) is isometrically Euclidean exactly when \(-\tfrac12 HD_pH\) is positive semidefinite, and the minimum ambient Euclidean dimension is its rank. Its nonzero spectrum is that of \(-D_p/2\) restricted to \(F\). Since \(\dim F=n\), the critical ranks are \(n-1\) and \(n-2\), while all subcritical ranks equal \(n\).

For odd \(n\), expand \(c_n=1-\pi^2/(2n^2)+O(n^{-4})\) and take the logarithm of the critical ratio. Along odd rim lengths, \(\cos(\pi/n)\) strictly increases and the function \(c\mapsto\log_2(2c/(2c-1))\) strictly decreases for \(c>1/2\), proving both monotonicity and the stated asymptotic law.

## Verification

The standalone standard-library program `check_wheel.py` reconstructs the powered-distance quadratic form independently by edge/nonedge pairs and checks its orthogonal block formula by exact rational arithmetic. It also compares every rim Fourier frequency against the proposed minimum for \(4\le n\le200\), tests radial dominance and the critical exponent, and independently evaluates sharp sine/cosine witnesses. It completed 10,009 checks without failure. These finite checks are supplementary; the preceding Fourier argument proves the formulas for every permitted \(n\) and \(p\).

For an explicit attainer of the gap, use a vector whose hub entry is zero and whose rim coordinates are \((-1)^j\) when \(n\) is even, or \(\cos(2\pi((n-1)/2)j/n)\) when \(n\) is odd. These vectors have zero sum and attain the asserted Rayleigh quotient.

## Relationship to prior work

Li–Weston (arXiv:0901.0695) establishes general behavior of strict negative type and its cutoff. Wolf (arXiv:1008.0964) develops finite-space negative-type gaps and computes the classical gap of **cycle path metrics**; its load-normalized gap is not the present \(\ell_2\)-Rayleigh invariant, and the wheel has different pair distances on the rim because of shortcuts via the hub. Sánchez (arXiv:1108.0451) provides a general finite metric determinant/inverse-matrix method and computes complete bipartite examples, not this wheel-family closed form. Murugan (arXiv:1112.5657) treats vertex-transitive graph metrics; \(W_n\) is not vertex transitive, as the hub and rim vertices have different degrees. Existing work on the Euclidean dimension of a **graph** via prescribed unit edges concerns a weaker realization notion than preserving every snowflaked shortest-path distance.

Thus the derivation here is not a claim that the general matrix criterion or the Fourier spectrum of a cycle is new. The proposed contribution is the wheel-specific all-exponent sharp Rayleigh law, the complete negative-type classification, and the parity-sensitive critical Euclidean rank. Older distance-geometry texts or alternate matrix formulations may nevertheless contain the same specialization; no claim of exhaustive novelty is made.

## Limitations

Only unweighted wheels with one hub, a simple cycle rim, and the unweighted shortest-path metric are covered. The normalized spectral gap is not the standard negative-type gap associated with normalized simplex loads. The theorem does not classify weighted wheels, generalized wheels with multiple hubs, wheels built on noncycle rims, or embeddings that preserve only graph edges. Full text of some older metric-transform and Euclidean graph-dimension literature could not be accessed; that leaves a residual historical coverage risk. The critical embeddings are guaranteed by a Gram representation, not by explicit coordinate tables in this report.

## References

- H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695v1 (publicly posted 2009-01-06), https://arxiv.org/abs/0901.0695.
- R. Wolf, *On the gap of finite metric spaces of p-negative type*, arXiv:1008.0964v1 (publicly posted 2010-08-05), https://arxiv.org/abs/1008.0964.
- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1 (publicly posted 2011-08-02), https://arxiv.org/abs/1108.0451.
- M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1 (publicly posted 2011-12-23), https://arxiv.org/abs/1112.5657.
- M. Horak, E. LaRose, J. Moore, M. Rooney and H. Rosenthal, *Roundness Properties of Graphs*, Involve 3 (2010), 67–91, DOI:10.2140/involve.2010.3.67, https://msp.org/involve/2010/3-1/involve-v3-n1-p05-p.pdf.
- M. Deza and H. Maehara, *Metric Transforms and Euclidean Embeddings*, Trans. Amer. Math. Soc. 317 (1990), 661–671, DOI:10.2307/2001482 (full text inaccessible in this examination).
- F. Buckley and F. Harary, *On the Euclidean Dimension of a Wheel*, Graphs Combin. 4 (1988), 23–30, DOI:10.1007/BF01864150 (different graph-edge embedding notion; full text inaccessible).
