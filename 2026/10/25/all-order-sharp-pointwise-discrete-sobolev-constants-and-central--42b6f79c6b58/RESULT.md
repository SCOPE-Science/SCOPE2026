# All-order sharp pointwise discrete Sobolev constants and central extremizers

## Finding
For integers \(r,d\geq1\), extend \(a=(a_1,\ldots,a_d)\in\mathbb C^d\) by zero to every integer index, and put \((\Delta a)_k=a_k-a_{k-1}\). The exact smallest constant in
\[
\max_{1\leq j\leq d}|a_j|\leq C_{r,d}\Big(\sum_{k=1}^{d+r}|(\Delta^r a)_k|^2\Big)^{1/2}
\]
is the following finite product-sum. Define the rising product \(R_s(t)=\prod_{h=0}^{s-1}(t+h)\), with \(R_0(t)=1\), and \(m=\lfloor(d+1)/2\rfloor\). Then
\[
\boxed{C_{r,d}^2=\frac{1}{((r-1)!)^2 R_{2r-1}(d+1)}\sum_{k=0}^{m-1}(d-2k)R_{r-1}(k+1)^2R_{r-1}(d-k+1)^2.}
\]
The only maximizing evaluation positions are \(j=m\) when \(d\) is odd, and \(j=m,m+1\) when \(d\) is even. All nonzero equality sequences are the complex scalar multiples of the corresponding Green vectors described below, with no further equality cases. For each fixed integer \(r\ge1\),
\[
\boxed{C_{r,d}\sim\frac{d^{r-1/2}}{2^{2r-1}(r-1)!\sqrt{2r-1}}\quad(d\to\infty).}
\]
In particular, at second difference order \(r=2\), the exact squared point-evaluation constant at position \(j\) is
\[
G_{jj}=\frac{j(j+1)(d-j+1)(d-j+2)(2dj+d-2j^2+2j+3)}{6(d+1)(d+2)(d+3)}.
\]

## Assumptions and scope
The integer orders and lengths satisfy \(r,d\ge1\). Sequences may be real or complex; no sign assumption is imposed. The difference is the backward difference of the zero extension on \(\mathbb Z\), and every nonzero difference term is counted, over indices \(1,\ldots,d+r\). All products use the convention \(R_0=1\). The norm on the right is a genuine Hilbert norm, since the difference map is injective. No statement is made about \(\ell^q\) targets at finite \(q\), or about noninteger difference orders.

## Proof
Let \(D\colon\mathbb C^d\to\mathbb C^{d+r}\) be the order-\(r\) difference matrix. Its positive definite Gram matrix \(H=D^*D\) is the symmetric Toeplitz matrix
\[
H_{ij}=\begin{cases}(-1)^{i-j}\binom{2r}{r+i-j},&|i-j|\le r,\\0,&|i-j|>r.\end{cases}
\]
Let \(G=H^{-1}\). By the Cauchy--Schwarz inequality in the inner product \(\langle u,v\rangle_D=\langle Du,Dv\rangle\),
\[
|a_j|^2\le G_{jj}\,\|Da\|_2^2,
\]
with equality if and only if \(a\) is a scalar multiple of \(Ge_j\). Thus the sharp squared constant is \(\max_jG_{jj}\).

We compute the complete first inverse column. For \(1\le j\le d\), set
\[
c_j=\frac{R_{r-1}(j)R_r(d-j+1)}{(r-1)!R_r(d+r)}.
\]
Then \(Hc=e_1\). Indeed, the right side as a polynomial in \(j\) has degree \(2r-1\), and its centered order-\(2r\) finite difference vanishes identically. For \(r\ge2\), the polynomial vanishes at the left sites \(j=0,-1,\ldots,2-r\); for \(r=1\), no left-side polynomial zero is needed. It also vanishes at the right sites \(j=d+1,\ldots,d+r\). These are exactly the fictitious sites involved in rows \(2,\ldots,d\). Only row \(1\) misses the polynomial value at \(j=1-r\); the corresponding Toeplitz coefficient is \((-1)^r\) and this polynomial value is \((-1)^{r-1}\). Removing this term gives \((Hc)_1=1\). Therefore \(c_j=G_{j1}\), and in particular \(c_1=R_r(d)/R_r(d+r)>0\). These statements include \(r=1\) under the empty-product convention.

For completeness, the Toeplitz inverse diagonal recurrence (Trench--Gohberg--Semencul identity) says that for a real symmetric invertible Toeplitz matrix with inverse first column \(c\) and \(c_1\ne0\),
\[
G_{j+1,j+1}-G_{jj}=\frac{c_{j+1}^2-c_{d-j+1}^2}{c_1},\quad 1\le j<d,
\]
with \(G_{11}=c_1\). One directly verifies it by multiplying the Toeplitz matrix by \((LL^\mathsf T-UU^\mathsf T)/c_1\), where \(L\) is lower triangular Toeplitz with first column \((c_1,\ldots,c_d)^\mathsf T\), and \(U\) is lower triangular Toeplitz with first column \((0,c_d,\ldots,c_2)^\mathsf T\); the product is the identity. The diagonal of this inverse expression equals \(c_1^{-1}(\sum_{h=1}^j c_h^2-\sum_{h=1}^{j-1}c_{d-h+1}^2)\), giving the recurrence.

Substituting the explicit first column and canceling the common rising products yields
\[
\boxed{G_{j+1,j+1}-G_{jj}=\frac{(d-2j)R_{r-1}(j+1)^2R_{r-1}(d-j+1)^2}{((r-1)!)^2R_{2r-1}(d+1)}.}
\]
The same expression at \(j=0\) equals \(G_{11}\), so telescoping from index zero gives the stated finite sum for every \(G_{jj}\). For integer \(1\le j<d\), its sign is precisely the sign of \(d-2j\). Hence the diagonal strictly increases towards the middle, has one zero increment only when \(d\) is even, and strictly decreases afterwards. This proves both the exact sharp constant and all maximizing indices. The Cauchy--Schwarz equality condition already proves the equality-sequence classification. The stated order-two expression follows by expanding the finite sum (or checking its first value and the displayed recurrence).

For the asymptotic, divide the finite sum for the central index by \(d^{2r-1}\). Its summands form a Riemann sum converging to
\[
\frac1{((r-1)!)^2}\int_0^{1/2}(1-2x)[x(1-x)]^{2r-2}\,dx
=\frac{4^{-(2r-1)}}{(2r-1)((r-1)!)^2}.
\]
Taking the positive square root completes the proof.

## Verification
The independent algebraic paths are (i) a finite-difference polynomial check for the inverse first column, (ii) the standard Toeplitz inverse recurrence, and (iii) the positive factorization of the diagonal increment. An included pure-Python rational checker constructs the exact Gram matrix and inverts it for every \(1\le r\le5\), \(1\le d\le11\); it verifies the first column, every diagonal finite-sum identity, and the central maximum, yielding 715 exact assertions. These tests are finite consistency checks, not substitutes for the all-orders proof.

## Relationship to prior work
Hindov, Nitzan, Olsen, and Rydhe (2026) determine the \(\ell^1\)-versus-\(\ell^2\) sharp constant for every integer difference order, but explicitly scope their theorem to that target norm. The present result determines the distinct \(\ell^\infty\) target for every order and length and classifies all maximizers. The Toeplitz inverse recurrence is classical; Dow (2003, Section 3.3) explicitly computes the fourth-order case corresponding to \(r=2\), so the order-two specialization is *not* claimed individually as new. The new content is the all-order binomial-product inverse-column identity combined with universal central monotonicity, sharp constants and their asymptotic law. The general Toeplitz inversion machinery is acknowledged as a prerequisite rather than newly derived.

## Limitations
Historical priority for the all-orders closed product formula remains subject to further bibliographic review, particularly in the theory of discrete Green functions and Fisher--Hartwig Toeplitz inverses. The result does not say that a general Toeplitz inverse formula is new, nor does it settle other \(\ell^q\) targets. Independent scientific validation has not been performed.

## References
1. R. Hindov, S. Nitzan, J.-F. Olsen, E. Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1 (first posted 2026-10-13), https://arxiv.org/html/2610.19010v1.
2. M. Dow, *Explicit inverses of Toeplitz and associated matrices*, ANZIAM Journal **44** (2003), E185--E215, Sections 3 and 3.3, https://journal.austms.org.au/ojs/index.php/ANZIAMJ/article/view/493/357.
3. Gohberg--Semencul--Trench Toeplitz inverse recurrence, in Dow (2003), Section 3.3, citing Trench.
4. MSC2020, classification 46E39, *Sobolev (and similar kinds of) spaces of functions of discrete variables*, https://msc2020.org/MSC_2020.pdf.
