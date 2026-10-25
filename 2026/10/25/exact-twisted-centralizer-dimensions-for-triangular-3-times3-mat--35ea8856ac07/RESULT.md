# Exact twisted-centralizer dimensions for triangular \(3\times3\) matrices

## Finding
Let \(q\ge4\) be a prime power, \(K=\mathbb F_q\), and \(\omega\in K\setminus\{0,1,-1\}\). In the six-dimensional algebra \(T_3(K)\) of upper-triangular matrices, define
\[
C_\omega(A)=\{B\in T_3(K):AB=\omega BA\},\qquad
N_d=\#\{A\in T_3(K):\dim_K C_\omega(A)=d\}.
\]
The complete distribution is

| \(d\) | \(N_d\) |
|---:|---:|
| \(0\) | \(q^3(q-1)(q^2-5q+7)\) |
| \(1\) | \(q^2(q-1)(6q^2-13q-2)\) |
| \(2\) | \(q^2(q-1)(7q-1)\) |
| \(3\) | \(q(q-1)(4q-1)\) |
| \(4\) | \(2q(q-1)\) |
| \(5\) | \(q-1\) |
| \(6\) | \(1\) |

Thus the exact number of ordered pairs of triangular matrices satisfying the twisted commutation relation is
\[
\boxed{\#\{(A,B)\in T_3(K)^2:AB=\omega BA\}
=q^3(2q-1)(11q^2-15q+5).}
\]
For the directed \(\omega\)-commuting graph on the eligible *nonzero* matrices, with loops permitted as in Markova's definition, the number of arcs is this expression minus \(2q^6-1\). All these counts are independent of the multiplicative order of \(\omega\), including cases in which \(\omega\) has order three or four.

## Assumptions and scope
The coefficient field is an arbitrary finite field of order \(q\ge4\). The twist is nonzero and neither \(1\) nor \(-1\). Both factors must be upper triangular in one fixed ordered basis; this is **not** a count of all \(3\times3\) matrices. No assumption on characteristic or splitting of polynomials is made. The arc convention permits loops and excludes the zero vertex.

## Proof
Write
\[
A=\begin{pmatrix}a&x&z\\0&b&y\\0&0&c\end{pmatrix},\qquad
B=\begin{pmatrix}u&r&t\\0&v&s\\0&0&w\end{pmatrix}.
\]
The six independent coordinate conditions for \(AB=\omega BA\) are
\[
(1-\omega)au=(1-\omega)bv=(1-\omega)cw=0,
\]
\[
(a-\omega b)r+x(v-\omega u)=0,\qquad
(b-\omega c)s+y(w-\omega v)=0,
\]
\[
(a-\omega c)t+xs-\omega yr+z(w-\omega u)=0.
\]
These equations constitute a linear homogeneous system in the six coordinates of \(B\); its nullity is \(\dim C_\omega(A)\).

Put \(m=q-1\). First, if \(a=b=c=0\), the rank of the remaining three equations is controlled by the vanishing of \(x\) and \(y\), and, when both vanish, by \(z\). This contributes one matrix of nullity six, \(m\) of nullity five, \(2mq\) of nullity four, and \(m^2q\) of nullity three.

Second, if exactly one diagonal coordinate is nonzero, there are three placements. If it is the first or last coordinate, the exceptional condition is respectively \(y=0\) or \(x=0\); if it is the middle coordinate, the exceptional condition is \(bz=xy\). In each placement there are \(mq^2\) matrices of nullity three and \(m^2q^2\) of nullity two. The middle case follows directly by eliminating \(r\) and \(s\), leaving \((z-xy/b)(w-\omega u)=0\) and a free \(t\).

Third, when exactly two diagonal coordinates are nonzero, in each placement there are precisely \(m\) resonant choices of their nonzero values among \(m^2\) choices. The resonance is \(b=\omega c\), \(a=\omega c\), or \(a=\omega b\), according to the zero position. The remaining off-diagonal coordinates are arbitrary. Hence this stratum contributes \(3mq^3\) matrices of nullity two and \(3(m^2-m)q^3\) of nullity one. For the middle-zero case, the potentially additional condition in the last equation is a multiple of \(a-\omega c\), so it vanishes automatically precisely in the resonant case.

Finally, assume all three diagonal entries are nonzero, so \(u=v=w=0\). Let \(E_{12},E_{23},E_{13}\) denote the respective equalities \(a=\omega b\), \(b=\omega c\), \(a=\omega c\). Each equality holds for \(m^2\) ordered nonzero triples; any pair holds for \(m\) triples; all three cannot hold because \(\omega\ne1\). Thus there are \(m^3-3m^2+3m\) triples with no resonance, and \(3(m^2-2m)\) triples with exactly one. A single resonance contributes nullity one, and no resonance contributes nullity zero, regardless of \(x,y,z\).

For the \(m\) triples with \(E_{12}\) and \(E_{23}\), the coefficient \(a-\omega c\) is nonzero; hence \(r,s\) are free and \(t\) is uniquely determined, giving nullity two for all \(q^3\) off-diagonal triples. For the \(m\) triples with \(E_{12}\) and \(E_{13}\), one has \(s=0\) and \(yr=0\): nullity two exactly when \(y=0\), for \(q^2\) off-diagonal triples, and nullity one otherwise. The case \(E_{23}\) and \(E_{13}\) is symmetric, with \(x=0\) instead. Therefore the fully nonzero diagonal stratum contributes
\[
\begin{array}{c|c}
\text{nullity}&\text{number of matrices}\\\hline
0&(m^3-3m^2+3m)q^3\\
1&3(m^2-2m)q^3+2m^2q^2\\
2&mq^3+2mq^2.
\end{array}
\]

Adding the four disjoint diagonal strata gives exactly the seven formulas stated above, and their sum is \(q^6\). For each \(A\), there are \(q^{\dim C_\omega(A)}\) solutions \(B\), so
\[
\sum_{d=0}^6 N_dq^d=q^3(2q-1)(11q^2-15q+5).
\]
Every ordered pair with \(A,B\ne0\) that satisfies the relation is an arc of the standard graph: its nonzero intertwiner implies that the spectra of \(A\) and \(\omega A\) intersect, and similarly for \(B\). Conversely every arc is such a pair. Of the counted pairs, exactly \(2q^6-1\) have at least one zero matrix factor, which proves the arc formula. The resonance counts used only \(\omega\ne0,1\), so no multiplicative-order parameter appears. This completes the proof.

## Verification
Run the included standalone script with `python verify.py`. It enumerates all \(q^6\) triangular matrices and independently row-reduces the defining six-by-six linear system over \(\mathbb F_4\), \(\mathbb F_5\), and \(\mathbb F_7\), testing multiple twists of different multiplicative orders. The completed execution printed `VERIFY_OK`. Specifically, at \(q=4\) it found \(54208\) pairs, at \(q=5\) it found \(230625\), and at \(q=7\) it found \(1957501\). These checks test the formulas but do not replace the uniform proof above.

## Relationship to prior work
Markova's 2026 paper studies the vertex sets, connectivity and diameter of the directed \(\omega\)-commuting graph for upper-triangular matrix algebras, including the distinction between order two and order at least three. The present result supplies the full twisted-centralizer nullity distribution and exact arc count in the first size \(n=3\) where that graph is weakly connected. Huang's quantum-plane enumeration gives global counts of pairs in the *full* matrix algebra; it does not provide the upper-triangular count, whose flag-preserving constraint is not recovered by subtracting a specified conjugacy-invariant collection. Earlier work on twisted-centralizer codes likewise concerns the full matrix space, not its fixed upper-triangular subalgebra.

## Limitations
The theorem fixes matrix size three and excludes twists \(0,1,-1\); no higher-dimensional or excluded-twist formulas are asserted. The self-review has not been independently audited. An unindexed specialized triangular pair-count may exist; bibliographic comparison cannot certify worldwide priority. The finite verification treats only three field orders, whereas the proof treats every permitted finite field.

## References
1. O. V. Markova, *The \(\omega\)-commuting graph of the upper-triangular matrix algebra*, Electronic Journal of Linear Algebra **42** (2026), 314–328, DOI: `10.13001/ela.2026.9879`. Official article page records online publication on 2026-05-10.
2. Y. Huang, *Counting on the variety of modules over the quantum plane*, Algebraic Combinatorics **5** (2022), 583–592, DOI: `10.5802/alco.230`, arXiv:2110.15570.
3. A. Alahmadi, S. P. Glasby, C. E. Praeger, *On the dimension of twisted centralizer codes*, Finite Fields and Their Applications **48** (2017), 37–56, arXiv:1607.05838.
4. A. Alahmadi, S. P. Glasby, C. E. Praeger, P. Solé, B. Yildiz, *Twisted Centralizer Codes*, Linear Algebra and its Applications **524** (2017), 235–249, arXiv:1608.04079.
