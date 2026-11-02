# A double Hasse divisor and sixteen rank-zero fibers in a genus-four trigonal family

## Finding
Let \(k\) be algebraically closed of characteristic \(7\), and let \(C_{u,v}\) be the smooth projective model of
\[
 y^3=x^5+ux^3+vx+1.
\]
Write \(\Delta(u,v)\) for the discriminant in \(x\) of the right-hand side, and restrict to the smooth coefficient domain \(\Delta(u,v)\ne0\). Put \(H(u,v)=u^2+2v\). Every curve has genus \(4\). The Jacobian \(7\)-rank \(f_7\) and \(a\)-number satisfy exactly
\[
(f_7(C_{u,v}),a(C_{u,v}))=
\begin{cases}
(4,0),&H(u,v)\ne0,\\
(0,2),&H(u,v)=0\ \text{and}\ [u=0\ \text{or}\ u^{20}=1],\\
(2,2),&H(u,v)=0\ \text{and}\ u\ne0,\ u^{20}\ne1.
\end{cases}
\]
On the smooth part of \(H=0\), the condition \(u^{20}=1\) automatically excludes \(u^5=1\), as those five parameters are singular. The Hasse invariant, in the natural differential trivialization, has equation \(H^2\Delta\), so its divisor on the smooth coefficient domain is twice the reduced conic \(H=0\). Its rank-zero locus comprises **exactly sixteen distinct marked geometric parameters**, namely \(v=3u^2\) with \(u=0\), \(u^5=-1\), or \(u^{10}=-1\). Their Frobenius orbit degrees over \(\mathbb F_7\) are \(1,1,2,4,4,4\). No intermediate rank one or three occurs.

## Assumptions and scope
The field \(k\) is algebraically closed of characteristic \(7\); \(u,v\in k\) are *marked coefficients*, not geometric isomorphism classes. The polynomial \(x^5+ux^3+vx+1\) is required to be squarefree. The discriminant is
\[
\Delta=3u^5+2u^4v^3+3u^3v-2u^2v^4-2uv^2-3v^5+3\quad\text{in }\mathbb F_7[u,v].
\]
Since \(3\) and \(5\) are coprime and the polynomial has degree \(5\), the normalized curve has genus \((3-1)(5-1)/2=4\) and exactly one point over infinity. In particular, no singular affine model is included in the conclusions.

## Proof
Write \(f(x)=x^5+ux^3+vx+1\). A basis of regular differentials is
\[
\omega_0=dx/y,\quad\omega_1=dx/y^2,\quad
\omega_2=x\,dx/y^2,\quad\omega_3=x^2\,dx/y^2.
\]
The Cartier operator respects the summands spanned by \(\omega_0\) and by \(\omega_1,\omega_2,\omega_3\), because \(7\equiv1\pmod3\). Its coefficient matrix, raised entrywise to the seventh power, has diagonal blocks \([H]\) and
\[
B=\begin{pmatrix}
-u^2-3uv^3-2v & -2uv^2-3 & -2uv+v^4\\
-2u & u^4-2u^2v-v^2 & -2u^2-2v\\
1&0&-3u
\end{pmatrix}.
\]
To derive these blocks without a convention ambiguity, the coefficient in row \(i\), column \(j\) for \(dx/y^2\) is \([x^{7(i+1)-1-j}]f(x)^4\), with \(0\le i,j\le2\). The scalar coefficient for \(dx/y\) is \([x^6]f(x)^2\). All these coefficients are then seventh-rooted to obtain the Cartier matrix itself. Exact polynomial expansion gives
\[
 [x^6]f^2=H,\qquad \det B=H\Delta.
\]
For \(H\ne0\), nonsingularity gives \(\Delta\ne0\), hence the full Cartier matrix is invertible. Therefore the Jacobian is ordinary, so \((f_7,a)=(4,0)\).

On \(H=0\), necessarily \(v=3u^2\), and
\[
 \Delta(u,3u^2)=3(u^5-1)^2.
\]
Thus smooth parameters on the conic are exactly those with \(u^5\ne1\). Substitution gives the three-by-three block
\[
M(u)=\begin{pmatrix}
3u^7&3(u^5-1)&-3u^8+u^3\\
-2u&0&-u^2\\
1&0&-3u
\end{pmatrix}.
\]
It has determinant zero, while the minor on rows \(1,3\) and columns \(1,2\), indexed from one, is \(-3(u^5-1)\), which is nonzero for every smooth member. Thus its rank is exactly \(2\); the scalar block vanishes, giving \(a(C)=4-2=2\).

Let \(\sigma\) denote seventh-power Frobenius on coefficients. A Hasse–Witt matrix for the dual Frobenius operator is \(B^{\mathsf T}\) (respectively \(M^{\mathsf T}\) on the conic), since the original Cartier matrix was specified by its seventh powers. Hence the two-iterate matrix on the three-dimensional block has transpose \(M(u^7)M(u)\), not the reverse-order product. Exact computation in \(\mathbb F_7[u]\) yields
\[
 \gcd\bigl(\text{all nonzero }2\!\times\!2\text{ minors of }M(u^7)M(u)\bigr)
 =u(u^5-1)^9(u^5+1)(u^{10}+1),
\]
normalized to be monic. Set \(S(u)=u(u^5+1)(u^{10}+1)\). For any smooth \(u\) with \(S(u)\ne0\), the two-iterate map has rank \(2\), equal to the one-iterate rank. Its image has stabilized, so its stable rank and the Jacobian \(7\)-rank are \(2\).

For every root of \(S\), the *third* Frobenius iterate vanishes: entrywise polynomial division gives
\[
M(u^{49})M(u^7)M(u)\equiv 0\pmod{S(u)}.
\]
This is a polynomial identity in the quotient ring \(\mathbb F_7[u]/(S)\), not an enumeration of a finite field. It proves stable rank zero simultaneously for all geometric roots of \(S\). The scalar summand is already zero there. There are no other stable-rank possibilities.

The factors \(u\), \(u^5+1\), and \(u^{10}+1\) are pairwise coprime and squarefree over \(\mathbb F_7\). Their degrees are \(1,5,10\), and no zero is singular because a nonzero root has \(u^5=-1\) or \((u^5)^2=-1\), never \(u^5=1\). Thus precisely \(16\) distinct smooth coefficient parameters have rank zero. The irreducible factor degrees are \(1,1,2,4,4,4\), giving the asserted Frobenius orbits. In particular the exceptional set is reduced.

## Verification
Run `python verify_symbolic.py` (SymPy required). It independently reconstructs the coefficient matrices from \(f^2\) and \(f^4\), checks the discriminant factorization, calculates and monic-normalizes the polynomial gcd of every two-by-two minor, and proves the third-iterate congruence by exact quotient-ring arithmetic. Its successful marker is `SYMBOLIC_DIVISOR_AND_STABLE_RANK_OK`. The computation is over the polynomial rings themselves, so it proves the identities uniformly over the algebraic closure.

Run `python verify_point_counts.py` (Python standard library). Its separate elementary extension-field enumerator counts points for four smooth prime-field parameter pairs through extension degree four. It obtains Newton-identity Weil coefficients with \(7\)-adic ranks \(0,0,2,4\), matching the predicted cases. Its successful marker is `INDEPENDENT_POINT_COUNTS_OK`. Finite point counts are corroboration rather than a proof of the infinite-parameter classification.

## Relationship to prior work
The general Cartier–Manin formula for superelliptic curves in Sutherland (2020), particularly Lemma 6, Eq. (8) and Example 7, supplies the coefficient-basis method. Achter and Howe (2017) explain the essential transpose and semilinear-order conventions. Kudo, Harashita and Senda (2019) study supersingular genus-four Howe curves, not the marked cyclic trigonal family considered here. The new assertion is the complete two-parameter Hasse divisor with its multiplicity and the precise sixteen-point stable-rank-zero locus; it is not a claim to the general Cartier algorithm or general existence of genus-four rank-zero curves. A later 2025 article by Sohn studies genus-four superelliptic \(a\)-numbers; its full text could not be inspected, so overlap with the \(a\)-number component remains a priority risk. No geometric isomorphism-class census is asserted.

## Limitations
A zero \(7\)-rank does not alone prove supersingularity or determine the Newton polygon. The result is about marked coefficients on this specific smooth family, not all trigonal curves of genus four, and does not classify geometric isomorphism types. Its mathematical originality assessment relies on accessible primary literature and mathematical-record searches; priority cannot be guaranteed, and one potentially relevant full text remained unavailable.

## References
1. J. D. Achter and E. W. Howe, *Hasse–Witt and Cartier–Manin matrices: A warning and a request*, arXiv:1710.10726 (first public 2017-10-30), https://arxiv.org/abs/1710.10726.
2. A. V. Sutherland, *Counting points on superelliptic curves in average polynomial time*, arXiv:2004.10189 (first public 2020-04-21), https://arxiv.org/abs/2004.10189.
3. M. Kudo, S. Harashita, H. Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic*, arXiv:1903.08095 (first public 2019-03-19), https://arxiv.org/abs/1903.08095.
4. G. Sohn, *The \(a\)-number of superelliptic curves of genus four*, Journal of Applied and Pure Mathematics 7 (2025), 59–66, DOI:10.23091/japm.2025.059; full text not obtained.
