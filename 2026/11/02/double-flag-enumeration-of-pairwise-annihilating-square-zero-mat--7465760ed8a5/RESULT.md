# Double-flag enumeration of pairwise annihilating square-zero matrix tuples

## Finding
For every prime power \(q\), integers \(n,m\ge1\), and every prescribed vector of ranks \(\mathbf r=(r_1,\ldots,r_m)\), there is an exact formula for the number of ordered \(m\)-tuples of matrices \((T_1,\ldots,T_m)\in M_n(\mathbb F_q)^m\) satisfying \(T_iT_j=0\) for every ordered pair \(i,j\), with \(\operatorname{rank}T_i=r_i\), common image span of dimension \(t\), and common kernel of dimension \(k\).

Write \({a\brack b}_q\) for the Gaussian binomial coefficient (zero unless \(0\le b\le a\)), and let the number of rank-\(r\) linear maps from a \(b\)-space to an \(a\)-space be
\[
R_q(a,b;r)={a\brack r}_q\prod_{h=0}^{r-1}(q^b-q^h).
\]
Set \(d=n-k\). When \(0\le t\le k\le n\), the exact number is
\[
\boxed{N_{n,q}(\mathbf r,t,k)={n\brack k}_q{k\brack t}_q
\sum_{j=0}^{t}\sum_{\ell=0}^{d}
(-1)^{t-j+\ell}q^{\binom{t-j}{2}+\binom{\ell}{2}}
{t\brack j}_q{d\brack\ell}_q
\prod_{i=1}^{m}R_q(j,d-\ell;r_i).}
\]
For parameter values outside \(0\le t\le k\le n\), the count is zero. This joint distribution simultaneously determines every marginal distribution of individual ranks, the common image span, and the common kernel, for arbitrary tuple length. It counts actual labeled matrices rather than similarity classes.

## Assumptions and scope
All vector spaces are finite-dimensional over \(\mathbb F_q\). The ordered-pair condition includes \(i=j\), hence each matrix is square-zero. Define \(U=\sum_i\operatorname{im}T_i\) and \(K=\bigcap_i\ker T_i\); then \(t=\dim U\), \(k=\dim K\). An empty product equals one. The formula handles zero maps, \(n=1\), \(m=1\), and all field characteristics without exceptional conventions. Formula evaluation uses integer Gaussian coefficients and finite sums; there is no analytic convergence condition.

## Proof
**1. Exact flag factorization.** The product equations imply \(T_j(\operatorname{im}T_i)=0\) for every \(i,j\), so \(U\subseteq K\). Conversely, choose any flag \(U\subseteq K\subseteq V\) with the prescribed dimensions. Every tuple with common image span \(U\) and common kernel \(K\) factors uniquely through maps \(f_i:D=V/K\to U\), by \(T_i=\iota_U f_i\pi_K\). Since \(U\subseteq K\), all products of these maps vanish. Further, \(\operatorname{rank}T_i=\operatorname{rank}f_i\), their images span \(U\) exactly when the images of \(f_i\) do, and their common kernel equals \(K\) exactly when \(\bigcap_i\ker f_i=0\) inside \(D\). There are \({n\brack k}_q{k\brack t}_q\) choices of the flag. No choice of splittings is necessary.

**2. Exact rank-map count.** For any \(a,b,r\), first choose an \(r\)-dimensional image in the \(a\)-space (\({a\brack r}_q\) choices), and then choose a surjection from the \(b\)-space to that image (\(\prod_{h=0}^{r-1}(q^b-q^h)\) choices). Their product is \(R_q(a,b;r)\).

**3. Two independent subspace Möbius inversions.** In the lattice of subspaces of a finite-dimensional \(\mathbb F_q\)-space the interval Möbius function is \(\mu(W,Z)=(-1)^c q^{\binom c2}\), where \(c=\dim Z-\dim W\). To require that the images of the \(f_i\) span all of \(U\), invert over subspaces \(W\subseteq U\); a subspace of dimension \(j\) contributes \((-1)^{t-j}q^{\binom{t-j}2}{t\brack j}_q\). Independently, to require that their common kernel in \(D\) is zero, invert over subspaces \(H\subseteq D\) on which every \(f_i\) vanishes; a subspace of dimension \(\ell\) contributes \((-1)^\ell q^{\binom\ell2}{d\brack\ell}_q\). For fixed \(W,H\), the \(f_i\) are independent rank-\(r_i\) maps \(D/H\to W\). There are precisely \(\prod_iR_q(j,d-\ell;r_i)\) such tuples. Multiplication by the flag count proves the displayed formula, including degenerate and boundary cases. This argument is an exact finite count, not an asymptotic or experimental inference.

**4. Classical one-operator boundary.** For \(m=1\), a map of rank \(r\) has \(t=r\) and \(k=n-r\), and the formula reduces to the familiar square-zero rank census \({n\brack n-r}_q{n-r\brack r}_q\lvert\operatorname{GL}_r(\mathbb F_q)\rvert\). This reduction also verifies the handling of empty or impossible strata.

## Verification
The accompanying standard-library checker `check.py` independently enumerates all matrices and all ordered tuples in six small prime-field configurations, computes the original pairwise products, and determines the triple of statistics by Gaussian elimination. It checks every attainable and unattainable rank/image/kernel stratum against the exact formula. A second checker `check_f4.py` uses genuine extension-field arithmetic in \(\mathbb F_4=\mathbb F_2[z]/(z^2+z+1)\). Run `python3 check.py` and `python3 check_f4.py` from the directory containing both scripts. The captured exact output is in `check_output.txt`. Finite verification is corroborative; the proof above establishes arbitrary sizes and finite fields.

The exhaustive tuple totals in the six primary cases, expressed as \((n,q,m;\mathrm{total})\), are \((2,2,2;10)\), \((2,3,3;105)\), \((3,2,2;148)\), \((3,2,3;736)\), \((3,3,2;1665)\), \((4,2,2;8296)\). Over \(\mathbb F_4\), the \((2,4,2)\) total is \(76\).

## Relationship to prior work
Schröer [1] studies geometric irreducible components for mutually annihilating nilpotent **pairs**, including square-zero pairs. Bondarenko–Gerasimova–Sergeichuk [2] give canonical forms for arbitrary-field **pairs** under simultaneous similarity. Britnell–Wildon [3] treat commuting similarity classes and nilpotent class types over finite fields, not enumeration of labeled zero-product tuples refined by two joint subspaces. Huang [4] provides generating series for mutually annihilating **pairs** and nilpotent pairs over finite fields, without the present all-arity, individual-rank, common-image, common-kernel refinement. The present formula does not claim new pair classification, individual square-zero rank counts, Gaussian coefficients, or Möbius inversion as techniques. Its contribution is the uniform joint refined count for all arities, including the independent socle/radical dimensions of representations of a local radical-square-zero algebra with arbitrary loop number.

## Limitations
The result counts labeled representations, not simultaneous-conjugacy classes, indecomposable types, orbit closures, or scheme structures. It applies to all ordered products equal to zero; merely commuting square-zero matrices need not satisfy these conditions. The finite-field formula is not an arbitrary-field geometric component classification. An unidentified general enumerative theorem for multi-loop radical-square-zero representations could imply this specialization; literature priority has not been independently validated.

## References
[1] Jan Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293, first posted 2002-11-19.

[2] Vitalij M. Bondarenko, Tatiana G. Gerasimova, Vladimir V. Sergeichuk, *Pairs of mutually annihilating operators*, arXiv:0812.2155, first posted 2008-12-11.

[3] John R. Britnell, Mark Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, first posted 2010-01-06; primary MSC 15A27 in the published article.

[4] Yifeng Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566, first posted 2021-10-29.
