# Hilbert-point distance profiles recover all summand distortions
## Finding
Let \(X_i\) be finite-dimensional real normed spaces of dimensions \(n_i\), and put
\[
d_i=d_{\mathrm{BM}}(X_i,\ell_2^{n_i}),\qquad
f(p)=d_{\mathrm{BM}}(X_1\oplus_p\cdots\oplus_pX_k,\ell_2^{n_1+\cdots+n_k}).
\]
The complete multiset of component distortions \(\{d_1,\ldots,d_k\}\), including multiplicity, is determined by the values of \(f\) on any one-sided punctured neighborhood of \(p=2\).

For an explicit reconstruction, let \(r>2\), set
\[
p_r=\frac{2r}{r-2},\qquad S_1(r)=f(p_r)^r,
\]
and write the distinct component distances as \(D_1>\cdots>D_s\), with multiplicities \(m_1,\ldots,m_s\). Then
\[
D_j=\lim_{r\to\infty}S_j(r)^{1/r},\qquad
m_j=\lim_{r\to\infty}\frac{S_j(r)}{D_j^r},\qquad
S_{j+1}(r)=S_j(r)-m_jD_j^r.
\]
The recursion stops exactly when the residual is zero.

The local shape at the Hilbert exponent already reveals the multiplicity \(m=m_1\) of the largest component distance \(D=D_1\). As \(h\downarrow0\),
\[
\log\frac{f(2+h)}D=\frac{h\log m}{2(2+h)}+O\!\left(h e^{-c/h}\right),\qquad
\log\frac{f(2-h)}D=\frac{h\log m}{2(2-h)}+O\!\left(h e^{-c/h}\right),
\]
with some \(c>0\) if a smaller component distance exists; if all component distances equal \(D\), the main terms are exact. Hence, for \(m\ge2\),
\[
f'(2-)=-\frac{D\log m}{4},\qquad f'(2+)=\frac{D\log m}{4}.
\]
If \(m=1\), the excess \(f(p)-D\) is flat to every algebraic order and \(f\) extends \(C^\infty\) through \(2\), with every derivative there equal to zero.

## Assumptions and scope
The result concerns finite collections \(X_1,\ldots,X_k\) of finite-dimensional real normed spaces and only the scalar Euclidean distortions \(d_i\). It does not reconstruct the summand spaces themselves, their dimensions, or their mutual Banach--Mazur distances. The reconstruction assumes the exact profile as a mathematical function, not noisy numerical samples.

The result uses the exact \(\ell_p\)-sum distance theorem of Grundbacher and Kobos. Their theorem applies to every \(p\in[1,\infty]\) and states, with
\[
r(p)=\frac{2p}{|p-2|},
\]
that \(f(p)=\|(d_1,\ldots,d_k)\|_{r(p)}\), with \(r(2)=\infty\).

## Proof
For \(r>2\), the choice \(p_r=2r/(r-2)>2\) satisfies \(r(p_r)=r\). Therefore the cited exact distance formula gives the identity
\[
S_1(r)=f(p_r)^r=\sum_{i=1}^k d_i^r=\sum_{j=1}^s m_jD_j^r.
\]
This is a finite exponential sum in the variable \(r\).

Divide by \(D_1^r\). Since \(D_j/D_1<1\) for every \(j>1\),
\[
S_1(r)^{1/r}=D_1\left(m_1+\sum_{j>1}m_j(D_j/D_1)^r\right)^{1/r}\longrightarrow D_1,
\]
and
\[
\frac{S_1(r)}{D_1^r}=m_1+\sum_{j>1}m_j(D_j/D_1)^r\longrightarrow m_1.
\]
Subtracting \(m_1D_1^r\) leaves \(\sum_{j>1}m_jD_j^r\). Repeating the same argument gives the stated recursion and recovers every distinct distance and its multiplicity. Consequently equality of the profile on any interval \((2,2+\varepsilon)\) gives equality of \(S_1(r)\) for all sufficiently large \(r\), hence the same recursive data and the same multiset. The conjugate-exponent symmetry in the cited theorem gives the identical conclusion from a left-hand germ.

For the local regularity, write \(D=D_1\), \(m=m_1\), and, when \(s>1\), let \(q=D_2/D<1\). For \(h>0\),
\[
\frac1{r(2+h)}=\frac{h}{2(2+h)},\qquad
\frac1{r(2-h)}=\frac{h}{2(2-h)}.
\]
Also
\[
\frac{f(2\pm h)}D=\left(m+R_\pm(h)\right)^{1/r(2\pm h)},
\]
where \(0\le R_\pm(h)\le(k-m)q^{r(2\pm h)}\). Since
\[
r(2+h)=\frac4h+2,\qquad r(2-h)=\frac4h-2,
\]
we have \(R_\pm(h)=O(e^{-c/h})\) with \(c=4\log(D/D_2)>0\). Taking logarithms and using \(\log(m+R)=\log m+O(R)\) yields the displayed asymptotics. If \(s=1\), then \(R_\pm=0\) identically.

When \(m\ge2\), division by \(h\) gives the one-sided logarithmic slopes \(\pm(\log m)/4\), and multiplication by \(D\) gives the one-sided derivatives of \(f\). When \(m=1\), the main term vanishes and every derivative of \(h e^{-c/h}\) tends to zero as \(h\downarrow0\); therefore the two branches glue smoothly to the constant value \(D\), with all derivatives at \(2\) equal to zero.

## Verification
A standard-library checker accompanies this note. It verifies exactly, using rational arithmetic, the change of variables \(p_r=2r/(r-2)\), the two formulas for \(1/r(2\pm h)\), and numerically stress-tests the recursive recovery and the predicted one-sided cusp slopes on several multisets. These computations are consistency checks only; the proof above is analytic and does not rely on finite testing.

## Relationship to prior work
Grundbacher and Kobos prove the exact formula
\[
f(p)=\|(d_1,\ldots,d_k)\|_{2p/|p-2|}
\]
and record as Corollary 2.3 that \(f\) is minimized at \(p=2\), is invariant under conjugating \(p\), and is bounded above by its endpoint value. The checked full text does not state an inverse reconstruction of the multiset \(\{d_i\}\), a differentiability classification at \(p=2\), or the cusp coefficient \((\log m)/4\). Searches for formulations involving reconstruction, multiplicity, differentiability, a Hilbert-exponent cusp, and the source's Corollary 2.3 returned no covering statement.

The new point is therefore not a new Banach--Mazur distance formula. It is an inverse and local-regularity consequence of that formula: a scalar distance profile near a single exponent encodes all component Euclidean distortions, and its first local singularity records the multiplicity of the worst component.

## Limitations
The reconstruction is exact-data identifiability; it is not a numerically stable recovery theorem. Recovering lower distortion levels requires subtracting dominant exponential terms and can be ill-conditioned under noise. The result also does not identify the isometry classes or dimensions of the summands. A generic finite-exponential-sum inversion principle may occur elsewhere; the originality claim is limited to this Banach--Mazur profile consequence after the literature and database comparisons described in the review.

## References
1. F. Grundbacher and T. Kobos, *Exact Banach--Mazur distances of certain \(\ell_p\)-sums and cones*, arXiv:2603.18268v1, first public 2026-03-18. Theorem 1.1 and Corollary 2.3.
