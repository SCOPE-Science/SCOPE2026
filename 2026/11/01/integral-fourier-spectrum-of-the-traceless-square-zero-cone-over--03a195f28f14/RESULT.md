# Integral Fourier spectrum of the traceless square-zero cone over prime-square rings

## Finding
For every odd prime \(p\), let \(R=\mathbb Z/p^2\mathbb Z\), \(G=R^3\), and
\[
C_p=\{(a,b,c)\in G:a^2+bc=0\text{ in }R\}.
\]
This is the parameter space of traceless, square-zero matrices
\(\left(\begin{smallmatrix}a&b\\c&-a\end{smallmatrix}\right)\).
Let \(T_p\) be convolution on \(\ell^2(G)\) with the indicator \(\mathbf1_{C_p}\), without an averaging factor. All its eigenvalues are integers, and its complete spectrum (eigenvalue followed by multiplicity) is
\[
\begin{array}{c|c}
 p^4+p^3-p^2&1\\
 p^2(2p-1)&p(p^2-1)/2\\
 p^2(p-1)&p^4-1\\
 -p^2&p(p-1)^2/2+p^2(p-1)(p^2-1)\\
 0&p^6-p^5
\end{array}.
\]
In particular,
\[
\operatorname{rank}T_p=p^5,\qquad \dim\ker T_p=p^6-p^5.
\]
For a frequency \(M=(u,v,w)\in G\), put \(\Delta(M)=u^2+4vw\). Its Fourier character is in the kernel exactly when \(M\notin pG\) and \(\Delta(M)\not\equiv0\pmod p\). Thus the kernel has an explicit Fourier basis, not just a dimension.

## Assumptions and scope
The prime \(p\) is odd; in particular \(2,4\) are units of \(R\). The Fourier transform is unnormalized:
\[
\widehat{\mathbf1}_{C_p}(M)=\sum_{x\in C_p}\exp(2\pi i\langle M,x\rangle/p^2),
\]
with coordinate pairing \(\langle (u,v,w),(a,b,c)\rangle=ua+vb+wc\). The convolution convention is \((T_p f)(y)=\sum_{x\in C_p}f(y-x)\). Under this convention each additive character is an eigenvector of eigenvalue \(\widehat{\mathbf1}_{C_p}(M)\). No statement is made about the characteristic-two case, arbitrary prime powers beyond the square, or other quadratic forms with degenerate reduction.

## Proof
**Step 1: Exact character-sum identity.** Write \(n=p^2\) and \(e_n(t)=\exp(2\pi it/n)\). Character orthogonality for \(a^2+bc=0\) gives
\[
\widehat{\mathbf1}_{C_p}(M)=\frac1n\sum_{s\bmod n}\sum_{a,b,c\bmod n}e_n\bigl(s(a^2+bc)+ua+vb+wc\bigr).
\]
The term \(s=0\) contributes \(p^4\mathbf1_{\{M=0\}}\). For \(s\in R^\times\), completion of the square and the bilinear sum yield
\[
\sum_a e_n(sa^2+ua)=p\,e_n(-u^2/(4s)),\qquad
\sum_{b,c}e_n(sbc+vb+wc)=p^2e_n(-vw/s).
\]
The quadratic Gauss sum modulo \(p^2\) is \(p\) for every unit multiplier. Summing over units, inversion permutes them, and the contribution after dividing by \(n\) is
\[
p\,c_{p^2}(\Delta(M)),
\]
where the Ramanujan sum satisfies
\[
c_{p^2}(t)=\begin{cases}p(p-1),&p^2\mid t,\\-p,&p\mid t\text{ but }p^2\nmid t,\\0,&p\nmid t.\end{cases}
\]
For \(s=pj\) with \(j\in\mathbb F_p^\times\), summing first over lifts by \(p\) gives zero unless \(M=pM_1\). In that case, each quadratic exponential over \(R^3\) is \(p^3\) times the corresponding sum over \(\mathbb F_p^3\). For a unit \(j\), completing the square over the field gives
\[
\sum_{a,b,c\in\mathbb F_p}e_p\bigl(j(a^2+bc)+\langle M_1,(a,b,c)\rangle\bigr)
=pG_p(j)\,e_p\bigl(-\Delta(M_1)/(4j)\bigr),
\]
where \(G_p(j)=\sum_a e_p(ja^2)\). The elementary quadratic Gauss identity \(G_p(1)^2=\chi_p(-1)p\) and the change of variables \(j\mapsto j^{-1}\) imply
\[
\sum_{j\ne0}G_p(j)e_p\bigl(-\Delta(M_1)/(4j)\bigr)=p\chi_p(\Delta(M_1)),
\]
including \(\Delta(M_1)=0\) by defining \(\chi_p(0)=0\). Consequently the full, exact formula is
\[
\boxed{\widehat{\mathbf1}_{C_p}(M)
=p^4\mathbf1_{\{M=0\}}+p\,c_{p^2}(\Delta(M))
+p^3\mathbf1_{\{M\in pG\}}\chi_p(\Delta(M/p)).}
\]
Here \(M/p\) denotes the uniquely determined coordinate residues modulo \(p\) when \(M\in pG\), so its quadratic character is well defined.

**Step 2: Nonvanishing and multiplicities.** If \(M\notin pG\), the last term vanishes; the first term also vanishes. The Ramanujan sum is nonzero exactly when \(\Delta(M)\equiv0\pmod p\), and then it equals \(-p^2\) or \(p^2(p-1)\). If \(M=pM_1\), the eigenvalue is \(p^2(p-1)+p^3\chi_p(\Delta(M_1))\), except for the extra \(p^4\) when \(M=0\). Each of the three possibilities for \(\chi_p\) is nonzero for every odd prime. This proves the stated Fourier-null criterion.

For the nondegenerate quadratic form \(\Delta\) over \(\mathbb F_p^3\), the zero set has \(p^2\) points; each nonzero square value has \(p^2+p\) preimages and each nonsquare value has \(p^2-p\) preimages. Indeed, for fixed \(u\), solving \(vw=(t-u^2)/4\) yields \(2p-1\) solutions if \(u^2=t\) and \(p-1\) otherwise. In the primitive stratum \(M\notin pG\), there are \(p^2-1\) nonzero isotropic reductions \(\bar M\). For each, the derivative of \(\Delta\) is nonzero, so of its \(p^3\) lifts exactly \(p^2\) satisfy \(\Delta(M)=0\pmod{p^2}\); the remaining \((p-1)p^2\) have valuation exactly one. Combining these with the \(M=pM_1\) stratum gives precisely the five multiplicities in the table. They sum to \(p^6=|G|\), while the nonzero multiplicities sum to \(p^5\).

## Verification
An accompanying standalone Python checker performs exact cyclotomic-integer tests, exhaustively over all \(p^6\) Fourier frequencies for each of \(p=3,5\). It constructs the cone, forms each character-sum polynomial, and verifies the predicted integer using divisibility by \(\Phi_{p^2}(z)=1+z^p+\cdots+z^{(p-1)p}\), without floating-point arithmetic. It checks the exact spectral multiplicities and trace sum. Running \(\texttt{python3 check_cone_fourier.py}\) yields \(\texttt{EXACT_QUADRATIC_CONE_P2_OK}\) for both primes. The all-prime theorem rests on the algebraic derivation above, not on enumeration.

## Relationship to prior work
Character diagonalization of abelian Cayley convolution and evaluations of quadratic Gauss and Ramanujan sums are classical. Liu and Zhou (2012) analyze unitary Cayley graphs of finite commutative rings; Liu and Zhou (2015) analyze Cayley sets given by squares of units. Those sets are not the zero set of a three-variable quadratic form on \((\mathbb Z/p^2\mathbb Z)^3\). Momihara and Xiang (2012) use quadratic forms to build strongly regular Cayley graphs over finite **fields** in even dimension. The present spectrum concerns a nonreduced **ring** and an odd-dimensional null cone, and is not an instance of the inspected graph families. The novelty claim is confined to the complete five-level spectrum, exact Fourier kernel, and rank collapse for this particular natural cone; no general Gauss-sum novelty is asserted.

## Limitations
An equivalent derivation may exist in more general treatments of quadratic Gauss sums over finite local rings or quadratic-space association schemes that were not located in this bounded literature inspection. There has been no independent mathematical audit or verification. The result does not classify higher prime-power rings.

## References
- X. Liu and S. Zhou, *Spectral Properties of Unitary Cayley Graphs of Finite Commutative Rings*, Electronic Journal of Combinatorics 19 (2012), P13, DOI: 10.37236/2390, first online October 25, 2012.
- K. Momihara and Q. Xiang, *Lifting Constructions of Strongly Regular Cayley Graphs*, arXiv:1212.5752, first posted December 23, 2012.
- X. Liu and S. Zhou, *Quadratic unitary Cayley graphs of finite commutative rings*, arXiv:1504.02934, first posted April 12, 2015.
