# The Cartier rank-two divisor for genus-four dihedral hyperelliptic curves in characteristic seven

## Finding
Let \(k=\overline{\mathbf F}_7\). Define
\[
 C_{s,t}:\quad y^2=x^9+s x^7+(t+2)x^5+s x^3+x,
 \qquad (s,t)\in k^2.
\]
Put
\[
 \Delta(s,t)=(s^2-4t)((t+4)^2-4s^2),\qquad
 P(s,t)=2s^4+2s^2t^2+2s^2t+s^2+4t^2+2t-1.
\]
**Theorem.** If \(\Delta(s,t)\ne0\), then \(C_{s,t}\) is a smooth genus-four hyperelliptic curve and its Jacobian has \(a\)-number
\[
 a(C_{s,t})=\begin{cases}2,&P(s,t)=0,\\0,&P(s,t)\ne0.\end{cases}
\]
Thus its nonordinary parameter locus on this smooth two-dimensional normal-form family is exactly the nonempty hypersurface \(P=0\); \(a=1,3,4\) never occur. Moreover, among \(49\) pairs \((s,t)\in\mathbf F_7^2\), exactly \(31\) produce smooth curves. Of those, exactly the two pairs \((2,5)\) and \((5,5)\) have \(a=2\), and each of these has \(7\)-rank zero; all other \(29\) smooth pairs are ordinary. The pair counts are **not** counts of isomorphism classes.

## Assumptions and scope
All geometric claims are over the algebraic closure \(k\) in characteristic \(7\). The model is the dihedral-symmetry normal form of Ohashi–Kudo, equation (3.7), with their coefficient \(B=t+2\). The \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_7,\operatorname{Jac}(C)[7])\), equivalently the dimension of the kernel of Cartier on regular differentials. The finite parameter census concerns the **specified models** with \(s,t\in\mathbf F_7\), not all isomorphic curves or all arithmetic twists.

For smoothness, write \(f(x)=x g(x^2)\), where
\[
 g(z)=z^4+s z^3+(t+2)z^2+s z+1
     =(z^2+a z+1)(z^2+b z+1),\quad a+b=s,\ ab=t.
\]
The factors are squarefree, with no common root, exactly when \(a\ne b\), \(a^2\ne4\), and \(b^2\ne4\). These conditions are equivalent to \(\Delta(s,t)\ne0\), because
\[
 (a-b)^2=s^2-4t,\qquad (a^2-4)(b^2-4)=(t+4)^2-4s^2.
\]
The factor \(x\) is simple because \(g(0)=1\). Thus \(f\) is squarefree of degree \(9\), and its smooth projective model has genus \(4\).

## Proof
Write \(f(x)^3=\sum_m\gamma_m x^m\), and use the standard basis \(x^{j-1}dx/y\), for \(1\le j\le4\), of regular differentials. In characteristic \(7\), a Cartier–Manin matrix, up to entrywise seventh roots and the usual choice of transpose convention, has entries \(M_{ij}=\gamma_{7i-j}\). Because \(f(x)^3=x^3g(x^2)^3\), only odd-degree coefficients survive. Direct coefficient extraction gives
\[
 M=\begin{pmatrix}
 0&A&0&1\\ B&0&D&0\\0&D&0&B\\1&0&A&0
 \end{pmatrix},
\]
where all coefficients lie in \(k\) and
\[
 A=3s,\quad B=3s(s^2+t^2+6t+10),\quad
 D=3(s^2t+4s^2+t^2+4t+5).
\]
Here all displayed integer coefficients are interpreted in characteristic \(7\).

Reorder the rows as \((1,3,2,4)\) and the columns as \((2,4,1,3)\). This produces the direct sum of blocks
\[
 U=\begin{pmatrix}A&1\\D&B\end{pmatrix},\qquad
 V=\begin{pmatrix}B&D\\1&A\end{pmatrix}.
\]
Each block has a nonzero entry \(1\), and both have determinant \(AB-D\). Expansion in \(\mathbf F_7[s,t]\) gives **the exact identity**
\[
 AB-D=P(s,t).
\]
Consequently, each block has rank \(2\) if \(P\ne0\) and rank \(1\) if \(P=0\). The full matrix has rank \(4\) or \(2\), respectively. Since the seventh-root automorphism preserves matrix rank, the Cartier kernel has dimension \(0\) or \(2\), which proves the universal assertion.

For the finite-field statement, set \(u=s^2\in\{0,1,2,4}\). In \(\mathbf F_7\), the equation \(P(s,t)=0\) becomes
\[
 2u^2+(2t^2+2t+1)u+4t^2+2t-1=0.
\]
Checking \(t\in\mathbf F_7\) yields no solutions for \(u=0,1\), only \(t=4\) for \(u=2\), and \(t\in\{0,5}\) for \(u=4\). The solutions \((u,t)=(2,4)\) and \((4,0)\) satisfy \(\Delta=0\); only \((u,t)=(4,5)\) is smooth, with \(\Delta=3\). It gives exactly \(s=2,5\). Direct exhaustive evaluation of \(\Delta\) for all \(49\) pairs yields \(31\) smooth pairs (and \(18\) nonsmooth pairs).

For \((s,t)=(2,5)\), the matrix is
\[
 \begin{pmatrix}0&6&0&1\\1&0&6&0\\0&6&0&1\\1&0&6&0\end{pmatrix},
\]
and for \((5,5)\) it is
\[
 \begin{pmatrix}0&1&0&1\\6&0&6&0\\0&6&0&6\\1&0&1&0\end{pmatrix}.
\]
Both have square zero over \(\mathbf F_7\). Since Frobenius acts trivially on matrix coefficients in \(\mathbf F_7\), the semilinear iterates of Cartier have zero stable rank: both Jacobians have \(7\)-rank \(0\). At every other smooth pair, Cartier is invertible, hence the Jacobian is ordinary and has \(7\)-rank \(4\). This establishes the stated \(29+2\) census.

## Verification
The accompanying standalone Python script `checks/cartier_rank_check.py` uses only the standard library. It proves the matrix identity and \(AB-D=P\) as polynomial identities over \(\mathbf F_7[s,t]\) via exact coefficient-dictionary arithmetic; independently recomputes \(f^3\), matrix ranks, and smoothness for each of the \(49\) base-field pairs; and checks that the two exceptional matrices square to zero. Run from the extracted package with `python3 checks/cartier_rank_check.py`. Expected terminal lines begin `SYMBOLIC_IDENTITY_OK`, `F7_CENSUS_OK`, and `P_RANK_ZERO_CHECK_OK`. The polynomial identities, not the finite enumeration, justify the assertion for arbitrary algebraically closed \(k\).

## Relationship to prior work
Ohashi and Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group* (2023), supply this dihedral genus-four normal form (their equation (3.7)) and develop searches for **superspecial** curves (Cartier rank \(0\)). Their treatment is not an explicit classification of the characteristic-seven rank-\(2\) locus or of its \(\mathbf F_7\) parameter points. Frei's *The a-number of hyperelliptic curves* (2017) studies general bounds and the near-maximal case \(a=g-1\), not this dihedral two-parameter rank divisor. Kudo–Nakagawa–Takagi (2022) investigate a different order-six automorphism condition and superspeciality; Novoselov (2020) studies point counts for the narrower trinomial family. The proof here supplies an exact rank-stratification equation and finite-field analysis, not an independent theorem on the superspecial census.

## Limitations
The theorem does not assert anything about \(7\)-rank for arbitrary geometric parameters on \(P=0\), except for the two specified \(\mathbf F_7\)-rational pairs. It does not identify the isomorphism classes or twists represented by the \(31\) smooth parameter pairs. No classification of Newton polygons, Ekedahl–Oort types, or isogeny classes is claimed. Published-work comparisons are based on the identified references and relevant sections; exhaustive coverage of every related source cannot be certified by a search.

## References
1. R. Ohashi and M. Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858 (first public 28 December 2023), esp. Sections 2 and 3.1, eq. (3.7). https://arxiv.org/abs/2312.16858
2. S. Frei, *The a-number of hyperelliptic curves*, arXiv:1703.03516 (2017), Sections 2–4. https://arxiv.org/abs/1703.03516
3. M. Kudo, T. Nakagawa, and T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing a cyclic group of order six*, arXiv:2210.14822 (2022). https://arxiv.org/abs/2210.14822
4. S. A. Novoselov, *Counting points on hyperelliptic curves of type \(y^2=x^{2g+1}+a x^{g+1}+b x\)*, Finite Fields and Their Applications 2020, doi:10.1016/j.ffa.2020.101757.
