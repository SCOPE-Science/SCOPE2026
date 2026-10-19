# Jordan-orbit stratification and codimension decay of regular nilpotents in restricted-range semigroups

## Finding
Let \(V\) be an \(n\)-dimensional vector space over \(\mathbb F_q\), and let \(W\le V\) have dimension \(r\ge1\) and codimension \(c=n-r\ge0\). Put \(S(V,W)=\{T\in\operatorname{End}_{\mathbb F_q}(V):T(V)\subseteq W\}\). A map \(T\in S(V,W)\) is *regular* when \(T=TUT\) for some \(U\in S(V,W)\). For a nilpotent \(T\), its Jordan type is the partition of its dimension recording the nilpotent block sizes.

**Theorem.** The regular nilpotents in \(S(V,W)\) form exactly one conjugacy orbit under the group \(\operatorname{GL}(V)_W\) preserving \(W\), for each partition \(\lambda\vdash r\). The corresponding ambient Jordan type is \(\lambda\cup(1^c)\), its rank is \(r-\ell(\lambda)\), and its nilpotency index is \(\lambda_1\). Its cardinality is
\[
N_{\lambda}(q)q^{c(r-\ell(\lambda))},\qquad
N_{\lambda}(q)=\frac{|\operatorname{GL}_r(q)|}{q^{\sum_{j\ge1}(\lambda'_j)^2}\prod_{s\ge1}\prod_{a=1}^{m_s(\lambda)}(1-q^{-a})}.
\]
Here \(\lambda'\) is the conjugate partition, \(m_s(\lambda)\) is the number of parts equal to \(s\), and empty products are one. Consequently the complete regular-nilpotent rank/index enumerator is
\[
H_{r,c,q}(X,Y)=\sum_{\lambda\vdash r}N_{\lambda}(q)q^{c(r-\ell(\lambda))}X^{r-\ell(\lambda)}Y^{\lambda_1}.
\]
The entire nilpotent population of \(S(V,W)\), including nonregular maps, has cardinality \(q^{rc+r^2-r}\). Therefore, with \(r,q\) fixed and \(c\to\infty\), the fraction of nilpotent elements that are regular is
\[
\frac{H_{r,c,q}(1,1)}{q^{rc+r^2-r}}=
\left(\prod_{i=2}^{r}(1-q^{-i})\right)q^{-c}+O_{r,q}(q^{-2c}).
\]
For \(r=1\), this expression equals \(q^{-c}\) exactly. For \(c>0\), the largest nilpotency index among regular nilpotents is \(r\), while the largest index among all nilpotents is \(r+1\).

## Assumptions and scope
The field is any finite field of prime-power order \(q\ge2\). The integer dimensions satisfy \(r\ge1\) and \(c\ge0\). A nilpotency index is the least positive integer \(k\) with \(T^k=0\); thus the zero map has index one. A regular element is von Neumann regular **in the restricted-range semigroup**, not merely in the full endomorphism ring. Counts concern labeled linear endomorphisms of the fixed pair \((V,W)\), not abstract semigroup isomorphism classes. The group \(\operatorname{GL}(V)_W\) acts by conjugation, preserving \(S(V,W)\).

## Proof
Choose \(V=W\oplus C\), with \(\dim C=c\). Each restricted-range endomorphism has a unique block form
\[
T=\begin{pmatrix} B&D\\0&0\end{pmatrix},\qquad B\in M_r(\mathbb F_q),\quad D\in M_{r\times c}(\mathbb F_q).
\]
If \(T=TUT\) for \(U\in S(V,W)\), then \(\operatorname{im} T=\operatorname{im}(TUT)\subseteq T(W)=\operatorname{im}B\). Conversely, if \(\operatorname{im}D\subseteq\operatorname{im}B\), choose a linear generalized inverse \(F\) of \(B\) satisfying \(BFB=B\) and acting as a right inverse of \(B\) on \(\operatorname{im}B\). With \(U=\begin{psmallmatrix}F&0\\0&0\end{psmallmatrix}\) this gives \(TUT=T\). Thus regularity is equivalent to \(\operatorname{im}D\subseteq\operatorname{im}B\).

For a regular \(T\), choose \(E\in M_{r\times c}(\mathbb F_q)\) such that \(D=BE\). The invertible shear \(P=\begin{psmallmatrix}I_r&E\\0&I_c\end{psmallmatrix}\), which stabilizes \(W\), obeys
\[
T=P^{-1}\begin{pmatrix}B&0\\0&0\end{pmatrix}P.
\]
Therefore regular elements inherit, up to parabolic conjugacy, precisely the similarity classes of their \(W\)-restrictions \(B\). Conversely, any two such normal forms with similar \(B\)'s are conjugate by an element preserving \(W\). Since \(T^k=\begin{psmallmatrix}B^k&B^{k-1}D\\0&0\end{psmallmatrix}\) for \(k\ge1\), nilpotency of \(T\) is equivalent to nilpotency of \(B\). A nilpotent \(B\) of Jordan type \(\lambda\vdash r\) consequently gives the claimed ambient Jordan type, rank and index.

For each fixed nilpotent \(B\) of rank \(r-\ell(\lambda)\), the columns of \(D\) may be chosen independently from \(\operatorname{im}B\). This yields exactly \(q^{c(r-\ell(\lambda))}\) regular lifts. The standard nilpotent similarity-class centralizer count is \(q^{\sum_j(\lambda'_j)^2}\prod_{s,a}(1-q^{-a})\), obtained by considering the invertible endomorphisms of the \(\mathbb F_q[t]\)-module with cyclic summands of lengths \(\lambda_i\). Orbit–stabilizer gives \(N_\lambda(q)\) as displayed. Summing over partitions proves \(H_{r,c,q}\).

Every nilpotent \(B\) admits **all** \(q^{rc}\) choices of \(D\), whether regular or not. The classical finite-field nilpotent-matrix identity \(\sum_{\lambda\vdash r}N_\lambda(q)=q^{r^2-r}\) proves the total count. The unique partition yielding the maximum rank \(r-1\) is \((r)\), with \(N_{(r)}(q)=q^{r^2-r}\prod_{i=2}^{r}(1-q^{-i})\); all other partitions have rank at most \(r-2\). This proves the uniform stated asymptotic, including the exact case \(r=1\).

Finally \(B^r=0\) implies \(T^{r+1}=0\), while the regular shear normal form gives index at most \(r\). For \(c\ge1\), take \(B\) as a single nilpotent Jordan block of size \(r\) and choose one column of \(D\) outside \(\operatorname{im}B\) so that \(B^{r-1}D\ne0\). This produces a nonregular nilpotent of index \(r+1\), proving sharpness.

## Verification
The accompanying standalone Python 3 checker enumerates every matrix in \(S(V,W)\) over the prime fields with \((q,r,c)=(2,1,0),(2,1,2),(3,1,2),(2,2,0),(2,2,1),(2,2,2),(3,2,1),(2,3,0),(2,3,1)\). It independently computes nilpotency, matrix ranks and Jordan types from ranks of powers. The resulting complete multiplicity dictionaries agree with the partition formula. In addition, for \((q,r,c)=(2,2,1)\), it independently checks the regularity criterion by exhaustively searching for a witness \(U\) with \(TUT=T\), without using the rank shortcut. The program prints `VERIFY_OK` on success.

For the smallest nontrivial codimension example \((q,r,c)=(2,2,2)\), exactly \(13\) of the \(64\) nilpotent endomorphisms are regular. For \((q,r,c)=(2,3,1)\), the corresponding count is \(211\) of \(512\).

## Relationship to prior work
The regularity criterion \(T(V)=T(W)\) is established in the literature on semigroups of transformations with restricted range. Grau's 2022 preprint (published 2023) develops regular elements, Green's relations, ideals, and extended Green's relations in the more general setting of independence algebras. The closely related 2017 paper of Sommanee and Sangkhanan studies maximal regular subsemigroups and their generating ranks. These structural facts are inputs, not claimed here as new. The conjugacy-orbit classification **of regular nilpotents**, its Jordan-type-dependent multiplicities and the codimension asymptotic are the contributions assessed here. The finite-field nilpotent orbit formula and nilpotent-matrix total are classical inputs, not newly claimed results.

## Limitations
The classification concerns only the regular nilpotent stratum of restricted-range linear endomorphisms; nonregular nilpotents need not have the same Jordan-type correspondence. It does not generalize without further work to arbitrary independence algebras or non-field base rings. Small-field enumerations verify examples but are not proofs for all finite fields; the proof above establishes the infinite families. Prior literature on restricted-range semigroup structure may contain unrecognized equivalent refinements, especially in works for which only abstracts were available.

## References
1. A. Grau, *The semigroup of endomorphisms with restricted range of an independence algebra*, arXiv:2206.12526 (first posted 25 June 2022); *Semigroup Forum* 106 (2023), 128–159, DOI: 10.1007/s00233-022-10324-z. Relevant sections: 1, 3–5.
2. W. Sommanee and K. Sangkhanan, *The regular part of a semigroup of linear transformations with restricted range*, *Journal of the Australian Mathematical Society* 103 (2017), 402–419, DOI: 10.1017/S144678871600080X. Relevant sections: 1, 4, 5.
3. R. P. Sullivan, *Semigroups of linear transformations with restricted range*, *Bulletin of the Australian Mathematical Society* 77 (2008), 441–453, DOI: 10.1017/S0004972708000385.
4. S. Nenthein and Y. Kemprasit, *Regular elements of some semigroups of linear transformations and matrices*, *International Mathematical Forum* 2 (2007), 155–166, DOI: 10.12988/imf.2007.07014.
