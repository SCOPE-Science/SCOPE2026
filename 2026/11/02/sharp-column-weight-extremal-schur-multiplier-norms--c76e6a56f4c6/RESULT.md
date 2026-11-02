# Sharp column-weight extremal Schur multiplier norms

## Finding
Let \(v\ge2\) and \(1\le k<v\) be integers. For every integer \(n\ge1\), let \(B\) be a \(v\)-by-\(n\) zero-one matrix with exactly \(k\) ones in each column, and let \(J\) be the all-ones matrix of the same size. For every pair of complex scalars \(a,b\), write \(\mathcal S_{aJ+bB}\) for Schur multiplication by \(aJ+bB\) on the spectral-norm space of complex \(v\)-by-\(n\) matrices. The following is the **exact universal extremum**, with no bound on the number of columns:

\[
\sup_{n\ge1}\ \sup_{B:\ \sum_i B_{ij}=k}\|\mathcal S_{aJ+bB}\|
=\left|a+\frac{bk}{v}\right|+\frac{|b|}{v}\sqrt{k(v-k)(v-1)}.
\]

The maximum is attained by the incidence matrix whose columns are all \(k\)-subsets of a \(v\)-element set. More generally, the same equality holds for every nontrivial \(2\)-\((v,k,\lambda)\) block design, with each block represented by one column. For real \(a,b\), the optimal constant and these examples are unchanged if the spectral-norm spaces are taken over the reals.

In particular, if each column of a sign matrix has exactly \(k\) negative entries (put \(a=1,b=-2\)), its sharp universal Schur norm is
\[
\left|1-\frac{2k}{v}\right|+\frac{2}{v}\sqrt{k(v-k)(v-1)}.
\]
If each column of a zero-one symbol has exactly \(k\) ones (put \(a=0,b=1\)), the sharp universal norm is
\[
\frac{k}{v}+\frac{1}{v}\sqrt{k(v-k)(v-1)}.
\]

The sign extremum approaches \(1+2\sqrt{k}\) for fixed \(k\) as \(v\to\infty\), although the negative-entry density tends to zero. For even \(v\) and \(k=v/2\), it is exactly \(\sqrt{v-1}\). In the balanced case, any sign matrix attaining that value has at least \(v-1\) columns; whenever an order-\(v\) real Hadamard matrix exists, deleting its all-ones column after normalization gives an extremizer with exactly \(v-1\) columns. In particular, this column minimum is attained for every Sylvester order \(v=2^j\), \(j\ge1\).

## Assumptions and scope
The row count \(v\) is fixed, the common column weight satisfies \(1\le k\le v-1\), and the column count \(n\) is any positive integer. Multiplication acts on matrices as operators \(\ell_2^n\to\ell_2^v\), so the norm is the usual spectral operator norm, **not** the entrywise Frobenius norm or a graph adjacency norm. The first theorem allows complex \(a,b\), and all upper and lower bounds apply to complex matrices. Its real-scalar case also holds over real operator spaces. No assertion that an arbitrary admissible \(B\) is an extremizer is made.

## Proof
**1. A universal sharp upper bound.** Put \(c=a+bk/v\), and let \({\bf1}\in\mathbb R^v\) denote the all-ones vector. Define \(h_i=e_i-v^{-1}{\bf1}\) and, for the \(j\)-th incidence column \(B_j\), define \(f_j=B_j-(k/v){\bf1}\). Since the entries of \(B_j\) are zero or one and its column sum is \(k\),
\[
\langle h_i,f_j\rangle=B_{ij}-k/v,\qquad
\|h_i\|_2^2=1-1/v,\qquad
\|f_j\|_2^2=k(1-k/v).
\]
Consequently \((aJ+bB)_{ij}=c+b\langle h_i,f_j\rangle\). For \(b\ne0\), any \(\tau>0\) gives a factorization using row vectors
\(u_i=(c/\sqrt\tau,\sqrt{|b|}\,h_i)\) and column vectors
\(w_j=(\sqrt\tau,b f_j/\sqrt{|b|})\). Their algebraic pairings are the desired matrix entries. The elementary Schur factorization bound gives
\[
\|\mathcal S_{aJ+bB}\|\le
\sqrt{\left(\frac{|c|^2}{\tau}+|b|\frac{v-1}{v}\right)
\left(\tau+|b|\frac{k(v-k)}v\right)}.
\]
Here the bound follows by expressing the entrywise product as a sum of diagonal left and right multipliers and applying the operator Cauchy–Schwarz inequality. Minimizing in \(\tau\) gives
\[
\|\mathcal S_{aJ+bB}\|
\le |c|+\frac{|b|}{v}\sqrt{k(v-k)(v-1)}.
\]
If \(b=0\), the multiplier is scalar and has norm \(|a|\). If \(c=0\), the same bound follows by taking \(\tau\downarrow0\), or by omitting the constant factor; thus the boundary cases are included.

**2. A universal nuclear-trace lower bound.** For every complex \(v\)-by-\(n\) matrix \(M\), let \(Q\) be its rectangular polar partial isometry, chosen so \(\|Q\|_{\mathrm{op}}\le1\) and \(\sum_{ij}M_{ij}\overline{Q_{ij}}=\|M\|_*\). Testing \(\mathcal S_M\) on \(\overline Q\) and pairing its output with normalized all-ones vectors gives
\[
\|\mathcal S_M\|\ge\frac{\|M\|_*}{\sqrt{vn}}.
\]
The same argument uses a real polar partial isometry when \(M\) is real.

**3. Tightness via complete uniform incidence.** Take \(N\) with one column for every \(k\)-subset of \(\{1,\ldots,v\}\), so \(n=\binom vk\). Every point belongs to \(r=\binom{v-1}{k-1}\) blocks, every distinct pair to \(\lambda=\binom{v-2}{k-2}\) blocks (zero if \(k=1\)), and
\[
NN^*=(r-\lambda)I+\lambda J,\qquad
r-\lambda=\frac{nk(v-k)}{v(v-1)}.
\]
For \(M=aJ+bN\), the normalized constant row direction has singular value \(\sqrt{vn}|c|\); each of the \(v-1\) orthogonal row directions has singular value \(|b|\sqrt{r-\lambda}\). Thus
\[
\frac{\|M\|_*}{\sqrt{vn}}
=|c|+\frac{(v-1)|b|\sqrt{r-\lambda}}{\sqrt{vn}}
=|c|+\frac{|b|}{v}\sqrt{k(v-k)(v-1)},
\]
matching the upper bound. If a \(2\)-\((v,k,\lambda)\) block design is used instead, the same incidence identity holds with \(r=\lambda(v-1)/(k-1)\), hence the same conclusion. When \(k=1\), the complete singleton system supplies the required equality separately.

**4. Balanced-column minimum and sparse asymptotics.** In the signed case with \(v\) even and \(k=v/2\), the sharp expression becomes \(\sqrt{v-1}\). Every \(v\)-by-\(n\) sign matrix satisfies \(\|\mathcal S_M\|\le\sqrt n\), because \(\|M\circ X\|_{\mathrm{op}}\le\|M\circ X\|_F=\|X\|_F\le\sqrt n\|X\|_{\mathrm{op}}\). Therefore equality forces \(n\ge v-1\). A normalized Hadamard matrix of order \(v\), with its constant column removed, has balanced columns and mutually orthogonal remaining columns; the nuclear-trace lower bound equals \(\sqrt{v-1}\), proving the sharp column count whenever such a matrix exists. For fixed \(k\), expansion of the exact sign formula gives
\[
1+2\sqrt k-\frac{2k+(k+1)\sqrt k}{v}+O_k(v^{-2}).
\]

## Verification
A standalone numerical verifier `verify_sparse_sign.py` reconstructs every complete \(k\)-subset incidence system with \(2\le v\le9\), checks its integral two-design Gram identity, and independently evaluates singular values and polar witnesses for five coefficient pairs (180 full-orbit cases). It also tests the universal bound against nuclear-trace lower bounds on 1,155 random admissible column systems, and verifies the balanced four-row Hadamard example. Replay with `python3 verify_sparse_sign.py` using NumPy. These tests check implementation and finite boundary cases; the proof above establishes the infinite quantified theorem.

## Relationship to prior work
The Schur-factorization upper bound is classical (Grothendieck–Haagerup), and Davidson and Donsig's *Norms of Schur Multipliers* (2005) provides sparse-pattern bounds and Mathias's normalized-trace criterion for suitably symmetric square matrices. Levene's *Norms of idempotent Schur multipliers* (2013/2014) studies norms of zero-one symbols and their small-norm gaps. Holbrook, Johnston, and Schoch's *Real Schur norms and Hadamard matrices*, first public June 6, 2022, establishes the unrestricted square sign-matrix maximum and its relation to Hadamard matrices, including discussion of rectangular norms. This finding instead solves the **fixed column Hamming weight**, arbitrary-width extremal problem for an entire complex two-level affine pencil, with exact finite-size constants and design-based equality. The proof is elementary once the classical Schur-factorization framework is available; no assertion of priority for that framework is made.

## Limitations
The theorem is about the **supremum across all finite widths**, not an exact formula for every individual incidence matrix or for every prescribed width. The complete family of equality supports is not classified, and one should not infer that only block designs attain equality. Results for different column weights, or for matrix norms other than the spectral norm, are not proved. Broad prior multiplier-factorization theorems may permit alternative derivations; a hidden earlier exact constrained extremal statement remains possible.

## References
1. J. Holbrook, N. Johnston, and J.-P. Schoch, *Real Schur norms and Hadamard matrices*, arXiv:2206.02863v1 (first posted 2022-06-06), https://arxiv.org/abs/2206.02863.
2. K. R. Davidson and A. P. Donsig, *Norms of Schur Multipliers*, arXiv:math/0506073v1 (2005), especially the factorization estimates and Theorem 4.5, https://arxiv.org/abs/math/0506073.
3. R. H. Levene, *Norms of idempotent Schur multipliers*, arXiv:1302.4849 (first posted 2013; revised 2014), https://arxiv.org/abs/1302.4849.
