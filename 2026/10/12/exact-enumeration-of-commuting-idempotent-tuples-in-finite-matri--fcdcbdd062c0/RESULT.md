# Exact enumeration of commuting idempotent tuples in finite matrix algebras
## Finding
For a prime power \(q\), let \(C_{n,m}(q)\) denote the number of ordered \(m\)-tuples \((E_1,\ldots,E_m)\) of pairwise commuting idempotents in \(M_n(\mathbb F_q)\). Then
\[
C_{n,m}(q)=\sum_{\substack{(d_\varepsilon)_{\varepsilon\in\{0,1\}^m}\\ d_\varepsilon\ge0,\ \sum_\varepsilon d_\varepsilon=n}}
\frac{|\operatorname{GL}_n(q)|}{\prod_{\varepsilon\in\{0,1\}^m}|\operatorname{GL}_{d_\varepsilon}(q)|},
\]
where \(|\operatorname{GL}_0(q)|=1\). Thus pairwise commuting idempotent tuples are enumerated by ordered \(2^m\)-part direct-sum decompositions of \(\mathbb F_q^n\).

For \(m=1\), write
\[
I_n(q)=\sum_{r=0}^n\frac{|\operatorname{GL}_n(q)|}{|\operatorname{GL}_r(q)|\,|\operatorname{GL}_{n-r}(q)|}.
\]
If two idempotents are chosen independently and uniformly from the idempotents of \(M_n(\mathbb F_q)\), their commuting probability is
\[
P_n(q)=\frac{C_{n,2}(q)}{I_n(q)^2}.
\]
For fixed \(n\) and \(q\to\infty\) through prime powers,
\[
P_n(q)=\begin{cases}
q^{-n^2/4}\bigl(1+O_n(q^{-1})\bigr),&n\equiv0\pmod 4,\\
q^{-(n^2-1)/4}\bigl(1+O_n(q^{-1})\bigr),&n\equiv1,3\pmod 4,\\
6q^{-(n^2/4+1)}\bigl(1+O_n(q^{-1})\bigr),&n\equiv2\pmod 4.
\end{cases}
\]

## Assumptions and scope
The field is an arbitrary finite field \(\mathbb F_q\); no restriction on characteristic is used. The integers satisfy \(n\ge0\) and \(m\ge1\). Zero-dimensional joint eigenspaces are allowed. The asymptotic statement keeps \(n\) fixed and lets \(q\) tend to infinity through prime powers.

A complete orthogonal family associated with the tuple is obtained from
\[
P_\varepsilon=\prod_{i=1}^m\left(\varepsilon_iE_i+(1-\varepsilon_i)(I-E_i)\right),
\qquad \varepsilon\in\{0,1\}^m.
\]
Some \(P_\varepsilon\) may be zero. The nonzero members are mutually orthogonal and sum to \(I\).

## Proof
Every idempotent \(E\) has minimal polynomial dividing \(t(t-1)\). The two roots are distinct in every characteristic, so every idempotent is diagonalizable over \(\mathbb F_q\). A pairwise commuting family of diagonalizable endomorphisms is simultaneously diagonalizable. For the present family this gives the canonical direct sum
\[
\mathbb F_q^n=\bigoplus_{\varepsilon\in\{0,1\}^m}V_\varepsilon,
\qquad
V_\varepsilon=\bigcap_{i=1}^m\ker(E_i-\varepsilon_iI).
\]
Conversely, from any ordered direct-sum decomposition indexed by \(\{0,1\}^m\), define \(E_i\) to act as the scalar \(\varepsilon_i\) on \(V_\varepsilon\). These are pairwise commuting idempotents, and the two constructions are inverse.

Fix dimensions \(d_\varepsilon=\dim V_\varepsilon\). The group \(\operatorname{GL}_n(q)\) acts transitively on ordered direct-sum decompositions with this dimension profile. The stabilizer of the standard decomposition is exactly \(\prod_\varepsilon\operatorname{GL}_{d_\varepsilon}(q)\). Orbit-stabilizer therefore gives the displayed exact formula for \(C_{n,m}(q)\). Setting \(m=1\) gives the formula for \(I_n(q)\), and setting \(m=2\) gives the numerator of \(P_n(q)\).

For the asymptotic, use
\[
|\operatorname{GL}_d(q)|=q^{d^2}\bigl(1+O_d(q^{-1})\bigr).
\]
For \(I_n(q)\), the largest exponent \(n^2-r^2-(n-r)^2\) occurs at the most balanced two-part profile. Its leading multiplicity is \(1\) for even \(n\) and \(2\) for odd \(n\). For \(C_{n,2}(q)\), the largest exponent \(n^2-\sum_{j=1}^4 d_j^2\) occurs at the most balanced ordered four-part profiles. If \(n=4a+s\) with \(0\le s<4\), there are \(\binom4s\) such profiles, with \(s\) parts equal to \(a+1\) and \(4-s\) parts equal to \(a\). Dividing the leading terms yields the three congruence cases above. In particular, when \(s=2\), the six choices of the two larger parts give the coefficient \(6\).

## Verification
The standalone verifier enumerates all matrices over small prime fields, filters idempotents directly, and counts commuting pairs or triples by matrix multiplication. It checks the formula for pairs at \((n,q)=(1,2),(2,2),(2,3),(2,5),(3,2)\), and for triples at \((n,q)=(2,2),(2,3)\). The observed pair counts are respectively \(4,40,76,184,1012\), and the observed triple counts are \(176,344\). These finite checks support, but do not replace, the general proof.

## Relationship to prior work
Ánh, Birkenmeier, and van Wyk use complete orthogonal idempotents and their Peirce decompositions as a structural description of rings; the first public arXiv version is dated 22 July 2015 and the work lists MSC \(16S50\) first. Ferraz, Polcino Milies, and Taufer count left ideals in \(M_n(\mathbb F_q)\) and the idempotent generators of each left ideal. Dolžan gives exact single-idempotent counts and bounds for finite matrix rings. These sources motivate the decomposition viewpoint but do not state the joint-eigenspace tuple count above.

Elyze, Guterman, Morrison, and Šivic use rank-constrained idempotents to organize components of a higher-distance commuting variety: their idempotent is a common matrix commuting with an arbitrary pair, rather than requiring the two counted matrices themselves to be idempotent. Their full text therefore supplies a close geometric comparison but not the finite-field point count proved here.

The broader Feit–Fine theory counts all ordered commuting matrix pairs. Fulman and Guralnick's full-text reproof states that unrestricted result and separately derives a nilpotent commuting-pair generating function; a full-text search of that paper found no occurrence of “idempotent”. Thus the present result is a restriction to a structurally distinguished locus, with an elementary direct-sum formula and a mod-four probability asymptotic not supplied by the unrestricted count.

## Limitations
The exact formula is only for idempotent tuples; it does not refine the count by conjugacy classes beyond the joint-eigenspace dimension profile, and it does not count arbitrary commuting semisimple tuples with more than two eigenvalues. The asymptotic is for fixed \(n\) as \(q\to\infty\), not for growing \(n\) at fixed field size. The Feit–Fine original 1960 paper was not available as full text in this run; comparison instead used the full-text 2018 reproof and its explicit statement of the Feit–Fine theorem.

## References
1. P. N. Ánh, G. F. Birkenmeier, L. van Wyk, “Idempotents and structures of rings,” arXiv:1507.06290; Linear and Multilinear Algebra 64 (2016), 2002–2029, DOI 10.1080/03081087.2015.1134429.
2. R. A. Ferraz, C. Polcino Milies, E. Taufer, “Left ideals in matrix rings over finite fields,” arXiv:1711.09289.
3. D. Dolžan, “Bounds for the number of idempotents in finite rings,” Communications in Algebra 49 (2021), 4800–4807, DOI 10.1080/00927872.2021.1929277.
4. W. Feit, N. J. Fine, “Pairs of commuting matrices over a finite field,” Duke Mathematical Journal 27 (1960), 91–94, DOI 10.1215/S0012-7094-60-02709-5.
5. J. Fulman, R. Guralnick, “Enumeration of Commuting Pairs in Lie Algebras over Finite Fields,” Annals of Combinatorics 22 (2018), 295–316, DOI 10.1007/s00026-018-0390-4.
