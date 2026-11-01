# Sharp commutator spectrum and balanced coarse-graining for Mercedes-type Parseval frames

## Finding
Let \(k\ge3\) be an integer and let \((e_j)_{j=1}^k\) be a Mercedes-type complex Parseval frame with Gram matrix \(G=I_k-k^{-1}\mathbf1\mathbf1^*\). For a subset \(A\subseteq[k]\), define its binary effect \(E_A=\sum_{j\in A}e_je_j^*\). For two sets \(A,B\), define four Venn counts
\[
x=|A\cap B|,\quad y=|A\setminus B|,\quad z=|B\setminus A|,\quad w=|[k]\setminus(A\cup B)|,
\qquad x+y+z+w=k.
\]
Then the skew-adjoint commutator has rank at most two and its possible nonzero eigenvalues are
\[
\pm i\,d(A,B),\qquad d(A,B)^2=\frac{xyz+xyw+xzw+yzw}{k^3}.
\]
In particular,
\[
\|[E_A,E_B]\|=d(A,B),
\]
and the commutator vanishes if and only if at most two of \(x,y,z,w\) are positive.

Writing \(k=4q+r\) with \(q\in\mathbb Z_{\ge0}\) and \(r\in\{0,1,2,3\}\), the sharp maximum among all ordered pairs of binary coarse-grainings is
\[
C_k=\max_{A,B\subseteq[k]}\|[E_A,E_B]\|
=\left(\frac{4q^3+3rq^2+r(r-1)q+\binom r3}{k^3}\right)^{1/2}.
\]
**Complete equality classification:** an ordered pair \((A,B)\) attains this maximum if and only if the four Venn-cell counts are \(q\) or \(q+1\), with exactly \(r\) of them equal to \(q+1\). Therefore \(C_k\le1/4\), with equality if and only if \(4\mid k\). For example, \(C_3=1/(3\sqrt3)\) and \(C_4=1/4\).

The two associated binary POVMs, \((E_A,I-E_A)\) and \((E_B,I-E_B)\), are **jointly measurable**: their four joint effects are the sums of the same rank-one frame effects over \(A\cap B\), \(A\setminus B\), \(B\setminus A\), and the remaining cell. The theorem therefore quantifies noncommutativity *inside a compatible measurement family*; it makes no claim of incompatibility.

## Assumptions and scope
We work on a complex Hilbert space \(H\) of dimension \(k-1\), and \(k\ge3\) is arbitrary. A Parseval frame has \(\sum_j e_je_j^*=I_H\). The specified Gram matrix is the normalization used for Mercedes-type frames in the motivating literature; multiplying individual frame vectors by phases leaves the effects unchanged. Under the coefficient-analysis isometry, \(H\) is identified with \(\mathbf1^\perp\subseteq\mathbb C^k\), and \(e_j\) is identified with \(P\varepsilon_j\), where
\[
P=I_k-\frac1k\mathbf1\mathbf1^*,\qquad \varepsilon_j\text{ is the standard coordinate vector}.
\]
The effects are positive contractions; the operator norm, eigenvalues and rank refer to their action on \(H\). The theorem concerns binary subset coarse-grainings of one fixed discrete rank-one POVM, not arbitrary jointly measurable effects or arbitrary Parseval frames.

## Proof
**Compression and rank-two reduction.** Under the above identification, writing \(D_A\) for the coordinate projection onto \(A\), we have \(E_A=PD_AP|_{\mathbf1^\perp}\). Since \(D_A D_B=D_BD_A=D_{A\cap B}\), insertion of \(P=I_k-k^{-1}\mathbf1\mathbf1^*\) gives the *exact* identity
\[
[E_A,E_B]=\frac1k(vu^*-uv^*)\big|_{\mathbf1^\perp},
\qquad u=P\mathbf1_A,\quad v=P\mathbf1_B.
\]
Here \(u,v\) are real vectors in \(\mathbf1^\perp\), so the commutator is a real skew-symmetric operator of rank at most two. In the real plane spanned by \(u,v\), its eigenvalues are \(\pm i k^{-1}\sqrt{\|u\|^2\|v\|^2-(u^*v)^2}\); if \(u,v\) are dependent, it vanishes.

**Four-cell determinant.** Put \(a=|A|=x+y\), \(b=|B|=x+z\). Directly,
\[
\|u\|^2=\frac{a(k-a)}k,\qquad
\|v\|^2=\frac{b(k-b)}k,\qquad
u^*v=\frac{kx-ab}{k}.
\]
An expansion, or the covariance determinant of two indicator variables on the uniform \(k\)-point set, gives
\[
\|u\|^2\|v\|^2-(u^*v)^2
=\frac{xyz+xyw+xzw+yzw}{k}.
\]
The claimed norm and eigenvalues follow after dividing by \(k^2\). Since every term in the numerator is nonnegative and every triple of distinct Venn cells contributes its product, this numerator is positive precisely when at least three of the four cell sizes are positive. This proves the commutativity criterion without an implicit genericity assumption.

**Global discrete maximum and rigidity.** Every nonnegative integer four-tuple with sum \(k\) occurs as the Venn counts of some pair \((A,B)\). Define
\[
\mathscr E_3(x,y,z,w)=xyz+xyw+xzw+yzw.
\]
For two selected variables \(a,b\) and the other two \(c,d\), the exact identity
\[
\mathscr E_3=ab(c+d)+(a+b)cd
\]
shows that, if \(a\ge b+2\) and \(c+d>0\), replacing \((a,b)\) by \((a-1,b+1)\) increases \(\mathscr E_3\) by \((a-b-1)(c+d)>0\). For \(k\ge3\), the maximum is positive (put one unit in each of three distinct cells). Consequently no maximizer can have \(c+d=0\), because such a tuple has \(\mathscr E_3=0\). Every maximizing tuple therefore has all pairwise differences at most one. Conversely, pairwise smoothing strictly raises \(\mathscr E_3\) until the four counts differ by at most one, so all and only the balanced tuples maximize it. Substituting \(r\) entries \(q+1\) and \(4-r\) entries \(q\) gives
\[
\mathscr E_3^{\max}=4q^3+3rq^2+r(r-1)q+\binom r3.
\]
Finally, equality in the continuous Maclaurin inequality \(\mathscr E_3\le4(k/4)^3=k^3/16\) requires all four variables to equal \(k/4\), which is an integer precisely when \(4\mid k\). Thus \(C_k\le1/4\), with strict inequality otherwise. The equality classifications follow.

## Verification
The accompanying standalone script `scripts/check_mercedes_commutators.py` uses only standard-library exact rational arithmetic. It constructs the compression \(P D_A P\) and directly multiplies effect matrices for *all* pairs of subsets for \(k=3,4,5\). It checks the exterior-product identity, Frobenius norm, commutativity criterion, and cubic spectral identity \([E_A,E_B]^3=-d(A,B)^2[E_A,E_B]\). It also enumerates all nonnegative four-tuples for each \(3\le k\le21\) and compares the global maximum and every equality tuple with the closed formula. The executed script reported **6,779 exact assertions passed**. Finite enumeration is not used to justify the arbitrary-\(k\) theorem: the preceding proof does that.

## Relationship to prior work
Kużel and Łukasiewicz, *Operators and POVMs generated by Parseval frames*, arXiv:2601.11225v1 (January 16, 2026), introduce Parseval-frame POVMs, establish joint measurability for POVMs built from the same frame (their Proposition 5), and give the Mercedes-type Gram matrix in equation (4.13). Their Theorem 13 instead concerns the spectrum of a *single* frame-generated observable and does not give the operator norm, spectrum, commutativity cases, or optimal partitions for the commutator of *two binary coarse-grainings*. The journal version in *Banach Journal of Mathematical Analysis* 20 (2026), article 49, was checked for the same comparison. The present result supplies an exact all-\(k\) extremal description by reducing the compressed commutator to a rank-two skew exterior product and then optimizing a four-cell elementary symmetric polynomial.

General operator and POVM literature supplies the notions of compatibility, coarse-graining and matrix commutators; those notions alone do not state the four-cell norm or all finite-size extremizers. The distinction between joint measurability and commutation is essential: compatibility here follows immediately from a common four-outcome refinement despite strict positive commutator norm for three or four nonempty cells.

## Limitations
The result concerns one fixed Mercedes-type Parseval frame family and **binary subset sums only**. It does not optimize over arbitrary Parseval frames, nonbinary stochastic postprocessings, unrelated compatible POVMs, or physical implementations. The numerical norm is an operator-theoretic noncommutativity measure and does not establish measurement incompatibility. The equalities are exact within the stated normalization. Publication priority is not independently certified; older compressed-projection or simplex-POVM formulas under different terminology could cover the same invariant.

## References
1. S. Kużel and P. Łukasiewicz, *Operators and POVMs generated by Parseval frames*, arXiv:2601.11225v1, publicly posted January 16, 2026. https://arxiv.org/html/2601.11225v1
2. S. Kużel and P. Łukasiewicz, *Operators and POVMs generated by Parseval frames*, *Banach Journal of Mathematical Analysis* **20** (2026), article 49. https://doi.org/10.1007/s43037-026-00514-0
3. H. Zhu, *Quantum Measurements in the Light of Quantum State Estimation*, *PRX Quantum* **3** (2022), 030306. https://doi.org/10.1103/PRXQuantum.3.030306
