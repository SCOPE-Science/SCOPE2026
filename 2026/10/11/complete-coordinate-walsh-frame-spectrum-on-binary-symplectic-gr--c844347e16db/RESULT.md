# Complete coordinate Walsh-frame spectrum on binary symplectic groups
## Finding
For every integer \(m\ge 2\), set \(d=2m\), \(Q=2^d\), and let \(\operatorname{Sp}(d,2)\) be the group of invertible binary matrices preserving the standard symplectic form \(J=\begin{psmallmatrix}0&I_m\\I_m&0\end{psmallmatrix}\). On this group, with normalized counting measure, consider the \(1+d^2\) real-valued functions
\[
 f_0(A)=1,\qquad f_{ij}(A)=(-1)^{A_{ij}}\quad(1\le i,j\le d).
\]
These functions form a linearly independent Riesz family. Their complete Gram eigenvalue multiset, sharp bounds, and equality eigenspaces are as follows.

Define
\[
 \beta=-\frac1{Q-1},\quad a=\frac{2Q}{(Q-1)(Q-4)},\quad b=\frac2{Q-1},\quad c=\frac{Q}{Q-1},
\]
\[
 s=c+b-2a(d-2),\qquad t=c-b,\qquad r=c+4a+b,\qquad v=c+b,
\]
\[
 g=c+\beta d^2+a(d-2)^2+b,\qquad h=\beta d,\qquad
 \ell_\pm=\frac{1+g\pm\sqrt{(1-g)^2+4h^2}}2.
\]
The Gram spectrum, counted with multiplicity, is
\[
\begin{array}{c|ccccc}
 \text{eigenvalue}&s&t&r&v&\ell_-,\ell_+\\\hline
 \text{multiplicity}&2(m-1)&2m^2&(m-1)^2&m^2&1\text{ each}.
\end{array}
\]
Different displayed eigenvalue expressions may coincide at an isolated small parameter; the table is a multiset statement. The sharp lower bound is always \(s\); the sharp upper bound is \(r\) when \(m\in\{2,3\}\), and \(\ell_+\) when \(m\ge4\). Both upper-bound alternatives are strictly separated at these respective parameter ranges. Thus the sharp squared Riesz condition number is
\[
 \kappa_m^2=\begin{cases}r/s,&m=2,3,\\\ell_+/s,&m\ge4.\end{cases}
\]
In particular \(\kappa_2^2=43/11\), \(\kappa_3^2=559/367\), and as \(m\to\infty\),
\[
 \kappa_m^2=1+\frac{d^2+O(d)}{2^d}.
\]

## Assumptions and scope
All vector spaces, matrices, and bilinear pairings in the construction use \(\mathbb F_2\). The standard form pairs coordinate \(i\) with \(\tau(i)=i+m\) for \(1\le i\le m\), and \(\tau(i)=i-m\) otherwise. Let \(\mathbf1\in\mathbb R^d\) denote the all-ones vector. Define the orthogonal subspaces
\[
 U=\operatorname{span}\{\mathbf1\},\quad
 V=\left\{x:x_i=x_{\tau(i)},\ \sum_i x_i=0\right\},\quad
 W=\left\{x:x_i=-x_{\tau(i)}\right\}.
\]
Their dimensions are \(1,m-1,m\), respectively. Regard the \(d^2\) nonconstant coordinate features as indexed by \(\mathbb R^d\otimes\mathbb R^d\). In the full coefficient space \(\mathbb R\oplus(\mathbb R^d\otimes\mathbb R^d)\), the equality eigenspaces are
\[
\begin{array}{c|l}
 s& U\otimes V\oplus V\otimes U\\
 t& U\otimes W\oplus W\otimes U\oplus V\otimes W\oplus W\otimes V\\
 r&V\otimes V\\
 v&W\otimes W.
\end{array}
\]
For the remaining pair, put \(e_0=(1,0)\) and \(u=(0,d^{-1}\mathbf1\otimes\mathbf1)\), which are orthonormal. The eigenspace for \(\ell\in\{\ell_-,\ell_+\}\) is the line spanned by \(h e_0+(\ell-1)u\). If eigenvalues accidentally coincide, their eigenspaces are summed. All assertions include the smallest allowed dimension \(d=4\); no claim is made for \(d=2\).

## Proof
**Exact pair correlations.** Symplectic transitivity (Witt extension) makes a single column uniform among nonzero vectors and an ordered pair of distinct columns uniform among linearly independent pairs \((x,y)\) with prescribed pairing \(\langle x,y\rangle=c\in\mathbb F_2\). Let \(Q=2^d\). The numbers of such pairs are
\[
 N_1=(Q-1)Q/2,\qquad N_0=(Q-1)(Q/2-2).
\]
For nonzero coordinate covectors \(a_1,a_2\), binary character orthogonality gives the unrestricted identity
\[
 \sum_{\langle x,y\rangle=c}(-1)^{a_1\cdot x+a_2\cdot y}
 =\frac Q2(-1)^{c+\langle a_1,a_2\rangle}.
\]
Indeed, insert \(\mathbf1_{\langle x,y\rangle=c}=[1+(-1)^{c+\langle x,y\rangle}]/2\), sum first in \(y\), and use the invertibility and involutivity of the matrix \(J\). For \(c=1\), all pairs are automatically linearly independent. For \(c=0\), subtract pairs with \(x=0\), \(y=0\), or \(x=y\); inclusion-exclusion yields the numerator
\[
 \frac Q2(-1)^{\langle a_1,a_2\rangle}-Q\mathbf1_{a_1=a_2}+2.
\]
Dividing by \(N_c\), and also treating identical columns using uniform nonzero vectors, proves the Gram correlation rule: diagonal entries are \(1\); any distinct pair of features has value \(\beta=-1/(Q-1)\), except that features \((i,j),(k,l)\) with \(i\ne k\), \(j\ne l\) have value
\[
 \begin{cases}
 (Q+4)/[(Q-1)(Q-4)],& k\ne\tau(i),\ l\ne\tau(j),\\
 1/(Q-1),&k=\tau(i),\ l=\tau(j),
 \end{cases}
\]
in those two exceptional cases. Every constant-to-coordinate Gram entry equals \(\beta\).

**Gram diagonalization.** Let \(M\) be the permutation matrix of \(\tau\), \(K=\mathbf1\mathbf1^{\mathsf T}-I-M\), and let \(\mathsf J\) denote the all-ones \(d\)-by-\(d\) matrix. The coordinate-coordinate block is exactly
\[
 G_{\rm coord}=(1-\beta)I_{d^2}+\beta(\mathsf J\otimes\mathsf J)
 +a(K\otimes K)+b(M\otimes M).
\]
The simultaneous eigenvalue triples of \((\mathsf J,M,K)\) on \(U,V,W\) are \((d,1,d-2)\), \((0,1,-2)\), and \((0,-1,0)\). Tensoring yields \(s,t,r,v\) and all their claimed eigenspaces and dimensions. The constant and normalized uniform tensor couple only to each other, giving the two-by-two real symmetric block
\[
 \begin{pmatrix}1&h\\h&g\end{pmatrix},
\]
whose eigenvalues and eigenlines are precisely \(\ell_\pm\).

**Strict extremal ordering.** Direct algebra gives
\[
 s=\frac{Q^2+(6-4d)Q-8}{(Q-1)(Q-4)}>0
\]
for every even \(d\ge4\), because \(Q=2^d\ge4d\). Also \(s<t\), \(s<v\), and \(s<r\). The determinant of the displayed two-by-two block minus \(sI\) is
\[
 \frac{4d\,[Q^2(d^2-7d+11)+Q(4d^2-6d-12)+8d]}{(Q-4)^2(Q-1)^2}>0.
\]
The bracket is positive directly at \(d=4,Q=16\) and has all positive summands for even \(d\ge6\). Since \(s<1\), positivity of this determinant implies \(s<\ell_-\). This proves positive definiteness and the sharp lower bound.

The largest scalar eigenvalue is \(r>1\). Since \(\ell_-<1<r\), the sign of the determinant of the two-by-two block minus \(rI\) decides whether \(r\) or \(\ell_+\) is larger. That determinant equals
\[
 -\frac{4d\,[Q^2(3d-22)+Q(6d+24)-8d]}{(Q-4)^2(Q-1)^2}.
\]
Its bracket is negative at \((d,Q)=(4,16)\) and \((6,64)\), and strictly positive for every even \(d\ge8\). This establishes the claimed strict crossover and sharp upper bound. Finally, the explicit formulas imply \(s=1-(4d+O(1))/Q\) and \(\ell_+=1+(d^2+O(d))/Q\); their ratio gives the stated condition-number asymptotic.

## Verification
The included standalone `symplectic_frame_check.py` (Python 3 with SymPy and NumPy) independently constructs all \(720\) elements of \(\operatorname{Sp}(4,2)\) by symplectic transvections and compares all \(289\) exact Gram entries against the formula. It directly enumerates admissible two-column pairs in dimensions \(4,6,8\), checks tensor eigenspaces in dimensions \(4,6\), verifies both determinant identities symbolically, and tests the crossover inequalities for dimensions \(4\) through \(128\). Run `python symplectic_frame_check.py`; the expected terminal marker is `VERIFY_OK`. The infinite-dimensional-range assertion is proved by the algebra above, not inferred from these checks.

## Relationship to prior work
Eldar and Bölcskei (arXiv:math/0108096, initially public 13 August 2001) develop Gram and Fourier diagonalization methods for finite frames generated by abelian unitary groups; their theorems do not furnish the specific Gram coefficients or the present symplectic-group spectrum. Kim (arXiv:0907.3970) studies exponential sums and codes associated with symplectic-group parabolic double cosets, using different observables. Abiad and Haemers (arXiv:1412.2945) analyze binary symplectic graphs and graph switching, not Fourier-coordinate frames on the finite symplectic matrix group. These are methodological or object-level neighbors rather than identified equivalent statements. No historical-priority or exhaustive-literature certification is asserted.

## Limitations
The family consists only of the constant and degree-one ambient Walsh characters, not all Fourier characters on the binary matrix space. The Gram spectrum gives sharp Riesz bounds for their span; it does not assert that they span all functions on \(\operatorname{Sp}(d,2)\), nor extend the formula to odd characteristic or to \(d=2\). The Gram entries rely on the chosen standard symplectic basis; arbitrary coordinate changes must transport the frequency family accordingly. A previously unnoticed representation-theoretic formula could imply the result.

## References
1. Y. C. Eldar and H. Bölcskei, *Geometrically Uniform Frames*, arXiv:math/0108096v1 (13 August 2001), especially Theorem 1 and Section 4. https://arxiv.org/abs/math/0108096
2. D. S. Kim, *Infinite Families of Recursive Formulas Generating Power Moments of Kloosterman Sums: Symplectic Case*, arXiv:0907.3970v1 (23 July 2009), especially Theorem 1 and Sections 2–5. https://arxiv.org/abs/0907.3970
3. A. Abiad and W. H. Haemers, *Switched symplectic graphs and their 2-ranks*, arXiv:1412.2945 (initially public 2014), especially Sections 1–4. https://arxiv.org/abs/1412.2945
