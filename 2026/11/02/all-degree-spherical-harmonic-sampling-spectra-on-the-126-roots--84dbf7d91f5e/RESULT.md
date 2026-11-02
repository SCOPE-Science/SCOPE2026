# All-degree spherical-harmonic sampling spectra on the 126 roots of \(E_7\)

## Finding
Let \(X\subset S^6\) be the 126 normalized roots of the \(E_7\) root system, and let \(\mathcal H_k\) be the degree-\(k\) spherical harmonics in seven real dimensions. Write \(E_k:\mathcal H_k\to\mathbb R^X\) for point evaluation and \(h_k=\dim\mathcal H_k\). The normalized sample Gram matrix \(G_k=h_k^{-1}E_kE_k^{\mathsf T}\), using the orthonormal spherical-harmonic basis and probability surface measure, has the **complete** spectrum below, for every integer \(k\ge0\).

Let \(P_k(t)=C_k^{5/2}(t)/C_k^{5/2}(1)\), \(u_k=P_k(1/2)\), and \(v_k=P_k(0)\). In addition to 63 zero eigenvalues arising from antipodal parity, the potentially nonzero levels are

\[
\begin{array}{c|c|c}
\text{parity of }k&\text{eigenvalue}&\text{multiplicity}\\ \hline
\text{odd}&2(1+16u_k)&7\\
\text{odd}&2(1-2u_k)&56\\ \hline
\text{even}&2(1+32u_k+30v_k)&1\\
\text{even}&2(1+4u_k-5v_k)&27\\
\text{even}&2(1-4u_k+3v_k)&35
\end{array}
\]

A listed level may itself be zero; all 126 eigenvalues are counted. **Every listed level is nonnegative.** The exact rank classification is

\[
\operatorname{rank}E_k=
\begin{cases}
1,7,27,56,62,& k=0,1,2,3,4\text{ respectively},\\
63,&k\ge5.
\end{cases}
\]

Thus each exact degree at least five samples all 63 coordinates of its own antipodal parity, and no exact degree samples the other parity. Moreover the consecutive two-degree evaluation \(E_k\oplus E_{k+1}\), understood as the evaluation of the direct sum of the two harmonic spaces, is surjective onto \(\mathbb R^X\) **if and only if \(k\ge5\)**. In particular degrees five and six are the first consecutive pair allowing interpolation of arbitrary data on all 126 roots; degrees four and five leave exactly one even-direction obstruction.

## Assumptions and scope
The \(E_7\) roots are taken in the hyperplane \(H=\{x\in\mathbb R^8:\sum_{i=1}^8x_i=0\}\). The 126 integer vectors \(w\) are the 56 vectors \(2e_i-2e_j\) for \(i\ne j\) and the 70 vectors with exactly four coordinates \(+1\) and four coordinates \(-1\). Every such \(w\) has squared norm eight, and \(X=\{w/\sqrt8\}\). The evaluation map is real, although the same spectrum and ranks hold after complexification. No graph metric or Gaussian distance-power kernel enters this claim.

The orthonormal basis for \(\mathcal H_k\) uses \(\int_{S^6}f(x)g(x)\,d\sigma(x)\) with \(\sigma\) a probability measure. The addition theorem consequently gives \(G_k(x,y)=P_k(\langle x,y\rangle)\). The dimension \(h_k=\binom{k+6}{6}-\binom{k+4}{6}\), with binomial coefficients of negative top index interpreted as zero, is included only to fix normalization: the eigenvalues above refer to \(G_k\), not to the unnormalized \(E_kE_k^{\mathsf T}\).

## Proof
**1. Exact finite inner-product scheme.** Choose one vector from each antipodal pair, giving 63 representatives \(r_i\in X\). Define two integer \(63\times63\) matrices with zero diagonal by \(B_{ij}=2\langle r_i,r_j\rangle\) and \(A_{ij}=|B_{ij}|\) for \(i\ne j\). All off-diagonal inner products are \(0\) or \(\pm\tfrac12\). Direct counting from the two explicit types of integer roots gives the identities

\[
B^2=14B+32I,\qquad A^2=16I+16J,\qquad A\mathbf1=32\mathbf1.
\]

Here \(J\) is the all-one matrix. These finite identities can be checked without numerical approximation: the supplied standalone checker generates every vector and counts every pair and common neighbor. An independent short route to the signed identity is the tight-frame equation \(\sum_{i=1}^{63}r_ir_i^{\mathsf T}=9I_H\), which makes \(B=2RR^{\mathsf T}-2I\). For the unsigned identity, each of the four root-type pairing cases has exactly 16 common neighbors when the pair is distinct, whether or not it is adjacent; the diagonal count is 32. The checker explicitly enumerates all 1,953 unordered pairs, including these cases, rather than inferring universal validity from sampled instances.

Since \(B=2RR^{\mathsf T}-2I\), \(\operatorname{rank}(B+2I)=7\), so \(B\) has eigenvalues \(16\) with multiplicity 7 and \(-2\) with multiplicity 56. The unsigned matrix \(A\) has constant eigenvalue 32. On the 62-dimensional orthogonal complement of constants, the equation \(A^2=16I\) makes the eigenvalues \(\pm4\). The trace-zero identity \(32+4m_+-4m_-=0\), together with \(m_++m_-=62\), yields multiplicities 27 and 35.

**2. Harmonic Gram diagonalization.** The addition theorem and \(P_k(-t)=(-1)^kP_k(t)\) split \(\mathbb R^X\) into the 63-dimensional functions even and odd under antipodal exchange. The wrong-parity space lies in the kernel. On the right-parity space, the Gram operator is twice the 63-by-63 matrix

\[
I+u_kB\quad(k\text{ odd}),\qquad
(1-v_k)I+(u_k-v_k)A+v_kJ\quad(k\text{ even}).
\]

Inserting the spectra of \(A\) and \(B\) yields precisely the five displayed eigenvalue formulas, with all multiplicities.

**3. The five exceptional ranks.** The normalized Gegenbauer recurrence is

\[
P_0(t)=1,\quad P_1(t)=t,\quad
P_{k+1}(t)=\frac{2k+5}{k+5}tP_k(t)-\frac{k}{k+5}P_{k-1}(t).
\]

For \(k=0,1,2,3,4\), the relevant values \((u_k,v_k)\) are respectively \((1,1)\), \((1/2,0)\), \((1/8,-1/6)\), \((-1/16,0)\), and \((-23/256,1/16)\). Substitution gives ranks \(1,7,27,56,62\), respectively, and no negative eigenvalues.

**4. Strict positivity in every later degree.** The normalized Gegenbauer integral formula is

\[
P_k(t)=\mathbb E\left[(t+i\sqrt{1-t^2}\,Z)^k\right],
\]

where \(Z\in[-1,1]\) has density proportional to \((1-Z^2)^{3/2}\). Therefore for every \(m\ge0\),

\[
|u_k|\le U_m:=\mathbb E\left[(\tfrac14+\tfrac34Z^2)^m\right]\quad(k\ge2m),
\qquad
|v_k|\le V_m:=\mathbb E[|Z|^{2m}]\quad(k\ge2m).
\]

The explicit beta moments \(\mathbb EZ^{2j}=(1/2)_j/(3)_j\) give

\[
U_4=\frac{1437}{32768}<\frac1{16},\qquad
U_6=\frac{304825}{16777216},\qquad
V_6=\frac{33}{4096},\qquad
32U_6+30V_6<1.
\]

For odd \(k\ge9\), the first bound makes both \(1+16u_k\) and \(1-2u_k\) strictly positive. The remaining odd values \(u_5=-19/512\), \(u_7=137/4096\) give strict positivity directly. For even \(k\ge12\), the last inequality shows \(1+32u_k+30v_k>0\); it also implies \(1+4u_k-5v_k>0\) and \(1-4u_k+3v_k>0\). The intervening even degrees \(k=6,8,10\) are covered by the exact rational recurrence; the standalone checker gives each of their three strictly positive levels. Consequently all appropriate parity sectors have full rank 63 from degree five onward.

**5. Consecutive-degree interpolation.** Adjacent degrees have opposite antipodal parity, and their evaluation images are orthogonal. Their combined rank equals the sum of their individual ranks. For \(k=0,1,2,3,4\) these sums are \(8,34,83,118,125\), strictly below 126. For every \(k\ge5\) the sum is \(63+63=126\). This proves the sharp cutoff.

## Verification
The complete finite calculation uses exact integers for the 126 root vectors and the signed/unsigned 63-by-63 matrices, and rational arithmetic for the Gegenbauer recurrence and moment bounds. Run `python3 verify.py`; it regenerates the configuration and checks all pairwise inner products, all 63-by-63 matrix identities, all 64 tight-frame entries, all exact low-degree ranks, the analytic tail-bound inequalities, and the sharp consecutive-degree cutoff. A successful execution ends with `E7_ROOT_HARMONIC_CERTIFICATE_OK`. These computations check identities on one fully specified finite root configuration; the all-degree assertion additionally requires the displayed analytic moment inequalities, which are proved above.

## Relationship to prior work
Delsarte, Goethals and Seidel introduced and studied spherical-code association schemes and Gegenbauer addition kernels; the kernel and harmonic decomposition here are standard. Bussemaker, Cvetković and Seidel analyzed graphs associated with exceptional root systems and their eigenvalue structure; the 63 antipodal root directions and their finite graph relations belong to this established framework. Bannai, Okuda and Tagami, and subsequently Zhu and collaborators, studied designs of a fixed harmonic index, vanishing moments, and lower bounds; these notions concern different questions than the **all-degree evaluation ranks and the smallest consecutive pair with surjective evaluation**. The new point is not the root system, its angle counts, the general addition theorem, or existence of the low-degree design, but the simultaneous exact spectra and rigorous absence of additional rank loss at any high harmonic degree. No claim of priority beyond the bounded comparisons described in the review is made.

## Limitations
The result is restricted to the full 126-root configuration and exact-degree harmonics (or the consecutive two-degree sum). It does not classify arbitrary selected subsets of roots, general quadrature weights, optimally conditioned interpolation, or low-pass spaces. Complete spectral formula and strict tail positivity are established within this scope. The finite root-identity verification is executable, not an independently reviewed formal proof. Earlier literature on exceptional-root schemes may contain equivalent spectral formulations; independent novelty assessment is outstanding.

## References
1. P. Delsarte, J. M. Goethals and J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata **6** (1977), 363–388. Public full text: https://www.math.unipd.it/~alvise/PHD_2024/LEZIONI/SPHERE/PDF/DELSARTE%20Spherical%20codes%20and%20designs.pdf.
2. F. C. Bussemaker, D. M. Cvetković and J. J. Seidel, *Graphs related to exceptional root systems*, Eindhoven memorandum (1976). Public full text: https://pure.tue.nl/ws/portalfiles/portal/4386333/696566.pdf.
3. E. Bannai, T. Okuda and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101, first posted 2013-08-23. https://arxiv.org/abs/1308.5101.
4. Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim and W.-H. Yu, *More on spherical designs of harmonic index t*, arXiv:1507.05373, first posted 2015-07-20. https://arxiv.org/abs/1507.05373.
