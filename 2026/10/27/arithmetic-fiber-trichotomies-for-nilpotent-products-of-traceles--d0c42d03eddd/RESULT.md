# Arithmetic fiber trichotomies for nilpotent products of traceless two-by-two matrices

## Finding
For every prime power \(q\), consider the three-dimensional vector space \(V_q=\{A\in M_2(\mathbb F_q):\operatorname{tr}A=0\}\), sampled uniformly. Its matrix-product nilpotency relation has an exact conditional fiber census, sharply different in odd and even characteristics, but the total number of ordered pairs with nilpotent product is the *same polynomial in the field size*:
\[
\#\{(A,B)\in V_q^2:AB\text{ nilpotent}\}=2q^4+q^3-3q^2+q.
\]
The zero-product count is \(3q^3-q^2-q\); the remaining \(2q(q-1)(q^2-1)\) products are nonzero, necessarily square-zero. Thus
\[
\Pr(AB\text{ nilpotent})=\frac{2q^4+q^3-3q^2+q}{q^6}=2q^{-2}+q^{-3}-3q^{-4}+q^{-5}.
\]
The number of admissible right factors \(B\) varies according to arithmetic type of \(A\), as given below.

## Assumptions and scope
Let \(q\ge 2\) be any prime power and \(K=\mathbb F_q\). All traces, determinants, and products refer to ordinary matrices over \(K\); this is **not** the Lie-bracket product on \(V_q\). For \(A\in V_q\), define \(f(A)=\#\{B\in V_q:AB\text{ is nilpotent}\}\). The matrix \(AB\) need not be traceless before testing nilpotency. A two-by-two matrix is nilpotent exactly when both its trace and determinant vanish, in every characteristic.

If \(q\) is odd, the complete fiber distribution is:

| Type of \(A\) | Number of such \(A\) | \(f(A)\) |
|---|---:|---:|
| Zero | \(1\) | \(q^3\) |
| Nonzero nilpotent | \(q^2-1\) | \(q^2\) |
| Invertible with two distinct eigenvalues in \(K\) | \(q(q^2-1)/2\) | \(2q-1\) |
| Invertible with irreducible quadratic characteristic polynomial | \(q(q-1)^2/2\) | \(1\) |

If \(q\) is even, the complete distribution is:

| Type of \(A\) | Number of such \(A\) | \(f(A)\) |
|---|---:|---:|
| Zero | \(1\) | \(q^3\) |
| Nonzero nilpotent | \(q^2-1\) | \(q^2\) |
| Nonzero scalar | \(q-1\) | \(q^2\) |
| Invertible nonscalar | \((q-1)(q^2-1)\) | \(q\) |

In even characteristic the nonzero scalar matrices lie in \(V_q\), unlike in odd characteristic.

## Proof
**1. The nilpotent cone.** Write a traceless matrix as
\[
A=\begin{pmatrix}a&b\\c&-a\end{pmatrix}.
\]
Its determinant is \(-a^2-bc\), so it is nilpotent exactly when \(a^2+bc=0\). For each nonzero \(b\), each \(a\) determines precisely one \(c\), giving \(q(q-1)\) matrices. For \(b=0\), the equation forces \(a=0\) and leaves \(c\) arbitrary, giving \(q\). Hence the nilpotent cone has exactly \(q^2\) elements. In characteristic two, the same equation and count apply since \(-a=a\).

**2. The event identity.** Because \(\det(AB)=\det(A)\det(B)\),
\[
AB\text{ is nilpotent}\iff \operatorname{tr}(AB)=0\quad\text{and}\quad(\det A=0\text{ or }\det B=0).
\]
The trace-product pairing is nondegenerate on \(V_q\) in odd characteristic but degenerate in characteristic two. In either characteristic, if \(A\) is nonzero and nilpotent, the linear functional \(B\mapsto\operatorname{tr}(AB)\) is nonzero: every such \(A\) is similar to \(E_{12}\), in which coordinates it reads \(B\mapsto B_{21}\). Thus precisely \(q^2\) traceless right factors have zero trace product; if \(A=0\), there are \(q^3\). Writing
\[
H=\#\{(A,B):A\text{ nilpotent},\ \operatorname{tr}(AB)=0\},
\]
we get \(H=q^3+(q^2-1)q^2=q^4+q^3-q^2\).

**3. Intersection of the two cones.** Fix nonzero nilpotent \(A\) and conjugate it to \(E_{12}\). Then \(\operatorname{tr}(AB)=0\) forces \(B_{21}=0\). With trace zero and determinant zero, write
\[
B=\begin{pmatrix}u&v\\0&-u\end{pmatrix},\quad 0=\det B=-u^2,
\]
forcing \(u=0\), while \(v\) is arbitrary. Hence precisely \(q\) nilpotent \(B\) satisfy \(\operatorname{tr}(AB)=0\) for each nonzero nilpotent \(A\), and \(q^2\) do so for \(A=0\). The overlap of the two events counted by \(H\) and its transpose has size
\[
I=q^2+(q^2-1)q=q^3+q^2-q.
\]
Inclusion-exclusion gives \(2H-I=2q^4+q^3-3q^2+q\) for all \(q\).

**4. Zero products versus nonzero nilpotent products.** If \(A=0\), every \(B\in V_q\) annihilates it, contributing \(q^3\). If \(A\ne0\) is nilpotent, conjugation to \(E_{12}\) shows \(AB=0\) exactly for \(B=vE_{12}\), contributing \(q\). Any invertible \(A\) has \(AB=0\) only when \(B=0\). Therefore the zero-product census is
\[
Z=q^3+(q^2-1)q+(q^3-q^2)=3q^3-q^2-q.
\]
Subtracting from \(2H-I\) yields \(2q(q-1)(q^2-1)\) ordered nonzero nilpotent products. Every nonzero nilpotent two-by-two matrix has square zero.

**5. Odd-characteristic conditional fibers.** The first two cases follow from steps 1–2. Suppose \(A\) is invertible. Then \(B\) must be nilpotent and orthogonal to \(A\) under \(\operatorname{tr}(AB)\). If \(A\) is split, it is similar to \(\operatorname{diag}(t,-t)\) with \(t\ne0\). Writing \(B=\left(\begin{smallmatrix}u&v\\w&-u\end{smallmatrix}\right)\), the orthogonality equation forces \(u=0\) and nilpotency becomes \(vw=0\); this has \(2q-1\) solutions. If \(A\) is nonsplit and a nonzero nilpotent \(B\) were orthogonal to it, conjugating \(B\) to \(E_{12}\) would force the lower-left entry of \(A\) to vanish, making the characteristic polynomial of \(A\) split. This is impossible. Thus only \(B=0\) remains, and \(f(A)=1\). For the multiplicities, each nonzero square value \(t^2\) of \(-\det A\) corresponds to one split conjugacy class of size \(q(q+1)\); there are \((q-1)/2\) values. Each nonsquare value corresponds to one nonsplit conjugacy class of size \(q(q-1)\), again with \((q-1)/2\) values. These give the tabulated counts.

**6. Even-characteristic conditional fibers.** Represent \(A=\left(\begin{smallmatrix}a&b\\c&a\end{smallmatrix}\right)\) and \(B=\left(\begin{smallmatrix}u&v\\w&u\end{smallmatrix}\right)\). Then
\[
\operatorname{tr}(AB)=bw+cv,\qquad B\text{ nilpotent}\iff u^2+vw=0.
\]
If \(A=aI\) with \(a\ne0\), orthogonality is automatic and all \(q^2\) nilpotent \(B\) work. If \(A\) is invertible nonscalar, \((b,c)\ne(0,0)\), so the condition \(bw+cv=0\) has exactly \(q\) solutions \((v,w)\). For each, the Frobenius map \(u\mapsto u^2\) is a bijection of \(K\), giving exactly one nilpotent \(B\). Thus \(f(A)=q\). There are \(q-1\) nonzero scalar matrices; subtract these from the total \(q^3-q^2\) invertible traceless matrices to get \((q-1)(q^2-1)\) invertible nonscalars. This completes the census.

## Verification
Run the standalone file `verify.py` using Python 3 with no third-party packages. It enumerates all ordered pairs of traceless two-by-two matrices in \(\mathbb F_q\) for \(q=2,3,4,5,7,9\), including two nonprime extension fields represented through irreducible polynomials. It separately implements matrix multiplication, trace, determinant, direct nilpotence testing, predicted fiber classifications, zero-product counts, and total formula. All six exhaustive checks print `VERIFY_OK`. The proof applies to every prime power; finite checking is supporting evidence only.

## Relationship to prior work
Sarma and Subedi study nilpotent-product probabilities of *whole finite rings*, including triangular matrix rings. The traceless space \(V_q\) is not a unital subring of \(M_2(\mathbb F_q)\), and the ring-wide probability does not supply this trace-conditioned fiber census. Lopatin classifies simultaneous-conjugacy orbits of tuples **whose individual factors are nilpotent**, whereas the present event allows invertible factors and distinguishes their split and nonsplit behavior. Zaid, Sarmin and Khasraw count certain zero products of finite matrices, not nilpotent products under the traceless restriction. Their corresponding definitions and scope are credited; no orbit classification or whole-ring formula is claimed anew.

## Limitations
No claim is made for general matrix dimension, nonzero prescribed product fibers, or factors independently conditioned on different traces. The computations are exhaustive only over the six fields listed. Absence of a discovered equivalent exact conditional census does not establish literature uniqueness; related unindexed quadratic-incidence identities may provide another derivation. No independent mathematical audit has been performed.

## References
1. D. Sarma and T. Subedi, *Nilpotent Product Probability of Finite Rings*, arXiv:2610.07892 (2026), https://arxiv.org/html/2610.07892v1.
2. A. Lopatin, *On m-tuples of nilpotent 2x2 matrices over an arbitrary field*, arXiv:2310.00477 (2023), https://arxiv.org/abs/2310.00477.
3. N. Zaid, N. H. Sarmin and S. M. S. Khasraw, *The Zero Product Probability of Some Finite Ring of Matrices Based on the Order of the Annihilator*, J. Indones. Math. Soc. 31 (2025), https://jims-a.org/index.php/jimsa/article/download/1838/432/9172.
